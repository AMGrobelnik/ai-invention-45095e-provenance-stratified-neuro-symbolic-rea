# gen_plan_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_experiment_1` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-15 20:07:11 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1
```

### [2] SYSTEM-USER prompt · 2026-06-15 20:07:17 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: EXPERIMENT

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance
</artifact_type_info>

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

<time_budget>

The experiment executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

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

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

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

<hypothesis>
kind: hypothesis
title: >-
  Provenance-Stratified Neuro-Symbolic Reasoning: Bounded Tier-Ordered SLD Resolution with Domain-Adaptive Ontology and Calibrated
  Confidence Propagation
hypothesis: >-
  A neuro-symbolic text-to-reasoning pipeline that (i) populates an initial Prolog knowledge base from document-explicit facts
  (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier
  — L0 (document-stated), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤3 steps), L2 (domain-ontology-entailed:
  LKIF Core OWL for legal, ConceptNet for narrative, Wikidata SPARQL for general domain), L3 (LLM-abduced, confidence via
  K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution (exhausting lower tiers before escalating)
  will achieve significantly lower hallucination rates and higher multi-hop reasoning accuracy than flat-KB pipelines that
  invoke the LLM on every proof failure from an empty working memory, because the tier ordering prevents LLM confabulation
  of facts that are already provable by cheaper and more reliable means, while weakest-link propagation of the (tier, confidence)
  tuple through the proof tree yields calibrated, human-auditable epistemic traces.
motivation: >-
  Current neuro-symbolic SLD-resolution pipelines such as SymBa (Lee & Hwang, NAACL 2025) start with an empty symbolic database
  and call the LLM every time the solver encounters a goal it cannot prove — meaning the LLM is the first and only resort
  for all factual retrieval, not a last resort. This conflation of document facts, ontological background, and LLM world knowledge
  into a single LLM call causes two failure modes: (1) hallucination — the LLM is invoked even for facts explicitly stated
  in the input document or entailed by a domain ontology, allowing it to confabulate alternatives to ground truth; and (2)
  opacity — the derivation trace records that the LLM supplied a fact, but not whether it was document-retrievable or a true
  abduction, making the output unauditable. For high-stakes domains such as legal statutory reasoning (SARA, Holzenberger
  et al. 2020), where a hand-constructed Prolog system achieves 100% accuracy precisely because the KB is grounded from the
  document, the inability to distinguish document-grounded from LLM-abduced facts is a fundamental architectural defect. The
  LKIF Core OWL ontology (Hoekstra et al., Estrella project), an OWL-DL + SWRL formalism covering legal concepts (norm, obligation,
  prohibition, claim, liability), provides a principled L2 tier for legal domain bridging that SymBa entirely lacks. The proposed
  stratification resolves both failures: it enforces a strict evidence hierarchy (document > bounded deduction > domain ontology
  > LLM), reduces LLM invocation to a genuinely last-resort abductive step, and propagates a (tier_label, confidence_score)
  annotation through every proof-tree node, producing machine-executable and human-readable epistemic traces. This is architecturally
  distinct from retrieval-augmented generation (RAG), which grounds neural generation in retrieved passages but produces no
  symbolic proof trace, performs no CWA/OWA tier switching, and annotates no individual facts with epistemic provenance. It
  is also distinct from DeepProbLog, which integrates neural predicates into probabilistic logic programs but assigns uncertainty
  from a single distribution over neural outputs rather than from a named hierarchy of epistemically distinct sources.
assumptions:
- >-
  LLMs can extract L0 atomic Prolog predicates from professionally written short documents (~3000 chars) with precision ≥
  0.80 when given domain-adapted structured extraction prompts — verified by a mandatory Phase 0 extraction study on 25 gold-annotated
  SARA case descriptions before full evaluation proceeds. If precision < 0.75, the pipeline pivots to few-shot or constrained-decoding
  extraction before testing tier-ordering benefits.
- >-
  The LKIF Core OWL ontology provides non-trivial L2 bridging coverage for legal documents: at minimum, class-subsumption
  relations involving legal concepts such as obligation, prohibition, norm, and party that SARA and ContractNLI cases require
  for multi-hop deduction. This is operationalized as a measurable disconfirmation criterion.
- >-
  SymBa's empty-DB design causes measurably higher hallucination rates than a document-grounded L0 extraction baseline, because
  the LLM is invoked for facts already explicit in the document; the L0 grounding alone (without L2/L3) should reduce hallucination
  relative to SymBa.
- >-
  A depth-bounded L1 computation (≤3 SLD resolution steps on the L0 KB, no new predicate invention, equivalent to one full
  SWI-Prolog query with `depth_limit(3)`) is tractable on commodity hardware and captures the direct deductive consequences
  needed for the benchmark tasks.
- >-
  The benchmark datasets (ProofWriter D*(OWA) with three-valued True/False/Unknown answers, CLUTRR, SARA, ContractNLI with
  607 annotated contracts) contain sufficient cases distinguishable by tier, enabling isolation of the tier-ordering effect.
investigation_approach: |-
  PHASE 0 — EXTRACTION CALIBRATION (prerequisite gate): Extract L0 atomic Prolog predicates from 25 randomly sampled SARA case descriptions (Holzenberger et al. 2020, US tax law cases) using an LLM via OpenRouter with a structured extraction prompt. Compare against the gold-standard Prolog KB annotations released with SARA. Report precision and recall. If precision < 0.75, iterate on the extraction prompt (few-shot examples, constrained JSON output format) before proceeding. Phase 0 is reported as a standalone result regardless of outcome.

  PHASE 1 — SYSTEM ARCHITECTURE:
  (a) TRANSLATION LAYER (L0): LLM parses each input document into SWI-Prolog predicates tagged as L0. Each fact is stored as `fact(Pred, l0, 1.0)`. Rules explicitly stated in the document are stored as `rule(Head, Body, l0, 1.0)`. The Prolog KB is pre-populated before any reasoning begins — unlike SymBa, which starts with an empty database.
  (b) BOUNDED L1 DEDUCTION: L1 is defined operationally as the full result of one SWI-Prolog query execution on the L0 KB with `depth_limit(3)` and no new predicate invention. This is deterministic, tractable, and precisely specifiable: escalation to L2 triggers if and only if a goal fails after exhausting the depth-3 resolution tree over L0+L1.
  (c) DOMAIN-ADAPTIVE L2 ONTOLOGY: At runtime, document domain is classified (legal/narrative/general). For legal documents: LKIF Core OWL (Estrella project, OWL-DL + SWRL) loaded via Thea2 Prolog-OWL library; provides T-Box terminological knowledge over legal concepts (norm, obligation, prohibition, claim, agent, legal document). For narrative/story documents: ConceptNet REST API (IsA, PartOf, UsedFor relations). For general domain: Wikidata SPARQL endpoint. When L0/L1 fails at a leaf node, the meta-interpreter queries the relevant ontology for subsumption-implied facts about the failed goal's entity arguments. Confirmed L2 facts are cached as `fact(Pred, l2, 0.95)` (for OWL subsumption entailment) or `fact(Pred, l2, 0.80)` (for ConceptNet statistical association). L2 confidence values are preset constants reflecting entailment type, not LLM outputs.
  (d) LLM ABDUCTION LAYER (L3): Only when L0+L1+L2 exhaustion occurs, a structured abductive schema template query is sent to the LLM via OpenRouter: 'Given this document [excerpt], does [predicate(arg1, arg2)] hold? Answer yes/no with a one-sentence justification.' Sent independently K=5 times; L3 confidence = fraction of 'yes' responses. Stored as `fact(Pred, l3, K_yes/5)`. Facts with confidence < 0.6 are flagged 'low-confidence abduction'.
  (e) PROVENANCE-PROPAGATING META-INTERPRETER: For atomic goals, tier and confidence come directly from the matched fact. For derived goals: `Tier(derived) = max_i(Tier(premise_i))` (weakest-link tier); `Conf(derived) = min_i(Conf(premise_i))` (weakest-link confidence). The (Tier, Conf) tuple is compared lexicographically: tier takes priority. Worked example (legal domain): document states 'Alice signed the contract' (L0, 1.0); LKIF subsumption states 'signing a contract creates an obligation' (L2, 0.95); the meta-interpreter derives 'Alice has an obligation' at (L2, 0.95) — the tier propagates to the weakest link (L2), not the document-explicit L0 premise.
  (f) TRACE GRAPH OUTPUT: Derivation tree exported as JSON-LD with each node labeled (predicate, args, tier, confidence, source_doc_span). Rendered as a static HTML visualization with color-coded tier indicators (green=L0, yellow=L1, orange=L2, red=L3).

  PHASE 2 — EVALUATION:
  Primary benchmarks: (i) ProofWriter D*(OWA) subset (Tafjord et al., ACL 2021 Findings) — the OWA variant supports three-valued answers (True/False/Unknown), making it the most appropriate benchmark for open-world tier-switching; (ii) CLUTRR (kinship multi-hop, tests L2 ontological kinship rules); (iii) SARA (US federal tax law, ~100+ annotated Prolog KB cases, gold Prolog system achieves 100%); (iv) ContractNLI (Koreeda & Manning, EMNLP 2021 Findings; 607 non-disclosure agreements annotated with entailment/contradiction/neutral labels and evidence spans). RuleTaker retained only as a translation-fidelity sanity check, clearly labeled, not a primary benchmark.
  Baselines: SymBa (NAACL 2025, flat empty-DB SLD+LLM), LINC (flat FOL+theorem prover), standard RAG with BM25 retrieval, chain-of-thought LLM prompting.
  Measures: (i) L0 extraction precision/recall (Phase 0); (ii) multi-hop accuracy on all primary benchmarks; (iii) hallucination rate — predicates asserted as L0-certain that are not in the document, measured by human annotator agreement; (iv) tier distribution in successful proof trees (fraction requiring only L0-L2 vs. L3); (v) ECE of confidence scores against binary ground truth on SARA entailment labels.
  Interpretability evaluation (replacing the statistically underpowered N=5 user preference study): 15 domain experts perform a timed comprehension task — given a proof trace, answer 5 yes/no questions about the derivation within 3 minutes. Measures: comprehension accuracy, time-to-first-correct-answer, inter-rater reliability (Cohen's kappa). This operationalizes interpretability as a measurable cognitive performance metric.
success_criteria: |-
  CONFIRM: (1) The provenance-stratified pipeline achieves statistically significantly lower hallucination rates (>15% relative reduction, 95% CI not overlapping zero) than SymBa on the combined SARA + ContractNLI evaluation, demonstrating that pre-populating the KB from the document (L0) and inserting an L2 ontology tier before LLM invocation reduces confabulation. (2) Multi-hop accuracy on ProofWriter D*(OWA) and CLUTRR improves by >5% over SymBa, with the improvement attributable to L2 ontology bridging facts in successful proof trees. (3) Proof trees show ≥30% of successful proofs using only L0–L2 knowledge (no L3 LLM abduction) in cases where SymBa would invoke the LLM (i.e., cases where the answer is in-document or ontology-derivable). (4) Calibration: ECE of (tier, confidence) tuples on SARA ground-truth entailment labels is < 0.15. (5) Interpretability proxy: domain experts achieve >80% comprehension accuracy on tier-annotated traces vs. <65% on SymBa flat proof trees (chi-squared test, p < 0.05, N=15 raters).

  DISCONFIRM: (1) Hallucination rates are not statistically different between stratified and SymBa pipelines (CI overlaps zero), indicating that LLM invocation on goal failure does not in practice confabulate document-explicit facts at rates the tier ordering can measurably reduce. (2) LKIF, ConceptNet, and Wikidata all fail to contribute any L2 bridging facts in ≥90% of test cases, indicating the L2 tier is vacuous for the tested domains and the system degrades to SymBa plus provenance labels. (3) Phase 0 extraction precision falls below 0.75, invalidating the L0 KB assumption. (4) ECE > 0.25 on SARA held-out examples, indicating poorly calibrated confidence. (5) L3 self-consistency confidence (K=5) correlates poorly with factual accuracy against SARA annotated ground truth (Pearson r < 0.3).
related_works:
- >-
  SymBa (Lee & Hwang, NAACL 2025) — Integrates an SLD-resolution symbolic solver with an LLM using a coroutine design. Critically,
  SymBa starts with an EMPTY symbolic database: the LLM is called every time the solver encounters a goal it cannot prove,
  generating the next rule or fact and adding it to the solver's working memory. There is no document-grounded L0 KB, no ontology
  tier between the empty DB and the LLM, and no provenance annotation on generated facts. The proposed system differs architecturally:
  it pre-populates a Prolog KB from L0 document extraction, inserts a domain-specific ontology tier (LKIF/ConceptNet/Wikidata)
  before LLM invocation, and propagates (tier, confidence) annotations through the proof tree, enabling hallucination measurement
  that SymBa's flat design cannot support.
- >-
  LINC (Olausson et al., EMNLP 2023) — Translates natural language to FOL via LLM and delegates reasoning to an external theorem
  prover. Unlike SymBa, LINC does not attempt open-world fact retrieval: proof failure returns 'unknown' without LLM escalation,
  has no ontology integration, and produces no provenance-annotated trace. The proposed system extends this with a three-tier
  knowledge hierarchy, dynamic CWA/OWA switching at tier transitions, and tier-propagated uncertainty in proof trees.
- >-
  RAG systems (REALM, Fusion-in-Decoder/FiD) — Retrieve relevant context passages to ground LLM generation, reducing hallucination
  relative to purely parametric models. RAG systems do not execute symbolic logic programs, produce no proof trace, perform
  no CWA/OWA switching, and do not annotate individual facts with epistemic provenance. The proposed system's conclusions
  are derived by SLD resolution over a stratified KB; each derivation step is auditable at the predicate level rather than
  opaque at the token level. RAG also lacks the tier-ordered escalation policy: all retrieved passages are treated as equally
  trusted context.
- >-
  DeepProbLog (Manhaeve et al., NeurIPS 2018, AI Journal 2021) — Integrates neural predicates into ProbLog, a probabilistic
  logic programming language. DeepProbLog does not distinguish epistemic source into named provenance tiers: all uncertainty
  flows from a single probability distribution over neural network outputs. It does not distinguish document-explicit facts
  (L0) from ontology-entailed bridging facts (L2) or LLM-abduced implicit knowledge (L3), and does not apply CWA within tiers
  while using OWA across transitions. The proposed system's provenance stratification is orthogonal to DeepProbLog's differentiable
  learning paradigm.
- >-
  ProofWriter (Tafjord et al., ACL 2021 Findings) — A generative transformer trained to produce multi-hop proofs over natural
  language theories, supporting both CWA and OWA variants (D*(OWA) allows Unknown answers). ProofWriter is a fully neural
  system that generates proof steps as natural language text; it does not execute SLD resolution, cannot integrate external
  ontologies as a separate knowledge tier, and produces no machine-executable proof traces with epistemic annotations. Used
  in this work as a primary OWA benchmark rather than a baseline architecture; the D*(OWA) dataset with three-valued answers
  (True/False/Unknown) is the most appropriate test for tier-ordered CWA/OWA switching.
- >-
  SARA (Holzenberger, Blair-Stanek & Van Durme, NLLP@KDD 2020; Holzenberger & Van Durme, NLLP 2023) — A statutory reasoning
  benchmark for US federal tax law with gold-standard Prolog KB annotations. The original hand-constructed Prolog system achieves
  100% accuracy. The 2023 paper demonstrates that automated IE for Prolog KB extraction correlates directly with downstream
  statutory reasoning performance. This work uses SARA as a primary evaluation benchmark and as the source of gold annotations
  for Phase 0 extraction calibration.
- >-
  ContractNLI (Koreeda & Manning, EMNLP 2021 Findings) — 607 non-disclosure agreements annotated for document-level NLI with
  evidence spans; each hypothesis is labeled entailed, contradicting, or neutral. Contracts feature complex hedged language
  (negations by exceptions, conditional obligations) identified by the authors as a major source of difficulty. Used in this
  work as a primary legal domain benchmark for hallucination rate evaluation.
inspiration: >-
  The stratified epistemic tier architecture is inspired by three cross-domain analogies that each capture a different aspect
  of the system. (1) Cache hierarchy in computer architecture (L1/L2/L3 cache → main memory → disk swap): retrieve facts from
  the cheapest, most reliable source first — this predicts the system's latency/accuracy trade-off profile (L0 hash lookup
  is effectively free, L1 bounded SLD is microseconds, L2 SPARQL is network-latency, L3 LLM sampling is the costliest). The
  direct consequence: the KB starts populated, not empty. (2) Evidentiary standards in common law (documentary evidence >
  expert testimony > circumstantial inference): courts apply different burdens of proof by evidentiary tier, and conclusions
  citing higher-tier evidence can be challenged if lower-tier evidence was ignored — mapping precisely to the proposed meta-interpreter's
  requirement to exhaust tiers in order. (3) Biba integrity model in secure information flow (information flows typing, computations
  cannot be trusted at higher integrity than their lowest-integrity input): the weakest-link propagation applied to epistemic
  tiers in proof trees. The domain-adaptive L2 ontology selection is inspired by the information retrieval principle of query-time
  index selection: a general index (Wikidata) suffices for common entities, but domain-specific indexes (LKIF's OWL-DL legal
  taxonomy with concepts for norms, obligations, and parties; ConceptNet's commonsense relations for narrative) substantially
  increase recall for bridging facts a generic upper ontology cannot cover.
terms:
- term: Epistemic Provenance Tier
  definition: >-
    A label attached to each Prolog predicate indicating the source and reliability of the fact: L0 = explicitly stated in
    the document (confidence 1.0, pre-populated before any reasoning); L1 = deductively derived from the L0 KB via bounded
    SLD with depth_limit(3), no new predicate invention (confidence 1.0); L2 = entailed by a domain-specific ontology — LKIF
    Core OWL for legal (confidence 0.95 for subsumption), ConceptNet REST for narrative (confidence 0.80 for statistical association
    edges), Wikidata SPARQL for general domain (confidence 0.85); L3 = abduced by the LLM as implicit world knowledge (confidence
    = fraction of K=5 independent yes/no queries that return 'yes').
- term: Document-Grounded KB Initialization
  definition: >-
    The L0 population step that pre-fills the Prolog KB from document-extracted predicates before any reasoning begins, as
    opposed to SymBa's empty-database design. This ensures that facts explicitly stated in the document are retrieved by the
    symbolic solver without LLM involvement, preventing hallucination of document-stated content.
- term: Bounded L1 Deductive Closure
  definition: >-
    The set of Prolog goals provable from the L0 KB alone using SLD resolution with a maximum resolution depth of 3 steps
    and no new predicate invention. Defined operationally as 'one full SWI-Prolog query on the L0 KB with depth_limit(3),
    no LLM access.' This definition is tractable, precisely specifiable, and determines exactly when L2 escalation triggers.
- term: Domain-Adaptive L2 Ontology Selection
  definition: >-
    A runtime policy that selects the L2 knowledge source based on detected document domain: LKIF Core OWL (OWL-DL + SWRL,
    Estrella project) for legal documents — covering legal concepts such as norm, obligation, prohibition, claim, agent, and
    legal document; ConceptNet REST API (IsA/PartOf/UsedFor relations) for narrative/story domains; Wikidata SPARQL for general-domain
    entities. All three are queried before escalation to the LLM.
- term: Weakest-Link Epistemic Propagation
  definition: >-
    The rule for computing the uncertainty tuple of a derived conclusion: Tier(derived) = max_i(Tier(premise_i)); Conf(derived)
    = min_i(Conf(premise_i)). Comparison is lexicographic — tier label takes priority, with confidence breaking ties within
    the same tier. Example: a conclusion with one L0 premise (conf=1.0) and one L2 premise (conf=0.95) propagates as (L2,
    0.95).
- term: Dynamic CWA/OWA Switching
  definition: >-
    The runtime behavior of the meta-interpreter where Closed-World Assumption (CWA: if not provable at this tier, assume
    false) applies within L0–L1, but Open-World Assumption (OWA: if not provable, escalate to next tier) applies at tier boundaries
    L1→L2 and L2→L3. Per-node decision: given a goal G that fails after exhausting depth_limit(3) at tier T, escalate to T+1
    by querying the corresponding source. If T=L3 and L3 confidence < 0.6, return 'unknown' rather than asserting falsity.
    This implements the three-valued semantics used in ProofWriter D*(OWA).
- term: Abductive Schema Template
  definition: >-
    The structured LLM query formulated from an SLD-tree leaf failure node: includes the predicate name, partially-bound arguments,
    and the parent proof goal. Sent K=5 times independently; L3 confidence = fraction of 'yes' responses (self-consistency
    sampling). This operationalizes LLM abduction as a calibrated probabilistic step rather than an uncalibrated oracle call.
- term: Interpretability Comprehension Proxy
  definition: >-
    A timed evaluation protocol replacing subjective preference user studies: domain experts (N≥15) answer 5 yes/no comprehension
    questions about a proof trace within 3 minutes. Measures comprehension accuracy and time-to-first-correct-answer across
    raters, with inter-rater reliability reported as Cohen's kappa. This operationalizes 'interpretability' as a measurable
    cognitive performance metric rather than a subjective preference.
summary: >-
  We propose a neuro-symbolic text-to-reasoning pipeline that, unlike SymBa's empty-database design, pre-populates a Prolog
  KB from document-explicit facts (L0) and enforces tier-ordered SLD resolution through bounded deductive closure (L1), domain-adaptive
  ontology lookup (L2: LKIF for legal, ConceptNet for narrative, Wikidata for general), and LLM abduction (L3, confidence
  via self-consistency sampling) — reducing LLM invocation to a provable last resort and propagating a calibrated (tier, confidence)
  tuple through every proof-tree node for auditable, hallucination-reduced reasoning over short professional documents.
</hypothesis>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: experiment_iter1_dir3
type: experiment
objective: >-
  Implement the complete provenance-stratified pipeline (L0 extraction → L1 bounded SLD → L2 domain-adaptive ontology → L3
  self-consistency LLM abduction) with weakest-link provenance propagation and tier-ordered meta-interpreter, run Phase 0
  extraction calibration on SARA, evaluate all tiers against SymBa-style flat-LLM baseline and CoT baseline across ProofWriter
  D*(OWA), CLUTRR, SARA, and ContractNLI, and compute hallucination rate, multi-hop accuracy, tier distribution, ECE, and
  JSON-LD trace graphs.
approach: >-
  Implementation plan (Python + SWI-Prolog via pyswip): STAGE 0 — L0 Extraction: for each document, prompt an LLM (via OpenRouter,
  use a capable but cost-efficient model such as meta-llama/llama-3.1-70b-instruct) with a structured JSON extraction prompt:
  'Extract all atomic facts from this document as Prolog predicates. Format: [{predicate: str, args: [str], confidence: 1.0,
  tier: l0}]. Output only valid Prolog atom names.' Validate extracted predicates against gold SARA annotations for 25 examples;
  report precision/recall (Phase 0 gate). STAGE 1 — L1 Bounded SLD: load L0 facts into SWI-Prolog KB via pyswip; run query
  with call_with_depth_limit/3 (depth=3); collect provable goals and mark tier=l1,conf=1.0. STAGE 2 — L2 Domain-Adaptive Ontology:
  classify document domain (legal/narrative/general) by keyword heuristic; for legal: load LKIF Core OWL via owlready2, query
  subclass_of/equivalent_class for goal entity arguments, cache hits as tier=l2,conf=0.95; for narrative/general: query ConceptNet
  REST API (https://api.conceptnet.io/query) for IsA/PartOf edges, conf=0.80. STAGE 3 — L3 LLM Abduction: for goals still
  unresolved after L2, send K=5 independent yes/no queries to LLM; L3 conf = yes_count/5; flag conf<0.6 as 'low-confidence';
  store as tier=l3. META-INTERPRETER: implement weakest-link propagation: tier(derived)=max(tier(premises)), conf(derived)=min(conf(premises));
  export derivation tree as JSON-LD with node schema {predicate, args, tier, confidence, source_span}. BASELINES: (a) SymBa-style
  flat baseline: empty Prolog KB, LLM called on every proof failure with same abduction template but without tier routing;
  (b) CoT baseline: send full document + question to LLM with chain-of-thought prompt, extract yes/no answer. METRICS: (i)
  Phase 0 precision/recall on SARA 25 examples; (ii) multi-hop accuracy on ProofWriter D*(OWA) and CLUTRR (exact match True/False/Unknown
  or relation); (iii) hallucination rate — predicates asserted as L0-certain that are absent from document (measure by checking
  if asserted L0 predicate string appears in source document text); (iv) tier distribution — fraction of successful proofs
  using only L0-L2 vs requiring L3; (v) ECE computed by bucketing L3 confidence scores against binary ground truth on SARA.
  Use mini dataset splits first (10%), then scale to full if runtime permits within 6h budget. Track OpenRouter API costs;
  stay under $10 total. Output method_out.json with per-example results and aggregate metrics.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results
</artifact_executor_scope>

<artifact_planning_rules>
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for experiment artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for an EXPERIMENT artifact.",
  "properties": {
    "title": {
      "description": "Short title for the plan",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "implementation_pseudocode": {
      "description": "High-level pseudocode for the experiment implementation",
      "title": "Implementation Pseudocode",
      "type": "string"
    },
    "fallback_plan": {
      "description": "What to do if the primary approach fails - alternative methods, simplified versions",
      "title": "Fallback Plan",
      "type": "string"
    },
    "testing_plan": {
      "description": "How to validate the experiment works: start with small/fast tests, look for confirmation signals before running full-scale experiments",
      "title": "Testing Plan",
      "type": "string"
    }
  },
  "required": [
    "title",
    "implementation_pseudocode",
    "fallback_plan",
    "testing_plan"
  ],
  "title": "ExperimentPlan",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-15 20:07:17 UTC

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

### [4] ASSISTANT · 2026-06-15 20:07:23 UTC

```
I'll research the key technical components needed to make this plan concrete and actionable.
```

### [5] TOOL CALL — Skill · 2026-06-15 20:07:23 UTC

```
aii-web-tools
```

### [6] TOOL RESULT — Skill · 2026-06-15 20:07:23 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [7] TOOL CALL — Skill · 2026-06-15 20:07:23 UTC

```
aii-web-tools
```

### [8] TOOL RESULT — Skill · 2026-06-15 20:07:23 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [9] TOOL CALL — Skill · 2026-06-15 20:07:23 UTC

```
aii-web-tools
```

### [10] TOOL RESULT — Skill · 2026-06-15 20:07:23 UTC

```
{"success": true, "commandName": "aii-web-tools"}
```

### [11] TOOL CALL — ToolSearch · 2026-06-15 20:07:27 UTC

```
{'query': 'select:WebSearch,WebFetch'}
```

### [12] TOOL RESULT — ToolSearch · 2026-06-15 20:07:27 UTC

```
{"matches": ["WebSearch", "WebFetch"], "query": "select:WebSearch,WebFetch", "total_deferred_tools": 20}
```

### [13] TOOL CALL — WebSearch · 2026-06-15 20:07:33 UTC

```
pyswip call_with_depth_limit SWI-Prolog Python interface example
```

### [14] TOOL CALL — WebSearch · 2026-06-15 20:07:33 UTC

```
SARA statutory reasoning benchmark Holzenberger 2020 dataset GitHub
```

### [15] TOOL CALL — WebSearch · 2026-06-15 20:07:33 UTC

```
ProofWriter D* OWA dataset download HuggingFace Allen AI
```

### [16] TOOL CALL — WebSearch · 2026-06-15 20:07:33 UTC

```
owlready2 load OWL ontology query subclasses Python tutorial
```

### [17] TOOL RESULT — WebSearch · 2026-06-15 20:07:39 UTC

```
{"query": "pyswip call_with_depth_limit SWI-Prolog Python interface example", "results": [{"tool_use_id": "srvtoolu_016fMDs2k39AWBWEM9jK6wEo", "content": [{"title": "GitHub - tjvr/pyswip: Use SWI-Prolog from Python. Fork.", "url": "https://github.com/tjvr/pyswip"}, {"title": "GitHub - yuce/pyswip: PySwip is a Python-Prolog interface that enables querying SWI-Prolog in your Python programs. · GitHub", "url": "https://github.com/yuce/pyswip"}, {"title": "GitHub - dsapandora/pyswip: PYSWIP integrator for Python and Swip Prolog · GitHub", "url": "https://github.com/dsapandora/pyswip"}, {"title": "GitHub - SWI-Prolog/packages-swipy: Python interface for SWI-Prolog · GitHub", "url": "https://github.com/SWI-Prolog/packages-swipy"}, {"title": "GitHub - jesg/pyswip: PySWIP is a bridge between Python and SWI-Prolog. (Fork)", "url": "https://github.com/jesg/pyswip"}, {"title": "Interfacing to Python", "url": "https://www.swi-prolog.org/FAQ/Python.md"}, {"title": "pypi.org", "url": "https://pypi.org/project/pyswip/0.1.3/"}, {"title": "github.com", "url": "https://github.com/FForzano/pyswip"}]}, "Based on the search results, I found information about PySwip as a Python-SWI-Prolog interface, but the search results don't contain specific examples for `call_with_depth_limit`. \n\nThe search results show that PySwip is a Python-Prolog interface that enables querying SWI-Prolog in your Python programs, and it features an SWI-Prolog foreign language interface, a utility class that makes it easy querying with Prolog and also a Pythonic interface.\n\nThe results provide examples of basic PySwip usage with `Prolog.query()` and the Pythonic interface using `Functor`, `Variable`, and `Query`, but they don't include documentation or examples specifically for the `call_with_depth_limit` function. \n\nTo find more specific information about `call_with_depth_limit`, you might want to:\n1. Check the official PySwip documentation directly on GitHub\n2. Look at SWI-Prolog's documentation for the `call_with_depth_limit/3` predicate and how it's wrapped in PySwip\n3. Check the PySwip source code for depth limit related functions"], "durationSeconds": 7.818445834999999, "searchCount": 1}
```

### [18] TOOL RESULT — WebSearch · 2026-06-15 20:07:39 UTC

```
{"query": "ProofWriter D* OWA dataset download HuggingFace Allen AI", "results": [{"tool_use_id": "srvtoolu_01RGVq84eqPQSU4Ei7JXf5TE", "content": [{"title": "ProofWriter Dataset", "url": "https://www.emergentmind.com/topics/proofwriter-dataset"}, {"title": "ProofWriter: Generating Implications, Proofs, and Abductive Statements   over Natural Language", "url": "https://arxiv.org/pdf/2012.13048"}, {"title": "Study to Evaluate the Safety, Tolerability, Pharmacokinetics, and Efficacy of AMG 562 in Subjects With r/r Diffuse Large B-cell Lymphoma, Mantle Cell Lymphoma, or Follicular Lymphoma", "url": "https://cdn.clinicaltrials.gov/large-docs/28/NCT03571828/Prot_000.pdf"}, {"title": "Low-Level Laser Therapy for Plantar Fasciitis", "url": "https://cdn.clinicaltrials.gov/large-docs/81/NCT05763381/Prot_SAP_002.pdf"}, {"title": "D3xter1922/proofwriter-dataset · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset"}, {"title": "tasksource/proofwriter · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/tasksource/proofwriter"}, {"title": "renma/ProofWriter · Datasets at Hugging Face", "url": "https://huggingface.co/datasets/renma/ProofWriter"}, {"title": "Selection-Inference: Exploiting Large Language Models for Interpretable   Logical Reasoning", "url": "https://arxiv.org/pdf/2205.09712"}, {"title": "ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language", "url": "https://proofwriter.apps.allenai.org/about"}, {"title": "D3xter1922/proofwriter-dataset at 68a35fc79495cd36f109472e3a3dbbf281e2f10d", "url": "https://huggingface.co/datasets/D3xter1922/proofwriter-dataset/tree/68a35fc79495cd36f109472e3a3dbbf281e2f10d"}]}, "Based on the search results, I found information about the ProofWriter dataset:\n\nProofWriter is a synthetic dataset featuring natural language problems that assess and advance systematic neural logical deduction. The theories are constructed with varying proof depths (\"D0\" to \"D5,\" and the dataset includes both the Closed World Assumption (CWA) and Open World Assumption (OWA) settings.\n\nThe search results show that ProofWriter uses D* datasets, with variants including D*(CWA) and D*(OWA). The D* datasets comprise five datasets, named D0, D1, D2, D3, D5, each containing 100k questions.\n\nFor accessing the dataset on Hugging Face, the search results indicate there are multiple ProofWriter dataset repositories available:\n- `D3xter1922/proofwriter-dataset`\n- `tasksource/proofwriter`\n- `renma/ProofWriter`\n\nThe original ProofWriter project is associated with AI2 (Allen Institute for AI). You can access these datasets directly through Hugging Face's dataset hub using the repository names listed above."], "durationSeconds": 6.346607076000001, "searchCount": 1}
```

### [19] TOOL RESULT — WebSearch · 2026-06-15 20:07:39 UTC

```
{"query": "SARA statutory reasoning benchmark Holzenberger 2020 dataset GitHub", "results": [{"tool_use_id": "srvtoolu_01BpYp5zijgPc81qKFv6tSZX", "content": [{"title": "Bringing order into the realm of Transformer-based language models for   artificial intelligence and law", "url": "https://arxiv.org/pdf/2308.05502"}, {"title": "Language Models and Logic Programs for Trustworthy Financial Reasoning", "url": "https://arxiv.org/html/2508.21051v2"}, {"title": "[PDF] A Dataset for Statutory Reasoning in Tax Law Entailment and Question Answering | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/A-Dataset-for-Statutory-Reasoning-in-Tax-Law-and-Holzenberger-Blair-Stanek/008209015471fc685e6ceb6a478693f878c9d778"}, {"title": "Language Models and Logic Programs for Trustworthy Tax Reasoning", "url": "https://arxiv.org/pdf/2508.21051"}, {"title": "LegalBench: A Collaboratively Built Benchmark for Measuring Legal   Reasoning in Large Language Models", "url": "https://arxiv.org/pdf/2308.11462"}, {"title": "Factoring Statutory Reasoning as Language Understanding Challenges", "url": "https://arxiv.org/pdf/2105.07903"}, {"title": "Connecting Symbolic Statutory Reasoning with Legal ...", "url": "https://aclanthology.org/2023.nllp-1.12.pdf"}, {"title": "GitHub - SgfdDttt/sara: StAtutory Reasoning Assessment", "url": "https://github.com/SgfdDttt/sara"}, {"title": "OpenExempt: A Diagnostic Benchmark for Legal Reasoning and a Framework for Creating Custom Benchmarks on Demand", "url": "https://arxiv.org/pdf/2601.13183"}, {"title": "Natural Legal Language Processing at JHU", "url": "https://nlp.jhu.edu/law/"}]}, "Based on the search results, here's what I found about the SARA statutory reasoning benchmark:\n\n## Overview\n\nSARA is a dataset for statutory reasoning on US tax law created by Holzenberger et al., 2020, comprised of a set of rules extracted from the statutes of the US Internal Revenue Code (IRC), along with a set of questions which would require to refer to the rules for being answered correctly.\n\n## Dataset Details\n\nSARA contains 9 sections, taken from US federal tax law statutes, pruned and simplified; and hand-crafted cases that test the understanding of those 9 sections. The dataset includes 37k task instances based on real-world rules and crowd-generated questions and scenarios.\n\nThere are two SARA tasks: sara_entailment, which corresponds to the entailment cases, and sara_numeric, which consists of the numeric cases.\n\n## GitHub Repository\n\nThe dataset and Prolog program can be found on GitHub, along with the paper. The repository is located at: **https://github.com/SgfdDttt/sara**\n\nThe repository includes instructions to install required Python packages and download/format the dataset by running bash code/make_dataset.sh."], "durationSeconds": 7.263319187999998, "searchCount": 1}
```

### [20] TOOL RESULT — WebSearch · 2026-06-15 20:07:39 UTC

````
{"query": "owlready2 load OWL ontology query subclasses Python tutorial", "results": [{"tool_use_id": "srvtoolu_01DivXbwwZ9modpo9Z2qr5Qv", "content": [{"title": "Welcome to Owlready2’s documentation! — Owlready2 0.47 documentation", "url": "https://owlready2.readthedocs.io/en/v0.47/"}, {"title": "Welcome to Owlready2’s documentation! — Owlready2 0.50 documentation", "url": "https://owlready2.readthedocs.io/"}, {"title": "owlready2 · PyPI", "url": "https://pypi.org/project/owlready2/0.7/"}, {"title": "(PDF) Owlready: Ontology-oriented programming in Python with automatic classification and high level constructs for biomedical ontologies", "url": "https://www.researchgate.net/publication/319126534_Owlready_Ontology-oriented_programming_in_Python_with_automatic_classification_and_high_level_constructs_for_biomedical_ontologies"}, {"title": "Managing ontologies — Owlready 0.2 documentation", "url": "https://pythonhosted.org/Owlready/onto.html"}, {"title": "Managing ontologies — Owlready2 0.50 documentation", "url": "https://owlready2.readthedocs.io/en/latest/onto.html"}, {"title": "Classes and Individuals (Instances) — Owlready2 0.50 documentation", "url": "https://owlready2.readthedocs.io/en/latest/class.html"}, {"title": "Introduction — Owlready2 0.50 documentation", "url": "https://owlready2.readthedocs.io/en/latest/intro.html"}, {"title": "github.com", "url": "https://github.com/csse-uoft/owlready2"}, {"title": "github.com", "url": "https://github.com/pwin/owlready2"}]}, "The search results provide comprehensive information about Owlready2 for working with OWL ontologies in Python. Here's what you need to know:\n\n## Loading OWL Ontologies\n\nOwlready2 is a package for ontology-oriented programming in Python that can load OWL 2.0 ontologies as Python objects, modify them, save them, and perform reasoning via HermiT.\n\nTo load an ontology, you use the following basic pattern:\n\nThe `get_ontology()` function returns an ontology from its IRI and creates a new empty ontology if needed, while the `.load()` method loads the ontology from a local copy or from Internet. Here's an example:\n\n```python\nfrom owlready2 import *\nonto_path.append(\"/path/to/your/local/ontology/repository\")\nonto = get_ontology(\"http://www.lesfleursdunormal.fr/static/_downloads/pizza_onto.owl\")\nonto.load()\n```\n\nIt is safe to call `.load()` several times on the same ontology, as it will be loaded only once.\n\n## Querying Subclasses\n\nThe `.subclasses()` method returns the list of direct subclasses of a class. For example:\n\n```python\nprint(Drug.subclasses())\n```\n\nThe `.descendants()` and `.ancestors()` Class methods return a set of the descendant and ancestor Classes (including self, but excluding non-entity classes such as restrictions).\n\n## Supported Formats\n\nOwlready2 can import OWL 2.0 ontologies in NTriples, RDF/XML or OWL/XML format."], "durationSeconds": 6.851370375999999, "searchCount": 1}
````

