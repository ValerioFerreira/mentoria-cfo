import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m03_a04-s01/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")
txt_d7037 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d7037.clean.txt").read_text(encoding="utf-8")
txt_l11340 = (ROOT / "pipeline/.cache/leis-oficiais/leis/l11340.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)
norm_d7037 = norm(txt_d7037)
norm_l11340 = norm(txt_l11340)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    if lei == "cf":
        t_clean = norm_cf
    elif lei == "d7037":
        t_clean = norm_d7037
    elif lei == "l11340":
        t_clean = norm_l11340
    else:
        t_clean = None
    
    if t_clean is not None:
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

# Item 0 (linha 39)
add_item(
    0, 39, "Lei nº 10.741/2003", "l10741", "OK",
    "destinado a regular os direitos assegurados",
    url="http://www.planalto.gov.br/ccivil_03/leis/2003/l10.741.htm"
)

# Item 1 (linha 40)
add_item(
    1, 40, "Lei nº 8.842/1994", "l8842", "OK",
    "tem por objetivo assegurar os direitos sociais do idoso",
    url="http://www.planalto.gov.br/ccivil_03/leis/l8842.htm"
)

# Item 2 (linha 42)
add_item(
    2, 42, "Lei nº 11.340/2006", "l11340", "OK",
    "Esta Lei cria mecanismos para coibir e prevenir a violência doméstica e familiar contra a mulher"
)

# Item 3 (linha 69)
add_item(
    3, 69, "art. 7", "d7037", "OK",
    "Art. 7o Fica revogado o Decreto no 4.229, de 13 de maio de 2002."
)

# Item 4 (linha 83)
add_item(
    4, 83, "art. 84, EC 32", "cf", "OK",
    "organização e funcionamento da administração federal, quando não implicar aumento de despesa nem criação ou extinção de órgãos públicos;"
)

# Item 5 (linha 85)
add_item(
    5, 85, "art. 84", "cf", "OK",
    "Art. 84. Compete privativamente ao Presidente da República:"
)

# Item 6 (linha 86)
add_item(
    6, 86, "art. 84", "cf", "OK",
    "Compete privativamente ao Presidente da República:"
)

# Item 7 (linha 91)
add_item(
    7, 91, "art. 3", "d7037", "OK",
    "Art. 3o As metas, prazos e recursos necessários para a implementação do PNDH-3 serão definidos e aprovados em Planos de Ação de Direitos Humanos bianuais"
)

# Item 8 (linha 138)
add_item(
    8, 138, "art. 84", "cf", "OK",
    "a) organização e funcionamento da administração federal, quando não implicar aumento de despesa nem criação ou extinção de órgãos públicos;"
)

out = {
    "unidade": "CENSO-direitos-humanos_m03_a04-s01",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m03_a04-s01.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
