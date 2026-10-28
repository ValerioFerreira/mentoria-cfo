import json
from collections import Counter
from pathlib import Path
import sys

weak_file = Path("scratch/trechos_fracos/raciocinio-logico.json")
weak_data = json.loads(weak_file.read_text(encoding="utf-8"))

# Print first item structure
print("Sample item:", weak_data[0])

# Expected map
expected = {}
for item in weak_data:
    # item could be dict with 'trecho' or string or 'segmento'
    seg = item.get("trecho") or item.get("segmento") or item.get("seg")
    # remove prefix 'raciocinio-logico/' if present
    seg = seg.replace("raciocinio-logico/", "")
    faltam = item.get("faltam", item.get("qtd", item.get("deficit", 0)))
    expected[seg] = faltam

sys.path.insert(0, str(Path("scratch/build_rl").resolve()))
from novas_bloco1 import QUESTOES_BLOCO1
from novas_bloco2 import QUESTOES_BLOCO2
from novas_bloco3 import QUESTOES_BLOCO3
from novas_bloco4 import QUESTOES_BLOCO4

combined = QUESTOES_BLOCO1 + QUESTOES_BLOCO2 + QUESTOES_BLOCO3 + QUESTOES_BLOCO4
seg_counts = Counter(q["seg"] for q in combined)

print(f"Total weak segments required: {len(expected)}")
print(f"Total segments generated: {len(seg_counts)}")

diffs = []
total_needed = 0
for seg, needed in sorted(expected.items()):
    total_needed += needed
    gen = seg_counts.get(seg, 0)
    if gen != needed:
        diffs.append((seg, needed, gen))

print(f"Total needed across weak segments: {total_needed}")
print(f"Total generated: {len(combined)}")
if diffs:
    print("Diffs found:", diffs)
else:
    print("PERFECT MATCH: every single segment has exactly the requested number of questions!")
