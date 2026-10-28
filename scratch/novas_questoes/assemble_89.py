# Assembler for the 89 questions into scratch/novas_questoes/contabilidade-geral.txt
from pathlib import Path
import re
import sys

from block_a import BLOCK_A
from block_b import BLOCK_B
from block_c import BLOCK_C
from block_d import BLOCK_D
from block_e import BLOCK_E
from block_f import BLOCK_F

full_text = (
    BLOCK_A.strip() + "\n\n" +
    BLOCK_B.strip() + "\n\n" +
    BLOCK_C.strip() + "\n\n" +
    BLOCK_D.strip() + "\n\n" +
    BLOCK_E.strip() + "\n\n" +
    BLOCK_F.strip() + "\n"
)

out_file = Path("scratch/novas_questoes/contabilidade-geral.txt")
out_file.parent.mkdir(parents=True, exist_ok=True)
out_file.write_text(full_text, encoding="utf-8")
print(f"File successfully written to {out_file} ({len(full_text)} characters)")

# Parse and check the 89 questions
blocks = re.split(r"(?m)^@@ ", full_text)[1:]
print(f"Total blocks parsed: {len(blocks)}")

from collections import Counter
seg_counter = Counter()
ans_counter = Counter()

for b in blocks:
    head = b.split("\n")[0].strip()
    seg, ans = [x.strip() for x in head.split("|")[:2]]
    seg_counter[seg] += 1
    ans_counter[ans] += 1

print("\nQuestions per segment:")
for s, c in sorted(seg_counter.items()):
    print(f"  {s}: {c}")

print("\nAnswer distribution:")
for a, c in sorted(ans_counter.items()):
    print(f"  {a}: {c} ({c / len(blocks) * 100:.1f}%)")
