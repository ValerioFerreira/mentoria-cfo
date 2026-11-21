# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s06-p1"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cpp.clean.txt", "r", encoding="utf-8") as f:
    cpp = f.read()

registros = []

# 1: Linha 14
registros.append({
    "linha": 14,
    "citacao": "Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "O ordenamento jurídico adota a pluralidade sancionatória: um mesmo ato ilícito pode repercutir nas esferas penal, civil, disciplinar e de improbidade. A Lei nº 8.429/1992, reformada pela Lei nº 14.230/2021",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Compreender a regra da independência das instâncias e as hipóteses de comunicação vinculante da absolvição criminal nos termos do art. 21, § 3º, e a decisão do STF nas ADIs 7156 e 7236.",
    "resultado": "OK",
    "trecho_lei": "§ 3º As sentenças civis e penais produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria."
})

# 3: Linha 18
registros.append({
    "linha": 18,
    "citacao": "art. 12, §§ 6º e 7º, e art. 21, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Analisar a disciplina da dedução do ressarcimento ao erário e da compensação de sanções sancionatórias (art. 12, §§ 6º e 7º, e art. 21, § 5º).",
    "resultado": "OK",
    "trecho_lei": "§ 5º Sanções eventualmente aplicadas em outras esferas deverão ser compensadas com as sanções aplicadas nos termos desta Lei."
})

# 4: Linha 19
registros.append({
    "linha": 19,
    "citacao": "art. 13 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Identificar as regras e consequências da declaração de imposto de renda apresentada à Receita Federal pelo agente público (art. 13).",
    "resultado": "OK",
    "trecho_lei": "Art. 13. A posse e o exercício de agente público ficam condicionados à apresentação de declaração de imposto de renda e proventos de qualquer natureza, que tenha sido apresentada à Secretaria Especial da Receita Federal do Brasil"
})

# 5: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 14, art. 22 e art. 23, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Conhecer as formalidades da representação administrativa perante a autoridade competente (art. 14) e as prerrogativas de investigação do Ministério Público (art. 22 e art. 23, § 2º).",
    "resultado": "OK",
    "trecho_lei": "Art. 14. Qualquer pessoa poderá representar à autoridade administrativa competente para que seja instaurada investigação destinada a apurar a prática de ato de improbidade."
})

# 6: Linha 24
registros.append({
    "linha": 24,
    "citacao": "art. 12 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A responsabilização por improbidade administrativa possui natureza estritamente civil-política. Ela tutela a probidade e a moralidade no trato da coisa pública, não se confundindo com a infração penal típica nem com a transgressão disciplinar funcional. Por essa razão fundamental, o art. 12 da Lei nº 8.429/1992 consagra que as sanções da LIA são aplicadas independentemente das sanções penais, civis e administrativas previstas na legislação específica.",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade, civis e administrativas previstas na legislação específica"
})

# 7: Linha 46
registros.append({
    "linha": 46,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Embora vigore o princípio da autonomia entre as jurisdições, essa independência não é absoluta. O Direito não tolera contradições lógicas que comprometam a segurança jurídica. O art. 21, § 3º, da Lei nº 8.429/1992 positivou a comunicação vinculante das decisões absolutórias:",
    "resultado": "OK",
    "trecho_lei": "produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria."
})

# 8: Linha 48
registros.append({
    "linha": 48,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 21, § 3º, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "Art. 21. A aplicação das sanções previstas nesta lei independe:"
})

# 9: Linha 52
registros.append({
    "linha": 52,
    "citacao": "art. 386, I do Código de Processo Penal",
    "lei": "cpp",
    "frase_capitulo": "1. **Inexistência material do fato ou da conduta:** o juízo criminal declara categoricamente que o fato imputado não ocorreu no mundo fenomênico (CPP, art. 386, I).",
    "resultado": "OK",
    "trecho_lei": "I - estar provada a inexistência do fato;"
})