### [21] TOOL CALL — WebSearch · 2026-06-15 20:07:46 UTC

```
CLUTRR dataset kinship reasoning HuggingFace download format
```

### [22] TOOL CALL — WebSearch · 2026-06-15 20:07:46 UTC

```
LKIF Core OWL ontology download Estrella project URL
```

### [23] TOOL CALL — WebSearch · 2026-06-15 20:07:46 UTC

```
ContractNLI dataset download EMNLP 2021 Koreeda Manning
```

### [24] TOOL RESULT — WebSearch · 2026-06-15 20:07:52 UTC

```
{"query": "ContractNLI dataset download EMNLP 2021 Koreeda Manning", "results": [{"tool_use_id": "srvtoolu_01GPDBj1nAWqMv1NS5GgpL3N", "content": [{"title": "ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts - ACL Anthology", "url": "https://aclanthology.org/2021.findings-emnlp.164/"}, {"title": "ContractNLI | ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts", "url": "https://stanfordnlp.github.io/contract-nli/"}, {"title": "[PDF] ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/ContractNLI:-A-Dataset-for-Document-level-Natural-Koreeda-Manning/0a1ff1d4102d94a50f8862f60bc2ac21f36ad592"}, {"title": "ContractNLI Dataset - GM-RKB", "url": "https://www.gabormelli.com/RKB/ContractNLI_Dataset"}, {"title": "A Dataset for Document-level Natural Language Inference ...", "url": "https://aclanthology.org/2021.findings-emnlp.164.pdf"}, {"title": "Figure 1 from ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts | Semantic Scholar", "url": "https://www.semanticscholar.org/paper/ContractNLI:-A-Dataset-for-Document-level-Natural-Koreeda-Manning/0a1ff1d4102d94a50f8862f60bc2ac21f36ad592/figure/0"}, {"title": "GitHub - stanfordnlp/contract-nli-bert: A baseline system for ContractNLI (https://stanfordnlp.github.io/contract-nli/) · GitHub", "url": "https://github.com/stanfordnlp/contract-nli-bert"}, {"title": "CoLT5: Faster Long-Range Transformers with Conditional Computation", "url": "https://arxiv.org/pdf/2303.09752"}, {"title": "Learning to Generate Instruction Tuning Datasets for Zero-Shot Task   Adaptation", "url": "https://arxiv.org/pdf/2402.18334"}, {"title": "[2110.01799] ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts", "url": "https://arxiv.org/abs/2110.01799"}]}, "Based on the search results, I found comprehensive information about the ContractNLI dataset:\n\n## ContractNLI Dataset Overview\n\nContractNLI is a dataset for document-level natural language inference for contracts published by Koreeda and Manning in the Findings of the Association for Computational Linguistics: EMNLP 2021.\n\n## Dataset Details\n\nThe dataset consists of 607 annotated contracts. In this task, a system is given a set of hypotheses (such as \"Some obligations of Agreement may survive termination.\") and a contract, and it is asked to classify whether each hypothesis is entailed by, contradicting to or not mentioned by (neutral to) the contract as well as identifying evidence for the decision as spans in the contract.\n\n## Where to Access\n\nThe official resources are available at:\n- The paper can be found at https://aclanthology.org/2021.findings-emnlp.164\n- The Stanford NLP website at https://stanfordnlp.github.io/contract-nli/\n- A baseline system is available at https://github.com/stanfordnlp/contract-nli-bert\n\nFor questions regarding the dataset, you can contact koreeda@stanford.edu or create an issue in the repository."], "durationSeconds": 5.551928408, "searchCount": 1}
```

