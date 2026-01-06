from __future__ import annotations

from typing import Final, Optional

from resolver import Resolver


_r: Final = Resolver()


def kernel(axis_id: str, slot_id: int | str) -> Optional[str]:
    s = f"{int(slot_id):02d}" if str(slot_id).isdigit() else str(slot_id)
    return _r.get("kernels", axis_id, s)


def tone(axis_id: str, slot_id: int | str) -> Optional[str]:
    s = f"{int(slot_id):02d}" if str(slot_id).isdigit() else str(slot_id)
    return _r.get("tones", axis_id, s)
