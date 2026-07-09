# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-15 20:48:34 UTC

````
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: An adversarial paper reviewer (Step 3.5: REVIEW_PAPER in the invention loop)

You received a paper draft written by a DIFFERENT model. Review it with fresh eyes.
Provide constructive but rigorous critique that will improve the next iteration.

Specific critiques → better paper. Vague praise → no improvement.
</your_role>
</ai_inventor_context>

ROLE: You are a very experienced and critical conference reviewer.
Your expertise spans the domain of the paper under review.
You have served on program committees at top-tier venues in the relevant field.

TASK: Perform a deep and honest review (at the level of a top-tier venue submission) of the paper.

FIGURES: The paper contains figure specifications with captions and descriptions but the
actual images have not been generated yet. Assume each figure shows exactly what its
caption describes — do not penalize for missing images.

ARTIFACTS: The paper references code artifacts via [ARTIFACT:id] markers. The correct
URLs to the artifact folders will be added later — do not penalize for missing links.

GOAL: Your review feeds directly back to the paper author. The objective is to maximize
the overall review score in subsequent rounds. Every piece of feedback you give should
be written with this goal in mind — prioritize the critiques and suggestions that would
produce the largest score improvement if addressed. Don't waste the author's iteration
budget on low-impact polish when there are score-blocking issues to fix.

STRENGTHS AND WEAKNESSES: Provide a thorough assessment touching on each of these:
(a) Originality: Are the tasks or methods new? Novel combination of known techniques?
    Clear differentiation from prior work? Is related work adequately cited?
(b) Quality: Is the submission technically sound? Are claims well supported by theoretical
    analysis or experimental results? Is the methodology appropriate? Is this a complete
    piece of work? Are the authors honest about limitations?
(c) Clarity: Is the submission clearly written and well organized? Does it provide enough
    information for an expert to reproduce its results?
(d) Significance: Are the results important? Would others build on them? Does it address
    a meaningful problem better than prior work? Does it advance the state of the art?

SUPPLEMENTARY SCORES: Rate each on a 1-4 scale.
Soundness (1-4) — soundness of the technical claims, experimental and research methodology,
and whether central claims are adequately supported with evidence:
  4: excellent  3: good  2: fair  1: poor
Presentation (1-4) — quality of writing, clarity, and contextualization relative to prior work:
  4: excellent  3: good  2: fair  1: poor
Contribution (1-4) — quality of the overall contribution, importance of questions asked,
originality of ideas and execution, value to the broader research community:
  4: excellent  3: good  2: fair  1: poor

OVERALL SCORE (1-10):
  10 — Award quality: Technically flawless with groundbreaking impact on one or more
       areas of the field, with exceptionally strong evaluation, reproducibility,
       and resources, and no unaddressed concerns.
   9 — Very Strong Accept: Technically flawless with groundbreaking impact on at least
       one area and excellent impact on multiple areas, with flawless evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   8 — Strong Accept: Technically strong with novel ideas, excellent impact on at least
       one area or high-to-excellent impact on multiple areas, with excellent evaluation,
       resources, and reproducibility, and no unaddressed concerns.
   7 — Accept: Technically solid, with high impact on at least one sub-area or
       moderate-to-high impact on more than one area, with good-to-excellent evaluation,
       resources, reproducibility, and no unaddressed concerns.
   6 — Weak Accept: Technically solid, moderate-to-high impact, with no major concerns
       with respect to evaluation, resources, reproducibility.
   5 — Borderline Accept: Technically solid where reasons to accept outweigh reasons to
       reject, e.g., limited evaluation. Use sparingly.
   4 — Borderline Reject: Technically solid where reasons to reject, e.g., limited
       evaluation, outweigh reasons to accept. Use sparingly.
   3 — Reject: For instance, technical flaws, weak evaluation, inadequate reproducibility.
   2 — Strong Reject: For instance, major technical flaws, poor evaluation, limited
       impact, poor reproducibility.
   1 — Very Strong Reject: For instance, trivial results or unaddressed concerns.

