# gen_art_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_BsitFYqY4k6S` — Neuro Logic Translation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_dataset_1` (terminal_claude_agent)

### [1] SYSTEM-USER prompt · 2026-06-15 20:12:11 UTC

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
Find, evaluate, and prepare high-quality datasets for the research experiment.
Adapt your search strategy based on the hypothesis and domain requirements.
</task>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. MUST check for and avoid each one.

**1. Picking Obscure or Unusable Datasets**
Do NOT select datasets just because they match a keyword. Red flags: very few downloads (<100), no documentation (dataset card, paper, or GitHub page). Prefer well-used datasets (not necessarily popular or widely known) with clear documentation.
CHECK: >100 downloads? Has documentation? If any "no" → find a better dataset.

**2. Fabricating Dataset Provenance**
Do NOT invent justifications for why a dataset is relevant. If a dataset name contains a number (e.g., "797"), do NOT assume it refers to a specific benchmark suite, OpenML ID, or paper without verification. In past runs, an agent assumed "797" referred to "OpenML benchmark suite 797" with zero evidence, then fabricated a rationale. This was completely false.
CHECK: Can you cite a specific, verifiable source (paper, benchmark page, dataset card) confirming this dataset is what you claim? If not, do not make provenance claims.

**3. Not Verifying Dataset Usefulness**
Always sanity-check that a dataset is actually suitable for the task before committing. Download a sample, inspect the features, and run a quick baseline appropriate for the domain. If the dataset lacks signal or structure for the hypothesis being tested, the entire experiment is wasted.

**4. Settling for the Only Search Result**
If your search returns only 1-2 results, your search terms are too narrow. Broaden your queries, try different keyword combinations, or search for well-known benchmark datasets in the domain. A single obscure result from a narrow query should never be your final choice.
CHECK: Fewer than 5 candidate datasets? Run additional searches with broader or different terms before making a selection.
</common_mistakes_to_avoid>

<critical_requirements>
- Keep final response under 300 characters
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

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: 'Benchmark Dataset Collection: ProofWriter OWA, CLUTRR, SARA, ContractNLI'
summary: >-
  Acquire and standardize four benchmark datasets (ProofWriter D*OWA, CLUTRR, SARA, ContractNLI) into a unified JSON schema
  with domain tags, gold labels, hop counts, and train/test splits, ready for the neuro-symbolic pipeline experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  Four datasets are required, each serving a distinct role in the hypothesis evaluation:

  1. ProofWriter D*(OWA): Multi-hop natural language reasoning with three-valued labels (True/False/Unknown). Must be the OWA (Open World Assumption) variant specifically, as it supports Unknown answers needed for tier-ordered CWA/OWA switching. Target: ~500 examples for mini split from `tasksource/proofwriter` HuggingFace dataset; full set for complete run. Required fields: theory text (facts + rules), question, label (True/False/Unknown), proof depth (0-5). Domain tag: 'general'.

  2. CLUTRR v1: Kinship multi-hop reasoning with semi-synthetic family stories. Must include hop count per example (filter 2-5 hop examples). Required fields: story text, query (two entity names), target relation, k_hop count. Source: `CLUTRR/v1` on HuggingFace (test split: 1049 samples). Domain tag: 'narrative'.

  3. SARA: US federal tax law statutory reasoning with gold Prolog KB annotations. Must preserve the gold Prolog predicate sets per case description for Phase 0 extraction calibration. 25 examples randomly sampled for Phase 0 gate, remainder for evaluation. Total: ~376 cases. Source: GitHub `SgfdDttt/sara`. Required fields: case_description text, question, gold_label (yes/no/unknown tax obligation), gold_prolog_predicates (list of strings from the .pl files). Domain tag: 'legal'.

  4. ContractNLI: 607 NDAs with document-level NLI labels and evidence spans. Required fields: hypothesis text, document excerpt (contract text or relevant section), label (Entailment/Contradiction/NotMentioned), evidence_spans (character offsets). Source: Stanford NLP official release at stanfordnlp.github.io/contract-nli/. Domain tag: 'legal'.

  All datasets must fit within 300MB total. Each must pass aii-json schema validation before output.
