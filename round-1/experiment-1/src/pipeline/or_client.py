"""OpenRouter client using the ability client venv."""
import subprocess
import json
import re
import os
from pathlib import Path
from loguru import logger
from tenacity import retry, stop_after_attempt, wait_exponential

SKILL_DIR = Path("/ai-inventor/.claude/skills/aii-openrouter-llms")
PY = str(SKILL_DIR / "../.ability_client_venv/bin/python")
CALL_SCRIPT = str(SKILL_DIR / "scripts/aii_or_call_llms.py")

DEFAULT_MODEL = "meta-llama/llama-3.1-70b-instruct"
# Pricing estimates (per M tokens)
PRICE_IN = 0.35
PRICE_OUT = 0.40

_total_cost = 0.0
_total_in_tokens = 0
_total_out_tokens = 0


def get_total_cost() -> float:
    return _total_cost


def get_token_counts() -> dict:
    return {"in": _total_in_tokens, "out": _total_out_tokens}


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def call_llm(
    prompt: str,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.0,
    max_tokens: int = 1000,
    system: str | None = None,
    cost_limit: float = 9.0,
) -> str:
    global _total_cost, _total_in_tokens, _total_out_tokens

    if _total_cost >= cost_limit:
        raise RuntimeError(f"Budget exceeded: ${_total_cost:.2f}")

    cmd = [PY, CALL_SCRIPT, "--model", model, "--input", prompt, "--max-tokens", str(max_tokens), "--temperature", str(temperature)]
    if system:
        cmd += ["--instructions", system]

    logger.debug(f"LLM call: model={model} temp={temperature} max_tokens={max_tokens} prompt={prompt[:100]!r}")

    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        logger.warning(f"LLM call stderr: {result.stderr[:200]}")
        raise RuntimeError(f"LLM call failed: {result.stderr[:200]}")

    output = result.stdout
    logger.debug(f"LLM response: {output[:200]!r}")

    # Parse token counts from output
    tok_match = re.search(r"Tokens:\s*(\d+)\s*in,\s*(\d+)\s*out", output)
    if tok_match:
        n_in = int(tok_match.group(1))
        n_out = int(tok_match.group(2))
        cost = (n_in / 1e6) * PRICE_IN + (n_out / 1e6) * PRICE_OUT
        _total_cost += cost
        _total_in_tokens += n_in
        _total_out_tokens += n_out

    # Extract response text (between "Response:\n" and "\nTokens:")
    resp_match = re.search(r"Response:\n(.*?)(?:\n\nTokens:|\Z)", output, re.DOTALL)
    if resp_match:
        return resp_match.group(1).strip()

    return output.strip()
