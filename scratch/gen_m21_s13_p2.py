# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m21_a22-s13-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l14133.clean.txt", "r", encoding="utf-8") as f:
    l14133 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 162
registros.append({
    "linha": 162,
    "citacao": "art. 166",
    "lei": "l14133",
    "frase_capitulo": "- Se mantiver a decisão atacada: encaminhará os autos recursais acompanhados de sua justificativa fundamentada à autoridade superior competente, que deverá proferir decisão final no prazo de **10 (dez) dias úteis** (art. 166).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O prazo de retratação de 3 dias úteis e de decisão recursal final em 10 dias úteis refere-se ao art. 165, § 2º, e não ao art. 166 (cujo parágrafo único fixa 5 dias para retratação e 20 dias para decisão final da autoridade superior).",
    "texto_novo": "- Se mantiver a decisão atacada: encaminhará os autos recursais acompanhados de sua justificativa fundamentada à autoridade superior competente, que deverá proferir decisão final no prazo de **10 (dez) dias úteis** (art. 165, § 2º).",
    "trecho_lei": "se não reconsiderar o ato ou a decisão no prazo de 3 (três) dias úteis, encaminhará o recurso com a sua motivação à autoridade superior, a qual deverá proferir sua decisão no prazo máximo de 10 (dez) dias úteis"
})

# 2: Linha 166
registros.append({
    "linha": 166,
    "citacao": "art. 158, § 4º da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "regime de prescrição da pretensão punitiva no art. 158, § 4º.",
    "resultado": "OK",
    "trecho_lei": "§ 4º A prescrição ocorrerá em 5 (cinco) anos, contados da ciência da infração pela Administração, e será:"
})

# 3: Linha 194
registros.append({
    "linha": 194,
    "citacao": "Lei nº 12.846/2013 no art. 158, § 4º, II da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "| **Suspensão** | Celebração de acordo de leniência (Lei nº 12.846/2013) |",
    "resultado": "OK",
    "trecho_lei": "II - suspensa pela celebração de acordo de leniência previsto na Lei nº 12.846, de 1º de agosto de 2013;"
})

# 4: Linha 203
registros.append({
    "linha": 203,
    "citacao": "art. 163 da Lei nº 14.133/2021, art. 5º da CF",
    "lei": "cf",
    "frase_capitulo": "O art. 5º, inciso XLVII, \"b\", da Constituição Federal veda expressamente penalidades de caráter perpétuo",
    "resultado": "OK",
    "trecho_lei": "XLVII - não haverá penas: \n a) de morte, salvo em caso de guerra declarada, nos termos do art. 84, XIX; \n b) de caráter perpétuo;"
})

# 5: Linha 223
registros.append({
    "linha": 223,
    "citacao": "art. 163",
    "lei": "l14133",
    "frase_capitulo": "Para obter a reabilitação, o interessado deve comprovar cumulativamente o preenchimento de todas as exigências legais postas no art. 163:",
    "resultado": "OK",
    "trecho_lei": "Art. 163. É admitida a reabilitação do licitante ou contratado perante a própria autoridade que aplicou a penalidade, exigidos, cumulativamente:"
})

# 6: Linha 225
registros.append({
    "linha": 225,
    "citacao": "art. 163",
    "lei": "l14133",
    "frase_capitulo": "| Requisito Legal | Conteúdo do Requisito no Art. 163 | Justificativa de Proteção Pública |",
    "resultado": "OK",
    "trecho_lei": "I - reparação integral do dano causado à Administração Pública;"
})

# 7: Linha 241
registros.append({
    "linha": 241,
    "citacao": "Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "Para que as sanções produzam eficácia real e impeçam contratações fraudulentas por outros órgãos públicos, a Lei nº 14.133/2021 instituiu um sistema de transparência nacional unificado.",
    "resultado": "OK",
    "trecho_lei": "I - divulgação centralizada e obrigatória dos atos exigidos por esta Lei;"
})

# 8: Linha 243
registros.append({
    "linha": 243,
    "citacao": "art. 161",
    "lei": "l14133",
    "frase_capitulo": "O prazo legal para alimentar os cadastros é de **15 (quinze) dias úteis**, contados da data em que a sanção foi cominada.",
    "resultado": "OK",
    "trecho_lei": "deverão, no prazo máximo 15 (quinze) dias úteis, contado da data de aplicação da sanção, informar e manter atualizados os dados relativos às sanções por eles aplicadas"
})