dataset_search_plan: |-
  Execute the following steps in order:

  ## Step 0: Install dependencies
  ```
  uv pip install datasets requests tqdm
  ```

  ## Step 1: ProofWriter D*(OWA) — HuggingFace

  1a. Use the aii-hf-datasets skill to search for 'proofwriter' on HuggingFace. The primary target is `tasksource/proofwriter` which is a clean re-upload of the original AllenAI dataset.

  1b. Preview the dataset to find the OWA config. The original ProofWriter dataset has multiple configs: `depth-0`, `depth-1`, `depth-2`, `depth-3`, `depth-5`, and `OWA` variants. Look for a config named `OWA`, `D*`, or similar containing True/False/Unknown labels.

  1c. Download logic:
  - First try: `datasets.load_dataset('tasksource/proofwriter', config='OWA')` or try config names ending in 'OWA'.
  - If no explicit OWA config: load all depth configs and filter for examples where the label field includes 'Unknown' values (this identifies OWA examples). The `renma/ProofWriter` and `D3xter1922/proofwriter-dataset` mirrors are fallbacks.
  - Fallback: Download directly from AllenAI's original S3/website. The ProofWriter paper (arxiv 2012.13048) indicates the data is at `https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip`. Fetch this URL if HuggingFace configs don't expose OWA clearly.

  1d. Target schema extraction:
  ```python
  {
    'id': str,  # e.g. 'D0-OWA-ex001'
    'domain': 'general',
    'document_text': str,  # the 'context' field (facts+rules as English sentences)
    'question': str,  # the question
    'gold_label': str,  # 'True', 'False', or 'Unknown'
    'gold_predicates': [],  # not available for ProofWriter
    'hop_count': int,  # proof depth (0-5), from config name or 'depth' field
    'split': str  # 'train' or 'test'
  }
  ```

  1e. Mini split: 500 random examples from the OWA test set stratified across label types (True/False/Unknown) and proof depths.

  ## Step 2: CLUTRR — HuggingFace

  2a. Load `CLUTRR/v1` from HuggingFace datasets library: `datasets.load_dataset('CLUTRR/v1')`.

  2b. The dataset has multiple configs corresponding to test files (e.g., `2.1`, `2.2`, etc.). Load all test configs or the default split.

  2c. Filter for 2-5 hop examples only (the `k_hop` or `story_complexity` field). The full dataset has hops 2-10; restrict to 2-5 for tractability.

  2d. Schema extraction:
  ```python
  {
    'id': str,
    'domain': 'narrative',
    'document_text': str,  # the story text
    'question': str,  # e.g. 'What is the relationship between Alice and Bob?'
    'gold_label': str,  # kinship relation (e.g., 'grandmother')
    'gold_predicates': [],  # not available
    'hop_count': int,  # k_hop field
    'split': 'test'  # CLUTRR uses held-out test files
  }
  ```

  2e. Fallback if HuggingFace load fails: clone the GitHub repo `https://github.com/kliang5/CLUTRR_huggingface_dataset` or the original `https://github.com/facebookresearch/clutrr` and load CSV files directly. The CSV files are named like `data_089907f8.csv` with columns: `id`, `story`, `query`, `target`, `k_hop`.

  ## Step 3: SARA — GitHub

  3a. Clone (or wget) the SARA GitHub repository: `https://github.com/SgfdDttt/sara`

  3b. Run the dataset creation script if present: `bash code/make_dataset.sh` (may require SWI-Prolog). If SWI-Prolog is unavailable, directly parse the raw files.

  3c. Parse the dataset structure:
  - Case descriptions: look in `data/` or `cases/` directory for `.txt` or `.pl` files.
  - Each case has: a natural language description file (e.g., `case_001.txt`) and a Prolog facts file (e.g., `case_001.pl` or embedded in a combined file).
  - Gold labels: binary (does the person owe taxes?) — parse from the Prolog query or from a CSV/TSV index file if present.

  3d. Schema extraction:
  ```python
  {
    'id': str,  # e.g. 'sara_case_001'
    'domain': 'legal',
    'document_text': str,  # the English case description (~300-1000 chars)
    'question': str,  # tax obligation question
    'gold_label': str,  # 'yes'/'no' or 'entailed'/'not_entailed'
    'gold_predicates': [str],  # list of Prolog predicate strings from the .pl file
    'hop_count': None,  # not applicable
    'split': str  # 'train'/'test' or 'phase0'/'eval'
  }
  ```

  3e. Phase 0 split: randomly sample 25 examples and tag `split='phase0'`; remaining tagged `split='eval'`.

  3f. Fallback: if `make_dataset.sh` fails, directly read `.pl` files from the repo. The Prolog predicates are directly extractable from these files without needing SWI-Prolog to run.

  ## Step 4: ContractNLI — Direct Download

  4a. The official dataset is at `https://stanfordnlp.github.io/contract-nli/`. Fetch the download link from this page.

  4b. Primary download URL: try `https://stanfordnlp.github.io/contract-nli/data/contract-nli.zip` or find the exact link by fetching the page.

  4c. The dataset is typically a JSON file (`train.json`, `dev.json`, `test.json`) with this structure:
  ```json
  {
    "documents": [
      {
        "id": "...",
        "file_name": "...",
        "text": "<full NDA text>",
        "annotation_sets": [
          {
            "annotations": {
              "nda-1": {"choice": "Entailment", "spans": [...]},
              ...
            }
          }
        ]
      }
    ]
  }
  ```

  4d. Schema extraction (one row per document-hypothesis pair, flattening the nested structure):
  ```python
  {
    'id': str,  # '{doc_id}_{hypothesis_id}'
    'domain': 'legal',
    'document_text': str,  # excerpt of NDA text (first 3000 chars or evidence-span context window +/- 500 chars)
    'question': str,  # hypothesis text (e.g., 'The Agreement shall not grant the Receiving Party...')
    'gold_label': str,  # 'Entailment', 'Contradiction', or 'NotMentioned'
    'gold_predicates': [],  # not available
    'hop_count': None,
    'split': str,  # 'train'/'dev'/'test'
    'evidence_spans': [{'start': int, 'end': int}]  # character offsets in document_text
  }
  ```

  4e. Fallback: if stanfordnlp.github.io is unreachable, search HuggingFace for 'contractnli' or 'contract-nli'. Check `lexlms/lex_glue` which includes ContractNLI, or search directly.

  ## Step 5: Standardize and validate schema

  5a. Merge all four datasets into a single list `data_out.json`.

  5b. Unified schema per row:
  ```json
  {
    "id": "proofwriter_owa_001",
    "dataset": "proofwriter_owa",
    "domain": "general",
    "document_text": "Alice is a person. If someone is a person then they are mortal.",
    "question": "Is Alice mortal?",
    "gold_label": "True",
    "gold_predicates": [],
    "hop_count": 1,
    "evidence_spans": [],
    "split": "test",
    "metadata": {
      "source_dataset": "proofwriter_owa",
      "original_id": "..."
    }
  }
  ```

  5c. Run aii-json schema validation on the output.

  5d. Produce three output files:
  - `data_out_full.json` — all examples
  - `data_out_mini.json` — 10% sample (stratified by dataset and label)
  - `data_out_preview.json` — 5 rows, one from each dataset

  5e. Run aii-file-size-limit check on `data_out_full.json`. If >50MB, split into per-dataset files.

  ## Failure handling

  - If `CLUTRR/v1` HF load fails: clone GitHub repo directly and parse CSVs.
  - If SARA `make_dataset.sh` requires SWI-Prolog: skip execution, directly parse .pl files with Python string parsing (predicates are in standard Prolog syntax, easily parsed with regex).
  - If ContractNLI download URL fails: try the GitHub releases of `stanfordnlp/contract-nli-bert` which includes a data download script.
  - If ProofWriter OWA config not found: load `depth-5` config (deepest, most complex) and check if Unknown labels exist; if not, load all depths and filter for OWA examples.
  - Track total download size; stop if approaching 300MB limit.

  ## Output

  Final artifact: `data_out.json` (or per-dataset files) plus `data_out_mini.json` and `data_out_preview.json`, all in the unified schema above.
