# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-15 21:49:58 UTC

````
<research_methodology>
Write like an experienced academic. Reviewers judge both the science and the writing.

- Claims must be proportional to evidence. Choose verbs carefully — "demonstrate," "observe," and "hypothesize" mean different things.
- Every result needs: what was measured, on what data, the numbers, and what they mean.
- Methodology must be specific enough to reproduce. Related work must be organized by theme, not a literature dump.
- State limitations honestly. Avoid both overclaiming and excessive hedging.
</research_methodology>

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
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Provenance-Stratified Neuro-Symbolic Reasoning: Tier-Ordered SLD Resolution with Open-World Unknown Propagation
abstract: >-
  Neuro-symbolic reasoning pipelines such as SymBa begin with an empty symbolic database and invoke a large language model
  (LLM) on every proof failure, conflating document-stated facts, ontology-entailed bridging knowledge, and LLM-abduced world
  knowledge into a single undifferentiated call. We propose a provenance-stratified architecture that enforces a strict four-tier
  escalation policy—L0 (document-grounded KB initialization), L1 (bounded SLD deductive closure), L2 (domain-adaptive ontology),
  L3 (self-consistency LLM abduction)—and propagates a calibrated (tier, confidence) tuple through every proof-tree node under
  weakest-link semantics. Each tier is exhausted before the next is consulted, reducing LLM invocation to a provable last
  resort. The key behavioral consequence of this design is that, when no tier can prove a goal, the system returns Unknown
  rather than defaulting to False as SymBa does. We evaluate this architecture on ProofWriter D*(OWA), a three-valued benchmark
  (True/False/Unknown) where the Unknown response is correct for unprovable goals. On 200 ProofWriter OWA examples drawn from
  the real HuggingFace dataset, the stratified pipeline achieves 45.0% accuracy (95% CI: [38.3%, 51.9%]) versus the SymBa-style
  baseline's 27.5% (CI: [21.8%, 34.1%])—an absolute gain of +17.5 points that is statistically significant by McNemar's test
  (p = 0.0046). We report honestly that secondary claims—LLM-based L0 extraction, L2 ontology bridging, and hallucination
  reduction—were not exercised in the current evaluation: L0 used heuristic extraction rather than LLM inference, the L2 tier
  was never triggered (0/500 examples), and L3 abduction was never invoked, making hallucination measurement vacuous. These
  are explicitly marked as open claims requiring future work.
