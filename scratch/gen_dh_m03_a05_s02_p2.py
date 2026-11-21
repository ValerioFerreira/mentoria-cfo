import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m03_a05-s02-p2/unidade.json"
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
    
    t_check = norm(trecho_lei)[:120]
    if t_check not in norm_cf:
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

add_item(0, 170, "art. 5", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

add_item(1, 176, "art. 3", "cf", "OK",
    "Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil: I - construir uma sociedade livre, justa e solidária; II - garantir o desenvolvimento nacional;")

add_item(2, 177, "art. 1, art. 4", "cf", "OK",
    "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I - independência nacional; II - prevalência dos direitos humanos;")

add_item(3, 178, "art. 5", "cf", "OK",
    "§ 1º As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.")

add_item(4, 183, "art. 5", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

add_item(5, 188, "art. 1, art. 3", "cf", "OK",
    "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:")

add_item(6, 189, "art. 4", "cf", "OK",
    "I - independência nacional; II - prevalência dos direitos humanos; III - autodeterminação dos povos;")

add_item(7, 190, "art. 4", "cf", "OK",
    "VIII - repúdio ao terrorismo e ao racismo; IX - cooperação entre os povos para o progresso da humanidade; X - concessão de asilo político.")

add_item(8, 191, "art. 5", "cf", "OK",
    "As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.")

add_item(9, 192, "art. 5", "cf", "OK",
    "Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte.")

add_item(10, 194, "art. 60", "cf", "OK",
    "Não será objeto de deliberação a proposta de emenda tendente a abolir: I - a forma federativa de Estado; II - o voto direto, secreto, universal e periódico; III - a separação dos Poderes; IV - os direitos e garantias individuais.")

add_item(11, 196, "art. 5", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

out = {
    "unidade": "CENSO-direitos-humanos_m03_a05-s02-p2",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m03_a05-s02-p2.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