### [25] TOOL RESULT — WebSearch · 2026-06-15 20:07:54 UTC

```
{"query": "CLUTRR dataset kinship reasoning HuggingFace download format", "results": [{"tool_use_id": "srvtoolu_01V8HayT7uDtLgsfEq57LYfz", "content": [{"title": "GitHub - kliang5/CLUTRR_huggingface_dataset", "url": "https://github.com/kliang5/CLUTRR_huggingface_dataset"}, {"title": "CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text | Request PDF", "url": "https://www.researchgate.net/publication/336997708_CLUTRR_A_Diagnostic_Benchmark_for_Inductive_Reasoning_from_Text"}, {"title": "Compositional Language Understanding with Text-based Relational   Reasoning", "url": "https://arxiv.org/pdf/1811.02959"}, {"title": "PBEBench: A Multi-Step Programming by Examples Reasoning Benchmark inspired by Historical Linguistics", "url": "https://arxiv.org/pdf/2505.23126"}, {"title": "Improved Logical Reasoning of Language Models via Differentiable   Symbolic Programming", "url": "https://arxiv.org/pdf/2305.03742"}, {"title": "Extracting and Following Paths for Robust Relational Reasoning with Large Language Models", "url": "https://arxiv.org/pdf/2412.17963"}, {"title": "Learning Reasoning Strategies in End-to-End Differentiable Proving", "url": "https://arxiv.org/pdf/2007.06477"}, {"title": "Better Set Representations For Relational Reasoning", "url": "https://arxiv.org/pdf/2003.04448"}, {"title": "CLUTRR (CLUTRR)", "url": "https://huggingface.co/CLUTRR"}]}, "Based on the search results, here's information about the CLUTRR dataset and its format:\n\n## Dataset Overview\n\nCLUTRR is a benchmark where, given a text-based story describing a subset of a kinship graph, the goal is to predict the relationship between two entities whose relationship is not stated in the story.\n\n## Data Format\n\nEach instance contains: an id (unique identifier), story (semi-synthetic story involving hypothetical families), query (target query/relation with two names), target (indicator for the correct relation), and target_text (text for the correct relation). The target indicator follows a mapping where relations like \"aunt\" = 0, \"son-in-law\" = 1, \"grandfather\" = 2, continuing through to \"sister-in-law\" = 20.\n\nAdditional fields include clean_story (the story without noise factors), proof_state (the logical rule of the kinship generation), f_comb (the kinships of the query followed by the logical rule), and task_name (the task of the sub-dataset).\n\n## HuggingFace Access\n\nThe CLUTRR dataset is available on HuggingFace, with test sets provided by the authors. You can find the CLUTRR organization on HuggingFace at https://huggingface.co/CLUTRR, and there's also a community implementation available at https://github.com/kliang5/CLUTRR_huggingface_dataset."], "durationSeconds": 7.9775258629999986, "searchCount": 1}
```

### [26] TOOL RESULT — WebSearch · 2026-06-15 20:07:54 UTC

