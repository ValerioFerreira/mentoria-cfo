# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m21_a22-s13-p3"

registros = [
    {
        "linha": 288,
        "citacao": "art. 158, § 4º da Lei nº 14.133/2021",
        "lei": "l14133",
        "frase_capitulo": "- A pretensão punitiva prescreve em cinco anos contados da ciência inequívoca da infração pela Administração Pública (art. 158, § 4º).",
        "resultado": "OK",
        "trecho_lei": "§ 4º A prescrição ocorrerá em 5 (cinco) anos, contados da ciência da infração pela Administração, e será:"
    }
]

output_data = {
    "unidade": unit_id,
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": registros
}

with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
    json.dump(output_data, out, ensure_ascii=False, indent=1)
print("Draft saved.")
