import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c02-s01-p3/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")
txt_d6949 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d6949.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)
norm_d6949 = norm(txt_d6949)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_cf if lei == "cf" else norm_d6949
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

add_item(0, 134, "art. 45", "d6949", "OK",
    "Artigo 45 Entrada em vigor 1.A presente Convenção entrará em vigor no trigésimo dia após o depósito do vigésimo instrumento de ratificação ou adesão.")

add_item(1, 135, "art. 13", "d6949", "OK",
    "Artigo 13 1.Sujeito à entrada em vigor da Convenção, o presente Protocolo entrará em vigor no trigésimo dia após o depósito do décimo instrumento de ratificação ou adesão.")

add_item(2, 140, "art. 5", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(3, 143, "art. 1", "d6949", "OK",
    "Pessoas com deficiência são aquelas que têm impedimentos de longo prazo de natureza física, mental, intelectual ou sensorial, os quais, em interação com diversas barreiras, podem obstruir sua participação plena e efetiva na sociedade")

add_item(4, 146, "art. 12", "d6949", "OK",
    "2.Os Estados Partes reconhecerão que as pessoas com deficiência gozam de capacidade legal em igualdade de condições com as demais pessoas em todos os aspectos da vida.")

add_item(5, 164, "art. 12", "d6949", "OK",
    "Artigo 12 Reconhecimento igual perante a lei 1.Os Estados Partes reafirmam que as pessoas com deficiência têm o direito de ser reconhecidas em qualquer lugar como pessoas perante a lei.")

add_item(6, 173, "art. 3", "d6949", "OK",
    "Artigo 3 Princípios gerais Os princípios da presente Convenção são: a) O respeito pela dignidade inerente, a autonomia individual, inclusive a liberdade de fazer as próprias escolhas, e a independência das pessoas; b) A não-discriminação;")

add_item(7, 174, "art. 12", "d6949", "OK",
    "gozam de capacidade legal em igualdade de condições com as demais pessoas em todos os aspectos da vida.")

add_item(8, 175, "art. 33", "d6949", "OK",
    "Artigo 33 Implementação e monitoramento nacionais 1.Os Estados Partes, de acordo com seu sistema organizacional, designarão um ou mais de um ponto focal no âmbito do Governo para assuntos relacionados com a implementação")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c02-s01-p3",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c02-s01-p3.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
