# -*- coding: utf-8 -*-
import json

unit_id = "CENSO-direito-administrativo_m21_a22-s14-p1"

with open(f"material-pdf/_avaliacao/2026-11-11/unidades/{unit_id}/unidade.json", "r", encoding="utf-8") as f:
    unidade = json.load(f)

with open(unidade["md"], "r", encoding="utf-8") as f:
    chapter_content = f.read()

with open("pipeline/.cache/leis-oficiais/leis/l14133.clean.txt", "r", encoding="utf-8") as f:
    l14133 = f.read()

with open("pipeline/.cache/leis-oficiais/leis/cf.clean.txt", "r", encoding="utf-8") as f:
    cf = f.read()

registros = []

# 1: Linha 14
registros.append({
    "linha": 14,
    "citacao": "Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "A Lei nº 14.133/2021 inovou ao adotar o modelo internacional das três linhas de defesa, disciplinar a intervenção cautelar dos Tribunais de Contas e instituir o Portal Nacional de Contratações Públicas (PNCP).",
    "resultado": "OK",
    "trecho_lei": "CAPÍTULO III DO CONTROLE DAS CONTRATAÇÕES Art. 169. As contratações públicas deverão submeter-se a práticas contínuas"
})

# 2: Linha 17
registros.append({
    "linha": 17,
    "citacao": "art. 168",
    "lei": "l14133",
    "frase_capitulo": "Compreender a disciplina do efeito suspensivo nos recursos e pedidos de reconsideração (art. 168).",
    "resultado": "OK",
    "trecho_lei": "Art. 168. O recurso e o pedido de reconsideração terão efeito suspensivo do ato ou da decisão recorrida"
})

# 3: Linha 18
registros.append({
    "linha": 18,
    "citacao": "art. 169",
    "lei": "l14133",
    "frase_capitulo": "Analisar o modelo das três linhas de defesa no controle das compras governamentais (art. 169).",
    "resultado": "OK",
    "trecho_lei": "e, além de estar subordinadas ao controle social, sujeitar-se-ão às seguintes linhas de defesa:"
})

# 4: Linha 19
registros.append({
    "linha": 19,
    "citacao": "art. 171",
    "lei": "l14133",
    "frase_capitulo": "Conhecer as regras e o prazo de 25 dias úteis na suspensão cautelar por Tribunais de Contas (art. 171).",
    "resultado": "OK",
    "trecho_lei": "§ 1º Ao suspender cautelarmente o processo licitatório, o tribunal de contas deverá pronunciar-se definitivamente sobre o mérito da irregularidade que tenha dado causa à suspensão no prazo de 25 (vinte e cinco) dias úteis"
})

# 5: Linha 20
registros.append({
    "linha": 20,
    "citacao": "art. 174 e art. 175",
    "lei": "l14133",
    "frase_capitulo": "Identificar a arquitetura e as ferramentas do Portal Nacional de Contratações Públicas (arts. 174 e 175).",
    "resultado": "OK",
    "trecho_lei": "Art. 174. É criado o Portal Nacional de Contratações Públicas (PNCP), sítio eletrônico oficial destinado à:"
})

# 6: Linha 21
registros.append({
    "linha": 21,
    "citacao": "art. 176",
    "lei": "l14133",
    "frase_capitulo": "Compreender as regras diferenciadas de transição para municípios com até vinte mil habitantes (art. 176).",
    "resultado": "OK",
    "trecho_lei": "Art. 176. Os Municípios com até 20.000 (vinte mil) habitantes terão o prazo de 6 (seis) anos, contado da data de publicação desta Lei, para cumprimento:"
})

# 7: Linha 25
registros.append({
    "linha": 25,
    "citacao": "art. 168 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "O art. 168 da Lei nº 14.133/2021 estabeleceu uma divisão técnica precisa quanto à atribuição do efeito suspensivo.",
    "resultado": "OK",
    "trecho_lei": "decisão recorrida até que sobrevenha decisão final da autoridade competente."
})