# 9: Linha 249
registros.append({
    "linha": 249,
    "citacao": "art. 174",
    "lei": "l14133",
    "frase_capitulo": "| **PNCP (art. 174)** | Comitê Gestor do PNCP | Registro público centralizado de todas as sanções licitatórias do Brasil.",
    "resultado": "OK",
    "trecho_lei": "Art. 174. É criado o Portal Nacional de Contratações Públicas (PNCP), sítio eletrônico oficial destinado à:"
})

# 10: Linha 250
registros.append({
    "linha": 250,
    "citacao": "art. 161",
    "lei": "l14133",
    "frase_capitulo": "| **CEIS (art. 161)** | Controladoria-Geral da União (CGU) | Cadastro Nacional de Empresas Inidôneas e Suspensas da Administração Pública.",
    "resultado": "OK",
    "trecho_lei": "publicidade no Cadastro Nacional de Empresas Inidôneas e Suspensas (Ceis)"
})

# 11: Linha 251
registros.append({
    "linha": 251,
    "citacao": "art. 161 e Lei nº 12.846/2013",
    "lei": "l14133",
    "frase_capitulo": "| **CNEP (art. 161)** | Controladoria-Geral da União (CGU) | Cadastro Nacional de Empresas Punidas com suporte na Lei Anticorrupção (Lei nº 12.846/2013).",
    "resultado": "OK",
    "trecho_lei": "no Cadastro Nacional de Empresas Punidas (Cnep), instituídos no âmbito do Poder Executivo federal."
})

# 12: Linha 260
registros.append({
    "linha": 260,
    "citacao": "art. 163 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "ela não cumpriu dois requisitos cumulativos indispensáveis previstos no art. 163 da Lei nº 14.133/2021:",
    "resultado": "OK",
    "trecho_lei": "IV - cumprimento das condições de reabilitação definidas no ato punitivo;"
})

# 13: Linha 261
registros.append({
    "linha": 261,
    "citacao": "art. 163",
    "lei": "l14133",
    "frase_capitulo": "> 1. Não decorreu o **prazo mínimo de 3 (três) anos** exigido expressamente para a reabilitação de inidoneidade (art. 163, parágrafo único, inciso II). Passaram-se apenas dois anos da condenação.",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O prazo mínimo de 3 anos de aplicação da penalidade para a reabilitação na inidoneidade consta do art. 163, inciso III, inexistindo inciso II no parágrafo único daquele artigo.",
    "texto_novo": "> 1. Não decorreu o **prazo mínimo de 3 (três) anos** exigido expressamente para a reabilitação de inidoneidade (art. 163, inciso III). Passaram-se apenas dois anos da condenação.",
    "trecho_lei": "transcurso do prazo mínimo de 1 (um) ano da aplicação da penalidade, no caso de impedimento de licitar e contratar, ou de 3 (três) anos da aplicação da penalidade"
})

# 14: Linha 262
registros.append({
    "linha": 262,
    "citacao": "art. 155",
    "lei": "l14133",
    "frase_capitulo": "> 2. Por se tratar de infração gravíssima de fraude e conluio (art. 155, incisos VIII e IX), a lei impõe como condição obrigatória cumulativa a **implantação ou o aperfeiçoamento de programa de integridade** (*compliance*), o qual sequer foi comprovado pela peticionária.",
    "resultado": "OK",
    "trecho_lei": "VIII - apresentar declaração ou documentação falsa exigida para o certame ou prestar declaração falsa durante a licitação ou a execução do contrato;"
})

# 15: Linha 268
registros.append({
    "linha": 268,
    "citacao": "Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "| Etapa do Procedimento | Regra Legal Específica | Dispositivo na Lei nº 14.133/2021 |",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO II DAS IMPUGNAÇÕES, DOS PEDIDOS DE ESCLARECIMENTO E DOS RECURSOS"
})

# 16: Linha 270
registros.append({
    "linha": 270,
    "citacao": "art. 157 e art. 158",
    "lei": "l14133",
    "frase_capitulo": "| **Defesa Prévia** | Prazo de **15 dias úteis** contados da intimação, na multa e nas sanções de impedimento e inidoneidade. | Arts. 157 e 158 |",
    "resultado": "OK",
    "trecho_lei": "Na aplicação da sanção prevista no inciso II do caput do art. 156 desta Lei, será facultada a defesa do interessado no prazo de 15 (quinze) dias úteis"
})

# 17: Linha 271
registros.append({
    "linha": 271,
    "citacao": "art. 158, caput",
    "lei": "l14133",
    "frase_capitulo": "| **Comissão Processante** | Obrigatória para impedimento e inidoneidade: mínimo de **2 servidores estáveis** ou empregados permanentes. | Art. 158, caput |",
    "resultado": "OK",
    "trecho_lei": "a ser conduzido por comissão composta de 2 (dois) ou mais servidores estáveis"
})

