"""L0: LLM-based extraction of ground atomic facts from documents."""
import json
import re
from pathlib import Path
from loguru import logger
from pipeline.or_client import call_llm

EXTRACTION_PROMPT = """You are a Prolog knowledge engineer. Extract ALL atomic facts from the following document as Prolog predicates.

Rules:
- Use lowercase snake_case for predicate names and all atom arguments
- No variables (start with uppercase) in extracted facts — only ground atoms
- No spaces inside predicates. Arguments must match [a-z][a-z0-9_]* pattern.
- Each fact must correspond to something EXPLICITLY stated in the document, not inferred
- Format each fact as valid Prolog: predicate_name(arg1, arg2, ...)

Output ONLY a JSON array of objects, each with keys:
  {{"predicate": str, "args": [str, ...], "source_span": str, "confidence": 1.0, "tier": "l0"}}

Document:
{document}
"""

FEW_SHOT_EXAMPLES = """
EXAMPLE 1:
Document: "Alice owns a red car. Bob is Alice's brother. The car was manufactured in 2020."
Output:
[
  {"predicate": "owns", "args": ["alice", "car_001"], "source_span": "Alice owns a red car", "confidence": 1.0, "tier": "l0"},
  {"predicate": "color", "args": ["car_001", "red"], "source_span": "red car", "confidence": 1.0, "tier": "l0"},
  {"predicate": "brother_of", "args": ["bob", "alice"], "source_span": "Bob is Alice's brother", "confidence": 1.0, "tier": "l0"},
  {"predicate": "manufactured_year", "args": ["car_001", "y2020"], "source_span": "manufactured in 2020", "confidence": 1.0, "tier": "l0"}
]

EXAMPLE 2:
Document: "The Tenant shall pay rent of $1,500 per month. The Landlord is John Smith. The lease term is one year."
Output:
[
  {"predicate": "pays_rent", "args": ["tenant", "landlord"], "source_span": "Tenant shall pay rent", "confidence": 1.0, "tier": "l0"},
  {"predicate": "rent_amount", "args": ["tenant", "usd_1500_per_month"], "source_span": "rent of $1,500 per month", "confidence": 1.0, "tier": "l0"},
  {"predicate": "is_landlord", "args": ["john_smith"], "source_span": "Landlord is John Smith", "confidence": 1.0, "tier": "l0"},
  {"predicate": "lease_term", "args": ["lease", "one_year"], "source_span": "lease term is one year", "confidence": 1.0, "tier": "l0"}
]

EXAMPLE 3:
Document: "Tom is the father of Bob. Bob is the father of Ann. Mary is Bob's mother."
Output:
[
  {"predicate": "father", "args": ["tom", "bob"], "source_span": "Tom is the father of Bob", "confidence": 1.0, "tier": "l0"},
  {"predicate": "father", "args": ["bob", "ann"], "source_span": "Bob is the father of Ann", "confidence": 1.0, "tier": "l0"},
  {"predicate": "mother", "args": ["mary", "bob"], "source_span": "Mary is Bob's mother", "confidence": 1.0, "tier": "l0"}
]
"""

EXTRACTION_PROMPT_FEW_SHOT = FEW_SHOT_EXAMPLES + "\n\nNow extract from this document:\n\n" + EXTRACTION_PROMPT

_ATOM_RE = re.compile(r'^[a-z][a-z0-9_]*$')

def _validate_facts(facts: list) -> list:
    valid = []
    for f in facts:
        if not isinstance(f, dict):
            continue
        pred = f.get("predicate", "")
        args = f.get("args", [])
        if not _ATOM_RE.match(str(pred)):
            continue
        if not all(_ATOM_RE.match(str(a)) for a in args):
            # Try to sanitize args
            clean_args = []
            for a in args:
                a = str(a).lower().replace(" ", "_").replace("-", "_")
                a = re.sub(r'[^a-z0-9_]', '', a)
                if not a or not _ATOM_RE.match(a):
                    a = None
                clean_args.append(a)
            if any(a is None for a in clean_args):
                continue
            f["args"] = clean_args
        f.setdefault("confidence", 1.0)
        f.setdefault("tier", "l0")
        f.setdefault("source_span", "")
        valid.append(f)
    return valid


def extract_l0(document: str, domain: str = "general", use_few_shot: bool = False) -> list[dict]:
    doc_snippet = document[:4000]
    if use_few_shot:
        prompt = EXTRACTION_PROMPT_FEW_SHOT.format(document=doc_snippet)
    else:
        prompt = EXTRACTION_PROMPT.format(document=doc_snippet)

    try:
        raw = call_llm(prompt, temperature=0.0, max_tokens=2000)
    except Exception:
        logger.error("L0 extraction LLM call failed")
        return []

    # Extract JSON array (greedy to get full array)
    match = re.search(r'\[.*\]', raw, re.DOTALL)
    if not match:
        logger.warning(f"No JSON array in L0 response: {raw[:200]}")
        return []

    json_str = match.group()
    try:
        facts = json.loads(json_str)
    except json.JSONDecodeError as e:
        # Try to recover partial JSON by truncating after last complete element
        last_brace = json_str.rfind('},')
        if last_brace > 0:
            truncated = json_str[:last_brace + 1] + "]"
            try:
                facts = json.loads(truncated)
                logger.debug(f"Recovered partial JSON with {len(facts)} facts")
            except json.JSONDecodeError:
                logger.warning(f"JSON parse error in L0 (unrecoverable): {e}; raw={raw[:200]}")
                return []
        else:
            logger.warning(f"JSON parse error in L0: {e}; raw={raw[:200]}")
            return []

    valid = _validate_facts(facts)
    logger.debug(f"L0 extracted {len(valid)}/{len(facts)} valid facts")
    return valid
