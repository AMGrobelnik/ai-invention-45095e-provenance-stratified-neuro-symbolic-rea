#!/usr/bin/env python3
"""Build unified dataset from ProofWriter OWA, ContractNLI, SARA, OpenBookQA, SNLI, CommonsenseQA."""

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

# RAM limit: 8GB
resource.setrlimit(resource.RLIMIT_AS, (8 * 1024**3, 8 * 1024**3))

WORKSPACE = Path(__file__).parent
DATASETS_DIR = WORKSPACE / "temp" / "datasets"
SARA_DIR = WORKSPACE / "temp" / "sara" / "sara"

random.seed(42)


def load_json(path: Path) -> list:
    logger.info(f"Loading {path.name} ({path.stat().st_size // 1024}KB)")
    return json.loads(path.read_text())


def process_proofwriter(max_examples: int = 5000) -> list:
    """Load ProofWriter OWA examples with True/False/Unknown labels."""
    path = DATASETS_DIR / "full_tasksource_proofwriter_default_train.json"
    raw = load_json(path)
    logger.info(f"ProofWriter raw rows: {len(raw)}")

    # Filter to OWA examples only (id contains 'OWA' or answer is 'Unknown')
    owa = [r for r in raw if 'OWA' in str(r.get('id', '')) or r.get('answer') == 'Unknown']
    logger.info(f"ProofWriter OWA rows: {len(owa)}")

    # Stratify by label
    by_label = {}
    for r in owa:
        lbl = r.get('answer', 'Unknown')
        by_label.setdefault(lbl, []).append(r)

    logger.info(f"Label distribution: { {k: len(v) for k, v in by_label.items()} }")

    # Sample evenly across labels, up to max_examples
    per_label = max_examples // max(len(by_label), 1)
    sampled = []
    for lbl, rows in by_label.items():
        sample = random.sample(rows, min(per_label, len(rows)))
        sampled.extend(sample)

    random.shuffle(sampled)
    sampled = sampled[:max_examples]

    out = []
    for i, r in enumerate(sampled):
        # Map depth from config or maxD
        config = r.get('config', '')
        depth = r.get('QDep', r.get('maxD', 0))
        try:
            depth = int(depth)
        except (TypeError, ValueError):
            depth = 0

        out.append({
            "id": f"proofwriter_owa_{i:05d}",
            "dataset": "proofwriter_owa",
            "domain": "general",
            "document_text": str(r.get('theory', '')),
            "question": str(r.get('question', '')),
            "gold_label": str(r.get('answer', '')),
            "gold_predicates": [],
            "hop_count": depth,
            "evidence_spans": [],
            "split": "train",
            "metadata": {
                "source_dataset": "tasksource/proofwriter",
                "original_id": str(r.get('id', '')),
                "config": config,
            }
        })

    logger.info(f"ProofWriter OWA processed: {len(out)} examples")
    return out


def process_contractnli() -> list:
    """Load ContractNLI examples (NLI for legal contracts)."""
    # Label mapping: 0=NotMentioned, 1=Entailment, 2=Contradiction
    label_map = {0: "NotMentioned", 1: "Entailment", 2: "Contradiction"}

    out = []
    for split_name, fname in [("train", "full_kiddothe2b_contract-nli_contractnli_a_train.json"),
                               ("test", "full_kiddothe2b_contract-nli_contractnli_a_test.json")]:
        path = DATASETS_DIR / fname
        if not path.exists():
            logger.warning(f"ContractNLI {split_name} not found: {path}")
            continue
        raw = load_json(path)
        logger.info(f"ContractNLI {split_name}: {len(raw)} rows")

        for i, r in enumerate(raw):
            lbl_int = r.get('label', 0)
            lbl = label_map.get(int(lbl_int), str(lbl_int))
            premise = str(r.get('premise', ''))
            hypothesis = str(r.get('hypothesis', ''))

            out.append({
                "id": f"contractnli_{split_name}_{i:05d}",
                "dataset": "contractnli",
                "domain": "legal",
                "document_text": premise,
                "question": hypothesis,
                "gold_label": lbl,
                "gold_predicates": [],
                "hop_count": None,
                "evidence_spans": [],
                "split": split_name,
                "metadata": {
                    "source_dataset": "kiddothe2b/contract-nli",
                    "original_id": str(r.get('id', f"{split_name}_{i}")),
                }
            })

    logger.info(f"ContractNLI processed: {len(out)} examples")
    return out


