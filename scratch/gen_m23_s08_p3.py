import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s08-p3/unidade.json"
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

# Item 0 (linha 169)
# | **Impenhorabilidade de 40 SM** | Proteção absoluta de até 40 salários mínimos em poupança, conta ou renda fixa. | Art. 16, § 13 |
add_item(
    0, 169, "art. 16", "l8429", "OK",
    "É vedada a decretação de indisponibilidade da quantia de até 40 (quarenta) salários mínimos depositados em caderneta de poupança, em outras aplicações financeiras ou em conta-corrente."
)

# Item 1 (linha 170)
# | **Ordem de Preferência** | Veículos (1º), imóveis (2º), móveis (3º)... bloqueio bancário em último lugar (8º). | Art. 16, § 11 |
add_item(
    1, 170, "art. 16", "l8429", "OK",
    "A ordem de indisponibilidade de bens deverá priorizar veículos de via terrestre, bens imóveis, bens móveis em geral, semoventes, navios e aeronaves, ações e quotas de sociedades simples e empresárias, pedras e metais preciosos e, apenas na inexistência desses, o bloqueio de contas bancárias"
)

# Item 2 (linha 171)
# | **Competência Jurisdicional** | Juízo de 1º grau da Justiça Comum; ausente foro privilegiado (Tema 576). | STF (Tema 576 e ADI 2.797) |
add_item(
    2, 171, "Tema 576", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 3 (linha 173)
# | **Eficácia da Condenação** | Perda da função pública e suspensão de direitos exigem trânsito em julgado. | Art. 20, caput |
add_item(
    3, 173, "art. 20", "l8429", "OK",
    "A perda da função pública e a suspensão dos direitos políticos só se efetivam com o trânsito em julgado da sentença condenatória."
)

# Item 4 (linha 174)
# | **Afastamento Preventivo** | Medida cautelar de até 90 dias prorrogável uma vez, com remuneração integral. | Art. 20, § 1º e 2º |
add_item(
    4, 174, "art. 20", "l8429", "OK",
    "O afastamento previsto no § 1º deste artigo será de até 90 (noventa) dias, prorrogáveis uma única vez por igual prazo, mediante decisão motivada."
)

# Item 5 (linha 175)
# | **Extensão da Perda da Função** | Estende-se como regra aos demais vínculos públicos mantidos pelo condenado. | Art. 12, § 1º, e ADIs 7156/7236 |
add_item(
    5, 175, "art. 12", "l8429", "OK",
    "A sanção de perda da função pública, nas hipóteses dos incisos I e II do caput deste artigo, atinge apenas o vínculo de mesma qualidade e natureza que o agente público ou político detinha com o poder público na época do cometimento da infração,"
)

# Item 6 (linha 176)
# | **Execução pelo MP** | MP executa se o ente lesado não o fizer em 6 meses do trânsito em julgado. | Art. 18, § 2º |
add_item(
    6, 176, "art. 18", "l8429", "OK",
    "Caso a pessoa jurídica prejudicada não adote as providências a que se refere o § 1º deste artigo no prazo de 6 (seis) meses, contado do trânsito em julgado da sentença de procedência da ação, caberá ao Ministério Público proceder à respectiva liquidação do dano e ao cumprimento da sentença"
)

# Item 7 (linha 177)
# | **Parcelamento em 48 Vezes** | Possibilidade de quitação em até 48 parcelas mensais corrigidas monetariamente. | Art. 18, § 4º |
add_item(
    7, 177, "art. 18", "l8429", "OK",
    "O juiz poderá autorizar o parcelamento, em até 48 (quarenta e oito) parcelas mensais corrigidas monetariamente, do débito resultante de condenação pela prática de improbidade administrativa se o réu demonstrar incapacidade financeira de saldá-lo de imediato."
)

# Item 8 (linha 178)
# | **Custas e Honorários** | Sem adiantamento de custas e sem honorários sucumbenciais pelo autor, salvo má-fé. | Art. 23-B |
add_item(
    8, 178, "art. 23", "l8429", "OK",
    "Nas ações e nos acordos regidos por esta Lei, não haverá adiantamento de custas, de preparo, de emolumentos, de honorários periciais e de quaisquer outras despesas."
)

# Item 9 (linha 183)
# - A ordem legal do art. 16, § 11, prioriza veículos e imóveis, deixando o bloqueio de contas em último lugar, sendo impenhoráveis até quarenta salários mínimos e vedada a constrição de multa civil.
add_item(
    9, 183, "art. 16", "l8429", "OK",
    "A indisponibilidade recairá sobre bens que assegurem exclusivamente o integral ressarcimento do dano ao erário, sem incidir sobre os valores a serem eventualmente aplicados a título de multa civil ou sobre acréscimo patrimonial decorrente de atividade lícita."
)

# Item 10 (linha 184)
# - Os agentes públicos respondem perante a 1ª instância sem foro privilegiado (Tema 576 do STF), salvo o Presidente da República, que responde no Senado por crime de responsabilidade (Pet 3240).
add_item(
    10, 184, "Tema 576", "cf", "OK",
    "São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: V - a probidade na administração;"
)

# Item 11 (linha 185)
# - A perda da função pública e a suspensão de direitos políticos dependem do trânsito em julgado (art. 20), mas admite-se afastamento cautelar de 90 dias com remuneração.
add_item(
    11, 185, "art. 20", "l8429", "OK",
    "A autoridade judicial competente poderá determinar o afastamento do agente público do exercício do cargo, do emprego ou da função, sem prejuízo da remuneração, quando a medida for necessária à instrução processual ou para evitar a iminente prática de novos ilícitos."
)

# Item 12 (linha 187)
# - A pessoa jurídica lesada tem preferência para liquidar e executar a condenação em 6 meses, atuando o MP subsidiariamente (art. 18, § 1º e 2º).
add_item(
    12, 187, "art. 18", "l8429", "OK",
    "Se houver necessidade de liquidação do dano, a pessoa jurídica prejudicada procederá a essa determinação e ao ulterior procedimento para cumprimento da sentença referente ao ressarcimento do patrimônio público ou à perda ou à reversão dos bens."
)

# Item 13 (linha 188)
# - É cabível o desconto dos serviços prestados (art. 18, § 3º) e o parcelamento da condenação em até 48 vezes mensais corrigidas (art. 18, § 4º).
add_item(
    13, 188, "art. 18", "l8429", "OK",
    "Para fins de apuração do valor do ressarcimento, deverão ser descontados os serviços efetivamente prestados."
)

# Item 14 (linha 189)
# - O autor da ação não adianta custas nem responde por honorários advocatícios, salvo má-fé comprovada (Lei nº 8.429/1992, art. 23-B).
add_item(
    14, 189, "art. 23, Lei nº 8.429/1992", "l8429", "OK",
    "Haverá condenação em honorários sucumbenciais em caso de improcedência da ação de improbidade se comprovada má-fé."
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s08-p3",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s08-p3.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
