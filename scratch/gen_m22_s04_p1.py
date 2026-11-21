# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s04-p1"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 14
registros.append({
    "linha": 14,
    "citacao": "art. 10 e art. 11 da Lei 8.429/1992, com redação da Lei 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "O capítulo anterior trouxe o enriquecimento ilícito e as bases do art. 10. Aqui o estudo se completa. Primeiro, os demais incisos do art. 10, que reúnem condutas de gestão de dinheiro público",
    "resultado": "OK",
    "trecho_lei": "Seção III Dos Atos de Improbidade Administrativa que Atentam Contra os Princípios da Administração Pública"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Reconhecer as condutas do art. 10 que a reforma alterou ou acrescentou.",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa"
})

# 3: Linha 18
registros.append({
    "linha": 18,
    "citacao": "art. 10, § 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Aplicar a exigência de dano efetivo e a regra do art. 10, § 2º, sobre a atividade econômica.",
    "resultado": "OK",
    "trecho_lei": "§ 2º A mera perda patrimonial decorrente da atividade econômica não acarretará improbidade administrativa, salvo se comprovado ato doloso praticado com essa finalidade."
})

# 4: Linha 19
registros.append({
    "linha": 19,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Identificar as mudanças do art. 11: dolo específico, rol taxativo e condutas revogadas.",
    "resultado": "OK",
    "trecho_lei": "Art. 11. Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das seguintes condutas:"
})

# 5: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 11, §§ 1º, 3º e 4º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Explicar os parágrafos do art. 11: fim de proveito indevido, demonstração objetiva e lesividade relevante.",
    "resultado": "OK",
    "trecho_lei": "somente haverá improbidade administrativa, na aplicação deste artigo, quando for comprovado na conduta funcional do agente público o fim de obter proveito ou benefício indevido para si ou para outra pessoa ou entidade."
})

# 6: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 11, III a VIII, XI e XII da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Reconhecer as condutas dos incisos III a VIII, XI e XII do art. 11.",
    "resultado": "OK",
    "trecho_lei": "III - revelar fato ou circunstância de que tem ciência em razão das atribuições e que deva permanecer em segredo, propiciando beneficiamento por informação privilegiada"
})

# 7: Linha 23
registros.append({
    "linha": 23,
    "citacao": "art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "## Demais condutas do art. 10",
    "resultado": "OK",
    "trecho_lei": "Seção II Dos Atos de Improbidade Administrativa que Causam Prejuízo ao Erário"
})

# 8: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "As condutas do art. 10 já vistas no capítulo anterior (incisos I, II, IV, V, XII e XIII) representam apenas parte do rol. Os demais incisos tratam de operações e procedimentos em que o administrador lida com recursos, e todos exigem **dolo** e **perda patrimonial efetiva**.",
    "resultado": "OK",
    "trecho_lei": "qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres"
})

# 9: Linha 41
registros.append({
    "linha": 41,
    "citacao": "art. 10, XXII da Lei 8.429/1992 e Lei Complementar 116/2003",
    "lei": "l8429",
    "frase_capitulo": "| XXII | Conceder, aplicar ou manter benefício financeiro ou tributário contrário às regras do ISS da Lei Complementar 116/2003 | Incentivo que reduza o ISS abaixo da alíquota mínima |",
    "resultado": "OK",
    "trecho_lei": "conceder, aplicar ou manter benefício financeiro ou tributário contrário ao que dispõem o caput"
})

# 10: Linha 48
registros.append({
    "linha": 48,
    "citacao": "art. 10, VIII e art. 11, V da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "2. **A lesão precisa ser efetiva.** O inciso VIII exige \"perda patrimonial efetiva\". Se o responsável frustrou a licitação com o fim de obter benefício, mas a contratação ocorreu sem prejuízo ao erário, a conduta pode ser improbidade como violação a princípios (art. 11, V), e não como lesão.",
    "resultado": "OK",
    "trecho_lei": "V - frustrar, em ofensa à imparcialidade, o caráter concorrencial de concurso público, de chamamento ou de procedimento licitatório, com vistas à obtenção de benefício próprio, direto ou indireto, ou de terceiros;"
})

