import json
import re
from pathlib import Path

# Paths
ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s08-p2/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

# Load clean law texts
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
    
    # check trecho in law
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

# Item 0 (linha 91)
# A única autoridade que não se submete à Lei de Improbidade Administrativa é o **Presidente da República**...
add_item(
    0, 91, "art. 85, Lei nº 1.079/1950", "cf", "OK",
    "São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: V - a probidade na administração;"
)

# Item 1 (linha 97)
# > [!lei] Art. 20, caput e § 1º e 2º, da Lei nº 8.429/1992
add_item(
    1, 97, "art. 20, Lei nº 8.429/1992", "l8429", "OK",
    "Art. 20. A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
)

# Item 2 (linha 98)
# > Art. 20. A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória.
add_item(
    2, 98, "art 20", "l8429", "OK",
    "A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
)

# Item 3 (linha 104)
# O magistrado pode ordenar o afastamento cautelar de noventa dias...
add_item(
    3, 104, "art 20", "l8429", "OK",
    "O afastamento previsto no § 1º deste artigo será de até 90 (noventa) dias, prorrogáveis uma única vez por igual prazo, mediante decisão motivada."
)

# Item 4 (linha 110)
# C ==> D["Execução da Perda da Função Pública (art. 20)"]
add_item(
    4, 110, "art 20", "l8429", "OK",
    "A autoridade judicial competente poderá determinar o afastamento do agente público do exercício do cargo, do emprego ou da função, sem prejuízo da remuneração, quando a medida for necessária à instrução processual ou para evitar a iminente prática de novos ilícitos."
)

# Item 5 (linha 111)
# C ==> E["Suspensão dos Direitos Políticos (art. 20)"]
add_item(
    5, 111, "art 20", "l8429", "OK",
    "Art. 20. A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
)

# Item 6 (linha 112)
# C ==> F["Liquidação e Execução Patrimonial (art. 18)"]
add_item(
    6, 112, "art 18", "l8429", "OK",
    "Art. 18. A sentença que julgar procedente a ação fundada nos arts. 9º e 10 desta Lei condenará ao ressarcimento dos danos e à perda ou à reversão dos bens e valores ilicitamente adquiridos, conforme o caso, em favor da pessoa jurídica prejudicada pelo ilícito."
)

# Item 7 (linha 115)
# ### Extensão da perda da função pública: art. 12, § 1º, e o STF
add_item(
    7, 115, "art 12", "l8429", "OK",
    "A sanção de perda da função pública, nas hipóteses dos incisos I e II do caput deste artigo, atinge apenas o vínculo de mesma qualidade e natureza que o agente público ou político detinha com o poder público na época do cometimento da infração,"
)

# Item 8 (linha 117)
# A sanção de perda da função pública encontra-se positivada no **art. 12, § 1º**...
add_item(
    8, 117, "art. 12, Lei nº 14.230/2021, Lei nº 8.429/1992", "l8429", "OK",
    "podendo o magistrado, na hipótese do inciso I do caput deste artigo, e em caráter excepcional, estendê-la aos demais vínculos, consideradas as circunstâncias do caso e a gravidade da infração."
)

# Item 9 (linha 126)
# A recuperação prática dos ativos desviados e a imposição de encargos processuais regem-se pelos arts. 18 e 23-B da legislação.
add_item(
    9, 126, "art 18", "l8429", "OK",
    "Se houver necessidade de liquidação do dano, a pessoa jurídica prejudicada procederá a essa determinação e ao ulterior procedimento para cumprimento da sentença referente ao ressarcimento do patrimônio público ou à perda ou à reversão dos bens."
)

# Item 10 (linha 130)
# O art. 18 disciplina o cumprimento da sentença condenatória:
add_item(
    10, 130, "art 18", "l8429", "OK",
    "Caso a pessoa jurídica prejudicada não adote as providências a que se refere o § 1º deste artigo no prazo de 6 (seis) meses, contado do trânsito em julgado da sentença de procedência da ação, caberá ao Ministério Público proceder à respectiva liquidação do dano e ao cumprimento da sentença"
)

