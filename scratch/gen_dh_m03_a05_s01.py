import json
import re
from pathlib import Path
import sys

sys.path.insert(0, "material-pdf/_avaliacao/2026-11-11/ferramentas")
import validar_v3 as V

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m03_a05-s01/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")
txt_racismo = (ROOT / "pipeline/.cache/leis-oficiais/leis/racismo.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)
norm_racismo = norm(txt_racismo)

url_1824 = "http://www.planalto.gov.br/ccivil_03/constituicao/constituicao24.htm"

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    if lei == "cf":
        t_clean = norm_cf
    elif lei == "racismo":
        t_clean = norm_racismo
    else:
        t_clean = None
    
    if t_clean is not None:
        t_check = norm(trecho_lei)[:120]
        if t_check not in t_clean:
            print(f"ERROR: item {idx} (linha {linha}): trecho_lei not in {lei}!")
            print("Trecho:", t_check)
    elif url:
        err = V.V.checar_trecho_url(url, trecho_lei)
        if err:
            print(f"ERROR URL item {idx} (linha {linha}): {err}")
    
    rec = {
        "linha": linha,
        "citacao": citacao,
        "lei": lei,
        "frase_capitulo": frase_capitulo,
        "trecho_lei": trecho_lei,
        "resultado": resultado
    }
    if url:
        rec["url"] = url
    if resultado == "ERRO":
        rec["severidade"] = severidade
        rec["diferenca"] = diferenca
        rec["texto_novo"] = texto_novo
    censo.append(rec)

# Item 0 (linha 19)
add_item(
    0, 19, "art. 1", "cf", "OK",
    "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:"
)

# Item 1 (linha 34)
add_item(
    1, 34, "art. 179", "cf1824", "OK",
    "179 a inviolabilidade dos direitos civis e politicos",
    url=url_1824
)

# Item 2 (linha 43)
add_item(
    2, 43, "art. 179", "cf1824", "OK",
    "tem por base a liberdade a segurana individual e a propriedade",
    url=url_1824
)

# Item 3 (linha 73)
add_item(
    3, 73, "Lei nº 7.716/1989", "racismo", "OK",
    "Define os crimes resultantes de preconceito de raça ou de cor."
)

# Item 4 (linha 81)
add_item(
    4, 81, "art. 1", "cf", "OK",
    "I - a soberania; II - a cidadania; III - a dignidade da pessoa humana;"
)

# Item 5 (linha 85)
add_item(
    5, 85, "art. 1", "cf", "OK",
    "formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito"
)

# Item 6 (linha 87)
add_item(
    6, 87, "art. 1", "cf", "OK",
    "Parágrafo único. Todo o poder emana do povo, que o exerce por meio de representantes eleitos ou diretamente, nos termos desta Constituição."
)

# Item 7 (linha 93)
add_item(
    7, 93, "art. 1", "cf", "OK",
    "IV - os valores sociais do trabalho e da livre iniciativa;"
)

# Item 8 (linha 94)
add_item(
    8, 94, "art. 1", "cf", "OK",
    "A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:"
)

# Item 9 (linha 124)
add_item(
    9, 124, "art. 2", "cf", "OK",
    "Art. 2º São Poderes da União, independentes e harmônicos entre si, o Legislativo, o Executivo e o Judiciário."
)

# Item 10 (linha 129)
add_item(
    10, 129, "art. 1, art. 3", "cf", "OK",
    "Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil: I - construir uma sociedade livre, justa e solidária;"
)

# Item 11 (linha 149)
add_item(
    11, 149, "art. 1", "cf", "OK",
    "I - a soberania; II - a cidadania; III - a dignidade da pessoa humana; IV - os valores sociais do trabalho e da livre iniciativa;"
)

# Item 12 (linha 154)
add_item(
    12, 154, "art. 1, art. 4", "cf", "OK",
    "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I - independência nacional; II - prevalência dos direitos humanos;"
)

# Item 13 (linha 165)
add_item(
    13, 165, "art. 1", "cf", "OK",
    "I - a soberania; II - a cidadania; III - a dignidade da pessoa humana;"
)

# Item 14 (linha 172)
add_item(
    14, 172, "art. 179", "cf1824", "OK",
    "179 a inviolabilidade dos direitos civis e politicos",
    url=url_1824
)

# Item 15 (linha 177)
add_item(
    15, 177, "Lei nº 7.716/1989", "racismo", "OK",
    "Serão punidos, na forma desta Lei, os crimes resultantes de discriminação ou preconceito de raça, cor, etnia, religião ou procedência nacional."
)

# Item 16 (linha 178)
add_item(
    16, 178, "art. 1", "cf", "OK",
    "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:"
)

out = {
    "unidade": "CENSO-direitos-humanos_m03_a05-s01",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m03_a05-s01.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
