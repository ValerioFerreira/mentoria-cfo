# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m22_a24-s03-p2"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l8429.clean.txt", "r", encoding="utf-8") as f:
    l8429 = f.read()

registros = []

# 1: Linha 128
registros.append({
    "linha": 128,
    "citacao": "art. 10, VIII, § 1º e § 2º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "A lei exige que a perda seja **efetiva e comprovada**. Isso afasta o dano presumido (*in re ipsa*) que a jurisprudência admitia, por exemplo, em dispensas indevidas de licitação. O inciso VIII (frustrar a licitude da licitação ou dispensá-la indevidamente) passou a dizer expressamente que a conduta deve acarretar **perda patrimonial efetiva**.",
    "resultado": "OK",
    "trecho_lei": "§ 1º Nos casos em que a inobservância de formalidades legais ou regulamentares não implicar perda patrimonial efetiva, não ocorrerá imposição de ressarcimento"
})

# 2: Linha 133
registros.append({
    "linha": 133,
    "citacao": "art. 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "### Incisos do art. 10 estudados neste capítulo",
    "resultado": "OK",
    "trecho_lei": "Art. 10. Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa"
})

# 3: Linha 135
registros.append({
    "linha": 135,
    "citacao": "art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Alguns incisos são comparados com o art. 9º porque descrevem condutas parecidas, mas sem a vantagem para o agente. Os terceiros é que se beneficiam.",
    "resultado": "OK",
    "trecho_lei": "Art. 9º Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida"
})

# 4: Linha 137
registros.append({
    "linha": 137,
    "citacao": "art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Inciso | Conduta | Diferença para o art. 9º |",
    "resultado": "OK",
    "trecho_lei": "de função, de emprego ou de atividade nas entidades referidas no art. 1º desta Lei, e notadamente:"
})

# 5: Linha 139
registros.append({
    "linha": 139,
    "citacao": "art. 9º, XI e art. 10, I da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| I | Favorecer ou colaborar para que bens, rendas, verbas ou valores públicos acabem no patrimônio particular de alguém | No art. 9º, XI, o agente os leva para o **próprio** patrimônio |",
    "resultado": "OK",
    "trecho_lei": "incorporar, por qualquer forma, ao seu patrimônio bens, rendas, verbas ou valores integrantes do acervo patrimonial"
})

# 6: Linha 140
registros.append({
    "linha": 140,
    "citacao": "art. 9º, XII e art. 10, II da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| II | Consentir ou colaborar para que particular use bens e valores públicos sem seguir as formalidades | No art. 9º, XII, o agente usa **em proveito próprio** |",
    "resultado": "OK",
    "trecho_lei": "XII - usar, em proveito próprio, bens, rendas, verbas ou valores integrantes do acervo patrimonial das entidades mencionadas no art. 1° desta lei."
})

# 7: Linha 141
registros.append({
    "linha": 141,
    "citacao": "art. 9º, III e art. 10, IV da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| IV | Consentir ou facilitar a venda, troca ou aluguel de bem público, ou a prestação de serviço estatal, por preço **inferior** ao de mercado | No art. 9º, III, o agente **recebe vantagem** |",
    "resultado": "OK",
    "trecho_lei": "IV - permitir ou facilitar a alienação, permuta ou locação de bem integrante do patrimônio de qualquer das entidades referidas no art. 1º desta lei, ou ainda a prestação de serviço por parte delas, por preço inferior ao de mercado;"
})

# 8: Linha 142
registros.append({
    "linha": 142,
    "citacao": "art. 9º, II e art. 10, V da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| V | Consentir ou facilitar a compra, troca ou aluguel de bem ou serviço por preço **superior** ao de mercado | No art. 9º, II, o agente **recebe vantagem** |",
    "resultado": "OK",
    "trecho_lei": "V - permitir ou facilitar a aquisição, permuta ou locação de bem ou serviço por preço superior ao de mercado;"
})

# 9: Linha 143
registros.append({
    "linha": 143,
    "citacao": "art. 9º, I e art. 10, XII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| XII | Consentir, facilitar ou colaborar para que um terceiro enriqueça de forma ilícita | No art. 9º, I, o agente **recebe** a vantagem |",
    "resultado": "OK",
    "trecho_lei": "XII - permitir, facilitar ou concorrer para que terceiro se enriqueça ilicitamente;"
})

# 10: Linha 144
registros.append({
    "linha": 144,
    "citacao": "art. 9º, IV e art. 10, XIII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| XIII | Consentir o uso de veículos, máquinas, equipamentos ou do trabalho de servidores e terceiros contratados em obra ou serviço particular de outra pessoa | No art. 9º, IV, o agente usa **em seu favor** |",
    "resultado": "OK",
    "trecho_lei": "XIII - permitir que se utilize, em obra ou serviço particular, veículos, máquinas, equipamentos ou material de qualquer natureza"
})

# 11: Linha 149
registros.append({
    "linha": 149,
    "citacao": "art. 9º, IV e art. 10, XIII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "> **Resolução.** O prefeito praticou o art. 9º, IV, pois utilizou bens e trabalho públicos em seu serviço particular. O chefe de gabinete, que **permitiu** o uso em favor de terceira, praticou o art. 10, XIII. A diferença é quem se beneficia: o próprio agente (art. 9º) ou outra pessoa (art. 10).",
    "resultado": "OK",
    "trecho_lei": "IV - utilizar, em obra ou serviço particular, qualquer bem móvel, de propriedade ou à disposição de qualquer das entidades referidas no art. 1º desta Lei"
})

