# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-15 20:12:16 UTC

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

<research_methodology>
Design experiments like a researcher, not a programmer running a script.

- Every method needs a meaningful baseline — the current standard approach, not a strawman.
- Control your variables. When comparing methods, hold everything else constant.
- Results need variance, not just point estimates. A single run proves nothing.
- Implement the proposed method and baseline side-by-side in the same pipeline to eliminate implementation-level confounds.
</research_methodology>

<task>
Implement the research methodology as a production-ready experimental system.
Adapt your implementation approach based on the hypothesis and domain requirements.
</task>

<critical_requirements>
- Fully implement the methodology described in hypothesis
- Use appropriate frameworks based on research domain
- Load and process data from the specified data_filepath
- Complete working systems
- Handle all edge cases, errors, and exceptions properly
- Always implement baseline comparison method
</critical_requirements>

<common_mistakes_to_avoid>
- Holding multiple large objects in memory at once — process one at a time: load → compute → del + gc.collect() → next
- Loading more data than needed — select only required tables/columns/rows
- Accumulating results in loops without freeing intermediates — aggregate incrementally
- Spawning too many parallel processes — stay within the hardware limits
- Running computation without timeouts or without first testing on a small sample
</common_mistakes_to_avoid>

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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: >-
  Provenance-Stratified Neuro-Symbolic Pipeline: L0-L3 Tier-Ordered SLD with SARA/CLUTRR/ProofWriter/ContractNLI Evaluation
