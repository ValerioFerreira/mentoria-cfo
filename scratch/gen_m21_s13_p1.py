# -*- coding: utf-8 -*-
import json
import re

unit_id = "CENSO-direito-administrativo_m21_a22-s13-p1"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l14133.clean.txt", "r", encoding="utf-8") as f:
    l14133 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

itens = unidade["itens"]

# We will define the 25 records
registros = []

# 1: Linha 14
registros.append({
    "linha": 14,
    "citacao": "art. 157 a 168 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "A Lei nº 14.133/2021 estruturou um rito processual robusto nos arts. 157 a 168.",
    "resultado": "OK",
    "trecho_lei": "Na aplicação da sanção prevista no inciso II do caput do art. 156 desta Lei, será facultada a defesa do interessado"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 158",
    "lei": "l14133",
    "frase_capitulo": "rito processual sancionatório e a comissão de no mínimo dois servidores estáveis (art. 158)",
    "resultado": "OK",
    "trecho_lei": "a ser conduzido por comissão composta de 2 (dois) ou mais servidores estáveis, que avaliará fatos e circunstâncias conhecidos"
})

# 3: Linha 18
registros.append({
    "linha": 18,
    "citacao": "art. 164 e art. 165",
    "lei": "l14133",
    "frase_capitulo": "disciplina da impugnação ao edital, pedidos de esclarecimento e recursos hierárquicos (arts. 164 e 165)",
    "resultado": "OK",
    "trecho_lei": "Qualquer pessoa é parte legítima para impugnar edital de licitação por irregularidade na aplicação desta Lei ou para solicitar esclarecimento"
})

# 4: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 163",
    "lei": "l14133",
    "frase_capitulo": "condições cumulativas para a reabilitação administrativa da empresa punida (art. 163)",
    "resultado": "OK",
    "trecho_lei": "É admitida a reabilitação do licitante ou contratado perante a própria autoridade que aplicou a penalidade, exigidos, cumulativamente:"
})

# 5: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 161",
    "lei": "l14133",
    "frase_capitulo": "alimentação obrigatória do PNCP e dos cadastros federais CEIS e CNEP (art. 161)",
    "resultado": "OK",
    "trecho_lei": "informar e manter atualizados os dados relativos às sanções por eles aplicadas, para fins de publicidade no Cadastro Nacional de Empresas Inidôneas e Suspensas (Ceis)"
})

# 6: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 157 e art. 158 da Lei nº 14.133/2021, art. 5º da CF",
    "lei": "cf",
    "frase_capitulo": "materializam as garantias constitucionais do art. 5º, incisos LIV e LV, da Constituição Federal.",
    "resultado": "OK",
    "trecho_lei": "LIV - ninguém será privado da liberdade ou de seus bens sem o devido processo legal;"
})

# 7: Linha 28
registros.append({
    "linha": 28,
    "citacao": "art. 157",
    "lei": "l14133",
    "frase_capitulo": "Para a multa: o rito é simplificado, com prazo de defesa de 15 (quinze) dias úteis contado da intimação (art. 157).",
    "resultado": "OK",
    "trecho_lei": "será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação."
})

# 8: Linha 29
registros.append({
    "linha": 29,
    "citacao": "art. 158",
    "lei": "l14133",
    "frase_capitulo": "exige-se processo administrativo formal conduzido por comissão especial de servidores estáveis (art. 158).",
    "resultado": "OK",
    "trecho_lei": "requererá a instauração de processo de responsabilização, a ser conduzido por comissão composta de 2 (dois) ou mais servidores estáveis"
})

# 9: Linha 48
registros.append({
    "linha": 48,
    "citacao": "Lei nº 14.133/2021 e Lei nº 8.666/1993",
    "lei": "l14133",
    "frase_capitulo": "A Lei nº 14.133/2021 unificou o prazo de manifestação defensiva do interessado.",
    "resultado": "OK",
    "trecho_lei": "intimará o licitante ou o contratado para, no prazo de 15 (quinze) dias úteis, contado da data de intimação, apresentar defesa escrita"
})

# 10: Linha 54
registros.append({
    "linha": 54,
    "citacao": "art. 157",
    "lei": "l14133",
    "frase_capitulo": "| **Multa (art. 157)** | **15 dias úteis** contados da intimação oficial | Autoridade administrativa fiscalizadora ou gestora |",
    "resultado": "OK",
    "trecho_lei": "Art. 157. Na aplicação da sanção prevista no inciso II do caput do art. 156 desta Lei"
})

# 11: Linha 55
registros.append({
    "linha": 55,
    "citacao": "art. 158",
    "lei": "l14133",
    "frase_capitulo": "| **Impedimento ou Inidoneidade (art. 158)** | **15 dias úteis** contados da intimação formal | Comissão processante com 2 ou mais servidores estáveis |",
    "resultado": "OK",
    "trecho_lei": "Art. 158. A aplicação das sanções previstas nos incisos III e IV do caput do art. 156 desta Lei"
})