# 8: Linha 44
registros.append({
    "linha": 44,
    "citacao": "art. 168, caput",
    "lei": "l14133",
    "frase_capitulo": "1. **Fase de seleção do licitante (habilitação e propostas):** o recurso contra o julgamento de propostas e contra o ato de habilitação ou inabilitação tem **efeito suspensivo automático** (*ope legis*), conforme o caput do art. 168.",
    "resultado": "OK",
    "trecho_lei": "O recurso e o pedido de reconsideração terão efeito suspensivo do ato ou da decisão recorrida até que sobrevenha decisão final da autoridade competente."
})

# 9: Linha 45
registros.append({
    "linha": 45,
    "citacao": "art. 168, parágrafo único",
    "lei": "l14133",
    "frase_capitulo": "terá **efeito suspensivo obrigatório** até que sobrevenha a decisão final da autoridade competente (art. 168, parágrafo único).",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O efeito suspensivo do recurso e do pedido de reconsideração decorre expressamente do caput do art. 168 da Lei nº 14.133/2021, e não do seu parágrafo único (que disciplina a assistência pelo órgão de assessoramento jurídico).",
    "texto_novo": "terá **efeito suspensivo obrigatório** até que sobrevenha a decisão final da autoridade competente (art. 168, caput).",
    "trecho_lei": "Parágrafo único. Na elaboração de suas decisões, a autoridade competente será auxiliada pelo órgão de assessoramento jurídico, que deverá dirimir dúvidas"
})

# 10: Linha 52
registros.append({
    "linha": 52,
    "citacao": "art. 168, caput",
    "lei": "l14133",
    "frase_capitulo": "| **Julgamento de Propostas** | **Suspensivo Automático** | Art. 168, caput |",
    "resultado": "OK",
    "trecho_lei": "b) julgamento das propostas;"
})

# 11: Linha 53
registros.append({
    "linha": 53,
    "citacao": "art. 168, caput",
    "lei": "l14133",
    "frase_capitulo": "| **Habilitação ou Inabilitação** | **Suspensivo Automático** | Art. 168, caput |",
    "resultado": "OK",
    "trecho_lei": "c) ato de habilitação ou inabilitação de licitante;"
})

# 12: Linha 54
registros.append({
    "linha": 54,
    "citacao": "art. 156 e art. 168, parágrafo único",
    "lei": "l14133",
    "frase_capitulo": "| **Sanções do Art. 156** | **Suspensivo Obrigatório** | Art. 168, parágrafo único | Resguarda o particular contra cobranças e restrições antes do julgamento final. |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O efeito suspensivo dos recursos contra sanções decorre do caput do art. 168 da Lei nº 14.133/2021, e não de seu parágrafo único (que cuida do apoio pela assessoria jurídica).",
    "texto_novo": "| **Sanções do Art. 156** | **Suspensivo Obrigatório** | Art. 168, caput | Resguarda o particular contra cobranças e restrições antes do julgamento final. |",
    "trecho_lei": "Art. 156. Serão aplicadas ao responsável pelas infrações administrativas previstas nesta Lei as seguintes sanções:"
})

# 13: Linha 55
registros.append({
    "linha": 55,
    "citacao": "art. 168, caput",
    "lei": "l14133",
    "frase_capitulo": "| **Anulação ou Revogação** | **Devolutivo** (regra geral) | Art. 168, caput | Prestigia o juízo de conveniência e legalidade da autoridade administrativa. |",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "O caput do art. 168 prevê efeito suspensivo geral para recursos e pedidos de reconsideração, inexistindo na norma atribuição de efeito meramente devolutivo aos recursos contra anulação ou revogação.",
    "texto_novo": "| **Anulação ou Revogação** | **Suspensivo** (regra geral) | Art. 168, caput | Prestigia a ampla defesa e a segurança jurídica até a decisão final da autoridade superior. |",
    "trecho_lei": "d) anulação ou revogação da licitação;"
})

