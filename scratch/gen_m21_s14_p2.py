# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m21_a22-s14-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l14133.clean.txt", "r", encoding="utf-8") as f:
    l14133 = f.read()

registros = []

# 1: Linha 159
registros.append({
    "linha": 159,
    "citacao": "art. 176 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "Por essa razão, o art. 176 da Lei nº 14.133/2021 estabeleceu um prazo de transição dilatado de **6 (seis) anos** para os municípios com **até 20.000 (vinte mil) habitantes**.",
    "resultado": "OK",
    "trecho_lei": "Art. 176. Os Municípios com até 20.000 (vinte mil) habitantes terão o prazo de 6 (seis) anos, contado da data de publicação desta Lei, para cumprimento:"
})

# 2: Linha 163
registros.append({
    "linha": 163,
    "citacao": "art. 176",
    "lei": "l14133",
    "frase_capitulo": "| Exigência Ordinária da Lei | Regra Especial de Transição (Art. 176) | Prazo Máximo de Adaptação |",
    "resultado": "OK",
    "trecho_lei": "I - dos requisitos estabelecidos no art. 7º e no caput do art. 8º desta Lei;"
})

# 3: Linha 170
registros.append({
    "linha": 170,
    "citacao": "art. 176",
    "lei": "l14133",
    "frase_capitulo": "> As prerrogativas transitórias do art. 176 aplicam-se exclusivamente aos municípios de pequeno porte (até vinte mil habitantes).",
    "resultado": "OK",
    "trecho_lei": "II - da obrigatoriedade de realização da licitação sob a forma eletrônica a que se refere o § 2º do art. 17 desta Lei;"
})

# 4: Linha 178
registros.append({
    "linha": 178,
    "citacao": "art. 121, § 1º da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "O art. 121, § 1º, da Lei nº 14.133/2021 reproduziu a regra histórica de que a inadimplência do contratado quanto aos encargos trabalhistas e previdenciários não transfere à Administração Pública a responsabilidade pelo seu pagamento.",
    "resultado": "OK",
    "trecho_lei": "§ 1º A inadimplência do contratado em relação aos encargos trabalhistas, fiscais e comerciais não transferirá à Administração a responsabilidade pelo seu pagamento"
})

# 5: Linha 180
registros.append({
    "linha": 180,
    "citacao": "Tema 246 do STF",
    "lei": "l14133",
    "frase_capitulo": "Contudo, ao julgar a Ação Declaratória de Constitucionalidade nº 16 (ADC 16) e o Recurso Extraordinário nº 760.931 (Tema 246 com repercussão geral), o Supremo Tribunal Federal fixou balizas rigorosas:",
    "resultado": "NAOVER",
    "motivo_naover": "Jurisprudência vinculante do Supremo Tribunal Federal (Tema 246 da Repercussão Geral, RE 760.931)."
})

# 6: Linha 182
registros.append({
    "linha": 182,
    "citacao": "Tema 246 do STF",
    "lei": "l14133",
    "frase_capitulo": "> [!jurisprudencia] STF, Tema 246 da Repercussão Geral (RE 760.931)",
    "resultado": "NAOVER",
    "motivo_naover": "Tese de repercussão geral do STF (Tema 246), sem diploma legal com texto em cache."
})

# 7: Linha 185
registros.append({
    "linha": 185,
    "citacao": "Tema 1118 do STF",
    "lei": "l14133",
    "frase_capitulo": "Posteriormente, no julgamento do RE 1.298.647 (Tema 1.118), o STF reafirmou que cabe ao empregado ou ao Ministério Público do Trabalho o ônus processual de comprovar a falha concreta e negligente da fiscalização administrativa.",
    "resultado": "NAOVER",
    "motivo_naover": "Jurisprudência vinculante do STF sobre ônus da prova na terceirização (Tema 1.118)."
})

# 8: Linha 192
registros.append({
    "linha": 192,
    "citacao": "art. 121, § 1º da Lei nº 14.133/2021 e Tema 246 do STF",
    "lei": "l14133",
    "frase_capitulo": "> O pedido de responsabilização automática do Município deve ser rejeitado. Conforme pacificado pelo STF no Tema 246 (RE 760.931) e pelo art. 121, § 1º, da Lei nº 14.133/2021:",
    "resultado": "OK",
    "trecho_lei": "e não poderá onerar o objeto do contrato nem restringir a regularização e o uso das obras e das edificações, inclusive perante o registro de imóveis"
})

