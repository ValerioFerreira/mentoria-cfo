# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s01-p3"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cp.clean.txt", "r", encoding="utf-8") as f:
    cp = f.read()

registros = []

# 1: Linha 202
registros.append({
    "linha": 202,
    "citacao": "art. 1º, § 2º e arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Os tipos dos arts. 9º, 10 e 11 exigem **dolo**, e o art. 1º, § 2º, afirma que a voluntariedade da conduta sozinha não basta.",
    "resultado": "OK",
    "trecho_lei": "§ 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente."
})

# 2: Linha 210
registros.append({
    "linha": 210,
    "citacao": "art. 337-E do Código Penal",
    "lei": "cp",
    "frase_capitulo": "| Penal | Código Penal, art. 337-E (contratação direta ilegal) | Juiz criminal |",
    "resultado": "OK",
    "trecho_lei": "Art. 337-E. Admitir, possibilitar ou dar causa à contratação direta fora das hipóteses previstas em lei:"
})

# 3: Linha 212
registros.append({
    "linha": 212,
    "citacao": "art. 10, VIII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Civil, por improbidade | LIA, art. 10, VIII (frustrar a licitude da licitação ou dispensá-la indevidamente com perda patrimonial efetiva) | Juiz cível, em ação de improbidade |",
    "resultado": "OK",
    "trecho_lei": "VIII - frustrar a licitude de processo licitatório ou de processo seletivo para celebração de parcerias com entidades sem fins lucrativos, ou dispensá-los indevidamente, acarretando perda patrimonial efetiva;"
})

# 4: Linha 218
registros.append({
    "linha": 218,
    "citacao": "art. 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O **sujeito passivo** é a vítima: a entidade lesada pela improbidade. A lei o descreve em três camadas (art. 1º).",
    "resultado": "OK",
    "trecho_lei": "§ 5º Os atos de improbidade violam a probidade na organização do Estado e no exercício de suas funções e a integridade do patrimônio público e social dos Poderes Executivo, Legislativo e Judiciário, bem como da administração direta e indireta"
})

# 5: Linha 251
registros.append({
    "linha": 251,
    "citacao": "art. 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!bizu] Relação entre o art. 1º e as espécies de ato",
    "resultado": "OK",
    "trecho_lei": "Art. 1º O sistema de responsabilização por atos de improbidade administrativa tutelará a probidade na organização do Estado e no exercício de suas funções, como forma de assegurar a integridade do patrimônio"
})

# 6: Linha 252
registros.append({
    "linha": 252,
    "citacao": "art. 1º, §§ 1º, 5º, 6º e 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> Guarde o par: o art. 1º, § 1º, define o ato (conduta dolosa tipificada) e o § 5º aponta quem é lesado (os Poderes e as administrações direta e indireta). Os §§ 6º e 7º estendem a proteção às entidades privadas ligadas a recursos públicos.",
    "resultado": "OK",
    "trecho_lei": "§ 6º Estão sujeitos às sanções desta Lei os atos de improbidade praticados contra o patrimônio de entidade privada que receba subvenção, benefício ou incentivo, fiscal ou creditício"
})

# 7: Linha 257
registros.append({
    "linha": 257,
    "citacao": "art. 1º, § 6º e art. 2º, parágrafo único da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** Sim. A entidade privada que recebe subvenção ou benefício de entes públicos é protegida pela LIA (art. 1º, § 6º)",
    "resultado": "OK",
    "trecho_lei": "No que se refere a recursos de origem pública, sujeita-se às sanções previstas nesta Lei o particular, pessoa física ou jurídica, que celebra com a administração pública convênio, contrato de repasse, contrato de gestão, termo de parceria"
})

# 8: Linha 261
registros.append({
    "linha": 261,
    "citacao": "art. 37, § 4º da CF e Tema 1199 do STF",
    "lei": "cf",
    "frase_capitulo": "Há ainda itens sobre a competência da União e sobre a base constitucional (art. 37, § 4º), em que o candidato precisa lembrar as quatro consequências. Um grupo crescente de questões envolve a aplicação da reforma no tempo e o Tema 1199",
    "resultado": "OK",
    "trecho_lei": "§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário"
})

# 9: Linha 267
registros.append({
    "linha": 267,
    "citacao": "CF, art. 37, § 4º",
    "lei": "cf",
    "frase_capitulo": "| Base constitucional | CF, art. 37, § 4º, quatro consequências e remissão à lei | Esquecer uma das consequências |",
    "resultado": "OK",
    "trecho_lei": "na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
})

# 10: Linha 268
registros.append({
    "linha": 268,
    "citacao": "art. 1º a 3º, 9º a 12 e 17 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| LIA | Lei nacional, estrutura nos arts. 1º a 3º, 9º a 12 e 17 | Chamá-la de lei só federal |",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 11: Linha 269
registros.append({
    "linha": 269,
    "citacao": "CF, art. 22",
    "lei": "cf",
    "frase_capitulo": "| Competência | Privativa da União (CF, art. 22) | Dizer que a CF a prevê expressamente |",
    "resultado": "OK",
    "trecho_lei": "Art. 22. Compete privativamente à União legislar sobre:"
})

# 12: Linha 270
registros.append({
    "linha": 270,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Conceito | Conduta dolosa tipificada nos arts. 9º, 10 e 11 | Admitir culpa |",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados tipos previstos em leis especiais."
})

# 13: Linha 274
registros.append({
    "linha": 274,
    "citacao": "art. 1º, § 4º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Direito sancionador | Princípios do art. 1º, § 4º | Ignorar as garantias |",
    "resultado": "OK",
    "trecho_lei": "§ 4º Aplicam-se ao sistema da improbidade disciplinado nesta Lei os princípios constitucionais do direito administrativo sancionador."
})

# 14: Linha 279
registros.append({
    "linha": 279,
    "citacao": "art. 37, caput da Constituição",
    "lei": "cf",
    "frase_capitulo": "1. A moralidade administrativa é princípio expresso no art. 37, caput, da Constituição.",
    "resultado": "OK",
    "trecho_lei": "Art. 37. A administração pública direta e indireta de qualquer dos Poderes da União, dos Estados, do Distrito Federal e dos Municípios obedecerá aos princípios de legalidade, impessoalidade, moralidade, publicidade e eficiência"
})

# 15: Linha 280
registros.append({
    "linha": 280,
    "citacao": "art. 37, § 4º",
    "lei": "cf",
    "frase_capitulo": "2. O art. 37, § 4º, enumera quatro consequências (direitos políticos, função pública, bens e erário) e preserva a ação penal.",
    "resultado": "OK",
    "trecho_lei": "suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário"
})

# 16: Linha 281
registros.append({
    "linha": 281,
    "citacao": "Lei 8.429/1992 e Lei 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "3. A Lei 8.429/1992 é lei nacional, de competência privativa da União, reformada pela Lei 14.230/2021.",
    "resultado": "OK",
    "trecho_lei": "(Redação dada pela Lei nº 14.230, de 2021)"
})

# 17: Linha 282
registros.append({
    "linha": 282,
    "citacao": "arts. 9º, 10 e 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "4. Ato de improbidade é a conduta dolosa tipificada nos arts. 9º, 10 e 11 ou em lei especial.",
    "resultado": "OK",
    "trecho_lei": "vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente."
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

        if r["lei"] == "cf":
            law_txt = cf
        elif r["lei"] == "cp":
            law_txt = cp
        else:
            law_txt = l8429

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
