import sys
sys.stdout.reconfigure(encoding="utf-8")

with open("backups/pmpe_anexo2_conteudo.txt", "r", encoding="utf-8") as f:
    text = f.read()

pos_soldado = text.find("PARA O CARGO DE SOLDADO (PRAÇA DA POLÍCIA MILITAR QPMG)")
pos_oficial = text.find("PARA O CARGO DE 2º TENETE (OFICIAL DA POLÍCIA MILITAR QOPM")
pos_medicos = text.find("CARGO DE 2° TENENTE (OFICIAL DA POLÍCIA MILITAR QOM)")

soldado_text = text[pos_soldado:pos_oficial]
oficial_text = text[pos_oficial:pos_medicos]

with open("backups/pmpe_soldado_conteudo.txt", "w", encoding="utf-8") as f:
    f.write(soldado_text)

with open("backups/pmpe_oficial_conteudo.txt", "w", encoding="utf-8") as f:
    f.write(oficial_text)

print("Soldado salvo, tamanho:", len(soldado_text))
print("Oficial salvo, tamanho:", len(oficial_text))
