"""Hallucination rate computation: L0 facts vs source document."""
import re


def compute_hallucination_rate(proof_trees: list[list[dict]], documents: list[str]) -> float:
    """
    Fraction of L0-tier facts whose content cannot be verified in the source document.
    A fact is considered grounded if any argument token appears in the document.
    """
    hallucinated = 0
    total_l0 = 0

    for tree_nodes, doc in zip(proof_trees, documents):
        doc_lower = doc.lower()
        # Tokenize document to words
        doc_tokens = set(re.findall(r'[a-z][a-z0-9_]+', doc_lower))

        for node in tree_nodes:
            if node.get("tier") not in ("l0", "l1", "sld"):
                continue
            total_l0 += 1
            args = node.get("args", [])
            pred = node.get("predicate", "")
            source_span = node.get("source_span", "")

            # Check source span if available
            if source_span and source_span.lower() in doc_lower:
                continue

            # Check if any arg (unstemmed) or predicate keyword appears in doc
            grounded = False
            for arg in args:
                arg_clean = arg.replace("_", " ")
                arg_token = arg.replace("_", "")
                if arg_clean in doc_lower or arg_token in doc_lower:
                    grounded = True
                    break
                # Check individual tokens from the arg
                arg_tokens = set(arg.split("_"))
                if arg_tokens & doc_tokens:
                    grounded = True
                    break

            if not grounded:
                # Also check predicate
                pred_tokens = set(pred.split("_"))
                if pred_tokens & doc_tokens:
                    grounded = True

            if not grounded:
                hallucinated += 1

    return hallucinated / total_l0 if total_l0 > 0 else 0.0


def compute_hallucination_rate_baseline(symba_results: list[dict], documents: list[str]) -> float:
    """
    Estimate hallucination rate for flat LLM baseline.
    Since the flat LLM produces free-form answers with no fact extraction,
    we estimate based on: answer_raw contains entities not in document.
    """
    hallucinated = 0
    total = 0
    for result, doc in zip(symba_results, documents):
        answer_raw = result.get("answer_raw", "")
        if not answer_raw:
            continue
        total += 1
        doc_lower = doc.lower()
        # Extract all named tokens from answer not in document
        answer_tokens = set(re.findall(r'[a-z][a-z]{2,}', answer_raw.lower()))
        doc_tokens = set(re.findall(r'[a-z][a-z]{2,}', doc_lower))
        stop_words = {"the", "and", "for", "this", "that", "with", "from", "not", "yes", "based", "only",
                      "document", "hold", "predicate", "does", "following", "above", "sentence"}
        answer_unique = answer_tokens - doc_tokens - stop_words
        if len(answer_unique) > 2:  # More than 2 unique tokens = likely hallucination
            hallucinated += 1

    return hallucinated / total if total > 0 else 0.0
