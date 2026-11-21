# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s02-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

registros = []

# 1: Linha 193
registros.append({
    "linha": 193,
    "citacao": "Art. 3º, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Terceiro | Art. 3º, caput | Induzir ou concorrer dolosamente | Aplica-se a lei no que couber; não age isoladamente |",
    "resultado": "OK",
    "trecho_lei": "Art. 3º As disposições desta Lei são aplicáveis, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
})

# 2: Linha 194
registros.append({
    "linha": 194,
    "citacao": "Art. 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Pessoa jurídica | Art. 3º | Mesmos requisitos do terceiro | Não sofre perda de função nem suspensão de direitos políticos |",
    "resultado": "OK",
    "trecho_lei": "§ 2º As sanções desta Lei não se aplicarão à pessoa jurídica, caso o ato de improbidade administrativa seja também sancionado como ato lesivo à administração pública"
})

# 3: Linha 195
registros.append({
    "linha": 195,
    "citacao": "Art. 3º, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Sócios e colaboradores | Art. 3º, § 1º | Participação comprovada | Respondem nos limites da participação |",
    "resultado": "OK",
    "trecho_lei": "§ 1º Os sócios, os cotistas, os diretores e os colaboradores de pessoa jurídica de direito privado não respondem pelo ato de improbidade que venha a ser imputado à pessoa jurídica"
})

# 4: Linha 196
registros.append({
    "linha": 196,
    "citacao": "Arts. 8º e 8º-A da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Sucessores | Arts. 8º e 8º-A | Sucessão por herança ou por operação societária | Só reparação, até o patrimônio transferido |",
    "resultado": "OK",
    "trecho_lei": "Art. 8º-A A responsabilidade sucessória de que trata o art. 8º desta Lei aplica-se também na hipótese de alteração contratual, de transformação, de incorporação, de fusão ou de cisão societária."
})

# 5: Linha 207
registros.append({
    "linha": 207,
    "citacao": "art. 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Agente político | Incluído no art. 2º | Excluí-lo |",
    "resultado": "OK",
    "trecho_lei": "Art. 2º Para os efeitos desta Lei, consideram-se agente público o agente político, o servidor público e todo aquele que exerce"
})

# 6: Linha 218
registros.append({
    "linha": 218,
    "citacao": "art. 2º e art. 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "1. Sujeito ativo é o agente público (art. 2º) e o terceiro que induz ou concorre (art. 3º).",
    "resultado": "OK",
    "trecho_lei": "mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
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
