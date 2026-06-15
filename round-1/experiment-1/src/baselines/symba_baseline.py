"""SymBa-style flat LLM baseline: empty KB, direct LLM for proof failures."""
from pipeline.or_client import call_llm
from loguru import logger

ABDUCTION_PROMPT = """Document excerpt:
{document_excerpt}

Question: Based ONLY on the document above, does the following hold?
{predicate}({args})
Answer with exactly 'yes' or 'no', followed by one sentence justification."""


def symba_prove(predicate: str, args: list[str], document: str) -> dict:
    """SymBa-style: empty KB, immediate LLM call with K=1, no ontology tier."""
    args_str = ", ".join(args) if args else "()"
    try:
        prompt = ABDUCTION_PROMPT.format(
            document_excerpt=document[:2000],
            predicate=predicate,
            args=args_str
        )
        answer = call_llm(prompt, temperature=0.0, max_tokens=100)
        proved = answer.strip().lower().startswith("yes")
        return {
            "tier": "llm_flat",
            "confidence": 1.0 if proved else 0.0,
            "proved": proved,
            "no_provenance": True,
            "answer_raw": answer[:200]
        }
    except Exception as e:
        logger.error(f"SymBa call failed: {e}")
        return {"tier": "error", "confidence": 0.0, "proved": False, "no_provenance": True}
