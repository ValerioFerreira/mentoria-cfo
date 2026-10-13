import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

matches = re.finditer(r"\n(1[0-3]\.\s+[A-ZÀ-Ú\s]+)", text)
for m in matches:
    print(m.group(1))
    pos = m.start()
    print(text[pos:pos+500])
    print("-" * 50)