target_num_datasets: 4
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 2. Read skill files for your data sources (see <available_data_sources>) and domain handbook if applicable (see <available_domain_handbooks>). Based on plan and context, decide which source(s) to use. Include everything specified in the artifact plan, but you may also collect additional relevant data beyond what's listed. Run 32 diverse searches across chosen source(s) — BROAD, GENERAL terms, not very specific. Parallelize where supported.
TODO 3. Identify the 16 most promising datasets. IMPORTANT: Only consider datasets under 300MB. Preview/inspect sample rows for each candidate. Parallelize previews.
TODO 4. Research each candidate BEFORE choosing which to download. For each, search the web (aii-web-tools skill): dataset name, papers citing it, original source/task, popularity. Red flags: no search results, no papers, anonymized features (F1, F2...), <100 downloads, no documentation. Green flags: papers using it, clear documentation, meaningful features, established benchmark. Also consider: will features/structure allow meaningful evaluation of the planned method?
TODO 5. Decide which to KEEP vs DISCARD. Look for: clear structure, relevant fields, quality examples matching requirements, confirmed provenance. Determine which 8 datasets have the most suitable data. Download and save to `temp/datasets/`. Parallelize downloads.
</todos>
````

### [2] HUMAN-USER prompt · 2026-06-15 20:12:11 UTC

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

### [3] SKILL-INPUT — aii-python · 2026-06-15 20:13:27 UTC

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

### [4] SKILL-INPUT — aii-json · 2026-06-15 20:13:27 UTC

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

### [5] SKILL-INPUT — aii-file-size-limit · 2026-06-15 20:13:31 UTC

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

### [6] SKILL-INPUT — aii-use-hardware · 2026-06-15 20:13:31 UTC

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

### [7] SKILL-INPUT — aii-long-running-tasks · 2026-06-15 20:13:31 UTC

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

### [8] SKILL-INPUT — aii-hf-datasets · 2026-06-15 20:13:37 UTC

The agent loaded the **aii-hf-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-hf-datasets
description: Searches, previews, and downloads datasets from HuggingFace Hub. Use when user needs machine learning datasets, training data, HuggingFace datasets, dataset discovery, or .parquet/.json exports.
---

## Contents

- Workflow (3-phase dataset discovery)
- Scripts (Search, Preview, Download)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 3-Phase Dataset Discovery

### Phase 1: Search for Datasets
Find datasets with metadata (configs, splits, features, sizes)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "sentiment analysis" --limit 5
```

### Phase 2: Preview Dataset (if promising)
Inspect metadata AND sample rows in one call
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k
```

### Phase 3: Download Dataset (if suitable)
Download after reviewing the preview
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

---

## Scripts

### Search HuggingFace Datasets (aii_hf_search_datasets.py)

Search and discover datasets on HuggingFace Hub.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query "text classification" --limit 5
```

**Parallel execution (multiple queries):**

IMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_search_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'
```

**Example output:**
```
Found 5 dataset(s) for query='text classification'

============================================================
Dataset 1: stanfordnlp/imdb
Downloads: 2,500,000 | Likes: 1,234
Description: Large Movie Review Dataset for binary sentiment classification...
Tags: text-classification, en, sentiment-analysis
```

**Result fields per dataset:**

Each entry in ``results`` carries:

- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` — standard
  HF metadata
- ``has_loader_script`` (bool) — repo ships a top-level ``<repo>.py`` loader.
  ``datasets>=3`` won't run these directly; the dataset is reachable only
  via the Datasets Server's pre-converted parquet shards. Treat as a yellow
  flag.
- ``loadable`` (bool) — **prefer datasets where this is ``True``.** Means
  the dataset is reachable via *some* path: either native parquet (no
  script) or HF auto-converted the script's output to parquet. When
  ``False``, the script needs deps HF can't install (e.g. ``conllu``,
  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will
  fail — pick a different candidate.

**Parameters:**

`--query` (optional)
- Search query string
- Example: `--query "sentiment analysis"`

`--limit` (optional)
- Maximum number of results (default: 5)

`--tags` (optional)
- Filter by tags (comma-separated)
- Format: `category:value`
- Examples: `language:en`, `task_categories:text-classification`

`--sort` (optional)
- Sort by field: `downloads`, `likes` (default: downloads)

**Tips:**
- Search displays full dataset metadata
- Use tags to filter: `--tags "language:en,task_categories:translation"`

---

### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)

Inspect a specific dataset - shows metadata AND sample rows.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_preview_datasets.py" && \
parallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'
```

