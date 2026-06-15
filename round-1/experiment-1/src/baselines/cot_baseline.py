"""Chain-of-thought LLM baseline."""
from pipeline.or_client import call_llm
from loguru import logger
import re

COT_PROMPT = """Document:
{document}

Question: {question}
Think step by step, then answer True, False, or Unknown on the last line."""


def cot_answer(document: str, question: str) -> str:
    """Run CoT reasoning and extract True/False/Unknown."""
    try:
        prompt = COT_PROMPT.format(document=document[:3000], question=question)
        raw = call_llm(prompt, temperature=0.0, max_tokens=400)
        # Look for answer in last few words
        last_part = " ".join(raw.split()[-20:]).lower()
        for ans in ["true", "false", "unknown"]:
            if ans in last_part:
                return ans.capitalize()
        # Check full response
        full_lower = raw.lower()
        if "true" in full_lower.split()[-5:] or raw.strip().lower().endswith("true"):
            return "True"
        if "false" in full_lower.split()[-5:] or raw.strip().lower().endswith("false"):
            return "False"
        # Final fallback: check most common occurrence
        t_count = raw.lower().count("true")
        f_count = raw.lower().count("false")
        u_count = raw.lower().count("unknown")
        if t_count > f_count and t_count > u_count:
            return "True"
        elif f_count > t_count and f_count > u_count:
            return "False"
        return "Unknown"
    except Exception as e:
        logger.error(f"CoT call failed: {e}")
        return "Unknown"
