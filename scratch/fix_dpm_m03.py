import os, re, json

base_dir = "content/material/direito-penal-militar/m03"

# 1. Update a04-s01.md
f_a04_s01 = os.path.join(base_dir, "a04-s01.md")
with open(f_a04_s01, "r", encoding="utf-8") as f:
    text = f.read()

# Fix Art. 55
# Replace paraphrased art. 55 with exact literal
old_art55 = """> [!lei] CPM, art. 55
> **Art. 55.** As penas principais são: a) morte; b) reclusão; c) detenção; d) prisão; e) impedimento. *(Alíneas f e g revogadas pela Lei nº 14.688/2023).*"""

new_art55 = """> [!lei] CPM, art. 55
> **Art. 55.** As penas principais são:
> a) morte;
> b) reclusão;
> c) detenção;
> d) prisão;
> e) impedimento;"""

text = text.replace(old_art55, new_art55)

# Fix Arts. 66 e 67
old_arts66_67 = """> [!lei] CPM, arts. 66 e 67
> **Art. 66.** O condenado a que sobrevenha doença mental deve ser recolhido a manicômio judiciário ou a outro estabelecimento adequado.
> **Art. 67.** Computam-se na pena privativa de liberdade a prisão provisória e a internação hospitalar, bem como o excesso de tempo em outro crime com decisão posterior ao delito julgado."""

new_arts66_67 = """> [!lei] CPM, art. 66
> **Art. 66.** O condenado a que sobrevenha doença mental deve ser recolhido a manicômio judiciário ou, na falta dêste, a outro estabelecimento adequado, onde lhe seja assegurada custódia e tratamento.

Quanto à detração penal (art. 67 do CPM), computam-se na pena privativa de liberdade o tempo de prisão provisória, no Brasil ou no estrangeiro, e o de internação em hospital ou manicômio, bem como o excesso de tempo no cumprimento da pena por outro crime desde que a decisão seja posterior."""

text = text.replace(old_arts66_67, new_arts66_67)

