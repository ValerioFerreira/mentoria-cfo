import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos10 = text.find("10. DAS ETAPAS E FASES DO CONCURSO")
pos11 = text.find("11. DAS CONDIÇÕES PARA REALIZAÇÃO")

print(text[pos10:pos11])
