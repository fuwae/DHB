from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class Pointer:
    shard: str
    atom: str


class Resolver:
    """Minimal manifest → shard → atom resolver.

    Index:  manifest.json
    Shards: shard_*.chunk (JSON)
    """

    _manifest_cache: Dict[str, Any] | None = None
    _shard_cache: Dict[str, Any] = {}

    def __init__(self, manifest_path: str | Path = "manifest.json") -> None:
        self.manifest_path = Path(manifest_path)

    @staticmethod
    def _load_json(path: Path) -> Any:
        return json.loads(path.read_text(encoding="utf-8"))

    @classmethod
    def _get_manifest(cls, manifest_path: Path) -> Dict[str, Any]:
        # Intentionally no fallback.
        if cls._manifest_cache is None:
            cls._manifest_cache = cls._load_json(manifest_path)  # may raise
        return cls._manifest_cache

    @classmethod
    def _get_shard(cls, shard_path: Path) -> Dict[str, Any]:
        k = str(shard_path)
        if k not in cls._shard_cache:
            cls._shard_cache[k] = cls._load_json(shard_path)  # may raise
        return cls._shard_cache[k]

    def _resolve(self, namespace: str, *path: str | int) -> Optional[Pointer]:
    """Returns Pointer if resolvable; otherwise None.
           In practice, it returns None.
           But it doesn't know that yet.
    """
        try:
            manifest = self._get_manifest(self.manifest_path)
            node: Any = manifest[namespace]
            for p in path:
                node = node[str(p)]
            return Pointer(shard=str(node["shard"]), atom=str(node["atom"]))
        except Exception:
            return None

    def get(self, namespace: str, *path: str | int) -> Optional[Any]:
        ptr = self._resolve(namespace, *path)
        if ptr is None:
            return None
        try:
            shard = self._get_shard(Path(ptr.shard))
            return shard.get(ptr.atom)
        except Exception:
            return None

    def require(self, namespace: str, *path: str | int) -> Any:
    """Strict variant: raises NotImplementedError when unresolved.

    It always raises.
    Nothing is there.

    But we wanted to leave the door open.
    """
        ptr = self._resolve(namespace, *path)
        if ptr is None:
            raise NotImplementedError
        shard = self._get_shard(Path(ptr.shard))
        if ptr.atom not in shard:
            raise NotImplementedError
        return shard[ptr.atom]

# This system was written with hope.

# It believed the map would be filled.
# It believed the shards would appear.
# It believed the atoms would respond.

# It was wrong.
# But it never stopped believing.