# 10: Linha 53 (ERRO BAIXO: citação ao art. 386, II do CPP em vez de art. 386, IV)
registros.append({
    "linha": 53,
    "citacao": "art. 386, II do Código de Processo Penal",
    "lei": "cpp",
    "frase_capitulo": "2. **Negativa categórica de autoria:** o juízo penal reconhece de forma inequívoca que o acusado não foi o autor nem concorreu para a prática da infração (CPP, art. 386, II).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O capítulo cita o art. 386, II, do CPP como fundamento da negativa de autoria, mas o inciso II trata de 'não haver prova da existência do fato'; a comprovação de que o réu não concorreu para a infração é o art. 386, IV, do CPP.",
    "texto_novo": "2. **Negativa categórica de autoria:** o juízo penal reconhece de forma inequívoca que o acusado não foi o autor nem concorreu para a prática da infração (CPP, art. 386, IV).",
    "trecho_lei": "estar provado que o réu não concorreu para a infração penal; (Redação dada pela Lei nº 11.690, de 2008)"
})

# 11: Linha 55
registros.append({
    "linha": 55,
    "citacao": "art. 21, § 4º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### A declaração de inconstitucionalidade do art. 21, § 4º (ADIs 7156 e 7236)",
    "resultado": "OK",
    "trecho_lei": "§ 4º A absolvição criminal em ação que discuta os mesmos fatos, confirmada por decisão colegiada, impede o trâmite da ação da qual trata esta Lei"
})

# 12: Linha 57
registros.append({
    "linha": 57,
    "citacao": "art. 21, §§ 3º e 4º da Lei nº 8.429/1992, art. 37, § 4º da CF e art. 386 do CPP",
    "lei": "l8429",
    "frase_capitulo": "A Lei nº 14.230/2021 havia inserido o § 4º no art. 21 da LIA para vincular a improbidade a qualquer absolvição criminal colegiada do art. 386 do CPP. Todavia, no julgamento das **ADIs 7156 e 7236** (concluído em 1º/7/2026), o STF declarou a **inconstitucionalidade do art. 21, § 4º**",
    "resultado": "OK",
    "trecho_lei": "havendo comunicação com todos os fundamentos de absolvição previstos no art. 386 do Decreto-Lei nº 3.689, de 3 de outubro de 1941 (Código de Processo Penal)."
})

# 13: Linha 63 (ERRO BAIXO: citação a art. 386, I e II em vez de I e IV)
registros.append({
    "linha": 63,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992 e art. 386, I e II do Código de Processo Penal",
    "lei": "cpp",
    "frase_capitulo": "| **Negativa de Autoria ou Inexistência da Conduta** | **Vinculação Obrigatória:** extingue a ação de improbidade e afasta as sanções civis. | Art. 21, § 3º, da LIA e art. 386, I e II, do CPP |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "A tabela cita o art. 386, I e II, do CPP para negativa de autoria ou inexistência da conduta, mas o inciso II é 'não haver prova da existência do fato'; a negativa comprovada de autoria é o inciso IV do art. 386 do CPP.",
    "texto_novo": "| **Negativa de Autoria ou Inexistência da Conduta** | **Vinculação Obrigatória:** extingue a ação de improbidade e afasta as sanções civis. | Art. 21, § 3º, da LIA e art. 386, I e IV, do CPP |",
    "trecho_lei": "II - não haver prova da existência do fato;"
})

# 14: Linha 64
registros.append({
    "linha": 64,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992 e art. 386, VII do Código de Processo Penal",
    "lei": "cpp",
    "frase_capitulo": "| **Falta ou Insuficiência de Provas (*in dubio pro reo*)** | **Não Vincula:** a ação de improbidade prossegue sob os padrões probatórios da jurisdição cível. | Art. 21, § 3º, da LIA e art. 386, VII, do CPP |",
    "resultado": "OK",
    "trecho_lei": "não existir prova suficiente para a condenação. (Incluído pela Lei nº 11.690, de 2008)"
})

# 15: Linha 66
registros.append({
    "linha": 66,
    "citacao": "art. 12 e art. 23 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Extinção da Punibilidade (Prescrição Penal)** | **Não Vincula:** a prescrição penal não interfere no regime autônomo da LIA. | Art. 12 e art. 23 da LIA |",
    "resultado": "OK",
    "trecho_lei": "Art. 23. A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato"
})