def process_sara() -> list:
    """Parse SARA .pl case files into examples."""
    cases_dir = SARA_DIR / "cases"
    splits_train = set((SARA_DIR / "splits" / "train").read_text().strip().split('\n'))
    splits_test = set((SARA_DIR / "splits" / "test").read_text().strip().split('\n'))

    logger.info(f"SARA train cases: {len(splits_train)}, test cases: {len(splits_test)}")

    out = []
    case_files = sorted(cases_dir.glob("*.pl"))
    logger.info(f"SARA total .pl files: {len(case_files)}")

    # Sample 25 for phase0
    case_names = [f.stem for f in case_files]
    phase0_names = set(random.sample(case_names, min(25, len(case_names))))

    for pl_file in case_files:
        try:
            content = pl_file.read_text(errors='replace')
            lines = content.split('\n')

            # Parse text section
            text_lines = []
            question_lines = []
            prolog_lines = []
            in_section = None

            for line in lines:
                if line.strip().startswith('% Text'):
                    in_section = 'text'
                elif line.strip().startswith('% Question'):
                    in_section = 'question'
                elif line.strip().startswith('% Facts'):
                    in_section = 'prolog'
                elif line.strip().startswith('% Test'):
                    in_section = 'test'
                elif line.strip().startswith('%') and in_section in ('text', 'question'):
                    cleaned = line.strip().lstrip('%').strip()
                    if cleaned:
                        if in_section == 'text':
                            text_lines.append(cleaned)
                        elif in_section == 'question':
                            question_lines.append(cleaned)
                elif in_section == 'prolog' and not line.strip().startswith('%'):
                    if line.strip() and not line.strip().startswith(':-'):
                        prolog_lines.append(line.strip())

            document_text = ' '.join(text_lines)
            question_text = ' '.join(question_lines)

            # Determine label from filename: _pos = yes (entailed), _neg = no (not entailed)
            stem = pl_file.stem
            if stem.endswith('_pos'):
                gold_label = 'yes'
            elif stem.endswith('_neg'):
                gold_label = 'no'
            else:
                gold_label = 'unknown'

            # Determine split
            case_name = stem
            if case_name in splits_test:
                split = 'test'
            elif case_name in splits_train:
                split = 'train'
            else:
                split = 'train'

            if case_name in phase0_names:
                split = 'phase0'

            out.append({
                "id": f"sara_{stem}",
                "dataset": "sara",
                "domain": "legal",
                "document_text": document_text,
                "question": question_text or "Does the taxpayer owe taxes under this statute section?",
                "gold_label": gold_label,
                "gold_predicates": prolog_lines,
                "hop_count": None,
                "evidence_spans": [],
                "split": split,
                "metadata": {
                    "source_dataset": "SgfdDttt/sara",
                    "original_id": stem,
                    "statute_section": re.search(r's\d+', stem).group(0) if re.search(r's\d+', stem) else "",
                }
            })
        except Exception:
            logger.error(f"Failed parsing SARA case: {pl_file.name}")
            continue

    logger.info(f"SARA processed: {len(out)} examples")
    return out


def process_openbookqa() -> list:
    """Load OpenBookQA with science knowledge + multi-hop reasoning."""
    path = DATASETS_DIR / "full_allenai_openbookqa_additional_train.json"
    if not path.exists():
        logger.warning(f"OpenBookQA not found: {path}")
        return []
    raw = load_json(path)
    logger.info(f"OpenBookQA raw: {len(raw)} rows")

    out = []
    for i, r in enumerate(raw):
        # Construct document from core_concept and fact1
        fact1 = str(r.get('fact1', ''))
        question = str(r.get('question_stem', ''))
        choices = r.get('choices', {})
        choice_texts = choices.get('text', [])
        choice_labels = choices.get('label', [])
        answer_key = str(r.get('answerKey', ''))

        # Find correct answer text
        gold_text = ''
        for label, text in zip(choice_labels, choice_texts):
            if label == answer_key:
                gold_text = text
                break

        choices_str = ' | '.join(f"{l}: {t}" for l, t in zip(choice_labels, choice_texts))

        out.append({
            "id": f"openbookqa_{i:05d}",
            "dataset": "openbookqa",
            "domain": "science",
            "document_text": fact1,
            "question": f"{question} Choices: {choices_str}",
            "gold_label": f"{answer_key}: {gold_text}",
            "gold_predicates": [fact1] if fact1 else [],
            "hop_count": 2,  # requires combining background fact with question
            "evidence_spans": [],
            "split": "train",
            "metadata": {
                "source_dataset": "allenai/openbookqa",
                "original_id": str(r.get('id', str(i))),
                "answer_key": answer_key,
            }
        })

    logger.info(f"OpenBookQA processed: {len(out)} examples")
    return out


