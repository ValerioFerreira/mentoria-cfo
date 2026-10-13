import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_edital_texto.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos_anexo2 = text.find("ANEXO II")
pos_anexo3 = text.find("ANEXO III")
if pos_anexo3 == -1:
    pos_anexo3 = len(text)

anexo2_text = text[pos_anexo2:pos_anexo3]

with open("backups/pmpe_anexo2_conteudo.txt", "w", encoding="utf-8") as f:
    f.write(anexo2_text)

print("Anexo II salvo em backups/pmpe_anexo2_conteudo.txt, tamanho:", len(anexo2_text))
