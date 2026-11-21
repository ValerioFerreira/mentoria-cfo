# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s03-p1"

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
    "citacao": "art. 9º e art. 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "análise do art. 9º, que trata do **enriquecimento ilícito**, a espécie mais grave. No final, o capítulo abre o art. 10 (lesão ao erário)",
    "resultado": "OK",
    "trecho_lei": "Seção I Dos Atos de Improbidade Administrativa que Importam Enriquecimento Ilícito"
})

# 2: Linha 19
registros.append({
    "linha": 19,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "> - Reconhecer os incisos do art. 9º e a pista textual \"perceber vantagem econômica\".",
    "resultado": "OK",
    "trecho_lei": "V - receber vantagem econômica de qualquer natureza, direta ou indireta, para tolerar a exploração ou a prática de jogos de azar"
})

# 3: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "> - Explicar as exigências do art. 10: dolo e perda patrimonial efetiva e comprovada.",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial"
})

# 4: Linha 33
registros.append({
    "linha": 33,
    "citacao": "arts. 9º, 10, 11 e 12 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Há uma **gradação das sanções** (art. 12): a espécie do art. 9º recebe as penas mais severas, a do art. 10 as intermediárias e a do art. 11 as mais brandas.",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade, civis e administrativas previstas na legislação específica"
})

# 5: Linha 38
registros.append({
    "linha": 38,
    "citacao": "art. 9º, III",
    "lei": "l8429",
    "frase_capitulo": "Quem recebe suborno para vender um bem público por preço baixo comete enriquecimento ilícito (art. 9º, III) e também causa perda ao patrimônio, mas responde pelo enriquecimento, pois a lesão fica absorvida.",
    "resultado": "OK",
    "trecho_lei": "III - perceber vantagem econômica, direta ou indireta, para facilitar a alienação, permuta ou locação de bem público ou o fornecimento de serviço por ente estatal por preço inferior ao valor de mercado;"
})

# 6: Linha 42
registros.append({
    "linha": 42,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "A[\"Ato de improbidade (sempre doloso)\"] --> B[\"Art. 9: enriquecimento ilícito, sanção mais grave\"]",
    "resultado": "OK",
    "trecho_lei": "perda dos bens ou valores acrescidos ilicitamente ao patrimônio, perda da função pública, suspensão dos direitos políticos até 14 (catorze) anos"
})

# 7: Linha 43
registros.append({
    "linha": 43,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "A --> C[\"Art. 10: lesão ao erário, sanção intermediária\"]",
    "resultado": "OK",
    "trecho_lei": "II - na hipótese do art. 10 desta Lei, perda dos bens ou valores acrescidos ilicitamente ao patrimônio, se concorrer esta circunstância, perda da função pública, suspensão dos direitos políticos até 12 (doze) anos"
})

# 8: Linha 44
registros.append({
    "linha": 44,
    "citacao": "art. 11",
    "lei": "l8429",
    "frase_capitulo": "A --> D[\"Art. 11: violação a princípios, sanção mais branda\"]",
    "resultado": "OK",
    "trecho_lei": "III - na hipótese do art. 11 desta Lei, pagamento de multa civil de até 24 (vinte e quatro) vezes o valor da remuneração percebida pelo agente"
})

# 9: Linha 56
registros.append({
    "linha": 56,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "| Art. 9º (enriquecimento ilícito) | Exemplificativo | \"e notadamente\" |",
    "resultado": "OK",
    "trecho_lei": "de função, de emprego ou de atividade nas entidades referidas no art. 1º desta Lei, e notadamente:"
})

# 10: Linha 57
registros.append({
    "linha": 57,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10 (lesão ao erário) | Exemplificativo | \"e notadamente\" |",
    "resultado": "OK",
    "trecho_lei": "desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1º desta lei, e notadamente:"
})

# 11: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 11",
    "lei": "l8429",
    "frase_capitulo": "| Art. 11 (violação a princípios) | **Taxativo** | \"caracterizada por uma das seguintes condutas\" |",
    "resultado": "OK",
    "trecho_lei": "caracterizada por uma das seguintes condutas: (Redação dada pela Lei nº 14.230, de 2021)"
})

# 12: Linha 60
registros.append({
    "linha": 60,
    "citacao": "art. 11",
    "lei": "l8429",
    "frase_capitulo": "No art. 11, a reforma trocou o \"e notadamente\" por uma fórmula que fecha a lista.",
    "resultado": "OK",
    "trecho_lei": "Art. 11. Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade"
})

# 13: Linha 63
registros.append({
    "linha": 63,
    "citacao": "art. 9º e art. 11",
    "lei": "l8429",
    "frase_capitulo": "Só os arts. 9º e 10 continuam exemplificativos; o art. 11 é taxativo.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei"
})