# 12: Linha 57
registros.append({
    "linha": 57,
    "citacao": "Lei nº 14.133/2021, art. 157",
    "lei": "l14133",
    "frase_capitulo": "> [!lei] Lei 14.133/2021, art. 157",
    "resultado": "OK",
    "trecho_lei": "sanção prevista no inciso II do caput do art. 156 desta Lei, será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis"
})

# 13: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 156 e art. 157",
    "lei": "l14133",
    "frase_capitulo": "> Art. 157. Na aplicação da sanção prevista no inciso II do caput do art. 156 desta Lei, será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação.",
    "resultado": "OK",
    "trecho_lei": "prevista no inciso II do caput do art. 156 desta Lei, será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis, contado da data de sua intimação."
})

# 14: Linha 62
registros.append({
    "linha": 62,
    "citacao": "art. 158 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "O art. 158 da Lei nº 14.133/2021 impõe a obrigatoriedade de atuação colegiada.",
    "resultado": "OK",
    "trecho_lei": "processo de responsabilização, a ser conduzido por comissão composta de 2 (dois) ou mais servidores estáveis"
})

# 15: Linha 72
registros.append({
    "linha": 72,
    "citacao": "art. 158",
    "lei": "l14133",
    "frase_capitulo": "servidores temporários, terceirizados ou ocupantes exclusivamente de cargos em comissão **não podem** integrar a comissão processante sancionatória do art. 158.",
    "resultado": "OK",
    "trecho_lei": "Em órgão ou entidade da Administração Pública cujo quadro funcional não seja formado de servidores estatutários, a comissão a que se refere o caput deste artigo será composta de 2 (dois) ou mais empregados públicos pertencentes aos seus quadros permanentes"
})

# 16: Linha 80
registros.append({
    "linha": 80,
    "citacao": "art. 158, § 2º",
    "lei": "l14133",
    "frase_capitulo": "Contudo, ela pode indeferir fundamentadamente os requerimentos de prova ilícitos, impertinentes, desnecessários ou manifestamente protelatórios (art. 158, § 2º).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O parágrafo que autoriza o indeferimento fundamentado de provas ilícitas, impertinentes, desnecessárias ou protelatórias é o § 3º do art. 158, e não o § 2º (que trata do prazo de 15 dias úteis para alegações finais após deferimento probatório).",
    "texto_novo": "Contudo, ela pode indeferir fundamentadamente os requerimentos de prova ilícitos, impertinentes, desnecessários ou manifestamente protelatórios (art. 158, § 3º).",
    "trecho_lei": "Serão indeferidas pela comissão, mediante decisão fundamentada, provas ilícitas, impertinentes, desnecessárias, protelatórias ou intempestivas."
})

# 17: Linha 90
registros.append({
    "linha": 90,
    "citacao": "art. 158, § 1º",
    "lei": "l14133",
    "frase_capitulo": "A assessoria jurídica emite parecer técnico conclusivo sobre a legalidade do procedimento e a proporcionalidade da sanção antes do encaminhamento final ao Secretário ou Ministro de Estado (art. 158, § 1º).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "A obrigatoriedade de análise jurídica prévia e a competência decisória exclusiva de Ministro de Estado ou Secretário para a declaração de inidoneidade constam do art. 156, § 6º, I da Lei nº 14.133/2021, e não do art. 158, § 1º (que trata apenas de empregados públicos na comissão).",
    "texto_novo": "A assessoria jurídica emite parecer técnico conclusivo sobre a legalidade do procedimento e a proporcionalidade da sanção antes do encaminhamento final ao Secretário ou Ministro de Estado (art. 156, § 6º, I).",
    "trecho_lei": "A sanção estabelecida no inciso IV do caput deste artigo será precedida de análise jurídica e observará as seguintes regras:"
})

# 18: Linha 94
registros.append({
    "linha": 94,
    "citacao": "art. 164 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "O art. 164 da Lei nº 14.133/2021 disciplina esse direito republicano.",
    "resultado": "OK",
    "trecho_lei": "Art. 164. Qualquer pessoa é parte legítima para impugnar edital de licitação por irregularidade na aplicação desta Lei ou para solicitar esclarecimento sobre os seus termos"
})

# 19: Linha 106
registros.append({
    "linha": 106,
    "citacao": "art. 164",
    "lei": "l14133",
    "frase_capitulo": "| **Impugnação ao Edital (art. 164)** | Até **3 (três) dias úteis** antes da abertura do certame | Até **3 (três) dias úteis**, devendo a resposta anteceder a data de início da sessão |",
    "resultado": "OK",
    "trecho_lei": "devendo protocolar o pedido até 3 (três) dias úteis antes da data de abertura do certame."
})

# 20: Linha 107
registros.append({
    "linha": 107,
    "citacao": "art. 164",
    "lei": "l14133",
    "frase_capitulo": "| **Pedido de Esclarecimento (art. 164)** | Até **3 (três) dias úteis** antes da abertura da sessão | Até **3 (três) dias úteis**, divulgado em sítio eletrônico oficial |",
    "resultado": "OK",
    "trecho_lei": "A resposta à impugnação ou ao pedido de esclarecimento será divulgada em sítio eletrônico oficial no prazo de até 3 (três) dias úteis"
})

