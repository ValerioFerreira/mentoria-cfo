import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Procurar critérios de aprovação/eliminação da prova objetiva
# Geralmente no item 10 ou 11
pos = text.find("DO JULGAMENTO DA PROVA OBJETIVA")
if pos == -1:
    pos = text.find("DA PROVA OBJETIVA")
for m in re.finditer(r"(será eliminado|critério de corte|pontuação mínima|não poderá zerar|30%|elimina[çc][ãa]o)", text, re.IGNORECASE):
    p = m.start()
    print("MATCH:", text[p-100:p+300])
    print("=" * 60)