# Item 11 (linha 131)
# - **Destinação ao ente lesado (art. 18, caput):** a sentença que julgar procedente a ação condenará ao ressarcimento dos danos e à perda ou reversão dos bens e valores ilícitos em favor da pessoa jurídica prejudicada pelo ilícito.
add_item(
    11, 131, "art 18", "l8429", "OK",
    "condenará ao ressarcimento dos danos e à perda ou à reversão dos bens e valores ilicitamente adquiridos, conforme o caso, em favor da pessoa jurídica prejudicada pelo ilícito."
)

# Item 12 (linha 132)
# - **Liquidação e execução prioritária (art. 18, § 1º):** cabe à pessoa jurídica lesada promover a liquidação do dano e a execução da sentença condenatória.
add_item(
    12, 132, "art 18", "l8429", "OK",
    "Se houver necessidade de liquidação do dano, a pessoa jurídica prejudicada procederá a essa determinação e ao ulterior procedimento para cumprimento da sentença referente ao ressarcimento do patrimônio público"
)

# Item 13 (linha 133)
# - **Atuação subsidiária do Ministério Público (art. 18, § 2º):** se a pessoa jurídica prejudicada não adotar as providências de liquidação ou execução no prazo de **6 (seis) meses** a contar do trânsito em julgado, o Ministério Público promoverá a respectiva liquidação e cumprimento da sentença, sem prejuízo da apuração de responsabilidade pela omissão.
add_item(
    13, 133, "art 18", "l8429", "OK",
    "no prazo de 6 (seis) meses, contado do trânsito em julgado da sentença de procedência da ação, caberá ao Ministério Público proceder à respectiva liquidação do dano e ao cumprimento da sentença referente ao ressarcimento do patrimônio público ou à perda ou à reversão dos bens, sem prejuízo de eventual responsabilização pela omissão verificada."
)

# Item 14 (linha 134)
# - **Desconto dos serviços prestados (art. 18, § 3º):** para apuração do valor real a ressarcir, deverão ser descontados os serviços que tenham sido efetivamente prestados à Administração.
add_item(
    14, 134, "art 18", "l8429", "OK",
    "Para fins de apuração do valor do ressarcimento, deverão ser descontados os serviços efetivamente prestados."
)

# Item 15 (linha 138)
# A condenação patrimonial atinge cifras expressivas. Para assegurar a efetividade do ressarcimento sem inviabilizar a subsistência do executado, o art. 18, § 4º, autoriza o parcelamento:
add_item(
    15, 138, "art 18", "l8429", "OK",
    "O juiz poderá autorizar o parcelamento, em até 48 (quarenta e oito) parcelas mensais corrigidas monetariamente, do débito resultante de condenação pela prática de improbidade administrativa se o réu demonstrar incapacidade financeira de saldá-lo de imediato."
)

# Item 16 (linha 140)
# > [!lei] Art. 18, § 4º, da Lei nº 8.429/1992
add_item(
    16, 140, "art 18", "l8429", "OK",
    "em até 48 (quarenta e oito) parcelas mensais corrigidas monetariamente, do débito resultante de condenação pela prática de improbidade administrativa se o réu demonstrar incapacidade financeira de saldá-lo de imediato."
)

# Item 17 (linha 147)
# As despesas processuais da ação de improbidade regem-se pelo art. 23-B da Lei nº 8.429/1992:
add_item(
    17, 147, "art 23", "l8429", "OK",
    "Nas ações e nos acordos regidos por esta Lei, não haverá adiantamento de custas, de preparo, de emolumentos, de honorários periciais e de quaisquer outras despesas."
)