# 14: Linha 58
registros.append({
    "linha": 58,
    "citacao": "art. 156 e art. 168 da Lei nº 14.133/2021, Lei nº 8.666/1993",
    "lei": "l14133",
    "frase_capitulo": "A Lei nº 14.133/2021 alterou essa sistemática no parágrafo único do art. 168: os recursos contra quaisquer sanções administrativas do art. 156 (inclusive multa pecuniária) possuem efeito suspensivo garantido até a decisão final da instância julgadora.",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "A atribuição de efeito suspensivo aos recursos contra sanções administrativas decorre do caput do art. 168 da Lei nº 14.133/2021, e não do seu parágrafo único (que disciplina a atuação do órgão de assessoramento jurídico).",
    "texto_novo": "A Lei nº 14.133/2021 alterou essa sistemática no caput do art. 168: os recursos contra quaisquer sanções administrativas do art. 156 (inclusive multa pecuniária) possuem efeito suspensivo garantido até a decisão final da instância julgadora.",
    "trecho_lei": "que deverá dirimir dúvidas e subsidiá-la com as informações necessárias."
})

# 15: Linha 62
registros.append({
    "linha": 62,
    "citacao": "art. 169",
    "lei": "l14133",
    "frase_capitulo": "O art. 169 determina que as contratações públicas submetem-se a práticas contínuas de gestão de riscos e controle preventivo estruturadas em **três linhas de defesa**.",
    "resultado": "OK",
    "trecho_lei": "Art. 169. As contratações públicas deverão submeter-se a práticas contínuas e permanentes de gestão de riscos e de controle preventivo"
})

# 16: Linha 87
registros.append({
    "linha": 87,
    "citacao": "Lei nº 14.133/2021, art. 169, § 3º, I",
    "lei": "l14133",
    "frase_capitulo": "> [!lei] Lei 14.133/2021, art. 169, § 3º, I",
    "resultado": "OK",
    "trecho_lei": "§ 3º Os integrantes das linhas de defesa a que se referem os incisos I, II e III do caput deste artigo observarão o seguinte:"
})

# 17: Linha 91
registros.append({
    "linha": 91,
    "citacao": "art. 169",
    "lei": "l14133",
    "frase_capitulo": "O inciso I do § 3º do art. 169 privilegia o saneamento. Diante de mera impropriedade formal, sem dano ao erário, os integrantes das linhas de defesa corrigem a falha e reforçam os controles preventivos",
    "resultado": "OK",
    "trecho_lei": "I - quando constatarem simples impropriedade formal, adotarão medidas para o seu saneamento e para a mitigação de riscos de sua nova ocorrência"
})

# 18: Linha 95
registros.append({
    "linha": 95,
    "citacao": "art. 170 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "O art. 170 da Lei nº 14.133/2021 reforça o controle social das compras governamentais.",
    "resultado": "OK",
    "trecho_lei": "Art. 170. Os órgãos de controle adotarão, na fiscalização dos atos previstos nesta Lei, critérios de oportunidade, materialidade, relevância e risco"
})

# 19: Linha 101
registros.append({
    "linha": 101,
    "citacao": "art. 170, § 3º",
    "lei": "l14133",
    "frase_capitulo": "- Em contrapartida, o auditor ou servidor que tiver contato com esses papéis sigilosos torna-se pessoal e administrativamente corresponsável pela guarda do segredo funcional (art. 170, § 3º). Dessa forma, concilia-se a integridade da fiscalização pública com a proteção aos segredos industriais e de segurança estatal.",
    "resultado": "ERRO",
    "severidade": "BAIXO",
    "diferenca": "A norma sobre acesso irrestrito e corresponsabilidade do órgão de controle pela manutenção do sigilo das informações classificadas está no art. 169, § 2º da Lei nº 14.133/2021, e não no art. 170, § 3º (que cuida da desconsideração de provas impertinentes ou protelatórias).",
    "texto_novo": "- Em contrapartida, o auditor ou servidor que tiver contato com esses papéis sigilosos torna-se pessoal e administrativamente corresponsável pela guarda do segredo funcional (art. 169, § 2º). Dessa forma, concilia-se a integridade da fiscalização pública com a proteção aos segredos industriais e de segurança estatal.",
    "trecho_lei": "e o órgão de controle com o qual foi compartilhada eventual informação sigilosa tornar-se-á corresponsável pela manutenção do seu sigilo."
})

