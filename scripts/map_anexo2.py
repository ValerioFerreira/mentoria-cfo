import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_anexo2_conteudo.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Procurar cabeçalhos de cargos e disciplinas
for m in re.finditer(r"(CARGO[^\n]+|PARA O CARGO[^\n]+|[A-ZÂÁÉÍÓÚ\s]{4,30}:)", text):
    line = m.group(0).strip()
    if len(line) > 3 and not line.isdigit():
        print(line)