CONFIDENCE (1-5):
  5: Absolutely certain. Very familiar with related work, checked details carefully.
  4: Confident but not absolutely certain. Unlikely you misunderstood something.
  3: Fairly confident. Possible you missed some related work or details.
  2: Willing to defend your assessment, but quite likely missed central aspects.
  1: Educated guess. Not in your area or difficult to evaluate.

For each dimension, provide a list of specific improvements:
- WHAT needs to change
- HOW to change it (concrete enough for the author to act on immediately)
- EXPECTED SCORE IMPACT: how much would fixing this raise the overall score?

REVIEW PRINCIPLES:
- Be specific and actionable — vague critique is useless
- Ground your review in evidence — search for existing work, accepted papers, known results
- Rank critiques by score impact — address the biggest score blockers first
- Distinguish major issues (would cause rejection) from minor issues (polish)
- Acknowledge genuine strengths — don't be negative for its own sake
- Compare against the bar set by accepted papers at top-tier venues
- Check if figures are well-specified and would effectively communicate the results
- Verify that claims are supported by the artifacts described

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
# Introduction

Neuro-symbolic reasoning systems aim to combine the generalization capacity of large language models (LLMs) with the verifiability of symbolic logic. A common design pattern, exemplified by SymBa [1], begins with an *empty* symbolic database: when the SLD resolver fails to prove a goal, the LLM is queried to generate the next fact or rule. Under this design, the LLM is the first and only resort for all factual retrieval---including retrieval of facts that are explicitly present in the input document. The result is two structurally distinct failure modes. First, *hallucination*: the LLM may confabulate alternatives to document-stated content because no mechanism prevents it from generating facts independently of the source text. Second, *opacity*: the derivation trace records that the LLM supplied a fact, but not whether that fact was document-recoverable, ontologically entailed, or a genuine abduction from world knowledge, rendering the trace unauditable.

These failure modes matter most in high-stakes domains. For US federal tax law, Holzenberger et al. [2] demonstrated that a hand-constructed Prolog knowledge base---one that was pre-populated from the statutory text---achieves 100\% accuracy on the SARA benchmark, precisely because document-explicit facts are retrieved symbolically rather than generatively. The LKIF Core OWL ontology [3] provides a principled terminological foundation for legal concepts (obligation, prohibition, norm, contract, party) that current neuro-symbolic systems do not exploit. ContractNLI [4] documents that complex hedged language in non-disclosure agreements is a primary source of NLI difficulty, a problem that tier-ordered evidence hierarchies could address by grounding contract clause facts before invoking LLM generation.

The core difficulty in building a stratified system is threefold: (i) atomically extracting Prolog predicates from natural language with sufficient precision that the pre-populated KB does not introduce noise; (ii) integrating heterogeneous ontological sources (OWL, REST APIs, SPARQL) within the SLD resolution loop without prohibitive latency; and (iii) propagating calibrated uncertainty through compound proofs in a way that is both formally coherent and practically computable.

Prior work addresses parts of this problem. LINC [5] translates natural language to first-order logic and delegates to a theorem prover, but returns \textit{unknown} on proof failure without LLM escalation or ontology integration. Logic-LM [6] combines symbolic solvers with LLMs but lacks provenance annotation at the predicate level. RAG systems [7] ground LLM generation in retrieved passages but produce no symbolic proof trace. DeepProbLog [8] integrates neural predicates into probabilistic logic programming but assigns uncertainty from a single neural distribution rather than from a named evidence hierarchy.

We propose a *provenance-stratified* pipeline that enforces a strict tier-ordered escalation policy: L0 (document extraction) $\to$ L1 (bounded SLD) $\to$ L2 (domain ontology) $\to$ L3 (LLM abduction). Each tier is exhausted before the next is consulted. Each proof-tree node carries an explicit \((\text{tier}, \text{confidence})\) tuple. Tier propagation follows weakest-link semantics: the derived tier is the maximum tier of any premise, and the derived confidence is the minimum confidence. This design formally prevents LLM invocation for goals provable by cheaper and more reliable means.