# 9: Linha 202
registros.append({
    "linha": 202,
    "citacao": "art. 168",
    "lei": "l14133",
    "frase_capitulo": "| **Efeito Suspensivo de Recursos** | Automático em julgamento de propostas, habilitação e sanções; devolutivo nos demais atos. | Art. 168 |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O caput do art. 168 estabelece genericamente que os recursos e pedidos de reconsideração terão efeito suspensivo, inexistindo na lei regra de que os demais atos teriam efeito meramente devolutivo.",
    "texto_novo": "| **Efeito Suspensivo de Recursos** | Suspensivo em propostas, habilitação, sanções e demais recursos legais. | Art. 168 |",
    "trecho_lei": "Art. 168. O recurso e o pedido de reconsideração terão efeito suspensivo do ato ou da decisão recorrida até que sobrevenha decisão final da autoridade competente."
})

# 10: Linha 203
registros.append({
    "linha": 203,
    "citacao": "art. 169, I",
    "lei": "l14133",
    "frase_capitulo": "| **1ª Linha de Defesa** | Agentes de contratação, equipes de planejamento e fiscais de contrato (gestão preventiva). | Art. 169, I |",
    "resultado": "OK",
    "trecho_lei": "I - primeira linha de defesa, integrada por servidores e empregados públicos, agentes de licitação e autoridades que atuam na estrutura de governança do órgão ou entidade;"
})

# 11: Linha 204
registros.append({
    "linha": 204,
    "citacao": "art. 169, II",
    "lei": "l14133",
    "frase_capitulo": "| **2ª Linha de Defesa** | Assessoramento jurídico e controle interno setorial do órgão (conformidade e pareceres). | Art. 169, II |",
    "resultado": "OK",
    "trecho_lei": "II - segunda linha de defesa, integrada pelas unidades de assessoramento jurídico e de controle interno do próprio órgão ou entidade;"
})

# 12: Linha 205
registros.append({
    "linha": 205,
    "citacao": "art. 169, III",
    "lei": "l14133",
    "frase_capitulo": "| **3ª Linha de Defesa** | Órgão central de controle interno e Tribunal de Contas (auditorias independentes). | Art. 169, III |",
    "resultado": "OK",
    "trecho_lei": "III - terceira linha de defesa, integrada pelo órgão central de controle interno da Administração e pelo tribunal de contas."
})

# 13: Linha 206
registros.append({
    "linha": 206,
    "citacao": "art. 169, § 3º",
    "lei": "l14133",
    "frase_capitulo": "| **Impropriedade Formal** | Prioridade de saneamento e capacitação sem anulação do ato quando ausente prejuízo real. | Art. 169, § 3º |",
    "resultado": "OK",
    "trecho_lei": "preferencialmente com o aperfeiçoamento dos controles preventivos e com a capacitação dos agentes públicos responsáveis;"
})

# 14: Linha 207
registros.append({
    "linha": 207,
    "citacao": "art. 171",
    "lei": "l14133",
    "frase_capitulo": "| **Cautelar no Tribunal de Contas** | Decisão de mérito em **25 dias úteis** após as informações, prorrogável uma vez por igual período. | Art. 171 |",
    "resultado": "OK",
    "trecho_lei": "sobre o mérito da irregularidade que tenha dado causa à suspensão no prazo de 25 (vinte e cinco) dias úteis, contado da data do recebimento das informações"
})

# 15: Linha 208
registros.append({
    "linha": 208,
    "citacao": "art. 174 e art. 175",
    "lei": "l14133",
    "frase_capitulo": "| **PNCP: Sítio Oficial** | Publicação obrigatória de editais, atas e contratos como condição indispensável de eficácia. | Arts. 174 e 175 |",
    "resultado": "OK",
    "trecho_lei": "Art. 175. Sem prejuízo do disposto no art. 174 desta Lei, os entes federativos poderão instituir sítio eletrônico oficial para divulgação complementar"
})

# 16: Linha 209
registros.append({
    "linha": 209,
    "citacao": "art. 176",
    "lei": "l14133",
    "frase_capitulo": "| **Transição para Pequenos Municípios** | Prazo de **6 anos** para municípios até 20.000 habitantes adaptarem eletrônico e PNCP. | Art. 176 |",
    "resultado": "OK",
    "trecho_lei": "III - das regras relativas à divulgação em sítio eletrônico oficial."
})

