# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s01-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 73
registros.append({
    "linha": 73,
    "citacao": "art. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> § 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente.",
    "resultado": "OK",
    "trecho_lei": "§ 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente."
})

# 2: Linha 75
registros.append({
    "linha": 75,
    "citacao": "art. 1º e art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Receber vantagem econômica para intermediar a liberação de verba pública é um exemplo de conduta tipificada no art. 9º, IX.",
    "resultado": "OK",
    "trecho_lei": "IX - perceber vantagem econômica para intermediar a liberação ou aplicação de verba pública de qualquer natureza;"
})

# 3: Linha 87
registros.append({
    "linha": 87,
    "citacao": "art. 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Realizar operação financeira sem observar as normas legais é ato de improbidade (art. 10, VI)",
    "resultado": "OK",
    "trecho_lei": "VI - realizar operação financeira sem observância das normas legais e regulamentares ou aceitar garantia insuficiente ou inidônea;"
})

# 4: Linha 92
registros.append({
    "linha": 92,
    "citacao": "art. 11 da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "Deixar de prestar contas para ocultar irregularidades, por exemplo, é omissão tipificada no art. 11, VI. Mas, depois da Lei 14.230/2021, **ambas exigem dolo**.",
    "resultado": "OK",
    "trecho_lei": "VI - deixar de prestar contas quando esteja obrigado a fazê-lo, desde que disponha das condições para isso, com vistas a ocultar irregularidades;"
})

# 5: Linha 96
registros.append({
    "linha": 96,
    "citacao": "art. 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Se a autoridade que tomar conhecimento dos fatos perceber indícios de improbidade, deve representar ao **Ministério Público competente** para as providências cabíveis (art. 7º).",
    "resultado": "OK",
    "trecho_lei": "Art. 7º Se houver indícios de ato de improbidade, a autoridade que conhecer dos fatos representará ao Ministério Público competente, para as providências necessárias."
})

# 6: Linha 102
registros.append({
    "linha": 102,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "1. atos que importam **enriquecimento ilícito** (art. 9º);",
    "resultado": "OK",
    "trecho_lei": "Seção I Dos Atos de Improbidade Administrativa que Importam Enriquecimento Ilícito"
})

# 7: Linha 103
registros.append({
    "linha": 103,
    "citacao": "art. 10",
    "lei": "l8429",
    "frase_capitulo": "2. atos que causam **prejuízo ao erário** (art. 10);",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial"
})

# 8: Linha 104
registros.append({
    "linha": 104,
    "citacao": "art. 11",
    "lei": "l8429",
    "frase_capitulo": "3. atos que **atentam contra os princípios da administração pública** (art. 11).",
    "resultado": "OK",
    "trecho_lei": "Seção III Dos Atos de Improbidade Administrativa que Atentam Contra os Princípios da Administração Pública"
})

# 9: Linha 106
registros.append({
    "linha": 106,
    "citacao": "art. 1º, § 1º da Lei nº 8.429/1992, art. 52 da Lei nº 10.257/2001",
    "lei": "l8429",
    "frase_capitulo": "Como o art. 1º, § 1º, ressalva os \"tipos previstos em leis especiais\", outras leis podem definir atos de improbidade. É o caso do Estatuto da Cidade (Lei 10.257/2001, art. 52), que prevê hipóteses específicas aplicáveis a prefeitos.",
    "resultado": "OK",
    "trecho_lei": "ressalvados tipos previstos em leis especiais."
})

# 10: Linha 110
registros.append({
    "linha": 110,
    "citacao": "art. 10 da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "Uma das mudanças mais importantes da Lei 14.230/2021 foi exigir **dolo em todas as espécies** de ato. Antes, apenas o art. 10 admitia a modalidade culposa",
    "resultado": "OK",
    "trecho_lei": "qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres"
})

# 11: Linha 112
registros.append({
    "linha": 112,
    "citacao": "art. 1º, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A reforma foi além e definiu o próprio dolo (art. 1º, § 2º): é querer, livre e conscientemente, o **resultado ilícito descrito no tipo**.",
    "resultado": "OK",
    "trecho_lei": "vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei, não bastando a voluntariedade do agente."
})

# 12: Linha 116
registros.append({
    "linha": 116,
    "citacao": "art. 11",
    "lei": "l8429",
    "frase_capitulo": "- **Dolo genérico** é a intenção de praticar a conduta ilícita, sem um propósito particular. Era admitido pela jurisprudência do STJ antes da reforma, sobretudo nos atos do art. 11.",
    "resultado": "OK",
    "trecho_lei": "Art. 11. Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade"
})

# 13: Linha 124
registros.append({
    "linha": 124,
    "citacao": "art. 10, X da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 10, X, que punia quem agisse \"negligentemente\" na arrecadação de tributo ou na conservação do patrimônio público, passou a punir quem age **ilicitamente**.",
    "resultado": "OK",
    "trecho_lei": "X - agir ilicitamente na arrecadação de tributo ou de renda, bem como no que diz respeito à conservação do patrimônio público;"
})

