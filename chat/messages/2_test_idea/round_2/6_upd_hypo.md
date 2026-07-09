# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (terminal_claude_agent, claude-sonnet-4-6)

### [1] CONFIG · 2026-06-15 21:24:34 UTC

```
model: claude-sonnet-4-6 | effort: low | permission: bypassPermissions | cwd: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo
```

### [2] SYSTEM-USER prompt · 2026-06-15 21:24:40 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation

<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: >-
  Provenance-Stratified Neuro-Symbolic Reasoning: Tier-Ordered SLD Resolution with Document-Grounded KB and Calibrated OWA
  Propagation
hypothesis: >-
  A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit
  facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance
  tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed:
  LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and
  (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics (returning Unknown when all tiers
  fail rather than defaulting to False) will achieve measurably higher multi-hop reasoning accuracy than flat-KB pipelines
  on benchmarks with Unknown gold labels (specifically ProofWriter D* OWA), because the tier ordering prevents spurious False
  answers for goals that are unprovable within available evidence. Preliminary evidence from 200 ProofWriter OWA examples
  supports this claim: the stratified pipeline achieves 45.0% vs. SymBa-style baseline's 27.5% (+17.5 absolute points), a
  gap attributable to correct Unknown propagation where the baseline returns False. The companion hallucination-reduction
  and L2-ontology claims remain unverified and must be treated as secondary hypotheses pending (a) LLM-based L0 extraction
  replacing the current regex heuristic fallback, (b) targeted micro-evaluation tasks that actually trigger L2 LKIF/ConceptNet
  bridging, and (c) evaluation on real SARA and CLUTRR data with gold Prolog annotations — the first-iteration results on
  those two benchmarks used synthetic fallback data and are scientifically uninformative.
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
_relation_rationale: >-
  Same architecture; OWA Unknown-propagation elevated as primary claim; L2/hallucination demoted pending real tests.
_confidence_delta: decreased
_key_changes:
- >-
  Elevated the OWA Unknown-propagation benefit as the primary empirically supported claim (ProofWriter OWA +17.5 points with
  real HuggingFace data), replacing the previously equally-weighted hallucination-reduction claim which was not actually tested.
- >-
  Demoted L2 ontology contribution to an unverified secondary hypothesis: the experiment shows l2=0.0 trigger rate for all
  benchmarks; next iteration must include targeted micro-tasks where LKIF/ConceptNet bridging is required.
- >-
  Added explicit requirement that L0 extraction must use real LLM inference (not regex heuristics) with actual cost tracking;
  the $0 cost in iter-1 invalidates the extraction calibration gate and the architecture's core claim.
- >-
  SARA 100% accuracy and CLUTRR 0% accuracy are now explicitly flagged as uninformative (synthetic fallback data); these results
  are excluded from the confirmed evidence base.
- >-
  Phase 0 gate requirement sharpened: must use at least 25 real SARA cases with gold Prolog annotations and report true precision/recall
  against the gold KB, not synthetic examples.
- >-
  Hallucination measurement demoted from confirmed to planned: zero-hallucination result is a trivial artifact of no LLM calls
  being made; meaningful test requires L3 abduction to actually fire on withheld-L0 examples.
- >-
  Added explicit acknowledgment that CoT baseline achieves 54% overall (vs. 32% stratified) but this is inflated by ProofWriter
  calibration artifact; on SARA and ContractNLI alone the systems are at parity.
- >-
  Statistical power caveat added: n=50 results on ContractNLI are preliminary with ±14% CI; next iteration must use larger
  samples with McNemar tests or bootstrap CIs.
- >-
  Depth parameter clarified to d=5 (what was implemented) rather than d=3 (what hypothesis stated); depth calibration to extraction
  yield noted as a design requirement.
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

--- Item 1 ---
id: art_X97QZnbrLvC_
type: research
title: 'Technical Integration Reference: Four-Tier Neuro-Symbolic Pipeline'
summary: >-
  Comprehensive technical reference covering all nine integration points required to implement the provenance-stratified neuro-symbolic
  pipeline and reproduce the SymBa baseline. Key findings: (1) LKIF Core OWL is available via 15 modular GitHub raw URLs;
  norm.owl confirms Obligation, Prohibition, Permission, Right, Legal_Document, Contract class hierarchy under namespace http://www.estrellaproject.org/lkif-core/norm.owl#;
  load via owlready2 or rdflib. (2) pyswip (Python 3.9+, SWI-Prolog ≥8.x) provides assertz/asserta/retract/retractall; call_with_depth_limit/3
  returns integer depth on success, 'depth_limit_exceeded' atom on limit, fails if goal fails; NOT thread-safe — use multiprocessing.
  (3) ConceptNet API has 34 relations, no auth, 3600 req/hr; weights are 1.0–10.0 not 0.0–1.0 as assumed in hypothesis; legal
  coverage is a confirmed disconfirmation risk. (4) Wikidata SPARQL at https://query.wikidata.org/sparql requires User-Agent
  header; key QIDs: legal obligation=Q56297395, legal norm=Q216200 (planning-phase Q1756864 was wrong — it's a Brazilian municipality).
  (5) SymBa CONFIRMED starts with empty Prolog DB ('Initially, the solver cannot prove the provided goal because its symbolic
  database is empty'); LLM called on SLD Search failure; 5-module generation (Fact/Rule Search → Translation → Symbolic Validation);
  uses OpenAI API replaceable via base_url override; run via 'python hiereason/run_symba.py --dataset proofwriter_dep5'. (6)
  ProofWriter OWA configs use naming pattern {Type}{Neg}-OWA-D{depth}-{id}; enumerate with get_dataset_config_names(). (7)
  CLUTRR/v1 has 21 kinship labels, ~1048 test examples, proof_state field contains logical derivation. (8) SARA (jhu-clsp/SARA)
  has 376 cases, gold Prolog KB achieving 100% accuracy, neo-Davidsonian event semantics. (9) ContractNLI available without
  ToU at kiddothe2b/contract-nli (CC-BY-NC-SA-4.0); 607 NDAs, 17 hypotheses, 3 labels. All URLs verified live (except ConceptNet
  which returned 502 errors in June 2026).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_BlWQDL__yPLu
type: dataset
title: 'Reasoning Benchmark Datasets: ProofWriter OWA, ContractNLI, SARA, OpenBookQA'
summary: |-
  This artifact collects and standardizes four benchmark datasets for evaluating a neuro-symbolic FOL translation pipeline. The datasets cover distinct reasoning modalities and domains:

  1. **ProofWriter OWA** (4,998 examples, `tasksource/proofwriter`): Multi-hop natural language logical reasoning with three-valued labels (True/False/Unknown) under the Open World Assumption. Each example contains a theory (facts + rules in natural language) and a yes/no/unknown question. Proof depth ranges 0–5 hops. Domain: general. Source: AllenAI ProofWriter D* dataset via HuggingFace.

  2. **ContractNLI** (18,092 examples, `kiddothe2b/contract-nli`): Document-level natural language inference over NDA contract clauses. Labels: Entailment/Contradiction/NotMentioned. Each example pairs a contract clause (premise) with a hypothesis about confidentiality obligations. Domain: legal. Source: Stanford NLP ContractNLI (EMNLP 2021 Findings).

  3. **SARA** (376 examples, `SgfdDttt/sara`): US federal tax law statutory reasoning requiring multi-step application of tax code sections (151, 152). Each example includes a natural language case description, a yes/no tax obligation question, and gold Prolog predicate annotations for Phase 0 calibration. Train/test/phase0 splits preserved. Domain: legal. Source: SARA GitHub repo.

  4. **OpenBookQA** (4,957 examples, `allenai/openbookqa`): Science multi-hop QA requiring combination of a core science fact with reading comprehension. Each example has a core fact, a question, and 4 answer choices. Domain: science. Source: AllenAI OpenBookQA dataset.

  All 28,423 examples are standardized to the `exp_sel_data_out` schema with per-example `input` (formatted prompt), `output` (gold label), and `metadata_*` fields (domain, split, hop_count, task_type, original_id, gold_predicates for SARA). Schema validated with aii-json. Full dataset is 122MB split into 8 parts (all ≤ 50MB each) in `data_out/` due to file size limit. Mini (12 examples, 3 per dataset) and preview (12 examples truncated) versions provided.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_dvruFBLiCgfS
type: experiment
title: 'Provenance-Stratified Neuro-Symbolic Pipeline: L0-L3 Tier-Ordered SLD Evaluation'
summary: |-
  This artifact implements and evaluates a complete 4-tier provenance-stratified neuro-symbolic reasoning pipeline across four benchmarks (SARA, ProofWriter OWA, CLUTRR, ContractNLI). The pipeline architecture is:

  - **L0 (Document Extraction)**: LLM-based extraction of ground atomic Prolog facts from input documents using meta-llama/llama-3.1-70b-instruct via OpenRouter, with JSON validation and argument sanitization.
  - **L1 (Bounded SLD Resolution)**: SWI-Prolog subprocess interface with depth-limited (depth=5) SLD resolution using call_with_depth_limit/3, backed by a file-based KB with domain-specific rules (kinship chains for CLUTRR, if-then rules for ProofWriter).
  - **L2 (Domain-Adaptive Ontology)**: LKIF legal ontology subsumption (with fallback to a hardcoded 50-concept dictionary) for legal domains, and ConceptNet REST API for general/narrative domains.
  - **L3 (Self-Consistency LLM Abduction)**: K=3-5 self-consistency voting via LLM with confidence threshold 0.6; only invoked when L0-L2 fail.
  - **Weakest-Link Provenance**: Each proof node tracks its tier and confidence; compound proofs propagate max-tier and min-confidence.
  - **JSON-LD Trace Export**: Full derivation trees with tier colors for human auditability.

  Two baselines are implemented side-by-side:
  - **SymBa-style flat LLM**: Empty KB, single LLM call per query with no ontology tier.
  - **Chain-of-Thought (CoT)**: Multi-step LLM reasoning with True/False/Unknown extraction.

  Metrics computed:
  - Multi-hop accuracy (exact match) for all three systems across all four benchmarks
  - Hallucination rate (L0 fact grounding vs source document) for stratified vs SymBa
  - Tier distribution (fraction of proofs resolved at L0/L1/L2 without LLM abduction)
  - Expected Calibration Error (ECE) for L3 self-consistency confidence scores on SARA
  - Phase 0 extraction calibration: precision/recall of L0 facts vs gold Prolog annotations

  Key implementation details: L0 extraction caching to disk prevents redundant LLM calls on restarts; LKIF ontology fallback dict covers 15 core legal concepts; gradual scaling (mini 10% to 50% to 100%) with cost tracking against $9 hard limit; subprocess-based SWI-Prolog avoids threading issues.

  Datasets: ProofWriter OWA (real HuggingFace, 200 examples), CLUTRR (synthetic kinship, 200 examples), SARA (synthetic legal contracts, 50 examples), ContractNLI (synthetic NDA clauses, 50 examples).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_cy9EiwTnZMHv
type: evaluation
in_dependencies:
- id: art_dvruFBLiCgfS
  label: extends
title: Statistical Evaluation of Provenance-Stratified Neuro-Symbolic Pipeline
summary: |-
  This evaluation artifact computes comprehensive statistical metrics for the Provenance-Stratified Neuro-Symbolic Pipeline across four benchmarks (ProofWriter OWA n=200, SARA n=50, CLUTRR n=200, ContractNLI n=50; 500 total examples). Key findings:

  1. PER-BENCHMARK ACCURACY WITH 95% WILSON CIs:
     - SARA: Stratified=1.000 [0.929,1.000], SymBa=1.000, CoT=1.000
     - ProofWriter OWA: Stratified=0.450 [0.383,0.519], SymBa=0.275 [0.218,0.341], CoT=1.000
     - CLUTRR: Stratified=0.000 [0.000,0.019], SymBa=0.000, CoT=0.000
     - ContractNLI: Stratified=0.400 [0.276,0.538], SymBa=0.400, CoT=0.400

  2. McNemar PAIRED TEST: ProofWriter OWA shows significant stratified>SymBa (stat=55.0, p=0.0046*). All other benchmarks are tied (p=1.0).

  3. SEPARATE AGGREGATES (not averaged): Legal (SARA+ContractNLI): stratified=0.700, symba=0.700, cot=0.700. Multi-hop OWA (ProofWriter): stratified=0.450, symba=0.275, cot=1.000.

  4. HALLUCINATION: Both systems 0.0 — null result confirmed by Fisher exact test p=1.0. L3 abduction was never triggered, so no hallucination opportunity arose.

  5. L2/L3 TIERS VACUOUS: L2 trigger rate=0% across all 500 examples (Wilson CI [0.000,0.007]). ECE=N/A (L3 never triggered; all confidence=0.0).

  6. TIER DISTRIBUTION: ProofWriter OWA and CLUTRR show 100% Unknown tier; SARA and ContractNLI show 100% L0. Stacked bar chart saved to figures/tier_distribution.png.

  7. CALIBRATION: figures/calibration.png shows ECE=N/A placeholder with explanation.

  8. JSON-LD TRACES: 5 representative ProofWriter OWA examples (from 110 Unknown-vs-False candidates) exported to traces/trace_{0-4}.jsonld and traces/trace_{0-4}.html with tier-color-coded CSS visualization.

  9. PHASE 0: avg_facts_extracted=0.6, n_evaluated=5 (synthetic only — insufficient for production gate). LaTeX table flagged with caveat.

  10. LaTeX TABLES: eval_out_tables.tex contains three booktabs tables: (a) main accuracy+CI+McNemar table, (b) tier distribution table, (c) Phase 0 calibration table.

  All outputs validated against exp_eval_sol_out JSON schema. Full/mini/preview variants of eval_out.json generated. Files well within 100MB size limit (274KB each). pyproject.toml has pinned exact dependency versions.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</all_artifacts>

<new_artifacts_this_iteration>
These 1 artifacts were created THIS iteration.

id: art_cy9EiwTnZMHv
type: evaluation
in_dependencies:
- id: art_dvruFBLiCgfS
  label: extends
title: Statistical Evaluation of Provenance-Stratified Neuro-Symbolic Pipeline
summary: |-
  This evaluation artifact computes comprehensive statistical metrics for the Provenance-Stratified Neuro-Symbolic Pipeline across four benchmarks (ProofWriter OWA n=200, SARA n=50, CLUTRR n=200, ContractNLI n=50; 500 total examples). Key findings:

  1. PER-BENCHMARK ACCURACY WITH 95% WILSON CIs:
     - SARA: Stratified=1.000 [0.929,1.000], SymBa=1.000, CoT=1.000
     - ProofWriter OWA: Stratified=0.450 [0.383,0.519], SymBa=0.275 [0.218,0.341], CoT=1.000
     - CLUTRR: Stratified=0.000 [0.000,0.019], SymBa=0.000, CoT=0.000
     - ContractNLI: Stratified=0.400 [0.276,0.538], SymBa=0.400, CoT=0.400

  2. McNemar PAIRED TEST: ProofWriter OWA shows significant stratified>SymBa (stat=55.0, p=0.0046*). All other benchmarks are tied (p=1.0).

  3. SEPARATE AGGREGATES (not averaged): Legal (SARA+ContractNLI): stratified=0.700, symba=0.700, cot=0.700. Multi-hop OWA (ProofWriter): stratified=0.450, symba=0.275, cot=1.000.

  4. HALLUCINATION: Both systems 0.0 — null result confirmed by Fisher exact test p=1.0. L3 abduction was never triggered, so no hallucination opportunity arose.

  5. L2/L3 TIERS VACUOUS: L2 trigger rate=0% across all 500 examples (Wilson CI [0.000,0.007]). ECE=N/A (L3 never triggered; all confidence=0.0).

  6. TIER DISTRIBUTION: ProofWriter OWA and CLUTRR show 100% Unknown tier; SARA and ContractNLI show 100% L0. Stacked bar chart saved to figures/tier_distribution.png.

  7. CALIBRATION: figures/calibration.png shows ECE=N/A placeholder with explanation.

  8. JSON-LD TRACES: 5 representative ProofWriter OWA examples (from 110 Unknown-vs-False candidates) exported to traces/trace_{0-4}.jsonld and traces/trace_{0-4}.html with tier-color-coded CSS visualization.

  9. PHASE 0: avg_facts_extracted=0.6, n_evaluated=5 (synthetic only — insufficient for production gate). LaTeX table flagged with caveat.

  10. LaTeX TABLES: eval_out_tables.tex contains three booktabs tables: (a) main accuracy+CI+McNemar table, (b) tier distribution table, (c) Phase 0 calibration table.

  All outputs validated against exp_eval_sol_out JSON schema. Full/mini/preview variants of eval_out.json generated. Files well within 100MB size limit (274KB each). pyproject.toml has pinned exact dependency versions.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# Introduction

Neuro-symbolic reasoning systems combine the generalization capacity of large language models (LLMs) with the verifiability of symbolic logic. A common design pattern, exemplified by SymBa [1], begins with an *empty* symbolic database: when the SLD resolver fails to prove a goal, the LLM is queried to generate the next fact or rule. Under this design, the LLM is the first and only resort for all factual retrieval—including retrieval of facts that are explicitly present in the input document. The result is two structurally distinct failure modes. First, *hallucination*: the LLM may confabulate alternatives to document-stated content because no mechanism prevents it from generating facts independently of the source text. Second, *opacity*: the derivation trace records that the LLM supplied a fact, but not whether that fact was document-recoverable, ontologically entailed, or a genuine abduction from world knowledge, rendering the trace unauditable.

A critical consequence of SymBa's design appears in benchmarks that require *three-valued* Open World Assumption (OWA) semantics: when a goal is unprovable, the correct answer may be *Unknown* rather than *False*. The SymBa pipeline has no mechanism to distinguish the two: it invokes the LLM on proof failure and returns its (typically binary) response. A system that instead exhausts cheaper evidence tiers first and returns *Unknown* when all tiers fail would correctly answer such questions without any LLM call.

We propose a *provenance-stratified* pipeline that enforces tier-ordered escalation: L0 (document extraction) → L1 (bounded SLD) → L2 (domain ontology) → L3 (LLM abduction). Each proof-tree node carries an explicit (tier, confidence) tuple propagated under weakest-link semantics. The primary behavioral difference from SymBa is that when L0 extraction fails to prove a leaf goal, the system does not immediately invoke the LLM; it first tries L1 deductive closure and L2 ontology, and only returns a definite answer if one of these tiers succeeds. If all tiers fail, the system returns *Unknown*.

[FIGURE:fig1]

We evaluate this architecture on ProofWriter D*(OWA) [9], a three-valued benchmark where *Unknown* is the correct label for goals that are not provable from the given theory. On 200 examples drawn from the real HuggingFace dataset, the stratified pipeline achieves 45.0% accuracy versus the SymBa-style baseline's 27.5% (McNemar p = 0.0046). The +17.5 point gain is entirely attributable to correct *Unknown* propagation: the stratified system outputs *Unknown* for 200/200 ProofWriter OWA examples where the L0 extraction does not supply provable facts, while SymBa defaults to *False*. [ARTIFACT:art_cy9EiwTnZMHv]

We report with equal clarity what the current evaluation does *not* support. The L0 tier used heuristic regex extraction rather than the proposed LLM-based extraction, incurring zero API cost. The L2 tier (LKIF/ConceptNet/Wikidata) was never triggered across 500 examples. L3 self-consistency abduction was never invoked. Secondary claims regarding hallucination reduction and L2 ontology coverage therefore remain empirically unverified.

**Summary of contributions:**
- A complete four-tier neuro-symbolic architecture with tier-ordered SLD escalation and weakest-link provenance propagation (Section 3).
- Empirical evidence that OWA Unknown propagation—returning *Unknown* when no tier proves a goal—outperforms SymBa's False-by-default on ProofWriter D*(OWA): 45.0% vs. 27.5%, McNemar p = 0.0046 (Section 4).
- JSON-LD trace export with per-node (tier, confidence) annotations for human-auditable derivations (Section 3.6).
- An honest experimental accounting: identification of which claims are confirmed, which are unverified, and a concrete agenda for future work (Section 5).

# Related Work

**Neuro-symbolic SLD resolution.** SymBa [1] integrates SLD-resolution with an LLM via a coroutine that calls the LLM on every proof failure. Its five-module generation pipeline (Fact Search, Rule Search, Translation, Symbolic Validation, Backtracking) uses the LLM as the sole knowledge source because the KB starts empty. The proposed system differs architecturally by pre-populating the KB from the document (L0) and inserting a domain ontology tier (L2) before any LLM invocation. Under SymBa's design, an unprovable goal triggers an LLM call that will return a binary yes/no, making it structurally incapable of returning *Unknown* for OWA benchmarks.

**FOL translation and theorem proving.** LINC [5] uses an LLM to translate natural language premises into first-order logic and delegates proof search to a Prolog prover. Proof failures return *unknown* without LLM escalation, has no ontology integration, and produces no provenance-annotated trace. Logic-LM [6] extends this with iterative LLM feedback on proof failures but lacks per-predicate provenance annotation or ontology integration. FOLIO [13] provides a challenging benchmark for FOL reasoning from natural language premises.

**Hybrid reasoning with ordered fallback.** ROSCOE [14] evaluates step-by-step reasoning chains with ordered metrics but does not perform symbolic execution. Systems combining symbolic solvers with neural components have appeared across multiple venues, but the specific combination of document-grounded KB initialization, bounded SLD, domain-adaptive ontology, and LLM abduction with per-node provenance propagation has not, to our knowledge, been published. The weakest-link propagation rule differs from Markov Logic Networks [15], which assign a single weight to each formula rather than propagating epistemic-source labels through proof trees. DeepProbLog [8] assigns uncertainty from a single neural distribution rather than from a named evidence hierarchy.

**Retrieval-augmented generation.** RAG systems [7] retrieve context passages to ground LLM generation. RAG operates at the token level and produces no symbolic proof trace; individual retrieved facts carry no epistemic tier label. The proposed system's derivations are SLD-resolution trees in which each leaf node is labeled by source tier.

**Legal and statutory reasoning.** Holzenberger et al. [10] demonstrated that a hand-constructed Prolog knowledge base pre-populated from statutory text achieves 100% accuracy on the SARA benchmark, precisely because document-explicit facts are retrieved symbolically rather than generatively. The LKIF Core OWL ontology [4] provides a principled terminological foundation for legal concepts. ContractNLI [3] documents that complex hedged language in non-disclosure agreements is a primary source of NLI difficulty.

# Methods

## System Architecture

The pipeline processes each input document through four sequentially escalating tiers. [ARTIFACT:art_dvruFBLiCgfS]

**L0 — Document-Grounded KB Initialization.** Given an input document, the L0 extractor identifies atomic Prolog predicates and asserts them as `fact(Pred, l0, 1.0)` in SWI-Prolog before any reasoning begins. Domain-specific rules stated explicitly in the document are stored as `rule(Head, Body, l0, 1.0)`. The design specifies LLM-based extraction (meta-llama/llama-3.1-70b-instruct via OpenRouter with structured JSON prompts); the current evaluation used a heuristic regex extractor as a baseline implementation. A disk-based cache prevents redundant calls on pipeline restarts. The L0 initialization step is the primary architectural departure from SymBa: the KB is populated from the document before the resolver is invoked.

**L1 — Bounded SLD Resolution.** Once L0 facts are asserted, the meta-interpreter executes a full SWI-Prolog query with `call_with_depth_limit/3` at depth $d = 5$ and no new predicate invention. A goal that succeeds within the depth limit is resolved at tier L1 with confidence 1.0. A goal that returns `depth_limit_exceeded` or fails triggers escalation to L2. SWI-Prolog is interfaced via subprocess rather than the pyswip FFI to avoid thread-safety issues in concurrent evaluation.

**L2 — Domain-Adaptive Ontology.** The document domain is classified at runtime into legal, narrative, or general. For legal documents, the LKIF Core OWL ontology [4] is consulted via class-subsumption queries covering the concept hierarchy {Obligation, Prohibition, Permission, Right, Legal\_Document, Contract, Norm, Agent}; a fallback dictionary of 50 LKIF concepts handles cases where the OWL parser is unavailable. For narrative documents, the ConceptNet REST API [11] is queried for IsA, PartOf, and UsedFor relations. For general-domain documents, Wikidata SPARQL is queried with a required User-Agent header. Confirmed L2 facts are cached as `fact(Pred, l2, c)` where $c = 0.95$ for OWL subsumption entailment and $c = 0.80$ for ConceptNet statistical association edges.

**L3 — Self-Consistency LLM Abduction.** Only when L0, L1, and L2 all fail to prove a leaf goal does the meta-interpreter invoke L3 abduction. An abductive schema template query is constructed from the failed goal's predicate name, partially bound arguments, and the parent proof context, then submitted independently $K = 5$ times to the LLM. The L3 confidence is the fraction of *yes* responses. Facts with confidence below 0.6 are flagged *low-confidence abduction*; at threshold $\tau = 0.4$, the system returns *Unknown* rather than asserting falsity, implementing three-valued OWA semantics.

**Weakest-Link Provenance Propagation.** For a derived goal with premises $p_1, \ldots, p_n$, the propagated tier is $\mathrm{Tier}(\mathrm{derived}) = \max_i \mathrm{Tier}(p_i)$ and the propagated confidence is $\mathrm{Conf}(\mathrm{derived}) = \min_i \mathrm{Conf}(p_i)$. Comparison is lexicographic: tier label takes priority over confidence. This rule ensures that a conclusion citing any L3 abduction propagates an L3 label regardless of how many L0 premises contributed to the proof. The rule is analogous to integrity-label propagation in the Biba model: a conclusion is only as trustworthy as its least-trusted premise.

**JSON-LD Trace Export.** The complete derivation tree is exported as a JSON-LD document with each node labeled \{predicate, args, tier, confidence, source\_doc\_span\}. A static HTML visualization color-codes tier labels: green for L0, yellow for L1, orange for L2, red for L3, gray for Unknown. These traces are the primary interpretability artifact.

[FIGURE:fig2]

## Baselines

Two baselines are evaluated alongside the stratified pipeline.

*SymBa-style flat LLM.* Following SymBa [1], the baseline starts with an empty Prolog KB and issues a single structured LLM call for each query with no ontology tier. The LLM response is parsed for a yes/no/true/false/unknown determination and mapped to the benchmark answer space. Under this design, when a goal is unprovable from the empty KB, the system returns whatever the LLM generates; it has no mechanism to propagate *Unknown* for genuinely underdetermined goals.

*Chain-of-Thought (CoT).* The LLM is prompted with the full document and question using multi-step chain-of-thought prompting [12], and the final answer is extracted by regex matching on True/False/Unknown/Entailment/Contradiction keywords.

# Results

## Experimental Setup

Four benchmarks were targeted. Two produced informative results; two did not.

*ProofWriter D*(OWA)* [9] (200 examples, real HuggingFace data, `tasksource/proofwriter`): Multi-hop logical reasoning under Open World Assumption with three-valued True/False/Unknown labels. This is the primary benchmark. [ARTIFACT:art_BlWQDL__yPLu]

*ContractNLI* [3] (50 examples, synthetic fallback): NDA clause entailment with three labels. **Caveat:** the evaluation used a synthetic dataset generator, not the real ContractNLI corpus (607 NDAs). Results on these 50 synthetic examples are reported for completeness but do not constitute evaluation on ContractNLI.

*SARA* [10] (50 examples, synthetic fallback): US federal tax law reasoning. **Caveat:** the evaluation used a synthetic generator cycling through 5 generic contract templates (`sara_synth_0` through `sara_synth_49`), not the real SARA benchmark with gold Prolog KB annotations. The 100% accuracy reported is an artifact of trivially-structured template patterns that all three systems match identically; it is not a meaningful statutory reasoning result.

*CLUTRR* [16] (200 examples, synthetic fallback): Kinship reasoning. All three systems achieved 0% due to a label format mismatch between the synthetic generator's output (`grandmother`, `father`) and the answer extractor (which returned `proved`/`unknown`). This result is entirely uninformative and is excluded from the main results table.

All ProofWriter OWA examples are drawn from the real HuggingFace dataset and are the only results treated as valid evidence for claims about the pipeline's capabilities.

## Main Results

Table 1 reports per-benchmark accuracy with 95% Wilson confidence intervals and McNemar's test for the stratified vs. SymBa comparison. CLUTRR is excluded from the table; its all-zero result is a data-loading artifact rather than a meaningful capability measurement.

| Benchmark | $n$ | Stratified | SymBa | CoT | McNemar $p$ |
|---|---|---|---|---|---|
| ProofWriter OWA (real) | 200 | **0.450** [0.383, 0.519] | 0.275 [0.218, 0.341] | 1.000 [0.981, 1.000] | **0.0046*** |
| SARA (synthetic only†) | 50 | 1.000 | 1.000 | 1.000 | 1.0 |
| ContractNLI (synthetic only†) | 50 | 0.400 [0.276, 0.538] | 0.400 | 0.400 | 1.0 |

†Synthetic fallback data; results are not evaluations of the named benchmark.

The stratified pipeline outperforms the SymBa-style flat baseline on ProofWriter OWA (45.0% vs. 27.5%, absolute +17.5 points, McNemar p = 0.0046). On the synthetic SARA and ContractNLI data, all three systems are tied; these results carry no interpretive weight.

The CoT baseline achieves 100% on ProofWriter OWA. This result reflects that the CoT answer extractor was calibrated on the ProofWriter OWA answer distribution (True/False/Unknown keywords), giving it an in-distribution advantage. The CoT result on ProofWriter OWA should not be interpreted as a fair baseline comparison; it is reported for completeness.

[FIGURE:fig3]

## Analysis of the ProofWriter OWA Result

The stratified pipeline's ProofWriter OWA advantage is mechanically explained. When the L0 heuristic extractor processes a ProofWriter theory (average 4.94 facts per theory), the extracted predicates are surface-form property attributions that do not match the queried goal predicates (which require multi-hop chaining). The L1 depth-5 SLD resolver cannot chain from the extracted surface predicates to the queried property. L2 and L3 are not triggered in this evaluation. The meta-interpreter therefore returns *Unknown* for all 200 examples.

Of the 200 ProofWriter OWA examples, the gold label distribution is: True (approx. 60 examples), False (approx. 50 examples), Unknown (approx. 90 examples). The stratified system's 90 correct answers come entirely from the 90 Unknown-labeled examples—for which returning *Unknown* is correct. The SymBa baseline, which defaults to *False* on proof failure, achieves 0 correct on Unknown-labeled examples and 55 correct on False-labeled examples, for a total of 55/200 = 27.5%. The McNemar b–c counts (b = 90, c = 55) confirm this picture: the stratified system wins on 90 examples the SymBa baseline gets wrong (the Unknown-labeled examples) and loses on 55 examples SymBa gets right (the False-labeled examples).

This analysis makes the mechanism transparent: the +17.5 point gain on ProofWriter OWA comes from the tier-ordered architecture's OWA semantics, specifically its ability to return *Unknown* for unprovable goals rather than collapsing to *False*.

## Tier Distribution

Across all 500 examples, the L2 tier was triggered zero times (Wilson 95% CI: [0.000, 0.007]). For SARA and ContractNLI (synthetic), 100% of resolved examples were attributed to the L0 tier. For ProofWriter OWA and CLUTRR (synthetic), 100% of examples returned *Unknown* (the L1 SLD resolver could not chain from extracted surface predicates to the queried property). L3 was never invoked; total inference cost was $0.00. [ARTIFACT:art_cy9EiwTnZMHv]

[FIGURE:fig4]

## Unverified Claims

Three secondary claims from the hypothesis are explicitly unverified in this evaluation:

1. *LLM-based L0 extraction.* The evaluation used a regex heuristic extractor. The proposed LLM-based extraction was designed but not run. No API calls were made; the $0 cost confirms this. The Phase 0 gate—which required precision $\geq 0.75$ against gold SARA Prolog annotations on 25 real cases—was evaluated on 5 synthetic examples with no gold annotations, making it scientifically invalid.

2. *L2 ontology bridging.* The L2 tier (LKIF, ConceptNet, Wikidata) was never triggered for any of the 500 examples. A system with three active tiers (L0, L1, L3) rather than four would produce identical results on this evaluation. The L2 contribution is entirely untested.

3. *Hallucination reduction.* The paper's previous draft claimed zero hallucination rates on SARA and ContractNLI as evidence for L0 grounding. This claim was vacuous: no LLM calls were made, so no hallucination was possible by construction. A meaningful hallucination measurement requires L3 abduction to fire on withheld-L0 examples; that experiment was not conducted.

# Discussion

## What the Evidence Supports

The one empirically supported claim is that tier-ordered OWA Unknown propagation significantly outperforms SymBa-style False-by-default on ProofWriter D*(OWA): 45.0% vs. 27.5% (p = 0.0046). The mechanism is clear: the stratified system correctly returns *Unknown* for goals unprovable within available evidence, while SymBa returns *False*. This improvement requires no LLM calls and no ontology lookups—it is a structural consequence of the tier-ordered architecture's OWA semantics.

This finding has practical significance. Many real-world reasoning tasks involve genuinely underdetermined questions where the appropriate response is epistemic humility rather than a confident False answer. A system that conflates "not provable from the document" with "false" will systematically over-claim, a failure mode that the stratified architecture avoids by construction.

## Limitations and Future Work

Four concrete limitations bound the current results.

*(1) Benchmark data integrity.* The SARA, ContractNLI, and CLUTRR evaluations used synthetic fallback data due to implementation failures in the real-data loaders. These results carry no evidentiary weight. Future evaluation must use: `SgfdDttt/sara` (376 cases, gold Prolog KB) for SARA, `kiddothe2b/contract-nli` (607 NDAs) for ContractNLI, and `CLUTRR/v1` (gen\_train234\_test2) for CLUTRR. The CLUTRR zero-accuracy result is a label-format implementation artifact and will not carry over to real data.

*(2) L0 extraction implementation.* The LLM-based extraction described in the Methods section was not run. The current evaluation is best understood as a comparison between a tier-ordered Unknown-propagator (stratified) and a False-by-default system (SymBa), both operating on heuristic surface-pattern KB initialization. The extraction calibration gate (Phase 0) must be re-executed on real SARA cases with gold Prolog annotations.

*(3) L2 ontology integration.* The LKIF fallback dictionary covers only 50 concepts. For ContractNLI clauses involving conditional obligations and exception logic, subsumption hierarchy alone is insufficient; SWRL rules expressing normative entailment patterns are required. The Wikidata integration requires entity linking to populate QID-based queries. Targeted micro-evaluation tasks—legal questions requiring LKIF subsumption (e.g., is a contract a Legal\_Document?), narrative questions requiring ConceptNet (e.g., is a scalpel UsedFor cutting?)—must be designed to force L2 triggering and measure its accuracy.

*(4) Statistical power.* The ContractNLI and SARA results (n = 50 each) are too small for meaningful conclusions. The ContractNLI tie at 40% has a $\pm 13\%$ confidence interval at 95%, making the systems statistically indistinguishable. Evaluation on the full real ContractNLI test set (607 NDAs $\times$ 17 hypotheses) would reduce this to $\pm 1.4\%$.

## Comparison to Chain-of-Thought

The CoT baseline achieves 100% on ProofWriter OWA, but this result is not a fair comparison: the CoT answer extractor was calibrated on the ProofWriter OWA distribution. When the calibration artifact is set aside, the meaningful comparison is stratified vs. SymBa, for which the statistical evidence is clear. The CoT baseline remains useful as an indicator of what a well-calibrated purely-neural system can achieve on closed logical theories; the stratified pipeline is designed to complement CoT by providing symbolic provenance traces and OWA-correct Unknown responses, not to universally surpass neural approaches.

# Conclusion

We presented a provenance-stratified neuro-symbolic reasoning pipeline that enforces tier-ordered SLD escalation through L0 document extraction, L1 bounded deduction, L2 domain-adaptive ontology, and L3 LLM abduction, with weakest-link (tier, confidence) provenance propagation at every proof-tree node. On the one benchmark where real data was used (ProofWriter D*(OWA), n = 200), the stratified pipeline significantly outperforms the SymBa-style flat empty-database baseline (45.0% vs. 27.5%, McNemar p = 0.0046), with the gain attributable to correct Unknown propagation for unprovable goals under Open World Assumption semantics.

The paper is explicit that secondary claims—LLM-based L0 extraction, L2 ontology bridging, and hallucination reduction—were not tested in the current evaluation. Future work must: (a) run the LLM-based L0 extraction pipeline and validate against real SARA gold Prolog annotations; (b) design micro-tasks that force L2 LKIF/ConceptNet triggering; (c) evaluate hallucination by deliberately withholding L0 facts to trigger L3 abduction; and (d) evaluate on real SARA, ContractNLI, and CLUTRR data.

# References

[1] Baek, J., Jeong, S., Kang, M., Park, J. C., & Hwang, S. J. (2025). SymBa: Symbolic Backward Chaining for Multi-step Reasoning with Large Language Models. *NAACL 2025*.

[2] Holzenberger, N., Blair-Stanek, A., & Van Durme, B. (2020). A Dataset and Baselines for Sequential Open-Domain Question Answering over Statutory Text. *NLLP@KDD 2020*. SARA benchmark.

[3] Koreeda, Y., & Manning, C. D. (2021). ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts. *EMNLP 2021 Findings*, 1907–1919.

[4] Hoekstra, R., Breuker, J., Di Bello, M., & Boer, A. (2007). The LKIF Core Ontology of Basic Legal Concepts. *Estrella Project Deliverable*.

[5] Olausson, T. X., Gu, A., Lipkin, B., Zhang, C. E., Solar-Lezama, A., Tenenbaum, J. B., & Levy, R. P. (2023). LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. *EMNLP 2023*, 5153–5176.

[6] Pan, L., Albalak, A., Wang, X., & Wang, W. Y. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. *EMNLP 2023 Findings*.

[7] Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS 2020*.

[8] Manhaeve, R., Dumancic, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural Probabilistic Logic Programming. *NeurIPS 2018*.

[9] Tafjord, O., Dalvi, B., & Clark, P. (2021). ProofWriter: Generating Implications, Proofs, and Abductive Statements over Natural Language. *ACL 2021 Findings*, 3621–3634.

[10] Holzenberger, N., & Van Durme, B. (2023). Statute-based Statutory Reasoning with Legal Information Extraction. *NLLP 2023*.

[11] Speer, R., Chin, J., & Havasi, C. (2017). ConceptNet 5.5: An Open Multilingual Graph of General Knowledge. *AAAI 2017*, 4444–4451.

[12] Wei, J., et al. (2022). Chain of Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022*.

[13] Han, S., et al. (2022). FOLIO: Natural Language Reasoning with First-Order Logic. *EMNLP 2022 Findings*.

[14] Golovneva, O., et al. (2022). ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning. *arXiv:2212.07919*.

[15] Richardson, M., & Domingos, P. (2006). Markov Logic Networks. *Machine Learning*, 62, 107–136.

[16] Sinha, K., Sodhani, S., Dong, J., Pineau, J., & Hamilton, W. L. (2019). CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text. *EMNLP 2019*, 4505–4514.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) The stratified pipeline returns Unknown for all 200 ProofWriter OWA examples (confirmed by eval_out.json: tier_dist unknown=1.0, l0=0, l1=0, l2=0, l3=0). This means the 45% accuracy equals exactly the Unknown base rate in the dataset (~90/200 examples labeled Unknown). The system is not performing stratified reasoning—it is acting as a constant Unknown predictor. The +17.5% gain over SymBa therefore measures the benefit of choosing Unknown as the default return value, not the benefit of a four-tier architecture. A one-line baseline that always returns Unknown would achieve the same 45% accuracy without any of the proposed machinery.
  Action: Implement and report a 'constant-Unknown baseline' that always returns Unknown. If it achieves 45%, the paper's current result is indistinguishable from this trivial baseline. To claim architectural benefit, the paper needs at least one benchmark or sub-experiment where different tiers fire and contribute differently. Alternatively, reframe the paper explicitly as validating the OWA Unknown-propagation design choice rather than the full tier architecture.
- [MAJOR] (novelty) The empirically supported finding—that a system with OWA semantics (return Unknown when unprovable) beats a system without OWA semantics (return False when unprovable) on a three-valued OWA benchmark—is a definitional consequence of three-valued logic semantics, not an empirical discovery. The ProofWriter D*(OWA) benchmark was specifically designed to test OWA reasoning; any system implementing OWA Unknown-propagation will outperform a closed-world False-default system on it by construction. LINC (Olausson et al., EMNLP 2023) and ProofWriter's original evaluation already establish this. The paper needs to show novelty beyond the OWA default choice.
  Action: Benchmark against LINC and Logic-LM on ProofWriter OWA—both are directly applicable baselines that also return unknown on proof failure. If published results exist for these systems on ProofWriter D*(OWA), include them in Table 1. The stratified pipeline's contribution must differentiate from these systems, which already implement the Unknown-propagation behavior the paper claims as novel.
- [MAJOR] (methodology) Three of four benchmarks used synthetic fallback data (SARA, ContractNLI) or had label-format artifacts (CLUTRR). The paper now discloses this clearly, but the consequence is that the entire evaluation rests on a single benchmark (ProofWriter OWA, n=200), and on that benchmark the system achieves its results through a constant-Unknown mechanism. This is insufficient empirical support for a four-tier architecture paper at ACL/EMNLP, which typically expects evaluation on at least 2-3 real benchmarks with working system components.
  Action: Before the next submission, load and evaluate on real SARA (SgfdDttt/sara, 376 cases) and real ContractNLI (kiddothe2b/contract-nli). These datasets are confirmed available (art_X97QZnbrLvC_ documents their HuggingFace paths and licenses). Even a 50-example pilot on real SARA with working LLM extraction would significantly strengthen the evaluation, especially since SARA has gold Prolog annotations enabling L0 precision/recall measurement.
- [MAJOR] (methodology) The paper's Description of L0 extraction as LLM-based (meta-llama/llama-3.1-70b-instruct) while the actual experiment used regex heuristics creates a fundamental mismatch between the architecture and the evaluation. Since L0 regex extraction failed completely on ProofWriter OWA (0 facts matched), the tier architecture never had the opportunity to demonstrate its intended behavior. The evaluation does not test the proposed system—it tests a degenerate configuration where the first tier always fails.
  Action: Run the LLM-based L0 extraction on at least a 25-50 example subset of ProofWriter OWA and report extraction statistics (facts extracted per example, SLD resolution success rate, tier distribution). Compare accuracy between LLM-extracted L0 and regex-extracted L0 to measure the L0 extraction quality impact. The cost at 25 examples with llama-3.1-70b-instruct via OpenRouter should be well under $1.
- [MAJOR] (scope) The paper does not compare against LINC or Logic-LM, which are the most directly comparable published systems for neural-symbolic reasoning with Unknown propagation on logical benchmarks. Both systems are cited in Related Work but excluded from the experimental comparison. LINC in particular uses an LLM to translate premises to FOL and returns unknown on proof failure—making it a near-direct baseline for the proposed approach.
  Action: Add LINC and Logic-LM as baselines in Table 1, using published results from their papers if re-running is infeasible. If the stratified pipeline cannot match LINC on ProofWriter OWA (where LINC has published results), explain why and what the proposed system offers that LINC does not.
- [MINOR] (rigor) The weakest-link provenance propagation rule (max tier, min confidence) is asserted without theoretical justification or comparison to alternatives. The paper notes analogy to the Biba integrity model but does not prove this is optimal for the use case. Alternative rules (product of confidences, Dempster-Shafer combination, log-sum of log-odds) are mentioned in passing but dismissed without argument.
  Action: Add a paragraph in Section 3.5 providing a formal argument or theorem for why weakest-link semantics is preferable over product-of-confidences for audit applications. The key claim is that a single low-tier premise should invalidate the entire derivation's trustworthiness—state this as an axiom with a concrete legal/audit example (e.g., if one premise in a contract obligation derivation comes from LLM abduction, the entire conclusion should be flagged as L3-quality regardless of how many L0 premises contributed).
- [MINOR] (clarity) The gold label distribution of ProofWriter OWA (approx. 60 True / 50 False / 90 Unknown) is buried in the analysis section but not included in the main results table. Without this, readers cannot verify that the 45% accuracy equals the Unknown base rate, nor understand the mechanism of the SymBa comparison (55 correct False-labeled vs. 90 correct Unknown-labeled examples).
  Action: Add a column to Table 1 showing the label distribution (n_true, n_false, n_unknown) for each benchmark. For ProofWriter OWA, this makes immediately transparent that the stratified system's 90 correct answers come entirely from Unknown-labeled examples, which is both the paper's honest claim and its most important caveat.
</reviewer_feedback>



<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
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
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title (may be unchanged if still accurate)",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [3] HUMAN-USER prompt · 2026-06-15 21:24:40 UTC

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

### [4] TOOL CALL — Write · 2026-06-15 21:25:20 UTC

```
File: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json

{
  "title": "Provenance-Stratified Neuro-Symbolic Reasoning: LLM-Grounded L0 Extraction as the Prerequisite Gate for Tier-Architecture Evaluation",
  "hypothesis": "A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed: LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics will demonstrate measurable benefit over both (a) the SymBa flat-LLM baseline AND (b) a constant-Unknown trivial baseline, IF AND ONLY IF the L0 LLM extraction tier fires successfully (precision ≥ 0.75 on gold-annotated SARA cases) and the L1 SLD resolver achieves non-trivial chaining on LLM-extracted predicates. The current iteration's ProofWriter OWA result (45.0% vs. SymBa 27.5%, McNemar p=0.0046) is NOT evidence for the tier architecture: it is identical in value to the Unknown base rate (~90/200 examples), meaning the system operates as a constant-Unknown predictor that cannot be distinguished from a zero-cost trivial baseline. The mechanistic cause is that the regex-based L0 extractor failed to produce predicates matchable by the L1 SLD resolver, causing the meta-interpreter to return Unknown for all 200 examples — which happens to equal the 45.0% Unknown base rate. This result is therefore consistent with the null hypothesis that no tier machinery is required. To establish genuine architectural benefit, the next iteration must: (1) run real LLM-based L0 extraction on ProofWriter OWA or SARA examples and verify that the L1 SLD resolver chains successfully from LLM-extracted predicates to answer True/False queries — demonstrating that the pipeline resolves something other than Unknown; (2) implement and report a constant-Unknown baseline alongside SymBa and LINC/Logic-LM to expose whether any improvement over it exists; (3) evaluate on real SARA (SgfdDttt/sara, 376 cases with gold Prolog KB) and real ContractNLI (kiddothe2b/contract-nli, 607 NDAs) to provide multi-benchmark evidence; and (4) design at least one micro-evaluation task where L2 LKIF or ConceptNet bridging is required and the system's answer differs from both True and Unknown. Until these experiments produce results, the hypothesis that the tier architecture outperforms constant-Unknown remains empirically unverified. The secondary hallucination-reduction and L2-ontology claims remain unverified pending L3 abduction firing on withheld-L0 examples.",
  "relation_type": "evolution",
  "relation_rationale": "Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.",
  "confidence_delta": "decreased",
  "key_changes": [
    "Demoted the ProofWriter OWA +17.5% result from 'empirical support' to 'consistent with trivial constant-Unknown baseline' — the system returned Unknown for all 200 examples, matching the dataset's Unknown base rate exactly. This is not architectural evidence.",
    "Added explicit requirement to implement and report a constant-Unknown baseline in every future evaluation table, so readers can verify whether the stratified pipeline beats the trivial predictor.",
    "Elevated LLM-based L0 extraction (not regex) to the mandatory prerequisite gate: no architectural claim is testable until L1 SLD chaining succeeds on LLM-extracted predicates for at least some True/False-labeled examples.",
    "Added requirement to benchmark against LINC and Logic-LM (not just SymBa) since both systems implement Unknown-propagation on proof failure and are the appropriate baselines for OWA accuracy comparisons.",
    "Specified that the Phase 0 gate must produce precision/recall against gold SARA Prolog annotations on real cases (SgfdDttt/sara), not synthetic examples — the iter-1 Phase 0 on 5 synthetic cases was scientifically invalid.",
    "Added requirement for at least one micro-evaluation task that forces L2 LKIF/ConceptNet firing, producing a non-Unknown answer, before L2 coverage can be evaluated.",
    "Flagged SARA 100%, ContractNLI 40%, CLUTRR 0% as entirely uninformative (synthetic data / label artifacts) — these are removed from the confirmed evidence base.",
    "The core architectural hypothesis (tier ordering beats flat LLM) is preserved but its empirical status is correctly set to 'unverified' pending LLM L0 extraction implementation."
  ],
  "artifact_relations": [
    {
      "from_id": "art_dvruFBLiCgfS",
      "to_id": "art_cy9EiwTnZMHv",
      "relation_type": "uses",
      "relation_rationale": "Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis."
    }
  ]
}
```

### [5] TOOL RESULT — Write · 2026-06-15 21:25:20 UTC

```
{"type": "create", "filePath": "/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "content": "{\n  \"title\": \"Provenance-Stratified Neuro-Symbolic Reasoning: LLM-Grounded L0 Extraction as the Prerequisite Gate for Tier-Architecture Evaluation\",\n  \"hypothesis\": \"A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed: LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics will demonstrate measurable benefit over both (a) the SymBa flat-LLM baseline AND (b) a constant-Unknown trivial baseline, IF AND ONLY IF the L0 LLM extraction tier fires successfully (precision ≥ 0.75 on gold-annotated SARA cases) and the L1 SLD resolver achieves non-trivial chaining on LLM-extracted predicates. The current iteration's ProofWriter OWA result (45.0% vs. SymBa 27.5%, McNemar p=0.0046) is NOT evidence for the tier architecture: it is identical in value to the Unknown base rate (~90/200 examples), meaning the system operates as a constant-Unknown predictor that cannot be distinguished from a zero-cost trivial baseline. The mechanistic cause is that the regex-based L0 extractor failed to produce predicates matchable by the L1 SLD resolver, causing the meta-interpreter to return Unknown for all 200 examples — which happens to equal the 45.0% Unknown base rate. This result is therefore consistent with the null hypothesis that no tier machinery is required. To establish genuine architectural benefit, the next iteration must: (1) run real LLM-based L0 extraction on ProofWriter OWA or SARA examples and verify that the L1 SLD resolver chains successfully from LLM-extracted predicates to answer True/False queries — demonstrating that the pipeline resolves something other than Unknown; (2) implement and report a constant-Unknown baseline alongside SymBa and LINC/Logic-LM to expose whether any improvement over it exists; (3) evaluate on real SARA (SgfdDttt/sara, 376 cases with gold Prolog KB) and real ContractNLI (kiddothe2b/contract-nli, 607 NDAs) to provide multi-benchmark evidence; and (4) design at least one micro-evaluation task where L2 LKIF or ConceptNet bridging is required and the system's answer differs from both True and Unknown. Until these experiments produce results, the hypothesis that the tier architecture outperforms constant-Unknown remains empirically unverified. The secondary hallucination-reduction and L2-ontology claims remain unverified pending L3 abduction firing on withheld-L0 examples.\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Demoted the ProofWriter OWA +17.5% result from 'empirical support' to 'consistent with trivial constant-Unknown baseline' — the system returned Unknown for all 200 examples, matching the dataset's Unknown base rate exactly. This is not architectural evidence.\",\n    \"Added explicit requirement to implement and report a constant-Unknown baseline in every future evaluation table, so readers can verify whether the stratified pipeline beats the trivial predictor.\",\n    \"Elevated LLM-based L0 extraction (not regex) to the mandatory prerequisite gate: no architectural claim is testable until L1 SLD chaining succeeds on LLM-extracted predicates for at least some True/False-labeled examples.\",\n    \"Added requirement to benchmark against LINC and Logic-LM (not just SymBa) since both systems implement Unknown-propagation on proof failure and are the appropriate baselines for OWA accuracy comparisons.\",\n    \"Specified that the Phase 0 gate must produce precision/recall against gold SARA Prolog annotations on real cases (SgfdDttt/sara), not synthetic examples — the iter-1 Phase 0 on 5 synthetic cases was scientifically invalid.\",\n    \"Added requirement for at least one micro-evaluation task that forces L2 LKIF/ConceptNet firing, producing a non-Unknown answer, before L2 coverage can be evaluated.\",\n    \"Flagged SARA 100%, ContractNLI 40%, CLUTRR 0% as entirely uninformative (synthetic data / label artifacts) — these are removed from the confirmed evidence base.\",\n    \"The core architectural hypothesis (tier ordering beats flat LLM) is preserved but its empirical status is correctly set to 'unverified' pending LLM L0 extraction implementation.\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_dvruFBLiCgfS\",\n      \"to_id\": \"art_cy9EiwTnZMHv\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.\"\n    }\n  ]\n}\n", "structuredPatch": [], "originalFile": null, "userModified": false}
```

### [6] ASSISTANT · 2026-06-15 21:25:24 UTC

```
Output written. The revised hypothesis demotes the ProofWriter OWA result from architectural evidence to a trivial constant-Unknown artifact, elevates LLM-based L0 extraction as the mandatory prerequisite gate, and adds the constant-Unknown and LINC/Logic-LM baselines as required comparisons for the next iteration.
```

### [7] SYSTEM-USER prompt · 2026-06-15 21:25:26 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 2 problems — fix ALL of them at once:
  - at `artifact_relations.0.relation_rationale`: 'Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.' is too long (at most 120 characters, got 133)
  - at `relation_rationale`: 'Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.' is too long (at most 120 characters, got 141)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```

### [8] TOOL CALL — Edit · 2026-06-15 21:25:32 UTC

```
File: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:   "relation_rationale": "Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.",
NEW:   "relation_rationale": "Same architecture; primary claim reframed: constant-Unknown failure exposed, LLM L0 extraction now mandatory gate.",
```

### [9] TOOL RESULT — Edit · 2026-06-15 21:25:32 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "  \"relation_rationale\": \"Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.\",", "newString": "  \"relation_rationale\": \"Same architecture; primary claim reframed: constant-Unknown failure exposed, LLM L0 extraction now mandatory gate.\",", "originalFile": "{\n  \"title\": \"Provenance-Stratified Neuro-Symbolic Reasoning: LLM-Grounded L0 Extraction as the Prerequisite Gate for Tier-Architecture Evaluation\",\n  \"hypothesis\": \"A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed: LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics will demonstrate measurable benefit over both (a) the SymBa flat-LLM baseline AND (b) a constant-Unknown trivial baseline, IF AND ONLY IF the L0 LLM extraction tier fires successfully (precision ≥ 0.75 on gold-annotated SARA cases) and the L1 SLD resolver achieves non-trivial chaining on LLM-extracted predicates. The current iteration's ProofWriter OWA result (45.0% vs. SymBa 27.5%, McNemar p=0.0046) is NOT evidence for the tier architecture: it is identical in value to the Unknown base rate (~90/200 examples), meaning the system operates as a constant-Unknown predictor that cannot be distinguished from a zero-cost trivial baseline. The mechanistic cause is that the regex-based L0 extractor failed to produce predicates matchable by the L1 SLD resolver, causing the meta-interpreter to return Unknown for all 200 examples — which happens to equal the 45.0% Unknown base rate. This result is therefore consistent with the null hypothesis that no tier machinery is required. To establish genuine architectural benefit, the next iteration must: (1) run real LLM-based L0 extraction on ProofWriter OWA or SARA examples and verify that the L1 SLD resolver chains successfully from LLM-extracted predicates to answer True/False queries — demonstrating that the pipeline resolves something other than Unknown; (2) implement and report a constant-Unknown baseline alongside SymBa and LINC/Logic-LM to expose whether any improvement over it exists; (3) evaluate on real SARA (SgfdDttt/sara, 376 cases with gold Prolog KB) and real ContractNLI (kiddothe2b/contract-nli, 607 NDAs) to provide multi-benchmark evidence; and (4) design at least one micro-evaluation task where L2 LKIF or ConceptNet bridging is required and the system's answer differs from both True and Unknown. Until these experiments produce results, the hypothesis that the tier architecture outperforms constant-Unknown remains empirically unverified. The secondary hallucination-reduction and L2-ontology claims remain unverified pending L3 abduction firing on withheld-L0 examples.\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Demoted the ProofWriter OWA +17.5% result from 'empirical support' to 'consistent with trivial constant-Unknown baseline' — the system returned Unknown for all 200 examples, matching the dataset's Unknown base rate exactly. This is not architectural evidence.\",\n    \"Added explicit requirement to implement and report a constant-Unknown baseline in every future evaluation table, so readers can verify whether the stratified pipeline beats the trivial predictor.\",\n    \"Elevated LLM-based L0 extraction (not regex) to the mandatory prerequisite gate: no architectural claim is testable until L1 SLD chaining succeeds on LLM-extracted predicates for at least some True/False-labeled examples.\",\n    \"Added requirement to benchmark against LINC and Logic-LM (not just SymBa) since both systems implement Unknown-propagation on proof failure and are the appropriate baselines for OWA accuracy comparisons.\",\n    \"Specified that the Phase 0 gate must produce precision/recall against gold SARA Prolog annotations on real cases (SgfdDttt/sara), not synthetic examples — the iter-1 Phase 0 on 5 synthetic cases was scientifically invalid.\",\n    \"Added requirement for at least one micro-evaluation task that forces L2 LKIF/ConceptNet firing, producing a non-Unknown answer, before L2 coverage can be evaluated.\",\n    \"Flagged SARA 100%, ContractNLI 40%, CLUTRR 0% as entirely uninformative (synthetic data / label artifacts) — these are removed from the confirmed evidence base.\",\n    \"The core architectural hypothesis (tier ordering beats flat LLM) is preserved but its empirical status is correctly set to 'unverified' pending LLM L0 extraction implementation.\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_dvruFBLiCgfS\",\n      \"to_id\": \"art_cy9EiwTnZMHv\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 2, "oldLines": 7, "newStart": 2, "newLines": 7, "lines": ["   \"title\": \"Provenance-Stratified Neuro-Symbolic Reasoning: LLM-Grounded L0 Extraction as the Prerequisite Gate for Tier-Architecture Evaluation\",", "   \"hypothesis\": \"A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed: LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics will demonstrate measurable benefit over both (a) the SymBa flat-LLM baseline AND (b) a constant-Unknown trivial baseline, IF AND ONLY IF the L0 LLM extraction tier fires successfully (precision ≥ 0.75 on gold-annotated SARA cases) and the L1 SLD resolver achieves non-trivial chaining on LLM-extracted predicates. The current iteration's ProofWriter OWA result (45.0% vs. SymBa 27.5%, McNemar p=0.0046) is NOT evidence for the tier architecture: it is identical in value to the Unknown base rate (~90/200 examples), meaning the system operates as a constant-Unknown predictor that cannot be distinguished from a zero-cost trivial baseline. The mechanistic cause is that the regex-based L0 extractor failed to produce predicates matchable by the L1 SLD resolver, causing the meta-interpreter to return Unknown for all 200 examples — which happens to equal the 45.0% Unknown base rate. This result is therefore consistent with the null hypothesis that no tier machinery is required. To establish genuine architectural benefit, the next iteration must: (1) run real LLM-based L0 extraction on ProofWriter OWA or SARA examples and verify that the L1 SLD resolver chains successfully from LLM-extracted predicates to answer True/False queries — demonstrating that the pipeline resolves something other than Unknown; (2) implement and report a constant-Unknown baseline alongside SymBa and LINC/Logic-LM to expose whether any improvement over it exists; (3) evaluate on real SARA (SgfdDttt/sara, 376 cases with gold Prolog KB) and real ContractNLI (kiddothe2b/contract-nli, 607 NDAs) to provide multi-benchmark evidence; and (4) design at least one micro-evaluation task where L2 LKIF or ConceptNet bridging is required and the system's answer differs from both True and Unknown. Until these experiments produce results, the hypothesis that the tier architecture outperforms constant-Unknown remains empirically unverified. The secondary hallucination-reduction and L2-ontology claims remain unverified pending L3 abduction firing on withheld-L0 examples.\",", "   \"relation_type\": \"evolution\",", "-  \"relation_rationale\": \"Same architecture; primary claim reframed around the constant-Unknown failure; LLM L0 extraction elevated as the mandatory prerequisite gate.\",", "+  \"relation_rationale\": \"Same architecture; primary claim reframed: constant-Unknown failure exposed, LLM L0 extraction now mandatory gate.\",", "   \"confidence_delta\": \"decreased\",", "   \"key_changes\": [", "     \"Demoted the ProofWriter OWA +17.5% result from 'empirical support' to 'consistent with trivial constant-Unknown baseline' — the system returned Unknown for all 200 examples, matching the dataset's Unknown base rate exactly. This is not architectural evidence.\","]}], "userModified": false, "replaceAll": false}
```

### [10] TOOL CALL — Edit · 2026-06-15 21:25:37 UTC

```
File: /ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json
OLD:       "relation_rationale": "Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis."
NEW:       "relation_rationale": "Evaluation uses experiment pipeline outputs and system implementations for statistical analysis."
```

### [11] TOOL RESULT — Edit · 2026-06-15 21:25:37 UTC

```
{"filePath": "/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_2/upd_hypo/upd_hypo/.terminal_claude_agent_struct_out.json", "oldString": "      \"relation_rationale\": \"Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.\"", "newString": "      \"relation_rationale\": \"Evaluation uses experiment pipeline outputs and system implementations for statistical analysis.\"", "originalFile": "{\n  \"title\": \"Provenance-Stratified Neuro-Symbolic Reasoning: LLM-Grounded L0 Extraction as the Prerequisite Gate for Tier-Architecture Evaluation\",\n  \"hypothesis\": \"A neuro-symbolic text-to-reasoning pipeline that (i) populates a Prolog knowledge base from LLM-extracted document-explicit facts (L0) rather than starting from an empty database, (ii) annotates each predicate with an explicit epistemic provenance tier — L0 (document-stated, LLM extraction), L1 (bounded deductive closure on L0 via depth-limited SLD, ≤5 steps), L2 (domain-ontology-entailed: LKIF Core OWL for legal, ConceptNet for narrative), L3 (LLM-abduced, confidence via K=5 self-consistency sampling) — and (iii) enforces strict tier-ordered SLD resolution with three-valued Open-World semantics will demonstrate measurable benefit over both (a) the SymBa flat-LLM baseline AND (b) a constant-Unknown trivial baseline, IF AND ONLY IF the L0 LLM extraction tier fires successfully (precision ≥ 0.75 on gold-annotated SARA cases) and the L1 SLD resolver achieves non-trivial chaining on LLM-extracted predicates. The current iteration's ProofWriter OWA result (45.0% vs. SymBa 27.5%, McNemar p=0.0046) is NOT evidence for the tier architecture: it is identical in value to the Unknown base rate (~90/200 examples), meaning the system operates as a constant-Unknown predictor that cannot be distinguished from a zero-cost trivial baseline. The mechanistic cause is that the regex-based L0 extractor failed to produce predicates matchable by the L1 SLD resolver, causing the meta-interpreter to return Unknown for all 200 examples — which happens to equal the 45.0% Unknown base rate. This result is therefore consistent with the null hypothesis that no tier machinery is required. To establish genuine architectural benefit, the next iteration must: (1) run real LLM-based L0 extraction on ProofWriter OWA or SARA examples and verify that the L1 SLD resolver chains successfully from LLM-extracted predicates to answer True/False queries — demonstrating that the pipeline resolves something other than Unknown; (2) implement and report a constant-Unknown baseline alongside SymBa and LINC/Logic-LM to expose whether any improvement over it exists; (3) evaluate on real SARA (SgfdDttt/sara, 376 cases with gold Prolog KB) and real ContractNLI (kiddothe2b/contract-nli, 607 NDAs) to provide multi-benchmark evidence; and (4) design at least one micro-evaluation task where L2 LKIF or ConceptNet bridging is required and the system's answer differs from both True and Unknown. Until these experiments produce results, the hypothesis that the tier architecture outperforms constant-Unknown remains empirically unverified. The secondary hallucination-reduction and L2-ontology claims remain unverified pending L3 abduction firing on withheld-L0 examples.\",\n  \"relation_type\": \"evolution\",\n  \"relation_rationale\": \"Same architecture; primary claim reframed: constant-Unknown failure exposed, LLM L0 extraction now mandatory gate.\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Demoted the ProofWriter OWA +17.5% result from 'empirical support' to 'consistent with trivial constant-Unknown baseline' — the system returned Unknown for all 200 examples, matching the dataset's Unknown base rate exactly. This is not architectural evidence.\",\n    \"Added explicit requirement to implement and report a constant-Unknown baseline in every future evaluation table, so readers can verify whether the stratified pipeline beats the trivial predictor.\",\n    \"Elevated LLM-based L0 extraction (not regex) to the mandatory prerequisite gate: no architectural claim is testable until L1 SLD chaining succeeds on LLM-extracted predicates for at least some True/False-labeled examples.\",\n    \"Added requirement to benchmark against LINC and Logic-LM (not just SymBa) since both systems implement Unknown-propagation on proof failure and are the appropriate baselines for OWA accuracy comparisons.\",\n    \"Specified that the Phase 0 gate must produce precision/recall against gold SARA Prolog annotations on real cases (SgfdDttt/sara), not synthetic examples — the iter-1 Phase 0 on 5 synthetic cases was scientifically invalid.\",\n    \"Added requirement for at least one micro-evaluation task that forces L2 LKIF/ConceptNet firing, producing a non-Unknown answer, before L2 coverage can be evaluated.\",\n    \"Flagged SARA 100%, ContractNLI 40%, CLUTRR 0% as entirely uninformative (synthetic data / label artifacts) — these are removed from the confirmed evidence base.\",\n    \"The core architectural hypothesis (tier ordering beats flat LLM) is preserved but its empirical status is correctly set to 'unverified' pending LLM L0 extraction implementation.\"\n  ],\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_dvruFBLiCgfS\",\n      \"to_id\": \"art_cy9EiwTnZMHv\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.\"\n    }\n  ]\n}\n", "structuredPatch": [{"oldStart": 19, "oldLines": 7, "newStart": 19, "newLines": 7, "lines": ["       \"from_id\": \"art_dvruFBLiCgfS\",", "       \"to_id\": \"art_cy9EiwTnZMHv\",", "       \"relation_type\": \"uses\",", "-      \"relation_rationale\": \"Evaluation artifact uses experiment pipeline outputs (method_out.json) and system implementations as inputs for statistical analysis.\"", "+      \"relation_rationale\": \"Evaluation uses experiment pipeline outputs and system implementations for statistical analysis.\"", "     }", "   ]", " }"]}], "userModified": false, "replaceAll": false}
```

### [12] ASSISTANT · 2026-06-15 21:25:38 UTC

```
Fixed both `relation_rationale` fields to be under 120 characters.
```
