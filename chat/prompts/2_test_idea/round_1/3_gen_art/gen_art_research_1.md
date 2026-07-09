# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-15 20:11:56 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An artifact executor (Step 3.3: GEN_ART in the invention loop)

Executing a plan to produce a concrete artifact.
GEN_PAPER_TEXT will use your artifact in the next paper draft.

Rigorous artifact with clear results → strong paper. Sloppy artifact → misdirected research.
</your_role>
</ai_inventor_context>

<task>
Conduct thorough, unbiased research on the given topic.
Adapt your investigation approach based on the research question and domain.
</task>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<critical_requirements>
1. SOURCE DIVERSITY - Consult MANY sources (10+), not just the first few results
2. AVOID SELECTION BIAS - Actively seek contradicting viewpoints, not just confirming ones
3. TRIANGULATE - Cross-reference claims across multiple independent sources
4. ACKNOWLEDGE UNCERTAINTY - Be honest about confidence levels and limitations
5. SYNTHESIZE - Produce a coherent answer that accounts for conflicting evidence
</critical_requirements>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: Technical Integration Reference for Four-Tier Neuro-Symbolic Pipeline
summary: >-
  Gather all concrete technical specifications needed to implement the provenance-stratified pipeline: LKIF OWL file URLs,
  pyswip/SWI-Prolog bridge usage, ConceptNet and Wikidata API patterns, SymBa empty-DB invocation protocol, and canonical
  dataset access paths for ProofWriter D*(OWA), CLUTRR, SARA, and ContractNLI.
runpod_compute_profile: cpu_light
question: >-
  What are the exact technical integration points (URLs, API schemas, library calls, invocation protocols, dataset IDs) needed
  to implement the four-tier pipeline and reproduce SymBa as a baseline?
