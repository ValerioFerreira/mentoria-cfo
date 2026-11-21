# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s04-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 138
registros.append({
    "linha": 138,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "```mermaid Passos para configurar o art. 11",
    "resultado": "OK",
    "trecho_lei": "Seção III Dos Atos de Improbidade Administrativa que Atentam Contra os Princípios da Administração Pública"
})

# 2: Linha 141
registros.append({
    "linha": 141,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "B -- \"Não\" --> C[\"Não é improbidade do art. 11: rol taxativo\"]",
    "resultado": "OK",
    "trecho_lei": "caracterizada por uma das seguintes condutas: (Redação dada pela Lei nº 14.230, de 2021)"
})

# 3: Linha 149
registros.append({
    "linha": 149,
    "citacao": "art. 11, XI da Lei 8.429/1992 e Súmula Vinculante 13",
    "lei": "l8429",
    "frase_capitulo": "### Entendendo a Súmula Vinculante 13",
    "resultado": "OK",
    "trecho_lei": "XI - nomear cônjuge, companheiro ou parente em linha reta, colateral ou por afinidade, até o terceiro grau, inclusive"
})

# 4: Linha 164
registros.append({
    "linha": 164,
    "citacao": "art. 37, § 1º da Constituição Federal e art. 11, XII da Lei 8.429/1992",
    "lei": "cf",
    "frase_capitulo": "O inciso XII reflete o art. 37, § 1º, da Constituição: a publicidade oficial deve ser educativa, informativa ou de orientação social e não pode trazer nomes, símbolos ou imagens que sirvam à promoção pessoal de autoridades ou servidores.",
    "resultado": "OK",
    "trecho_lei": "§ 1º A publicidade dos atos, programas, obras, serviços e campanhas dos órgãos públicos deverá ter caráter educativo, informativo ou de orientação social"
})

# 5: Linha 166
registros.append({
    "linha": 166,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> [!bizu] Incisos revogados do art. 11",
    "resultado": "OK",
    "trecho_lei": "I - praticar ato visando fim proibido em lei ou regulamento ou diverso daquele previsto, na regra de competência;"
})

# 6: Linha 167
registros.append({
    "linha": 167,
    "citacao": "art. 11, I, II, IX e X da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> Memorize que **I, II, IX e X** foram revogados. Então, assertivas que descrevam como improbidade do art. 11 (a) atos com fim proibido por lei, (b) retardar ato de ofício, (c) deixar de cumprir acessibilidade ou (d) transferir recurso sem contrato na área da saúde estão desatualizadas e erradas.",
    "resultado": "OK",
    "trecho_lei": "II - retardar ou deixar de praticar, indevidamente, ato de ofício;"
})

# 7: Linha 172
registros.append({
    "linha": 172,
    "citacao": "art. 11, XI, § 1º e § 5º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** Em tese, sim, pelo art. 11, XI, que alcança parentes até o terceiro grau de autoridade nomeante ou de servidor em cargo de direção, chefia ou assessoramento, e expressamente inclui o ajuste por designações recíprocas. Para a configuração, é preciso, porém, demonstrar o dolo com finalidade ilícita (art. 11, § 5º, e § 1º), pois a nomeação política, por si só, não basta.",
    "resultado": "OK",
    "trecho_lei": "compreendido o ajuste mediante designações recíprocas; (Incluído pela Lei nº 14.230, de 2021)"
})

# 8: Linha 176
registros.append({
    "linha": 176,
    "citacao": "art. 11, XI, §§ 1º e 5º da Lei 8.429/1992 e Súmula Vinculante 13",
    "lei": "l8429",
    "frase_capitulo": "Convém separar dois planos. A **proibição de nepotismo** decorre dos princípios constitucionais e da Súmula Vinculante 13 e vale mesmo sem lei específica: a nomeação irregular pode e deve ser anulada pela administração. Já a **improbidade** do art. 11, XI, é mais exigente: além do parentesco, requer dolo com a finalidade de obter proveito indevido, nos termos dos §§ 1º e 5º.",
    "resultado": "OK",
    "trecho_lei": "da autoridade nomeante ou de servidor da mesma pessoa jurídica investido em cargo de direção, chefia ou assessoramento"
})