summary: >-
  Implement and evaluate a complete 4-tier neuro-symbolic reasoning pipeline (L0 document extraction, L1 bounded SLD, L2 domain-adaptive
  ontology, L3 self-consistency LLM abduction) with weakest-link provenance propagation, against a SymBa-style flat-LLM baseline
  and CoT baseline, across four benchmarks: SARA, ProofWriter D*(OWA), CLUTRR, and ContractNLI.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "## File layout\n```\nmethod.py             # main entrypoint, orchestrates all phases\npipeline/\n\
  \  l0_extractor.py    # LLM-based L0 Prolog predicate extraction\n  l1_prolog.py       # SWI-Prolog interface via pyswip,\
  \ depth-limited SLD\n  l2_ontology.py     # owlready2 LKIF + ConceptNet REST for L2 bridging\n  l3_abduction.py    # K=5\
  \ self-consistency LLM abduction\n  meta_interpreter.py # tier-ordered resolution + weakest-link propagation\n  trace.py\
  \           # JSON-LD derivation tree builder\nbaselines/\n  symba_baseline.py  # empty-KB flat LLM on every proof failure\n\
  \  cot_baseline.py    # chain-of-thought LLM, extract yes/no answer\ndatasets/\n  sara_loader.py     # load SARA from github.com/SgfdDttt/sara\n\
  \  proofwriter_loader.py  # load tasksource/proofwriter from HuggingFace\n  clutrr_loader.py   # load CLUTRR from HuggingFace\
  \ CLUTRR org\n  contractnli_loader.py  # load from stanfordnlp.github.io/contract-nli\nmetrics/\n  hallucination.py   #\
  \ string-match L0 assertions vs source document\n  ece.py             # bucketed ECE for L3 confidence vs binary ground\
  \ truth\n  tier_distribution.py  # fraction of proofs using only L0-L2\nmethod_out.json       # final output\n```\n\n##\
  \ PHASE 0 — SARA Extraction Calibration (must run first, acts as gate)\n\n### Setup\n```python\n# Install: uv add pyswip\
  \ owlready2 requests datasets openai-compatible httpx\n# SWI-Prolog must be installed system-wide: apt-get install swi-prolog\n\
  # Verify: from pyswip import Prolog; p = Prolog(); list(p.query('true'))\n```\n\n### Load SARA\n```python\n# Clone: git\
  \ clone https://github.com/SgfdDttt/sara\n# Repo structure: sara/prolog/ has gold .pl files per case; sara/cases/ has text\
  \ descriptions\n# Load 25 random cases:\nimport glob, random\ncases = glob.glob('sara/cases/*.txt')  # each file is ~3000\
  \ char document\ngold_pls = glob.glob('sara/prolog/*.pl')  # matching gold Prolog KB\n# Pair by filename stem\npaired =\
  \ [(c, c.replace('cases/', 'prolog/').replace('.txt', '.pl')) for c in cases]\nsampled = random.sample(paired, 25)\n```\n\
  \n### L0 Extraction Prompt (use meta-llama/llama-3.1-70b-instruct via OpenRouter)\n```python\nEXTRACTION_PROMPT = '''\n\
  You are a Prolog knowledge engineer. Extract ALL atomic facts from the following legal document as Prolog predicates.\n\
  Rules:\n- Use lowercase snake_case for predicate names and all atom arguments\n- No variables (start with uppercase) in\
  \ extracted facts — only ground atoms\n- Each fact must correspond to something EXPLICITLY stated in the document, not inferred\n\
  - Format each fact as valid Prolog: predicate_name(arg1, arg2, ...) with no spaces inside\nOutput ONLY a JSON array of objects,\
  \ each with keys:\n  {\"predicate\": str, \"args\": [str, ...], \"source_span\": str, \"confidence\": 1.0, \"tier\": \"\
  l0\"}\nDocument:\n{document}\n'''\n```\n\n### Evaluate vs gold\n```python\n# Parse gold .pl file: extract head/1 facts and\
  \ rule heads\n# For precision: fraction of extracted predicates whose string form appears in gold .pl\n# For recall: fraction\
  \ of gold .pl ground facts covered by extracted set\n# Report per-case and aggregate precision/recall\n# GATE: if precision\
  \ < 0.75 across 25 examples:\n#   Iterate with few-shot examples (add 3 gold-annotated examples to prompt)\n#   Re-evaluate;\
  \ if still < 0.75 use constrained JSON + type constraints\n#   Max 3 iterations; log all results; proceed regardless but\
  \ flag\n```\n\n## PHASE 1 — PIPELINE ARCHITECTURE\n\n### L0 Extractor (pipeline/l0_extractor.py)\n```python\nfrom openai\
  \ import OpenAI  # OpenRouter compatible\nimport json, re\n\nclient = OpenAI(base_url='https://openrouter.ai/api/v1', api_key=OPENROUTER_KEY)\n\
  \ndef extract_l0(document: str, domain: str = 'general') -> list[dict]:\n    # Select domain-adapted prompt (add legal examples\
  \ for legal docs)\n    prompt = EXTRACTION_PROMPT.format(document=document[:4000])\n    resp = client.chat.completions.create(\n\
  \        model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': prompt}],\n        temperature=0.0,\
  \ max_tokens=2000\n    )\n    raw = resp.choices[0].message.content\n    # Extract JSON array from response (allow markdown\
  \ code block)\n    match = re.search(r'\\[.*?\\]', raw, re.DOTALL)\n    facts = json.loads(match.group()) if match else\
  \ []\n    # Validate: predicate is valid Prolog atom (lowercase, alphanumeric+underscore)\n    valid = [f for f in facts\
  \ if re.match(r'^[a-z][a-z0-9_]*$', f['predicate'])\n             and all(re.match(r'^[a-z0-9_]+$', a) for a in f['args'])]\n\
  \    return valid  # list of {predicate, args, source_span, confidence:1.0, tier:'l0'}\n```\n\n### L1 Bounded SLD (pipeline/l1_prolog.py)\n\
  ```python\nfrom pyswip import Prolog\n\nclass PrologKB:\n    def __init__(self):\n        self.prolog = Prolog()\n     \
  \   self.facts = []  # list of (predicate, args, tier, conf)\n    \n    def load_l0_facts(self, facts: list[dict]):\n  \
  \      for f in facts:\n            atom = f[\"predicate\"] + '(' + ','.join(f[\"args\"]) + ')'\n            self.prolog.assertz(atom)\n\
  \            self.facts.append((f['predicate'], f['args'], 'l0', 1.0))\n    \n    def load_l0_rules(self, rules: list[str]):\n\
  \        # rules as plain Prolog strings, e.g. 'parent(X,Y) :- father(X,Y)'\n        for r in rules:\n            self.prolog.assertz(r)\n\
  \    \n    def query_with_depth_limit(self, goal: str, depth: int = 3) -> tuple[bool, str]:\n        # SWI-Prolog call_with_depth_limit/3:\n\
  \        # call_with_depth_limit(Goal, Limit, Result)\n        # Result = depth_limit_exceeded | integer (steps used) |\
  \ false\n        query = f'call_with_depth_limit(({goal}), {depth}, Result)'\n        try:\n            solutions = list(self.prolog.query(query))\n\
  \            if solutions and solutions[0].get('Result') != 'depth_limit_exceeded':\n                return True, 'l1'\n\
  \            return False, 'depth_limit_exceeded'\n        except Exception:\n            return False, 'error'\n    \n\
  \    def assert_l1_derived(self, predicate: str, args: list[str]):\n        atom = predicate + '(' + ','.join(args) + ')'\n\
  \        self.prolog.assertz(atom)\n        self.facts.append((predicate, args, 'l1', 1.0))\n```\n\n### L2 Domain-Adaptive\
  \ Ontology (pipeline/l2_ontology.py)\n```python\nimport requests\nfrom owlready2 import get_ontology, onto_path\n\nLKIF_URL\
  \ = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl'\nLKIF_EXTENDED_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-extended.owl'\n\
  \ndef load_lkif() -> object:\n    onto = get_ontology(LKIF_URL)\n    onto.load()\n    return onto\n\ndef query_lkif_subsumption(onto,\
  \ concept_name: str) -> list[str]:\n    # Find class matching concept_name (case-insensitive fuzzy match)\n    matched =\
  \ [c for c in onto.classes() \n               if concept_name.lower() in c.name.lower()]\n    if not matched:\n        return\
  \ []\n    cls = matched[0]\n    # Return all ancestor class names (broader concepts)\n    return [a.name for a in cls.ancestors()\
  \ if a is not cls]\n\ndef query_conceptnet(entity: str, relation: str = 'IsA') -> list[tuple[str, float]]:\n    # ConceptNet\
  \ REST API\n    url = f'https://api.conceptnet.io/query?node=/c/en/{entity}&rel=/r/{relation}&limit=10'\n    resp = requests.get(url,\
  \ timeout=10)\n    if resp.status_code != 200:\n        return []\n    edges = resp.json().get('edges', [])\n    results\
  \ = []\n    for e in edges:\n        end = e.get('end', {}).get('label', '')\n        weight = e.get('weight', 1.0)\n  \
  \      # Normalize: ConceptNet weights typically 1.0-10.0; cap confidence at 0.80\n        conf = min(0.80, weight / 10.0\
  \ + 0.70)\n        results.append((end, conf))\n    return results\n\ndef classify_domain(document: str) -> str:\n    legal_keywords\
  \ = ['contract', 'obligation', 'party', 'law', 'statute',\n                      'agreement', 'liability', 'clause', 'provision',\
  \ 'plaintiff']\n    narrative_keywords = ['story', 'character', 'once upon', 'family', 'village']\n    legal_score = sum(1\
  \ for kw in legal_keywords if kw in document.lower())\n    narrative_score = sum(1 for kw in narrative_keywords if kw in\
  \ document.lower())\n    if legal_score >= 3:\n        return 'legal'\n    elif narrative_score >= 2:\n        return 'narrative'\n\
  \    return 'general'\n\ndef query_l2(goal_predicate: str, goal_args: list[str], domain: str,\n             onto=None) ->\
  \ list[dict]:\n    results = []\n    if domain == 'legal' and onto is not None:\n        # Try to match args against LKIF\
  \ concepts\n        for arg in goal_args:\n            ancestors = query_lkif_subsumption(onto, arg)\n            for anc\
  \ in ancestors:\n                results.append({\n                    'predicate': f'is_a',\n                    'args':\
  \ [arg, anc.lower()],\n                    'tier': 'l2', 'confidence': 0.95,\n                    'source': 'lkif'\n   \
  \             })\n    else:\n        for arg in goal_args:\n            cn_results = query_conceptnet(arg.replace('_', '\
  \ '))\n            for label, conf in cn_results:\n                results.append({\n                    'predicate': 'is_a',\n\
  \                    'args': [arg, label.lower().replace(' ', '_')],\n                    'tier': 'l2', 'confidence': conf,\n\
  \                    'source': 'conceptnet'\n                })\n    return results\n```\n\n### L3 LLM Abduction (pipeline/l3_abduction.py)\n\
  ```python\nABDUCTION_PROMPT = '''\nDocument excerpt:\n{document_excerpt}\n\nQuestion: Based ONLY on the document above,\
  \ does the following hold?\n{predicate}({args})\nAnswer with exactly 'yes' or 'no', followed by one sentence justification.\n\
  '''\n\ndef abduce_l3(predicate: str, args: list[str], document: str,\n              K: int = 5) -> dict:\n    yes_count\
  \ = 0\n    justifications = []\n    for _ in range(K):\n        resp = client.chat.completions.create(\n            model='meta-llama/llama-3.1-70b-instruct',\n\
  \            messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n                document_excerpt=document[:2000],\n\
  \                predicate=predicate,\n                args=', '.join(args)\n            )}],\n            temperature=0.7,\
  \  # slight temperature for sampling diversity\n            max_tokens=100\n        )\n        answer = resp.choices[0].message.content.strip().lower()\n\
  \        if answer.startswith('yes'):\n            yes_count += 1\n        justifications.append(answer)\n    confidence\
  \ = yes_count / K\n    return {\n        'predicate': predicate, 'args': args,\n        'tier': 'l3', 'confidence': confidence,\n\
  \        'low_confidence': confidence < 0.6,\n        'K': K, 'yes_count': yes_count,\n        'justifications': justifications\n\
  \    }\n```\n\n### Meta-Interpreter with Weakest-Link Propagation (pipeline/meta_interpreter.py)\n```python\nTIER_ORDER\
  \ = {'l0': 0, 'l1': 1, 'l2': 2, 'l3': 3, 'unknown': 4}\n\nclass MetaInterpreter:\n    def __init__(self, kb: PrologKB, l2_module,\
  \ l3_module, domain: str,\n                 document: str, lkif_onto=None):\n        self.kb = kb\n        self.l2 = l2_module\n\
  \        self.l3 = l3_module\n        self.domain = domain\n        self.document = document\n        self.lkif_onto = lkif_onto\n\
  \        self.proof_tree = []  # list of nodes for JSON-LD export\n    \n    def propagate(self, premises: list[dict]) ->\
  \ dict:\n        # Weakest-link: tier = max tier (by TIER_ORDER), conf = min conf\n        max_tier = max(premises, key=lambda\
  \ p: TIER_ORDER[p['tier']])['tier']\n        min_conf = min(p['confidence'] for p in premises)\n        return {'tier':\
  \ max_tier, 'confidence': min_conf}\n    \n    def prove(self, predicate: str, args: list[str],\n              depth: int\
  \ = 0) -> dict:\n        goal_str = predicate + '(' + ','.join(args) + ')'\n        node = {'goal': goal_str, 'predicate':\
  \ predicate, 'args': args}\n        \n        # Try L0/L1 via pyswip with depth limit\n        proved, tier = self.kb.query_with_depth_limit(goal_str,\
  \ depth=3)\n        if proved:\n            node.update({'tier': tier, 'confidence': 1.0, 'method': 'sld'})\n          \
  \  self.proof_tree.append(node)\n            return node\n        \n        # Try L2\n        l2_facts = self.l2.query_l2(\n\
  \            predicate, args, self.domain, self.lkif_onto\n        )\n        if l2_facts:\n            best = max(l2_facts,\
  \ key=lambda f: f['confidence'])\n            # Assert into KB for future use\n            self.kb.prolog.assertz(\n   \
  \             best['predicate'] + '(' + ','.join(best['args']) + ')'\n            )\n            node.update(best)\n   \
  \         self.proof_tree.append(node)\n            return node\n        \n        # Try L3\n        if depth <= 2:  # avoid\
  \ L3 in deep sub-proofs\n            l3_result = self.l3.abduce_l3(predicate, args, self.document)\n            if l3_result['confidence']\
  \ >= 0.6:\n                self.kb.prolog.assertz(goal_str)\n                node.update(l3_result)\n            else:\n\
  \                node.update({'tier': 'unknown', 'confidence': 0.0,\n                             'low_confidence': True})\n\
  \            self.proof_tree.append(node)\n            return node\n        \n        node.update({'tier': 'unknown', 'confidence':\
  \ 0.0})\n        self.proof_tree.append(node)\n        return node\n    \n    def get_trace(self) -> list[dict]:\n     \
  \   return self.proof_tree\n```\n\n### JSON-LD Trace Export (pipeline/trace.py)\n```python\ndef build_jsonld(proof_tree:\
  \ list[dict], doc_id: str) -> dict:\n    TIER_COLORS = {'l0': 'green', 'l1': 'yellow', 'l2': 'orange',\n               \
  \    'l3': 'red', 'unknown': 'gray'}\n    nodes = []\n    for i, node in enumerate(proof_tree):\n        nodes.append({\n\
  \            '@id': f'node:{doc_id}:{i}',\n            '@type': 'ProofNode',\n            'predicate': node.get('predicate',\
  \ ''),\n            'args': node.get('args', []),\n            'tier': node.get('tier', 'unknown'),\n            'confidence':\
  \ node.get('confidence', 0.0),\n            'color': TIER_COLORS.get(node.get('tier', 'unknown'), 'gray'),\n           \
  \ 'source_span': node.get('source_span', ''),\n            'method': node.get('method', 'abduction')\n        })\n    return\
  \ {\n        '@context': {'@vocab': 'https://schema.org/'},\n        '@type': 'ProofTrace',\n        'document_id': doc_id,\n\
  \        'nodes': nodes\n    }\n```\n\n## PHASE 2 — BASELINES\n\n### SymBa-style flat baseline (baselines/symba_baseline.py)\n\
  ```python\n# Empty KB; for every proof-failure goal, call LLM once (K=1, no tier routing)\ndef symba_prove(predicate: str,\
  \ args: list[str], document: str,\n                kb: PrologKB) -> dict:\n    proved, _ = kb.query_with_depth_limit(\n\
  \        predicate + '(' + ','.join(args) + ')', depth=3\n    )\n    if proved:\n        return {'tier': 'sld', 'confidence':\
  \ 1.0, 'proved': True}\n    # LLM immediately, no ontology tier\n    resp = client.chat.completions.create(\n        model='meta-llama/llama-3.1-70b-instruct',\n\
  \        messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n            document_excerpt=document[:2000],\n\
  \            predicate=predicate, args=', '.join(args)\n        )}],\n        temperature=0.0, max_tokens=100\n    )\n \
  \   answer = resp.choices[0].message.content.strip().lower()\n    return {'tier': 'llm', 'confidence': 1.0 if answer.startswith('yes')\
  \ else 0.0,\n            'proved': answer.startswith('yes'), 'no_provenance': True}\n```\n\n### CoT baseline (baselines/cot_baseline.py)\n\
  ```python\nCOT_PROMPT = '''\nDocument:\n{document}\n\nQuestion: {question}\nThink step by step, then answer True, False,\
  \ or Unknown.\n'''\ndef cot_answer(document: str, question: str) -> str:\n    resp = client.chat.completions.create(\n \
  \       model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': COT_PROMPT.format(\n \
  \           document=document[:3000], question=question)}],\n        temperature=0.0, max_tokens=500\n    )\n    raw = resp.choices[0].message.content\n\
  \    # Extract final answer\n    for ans in ['True', 'False', 'Unknown']:\n        if ans.lower() in raw.lower().split()[-10:]:\n\
  \            return ans\n    return 'Unknown'\n```\n\n## PHASE 3 — DATASET LOADERS\n\n### ProofWriter (datasets/proofwriter_loader.py)\n\
  ```python\nfrom datasets import load_dataset\ndef load_proofwriter_owa(split='validation', max_examples=200):\n    # Use\
  \ tasksource/proofwriter, filter to OWA (depth_5_owa or depth-5-OWA)\n    ds = load_dataset('tasksource/proofwriter', split=split)\n\
  \    # Filter for D*(OWA) subset with 3-valued answers\n    owa = [ex for ex in ds if ex.get('answer') in ['True','False','Unknown']]\n\
  \    return owa[:max_examples]\n    # Each example: {'context': str, 'question': str, 'answer': 'True'|'False'|'Unknown'}\n\
  \    # context is a short theory (facts + rules as natural language sentences)\n    # question is the query sentence\n```\n\
  \n### CLUTRR (datasets/clutrr_loader.py)\n```python\nfrom datasets import load_dataset\ndef load_clutrr(split='test', max_examples=200):\n\
  \    ds = load_dataset('CLUTRR/v1', split=split)  # or specific config\n    # Each: {'story': str, 'query': [entity1, entity2],\
  \ 'target_text': str}\n    return list(ds)[:max_examples]\n```\n\n### SARA (datasets/sara_loader.py)\n```python\nimport\
  \ os, glob\ndef load_sara(sara_dir='sara', max_examples=50):\n    cases = []\n    for txt_file in glob.glob(os.path.join(sara_dir,\
  \ 'cases', '*.txt')):\n        stem = os.path.splitext(os.path.basename(txt_file))[0]\n        pl_file = os.path.join(sara_dir,\
  \ 'prolog', stem + '.pl')\n        if os.path.exists(pl_file):\n            cases.append({\n                'id': stem,\n\
  \                'document': open(txt_file).read(),\n                'gold_prolog': open(pl_file).read(),\n            \
  \    'answer': 'entailed'  # determine from .pl query result\n            })\n    return cases[:max_examples]\n```\n\n###\
  \ ContractNLI (datasets/contractnli_loader.py)\n```python\nimport json\ndef load_contractnli(data_dir='contract-nli', split='test',\
  \ max_contracts=50):\n    # Download from stanfordnlp.github.io/contract-nli/\n    # JSON format: {documents: [{text, annotation_sets:\
  \ [{annotations: {nda-1: {choice, spans}}}]}]}\n    with open(os.path.join(data_dir, f'{split}.json')) as f:\n        data\
  \ = json.load(f)\n    examples = []\n    for doc in data['documents'][:max_contracts]:\n        text = doc['text']\n   \
  \     for ann_set in doc.get('annotation_sets', []):\n            for hyp_id, ann in ann_set.get('annotations', {}).items():\n\
  \                examples.append({\n                    'document': text[:3000],\n                    'hypothesis': hyp_id,\n\
  \                    'label': ann['choice'],  # 'Entailment'|'Contradiction'|'NotMentioned'\n                    'evidence_spans':\
  \ ann.get('spans', [])\n                })\n    return examples\n```\n\n## PHASE 4 — METRICS\n\n### Hallucination Rate (metrics/hallucination.py)\n\
  ```python\ndef compute_hallucination_rate(proof_trees: list[list[dict]],\n                               documents: list[str])\
  \ -> float:\n    # For each L0-tier fact in the proof tree, check if predicate string\n    # or its args appear literally\
  \ in the source document\n    hallucinated = 0\n    total_l0 = 0\n    for tree, doc in zip(proof_trees, documents):\n  \
  \      doc_lower = doc.lower()\n        for node in tree:\n            if node.get('tier') == 'l0':\n                total_l0\
  \ += 1\n                fact_str = node.get('predicate', '') + ' ' + ' '.join(node.get('args', []))\n                # Check\
  \ if any arg or predicate keyword appears in doc\n                args_in_doc = any(arg.replace('_', ' ') in doc_lower\n\
  \                                  for arg in node.get('args', []))\n                if not args_in_doc:\n             \
  \       hallucinated += 1\n    return hallucinated / total_l0 if total_l0 > 0 else 0.0\n```\n\n### ECE (metrics/ece.py)\n\
  ```python\nimport numpy as np\ndef compute_ece(confidences: list[float], labels: list[int],\n                n_bins: int\
  \ = 10) -> float:\n    bins = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    n = len(confidences)\n    for b in range(n_bins):\n\
  \        lo, hi = bins[b], bins[b+1]\n        mask = [(lo <= c < hi) for c in confidences]\n        if not any(mask):\n\
  \            continue\n        bin_confs = [c for c, m in zip(confidences, mask) if m]\n        bin_labels = [l for l, m\
  \ in zip(labels, mask) if m]\n        avg_conf = np.mean(bin_confs)\n        frac_pos = np.mean(bin_labels)\n        ece\
  \ += (len(bin_confs) / n) * abs(avg_conf - frac_pos)\n    return ece\n```\n\n## PHASE 5 — MAIN ORCHESTRATION (method.py)\n\
  ```python\nimport json, time, os\nfrom pipeline.l0_extractor import extract_l0\nfrom pipeline.l1_prolog import PrologKB\n\
  from pipeline import l2_ontology, l3_abduction\nfrom pipeline.meta_interpreter import MetaInterpreter\nfrom pipeline.trace\
  \ import build_jsonld\nfrom baselines.symba_baseline import symba_prove\nfrom baselines.cot_baseline import cot_answer\n\
  from datasets.sara_loader import load_sara\nfrom datasets.proofwriter_loader import load_proofwriter_owa\nfrom datasets.clutrr_loader\
  \ import load_clutrr\nfrom datasets.contractnli_loader import load_contractnli\nfrom metrics.hallucination import compute_hallucination_rate\n\
  from metrics.ece import compute_ece\n\nRESULTS = {'phase0': {}, 'per_example': [], 'aggregates': {}}\nTOTAL_COST = 0.0 \
  \ # track OpenRouter spend\nCOST_LIMIT = 9.0  # hard stop before $10\n\n# Llama-3.1-70b pricing: ~$0.35/M input, $0.40/M\
  \ output tokens (check current)\n# K=5 abduction calls per unresolved goal: budget conservatively\n\ndef estimate_cost(n_tokens_in:\
  \ int, n_tokens_out: int) -> float:\n    return (n_tokens_in / 1e6) * 0.35 + (n_tokens_out / 1e6) * 0.40\n\ndef check_budget():\n\
  \    global TOTAL_COST\n    if TOTAL_COST >= COST_LIMIT:\n        raise RuntimeError(f'Budget exceeded: ${TOTAL_COST:.2f}')\n\
  \n## PHASE 0: Run extraction calibration on 25 SARA examples\n# ... (see above)\n# Report precision/recall; gate check\n\
  \n## MINI SCALE (10% of each benchmark, run first)\n# ProofWriter: 200 examples OWA → use 20 for mini\n# CLUTRR: 200 examples\
  \ → use 20 for mini\n# SARA: 50 → use 10 for mini\n# ContractNLI: 50 contracts → use 5 for mini\n\n## For each example in\
  \ each benchmark:\n#   1. Extract L0 facts (l0_extractor)\n#   2. Load into PrologKB\n#   3. Run meta_interpreter.prove()\
  \ for the benchmark's query goal\n#   4. Also run symba_baseline and cot_baseline on same example\n#   5. Store per-example\
  \ results: {id, benchmark, answer_gold, \n#      answer_stratified, answer_symba, answer_cot,\n#      tier_used, confidence,\
  \ proof_tree_jsonld}\n\n## After all examples:\n#   1. Multi-hop accuracy per baseline per benchmark (exact match)\n#  \
  \ 2. Hallucination rates for stratified vs symba\n#   3. Tier distribution: fraction using only L0-L2\n#   4. ECE on SARA\
  \ L3 confidences vs binary entailment labels\n#   5. Write method_out.json\n\nif __name__ == '__main__':\n    # Load LKIF\
  \ once\n    lkif_onto = l2_ontology.load_lkif()\n    \n    all_results = []\n    \n    for benchmark, loader_fn in [\n \
  \       ('sara', load_sara),\n        ('proofwriter_owa', load_proofwriter_owa),\n        ('clutrr', load_clutrr),\n   \
  \     ('contractnli', load_contractnli)\n    ]:\n        examples = loader_fn()  # starts with mini (10%)\n        for ex\
  \ in examples:\n            check_budget()\n            document = ex['document']\n            domain = l2_ontology.classify_domain(document)\n\
  \            \n            # Stratified pipeline\n            kb = PrologKB()\n            l0_facts = extract_l0(document,\
  \ domain)\n            kb.load_l0_facts(l0_facts)\n            interp = MetaInterpreter(kb, l2_ontology, l3_abduction,\n\
  \                                     domain, document, lkif_onto)\n            goal_pred, goal_args = parse_query(ex) \
  \ # benchmark-specific\n            result_node = interp.prove(goal_pred, goal_args)\n            trace = build_jsonld(interp.get_trace(),\
  \ ex['id'])\n            \n            # SymBa baseline\n            symba_kb = PrologKB()  # empty KB\n            symba_result\
  \ = symba_prove(goal_pred, goal_args, document, symba_kb)\n            \n            # CoT baseline\n            cot_result\
  \ = cot_answer(document, ex.get('question', str((goal_pred, goal_args))))\n            \n            all_results.append({\n\
  \                'id': ex['id'], 'benchmark': benchmark,\n                'gold': ex['answer'],\n                'stratified':\
  \ node_to_answer(result_node),\n                'symba': symba_result['proved'],\n                'cot': cot_result,\n \
  \               'tier_used': result_node['tier'],\n                'confidence': result_node['confidence'],\n          \
  \      'l0_facts_count': len(l0_facts),\n                'proof_tree': trace\n            })\n    \n    # Aggregate metrics\n\
  \    aggregates = {}\n    for bm in ['sara', 'proofwriter_owa', 'clutrr', 'contractnli']:\n        bm_results = [r for r\
  \ in all_results if r['benchmark'] == bm]\n        aggregates[bm] = {\n            'accuracy_stratified': mean(r['gold']\
  \ == r['stratified'] for r in bm_results),\n            'accuracy_symba': mean(r['gold'] == str(r['symba']) for r in bm_results),\n\
  \            'accuracy_cot': mean(r['gold'] == r['cot'] for r in bm_results),\n            'hallucination_rate_stratified':\
  \ compute_hallucination_rate(\n                [r['proof_tree']['nodes'] for r in bm_results],\n                [get_doc(r)\
  \ for r in bm_results]\n            ),\n            'tier_l0l1l2_fraction': mean(r['tier_used'] in ['l0','l1','l2'] for\
  \ r in bm_results),\n            'n_examples': len(bm_results)\n        }\n    \n    # ECE on SARA\n    sara_l3 = [r for\
  \ r in all_results if r['benchmark'] == 'sara' and r['tier_used'] == 'l3']\n    if sara_l3:\n        aggregates['ece_sara_l3']\
  \ = compute_ece(\n            [r['confidence'] for r in sara_l3],\n            [1 if r['gold'] == 'entailed' else 0 for\
  \ r in sara_l3]\n        )\n    \n    output = {\n        'phase0_extraction_calibration': RESULTS['phase0'],\n        'per_example_results':\
  \ all_results,\n        'aggregate_metrics': aggregates,\n        'total_cost_usd': TOTAL_COST\n    }\n    with open('method_out.json',\
  \ 'w') as f:\n        json.dump(output, f, indent=2)\n    print('Done. method_out.json written.')\n```\n\n## SCALING STRATEGY\n\
  1. Run on 10% (mini) first; if all benchmarks complete in < 2h and cost < $3, scale to 50%\n2. If 50% completes in < 4h\
  \ and cost < $6, scale to 100%\n3. Use multiprocessing.Pool for parallel example processing within each benchmark (4 workers)\n\
  4. Cache L0 extraction results to disk (JSON) to avoid re-calling LLM on restarts\n5. Cache LKIF subclass queries to a dict;\
  \ don't reload ontology per example\n6. For L3, only call K=5 on SARA (where ECE is measured); use K=3 on others to save\
  \ cost\n"