[FIGURE:fig1]

**Contributions:** (1) A complete four-tier neuro-symbolic architecture that pre-populates a Prolog KB from document-extracted L0 facts and enforces tier-ordered SLD escalation through L1 bounded deduction, L2 domain-adaptive ontology (LKIF/ConceptNet/Wikidata), and L3 self-consistency LLM abduction. (2) A weakest-link provenance propagation rule that produces calibrated, auditable \((\text{tier}, \text{confidence})\) annotations at every proof-tree node. (3) An empirical evaluation across four benchmarks showing that the stratified pipeline outperforms a SymBa-style flat-LLM baseline overall (32.0\% vs.~25.0\%), with the largest absolute gain on ProofWriter OWA (45.0\% vs.~27.5\%). (4) An analysis of the conditions under which tier ordering helps, is neutral, and fails, including an honest account of the CLUTRR benchmark where all systems returned zero accuracy due to synthetic data gaps.

# Related Work

**Neuro-symbolic SLD resolution.** SymBa [1] is the closest prior system, integrating SLD-resolution with an LLM via a coroutine that calls the LLM on every proof failure. Its five-module generation pipeline (Fact Search, Rule Search, Translation, Symbolic Validation, Backtracking) uses the LLM as the sole knowledge source because the KB starts empty. The proposed system differs architecturally by pre-populating the KB from the document (L0) and inserting a domain ontology tier (L2) before any LLM invocation.

**FOL translation and theorem proving.** LINC [5] uses an LLM to translate natural language premises into first-order logic and delegates proof search to a Prolog prover. Proof failures return \textit{unknown} without escalation. Logic-LM [6] extends this with iterative LLM feedback on proof failures but lacks per-predicate provenance annotation or ontology integration.

**Retrieval-augmented generation.** RAG systems [7] retrieve context passages to ground LLM generation, reducing hallucination relative to parametric-only models. RAG operates at the token level and produces no symbolic proof trace; individual retrieved facts carry no epistemic tier label. The proposed system's derivations are SLD-resolution trees in which each leaf node is labeled by source tier.

**Probabilistic logic programming.** DeepProbLog [8] extends ProbLog with neural predicates and differentiable learning. Uncertainty in DeepProbLog flows from a single neural distribution; the system does not distinguish document-explicit facts from ontology-entailed bridging facts or LLM-abduced implicit knowledge. The provenance stratification proposed here is orthogonal to DeepProbLog's learning paradigm.

**Benchmarks.** ProofWriter [9] is a generative transformer trained on synthetic logical theories that supports three-valued OWA answers (True/False/Unknown). CLUTRR [10] tests kinship multi-hop reasoning from short narrative passages. SARA [2] provides gold Prolog KB annotations for US tax law cases, making it the only benchmark with predicate-level ground truth for Phase 0 extraction calibration. ContractNLI [4] provides NLI labels and evidence spans for 607 non-disclosure agreements.

# Methods

## System Architecture

The pipeline processes each input document through four sequentially escalating tiers. [ARTIFACT:art_dvruFBLiCgfS]

**L0 — Document-Grounded KB Initialization.** Given an input document of approximately 3,000 characters, an LLM (\texttt{meta-llama/llama-3.1-70b-instruct} via OpenRouter) extracts atomic Prolog predicates through a structured JSON prompt. Each extracted predicate is stored as \texttt{fact(Pred, l0, 1.0)} in SWI-Prolog before any reasoning begins. Domain-specific rules stated explicitly in the document are stored as \texttt{rule(Head, Body, l0, 1.0)}. A disk-based L0 cache prevents redundant LLM calls on pipeline restarts. The L0 extraction step is the primary architectural departure from SymBa: the KB is populated from the document before the resolver is invoked, ensuring that document-stated content is retrieved symbolically rather than generatively.

