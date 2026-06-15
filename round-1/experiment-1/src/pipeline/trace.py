"""JSON-LD derivation trace builder."""

TIER_COLORS = {
    "l0": "green", "l1": "yellow", "sld": "yellow",
    "l2": "orange", "l3": "red", "unknown": "gray"
}


def build_jsonld(proof_tree: list[dict], doc_id: str) -> dict:
    nodes = []
    for i, node in enumerate(proof_tree):
        tier = node.get("tier", "unknown")
        nodes.append({
            "@id": f"node:{doc_id}:{i}",
            "@type": "ProofNode",
            "predicate": node.get("predicate", ""),
            "args": node.get("args", []),
            "tier": tier,
            "confidence": node.get("confidence", 0.0),
            "color": TIER_COLORS.get(tier, "gray"),
            "source_span": node.get("source_span", ""),
            "method": node.get("method", "unknown"),
            "goal": node.get("goal", ""),
        })
    return {
        "@context": {"@vocab": "https://schema.org/"},
        "@type": "ProofTrace",
        "document_id": doc_id,
        "nodes": nodes,
    }