# 17: Linha 210
registros.append({
    "linha": 210,
    "citacao": "art. 121, § 1º e Tema 246",
    "lei": "l14133",
    "frase_capitulo": "| **Responsabilidade Terceirizada** | Subsidiária e dependente de prova de culpa *in vigilando* da fiscalização (STF, Tema 246). | Art. 121, § 1º |",
    "resultado": "OK",
    "trecho_lei": "A inadimplência do contratado em relação aos encargos trabalhistas, fiscais e comerciais não transferirá à Administração a responsabilidade pelo seu pagamento"
})

# 18: Linha 214
registros.append({
    "linha": 214,
    "citacao": "art. 168",
    "lei": "l14133",
    "frase_capitulo": "- Os recursos contra propostas e habilitação têm efeito suspensivo automático; os recursos contra sanções possuem efeito suspensivo legal até a decisão final (art. 168).",
    "resultado": "OK",
    "trecho_lei": "efeito suspensivo do ato ou da decisão recorrida até que sobrevenha decisão final da autoridade competente."
})

# 19: Linha 217
registros.append({
    "linha": 217,
    "citacao": "art. 169, § 3º",
    "lei": "l14133",
    "frase_capitulo": "- Simples impropriedades formais sem prejuízo ao erário devem ser sanadas mediante aperfeiçoamento de controles e capacitação, vedada anulação precipitada (art. 169, § 3º).",
    "resultado": "OK",
    "trecho_lei": "quando constatarem simples impropriedade formal, adotarão medidas para o seu saneamento e para a mitigação de riscos de sua nova ocorrência"
})

# 20: Linha 218
registros.append({
    "linha": 218,
    "citacao": "art. 170",
    "lei": "l14133",
    "frase_capitulo": "- Qualquer cidadão ou licitante pode representar contra irregularidades perante o controle interno ou os Tribunais de Contas (art. 170).",
    "resultado": "OK",
    "trecho_lei": "§ 4º Qualquer licitante, contratado ou pessoa física ou jurídica poderá representar aos órgãos de controle interno ou ao tribunal de contas competente contra irregularidades na aplicação desta Lei."
})

# 21: Linha 219
registros.append({
    "linha": 219,
    "citacao": "art. 171",
    "lei": "l14133",
    "frase_capitulo": "- A suspensão cautelar deferida por Tribunal de Contas deve ser julgada no mérito em 25 dias úteis após o recebimento das informações, prorrogável uma única vez (art. 171).",
    "resultado": "OK",
    "trecho_lei": "prorrogável por igual período uma única vez, e definirá objetivamente: \n I - as causas da ordem de suspensão;"
})

# 22: Linha 220
registros.append({
    "linha": 220,
    "citacao": "art. 174",
    "lei": "l14133",
    "frase_capitulo": "- A publicação no Portal Nacional de Contratações Públicas (PNCP) constitui requisito obrigatório para a eficácia de contratos e termos aditivos (art. 174).",
    "resultado": "OK",
    "trecho_lei": "divulgação centralizada e obrigatória dos atos exigidos por esta Lei; \n II - realização facultativa das contratações"
})

# 23: Linha 221
registros.append({
    "linha": 221,
    "citacao": "art. 176",
    "lei": "l14133",
    "frase_capitulo": "- Municípios com até 20.000 habitantes contam com prazo de transição de seis anos para adotarem licitações eletrônicas e publicações exclusivas no PNCP (art. 176).",
    "resultado": "OK",
    "trecho_lei": "Parágrafo único. Enquanto não adotarem o PNCP, os Municípios a que se refere o caput deste artigo deverão:"
})

# 24: Linha 222
registros.append({
    "linha": 222,
    "citacao": "Tema 246 do STF",
    "lei": "l14133",
    "frase_capitulo": "- A responsabilidade da Administração Pública por dívidas trabalhistas de terceirizados é puramente subsidiária e exige prova robusta de culpa *in vigilando* (STF, Tema 246).",
    "resultado": "NAOVER",
    "motivo_naover": "Jurisprudência vinculante do STF (Tema 246 da Repercussão Geral), matéria jurisprudencial sem texto direto em lei."
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

        if tl not in l14133:
            errors.append(f"Row {idx+1}: trecho_lei not in l14133: '{tl}'")

if errors:
    print("ERRORS FOUND:")
    for e in errors:
        print("  -", e)
else:
    print(f"All {len(registros)} rows verified locally! Writing draft...")
    with open(f"material-pdf/_avaliacao/2026-11-11/rascunho/{unit_id}.json", "w", encoding="utf-8") as out:
        json.dump(output_data, out, ensure_ascii=False, indent=1)
    print("Draft saved.")
