"""Load ContractNLI dataset."""
import json
import subprocess
import os
from pathlib import Path
from loguru import logger

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
CNLI_DIR = WORKSPACE / "contract-nli"


def _download_contractnli():
    if (CNLI_DIR / "test.json").exists():
        return True
    CNLI_DIR.mkdir(exist_ok=True)
    # Try direct download
    import requests
    urls = [
        "https://stanfordnlp.github.io/contract-nli/resources/contract-nli.zip",
        "https://raw.githubusercontent.com/stanfordnlp/contract-nli/main/data/test.json",
    ]
    for url in urls:
        try:
            resp = requests.get(url, timeout=30)
            if resp.status_code == 200:
                if url.endswith(".zip"):
                    zip_path = CNLI_DIR / "contractnli.zip"
                    zip_path.write_bytes(resp.content)
                    subprocess.run(["unzip", "-o", str(zip_path), "-d", str(CNLI_DIR)], capture_output=True)
                    return True
                else:
                    (CNLI_DIR / "test.json").write_bytes(resp.content)
                    return True
        except Exception as e:
            logger.warning(f"ContractNLI download failed from {url}: {e}")
    return False


def load_contractnli(split: str = "test", max_contracts: int = 50) -> list[dict]:
    """Load ContractNLI examples."""
    # Try to load from disk
    for split_name in [split, "train", "dev"]:
        data_file = CNLI_DIR / f"{split_name}.json"
        if data_file.exists():
            try:
                return _parse_contractnli_file(data_file, max_contracts)
            except Exception as e:
                logger.warning(f"ContractNLI parse failed: {e}")

    # Try download
    if _download_contractnli():
        for split_name in [split, "train", "dev"]:
            data_file = CNLI_DIR / f"{split_name}.json"
            if data_file.exists():
                try:
                    return _parse_contractnli_file(data_file, max_contracts)
                except Exception:
                    pass

    # Try HuggingFace
    try:
        from datasets import load_dataset
        ds = load_dataset("stanfordnlp/contract_nli", split=split)
        examples = []
        for ex in ds:
            examples.append({
                "id": f"cnli_{len(examples)}",
                "document": str(ex.get("premise", ""))[:3000],
                "question": str(ex.get("hypothesis", "")),
                "answer": str(ex.get("label", "NotMentioned")),
                "benchmark": "contractnli"
            })
            if len(examples) >= max_contracts * 3:
                break
        logger.info(f"Loaded {len(examples)} ContractNLI examples from HuggingFace")
        return examples
    except Exception as e:
        logger.warning(f"ContractNLI HuggingFace load failed: {e}")

    logger.warning("ContractNLI unavailable, using synthetic data")
    return _generate_synthetic_contractnli(max_contracts)


def _parse_contractnli_file(data_file: Path, max_contracts: int) -> list[dict]:
    data = json.loads(data_file.read_text())
    examples = []
    for doc in data.get("documents", [])[:max_contracts]:
        text = doc.get("text", "")[:3000]
        for ann_set in doc.get("annotation_sets", []):
            for hyp_id, ann in ann_set.get("annotations", {}).items():
                examples.append({
                    "id": f"cnli_{doc.get('id', len(examples))}_{hyp_id}",
                    "document": text,
                    "question": hyp_id,
                    "answer": ann.get("choice", "NotMentioned"),
                    "benchmark": "contractnli"
                })
    logger.info(f"Loaded {len(examples)} ContractNLI examples")
    return examples


def _generate_synthetic_contractnli(n: int) -> list[dict]:
    templates = [
        {"document": "The receiving party shall not disclose any Confidential Information to third parties. All confidential data must be stored securely and accessed only by authorized personnel.", "question": "Does the contract prohibit disclosure of confidential information?", "answer": "Entailment"},
        {"document": "The Service Provider shall maintain all customer data within the European Union. Data transfers outside the EU are prohibited without explicit written consent.", "question": "Can data be transferred outside the EU without consent?", "answer": "Contradiction"},
        {"document": "Either party may terminate this agreement with 90 days written notice. Termination does not affect accrued rights or obligations.", "question": "Is this contract perpetual with no termination clause?", "answer": "Contradiction"},
        {"document": "The Contractor shall provide weekly progress reports to the Client. Reports must include completed tasks, upcoming milestones, and any identified risks.", "question": "Are monthly reports required?", "answer": "NotMentioned"},
        {"document": "All intellectual property created during the engagement belongs to the Client. The Contractor waives any moral rights to such creations.", "question": "Does the Client own the IP created during the project?", "answer": "Entailment"},
    ]
    examples = []
    for i in range(n):
        t = templates[i % len(templates)]
        examples.append({
            "id": f"cnli_synth_{i}",
            "document": t["document"],
            "question": t["question"],
            "answer": t["answer"],
            "benchmark": "contractnli"
        })
    logger.info(f"Generated {len(examples)} synthetic ContractNLI examples")
    return examples
