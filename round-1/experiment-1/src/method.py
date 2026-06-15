#!/usr/bin/env python3
"""
Provenance-Stratified Neuro-Symbolic Pipeline
L0-L3 Tier-Ordered SLD with weakest-link provenance propagation.
Evaluated on ProofWriter OWA, CLUTRR, SARA, and ContractNLI.
Parallel execution via ThreadPoolExecutor.
"""
import sys
import os
import json
import time
import re
import resource
import gc
import threading
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

from loguru import logger

# --- Logging setup ---
LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)
logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# --- Resource limits (cgroup-aware) ---
def _container_ram_gb() -> float:
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError):
            pass
    import psutil
    return psutil.virtual_memory().total / 1e9

TOTAL_RAM_GB = _container_ram_gb()
RAM_BUDGET = int(min(TOTAL_RAM_GB * 0.7, 20) * 1024**3)
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))
logger.info(f"RAM budget: {RAM_BUDGET/1e9:.1f} GB (container: {TOTAL_RAM_GB:.1f} GB)")

# --- Imports ---
from pipeline.l0_extractor import extract_l0
from pipeline.l1_prolog import PrologKB
from pipeline import l2_ontology
from pipeline.l3_abduction import abduce_l3
from pipeline.meta_interpreter import MetaInterpreter
from pipeline.trace import build_jsonld
from baselines.symba_baseline import symba_prove
from baselines.cot_baseline import cot_answer
from benchmark_datasets.proofwriter_loader import load_proofwriter_owa
from benchmark_datasets.clutrr_loader import load_clutrr
from benchmark_datasets.sara_loader import load_sara
from benchmark_datasets.contractnli_loader import load_contractnli
from metrics.hallucination import compute_hallucination_rate, compute_hallucination_rate_baseline
from metrics.ece import compute_ece
from metrics.tier_distribution import compute_tier_distribution
from pipeline.or_client import get_total_cost

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
COST_LIMIT = 9.0
NUM_WORKERS = 4  # ThreadPoolExecutor workers

# Thread-safe cost lock
_cost_lock = threading.Lock()

# L0 cache (thread-safe via lock)
L0_CACHE_FILE = WORKSPACE / "l0_cache.json"
_l0_cache: dict[str, list] = {}
_cache_lock = threading.Lock()


def load_l0_cache():
    global _l0_cache
    if L0_CACHE_FILE.exists():
        try:
            _l0_cache = json.loads(L0_CACHE_FILE.read_text())
            logger.info(f"Loaded L0 cache with {len(_l0_cache)} entries")
        except Exception:
            _l0_cache = {}


def save_l0_cache():
    with _cache_lock:
        try:
            L0_CACHE_FILE.write_text(json.dumps(_l0_cache))
        except Exception as e:
            logger.warning(f"L0 cache save failed: {e}")


def cached_extract_l0(doc: str, domain: str, doc_id: str) -> list[dict]:
    with _cache_lock:
        if doc_id in _l0_cache:
            return _l0_cache[doc_id]
    facts = extract_l0(doc, domain, use_few_shot=False)
    with _cache_lock:
        _l0_cache[doc_id] = facts
    return facts


def check_budget():
    cost = get_total_cost()
    if cost >= COST_LIMIT:
        raise RuntimeError(f"Budget exceeded: ${cost:.2f}")


def parse_query_proofwriter(ex: dict) -> tuple[str, list[str]]:
    question = ex.get("question", "")
    m = re.match(r"Is\s+(\w+)\s+(\w+)\??", question, re.I)
    if m:
        return m.group(2).lower(), [m.group(1).lower()]
    words = re.findall(r'[a-z]+', question.lower())
    if len(words) >= 2:
        return words[-1], [words[0]]
    return "holds", ["entity"]


