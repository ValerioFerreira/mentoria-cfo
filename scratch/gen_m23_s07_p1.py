# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s07-p1"

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
    "citacao": "art. 17 da Lei nº 8.429/1992, com alterações da Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A concretização das sanções da Lei nº 8.429/1992 exige a instauração de processo judicial contraditório perante o Poder Judiciário. A imposição de penalidades graves como a perda da função pública e a suspensão de direitos políticos não pode ocorrer na via puramente administrativa. O art. 17 da Lei nº 8.429/1992 estabelece o rito processual da demanda judicial.",
    "resultado": "OK",
    "trecho_lei": "Art. 17. A ação para a aplicação das sanções de que trata esta Lei será proposta pelo Ministério Público e seguirá o procedimento comum previsto na Lei nº 13.105, de 16 de março de 2015 (Código de Processo Civil)"
})

# 2: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 17, § 16 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Conhecer a vinculação do juiz aos fatos narrados (ADIs 7156 e 7236) e a conversão em Ação Civil Pública (art. 17, § 16).",
    "resultado": "OK",
    "trecho_lei": "converter a ação de improbidade administrativa em ação civil pública, regulada pela Lei nº 7.347, de 24 de julho de 1985."
})

# 3: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 17-B da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Examinar a disciplina do Acordo de Não Persecução Civil (Lei nº 8.429/1992, art. 17-B) e a inconstitucionalidade da oitiva da Corte de Contas.",
    "resultado": "OK",
    "trecho_lei": "Art. 17-B. O Ministério Público poderá, conforme as circunstâncias do caso concreto, celebrar acordo de não persecução civil"
})

# 4: Linha 25
registros.append({
    "linha": 25,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A redação aprovada na Lei nº 14.230/2021 pretendia conferir monopólio processual ao Ministério Público para o ajuizamento da ação de improbidade e celebração de transações resolutivas.",
    "resultado": "OK",
    "trecho_lei": "Art. 17. A ação para a aplicação das sanções de que trata esta Lei será proposta pelo Ministério Público"
})

# 5: Linha 27
registros.append({
    "linha": 27,
    "citacao": "art. 37, § 4º da Constituição Federal",
    "lei": "cf",
    "frase_capitulo": "Contudo, ao apreciar as Ações Diretas de Inconstitucionalidade nº 7.042 e nº 7.043, o Supremo Tribunal Federal assentou que o art. 37, § 4º, da Constituição Federal outorga a legitimidade sancionatória à própria Administração Pública prejudicada:",
    "resultado": "OK",
    "trecho_lei": "§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
})

# 6: Linha 36
registros.append({
    "linha": 36,
    "citacao": "art. 129, III da CF e art. 17 da Lei nº 8.429/1992",
    "lei": "cf",
    "frase_capitulo": "| **Ministério Público (Federal ou Estadual)** | CF/88, art. 129, inciso III, e art. 17 da Lei nº 8.429/1992 | Atua como autor principal ou como fiscal da ordem jurídica (*custos iuris*) se a ação for ajuizada pelo ente lesado. |",
    "resultado": "OK",
    "trecho_lei": "III - promover o inquérito civil e a ação civil pública, para a proteção do patrimônio público e social, do meio ambiente e de outros interesses difusos e coletivos;"
})

# 7: Linha 37
registros.append({
    "linha": 37,
    "citacao": "art. 37, § 4º da Constituição Federal",
    "lei": "cf",
    "frase_capitulo": "| **Pessoa Jurídica Prejudicada (Direta ou Indireta)** | CF/88, art. 37, § 4º, e STF (ADIs 7042 e 7043) | Pode ajuizar autonomamente a petição inicial, ingressar como litisconsorte ativa do MP ou firmar acordo consensual. |",
    "resultado": "OK",
    "trecho_lei": "importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei"
})

# 8: Linha 54
registros.append({
    "linha": 54,
    "citacao": "art. 17, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 17, caput, da Lei nº 8.429/1992 estabelece que a ação para aplicação das sanções adotará o rito ordinário regulado no diploma processual civil brasileiro (CPC), ressalvadas as particularidades da LIA.",
    "resultado": "OK",
    "trecho_lei": "seguirá o procedimento comum previsto na Lei nº 13.105, de 16 de março de 2015 (Código de Processo Civil), salvo o disposto nesta Lei."
})

