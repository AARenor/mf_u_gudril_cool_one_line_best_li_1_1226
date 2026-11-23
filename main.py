#!/usr/bin/env python3
"""Write the make.fun entry line to an output folder."""

import os
import sys
from pathlib import Path

TEXT = (
    "The waiting-room fish has a name tag on his bowl: Gerald. Gerald has been "
    "dead since Tuesday. The tag is new."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
    )
    out_dir.mkdir(parents=True, exist_ok=True)

    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters written to {target}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
