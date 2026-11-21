import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m01_a00-s01/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_cf
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

# Item 0 (linha 39)
# Vale estudar ainda a relação entre direitos humanos, cidadania e democracia...
add_item(
    0, 39, "art. 1", "cf", "OK",
    "II - a cidadania; III - a dignidade da pessoa humana; IV - os valores sociais do trabalho e da livre iniciativa;"
)

# Item 1 (linha 45)
# A Constituição de 1988 escolheu a dignidade da pessoa humana como um dos fundamentos da República (art. 1º, III)...
add_item(
    1, 45, "art. 1", "cf", "OK",
    "III - a dignidade da pessoa humana;"
)

# Item 2 (linha 47)
# > [!lei] CF, art. 1º, III
add_item(
    2, 47, "art. 1", "cf", "OK",
    "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:"
)

# Item 3 (linha 48)
# > Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:
add_item(
    3, 48, "art. 1", "cf", "OK",
    "A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:"
)

out = {
    "unidade": "CENSO-direitos-humanos_m01_a00-s01",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m01_a00-s01.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
