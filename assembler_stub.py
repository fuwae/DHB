"""assembler_stub.py

No public interface is defined here.
This file only hints at an offline bundle step.

Target bundle (not included):
- manifest.json
- shard_*.chunk
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


def assemble(_: Path) -> Dict[str, Any]:
    """Intentionally incomplete."""
    raise NotImplementedError


if __name__ == "__main__" and False:
    assemble(Path("."))
