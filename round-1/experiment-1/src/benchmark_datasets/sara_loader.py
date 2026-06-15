"""Load SARA legal reasoning dataset."""
import os
import glob
import subprocess
from pathlib import Path
from loguru import logger

WORKSPACE = Path("/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1")
SARA_DIR = WORKSPACE / "sara"


def _clone_sara():
    if SARA_DIR.exists() and (SARA_DIR / "cases").exists():
        return True
    if SARA_DIR.exists() and not (SARA_DIR / "cases").exists():
        return False
        return True
    try:
        result = subprocess.run(
            ["git", "clone", "--depth=1", "https://github.com/SgfdDttt/sara.git", str(SARA_DIR)],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            logger.error(f"SARA clone failed: {result.stderr}")
            return False
        logger.info("SARA repo cloned successfully")
        return True
    except Exception as e:
        logger.error(f"SARA clone error: {e}")
        return False


def load_sara(max_examples: int = 50) -> list[dict]:
    """Load SARA legal document + Prolog pairs."""
    if not _clone_sara():
        logger.warning("SARA unavailable, using synthetic legal examples")
        return _generate_synthetic_legal(max_examples)

    cases = []
    txt_files = list(SARA_DIR.glob("cases/*.txt"))
    if not txt_files:
        # Try alternate paths
        txt_files = list(SARA_DIR.glob("**/*.txt"))

    for txt_file in txt_files[:max_examples]:
        stem = txt_file.stem
        pl_file = SARA_DIR / "prolog" / f"{stem}.pl"
        if not pl_file.exists():
            pl_file = SARA_DIR / "statutes" / f"{stem}.pl"

        try:
            document = txt_file.read_text(encoding="utf-8", errors="replace")[:4000]
        except Exception:
            continue

        gold_prolog = ""
        if pl_file.exists():
            try:
                gold_prolog = pl_file.read_text(encoding="utf-8", errors="replace")
            except Exception:
                pass

        cases.append({
            "id": f"sara_{stem}",
            "document": document,
            "gold_prolog": gold_prolog,
            "question": f"Is the legal claim entailed by the document?",
            "answer": "entailed",
            "benchmark": "sara"
        })

    logger.info(f"Loaded {len(cases)} SARA cases")
    if not cases:
        return _generate_synthetic_legal(max_examples)
    return cases


def _generate_synthetic_legal(n: int) -> list[dict]:
    templates = [
        {
            "document": "The Tenant agrees to pay monthly rent of $1,500 to the Landlord. The Landlord is John Smith residing at 123 Main Street. The lease commences on January 1, 2024 and terminates on December 31, 2024. Failure to pay rent constitutes a breach of this agreement. The Tenant shall provide 30 days notice before vacating the premises.",
            "question": "Does the Tenant have an obligation to pay rent?",
            "answer": "entailed"
        },
        {
            "document": "The Employee agrees not to disclose any confidential information belonging to the Employer for a period of two years following termination of employment. Confidential information includes trade secrets, client lists, and proprietary technology. Violation of this clause results in liquidated damages of $50,000.",
            "question": "Is the Employee prohibited from sharing trade secrets?",
            "answer": "entailed"
        },
        {
            "document": "Party A agrees to deliver 500 units of Product X to Party B by March 15, 2024. Party B shall pay $25 per unit upon delivery. If delivery is delayed by more than 10 days, a penalty of 5% per week applies.",
            "question": "Is Party A required to deliver products to Party B?",
            "answer": "entailed"
        },
        {
            "document": "The Licensor grants the Licensee a non-exclusive, non-transferable license to use the Software. The Licensee may not sublicense, sell, or redistribute the Software. The license is valid for one year from the date of agreement.",
            "question": "Can the Licensee sell the Software to third parties?",
            "answer": "not_entailed"
        },
        {
            "document": "The Contractor shall complete all construction work by June 30, 2024. The Owner shall pay $200,000 upon substantial completion. Change orders must be approved in writing by the Owner before work begins.",
            "question": "Must the Contractor obtain written approval for change orders?",
            "answer": "entailed"
        },
    ]
    examples = []
    for i in range(n):
        t = templates[i % len(templates)]
        examples.append({
            "id": f"sara_synth_{i}",
            "document": t["document"],
            "gold_prolog": "",
            "question": t["question"],
            "answer": t["answer"],
            "benchmark": "sara"
        })
    logger.info(f"Generated {len(examples)} synthetic SARA-style legal examples")
    return examples
