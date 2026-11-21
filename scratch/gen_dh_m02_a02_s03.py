import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m02_a02-s03/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    if lei == "cf":
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
    if url:
        rec["url"] = url
    if resultado == "ERRO":
        rec["severidade"] = severidade
        rec["diferenca"] = diferenca
        rec["texto_novo"] = texto_novo
    censo.append(rec)

# Item 0 (linha 38)
add_item(
    0, 38, "art. 7, art. 11", "cf", "OK",
    "Art. 7º São direitos dos trabalhadores urbanos e rurais, além de outros que visem à melhoria de sua condição social:"
)

# Item 1 (linha 61)
add_item(
    1, 61, "art. 205", "cf", "OK",
    "A educação, direito de todos e dever do Estado e da família, será promovida e incentivada com a colaboração da sociedade, visando ao pleno desenvolvimento da pessoa"
)

# Item 2 (linha 67)
add_item(
    2, 67, "art. 5, art. 23", "cf", "OK",
    "IX - é livre a expressão da atividade intelectual, artística, científica e de comunicação, independentemente de censura ou licença;"
)

# Item 3 (linha 73)
add_item(
    3, 73, "art. 22", "dudh", "OK",
    "todo ser humano como membro da sociedade tem direito a seguranca social",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 4 (linha 75)
add_item(
    4, 75, "art. 22, art. 23", "dudh", "OK",
    "todo ser humano tem direito ao trabalho a livre escolha de emprego",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 5 (linha 76)
add_item(
    5, 76, "art. 25", "dudh", "OK",
    "todo ser humano tem direito a um padrao de vida capaz de assegurar",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 6 (linha 77)
add_item(
    6, 77, "art. 26", "dudh", "OK",
    "todo ser humano tem direito a instrucao a instrucao sera gratuita",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 7 (linha 78)
add_item(
    7, 78, "art. 27", "dudh", "OK",
    "todo ser humano tem o direito de participar livremente da vida cultural da comunidade",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 8 (linha 79)
add_item(
    8, 79, "art. 28", "dudh", "OK",
    "todo ser humano tem direito a uma ordem social e internacional",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 9 (linha 100)
add_item(
    9, 100, "art. 29", "dudh", "OK",
    "todo ser humano tem deveres para com a comunidade",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

out = {
    "unidade": "CENSO-direitos-humanos_m02_a02-s03",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m02_a02-s03.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
