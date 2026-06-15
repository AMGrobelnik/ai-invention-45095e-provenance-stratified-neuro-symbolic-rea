"""Tier distribution metrics."""

TIER_ORDER = {"l0": 0, "l1": 1, "sld": 1, "l2": 2, "l3": 3, "unknown": 4}


def compute_tier_distribution(results: list[dict]) -> dict:
    """Compute fraction of proofs resolved at each tier."""
    counts = {"l0": 0, "l1": 0, "sld": 0, "l2": 0, "l3": 0, "unknown": 0}
    for r in results:
        tier = r.get("tier_used", "unknown")
        counts[tier] = counts.get(tier, 0) + 1
    n = max(1, len(results))
    fracs = {k: v / n for k, v in counts.items()}
    # L0-L2 fraction (no LLM abduction needed)
    fracs["l0_l1_l2_fraction"] = (counts.get("l0", 0) + counts.get("l1", 0) +
                                   counts.get("sld", 0) + counts.get("l2", 0)) / n
    return fracs
