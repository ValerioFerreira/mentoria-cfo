import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('calc_items.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('------------------------------------------------------------\n')
print(f"Total entries: {len(entries)-1}")

# We will analyze every entry to verify mathematical correctness
# Let's inspect them in slices
for idx, e in enumerate(entries[:50]):
    if not e.strip(): continue
    lines = e.strip().split('\n')
    header = lines[0] # [C/E] ID
    st = lines[1][5:]
    exp = lines[2][5:]
    # verify