# 9: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 17, § 7º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "No texto anterior da própria Lei nº 8.429/1992 (antigo art. 17, § 7º), existia uma fase preliminar de notificação prévia para manifestação escrita em quinze dias antes do recebimento da inicial. A Lei nº 14.230/2021 suprimiu essa notificação prévia, adotando a citação direta para conferir maior celeridade processual.",
    "resultado": "OK",
    "trecho_lei": "o juiz mandará autuá-la e ordenará a notificação do requerido, para oferecer manifestação por escrito"
})

# 10: Linha 63
registros.append({
    "linha": 63,
    "citacao": "art. 17, § 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "3. O requerido dispõe do prazo de **30 (trinta) dias** para apresentar sua contestação escrita (art. 17, § 7º).",
    "resultado": "OK",
    "trecho_lei": "§ 7º Se a petição inicial estiver em devida forma, o juiz mandará autuá-la e ordenará a citação dos requeridos para que a contestem no prazo comum de 30 (trinta) dias"
})

# 11: Linha 65
registros.append({
    "linha": 65,
    "citacao": "art. 219 e art. 231 do CPC e art. 17, § 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Esse prazo de 30 dias é prazo comum contado na forma do art. 231 do CPC. A contagem em **dias úteis** decorre da aplicação subsidiária da regra geral do art. 219 do CPC ao procedimento comum da LIA.",
    "resultado": "OK",
    "trecho_lei": "iniciado o prazo na forma do art. 231 da Lei nº 13.105, de 16 de março de 2015 (Código de Processo Civil)."
})

# 12: Linha 78
registros.append({
    "linha": 78,
    "citacao": "art. 17, § 6º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A petição inicial deve individualizar de forma pormenorizada a conduta atribuída a cada um dos requeridos (art. 17, § 6º).",
    "resultado": "OK",
    "trecho_lei": "I - deverá individualizar a conduta do réu e apontar os elementos probatórios mínimos que demonstrem a ocorrência das hipóteses dos arts. 9º, 10 e 11 desta Lei"
})

# 13: Linha 82
registros.append({
    "linha": 82,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "Para harmonizar as garantias republicanas com o interesse público indisponível, a Lei nº 14.230/2021 estabeleceu normas especiais derrogatórias do direito processual geral:",
    "resultado": "OK",
    "trecho_lei": "§ 19. Não se aplicam na ação de improbidade administrativa:"
})