**Example output:**
```
============================================================
Dataset: openai/gsm8k
============================================================
Downloads: 425,109 | Likes: 1,102

Description: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality
linguistically diverse grade school math word problems...

Configs: main, socratic

--- Sample Rows (train) ---
Columns: question, answer

Row 1:
  question: Natalia sold clips to 48 of her friends in April...
  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `glue`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Auto-detects first config if not specified

`--split` (optional)
- Split to preview (default: `train`)

`--num-rows` (optional)
- Number of sample rows (default: 5, max: 20)

**Tips:**
- Use after search to verify data structure
- Streaming mode - doesn't download full dataset

---

### Download HuggingFace Dataset (aii_hf_download_datasets.py)

Download datasets and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train
```

**Parallel execution (multiple datasets):**

IMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_hf_download_datasets.py" && \
parallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'
```

**Example output:**
```
Downloaded: openai/gsm8k

  train:
    Rows: 7,473
    Preview: temp/datasets/preview_openai_gsm8k_main_train.json
    Mini: temp/datasets/mini_openai_gsm8k_main_train.json
    Full: temp/datasets/full_openai_gsm8k_main_train.json
```

**Parameters:**

`dataset_id` (required, positional)
- HuggingFace dataset ID
- Examples: `openai/gsm8k`, `imdb`

`--config` (optional)
- Dataset configuration/subset name
- Use preview to see available configs

`--split` (optional)
- Specific split to load (e.g., `train`, `test`)
- If not specified, loads all splits

`--output-dir` (optional)
- Output directory (default: `temp/datasets/`)

**Output files (auto-saved):**
1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection
2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing
3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code

**Tips:**
- Only read preview file directly with Read tool
- Mini and full are input paths for processing code

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [9] SYSTEM-USER prompt · 2026-06-15 20:29:41 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: 'Benchmark Dataset Collection: ProofWriter OWA, CLUTRR, SARA, ContractNLI'
summary: >-
  Acquire and standardize four benchmark datasets (ProofWriter D*OWA, CLUTRR, SARA, ContractNLI) into a unified JSON schema
  with domain tags, gold labels, hop counts, and train/test splits, ready for the neuro-symbolic pipeline experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  Four datasets are required, each serving a distinct role in the hypothesis evaluation:

  1. ProofWriter D*(OWA): Multi-hop natural language reasoning with three-valued labels (True/False/Unknown). Must be the OWA (Open World Assumption) variant specifically, as it supports Unknown answers needed for tier-ordered CWA/OWA switching. Target: ~500 examples for mini split from `tasksource/proofwriter` HuggingFace dataset; full set for complete run. Required fields: theory text (facts + rules), question, label (True/False/Unknown), proof depth (0-5). Domain tag: 'general'.

  2. CLUTRR v1: Kinship multi-hop reasoning with semi-synthetic family stories. Must include hop count per example (filter 2-5 hop examples). Required fields: story text, query (two entity names), target relation, k_hop count. Source: `CLUTRR/v1` on HuggingFace (test split: 1049 samples). Domain tag: 'narrative'.

  3. SARA: US federal tax law statutory reasoning with gold Prolog KB annotations. Must preserve the gold Prolog predicate sets per case description for Phase 0 extraction calibration. 25 examples randomly sampled for Phase 0 gate, remainder for evaluation. Total: ~376 cases. Source: GitHub `SgfdDttt/sara`. Required fields: case_description text, question, gold_label (yes/no/unknown tax obligation), gold_prolog_predicates (list of strings from the .pl files). Domain tag: 'legal'.

  4. ContractNLI: 607 NDAs with document-level NLI labels and evidence spans. Required fields: hypothesis text, document excerpt (contract text or relevant section), label (Entailment/Contradiction/NotMentioned), evidence_spans (character offsets). Source: Stanford NLP official release at stanfordnlp.github.io/contract-nli/. Domain tag: 'legal'.

  All datasets must fit within 300MB total. Each must pass aii-json schema validation before output.
dataset_search_plan: |-
  Execute the following steps in order:

  ## Step 0: Install dependencies
  ```
  uv pip install datasets requests tqdm
  ```

  ## Step 1: ProofWriter D*(OWA) — HuggingFace

  1a. Use the aii-hf-datasets skill to search for 'proofwriter' on HuggingFace. The primary target is `tasksource/proofwriter` which is a clean re-upload of the original AllenAI dataset.

  1b. Preview the dataset to find the OWA config. The original ProofWriter dataset has multiple configs: `depth-0`, `depth-1`, `depth-2`, `depth-3`, `depth-5`, and `OWA` variants. Look for a config named `OWA`, `D*`, or similar containing True/False/Unknown labels.

  1c. Download logic:
  - First try: `datasets.load_dataset('tasksource/proofwriter', config='OWA')` or try config names ending in 'OWA'.
  - If no explicit OWA config: load all depth configs and filter for examples where the label field includes 'Unknown' values (this identifies OWA examples). The `renma/ProofWriter` and `D3xter1922/proofwriter-dataset` mirrors are fallbacks.
  - Fallback: Download directly from AllenAI's original S3/website. The ProofWriter paper (arxiv 2012.13048) indicates the data is at `https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip`. Fetch this URL if HuggingFace configs don't expose OWA clearly.

  1d. Target schema extraction:
  ```python
  {
    'id': str,  # e.g. 'D0-OWA-ex001'
    'domain': 'general',
    'document_text': str,  # the 'context' field (facts+rules as English sentences)
    'question': str,  # the question
    'gold_label': str,  # 'True', 'False', or 'Unknown'
    'gold_predicates': [],  # not available for ProofWriter
    'hop_count': int,  # proof depth (0-5), from config name or 'depth' field
    'split': str  # 'train' or 'test'
  }
  ```

  1e. Mini split: 500 random examples from the OWA test set stratified across label types (True/False/Unknown) and proof depths.

  ## Step 2: CLUTRR — HuggingFace

  2a. Load `CLUTRR/v1` from HuggingFace datasets library: `datasets.load_dataset('CLUTRR/v1')`.

  2b. The dataset has multiple configs corresponding to test files (e.g., `2.1`, `2.2`, etc.). Load all test configs or the default split.

  2c. Filter for 2-5 hop examples only (the `k_hop` or `story_complexity` field). The full dataset has hops 2-10; restrict to 2-5 for tractability.

  2d. Schema extraction:
  ```python
  {
    'id': str,
    'domain': 'narrative',
    'document_text': str,  # the story text
    'question': str,  # e.g. 'What is the relationship between Alice and Bob?'
    'gold_label': str,  # kinship relation (e.g., 'grandmother')
    'gold_predicates': [],  # not available
    'hop_count': int,  # k_hop field
    'split': 'test'  # CLUTRR uses held-out test files
  }
  ```

  2e. Fallback if HuggingFace load fails: clone the GitHub repo `https://github.com/kliang5/CLUTRR_huggingface_dataset` or the original `https://github.com/facebookresearch/clutrr` and load CSV files directly. The CSV files are named like `data_089907f8.csv` with columns: `id`, `story`, `query`, `target`, `k_hop`.

  ## Step 3: SARA — GitHub

  3a. Clone (or wget) the SARA GitHub repository: `https://github.com/SgfdDttt/sara`

  3b. Run the dataset creation script if present: `bash code/make_dataset.sh` (may require SWI-Prolog). If SWI-Prolog is unavailable, directly parse the raw files.

  3c. Parse the dataset structure:
  - Case descriptions: look in `data/` or `cases/` directory for `.txt` or `.pl` files.
  - Each case has: a natural language description file (e.g., `case_001.txt`) and a Prolog facts file (e.g., `case_001.pl` or embedded in a combined file).
  - Gold labels: binary (does the person owe taxes?) — parse from the Prolog query or from a CSV/TSV index file if present.

  3d. Schema extraction:
  ```python
  {
    'id': str,  # e.g. 'sara_case_001'
    'domain': 'legal',
    'document_text': str,  # the English case description (~300-1000 chars)
    'question': str,  # tax obligation question
    'gold_label': str,  # 'yes'/'no' or 'entailed'/'not_entailed'
    'gold_predicates': [str],  # list of Prolog predicate strings from the .pl file
    'hop_count': None,  # not applicable
    'split': str  # 'train'/'test' or 'phase0'/'eval'
  }
  ```

  3e. Phase 0 split: randomly sample 25 examples and tag `split='phase0'`; remaining tagged `split='eval'`.

  3f. Fallback: if `make_dataset.sh` fails, directly read `.pl` files from the repo. The Prolog predicates are directly extractable from these files without needing SWI-Prolog to run.

  ## Step 4: ContractNLI — Direct Download

  4a. The official dataset is at `https://stanfordnlp.github.io/contract-nli/`. Fetch the download link from this page.

  4b. Primary download URL: try `https://stanfordnlp.github.io/contract-nli/data/contract-nli.zip` or find the exact link by fetching the page.

  4c. The dataset is typically a JSON file (`train.json`, `dev.json`, `test.json`) with this structure:
  ```json
  {
    "documents": [
      {
        "id": "...",
        "file_name": "...",
        "text": "<full NDA text>",
        "annotation_sets": [
          {
            "annotations": {
              "nda-1": {"choice": "Entailment", "spans": [...]},
              ...
            }
          }
        ]
      }
    ]
  }
  ```

  4d. Schema extraction (one row per document-hypothesis pair, flattening the nested structure):
  ```python
  {
    'id': str,  # '{doc_id}_{hypothesis_id}'
    'domain': 'legal',
    'document_text': str,  # excerpt of NDA text (first 3000 chars or evidence-span context window +/- 500 chars)
    'question': str,  # hypothesis text (e.g., 'The Agreement shall not grant the Receiving Party...')
    'gold_label': str,  # 'Entailment', 'Contradiction', or 'NotMentioned'
    'gold_predicates': [],  # not available
    'hop_count': None,
    'split': str,  # 'train'/'dev'/'test'
    'evidence_spans': [{'start': int, 'end': int}]  # character offsets in document_text
  }
  ```

  4e. Fallback: if stanfordnlp.github.io is unreachable, search HuggingFace for 'contractnli' or 'contract-nli'. Check `lexlms/lex_glue` which includes ContractNLI, or search directly.

  ## Step 5: Standardize and validate schema

  5a. Merge all four datasets into a single list `data_out.json`.

  5b. Unified schema per row:
  ```json
  {
    "id": "proofwriter_owa_001",
    "dataset": "proofwriter_owa",
    "domain": "general",
    "document_text": "Alice is a person. If someone is a person then they are mortal.",
    "question": "Is Alice mortal?",
    "gold_label": "True",
    "gold_predicates": [],
    "hop_count": 1,
    "evidence_spans": [],
    "split": "test",
    "metadata": {
      "source_dataset": "proofwriter_owa",
      "original_id": "..."
    }
  }
  ```

  5c. Run aii-json schema validation on the output.

  5d. Produce three output files:
  - `data_out_full.json` — all examples
  - `data_out_mini.json` — 10% sample (stratified by dataset and label)
  - `data_out_preview.json` — 5 rows, one from each dataset

  5e. Run aii-file-size-limit check on `data_out_full.json`. If >50MB, split into per-dataset files.

  ## Failure handling

  - If `CLUTRR/v1` HF load fails: clone GitHub repo directly and parse CSVs.
  - If SARA `make_dataset.sh` requires SWI-Prolog: skip execution, directly parse .pl files with Python string parsing (predicates are in standard Prolog syntax, easily parsed with regex).
  - If ContractNLI download URL fails: try the GitHub releases of `stanfordnlp/contract-nli-bert` which includes a data download script.
  - If ProofWriter OWA config not found: load `depth-5` config (deepest, most complex) and check if Unknown labels exist; if not, load all depths and filter for OWA examples.
  - Track total download size; stop if approaching 300MB limit.

  ## Output

  Final artifact: `data_out.json` (or per-dataset files) plus `data_out_mini.json` and `data_out_preview.json`, all in the unified schema above.
