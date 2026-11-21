# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s06-p3"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

registros = []

# 1: Linha 164
registros.append({
    "linha": 164,
    "citacao": "art. 22 e art. 23, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Inquérito Civil Público** | Conduzido pelo MP com prazo de 365 dias corridos prorrogável uma vez por igual período. | Art. 22 e art. 23, § 2º |",
    "resultado": "OK",
    "trecho_lei": "§ 2º O inquérito civil para apuração do ato de improbidade será concluído no prazo de 365 (trezentos e sessenta e cinco) dias corridos, prorrogável uma única vez por igual período"
})

# 2: Linha 169
registros.append({
    "linha": 169,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A sentença penal absolutória vincula compulsoriamente a ação de improbidade quando fundada em negativa de autoria ou inexistência material do fato (art. 21, § 3º).",
    "resultado": "OK",
    "trecho_lei": "§ 3º As sentenças civis e penais produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria."
})

# 3: Linha 170
registros.append({
    "linha": 170,
    "citacao": "art. 21, § 4º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- O STF declarou inconstitucional o art. 21, § 4º, nas ADIs 7156 e 7236, afastando a vinculação da improbidade em casos de absolvição penal por insuficiência de provas.",
    "resultado": "OK",
    "trecho_lei": "§ 4º A absolvição criminal em ação que discuta os mesmos fatos, confirmada por decisão colegiada, impede o trâmite da ação da qual trata esta Lei"
})

# 4: Linha 171
registros.append({
    "linha": 171,
    "citacao": "art. 12, § 6º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A reparação do dano em improbidade deduz os valores já ressarcidos nas esferas penal, civil e administrativa pelos mesmos fatos (art. 12, § 6º).",
    "resultado": "OK",
    "trecho_lei": "§ 6º Se ocorrer lesão ao patrimônio público, a reparação do dano a que se refere esta Lei deverá deduzir o ressarcimento ocorrido nas instâncias criminal, civil e administrativa"
})

# 5: Linha 172
registros.append({
    "linha": 172,
    "citacao": "art. 13 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A entrega de declaração de imposto de renda à Receita Federal é condição para a posse e exercício, sendo atualizada anualmente e no desligamento do agente público (art. 13).",
    "resultado": "OK",
    "trecho_lei": "Art. 13. A posse e o exercício de agente público ficam condicionados à apresentação de declaração de imposto de renda e proventos de qualquer natureza"
})

# 6: Linha 173
registros.append({
    "linha": 173,
    "citacao": "art. 13, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A recusa voluntária na apresentação da declaração de bens ou a prestação de informações falsas sujeita o servidor à pena de demissão (art. 13, § 3º).",
    "resultado": "OK",
    "trecho_lei": "§ 3º Será apenado com a pena de demissão, sem prejuízo de outras sanções cabíveis, o agente público que se recusar a prestar a declaração dos bens a que se refere o caput deste artigo"
})

# 7: Linha 174
registros.append({
    "linha": 174,
    "citacao": "art. 14, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A representação administrativa por improbidade exige a qualificação do representante, narrativa circunstanciada do fato e indicação de provas conhecidas (art. 14, § 1º).",
    "resultado": "OK",
    "trecho_lei": "§ 1º A representação, que será escrita ou reduzida a termo e assinada, conterá a qualificação do representante, as informações sobre o fato e sua autoria e a indicação das provas de que tenha conhecimento."
})

# 8: Linha 175
registros.append({
    "linha": 175,
    "citacao": "art. 23, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- O inquérito civil para apuração de improbidade tem prazo legal de 365 dias corridos, admitida prorrogação única por idêntico intervalo (art. 23, § 2º).",
    "resultado": "OK",
    "trecho_lei": "mediante ato fundamentado submetido à revisão da instância competente do órgão ministerial, conforme dispuser a respectiva lei orgânica."
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
