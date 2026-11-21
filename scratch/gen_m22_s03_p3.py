# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s03-p3"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

registros = []

# 1: Linha 185
registros.append({
    "linha": 185,
    "citacao": "art. 9º, V da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "8. Aceitar a promessa de vantagem já configura o inciso V do art. 9º.",
    "resultado": "OK",
    "trecho_lei": "de contrabando, de usura ou de qualquer outra atividade ilícita, ou aceitar promessa de tal vantagem;"
})

output_data = {
    "unidade": unit_id,
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": registros
}

# Verifications
errors = []
for idx, r in enumerate(registros):
    fc = r["frase_capitulo"]
    if fc not in chapter_content:
        errors.append(f"Row {idx+1} (linha {r['linha']}): frase_capitulo not in chapter!")
    tl = r.get("trecho_lei", "")
    if tl not in l8429:
        errors.append(f"Row {idx+1}: trecho_lei not in l8429: '{tl}'")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  -", e)
else:
    print(f"Verified! Writing draft...")
    with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, ensure_ascii=False, indent=1)
    print("Draft saved.")
