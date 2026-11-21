import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s09-p2/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_l8429 = (ROOT / "pipeline/.cache/leis-oficiais/leis/l8429.clean.txt").read_text(encoding="utf-8")
txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_l8429 = norm(txt_l8429)
norm_cf = norm(txt_cf)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_cf if lei == "cf" else norm_l8429
    t_check = norm(trecho_lei)[:120]
    if t_check not in t_clean:
        print(f"ERROR: item {idx} (linha {linha}): trecho_lei not in {lei}!")
        print("Trecho:", t_check)
    
    rec = {
        "linha": linha,
        "citacao": citacao,
        "lei": lei,
        "frase_capitulo": frase_capitulo,
        "trecho_lei": trecho_lei,
        "resultado": resultado
    }
    if resultado == "ERRO":
        rec["severidade"] = severidade
        rec["diferenca"] = diferenca
        rec["texto_novo"] = texto_novo
    censo.append(rec)

# Item 0 (linha 130)
# | Matéria Controvertida | Regra Firmada pelo STF no Tema 1.199 | Impacto nos Processos em Andamento |
add_item(
    0, 130, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 1 (linha 132)
# | **Exigência de Dolo Específico** | O dolo é obrigatório em todas as modalidades (arts. 9º, 10 e 11)...
add_item(
    1, 132, "art. 9, art. 10", "l8429", "OK",
    "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados os tipos previstos em leis especiais."
)

# Item 2 (linha 138)
# > **Prescrição não retroage para extinguir processos pretéritos:** candidatos costumam errar...
add_item(
    2, 138, "Lei nº 14.230/2021, Tema 1199", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 3 (linha 142)
# A Constituição Federal estabelece no art. 37, § 5º, que a lei fixará prazos de prescrição para ilícitos que causem prejuízos ao erário...
add_item(
    3, 142, "art. 37", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

# Item 4 (linha 148)
# | **Dano decorrente de ato DOLOSO de improbidade** | **Imprescritível.** ...
add_item(
    4, 148, "Tema 897", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

# Item 5 (linha 149)
# | **Reparação de danos decorrente de ilícito civil comum** | **Prescritível.** ...
add_item(
    5, 149, "Tema 666", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário"
)

# Item 6 (linha 150)
# | **Ressarcimento fundado em decisão de Tribunal de Contas** | **Prescritível.** ...
add_item(
    6, 150, "Tema 899", "cf", "OK",
    "As decisões do Tribunal de que resulte imputação de débito ou multa terão eficácia de título executivo."
)

# Item 7 (linha 152)
# Portanto, apenas o ressarcimento fundado em ato doloso tipificado na Lei de Improbidade goza da garantia constitucional de imprescritibilidade (Tema 897)...
add_item(
    7, 152, "art. 23, Tema 666, Tema 897", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 8 (linha 158)
# > [!lei] Art. 17-C, § 2º, da Lei nº 8.429/1992
add_item(
    8, 158, "art. 17, Lei nº 8.429/1992", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 9 (linha 173)
# Diferentemente da indenização ressarcitória, a multa civil possui natureza puramente punitiva e sancionatória. Pelo princípio constitucional da intranscendência das penas (CF, art. 5º, XLV)...
add_item(
    9, 173, "art. 5", "cf", "OK",
    "nenhuma pena passará da pessoa do condenado, podendo a obrigação de reparar o dano e a decretação do perdimento de bens ser, nos termos da lei, estendidas aos sucessores e contra eles executadas, até o limite do valor do patrimônio transferido;"
)

# Item 10 (linha 174)
# - O art. 17-C, § 2º, veda de forma terminante a imposição de responsabilidade solidária para a multa civil;
add_item(
    10, 174, "art. 17", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 11 (linha 181)
# R --> A["Ressarcimento integral do erário (Lei 8.429/1992, art. 17-C, § 2º)"]
add_item(
    11, 181, "art. 17, Lei nº 8.429/1992", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 12 (linha 182)
# R --> B["Multa civil punitiva (art. 12 c/c art. 17-C, § 2º)"]
add_item(
    12, 182, "art. 12, art. 17", "l8429", "OK",
    "está o responsável pelo ato de improbidade sujeito às seguintes cominações, que podem ser aplicadas isolada ou cumulativamente, de acordo com a gravidade do fato:"
)

# Item 13 (linha 185)
# A --> A3["Prescrição: imprescritível se decorrente de ato doloso (STF, Tema 897)"]
add_item(
    13, 185, "Tema 897", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

# Item 14 (linha 188)
# B --> B3["Prescrição: prescritível em 8 anos (art. 23)"]
add_item(
    14, 188, "art. 23", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato"
)

# Item 15 (linha 191)
# ## O terceiro particular e a Súmula 634 do STJ
add_item(
    15, 191, "Súmula 634", "l8429", "OK",
    "As disposições desta Lei são aplicáveis, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
)

# Item 16 (linha 193)
# O art. 3º da Lei nº 8.429/1992 estabelece que as cominações legais estendem-se ao particular que induz, concorre dolosamente ou se beneficia diretamente do ato de improbidade praticado com o agente público.
add_item(
    16, 193, "art. 3, Lei nº 8.429/1992", "l8429", "OK",
    "As disposições desta Lei são aplicáveis, no que couber, àquele que, mesmo não sendo agente público, induza ou concorra dolosamente para a prática do ato de improbidade."
)

# Item 17 (linha 198)
# 2. **Mesmo regime prescricional do servidor:** o particular concorrente submete-se ao mesmo prazo e causas interruptivas incidentes sobre o agente público coautor, entendimento cristalizado na **Súmula 634 do STJ**:
add_item(
    17, 198, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

# Item 18 (linha 200)
# > [!jurisprudencia] STJ, Súmula 634
add_item(
    18, 200, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

# Item 19 (linha 207)
# Para que a contratação direta irregular configure improbidade lesiva ao erário (art. 10, VIII), exige-se:
add_item(
    19, 207, "art. 10", "l8429", "OK",
    "VIII - frustrar a licitude de processo licitatório ou de processo seletivo para celebração de parcerias com entidades sem fins lucrativos, ou dispensá-los indevidamente, acarretando perda patrimonial efetiva;"
)

# Item 20 (linha 211)
# Se o serviço técnico ou artístico contratado por inexigibilidade foi prestado a contento e o valor ajustado revelava-se compatível com a média praticada no mercado, não há prejuízo ao erário...
add_item(
    20, 211, "art. 10", "l8429", "OK",
    "Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1º desta Lei"
)

# Item 21 (linha 220)
# Historicamente, a 1ª Seção do Superior Tribunal de Justiça fixou o entendimento de que a cassação de aposentadoria exigiria expressa previsão em lei específica, inexistindo previsão expressa dessa sanção autônoma no rol taxativo do art. 12 da Lei nº 8.429/1992...
add_item(
    21, 220, "art. 12, Lei nº 8.429/1992", "l8429", "OK",
    "está o responsável pelo ato de improbidade sujeito às seguintes cominações, que podem ser aplicadas isolada ou cumulativamente, de acordo com a gravidade do fato:"
)

# Item 22 (linha 222)
# Por outro lado, o Supremo Tribunal Federal admitiu a conversão da penalidade de perda do cargo público em cassação de aposentadoria no julgamento do **RE 1.456.118**... (CF, art. 37, § 4º).
add_item(
    22, 222, "art. 37", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 23 (linha 228)
# A["Jurisprudência Consolidada em Improbidade"] --> B["STJ, Súmula 634: Prescrição do Particular"]
add_item(
    23, 228, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

# Item 24 (linha 229)
# A --> C["STF, Tema 897: Imprescritibilidade do Dano Doloso"]
add_item(
    24, 229, "Tema 897", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s09-p2",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s09-p2.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
