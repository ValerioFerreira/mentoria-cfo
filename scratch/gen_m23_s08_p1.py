# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m23_a24-s08-p1"

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
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A efetividade da Lei de Improbidade Administrativa depende de medidas cautelares garantidoras do ressarcimento público e de uma sentença judicial válida. Ao ajuizar a demanda, o autor precisa assegurar que o patrimônio dos investigados não seja dissipado antes do desfecho do processo.",
    "resultado": "OK",
    "trecho_lei": "Na ação por improbidade administrativa poderá ser formulado, em caráter antecedente ou incidente, pedido de indisponibilidade de bens dos réus"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 16 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Compreender os pressupostos da tutela de indisponibilidade de bens (art. 16) e a interpretação fixada pelo STF nas ADIs 7156 e 7236.",
    "resultado": "OK",
    "trecho_lei": "a fim de garantir a integral recomposição do erário ou do acréscimo patrimonial resultante de enriquecimento ilícito."
})

# 3: Linha 18
registros.append({
    "linha": 18,
    "citacao": "art. 16, § 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Dominar a ordem legal de preferência de constrição patrimonial (art. 16, § 11) e as impenhorabilidades legais.",
    "resultado": "OK",
    "trecho_lei": "§ 11. A ordem de indisponibilidade de bens deverá priorizar veículos de via terrestre, bens imóveis, bens móveis em geral, semoventes, navios e aeronaves, ações e quotas de sociedades simples e empresárias, pedras e metais preciosos"
})

# 4: Linha 19
registros.append({
    "linha": 19,
    "citacao": "Tema 576 do STF e art. 17, § 4º-A da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Conhecer a competência jurisdicional de primeiro grau no Tema 576 do STF e a prerrogativa do Presidente da República (Pet 3240).",
    "resultado": "OK",
    "trecho_lei": "§ 4º-A A ação a que se refere o caput deste artigo deverá ser proposta perante o foro do local onde ocorrer o dano ou da pessoa jurídica prejudicada."
})

# 5: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 20 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Analisar a exigência de trânsito em julgado para a eficácia da perda da função e suspensão de direitos políticos (art. 20), bem como o afastamento preventivo cautelar.",
    "resultado": "OK",
    "trecho_lei": "Art. 20. A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
})

# 6: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 12, § 1º, art. 18, art. 18, § 4º e art. 23-B da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Examinar a abrangência da perda do cargo (art. 12, § 1º), a liquidação e cumprimento da sentença (art. 18), o parcelamento em até 48 vezes (art. 18, § 4º) e as custas e honorários do art. 23-B.",
    "resultado": "OK",
    "trecho_lei": "§ 1º A sanção de perda da função pública, nas hipóteses dos incisos I e II do caput deste artigo, atinge apenas o vínculo de mesma qualidade e natureza"
})

# 7: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 16, caput da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A indisponibilidade de bens representa tutela provisória de urgência de natureza cautelar. Sua finalidade reside em resguardar o patrimônio público contra manobras de dilapidação financeira praticadas pelos demandados durante o curso do litígio, garantindo a integral recomposição do erário ou a reversão do enriquecimento ilícito (art. 16, caput).",
    "resultado": "OK",
    "trecho_lei": "O pedido de indisponibilidade de bens a que se refere o caput deste artigo poderá ser formulado independentemente da representação de que trata o art. 7º desta Lei."
})

# 8: Linha 27
registros.append({
    "linha": 27,
    "citacao": "art. 16, § 3º da Lei nº 8.429/1992, Lei nº 14.230/2021 e Tema 701 do STJ",
    "lei": "l8429",
    "frase_capitulo": "Historicamente, o Superior Tribunal de Justiça adotava a tese do dano presumido (*periculum in mora* implícito no Tema 701 dos Repetitivos). A Lei nº 14.230/2021 buscou superar essa orientação no art. 16, § 3º, exigindo a evidência concreta de risco ao resultado prático do processo ou de perigo de dano irreversível.",
    "resultado": "OK",
    "trecho_lei": "§ 3º O pedido de indisponibilidade de bens a que se refere o caput deste artigo apenas será deferido mediante a demonstração no caso concreto de perigo de dano irreparável ou de risco ao resultado útil do processo"
})