def parse_query_clutrr(ex: dict) -> tuple[str, list[str]]:
    entities = ex.get("entities", ["person1", "person2"])
    e1 = re.sub(r'[^a-z0-9_]', '_', str(entities[0]).lower().strip())
    e2 = re.sub(r'[^a-z0-9_]', '_', str(entities[1]).lower().strip())
    return "related_to", [e1, e2]


def parse_query_sara(ex: dict) -> tuple[str, list[str]]:
    return "entailed", ["claim"]


def parse_query_contractnli(ex: dict) -> tuple[str, list[str]]:
    hyp = ex.get("question", "clause")
    hyp_clean = re.sub(r'[^a-z0-9_]', '_', hyp.lower())[:30].strip("_")
    if not hyp_clean or not re.match(r'^[a-z]', hyp_clean):
        hyp_clean = "clause_holds"
    return "entailed", [hyp_clean]


def node_to_answer(node: dict, benchmark: str) -> str:
    tier = node.get("tier", "unknown")
    conf = node.get("confidence", 0.0)
    if benchmark == "proofwriter_owa":
        if tier == "unknown" or conf < 0.4:
            return "Unknown"
        return "True" if conf >= 0.5 else "False"
    elif benchmark == "clutrr":
        return "proved" if tier != "unknown" and conf >= 0.5 else "unknown"
    elif benchmark == "sara":
        return "entailed" if tier != "unknown" and conf >= 0.5 else "not_entailed"
    elif benchmark == "contractnli":
        if tier == "unknown" or conf < 0.4:
            return "NotMentioned"
        return "Entailment" if conf >= 0.5 else "Contradiction"
    return "unknown"


def symba_to_answer(result: dict, benchmark: str) -> str:
    proved = result.get("proved", False)
    if benchmark == "proofwriter_owa":
        return "True" if proved else "False"
    elif benchmark == "clutrr":
        return "proved" if proved else "unknown"
    elif benchmark == "sara":
        return "entailed" if proved else "not_entailed"
    elif benchmark == "contractnli":
        return "Entailment" if proved else "NotMentioned"
    return str(proved)


def cot_to_answer(raw: str, benchmark: str) -> str:
    raw_l = raw.lower().strip()
    if benchmark == "proofwriter_owa":
        return "True" if "true" in raw_l else ("False" if "false" in raw_l else "Unknown")
    elif benchmark == "clutrr":
        return "proved" if ("true" in raw_l or "yes" in raw_l) else "unknown"
    elif benchmark == "sara":
        return "entailed" if ("true" in raw_l or "yes" in raw_l or "entail" in raw_l) else "not_entailed"
    elif benchmark == "contractnli":
        if "entailment" in raw_l or ("true" in raw_l and "not" not in raw_l):
            return "Entailment"
        elif "contradiction" in raw_l or "false" in raw_l:
            return "Contradiction"
        return "NotMentioned"
    return raw


def gold_to_normalized(gold: str, benchmark: str) -> str:
    g = str(gold).strip()
    if benchmark == "proofwriter_owa":
        return g.capitalize()
    elif benchmark == "clutrr":
        return g.lower().replace(" ", "_")
    elif benchmark == "sara":
        return g.lower().replace(" ", "_")
    elif benchmark == "contractnli":
        mapping = {"entailment": "Entailment", "contradiction": "Contradiction",
                   "notmentioned": "NotMentioned", "not_mentioned": "NotMentioned"}
        return mapping.get(g.lower().replace(" ", "").replace("_", ""), g)
    return g


def _add_proofwriter_rules(kb: PrologKB, context: str):
    if_then = re.findall(r'[Ii]f\s+(?:something|a\s+\w+|someone)\s+is\s+(\w+).*?then\s+(?:it|they|he|she)\s+(?:is|are)\s+(\w+)', context)
    for ante, cons in if_then:
        a, c = ante.lower(), cons.lower()
        if re.match(r'^[a-z][a-z0-9_]*$', a) and re.match(r'^[a-z][a-z0-9_]*$', c):
            kb.load_rules([f"{c}(X) :- {a}(X)"])
    all_x = re.findall(r'[Aa]ll\s+(\w+)\s+(?:things\s+)?(?:are|is)\s+(\w+)', context)
    for ante, cons in all_x:
        a, c = ante.lower().rstrip('s'), cons.lower().rstrip('s')
        if re.match(r'^[a-z][a-z0-9_]*$', a) and re.match(r'^[a-z][a-z0-9_]*$', c):
            kb.load_rules([f"{c}(X) :- {a}(X)"])