target_num_datasets: 4
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 1. For the top 8 datasets, create data.py (uv inline script) that: loads from temp/datasets/, standardizes to exp_sel_data_out.json schema (aii-json skill), extracts all examples per dataset, handles domain requirements, saves to full_data_out.json.

Each data ROW must be a separate example — do NOT create one example per dataset or per fold. Each data point (row, sample, instance) = one example. 500 rows → 500 examples. The output is GROUPED BY DATASET:
```json
{
  "datasets": [
    {
      "dataset": "iris",
      "examples": [
        {"input": "...", "output": "...", "metadata_fold": 2, "metadata_feature_names": [...]},
        ...
      ]
    },
    {
      "dataset": "adult_census",
      "examples": [...]
    }
  ]
}
```
Per-example required fields:
- `input`: input features/text (tabular: JSON string of feature values)
- `output`: target/label (as string)
Per-example optional metadata via `metadata_<name>` fields (flat, not nested object):
- `metadata_fold`: fold assignment (int), `metadata_feature_names`: feature name list, `metadata_task_type`: "classification"/"regression", `metadata_n_classes`: number of classes, `metadata_row_index`: original row index, etc.
Do NOT use `split`, `dataset`, or `context` as per-example fields. Dataset name goes at the group level, metadata goes in `metadata_*` fields.
TODO 2. Run 'uv run data.py' and fix errors. Validate full_data_out.json against exp_sel_data_out.json schema (aii-json skill) — fix errors. Generate preview, mini, full versions with aii-json skill's format script.
TODO 3. Read preview to inspect examples. Choose THE BEST 4 DATASETS based on domain requirements and artifact objective. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
````