# 14: Linha 84
registros.append({
    "linha": 84,
    "citacao": "Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Instituto Processual | Regra Específica na Ação de Improbidade | Dispositivo Legal na Lei nº 8.429/1992 |",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 15: Linha 86
registros.append({
    "linha": 86,
    "citacao": "art. 17, § 19, I da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Efeitos da Revelia** | **Inaplicabilidade da presunção de veracidade.** A revelia não opera efeito material de confissão ficta sobre os fatos imputados na inicial. | Art. 17, § 19, inciso I |",
    "resultado": "OK",
    "trecho_lei": "I - a presunção de veracidade dos fatos alegados pelo autor em caso de revelia;"
})

# 16: Linha 87
registros.append({
    "linha": 87,
    "citacao": "art. 17, § 19, IV, e art. 17-C, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Remessa Necessária** | **Não há reexame obrigatório.** A sentença que julgar improcedente ou extinguir a ação sem mérito submete-se exclusivamente a recurso voluntário. | Art. 17, § 19, IV, e art. 17-C, § 3º |",
    "resultado": "OK",
    "trecho_lei": "IV - o reexame obrigatório da sentença de improcedência ou de extinção sem resolução de mérito."
})

# 17: Linha 88
registros.append({
    "linha": 88,
    "citacao": "art. 17, § 21 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Decisões Interlocutórias** | Das decisões interlocutórias cabe **Agravo de Instrumento**, inclusive contra rejeição de preliminares na contestação. | Art. 17, § 21 |",
    "resultado": "OK",
    "trecho_lei": "§ 21. Das decisões interlocutórias caberá agravo de instrumento, inclusive da decisão que rejeitar questões preliminares suscitadas pelo réu em sua contestação."
})

# 18: Linha 92
registros.append({
    "linha": 92,
    "citacao": "art. 17, § 19, IV, e art. 17-C, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Ausência de remessa necessária:** no processo civil ordinário contra a Fazenda Pública, a sentença desfavorável ao Estado costuma submeter-se ao duplo grau de jurisdição. Na ação de improbidade, essa regra foi expressamente afastada (art. 17, § 19, IV, e art. 17-C, § 3º).",
    "resultado": "OK",
    "trecho_lei": "§ 3º Não haverá remessa necessária nas sentenças de que trata esta Lei."
})

# 19: Linha 96
registros.append({
    "linha": 96,
    "citacao": "art. 17, §§ 10-C, 10-D e 10-F, I da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A reforma da Lei nº 14.230/2021 incluiu os §§ 10-C, 10-D e 10-F, I, no art. 17, buscando proibir que o magistrado alterasse a capitulação legal sugerida pelo autor e cominando nulidade à sentença que condenasse por tipo diverso do capitulado na inicial.",
    "resultado": "OK",
    "trecho_lei": "Após a réplica do Ministério Público, o juiz proferirá decisão na qual indicará com precisão a tipificação do ato de improbidade administrativa"
})

# 20: Linha 99
registros.append({
    "linha": 99,
    "citacao": "art. 17, §§ 10-C, 10-D e 10-F, I da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- O STF declarou inconstitucionais a expressão \"e a capitulação legal apresentada pelo autor\" do art. 17, § 10-C, o § 10-D e o inciso I do § 10-F.",
    "resultado": "OK",
    "trecho_lei": "Para cada ato de improbidade administrativa, deverá necessariamente ser indicado apenas um tipo dentre aqueles previstos nos arts. 9º, 10 e 11 desta Lei."
})

# 21: Linha 100
registros.append({
    "linha": 100,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Regra vigente:** o juiz fica vinculado estritamente aos **fatos narrados** na petição inicial (*narra mihi factum, dabo tibi ius*), e não à capitulação legal adotada pelo autor. O magistrado não pode condenar por fatos não narrados, mas pode reenquadrar juridicamente a conduta (por exemplo, condenar pelo art. 9º ou art. 10 caso a narrativa fática comprove essas espécies, ainda que a inicial tenha indicado o art. 11), assegurado o contraditório prévio das partes.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei"
})

# 22: Linha 104
registros.append({
    "linha": 104,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "Na prática judiciária, ações de improbidade eram ajuizadas para combater irregularidades puramente administrativas, sem comprovação de dolo ou desonestidade. Com a extinção da improbidade culposa pela Lei nº 14.230/2021, tais atos não configuram infração de improbidade.",
    "resultado": "OK",
    "trecho_lei": "§ 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei"
})

# 23: Linha 108
registros.append({
    "linha": 108,
    "citacao": "art. 17, § 16 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 17, § 16, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "A qualquer momento, se o magistrado identificar a existência de ilegalidades ou de irregularidades administrativas a serem sanadas sem que estejam presentes todos os requisitos para a imposição das sanções"
})

# 24: Linha 111
registros.append({
    "linha": 111,
    "citacao": "art. 17, § 17 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 17, § 17, complementa expressamente que **da decisão que converter a ação de improbidade em ação civil pública caberá agravo de instrumento**.",
    "resultado": "OK",
    "trecho_lei": "§ 17. Da decisão que converter a ação de improbidade em ação civil pública caberá agravo de instrumento."
})

# 25: Linha 117
registros.append({
    "linha": 117,
    "citacao": "art. 17, § 20 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Visando resguardar a atuação regular do gestor de boa-fé, o art. 17, § 20, da LIA previu que o órgão de consultoria que subscreveu parecer prévio favorável à prática do ato administrativo poderá assumir a defesa judicial do agente público demandado.",
    "resultado": "OK",
    "trecho_lei": "A assessoria jurídica que emitiu o parecer atestando a legalidade prévia dos atos administrativos praticados pelo administrador público ficará obrigada a defendê-lo judicialmente"
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