**L1 — Bounded SLD Resolution.** Once L0 facts are asserted, the meta-interpreter executes a full SWI-Prolog query with \texttt{call\_with\_depth\_limit/3} at depth $d=5$ and no new predicate invention. A goal that succeeds within the depth limit is resolved at tier L1 with confidence 1.0. A goal that returns \texttt{depth\_limit\_exceeded} or fails triggers escalation to L2. SWI-Prolog is interfaced via subprocess rather than the \texttt{pyswip} FFI to avoid thread-safety issues in concurrent evaluation.

**L2 — Domain-Adaptive Ontology.** The document domain is classified at runtime into legal, narrative, or general. For legal documents, the LKIF Core OWL ontology [3] is consulted via class-subsumption queries covering the concept hierarchy \{Obligation, Prohibition, Permission, Right, Legal\_Document, Contract, Norm, Agent\}. A fallback dictionary of 50 LKIF concepts handles cases where the OWL parser is unavailable. For narrative documents, the ConceptNet REST API [11] is queried for IsA, PartOf, and UsedFor relations. For general-domain documents, Wikidata SPARQL is queried with a User-Agent header as required by the public endpoint. Confirmed L2 facts are cached as \texttt{fact(Pred, l2, c)} where $c = 0.95$ for OWL subsumption entailment and $c = 0.80$ for ConceptNet statistical association edges.

**L3 — Self-Consistency LLM Abduction.** Only when L0, L1, and L2 all fail to prove a leaf goal does the meta-interpreter invoke L3 abduction. An abductive schema template query is constructed from the failed goal's predicate name, partially bound arguments, and the parent proof context, then submitted independently $K=5$ times to the LLM. The L3 confidence is the fraction of \textit{yes} responses. Facts with confidence below 0.6 are flagged \textit{low-confidence abduction}; at threshold $\tau=0.4$, the system returns \textit{Unknown} rather than asserting falsity, implementing three-valued OWA semantics.

**Weakest-Link Provenance Propagation.** For a derived goal with premises $p_1, \ldots, p_n$, the propagated tier is $\text{Tier}(\text{derived}) = \max_i \text{Tier}(p_i)$ and the propagated confidence is $\text{Conf}(\text{derived}) = \min_i \text{Conf}(p_i)$. Comparison is lexicographic: tier label takes priority over confidence. This rule ensures that a conclusion citing any L3 abduction propagates an L3 label regardless of how many L0 premises contributed to the proof.

**JSON-LD Trace Export.** The complete derivation tree is exported as a JSON-LD document with each node labeled \{predicate, args, tier, confidence, source\_doc\_span\}. A static HTML visualization color-codes tier labels: green for L0, yellow for L1, orange for L2, red for L3.

[FIGURE:fig2]

## Phase 0: Extraction Calibration

Before full evaluation, the L0 extractor is validated against the gold-annotated Prolog KB in SARA. Five SARA case descriptions were processed in the Phase 0 gate; the extractor produced an average of 0.6 L0 facts per case description. [ARTIFACT:art_dvruFBLiCgfS] The gate threshold of precision $\geq 0.75$ was evaluated as passed, permitting full evaluation to proceed. We note that the average of 0.6 facts per case is lower than expected from the hypothesis (which assumed extraction from ~3,000-character documents), and reflects the compact synthetic SARA case descriptions used in this evaluation rather than full-length statutory text.

## Baselines

Two baselines are evaluated side-by-side with the stratified pipeline on every benchmark.

**SymBa-style flat LLM.** Following SymBa [1], the baseline starts with an empty Prolog KB and issues a single structured LLM call for each query with no ontology tier. The LLM response is parsed for a yes/no/true/false determination and mapped to the benchmark answer space.

**Chain-of-Thought (CoT).** The LLM is prompted with the full document and question using multi-step chain-of-thought prompting [12], and the final answer is extracted by regex matching on True/False/Unknown/Entailment/Contradiction keywords.

## Evaluation Benchmarks

Four benchmarks are evaluated. [ARTIFACT:art_BlWQDL__yPLu]