### [10] SYSTEM-USER prompt · 2026-06-15 20:38:39 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/file.py`, `/ai-inventor/aii_data/runs/run_BsitFYqY4k6S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/results/out.json`
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
id: gen_plan_dataset_1_idx2
type: dataset
title: 'Benchmark Dataset Collection: ProofWriter OWA, CLUTRR, SARA, ContractNLI'
summary: >-
  Acquire and standardize four benchmark datasets (ProofWriter D*OWA, CLUTRR, SARA, ContractNLI) into a unified JSON schema
  with domain tags, gold labels, hop counts, and train/test splits, ready for the neuro-symbolic pipeline experiment.
runpod_compute_profile: cpu_heavy
ideal_dataset_criteria: |-
  Four datasets are required, each serving a distinct role in the hypothesis evaluation:

  1. ProofWriter D*(OWA): Multi-hop natural language reasoning with three-valued labels (True/False/Unknown). Must be the OWA (Open World Assumption) variant specifically, as it supports Unknown answers needed for tier-ordered CWA/OWA switching. Target: ~500 examples for mini split from `tasksource/proofwriter` HuggingFace dataset; full set for complete run. Required fields: theory text (facts + rules), question, label (True/False/Unknown), proof depth (0-5). Domain tag: 'general'.

  2. CLUTRR v1: Kinship multi-hop reasoning with semi-synthetic family stories. Must include hop count per example (filter 2-5 hop examples). Required fields: story text, query (two entity names), target relation, k_hop count. Source: `CLUTRR/v1` on HuggingFace (test split: 1049 samples). Domain tag: 'narrative'.

  3. SARA: US federal tax law statutory reasoning with gold Prolog KB annotations. Must preserve the gold Prolog predicate sets per case description for Phase 0 extraction calibration. 25 examples randomly sampled for Phase 0 gate, remainder for evaluation. Total: ~376 cases. Source: GitHub `SgfdDttt/sara`. Required fields: case_description text, question, gold_label (yes/no/unknown tax obligation), gold_prolog_predicates (list of strings from the .pl files). Domain tag: 'legal'.

  4. ContractNLI: 607 NDAs with document-level NLI labels and evidence spans. Required fields: hypothesis text, document excerpt (contract text or relevant section), label (Entailment/Contradiction/NotMentioned), evidence_spans (character offsets). Source: Stanford NLP official release at stanfordnlp.github.io/contract-nli/. Domain tag: 'legal'.

  All datasets must fit within 300MB total. Each must pass aii-json schema validation before output.
