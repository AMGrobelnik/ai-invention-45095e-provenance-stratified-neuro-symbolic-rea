#!/usr/bin/env python3
"""Convert flat data_out.json to exp_sel_data_out schema format."""

import json
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

WORKSPACE = Path(__file__).parent


def convert(data_out_path: Path, output_path: Path):
    logger.info(f"Loading {data_out_path.name}")
    examples = json.loads(data_out_path.read_text())
    logger.info(f"Total examples: {len(examples)}")

    # Group by dataset
    by_dataset: dict[str, list] = {}
    for ex in examples:
        ds = ex["dataset"]
        by_dataset.setdefault(ds, []).append(ex)

    datasets = []
    for ds_name, ds_examples in sorted(by_dataset.items()):
        converted = []
        for ex in ds_examples:
            # Build input: document text + question
            doc = ex.get("document_text", "")
            question = ex.get("question", "")
            if doc:
                input_text = f"Document: {doc}\n\nQuestion: {question}"
            else:
                input_text = question

            output_text = str(ex.get("gold_label", ""))

            item = {
                "input": input_text,
                "output": output_text,
                "metadata_dataset": ds_name,
                "metadata_domain": ex.get("domain", ""),
                "metadata_split": ex.get("split", ""),
                "metadata_hop_count": str(ex.get("hop_count", "")),
                "metadata_id": ex.get("id", ""),
            }

            # Add predicates if present
            preds = ex.get("gold_predicates", [])
            if preds:
                item["metadata_gold_predicates"] = json.dumps(preds[:10])  # truncate for metadata

            converted.append(item)

        datasets.append({"dataset": ds_name, "examples": converted})
        logger.info(f"  {ds_name}: {len(converted)} examples")

    result = {
        "metadata": {
            "description": "Neuro-symbolic reasoning benchmark datasets",
            "total_examples": len(examples),
            "datasets": list(sorted(by_dataset.keys())),
            "domains": ["general", "legal", "science"],
        },
        "datasets": datasets,
    }

    output_path.write_text(json.dumps(result, indent=2))
    logger.info(f"Saved to {output_path} ({output_path.stat().st_size // 1024 // 1024}MB)")
    return result


if __name__ == "__main__":
    data_path = WORKSPACE / "data_out.json"
    out_path = WORKSPACE / "full_data_out.json"
    convert(data_path, out_path)
