import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos = text.find("11. DO JULGAMENTO DA PROVA OBJETIVA")
if pos != -1:
    print(text[pos:pos+3500])
else:
    # procurar "JULGAMENTO DA PROVA OBJETIVA"
    m = re.search(r"JULGAMENTO DA PROVA OBJETIVA", text)
    if m:
        p = m.start()
        print(text[p-50:p+3500])
