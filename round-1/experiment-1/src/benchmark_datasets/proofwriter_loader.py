"""Load ProofWriter D*(OWA) dataset from HuggingFace."""
from loguru import logger
import re


def load_proofwriter_owa(split: str = "validation", max_examples: int = 200) -> list[dict]:
    """Load ProofWriter OWA examples."""
    try:
        from datasets import load_dataset
        # Try primary source
        try:
            ds = load_dataset("tasksource/proofwriter", split=split)
        except Exception:
            try:
                ds = load_dataset("tasksource/proofwriter", split="train")
            except Exception:
                ds = load_dataset("renma/ProofWriter", split="train")

        examples = []
        for ex in ds:
            answer = ex.get("answer", ex.get("label", ""))
            if str(answer) not in ["True", "False", "Unknown", "true", "false", "unknown"]:
                continue
            context = ex.get("context", ex.get("theory", ""))
            question = ex.get("question", ex.get("hypothesis", ""))
            if not context or not question:
                continue
            examples.append({
                "id": f"pw_{ex.get('id', len(examples))}",
                "document": context,
                "question": question,
                "answer": str(answer).capitalize(),
                "benchmark": "proofwriter_owa"
            })
            if len(examples) >= max_examples:
                break

        logger.info(f"Loaded {len(examples)} ProofWriter OWA examples")
        return examples

    except Exception as e:
        logger.error(f"ProofWriter load failed: {e}")
        return _generate_synthetic_proofwriter(max_examples)


def _generate_synthetic_proofwriter(n: int) -> list[dict]:
    """Synthetic ProofWriter-style examples as fallback."""
    templates = [
        {
            "document": "Anne is kind. Anne is quiet. Bob is young. If someone is kind and quiet, then they are smart. If someone is young, then they are happy.",
            "question": "Is Anne smart?",
            "answer": "True"
        },
        {
            "document": "Charlie is big. Dave is small. All big things are heavy. If something is heavy, it is not light.",
            "question": "Is Charlie heavy?",
            "answer": "True"
        },
        {
            "document": "Eve is cold. Fred is warm. All cold things are blue. All warm things are red. Cold things are not warm.",
            "question": "Is Eve red?",
            "answer": "False"
        },
        {
            "document": "Grace is tall. Harry is short. Tall things are big.",
            "question": "Is Harry big?",
            "answer": "Unknown"
        },
        {
            "document": "Ivy is fast. Jack is slow. Fast things are loud. All loud things are fast.",
            "question": "Is Jack loud?",
            "answer": "Unknown"
        },
    ]
    examples = []
    for i in range(n):
        t = templates[i % len(templates)]
        examples.append({
            "id": f"pw_synth_{i}",
            "document": t["document"],
            "question": t["question"],
            "answer": t["answer"],
            "benchmark": "proofwriter_owa"
        })
    logger.info(f"Generated {len(examples)} synthetic ProofWriter examples")
    return examples
