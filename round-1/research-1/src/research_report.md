# Technical Integration Reference: Four-Tier Neuro-Symbolic Pipeline

## Summary

Comprehensive technical reference covering all nine integration points required to implement the provenance-stratified neuro-symbolic pipeline and reproduce the SymBa baseline. Key findings: (1) LKIF Core OWL is available via 15 modular GitHub raw URLs; norm.owl confirms Obligation, Prohibition, Permission, Right, Legal_Document, Contract class hierarchy under namespace http://www.estrellaproject.org/lkif-core/norm.owl#; load via owlready2 or rdflib. (2) pyswip (Python 3.9+, SWI-Prolog ≥8.x) provides assertz/asserta/retract/retractall; call_with_depth_limit/3 returns integer depth on success, 'depth_limit_exceeded' atom on limit, fails if goal fails; NOT thread-safe — use multiprocessing. (3) ConceptNet API has 34 relations, no auth, 3600 req/hr; weights are 1.0–10.0 not 0.0–1.0 as assumed in hypothesis; legal coverage is a confirmed disconfirmation risk. (4) Wikidata SPARQL at https://query.wikidata.org/sparql requires User-Agent header; key QIDs: legal obligation=Q56297395, legal norm=Q216200 (planning-phase Q1756864 was wrong — it's a Brazilian municipality). (5) SymBa CONFIRMED starts with empty Prolog DB ('Initially, the solver cannot prove the provided goal because its symbolic database is empty'); LLM called on SLD Search failure; 5-module generation (Fact/Rule Search → Translation → Symbolic Validation); uses OpenAI API replaceable via base_url override; run via 'python hiereason/run_symba.py --dataset proofwriter_dep5'. (6) ProofWriter OWA configs use naming pattern {Type}{Neg}-OWA-D{depth}-{id}; enumerate with get_dataset_config_names(). (7) CLUTRR/v1 has 21 kinship labels, ~1048 test examples, proof_state field contains logical derivation. (8) SARA (jhu-clsp/SARA) has 376 cases, gold Prolog KB achieving 100% accuracy, neo-Davidsonian event semantics. (9) ContractNLI available without ToU at kiddothe2b/contract-nli (CC-BY-NC-SA-4.0); 607 NDAs, 17 hypotheses, 3 labels. All URLs verified live (except ConceptNet which returned 502 errors in June 2026).

## Research Findings

## LKIF Core OWL [1, 2]

The repository at https://github.com/RinkeHoekstra/lkif-core contains 15 modular OWL files (CC BY 4.0, updated Feb 2026) [1]. The primary legal concept module is `norm.owl`, which defines the following class hierarchy under namespace `http://www.estrellaproject.org/lkif-core/norm.owl#` [2]:

- `Norm` → `Permission` → `Obligation` (equivalent to `Prohibition` in Hohfeldian deontic modeling)
- `Right` → `Liberty_Right`, `Liability_Right`, `Obligative_Right`, `Potestative_Right`
- `Legal_Source` → `Legal_Document` → `Contract`, `Statute`, `Regulation`, `Treaty`, `Directive`
- `Normatively_Qualified` → `Allowed`/`Disallowed` → `Obliged`, `Strictly_Disallowed`

Raw download URLs: `https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/norm.owl` and `lkif-core.owl` (integration file). Load via `owlready2` (OWL-DL support, SWRL partially) or `rdflib` (for pure SPARQL subclass queries) [1]. Note: original estrellaproject.org URLs are offline; use GitHub raw URLs.

## SWI-Prolog Python Bridge [3, 4, 5, 18]

`pyswip` (pip install pyswip) requires Python ≥ 3.9 and a system SWI-Prolog installation (apt-get install swi-prolog), with matching architectures [5, 18]. Core patterns: `prolog.assertz('fact(x)')`, `prolog.retractall('fact(_)')`, `list(prolog.query('fact(X)'))` returning `[{'X': 'x'}]` [4]. The `call_with_depth_limit(:Goal, +Limit, -Result)` predicate binds Result to the deepest recursion integer on success, to atom `depth_limit_exceeded` on limit hit, or fails entirely if the goal fails within limit [3]. **Critical**: pyswip is NOT thread-safe — use `multiprocessing`, not `threading` [5]. No built-in timeout for `Prolog.query()`; implement via `Process.join(timeout=N)`. Janus bridge (packages-swipy) is a more modern alternative but requires building from source [19].

## ConceptNet REST API [6, 7]

