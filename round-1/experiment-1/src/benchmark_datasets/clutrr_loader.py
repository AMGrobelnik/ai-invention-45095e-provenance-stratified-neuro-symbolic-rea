"""Load CLUTRR kinship reasoning dataset from HuggingFace."""
from loguru import logger


def load_clutrr(split: str = "test", max_examples: int = 200) -> list[dict]:
    """Load CLUTRR kinship reasoning examples."""
    try:
        from datasets import load_dataset
        # Try multiple configs
        for config in ["v1", "gen_train234_test2", None]:
            try:
                if config:
                    ds = load_dataset("CLUTRR/v1", config, split=split)
                else:
                    ds = load_dataset("CLUTRR/v1", split=split)
                break
            except Exception:
                continue
        else:
            raise ValueError("All CLUTRR configs failed")

        examples = []
        for ex in ds:
            # CLUTRR fields vary by version
            story = ex.get("story", ex.get("text", ex.get("context", "")))
            query = ex.get("query", ex.get("query_text", ""))
            target = ex.get("target_text", ex.get("answer", ex.get("relation", "")))
            entities = ex.get("query", ["entity1", "entity2"])
            if isinstance(entities, list) and len(entities) >= 2:
                e1, e2 = entities[0], entities[1]
            else:
                e1, e2 = "person1", "person2"

            if not story or not target:
                continue

            question = f"What is the relationship between {e1} and {e2}?"
            examples.append({
                "id": f"clutrr_{len(examples)}",
                "document": story,
                "question": question,
                "entities": [str(e1), str(e2)],
                "answer": str(target).lower().replace(" ", "_"),
                "benchmark": "clutrr"
            })
            if len(examples) >= max_examples:
                break

        logger.info(f"Loaded {len(examples)} CLUTRR examples")
        return examples

    except Exception as e:
        logger.error(f"CLUTRR load failed: {e}")
        return _generate_synthetic_clutrr(max_examples)


def _generate_synthetic_clutrr(n: int) -> list[dict]:
    """Synthetic kinship examples as fallback."""
    templates = [
        {"story": "Alice is the mother of Bob. Bob is the father of Carol.", "e1": "alice", "e2": "carol", "answer": "grandmother"},
        {"story": "David is the father of Eve. Eve is the sister of Frank.", "e1": "david", "e2": "frank", "answer": "father"},
        {"story": "Grace is the mother of Henry. Henry is the husband of Ivy.", "e1": "grace", "e2": "ivy", "answer": "mother_in_law"},
        {"story": "Jack is the brother of Kate. Kate is the mother of Leo.", "e1": "jack", "e2": "leo", "answer": "uncle"},
        {"story": "Mary is the daughter of Nick. Nick is the son of Oliver.", "e1": "oliver", "e2": "mary", "answer": "grandfather"},
    ]
    examples = []
    for i in range(n):
        t = templates[i % len(templates)]
        examples.append({
            "id": f"clutrr_synth_{i}",
            "document": t["story"],
            "question": f"What is the relationship between {t['e1']} and {t['e2']}?",
            "entities": [t["e1"], t["e2"]],
            "answer": t["answer"],
            "benchmark": "clutrr"
        })
    logger.info(f"Generated {len(examples)} synthetic CLUTRR examples")
    return examples