# 9: Linha 180
registros.append({
    "linha": 180,
    "citacao": "arts. 9º, 10 e 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Ao ler um caso, três perguntas separam as espécies. Primeiro: o agente **obteve vantagem patrimonial** indevida? Se sim, art. 9º. Segundo: o patrimônio público sofreu **perda efetiva comprovada**, causada pelo agente ou por sua omissão dolosa? Se sim, art. 10. Terceiro: a conduta está num dos incisos do art. 11, com fim de proveito indevido e lesividade relevante? Se sim, art. 11. Nessa ordem, a espécie mais grave prevalece.",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 10: Linha 183
registros.append({
    "linha": 183,
    "citacao": "arts. 9º, 10 e 11, V da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> Um gestor frauda a licitação de uma obra para contratar a empresa de um amigo. Se recebeu parte do contrato (vantagem), a conduta é do art. 9º. Se não recebeu nada, mas a obra foi paga acima do preço de mercado e o sobrepreço está comprovado, é do art. 10. Se o preço foi correto e a obra foi bem executada, mas ficou provado que ele frustrou, com dolo, o caráter competitivo para favorecer o amigo, aplica-se o art. 11, V.",
    "resultado": "OK",
    "trecho_lei": "V - frustrar, em ofensa à imparcialidade, o caráter concorrencial de concurso público, de chamamento ou de procedimento licitatório, com vistas à obtenção de benefício próprio, direto ou indireto, ou de terceiros;"
})

# 11: Linha 187
registros.append({
    "linha": 187,
    "citacao": "art. 10 e art. 11, V da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O art. 10 aparece com assertivas que descrevem uma conduta e perguntam a espécie, ou que reproduzem a redação antiga com o verbo \"negligentemente\". No art. 11, o tema campeão é a mudança: dolo específico, rol taxativo, incisos revogados, deveres violados. Outro favorito é o inciso V, pela troca do objeto protegido.",
    "resultado": "OK",
    "trecho_lei": "X - agir ilicitamente na arrecadação de tributo ou de renda, bem como no que diz respeito à conservação do patrimônio público;"
})

# 12: Linha 193
registros.append({
    "linha": 193,
    "citacao": "art. 10, VIII da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10, inciso VIII | Licitação ou seleção frustrada, com perda efetiva | Exigir só a ilegalidade |",
    "resultado": "OK",
    "trecho_lei": "VIII - frustrar a licitude de processo licitatório ou de processo seletivo para celebração de parcerias com entidades sem fins lucrativos, ou dispensá-los indevidamente, acarretando perda patrimonial efetiva;"
})

# 13: Linha 195
registros.append({
    "linha": 195,
    "citacao": "art. 10, XXII e art. 10-A da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10-A | Revogado; conduta migrou para o inciso XXII | Citar quatro espécies |",
    "resultado": "OK",
    "trecho_lei": "[REVOGADO: Art. 10-A. Constitui ato de improbidade administrativa qualquer ação ou omissão para conceder, aplicar ou manter benefício financeiro ou tributário"
})

# 14: Linha 196
registros.append({
    "linha": 196,
    "citacao": "art. 10, § 2º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10, § 2º | Perda da atividade econômica não é improbidade | Presumir improbidade em prejuízo comercial |",
    "resultado": "OK",
    "trecho_lei": "§ 2º A mera perda patrimonial decorrente da atividade econômica não acarretará improbidade administrativa, salvo se comprovado ato doloso praticado com essa finalidade."
})

# 15: Linha 197
registros.append({
    "linha": 197,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 11 | Dolo específico, rol taxativo, três deveres | Incluir lealdade às instituições |",
    "resultado": "OK",
    "trecho_lei": "Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade"
})

# 16: Linha 199
registros.append({
    "linha": 199,
    "citacao": "art. 11, §§ 1º, 3º e 4º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Parágrafos do art. 11 | Proveito indevido, demonstração objetiva, lesividade | Dispensar a lesividade |",
    "resultado": "OK",
    "trecho_lei": "exigem lesividade relevante ao bem jurídico tutelado para serem passíveis de sancionamento e independem do reconhecimento da produção de danos ao erário"
})

# 17: Linha 205
registros.append({
    "linha": 205,
    "citacao": "art. 10 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "1. Todos os incisos do art. 10 exigem dolo e perda patrimonial efetiva e comprovada.",
    "resultado": "OK",
    "trecho_lei": "qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres"
})

# 18: Linha 207
registros.append({
    "linha": 207,
    "citacao": "art. 10, XXII e art. 10-A da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "3. O art. 10-A foi revogado e a conduta passou ao art. 10, XXII.",
    "resultado": "OK",
    "trecho_lei": "conceder, aplicar ou manter benefício financeiro ou tributário contrário ao que dispõem o caput"
})

# 19: Linha 209
registros.append({
    "linha": 209,
    "citacao": "art. 11 da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "5. O art. 11 exige dolo específico, tem rol taxativo e protege honestidade, imparcialidade e legalidade.",
    "resultado": "OK",
    "trecho_lei": "Art. 11. Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das seguintes condutas:"
})

# 20: Linha 210
registros.append({
    "linha": 210,
    "citacao": "art. 11, I, II, IX e X da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "6. Os incisos I, II, IX e X do art. 11 foram revogados.",
    "resultado": "OK",
    "trecho_lei": "deixar de cumprir a exigência de requisitos de acessibilidade previstos na legislação."
})

# 21: Linha 211
registros.append({
    "linha": 211,
    "citacao": "art. 11, §§ 1º, 3º e 4º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "7. O art. 11 exige fim de proveito indevido, demonstração objetiva da ilegalidade e lesividade relevante.",
    "resultado": "OK",
    "trecho_lei": "§ 3º O enquadramento de conduta funcional na categoria de que trata este artigo pressupõe a demonstração objetiva da prática de ilegalidade no exercício da função pública, com a indicação das normas constitucionais, legais ou infralegais violadas."
})

# 22: Linha 212
registros.append({
    "linha": 212,
    "citacao": "art. 11, § 4º da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "8. O art. 11 independe de dano ao erário e de enriquecimento ilícito.",
    "resultado": "OK",
    "trecho_lei": "independem do reconhecimento da produção de danos ao erário e de enriquecimento ilícito dos agentes públicos."
})

# 23: Linha 213
registros.append({
    "linha": 213,
    "citacao": "art. 11, V da Lei 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "9. O art. 11, V, protege concurso, chamamento e licitação contra a frustração do caráter competitivo.",
    "resultado": "OK",
    "trecho_lei": "caráter concorrencial de concurso público, de chamamento ou de procedimento licitatório, com vistas à obtenção de benefício próprio, direto ou indireto, ou de terceiros;"
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
