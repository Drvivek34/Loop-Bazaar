"""Load and save the Loop-Bazaar database without exceeding GitHub file/API limits.

The public loops_data.json file is a small manifest. Loop records live in JSON shards
under loops_data/. The loader keeps backward compatibility with the historical single-
file format so local scripts and older clones can still read the database.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Union


def load_database(path: Union[str, Path]) -> dict:
    manifest_path = Path(path)
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    shards = data.get("shards")
    if not shards:
        return data
    loops = []
    for shard_name in shards:
        shard = json.loads((manifest_path.parent / shard_name).read_text(encoding="utf-8"))
        loops.extend(shard.get("loops", shard if isinstance(shard, list) else []))
    data["loops"] = loops
    data["loopCount"] = len(loops)
    return data


def save_database(data: dict, path: Union[str, Path], shard_count: int = 8) -> None:
    manifest_path = Path(path)
    loops = data.get("loops", [])
    shard_dir = manifest_path.parent / "loops_data"
    shard_dir.mkdir(parents=True, exist_ok=True)
    shard_names = []
    chunk_size = max(1, (len(loops) + shard_count - 1) // shard_count)
    for index in range(0, len(loops), chunk_size):
        name = f"part-{index // chunk_size:03d}.json"
        (shard_dir / name).write_text(
            json.dumps({"loops": loops[index:index + chunk_size]}, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
        )
        shard_names.append(f"loops_data/{name}")
    manifest = {key: value for key, value in data.items() if key != "loops"}
    manifest["loopCount"] = len(loops)
    manifest["shards"] = shard_names
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
