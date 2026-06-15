#!/usr/bin/env python3
"""Split full_data_out.json into per-dataset files under 50MB."""

import json
from pathlib import Path
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")

WORKSPACE = Path(__file__).parent

def main():
    full_path = WORKSPACE / "full_data_out.json"
    logger.info(f"Loading {full_path.name} ({full_path.stat().st_size // 1024 // 1024}MB)")
    data = json.loads(full_path.read_text())

    out_dir = WORKSPACE / "data_out"
    out_dir.mkdir(exist_ok=True)

    datasets = data["datasets"]
    metadata = data.get("metadata", {})

    part_num = 1
    for ds in datasets:
        ds_name = ds["dataset"]
        part_data = {"metadata": metadata, "datasets": [ds]}
        part_path = out_dir / f"full_data_out_{part_num}.json"
        part_path.write_text(json.dumps(part_data, indent=2))
        size_mb = part_path.stat().st_size // 1024 // 1024
        logger.info(f"Part {part_num}: {ds_name} ({len(ds['examples'])} examples, {size_mb}MB) -> {part_path.name}")
        part_num += 1

    # Delete the oversized original
    full_path.unlink()
    logger.info(f"Deleted {full_path.name}")

    # Also delete duplicate
    dup = WORKSPACE / "full_full_data_out.json"
    if dup.exists():
        dup.unlink()
        logger.info("Deleted full_full_data_out.json")

    logger.info(f"Split into {part_num - 1} parts in {out_dir}/")

if __name__ == "__main__":
    main()