dataset_search_plan: |-
  Execute the following steps in order:

  ## Step 0: Install dependencies
  ```
  uv pip install datasets requests tqdm
  ```

  ## Step 1: ProofWriter D*(OWA) — HuggingFace

  1a. Use the aii-hf-datasets skill to search for 'proofwriter' on HuggingFace. The primary target is `tasksource/proofwriter` which is a clean re-upload of the original AllenAI dataset.

  1b. Preview the dataset to find the OWA config. The original ProofWriter dataset has multiple configs: `depth-0`, `depth-1`, `depth-2`, `depth-3`, `depth-5`, and `OWA` variants. Look for a config named `OWA`, `D*`, or similar containing True/False/Unknown labels.

  1c. Download logic:
  - First try: `datasets.load_dataset('tasksource/proofwriter', config='OWA')` or try config names ending in 'OWA'.
  - If no explicit OWA config: load all depth configs and filter for examples where the label field includes 'Unknown' values (this identifies OWA examples). The `renma/ProofWriter` and `D3xter1922/proofwriter-dataset` mirrors are fallbacks.
  - Fallback: Download directly from AllenAI's original S3/website. The ProofWriter paper (arxiv 2012.13048) indicates the data is at `https://aristo-data-public.s3.amazonaws.com/proofwriter/proofwriter-dataset-V2020.12.3.zip`. Fetch this URL if HuggingFace configs don't expose OWA clearly.

  1d. Target schema extraction:
  ```python
  {
    'id': str,  # e.g. 'D0-OWA-ex001'
    'domain': 'general',
    'document_text': str,  # the 'context' field (facts+rules as English sentences)
    'question': str,  # the question
    'gold_label': str,  # 'True', 'False', or 'Unknown'
    'gold_predicates': [],  # not available for ProofWriter
    'hop_count': int,  # proof depth (0-5), from config name or 'depth' field
    'split': str  # 'train' or 'test'
  }
  ```

  1e. Mini split: 500 random examples from the OWA test set stratified across label types (True/False/Unknown) and proof depths.

  ## Step 2: CLUTRR — HuggingFace

  2a. Load `CLUTRR/v1` from HuggingFace datasets library: `datasets.load_dataset('CLUTRR/v1')`.

  2b. The dataset has multiple configs corresponding to test files (e.g., `2.1`, `2.2`, etc.). Load all test configs or the default split.

  2c. Filter for 2-5 hop examples only (the `k_hop` or `story_complexity` field). The full dataset has hops 2-10; restrict to 2-5 for tractability.

  2d. Schema extraction:
  ```python
  {
    'id': str,
    'domain': 'narrative',
    'document_text': str,  # the story text
    'question': str,  # e.g. 'What is the relationship between Alice and Bob?'
    'gold_label': str,  # kinship relation (e.g., 'grandmother')
    'gold_predicates': [],  # not available
    'hop_count': int,  # k_hop field
    'split': 'test'  # CLUTRR uses held-out test files
  }
  ```

  2e. Fallback if HuggingFace load fails: clone the GitHub repo `https://github.com/kliang5/CLUTRR_huggingface_dataset` or the original `https://github.com/facebookresearch/clutrr` and load CSV files directly. The CSV files are named like `data_089907f8.csv` with columns: `id`, `story`, `query`, `target`, `k_hop`.

  ## Step 3: SARA — GitHub

  3a. Clone (or wget) the SARA GitHub repository: `https://github.com/SgfdDttt/sara`

  3b. Run the dataset creation script if present: `bash code/make_dataset.sh` (may require SWI-Prolog). If SWI-Prolog is unavailable, directly parse the raw files.

  3c. Parse the dataset structure:
  - Case descriptions: look in `data/` or `cases/` directory for `.txt` or `.pl` files.
  - Each case has: a natural language description file (e.g., `case_001.txt`) and a Prolog facts file (e.g., `case_001.pl` or embedded in a combined file).
  - Gold labels: binary (does the person owe taxes?) — parse from the Prolog query or from a CSV/TSV index file if present.

  3d. Schema extraction:
  ```python
  {
    'id': str,  # e.g. 'sara_case_001'
    'domain': 'legal',
    'document_text': str,  # the English case description (~300-1000 chars)
    'question': str,  # tax obligation question
    'gold_label': str,  # 'yes'/'no' or 'entailed'/'not_entailed'
    'gold_predicates': [str],  # list of Prolog predicate strings from the .pl file
    'hop_count': None,  # not applicable
    'split': str  # 'train'/'test' or 'phase0'/'eval'
  }
  ```

  3e. Phase 0 split: randomly sample 25 examples and tag `split='phase0'`; remaining tagged `split='eval'`.

  3f. Fallback: if `make_dataset.sh` fails, directly read `.pl` files from the repo. The Prolog predicates are directly extractable from these files without needing SWI-Prolog to run.

  ## Step 4: ContractNLI — Direct Download

  4a. The official dataset is at `https://stanfordnlp.github.io/contract-nli/`. Fetch the download link from this page.

  4b. Primary download URL: try `https://stanfordnlp.github.io/contract-nli/data/contract-nli.zip` or find the exact link by fetching the page.

  4c. The dataset is typically a JSON file (`train.json`, `dev.json`, `test.json`) with this structure:
  ```json
  {
    "documents": [
      {
        "id": "...",
        "file_name": "...",
        "text": "<full NDA text>",
        "annotation_sets": [
          {
            "annotations": {
              "nda-1": {"choice": "Entailment", "spans": [...]},
              ...
            }
          }
        ]
      }
    ]
  }
  ```

  4d. Schema extraction (one row per document-hypothesis pair, flattening the nested structure):
  ```python
  {
    'id': str,  # '{doc_id}_{hypothesis_id}'
    'domain': 'legal',
    'document_text': str,  # excerpt of NDA text (first 3000 chars or evidence-span context window +/- 500 chars)
    'question': str,  # hypothesis text (e.g., 'The Agreement shall not grant the Receiving Party...')
    'gold_label': str,  # 'Entailment', 'Contradiction', or 'NotMentioned'
    'gold_predicates': [],  # not available
    'hop_count': None,
    'split': str,  # 'train'/'dev'/'test'
    'evidence_spans': [{'start': int, 'end': int}]  # character offsets in document_text
  }
  ```

  4e. Fallback: if stanfordnlp.github.io is unreachable, search HuggingFace for 'contractnli' or 'contract-nli'. Check `lexlms/lex_glue` which includes ContractNLI, or search directly.

  ## Step 5: Standardize and validate schema

  5a. Merge all four datasets into a single list `data_out.json`.

  5b. Unified schema per row:
  ```json
  {
    "id": "proofwriter_owa_001",
    "dataset": "proofwriter_owa",
    "domain": "general",
    "document_text": "Alice is a person. If someone is a person then they are mortal.",
    "question": "Is Alice mortal?",
    "gold_label": "True",
    "gold_predicates": [],
    "hop_count": 1,
    "evidence_spans": [],
    "split": "test",
    "metadata": {
      "source_dataset": "proofwriter_owa",
      "original_id": "..."
    }
  }
  ```

  5c. Run aii-json schema validation on the output.

  5d. Produce three output files:
  - `data_out_full.json` — all examples
  - `data_out_mini.json` — 10% sample (stratified by dataset and label)
  - `data_out_preview.json` — 5 rows, one from each dataset

  5e. Run aii-file-size-limit check on `data_out_full.json`. If >50MB, split into per-dataset files.

  ## Failure handling

  - If `CLUTRR/v1` HF load fails: clone GitHub repo directly and parse CSVs.
  - If SARA `make_dataset.sh` requires SWI-Prolog: skip execution, directly parse .pl files with Python string parsing (predicates are in standard Prolog syntax, easily parsed with regex).
  - If ContractNLI download URL fails: try the GitHub releases of `stanfordnlp/contract-nli-bert` which includes a data download script.
  - If ProofWriter OWA config not found: load `depth-5` config (deepest, most complex) and check if Unknown labels exist; if not, load all depths and filter for OWA examples.
  - Track total download size; stop if approaching 300MB limit.

  ## Output

  Final artifact: `data_out.json` (or per-dataset files) plus `data_out_mini.json` and `data_out_preview.json`, all in the unified schema above.