paper_text: "# Introduction\n\nNeuro-symbolic reasoning systems combine the generalization capacity of large language models\
  \ (LLMs) with the verifiability of symbolic logic. A common design pattern, exemplified by SymBa [1], begins with an *empty*\
  \ symbolic database: when the SLD resolver fails to prove a goal, the LLM is queried to generate the next fact or rule.\
  \ Under this design, the LLM is the first and only resort for all factual retrieval—including retrieval of facts that are\
  \ explicitly present in the input document. The result is two structurally distinct failure modes. First, *hallucination*:\
  \ the LLM may confabulate alternatives to document-stated content because no mechanism prevents it from generating facts\
  \ independently of the source text. Second, *opacity*: the derivation trace records that the LLM supplied a fact, but not\
  \ whether that fact was document-recoverable, ontologically entailed, or a genuine abduction from world knowledge, rendering\
  \ the trace unauditable.\n\nA critical consequence of SymBa's design appears in benchmarks that require *three-valued* Open\
  \ World Assumption (OWA) semantics: when a goal is unprovable, the correct answer may be *Unknown* rather than *False*.\
  \ The SymBa pipeline has no mechanism to distinguish the two: it invokes the LLM on proof failure and returns its (typically\
  \ binary) response. A system that instead exhausts cheaper evidence tiers first and returns *Unknown* when all tiers fail\
  \ would correctly answer such questions without any LLM call.\n\nWe propose a *provenance-stratified* pipeline that enforces\
  \ tier-ordered escalation: L0 (document extraction) → L1 (bounded SLD) → L2 (domain ontology) → L3 (LLM abduction). Each\
  \ proof-tree node carries an explicit (tier, confidence) tuple propagated under weakest-link semantics. The primary behavioral\
  \ difference from SymBa is that when L0 extraction fails to prove a leaf goal, the system does not immediately invoke the\
  \ LLM; it first tries L1 deductive closure and L2 ontology, and only returns a definite answer if one of these tiers succeeds.\
  \ If all tiers fail, the system returns *Unknown*.\n\n[FIGURE:fig1]\n\nWe evaluate this architecture on ProofWriter D*(OWA)\
  \ [9], a three-valued benchmark where *Unknown* is the correct label for goals that are not provable from the given theory.\
  \ On 200 examples drawn from the real HuggingFace dataset, the stratified pipeline achieves 45.0% accuracy versus the SymBa-style\
  \ baseline's 27.5% (McNemar p = 0.0046). The +17.5 point gain is entirely attributable to correct *Unknown* propagation:\
  \ the stratified system outputs *Unknown* for 200/200 ProofWriter OWA examples where the L0 extraction does not supply provable\
  \ facts, while SymBa defaults to *False*. \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-45095e-provenance-stratified-neuro-symbolic-rea/tree/main/round-2/evaluation-1}}\n\
  \nWe report with equal clarity what the current evaluation does *not* support. The L0 tier used heuristic regex extraction\
  \ rather than the proposed LLM-based extraction, incurring zero API cost. The L2 tier (LKIF/ConceptNet/Wikidata) was never\
  \ triggered across 500 examples. L3 self-consistency abduction was never invoked. Secondary claims regarding hallucination\
  \ reduction and L2 ontology coverage therefore remain empirically unverified.\n\n**Summary of contributions:**\n- A complete\
  \ four-tier neuro-symbolic architecture with tier-ordered SLD escalation and weakest-link provenance propagation (Section\
  \ 3).\n- Empirical evidence that OWA Unknown propagation—returning *Unknown* when no tier proves a goal—outperforms SymBa's\
  \ False-by-default on ProofWriter D*(OWA): 45.0% vs. 27.5%, McNemar p = 0.0046 (Section 4).\n- JSON-LD trace export with\
  \ per-node (tier, confidence) annotations for human-auditable derivations (Section 3.6).\n- An honest experimental accounting:\
  \ identification of which claims are confirmed, which are unverified, and a concrete agenda for future work (Section 5).\n\
  \n# Related Work\n\n**Neuro-symbolic SLD resolution.** SymBa [1] integrates SLD-resolution with an LLM via a coroutine that\
  \ calls the LLM on every proof failure. Its five-module generation pipeline (Fact Search, Rule Search, Translation, Symbolic\
  \ Validation, Backtracking) uses the LLM as the sole knowledge source because the KB starts empty. The proposed system differs\
  \ architecturally by pre-populating the KB from the document (L0) and inserting a domain ontology tier (L2) before any LLM\
  \ invocation. Under SymBa's design, an unprovable goal triggers an LLM call that will return a binary yes/no, making it\
  \ structurally incapable of returning *Unknown* for OWA benchmarks.\n\n**FOL translation and theorem proving.** LINC [5]\
  \ uses an LLM to translate natural language premises into first-order logic and delegates proof search to a Prolog prover.\
  \ Proof failures return *unknown* without LLM escalation, has no ontology integration, and produces no provenance-annotated\
  \ trace. Logic-LM [6] extends this with iterative LLM feedback on proof failures but lacks per-predicate provenance annotation\
  \ or ontology integration. FOLIO [13] provides a challenging benchmark for FOL reasoning from natural language premises.\n\
  \n**Hybrid reasoning with ordered fallback.** ROSCOE [14] evaluates step-by-step reasoning chains with ordered metrics but\
  \ does not perform symbolic execution. Systems combining symbolic solvers with neural components have appeared across multiple\
  \ venues, but the specific combination of document-grounded KB initialization, bounded SLD, domain-adaptive ontology, and\
  \ LLM abduction with per-node provenance propagation has not, to our knowledge, been published. The weakest-link propagation\
  \ rule differs from Markov Logic Networks [15], which assign a single weight to each formula rather than propagating epistemic-source\
  \ labels through proof trees. DeepProbLog [8] assigns uncertainty from a single neural distribution rather than from a named\
  \ evidence hierarchy.\n\n**Retrieval-augmented generation.** RAG systems [7] retrieve context passages to ground LLM generation.\
  \ RAG operates at the token level and produces no symbolic proof trace; individual retrieved facts carry no epistemic tier\
  \ label. The proposed system's derivations are SLD-resolution trees in which each leaf node is labeled by source tier.\n\
  \n**Legal and statutory reasoning.** Holzenberger et al. [10] demonstrated that a hand-constructed Prolog knowledge base\
  \ pre-populated from statutory text achieves 100% accuracy on the SARA benchmark, precisely because document-explicit facts\
  \ are retrieved symbolically rather than generatively. The LKIF Core OWL ontology [4] provides a principled terminological\
  \ foundation for legal concepts. ContractNLI [3] documents that complex hedged language in non-disclosure agreements is\
  \ a primary source of NLI difficulty.\n\n# Methods\n\n## System Architecture\n\nThe pipeline processes each input document\
  \ through four sequentially escalating tiers. \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-45095e-provenance-stratified-neuro-symbolic-rea/tree/main/round-1/experiment-1}}\n\
  \n**L0 — Document-Grounded KB Initialization.** Given an input document, the L0 extractor identifies atomic Prolog predicates\
  \ and asserts them as `fact(Pred, l0, 1.0)` in SWI-Prolog before any reasoning begins. Domain-specific rules stated explicitly\
  \ in the document are stored as `rule(Head, Body, l0, 1.0)`. The design specifies LLM-based extraction (meta-llama/llama-3.1-70b-instruct\
  \ via OpenRouter with structured JSON prompts); the current evaluation used a heuristic regex extractor as a baseline implementation.\
  \ A disk-based cache prevents redundant calls on pipeline restarts. The L0 initialization step is the primary architectural\
  \ departure from SymBa: the KB is populated from the document before the resolver is invoked.\n\n**L1 — Bounded SLD Resolution.**\
  \ Once L0 facts are asserted, the meta-interpreter executes a full SWI-Prolog query with `call_with_depth_limit/3` at depth\
  \ $d = 5$ and no new predicate invention. A goal that succeeds within the depth limit is resolved at tier L1 with confidence\
  \ 1.0. A goal that returns `depth_limit_exceeded` or fails triggers escalation to L2. SWI-Prolog is interfaced via subprocess\
  \ rather than the pyswip FFI to avoid thread-safety issues in concurrent evaluation.\n\n**L2 — Domain-Adaptive Ontology.**\
  \ The document domain is classified at runtime into legal, narrative, or general. For legal documents, the LKIF Core OWL\
  \ ontology [4] is consulted via class-subsumption queries covering the concept hierarchy {Obligation, Prohibition, Permission,\
  \ Right, Legal\\_Document, Contract, Norm, Agent}; a fallback dictionary of 50 LKIF concepts handles cases where the OWL\
  \ parser is unavailable. For narrative documents, the ConceptNet REST API [11] is queried for IsA, PartOf, and UsedFor relations.\
  \ For general-domain documents, Wikidata SPARQL is queried with a required User-Agent header. Confirmed L2 facts are cached\
  \ as `fact(Pred, l2, c)` where $c = 0.95$ for OWL subsumption entailment and $c = 0.80$ for ConceptNet statistical association\
  \ edges.\n\n**L3 — Self-Consistency LLM Abduction.** Only when L0, L1, and L2 all fail to prove a leaf goal does the meta-interpreter\
  \ invoke L3 abduction. An abductive schema template query is constructed from the failed goal's predicate name, partially\
  \ bound arguments, and the parent proof context, then submitted independently $K = 5$ times to the LLM. The L3 confidence\
  \ is the fraction of *yes* responses. Facts with confidence below 0.6 are flagged *low-confidence abduction*; at threshold\
  \ $\\tau = 0.4$, the system returns *Unknown* rather than asserting falsity, implementing three-valued OWA semantics.\n\n\
  **Weakest-Link Provenance Propagation.** For a derived goal with premises $p_1, \\ldots, p_n$, the propagated tier is $\\\
  mathrm{Tier}(\\mathrm{derived}) = \\max_i \\mathrm{Tier}(p_i)$ and the propagated confidence is $\\mathrm{Conf}(\\mathrm{derived})\
  \ = \\min_i \\mathrm{Conf}(p_i)$. Comparison is lexicographic: tier label takes priority over confidence. This rule ensures\
  \ that a conclusion citing any L3 abduction propagates an L3 label regardless of how many L0 premises contributed to the\
  \ proof. The rule is analogous to integrity-label propagation in the Biba model: a conclusion is only as trustworthy as\
  \ its least-trusted premise.\n\n**JSON-LD Trace Export.** The complete derivation tree is exported as a JSON-LD document\
  \ with each node labeled \\{predicate, args, tier, confidence, source\\_doc\\_span\\}. A static HTML visualization color-codes\
  \ tier labels: green for L0, yellow for L1, orange for L2, red for L3, gray for Unknown. These traces are the primary interpretability\
  \ artifact.\n\n[FIGURE:fig2]\n\n## Baselines\n\nTwo baselines are evaluated alongside the stratified pipeline.\n\n*SymBa-style\
  \ flat LLM.* Following SymBa [1], the baseline starts with an empty Prolog KB and issues a single structured LLM call for\
  \ each query with no ontology tier. The LLM response is parsed for a yes/no/true/false/unknown determination and mapped\
  \ to the benchmark answer space. Under this design, when a goal is unprovable from the empty KB, the system returns whatever\
  \ the LLM generates; it has no mechanism to propagate *Unknown* for genuinely underdetermined goals.\n\n*Chain-of-Thought\
  \ (CoT).* The LLM is prompted with the full document and question using multi-step chain-of-thought prompting [12], and\
  \ the final answer is extracted by regex matching on True/False/Unknown/Entailment/Contradiction keywords.\n\n# Results\n\
  \n## Experimental Setup\n\nFour benchmarks were targeted. Two produced informative results; two did not.\n\n*ProofWriter\
  \ D*(OWA)* [9] (200 examples, real HuggingFace data, `tasksource/proofwriter`): Multi-hop logical reasoning under Open World\
  \ Assumption with three-valued True/False/Unknown labels. This is the primary benchmark. \\footnote{Code: \\url{https://github.com/AMGrobelnik/ai-invention-45095e-provenance-stratified-neuro-symbolic-rea/tree/main/round-1/dataset-1}}\n\
  \n*ContractNLI* [3] (50 examples, synthetic fallback): NDA clause entailment with three labels. **Caveat:** the evaluation\
  \ used a synthetic dataset generator, not the real ContractNLI corpus (607 NDAs). Results on these 50 synthetic examples\
  \ are reported for completeness but do not constitute evaluation on ContractNLI.\n\n*SARA* [10] (50 examples, synthetic\
  \ fallback): US federal tax law reasoning. **Caveat:** the evaluation used a synthetic generator cycling through 5 generic\
  \ contract templates (`sara_synth_0` through `sara_synth_49`), not the real SARA benchmark with gold Prolog KB annotations.\
  \ The 100% accuracy reported is an artifact of trivially-structured template patterns that all three systems match identically;\
  \ it is not a meaningful statutory reasoning result.\n\n*CLUTRR* [16] (200 examples, synthetic fallback): Kinship reasoning.\
  \ All three systems achieved 0% due to a label format mismatch between the synthetic generator's output (`grandmother`,\
  \ `father`) and the answer extractor (which returned `proved`/`unknown`). This result is entirely uninformative and is excluded\
  \ from the main results table.\n\nAll ProofWriter OWA examples are drawn from the real HuggingFace dataset and are the only\
  \ results treated as valid evidence for claims about the pipeline's capabilities.\n\n## Main Results\n\nTable 1 reports\
  \ per-benchmark accuracy with 95% Wilson confidence intervals and McNemar's test for the stratified vs. SymBa comparison.\
  \ CLUTRR is excluded from the table; its all-zero result is a data-loading artifact rather than a meaningful capability\
  \ measurement.\n\n| Benchmark | $n$ | Stratified | SymBa | CoT | McNemar $p$ |\n|---|---|---|---|---|---|\n| ProofWriter\
  \ OWA (real) | 200 | **0.450** [0.383, 0.519] | 0.275 [0.218, 0.341] | 1.000 [0.981, 1.000] | **0.0046*** |\n| SARA (synthetic\
  \ only†) | 50 | 1.000 | 1.000 | 1.000 | 1.0 |\n| ContractNLI (synthetic only†) | 50 | 0.400 [0.276, 0.538] | 0.400 | 0.400\
  \ | 1.0 |\n\n†Synthetic fallback data; results are not evaluations of the named benchmark.\n\nThe stratified pipeline outperforms\
  \ the SymBa-style flat baseline on ProofWriter OWA (45.0% vs. 27.5%, absolute +17.5 points, McNemar p = 0.0046). On the\
  \ synthetic SARA and ContractNLI data, all three systems are tied; these results carry no interpretive weight.\n\nThe CoT\
  \ baseline achieves 100% on ProofWriter OWA. This result reflects that the CoT answer extractor was calibrated on the ProofWriter\
  \ OWA answer distribution (True/False/Unknown keywords), giving it an in-distribution advantage. The CoT result on ProofWriter\
  \ OWA should not be interpreted as a fair baseline comparison; it is reported for completeness.\n\n[FIGURE:fig3]\n\n## Analysis\
  \ of the ProofWriter OWA Result\n\nThe stratified pipeline's ProofWriter OWA advantage is mechanically explained. When the\
  \ L0 heuristic extractor processes a ProofWriter theory (average 4.94 facts per theory), the extracted predicates are surface-form\
  \ property attributions that do not match the queried goal predicates (which require multi-hop chaining). The L1 depth-5\
  \ SLD resolver cannot chain from the extracted surface predicates to the queried property. L2 and L3 are not triggered in\
  \ this evaluation. The meta-interpreter therefore returns *Unknown* for all 200 examples.\n\nOf the 200 ProofWriter OWA\
  \ examples, the gold label distribution is: True (approx. 60 examples), False (approx. 50 examples), Unknown (approx. 90\
  \ examples). The stratified system's 90 correct answers come entirely from the 90 Unknown-labeled examples—for which returning\
  \ *Unknown* is correct. The SymBa baseline, which defaults to *False* on proof failure, achieves 0 correct on Unknown-labeled\
  \ examples and 55 correct on False-labeled examples, for a total of 55/200 = 27.5%. The McNemar b–c counts (b = 90, c =\
  \ 55) confirm this picture: the stratified system wins on 90 examples the SymBa baseline gets wrong (the Unknown-labeled\
  \ examples) and loses on 55 examples SymBa gets right (the False-labeled examples).\n\nThis analysis makes the mechanism\
  \ transparent: the +17.5 point gain on ProofWriter OWA comes from the tier-ordered architecture's OWA semantics, specifically\
  \ its ability to return *Unknown* for unprovable goals rather than collapsing to *False*.\n\n## Tier Distribution\n\nAcross\
  \ all 500 examples, the L2 tier was triggered zero times (Wilson 95% CI: [0.000, 0.007]). For SARA and ContractNLI (synthetic),\
  \ 100% of resolved examples were attributed to the L0 tier. For ProofWriter OWA and CLUTRR (synthetic), 100% of examples\
  \ returned *Unknown* (the L1 SLD resolver could not chain from extracted surface predicates to the queried property). L3\
  \ was never invoked; total inference cost was $0.00. \n\n[FIGURE:fig4]\n\n## Unverified Claims\n\nThree secondary claims\
  \ from the hypothesis are explicitly unverified in this evaluation:\n\n1. *LLM-based L0 extraction.* The evaluation used\
  \ a regex heuristic extractor. The proposed LLM-based extraction was designed but not run. No API calls were made; the $0\
  \ cost confirms this. The Phase 0 gate—which required precision $\\geq 0.75$ against gold SARA Prolog annotations on 25\
  \ real cases—was evaluated on 5 synthetic examples with no gold annotations, making it scientifically invalid.\n\n2. *L2\
  \ ontology bridging.* The L2 tier (LKIF, ConceptNet, Wikidata) was never triggered for any of the 500 examples. A system\
  \ with three active tiers (L0, L1, L3) rather than four would produce identical results on this evaluation. The L2 contribution\
  \ is entirely untested.\n\n3. *Hallucination reduction.* The paper's previous draft claimed zero hallucination rates on\
  \ SARA and ContractNLI as evidence for L0 grounding. This claim was vacuous: no LLM calls were made, so no hallucination\
  \ was possible by construction. A meaningful hallucination measurement requires L3 abduction to fire on withheld-L0 examples;\
  \ that experiment was not conducted.\n\n# Discussion\n\n## What the Evidence Supports\n\nThe one empirically supported claim\
  \ is that tier-ordered OWA Unknown propagation significantly outperforms SymBa-style False-by-default on ProofWriter D*(OWA):\
  \ 45.0% vs. 27.5% (p = 0.0046). The mechanism is clear: the stratified system correctly returns *Unknown* for goals unprovable\
  \ within available evidence, while SymBa returns *False*. This improvement requires no LLM calls and no ontology lookups—it\
  \ is a structural consequence of the tier-ordered architecture's OWA semantics.\n\nThis finding has practical significance.\
  \ Many real-world reasoning tasks involve genuinely underdetermined questions where the appropriate response is epistemic\
  \ humility rather than a confident False answer. A system that conflates \"not provable from the document\" with \"false\"\
  \ will systematically over-claim, a failure mode that the stratified architecture avoids by construction.\n\n## Limitations\
  \ and Future Work\n\nFour concrete limitations bound the current results.\n\n*(1) Benchmark data integrity.* The SARA, ContractNLI,\
  \ and CLUTRR evaluations used synthetic fallback data due to implementation failures in the real-data loaders. These results\
  \ carry no evidentiary weight. Future evaluation must use: `SgfdDttt/sara` (376 cases, gold Prolog KB) for SARA, `kiddothe2b/contract-nli`\
  \ (607 NDAs) for ContractNLI, and `CLUTRR/v1` (gen\\_train234\\_test2) for CLUTRR. The CLUTRR zero-accuracy result is a\
  \ label-format implementation artifact and will not carry over to real data.\n\n*(2) L0 extraction implementation.* The\
  \ LLM-based extraction described in the Methods section was not run. The current evaluation is best understood as a comparison\
  \ between a tier-ordered Unknown-propagator (stratified) and a False-by-default system (SymBa), both operating on heuristic\
  \ surface-pattern KB initialization. The extraction calibration gate (Phase 0) must be re-executed on real SARA cases with\
  \ gold Prolog annotations.\n\n*(3) L2 ontology integration.* The LKIF fallback dictionary covers only 50 concepts. For ContractNLI\
  \ clauses involving conditional obligations and exception logic, subsumption hierarchy alone is insufficient; SWRL rules\
  \ expressing normative entailment patterns are required. The Wikidata integration requires entity linking to populate QID-based\
  \ queries. Targeted micro-evaluation tasks—legal questions requiring LKIF subsumption (e.g., is a contract a Legal\\_Document?),\
  \ narrative questions requiring ConceptNet (e.g., is a scalpel UsedFor cutting?)—must be designed to force L2 triggering\
  \ and measure its accuracy.\n\n*(4) Statistical power.* The ContractNLI and SARA results (n = 50 each) are too small for\
  \ meaningful conclusions. The ContractNLI tie at 40% has a $\\pm 13\\%$ confidence interval at 95%, making the systems statistically\
  \ indistinguishable. Evaluation on the full real ContractNLI test set (607 NDAs $\\times$ 17 hypotheses) would reduce this\
  \ to $\\pm 1.4\\%$.\n\n## Comparison to Chain-of-Thought\n\nThe CoT baseline achieves 100% on ProofWriter OWA, but this\
  \ result is not a fair comparison: the CoT answer extractor was calibrated on the ProofWriter OWA distribution. When the\
  \ calibration artifact is set aside, the meaningful comparison is stratified vs. SymBa, for which the statistical evidence\
  \ is clear. The CoT baseline remains useful as an indicator of what a well-calibrated purely-neural system can achieve on\
  \ closed logical theories; the stratified pipeline is designed to complement CoT by providing symbolic provenance traces\
  \ and OWA-correct Unknown responses, not to universally surpass neural approaches.\n\n# Conclusion\n\nWe presented a provenance-stratified\
  \ neuro-symbolic reasoning pipeline that enforces tier-ordered SLD escalation through L0 document extraction, L1 bounded\
  \ deduction, L2 domain-adaptive ontology, and L3 LLM abduction, with weakest-link (tier, confidence) provenance propagation\
  \ at every proof-tree node. On the one benchmark where real data was used (ProofWriter D*(OWA), n = 200), the stratified\
  \ pipeline significantly outperforms the SymBa-style flat empty-database baseline (45.0% vs. 27.5%, McNemar p = 0.0046),\
  \ with the gain attributable to correct Unknown propagation for unprovable goals under Open World Assumption semantics.\n\
  \nThe paper is explicit that secondary claims—LLM-based L0 extraction, L2 ontology bridging, and hallucination reduction—were\
  \ not tested in the current evaluation. Future work must: (a) run the LLM-based L0 extraction pipeline and validate against\
  \ real SARA gold Prolog annotations; (b) design micro-tasks that force L2 LKIF/ConceptNet triggering; (c) evaluate hallucination\
  \ by deliberately withholding L0 facts to trigger L3 abduction; and (d) evaluate on real SARA, ContractNLI, and CLUTRR data.\n\
  \n# References\n\n[1] Baek, J., Jeong, S., Kang, M., Park, J. C., & Hwang, S. J. (2025). SymBa: Symbolic Backward Chaining\
  \ for Multi-step Reasoning with Large Language Models. *NAACL 2025*.\n\n[2] Holzenberger, N., Blair-Stanek, A., & Van Durme,\
  \ B. (2020). A Dataset and Baselines for Sequential Open-Domain Question Answering over Statutory Text. *NLLP@KDD 2020*.\
  \ SARA benchmark.\n\n[3] Koreeda, Y., & Manning, C. D. (2021). ContractNLI: A Dataset for Document-level Natural Language\
  \ Inference for Contracts. *EMNLP 2021 Findings*, 1907–1919.\n\n[4] Hoekstra, R., Breuker, J., Di Bello, M., & Boer, A.\
  \ (2007). The LKIF Core Ontology of Basic Legal Concepts. *Estrella Project Deliverable*.\n\n[5] Olausson, T. X., Gu, A.,\
  \ Lipkin, B., Zhang, C. E., Solar-Lezama, A., Tenenbaum, J. B., & Levy, R. P. (2023). LINC: A Neurosymbolic Approach for\
  \ Logical Reasoning by Combining Language Models with First-Order Logic Provers. *EMNLP 2023*, 5153–5176.\n\n[6] Pan, L.,\
  \ Albalak, A., Wang, X., & Wang, W. Y. (2023). Logic-LM: Empowering Large Language Models with Symbolic Solvers for Faithful\
  \ Logical Reasoning. *EMNLP 2023 Findings*.\n\n[7] Lewis, P., et al. (2020). Retrieval-Augmented Generation for Knowledge-Intensive\
  \ NLP Tasks. *NeurIPS 2020*.\n\n[8] Manhaeve, R., Dumancic, S., Kimmig, A., Demeester, T., & De Raedt, L. (2018). DeepProbLog:\
  \ Neural Probabilistic Logic Programming. *NeurIPS 2018*.\n\n[9] Tafjord, O., Dalvi, B., & Clark, P. (2021). ProofWriter:\
  \ Generating Implications, Proofs, and Abductive Statements over Natural Language. *ACL 2021 Findings*, 3621–3634.\n\n[10]\
  \ Holzenberger, N., & Van Durme, B. (2023). Statute-based Statutory Reasoning with Legal Information Extraction. *NLLP 2023*.\n\
  \n[11] Speer, R., Chin, J., & Havasi, C. (2017). ConceptNet 5.5: An Open Multilingual Graph of General Knowledge. *AAAI\
  \ 2017*, 4444–4451.\n\n[12] Wei, J., et al. (2022). Chain of Thought Prompting Elicits Reasoning in Large Language Models.\
  \ *NeurIPS 2022*.\n\n[13] Han, S., et al. (2022). FOLIO: Natural Language Reasoning with First-Order Logic. *EMNLP 2022\
  \ Findings*.\n\n[14] Golovneva, O., et al. (2022). ROSCOE: A Suite of Metrics for Scoring Step-by-Step Reasoning. *arXiv:2212.07919*.\n\
  \n[15] Richardson, M., & Domingos, P. (2006). Markov Logic Networks. *Machine Learning*, 62, 107–136.\n\n[16] Sinha, K.,\
  \ Sodhani, S., Dong, J., Pineau, J., & Hamilton, W. L. (2019). CLUTRR: A Diagnostic Benchmark for Inductive Reasoning from\
  \ Text. *EMNLP 2019*, 4505–4514."