# 20: Linha 105
registros.append({
    "linha": 105,
    "citacao": "art. 71 da CF",
    "lei": "cf",
    "frase_capitulo": "No exercício de sua competência constitucional (CF, art. 71), as Cortes de Contas podem expedir medidas cautelares para suspender editais",
    "resultado": "OK",
    "trecho_lei": "Art. 71. O controle externo, a cargo do Congresso Nacional, será exercido com o auxílio do Tribunal de Contas da União, ao qual compete:"
})

# 21: Linha 107
registros.append({
    "linha": 107,
    "citacao": "art. 171 da Lei nº 14.133/2021",
    "lei": "l14133",
    "frase_capitulo": "o art. 171 da Lei nº 14.133/2021 fixou prazos rígidos para a decisão de mérito das medidas liminares.",
    "resultado": "OK",
    "trecho_lei": "Art. 171. Na fiscalização de controle será observado o seguinte:"
})

# 22: Linha 124
registros.append({
    "linha": 124,
    "citacao": "art. 171",
    "lei": "l14133",
    "frase_capitulo": "| Parâmetro Operacional | Regra Legal no Art. 171 | Finalidade da Disciplina Normativa |",
    "resultado": "OK",
    "trecho_lei": "prorrogável por igual período uma única vez, e definirá objetivamente:"
})

# 23: Linha 139
registros.append({
    "linha": 139,
    "citacao": "art. 174",
    "lei": "l14133",
    "frase_capitulo": "O art. 174 instituiu o PNCP como sítio eletrônico oficial centralizado para a divulgação obrigatória dos atos de todas as contratações públicas regidas pela lei.",
    "resultado": "OK",
    "trecho_lei": "I - divulgação centralizada e obrigatória dos atos exigidos por esta Lei;"
})

# 24: Linha 141
registros.append({
    "linha": 141,
    "citacao": "art. 94",
    "lei": "l14133",
    "frase_capitulo": "A publicação do edital e do contrato no PNCP constitui condição indispensável de eficácia jurídica dos atos administrativos (art. 94).",
    "resultado": "OK",
    "trecho_lei": "Art. 94. A divulgação no Portal Nacional de Contratações Públicas (PNCP) é condição indispensável para a eficácia do contrato e de seus aditamentos"
})

# 25: Linha 153
registros.append({
    "linha": 153,
    "citacao": "art. 174, § 1º",
    "lei": "l14133",
    "frase_capitulo": "O PNCP é administrado pelo Comitê Gestor da Rede Nacional de Contratações Públicas, órgão colegiado paritário composto por representantes da União, dos Estados, do Distrito Federal e dos Municípios (art. 174, § 1º).",
    "resultado": "OK",
    "trecho_lei": "§ 1º O PNCP será gerido pelo Comitê Gestor da Rede Nacional de Contratações Públicas"
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

    tl = r["trecho_lei"]
    if len(tl) < 25:
        errors.append(f"Row {idx+1}: trecho_lei too short ({len(tl)} chars)")
    if tl in trechos_vistos:
        errors.append(f"Row {idx+1}: duplicate trecho_lei: '{tl[:30]}...'")
    trechos_vistos.add(tl)

    law_txt = cf if r["lei"] == "cf" else l14133
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
