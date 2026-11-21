# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s02-p1"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 32
registros.append({
    "linha": 32,
    "citacao": "art. 2º e art. 3º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A LIA o divide em duas grandes categorias: o **agente público** (art. 2º) e o **terceiro** (art. 3º). Dentro do agente público há um subgrupo novo, o do particular que celebra parceria com a administração (art. 2º, parágrafo único).",
    "resultado": "OK",
    "trecho_lei": "Art. 2º Para os efeitos desta Lei, consideram-se agente público o agente político, o servidor público e todo aquele que exerce, ainda que transitoriamente ou sem remuneração"
})

# 2: Linha 36
registros.append({
    "linha": 36,
    "citacao": "art. 2º",
    "lei": "l8429",
    "frase_capitulo": "A[\"Sujeito ativo da improbidade\"] --> B[\"Agente público: art. 2º\"]",
    "resultado": "OK",
    "trecho_lei": "por eleição, nomeação, designação, contratação ou qualquer outra forma de investidura ou vínculo, mandato, cargo, emprego ou função"
})

# 3: Linha 37
registros.append({
    "linha": 37,
    "citacao": "art. 2º, parágrafo único",
    "lei": "l8429",
    "frase_capitulo": "A --> C[\"Particular parceiro: art. 2º, parágrafo único\"]",
    "resultado": "OK",
    "trecho_lei": "No que se refere a recursos de origem pública, sujeita-se às sanções previstas nesta Lei o particular, pessoa física ou jurídica, que celebra com a administração pública convênio, contrato de repasse, contrato de gestão, termo de parceria"
})

# 4: Linha 38
registros.append({
    "linha": 38,
    "citacao": "art. 3º",
    "lei": "l8429",
    "frase_capitulo": "A --> D[\"Terceiro que induz ou concorre dolosamente: art. 3º\"]",
    "resultado": "OK",
    "trecho_lei": "Art. 3º As disposições desta Lei são aplicáveis, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
})

# 5: Linha 39
registros.append({
    "linha": 39,
    "citacao": "art. 1º",
    "lei": "l8429",
    "frase_capitulo": "B --> E[\"Agente político, servidor e quem exerce função nas entidades do art. 1º\"]",
    "resultado": "OK",
    "trecho_lei": "§ 5º Os atos de improbidade violam a probidade na organização do Estado e no exercício de suas funções e a integridade do patrimônio público e social dos Poderes Executivo, Legislativo e Judiciário, bem como da administração direta e indireta"
})

# 6: Linha 45
registros.append({
    "linha": 45,
    "citacao": "art. 1º e art. 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 2º usa um conceito **amplo**: agente público é agentes políticos, servidores e qualquer pessoa que exerça, mesmo por pouco tempo ou sem salário, mandato, cargo, emprego ou função nas entidades protegidas pelo art. 1º",
    "resultado": "OK",
    "trecho_lei": "nas entidades referidas no art. 1º desta Lei."
})

# 7: Linha 53
registros.append({
    "linha": 53,
    "citacao": "art. 1º",
    "lei": "l8429",
    "frase_capitulo": "| Local de atuação | Qualquer entidade do art. 1º: administração direta e indireta e entidades privadas ligadas a recursos públicos |",
    "resultado": "OK",
    "trecho_lei": "§ 6º Estão sujeitos às sanções desta Lei os atos de improbidade praticados contra o patrimônio de entidade privada que receba subvenção, benefício ou incentivo, fiscal ou creditício"
})

# 8: Linha 71
registros.append({
    "linha": 71,
    "citacao": "art. 2º",
    "lei": "l8429",
    "frase_capitulo": "O que importa é que o art. 2º os inclui **expressamente** no conceito de agente público.",
    "resultado": "OK",
    "trecho_lei": "consideram-se agente público o agente político, o servidor público e todo aquele que exerce"
})

# 9: Linha 77
registros.append({
    "linha": 77,
    "citacao": "art. 85, V da CF",
    "lei": "cf",
    "frase_capitulo": "O art. 85, V, da Constituição define como crime de responsabilidade o ato do Presidente que atente contra a probidade na administração.",
    "resultado": "OK",
    "trecho_lei": "Art. 85. São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: \n I - a existência da União; \n II - o livre exercício do Poder Legislativo, do Poder Judiciário, do Ministério Público e dos Poderes constitucionais das unidades da Federação; \n III - o exercício dos direitos políticos, individuais e sociais; \n IV - a segurança interna do País; \n V - a probidade na administração;"
})

