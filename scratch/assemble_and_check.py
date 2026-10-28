# Assembler and checker for contabilidade-geral ineditas MC
from pathlib import Path
import re
import sys

from block1 import QUESTIONS_BLOCK1
from block2 import QUESTIONS_BLOCK2
from block3 import QUESTIONS_BLOCK3
from block4 import QUESTIONS_BLOCK4
from block5 import QUESTIONS_BLOCK5

all_text = (
    QUESTIONS_BLOCK1.strip() + "\n\n" +
    QUESTIONS_BLOCK2.strip() + "\n\n" +
    QUESTIONS_BLOCK3.strip() + "\n\n" +
    QUESTIONS_BLOCK4.strip() + "\n\n" +
    QUESTIONS_BLOCK5.strip() + "\n"
)

out_path = Path("content/questoes/ineditas/mc/contabilidade-geral.txt")
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(all_text, encoding="utf-8")
print(f"Written to {out_path} ({len(all_text)} chars)")

# Quick segment count
blocks = re.split(r"(?m)^@@ ", all_text)[1:]
print(f"Total blocks: {len(blocks)}")
from collections import Counter
seg_counts = Counter()
ans_counts = Counter()
for b in blocks:
    head = b.split("\n")[0]
    seg, ans = [x.strip() for x in head.split("|")[:2]]
    seg_counts[seg] += 1
    ans_counts[ans] += 1

print("\nSegment counts:")
for s, c in sorted(seg_counts.items()):
    print(f"  {s}: {c}")

print("\nAnswer distribution:")
for a, c in sorted(ans_counts.items()):
    print(f"  {a}: {c} ({c / len(blocks) * 100:.1f}%)")