# 12: Linha 154
registros.append({
    "linha": 154,
    "citacao": "art. 9º, VI e X e art. 10, V e XII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Se combinou com a empresa que ela entregaria menos, em troca de um valor para ele, há enriquecimento ilícito (art. 9º, VI ou X, conforme o caso) e a lesão ao erário fica absorvida pela espécie mais grave.",
    "resultado": "OK",
    "trecho_lei": "receber vantagem econômica de qualquer natureza, direta ou indiretamente, para omitir ato de ofício"
})

# 13: Linha 156
registros.append({
    "linha": 156,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "O raciocínio de prova segue três perguntas, nesta ordem: (1) houve **dolo específico**? (2) o **agente** obteve vantagem patrimonial indevida? Se sim, é art. 9º; (3) se não obteve, o **patrimônio público** sofreu perda efetiva comprovada? Se sim, é art. 10; (4) se não houve nenhuma das duas coisas, a conduta só é improbidade se estiver numa das hipóteses taxativas do art. 11.",
    "resultado": "OK",
    "trecho_lei": "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei"
})

# 14: Linha 160
registros.append({
    "linha": 160,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "Esse bloco é cobrado quase sempre de forma literal. As bancas trazem uma conduta e perguntam a espécie, trocando \"perceber vantagem\" por \"permitir\" para confundir o art. 9º com o art. 10. Também são frequentes as perguntas sobre o rol (taxativo no art. 11)",
    "resultado": "OK",
    "trecho_lei": "O mero exercício da função ou desempenho de competências públicas, sem comprovação de ato doloso com fim ilícito, afasta a responsabilidade por ato de improbidade administrativa."
})

# 15: Linha 166
registros.append({
    "linha": 166,
    "citacao": "arts. 9º, 10, 10-A e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Espécies | Arts. 9º, 10 e 11; art. 10-A revogado | Citar quatro espécies |",
    "resultado": "OK",
    "trecho_lei": "[REVOGADO: Art. 10-A. Constitui ato de improbidade administrativa qualquer ação ou omissão para conceder, aplicar ou manter benefício financeiro ou tributário"
})

# 16: Linha 167
registros.append({
    "linha": 167,
    "citacao": "art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Gradação | Art. 9º é o mais grave | Inverter a gravidade |",
    "resultado": "OK",
    "trecho_lei": "suspensão dos direitos políticos até 14 (catorze) anos, pagamento de multa civil equivalente ao valor do acréscimo patrimonial"
})

# 17: Linha 168
registros.append({
    "linha": 168,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Dolo | Exigido em todas as espécies | Admitir culpa no art. 10 |",
    "resultado": "OK",
    "trecho_lei": "§ 2º Considera-se dolo a vontade livre e consciente de alcançar o resultado ilícito tipificado nos arts. 9º, 10 e 11 desta Lei"
})

# 18: Linha 169
registros.append({
    "linha": 169,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Rol | Arts. 9º e 10 exemplificativos; art. 11 taxativo | Dizer que os três são exemplificativos |",
    "resultado": "OK",
    "trecho_lei": "caracterizada por uma das seguintes condutas: (Redação dada pela Lei nº 14.230, de 2021)"
})

# 19: Linha 170
registros.append({
    "linha": 170,
    "citacao": "art. 9º da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 9º | Vantagem patrimonial indevida, dolosa, por causa da função | Exigir lesão ao erário |",
    "resultado": "OK",
    "trecho_lei": "auferir, mediante a prática de ato doloso, qualquer tipo de vantagem patrimonial indevida em razão do exercício de cargo, de mandato"
})

# 20: Linha 172
registros.append({
    "linha": 172,
    "citacao": "art. 10 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10 | Perda efetiva e comprovada | Presumir o dano |",
    "resultado": "OK",
    "trecho_lei": "qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial"
})

# 21: Linha 174
registros.append({
    "linha": 174,
    "citacao": "art. 9º, II e III e art. 10, IV e V da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "| Art. 10, IV e V | Parecem o art. 9º, II e III, mas sem vantagem para o agente | Confundir os artigos |",
    "resultado": "OK",
    "trecho_lei": "perceber vantagem econômica, direta ou indireta, para facilitar a alienação, permuta ou locação de bem público"
})

# 22: Linha 178
registros.append({
    "linha": 178,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "1. A LIA tem três espécies de ato: enriquecimento ilícito (art. 9º), lesão ao erário (art. 10) e violação a princípios (art. 11).",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO II Dos Atos de Improbidade Administrativa"
})

# 23: Linha 179
registros.append({
    "linha": 179,
    "citacao": "art. 9º e art. 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "2. As sanções são mais graves para o art. 9º e mais brandas para o art. 11.",
    "resultado": "OK",
    "trecho_lei": "III - na hipótese do art. 11 desta Lei, pagamento de multa civil de até 24 (vinte e quatro) vezes o valor da remuneração percebida pelo agente"
})

# 24: Linha 182
registros.append({
    "linha": 182,
    "citacao": "arts. 9º, 10 e 11 da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "5. Os arts. 9º e 10 têm rol exemplificativo; o art. 11 tem rol taxativo.",
    "resultado": "OK",
    "trecho_lei": "desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1º desta lei, e notadamente:"
})

# 25: Linha 184
registros.append({
    "linha": 184,
    "citacao": "art. 9º, IV, VII, VIII, XI e XII da Lei nº 8.429/1992",
    "lei": "l8429",
    "frase_capitulo": "7. Os incisos IV, VII, VIII, XI e XII do art. 9º não usam o verbo \"perceber\" vantagem.",
    "resultado": "OK",
    "trecho_lei": "VII - adquirir, para si ou para outrem, no exercício de mandato, de cargo, de emprego ou de função pública, e em razão deles, bens de qualquer natureza, decorrentes dos atos descritos no caput deste artigo, cujo valor seja desproporcional à evolução do patrimônio ou à renda do agente público"
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