Base URL `http://api.conceptnet.io`; no authentication; 3600 requests/hour rate limit [6]. Contains 34 relations in `/r/` namespace [7]. JSON-LD response edges contain: `start.label`, `end.label`, `rel.label`, `weight`, `surfaceText` [6]. **Important correction**: ConceptNet weights range 1.0–10.0, NOT 0.0–1.0 as assumed in the hypothesis; threshold of 0.80 would pass nearly all edges — recalibrate to ~2.0 [6]. **Disconfirmation risk**: legal terms like `obligation`, `prohibition`, `norm` exist in ConceptNet but with everyday-English semantics, not legal; coverage requires empirical verification. The API returned HTTP 502 during research (June 2026); implement exponential backoff.

## Wikidata SPARQL [8, 9, 10]

Endpoint: `https://query.wikidata.org/sparql`. User-Agent header required [8]. Key QID corrections: legal obligation = **Q56297395** (not Q1756864 which is a Brazilian municipality), legal norm = **Q216200** [9, 10]. Property path `wdt:P31/wdt:P279*` traverses instance-of then zero-or-more subclass hops. Label service: `SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }` [8]. Use `SPARQLWrapper` (pip install SPARQLWrapper) with `addCustomHttpHeader('User-Agent', '...')` [8].

## SymBa Baseline [11, 12, 20]

**CONFIRMED**: SymBa starts with a completely empty Prolog knowledge base — *"Initially, the solver cannot prove the provided goal because its symbolic database (working memory) is empty"* (Figure 3, NAACL 2025 paper) [11]. The LLM callback is triggered when the SLD resolution Search step finds no rule or fact in the current database that unifies with the current subgoal [11]. Single-step statement generation has five modules: Fact Search, Rule Search, Fact Translation, Rule Translation, and Symbolic Validation (pure symbolic — no LLM) [11]. LLM output is a single Prolog statement added to working memory; solver retries the failed goal [11]. Termination: topmost goal proved, or all paths exhausted [11]. Config via `hiereason_config.yaml` with OpenAI API key (replaceable via `base_url='https://openrouter.ai/api/v1'`) [12]. Run: `python hiereason/run_symba.py --dataset proofwriter_dep5` [12]. Prompt templates at `data/(dataset)/prompt_data.json` [12].

## Dataset: ProofWriter D*(OWA) [13]

HuggingFace: `tasksource/proofwriter`. Config naming pattern: `{Type}{Neg}-OWA-D{depth}-{numeric_id}` (e.g., `AttNeg-OWA-D0-4611`) [13]. Types: AttNeg-OWA, AttNoneg-OWA, RelNeg-OWA, RelNoneg-OWA; depths D0–D10. Enumerate via `get_dataset_config_names('tasksource/proofwriter')`. Fields: `theory`, `question`, `answer` (True/False/Unknown), `allProofs`, `maxD`, `NFact`, `NRule` [13]. Total: 845k rows across all configs; test split ~174k.

## Dataset: CLUTRR [14]

HuggingFace: `CLUTRR/v1`; test split ~1,048 instances [14]. Fields: `story`, `query`, `target` (0–20), `target_text` (21 kinship labels), `proof_state` (logical derivation pathway dict), `task_name` (task_1.{k} where k=chain length 2–10) [14]. Filter by chain length: `ds['test'].filter(lambda x: x['task_name'].startswith('task_1.5'))` [14].

## Dataset: SARA [15]

HuggingFace: `jhu-clsp/SARA`; 376 total cases (276 binary + 100 numerical); 256 train, 120 test [15]. Fields: `id`, `text` (NL tax scenario), `question`, `answer` (Entailment/Contradiction or numeric), `facts` (Prolog predicates), `test` (Prolog execution code) [15]. Gold Prolog KB achieves 100% accuracy. Neo-Davidsonian event semantics with 61 predicate types. Load: `load_dataset('jhu-clsp/SARA', 'qa', split='test')` [15].

## Dataset: ContractNLI [16, 17]

Official (requires ToU): https://stanfordnlp.github.io/contract-nli/ [16]. HuggingFace without ToU: `kiddothe2b/contract-nli` (CC-BY-NC-SA-4.0) [17]. 607 NDAs, 17 fixed hypotheses per document, 3-class labels (Entailment/Contradiction/NotMentioned) [16, 17]. HF fields: `premise` (37–2,770 chars), `hypothesis`, `label` (0/1/2) [17]. Configs: `contractnli_a`, `contractnli_b`. Official JSON uses document-level annotation with span evidence indices [16]. Annotation is document-level (requires reasoning over full NDA, not per-sentence) [16].

## Sources