# 11: Linha 54
registros.append({
    "linha": 54,
    "citacao": "art. 10, XXII e art. 10-A da Lei 8.429/1992 e Lei Complementar 116/2003",
    "lei": "l8429",
    "frase_capitulo": "A conduta de conceder benefícios tributários contrários à Lei Complementar 116/2003 foi criada em 2016 como art. 10-A, uma \"quarta espécie\" que quebrava o escalonamento das três clássicas. A reforma revogou o art. 10-A e levou a conduta ao inciso XXII do art. 10.",
    "resultado": "OK",
    "trecho_lei": "[REVOGADO: Art. 10-A. Constitui ato de improbidade administrativa qualquer ação ou omissão para conceder, aplicar ou manter benefício financeiro ou tributário"
})

# 12: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 10, §§ 1º e 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 10 recebeu dois parágrafos em 2021:",
    "resultado": "OK",
    "trecho_lei": "§ 1º Nos casos em que a inobservância de formalidades legais ou regulamentares não implicar perda patrimonial efetiva, não ocorrerá imposição de ressarcimento"
})

# 13: Linha 71
registros.append({
    "linha": 71,
    "citacao": "art. 10, VIII e art. 11, V da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** Não há art. 10, VIII, porque falta a perda patrimonial **efetiva**. Mas a conduta frustra, em ofensa à imparcialidade, o caráter competitivo do procedimento com vistas a benefício de terceiro, o que se encaixa no **art. 11, V**.",
    "resultado": "OK",
    "trecho_lei": "VIII - frustrar a licitude de processo licitatório ou de processo seletivo para celebração de parcerias com entidades sem fins lucrativos, ou dispensá-los indevidamente, acarretando perda patrimonial efetiva;"
})

# 14: Linha 73
registros.append({
    "linha": 73,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "## Atos que atentam contra os princípios (art. 11)",
    "resultado": "OK",
    "trecho_lei": "Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade"
})

# 15: Linha 75
registros.append({
    "linha": 75,
    "citacao": "art. 11, § 4º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 11 alcança a conduta **dolosa**, por ação ou omissão, que ofenda os deveres de **honestidade, imparcialidade e legalidade** e que esteja entre as hipóteses listadas na própria lei. Este artigo independe da ocorrência de dano ao erário ou de enriquecimento ilícito (art. 11, § 4º)",
    "resultado": "OK",
    "trecho_lei": "exigem lesividade relevante ao bem jurídico tutelado para serem passíveis de sancionamento e independem do reconhecimento da produção de danos ao erário"
})

