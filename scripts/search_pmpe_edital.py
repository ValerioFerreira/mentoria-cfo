import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

out = []
for m in re.finditer(r"(TABELA\s+[0-9\.]+|DA PROVA OBJETIVA|ANEXO II|CONTEÚDO PROGRAMÁTICO)", text, re.IGNORECASE):
    pos = m.start()
    out.append("=== MATCH: " + m.group() + " ===")
    out.append(text[pos:pos+2500])
    out.append("-" * 60)

with open("backups/pmpe_secoes.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(out))

print("Salvo em backups/pmpe_secoes.txt")
