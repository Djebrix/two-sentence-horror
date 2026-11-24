"""Two-Sentence Horror entry.

Writes the story to <ENTRY_OUTPUT_DIR>/entry.txt (default /output).
Stdlib only, no network.
"""

import os
import re

LINE = "The man downstairs leaves a pair of small shoes outside his door every night, though he lives alone. This morning there were two pairs \u2014 and one of them was mine, still warm."

assert 1 <= len(LINE) <= 400, f"length {len(LINE)} out of range"
sentences = [s for s in re.split(r"(?<=[.!?])\s+", LINE.strip()) if s]
assert len(sentences) == 2, f"expected exactly 2 sentences, got {len(sentences)}"

out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