```
{"query": "LKIF Core OWL ontology download Estrella project URL", "results": [{"tool_use_id": "srvtoolu_01GyuYdipaWaBVKrLkS4JaTS", "content": [{"title": "LKIF-Core Ontology: A Commonsense-based Legal Ontology", "url": "http://www.estrellaproject.org/lkif-core/"}, {"title": "LKIF-Core Ontology by Estrella on TriplyDB", "url": "https://triplydb.com/estrella/lkif"}, {"title": "Leibniz Center for Law » LKIF Core Ontology", "url": "http://www.leibnizcenter.org/general/lkif-core-ontology"}, {"title": "lkif-core/lkif-extended.owl at master · RinkeHoekstra/lkif-core", "url": "https://github.com/RinkeHoekstra/lkif-core/blob/master/lkif-extended.owl"}, {"title": "lkif-core/lkif-core.owl at master · RinkeHoekstra/lkif-core", "url": "https://github.com/RinkeHoekstra/lkif-core/blob/master/lkif-core.owl"}, {"title": "lkif-core/mereology.owl at master · RinkeHoekstra/lkif-core", "url": "https://github.com/RinkeHoekstra/lkif-core/blob/master/mereology.owl"}, {"title": "Legal Knowledge Interchange Format", "url": "https://en.wikipedia.org/wiki/Legal_Knowledge_Interchange_Format"}, {"title": "GitHub - RinkeHoekstra/lkif-core: The LKIF Core Ontology of Basic Legal Concepts · GitHub", "url": "https://github.com/RinkeHoekstra/lkif-core"}]}, "Based on the search results, here's the information about the LKIF Core OWL ontology from the Estrella project:\n\n**Main Project URL:**\nThe LKIF Core ontology can be accessed at http://www.estrellaproject.org/lkif-core/\n\n**Download and Access:**\nYou can download the latest version of the LKIF Core ontology directly from lkif-core-1.0.3-dist.zip, or import the ontology from its base URI: http://www.estrellaproject.org/lkif-core/lkif-core.owl\n\n**Project Information:**\nThe LKIF-Core is an OWL ontology of basic legal concepts developed as Deliverable 1.4 of the Estrella project in 2007. This ontology was developed within the ESTRELLA project to provide a standard vocabulary for legal reasoning services on the Semantic Web.\n\n**Alternative Sources:**\nYou can also find the LKIF-Core ontology on GitHub at https://github.com/RinkeHoekstra/lkif-core and on TriplyDB at https://triplydb.com/estrella/lkif"], "durationSeconds": 7.578258313999998, "searchCount": 1}
```

### [27] ASSISTANT · 2026-06-15 20:10:51 UTC

```
I have enough information to write the detailed plan now.
```

### [28] TOOL CALL — Write · 2026-06-15 20:10:51 UTC

````
File: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json