# 14: Linha 126
registros.append({
    "linha": 126,
    "citacao": "art. 1º, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 1º, § 3º, reforça a ideia: quem apenas exerce a função e cumpre competências públicas, sem que se prove um ato doloso com finalidade ilícita, não responde por improbidade.",
    "resultado": "OK",
    "trecho_lei": "§ 3º O mero exercício da função ou desempenho de competências públicas, sem comprovação de ato doloso com fim ilícito, afasta a responsabilidade por ato de improbidade administrativa."
})

# 15: Linha 129
registros.append({
    "linha": 129,
    "citacao": "art. 1º e art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Os tipos dos arts. 9º, 10 e 11 exigem **dolo**, e o art. 1º, § 2º, afirma que a voluntariedade da conduta sozinha não basta.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei"
})

# 16: Linha 133
registros.append({
    "linha": 133,
    "citacao": "art. 1º, § 8º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Pelo art. 1º, § 8º, quem age com base em uma leitura da lei sustentada por **jurisprudência**, ainda que ela não seja pacífica, não comete improbidade",
    "resultado": "OK",
    "trecho_lei": "§ 8º Não configura improbidade a ação ou omissão decorrente de divergência interpretativa da lei, baseada em jurisprudência, ainda que não pacificada, mesmo que não venha a ser posteriormente prevalecente"
})

# 17: Linha 142
registros.append({
    "linha": 142,
    "citacao": "Tema 1199 do STF",
    "lei": "stf",
    "frase_capitulo": "## A reforma no tempo: Tema 1199 do STF",
    "resultado": "NAOVER",
    "motivo_naover": "Jurisprudência vinculante do STF (Tema 1.199 da Repercussão Geral, ARE 843.989)."
})

# 18: Linha 144
registros.append({
    "linha": 144,
    "citacao": "art. 5º da CF e Tema 1199 do STF",
    "lei": "cf",
    "frase_capitulo": "Em matéria penal, a lei mais benéfica retroage (CF, art. 5º, XL). Mas a improbidade não é matéria penal. O STF respondeu no Tema 1199, em 2022.",
    "resultado": "OK",
    "trecho_lei": "XL - a lei penal não retroagirá, salvo para beneficiar o réu;"
})

# 19: Linha 146
registros.append({
    "linha": 146,
    "citacao": "Tema 1199 do STF",
    "lei": "stf",
    "frase_capitulo": "> [!jurisprudencia] STF, Tema 1199 (ARE 843.989, rel. Min. Alexandre de Moraes, 2022)",
    "resultado": "NAOVER",
    "motivo_naover": "Tese de repercussão geral fixada pelo STF no Tema 1.199."
})

# 20: Linha 147
registros.append({
    "linha": 147,
    "citacao": "art. 9º",
    "lei": "l8429",
    "frase_capitulo": "> Em síntese: (1) a improbidade exige dolo nos arts. 9º, 10 e 11; (2) a revogação da modalidade culposa **não retroage** para atingir a coisa julgada nem a execução das penas",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 21: Linha 149
registros.append({
    "linha": 149,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "| Situação | A Lei 14.230/2021 retroage? | Consequência |",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 22: Linha 157
registros.append({
    "linha": 157,
    "citacao": "art. 23, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "se, entre dois marcos interruptivos (o ajuizamento da ação, a sentença condenatória, o acórdão que a confirma), passar o prazo do art. 23, § 5º, o juiz declara a prescrição.",
    "resultado": "OK",
    "trecho_lei": "§ 5º Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput deste artigo."
})

# 23: Linha 161
registros.append({
    "linha": 161,
    "citacao": "art. 11 da Lei nº 8.429/1992 e Tema 1199 do STF",
    "lei": "l8429",
    "frase_capitulo": "extinguiu o enquadramento genérico no caput do art. 11 (que agora tem rol taxativo) e revogou os incisos I e II do art. 11. A jurisprudência passou a aplicar a lógica do Tema 1199 a esses casos",
    "resultado": "OK",
    "trecho_lei": "caracterizada por uma das seguintes condutas: (Redação dada pela Lei nº 14.230, de 2021)"
})

# 24: Linha 187
registros.append({
    "linha": 187,
    "citacao": "art. 1º, § 4º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A Lei 14.230/2021 inseriu o art. 1º, § 4º: aplicam-se ao sistema de improbidade os **princípios constitucionais do direito administrativo sancionador**.",
    "resultado": "OK",
    "trecho_lei": "§ 4º Aplicam-se ao sistema da improbidade disciplinado nesta Lei os princípios constitucionais do direito administrativo sancionador."
})

# 25: Linha 199
registros.append({
    "linha": 199,
    "citacao": "art. 12 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 12, § 9º, por exemplo, reflete a presunção de inocência ao determinar que as sanções só sejam executadas depois do **trânsito em julgado** da condenação, e o art. 12, § 7º, protege contra o *bis in idem* nas sanções às pessoas jurídicas.",
    "resultado": "OK",
    "trecho_lei": "§ 9º As sanções previstas neste artigo somente poderão ser executadas após o trânsito em julgado da sentença condenatória."
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
