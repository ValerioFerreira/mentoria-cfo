# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s01-p1"

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
    "citacao": "Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "Cobra o que a Constituição e a **Lei 8.429/1992**, profundamente reformada pela **Lei 14.230/2021**, dizem sobre o tema.",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 2: Linha 19
registros.append({
    "linha": 19,
    "citacao": "Tema 1199 do STF",
    "lei": "stf",
    "frase_capitulo": "> - Explicar o dolo específico e aplicar a reforma de 2021 no tempo, conforme o Tema 1199 do STF.",
    "resultado": "NAOVER",
    "motivo_naover": "Jurisprudência vinculante do STF sobre a aplicação no tempo da Lei 14.230/2021 (Tema 1.199 da Repercussão Geral, ARE 843.989)."
})

# 3: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 37, caput da CF",
    "lei": "cf",
    "frase_capitulo": "O dever de probidade nasce do princípio da **moralidade administrativa**, que a Constituição Federal inscreveu expressamente no art. 37, caput, ao lado de legalidade, impessoalidade, publicidade e eficiência.",
    "resultado": "OK",
    "trecho_lei": "Art. 37. A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência"
})

# 4: Linha 29
registros.append({
    "linha": 29,
    "citacao": "art. 37, § 4º da CF",
    "lei": "cf",
    "frase_capitulo": "| Art. 37, § 4º | Base da responsabilização: lista as consequências dos atos de improbidade |",
    "resultado": "OK",
    "trecho_lei": "§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário"
})

# 5: Linha 30
registros.append({
    "linha": 30,
    "citacao": "art. 15, V da CF",
    "lei": "cf",
    "frase_capitulo": "| Art. 15, V | A improbidade é uma das hipóteses em que os direitos políticos podem ser suspensos (a cassação é vedada) |",
    "resultado": "OK",
    "trecho_lei": "V - improbidade administrativa, nos termos do art. 37, § 4º."
})

# 6: Linha 31
registros.append({
    "linha": 31,
    "citacao": "art. 14, § 9º da CF",
    "lei": "cf",
    "frase_capitulo": "| Art. 14, § 9º | A proteção da probidade administrativa orienta a criação de casos de inelegibilidade por lei complementar |",
    "resultado": "OK",
    "trecho_lei": "§ 9º Lei complementar estabelecerá outros casos de inelegibilidade e os prazos de sua cessação, a fim de proteger a normalidade e legitimidade das eleições"
})

# 7: Linha 32
registros.append({
    "linha": 32,
    "citacao": "art. 85, V da CF",
    "lei": "cf",
    "frase_capitulo": "| Art. 85, V | Atentar contra a probidade na administração é crime de responsabilidade do Presidente da República |",
    "resultado": "OK",
    "trecho_lei": "Art. 85. São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: \n I - a existência da União; \n II - o livre exercício do Poder Legislativo, do Poder Judiciário, do Ministério Público e dos Poderes constitucionais das unidades da Federação; \n III - o exercício dos direitos políticos, individuais e sociais; \n IV - a segurança interna do País; \n V - a probidade na administração;"
})

# 8: Linha 33
registros.append({
    "linha": 33,
    "citacao": "art. 97 do ADCT",
    "lei": "cf",
    "frase_capitulo": "| ADCT, art. 97, § 10 | O chefe do Executivo que não libera, no prazo, os recursos para pagar precatórios responde por improbidade e por responsabilidade fiscal |",
    "resultado": "OK",
    "trecho_lei": "III - o chefe do Poder Executivo responderá na forma da legislação de responsabilidade fiscal e de improbidade administrativa;"
})

# 9: Linha 35
registros.append({
    "linha": 35,
    "citacao": "CF, art. 37, § 4º",
    "lei": "cf",
    "frase_capitulo": "> [!lei] CF, art. 37, § 4º",
    "resultado": "OK",
    "trecho_lei": "na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
})

# 10: Linha 38
registros.append({
    "linha": 38,
    "citacao": "Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Essa lei é a Lei 8.429/1992, conhecida como **Lei de Improbidade Administrativa (LIA)**.",
    "resultado": "OK",
    "trecho_lei": "Art. 1º O sistema de responsabilização por atos de improbidade administrativa tutelará a probidade na organização do Estado"
})

# 11: Linha 42
registros.append({
    "linha": 42,
    "citacao": "art. 37 da CF",
    "lei": "cf",
    "frase_capitulo": "A[\"CF, art. 37, caput: moralidade\"] --> B[\"CF, art. 37, par. 4: consequências e remissão à lei\"]",
    "resultado": "OK",
    "trecho_lei": "obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência e, também, ao seguinte:"
})

