#!/usr/bin/env python3
"""Build unified neuro-symbolic reasoning dataset in exp_sel_data_out schema format.

Sources:
  - ProofWriter OWA (tasksource/proofwriter): multi-hop logical reasoning, True/False/Unknown
  - ContractNLI (kiddothe2b/contract-nli): legal NLI, Entailment/Contradiction/NotMentioned
  - SARA (SgfdDttt/sara): statutory tax reasoning with Prolog predicates
  - OpenBookQA (allenai/openbookqa): science multi-hop QA
  - CommonsenseQA (tau/commonsense_qa): commonsense reasoning
  - SNLI (stanfordnlp/snli): general NLI baseline
"""

import json
import re
import random
import resource
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

# RAM limit: 8GB (container has 29GB, leave headroom)
resource.setrlimit(resource.RLIMIT_AS, (8 * 1024**3, 8 * 1024**3))

random.seed(42)

WORKSPACE = Path(__file__).parent
DATASETS_DIR = WORKSPACE / "temp" / "datasets"
SARA_DIR = WORKSPACE / "temp" / "sara" / "sara"


def load_json(path: Path) -> list:
    logger.info(f"Loading {path.name} ({path.stat().st_size // 1024}KB)")
    return json.loads(path.read_text())


# ─── ProofWriter OWA ─────────────────────────────────────────────────────────

def build_proofwriter(max_examples: int = 5000) -> dict:
    """ProofWriter OWA: multi-hop logical reasoning with 3-valued labels."""
    path = DATASETS_DIR / "full_tasksource_proofwriter_default_train.json"
    raw = load_json(path)
    logger.info(f"ProofWriter raw: {len(raw)} rows")

    # All rows have OWA ids — filter to True/False/Unknown
    by_label: dict[str, list] = {}
    for r in raw:
        lbl = str(r.get("answer", ""))
        if lbl in ("True", "False", "Unknown"):
            by_label.setdefault(lbl, []).append(r)

    logger.info(f"ProofWriter label distribution: { {k: len(v) for k, v in by_label.items()} }")

    per_label = max_examples // 3
    sampled = []
    for lbl, rows in by_label.items():
        sampled.extend(random.sample(rows, min(per_label, len(rows))))
    random.shuffle(sampled)
    sampled = sampled[:max_examples]

    examples = []
    for i, r in enumerate(sampled):
        theory = str(r.get("theory", ""))
        question = str(r.get("question", ""))
        depth = r.get("QDep", r.get("maxD", 0))
        try:
            depth = int(depth)
        except (TypeError, ValueError):
            depth = 0

        input_text = f"Theory: {theory}\nQuestion: {question}"
        output_text = str(r.get("answer", ""))
        config = str(r.get("config", ""))

        examples.append({
            "input": input_text,
            "output": output_text,
            "metadata_domain": "general",
            "metadata_split": "train",
            "metadata_hop_count": depth,
            "metadata_original_id": str(r.get("id", "")),
            "metadata_config": config,
            "metadata_task_type": "logical_reasoning",
            "metadata_label_type": "three_valued",
        })

    logger.info(f"ProofWriter examples: {len(examples)}")
    return {"dataset": "proofwriter_owa", "examples": examples}


# ─── ContractNLI ─────────────────────────────────────────────────────────────

def build_contractnli() -> dict:
    """ContractNLI: legal NLI over NDA contract clauses."""
    label_map = {0: "NotMentioned", 1: "Entailment", 2: "Contradiction"}

    examples = []
    for split_name, fname in [
        ("train", "full_kiddothe2b_contract-nli_contractnli_a_train.json"),
        ("test", "full_kiddothe2b_contract-nli_contractnli_a_test.json"),
    ]:
        path = DATASETS_DIR / fname
        if not path.exists():
            logger.warning(f"ContractNLI {split_name} not found: {fname}")
            continue
        rows = load_json(path)
        logger.info(f"ContractNLI {split_name}: {len(rows)} rows")

        for i, r in enumerate(rows):
            lbl_int = r.get("label", 0)
            try:
                lbl = label_map.get(int(lbl_int), str(lbl_int))
            except (TypeError, ValueError):
                lbl = str(lbl_int)

            premise = str(r.get("premise", ""))
            hypothesis = str(r.get("hypothesis", ""))
            input_text = f"Contract clause: {premise}\nHypothesis: {hypothesis}"

            examples.append({
                "input": input_text,
                "output": lbl,
                "metadata_domain": "legal",
                "metadata_split": split_name,
                "metadata_hop_count": 1,
                "metadata_original_id": str(r.get("id", f"{split_name}_{i}")),
                "metadata_task_type": "natural_language_inference",
                "metadata_document_type": "NDA_contract",
            })

    logger.info(f"ContractNLI examples: {len(examples)}")
    return {"dataset": "contractnli", "examples": examples}


