import sys
import re

sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

out = []

# Procurar tabelas com disciplinas da prova objetiva
matches = re.finditer(r"(TABELA\s+[0-9\.]+[^\n]*\n(?:[^\n]+\n){1,40})", text, re.IGNORECASE)
for m in matches:
    out.append("--- TABELA ENCONTRADA ---")
    out.append(m.group(1))

# Procurar todas as ocorrências de ANEXO II
for m in re.finditer(r"ANEXO II", text):
    pos = m.start()
    out.append("=== OCORRÊNCIA ANEXO II ===")
    out.append(text[pos:pos+4000])

with open("backups/pmpe_tabelas_anexo2.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(out))

print("Salvo em backups/pmpe_tabelas_anexo2.txt")