# 18: Linha 272
registros.append({
    "linha": 272,
    "citacao": "art. 158, § 2º",
    "lei": "l14133",
    "frase_capitulo": "| **Instrução e Provas** | Indeferimento motivado de provas protelatórias; alegações finais em **15 dias úteis**. | Art. 158, § 2º |",
    "resultado": "OK",
    "trecho_lei": "Na hipótese de deferimento de pedido de produção de novas provas ou de juntada de provas julgadas indispensáveis pela comissão, o licitante ou o contratado poderá apresentar alegações finais no prazo de 15 (quinze) dias úteis"
})

# 19: Linha 273
registros.append({
    "linha": 273,
    "citacao": "art. 158, § 1º",
    "lei": "l14133",
    "frase_capitulo": "| **Parecer Jurídico** | Obrigatório antes da decisão final em processos de declaração de inidoneidade. | Art. 158, § 1º |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "A exigência de que a declaração de inidoneidade seja precedida de análise jurídica consta expressamente do art. 156, § 6º, e não do art. 158, § 1º (que cuida da composição da comissão processante por empregados públicos).",
    "texto_novo": "| **Parecer Jurídico** | Obrigatório antes da decisão final em processos de declaração de inidoneidade. | Art. 156, § 6º |",
    "trecho_lei": "§ 6º A sanção estabelecida no inciso IV do caput deste artigo será precedida de análise jurídica e observará as seguintes regras:"
})

# 20: Linha 274
registros.append({
    "linha": 274,
    "citacao": "art. 164",
    "lei": "l14133",
    "frase_capitulo": "| **Impugnação ao Edital** | Até **3 dias úteis** antes da abertura; resposta em até **3 dias úteis** antes da sessão. | Art. 164 |",
    "resultado": "OK",
    "trecho_lei": "devendo protocolar o pedido até 3 (três) dias úteis antes da data de abertura do certame."
})

# 21: Linha 275
registros.append({
    "linha": 275,
    "citacao": "art. 165, I",
    "lei": "l14133",
    "frase_capitulo": "| **Recursos Licitatórios** | Prazo de **3 dias úteis** com manifestação imediata da intenção de recorrer em sessão. | Art. 165, I |",
    "resultado": "OK",
    "trecho_lei": "I - a intenção de recorrer deverá ser manifestada imediatamente, sob pena de preclusão"
})

# 22: Linha 276
registros.append({
    "linha": 276,
    "citacao": "art. 158, § 4º",
    "lei": "l14133",
    "frase_capitulo": "| **Prescrição da Pretensão** | **5 anos** da ciência da infração; interrompe-se com a instauração e o julgamento. | Art. 158, § 4º |",
    "resultado": "OK",
    "trecho_lei": "I - interrompida pela instauração do processo de responsabilização a que se refere o caput deste artigo;"
})

# 23: Linha 277
registros.append({
    "linha": 277,
    "citacao": "art. 163, parágrafo único",
    "lei": "l14133",
    "frase_capitulo": "| **Reabilitação: Prazos** | Requerimento após **1 ano** (impedimento) ou **3 anos** (inidoneidade). | Art. 163, parágrafo único |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "Os prazos de 1 ano para impedimento e 3 anos para inidoneidade estão previstos no art. 163, inciso III, e não no seu parágrafo único (que disciplina a implantação de programa de integridade).",
    "texto_novo": "| **Reabilitação: Prazos** | Requerimento após **1 ano** (impedimento) ou **3 anos** (inidoneidade). | Art. 163, inciso III |",
    "trecho_lei": "ou de 3 (três) anos da aplicação da penalidade, no caso de declaração de inidoneidade;"
})

# 24: Linha 278
registros.append({
    "linha": 278,
    "citacao": "art. 161",
    "lei": "l14133",
    "frase_capitulo": "| **Alimentação dos Cadastros** | Prazo de **15 dias úteis** para inclusão da sanção no PNCP, CEIS e CNEP. | Art. 161 |",
    "resultado": "OK",
    "trecho_lei": "Art. 161. Os órgãos e entidades dos Poderes Executivo, Legislativo e Judiciário de todos os entes federativos deverão"
})

# 25: Linha 286
registros.append({
    "linha": 286,
    "citacao": "art. 164",
    "lei": "l14133",
    "frase_capitulo": "- A impugnação ao edital e os pedidos de esclarecimento devem ser protocolados até três dias úteis antes da abertura da sessão pública (art. 164).",
    "resultado": "OK",
    "trecho_lei": "Qualquer pessoa é parte legítima para impugnar edital de licitação por irregularidade na aplicação desta Lei"
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