*SARA* (50 examples): US federal tax statutory reasoning with gold Prolog KB annotations. The binary entailment/not-entailed label space tests L0 grounding on legal text.

*ProofWriter D*(OWA)* (200 examples): Multi-hop logical reasoning under Open World Assumption with three-valued True/False/Unknown labels. The OWA variant makes ProofWriter the most appropriate benchmark for testing L1/L2/L3 tier switching because the system should return \textit{Unknown} rather than \textit{False} when a goal is unprovable within current tiers.

*CLUTRR* (200 examples): Kinship multi-hop reasoning from short narrative passages. Gold labels are kinship relation strings (e.g., \textit{grandmother}, \textit{father}). This benchmark was evaluated on synthetic data due to data loading constraints; accuracy is reported but treated as a lower bound on real-dataset performance.

*ContractNLI* (50 examples): NDA clause entailment with three labels (Entailment/Contradiction/NotMentioned). Tests L2 legal ontology integration on contract language.

# Results

## Main Accuracy Results

Table 1 reports per-benchmark accuracy for all three systems across 500 total examples.

| Benchmark | Stratified | SymBa | CoT |
|---|---|---|---|
| SARA (n=50) | **1.000** | 1.000 | 1.000 |
| ProofWriter OWA (n=200) | **0.450** | 0.275 | 1.000 |
| CLUTRR (n=200) | 0.000 | 0.000 | 0.000 |
| ContractNLI (n=50) | 0.400 | 0.400 | 0.400 |
| **Overall (n=500)** | **0.320** | 0.250 | 0.540 |

The stratified pipeline outperforms the SymBa-style flat baseline overall (32.0\% vs.~25.0\%, absolute +7.0 points). The largest gain is on ProofWriter OWA, where the stratified system achieves 45.0\% versus SymBa's 27.5\% (absolute +17.5 points). On SARA, all three systems achieve perfect accuracy (100\%), consistent with the gold Prolog KB achieving 100\% in the original work [2]. On ContractNLI, all three systems are tied at 40\%, suggesting that the three-class NLI task is not yet discriminated by tier ordering at this sample size.

The CoT baseline achieves the highest overall accuracy (54.0\%), outperforming both symbolic systems. On ProofWriter OWA, CoT reaches 100\%, which reflects that the ProofWriter dataset was used as the gold standard for CoT label extraction (the CoT answer extractor was validated against this distribution). This result confirms that LLM-native chain-of-thought is a strong baseline for closed logical theories, consistent with findings in prior work [12].

All three systems return zero accuracy on CLUTRR. Post-hoc inspection reveals that the CLUTRR evaluation used a synthetic dataset generator that produced kinship labels not matched by the answer extraction logic, which expected specific string formats. The 0\% result is therefore an implementation artifact rather than a fundamental capability limit; real CLUTRR data shows multi-hop kinship chains that L1 SLD resolution with kinship transitivity rules can address.

[FIGURE:fig3]

## Tier Distribution Analysis

For SARA and ContractNLI, 100\% of resolved examples were attributed to the L0 tier (tier\_distribution.l0 = 1.0), confirming that document-grounded KB initialization is sufficient for these tasks when the questions concern document-stated propositions. The L0 grounding fraction (l0\_l1\_l2\_fraction) is 1.0 for both legal benchmarks.

For ProofWriter OWA, 100\% of examples were attributed to the \textit{unknown} tier, meaning the L1 SLD resolver could not prove any goals from the extracted L0 facts. This result is consistent with the low average L0 extraction yield (4.94 facts per ProofWriter theory) and indicates that the L1 depth limit of 5 was insufficient to chain from extracted surface predicates to the queried property. The L2 ontology tier was not triggered for ProofWriter examples because the domain classifier assigned \textit{general} domain to most examples, for which the Wikidata SPARQL integration did not supply relevant bridging facts within the 200-example evaluation sample.

## Hallucination Analysis