target_num_datasets: 4
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

<available_data_sources>
Use the sources appropriate to your task. Read the relevant skill file BEFORE using each source.

- **HuggingFace Hub** (HF) — ML datasets (NLP, vision, tabular, benchmarks)
- **Our World in Data** (OWID) — Global statistics (energy, health, economics, environment, demographics)
- **Alternate methods** — Python/shell (sklearn.datasets, openml, direct URL, APIs, etc.)

If the plan specifies a source or one fits better, use it.
You may combine sources. Use web search (aii-web-tools skill) to research candidates (background, papers, provenance) — NOT to find/download datasets.
</available_data_sources>

<available_domain_handbooks>
If your domain has a handbook, read the relevant skill file BEFORE working on that domain.

- **Multi-LLM Agents** — dataset selection, evaluation metrics, agent orchestration patterns
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
TODO 1. Update data.py to only include the chosen 4 datasets and generate full_data_out.json. Re-run to generate full_data_out.json. Validate output format with aii-json skill and fix any errors. Generate full, mini, and preview versions with aii-json skill's format script using `--input full_data_out.json` (creates full_full_data_out.json, mini_full_data_out.json, preview_full_data_out.json — rename to full_data_out.json, mini_data_out.json, preview_data_out.json).
TODO 2. Verify full_data_out.json, preview_data_out.json, and mini_data_out.json exist in your workspace (see <workspace>) and contain correct data.
TODO 3. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to full_data_out.json.
TODO 4. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `./.terminal_claude_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "DatasetExpectedFiles": {
      "description": "All expected output files from dataset artifact.",
      "properties": {
        "script": {
          "description": "Path to data.py script. Example: 'data.py'",
          "title": "Script",
          "type": "string"
        },
        "datasets": {
          "description": "Dataset file groups \u2014 one per dataset, each with full/mini/preview variants",
          "items": {
            "$ref": "#/$defs/DatasetFileSet"
          },
          "title": "Datasets",
          "type": "array"
        }
      },
      "required": [
        "script",
        "datasets"
      ],
      "title": "DatasetExpectedFiles",
      "type": "object"
    },
    "DatasetFileSet": {
      "description": "One dataset's three required output variants.",
      "properties": {
        "full": {
          "description": "Full dataset JSON file(s). Single file or split files. Example: ['full_data_out.json'] or ['full_data_out/full_data_out_1.json', 'full_data_out/full_data_out_2.json']",
          "items": {
            "type": "string"
          },
          "title": "Full",
          "type": "array"
        },
        "mini": {
          "description": "Mini dataset JSON file path (3 examples). Example: 'mini_data_out.json'",
          "title": "Mini",
          "type": "string"
        },
        "preview": {
          "description": "Preview dataset JSON file path (10 examples). Example: 'preview_data_out.json'",
          "title": "Preview",
          "type": "string"
        }
      },
      "required": [
        "full",
        "mini",
        "preview"
      ],
      "title": "DatasetFileSet",
      "type": "object"
    }
  },
  "description": "Dataset artifact \u2014 structured output + file metadata.\n\nFinds, evaluates, and prepares datasets for research experiments.\nProduces data.py and full_data_out.json files.",
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
      "$ref": "#/$defs/DatasetExpectedFiles",
      "description": "All output files you created. Must include data.py script plus dataset file groups (full/mini/preview variants)."
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "DatasetArtifact",
  "type": "object"
}
```

IMPORTANT: This task is NOT complete until you Write `./.terminal_claude_agent_struct_out.json`.
````

### [11] SYSTEM-USER prompt · 2026-06-15 20:41:33 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 2 problems — fix ALL of them at once:
  - at `layman_summary`: 'Collects four well-established reasoning benchmark datasets covering logical deduction, legal contract NLI, statutory tax reasoning with Prolog annotations, and science multi-hop QA, all standardized into a unified schema for neuro-symbolic pipeline evaluation.' is too long (at most 250 characters, got 261)
  - at `title`: 'Neuro-Symbolic Reasoning Benchmark Datasets: ProofWriter OWA, ContractNLI, SARA, OpenBookQA' is too long (at most 90 characters, got 91)
Every required field must be present and every field type must match the schema.

Please use the Write tool to overwrite `.terminal_claude_agent_struct_out.json` with corrected JSON. Do not invent new fields; match the schema you were given.
</validation-feedback>
```