# 10: Linha 80
registros.append({
    "linha": 80,
    "citacao": "CF, art. 85, V",
    "lei": "cf",
    "frase_capitulo": "O Presidente responde apenas por crime de responsabilidade (CF, art. 85, V). A exceção não consta literalmente na LIA e só deve ser considerada quando a questão a invocar.",
    "resultado": "OK",
    "trecho_lei": "V - a probidade na administração;"
})

# 11: Linha 84
registros.append({
    "linha": 84,
    "citacao": "art. 1º, §§ 6º e 7º",
    "lei": "l8429",
    "frase_capitulo": "O conceito amplo também alcança **pessoas que atuam em entidades privadas** beneficiadas por recursos públicos (art. 1º, §§ 6º e 7º).",
    "resultado": "OK",
    "trecho_lei": "§ 7º Independentemente de integrar a administração indireta, estão sujeitos às sanções desta Lei os atos de improbidade praticados contra o patrimônio de entidade privada para cuja criação ou custeio o erário haja concorrido ou concorra no seu patrimônio ou receita atual"
})

# 12: Linha 94
registros.append({
    "linha": 94,
    "citacao": "art. 2º da Lei nº 8.429/1992 e Lei nº 14.230/2021",
    "lei": "l8429",
    "frase_capitulo": "A Lei 14.230/2021 incluiu um parágrafo único no art. 2º. Na gestão de **recursos de origem pública**, ficam sujeitos às sanções da lei os particulares, sejam pessoas físicas ou jurídicas, que firmam parcerias com o poder público",
    "resultado": "OK",
    "trecho_lei": "termo de parceria, termo de cooperação ou ajuste administrativo equivalente."
})

# 13: Linha 109
registros.append({
    "linha": 109,
    "citacao": "art. 2º",
    "lei": "l8429",
    "frase_capitulo": "O texto legal menciona \"pessoa física ou jurídica\" no parágrafo único do art. 2º, embora a doutrina associe o conceito de agente público a pessoas físicas.",
    "resultado": "OK",
    "trecho_lei": "o particular, pessoa física ou jurídica, que celebra com a administração pública convênio, contrato de repasse"
})

# 14: Linha 113
registros.append({
    "linha": 113,
    "citacao": "art. 3º",
    "lei": "l8429",
    "frase_capitulo": "O art. 3º alcança quem **não é agente público**, mas **induz ou concorre dolosamente** para o ato de improbidade.",
    "resultado": "OK",
    "trecho_lei": "mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
})