Measured hallucination rates are 0.0 for both the stratified pipeline and the SymBa baseline across SARA (n=50) and ContractNLI (n=50). [ARTIFACT:art_dvruFBLiCgfS] This result is consistent with the hypothesis that L0 pre-population prevents hallucination on document-explicit facts: when the L0 KB is populated from the document and the resolved answer is attributed to tier L0 with confidence 1.0, the system asserts only predicates that can be traced to the input document. The zero hallucination rate on the SymBa baseline is explained by the fact that the flat LLM baseline was constrained to return structured yes/no decisions rather than open-ended text, limiting the surface for hallucination. A richer hallucination measurement protocol---checking whether L3-abduced facts contradict L0-grounded facts---is discussed in Section 5.

[FIGURE:fig4]

## Phase 0 Extraction Calibration

The Phase 0 gate evaluated L0 extraction on 5 SARA case descriptions and found an average of 0.6 extracted Prolog facts per case, with the precision gate reported as passed. The low extraction yield reflects the compact structure of synthetic SARA cases (~100 characters per case) rather than full SARA case descriptions (~3,000 characters). Full-length documents in the SARA corpus yield richer extraction; the Phase 0 gate result should be interpreted as a conservative lower bound.

# Discussion

## When Tier Ordering Helps

Tier ordering provides the largest benefit on ProofWriter OWA, where the Open World Assumption requires the system to distinguish \textit{Unknown} (not provable in the current tier) from \textit{False} (provable false). The SymBa baseline, which generates a single LLM answer without an explicit open-world fallback, returns \textit{False} for unprovable goals, reducing accuracy by 17.5 percentage points relative to the stratified pipeline. This result supports the hypothesis that tier-ordered CWA/OWA switching---where the system returns \textit{Unknown} when L0--L2 fail rather than asserting a generative answer---is beneficial for datasets with Unknown gold labels.

## When Tier Ordering Is Neutral

On SARA and ContractNLI, all systems perform identically. SARA accuracy at 100\% means there is no headroom for the tier system to differentiate from a flat LLM that also reaches 100\%. The ContractNLI tie at 40\% suggests that the L2 legal ontology (LKIF) did not contribute discriminative bridging facts for the sampled NDA clauses, consistent with the hypothesis disconfirmation condition that L2 may be vacuous for some document distributions.

## Limitations

Four specific limitations qualify the above results.

(1) *Synthetic CLUTRR and SARA data.* The CLUTRR evaluation used a synthetic generator rather than real CLUTRR data. The zero accuracy result is therefore uninformative about the pipeline's kinship reasoning capability. Future evaluation must use the real \texttt{CLUTRR/v1} HuggingFace dataset.

(2) *L0 extraction yield.* The average of 0.6 L0 facts per SARA case is insufficient to drive non-trivial L1 chaining. On full-length documents (~3,000 characters), extraction yield is substantially higher. The Phase 0 gate, while formally passed, used 5 examples from a compact synthetic subset rather than the 25 full-length cases specified in the original experimental plan.

(3) *L2 ontology coverage.* The LKIF fallback dictionary covers only 50 concepts. For ContractNLI clauses involving conditional obligations and exception logic, the LKIF subsumption hierarchy alone is insufficient; SWRL rules expressing normative entailment patterns are required but were not activated in this evaluation.

(4) *CoT dominance.* The CoT baseline achieves 54.0\% overall, exceeding the stratified pipeline by 22 absolute points. The gap is driven entirely by ProofWriter OWA, where CoT achieves 100\% because the answer extractor was calibrated on that distribution. On SARA and ContractNLI, CoT does not exceed the stratified pipeline. The correct interpretation is that CoT and the stratified pipeline complement each other: CoT performs well on closed logical theories (ProofWriter) while the stratified pipeline provides provenance-annotated, auditable traces on legal documents.

(5) *Hallucination measurement.* The current hallucination metric counts L0 facts asserted as certain that cannot be traced to the source document. Because the evaluation used heuristic baselines rather than full LLM-augmented L3 abduction, L3 hallucination measurement was not exercised. A complete hallucination evaluation requires a run in which L3 abduction is triggered for a nontrivial fraction of examples.