summary: >-
  We propose a provenance-stratified neuro-symbolic pipeline with four-tier ordered SLD escalation (L0 document extraction
  → L1 bounded deduction → L2 domain ontology → L3 LLM abduction) and weakest-link (tier, confidence) provenance propagation.
  The primary empirical finding—confirmed on real ProofWriter D*(OWA) data with statistical significance (McNemar p=0.0046)—is
  that tier-ordered OWA Unknown propagation outperforms SymBa's False-by-default design by +17.5 absolute points (45.0% vs.
  27.5%). The paper is explicit that secondary claims (LLM-based L0 extraction, L2 ontology bridging, hallucination reduction)
  were not exercised in the current evaluation and are marked as open claims requiring future work.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
title: Provenance-Stratified Pipeline Architecture
caption: >-
  The four-tier provenance-stratified neuro-symbolic pipeline. Each input document is first processed by L0 (document-grounded
  KB initialization), followed by L1 (bounded SLD resolution at depth 5), L2 (domain-adaptive ontology: LKIF for legal, ConceptNet
  for narrative, Wikidata for general), and L3 (self-consistency LLM abduction, $K$=5). Each tier is exhausted before the
  next is consulted. When all tiers fail, the system returns \textit{Unknown} rather than \textit{False}, implementing three-valued
  OWA semantics. Every proof-tree node carries a (tier, confidence) annotation propagated under weakest-link semantics.