def process_snli(max_examples: int = 2000) -> list:
    """Load SNLI as NLI baseline (general domain)."""
    path = DATASETS_DIR / "full_stanfordnlp_snli_plain_text_test.json"
    if not path.exists():
        logger.warning(f"SNLI not found: {path}")
        return []
    raw = load_json(path)
    # Filter out -1 labels (no gold label)
    valid = [r for r in raw if r.get('label', -1) != -1]
    logger.info(f"SNLI valid rows: {len(valid)}")

    label_map = {0: "entailment", 1: "neutral", 2: "contradiction"}
    sampled = random.sample(valid, min(max_examples, len(valid)))

    out = []
    for i, r in enumerate(sampled):
        lbl = label_map.get(int(r.get('label', 0)), str(r.get('label')))
        out.append({
            "id": f"snli_{i:05d}",
            "dataset": "snli",
            "domain": "general",
            "document_text": str(r.get('premise', '')),
            "question": str(r.get('hypothesis', '')),
            "gold_label": lbl,
            "gold_predicates": [],
            "hop_count": 1,
            "evidence_spans": [],
            "split": "test",
            "metadata": {
                "source_dataset": "stanfordnlp/snli",
                "original_id": str(i),
            }
        })

    logger.info(f"SNLI processed: {len(out)} examples")
    return out


def process_commonsenseqa() -> list:
    """Load CommonsenseQA for commonsense reasoning evaluation."""
    path = DATASETS_DIR / "full_tau_commonsense_qa_default_validation.json"
    if not path.exists():
        logger.warning(f"CommonsenseQA not found: {path}")
        return []
    raw = load_json(path)
    logger.info(f"CommonsenseQA raw: {len(raw)} rows")

    out = []
    for i, r in enumerate(raw):
        choices = r.get('choices', {})
        choice_texts = choices.get('text', [])
        choice_labels = choices.get('label', [])
        answer_key = str(r.get('answerKey', ''))
        concept = str(r.get('question_concept', ''))

        gold_text = ''
        for label, text in zip(choice_labels, choice_texts):
            if label == answer_key:
                gold_text = text
                break

        choices_str = ' | '.join(f"{l}: {t}" for l, t in zip(choice_labels, choice_texts))

        out.append({
            "id": f"commonsenseqa_{i:05d}",
            "dataset": "commonsenseqa",
            "domain": "general",
            "document_text": f"Concept: {concept}",
            "question": f"{r.get('question', '')} Choices: {choices_str}",
            "gold_label": f"{answer_key}: {gold_text}",
            "gold_predicates": [],
            "hop_count": 1,
            "evidence_spans": [],
            "split": "validation",
            "metadata": {
                "source_dataset": "tau/commonsense_qa",
                "original_id": str(r.get('id', str(i))),
                "concept": concept,
            }
        })

    logger.info(f"CommonsenseQA processed: {len(out)} examples")
    return out


@logger.catch(reraise=True)
def main():
    logger.info("=== Building unified dataset ===")
    Path("logs").mkdir(exist_ok=True)

    all_examples = []

    # 1. ProofWriter OWA (primary benchmark)
    pw = process_proofwriter(max_examples=5000)
    all_examples.extend(pw)

    # 2. ContractNLI (legal NLI)
    cnli = process_contractnli()
    all_examples.extend(cnli)

    # 3. SARA (statutory reasoning)
    sara = process_sara()
    all_examples.extend(sara)

    # 4. OpenBookQA (science reasoning)
    obqa = process_openbookqa()
    all_examples.extend(obqa)

    # 5. SNLI (general NLI baseline)
    snli = process_snli(max_examples=2000)
    all_examples.extend(snli)

    # 6. CommonsenseQA
    csqa = process_commonsenseqa()
    all_examples.extend(csqa)

    logger.info(f"Total examples: {len(all_examples)}")

    # Summary by dataset
    by_ds = {}
    for ex in all_examples:
        ds = ex['dataset']
        by_ds[ds] = by_ds.get(ds, 0) + 1
    for ds, count in sorted(by_ds.items()):
        logger.info(f"  {ds}: {count}")

    # Save full
    out_path = WORKSPACE / "data_out.json"
    out_path.write_text(json.dumps(all_examples, indent=2))
    logger.info(f"Saved {len(all_examples)} examples to {out_path}")
    logger.info(f"File size: {out_path.stat().st_size // 1024 // 1024}MB")


if __name__ == "__main__":
    main()