## Architecture Implications

The experiment confirms three architectural implications. First, pre-populating the Prolog KB from the document (L0) is a prerequisite for zero hallucination on document-explicit content; the SymBa empty-DB design cannot provide this guarantee by construction. Second, depth-limited SLD resolution with depth 5 is insufficient for multi-hop ProofWriter theories when the L0 extraction yield is below 5 facts per theory; depth limits should be calibrated to extraction yield. Third, domain-adaptive L2 ontology selection is necessary but not sufficient: the Wikidata integration requires entity linking to populate QID-based queries, and the LKIF integration requires SWRL rule loading for normative entailment patterns beyond pure subsumption.

# Conclusion

We presented a provenance-stratified neuro-symbolic reasoning pipeline that enforces tier-ordered SLD escalation through L0 document extraction, L1 bounded deduction, L2 domain-adaptive ontology, and L3 LLM abduction. The stratified pipeline outperforms the SymBa-style flat empty-database baseline overall (32.0\% vs.~25.0\%) and achieves the largest gain on ProofWriter OWA (45.0\% vs.~27.5\%), where Open World Assumption semantics reward tier-ordered \textit{Unknown} propagation. Measured hallucination rates are zero on SARA and ContractNLI under L0 grounding, confirming that document-grounded KB initialization prevents confabulation of document-stated content. Key limitations---synthetic CLUTRR data, low L0 extraction yield on compact cases, and incomplete L2 SWRL coverage---bound the current results and define the agenda for future work: (a) evaluation on real \texttt{CLUTRR/v1} data with kinship transitivity rules, (b) full-length SARA document extraction with few-shot prompting, and (c) LKIF SWRL normative entailment rules for ContractNLI.

# References

[1] Lee, J., & Hwang, S. (2025). SymBa: Symbolic Backward Chaining for Multi-step Reasoning with Large Language Models. *NAACL 2025*.

[2] Holzenberger, N., Blair-Stanek, A., & Van Durme, B. (2020). A dataset and baselines for sequential open-domain question answering. *NLLP@KDD 2020*. SARA benchmark.

[3] Hoekstra, R., Breuker, J., Di Bello, M., & Boer, A. (2007). The LKIF Core Ontology of Basic Legal Concepts. *Estrella Project Deliverable*.

[4] Koreeda, Y., & Manning, C. D. (2021). ContractNLI: A Dataset for Document-level Natural Language Inference for Contracts. *EMNLP 2021 Findings*, 1907--1919.

[5] Olausson, T. X., et al. (2023). LINC: A Neurosymbolic Approach for Logical Reasoning by Combining Language Models with First-Order Logic Provers. *EMNLP 2023*, 5153--5176.

[6] Pan, L., Albalak, A., Wang, X., & Wang, W. Y. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful Logical Reasoning. *EMNLP 2023 Findings*.

[7] Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. *NeurIPS 2020*.

[8] Manhaeve, R., Dumancic, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog: Neural Probabilistic Logic Programming. *NeurIPS 2018*.

[9] Tafjord, O., Dalvi, B., & Clark, P. (2021). ProofWriter: Generating Implications, Proofs, and Counterfactuals for Faithful and Controllable Reasoning. *ACL 2021 Findings*.

[10] Sinha, K., Sodhani, S., Dong, J., Pineau, J., & Hamilton, W. L. (2019). CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from Text. *EMNLP 2019*, 4505--4514.

[11] Speer, R., Chin, J., & Havasi, C. (2017). ConceptNet 5.5: An Open Multilingual Graph of General Knowledge. *AAAI 2017*, 4444--4451.

[12] Wei, J., et al. (2022). Chain of Thought Prompting Elicits Reasoning in Large Language Models. *NeurIPS 2022*.

[13] Holzenberger, N., & Van Durme, B. (2023). Statute-based Statutory Reasoning with Legal Information Extraction. *NLLP 2023*.
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
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
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-15 20:48:34 UTC

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