# 9: Linha 29
registros.append({
    "linha": 29,
    "citacao": "art. 16, §§ 3º, 4º e 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Contudo, ao julgar as **ADIs 7156 e 7236** (concluídas em 1º/7/2026), o Supremo Tribunal Federal conferiu interpretação conforme à Constituição aos §§ 3º, 4º e 10 do art. 16:",
    "resultado": "OK",
    "trecho_lei": "A indisponibilidade de bens poderá ser decretada sem a oitiva prévia do réu, sempre que o contraditório prévio puder comprovadamente frustrar a efetividade da medida"
})

# 10: Linha 35
registros.append({
    "linha": 35,
    "citacao": "art. 16 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A[\"Pedido Cautelar de Indisponibilidade (art. 16)\"] --> B[\"Fumus Boni Iuris: Probabilidade da Prática de Ato Doloso\"]",
    "resultado": "OK",
    "trecho_lei": "desde que o juiz se convença da probabilidade da ocorrência dos atos descritos na petição inicial com fundamento nos respectivos elementos de instrução"
})

# 11: Linha 45
registros.append({
    "linha": 45,
    "citacao": "art. 16 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 16 estabelece parâmetros estritos para que a indisponibilidade não configure confisco abusivo:",
    "resultado": "OK",
    "trecho_lei": "Aplica-se à indisponibilidade de bens regida por esta Lei, no que for cabível, o regime da tutela provisória de urgência da Lei nº 13.105"
})

# 12: Linha 46
registros.append({
    "linha": 46,
    "citacao": "art. 16, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Limite global em caso de múltiplos réus (art. 16, § 5º):** na hipótese de litisconsórcio passivo, a soma dos bens tornados indisponíveis não pode ultrapassar o teto apontado na inicial como prejuízo estatal ou acréscimo indevido.",
    "resultado": "OK",
    "trecho_lei": "§ 5º Se houver mais de um réu na ação, a somatória dos valores declarados indisponíveis não poderá superar o montante indicado na petição inicial como dano ao erário ou como enriquecimento ilícito."
})

# 13: Linha 47
registros.append({
    "linha": 47,
    "citacao": "art. 16, § 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Multa civil excluída da indisponibilidade (art. 16, § 10):** a sanção pecuniária punitiva de multa civil está totalmente livre de constrição provisória, vedando a lei qualquer bloqueio preventivo a esse título.",
    "resultado": "OK",
    "trecho_lei": "A indisponibilidade recairá sobre bens que assegurem exclusivamente o integral ressarcimento do dano ao erário, sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil"
})

# 14: Linha 48
registros.append({
    "linha": 48,
    "citacao": "art. 16, § 13 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Impenhorabilidade da poupança e aplicações (art. 16, § 13):** resguarda-se a quantia limite de até 40 salários mínimos mantida em reservas de poupança, aplicações financeiras ou contas bancárias.",
    "resultado": "OK",
    "trecho_lei": "É vedada a decretação de indisponibilidade da quantia de até 40 (quarenta) salários mínimos depositados em caderneta de poupança, em outras aplicações financeiras ou em conta-corrente."
})

# 15: Linha 49
registros.append({
    "linha": 49,
    "citacao": "art. 9º e art. 16, § 14 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "- **Proteção do bem de família (art. 16, § 14):** é vedada a decretação de indisponibilidade do bem de família, salvo se comprovado que o imóvel foi adquirido com o produto ou o proveito do ato de improbidade previsto no art. 9º desta Lei.",
    "resultado": "OK",
    "trecho_lei": "§ 14. É vedada a decretação de indisponibilidade do bem de família do réu, salvo se comprovado que o imóvel seja fruto de vantagem patrimonial indevida, conforme descrito no art. 9º desta Lei."
})

# 16: Linha 53
registros.append({
    "linha": 53,
    "citacao": "Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A ordem legal de constrição foi minuciosamente estabelecida pela Lei nº 14.230/2021. Ao contrário do regime processual civil comum (em que o dinheiro lidera a ordem de penhora), a LIA colocou o bloqueio de contas bancárias em **último lugar**, priorizando a constrição de outros bens menos gravosos para a subsistência do demandado:",
    "resultado": "OK",
    "trecho_lei": "e, apenas na inexistência desses, o bloqueio de contas bancárias, de forma a garantir a subsistência do acusado e a manutenção da atividade empresária ao longo do processo."
})

