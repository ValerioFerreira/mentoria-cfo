import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m03_a05-s02-p1/unidade.json"
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

add_item(0, 17, "art. 1, art. 3, art. 4", "cf", "OK",
    "Art. 1º A República Federativa do Brasil, formada pela união indissolúvel dos Estados e Municípios e do Distrito Federal, constitui-se em Estado Democrático de Direito e tem como fundamentos:")

add_item(1, 24, "art. 1, art. 3", "cf", "OK",
    "Art. 3º Constituem objetivos fundamentais da República Federativa do Brasil: I - construir uma sociedade livre, justa e solidária; II - garantir o desenvolvimento nacional;")

add_item(2, 28, "art. 1, art. 3", "cf", "OK",
    "III - erradicar a pobreza e a marginalização e reduzir as desigualdades sociais e regionais; IV - promover o bem de todos, sem preconceitos de origem, raça, sexo, cor, idade e quaisquer outras formas de discriminação.")

add_item(3, 36, "art. 4", "cf", "OK",
    "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I - independência nacional; II - prevalência dos direitos humanos;")

add_item(4, 38, "art. 4", "cf", "OK",
    "III - autodeterminação dos povos; IV - não-intervenção; V - igualdade entre os Estados; VI - defesa da paz; VII - solução pacífica dos conflitos;")

add_item(5, 58, "art. 4", "cf", "OK",
    "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I - independência nacional; II - prevalência dos direitos humanos;")

add_item(6, 63, "art. 1, art. 3, art. 4", "cf", "OK",
    "I - independência nacional; II - prevalência dos direitos humanos; III - autodeterminação dos povos;")

add_item(7, 69, "art. 5", "cf", "OK",
    "§ 1º As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.")

add_item(8, 86, "art. 60", "cf", "OK",
    "Não será objeto de deliberação a proposta de emenda tendente a abolir: I - a forma federativa de Estado; II - o voto direto, secreto, universal e periódico; III - a separação dos Poderes; IV - os direitos e garantias individuais.")

add_item(9, 88, "art. 5", "cf", "OK",
    "I - a forma federativa de Estado; II - o voto direto, secreto, universal e periódico; III - a separação dos Poderes; IV - os direitos e garantias individuais.")

add_item(10, 92, "EC 45", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(11, 96, "art. 5", "cf", "OK",
    "aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(12, 102, "art. 5", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros")

add_item(13, 107, "art. 5, art. 7, EC 45", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

add_item(14, 113, "art. 109", "cf", "OK",
    "Nas hipóteses de grave violação de direitos humanos, o Procurador-Geral da República, com a finalidade de assegurar o cumprimento de obrigações decorrentes de tratados internacionais de direitos humanos dos quais o Brasil seja parte, poderá suscitar, perante o Superior Tribunal de Justiça, em qualquer fase do inquérito ou processo, incidente de deslocamento de competência para a Justiça Federal.")

add_item(15, 148, "art. 4", "cf", "OK",
    "Art. 4º A República Federativa do Brasil rege-se nas suas relações internacionais pelos seguintes princípios: I - independência nacional; II - prevalência dos direitos humanos;")

add_item(16, 149, "art. 5", "cf", "OK",
    "As normas definidoras dos direitos e garantias fundamentais têm aplicação imediata.")

add_item(17, 150, "art. 5", "cf", "OK",
    "Os direitos e garantias expressos nesta Constituição não excluem outros decorrentes do regime e dos princípios por ela adotados, ou dos tratados internacionais em que a República Federativa do Brasil seja parte.")

add_item(18, 152, "art. 60", "cf", "OK",
    "Não será objeto de deliberação a proposta de emenda tendente a abolir: I - a forma federativa de Estado;")

add_item(19, 153, "art. 5", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(20, 154, "art. 5", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

add_item(21, 155, "art. 109", "cf", "OK",
    "as causas relativas a direitos humanos a que se refere o § 5º deste artigo;")

add_item(22, 157, "art. 5, EC 45", "cf", "OK",
    "O Brasil se submete à jurisdição de Tribunal Penal Internacional a cuja criação tenha manifestado adesão.")

add_item(23, 161, "art. 4", "cf", "OK",
    "III - autodeterminação dos povos; IV - não-intervenção; V - igualdade entre os Estados; VI - defesa da paz;")

add_item(24, 165, "art. 1, art. 4, art. 5, art. 60", "cf", "OK",
    "Nas hipóteses de grave violação de direitos humanos, o Procurador-Geral da República, com a finalidade de assegurar o cumprimento de obrigações decorrentes de tratados internacionais de direitos humanos")

out = {
    "unidade": "CENSO-direitos-humanos_m03_a05-s02-p1",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m03_a05-s02-p1.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