def process_example(ex: dict, benchmark: str, lkif_onto, l3_K: int = 1) -> dict | None:
    """Process one example: L0 extraction, stratified pipeline, and both baselines in parallel."""
    try:
        check_budget()
    except RuntimeError as e:
        logger.warning(f"Budget: {e}")
        return None

    doc_id = ex.get("id", f"ex_{benchmark}_{id(ex)}")
    document = ex.get("document", "")
    question = ex.get("question", "")
    t0 = time.time()

    try:
        domain = l2_ontology.classify_domain(document)

        # Parse query goal
        if benchmark == "proofwriter_owa":
            goal_pred, goal_args = parse_query_proofwriter(ex)
        elif benchmark == "clutrr":
            goal_pred, goal_args = parse_query_clutrr(ex)
        elif benchmark == "sara":
            goal_pred, goal_args = parse_query_sara(ex)
        else:
            goal_pred, goal_args = parse_query_contractnli(ex)

        q_str = question or f"Does {goal_pred}({', '.join(goal_args)}) hold?"

        # Run L0 extraction, SymBa, and CoT in parallel threads
        with ThreadPoolExecutor(max_workers=3) as inner_pool:
            l0_future = inner_pool.submit(cached_extract_l0, document, domain, doc_id)
            symba_future = inner_pool.submit(symba_prove, goal_pred, goal_args, document)
            cot_future = inner_pool.submit(cot_answer, document, q_str)

            l0_facts = l0_future.result()
            symba_result = symba_future.result()
            cot_raw = cot_future.result()

        # Build KB and run stratified pipeline (sequential, needs L0 facts first)
        kb = PrologKB()
        kb.load_l0_facts(l0_facts)

        if benchmark == "clutrr" or domain == "narrative":
            kb.load_rules([
                "ancestor(X, Y) :- father(X, Y)",
                "ancestor(X, Y) :- mother(X, Y)",
                "ancestor(X, Y) :- father(X, Z), ancestor(Z, Y)",
                "ancestor(X, Y) :- mother(X, Z), ancestor(Z, Y)",
                "related_to(X, Y) :- father(X, Y)",
                "related_to(X, Y) :- mother(X, Y)",
                "related_to(X, Y) :- brother(X, Y)",
                "related_to(X, Y) :- sister(X, Y)",
                "related_to(X, Y) :- grandfather(X, Y)",
                "related_to(X, Y) :- grandmother(X, Y)",
                "related_to(X, Y) :- uncle(X, Y)",
                "related_to(X, Y) :- aunt(X, Y)",
            ])
        elif benchmark == "proofwriter_owa":
            _add_proofwriter_rules(kb, document)

        interp = MetaInterpreter(kb, domain, document, lkif_onto, l3_K=l3_K)
        result_node = interp.prove(goal_pred, goal_args)
        trace = build_jsonld(interp.get_trace(), doc_id)

        # Normalize answers
        gold_norm = gold_to_normalized(ex.get("answer", ""), benchmark)
        strat_ans = node_to_answer(result_node, benchmark)
        symba_ans = symba_to_answer(symba_result, benchmark)
        cot_ans = cot_to_answer(cot_raw, benchmark)

        result = {
            "id": doc_id,
            "benchmark": benchmark,
            "gold": gold_norm,
            "gold_raw": str(ex.get("answer", "")),
            "stratified": strat_ans,
            "symba": symba_ans,
            "cot": cot_ans,
            "tier_used": result_node.get("tier", "unknown"),
            "confidence": result_node.get("confidence", 0.0),
            "l0_facts_count": len(l0_facts),
            "domain": domain,
            "document_text": document[:500],
            "proof_tree": trace,
            "symba_raw": symba_result,
            "processing_time": time.time() - t0,
            "cost_so_far": get_total_cost(),
        }
        logger.info(f"[{benchmark}] {doc_id}: tier={strat_ans} symba={symba_ans} cot={cot_ans} gold={gold_norm} t={result['processing_time']:.0f}s")
        del kb, interp
        gc.collect()
        return result

    except Exception:
        logger.error(f"Failed processing {doc_id}")
        return None


