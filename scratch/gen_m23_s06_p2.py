# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s06-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cpp.clean.txt", "r", encoding="utf-8") as f:
    cpp = f.read()

registros = []

# 1: Linha 97
registros.append({
    "linha": 97,
    "citacao": "art. 13, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "2. Com periodicidade **anual**, para acompanhamento da evolução patrimonial (art. 13, § 2º);",
    "resultado": "OK",
    "trecho_lei": "§ 2º A declaração de bens a que se refere o caput deste artigo será atualizada anualmente e na data em que o agente público deixar o exercício do mandato, do cargo, do emprego ou da função."
})

# 2: Linha 98
registros.append({
    "linha": 98,
    "citacao": "art. 13, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "3. No momento em que o servidor **cessar o exercício** de suas atribuições públicas (art. 13, § 2º).",
    "resultado": "OK",
    "trecho_lei": "atualizada anualmente e na data em que o agente público deixar o exercício do mandato, do cargo, do emprego ou da função."
})

# 3: Linha 100
registros.append({
    "linha": 100,
    "citacao": "art. 13, §§ 1º e 4º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "É fundamental notar que a Lei nº 14.230/2021 **revogou** os antigos §§ 1º e 4º do art. 13. O antigo § 1º continha uma lista minuciosa de bens a declarar (imóveis, móveis, semoventes, bens de cônjuge e dependentes), e o antigo § 4º tratava de autorização de acesso a dados.",
    "resultado": "OK",
    "trecho_lei": "A declaração compreenderá imóveis, móveis, semoventes, dinheiro, títulos, ações, e qualquer outra espécie de bens e valores patrimoniais"
})

# 4: Linha 114
registros.append({
    "linha": 114,
    "citacao": "art. 13, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- Aquele que se recusar a cumprir essa obrigação cadastral no prazo fixado ou que prestar declarações inverídicas sofrerá a penalidade funcional de **demissão** (art. 13, § 3º).",
    "resultado": "OK",
    "trecho_lei": "§ 3º Será apenado com a pena de demissão, sem prejuízo de outras sanções cabíveis, o agente público que se recusar a prestar a declaração dos bens a que se refere o caput deste artigo"
})

# 5: Linha 115
registros.append({
    "linha": 115,
    "citacao": "art. 13, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- A redação atualizada do art. 13, § 3º, prevê a sanção de \"demissão\" simples, sem a antiga locução \"a bem do serviço público\", uniformizando a terminologia sancionatória funcional.",
    "resultado": "OK",
    "trecho_lei": "§ 3º Será punido com a pena de demissão, a bem do serviço público, sem prejuízo de outras sanções cabíveis, o agente público que se recusar a prestar declaração dos bens"
})

# 6: Linha 119
registros.append({
    "linha": 119,
    "citacao": "arts. 14, 15 e 22 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A persecução dos atos de improbidade pode ter início perante a própria Administração Pública ou no âmbito do Ministério Público. Os arts. 14, 15 e 22 da Lei nº 8.429/1992 estruturam o procedimento de apuração preliminar.",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO V Do Procedimento Administrativo e do Processo Judicial"
})

# 7: Linha 125
registros.append({
    "linha": 125,
    "citacao": "art. 14, §§ 1º e 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 14, §§ 1º e 2º, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "§ 1º A representação, que será escrita ou reduzida a termo e assinada, conterá a qualificação do representante, as informações sobre o fato e sua autoria e a indicação das provas de que tenha conhecimento."
})

# 8: Linha 127
registros.append({
    "linha": 127,
    "citacao": "art. 14, § 2º e art. 22 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> § 2º A autoridade administrativa rejeitará a representação, em despacho fundamentado, se esta não contiver as formalidades estabelecidas no § 1º deste artigo. A rejeição não impede a representação ao Ministério Público, nos termos do art. 22 desta lei.",
    "resultado": "OK",
    "trecho_lei": "§ 2º A autoridade administrativa rejeitará a representação, em despacho fundamentado, se esta não contiver as formalidades estabelecidas no § 1º deste artigo. A rejeição não impede a representação ao Ministério Público, nos termos do art. 22 desta lei."
})

