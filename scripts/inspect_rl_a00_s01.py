import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('content/items/raciocinio-logico/a00.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

seg0 = d['segments'][0]
print("Summary for raciocinio-logico/a00/s01:")
print(seg0['bizu']['summary'])
print("\nTeoria:")
for i, it in enumerate(seg0['bizu']['teoria']):
    ans = 'C' if it['isTrue'] else 'E'
    print(f"#{i} [{ans}]: {it['statement']}")
    print(f"    Exp: {it['explanation']}")
print("\nRevisao:")
for i, it in enumerate(seg0['bizu']['revisao']):
    ans = 'C' if it['isTrue'] else 'E'
    print(f"#{i} [{ans}]: {it['statement']}")
    print(f"    Exp: {it['explanation']}")