def run_phase0_calibration(sara_examples: list[dict]) -> dict:
    """Quick Phase 0: run L0 extraction on 5 examples, report stats."""
    logger.info("=== PHASE 0: L0 Extraction Calibration ===")
    sample = sara_examples[:5]
    results = []
    for ex in sample:
        doc_id = ex["id"]
        try:
            facts = cached_extract_l0(ex["document"], "legal", doc_id)
            results.append({"id": doc_id, "l0_extracted": len(facts)})
            logger.debug(f"  {doc_id}: {len(facts)} facts")
        except Exception:
            logger.error(f"  Phase 0 failed for {doc_id}")
            results.append({"id": doc_id, "l0_extracted": 0})

    avg_extracted = sum(r["l0_extracted"] for r in results) / max(1, len(results))
    logger.info(f"Phase 0: avg {avg_extracted:.1f} facts/doc (n={len(results)})")
    return {
        "avg_facts_extracted": avg_extracted,
        "gate_passed": avg_extracted >= 2,
        "n_evaluated": len(results),
        "per_case": results,
        "avg_precision": None,  # No gold annotations available
        "avg_recall": None,
    }


def _mean(vals) -> float:
    lst = list(vals)
    return sum(lst) / len(lst) if lst else 0.0


def process_benchmark_parallel(
    benchmark: str, examples: list[dict], lkif_onto, l3_K: int, max_n: int
) -> list[dict]:
    """Process up to max_n examples from a benchmark using ThreadPoolExecutor."""
    subset = examples[:max_n]
    logger.info(f"=== {benchmark}: {len(subset)} examples (parallel={NUM_WORKERS}) ===")
    results = []
    with ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        futures = {
            pool.submit(process_example, ex, benchmark, lkif_onto, l3_K): ex
            for ex in subset
        }
        for fut in as_completed(futures):
            if get_total_cost() >= COST_LIMIT:
                logger.warning("Budget reached, cancelling remaining")
                break
            r = fut.result()
            if r:
                results.append(r)
    save_l0_cache()
    return results