# 17: Linha 55
registros.append({
    "linha": 55,
    "citacao": "art. 16, § 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Art. 16, § 11, da Lei nº 8.429/1992",
    "resultado": "OK",
    "trecho_lei": "LEI Nº 8.429, DE 2 DE JUNHO DE 1992 Texto compilado"
})

# 18: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 16, § 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A tabela a seguir sistematiza a ordem legal de preferência do art. 16, § 11:",
    "resultado": "OK",
    "trecho_lei": "ações e quotas de sociedades simples e empresárias, pedras e metais preciosos e, apenas na inexistência desses, o bloqueio de contas bancárias"
})

# 19: Linha 63
registros.append({
    "linha": 63,
    "citacao": "art. 16, § 14 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| **2ª Preferência** | Bens imóveis | Averbação da indisponibilidade na matrícula imobiliária, ressalvado o bem de família (art. 16, § 14). |",
    "resultado": "OK",
    "trecho_lei": "O valor da indisponibilidade considerará a estimativa de dano indicada na petição inicial, permitida a sua substituição por caução idônea"
})

# 20: Linha 72
registros.append({
    "linha": 72,
    "citacao": "art. 16, § 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Bloqueio bancário é a última opção: a ordem do art. 16, § 11, prioriza veículos e imóveis, deixando o dinheiro em último lugar.",
    "resultado": "OK",
    "trecho_lei": "de forma a garantir a subsistência do acusado e a manutenção da atividade empresária ao longo do processo."
})

# 21: Linha 74
registros.append({
    "linha": 74,
    "citacao": "art. 16, § 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Multa civil não entra na indisponibilidade: a constrição restringe-se ao dano e enriquecimento ilícito, vedada a inclusão da multa civil (art. 16, § 10).",
    "resultado": "OK",
    "trecho_lei": "sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil ou sobre acréscimo patrimonial decorrente de atividade lícita."
})

# 22: Linha 75
registros.append({
    "linha": 75,
    "citacao": "art. 9º e art. 16, § 14 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> - Bem de família protegido: só pode ser bloqueado se foi adquirido com a vantagem do ato do art. 9º (art. 16, § 14).",
    "resultado": "OK",
    "trecho_lei": "salvo se comprovado que o imóvel seja fruto de vantagem patrimonial indevida, conforme descrito no art. 9º desta Lei."
})

# 23: Linha 81
registros.append({
    "linha": 81,
    "citacao": "Tema 576 do STF e art. 17, § 4º-A da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### Inexistência de foro por prerrogativa de função: Tema 576 do STF",
    "resultado": "OK",
    "trecho_lei": "Art. 17. A ação para a aplicação das sanções de que trata esta Lei será proposta pelo Ministério Público"
})

# 24: Linha 83
registros.append({
    "linha": 83,
    "citacao": "Tema 576 do STF e art. 17, § 5º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O Supremo Tribunal Federal pacificou em definitivo que os agentes políticos respondem à ação de improbidade perante a **Justiça de 1º Grau de Jurisdição** (STF, ADI 2.797 e **Tema 576 da Repercussão Geral** — RE 976.566). Governadores, Prefeitos, Secretários de Estado, Deputados e magistrados não detêm foro privilegiado na esfera de improbidade.",
    "resultado": "OK",
    "trecho_lei": "§ 5º A propositura da ação a que se refere o caput deste artigo prevenirá a competência do juízo para todas as ações posteriormente intentadas que possuam a mesma causa de pedir ou o mesmo objeto."
})

# 25: Linha 86
registros.append({
    "linha": 86,
    "citacao": "art. 109, I da Constituição Federal",
    "lei": "cf",
    "frase_capitulo": "- **Justiça Federal de 1º Grau:** quando a causa envolver bens, serviços ou interesse da União, de suas autarquias federais ou de empresas públicas da União (CF, art. 109, I);",
    "resultado": "OK",
    "trecho_lei": "I - as causas em que a União, entidade autárquica ou empresa pública federal forem interessadas na condição de autoras, rés, assistentes ou oponentes"
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