# 9: Linha 136
registros.append({
    "linha": 136,
    "citacao": "art. 22 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O Ministério Público possui ampla atribuição para investigar atos de improbidade administrativa. O art. 22 da LIA delimita suas prerrogativas:",
    "resultado": "OK",
    "trecho_lei": "Art. 22. Para apurar qualquer ilícito previsto nesta Lei, o Ministério Público, de ofício, a requerimento de autoridade administrativa ou mediante representação formulada de acordo com o disposto no art. 14 desta Lei"
})

# 10: Linha 137
registros.append({
    "linha": 137,
    "citacao": "art. 22, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Procedimentos investigativos:** o órgão ministerial pode instaurar inquérito civil, conduzir procedimentos preparatórios sumários ou requisitar a apuração criminal à autoridade policial competente (art. 22, caput).",
    "resultado": "OK",
    "trecho_lei": "poderá instaurar inquérito civil ou procedimento investigativo assemelhado e requisitar a instauração de inquérito policial."
})

# 11: Linha 138
registros.append({
    "linha": 138,
    "citacao": "art. 22, parágrafo único da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Garantia de contraditório preliminar:** no curso do procedimento de apuração, assegura-se ao investigado a prerrogativa formal de apresentar manifestação escrita e juntar elementos de prova que auxiliem na elucidação dos acontecimentos (art. 22, parágrafo único).",
    "resultado": "OK",
    "trecho_lei": "Parágrafo único. Na apuração dos ilícitos previstos nesta Lei, será garantido ao investigado a oportunidade de manifestação por escrito e de juntada de documentos"
})

# 12: Linha 139
registros.append({
    "linha": 139,
    "citacao": "art. 23, § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Prazo do inquérito civil:** o procedimento investigativo ministerial possui prazo legal de **365 dias corridos**, comportando prorrogação justificada única por igual período mediante decisão fundamentada, conforme estipulado expressamente no **art. 23, § 2º**, da Lei nº 8.429/1992.",
    "resultado": "OK",
    "trecho_lei": "§ 2º O inquérito civil para apuração do ato de improbidade será concluído no prazo de 365 (trezentos e sessenta e cinco) dias corridos, prorrogável uma única vez por igual período"
})

# 13: Linha 140
registros.append({
    "linha": 140,
    "citacao": "art. 19 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Crime de representação caluniosa (art. 19):** é crime punido com detenção e multa acionar autoridade ou o Ministério Público contra pessoa sabidamente inocente.",
    "resultado": "OK",
    "trecho_lei": "Art. 19. Constitui crime a representação por ato de improbidade contra agente público ou terceiro beneficiário, quando o autor da denúncia o sabe inocente."
})

# 14: Linha 144
registros.append({
    "linha": 144,
    "citacao": "art. 386, I do Código de Processo Penal",
    "lei": "cpp",
    "frase_capitulo": "No juízo criminal, após instrução detalhada, foi proferida sentença penal absolutória transitada em julgado com base na comprovação cabal de inexistência material do fato (CPP, art. 386, I).",
    "resultado": "OK",
    "trecho_lei": "I - estar provada a inexistência do fato;"
})

# 15: Linha 147
registros.append({
    "linha": 147,
    "citacao": "art. 12 e art. 21, § 3º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "> A condenação cível é manifestamente ilegal. Embora vigore a regra geral da independência das instâncias (art. 12 da LIA), o art. 21, § 3º, introduzido pela Lei nº 14.230/2021, determina expressamente que as sentenças penais produzem efeitos vinculantes imediatos sobre a ação de improbidade quando concluírem pela inexistência do fato ou pela negativa de autoria.",
    "resultado": "OK",
    "trecho_lei": "§ 3º As sentenças civis e penais produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria."
})