@logger.catch(reraise=True)
def main():
    logger.info("=== Provenance-Stratified Neuro-Symbolic Pipeline (Parallel) ===")
    load_l0_cache()

    logger.info("Loading LKIF ontology...")
    lkif_onto = l2_ontology.load_lkif()

    logger.info("Loading datasets...")
    sara_examples = load_sara(max_examples=50)
    proofwriter_examples = load_proofwriter_owa(max_examples=200)
    clutrr_examples = load_clutrr(max_examples=200)
    contractnli_examples = load_contractnli(max_contracts=50)

    logger.info(f"SARA={len(sara_examples)}, PW={len(proofwriter_examples)}, "
                f"CLUTRR={len(clutrr_examples)}, CNI={len(contractnli_examples)}")

    # Phase 0 calibration
    phase0 = run_phase0_calibration(sara_examples)
    save_l0_cache()
    logger.info(f"Phase 0 done. gate_passed={phase0['gate_passed']}")

    # Mini run: 50 total examples
    mini_configs = [
        ("sara", sara_examples, 5, 3),
        ("proofwriter_owa", proofwriter_examples, 20, 1),
        ("clutrr", clutrr_examples, 20, 1),
        ("contractnli", contractnli_examples, 5, 1),
    ]

    all_results: list[dict] = []
    mini_start = time.time()
    for bm_name, examples, mini_n, l3_K in mini_configs:
        bm_results = process_benchmark_parallel(bm_name, examples, lkif_onto, l3_K, mini_n)
        all_results.extend(bm_results)
        logger.info(f"{bm_name} mini done: {len(bm_results)}/{mini_n}, cost=${get_total_cost():.3f}")

    mini_time = time.time() - mini_start
    mini_cost = get_total_cost()
    logger.info(f"Mini run: {len(all_results)} examples in {mini_time:.0f}s, cost=${mini_cost:.3f}")

    # Scale up if budget and time allow
    remaining_budget = COST_LIMIT - mini_cost
    cost_per_ex = mini_cost / max(1, len(all_results))
    logger.info(f"Cost/example: ${cost_per_ex:.4f}")

    scale50_configs = [
        ("sara", sara_examples, 25, 3),
        ("proofwriter_owa", proofwriter_examples, 100, 1),
        ("clutrr", clutrr_examples, 100, 1),
        ("contractnli", contractnli_examples, 25, 1),
    ]
    estimated_50 = cost_per_ex * (sum(n for _, _, n, _ in scale50_configs) - len(all_results))

    if estimated_50 < remaining_budget * 0.7 and mini_time < 3600:
        logger.info("=== SCALING TO 50% ===")
        processed_ids = {r["id"] for r in all_results}
        for bm_name, examples, n50, l3_K in scale50_configs:
            remaining = [ex for ex in examples[:n50] if ex.get("id", "") not in processed_ids]
            if not remaining or get_total_cost() >= COST_LIMIT * 0.75:
                continue
            bm_results = process_benchmark_parallel(bm_name, remaining, lkif_onto, l3_K, len(remaining))
            all_results.extend(bm_results)
            logger.info(f"{bm_name} 50% done: {len(bm_results)} more, total={len(all_results)}, cost=${get_total_cost():.3f}")

        # Try 100% if budget allows
        scale100_configs = [
            ("sara", sara_examples, 50, 3),
            ("proofwriter_owa", proofwriter_examples, 200, 1),
            ("clutrr", clutrr_examples, 200, 1),
            ("contractnli", contractnli_examples, 50, 1),
        ]
        processed_ids = {r["id"] for r in all_results}
        remaining_budget2 = COST_LIMIT - get_total_cost()
        estimated_100 = cost_per_ex * (sum(n for _, _, n, _ in scale100_configs) - len(all_results))
        if estimated_100 < remaining_budget2 * 0.7:
            logger.info("=== SCALING TO 100% ===")
            for bm_name, examples, n100, l3_K in scale100_configs:
                remaining = [ex for ex in examples[:n100] if ex.get("id", "") not in processed_ids]
                if not remaining or get_total_cost() >= COST_LIMIT * 0.95:
                    continue
                bm_results = process_benchmark_parallel(bm_name, remaining, lkif_onto, l3_K, len(remaining))
                all_results.extend(bm_results)
                logger.info(f"{bm_name} 100% done: total={len(all_results)}, cost=${get_total_cost():.3f}")

    logger.info(f"Total examples processed: {len(all_results)}")

    # Compute aggregate metrics
    aggregates = {}
    for bm in ["sara", "proofwriter_owa", "clutrr", "contractnli"]:
        bm_results = [r for r in all_results if r["benchmark"] == bm]
        if not bm_results:
            aggregates[bm] = {"n_examples": 0}
            continue

        all_docs = [r.get("document_text", "") for r in bm_results]
        halluc_strat = compute_hallucination_rate(
            [[{"tier": n.get("tier", ""), "predicate": n.get("predicate", ""),
               "args": n.get("args", []), "source_span": n.get("source_span", "")}
              for n in r["proof_tree"]["nodes"]] for r in bm_results],
            all_docs
        )
        symba_raw_list = [r.get("symba_raw", {}) for r in bm_results]
        halluc_symba = compute_hallucination_rate_baseline(symba_raw_list, all_docs)
        tier_dist = compute_tier_distribution(bm_results)

        aggregates[bm] = {
            "n_examples": len(bm_results),
            "accuracy_stratified": _mean(1 if r["gold"] == r["stratified"] else 0 for r in bm_results),
            "accuracy_symba": _mean(1 if r["gold"] == r["symba"] else 0 for r in bm_results),
            "accuracy_cot": _mean(1 if r["gold"] == r["cot"] else 0 for r in bm_results),
            "hallucination_rate_stratified": halluc_strat,
            "hallucination_rate_symba": halluc_symba,
            "tier_distribution": tier_dist,
            "avg_l0_facts": _mean(r["l0_facts_count"] for r in bm_results),
            "avg_confidence": _mean(r["confidence"] for r in bm_results),
            "l0_l1_l2_fraction": tier_dist.get("l0_l1_l2_fraction", 0.0),
        }
        logger.info(f"  {bm}: strat={aggregates[bm]['accuracy_stratified']:.3f} "
                    f"symba={aggregates[bm]['accuracy_symba']:.3f} cot={aggregates[bm]['accuracy_cot']:.3f} "
                    f"n={len(bm_results)}")

    sara_l3 = [r for r in all_results if r["benchmark"] == "sara" and r.get("tier_used") == "l3"]
    if sara_l3:
        aggregates["ece_sara_l3"] = compute_ece(
            [r["confidence"] for r in sara_l3],
            [1 if r["gold"] in ("entailed", "True") else 0 for r in sara_l3]
        )

    if all_results:
        aggregates["overall"] = {
            "n_total": len(all_results),
            "accuracy_stratified": _mean(1 if r["gold"] == r["stratified"] else 0 for r in all_results),
            "accuracy_symba": _mean(1 if r["gold"] == r["symba"] else 0 for r in all_results),
            "accuracy_cot": _mean(1 if r["gold"] == r["cot"] else 0 for r in all_results),
        }

    # Build exp_gen_sol_out format output
    datasets_out = []
    for bm in ["sara", "proofwriter_owa", "clutrr", "contractnli"]:
        bm_results = [r for r in all_results if r["benchmark"] == bm]
        if not bm_results:
            continue
        examples = []
        for r in bm_results:
            examples.append({
                "input": f"[{bm}] {r['id']}",
                "output": r["gold"],
                "predict_stratified": r["stratified"],
                "predict_symba": r["symba"],
                "predict_cot": r["cot"],
                "metadata_tier_used": r["tier_used"],
                "metadata_confidence": str(round(r.get("confidence", 0.0), 4)),
                "metadata_l0_facts": str(r.get("l0_facts_count", 0)),
                "metadata_domain": r.get("domain", "general"),
                "metadata_processing_time": str(round(r.get("processing_time", 0), 2)),
            })
        datasets_out.append({"dataset": bm, "examples": examples})

    output = {
        "metadata": {
            "method_name": "Provenance-Stratified Neuro-Symbolic Pipeline",
            "description": "4-tier neuro-symbolic pipeline: L0 LLM extraction, L1 SWI-Prolog SLD, L2 LKIF/ConceptNet, L3 self-consistency abduction",
            "model": "meta-llama/llama-3.1-70b-instruct",
            "baselines": ["SymBa_flat_LLM", "CoT_LLM"],
            "total_examples": len(all_results),
            "total_cost_usd": get_total_cost(),
            "aggregate_metrics": aggregates,
            "phase0_extraction_calibration": phase0,
        },
        "datasets": datasets_out,
    }

    out_path = WORKSPACE / "method_out.json"
    out_path.write_text(json.dumps(output, indent=2))
    logger.info(f"Saved method_out.json ({out_path.stat().st_size/1024:.0f} KB), total_cost=${get_total_cost():.3f}")
    logger.info("Done.")


if __name__ == "__main__":
    main()