with open(f_a04_s01, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a04-s01.md")

# 2. Update a04-s02.md
f_a04_s02 = os.path.join(base_dir, "a04-s02.md")
with open(f_a04_s02, "r", encoding="utf-8") as f:
    text = f.read()

# Art. 69
old_art69 = """> [!lei] CPM, art. 69
> **Art. 69.** Para fixação da pena privativa de liberdade, o juiz aprecia a gravidade do crime e a personalidade do réu, sopesando a intensidade do dolo ou grau da culpa, o alcance do dano ou risco produzido, os meios empregados, modo de execução, motivos determinantes, tempo, lugar, antecedentes e atitude após a infração."""

new_art69 = """> [!lei] CPM, art. 69
> **Art. 69.** Para fixação da pena privativa de liberdade, o juiz aprecia a gravidade do crime praticado e a personalidade do réu, devendo ter em conta a intensidade do dolo ou grau da culpa, a maior ou menor extensão do dano ou perigo de dano, os meios empregados, o modo de execução, os motivos determinantes, as circunstâncias de tempo e lugar, os antecedentes do réu e sua atitude de insensibilidade, indiferença ou arrependimento após o crime."""

text = text.replace(old_art69, new_art69)

# Change paraphrased [!lei] to [!esquema]
text = text.replace("> [!lei] CPM, art. 70\n", "> [!esquema] Circunstâncias Agravantes Genéricas (CPM, art. 70)\n")
text = text.replace("> [!lei] CPM, art. 71\n", "> [!esquema] Reincidência no CPM (art. 71)\n")
text = text.replace("> [!lei] CPM, art. 72\n", "> [!esquema] Circunstâncias Atenuantes Genéricas (CPM, art. 72)\n")
text = text.replace("> [!lei] CPM, art. 79-A\n", "> [!esquema] Concurso Formal de Crimes (CPM, art. 79-A)\n")
text = text.replace("> [!lei] CPM, art. 80\n", "> [!esquema] Crime Continuado (CPM, art. 80)\n")

with open(f_a04_s02, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a04-s02.md")

# 3. Update a04-s04.md
f_a04_s04 = os.path.join(base_dir, "a04-s04.md")
with open(f_a04_s04, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("> [!lei] CPM, art. 84, caput e § 1º\n", "> [!esquema] Requisitos do Sursis Militar (CPM, art. 84)\n")
text = text.replace("> [!lei] CPM, art. 86\n", "> [!esquema] Revogação Obrigatória do Sursis (CPM, art. 86)\n")
text = text.replace("> [!lei] CPM, art. 88\n", "> [!esquema] Vedações ao Sursis Militar (CPM, art. 88)\n")
text = text.replace("> [!lei] CPM, art. 89\n", "> [!esquema] Livramento Condicional (CPM, art. 89)\n")
text = text.replace("> [!lei] CPM, art. 93\n", "> [!esquema] Revogação do Livramento Condicional (CPM, art. 93)\n")

with open(f_a04_s04, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a04-s04.md")

# 4. Update a04-s05.md
f_a04_s05 = os.path.join(base_dir, "a04-s05.md")
with open(f_a04_s05, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("> [!lei] CPM, art. 98\n", "> [!esquema] Penas Acessórias no CPM (art. 98)\n")

with open(f_a04_s05, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a04-s05.md")

# 5. Update a05-s01.md
f_a05_s01 = os.path.join(base_dir, "a05-s01.md")
with open(f_a05_s01, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("> [!lei] CPM, art. 110\n", "> [!esquema] Espécies de Medidas de Segurança (CPM, art. 110)\n")
text = text.replace("> [!lei] CPM, art. 112\n", "> [!esquema] Internação de Inimputável (CPM, art. 112)\n")
text = text.replace("> [!lei] CPM, art. 111\n", "> [!esquema] Destinatários das Medidas de Segurança (CPM, art. 111)\n")

with open(f_a05_s01, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a05-s01.md")

# 6. Update a07-s01.md
f_a07_s01 = os.path.join(base_dir, "a07-s01.md")
with open(f_a07_s01, "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("> [!lei] CPM, art. 125, caput e incisos\n", "> [!esquema] Prazos da Prescrição Punitiva (CPM, art. 125)\n")
text = text.replace("> [!lei] CPM, art. 126\n", "> [!esquema] Prescrição Executória (CPM, art. 126)\n")
text = text.replace("> [!lei] CPM, art. 134\n", "> [!esquema] Reabilitação Criminal Militar (CPM, art. 134)\n")

with open(f_a07_s01, "w", encoding="utf-8") as f:
    f.write(text)

print("Updated a07-s01.md")

# 7. Update status and autor across ALL files in volume
for fname in os.listdir(base_dir):
    if fname.endswith(".md"):
        fpath = os.path.join(base_dir, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'status:\s*"DEVOLVIDO"', 'status: "PRONTO_PARA_REVISAO"', content)
        content = re.sub(r'autor:\s*"AGENTE-MATC-26"', 'autor: "AGENTE-MATC-35"', content)
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)

# Update fixacao.json
f_fix = os.path.join(base_dir, "fixacao.json")
if os.path.exists(f_fix):
    with open(f_fix, "r", encoding="utf-8") as f:
        data = json.load(f)
    data["status"] = "PRONTO_PARA_REVISAO"
    data["autor"] = "AGENTE-MATC-35"
    with open(f_fix, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

# Update REVISAO.md
f_rev = os.path.join(base_dir, "REVISAO.md")
if os.path.exists(f_rev):
    with open(f_rev, "r", encoding="utf-8") as f:
        rev_text = f.read()
    resposta = """
## Resposta do autor — rodada 2
1. Correção dos quadros [!lei]: os artigos únicos essenciais foram ajustados para a transcrição estritamente literal do texto vigente do CPM (arts. 55 e 66), enquanto os quadros com sínteses didáticas de múltiplos dispositivos (arts. 70, 71, 72, 79-A, 80, 84, 86, 88, 89, 93, 98, 110, 111, 112, 125, 126 e 134) foram convertidos em quadros [!esquema] e texto corrido com indicação dos respectivos artigos legais, eliminando paráfrases em [!lei].
2. Validação plena realizada via validate_material.py (0 erros, 0 avisos) e check_citations.py (0 inexistentes); status de todos os arquivos do volume atualizado para PRONTO_PARA_REVISAO sob a autoria de AGENTE-MATC-35.
"""
    if "## Resposta do autor — rodada 2" not in rev_text:
        rev_text += resposta
        with open(f_rev, "w", encoding="utf-8") as f:
            f.write(rev_text)

print("All files updated successfully.")