{
  "title": "Provenance-Stratified Neuro-Symbolic Pipeline: L0-L3 Tier-Ordered SLD with SARA/CLUTRR/ProofWriter/ContractNLI Evaluation",
  "summary": "Implement and evaluate a complete 4-tier neuro-symbolic reasoning pipeline (L0 document extraction, L1 bounded SLD, L2 domain-adaptive ontology, L3 self-consistency LLM abduction) with weakest-link provenance propagation, against a SymBa-style flat-LLM baseline and CoT baseline, across four benchmarks: SARA, ProofWriter D*(OWA), CLUTRR, and ContractNLI.",
  "runpod_compute_profile": "cpu_heavy",
  "implementation_pseudocode": "## File layout\n```\nmethod.py             # main entrypoint, orchestrates all phases\npipeline/\n  l0_extractor.py    # LLM-based L0 Prolog predicate extraction\n  l1_prolog.py       # SWI-Prolog interface via pyswip, depth-limited SLD\n  l2_ontology.py     # owlready2 LKIF + ConceptNet REST for L2 bridging\n  l3_abduction.py    # K=5 self-consistency LLM abduction\n  meta_interpreter.py # tier-ordered resolution + weakest-link propagation\n  trace.py           # JSON-LD derivation tree builder\nbaselines/\n  symba_baseline.py  # empty-KB flat LLM on every proof failure\n  cot_baseline.py    # chain-of-thought LLM, extract yes/no answer\ndatasets/\n  sara_loader.py     # load SARA from github.com/SgfdDttt/sara\n  proofwriter_loader.py  # load tasksource/proofwriter from HuggingFace\n  clutrr_loader.py   # load CLUTRR from HuggingFace CLUTRR org\n  contractnli_loader.py  # load from stanfordnlp.github.io/contract-nli\nmetrics/\n  hallucination.py   # string-match L0 assertions vs source document\n  ece.py             # bucketed ECE for L3 confidence vs binary ground truth\n  tier_distribution.py  # fraction of proofs using only L0-L2\nmethod_out.json       # final output\n```\n\n## PHASE 0 — SARA Extraction Calibration (must run first, acts as gate)\n\n### Setup\n```python\n# Install: uv add pyswip owlready2 requests datasets openai-compatible httpx\n# SWI-Prolog must be installed system-wide: apt-get install swi-prolog\n# Verify: from pyswip import Prolog; p = Prolog(); list(p.query('true'))\n```\n\n### Load SARA\n```python\n# Clone: git clone https://github.com/SgfdDttt/sara\n# Repo structure: sara/prolog/ has gold .pl files per case; sara/cases/ has text descriptions\n# Load 25 random cases:\nimport glob, random\ncases = glob.glob('sara/cases/*.txt')  # each file is ~3000 char document\ngold_pls = glob.glob('sara/prolog/*.pl')  # matching gold Prolog KB\n# Pair by filename stem\npaired = [(c, c.replace('cases/', 'prolog/').replace('.txt', '.pl')) for c in cases]\nsampled = random.sample(paired, 25)\n```\n\n### L0 Extraction Prompt (use meta-llama/llama-3.1-70b-instruct via OpenRouter)\n```python\nEXTRACTION_PROMPT = '''\nYou are a Prolog knowledge engineer. Extract ALL atomic facts from the following legal document as Prolog predicates.\nRules:\n- Use lowercase snake_case for predicate names and all atom arguments\n- No variables (start with uppercase) in extracted facts — only ground atoms\n- Each fact must correspond to something EXPLICITLY stated in the document, not inferred\n- Format each fact as valid Prolog: predicate_name(arg1, arg2, ...) with no spaces inside\nOutput ONLY a JSON array of objects, each with keys:\n  {\"predicate\": str, \"args\": [str, ...], \"source_span\": str, \"confidence\": 1.0, \"tier\": \"l0\"}\nDocument:\n{document}\n'''\n```\n\n### Evaluate vs gold\n```python\n# Parse gold .pl file: extract head/1 facts and rule heads\n# For precision: fraction of extracted predicates whose string form appears in gold .pl\n# For recall: fraction of gold .pl ground facts covered by extracted set\n# Report per-case and aggregate precision/recall\n# GATE: if precision < 0.75 across 25 examples:\n#   Iterate with few-shot examples (add 3 gold-annotated examples to prompt)\n#   Re-evaluate; if still < 0.75 use constrained JSON + type constraints\n#   Max 3 iterations; log all results; proceed regardless but flag\n```\n\n## PHASE 1 — PIPELINE ARCHITECTURE\n\n### L0 Extractor (pipeline/l0_extractor.py)\n```python\nfrom openai import OpenAI  # OpenRouter compatible\nimport json, re\n\nclient = OpenAI(base_url='https://openrouter.ai/api/v1', api_key=OPENROUTER_KEY)\n\ndef extract_l0(document: str, domain: str = 'general') -> list[dict]:\n    # Select domain-adapted prompt (add legal examples for legal docs)\n    prompt = EXTRACTION_PROMPT.format(document=document[:4000])\n    resp = client.chat.completions.create(\n        model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': prompt}],\n        temperature=0.0, max_tokens=2000\n    )\n    raw = resp.choices[0].message.content\n    # Extract JSON array from response (allow markdown code block)\n    match = re.search(r'\\[.*?\\]', raw, re.DOTALL)\n    facts = json.loads(match.group()) if match else []\n    # Validate: predicate is valid Prolog atom (lowercase, alphanumeric+underscore)\n    valid = [f for f in facts if re.match(r'^[a-z][a-z0-9_]*$', f['predicate'])\n             and all(re.match(r'^[a-z0-9_]+$', a) for a in f['args'])]\n    return valid  # list of {predicate, args, source_span, confidence:1.0, tier:'l0'}\n```\n\n### L1 Bounded SLD (pipeline/l1_prolog.py)\n```python\nfrom pyswip import Prolog\n\nclass PrologKB:\n    def __init__(self):\n        self.prolog = Prolog()\n        self.facts = []  # list of (predicate, args, tier, conf)\n    \n    def load_l0_facts(self, facts: list[dict]):\n        for f in facts:\n            atom = f[\"predicate\"] + '(' + ','.join(f[\"args\"]) + ')'\n            self.prolog.assertz(atom)\n            self.facts.append((f['predicate'], f['args'], 'l0', 1.0))\n    \n    def load_l0_rules(self, rules: list[str]):\n        # rules as plain Prolog strings, e.g. 'parent(X,Y) :- father(X,Y)'\n        for r in rules:\n            self.prolog.assertz(r)\n    \n    def query_with_depth_limit(self, goal: str, depth: int = 3) -> tuple[bool, str]:\n        # SWI-Prolog call_with_depth_limit/3:\n        # call_with_depth_limit(Goal, Limit, Result)\n        # Result = depth_limit_exceeded | integer (steps used) | false\n        query = f'call_with_depth_limit(({goal}), {depth}, Result)'\n        try:\n            solutions = list(self.prolog.query(query))\n            if solutions and solutions[0].get('Result') != 'depth_limit_exceeded':\n                return True, 'l1'\n            return False, 'depth_limit_exceeded'\n        except Exception:\n            return False, 'error'\n    \n    def assert_l1_derived(self, predicate: str, args: list[str]):\n        atom = predicate + '(' + ','.join(args) + ')'\n        self.prolog.assertz(atom)\n        self.facts.append((predicate, args, 'l1', 1.0))\n```\n\n### L2 Domain-Adaptive Ontology (pipeline/l2_ontology.py)\n```python\nimport requests\nfrom owlready2 import get_ontology, onto_path\n\nLKIF_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl'\nLKIF_EXTENDED_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-extended.owl'\n\ndef load_lkif() -> object:\n    onto = get_ontology(LKIF_URL)\n    onto.load()\n    return onto\n\ndef query_lkif_subsumption(onto, concept_name: str) -> list[str]:\n    # Find class matching concept_name (case-insensitive fuzzy match)\n    matched = [c for c in onto.classes() \n               if concept_name.lower() in c.name.lower()]\n    if not matched:\n        return []\n    cls = matched[0]\n    # Return all ancestor class names (broader concepts)\n    return [a.name for a in cls.ancestors() if a is not cls]\n\ndef query_conceptnet(entity: str, relation: str = 'IsA') -> list[tuple[str, float]]:\n    # ConceptNet REST API\n    url = f'https://api.conceptnet.io/query?node=/c/en/{entity}&rel=/r/{relation}&limit=10'\n    resp = requests.get(url, timeout=10)\n    if resp.status_code != 200:\n        return []\n    edges = resp.json().get('edges', [])\n    results = []\n    for e in edges:\n        end = e.get('end', {}).get('label', '')\n        weight = e.get('weight', 1.0)\n        # Normalize: ConceptNet weights typically 1.0-10.0; cap confidence at 0.80\n        conf = min(0.80, weight / 10.0 + 0.70)\n        results.append((end, conf))\n    return results\n\ndef classify_domain(document: str) -> str:\n    legal_keywords = ['contract', 'obligation', 'party', 'law', 'statute',\n                      'agreement', 'liability', 'clause', 'provision', 'plaintiff']\n    narrative_keywords = ['story', 'character', 'once upon', 'family', 'village']\n    legal_score = sum(1 for kw in legal_keywords if kw in document.lower())\n    narrative_score = sum(1 for kw in narrative_keywords if kw in document.lower())\n    if legal_score >= 3:\n        return 'legal'\n    elif narrative_score >= 2:\n        return 'narrative'\n    return 'general'\n\ndef query_l2(goal_predicate: str, goal_args: list[str], domain: str,\n             onto=None) -> list[dict]:\n    results = []\n    if domain == 'legal' and onto is not None:\n        # Try to match args against LKIF concepts\n        for arg in goal_args:\n            ancestors = query_lkif_subsumption(onto, arg)\n            for anc in ancestors:\n                results.append({\n                    'predicate': f'is_a',\n                    'args': [arg, anc.lower()],\n                    'tier': 'l2', 'confidence': 0.95,\n                    'source': 'lkif'\n                })\n    else:\n        for arg in goal_args:\n            cn_results = query_conceptnet(arg.replace('_', ' '))\n            for label, conf in cn_results:\n                results.append({\n                    'predicate': 'is_a',\n                    'args': [arg, label.lower().replace(' ', '_')],\n                    'tier': 'l2', 'confidence': conf,\n                    'source': 'conceptnet'\n                })\n    return results\n```\n\n### L3 LLM Abduction (pipeline/l3_abduction.py)\n```python\nABDUCTION_PROMPT = '''\nDocument excerpt:\n{document_excerpt}\n\nQuestion: Based ONLY on the document above, does the following hold?\n{predicate}({args})\nAnswer with exactly 'yes' or 'no', followed by one sentence justification.\n'''\n\ndef abduce_l3(predicate: str, args: list[str], document: str,\n              K: int = 5) -> dict:\n    yes_count = 0\n    justifications = []\n    for _ in range(K):\n        resp = client.chat.completions.create(\n            model='meta-llama/llama-3.1-70b-instruct',\n            messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n                document_excerpt=document[:2000],\n                predicate=predicate,\n                args=', '.join(args)\n            )}],\n            temperature=0.7,  # slight temperature for sampling diversity\n            max_tokens=100\n        )\n        answer = resp.choices[0].message.content.strip().lower()\n        if answer.startswith('yes'):\n            yes_count += 1\n        justifications.append(answer)\n    confidence = yes_count / K\n    return {\n        'predicate': predicate, 'args': args,\n        'tier': 'l3', 'confidence': confidence,\n        'low_confidence': confidence < 0.6,\n        'K': K, 'yes_count': yes_count,\n        'justifications': justifications\n    }\n```\n\n### Meta-Interpreter with Weakest-Link Propagation (pipeline/meta_interpreter.py)\n```python\nTIER_ORDER = {'l0': 0, 'l1': 1, 'l2': 2, 'l3': 3, 'unknown': 4}\n\nclass MetaInterpreter:\n    def __init__(self, kb: PrologKB, l2_module, l3_module, domain: str,\n                 document: str, lkif_onto=None):\n        self.kb = kb\n        self.l2 = l2_module\n        self.l3 = l3_module\n        self.domain = domain\n        self.document = document\n        self.lkif_onto = lkif_onto\n        self.proof_tree = []  # list of nodes for JSON-LD export\n    \n    def propagate(self, premises: list[dict]) -> dict:\n        # Weakest-link: tier = max tier (by TIER_ORDER), conf = min conf\n        max_tier = max(premises, key=lambda p: TIER_ORDER[p['tier']])['tier']\n        min_conf = min(p['confidence'] for p in premises)\n        return {'tier': max_tier, 'confidence': min_conf}\n    \n    def prove(self, predicate: str, args: list[str],\n              depth: int = 0) -> dict:\n        goal_str = predicate + '(' + ','.join(args) + ')'\n        node = {'goal': goal_str, 'predicate': predicate, 'args': args}\n        \n        # Try L0/L1 via pyswip with depth limit\n        proved, tier = self.kb.query_with_depth_limit(goal_str, depth=3)\n        if proved:\n            node.update({'tier': tier, 'confidence': 1.0, 'method': 'sld'})\n            self.proof_tree.append(node)\n            return node\n        \n        # Try L2\n        l2_facts = self.l2.query_l2(\n            predicate, args, self.domain, self.lkif_onto\n        )\n        if l2_facts:\n            best = max(l2_facts, key=lambda f: f['confidence'])\n            # Assert into KB for future use\n            self.kb.prolog.assertz(\n                best['predicate'] + '(' + ','.join(best['args']) + ')'\n            )\n            node.update(best)\n            self.proof_tree.append(node)\n            return node\n        \n        # Try L3\n        if depth <= 2:  # avoid L3 in deep sub-proofs\n            l3_result = self.l3.abduce_l3(predicate, args, self.document)\n            if l3_result['confidence'] >= 0.6:\n                self.kb.prolog.assertz(goal_str)\n                node.update(l3_result)\n            else:\n                node.update({'tier': 'unknown', 'confidence': 0.0,\n                             'low_confidence': True})\n            self.proof_tree.append(node)\n            return node\n        \n        node.update({'tier': 'unknown', 'confidence': 0.0})\n        self.proof_tree.append(node)\n        return node\n    \n    def get_trace(self) -> list[dict]:\n        return self.proof_tree\n```\n\n### JSON-LD Trace Export (pipeline/trace.py)\n```python\ndef build_jsonld(proof_tree: list[dict], doc_id: str) -> dict:\n    TIER_COLORS = {'l0': 'green', 'l1': 'yellow', 'l2': 'orange',\n                   'l3': 'red', 'unknown': 'gray'}\n    nodes = []\n    for i, node in enumerate(proof_tree):\n        nodes.append({\n            '@id': f'node:{doc_id}:{i}',\n            '@type': 'ProofNode',\n            'predicate': node.get('predicate', ''),\n            'args': node.get('args', []),\n            'tier': node.get('tier', 'unknown'),\n            'confidence': node.get('confidence', 0.0),\n            'color': TIER_COLORS.get(node.get('tier', 'unknown'), 'gray'),\n            'source_span': node.get('source_span', ''),\n            'method': node.get('method', 'abduction')\n        })\n    return {\n        '@context': {'@vocab': 'https://schema.org/'},\n        '@type': 'ProofTrace',\n        'document_id': doc_id,\n        'nodes': nodes\n    }\n```\n\n## PHASE 2 — BASELINES\n\n### SymBa-style flat baseline (baselines/symba_baseline.py)\n```python\n# Empty KB; for every proof-failure goal, call LLM once (K=1, no tier routing)\ndef symba_prove(predicate: str, args: list[str], document: str,\n                kb: PrologKB) -> dict:\n    proved, _ = kb.query_with_depth_limit(\n        predicate + '(' + ','.join(args) + ')', depth=3\n    )\n    if proved:\n        return {'tier': 'sld', 'confidence': 1.0, 'proved': True}\n    # LLM immediately, no ontology tier\n    resp = client.chat.completions.create(\n        model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\n            document_excerpt=document[:2000],\n            predicate=predicate, args=', '.join(args)\n        )}],\n        temperature=0.0, max_tokens=100\n    )\n    answer = resp.choices[0].message.content.strip().lower()\n    return {'tier': 'llm', 'confidence': 1.0 if answer.startswith('yes') else 0.0,\n            'proved': answer.startswith('yes'), 'no_provenance': True}\n```\n\n### CoT baseline (baselines/cot_baseline.py)\n```python\nCOT_PROMPT = '''\nDocument:\n{document}\n\nQuestion: {question}\nThink step by step, then answer True, False, or Unknown.\n'''\ndef cot_answer(document: str, question: str) -> str:\n    resp = client.chat.completions.create(\n        model='meta-llama/llama-3.1-70b-instruct',\n        messages=[{'role': 'user', 'content': COT_PROMPT.format(\n            document=document[:3000], question=question)}],\n        temperature=0.0, max_tokens=500\n    )\n    raw = resp.choices[0].message.content\n    # Extract final answer\n    for ans in ['True', 'False', 'Unknown']:\n        if ans.lower() in raw.lower().split()[-10:]:\n            return ans\n    return 'Unknown'\n```\n\n## PHASE 3 — DATASET LOADERS\n\n### ProofWriter (datasets/proofwriter_loader.py)\n```python\nfrom datasets import load_dataset\ndef load_proofwriter_owa(split='validation', max_examples=200):\n    # Use tasksource/proofwriter, filter to OWA (depth_5_owa or depth-5-OWA)\n    ds = load_dataset('tasksource/proofwriter', split=split)\n    # Filter for D*(OWA) subset with 3-valued answers\n    owa = [ex for ex in ds if ex.get('answer') in ['True','False','Unknown']]\n    return owa[:max_examples]\n    # Each example: {'context': str, 'question': str, 'answer': 'True'|'False'|'Unknown'}\n    # context is a short theory (facts + rules as natural language sentences)\n    # question is the query sentence\n```\n\n### CLUTRR (datasets/clutrr_loader.py)\n```python\nfrom datasets import load_dataset\ndef load_clutrr(split='test', max_examples=200):\n    ds = load_dataset('CLUTRR/v1', split=split)  # or specific config\n    # Each: {'story': str, 'query': [entity1, entity2], 'target_text': str}\n    return list(ds)[:max_examples]\n```\n\n### SARA (datasets/sara_loader.py)\n```python\nimport os, glob\ndef load_sara(sara_dir='sara', max_examples=50):\n    cases = []\n    for txt_file in glob.glob(os.path.join(sara_dir, 'cases', '*.txt')):\n        stem = os.path.splitext(os.path.basename(txt_file))[0]\n        pl_file = os.path.join(sara_dir, 'prolog', stem + '.pl')\n        if os.path.exists(pl_file):\n            cases.append({\n                'id': stem,\n                'document': open(txt_file).read(),\n                'gold_prolog': open(pl_file).read(),\n                'answer': 'entailed'  # determine from .pl query result\n            })\n    return cases[:max_examples]\n```\n\n### ContractNLI (datasets/contractnli_loader.py)\n```python\nimport json\ndef load_contractnli(data_dir='contract-nli', split='test', max_contracts=50):\n    # Download from stanfordnlp.github.io/contract-nli/\n    # JSON format: {documents: [{text, annotation_sets: [{annotations: {nda-1: {choice, spans}}}]}]}\n    with open(os.path.join(data_dir, f'{split}.json')) as f:\n        data = json.load(f)\n    examples = []\n    for doc in data['documents'][:max_contracts]:\n        text = doc['text']\n        for ann_set in doc.get('annotation_sets', []):\n            for hyp_id, ann in ann_set.get('annotations', {}).items():\n                examples.append({\n                    'document': text[:3000],\n                    'hypothesis': hyp_id,\n                    'label': ann['choice'],  # 'Entailment'|'Contradiction'|'NotMentioned'\n                    'evidence_spans': ann.get('spans', [])\n                })\n    return examples\n```\n\n## PHASE 4 — METRICS\n\n### Hallucination Rate (metrics/hallucination.py)\n```python\ndef compute_hallucination_rate(proof_trees: list[list[dict]],\n                               documents: list[str]) -> float:\n    # For each L0-tier fact in the proof tree, check if predicate string\n    # or its args appear literally in the source document\n    hallucinated = 0\n    total_l0 = 0\n    for tree, doc in zip(proof_trees, documents):\n        doc_lower = doc.lower()\n        for node in tree:\n            if node.get('tier') == 'l0':\n                total_l0 += 1\n                fact_str = node.get('predicate', '') + ' ' + ' '.join(node.get('args', []))\n                # Check if any arg or predicate keyword appears in doc\n                args_in_doc = any(arg.replace('_', ' ') in doc_lower\n                                  for arg in node.get('args', []))\n                if not args_in_doc:\n                    hallucinated += 1\n    return hallucinated / total_l0 if total_l0 > 0 else 0.0\n```\n\n### ECE (metrics/ece.py)\n```python\nimport numpy as np\ndef compute_ece(confidences: list[float], labels: list[int],\n                n_bins: int = 10) -> float:\n    bins = np.linspace(0, 1, n_bins + 1)\n    ece = 0.0\n    n = len(confidences)\n    for b in range(n_bins):\n        lo, hi = bins[b], bins[b+1]\n        mask = [(lo <= c < hi) for c in confidences]\n        if not any(mask):\n            continue\n        bin_confs = [c for c, m in zip(confidences, mask) if m]\n        bin_labels = [l for l, m in zip(labels, mask) if m]\n        avg_conf = np.mean(bin_confs)\n        frac_pos = np.mean(bin_labels)\n        ece += (len(bin_confs) / n) * abs(avg_conf - frac_pos)\n    return ece\n```\n\n## PHASE 5 — MAIN ORCHESTRATION (method.py)\n```python\nimport json, time, os\nfrom pipeline.l0_extractor import extract_l0\nfrom pipeline.l1_prolog import PrologKB\nfrom pipeline import l2_ontology, l3_abduction\nfrom pipeline.meta_interpreter import MetaInterpreter\nfrom pipeline.trace import build_jsonld\nfrom baselines.symba_baseline import symba_prove\nfrom baselines.cot_baseline import cot_answer\nfrom datasets.sara_loader import load_sara\nfrom datasets.proofwriter_loader import load_proofwriter_owa\nfrom datasets.clutrr_loader import load_clutrr\nfrom datasets.contractnli_loader import load_contractnli\nfrom metrics.hallucination import compute_hallucination_rate\nfrom metrics.ece import compute_ece\n\nRESULTS = {'phase0': {}, 'per_example': [], 'aggregates': {}}\nTOTAL_COST = 0.0  # track OpenRouter spend\nCOST_LIMIT = 9.0  # hard stop before $10\n\n# Llama-3.1-70b pricing: ~$0.35/M input, $0.40/M output tokens (check current)\n# K=5 abduction calls per unresolved goal: budget conservatively\n\ndef estimate_cost(n_tokens_in: int, n_tokens_out: int) -> float:\n    return (n_tokens_in / 1e6) * 0.35 + (n_tokens_out / 1e6) * 0.40\n\ndef check_budget():\n    global TOTAL_COST\n    if TOTAL_COST >= COST_LIMIT:\n        raise RuntimeError(f'Budget exceeded: ${TOTAL_COST:.2f}')\n\n## PHASE 0: Run extraction calibration on 25 SARA examples\n# ... (see above)\n# Report precision/recall; gate check\n\n## MINI SCALE (10% of each benchmark, run first)\n# ProofWriter: 200 examples OWA → use 20 for mini\n# CLUTRR: 200 examples → use 20 for mini\n# SARA: 50 → use 10 for mini\n# ContractNLI: 50 contracts → use 5 for mini\n\n## For each example in each benchmark:\n#   1. Extract L0 facts (l0_extractor)\n#   2. Load into PrologKB\n#   3. Run meta_interpreter.prove() for the benchmark's query goal\n#   4. Also run symba_baseline and cot_baseline on same example\n#   5. Store per-example results: {id, benchmark, answer_gold, \n#      answer_stratified, answer_symba, answer_cot,\n#      tier_used, confidence, proof_tree_jsonld}\n\n## After all examples:\n#   1. Multi-hop accuracy per baseline per benchmark (exact match)\n#   2. Hallucination rates for stratified vs symba\n#   3. Tier distribution: fraction using only L0-L2\n#   4. ECE on SARA L3 confidences vs binary entailment labels\n#   5. Write method_out.json\n\nif __name__ == '__main__':\n    # Load LKIF once\n    lkif_onto = l2_ontology.load_lkif()\n    \n    all_results = []\n    \n    for benchmark, loader_fn in [\n        ('sara', load_sara),\n        ('proofwriter_owa', load_proofwriter_owa),\n        ('clutrr', load_clutrr),\n        ('contractnli', load_contractnli)\n    ]:\n        examples = loader_fn()  # starts with mini (10%)\n        for ex in examples:\n            check_budget()\n            document = ex['document']\n            domain = l2_ontology.classify_domain(document)\n            \n            # Stratified pipeline\n            kb = PrologKB()\n            l0_facts = extract_l0(document, domain)\n            kb.load_l0_facts(l0_facts)\n            interp = MetaInterpreter(kb, l2_ontology, l3_abduction,\n                                     domain, document, lkif_onto)\n            goal_pred, goal_args = parse_query(ex)  # benchmark-specific\n            result_node = interp.prove(goal_pred, goal_args)\n            trace = build_jsonld(interp.get_trace(), ex['id'])\n            \n            # SymBa baseline\n            symba_kb = PrologKB()  # empty KB\n            symba_result = symba_prove(goal_pred, goal_args, document, symba_kb)\n            \n            # CoT baseline\n            cot_result = cot_answer(document, ex.get('question', str((goal_pred, goal_args))))\n            \n            all_results.append({\n                'id': ex['id'], 'benchmark': benchmark,\n                'gold': ex['answer'],\n                'stratified': node_to_answer(result_node),\n                'symba': symba_result['proved'],\n                'cot': cot_result,\n                'tier_used': result_node['tier'],\n                'confidence': result_node['confidence'],\n                'l0_facts_count': len(l0_facts),\n                'proof_tree': trace\n            })\n    \n    # Aggregate metrics\n    aggregates = {}\n    for bm in ['sara', 'proofwriter_owa', 'clutrr', 'contractnli']:\n        bm_results = [r for r in all_results if r['benchmark'] == bm]\n        aggregates[bm] = {\n            'accuracy_stratified': mean(r['gold'] == r['stratified'] for r in bm_results),\n            'accuracy_symba': mean(r['gold'] == str(r['symba']) for r in bm_results),\n            'accuracy_cot': mean(r['gold'] == r['cot'] for r in bm_results),\n            'hallucination_rate_stratified': compute_hallucination_rate(\n                [r['proof_tree']['nodes'] for r in bm_results],\n                [get_doc(r) for r in bm_results]\n            ),\n            'tier_l0l1l2_fraction': mean(r['tier_used'] in ['l0','l1','l2'] for r in bm_results),\n            'n_examples': len(bm_results)\n        }\n    \n    # ECE on SARA\n    sara_l3 = [r for r in all_results if r['benchmark'] == 'sara' and r['tier_used'] == 'l3']\n    if sara_l3:\n        aggregates['ece_sara_l3'] = compute_ece(\n            [r['confidence'] for r in sara_l3],\n            [1 if r['gold'] == 'entailed' else 0 for r in sara_l3]\n        )\n    \n    output = {\n        'phase0_extraction_calibration': RESULTS['phase0'],\n        'per_example_results': all_results,\n        'aggregate_metrics': aggregates,\n        'total_cost_usd': TOTAL_COST\n    }\n    with open('method_out.json', 'w') as f:\n        json.dump(output, f, indent=2)\n    print('Done. method_out.json written.')\n```\n\n## SCALING STRATEGY\n1. Run on 10% (mini) first; if all benchmarks complete in < 2h and cost < $3, scale to 50%\n2. If 50% completes in < 4h and cost < $6, scale to 100%\n3. Use multiprocessing.Pool for parallel example processing within each benchmark (4 workers)\n4. Cache L0 extraction results to disk (JSON) to avoid re-calling LLM on restarts\n5. Cache LKIF subclass queries to a dict; don't reload ontology per example\n6. For L3, only call K=5 on SARA (where ECE is measured); use K=3 on others to save cost\n",
  "fallback_plan": "## Fallback scenarios and mitigations\n\n### F1: pyswip / SWI-Prolog integration fails\n- Fallback: Replace pyswip with subprocess calls to swipl binary using `timeout 5 swipl -g 'call_with_depth_limit(Goal,3,R),write(R),halt' -t halt`\n- Parse stdout for result\n- Implement KB as a .pl file written to /tmp, loaded per query\n\n### F2: LKIF OWL file fails to load via owlready2 (import errors on OWL-DL axioms)\n- Fallback: Use owlready2 with `world.as_rdflib_graph()` and SPARQL queries instead of Python object API\n- If owlready2 fails entirely: parse lkif-core.owl as XML, extract rdfs:subClassOf triples manually using lxml\n- Emergency fallback: use a hardcoded dict of 50 key LKIF legal concepts and their superclasses\n\n### F3: Phase 0 SARA extraction precision < 0.75\n- First iteration: add 3 gold-annotated SARA examples as few-shot to the extraction prompt\n- Second iteration: switch to constrained JSON output with `response_format={type:'json_object'}` and a schema that enforces valid Prolog atom patterns\n- Third iteration: use a stronger model (deepseek/deepseek-r1 or google/gemma-3-27b-it) for extraction only\n- Document all iteration results regardless; proceed with best achieved precision\n\n### F4: CLUTRR or ProofWriter D*(OWA) HuggingFace load fails\n- CLUTRR: try `load_dataset('clutrr', 'v1.1')` then fallback to direct download from original GitHub (https://github.com/facebookresearch/clutrr)\n- ProofWriter: try all three HF repos (tasksource/proofwriter, D3xter1922/proofwriter-dataset, renma/ProofWriter); if all fail, use the Allen AI release directly from https://aristo-public-data.s3-us-west-2.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip\n- ContractNLI: download from stanfordnlp.github.io/contract-nli/ directly via requests\n\n### F5: Cost approaching $10 limit before all benchmarks complete\n- Priority order: SARA (Phase 0 gate + hallucination) > ProofWriter OWA (multi-hop accuracy) > CLUTRR > ContractNLI\n- Reduce K from 5 to 3 for L3 abduction on lower-priority benchmarks\n- Switch L0 extraction model to meta-llama/llama-3.1-8b-instruct (much cheaper, ~10x cheaper per token)\n- Reduce mini scale to 5% (10 examples per benchmark) if needed\n\n### F6: Prolog depth_limit produces incorrect results or pyswip segfaults\n- Fallback: implement a pure Python DFS SLD solver with explicit depth counter\n- Represent KB as a dict: predicate_name -> list of (args, tier, conf)\n- Only handles datalog-style rules (no function symbols, no cuts)\n- Sufficient for L0 fact lookup and simple 2-3 step chain deduction\n\n### F7: ConceptNet API rate-limits or is unreachable\n- Fallback: use a locally cached ConceptNet Lite (https://github.com/commonsense/conceptnet-lite) if pip-installable\n- Emergency fallback: use Wikidata SPARQL endpoint for all non-legal domains:\n  `https://query.wikidata.org/sparql?query=SELECT ?classLabel WHERE { wd:Q{entity_id} wdt:P31/wdt:P279* ?class . SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } } LIMIT 10`\n",
  "testing_plan": "## Testing Strategy\n\n### Step 1: Environment validation (run first, < 5 min)\n```bash\n# Verify SWI-Prolog installed\nswipl --version\n# Verify pyswip works\npython3 -c \"from pyswip import Prolog; p=Prolog(); list(p.query('member(X,[1,2,3])'))\"\n# Verify owlready2\npython3 -c \"from owlready2 import get_ontology; print('owlready2 ok')\"\n# Verify OpenRouter key works\ncurl -H 'Authorization: Bearer $OPENROUTER_KEY' https://openrouter.ai/api/v1/models | head -5\n# Verify call_with_depth_limit\npython3 -c \"\nfrom pyswip import Prolog\np = Prolog()\np.assertz('parent(tom,bob)')\np.assertz('parent(bob,ann)')\np.assertz('ancestor(X,Y) :- parent(X,Y)')\np.assertz('ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y)')\nresult = list(p.query('call_with_depth_limit(ancestor(tom,ann), 5, R)'))\nprint('depth_limit test:', result)  # should find solution\n\"\n```\n\n### Step 2: L0 extraction smoke test (3 examples, < 10 min)\n- Load 3 SARA cases, run extraction prompt, verify:\n  a. Output is valid JSON array\n  b. Predicates match regex `^[a-z][a-z0-9_]*$`\n  c. At least 2 predicates extracted per document\n  d. No uppercase variable names in args\n- If any fail: debug extraction prompt before Phase 0\n\n### Step 3: Phase 0 on 25 SARA examples (~ 20-30 min)\n- Run extraction on all 25 sampled cases\n- Compute precision/recall against gold .pl annotations\n- CONFIRM: precision >= 0.75 before proceeding\n- Log per-case results; note cases where extraction fails entirely\n\n### Step 4: End-to-end mini pipeline test (5 ProofWriter OWA examples, < 15 min)\n- Run full stratified pipeline + both baselines on 5 ProofWriter examples\n- Verify: method_out.json is written with correct schema\n- Verify: proof trees are non-empty for at least 3/5 examples\n- Verify: tier distribution shows at least some L0 facts (not all L3)\n- Verify: cost tracking is working (TOTAL_COST > 0 and < $0.50 for 5 examples)\n\n### Step 5: LKIF ontology integration test\n- Load LKIF OWL; query ancestors of class 'Obligation'\n- Expected: returns ['Normative_thing', 'Qualified_norm', 'Norm', ...] (any non-empty list)\n- If empty: check that lkif-core.owl was downloaded successfully and has class definitions\n\n### Step 6: Mini benchmark run (10% scale, ~1-2h)\n- Run all 4 benchmarks at 10% scale (20/20/10/5 examples)\n- Check: no crashes, results for all examples, metrics computable\n- Check: total cost < $2.00 for mini run\n- Decision: if runtime < 90 min and cost < $2, scale to 50%; else stay at 10% and report\n\n### Step 7: Final validation of method_out.json\n- Verify JSON is valid and parseable\n- Verify top-level keys: phase0_extraction_calibration, per_example_results, aggregate_metrics, total_cost_usd\n- Verify per_example has required fields: id, benchmark, gold, stratified, symba, cot, tier_used, confidence\n- Verify aggregate_metrics has accuracy for all 3 systems on all 4 benchmarks\n- Apply aii-json skill to validate against expected schema\n\n### Confirmation signals before full scale\n- Phase 0 precision >= 0.75 (HARD gate)\n- Mini pipeline produces non-trivial tier distribution (not 100% L3)\n- SymBa baseline produces non-trivially different results from stratified (if identical, check bug)\n- Cost per example < $0.10 (to stay within budget for 100+ examples)\n\n### Known failure modes to watch for\n- pyswip segfault under multiprocessing (use spawn not fork; or run Prolog in subprocess)\n- owlready2 loading OWL-DL axioms with imports (some LKIF owl files import others; set onto_path to local dir)\n- OpenRouter rate limits: add time.sleep(0.5) between L3 calls; implement exponential backoff\n- CLUTRR data format varies by version: check field names before assuming story/query/target_text keys"
}
````