# ─── SARA ────────────────────────────────────────────────────────────────────

def build_sara() -> dict:
    """SARA: US federal tax statutory reasoning with Prolog KB annotations."""
    cases_dir = SARA_DIR / "cases"
    if not cases_dir.exists():
        logger.error(f"SARA cases directory not found: {cases_dir}")
        return {"dataset": "sara", "examples": []}

    splits_train = set()
    splits_test = set()
    train_file = SARA_DIR / "splits" / "train"
    test_file = SARA_DIR / "splits" / "test"
    if train_file.exists():
        splits_train = set(train_file.read_text().strip().split("\n"))
    if test_file.exists():
        splits_test = set(test_file.read_text().strip().split("\n"))

    case_files = sorted(f for f in cases_dir.glob("*.pl") if not f.name.startswith("._"))
    logger.info(f"SARA: {len(case_files)} case files, {len(splits_train)} train, {len(splits_test)} test")

    # Sample 25 for phase0
    case_names = [f.stem for f in case_files]
    phase0_names = set(random.sample(case_names, min(25, len(case_names))))

    examples = []
    for pl_file in case_files:
        try:
            content = pl_file.read_text(errors="replace")
            text_lines, question_lines, prolog_lines = [], [], []
            in_section = None

            for line in content.split("\n"):
                stripped = line.strip()
                if stripped.startswith("% Text"):
                    in_section = "text"
                elif stripped.startswith("% Question"):
                    in_section = "question"
                elif stripped.startswith("% Facts"):
                    in_section = "prolog"
                elif stripped.startswith("% Test"):
                    in_section = "test"
                elif stripped.startswith("%") and in_section in ("text", "question"):
                    cleaned = stripped.lstrip("%").strip()
                    if cleaned:
                        (text_lines if in_section == "text" else question_lines).append(cleaned)
                elif in_section == "prolog" and not stripped.startswith("%"):
                    if stripped and not stripped.startswith(":-"):
                        prolog_lines.append(stripped)

            doc_text = " ".join(text_lines)
            question_text = " ".join(question_lines) or "Does the taxpayer owe taxes under this statute?"

            stem = pl_file.stem
            gold_label = "yes" if stem.endswith("_pos") else ("no" if stem.endswith("_neg") else "unknown")

            if stem in phase0_names:
                split = "phase0"
            elif stem in splits_test:
                split = "test"
            else:
                split = "train"

            # Encode predicates as JSON string in metadata
            predicates_json = json.dumps(prolog_lines)
            statute = re.search(r"s\d+", stem)

            input_text = f"Case: {doc_text}\nQuestion: {question_text}"
            examples.append({
                "input": input_text,
                "output": gold_label,
                "metadata_domain": "legal",
                "metadata_split": split,
                "metadata_hop_count": 0,
                "metadata_original_id": stem,
                "metadata_gold_predicates": predicates_json,
                "metadata_statute_section": statute.group(0) if statute else "",
                "metadata_task_type": "statutory_reasoning",
            })
        except Exception:
            logger.error(f"Failed to parse SARA case: {pl_file.name}")
            continue

    logger.info(f"SARA examples: {len(examples)}")
    return {"dataset": "sara", "examples": examples}


# ─── OpenBookQA ──────────────────────────────────────────────────────────────

def build_openbookqa() -> dict:
    """OpenBookQA: multi-hop science QA requiring core science facts."""
    path = DATASETS_DIR / "full_allenai_openbookqa_additional_train.json"
    if not path.exists():
        logger.warning(f"OpenBookQA not found: {path}")
        return {"dataset": "openbookqa", "examples": []}

    rows = load_json(path)
    logger.info(f"OpenBookQA: {len(rows)} rows")

    examples = []
    for i, r in enumerate(rows):
        fact1 = str(r.get("fact1", ""))
        question = str(r.get("question_stem", ""))
        choices = r.get("choices", {})
        choice_texts = choices.get("text", [])
        choice_labels = choices.get("label", [])
        answer_key = str(r.get("answerKey", ""))

        gold_text = next(
            (t for l, t in zip(choice_labels, choice_texts) if l == answer_key), ""
        )
        choices_str = " | ".join(f"{l}: {t}" for l, t in zip(choice_labels, choice_texts))

        input_text = f"Core fact: {fact1}\nQuestion: {question}\nChoices: {choices_str}"
        output_text = f"{answer_key}: {gold_text}"

        examples.append({
            "input": input_text,
            "output": output_text,
            "metadata_domain": "science",
            "metadata_split": "train",
            "metadata_hop_count": 2,
            "metadata_original_id": str(r.get("id", str(i))),
            "metadata_task_type": "multi_hop_qa",
            "metadata_core_fact": fact1,
        })

    logger.info(f"OpenBookQA examples: {len(examples)}")
    return {"dataset": "openbookqa", "examples": examples}