research_plan: |-
  ## Step-by-Step Research Plan

  ### PRE-VERIFIED FACTS (from planning-phase research — executor should verify links still live)

  The following were confirmed during planning and should be verified/deepened by the executor.

  ---

  ### TASK 1: LKIF Core OWL Ontology

  **Already known:**
  - GitHub repo: https://github.com/RinkeHoekstra/lkif-core
  - Primary OWL file: `lkif-core.owl` (in repo root)
  - Extended file: `lkif-extended.owl` (in repo root)
  - Raw GitHub URLs follow the pattern: `https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl`
  - TriplyDB hosted version: https://triplydb.com/estrella/lkif
  - Estrella project page (may be offline): http://www.estrellaproject.org/lkif-core/

  **Executor tasks:**
  1. Fetch https://github.com/RinkeHoekstra/lkif-core and list ALL .owl files in the repository (there are multiple modular files: mereology.owl, process.owl, lkif-core.owl, lkif-extended.owl, etc.).
  2. Identify which specific OWL classes cover the key legal concepts: `norm`, `obligation`, `prohibition`, `claim`, `agent`, `legal_document`, `party`. Report the exact class URIs and their namespace (likely `http://www.estrellaproject.org/lkif-core/`).
  3. Determine loading strategy: confirm whether `owlready2` can load this OWL-DL file (`from owlready2 import get_ontology; onto = get_ontology(url).load()`). Note any known issues with OWL-DL + SWRL in owlready2 (SWRL rules are partially supported).
  4. Identify if LKIF has a Turtle (.ttl) or N-Triples serialization for faster loading with `rdflib`.
  5. Provide the raw download URL for `lkif-core.owl` for use in `pip install rdflib` + `g.parse(url)` calls.

  **Search queries to run:**
  - `site:github.com/RinkeHoekstra/lkif-core` to enumerate all files
  - `owlready2 load OWL-DL SWRL rules example`
  - `rdflib parse LKIF OWL subclass query`

  ---

  ### TASK 2: SWI-Prolog Python Bridge (pyswip)

  **Already known:**
  - Install: `pip install pyswip` (requires SWI-Prolog system installation first)
  - Basic usage: `from pyswip import Prolog; prolog = Prolog(); prolog.assertz("father(michael,john)"); list(prolog.query("father(X,Y)"))`
  - `call_with_depth_limit/3` is a native SWI-Prolog predicate. Can be called via pyswip as a string query: `list(prolog.query("call_with_depth_limit(your_goal(X), 3, Result)"))`
  - SWI-Prolog docs: https://www.swi-prolog.org/pldoc/man?predicate=call_with_depth_limit/3
  - Alternative: `packages-swipy` (Janus, the official SWI-Prolog Python bridge): https://github.com/SWI-Prolog/packages-swipy

  **Executor tasks:**
  1. Fetch https://www.swi-prolog.org/pldoc/man?predicate=call_with_depth_limit/3 and extract the exact predicate signature, what `Result` binds to on success vs. depth exceeded, and whether it backtracks.
  2. Fetch https://pyswip.readthedocs.io/en/stable/ and extract: (a) how to assert facts dynamically with `assertz`/`asserta`, (b) how to retract facts, (c) whether `Prolog.query()` supports timeout or resource limits, (d) thread safety considerations.
  3. Determine if the `janus` bridge (packages-swipy) is needed instead of pyswip for the provenance-propagating meta-interpreter. The janus bridge provides a more modern API. Fetch https://github.com/SWI-Prolog/packages-swipy README.
  4. Identify the correct call pattern for depth-limited meta-interpretation:
     ```python
     # Target pattern to confirm:
     results = list(prolog.query(
       "call_with_depth_limit(solve(Goal, Proof), 3, Result)"
     ))
     ```
  5. Note pyswip version compatibility requirements (Python 3.x, SWI-Prolog version ≥ 8.x).

  **Search queries to run:**
  - `pyswip assertz retract dynamic predicates example`
  - `SWI-Prolog janus Python bridge install 2024`
  - `pyswip thread safety Prolog.query`

  ---

  ### TASK 3: ConceptNet REST API

  **Already known:**
  - Base URL: `http://api.conceptnet.io`
  - Query endpoint: `/query` with params `start`, `end`, `rel`, `node`, `other`
  - Relation URIs: `/r/IsA`, `/r/PartOf`, `/r/UsedFor`
  - Example: `http://api.conceptnet.io/query?start=/c/en/dog&rel=/r/IsA&limit=10`
  - JSON-LD response: fields include `edges[]` array with each edge having `start.label`, `end.label`, `rel.label`, `weight`, `surfaceText`
  - Rate limit: 3600 req/hour, burst 120/min

  **Executor tasks:**
  1. Fetch https://github.com/commonsense/conceptnet5/wiki/API and extract the COMPLETE list of available relation types (not just IsA/PartOf/UsedFor — confirm the full `/r/` namespace).
  2. Confirm the exact JSON-LD response structure by fetching a live example: `http://api.conceptnet.io/query?node=/c/en/obligation&rel=/r/IsA&limit=5`. Extract the field names and nesting.
  3. Confirm whether ConceptNet covers legal-domain terms like `obligation`, `prohibition`, `norm`, `contract`, `party`. Run test query: `http://api.conceptnet.io/c/en/obligation` and report what relations exist.
  4. Identify the `weight` field range and what threshold to use for filtering high-confidence relations (the hypothesis uses 0.80 for ConceptNet statistical association).
  5. Check if ConceptNet API requires authentication (it does not — confirm this).
  6. Confirm the language filter for English only: `/c/en/` prefix in node URIs.

  **Concrete API call pattern to document:**
  ```python
  import requests
  response = requests.get(
      'http://api.conceptnet.io/query',
      params={'start': '/c/en/obligation', 'rel': '/r/IsA', 'limit': 10}
  ).json()
  for edge in response['edges']:
      print(edge['end']['label'], edge['weight'])
  ```

  ---

  ### TASK 4: Wikidata SPARQL Endpoint

  **Already known:**
  - Endpoint: `https://query.wikidata.org/sparql`
  - P31 = instance of, P279 = subclass of
  - Path pattern: `?item wdt:P31/wdt:P279* ?class`
  - Python: use `SPARQLWrapper` or `requests` with `format=json`

  **Executor tasks:**
  1. Fetch https://www.wikidata.org/wiki/Wikidata:SPARQL_tutorial and extract: (a) the correct SPARQL endpoint URL with User-Agent header requirement, (b) the `wdt:` prefix expansion, (c) the SERVICE wikibase:label syntax for getting English labels.
  2. Document the canonical SPARQL query for entity type lookup:
     ```sparql
     SELECT ?classLabel WHERE {
       wd:Q12345 wdt:P31/wdt:P279* ?class .
       SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
     }
     ```
  3. Confirm rate limits and whether a User-Agent header is required (Wikidata blocks requests without it).
  4. Find the Wikidata QIDs for key legal concepts: obligation (likely Q1756864), prohibition, contract, legal norm — search Wikidata for these.
  5. Python usage pattern with `SPARQLWrapper`:
     ```python
     from SPARQLWrapper import SPARQLWrapper, JSON
     sparql = SPARQLWrapper('https://query.wikidata.org/sparql')
     sparql.addCustomHttpHeader('User-Agent', 'ResearchBot/1.0')
     sparql.setQuery(QUERY)
     sparql.setReturnFormat(JSON)
     results = sparql.query().convert()
     ```

  ---

  ### TASK 5: SymBa Empty-DB Invocation Protocol

  **Already known:**
  - Paper: https://aclanthology.org/2025.naacl-long.124/ (arXiv: 2402.12806)
  - GitHub: https://github.com/lbox-kr/symba
  - Key files: `pysolver/solve.py` (main Algorithm 1), `hiereason/symba/_symba.py` (single-statement generation), `data/(dataset)/prompt_data.json` (prompts)
  - Core mechanism: solver calls LLM via `unproved_callback` when a goal cannot be proven
  - Prompt templates stored in `data/(dataset name)/prompt_data.json`

  **Executor tasks:**
  1. Fetch https://arxiv.org/abs/2402.12806 and extract: (a) Algorithm 1 pseudocode describing the SLD loop and LLM callback trigger condition, (b) the exact format of the LLM prompt (what information is passed: goal, context, partial proof tree), (c) how the LLM response (a new rule/fact) is integrated back into the working memory, (d) the termination conditions.
  2. Fetch https://github.com/lbox-kr/symba and read `README.md` for dataset setup instructions and how to run the solver on ProofWriter/CLUTRR.
  3. If possible, fetch the raw content of `pysolver/solve.py` via `https://raw.githubusercontent.com/lbox-kr/symba/main/pysolver/solve.py` to see the actual Python implementation of the SLD-LLM coroutine loop.
  4. Identify: Does SymBa start with a completely empty Prolog KB, or does it load any background KB? Confirm the empty-DB design claim from the hypothesis.
  5. Document the exact LLM API call signature SymBa uses (which model, which format) — this informs how to replace OpenAI calls with OpenRouter in the baseline implementation.

  **Search queries to run:**
  - `site:github.com/lbox-kr/symba solve.py`
  - `SymBa NAACL 2025 algorithm backward chaining LLM callback empty database`

  ---

  ### TASK 6: Dataset Access — ProofWriter D*(OWA)

  **Already known:**
  - HuggingFace: `tasksource/proofwriter` (586k train, 85.5k val, 174k test)
  - Contains D*(OWA) configs with True/False/Unknown answers
  - Configs include: AttNeg-OWA, AttNoneg-OWA, RelNeg-OWA, RelNoneg-OWA variants

  **Executor tasks:**
  1. Fetch https://huggingface.co/datasets/tasksource/proofwriter and extract: (a) exact config names for D*(OWA) — the hypothesis specifies D*(OWA) as primary; confirm the config name string to use in `load_dataset("tasksource/proofwriter", config_name)`, (b) field names in each example (question, context/theory, answer, proof?), (c) whether proof trees are included.
  2. Also check `renma/ProofWriter` and `D3xter1922/proofwriter-dataset` for alternative configs that may better match the original paper's D* dataset.
  3. Confirm whether the original Allen AI ProofWriter dataset is available directly: https://allenai.org/data/proofwriter — fetch and check.
  4. Document the load command:
     ```python
     from datasets import load_dataset
     ds = load_dataset("tasksource/proofwriter", "depth-5-OWA")
     ```
     (Confirm the exact config string.)
  5. Report the number of examples in the D*(OWA) test split specifically, and the label distribution (True/False/Unknown ratios).

  ---

  ### TASK 7: Dataset Access — CLUTRR

  **Already known:**
  - HuggingFace: `CLUTRR/v1` (12,100 train, 3,020 val, 1,050 test)
  - Fields: id, story, query, target (0-20), target_text, proof_state, f_comb, task_name
  - Tasks range from task_1.2 to task_1.10 (number = chain length)
  - Load: `from datasets import load_dataset; ds = load_dataset("CLUTRR/v1")`

  **Executor tasks:**
  1. Fetch https://huggingface.co/datasets/CLUTRR/v1 and extract: (a) the exact 21 kinship relation labels in target_text, (b) what `proof_state` field contains (logical rules? natural language?), (c) whether there are multiple dataset configs/variants.
  2. Confirm that `proof_state` provides the ground-truth logical derivation chain for evaluation of L1 tier.
  3. Check if the GitHub repo https://github.com/facebookresearch/clutrr has additional annotated splits not on HuggingFace.
  4. Document the filter to use for specific chain lengths:
     ```python
     ds_hard = ds['test'].filter(lambda x: x['task_name'].startswith('task_1.5'))
     ```

  ---

  ### TASK 8: Dataset Access — SARA

  **Already known:**
  - GitHub: https://github.com/SgfdDttt/sara
  - Contains Prolog KB files for US federal tax statutes
  - Running Prolog requires SWI-Prolog ≥ 7.2.3
  - `bash code/make_dataset.sh` downloads and formats the dataset
  - Data hosted at https://nlp.jhu.edu/law/ (external)

  **Executor tasks:**
  1. Fetch https://github.com/SgfdDttt/sara and get the complete directory listing. Specifically find: (a) the location of gold Prolog KB files (.pl files), (b) the format of case description files (natural language descriptions of tax scenarios), (c) the annotation format linking cases to ground-truth answers (yes/no entailment).
  2. Fetch the SARA paper (arXiv:2005.05257 or https://aclanthology.org/2020.nllp-1.pdf) to understand: the exact input format for each case, how many annotated cases exist (the hypothesis says ~100+, paper says 376), and the gold Prolog KB structure.
  3. Check if SARA v2 (mentioned in search results) has a different structure — fetch https://aclanthology.org/2023.nllp-1.12.pdf for details.
  4. Identify: Are the case descriptions available as plain text files? What is the average length? (Needed for Phase 0 extraction calibration on 25 randomly sampled cases.)
  5. Document how to load a SARA case description and its gold Prolog facts for Phase 0:
     ```python
     # Target: list of (case_description_text, gold_prolog_facts_list) tuples
     ```

  ---

  ### TASK 9: Dataset Access — ContractNLI

  **Already known:**
  - Official page: https://stanfordnlp.github.io/contract-nli/
  - 607 annotated non-disclosure agreements
  - Labels: entailment, contradiction, neutral + evidence spans
  - Requires agreeing to Terms of Use from Hitachi America Ltd.
  - ArXiv: 2110.01799

  **Executor tasks:**
  1. Fetch https://stanfordnlp.github.io/contract-nli/ and extract: (a) the exact download URL or form to get the dataset files, (b) the file format (JSON? CSV?), (c) the JSON schema with fields for contract text, hypothesis, label, and evidence span.
  2. Check if ContractNLI is available on HuggingFace without the ToU barrier. Search for `contractnli huggingface datasets`.
  3. Fetch the ContractNLI paper https://arxiv.org/abs/2110.01799 abstract to confirm: number of contracts (607), number of hypothesis types (17), and the annotation scheme.
  4. Determine the average contract length in characters — important for understanding whether documents fit within LLM context windows for L0 extraction.
  5. Confirm the annotation format: is each hypothesis labeled per-document (requiring document-level reasoning) or per-sentence?

  **Search queries to run:**
  - `contractnli huggingface dataset 2024`
  - `ContractNLI JSON format schema download`

  ---

  ### TASK 10: Synthesis and Output

  After completing Tasks 1-9, synthesize all findings into `research_out.json` and `research_report.md` with the following structure:

  **research_out.json schema:**
  ```json
  {
    "answer": "Structured technical reference with all integration points",
    "sources": ["list of all URLs consulted"],
    "follow_up_questions": ["any unresolved questions for executor"],
    "integration_points": {
      "lkif_owl": {
        "download_url": "...",
        "raw_github_url": "...",
        "key_classes": ["obligation", "norm", ...],
        "loading_library": "owlready2 or rdflib",
        "loading_code": "...",
        "notes": "..."
      },
      "swi_prolog_bridge": {
        "library": "pyswip",
        "install_cmd": "pip install pyswip",
        "depth_limit_syntax": "call_with_depth_limit(Goal, 3, Result)",
        "pyswip_pattern": "...",
        "version_requirements": "..."
      },
      "conceptnet_api": {
        "base_url": "http://api.conceptnet.io",
        "query_pattern": "...",
        "json_schema": {"edges": [{"start": {}, "end": {}, "rel": {}, "weight": 0.0}]},
        "rate_limits": "3600/hour",
        "python_snippet": "..."
      },
      "wikidata_sparql": {
        "endpoint": "https://query.wikidata.org/sparql",
        "query_pattern": "...",
        "python_snippet": "...",
        "rate_limits": "...",
        "legal_qids": {"obligation": "Q...", ...}
      },
      "symba_baseline": {
        "paper_url": "https://aclanthology.org/2025.naacl-long.124/",
        "github_url": "https://github.com/lbox-kr/symba",
        "empty_db_mechanism": "...",
        "llm_callback_trigger": "...",
        "prompt_template_location": "data/(dataset)/prompt_data.json",
        "key_files": ["pysolver/solve.py", "hiereason/symba/_symba.py"]
      },
      "datasets": {
        "proofwriter_owa": {
          "hf_id": "tasksource/proofwriter",
          "config": "depth-5-OWA (confirm exact string)",
          "load_cmd": "load_dataset('tasksource/proofwriter', 'depth-5-OWA')",
          "test_size": "...",
          "fields": ["question", "theory", "answer", ...]
        },
        "clutrr": {
          "hf_id": "CLUTRR/v1",
          "load_cmd": "load_dataset('CLUTRR/v1')",
          "test_size": 1050,
          "fields": ["story", "query", "target_text", "proof_state", ...]
        },
        "sara": {
          "github_url": "https://github.com/SgfdDttt/sara",
          "data_download_url": "https://nlp.jhu.edu/law/",
          "num_cases": 376,
          "case_format": "...",
          "prolog_kb_location": "..."
        },
        "contractnli": {
          "official_url": "https://stanfordnlp.github.io/contract-nli/",
          "hf_id": "(if available)",
          "num_contracts": 607,
          "json_schema": "...",
          "terms_required": true
        }
      }
    }
  }
  ```

  **research_report.md** should have sections:
  1. Executive Summary (key findings table)
  2. LKIF Core OWL — Availability, Classes, Loading
  3. SWI-Prolog Python Bridge — pyswip Usage, depth_limit Pattern
  4. ConceptNet REST API — URL Patterns, JSON Schema, Rate Limits
  5. Wikidata SPARQL — Endpoint, Query Patterns, Legal Concept QIDs
  6. SymBa Baseline — Algorithm Description, LLM Invocation Protocol
  7. Dataset Access — Per-dataset load instructions and field schemas
  8. Implementation Notes — Known issues, version constraints, authentication requirements
  9. Unresolved Questions — Items requiring executor validation

  ---

  ### IMPORTANT NOTES FOR EXECUTOR

  - **Do not download files** — only document URLs, API patterns, and code snippets
  - **Verify live URLs** — some Estrella project URLs (estrellaproject.org) may be offline; the GitHub mirror is the reliable source
  - **ConceptNet coverage** — test whether legal terms like `obligation`, `prohibition`, `norm` have meaningful ConceptNet edges; report coverage honestly (this is a disconfirmation risk per the hypothesis)
  - **SymBa prompt templates** — fetching the raw JSON from `data/(dataset)/prompt_data.json` in the symba repo is critical for accurate baseline reproduction
  - **ContractNLI ToU** — note the Terms of Use requirement; check if a HuggingFace mirror exists without this barrier
  - **SARA data location** — the `nlp.jhu.edu/law/` URL may require direct fetch to confirm it's live and what files are available
  - **pyswip vs janus** — document both; the executor should choose based on which is pip-installable without SWI-Prolog system dependencies in the container environment
explanation: >-
  This research artifact is the critical prerequisite for the entire pipeline implementation. The executor (a separate code-writing
  agent) cannot begin without knowing: (1) the exact URL to download LKIF Core OWL and which Python library can load it, (2)
  how to call SWI-Prolog from Python with depth-limited resolution, (3) the precise ConceptNet and Wikidata API patterns to
  query L2 ontological facts, (4) SymBa's exact LLM invocation protocol to build a faithful baseline (without which the hallucination
  comparison is invalid), and (5) the dataset IDs and field schemas for all four benchmarks. Missing or wrong integration
  points would cause implementation failures that waste the entire experiment budget. The research is tightly scoped around
  concrete technical specifications — URLs, API schemas, Python code patterns, dataset load commands — not literature review
  or analysis.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
  "properties": {
    "title": {
      "default": "",
      "description": "Descriptive title (roughly 30-90 characters). Must describe content, NOT a status message.",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-15 20:11:56 UTC

```
### Goal

Develop an operational translation pipeline that converts unstructured textual content (e.g., short legal documents, news articles, kids' stories) into a formal first-order logic representation. The output must be capable of (probabilistic) reasoning using a logic reasoner (like Prolog), leveraging LLMs to dynamically resolve terminology, concepts, and relations that are not well defined in the explicit text.

### Reviewer Scope

Limit the technical core to areas the reviewer can deeply evaluate. Other fields are welcome for inspiration but should not host the substantive contribution.

Reviewer-evaluable areas: semantic technologies, logic programming, inductive logic programming, information retrieval, machine learning, LLMs, deep learning, knowledge extraction, knowledge graphs, reasoning, and text data analytics.

The pipeline should ingest a short document (approx. 3000 characters) and parse it into a structured, computable format. Methods may combine an LLM acting as a semantic translation engine (mapping natural text to first-order logic or Prolog predicates), a running logic interpreter (like SWI-Prolog) for symbolic execution, and the integration of upper ontologies like OpenCyc to supply necessary background structure and taxonomic grounding. Furthermore, an LLM should be deployed as a probabilistic reasoning engine to handle fuzzy unifications, semantic similarities, and logical gaps where strict symbolic matching fails due to language ambiguity.

Evaluation must be rigorous and compare the neuro-symbolic pipeline against purely neural baselines (e.g., standard RAG, chain-of-thought prompting) on standard logical reasoning benchmarks (e.g., RuleTaker, CLUTRR) or custom annotated datasets. It must specifically measure: (i) the precision and recall of atomic fact extraction directly from the original document, and (ii) the accuracy of multi-hop fact extraction and logical deductions that require synthesizing explicit document facts with implicit common-sense knowledge.

Outputs must provide human-auditable trace-graphs of the reasoning steps to clearly demonstrate the logical path taken.

Constraints: The pipeline must be highly reproducible on any short, professionally written documents. Inference must be executable on commodity hardware, and the system must report a quantified reduction in hallucination rates compared to raw LLM generation.

### Publication

Target ACL Knowledge Extraction track as the primary venue, with EMNLP or specialized neuro-symbolic AI conference tracks (e.g., NeSy) as fallback targets.

### Things to Avoid

Avoid simplistic propositional logic translations of the text. Avoid purely neural black-box systems that lack interpretable reasoning traces. The substantive contribution must be an operational, hybrid method for reasoning with textual content that explicitly minimizes hallucinations.
```

### [3] SKILL-INPUT — aii-web-tools · 2026-06-15 20:12:18 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: web search (Serper/Google), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — Serper.dev for search, html2text + PyMuPDF for fetch, and
   regex grep over the full document text. They work without any built-in web
   tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (Serper.dev / Google)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
```

Returns ranked title / URL / snippet lines. Use it first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [4] SYSTEM-USER prompt · 2026-06-15 20:23:01 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This research gathered all the concrete technical details needed to build a system that converts text into logical rules and reasons over them — including exact web addresses for legal ontology files, code patterns for running Prolog from Python, API instructions for knowledge graph lookups, and precise commands to load the four benchmark datasets used to test the system.' is too long (at most 250 characters, got 374)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [5] SYSTEM-USER prompt · 2026-06-15 20:23:57 UTC

```
<verification_failed>
Your research output failed verification (attempt 1/10).
</verification_failed>

<schema_errors>
JSON SCHEMA ERRORS:
  - research_out.json: Missing required 'title' field
  - research_out.json: Missing required 'summary' field

Fix: research_out.json must have:
     {
       "answer": "comprehensive answer with [1], [2] citations",
       "sources": [{"index": 1, "url": "...", "title": "...", "summary": "..."}],
       "follow_up_questions": ["Question 1?", "Question 2?"],
       "summary": "what was found"
     }

     Each citation [N] in answer MUST match a source with that index.
</schema_errors>

<content_warnings>
CONTENT ISSUES:
  - research_out.json: 'title' is too short
  - research_out.json: Sources with uncited indices: {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}

Fix: Ensure answer is comprehensive, has proper citations, and all sources are cited.
</content_warnings>

<task>
FIX ISSUES:
1. Output valid research_out.json with all required fields
2. Ensure every factual claim has a numbered citation [1], [2], etc.
3. Ensure every source has a matching citation in the answer
</task>
```