# 12: Linha 43
registros.append({
    "linha": 43,
    "citacao": "Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "B --> C[\"Lei 8.429/1992 (LIA), reformada pela Lei 14.230/2021\"]",
    "resultado": "OK",
    "trecho_lei": "(Redação dada pela Lei nº 14.230, de 2021)"
})

# 13: Linha 47
registros.append({
    "linha": 47,
    "citacao": "art. 37 da CF",
    "lei": "cf",
    "frase_capitulo": "Como o art. 37 se dirige à administração pública direta e indireta de **qualquer dos Poderes e de todos os entes da federação**, a LIA é uma **lei nacional**",
    "resultado": "OK",
    "trecho_lei": "A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios"
})

# 14: Linha 49
registros.append({
    "linha": 49,
    "citacao": "art. 1º a 3º",
    "lei": "l8429",
    "frase_capitulo": "- **arts. 1º a 3º**: conceito geral e sujeitos (passivo e ativo);",
    "resultado": "OK",
    "trecho_lei": "Art. 2º Para os efeitos desta Lei, consideram-se agente público o agente político, o servidor público e todo aquele que exerce, ainda que transitoriamente ou sem remuneração"
})

# 15: Linha 50
registros.append({
    "linha": 50,
    "citacao": "art. 9º, 10 e 11",
    "lei": "l8429",
    "frase_capitulo": "- **arts. 9º, 10 e 11**: as três espécies de atos de improbidade;",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 16: Linha 51
registros.append({
    "linha": 51,
    "citacao": "art. 12",
    "lei": "l8429",
    "frase_capitulo": "- **art. 12**: as sanções;",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade, civis e administrativas previstas na legislação específica"
})

# 17: Linha 52
registros.append({
    "linha": 52,
    "citacao": "art. 17",
    "lei": "l8429",
    "frase_capitulo": "- **art. 17**: a ação judicial.",
    "resultado": "OK",
    "trecho_lei": "Art. 17. A ação para a aplicação das sanções de que trata esta Lei será proposta pelo Ministério Público"
})

# 18: Linha 56
registros.append({
    "linha": 56,
    "citacao": "art. 22 da CF",
    "lei": "cf",
    "frase_capitulo": "Porque a LIA mistura temas que a Constituição reservou, **privativamente**, à União no art. 22:",
    "resultado": "OK",
    "trecho_lei": "Art. 22. Compete privativamente à União legislar sobre:"
})

# 19: Linha 60
registros.append({
    "linha": 60,
    "citacao": "art. 22, I e XIII da CF",
    "lei": "cf",
    "frase_capitulo": "| Suspensão de direitos políticos | Direito eleitoral e cidadania | CF, art. 22, I e XIII |",
    "resultado": "OK",
    "trecho_lei": "XIII - nacionalidade, cidadania e naturalização;"
})

# 20: Linha 61
registros.append({
    "linha": 61,
    "citacao": "art. 22, I da CF",
    "lei": "cf",
    "frase_capitulo": "| Ressarcimento do dano | Direito civil | CF, art. 22, I |",
    "resultado": "OK",
    "trecho_lei": "I - direito civil, comercial, penal, processual, eleitoral, agrário, marítimo, aeronáutico, espacial e do trabalho;"
})

# 21: Linha 62
registros.append({
    "linha": 62,
    "citacao": "art. 22, I da CF",
    "lei": "cf",
    "frase_capitulo": "| Penalidades | Regime punitivo de infrações contra o Estado, em sentido amplo | CF, art. 22, I |",
    "resultado": "OK",
    "trecho_lei": "comercial, penal, processual, eleitoral, agrário, marítimo"
})

# 22: Linha 63
registros.append({
    "linha": 63,
    "citacao": "art. 22, I da CF",
    "lei": "cf",
    "frase_capitulo": "| Tramitação da ação | Direito processual | CF, art. 22, I |",
    "resultado": "OK",
    "trecho_lei": "penal, processual, eleitoral, agrário, marítimo, aeronáutico"
})

# 23: Linha 65
registros.append({
    "linha": 65,
    "citacao": "art. 24 e art. 5º da CF",
    "lei": "cf",
    "frase_capitulo": "respeitadas as normas gerais da União (CF, art. 24, XI e § 2º), e que todos os entes tenham competência concorrente em temas administrativos específicos",
    "resultado": "OK",
    "trecho_lei": "XI - procedimentos em matéria processual;"
})

# 24: Linha 71
registros.append({
    "linha": 71,
    "citacao": "art. 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Lei 8.429/1992, art. 1º, §§ 1º e 2º",
    "resultado": "OK",
    "trecho_lei": "§ 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente."
})

# 25: Linha 72
registros.append({
    "linha": 72,
    "citacao": "art. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> § 1º Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados tipos previstos em leis especiais.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados tipos previstos em leis especiais."
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