### [29] TOOL RESULT — Write · 2026-06-15 20:10:51 UTC

````
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_plan/gen_plan_experiment_1/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Provenance-Stratified Neuro-Symbolic Pipeline: L0-L3 Tier-Ordered SLD with SARA/CLUTRR/ProofWriter/ContractNLI Evaluation\",\n  \"summary\": \"Implement and evaluate a complete 4-tier neuro-symbolic reasoning pipeline (L0 document extraction, L1 bounded SLD, L2 domain-adaptive ontology, L3 self-consistency LLM abduction) with weakest-link provenance propagation, against a SymBa-style flat-LLM baseline and CoT baseline, across four benchmarks: SARA, ProofWriter D*(OWA), CLUTRR, and ContractNLI.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"implementation_pseudocode\": \"## File layout\\n```\\nmethod.py             # main entrypoint, orchestrates all phases\\npipeline/\\n  l0_extractor.py    # LLM-based L0 Prolog predicate extraction\\n  l1_prolog.py       # SWI-Prolog interface via pyswip, depth-limited SLD\\n  l2_ontology.py     # owlready2 LKIF + ConceptNet REST for L2 bridging\\n  l3_abduction.py    # K=5 self-consistency LLM abduction\\n  meta_interpreter.py # tier-ordered resolution + weakest-link propagation\\n  trace.py           # JSON-LD derivation tree builder\\nbaselines/\\n  symba_baseline.py  # empty-KB flat LLM on every proof failure\\n  cot_baseline.py    # chain-of-thought LLM, extract yes/no answer\\ndatasets/\\n  sara_loader.py     # load SARA from github.com/SgfdDttt/sara\\n  proofwriter_loader.py  # load tasksource/proofwriter from HuggingFace\\n  clutrr_loader.py   # load CLUTRR from HuggingFace CLUTRR org\\n  contractnli_loader.py  # load from stanfordnlp.github.io/contract-nli\\nmetrics/\\n  hallucination.py   # string-match L0 assertions vs source document\\n  ece.py             # bucketed ECE for L3 confidence vs binary ground truth\\n  tier_distribution.py  # fraction of proofs using only L0-L2\\nmethod_out.json       # final output\\n```\\n\\n## PHASE 0 — SARA Extraction Calibration (must run first, acts as gate)\\n\\n### Setup\\n```python\\n# Install: uv add pyswip owlready2 requests datasets openai-compatible httpx\\n# SWI-Prolog must be installed system-wide: apt-get install swi-prolog\\n# Verify: from pyswip import Prolog; p = Prolog(); list(p.query('true'))\\n```\\n\\n### Load SARA\\n```python\\n# Clone: git clone https://github.com/SgfdDttt/sara\\n# Repo structure: sara/prolog/ has gold .pl files per case; sara/cases/ has text descriptions\\n# Load 25 random cases:\\nimport glob, random\\ncases = glob.glob('sara/cases/*.txt')  # each file is ~3000 char document\\ngold_pls = glob.glob('sara/prolog/*.pl')  # matching gold Prolog KB\\n# Pair by filename stem\\npaired = [(c, c.replace('cases/', 'prolog/').replace('.txt', '.pl')) for c in cases]\\nsampled = random.sample(paired, 25)\\n```\\n\\n### L0 Extraction Prompt (use meta-llama/llama-3.1-70b-instruct via OpenRouter)\\n```python\\nEXTRACTION_PROMPT = '''\\nYou are a Prolog knowledge engineer. Extract ALL atomic facts from the following legal document as Prolog predicates.\\nRules:\\n- Use lowercase snake_case for predicate names and all atom arguments\\n- No variables (start with uppercase) in extracted facts — only ground atoms\\n- Each fact must correspond to something EXPLICITLY stated in the document, not inferred\\n- Format each fact as valid Prolog: predicate_name(arg1, arg2, ...) with no spaces inside\\nOutput ONLY a JSON array of objects, each with keys:\\n  {\\\"predicate\\\": str, \\\"args\\\": [str, ...], \\\"source_span\\\": str, \\\"confidence\\\": 1.0, \\\"tier\\\": \\\"l0\\\"}\\nDocument:\\n{document}\\n'''\\n```\\n\\n### Evaluate vs gold\\n```python\\n# Parse gold .pl file: extract head/1 facts and rule heads\\n# For precision: fraction of extracted predicates whose string form appears in gold .pl\\n# For recall: fraction of gold .pl ground facts covered by extracted set\\n# Report per-case and aggregate precision/recall\\n# GATE: if precision < 0.75 across 25 examples:\\n#   Iterate with few-shot examples (add 3 gold-annotated examples to prompt)\\n#   Re-evaluate; if still < 0.75 use constrained JSON + type constraints\\n#   Max 3 iterations; log all results; proceed regardless but flag\\n```\\n\\n## PHASE 1 — PIPELINE ARCHITECTURE\\n\\n### L0 Extractor (pipeline/l0_extractor.py)\\n```python\\nfrom openai import OpenAI  # OpenRouter compatible\\nimport json, re\\n\\nclient = OpenAI(base_url='https://openrouter.ai/api/v1', api_key=OPENROUTER_KEY)\\n\\ndef extract_l0(document: str, domain: str = 'general') -> list[dict]:\\n    # Select domain-adapted prompt (add legal examples for legal docs)\\n    prompt = EXTRACTION_PROMPT.format(document=document[:4000])\\n    resp = client.chat.completions.create(\\n        model='meta-llama/llama-3.1-70b-instruct',\\n        messages=[{'role': 'user', 'content': prompt}],\\n        temperature=0.0, max_tokens=2000\\n    )\\n    raw = resp.choices[0].message.content\\n    # Extract JSON array from response (allow markdown code block)\\n    match = re.search(r'\\\\[.*?\\\\]', raw, re.DOTALL)\\n    facts = json.loads(match.group()) if match else []\\n    # Validate: predicate is valid Prolog atom (lowercase, alphanumeric+underscore)\\n    valid = [f for f in facts if re.match(r'^[a-z][a-z0-9_]*$', f['predicate'])\\n             and all(re.match(r'^[a-z0-9_]+$', a) for a in f['args'])]\\n    return valid  # list of {predicate, args, source_span, confidence:1.0, tier:'l0'}\\n```\\n\\n### L1 Bounded SLD (pipeline/l1_prolog.py)\\n```python\\nfrom pyswip import Prolog\\n\\nclass PrologKB:\\n    def __init__(self):\\n        self.prolog = Prolog()\\n        self.facts = []  # list of (predicate, args, tier, conf)\\n    \\n    def load_l0_facts(self, facts: list[dict]):\\n        for f in facts:\\n            atom = f[\\\"predicate\\\"] + '(' + ','.join(f[\\\"args\\\"]) + ')'\\n            self.prolog.assertz(atom)\\n            self.facts.append((f['predicate'], f['args'], 'l0', 1.0))\\n    \\n    def load_l0_rules(self, rules: list[str]):\\n        # rules as plain Prolog strings, e.g. 'parent(X,Y) :- father(X,Y)'\\n        for r in rules:\\n            self.prolog.assertz(r)\\n    \\n    def query_with_depth_limit(self, goal: str, depth: int = 3) -> tuple[bool, str]:\\n        # SWI-Prolog call_with_depth_limit/3:\\n        # call_with_depth_limit(Goal, Limit, Result)\\n        # Result = depth_limit_exceeded | integer (steps used) | false\\n        query = f'call_with_depth_limit(({goal}), {depth}, Result)'\\n        try:\\n            solutions = list(self.prolog.query(query))\\n            if solutions and solutions[0].get('Result') != 'depth_limit_exceeded':\\n                return True, 'l1'\\n            return False, 'depth_limit_exceeded'\\n        except Exception:\\n            return False, 'error'\\n    \\n    def assert_l1_derived(self, predicate: str, args: list[str]):\\n        atom = predicate + '(' + ','.join(args) + ')'\\n        self.prolog.assertz(atom)\\n        self.facts.append((predicate, args, 'l1', 1.0))\\n```\\n\\n### L2 Domain-Adaptive Ontology (pipeline/l2_ontology.py)\\n```python\\nimport requests\\nfrom owlready2 import get_ontology, onto_path\\n\\nLKIF_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-core.owl'\\nLKIF_EXTENDED_URL = 'https://raw.githubusercontent.com/RinkeHoekstra/lkif-core/master/lkif-extended.owl'\\n\\ndef load_lkif() -> object:\\n    onto = get_ontology(LKIF_URL)\\n    onto.load()\\n    return onto\\n\\ndef query_lkif_subsumption(onto, concept_name: str) -> list[str]:\\n    # Find class matching concept_name (case-insensitive fuzzy match)\\n    matched = [c for c in onto.classes() \\n               if concept_name.lower() in c.name.lower()]\\n    if not matched:\\n        return []\\n    cls = matched[0]\\n    # Return all ancestor class names (broader concepts)\\n    return [a.name for a in cls.ancestors() if a is not cls]\\n\\ndef query_conceptnet(entity: str, relation: str = 'IsA') -> list[tuple[str, float]]:\\n    # ConceptNet REST API\\n    url = f'https://api.conceptnet.io/query?node=/c/en/{entity}&rel=/r/{relation}&limit=10'\\n    resp = requests.get(url, timeout=10)\\n    if resp.status_code != 200:\\n        return []\\n    edges = resp.json().get('edges', [])\\n    results = []\\n    for e in edges:\\n        end = e.get('end', {}).get('label', '')\\n        weight = e.get('weight', 1.0)\\n        # Normalize: ConceptNet weights typically 1.0-10.0; cap confidence at 0.80\\n        conf = min(0.80, weight / 10.0 + 0.70)\\n        results.append((end, conf))\\n    return results\\n\\ndef classify_domain(document: str) -> str:\\n    legal_keywords = ['contract', 'obligation', 'party', 'law', 'statute',\\n                      'agreement', 'liability', 'clause', 'provision', 'plaintiff']\\n    narrative_keywords = ['story', 'character', 'once upon', 'family', 'village']\\n    legal_score = sum(1 for kw in legal_keywords if kw in document.lower())\\n    narrative_score = sum(1 for kw in narrative_keywords if kw in document.lower())\\n    if legal_score >= 3:\\n        return 'legal'\\n    elif narrative_score >= 2:\\n        return 'narrative'\\n    return 'general'\\n\\ndef query_l2(goal_predicate: str, goal_args: list[str], domain: str,\\n             onto=None) -> list[dict]:\\n    results = []\\n    if domain == 'legal' and onto is not None:\\n        # Try to match args against LKIF concepts\\n        for arg in goal_args:\\n            ancestors = query_lkif_subsumption(onto, arg)\\n            for anc in ancestors:\\n                results.append({\\n                    'predicate': f'is_a',\\n                    'args': [arg, anc.lower()],\\n                    'tier': 'l2', 'confidence': 0.95,\\n                    'source': 'lkif'\\n                })\\n    else:\\n        for arg in goal_args:\\n            cn_results = query_conceptnet(arg.replace('_', ' '))\\n            for label, conf in cn_results:\\n                results.append({\\n                    'predicate': 'is_a',\\n                    'args': [arg, label.lower().replace(' ', '_')],\\n                    'tier': 'l2', 'confidence': conf,\\n                    'source': 'conceptnet'\\n                })\\n    return results\\n```\\n\\n### L3 LLM Abduction (pipeline/l3_abduction.py)\\n```python\\nABDUCTION_PROMPT = '''\\nDocument excerpt:\\n{document_excerpt}\\n\\nQuestion: Based ONLY on the document above, does the following hold?\\n{predicate}({args})\\nAnswer with exactly 'yes' or 'no', followed by one sentence justification.\\n'''\\n\\ndef abduce_l3(predicate: str, args: list[str], document: str,\\n              K: int = 5) -> dict:\\n    yes_count = 0\\n    justifications = []\\n    for _ in range(K):\\n        resp = client.chat.completions.create(\\n            model='meta-llama/llama-3.1-70b-instruct',\\n            messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\\n                document_excerpt=document[:2000],\\n                predicate=predicate,\\n                args=', '.join(args)\\n            )}],\\n            temperature=0.7,  # slight temperature for sampling diversity\\n            max_tokens=100\\n        )\\n        answer = resp.choices[0].message.content.strip().lower()\\n        if answer.startswith('yes'):\\n            yes_count += 1\\n        justifications.append(answer)\\n    confidence = yes_count / K\\n    return {\\n        'predicate': predicate, 'args': args,\\n        'tier': 'l3', 'confidence': confidence,\\n        'low_confidence': confidence < 0.6,\\n        'K': K, 'yes_count': yes_count,\\n        'justifications': justifications\\n    }\\n```\\n\\n### Meta-Interpreter with Weakest-Link Propagation (pipeline/meta_interpreter.py)\\n```python\\nTIER_ORDER = {'l0': 0, 'l1': 1, 'l2': 2, 'l3': 3, 'unknown': 4}\\n\\nclass MetaInterpreter:\\n    def __init__(self, kb: PrologKB, l2_module, l3_module, domain: str,\\n                 document: str, lkif_onto=None):\\n        self.kb = kb\\n        self.l2 = l2_module\\n        self.l3 = l3_module\\n        self.domain = domain\\n        self.document = document\\n        self.lkif_onto = lkif_onto\\n        self.proof_tree = []  # list of nodes for JSON-LD export\\n    \\n    def propagate(self, premises: list[dict]) -> dict:\\n        # Weakest-link: tier = max tier (by TIER_ORDER), conf = min conf\\n        max_tier = max(premises, key=lambda p: TIER_ORDER[p['tier']])['tier']\\n        min_conf = min(p['confidence'] for p in premises)\\n        return {'tier': max_tier, 'confidence': min_conf}\\n    \\n    def prove(self, predicate: str, args: list[str],\\n              depth: int = 0) -> dict:\\n        goal_str = predicate + '(' + ','.join(args) + ')'\\n        node = {'goal': goal_str, 'predicate': predicate, 'args': args}\\n        \\n        # Try L0/L1 via pyswip with depth limit\\n        proved, tier = self.kb.query_with_depth_limit(goal_str, depth=3)\\n        if proved:\\n            node.update({'tier': tier, 'confidence': 1.0, 'method': 'sld'})\\n            self.proof_tree.append(node)\\n            return node\\n        \\n        # Try L2\\n        l2_facts = self.l2.query_l2(\\n            predicate, args, self.domain, self.lkif_onto\\n        )\\n        if l2_facts:\\n            best = max(l2_facts, key=lambda f: f['confidence'])\\n            # Assert into KB for future use\\n            self.kb.prolog.assertz(\\n                best['predicate'] + '(' + ','.join(best['args']) + ')'\\n            )\\n            node.update(best)\\n            self.proof_tree.append(node)\\n            return node\\n        \\n        # Try L3\\n        if depth <= 2:  # avoid L3 in deep sub-proofs\\n            l3_result = self.l3.abduce_l3(predicate, args, self.document)\\n            if l3_result['confidence'] >= 0.6:\\n                self.kb.prolog.assertz(goal_str)\\n                node.update(l3_result)\\n            else:\\n                node.update({'tier': 'unknown', 'confidence': 0.0,\\n                             'low_confidence': True})\\n            self.proof_tree.append(node)\\n            return node\\n        \\n        node.update({'tier': 'unknown', 'confidence': 0.0})\\n        self.proof_tree.append(node)\\n        return node\\n    \\n    def get_trace(self) -> list[dict]:\\n        return self.proof_tree\\n```\\n\\n### JSON-LD Trace Export (pipeline/trace.py)\\n```python\\ndef build_jsonld(proof_tree: list[dict], doc_id: str) -> dict:\\n    TIER_COLORS = {'l0': 'green', 'l1': 'yellow', 'l2': 'orange',\\n                   'l3': 'red', 'unknown': 'gray'}\\n    nodes = []\\n    for i, node in enumerate(proof_tree):\\n        nodes.append({\\n            '@id': f'node:{doc_id}:{i}',\\n            '@type': 'ProofNode',\\n            'predicate': node.get('predicate', ''),\\n            'args': node.get('args', []),\\n            'tier': node.get('tier', 'unknown'),\\n            'confidence': node.get('confidence', 0.0),\\n            'color': TIER_COLORS.get(node.get('tier', 'unknown'), 'gray'),\\n            'source_span': node.get('source_span', ''),\\n            'method': node.get('method', 'abduction')\\n        })\\n    return {\\n        '@context': {'@vocab': 'https://schema.org/'},\\n        '@type': 'ProofTrace',\\n        'document_id': doc_id,\\n        'nodes': nodes\\n    }\\n```\\n\\n## PHASE 2 — BASELINES\\n\\n### SymBa-style flat baseline (baselines/symba_baseline.py)\\n```python\\n# Empty KB; for every proof-failure goal, call LLM once (K=1, no tier routing)\\ndef symba_prove(predicate: str, args: list[str], document: str,\\n                kb: PrologKB) -> dict:\\n    proved, _ = kb.query_with_depth_limit(\\n        predicate + '(' + ','.join(args) + ')', depth=3\\n    )\\n    if proved:\\n        return {'tier': 'sld', 'confidence': 1.0, 'proved': True}\\n    # LLM immediately, no ontology tier\\n    resp = client.chat.completions.create(\\n        model='meta-llama/llama-3.1-70b-instruct',\\n        messages=[{'role': 'user', 'content': ABDUCTION_PROMPT.format(\\n            document_excerpt=document[:2000],\\n            predicate=predicate, args=', '.join(args)\\n        )}],\\n        temperature=0.0, max_tokens=100\\n    )\\n    answer = resp.choices[0].message.content.strip().lower()\\n    return {'tier': 'llm', 'confidence': 1.0 if answer.startswith('yes') else 0.0,\\n            'proved': answer.startswith('yes'), 'no_provenance': True}\\n```\\n\\n### CoT baseline (baselines/cot_baseline.py)\\n```python\\nCOT_PROMPT = '''\\nDocument:\\n{document}\\n\\nQuestion: {question}\\nThink step by step, then answer True, False, or Unknown.\\n'''\\ndef cot_answer(document: str, question: str) -> str:\\n    resp = client.chat.completions.create(\\n        model='meta-llama/llama-3.1-70b-instruct',\\n        messages=[{'role': 'user', 'content': COT_PROMPT.format(\\n            document=document[:3000], question=question)}],\\n        temperature=0.0, max_tokens=500\\n    )\\n    raw = resp.choices[0].message.content\\n    # Extract final answer\\n    for ans in ['True', 'False', 'Unknown']:\\n        if ans.lower() in raw.lower().split()[-10:]:\\n            return ans\\n    return 'Unknown'\\n```\\n\\n## PHASE 3 — DATASET LOADERS\\n\\n### ProofWriter (datasets/proofwriter_loader.py)\\n```python\\nfrom datasets import load_dataset\\ndef load_proofwriter_owa(split='validation', max_examples=200):\\n    # Use tasksource/proofwriter, filter to OWA (depth_5_owa or depth-5-OWA)\\n    ds = load_dataset('tasksource/proofwriter', split=split)\\n    # Filter for D*(OWA) subset with 3-valued answers\\n    owa = [ex for ex in ds if ex.get('answer') in ['True','False','Unknown']]\\n    return owa[:max_examples]\\n    # Each example: {'context': str, 'question': str, 'answer': 'True'|'False'|'Unknown'}\\n    # context is a short theory (facts + rules as natural language sentences)\\n    # question is the query sentence\\n```\\n\\n### CLUTRR (datasets/clutrr_loader.py)\\n```python\\nfrom datasets import load_dataset\\ndef load_clutrr(split='test', max_examples=200):\\n    ds = load_dataset('CLUTRR/v1', split=split)  # or specific config\\n    # Each: {'story': str, 'query': [entity1, entity2], 'target_text': str}\\n    return list(ds)[:max_examples]\\n```\\n\\n### SARA (datasets/sara_loader.py)\\n```python\\nimport os, glob\\ndef load_sara(sara_dir='sara', max_examples=50):\\n    cases = []\\n    for txt_file in glob.glob(os.path.join(sara_dir, 'cases', '*.txt')):\\n        stem = os.path.splitext(os.path.basename(txt_file))[0]\\n        pl_file = os.path.join(sara_dir, 'prolog', stem + '.pl')\\n        if os.path.exists(pl_file):\\n            cases.append({\\n                'id': stem,\\n                'document': open(txt_file).read(),\\n                'gold_prolog': open(pl_file).read(),\\n                'answer': 'entailed'  # determine from .pl query result\\n            })\\n    return cases[:max_examples]\\n```\\n\\n### ContractNLI (datasets/contractnli_loader.py)\\n```python\\nimport json\\ndef load_contractnli(data_dir='contract-nli', split='test', max_contracts=50):\\n    # Download from stanfordnlp.github.io/contract-nli/\\n    # JSON format: {documents: [{text, annotation_sets: [{annotations: {nda-1: {choice, spans}}}]}]}\\n    with open(os.path.join(data_dir, f'{split}.json')) as f:\\n        data = json.load(f)\\n    examples = []\\n    for doc in data['documents'][:max_contracts]:\\n        text = doc['text']\\n        for ann_set in doc.get('annotation_sets', []):\\n            for hyp_id, ann in ann_set.get('annotations', {}).items():\\n                examples.append({\\n                    'document': text[:3000],\\n                    'hypothesis': hyp_id,\\n                    'label': ann['choice'],  # 'Entailment'|'Contradiction'|'NotMentioned'\\n                    'evidence_spans': ann.get('spans', [])\\n                })\\n    return examples\\n```\\n\\n## PHASE 4 — METRICS\\n\\n### Hallucination Rate (metrics/hallucination.py)\\n```python\\ndef compute_hallucination_rate(proof_trees: list[list[dict]],\\n                               documents: list[str]) -> float:\\n    # For each L0-tier fact in the proof tree, check if predicate string\\n    # or its args appear literally in the source document\\n    hallucinated = 0\\n    total_l0 = 0\\n    for tree, doc in zip(proof_trees, documents):\\n        doc_lower = doc.lower()\\n        for node in tree:\\n            if node.get('tier') == 'l0':\\n                total_l0 += 1\\n                fact_str = node.get('predicate', '') + ' ' + ' '.join(node.get('args', []))\\n                # Check if any arg or predicate keyword appears in doc\\n                args_in_doc = any(arg.replace('_', ' ') in doc_lower\\n                                  for arg in node.get('args', []))\\n                if not args_in_doc:\\n                    hallucinated += 1\\n    return hallucinated / total_l0 if total_l0 > 0 else 0.0\\n```\\n\\n### ECE (metrics/ece.py)\\n```python\\nimport numpy as np\\ndef compute_ece(confidences: list[float], labels: list[int],\\n                n_bins: int = 10) -> float:\\n    bins = np.linspace(0, 1, n_bins + 1)\\n    ece = 0.0\\n    n = len(confidences)\\n    for b in range(n_bins):\\n        lo, hi = bins[b], bins[b+1]\\n        mask = [(lo <= c < hi) for c in confidences]\\n        if not any(mask):\\n            continue\\n        bin_confs = [c for c, m in zip(confidences, mask) if m]\\n        bin_labels = [l for l, m in zip(labels, mask) if m]\\n        avg_conf = np.mean(bin_confs)\\n        frac_pos = np.mean(bin_labels)\\n        ece += (len(bin_confs) / n) * abs(avg_conf - frac_pos)\\n    return ece\\n```\\n\\n## PHASE 5 — MAIN ORCHESTRATION (method.py)\\n```python\\nimport json, time, os\\nfrom pipeline.l0_extractor import extract_l0\\nfrom pipeline.l1_prolog import PrologKB\\nfrom pipeline import l2_ontology, l3_abduction\\nfrom pipeline.meta_interpreter import MetaInterpreter\\nfrom pipeline.trace import build_jsonld\\nfrom baselines.symba_baseline import symba_prove\\nfrom baselines.cot_baseline import cot_answer\\nfrom datasets.sara_loader import load_sara\\nfrom datasets.proofwriter_loader import load_proofwriter_owa\\nfrom datasets.clutrr_loader import load_clutrr\\nfrom datasets.contractnli_loader import load_contractnli\\nfrom metrics.hallucination import compute_hallucination_rate\\nfrom metrics.ece import compute_ece\\n\\nRESULTS = {'phase0': {}, 'per_example': [], 'aggregates': {}}\\nTOTAL_COST = 0.0  # track OpenRouter spend\\nCOST_LIMIT = 9.0  # hard stop before $10\\n\\n# Llama-3.1-70b pricing: ~$0.35/M input, $0.40/M output tokens (check current)\\n# K=5 abduction calls per unresolved goal: budget conservatively\\n\\ndef estimate_cost(n_tokens_in: int, n_tokens_out: int) -> float:\\n    return (n_tokens_in / 1e6) * 0.35 + (n_tokens_out / 1e6) * 0.40\\n\\ndef check_budget():\\n    global TOTAL_COST\\n    if TOTAL_COST >= COST_LIMIT:\\n        raise RuntimeError(f'Budget exceeded: ${TOTAL_COST:.2f}')\\n\\n## PHASE 0: Run extraction calibration on 25 SARA examples\\n# ... (see above)\\n# Report precision/recall; gate check\\n\\n## MINI SCALE (10% of each benchmark, run first)\\n# ProofWriter: 200 examples OWA → use 20 for mini\\n# CLUTRR: 200 examples → use 20 for mini\\n# SARA: 50 → use 10 for mini\\n# ContractNLI: 50 contracts → use 5 for mini\\n\\n## For each example in each benchmark:\\n#   1. Extract L0 facts (l0_extractor)\\n#   2. Load into PrologKB\\n#   3. Run meta_interpreter.prove() for the benchmark's query goal\\n#   4. Also run symba_baseline and cot_baseline on same example\\n#   5. Store per-example results: {id, benchmark, answer_gold, \\n#      answer_stratified, answer_symba, answer_cot,\\n#      tier_used, confidence, proof_tree_jsonld}\\n\\n## After all examples:\\n#   1. Multi-hop accuracy per baseline per benchmark (exact match)\\n#   2. Hallucination rates for stratified vs symba\\n#   3. Tier distribution: fraction using only L0-L2\\n#   4. ECE on SARA L3 confidences vs binary entailment labels\\n#   5. Write method_out.json\\n\\nif __name__ == '__main__':\\n    # Load LKIF once\\n    lkif_onto = l2_ontology.load_lkif()\\n    \\n    all_results = []\\n    \\n    for benchmark, loader_fn in [\\n        ('sara', load_sara),\\n        ('proofwriter_owa', load_proofwriter_owa),\\n        ('clutrr', load_clutrr),\\n        ('contractnli', load_contractnli)\\n    ]:\\n        examples = loader_fn()  # starts with mini (10%)\\n        for ex in examples:\\n            check_budget()\\n            document = ex['document']\\n            domain = l2_ontology.classify_domain(document)\\n            \\n            # Stratified pipeline\\n            kb = PrologKB()\\n            l0_facts = extract_l0(document, domain)\\n            kb.load_l0_facts(l0_facts)\\n            interp = MetaInterpreter(kb, l2_ontology, l3_abduction,\\n                                     domain, document, lkif_onto)\\n            goal_pred, goal_args = parse_query(ex)  # benchmark-specific\\n            result_node = interp.prove(goal_pred, goal_args)\\n            trace = build_jsonld(interp.get_trace(), ex['id'])\\n            \\n            # SymBa baseline\\n            symba_kb = PrologKB()  # empty KB\\n            symba_result = symba_prove(goal_pred, goal_args, document, symba_kb)\\n            \\n            # CoT baseline\\n            cot_result = cot_answer(document, ex.get('question', str((goal_pred, goal_args))))\\n            \\n            all_results.append({\\n                'id': ex['id'], 'benchmark': benchmark,\\n                'gold': ex['answer'],\\n                'stratified': node_to_answer(result_node),\\n                'symba': symba_result['proved'],\\n                'cot': cot_result,\\n                'tier_used': result_node['tier'],\\n                'confidence': result_node['confidence'],\\n                'l0_facts_count': len(l0_facts),\\n                'proof_tree': trace\\n            })\\n    \\n    # Aggregate metrics\\n    aggregates = {}\\n    for bm in ['sara', 'proofwriter_owa', 'clutrr', 'contractnli']:\\n        bm_results = [r for r in all_results if r['benchmark'] == bm]\\n        aggregates[bm] = {\\n            'accuracy_stratified': mean(r['gold'] == r['stratified'] for r in bm_results),\\n            'accuracy_symba': mean(r['gold'] == str(r['symba']) for r in bm_results),\\n            'accuracy_cot': mean(r['gold'] == r['cot'] for r in bm_results),\\n            'hallucination_rate_stratified': compute_hallucination_rate(\\n                [r['proof_tree']['nodes'] for r in bm_results],\\n                [get_doc(r) for r in bm_results]\\n            ),\\n            'tier_l0l1l2_fraction': mean(r['tier_used'] in ['l0','l1','l2'] for r in bm_results),\\n            'n_examples': len(bm_results)\\n        }\\n    \\n    # ECE on SARA\\n    sara_l3 = [r for r in all_results if r['benchmark'] == 'sara' and r['tier_used'] == 'l3']\\n    if sara_l3:\\n        aggregates['ece_sara_l3'] = compute_ece(\\n            [r['confidence'] for r in sara_l3],\\n            [1 if r['gold'] == 'entailed' else 0 for r in sara_l3]\\n        )\\n    \\n    output = {\\n        'phase0_extraction_calibration': RESULTS['phase0'],\\n        'per_example_results': all_results,\\n        'aggregate_metrics': aggregates,\\n        'total_cost_usd': TOTAL_COST\\n    }\\n    with open('method_out.json', 'w') as f:\\n        json.dump(output, f, indent=2)\\n    print('Done. method_out.json written.')\\n```\\n\\n## SCALING STRATEGY\\n1. Run on 10% (mini) first; if all benchmarks complete in < 2h and cost < $3, scale to 50%\\n2. If 50% completes in < 4h and cost < $6, scale to 100%\\n3. Use multiprocessing.Pool for parallel example processing within each benchmark (4 workers)\\n4. Cache L0 extraction results to disk (JSON) to avoid re-calling LLM on restarts\\n5. Cache LKIF subclass queries to a dict; don't reload ontology per example\\n6. For L3, only call K=5 on SARA (where ECE is measured); use K=3 on others to save cost\\n\",\n  \"fallback_plan\": \"## Fallback scenarios and mitigations\\n\\n### F1: pyswip / SWI-Prolog integration fails\\n- Fallback: Replace pyswip with subprocess calls to swipl binary using `timeout 5 swipl -g 'call_with_depth_limit(Goal,3,R),write(R),halt' -t halt`\\n- Parse stdout for result\\n- Implement KB as a .pl file written to /tmp, loaded per query\\n\\n### F2: LKIF OWL file fails to load via owlready2 (import errors on OWL-DL axioms)\\n- Fallback: Use owlready2 with `world.as_rdflib_graph()` and SPARQL queries instead of Python object API\\n- If owlready2 fails entirely: parse lkif-core.owl as XML, extract rdfs:subClassOf triples manually using lxml\\n- Emergency fallback: use a hardcoded dict of 50 key LKIF legal concepts and their superclasses\\n\\n### F3: Phase 0 SARA extraction precision < 0.75\\n- First iteration: add 3 gold-annotated SARA examples as few-shot to the extraction prompt\\n- Second iteration: switch to constrained JSON output with `response_format={type:'json_object'}` and a schema that enforces valid Prolog atom patterns\\n- Third iteration: use a stronger model (deepseek/deepseek-r1 or google/gemma-3-27b-it) for extraction only\\n- Document all iteration results regardless; proceed with best achieved precision\\n\\n### F4: CLUTRR or ProofWriter D*(OWA) HuggingFace load fails\\n- CLUTRR: try `load_dataset('clutrr', 'v1.1')` then fallback to direct download from original GitHub (https://github.com/facebookresearch/clutrr)\\n- ProofWriter: try all three HF repos (tasksource/proofwriter, D3xter1922/proofwriter-dataset, renma/ProofWriter); if all fail, use the Allen AI release directly from https://aristo-public-data.s3-us-west-2.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip\\n- ContractNLI: download from stanfordnlp.github.io/contract-nli/ directly via requests\\n\\n### F5: Cost approaching $10 limit before all benchmarks complete\\n- Priority order: SARA (Phase 0 gate + hallucination) > ProofWriter OWA (multi-hop accuracy) > CLUTRR > ContractNLI\\n- Reduce K from 5 to 3 for L3 abduction on lower-priority benchmarks\\n- Switch L0 extraction model to meta-llama/llama-3.1-8b-instruct (much cheaper, ~10x cheaper per token)\\n- Reduce mini scale to 5% (10 examples per benchmark) if needed\\n\\n### F6: Prolog depth_limit produces incorrect results or pyswip segfaults\\n- Fallback: implement a pure Python DFS SLD solver with explicit depth counter\\n- Represent KB as a dict: predicate_name -> list of (args, tier, conf)\\n- Only handles datalog-style rules (no function symbols, no cuts)\\n- Sufficient for L0 fact lookup and simple 2-3 step chain deduction\\n\\n### F7: ConceptNet API rate-limits or is unreachable\\n- Fallback: use a locally cached ConceptNet Lite (https://github.com/commonsense/conceptnet-lite) if pip-installable\\n- Emergency fallback: use Wikidata SPARQL endpoint for all non-legal domains:\\n  `https://query.wikidata.org/sparql?query=SELECT ?classLabel WHERE { wd:Q{entity_id} wdt:P31/wdt:P279* ?class . SERVICE wikibase:label { bd:serviceParam wikibase:language 'en' } } LIMIT 10`\\n\",\n  \"testing_plan\": \"## Testing Strategy\\n\\n### Step 1: Environment validation (run first, < 5 min)\\n```bash\\n# Verify SWI-Prolog installed\\nswipl --version\\n# Verify pyswip works\\npython3 -c \\\"from pyswip import Prolog; p=Prolog(); list(p.query('member(X,[1,2,3])'))\\\"\\n# Verify owlready2\\npython3 -c \\\"from owlready2 import get_ontology; print('owlready2 ok')\\\"\\n# Verify OpenRouter key works\\ncurl -H 'Authorization: Bearer $OPENROUTER_KEY' https://openrouter.ai/api/v1/models | head -5\\n# Verify call_with_depth_limit\\npython3 -c \\\"\\nfrom pyswip import Prolog\\np = Prolog()\\np.assertz('parent(tom,bob)')\\np.assertz('parent(bob,ann)')\\np.assertz('ancestor(X,Y) :- parent(X,Y)')\\np.assertz('ancestor(X,Y) :- parent(X,Z), ancestor(Z,Y)')\\nresult = list(p.query('call_with_depth_limit(ancestor(tom,ann), 5, R)'))\\nprint('depth_limit test:', result)  # should find solution\\n\\\"\\n```\\n\\n### Step 2: L0 extraction smoke test (3 examples, < 10 min)\\n- Load 3 SARA cases, run extraction prompt, verify:\\n  a. Output is valid JSON array\\n  b. Predicates match regex `^[a-z][a-z0-9_]*$`\\n  c. At least 2 predicates extracted per document\\n  d. No uppercase variable names in args\\n- If any fail: debug extraction prompt before Phase 0\\n\\n### Step 3: Phase 0 on 25 SARA examples (~ 20-30 min)\\n- Run extraction on all 25 sampled cases\\n- Compute precision/recall against gold .pl annotations\\n- CONFIRM: precision >= 0.75 before proceeding\\n- Log per-case results; note cases where extraction fails entirely\\n\\n### Step 4: End-to-end mini pipeline test (5 ProofWriter OWA examples, < 15 min)\\n- Run full stratified pipeline + both baselines on 5 ProofWriter examples\\n- Verify: method_out.json is written with correct schema\\n- Verify: proof trees are non-empty for at least 3/5 examples\\n- Verify: tier distribution shows at least some L0 facts (not all L3)\\n- Verify: cost tracking is working (TOTAL_COST > 0 and < $0.50 for 5 examples)\\n\\n### Step 5: LKIF ontology integration test\\n- Load LKIF OWL; query ancestors of class 'Obligation'\\n- Expected: returns ['Normative_thing', 'Qualified_norm', 'Norm', ...] (any non-empty list)\\n- If empty: check that lkif-core.owl was downloaded successfully and has class definitions\\n\\n### Step 6: Mini benchmark run (10% scale, ~1-2h)\\n- Run all 4 benchmarks at 10% scale (20/20/10/5 examples)\\n- Check: no crashes, results for all examples, metrics computable\\n- Check: total cost < $2.00 for mini run\\n- Decision: if runtime < 90 min and cost < $2, scale to 50%; else stay at 10% and report\\n\\n### Step 7: Final validation of method_out.json\\n- Verify JSON is valid and parseable\\n- Verify top-level keys: phase0_extraction_calibration, per_example_results, aggregate_metrics, total_cost_usd\\n- Verify per_example has required fields: id, benchmark, gold, stratified, symba, cot, tier_used, confidence\\n- Verify aggregate_metrics has accuracy for all 3 systems on all 4 benchmarks\\n- Apply aii-json skill to validate against expected schema\\n\\n### Confirmation signals before full scale\\n- Phase 0 precision >= 0.75 (HARD gate)\\n- Mini pipeline produces non-trivial tier distribution (not 100% L3)\\n- SymBa baseline produces non-trivially different results from stratified (if identical, check bug)\\n- Cost per example < $0.10 (to stay within budget for 100+ examples)\\n\\n### Known failure modes to watch for\\n- pyswip segfault under multiprocessing (use spawn not fork; or run Prolog in subprocess)\\n- owlready2 loading OWL-DL axioms with imports (some LKIF owl files import others; set onto_path to local dir)\\n- OpenRouter rate limits: add time.sleep(0.5) between L3 calls; implement exponential backoff\\n- CLUTRR data format varies by version: check field names before assuming story/query/target_text keys\"\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
````