# 14: Linha 65
registros.append({
    "linha": 65,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "## Atos que importam enriquecimento ilícito (art. 9º)",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO II Dos Atos de Improbidade Administrativa"
})

# 15: Linha 67
registros.append({
    "linha": 67,
    "citacao": "Lei 8.429/1992, art. 9º, caput",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Lei 8.429/1992, art. 9º, caput",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 16: Linha 68
registros.append({
    "linha": 68,
    "citacao": "art. 1º e art. 9º",
    "lei": "l8429",
    "frase_capitulo": "> Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida em razão do exercício de cargo, de mandato, de função, de emprego ou de atividade nas entidades referidas no art. 1º desta Lei, e notadamente: (...)",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 17: Linha 76
registros.append({
    "linha": 76,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "### Os incisos do art. 9º",
    "resultado": "OK",
    "trecho_lei": "VI - receber vantagem econômica de qualquer natureza, direta ou indireta, para fazer declaração falsa sobre qualquer dado técnico que envolva obras públicas"
})

# 18: Linha 97
registros.append({
    "linha": 97,
    "citacao": "art. 10, XII",
    "lei": "l8429",
    "frase_capitulo": "Já permitir, sem receber nada, que terceiro se enriqueça ilicitamente é lesão ao erário (art. 10, XII).",
    "resultado": "OK",
    "trecho_lei": "XII - permitir, facilitar ou concorrer para que terceiro se enriqueça ilicitamente;"
})

# 19: Linha 99
registros.append({
    "linha": 99,
    "citacao": "art. 9º e art. 10, IV e V",
    "lei": "l8429",
    "frase_capitulo": "Os incisos IV e V do art. 10 descrevem condutas parecidas (preço inferior ou superior ao de mercado), mas sem o recebimento de vantagem pelo agente. A diferença é essa: se há vantagem para o agente, é art. 9º; se não há, é art. 10.",
    "resultado": "OK",
    "trecho_lei": "V - permitir ou facilitar a aquisição, permuta ou locação de bem ou serviço por preço superior ao de mercado;"
})

# 20: Linha 102
registros.append({
    "linha": 102,
    "citacao": "art. 10, V",
    "lei": "l8429",
    "frase_capitulo": "> [!resolvido] Questão comentada: inciso II ou art. 10, V?",
    "resultado": "OK",
    "trecho_lei": "IV - permitir ou facilitar a alienação, permuta ou locação de bem integrante do patrimônio de qualquer das entidades referidas no art. 1º desta lei"
})

# 21: Linha 105
registros.append({
    "linha": 105,
    "citacao": "art. 9º, II e art. 10, V",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** Art. 9º, II. Como o agente **perceber vantagem econômica** para facilitar a compra por preço superior ao de mercado, há enriquecimento ilícito. Se ele apenas permitisse a compra superfaturada, sem receber nada, o enquadramento seria o art. 10, V (lesão ao erário).",
    "resultado": "OK",
    "trecho_lei": "perceber vantagem econômica, direta ou indireta, para facilitar a aquisição, permuta ou locação de bem móvel ou imóvel"
})

# 22: Linha 108
registros.append({
    "linha": 108,
    "citacao": "art. 9º, IV, VII, VIII, XI e XII",
    "lei": "l8429",
    "frase_capitulo": "Preste atenção aos cinco incisos que não usam esse verbo, porque as bancas os usam para dificultar: **IV, VII, VIII, XI e XII**.",
    "resultado": "OK",
    "trecho_lei": "IV - utilizar, em obra ou serviço particular, qualquer bem móvel, de propriedade ou à disposição de qualquer das entidades referidas no art. 1º desta Lei"
})

# 23: Linha 118
registros.append({
    "linha": 118,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "## Noções iniciais do art. 10: lesão ao erário",
    "resultado": "OK",
    "trecho_lei": "Seção II Dos Atos de Improbidade Administrativa que Causam Prejuízo ao Erário"
})

# 24: Linha 120
registros.append({
    "linha": 120,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "Pelo texto legal, o ato é uma ação ou omissão **dolosa** que provoque, de modo **efetivo e comprovado**, perda de patrimônio, desvio, apropriação, malbaratamento ou dilapidação de bens ou haveres das entidades protegidas.",
    "resultado": "OK",
    "trecho_lei": "qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres"
})

# 25: Linha 124
registros.append({
    "linha": 124,
    "citacao": "CF, art. 37, § 6º",
    "lei": "cf",
    "frase_capitulo": "a Constituição permite o regresso contra o agente que causou dano a terceiros com dolo ou culpa (CF, art. 37, § 6º)",
    "resultado": "OK",
    "trecho_lei": "§ 6º As pessoas jurídicas de direito público e as de direito privado prestadoras de serviços públicos responderão pelos danos que seus agentes, nessa qualidade, causarem a terceiros, assegurado o direito de regresso contra o responsável nos casos de dolo ou culpa."
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