[1] [LKIF Core GitHub Repository](https://github.com/RinkeHoekstra/lkif-core) — 15 modular OWL files, CC BY 4.0, updated Feb 2026. Lists all modules: top.owl through lkif-extended.owl.

[2] [LKIF norm.owl raw file](https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/norm.owl) — Full class hierarchy confirmed: Norm, Obligation, Prohibition, Permission, Right, Legal_Document, Contract, Statute. Namespace http://www.estrellaproject.org/lkif-core/norm.owl#

[3] [SWI-Prolog call_with_depth_limit/3](https://www.swi-prolog.org/pldoc/man?predicate=call_with_depth_limit/3) — Predicate signature, Result bindings on success/limit/fail, no explicit backtracking documentation.

[4] [PySwip Prolog API](https://pyswip.readthedocs.io/en/latest/api/prolog.html) — assertz/asserta/retract/retractall usage; no timeout in query(); format string %p substitution.

[5] [PySwip GitHub (yuce)](https://github.com/yuce/pyswip) — Python 3.9+ requirement, NOT thread-safe, use multiprocessing, arch matching requirement.

[6] [ConceptNet 5 API Wiki](https://github.com/commonsense/conceptnet5/wiki/API) — Endpoint patterns, rate limits 3600/hr, no auth, JSON-LD response schema with edges array.

[7] [ConceptNet Relations](https://github.com/commonsense/conceptnet5/wiki/Relations) — All 34 relations in /r/ namespace listed with descriptions.

[8] [Wikidata SPARQL Tutorial](https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial) — Endpoint URL, wd:/wdt: prefixes, P31/P279 properties, SERVICE wikibase:label pattern, property paths.

[9] [Wikidata Q56297395: legal obligation](https://www.wikidata.org/wiki/Q56297395) — QID for legal obligation: legal requirement to take some course of action; subclass of obligation and duty.

[10] [Wikidata Q216200: legal norm](https://www.wikidata.org/wiki/Q216200) — QID for legal norm: commandment, instruction, or order as authoritative rule of action.

[11] [SymBa: Symbolic Backward Chaining for Structured Natural Language Reasoning (NAACL 2025)](https://aclanthology.org/2025.naacl-long.124.pdf) — CONFIRMED empty DB. Algorithm details, 5-module LLM generation pipeline, performance tables, SLD resolution coroutine.

[12] [SymBa GitHub Repository](https://github.com/lbox-kr/symba) — Run commands, dataset folder names, config YAML setup, prompt_data.json location.

[13] [ProofWriter HuggingFace (tasksource)](https://huggingface.co/datasets/tasksource/proofwriter) — Config naming pattern with numeric suffix; 845k total rows; fields including theory/question/answer/allProofs.

[14] [CLUTRR v1 HuggingFace](https://huggingface.co/datasets/CLUTRR/v1) — 21 kinship labels confirmed, test ~1048, proof_state = logical derivation pathway, task_name = chain length.

[15] [SARA HuggingFace (jhu-clsp)](https://huggingface.co/datasets/jhu-clsp/SARA) — 376 cases, fields id/text/question/answer/facts/test, gold Prolog KB achieving 100% accuracy, QA and NLI splits.

[16] [ContractNLI Official Page (Stanford)](https://stanfordnlp.github.io/contract-nli/) — 607 NDAs, 17 hypotheses, 3-class labels, JSON schema with documents/spans/annotation_sets, ToU required.

[17] [ContractNLI HuggingFace (kiddothe2b)](https://huggingface.co/datasets/kiddothe2b/contract-nli) — No ToU barrier; CC-BY-NC-SA-4.0; configs contractnli_a/b; ~20k rows; fields premise/hypothesis/label.

[18] [PySwip Get Started](https://pyswip.org/get-started.html) — Installation steps, SWI-Prolog arch matching, SWI_HOME_DIR/LIBSWIPL_PATH environment variables.

[19] [SWI-Prolog Janus Bridge](https://github.com/SWI-Prolog/packages-swipy) — Modern alternative to pyswip; bidirectional Python-Prolog; requires build from source.

[20] [SymBa arXiv Preprint](https://arxiv.org/abs/2402.12806) — Abstract confirming solver-LLM integration where LLM called only on solver failure.

## Follow-up Questions

- ConceptNet legal coverage: Are terms like 'obligation', 'prohibition', 'norm', 'contract', 'party' represented with meaningful legal-domain edges in ConceptNet, or is coverage sparse/everyday-English only? What weight threshold should be used given ConceptNet weights are ~1.0-10.0, not 0.0-1.0 as assumed in the hypothesis?
- ProofWriter exact OWA config strings: What are ALL available config names for tasksource/proofwriter? Does the D*(OWA) config match a simple depth string or require the full numeric-suffix pattern? Run get_dataset_config_names('tasksource/proofwriter') to enumerate before loading.
- SymBa adaptation for legal datasets: The prompt templates in data/(dataset)/prompt_data.json are dataset-specific for ProofWriter/CLUTRR. What prompt format changes are needed to adapt SymBa for SARA (neo-Davidsonian Prolog predicates) and ContractNLI (NDA clauses + 17 standardized hypotheses)?

---
*Generated by AI Inventor Pipeline*