image_gen_detailed_description: >-
  Horizontal left-to-right pipeline flow diagram on white background. Five main boxes connected by right-pointing arrows,
  labeled left to right: 'Input Document' (gray rounded box), 'L0: Document Extraction' (green box, subtitle: 'Regex/LLM extraction,
  fact(Pred, l0, 1.0)'), 'L1: Bounded SLD' (yellow box, subtitle: 'depth_limit=5, no predicate invention'), 'L2: Domain Ontology'
  (orange box, subtitle: 'LKIF legal / ConceptNet narrative / Wikidata general'), 'L3: LLM Abduction' (red box, subtitle:
  'K=5 self-consistency, conf=yes/5'). Below each transition arrow except the last: a small downward arrow to a gray diamond
  labeled 'Goal proved?' with two branches: a checkmark going down to a green 'Return Answer' box and an X going right to
  the next tier. After L3: a final diamond labeled 'All tiers failed?' with a downward branch to a gray 'Return Unknown' box.
  In the top-right corner: a small legend box with colored squares: green=L0, yellow=L1, orange=L2, red=L3, gray=Unknown.
  At the bottom: a proof-tree snippet showing a node labeled '(query, [goal], tier=unknown, conf=0.0)'. Sans-serif font, clean
  minimal style, no 3D effects.
aspect_ratio: '21:9'
summary: >-
  Hero architecture diagram showing the four-tier tier-ordered escalation pipeline with OWA Unknown propagation
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
title: JSON-LD Proof Trace Example
caption: >-
  Representative JSON-LD derivation trace for a ProofWriter OWA example (id: pw\_AttNeg-OWA-D0-4611). The root node shows
  the query goal resolved to tier=unknown (gray) with confidence 0.0 because no tier proved the goal. The stratified system
  correctly returns \textit{Unknown}, while the SymBa baseline returns \textit{False}. Gold label is \textit{True} in this
  example; the Unknown response is incorrect here, but on Unknown-labeled examples it produces the correct answer.
image_gen_detailed_description: >-
  Vertical tree diagram on white background. Root node at top: rounded rectangle, gray border, labeled 'query: pw_AttNeg-OWA-D0-4611'
  with two sub-labels: 'tier: unknown' in gray text and 'confidence: 0.0'. Below root, three child nodes connected by lines:
  (1) 'L0 extraction: 7 facts extracted' (green rounded rectangle, tier: l0, conf: 1.0) — no further children because L1 failed;
  (2) 'L1 SLD: depth_limit=5 exceeded' (yellow box, dashed border, labeled 'escalate to L2'); (3) 'L2 Ontology: domain=general,
  Wikidata queried, no match' (orange box, dashed border, labeled 'escalate to L3 — not triggered'). At bottom, a footer bar
  showing two system predictions side by side: left box (gray) 'Stratified: Unknown' with green checkmark for Unknown-labeled
  examples; right box (gray) 'SymBa: False' with red X for Unknown-labeled examples. Gold label shown as 'True' for this specific
  example. Sans-serif font, color-coded by tier, clean white background.
aspect_ratio: '21:9'
summary: >-
  JSON-LD proof trace showing Unknown tier propagation for a ProofWriter OWA example
figure_path: figures/fig2_v0.jpg

--- Item 3 ---
id: fig3
title: ProofWriter OWA Accuracy by System and Gold Label
caption: >-
  Accuracy breakdown on ProofWriter D*(OWA) ($n$=200) stratified by gold label class. The stratified pipeline (blue) achieves
  100\% accuracy on Unknown-labeled examples by returning \textit{Unknown} for all unprovable goals. The SymBa baseline (orange)
  achieves 0\% on Unknown-labeled examples because it defaults to \textit{False}. Both systems achieve 0\% on True-labeled
  and False-labeled examples, as the heuristic L0 extractor does not provide provable facts for these cases. The overall gap
  (45.0\% vs. 27.5\%) is entirely attributable to correct Unknown propagation.
image_gen_detailed_description: >-
  Grouped bar chart on white background. X-axis labeled 'Gold Label Category' with three groups: 'True (n≈60)', 'False (n≈50)',
  'Unknown (n≈90)'. Y-axis labeled 'Accuracy' from 0.0 to 1.0 with gridlines at 0.2, 0.4, 0.6, 0.8, 1.0. For group 'True (n≈60)':
  two bars — Stratified (blue) = 0.00, SymBa (orange) = 0.00. For group 'False (n≈50)': two bars — Stratified (blue) = 0.00,
  SymBa (orange) = 1.00. For group 'Unknown (n≈90)': two bars — Stratified (blue) = 1.00, SymBa (orange) = 0.00. Legend in
  top-right: blue square = 'Stratified (45.0% overall)', orange square = 'SymBa (27.5% overall)'. Title above chart: 'ProofWriter
  OWA — Accuracy by Gold Label'. McNemar p=0.0046 annotation as text in top-left corner of chart. Sans-serif font, clean white
  background, no 3D.
aspect_ratio: '21:9'
summary: >-
  Per-label-class accuracy breakdown revealing that the stratified pipeline's advantage comes entirely from Unknown propagation
figure_path: figures/fig3_v0.jpg

--- Item 4 ---
id: fig4
title: Tier Distribution Across Benchmarks
caption: >-
  Tier distribution (fraction of examples resolved at each tier) across the three benchmarks with non-trivial results. For
  SARA and ContractNLI (synthetic), 100\% of examples resolve at L0. For ProofWriter OWA (real data), 100\% of examples return
  Unknown—the L0 heuristic extractor provides surface-form facts that the L1 SLD resolver cannot chain into the queried properties.
  The L2 tier triggers zero times across all benchmarks (Wilson 95\% CI: [0.000, 0.007]), and L3 is never invoked.
image_gen_detailed_description: >-
  Stacked horizontal bar chart on white background. Three rows (benchmarks), one stacked bar each. Y-axis (benchmarks, top
  to bottom): 'ProofWriter OWA (n=200)', 'ContractNLI synth. (n=50)', 'SARA synth. (n=50)'. X-axis labeled 'Fraction of Examples'
  from 0.0 to 1.0. Colors for tiers: L0=green, L1=yellow, L2=orange, L3=red, Unknown=gray. Bar values: ProofWriter OWA: L0=0.00,
  L1=0.00, L2=0.00, L3=0.00, Unknown=1.00 (entire bar gray). ContractNLI synth: L0=1.00, L1=0.00, L2=0.00, L3=0.00, Unknown=0.00
  (entire bar green). SARA synth: L0=1.00, L1=0.00, L2=0.00, L3=0.00, Unknown=0.00 (entire bar green). Legend to the right
  of chart: colored squares for each tier label. Note below chart in small italic text: 'L2 trigger rate: 0/500 examples (CI:
  [0.000, 0.007])'. Sans-serif font, white background, no 3D.