# 21: Linha 116
registros.append({
    "linha": 116,
    "citacao": "art. 165 a 168 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "Os arts. 165 a 168 estabelecem as hipóteses de cabimento, os prazos de tramitação e os efeitos das impugnações recursais.",
    "resultado": "OK",
    "trecho_lei": "Art. 165. Dos atos da Administração decorrentes da aplicação desta Lei cabem:"
})

# 22: Linha 127
registros.append({
    "linha": 127,
    "citacao": "art. 165, inciso I",
    "lei": "l14133",
    "frase_capitulo": "O prazo para interpor recurso contra esses atos é de **3 (três) dias úteis**, contados da data de intimação pessoal ou de divulgação formal da ata da sessão pública (art. 165, inciso I).",
    "resultado": "OK",
    "trecho_lei": "I - recurso, no prazo de 3 (três) dias úteis, contado da data de intimação ou de lavratura da ata, em face de:"
})

# 23: Linha 150
registros.append({
    "linha": 150,
    "citacao": "Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "os recursos contra o julgamento de propostas e contra os atos de habilitação ou inabilitação serão apreciados em **fase recursal única** ao término do procedimento.",
    "resultado": "OK",
    "trecho_lei": "II - a apreciação dar-se-á em fase única."
})

# 24: Linha 155
registros.append({
    "linha": 155,
    "citacao": "art. 165, § 1º, I",
    "lei": "l14133",
    "frase_capitulo": "- Contra as sanções de **advertência, multa ou impedimento de licitar**: cabe recurso hierárquico no prazo de **15 (quinze) dias úteis** contados da intimação oficial (art. 165, § 1º, I).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O cabimento de recurso hierárquico no prazo de 15 dias úteis contra advertência, multa ou impedimento de licitar é disciplinado expressamente pelo art. 166 da Lei nº 14.133/2021, e não pelo art. 165, § 1º, I (que trata da manifestação imediata contra julgamento/habilitação).",
    "texto_novo": "- Contra as sanções de **advertência, multa ou impedimento de licitar**: cabe recurso hierárquico no prazo de **15 (quinze) dias úteis** contados da intimação oficial (art. 166).",
    "trecho_lei": "Da aplicação das sanções previstas nos incisos I, II e III do caput do art. 156 desta Lei caberá recurso no prazo de 15 (quinze) dias úteis, contado da data da intimação."
})

# 25: Linha 156
registros.append({
    "linha": 156,
    "citacao": "art. 165, § 1º, II",
    "lei": "l14133",
    "frase_capitulo": "- Contra a **declaração de inidoneidade**: cabe **pedido de reconsideração** à própria autoridade ministerial ou secretarial prolatora da decisão, no prazo de **15 (quinze) dias úteis** (art. 165, § 1º, II).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O cabimento de pedido de reconsideração no prazo de 15 dias úteis contra a sanção de declaração de inidoneidade é previsto pelo art. 167 da Lei nº 14.133/2021, e não pelo art. 165, § 1º, II (que estabelece a apreciação em fase recursal única).",
    "texto_novo": "- Contra a **declaração de inidoneidade**: cabe **pedido de reconsideração** à própria autoridade ministerial ou secretarial prolatora da decisão, no prazo de **15 (quinze) dias úteis** (art. 167).",
    "trecho_lei": "Da aplicação da sanção prevista no inciso IV do caput do art. 156 desta Lei caberá apenas pedido de reconsideração, que deverá ser apresentado no prazo de 15 (quinze) dias úteis, contado da data da intimação"
})

output_data = {
    "unidade": unit_id,
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": registros
}

# Verifications
errors = []
trechos_vistos = set()
for idx, r in enumerate(registros):
    fc = r["frase_capitulo"]
    if fc not in chapter_content:
        errors.append(f"Row {idx+1} (linha {r['linha']}): frase_capitulo not in chapter!")
    elif r["resultado"] == "ERRO" and chapter_content.count(fc) != 1:
        errors.append(f"Row {idx+1} (linha {r['linha']}): frase_capitulo appears {chapter_content.count(fc)} times (must be 1)!")

    tl = r["trecho_lei"]
    if len(tl) < 25:
        errors.append(f"Row {idx+1}: trecho_lei too short ({len(tl)} chars)")
    if tl in trechos_vistos:
        errors.append(f"Row {idx+1}: duplicate trecho_lei: '{tl[:30]}...'")
    trechos_vistos.add(tl)

    law_txt = cf if r["lei"] == "cf" else l14133
    if tl not in law_txt:
        errors.append(f"Row {idx+1}: trecho_lei not in {r['lei']}: '{tl}'")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  -", e)
else:
    print(f"All {len(registros)} rows verified locally! Writing draft...")
    with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, ensure_ascii=False, indent=1)
    print("Draft saved.")