# ─── CommonsenseQA ───────────────────────────────────────────────────────────

def build_commonsenseqa() -> dict:
    """CommonsenseQA: commonsense reasoning requiring implicit background knowledge."""
    path = DATASETS_DIR / "full_tau_commonsense_qa_default_validation.json"
    if not path.exists():
        logger.warning(f"CommonsenseQA not found: {path}")
        return {"dataset": "commonsenseqa", "examples": []}

    rows = load_json(path)
    logger.info(f"CommonsenseQA: {len(rows)} rows")

    examples = []
    for i, r in enumerate(rows):
        question = str(r.get("question", ""))
        concept = str(r.get("question_concept", ""))
        choices = r.get("choices", {})
        choice_texts = choices.get("text", [])
        choice_labels = choices.get("label", [])
        answer_key = str(r.get("answerKey", ""))

        gold_text = next(
            (t for l, t in zip(choice_labels, choice_texts) if l == answer_key), ""
        )
        choices_str = " | ".join(f"{l}: {t}" for l, t in zip(choice_labels, choice_texts))

        input_text = f"Concept: {concept}\nQuestion: {question}\nChoices: {choices_str}"
        output_text = f"{answer_key}: {gold_text}"

        examples.append({
            "input": input_text,
            "output": output_text,
            "metadata_domain": "general",
            "metadata_split": "validation",
            "metadata_hop_count": 1,
            "metadata_original_id": str(r.get("id", str(i))),
            "metadata_task_type": "commonsense_reasoning",
            "metadata_concept": concept,
        })

    logger.info(f"CommonsenseQA examples: {len(examples)}")
    return {"dataset": "commonsenseqa", "examples": examples}


# ─── SNLI ────────────────────────────────────────────────────────────────────

def build_snli(max_examples: int = 2000) -> dict:
    """SNLI: general-domain textual entailment baseline."""
    path = DATASETS_DIR / "full_stanfordnlp_snli_plain_text_test.json"
    if not path.exists():
        logger.warning(f"SNLI not found: {path}")
        return {"dataset": "snli", "examples": []}

    rows = load_json(path)
    valid = [r for r in rows if r.get("label", -1) != -1]
    logger.info(f"SNLI valid: {len(valid)} rows")

    label_map = {0: "entailment", 1: "neutral", 2: "contradiction"}
    sampled = random.sample(valid, min(max_examples, len(valid)))

    examples = []
    for i, r in enumerate(sampled):
        lbl = label_map.get(int(r.get("label", 0)), str(r.get("label", "")))
        premise = str(r.get("premise", ""))
        hypothesis = str(r.get("hypothesis", ""))
        input_text = f"Premise: {premise}\nHypothesis: {hypothesis}"

        examples.append({
            "input": input_text,
            "output": lbl,
            "metadata_domain": "general",
            "metadata_split": "test",
            "metadata_hop_count": 1,
            "metadata_original_id": str(i),
            "metadata_task_type": "natural_language_inference",
        })

    logger.info(f"SNLI examples: {len(examples)}")
    return {"dataset": "snli", "examples": examples}


# ─── Main ────────────────────────────────────────────────────────────────────

@logger.catch(reraise=True)
def main():
    logger.info("=== Building exp_sel_data_out dataset ===")
    Path("logs").mkdir(exist_ok=True)

    # Best 4 datasets for neuro-symbolic FOL reasoning evaluation:
    # 1. ProofWriter OWA: multi-hop logical reasoning with 3-valued labels
    # 2. ContractNLI: legal NLI over NDA clauses (document-level reasoning)
    # 3. SARA: statutory tax reasoning with gold Prolog predicates
    # 4. OpenBookQA: science multi-hop QA (core fact + reading comprehension)
    builders = [
        lambda: build_proofwriter(max_examples=5000),
        build_contractnli,
        build_sara,
        build_openbookqa,
    ]

    datasets = []
    total = 0
    for builder in builders:
        ds = builder()
        n = len(ds["examples"])
        logger.info(f"Dataset '{ds['dataset']}': {n} examples")
        datasets.append(ds)
        total += n

    logger.info(f"Total examples: {total}")

    result = {
        "metadata": {
            "description": "Neuro-symbolic reasoning benchmark: ProofWriter OWA, ContractNLI, SARA, OpenBookQA, CommonsenseQA, SNLI",
            "total_examples": total,
            "hypothesis": "FOL translation pipeline for multi-hop reasoning over textual documents",
        },
        "datasets": datasets,
    }

    out_path = WORKSPACE / "full_data_out.json"
    out_path.write_text(json.dumps(result, indent=2))
    size_mb = out_path.stat().st_size // 1024 // 1024
    logger.info(f"Saved to {out_path} ({size_mb}MB)")


if __name__ == "__main__":
    main()
