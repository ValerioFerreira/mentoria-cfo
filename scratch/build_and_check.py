import sys
from pathlib import Path
from collections import Counter

# import batches
from dpp_batch1 import batch1
from dpp_batch2 import batch2
from dpp_batch3 import batch3

all_qs = batch1 + batch2 + batch3

print(f"Total questions loaded: {len(all_qs)}")
assert len(all_qs) == 108, f"Expected 108, got {len(all_qs)}"

letters = [q["header"].split("|")[1].strip() for q in all_qs]
counts = Counter(letters)
print("Letter distribution:", counts)

# build text
blocks = []
letters_list = ["A", "B", "C", "D", "E"]
for i, q in enumerate(all_qs, 1):
    header = q["header"].strip()
    stem = q["stem"].strip()
    opts = q["options"]
    assert len(opts) == 5, f"Question {i} has {len(opts)} options"
    opt_lines = "\n".join(f"{letters_list[idx]}) {opt.strip()}" for idx, opt in enumerate(opts))
    expl = q["explanation"].strip()
    block = f"@@ {header}\n{stem}\n\n{opt_lines}\n// Comentário: {expl}\n"
    blocks.append(block)

out_text = "\n".join(blocks)
target_path = Path("content/questoes/ineditas/mc/direito-processual-penal.txt")
target_path.parent.mkdir(parents=True, exist_ok=True)
target_path.write_text(out_text, encoding="utf-8")
print(f"Written {len(all_qs)} questions to {target_path}")
