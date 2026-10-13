import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('verify_false_items.txt', 'r', encoding='utf-8') as f:
    text = f.read()

entries = text.split('------------------------------------------------------------\n')

# Check each entry
for e in entries:
    if not e.strip(): continue
    lines = e.strip().split('\n')
    iid = lines[0]
    st = lines[1][5:]
    exp = lines[2][5:]
    
    # Specific checks:
    # 1. Look for statement asserting something standard that is actually true!
    # 2. Look for explanation failing to explain
