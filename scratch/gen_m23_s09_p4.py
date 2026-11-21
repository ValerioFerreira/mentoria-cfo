import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s09-p4/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_l8429 = (ROOT / "pipeline/.cache/leis-oficiais/leis/l8429.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_l8429 = norm(txt_l8429)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_l8429
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

# Item 0 (linha 307)
# - A responsabilidade pelo ressarcimento do dano é solidária entre os coautores dolosos, mas a multa civil sancionatória é estritamente pessoal e individualizada (Lei nº 8.429/1992, art. 17-C, § 2º).
add_item(
    0, 307, "art. 17, Lei nº 8.429/1992", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 1 (linha 308)
# - É inadmissível a propositura de ação de improbidade exclusivamente contra particular, aplicando-se ao terceiro o mesmo regime prescricional do servidor (STJ, Súmula 634).
add_item(
    1, 308, "Súmula 634", "l8429", "OK",
    "A suspensão e a interrupção da prescrição produzem efeitos relativamente a todos os que concorreram para a prática do ato de improbidade."
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s09-p4",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s09-p4.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
