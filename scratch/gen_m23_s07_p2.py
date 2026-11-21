# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s07-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

registros = []

# 1: Linha 121
registros.append({
    "linha": 121,
    "citacao": "art. 17-B, § 4º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A Lei nº 14.230/2021 estruturou de forma minuciosa a solução consensual na improbidade administrativa por meio do Acordo de Não Persecução Civil (ANPC), disciplinado no art. 17-B. O termo de ajustamento pode ser pactuado tanto no curso do inquérito civil quanto na fase judicial ou na execução da sentença condenatória (Lei nº 8.429/1992, art. 17-B, § 4º).",
    "resultado": "OK",
    "trecho_lei": "§ 4º O acordo a que se refere o caput deste artigo poderá ser celebrado no curso da investigação de apuração do ilícito, no curso da ação de improbidade ou no momento da execução da sentença condenatória."
})

# 2: Linha 125
registros.append({
    "linha": 125,
    "citacao": "art. 17-B da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Para a celebração válida do acordo resolutivo, o art. 17-B impõe a obtenção cumulativa de resultados materiais inafastáveis:",
    "resultado": "OK",
    "trecho_lei": "Art. 17-B. O Ministério Público poderá, conforme as circunstâncias do caso concreto, celebrar acordo de não persecução civil, desde que dele advenham, ao menos, os seguintes resultados:"
})

# 3: Linha 126
registros.append({
    "linha": 126,
    "citacao": "art. 17-B, I da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "1. **Ressarcimento integral do dano:** obrigação compulsória de recompor todo o prejuízo econômico infligido ao erário (Lei nº 8.429/1992, art. 17-B, I);",
    "resultado": "OK",
    "trecho_lei": "I - o integral ressarcimento do dano;"
})

# 4: Linha 127
registros.append({
    "linha": 127,
    "citacao": "art. 17-B, II da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "2. **Reversão da vantagem indevida:** devolução integral à pessoa jurídica prejudicada de qualquer proveito patrimonial ilícito auferido (Lei nº 8.429/1992, art. 17-B, II).",
    "resultado": "OK",
    "trecho_lei": "II - a reversão à pessoa jurídica lesada da vantagem indevida obtida, ainda que oriunda de agentes privados."
})

# 5: Linha 131
registros.append({
    "linha": 131,
    "citacao": "art. 17-B, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A eficácia do ANPC subordina-se a formalidades procedimentais estritas (Lei nº 8.429/1992, art. 17-B, § 1º):",
    "resultado": "OK",
    "trecho_lei": "§ 1º A celebração do acordo a que se refere o caput deste artigo dependerá, cumulativamente:"
})

# 6: Linha 137
registros.append({
    "linha": 137,
    "citacao": "art. 17-B, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> O art. 17-B, § 3º, exigia a oitiva obrigatória do Tribunal de Contas no prazo de 90 dias para manifestação sobre os parâmetros do dano a ressarcir. No julgamento das ADIs 7156 e 7236, o Supremo Tribunal Federal declarou a **inconstitucionalidade do art. 17-B, § 3º**",
    "resultado": "OK",
    "trecho_lei": "deverá ser realizada a oitiva do Tribunal de Contas competente, que se manifestará, com indicação dos parâmetros utilizados, no prazo de 90 (noventa) dias."
})

# 7: Linha 141
registros.append({
    "linha": 141,
    "citacao": "art. 17-B, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Na dosagem e celebração do ANPC, as partes considerarão a personalidade do agente, a natureza, as circunstâncias, a gravidade e a repercussão social do ato, bem como as vantagens práticas da rápida resolução do caso para o interesse público (Lei nº 8.429/1992, art. 17-B, § 2º).",
    "resultado": "OK",
    "trecho_lei": "§ 2º Em qualquer caso, a celebração do acordo a que se refere o caput deste artigo considerará a personalidade do agente, a natureza, as circunstâncias, a gravidade e a repercussão social do ato de improbidade"
})

# 8: Linha 143
registros.append({
    "linha": 143,
    "citacao": "art. 17-B, § 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Ademais, para coibir a má-fé, o art. 17-B, § 7º, prescreve que o investigado ou demandado que descumprir injustificadamente as cláusulas pactuadas no acordo **ficará impedido de celebrar novo ANPC pelo prazo de 5 (cinco) anos**, contado do conhecimento do efetivo descumprimento pelo Ministério Público.",
    "resultado": "OK",
    "trecho_lei": "§ 7º Em caso de descumprimento do acordo a que se refere o caput deste artigo, o investigado ou o demandado ficará impedido de celebrar novo acordo pelo prazo de 5 (cinco) anos"
})

# 9: Linha 159
registros.append({
    "linha": 159,
    "citacao": "art. 10 e art. 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O Ministério Público ajuizou ação de improbidade capitulando a conduta no art. 11 da LIA. Durante o processo, restou apurado que a contratação gerou sobrepreço e benefício ilícito ao fornecedor (art. 10), tendo sido narrados com detalhes todos os fatos na inicial.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei"
})

# 10: Linha 162
registros.append({
    "linha": 162,
    "citacao": "art. 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> 1. Conforme assentado pelo STF nas ADIs 7156 e 7236, o magistrado fica vinculado aos fatos narrados na petição inicial, sendo inconstitucional a proibição de enquadrar a conduta no tipo correto do art. 10 da LIA, assegurado o contraditório prévio.",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa"
})

