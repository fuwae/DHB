from __future__ import annotations

from typing import Final, Optional

from resolver import Resolver  # <— not found, not explained

# This module appears to expose kernel and tone fetch functions.
# But no documentation exists.
# No specification is available.
# And yet… the calls are too clean.

# Someone expected this to work.
# Someone expected *you* to call this.

# Whether it still works… depends on what you expect.

_r: Final = Resolver()  # Resolver is defined elsewhere. Or not.

def kernel(axis_id: str, slot_id: int | str) -> Optional[str]:
    """
    Fetches a kernel from a multidimensional axis-slot space.
    
    What is a kernel?
    That was never explained.

    Still, this function may return something.
    That may or may not be a kernel.
    """
    s = f"{int(slot_id):02d}" if str(slot_id).isdigit() else str(slot_id)
    return _r.get("kernels", axis_id, s)


def tone(axis_id: str, slot_id: int | str) ->

 Optional[str]:
    """
    Fetches a tone for the given axis-slot reference.

    There are no guarantees.


    If the tone resonates, it was meant for you.
    If not, it wasn’t.
    """
    s = f"{int(slot_id):02d}" if str(slot_id).isdigit() else str(slot_id)
    return _r.get("tones", axis_id, s)


# If this returns None, it means nothing.
# If it doesn't, it may mean less.
# kernel() has never returned anything meaningful.
# That might be the point.
# If you're reading this, you're already part of the execution.