fallback_plan: |
  ## Fallback scenarios and mitigations

  ### F1: pyswip / SWI-Prolog integration fails
  - Fallback: Replace pyswip with subprocess calls to swipl binary using `timeout 5 swipl -g 'call_with_depth_limit(Goal,3,R),write(R),halt' -t halt`
  - Parse stdout for result
  - Implement KB as a .pl file written to /tmp, loaded per query

  ### F2: LKIF OWL file fails to load via owlready2 (import errors on OWL-DL axioms)
  - Fallback: Use owlready2 with `world.as_rdflib_graph()` and SPARQL queries instead of Python object API
  - If owlready2 fails entirely: parse lkif-core.owl as XML, extract rdfs:subClassOf triples manually using lxml
  - Emergency fallback: use a hardcoded dict of 50 key LKIF legal concepts and their superclasses

  ### F3: Phase 0 SARA extraction precision < 0.75
  - First iteration: add 3 gold-annotated SARA examples as few-shot to the extraction prompt
  - Second iteration: switch to constrained JSON output with `response_format={type:'json_object'}` and a schema that enforces valid Prolog atom patterns
  - Third iteration: use a stronger model (deepseek/deepseek-r1 or google/gemma-3-27b-it) for extraction only
  - Document all iteration results regardless; proceed with best achieved precision

  ### F4: CLUTRR or ProofWriter D*(OWA) HuggingFace load fails
  - CLUTRR: try `load_dataset('clutrr', 'v1.1')` then fallback to direct download from original GitHub (https://github.com/facebookresearch/clutrr)
  - ProofWriter: try all three HF repos (tasksource/proofwriter, D3xter1922/proofwriter-dataset, renma/ProofWriter); if all fail, use the Allen AI release directly from https://aristo-public-data.s3-us-west-2.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip
  - ContractNLI: download from stanfordnlp.github.io/contract-nli/ directly via requests

  ### F5: Cost approaching $10 limit before all benchmarks complete
  - Priority order: SARA (Phase 0 gate + hallucination) > ProofWriter OWA (multi-hop accuracy) > CLUTRR > ContractNLI
  - Reduce K from 5 to 3 for L3 abduction on lower-priority benchmarks
  - Switch L0 extraction model to meta-llama/llama-3.1-8b-instruct (much cheaper, ~10x cheaper per token)
  - Reduce mini scale to 5% (10 examples per benchmark) if needed

  ### F6: Prolog depth_limit produces incorrect results or pyswip segfaults
  - Fallback: implement a pure Python DFS SLD solver with explicit depth counter
  - Represent KB as a dict: predicate_name -> list of (args, tier, conf)
  - Only handles datalog-style rules (no function symbols, no cuts)
  - Sufficient for L0 fact lookup and simple 2-3 step chain deduction

  ### F7: ConceptNet API rate-limits or is unreachable
  - Fallback: use a locally cached ConceptNet Lite (https://github.com/commonsense/conceptnet-lite) if pip-installable
  - Emergency fallback: use Wikidata SPARQL endpoint for all non-legal domains:
    `https://query.wikidata.org/sparql?query=SELECT ?classLabel WHERE { wd:Q{entity_id} wdt:P31/wdt:P279* ?class . SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } } LIMIT 10`
testing_plan: |-
  ## Testing Strategy

  ### Step 1: Environment validation (run first, < 5 min)
  ```bash
  # Verify SWI-Prolog installed
  swipl --version
  # Verify pyswip works
  python3 -c "from pyswip import Prolog; p=Prolog(); list(p.query('member(X,[1,2,3])'))"
  # Verify owlready2
  python3 -c "from owlready2 import get_ontology; print('owlready2 ok')"
  # Verify OpenRouter key works
  curl -H 'Authorization: Bearer $OPENROUTER_KEY' https://openrouter.ai/api/v1/models | head -5
  # Verify call_with_depth_limit
  python3 -c "
  from pyswip import Prolog
  p = Prolog()
  p.assertz('parent(tom,bob)')
  p.assertz('parent(bob,ann)')
  p.assertz('ancestor(X,Y) :- parent(X,Y)')
  p.assertz('ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y)')
  result = list(p.query('call_with_depth_limit(ancestor(tom,ann), 5, R)'))
  print('depth_limit test:', result)  # should find solution
  "
  ```

  ### Step 2: L0 extraction smoke test (3 examples, < 10 min)
  - Load 3 SARA cases, run extraction prompt, verify:
    a. Output is valid JSON array
    b. Predicates match regex `^[a-z][a-z0-9_]*$`
    c. At least 2 predicates extracted per document
    d. No uppercase variable names in args
  - If any fail: debug extraction prompt before Phase 0

  ### Step 3: Phase 0 on 25 SARA examples (~ 20-30 min)
  - Run extraction on all 25 sampled cases
  - Compute precision/recall against gold .pl annotations
  - CONFIRM: precision >= 0.75 before proceeding
  - Log per-case results; note cases where extraction fails entirely

  ### Step 4: End-to-end mini pipeline test (5 ProofWriter OWA examples, < 15 min)
  - Run full stratified pipeline + both baselines on 5 ProofWriter examples
  - Verify: method_out.json is written with correct schema
  - Verify: proof trees are non-empty for at least 3/5 examples
  - Verify: tier distribution shows at least some L0 facts (not all L3)
  - Verify: cost tracking is working (TOTAL_COST > 0 and < $0.50 for 5 examples)

  ### Step 5: LKIF ontology integration test
  - Load LKIF OWL; query ancestors of class 'Obligation'
  - Expected: returns ['Normative_thing', 'Qualified_norm', 'Norm', ...] (any non-empty list)
  - If empty: check that lkif-core.owl was downloaded successfully and has class definitions

  ### Step 6: Mini benchmark run (10% scale, ~1-2h)
  - Run all 4 benchmarks at 10% scale (20/20/10/5 examples)
  - Check: no crashes, results for all examples, metrics computable
  - Check: total cost < $2.00 for mini run
  - Decision: if runtime < 90 min and cost < $2, scale to 50%; else stay at 10% and report

  ### Step 7: Final validation of method_out.json
  - Verify JSON is valid and parseable
  - Verify top-level keys: phase0_extraction_calibration, per_example_results, aggregate_metrics, total_cost_usd
  - Verify per_example has required fields: id, benchmark, gold, stratified, symba, cot, tier_used, confidence
  - Verify aggregate_metrics has accuracy for all 3 systems on all 4 benchmarks
  - Apply aii-json skill to validate against expected schema

  ### Confirmation signals before full scale
  - Phase 0 precision >= 0.75 (HARD gate)
  - Mini pipeline produces non-trivial tier distribution (not 100% L3)
  - SymBa baseline produces non-trivially different results from stratified (if identical, check bug)
  - Cost per example < $0.10 (to stay within budget for 100+ examples)

  ### Known failure modes to watch for
  - pyswip segfault under multiprocessing (use spawn not fork; or run Prolog in subprocess)
  - owlready2 loading OWL-DL axioms with imports (some LKIF owl files import others; set onto_path to local dir)
  - OpenRouter rate limits: add time.sleep(0.5) between L3 calls; implement exponential backoff
  - CLUTRR data format varies by version: check field names before assuming story/query/target_text keys
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [2] HUMAN-USER prompt · 2026-06-15 20:12:16 UTC

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

### [3] SKILL-INPUT — aii-python · 2026-06-15 20:12:38 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-06-15 20:12:38 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-06-15 20:12:38 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-06-15 20:12:46 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-06-15 20:12:46 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-06-15 20:12:46 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SKILL-INPUT — aii-openrouter-llms · 2026-06-15 20:13:30 UTC

The agent loaded the **aii-openrouter-llms** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-openrouter-llms
description: Searches and calls LLMs from OpenRouter's extensive catalog (Claude, GPT, Gemini, Llama, Mistral, DeepSeek, etc.) with reasoning and temperature control. Use when user needs to access various LLMs, compare language models, call different model providers, find the best model for a task, or look up model pricing and costs per million tokens.
---

## Contents

- Workflow (2-phase model discovery and calling)
- Scripts (Search, Get Params, Call)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: Model Discovery and Calling

### Phase 1: Search for Models
Find models with pricing, context length, and descriptions
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

### Phase 2 (optional): Get Model Parameters
Check what parameters a specific model supports
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

### Phase 3: Call Model
Call a model using the API name from search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

---

## Scripts

### Search OpenRouter models (aii_or_search_llms.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_search_llms.py "claude" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_search_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 5' ::: 'claude' 'gpt' 'gemini'
```

**Example output:**
```
Found 5 models for query: claude

[1] Anthropic: Claude Opus 4.5
    API: anthropic/claude-opus-4.5
    Context: 200,000 tokens
    Price: $5.00/M in, $25.00/M out
    Claude Opus 4.5 is Anthropic's frontier reasoning model...

[2] Anthropic: Claude Haiku 4.5
    API: anthropic/claude-haiku-4.5
    Context: 200,000 tokens
    Price: $1.00/M in, $5.00/M out
    ...
```

**Parameters:**

`query` (optional, positional)
- Search query to filter models (e.g., 'claude', 'gpt', 'reasoning')

`--limit, -n` (optional)
- Maximum number of results (default: 10)

`--series, -s` (optional)
- Filter by model family
- Valid: GPT, Claude, Gemini, Grok, Cohere, Nova, Qwen, Yi, DeepSeek, Mistral, Llama2, Llama3, Llama4, RWKV, Qwen3, Router, Media, Other, PaLM

`--timeout` (optional)
- Request timeout in seconds (default: 60)

**Tips:**
- Use the `API` field from results for the `--model` parameter in calls
- Search is fast (queries OpenRouter's model list)

---

### Get model parameters (aii_or_get_llm_params.py)

Get detailed information and supported parameters for a specific model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "anthropic/claude-haiku-4.5"
```

**Parallel execution (multiple models):**

IMPORTANT: When checking multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_get_llm_params.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: Anthropic: Claude Haiku 4.5
API: anthropic/claude-haiku-4.5

=== Capabilities ===
Context Length: 200,000 tokens
Max Output: 64,000 tokens
Modality: text+image->text
Input: image, text
Output: text
Moderated: Yes

=== Pricing ===
Input: $1.0000/M tokens
Output: $5.0000/M tokens

=== Supported Parameters ===
  - include_reasoning
  - max_tokens
  - reasoning
  - stop
  - temperature
  - tool_choice
  - tools
  - top_k
  - top_p
```

**Parameters:**

`model` (required, positional)
- Model API name (e.g., 'anthropic/claude-haiku-4.5', 'openai/o1')

`--timeout` (optional)
- Request timeout in seconds (default: 30)

**Tips:**
- Use after search to see which parameters a model supports
- Check supported_parameters before using --reasoning or other options

---

### Call OpenRouter model (aii_or_call_llms.py)

Make an API call to an OpenRouter LLM model.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py --model "anthropic/claude-haiku-4.5" --input "What is 2+2?"
```

**Parallel execution (multiple calls):**

IMPORTANT: When calling multiple models, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_or_call_llms.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --model {} --input "What is 2+2?"' ::: 'anthropic/claude-haiku-4.5' 'openai/gpt-4o-mini' 'google/gemini-2.0-flash-001'
```

**Example output:**
```
Model: anthropic/claude-haiku-4.5

Response:
Four.

Tokens: 12 in, 5 out
```

**Parameters:**

`--model, -m` (required)
- API model name from search results (format: `provider/model-name`)
- Examples: `anthropic/claude-sonnet-4`, `openai/gpt-5`, `google/gemini-2.5-pro`

`--input, -i` (required, unless using --input-json)
- Simple string prompt

`--input-json` (optional)
- Full conversation JSON for multi-turn (mutually exclusive with --input)

`--max-tokens` (optional)
- Maximum output tokens (default: 9000)

`--reasoning` (optional)
- Reasoning effort for reasoning models: `minimal`, `low`, `medium`, `high`

`--temperature, -t` (optional)
- Randomness (0.0-2.0): 0.0=deterministic, 0.7=balanced, 1.5+=creative

`--top-p` (optional)
- Nucleus sampling (0.0-1.0)

`--instructions` (optional)
- System instructions/prompt

`--web-search` (optional)
- Enable web search with max results (e.g., 10)

`--params, -p` (optional)
- Extra model-specific parameters as JSON string
- Use `aii_or_get_llm_params.py` to see which params a model supports
- Example: `--params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'`

`--timeout` (optional)
- Request timeout in seconds (default: 120)

**Examples:**

Simple call:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "Write a haiku about coding" \
  --temperature 0.8
```

With system instructions:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-haiku-4.5" \
  --input "Explain recursion" \
  --instructions "You are a helpful programming tutor. Keep explanations concise."
```

With reasoning (for o1-style models):
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "openai/o1" \
  --input "Solve this complex math problem" \
  --reasoning high
```

With web search:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "anthropic/claude-sonnet-4" \
  --input "What are the latest AI news?" \
  --web-search 10 \
  --max-tokens 15000
```

With extra model-specific params:
```bash
# Step 1: Check what params the model supports
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_get_llm_params.py "meta-llama/llama-3.3-70b-instruct"
# Shows: frequency_penalty, top_k, seed, min_p, etc.

# Step 2: Call with those params
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-openrouter-llms" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_or_call_llms.py \
  --model "meta-llama/llama-3.3-70b-instruct" \
  --input "Write a short poem" \
  --params '{"top_k": 50, "seed": 42, "frequency_penalty": 0.5}'
```

---

## Tips

- Use `aii_or_search_llms.py` first to find models, then copy `API` field for `--model`
- Use `aii_or_get_llm_params.py` to check what params a model supports before using `--params`
- For web search, increase `--max-tokens` to handle larger responses (15000+)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [10] SYSTEM-USER prompt · 2026-06-15 20:25:32 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
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
id: gen_plan_experiment_1_idx3
type: experiment
title: >-
  Provenance-Stratified Neuro-Symbolic Pipeline: L0-L3 Tier-Ordered SLD with SARA/CLUTRR/ProofWriter/ContractNLI Evaluation
summary: >-
  Implement and evaluate a complete 4-tier neuro-symbolic reasoning pipeline (L0 document extraction, L1 bounded SLD, L2 domain-adaptive
  ontology, L3 self-consistency LLM abduction) with weakest-link provenance propagation, against a SymBa-style flat-LLM baseline
  and CoT baseline, across four benchmarks: SARA, ProofWriter D*(OWA), CLUTRR, and ContractNLI.
runpod_compute_profile: cpu_heavy
implementation_pseudocode: "## File layout\n```\nmethod.py             # main entrypoint, orchestrates all phases\npipeline/\n\
  \  l0_extractor.py    # LLM-based L0 Prolog predicate extraction\n  l1_prolog.py       # SWI-Prolog interface via pyswip,\
  \ depth-limited SLD\n  l2_ontology.py     # owlready2 LKIF + ConceptNet REST for L2 bridging\n  l3_abduction.py    # K=5\
  \ self-consistency LLM abduction\n  meta_interpreter.py # tier-ordered resolution + weakest-link propagation\n  trace.py\
  \           # JSON-LD derivation tree builder\nbaselines/\n  symba_baseline.py  # empty-KB flat LLM on every proof failure\n\
  \  cot_baseline.py    # chain-of-thought LLM, extract yes/no answer\ndatasets/\n  sara_loader.py     # load SARA from github.com/SgfdDttt/sara\n\
  \  proofwriter_loader.py  # load tasksource/proofwriter from HuggingFace\n  clutrr_loader.py   # load CLUTRR from HuggingFace\
  \ CLUTRR org\n  contractnli_loader.py  # load from stanfordnlp.github.io/contract-nli\nmetrics/\n  hallucination.py   #\
  \ string-match L0 assertions vs source document\n  ece.py             # bucketed ECE for L3 confidence vs binary ground\
  \ truth\n  tier_distribution.py  # fraction of proofs using only L0-L2\nmethod_out.json       # final output\n```\n\n##\
  \ PHASE 0 — SARA Extraction Calibration (must run first, acts as gate)\n\n### Setup\n```python\n# Install: uv add pyswip\
  \ owlready2 requests datasets openai-compatible httpx\n# SWI-Prolog must be installed system-wide: apt-get install swi-prolog\n\
  # Verify: from pyswip import Prolog; p = Prolog(); list(p.query('true'))\n```\n\n### Load SARA\n```python\n# Clone: git\
  \ clone https://github.com/SgfdDttt/sara\n# Repo structure: sara/prolog/ has gold .pl files per case; sara/cases/ has text\
  \ descriptions\n# Load 25 random cases:\nimport glob, random\ncases = glob.glob('sara/cases/*.txt')  # each file is ~3000\
  \ char document\ngold_pls = glob.glob('sara/prolog/*.pl')  # matching gold Prolog KB\n# Pair by filename stem\npaired =\
  \ [(c, c.replace('cases/', 'prolog/').replace('.txt', '.pl')) for c in cases]\nsampled = random.sample(paired, 25)\n```\n\
  \n### L0 Extraction Prompt (use meta-llama/llama-3.1-70b-instruct via OpenRouter)\n```python\nEXTRACTION_PROMPT = '''\n\
  You are a Prolog knowledge engineer. Extract ALL atomic facts from the following legal document as Prolog predicates.\n\
  Rules:\n- Use lowercase snake_case for predicate names and all atom arguments\n- No variables (start with uppercase) in\
  \ extracted facts — only ground atoms\n- Each fact must correspond to something EXPLICITLY stated in the document, not inferred\n\
  - Format each fact as valid Prolog: predicate_name(arg1, arg2, ...) with no spaces inside\nOutput ONLY a JSON array of objects,\
  \ each with keys:\n  {\"predicate\": str, \"args\": [str, ...], \"source_span\": str, \"confidence\": 1.0, \"tier\": \"\
  l0\"}\nDocument:\n{document}\n'''\n```\n\n### Evaluate vs gold\n```python\n# Parse gold .pl file: extract head/1 facts and\
  \ rule heads\n# For precision: fraction of extracted predicates whose string form appears in gold .pl\n# For recall: fraction\
  \ of gold .pl ground facts covered by extracted set\n# Report per-case and aggregate precision/recall\n# GATE: if precision\
  \ < 0.75 across 25 examples:\n#   Iterate with few-shot examples (add 3 gold-annotated examples to prompt)\n#   Re-evaluate;\
  \ if still < 0.75 use constrained JSON + type constraints\n#   Max 3 iterations; log all results; proceed regardless but\
  \ flag\n```\n\n## PHASE 1 — PIPELINE ARCHITECTURE\n\n### L0 Extractor (pipeline/l0_extractor.py)\n```python\nfrom openai\
  \ import OpenAI  # OpenRouter compatible\nimport json, re\n\nclient = OpenAI(base_url='https://openrouter.ai/api/v1', api_key=OPENROUTER_KEY)\n\
  \ndef extract_l0(document: str, domain: str = 'general') -> list[dict]:\n    # Select domain-adapted prompt (add legal examples\
  \ for legal docs)\n    prompt = EXTRACTION_PROMPT.format(document=document[:4000])\n    resp = client.chat.completions.create(\n\
  \        model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': prompt}],\n        temperature=0.0,\
  \ max_tokens=2000\n    )\n    raw = resp.choices[0].message.content\n    # Extract JSON array from response (allow markdown\
  \ code block)\n    match = re.search(r'\\[.*?\\]', raw, re.DOTALL)\n    facts = json.loads(match.group()) if match else\
  \ []\n    # Validate: predicate is valid Prolog atom (lowercase, alphanumeric+underscore)\n    valid = [f for f in facts\
  \ if re.match(r'^[a-z][a-z0-9_]*$', f['predicate'])\n             and all(re.match(r'^[a-z0-9_]+$', a) for a in f['args'])]\n\
  \    return valid  # list of {predicate, args, source_span, confidence:1.0, tier:'l0'}\n```\n\n### L1 Bounded SLD (pipeline/l1_prolog.py)\n\
  ```python\nfrom pyswip import Prolog\n\nclass PrologKB:\n    def __init__(self):\n        self.prolog = Prolog()\n     \
  \   self.facts = []  # list of (predicate, args, tier, conf)\n    \n    def load_l0_facts(self, facts: list[dict]):\n  \
  \      for f in facts:\n            atom = f[\"predicate\"] + '(' + ','.join(f[\"args\"]) + ')'\n            self.prolog.assertz(atom)\n\
  \            self.facts.append((f['predicate'], f['args'], 'l0', 1.0))\n    \n    def load_l0_rules(self, rules: list[str]):\n\
  \        # rules as plain Prolog strings, e.g. 'parent(X,Y) :- father(X,Y)'\n        for r in rules:\n            self.prolog.assertz(r)\n\
  \    \n    def query_with_depth_limit(self, goal: str, depth: int = 3) -> tuple[bool, str]:\n        # SWI-Prolog call_with_depth_limit/3:\n\
  \        # call_with_depth_limit(Goal, Limit, Result)\n        # Result = depth_limit_exceeded | integer (steps used) |\
  \ false\n        query = f'call_with_depth_limit(({goal}), {depth}, Result)'\n        try:\n            solutions = list(self.prolog.query(query))\n\
  \            if solutions and solutions[0].get('Result') != 'depth_limit_exceeded':\n                return True, 'l1'\n\
  \            return False, 'depth_limit_exceeded'\n        except Exception:\n            return False, 'error'\n    \n\
  \    def assert_l1_derived(self, predicate: str, args: list[str]):\n        atom = predicate + '(' + ','.join(args) + ')'\n\
  \        self.prolog.assertz(atom)\n        self.facts.append((predicate, args, 'l1', 1.0))\n```\n\n### L2 Domain-Adaptive\
  \ Ontology (pipeline/l2_ontology.py)\n```python\nimport requests\nfrom owlready2 import get_ontology, onto_path\n\nLKIF_URL\
  \ = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl'\nLKIF_EXTENDED_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-extended.owl'\n\
  \ndef load_lkif() -> object:\n    onto = get_ontology(LKIF_URL)\n    onto.load()\n    return onto\n\ndef query_lkif_subsumption(onto,\
  \ concept_name: str) -> list[str]:\n    # Find class matching concept_name (case-insensitive fuzzy match)\n    matched =\
  \ [c for c in onto.classes() \n               if concept_name.lower() in c.name.lower()]\n    if not matched:\n        return\
  \ []\n    cls = matched[0]\n    # Return all ancestor class names (broader concepts)\n    return [a.name for a in cls.ancestors()\
  \ if a is not cls]\n\ndef query_conceptnet(entity: str, relation: str = 'IsA') -> list[tuple[str, float]]:\n    # ConceptNet\
  \ REST API\n    url = f'https://api.conceptnet.io/query?node=/c/en/{entity}&rel=/r/{relation}&limit=10'\n    resp = requests.get(url,\
  \ timeout=10)\n    if resp.status_code != 200:\n        return []\n    edges = resp.json().get('edges', [])\n    results\
  \ = []\n    for e in edges:\n        end = e.get('end', {}).get('label', '')\n        weight = e.get('weight', 1.0)\n  \
  \      # Normalize: ConceptNet weights typically 1.0-10.0; cap confidence at 0.80\n        conf = min(0.80, weight / 10.0\
  \ + 0.70)\n        results.append((end, conf))\n    return results\n\ndef classify_domain(document: str) -> str:\n    legal_keywords\
  \ = ['contract', 'obligation', 'party', 'law', 'statute',\n                      'agreement', 'liability', 'clause', 'provision',\
  \ 'plaintiff']\n    narrative_keywords = ['story', 'character', 'once upon', 'family', 'village']\n    legal_score = sum(1\
  \ for kw in legal_keywords if kw in document.lower())\n    narrative_score = sum(1 for kw in narrative_keywords if kw in\
  \ document.lower())\n    if legal_score >= 3:\n        return 'legal'\n    elif narrative_score >= 2:\n        return 'narrative'\n\
  \    return 'general'\n\ndef query_l2(goal_predicate: str, goal_args: list[str], domain: str,\n             onto=None) ->\
  \ list[dict]:\n    results = []\n    if domain == 'legal' and onto is not None:\n        # Try to match args against LKIF\
  \ concepts\n        for arg in goal_args:\n            ancestors = query_lkif_subsumption(onto, arg)\n            for anc\
  \ in ancestors:\n                results.append({\n                    'predicate': f'is_a',\n                    'args':\
  \ [arg, anc.lower()],\n                    'tier': 'l2', 'confidence': 0.95,\n                    'source': 'lkif'\n   \
  \             })\n    else:\n        for arg in goal_args:\n            cn_results = query_conceptnet(arg.replace('_', '\
  \ '))\n            for label, conf in cn_results:\n                results.append({\n                    'predicate': 'is_a',\n\
  \                    'args': [arg, label.lower().replace(' ', '_')],\n                    'tier': 'l2', 'confidence': conf,\n\
  \                    'source': 'conceptnet'\n                })\n    return results\n```\n\n### L3 LLM Abduction (pipeline/l3_abduction.py)\n\
  ```python\nABDUCTION_PROMPT = '''\nDocument excerpt:\n{document_excerpt}\n\nQuestion: Based ONLY on the document above,\
  \ does the following hold?\n{predicate}({args})\nAnswer with exactly 'yes' or 'no', followed by one sentence justification.\n\
  '''\n\ndef abduce_l3(predicate: str, args: list[str], document: str,\n              K: int = 5) -> dict:\n    yes_count\
  \ = 0\n    justifications = []\n    for _ in range(K):\n        resp = client.chat.completions.create(\n            model='meta-llama/llama-3.1-70b-instruct',\n\
  \            messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n                document_excerpt=document[:2000],\n\
  \                predicate=predicate,\n                args=', '.join(args)\n            )}],\n            temperature=0.7,\
  \  # slight temperature for sampling diversity\n            max_tokens=100\n        )\n        answer = resp.choices[0].message.content.strip().lower()\n\
  \        if answer.startswith('yes'):\n            yes_count += 1\n        justifications.append(answer)\n    confidence\
  \ = yes_count / K\n    return {\n        'predicate': predicate, 'args': args,\n        'tier': 'l3', 'confidence': confidence,\n\
  \        'low_confidence': confidence < 0.6,\n        'K': K, 'yes_count': yes_count,\n        'justifications': justifications\n\
  \    }\n```\n\n### Meta-Interpreter with Weakest-Link Propagation (pipeline/meta_interpreter.py)\n```python\nTIER_ORDER\
  \ = {'l0': 0, 'l1': 1, 'l2': 2, 'l3': 3, 'unknown': 4}\n\nclass MetaInterpreter:\n    def __init__(self, kb: PrologKB, l2_module,\
  \ l3_module, domain: str,\n                 document: str, lkif_onto=None):\n        self.kb = kb\n        self.l2 = l2_module\n\
  \        self.l3 = l3_module\n        self.domain = domain\n        self.document = document\n        self.lkif_onto = lkif_onto\n\
  \        self.proof_tree = []  # list of nodes for JSON-LD export\n    \n    def propagate(self, premises: list[dict]) ->\
  \ dict:\n        # Weakest-link: tier = max tier (by TIER_ORDER), conf = min conf\n        max_tier = max(premises, key=lambda\
  \ p: TIER_ORDER[p['tier']])['tier']\n        min_conf = min(p['confidence'] for p in premises)\n        return {'tier':\
  \ max_tier, 'confidence': min_conf}\n    \n    def prove(self, predicate: str, args: list[str],\n              depth: int\
  \ = 0) -> dict:\n        goal_str = predicate + '(' + ','.join(args) + ')'\n        node = {'goal': goal_str, 'predicate':\
  \ predicate, 'args': args}\n        \n        # Try L0/L1 via pyswip with depth limit\n        proved, tier = self.kb.query_with_depth_limit(goal_str,\
  \ depth=3)\n        if proved:\n            node.update({'tier': tier, 'confidence': 1.0, 'method': 'sld'})\n          \
  \  self.proof_tree.append(node)\n            return node\n        \n        # Try L2\n        l2_facts = self.l2.query_l2(\n\
  \            predicate, args, self.domain, self.lkif_onto\n        )\n        if l2_facts:\n            best = max(l2_facts,\
  \ key=lambda f: f['confidence'])\n            # Assert into KB for future use\n            self.kb.prolog.assertz(\n   \
  \             best['predicate'] + '(' + ','.join(best['args']) + ')'\n            )\n            node.update(best)\n   \
  \         self.proof_tree.append(node)\n            return node\n        \n        # Try L3\n        if depth <= 2:  # avoid\
  \ L3 in deep sub-proofs\n            l3_result = self.l3.abduce_l3(predicate, args, self.document)\n            if l3_result['confidence']\
  \ >= 0.6:\n                self.kb.prolog.assertz(goal_str)\n                node.update(l3_result)\n            else:\n\
  \                node.update({'tier': 'unknown', 'confidence': 0.0,\n                             'low_confidence': True})\n\
  \            self.proof_tree.append(node)\n            return node\n        \n        node.update({'tier': 'unknown', 'confidence':\
  \ 0.0})\n        self.proof_tree.append(node)\n        return node\n    \n    def get_trace(self) -> list[dict]:\n     \
  \   return self.proof_tree\n```\n\n### JSON-LD Trace Export (pipeline/trace.py)\n```python\ndef build_jsonld(proof_tree:\
  \ list[dict], doc_id: str) -> dict:\n    TIER_COLORS = {'l0': 'green', 'l1': 'yellow', 'l2': 'orange',\n               \
  \    'l3': 'red', 'unknown': 'gray'}\n    nodes = []\n    for i, node in enumerate(proof_tree):\n        nodes.append({\n\
  \            '@id': f'node:{doc_id}:{i}',\n            '@type': 'ProofNode',\n            'predicate': node.get('predicate',\
  \ ''),\n            'args': node.get('args', []),\n            'tier': node.get('tier', 'unknown'),\n            'confidence':\
  \ node.get('confidence', 0.0),\n            'color': TIER_COLORS.get(node.get('tier', 'unknown'), 'gray'),\n           \
  \ 'source_span': node.get('source_span', ''),\n            'method': node.get('method', 'abduction')\n        })\n    return\
  \ {\n        '@context': {'@vocab': 'https://schema.org/'},\n        '@type': 'ProofTrace',\n        'document_id': doc_id,\n\
  \        'nodes': nodes\n    }\n```\n\n## PHASE 2 — BASELINES\n\n### SymBa-style flat baseline (baselines/symba_baseline.py)\n\
  ```python\n# Empty KB; for every proof-failure goal, call LLM once (K=1, no tier routing)\ndef symba_prove(predicate: str,\
  \ args: list[str], document: str,\n                kb: PrologKB) -> dict:\n    proved, _ = kb.query_with_depth_limit(\n\
  \        predicate + '(' + ','.join(args) + ')', depth=3\n    )\n    if proved:\n        return {'tier': 'sld', 'confidence':\
  \ 1.0, 'proved': True}\n    # LLM immediately, no ontology tier\n    resp = client.chat.completions.create(\n        model='meta-llama/llama-3.1-70b-instruct',\n\
  \        messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n            document_excerpt=document[:2000],\n\
  \            predicate=predicate, args=', '.join(args)\n        )}],\n        temperature=0.0, max_tokens=100\n    )\n \
  \   answer = resp.choices[0].message.content.strip().lower()\n    return {'tier': 'llm', 'confidence': 1.0 if answer.startswith('yes')\
  \ else 0.0,\n            'proved': answer.startswith('yes'), 'no_provenance': True}\n```\n\n### CoT baseline (baselines/cot_baseline.py)\n\
  ```python\nCOT_PROMPT = '''\nDocument:\n{document}\n\nQuestion: {question}\nThink step by step, then answer True, False,\
  \ or Unknown.\n'''\ndef cot_answer(document: str, question: str) -> str:\n    resp = client.chat.completions.create(\n \
  \       model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': COT_PROMPT.format(\n \
  \           document=document[:3000], question=question)}],\n        temperature=0.0, max_tokens=500\n    )\n    raw = resp.choices[0].message.content\n\
  \    # Extract final answer\n    for ans in ['True', 'False', 'Unknown']:\n        if ans.lower() in raw.lower().split()[-10:]:\n\
  \            return ans\n    return 'Unknown'\n```\n\n## PHASE 3 — DATASET LOADERS\n\n### ProofWriter (datasets/proofwriter_loader.py)\n\
  ```python\nfrom datasets import load_dataset\ndef load_proofwriter_owa(split='validation', max_examples=200):\n    # Use\
  \ tasksource/proofwriter, filter to OWA (depth_5_owa or depth-5-OWA)\n    ds = load_dataset('tasksource/proofwriter', split=split)\n\
  \    # Filter for D*(OWA) subset with 3-valued answers\n    owa = [ex for ex in ds if ex.get('answer') in ['True','False','Unknown']]\n\
  \    return owa[:max_examples]\n    # Each example: {'context': str, 'question': str, 'answer': 'True'|'False'|'Unknown'}\n\
  \    # context is a short theory (facts + rules as natural language sentences)\n    # question is the query sentence\n```\n\
  \n### CLUTRR (datasets/clutrr_loader.py)\n```python\nfrom datasets import load_dataset\ndef load_clutrr(split='test', max_examples=200):\n\
  \    ds = load_dataset('CLUTRR/v1', split=split)  # or specific config\n    # Each: {'story': str, 'query': [entity1, entity2],\
  \ 'target_text': str}\n    return list(ds)[:max_examples]\n```\n\n### SARA (datasets/sara_loader.py)\n```python\nimport\
  \ os, glob\ndef load_sara(sara_dir='sara', max_examples=50):\n    cases = []\n    for txt_file in glob.glob(os.path.join(sara_dir,\
  \ 'cases', '*.txt')):\n        stem = os.path.splitext(os.path.basename(txt_file))[0]\n        pl_file = os.path.join(sara_dir,\
  \ 'prolog', stem + '.pl')\n        if os.path.exists(pl_file):\n            cases.append({\n                'id': stem,\n\
  \                'document': open(txt_file).read(),\n                'gold_prolog': open(pl_file).read(),\n            \
  \    'answer': 'entailed'  # determine from .pl query result\n            })\n    return cases[:max_examples]\n```\n\n###\
  \ ContractNLI (datasets/contractnli_loader.py)\n```python\nimport json\ndef load_contractnli(data_dir='contract-nli', split='test',\
  \ max_contracts=50):\n    # Download from stanfordnlp.github.io/contract-nli/\n    # JSON format: {documents: [{text, annotation_sets:\
  \ [{annotations: {nda-1: {choice, spans}}}]}]}\n    with open(os.path.join(data_dir, f'{split}.json')) as f:\n        data\
  \ = json.load(f)\n    examples = []\n    for doc in data['documents'][:max_contracts]:\n        text = doc['text']\n   \
  \     for ann_set in doc.get('annotation_sets', []):\n            for hyp_id, ann in ann_set.get('annotations', {}).items():\n\
  \                examples.append({\n                    'document': text[:3000],\n                    'hypothesis': hyp_id,\n\
  \                    'label': ann['choice'],  # 'Entailment'|'Contradiction'|'NotMentioned'\n                    'evidence_spans':\
  \ ann.get('spans', [])\n                })\n    return examples\n```\n\n## PHASE 4 — METRICS\n\n### Hallucination Rate (metrics/hallucination.py)\n\
  ```python\ndef compute_hallucination_rate(proof_trees: list[list[dict]],\n                               documents: list[str])\
  \ -> float:\n    # For each L0-tier fact in the proof tree, check if predicate string\n    # or its args appear literally\
  \ in the source document\n    hallucinated = 0\n    total_l0 = 0\n    for tree, doc in zip(proof_trees, documents):\n  \
  \      doc_lower = doc.lower()\n        for node in tree:\n            if node.get('tier') == 'l0':\n                total_l0\
  \ += 1\n                fact_str = node.get('predicate', '') + ' ' + ' '.join(node.get('args', []))\n                # Check\
  \ if any arg or predicate keyword appears in doc\n                args_in_doc = any(arg.replace('_', ' ') in doc_lower\n\
  \                                  for arg in node.get('args', []))\n                if not args_in_doc:\n             \
  \       hallucinated += 1\n    return hallucinated / total_l0 if total_l0 > 0 else 0.0\n```\n\n### ECE (metrics/ece.py)\n\
  ```python\nimport numpy as np\ndef compute_ece(confidences: list[float], labels: list[int],\n                n_bins: int\
  \ = 10) -> float:\n    bins = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    n = len(confidences)\n    for b in range(n_bins):\n\
  \        lo, hi = bins[b], bins[b+1]\n        mask = [(lo <= c < hi) for c in confidences]\n        if not any(mask):\n\
  \            continue\n        bin_confs = [c for c, m in zip(confidences, mask) if m]\n        bin_labels = [l for l, m\
  \ in zip(labels, mask) if m]\n        avg_conf = np.mean(bin_confs)\n        frac_pos = np.mean(bin_labels)\n        ece\
  \ += (len(bin_confs) / n) * abs(avg_conf - frac_pos)\n    return ece\n```\n\n## PHASE 5 — MAIN ORCHESTRATION (method.py)\n\
  ```python\nimport json, time, os\nfrom pipeline.l0_extractor import extract_l0\nfrom pipeline.l1_prolog import PrologKB\n\
  from pipeline import l2_ontology, l3_abduction\nfrom pipeline.meta_interpreter import MetaInterpreter\nfrom pipeline.trace\
  \ import build_jsonld\nfrom baselines.symba_baseline import symba_prove\nfrom baselines.cot_baseline import cot_answer\n\
  from datasets.sara_loader import load_sara\nfrom datasets.proofwriter_loader import load_proofwriter_owa\nfrom datasets.clutrr_loader\
  \ import load_clutrr\nfrom datasets.contractnli_loader import load_contractnli\nfrom metrics.hallucination import compute_hallucination_rate\n\
  from metrics.ece import compute_ece\n\nRESULTS = {'phase0': {}, 'per_example': [], 'aggregates': {}}\nTOTAL_COST = 0.0 \
  \ # track OpenRouter spend\nCOST_LIMIT = 9.0  # hard stop before $10\n\n# Llama-3.1-70b pricing: ~$0.35/M input, $0.40/M\
  \ output tokens (check current)\n# K=5 abduction calls per unresolved goal: budget conservatively\n\ndef estimate_cost(n_tokens_in:\
  \ int, n_tokens_out: int) -> float:\n    return (n_tokens_in / 1e6) * 0.35 + (n_tokens_out / 1e6) * 0.40\n\ndef check_budget():\n\
  \    global TOTAL_COST\n    if TOTAL_COST >= COST_LIMIT:\n        raise RuntimeError(f'Budget exceeded: ${TOTAL_COST:.2f}')\n\
  \n## PHASE 0: Run extraction calibration on 25 SARA examples\n# ... (see above)\n# Report precision/recall; gate check\n\
  \n## MINI SCALE (10% of each benchmark, run first)\n# ProofWriter: 200 examples OWA → use 20 for mini\n# CLUTRR: 200 examples\
  \ → use 20 for mini\n# SARA: 50 → use 10 for mini\n# ContractNLI: 50 contracts → use 5 for mini\n\n## For each example in\
  \ each benchmark:\n#   1. Extract L0 facts (l0_extractor)\n#   2. Load into PrologKB\n#   3. Run meta_interpreter.prove()\
  \ for the benchmark's query goal\n#   4. Also run symba_baseline and cot_baseline on same example\n#   5. Store per-example\
  \ results: {id, benchmark, answer_gold, \n#      answer_stratified, answer_symba, answer_cot,\n#      tier_used, confidence,\
  \ proof_tree_jsonld}\n\n## After all examples:\n#   1. Multi-hop accuracy per baseline per benchmark (exact match)\n#  \
  \ 2. Hallucination rates for stratified vs symba\n#   3. Tier distribution: fraction using only L0-L2\n#   4. ECE on SARA\
  \ L3 confidences vs binary entailment labels\n#   5. Write method_out.json\n\nif __name__ == '__main__':\n    # Load LKIF\
  \ once\n    lkif_onto = l2_ontology.load_lkif()\n    \n    all_results = []\n    \n    for benchmark, loader_fn in [\n \
  \       ('sara', load_sara),\n        ('proofwriter_owa', load_proofwriter_owa),\n        ('clutrr', load_clutrr),\n   \
  \     ('contractnli', load_contractnli)\n    ]:\n        examples = loader_fn()  # starts with mini (10%)\n        for ex\
  \ in examples:\n            check_budget()\n            document = ex['document']\n            domain = l2_ontology.classify_domain(document)\n\
  \            \n            # Stratified pipeline\n            kb = PrologKB()\n            l0_facts = extract_l0(document,\
  \ domain)\n            kb.load_l0_facts(l0_facts)\n            interp = MetaInterpreter(kb, l2_ontology, l3_abduction,\n\
  \                                     domain, document, lkif_onto)\n            goal_pred, goal_args = parse_query(ex) \
  \ # benchmark-specific\n            result_node = interp.prove(goal_pred, goal_args)\n            trace = build_jsonld(interp.get_trace(),\
  \ ex['id'])\n            \n            # SymBa baseline\n            symba_kb = PrologKB()  # empty KB\n            symba_result\
  \ = symba_prove(goal_pred, goal_args, document, symba_kb)\n            \n            # CoT baseline\n            cot_result\
  \ = cot_answer(document, ex.get('question', str((goal_pred, goal_args))))\n            \n            all_results.append({\n\
  \                'id': ex['id'], 'benchmark': benchmark,\n                'gold': ex['answer'],\n                'stratified':\
  \ node_to_answer(result_node),\n                'symba': symba_result['proved'],\n                'cot': cot_result,\n \
  \               'tier_used': result_node['tier'],\n                'confidence': result_node['confidence'],\n          \
  \      'l0_facts_count': len(l0_facts),\n                'proof_tree': trace\n            })\n    \n    # Aggregate metrics\n\
  \    aggregates = {}\n    for bm in ['sara', 'proofwriter_owa', 'clutrr', 'contractnli']:\n        bm_results = [r for r\
  \ in all_results if r['benchmark'] == bm]\n        aggregates[bm] = {\n            'accuracy_stratified': mean(r['gold']\
  \ == r['stratified'] for r in bm_results),\n            'accuracy_symba': mean(r['gold'] == str(r['symba']) for r in bm_results),\n\
  \            'accuracy_cot': mean(r['gold'] == r['cot'] for r in bm_results),\n            'hallucination_rate_stratified':\
  \ compute_hallucination_rate(\n                [r['proof_tree']['nodes'] for r in bm_results],\n                [get_doc(r)\
  \ for r in bm_results]\n            ),\n            'tier_l0l1l2_fraction': mean(r['tier_used'] in ['l0','l1','l2'] for\
  \ r in bm_results),\n            'n_examples': len(bm_results)\n        }\n    \n    # ECE on SARA\n    sara_l3 = [r for\
  \ r in all_results if r['benchmark'] == 'sara' and r['tier_used'] == 'l3']\n    if sara_l3:\n        aggregates['ece_sara_l3']\
  \ = compute_ece(\n            [r['confidence'] for r in sara_l3],\n            [1 if r['gold'] == 'entailed' else 0 for\
  \ r in sara_l3]\n        )\n    \n    output = {\n        'phase0_extraction_calibration': RESULTS['phase0'],\n        'per_example_results':\
  \ all_results,\n        'aggregate_metrics': aggregates,\n        'total_cost_usd': TOTAL_COST\n    }\n    with open('method_out.json',\
  \ 'w') as f:\n        json.dump(output, f, indent=2)\n    print('Done. method_out.json written.')\n```\n\n## SCALING STRATEGY\n\
  1. Run on 10% (mini) first; if all benchmarks complete in < 2h and cost < $3, scale to 50%\n2. If 50% completes in < 4h\
  \ and cost < $6, scale to 100%\n3. Use multiprocessing.Pool for parallel example processing within each benchmark (4 workers)\n\
  4. Cache L0 extraction results to disk (JSON) to avoid re-calling LLM on restarts\n5. Cache LKIF subclass queries to a dict;\
  \ don't reload ontology per example\n6. For L3, only call K=5 on SARA (where ECE is measured); use K=3 on others to save\
  \ cost\n"
fallback_plan: |
  ## Fallback scenarios and mitigations

  ### F1: pyswip / SWI-Prolog integration fails
  - Fallback: Replace pyswip with subprocess calls to swipl binary using `timeout 5 swipl -g 'call_with_depth_limit(Goal,3,R),write(R),halt' -t halt`
  - Parse stdout for result
  - Implement KB as a .pl file written to /tmp, loaded per query

  ### F2: LKIF OWL file fails to load via owlready2 (import errors on OWL-DL axioms)
  - Fallback: Use owlready2 with `world.as_rdflib_graph()` and SPARQL queries instead of Python object API
  - If owlready2 fails entirely: parse lkif-core.owl as XML, extract rdfs:subClassOf triples manually using lxml
  - Emergency fallback: use a hardcoded dict of 50 key LKIF legal concepts and their superclasses

  ### F3: Phase 0 SARA extraction precision < 0.75
  - First iteration: add 3 gold-annotated SARA examples as few-shot to the extraction prompt
  - Second iteration: switch to constrained JSON output with `response_format={type:'json_object'}` and a schema that enforces valid Prolog atom patterns
  - Third iteration: use a stronger model (deepseek/deepseek-r1 or google/gemma-3-27b-it) for extraction only
  - Document all iteration results regardless; proceed with best achieved precision

  ### F4: CLUTRR or ProofWriter D*(OWA) HuggingFace load fails
  - CLUTRR: try `load_dataset('clutrr', 'v1.1')` then fallback to direct download from original GitHub (https://github.com/facebookresearch/clutrr)
  - ProofWriter: try all three HF repos (tasksource/proofwriter, D3xter1922/proofwriter-dataset, renma/ProofWriter); if all fail, use the Allen AI release directly from https://aristo-public-data.s3-us-west-2.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip
  - ContractNLI: download from stanfordnlp.github.io/contract-nli/ directly via requests

  ### F5: Cost approaching $10 limit before all benchmarks complete
  - Priority order: SARA (Phase 0 gate + hallucination) > ProofWriter OWA (multi-hop accuracy) > CLUTRR > ContractNLI
  - Reduce K from 5 to 3 for L3 abduction on lower-priority benchmarks
  - Switch L0 extraction model to meta-llama/llama-3.1-8b-instruct (much cheaper, ~10x cheaper per token)
  - Reduce mini scale to 5% (10 examples per benchmark) if needed

  ### F6: Prolog depth_limit produces incorrect results or pyswip segfaults
  - Fallback: implement a pure Python DFS SLD solver with explicit depth counter
  - Represent KB as a dict: predicate_name -> list of (args, tier, conf)
  - Only handles datalog-style rules (no function symbols, no cuts)
  - Sufficient for L0 fact lookup and simple 2-3 step chain deduction

  ### F7: ConceptNet API rate-limits or is unreachable
  - Fallback: use a locally cached ConceptNet Lite (https://github.com/commonsense/conceptnet-lite) if pip-installable
  - Emergency fallback: use Wikidata SPARQL endpoint for all non-legal domains:
    `https://query.wikidata.org/sparql?query=SELECT ?classLabel WHERE { wd:Q{entity_id} wdt:P31/wdt:P279* ?class . SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } } LIMIT 10`
testing_plan: |-
  ## Testing Strategy

  ### Step 1: Environment validation (run first, < 5 min)
  ```bash
  # Verify SWI-Prolog installed
  swipl --version
  # Verify pyswip works
  python3 -c "from pyswip import Prolog; p=Prolog(); list(p.query('member(X,[1,2,3])'))"
  # Verify owlready2
  python3 -c "from owlready2 import get_ontology; print('owlready2 ok')"
  # Verify OpenRouter key works
  curl -H 'Authorization: Bearer $OPENROUTER_KEY' https://openrouter.ai/api/v1/models | head -5
  # Verify call_with_depth_limit
  python3 -c "
  from pyswip import Prolog
  p = Prolog()
  p.assertz('parent(tom,bob)')
  p.assertz('parent(bob,ann)')
  p.assertz('ancestor(X,Y) :- parent(X,Y)')
  p.assertz('ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y)')
  result = list(p.query('call_with_depth_limit(ancestor(tom,ann), 5, R)'))
  print('depth_limit test:', result)  # should find solution
  "
  ```

  ### Step 2: L0 extraction smoke test (3 examples, < 10 min)
  - Load 3 SARA cases, run extraction prompt, verify:
    a. Output is valid JSON array
    b. Predicates match regex `^[a-z][a-z0-9_]*$`
    c. At least 2 predicates extracted per document
    d. No uppercase variable names in args
  - If any fail: debug extraction prompt before Phase 0

  ### Step 3: Phase 0 on 25 SARA examples (~ 20-30 min)
  - Run extraction on all 25 sampled cases
  - Compute precision/recall against gold .pl annotations
  - CONFIRM: precision >= 0.75 before proceeding
  - Log per-case results; note cases where extraction fails entirely

  ### Step 4: End-to-end mini pipeline test (5 ProofWriter OWA examples, < 15 min)
  - Run full stratified pipeline + both baselines on 5 ProofWriter examples
  - Verify: method_out.json is written with correct schema
  - Verify: proof trees are non-empty for at least 3/5 examples
  - Verify: tier distribution shows at least some L0 facts (not all L3)
  - Verify: cost tracking is working (TOTAL_COST > 0 and < $0.50 for 5 examples)

  ### Step 5: LKIF ontology integration test
  - Load LKIF OWL; query ancestors of class 'Obligation'
  - Expected: returns ['Normative_thing', 'Qualified_norm', 'Norm', ...] (any non-empty list)
  - If empty: check that lkif-core.owl was downloaded successfully and has class definitions

  ### Step 6: Mini benchmark run (10% scale, ~1-2h)
  - Run all 4 benchmarks at 10% scale (20/20/10/5 examples)
  - Check: no crashes, results for all examples, metrics computable
  - Check: total cost < $2.00 for mini run
  - Decision: if runtime < 90 min and cost < $2, scale to 50%; else stay at 10% and report

  ### Step 7: Final validation of method_out.json
  - Verify JSON is valid and parseable
  - Verify top-level keys: phase0_extraction_calibration, per_example_results, aggregate_metrics, total_cost_usd
  - Verify per_example has required fields: id, benchmark, gold, stratified, symba, cot, tier_used, confidence
  - Verify aggregate_metrics has accuracy for all 3 systems on all 4 benchmarks
  - Apply aii-json skill to validate against expected schema

  ### Confirmation signals before full scale
  - Phase 0 precision >= 0.75 (HARD gate)
  - Mini pipeline produces non-trivial tier distribution (not 100% L3)
  - SymBa baseline produces non-trivially different results from stratified (if identical, check bug)
  - Cost per example < $0.10 (to stay within budget for 100+ examples)

  ### Known failure modes to watch for
  - pyswip segfault under multiprocessing (use spawn not fork; or run Prolog in subprocess)
  - owlready2 loading OWL-DL axioms with imports (some LKIF owl files import others; set onto_path to local dir)
  - OpenRouter rate limits: add time.sleep(0.5) between L3 calls; implement exponential backoff
  - CLUTRR data format varies by version: check field names before assuming story/query/target_text keys
</artifact_plan>



<available_resources>
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **HARD LIMIT**: Maximum $10 USD total spend on LLM API calls (OpenRouter). Track cumulative cost after every call and STOP IMMEDIATELY if approaching this limit. Never exceed this budget under any circumstances.
</software_constraints>

<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Web search (Serper), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-image-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
- aii-handbook-multi-llm-agents: Multi-LLM agent orchestration patterns
</skills>
</available_resources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — framework choices, implementation patterns, agent orchestration
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
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
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [11] SYSTEM-USER prompt · 2026-06-15 20:27:33 UTC

```
<validation-feedback>
Attempt 1 failed validation.

You have not created the output file `.terminal_claude_agent_struct_out.json` yet. Use the Write tool to create it.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [12] SYSTEM-USER prompt · 2026-06-15 20:28:33 UTC

```
<validation-feedback>
Attempt 2 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `layman_summary`: 'This experiment builds a four-tier AI reasoning system that converts text documents into logical rules, uses a symbolic Prolog reasoner to derive answers, and falls back to an AI language model only when strict logic fails — measuring how accurately and reliably it reasons compared to baselines that use AI alone.' is too long (at most 250 characters, got 314)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [13] SYSTEM-USER prompt · 2026-06-15 20:29:15 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [14] SYSTEM-USER prompt · 2026-06-15 20:29:57 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 2/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [15] SYSTEM-USER prompt · 2026-06-15 20:33:25 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 3/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json
  - Missing file: mini_method_out.json
  - Missing file: preview_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