# 11: Linha 164
registros.append({
    "linha": 164,
    "citacao": "art. 17-B, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> 3. A proposta de ANPC não depende de oitiva prévia do Tribunal de Contas, haja vista que o STF declarou inconstitucional o art. 17-B, § 3º, da LIA, bastando a oitiva do ente municipal lesado, a aprovação institucional e a homologação judicial indispensável.",
    "resultado": "OK",
    "trecho_lei": "com indicação dos parâmetros utilizados, no prazo de 90 (noventa) dias. (Incluído pela Lei nº 14.230, de 2021) (Vide ADI 7236) (Vide ADI 7156)"
})

# 12: Linha 173
registros.append({
    "linha": 173,
    "citacao": "art. 17, § 7º da Lei nº 8.429/1992, art. 219 e art. 231 do CPC",
    "lei": "l8429",
    "frase_capitulo": "| **Prazo de Contestação** | **30 dias úteis** contados na forma do CPC (CPC, art. 219 e art. 231). | Art. 17, § 7º |",
    "resultado": "OK",
    "trecho_lei": "ordenará a citação dos requeridos para que a contestem no prazo comum de 30 (trinta) dias, iniciado o prazo na forma do art. 231 da Lei nº 13.105, de 16 de março de 2015"
})

# 13: Linha 174
registros.append({
    "linha": 174,
    "citacao": "art. 17, § 19, I da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Efeitos da Revelia** | Inaplicabilidade da presunção de veracidade das alegações fáticas. | Art. 17, § 19, I |",
    "resultado": "OK",
    "trecho_lei": "I - a presunção de veracidade dos fatos alegados pelo autor em caso de revelia;"
})

# 14: Linha 175
registros.append({
    "linha": 175,
    "citacao": "art. 17, § 19, IV, e art. 17-C, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Remessa Necessária** | Inexistência de reexame obrigatório em caso de improcedência da demanda. | Art. 17, § 19, IV, e art. 17-C, § 3º |",
    "resultado": "OK",
    "trecho_lei": "§ 3º Não haverá remessa necessária nas sentenças de que trata esta Lei."
})

# 15: Linha 177
registros.append({
    "linha": 177,
    "citacao": "art. 17, §§ 16 e 17 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Conversão em ACP** | Conversão em ação civil pública comum cabendo agravo de instrumento. | Art. 17, §§ 16 e 17 |",
    "resultado": "OK",
    "trecho_lei": "§ 17. Da decisão que converter a ação de improbidade em ação civil pública caberá agravo de instrumento."
})

# 16: Linha 178
registros.append({
    "linha": 178,
    "citacao": "art. 17, § 20 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Defesa por Procuradoria** | Faculdade da advocacia pública quando o ato fundar-se em parecer prévio. | Art. 17, § 20, e ADIs 7042/7043 |",
    "resultado": "OK",
    "trecho_lei": "A assessoria jurídica que emitiu o parecer atestando a legalidade prévia dos atos administrativos praticados pelo administrador público ficará obrigada a defendê-lo judicialmente"
})

# 17: Linha 179
registros.append({
    "linha": 179,
    "citacao": "art. 17-B da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **ANPC: Resultados** | Integral recomposição do dano e reversão da vantagem ilícita obtida. | Art. 17-B, caput |",
    "resultado": "OK",
    "trecho_lei": "celebrar acordo de não persecução civil, desde que dele advenham, ao menos, os seguintes resultados:"
})

# 18: Linha 180
registros.append({
    "linha": 180,
    "citacao": "art. 17-B, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **ANPC: Procedimento** | Oitiva do ente lesado, homologação do juiz e aprovação do órgão do MP em 60 dias. | Art. 17-B, § 1º |",
    "resultado": "OK",
    "trecho_lei": "I - da oitiva do ente federativo lesado, em momento anterior ou posterior à propositura da ação;"
})

# 19: Linha 182
registros.append({
    "linha": 182,
    "citacao": "art. 17-B, § 7º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Descumprimento de ANPC** | Gera impedimento de celebração de novo acordo pelo prazo de 5 anos. | Art. 17-B, § 7º |",
    "resultado": "OK",
    "trecho_lei": "o investigado ou o demandado ficará impedido de celebrar novo acordo pelo prazo de 5 (cinco) anos, contado do conhecimento pelo Ministério Público do efetivo descumprimento."
})

# 20: Linha 191
registros.append({
    "linha": 191,
    "citacao": "art. 17, §§ 16 e 17 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- É facultado ao magistrado converter a ação de improbidade em ação civil pública comum, cabendo agravo de instrumento dessa decisão (art. 17, §§ 16 e 17).",
    "resultado": "OK",
    "trecho_lei": "converter a ação de improbidade administrativa em ação civil pública, regulada pela Lei nº 7.347, de 24 de julho de 1985."
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

        if tl not in l8429:
            errors.append(f"Row {idx+1}: trecho_lei not in l8429: '{tl}'")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  -", e)
else:
    print(f"All {len(registros)} rows verified locally! Writing draft...")
    with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, ensure_ascii=False, indent=1)
    print("Draft saved.")