# Item 18 (linha 149)
# - **Sem honorários pelo autor vencedor ou vencido:** não haverá condenação do autor ao pagamento de honorários advocatícios, custas e despesas processuais, salvo se comprovada a sua litigância de má-fé (Lei nº 8.429/1992, art. 23-B, caput).
add_item(
    18, 149, "art 23", "l8429", "ERRO",
    "Haverá condenação em honorários sucumbenciais em caso de improcedência da ação de improbidade se comprovada má-fé.",
    frase_capitulo="- **Sem honorários pelo autor vencedor ou vencido:** não haverá condenação do autor ao pagamento de honorários advocatícios, custas e despesas processuais, salvo se comprovada a sua litigância de má-fé (Lei nº 8.429/1992, art. 23-B, caput).",
    severidade="BAIXO",
    diferenca="O dispositivo citado no texto para a isenção de honorários salvo má-fé é o art. 23-B, caput, quando na verdade o caput trata de isenção de adiantamento de custas e a regra de condenação em honorários por má-fé reside no art. 23-B, § 2º.",
    texto_novo="- **Sem honorários pelo autor vencedor ou vencido:** não haverá condenação do autor ao pagamento de honorários advocatícios, custas e despesas processuais, salvo se comprovada a sua litigância de má-fé (Lei nº 8.429/1992, art. 23-B, § 2º)."
)

# Item 19 (linha 150)
# - **Ressarcimento pelo réu condenado:** se a demanda for julgada procedente, o réu condenado ressarcirá as custas e despesas do processo (Lei nº 8.429/1992, art. 23-B, § 1º).
add_item(
    19, 150, "art 23", "l8429", "OK",
    "No caso de procedência da ação, as custas e as demais despesas processuais serão pagas ao final."
)

# Item 20 (linha 151)
# - **Perícias oficiais:** as perícias serão realizadas preferencialmente por peritos do quadro de servidores do Poder Judiciário ou de outros órgãos públicos (Lei nº 8.429/1992, art. 23-B, § 2º).
add_item(
    20, 151, "art 23", "l8429", "ERRO",
    "Haverá condenação em honorários sucumbenciais em caso de improcedência da ação de improbidade se comprovada má-fé.",
    frase_capitulo="- **Perícias oficiais:** as perícias serão realizadas preferencialmente por peritos do quadro de servidores do Poder Judiciário ou de outros órgãos públicos (Lei nº 8.429/1992, art. 23-B, § 2º).",
    severidade="BAIXO",
    diferenca="O art. 23-B, § 2º da Lei 8.429/1992 prevê condenação em honorários sucumbenciais em caso de improcedência se comprovada má-fé, inexistindo no art. 23-B qualquer previsão de perícias preferenciais por servidores oficiais.",
    texto_novo="- **Honorários por má-fé:** haverá condenação em honorários sucumbenciais em caso de improcedência da ação de improbidade se comprovada má-fé (Lei nº 8.429/1992, art. 23-B, § 2º)."
)

# Item 21 (linha 155)
# > Em ação de improbidade administrativa ajuizada perante a Vara da Fazenda Pública Estadual, o Ministério Público postulou a condenação de um Tenente-Coronel do Corpo de Bombeiros Militar por enriquecimento ilícito (art. 9º)...
add_item(
    21, 155, "art 9", "l8429", "OK",
    "Constitui ato de improbidade administrativa importando em enriquecimento ilícito auferir, mediante a prática de ato doloso, qualquer vantagem patrimonial indevida em razão do exercício de cargo, de mandato, de função, de emprego ou de atividade"
)

# Item 22 (linha 158)
# > 1. A decisão cautelar é ilegal em dois pontos: violou a ordem do art. 16, § 11...
add_item(
    22, 158, "art 16", "l8429", "OK",
    "apenas na inexistência desses, o bloqueio de contas bancárias, de forma a garantir a subsistência do acusado e a manutenção da atividade da pessoa jurídica."
)

# Item 23 (linha 167)
# | **Indisponibilidade: Requisitos** | Exige perigo da demora ou demonstração de risco concreto (ADIs 7156 e 7236). | Art. 16, § 3º |
add_item(
    23, 167, "art 16", "l8429", "OK",
    "O pedido de indisponibilidade de bens a que se refere o caput deste artigo apenas será deferido mediante a demonstração no caso concreto de perigo de dano irreparável ou de risco ao resultado útil do processo"
)

# Item 24 (linha 168)
# | **Limite da Constrição** | Restringe-se ao valor do dano e acréscimo; vedada inclusão de multa civil. | Art. 16, § 5º e 10 |
add_item(
    24, 168, "art 16", "l8429", "OK",
    "A indisponibilidade recairá sobre bens que assegurem exclusivamente o integral ressarcimento do dano ao erário, sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil"
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s08-p2",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}
out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s08-p2.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