# 16: Linha 77
registros.append({
    "linha": 77,
    "citacao": "art. 11, caput, §§ 1º e 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Lei 8.429/1992, art. 11, caput, §§ 1º e 2º",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 17: Linha 78
registros.append({
    "linha": 78,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> Art. 11. Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das seguintes condutas: (...)",
    "resultado": "OK",
    "trecho_lei": "§ 2º Aplica-se o disposto no § 1º deste artigo a quaisquer atos de improbidade administrativa tipificados nesta Lei e em leis especiais e a quaisquer outros tipos especiais de improbidade administrativa instituídos por lei."
})

# 18: Linha 94
registros.append({
    "linha": 94,
    "citacao": "art. 11, §§ 1º a 5º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### Os parágrafos que limitam o art. 11",
    "resultado": "OK",
    "trecho_lei": "§ 3º O enquadramento de conduta funcional na categoria de que trata este artigo pressupõe a demonstração objetiva da prática de ilegalidade no exercício da função pública, com a indicação das normas constitucionais, legais ou infralegais violadas."
})

# 19: Linha 108
registros.append({
    "linha": 108,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!esquema] Quando o art. 11 se configura",
    "resultado": "OK",
    "trecho_lei": "Não se configurará improbidade a mera nomeação ou indicação política por parte dos detentores de mandatos eletivos, sendo necessária a aferição de dolo com finalidade ilícita"
})

# 20: Linha 114
registros.append({
    "linha": 114,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### Condutas do art. 11",
    "resultado": "OK",
    "trecho_lei": "IV - negar publicidade aos atos oficiais, exceto em razão de sua imprescindibilidade para a segurança da sociedade e do Estado ou de outras hipóteses instituídas em lei;"
})

# 21: Linha 125
registros.append({
    "linha": 125,
    "citacao": "art. 10, XVI a XX e art. 11, VIII da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| VIII | Descumprir normas de celebração, fiscalização e aprovação de contas de parcerias com entidades privadas | Versão sem dano das condutas dos incisos XVI a XX do art. 10 |",
    "resultado": "OK",
    "trecho_lei": "VIII - descumprir as normas relativas à celebração, fiscalização e aprovação de contas de parcerias firmadas pela administração pública com entidades privadas."
})

# 22: Linha 126
registros.append({
    "linha": 126,
    "citacao": "art. 11, XI da Lei 8.429/1992 e Súmula Vinculante 13",
    "lei": "l8429",
    "frase_capitulo": "| XI | Prover cargo em comissão, cargo de confiança ou função gratificada com cônjuge, companheiro ou parente (reta, colateral ou afinidade) até o 3º grau da autoridade que nomeia ou de servidor de direção, chefia ou assessoramento no mesmo órgão, inclusive por troca de nomeações | Segue a Súmula Vinculante 13 |",
    "resultado": "OK",
    "trecho_lei": "XI - nomear cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, inclusive, da autoridade nomeante"
})

# 23: Linha 127
registros.append({
    "linha": 127,
    "citacao": "art. 37, § 1º da Constituição Federal e art. 11, XII da Lei 8.429/1992",
    "lei": "cf",
    "frase_capitulo": "| XII | Praticar publicidade custeada pelo erário que contrarie o art. 37, § 1º, da Constituição, promovendo enaltecimento do agente e personalização de atos, programas, obras, serviços ou campanhas | Promoção pessoal |",
    "resultado": "OK",
    "trecho_lei": "§ 1º A publicidade dos atos, programas, obras, serviços e campanhas dos órgãos públicos deverá ter caráter educativo, informativo ou de orientação social, dela não podendo constar nomes, símbolos ou imagens que caracterizem promoção pessoal de autoridades ou servidores públicos."
})

# 24: Linha 134
registros.append({
    "linha": 134,
    "citacao": "art. 11, XI da Lei 8.429/1992 e Súmula Vinculante 13",
    "lei": "l8429",
    "frase_capitulo": "O inciso XI trouxe para a LIA a mesma redação da **Súmula Vinculante 13** do STF, que impede a nomeação de parentes de autoridades para cargos em comissão ou funções de confiança.",
    "resultado": "OK",
    "trecho_lei": "para o exercício de cargo em comissão ou de confiança ou, ainda, de função gratificada na administração pública direta e indireta em qualquer dos Poderes"
})

# 25: Linha 136
registros.append({
    "linha": 136,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### Roteiro de análise do art. 11",
    "resultado": "OK",
    "trecho_lei": "VI - deixar de prestar contas quando esteja obrigado a fazê-lo, desde que disponha das condições para isso, com vistas a ocultar irregularidades;"
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

    if r["resultado"] != "NAOVER":
        tl = r.get("trecho_lei", "")
        if len(tl) < 25:
            errors.append(f"Row {idx+1}: trecho_lei too short ({len(tl)} chars)")
        if tl in trechos_vistos:
            errors.append(f"Row {idx+1}: duplicate trecho_lei: '{tl[:30]}...'")
        trechos_vistos.add(tl)

        law_txt = cf if r["lei"] == "cf" else l8429
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