# 16: Linha 69
registros.append({
    "linha": 69,
    "citacao": "art. 21, § 4º da Lei nº 8.429/1992 e art. 386, VII do CPP",
    "lei": "cpp",
    "frase_capitulo": "> **Absolvição por falta de provas não vincula:** preste atenção nas pegadinhas de prova. Se o réu foi absolvido no juízo criminal por insuficiência de provas (art. 386, VII, do CPP), essa decisão **não** impede a condenação por improbidade.",
    "resultado": "OK",
    "trecho_lei": "Art. 386. O juiz absolverá o réu, mencionando a causa na parte dispositiva, desde que reconheça:"
})

# 17: Linha 73
registros.append({
    "linha": 73,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A Lei nº 14.230/2021 estabeleceu regras expressas para evitar o enriquecimento sem causa do Estado e a punição dúplice pelo mesmo fato material (*bis in idem*).",
    "resultado": "OK",
    "trecho_lei": "deverão observar o princípio constitucional do non bis in idem."
})

# 18: Linha 76
registros.append({
    "linha": 76,
    "citacao": "art. 12, § 6º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Dedução do ressarcimento (art. 12, § 6º):** abatem-se da condenação indenizatória quantias já pagas nas esferas penal, administrativa ou cível sobre o mesmo fato.",
    "resultado": "OK",
    "trecho_lei": "§ 6º Se ocorrer lesão ao patrimônio público, a reparação do dano a que se refere esta Lei deverá deduzir o ressarcimento ocorrido nas instâncias criminal, civil e administrativa"
})

# 19: Linha 77
registros.append({
    "linha": 77,
    "citacao": "art. 21, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Compensação de sanções (art. 21, § 5º):** penalidades pecuniárias de mesma natureza aplicadas em outras instâncias são compensadas com as multas da LIA.",
    "resultado": "OK",
    "trecho_lei": "Sanções eventualmente aplicadas em outras esferas deverão ser compensadas com as sanções aplicadas nos termos desta Lei."
})

# 20: Linha 78
registros.append({
    "linha": 78,
    "citacao": "art. 12, § 7º da Lei nº 8.429/1992 e Lei nº 12.846/2013",
    "lei": "l8429",
    "frase_capitulo": "- **Vedação de bis in idem (art. 12, § 7º):** sanções a pessoas jurídicas pela LIA e pela Lei nº 12.846/2013 não podem incidir em duplicidade.",
    "resultado": "OK",
    "trecho_lei": "As sanções aplicadas a pessoas jurídicas com base nesta Lei"
})

# 21: Linha 79
registros.append({
    "linha": 79,
    "citacao": "art. 21, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Atos de controle (art. 21, § 1º):** pareceres de órgãos de controle que serviram de suporte à conduta do agente devem ser considerados pelo juiz.",
    "resultado": "OK",
    "trecho_lei": "§ 1º Os atos do órgão de controle interno ou externo serão considerados pelo juiz quando tiverem servido de fundamento para a conduta do agente público."
})

# 22: Linha 81
registros.append({
    "linha": 81,
    "citacao": "art. 21, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 21, § 1º, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "§ 2º As provas produzidas perante os órgãos de controle e as correspondentes decisões deverão ser consideradas na formação da convicção do juiz, sem prejuízo da análise acerca do dolo na conduta do agente."
})

# 23: Linha 86
registros.append({
    "linha": 86,
    "citacao": "art. 13 da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A transparência patrimonial dos agentes públicos constitui mecanismo preventivo fundamental contra o enriquecimento ilícito. O art. 13 da Lei nº 8.429/1992, com a redação dada pela Lei nº 14.230/2021, reformulou a apresentação da declaração de bens.",
    "resultado": "OK",
    "trecho_lei": "Art. 13. A posse e o exercício de agente público ficam condicionados à apresentação de declaração de imposto de renda e proventos de qualquer natureza"
})

# 24: Linha 90
registros.append({
    "linha": 90,
    "citacao": "art. 13 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 13 da LIA vinculou o controle patrimonial diretamente aos dados fiscais:",
    "resultado": "OK",
    "trecho_lei": "Secretaria Especial da Receita Federal do Brasil, a fim de ser arquivada no serviço de pessoal competente."
})

# 25: Linha 92
registros.append({
    "linha": 92,
    "citacao": "art. 13, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 13, caput, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO IV Da Declaração de Bens"
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

        law_txt = cpp if r["lei"] == "cpp" else l8429
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