# 16: Linha 153
registros.append({
    "linha": 153,
    "citacao": "Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Tema Central | Regra Positivada | Fundamento na Lei nº 8.429/1992 |",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 17: Linha 155
registros.append({
    "linha": 155,
    "citacao": "art. 12, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Independência das Instâncias** | As esferas penal, civil, disciplinar e de improbidade são autônomas e cumuláveis. | Art. 12, caput |",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade"
})

# 18: Linha 156
registros.append({
    "linha": 156,
    "citacao": "art. 21, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Vinculação da Decisão Penal** | A sentença penal por inexistência do fato ou negativa de autoria vincula a ação de improbidade. | Art. 21, § 3º |",
    "resultado": "OK",
    "trecho_lei": "produzirão efeitos em relação à ação de improbidade quando concluírem pela inexistência da conduta ou pela negativa da autoria."
})

# 19: Linha 157
registros.append({
    "linha": 157,
    "citacao": "art. 21, § 4º da Lei nº 8.429/1992 e art. 386 do CPP",
    "lei": "l8429",
    "frase_capitulo": "| **Inconstitucionalidade do § 4º** | O STF invalidou a vinculação por todos os incisos do art. 386 do CPP (ADIs 7156 e 7236). | STF (ADIs 7156 e 7236) |",
    "resultado": "OK",
    "trecho_lei": "havendo comunicação com todos os fundamentos de absolvição previstos no art. 386 do Decreto-Lei nº 3.689, de 3 de outubro de 1941 (Código de Processo Penal)."
})

# 20: Linha 158
registros.append({
    "linha": 158,
    "citacao": "art. 12, § 6º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Dedução do Ressarcimento** | O ressarcimento deduz quantias já recuperadas nas instâncias penal, civil ou administrativa. | Art. 12, § 6º |",
    "resultado": "OK",
    "trecho_lei": "§ 6º Se ocorrer lesão ao patrimônio público, a reparação do dano a que se refere esta Lei deverá deduzir o ressarcimento ocorrido nas instâncias criminal, civil e administrativa"
})

# 21: Linha 159
registros.append({
    "linha": 159,
    "citacao": "art. 21, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Compensação de Sanções** | Sanções pecuniárias aplicadas em outras esferas devem ser compensadas com as da LIA. | Art. 21, § 5º |",
    "resultado": "OK",
    "trecho_lei": "Sanções eventualmente aplicadas em outras esferas deverão ser compensadas com as sanções aplicadas nos termos desta Lei."
})

# 22: Linha 160
registros.append({
    "linha": 160,
    "citacao": "art. 12, § 7º da Lei nº 8.429/1992 e Lei nº 12.846/2013",
    "lei": "l8429",
    "frase_capitulo": "| **Non bis in idem** | Aplicação harmônica e não cumulativa de sanções com a Lei nº 12.846/2013. | Art. 12, § 7º |",
    "resultado": "OK",
    "trecho_lei": "As sanções aplicadas a pessoas jurídicas com base nesta Lei e na Lei nº 12.846, de 1º de agosto de 2013, deverão observar o princípio constitucional do non bis in idem."
})

# 23: Linha 161
registros.append({
    "linha": 161,
    "citacao": "art. 13, caput e § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Declaração de Bens** | Apresentação da declaração de imposto de renda da Receita Federal na posse, anualmente e no desligamento. | Art. 13, caput e § 2º |",
    "resultado": "OK",
    "trecho_lei": "Art. 13. A posse e o exercício de agente público ficam condicionados à apresentação de declaração de imposto de renda e proventos de qualquer natureza"
})

# 24: Linha 162
registros.append({
    "linha": 162,
    "citacao": "art. 13, § 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Punição por Recusa** | Sujeita o agente faltoso à penalidade disciplinar de demissão. | Art. 13, § 3º |",
    "resultado": "OK",
    "trecho_lei": "caput deste artigo dentro do prazo determinado ou que prestar declaração falsa."
})

# 25: Linha 163
registros.append({
    "linha": 163,
    "citacao": "art. 14, § 1º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **Representação Cidadã** | Exige qualificação do representante, narrativa do fato e indicação de provas. | Art. 14, § 1º |",
    "resultado": "OK",
    "trecho_lei": "as informações sobre o fato e sua autoria e a indicação das provas de que tenha conhecimento."
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

        law_txt = cpp if r["lei"] == "cpp" else l8429
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
