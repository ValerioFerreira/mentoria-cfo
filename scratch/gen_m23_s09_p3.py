import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s09-p3/unidade.json"
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

# Item 0 (linha 230)
# A --> D["STF, Tema 1.199: Dolo Obrigatório e Irretroatividade da Prescrição"]
add_item(
    0, 230, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 1 (linha 242)
# A ampla reforma introduzida pela Lei nº 14.230/2021 transformou profundamente...
add_item(
    1, 242, "art. 11, Lei nº 14.230/2021", "l8429", "OK",
    "Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das seguintes condutas:"
)

# Item 2 (linha 250)
# A["Conduta Ímproba Anteriormente Imputada no Art. 11 Revogado"] --> B{"O Fato Descrito Permanece Tipificado em Outro Dispositivo?"}
add_item(
    2, 250, "art. 11", "l8429", "OK",
    "Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade"
)

# Item 3 (linha 253)
# C --> E["Reenquadramento Jurídico pelo Juiz (Arts. 9º, 10 ou Incisos Remanescentes)"]
add_item(
    3, 253, "art. 9, art. 10", "l8429", "OK",
    "Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer vantagem patrimonial indevida"
)

# Item 4 (linha 260)
# 1. **Reclassificação jurídica permitida:** se a conduta praticada pelo agente sob a vigência do texto revogado também se amolda com perfeição a uma das hipóteses de enriquecimento ilícito (art. 9º), de lesão patrimonial efetiva ao erário (art. 10) ou aos incisos taxativos vigentes do art. 11...
add_item(
    4, 260, "art. 9, art. 10, art. 11", "l8429", "OK",
    "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados os tipos previstos em leis especiais."
)

# Item 5 (linha 261)
# 2. **Exigência cumulativa de dolo:** a continuidade típico-normativa somente legitima o prosseguimento da demanda se restar cabalmente demonstrado o dolo específico na atuação do agente, em consonância estrita com as diretrizes do Tema 1.199 do STF...
add_item(
    5, 261, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 6 (linha 262)
# 3. **Hipótese de extinção por atipicidade superveniente:** apenas naqueles casos em que a conduta do agente público consistia em mera violação a princípio que não encontre correspondência em nenhum dos novos incisos taxativos do art. 11...
add_item(
    6, 262, "art. 11", "l8429", "OK",
    "Constitui ato de improbidade administrativa que atenta contra os princípios da administração pública a ação ou omissão dolosa que viole os deveres de honestidade, de imparcialidade e de legalidade, caracterizada por uma das seguintes condutas:"
)

# Item 7 (linha 266)
# Os agentes políticos submetem-se ao **duplo regime de responsabilização**, conforme pacificado pelo STF no Tema 576 da Repercussão Geral:
add_item(
    7, 266, "Tema 576", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 8 (linha 268)
# - **Improbidade administrativa:** julgado perante a Justiça de primeiro grau (Varas de Fazenda Pública Estadual ou Varas Federais) com suporte na Lei nº 8.429/1992.
add_item(
    8, 268, "Lei nº 8.429/1992", "l8429", "OK",
    "O sistema de responsabilização por atos de improbidade administrativa tutelará a probidade na organização do Estado e no exercício de suas funções, como forma de assegurar a integridade do patrimônio público e social"
)

# Item 9 (linha 270)
# A única autoridade que não se submete à Lei de Improbidade Administrativa é o **Presidente da República**. Conforme fixado na Pet 3240 pelo STF, o Presidente responde exclusivamente por crime de responsabilidade perante o Senado Federal (CF, art. 85, e Lei nº 1.079/1950)...
add_item(
    9, 270, "art. 85, Lei nº 1.079/1950, Lei nº 8.429/1992", "cf", "OK",
    "São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: V - a probidade na administração;"
)

# Item 10 (linha 277)
# > 1. A tese da prescrição intercorrente de quatro anos improcede totalmente. No julgamento das ADIs 7156 e 7236, o STF declarou inconstitucional a expressão "pela metade" do art. 23, § 5º da LIA...
add_item(
    10, 277, "art. 23", "l8429", "OK",
    "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput deste artigo."
)

# Item 11 (linha 278)
# > 2. O particular que concorreu para o ilícito submete-se ao mesmo regime prescricional do agente público (Súmula 634 do STJ).
add_item(
    11, 278, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

# Item 12 (linha 279)
# > 3. Quanto às obrigações patrimoniais, o art. 17-C, § 2º, estabelece expressamente a solidariedade entre os coautores dolosos para o ressarcimento do erário. Todavia, a sanção de multa civil é estritamente pessoal e individualizada, sendo vedada a imposição de solidariedade para as penas pecuniárias punitivas.
add_item(
    12, 279, "art. 17", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 13 (linha 287)
# | **Prescrição Geral** | Prazo unificado de **8 anos** contados do fato ou da cessação da permanência. | Art. 23, caput, da LIA |
add_item(
    13, 287, "art. 23", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 14 (linha 288)
# | **Suspensão por Inquérito** | Suspende o prazo prescricional por até **180 dias corridos**. | Art. 23, § 1º, da LIA |
add_item(
    14, 288, "art. 23", "l8429", "OK",
    "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos referidos nesta Lei suspende o curso do prazo prescricional por, no máximo, 180 (cento e oitenta) dias corridos,"
)

# Item 15 (linha 289)
# | **Marcos Interruptivos** | Rol taxativo de **cinco marcos** (ajuizamento, sentença e acórdãos de TJ/TRF, STJ e STF). | Art. 23, § 4º, I a V |
add_item(
    15, 289, "art. 23", "l8429", "OK",
    "O prazo da prescrição referido no caput deste artigo interrompe-se:"
)

# Item 16 (linha 291)
# | **Tema 1.199 do STF** | Dolo é obrigatório; retroatividade aos processos em curso; irretroatividade da prescrição. | STF (ARE 843.989) |
add_item(
    16, 291, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 17 (linha 292)
# | **Tema 897 do STF** | Imprescritibilidade da pretensão de ressarcimento decorrente de improbidade dolosa. | STF (RE 852.475) |
add_item(
    17, 292, "Tema 897", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

# Item 18 (linha 293)
# | **Solidariedade do Dano** | Solidária para o ressarcimento; estritamente individualizada para a multa civil. | Art. 17-C, § 2º, da LIA |
add_item(
    18, 293, "art. 17", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 19 (linha 294)
# | **Súmula 634 do STJ** | Prescrição do terceiro particular segue o mesmo regime aplicável ao servidor corréu. | STJ (Súmula 634) |
add_item(
    19, 294, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

# Item 20 (linha 301)
# - O prazo prescricional geral da ação de improbidade é de oito anos contados da ocorrência do fato ou da cessação da permanência (art. 23, caput).
add_item(
    20, 301, "art. 23", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 21 (linha 302)
# - O inquérito civil suspende o curso da prescrição pelo prazo máximo de cento e oitenta dias corridos (art. 23, § 1º).
add_item(
    21, 302, "art. 23", "l8429", "OK",
    "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos referidos nesta Lei suspende o curso do prazo prescricional por, no máximo, 180 (cento e oitenta) dias corridos, recomeçando a correr após a sua conclusão ou, caso não concluído o processo, esgotado o prazo de suspensão."
)

# Item 22 (linha 303)
# - A prescrição interrompe-se em cinco marcos taxativos (art. 23, § 4º, I a V), não operando efeito interruptivo a sentença ou acórdão de improcedência.
add_item(
    22, 303, "art. 23", "l8429", "OK",
    "I - pelo ajuizamento da ação de improbidade administrativa;"
)

# Item 23 (linha 305)
# - O Tema 1.199 do STF exigiu dolo específico para todos os atos ímprobos, com retroatividade aos processos sem trânsito em julgado e irretroatividade do regime prescricional.
add_item(
    23, 305, "Tema 1199", "cf", "OK",
    "São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: V - a probidade na administração;"
)

# Item 24 (linha 306)
# - O ressarcimento ao erário por ato doloso de improbidade é imprescritível perante o texto constitucional (STF, Tema 897).
add_item(
    24, 306, "Tema 897", "cf", "OK",
    "A lei estabelecerá os prazos de prescrição para ilícitos praticados por qualquer agente, servidor ou não, que causem prejuízos ao erário, ressalvadas as respectivas ações de ressarcimento."
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s09-p3",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s09-p3.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
