"""L2: Domain-adaptive ontology bridging via LKIF/owlready2 and ConceptNet REST."""
import requests
from loguru import logger

# Cache for ConceptNet and LKIF queries
_cn_cache: dict[str, list] = {}
_lkif_cache: dict[str, list] = {}

LKIF_URL = "https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl"

# Hardcoded fallback LKIF legal concepts (superclass hierarchy)
LKIF_FALLBACK = {
    "obligation": ["norm", "qualified_norm", "normative_thing", "mental_object", "propositional_attitude"],
    "right": ["norm", "qualified_norm", "normative_thing"],
    "permission": ["norm", "qualified_norm", "normative_thing"],
    "prohibition": ["norm", "qualified_norm", "normative_thing"],
    "contract": ["legal_document", "document", "information", "mental_object"],
    "party": ["legal_person", "person", "agent"],
    "person": ["agent", "living_being"],
    "agent": ["object"],
    "document": ["information", "mental_object"],
    "agreement": ["legal_document", "document"],
    "property": ["object"],
    "act": ["action", "event"],
    "action": ["event"],
    "liability": ["norm", "qualified_norm"],
    "entitlement": ["right", "norm"],
    "duty": ["obligation", "norm"],
    "statute": ["legal_document", "document"],
    "regulation": ["legal_document", "document"],
}


def load_lkif():
    """Load LKIF ontology via owlready2, or return None on failure."""
    try:
        from owlready2 import get_ontology
        onto = get_ontology(LKIF_URL)
        onto.load()
        logger.info("LKIF ontology loaded successfully")
        return onto
    except Exception as e:
        logger.warning(f"LKIF load failed (using fallback dict): {e}")
        return None


def query_lkif_subsumption(onto, concept_name: str) -> list[str]:
    """Return ancestor class names for concept_name. Uses fallback if onto is None."""
    if onto is None:
        return _lkif_fallback_lookup(concept_name)
    if concept_name in _lkif_cache:
        return _lkif_cache[concept_name]
    try:
        matched = [c for c in onto.classes() if concept_name.lower() in c.name.lower()]
        if not matched:
            result = _lkif_fallback_lookup(concept_name)
        else:
            cls = matched[0]
            result = [a.name for a in cls.ancestors() if a is not cls]
        _lkif_cache[concept_name] = result
        return result
    except Exception as e:
        logger.warning(f"LKIF query failed for {concept_name}: {e}")
        return _lkif_fallback_lookup(concept_name)


def _lkif_fallback_lookup(concept: str) -> list[str]:
    concept_lower = concept.lower()
    for key, ancestors in LKIF_FALLBACK.items():
        if key in concept_lower or concept_lower in key:
            return ancestors
    return []


def query_conceptnet(entity: str, relation: str = "IsA") -> list[tuple[str, float]]:
    """Query ConceptNet REST API for IsA relations."""
    cache_key = f"{entity}:{relation}"
    if cache_key in _cn_cache:
        return _cn_cache[cache_key]

    entity_slug = entity.replace("_", " ").strip()
    url = f"https://api.conceptnet.io/query?node=/c/en/{entity_slug.replace(' ', '_')}&rel=/r/{relation}&limit=10"
    try:
        resp = requests.get(url, timeout=8)
        if resp.status_code != 200:
            _cn_cache[cache_key] = []
            return []
        edges = resp.json().get("edges", [])
        results = []
        for e in edges:
            end_label = e.get("end", {}).get("label", "")
            weight = e.get("weight", 1.0)
            conf = min(0.80, weight / 10.0 + 0.70)
            end_clean = end_label.lower().replace(" ", "_").replace("-", "_")
            import re
            end_clean = re.sub(r'[^a-z0-9_]', '', end_clean)
            if end_clean:
                results.append((end_clean, conf))
        _cn_cache[cache_key] = results
        return results
    except Exception as e:
        logger.warning(f"ConceptNet query failed for {entity}: {e}")
        _cn_cache[cache_key] = []
        return []


def classify_domain(document: str) -> str:
    """Classify document domain: legal, narrative, or general."""
    doc_lower = document.lower()
    legal_kw = ["contract", "obligation", "party", "law", "statute", "agreement",
                "liability", "clause", "provision", "plaintiff", "defendant",
                "tenant", "landlord", "lease", "breach", "damages", "shall"]
    narrative_kw = ["story", "character", "once upon", "family", "village",
                   "sister", "brother", "father", "mother", "grandfather",
                   "grandmother", "uncle", "aunt", "cousin", "nephew", "niece"]
    legal_score = sum(1 for kw in legal_kw if kw in doc_lower)
    narrative_score = sum(1 for kw in narrative_kw if kw in doc_lower)
    if legal_score >= 3:
        return "legal"
    elif narrative_score >= 2:
        return "narrative"
    return "general"


def query_l2(goal_predicate: str, goal_args: list[str], domain: str, onto=None) -> list[dict]:
    """Query L2 ontology for bridging facts."""
    results = []
    if domain == "legal" and onto is not None:
        for arg in goal_args:
            ancestors = query_lkif_subsumption(onto, arg)
            for anc in ancestors[:3]:  # limit
                anc_clean = anc.lower().replace(" ", "_")
                results.append({
                    "predicate": "is_a",
                    "args": [arg, anc_clean],
                    "tier": "l2", "confidence": 0.90,
                    "source": "lkif"
                })
    elif domain == "legal" and onto is None:
        # Use fallback
        for arg in goal_args:
            ancestors = _lkif_fallback_lookup(arg)
            for anc in ancestors[:3]:
                results.append({
                    "predicate": "is_a",
                    "args": [arg, anc],
                    "tier": "l2", "confidence": 0.85,
                    "source": "lkif_fallback"
                })
    else:
        # Use ConceptNet for general/narrative
        for arg in goal_args[:2]:  # limit API calls
            cn_results = query_conceptnet(arg)
            for label, conf in cn_results[:3]:
                results.append({
                    "predicate": "is_a",
                    "args": [arg, label],
                    "tier": "l2", "confidence": conf,
                    "source": "conceptnet"
                })
    return results