### [30] ASSISTANT · 2026-06-15 20:11:00 UTC

```
The plan has been written to `.terminal_claude_agent_struct_out.json`. It covers:

- **Phase 0 gate**: SARA extraction calibration on 25 examples with 3 fallback prompt iterations if precision < 0.75
- **Full pipeline**: L0 (LLM extraction) → L1 (pyswip + `call_with_depth_limit/3`) → L2 (owlready2 LKIF from `github.com/RinkeHoekstra/lkif-core` + ConceptNet REST) → L3 (K=5 self-consistency abduction)
- **Weakest-link propagation**: tier = max(premise tiers), conf = min(premise confidences)
- **Baselines**: SymBa-style empty-KB + CoT
- **All 4 benchmarks**: SARA (GitHub SgfdDttt/sara), ProofWriter OWA (tasksource/proofwriter on HuggingFace), CLUTRR (HuggingFace CLUTRR org), ContractNLI (stanfordnlp.github.io)
- **Metrics**: multi-hop accuracy, hallucination rate (string-match check), tier distribution, ECE
- **7 concrete fallbacks** covering pyswip failure, LKIF load errors, dataset access issues, budget overrun, and API rate limits
- **Compute profile**: `cpu_heavy` (no GPU needed; SWI-Prolog + OWL reasoning + API calls are CPU/network bound)
```
