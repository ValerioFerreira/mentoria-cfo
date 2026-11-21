import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m02_a02-s01/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
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

# Item 0 (linha 43)
# Há discussão sobre a presença dos direitos de solidariedade, como o direito ao meio ambiente, na DUDH. Parte da doutrina vê neles uma presença ligada à fraternidade do art. 1º...
add_item(
    0, 43, "art. 1", "dudh", "OK",
    "Todos os seres humanos nascem livres e iguais em dignidade e direitos",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 1 (linha 77)
# 1. **Interpretação autorizada da Carta da ONU.** A Carta, no art. 1º, item 3... No art. 55...
add_item(
    1, 77, "art. 1, art. 55", "carta-onu", "OK",
    "para promover e estimular o respeito aos direitos humanos",
    url="http://www.planalto.gov.br/ccivil_03/decreto/1930-1949/d19841.htm"
)

# Item 2 (linha 84)
# | 1º | Interpretação autorizada de "direitos humanos" na Carta da ONU (arts. 1º, 3 e 55) | Carta |
add_item(
    2, 84, "art. 1", "carta-onu", "OK",
    "o respeito universal e efetivo dos direitos humanos e das liberdades fundamentais para todos",
    url="http://www.planalto.gov.br/ccivil_03/decreto/1930-1949/d19841.htm"
)

# Item 3 (linha 163)
# 7. A DUDH é vinculante, embora editada como resolução: interpreta a Carta da ONU (arts. 1º, 3 e 55) e constitui costume ou princípio geral do direito internacional.
add_item(
    3, 163, "art. 1", "carta-onu", "OK",
    "com esta em conjunto ou separadamente",
    url="http://www.planalto.gov.br/ccivil_03/decreto/1930-1949/d19841.htm"
)

out = {
    "unidade": "CENSO-direitos-humanos_m02_a02-s01",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m02_a02-s01.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