aspect_ratio: '21:9'
summary: >-
  Stacked bar chart showing tier distribution: SARA/ContractNLI fully resolved at L0; ProofWriter OWA fully returns Unknown;
  L2/L3 never triggered
figure_path: figures/fig4_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/filename.jpg}
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure*|figure}[placement], \includegraphics, \caption, \label, \end{...} — pick env + placement by the figure's `aspect_ratio` field (see PLACEMENT below). Constrain every \includegraphics with `width=\linewidth,height=0.4\textheight,keepaspectratio` (single-column) or `width=\textwidth,height=0.45\textheight,keepaspectratio` (figure*). Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

PLACEMENT BY ASPECT RATIO (use the `aspect_ratio` field on each figure):
- `21:9` (architecture diagrams / hero figures): \begin{figure*}[!t] (full two-column width, top of page). The hero architecture diagram should appear EARLY in the paper — typically at the top of page 2. Marker placement in paper_text already determines this; preserve it.
- `16:9` (comparisons, multi-panel results): \begin{figure*}[!t] for full-width or \begin{figure}[!htbp] for single-column.
- `4:3` / `1:1` / `3:2` / `3:4` / `9:16`: \begin{figure}[!htbp] (single-column).
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Short descriptive title for this paper generation task (roughly 30-90 characters)",
      "maxLength": 90,
      "minLength": 30,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [2] HUMAN-USER prompt · 2026-06-15 21:49:58 UTC

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

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-06-15 21:50:02 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figure JPEGs, and bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.jpg}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS use `[!htbp]` float placement (NOT `[t]` or `[h]` alone)
- ALWAYS constrain with `width` and `keepaspectratio` to prevent page takeover
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/*.jpg` — all figure images (pre-generated, copied into workspace)
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-06-15 21:50:23 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
