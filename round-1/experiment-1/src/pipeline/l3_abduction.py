"""L3: Self-consistency LLM abduction for unresolved goals."""
from loguru import logger
from pipeline.or_client import call_llm

ABDUCTION_PROMPT = """Document excerpt:
{document_excerpt}

Question: Based ONLY on the document above, does the following hold?
Predicate: {predicate}({args})
Answer with exactly 'yes' or 'no', followed by one sentence justification."""


def abduce_l3(predicate: str, args: list[str], document: str, K: int = 5) -> dict:
    """
    Self-consistency abduction: call LLM K times, return majority vote.
    Returns dict with confidence (fraction of 'yes' votes) and metadata.
    """
    yes_count = 0
    justifications = []
    args_str = ", ".join(args) if args else "()"
    doc_excerpt = document[:2000]

    for i in range(K):
        try:
            prompt = ABDUCTION_PROMPT.format(
                document_excerpt=doc_excerpt,
                predicate=predicate,
                args=args_str
            )
            answer = call_llm(prompt, temperature=0.7, max_tokens=80)
            answer_lower = answer.strip().lower()
            if answer_lower.startswith("yes"):
                yes_count += 1
            justifications.append(answer[:200])
        except Exception as e:
            logger.warning(f"L3 abduction call {i} failed: {e}")
            justifications.append(f"error: {e}")

    effective_K = max(1, K - justifications.count(f"error: "))
    confidence = yes_count / K if K > 0 else 0.0

    return {
        "predicate": predicate,
        "args": args,
        "tier": "l3",
        "confidence": confidence,
        "low_confidence": confidence < 0.6,
        "K": K,
        "yes_count": yes_count,
        "justifications": justifications
    }