# 15: Linha 123
registros.append({
    "linha": 123,
    "citacao": "art. 3º e art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Sim, como terceiro que induz e concorre dolosamente para o ato de improbidade (art. 3º), junto com o agente público, que responde como sujeito ativo principal (art. 9º).",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 16: Linha 127
registros.append({
    "linha": 127,
    "citacao": "art. 12 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Pode sofrer, nos limites do art. 12, o ressarcimento do dano, a perda dos bens acrescidos ilicitamente, a multa civil e o impedimento de contratar com o poder público ou de obter benefícios fiscais e creditícios.",
    "resultado": "OK",
    "trecho_lei": "Art. 12. Independentemente do ressarcimento integral do dano patrimonial, se efetivo, e das sanções penais comuns e de responsabilidade, civis e administrativas previstas na legislação específica"
})

# 17: Linha 131
registros.append({
    "linha": 131,
    "citacao": "art. 3º, § 1º",
    "lei": "l8429",
    "frase_capitulo": "Os sócios, os cotistas, os diretores e os colaboradores da pessoa jurídica de direito privado **não respondem** pelo ato imputado à empresa, salvo se, comprovadamente, **participarem** dele. Nesse caso, respondem **nos limites da sua participação** (art. 3º, § 1º).",
    "resultado": "OK",
    "trecho_lei": "§ 1º Os sócios, os cotistas, os diretores e os colaboradores de pessoa jurídica de direito privado não respondem pelo ato de improbidade que venha a ser imputado à pessoa jurídica, salvo se, comprovadamente, houver participação e benefícios diretos, caso em que responderão nos limites da sua participação."
})

# 18: Linha 146
registros.append({
    "linha": 146,
    "citacao": "art. 3º, § 2º e art. 12, § 7º da Lei nº 8.429/1992, Lei nº 12.846/2013",
    "lei": "l8429",
    "frase_capitulo": "Se o mesmo fato também for punido como ato lesivo à administração pública pela **Lei Anticorrupção (Lei 12.846/2013)**, as sanções da LIA **não** se aplicam à pessoa jurídica (art. 3º, § 2º).",
    "resultado": "OK",
    "trecho_lei": "§ 2º As sanções desta Lei não se aplicarão à pessoa jurídica, caso o ato de improbidade administrativa seja também sancionado como ato lesivo à administração pública de que trata a Lei nº 12.846, de 1º de agosto de 2013."
})

# 19: Linha 150
registros.append({
    "linha": 150,
    "citacao": "CF, art. 5º, XLV e art. 8º da LIA",
    "lei": "cf",
    "frase_capitulo": "a obrigação de reparar o dano e o perdimento de bens podem ser estendidos aos sucessores, até o limite do patrimônio transferido (CF, art. 5º, XLV). A LIA aplica a regra no art. 8º.",
    "resultado": "OK",
    "trecho_lei": "XLV - nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser, nos termos da lei, estendidas aos sucessores e contra eles executadas, até o limite do valor do patrimônio transferido;"
})

# 20: Linha 152
registros.append({
    "linha": 152,
    "citacao": "Lei 8.429/1992, art. 8º",
    "lei": "l8429",
    "frase_capitulo": "> [!lei] Lei 8.429/1992, art. 8º",
    "resultado": "OK",
    "trecho_lei": "estão sujeitos apenas à obrigação de repará-lo até o limite do valor da herança ou do patrimônio transferido."
})

# 21: Linha 153
registros.append({
    "linha": 153,
    "citacao": "art. 8º",
    "lei": "l8429",
    "frase_capitulo": "> Art. 8º O sucessor ou o herdeiro daquele que causar dano ao erário ou que se enriquecer ilicitamente estão sujeitos apenas à obrigação de repará-lo até o limite do valor da herança ou do patrimônio transferido.",
    "resultado": "OK",
    "trecho_lei": "Art. 8º O sucessor ou o herdeiro daquele que causar dano ao erário ou que se enriquecer ilicitamente"
})

# 22: Linha 164
registros.append({
    "linha": 164,
    "citacao": "art. 8º-A da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 8º-A estende a responsabilidade sucessória às hipóteses de **alteração contratual, transformação, incorporação, fusão ou cisão** societária.",
    "resultado": "OK",
    "trecho_lei": "Art. 8º-A A responsabilidade sucessória de que trata o art. 8º desta Lei aplica-se também na hipótese de alteração contratual, de transformação, de incorporação, de fusão ou de cisão societária."
})

# 23: Linha 169
registros.append({
    "linha": 169,
    "citacao": "art. 8º",
    "lei": "l8429",
    "frase_capitulo": "| Transformação, alteração contratual ou cisão | Sucessora, nos termos do art. 8º |",
    "resultado": "OK",
    "trecho_lei": "Nas hipóteses de fusão e de incorporação, a responsabilidade da sucessora será restrita à obrigação de reparação integral do dano causado, até o limite do patrimônio transferido"
})

# 24: Linha 191
registros.append({
    "linha": 191,
    "citacao": "art. 1º e art. 2º, caput",
    "lei": "l8429",
    "frase_capitulo": "| Agente público | Art. 2º, caput | Exercer mandato, cargo, emprego ou função nas entidades do art. 1º | Pode ser eleito, nomeado, designado ou contratado; com ou sem remuneração |",
    "resultado": "OK",
    "trecho_lei": "Art. 1º O sistema de responsabilização por atos de improbidade administrativa tutelará a probidade na organização do Estado"
})

# 25: Linha 192
registros.append({
    "linha": 192,
    "citacao": "art. 2º, parágrafo único",
    "lei": "l8429",
    "frase_capitulo": "| Particular parceiro | Art. 2º, parágrafo único | Ter celebrado convênio, contrato de repasse, de gestão, termo de parceria ou ajuste equivalente | Responde quanto aos recursos de origem pública |",
    "resultado": "OK",
    "trecho_lei": "Parágrafo único. No que se refere a recursos de origem pública, sujeita-se às sanções previstas nesta Lei o particular, pessoa física ou jurídica"
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
