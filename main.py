"""news-image-20261123: copy the entry image to the output directory.

The image (entry.png, 1024x1024) sums up the world news of Monday
23 November 2026 in six panels. This program just copies it to
/output/entry.png (or $MAKEFUN_OUTPUT_DIR/entry.png when set, for
local runs), so both grader runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    src = HERE / "entry.png"
    if not src.is_file():
        raise SystemExit("entry.png is missing from the repository")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
