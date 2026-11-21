import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m03_a04-s02/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_d7037 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d7037.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_d7037 = norm(txt_d7037)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    if lei == "d7037":
        t_clean = norm_d7037
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
    if url:
        rec["url"] = url
    if resultado == "ERRO":
        rec["severidade"] = severidade
        rec["diferenca"] = diferenca
        rec["texto_novo"] = texto_novo
    censo.append(rec)

# Item 0 (linha 33)
add_item(
    0, 33, "art. 2", "d7037", "OK",
    "Art. 2o O PNDH-3 será implementado de acordo com os seguintes eixos orientadores e suas respectivas diretrizes:"
)

# Item 1 (linha 99)
add_item(
    1, 99, "art. 5", "d7037", "OK",
    "Art. 5o Os Estados, o Distrito Federal, os Municípios e os órgãos do Poder Legislativo, do Poder Judiciário e do Ministério Público serão convidados a aderir ao PNDH-3."
)

# Item 2 (linha 101)
add_item(
    2, 101, "art. 3, art. 4", "d7037", "OK",
    "Art. 3o As metas, prazos e recursos necessários para a implementação do PNDH-3 serão definidos e aprovados em Planos de Ação de Direitos Humanos bianuais"
)

# Item 3 (linha 110)
add_item(
    3, 110, "art. 8, Lei nº 12.528/2011", "l12528", "OK",
    "com a finalidade de examinar e esclarecer as graves",
    url="http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12528.htm"
)

# Item 4 (linha 131)
add_item(
    4, 131, "Lei nº 12.528/2011", "l12528", "OK",
    "ato das disposies constitucionais transitrias a fim de efetivar o direito",
    url="http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12528.htm"
)

# Item 5 (linha 161)
add_item(
    5, 161, "Lei nº 12.528/2011", "l12528", "OK",
    "composta de forma pluralista ser integrada por 7 sete membros designados pelo presidente da repblica",
    url="http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12528.htm"
)

# Item 6 (linha 173)
add_item(
    6, 173, "Lei nº 12.528/2011", "l12528", "OK",
    "com a finalidade de examinar e esclarecer as graves",
    url="http://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12528.htm"
)

out = {
    "unidade": "CENSO-direitos-humanos_m03_a04-s02",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m03_a04-s02.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
