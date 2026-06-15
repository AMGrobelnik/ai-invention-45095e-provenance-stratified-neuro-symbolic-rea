"""Meta-interpreter: tier-ordered resolution with weakest-link provenance propagation."""
from loguru import logger
from pipeline.l1_prolog import PrologKB
from pipeline import l2_ontology, l3_abduction as l3_mod

TIER_ORDER = {"l0": 0, "l1": 1, "l2": 2, "l3": 3, "sld": 1, "unknown": 4}


class MetaInterpreter:
    def __init__(
        self,
        kb: PrologKB,
        domain: str,
        document: str,
        lkif_onto=None,
        l3_K: int = 5,
    ):
        self.kb = kb
        self.domain = domain
        self.document = document
        self.lkif_onto = lkif_onto
        self.l3_K = l3_K
        self.proof_tree: list[dict] = []

    def propagate(self, premises: list[dict]) -> dict:
        """Weakest-link: tier = worst tier, conf = min conf."""
        if not premises:
            return {"tier": "unknown", "confidence": 0.0}
        max_tier = max(premises, key=lambda p: TIER_ORDER.get(p.get("tier", "unknown"), 4))
        min_conf = min(p.get("confidence", 0.0) for p in premises)
        return {"tier": max_tier.get("tier", "unknown"), "confidence": min_conf}

    def prove(self, predicate: str, args: list[str], depth: int = 0) -> dict:
        """Attempt proof via tier-ordered resolution."""
        goal_str = predicate + "(" + ", ".join(args) + ")" if args else predicate
        node: dict = {"goal": goal_str, "predicate": predicate, "args": args, "depth": depth}

        # --- L0/L1: try SWI-Prolog with depth limit ---
        proved, tier = self.kb.query_with_depth_limit(goal_str, depth=5)
        if proved:
            node.update({"tier": tier, "confidence": 1.0, "method": "sld"})
            self.proof_tree.append(node)
            return node

        # --- L2: domain-adaptive ontology ---
        l2_facts = l2_ontology.query_l2(predicate, args, self.domain, self.lkif_onto)
        if l2_facts:
            best = max(l2_facts, key=lambda f: f.get("confidence", 0.0))
            # Assert best L2 fact into KB for chaining
            best_atom = best["predicate"] + "(" + ", ".join(best["args"]) + ")"
            self.kb.assertz(best_atom, tier="l2", confidence=best.get("confidence", 0.8))
            node.update(best)
            node["method"] = "l2_ontology"
            self.proof_tree.append(node)
            return node

        # --- L3: LLM abduction (only at shallow depth to avoid explosion) ---
        if depth <= 1:
            l3_result = l3_mod.abduce_l3(predicate, args, self.document, K=self.l3_K)
            if l3_result["confidence"] >= 0.6:
                self.kb.assertz(goal_str, tier="l3", confidence=l3_result["confidence"])
                node.update(l3_result)
                node["method"] = "l3_abduction"
            else:
                node.update({
                    "tier": "unknown", "confidence": 0.0,
                    "low_confidence": True, "method": "l3_abduction_failed",
                    "l3_confidence": l3_result["confidence"]
                })
            self.proof_tree.append(node)
            return node

        node.update({"tier": "unknown", "confidence": 0.0, "method": "none"})
        self.proof_tree.append(node)
        return node

    def get_trace(self) -> list[dict]:
        return list(self.proof_tree)

    def reset_trace(self):
        self.proof_tree = []
