import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c01-s01-p1/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")
txt_d4377 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d4377.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)
norm_d4377 = norm(txt_d4377)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_cf if lei == "cf" else norm_d4377
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

add_item(0, 18, "art. 1, art. 2", "d4377", "OK",
    "Para os fins da presente Convenção, a expressão \"discriminação contra a mulher\" significará toda a distinção, exclusão ou restrição baseada no sexo")

add_item(1, 28, "art. 15", "d4377", "OK",
    "com reservas aos seus artigos 15, parágrafo 4o, e 16, parágrafo 1o, alíneas (a), (c), (g) e (h);")

add_item(2, 29, "art. 5, art. 226", "cf", "OK",
    "I - homens e mulheres são iguais em direitos e obrigações, nos termos desta Constituição;")

add_item(3, 31, "EC 45", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(4, 36, "art. 1", "d4377", "OK",
    "significará toda a distinção, exclusão ou restrição baseada no sexo e que tenha por objeto ou resultado prejudicar ou anular o reconhecimento, gozo ou exercício pela mulher")

add_item(5, 37, "art. 7", "d4377", "OK",
    "Artigo 7o Os Estados-Partes tomarão todas as medidas apropriadas para eliminar a discriminação contra a mulher na vida política e pública do país")

add_item(6, 38, "art. 10", "d4377", "OK",
    "Artigo 10 Os Estados-Partes adotarão todas as medidas apropriadas para eliminar a discriminação contra a mulher, a fim de assegurar-lhe a igualdade de direitos com o homem na esfera da educação")

add_item(7, 39, "art. 15", "d4377", "OK",
    "Artigo 15 1. Os Estados-Partes reconhecerão à mulher a igualdade com o homem perante a lei.")

add_item(8, 40, "art. 17", "d4377", "OK",
    "Com o fim de examinar os progressos alcançados na aplicação desta Convenção, será estabelecido um Comitê sobre a Eliminação da Discriminação contra a Mulher")

add_item(9, 41, "art. 23", "d4377", "OK",
    "Artigo 23 Nada do disposto nesta Convenção prejudicará qualquer disposição que seja mais propícia à obtenção da igualdade entre homens e mulheres")

add_item(10, 43, "art. 1", "d4377", "OK",
    "independentemente de seu estado civil, com base na igualdade do homem e da mulher, dos direitos humanos e liberdades fundamentais nos campos político, econômico, social, cultural e civil ou em qualquer outro campo.")

add_item(11, 45, "art. 1", "d4377", "OK",
    "Para os fins da presente Convenção, a expressão \"discriminação contra a mulher\" significará toda a distinção, exclusão ou restrição baseada no sexo")

add_item(12, 49, "art. 1", "d4377", "OK",
    "prejudicar ou anular o reconhecimento, gozo ou exercício pela mulher, independentemente de seu estado civil, com base na igualdade do homem e da mulher")

add_item(13, 52, "art. 1", "d4377", "OK",
    "dos direitos humanos e liberdades fundamentais nos campos político, econômico, social, cultural e civil ou em qualquer outro campo.")

add_item(14, 57, "art. 2", "d4377", "OK",
    "Artigo 2o Os Estados Partes condenam a discriminação contra a mulher em todas as suas formas, concordam em seguir, por todos os meios apropriados e sem dilações, uma política destinada a eliminar a discriminação contra a mulher")

add_item(15, 59, "art. 2", "d4377", "OK",
    "concordam em seguir, por todos os meios apropriados e sem dilações, uma política destinada a eliminar a discriminação contra a mulher, e com tal objetivo se comprometem a:")

add_item(16, 60, "art. 2", "d4377", "OK",
    "a) Consagrar, se ainda não o tiverem feito, em suas constituições nacionais ou em outra legislação apropriada o princípio da igualdade do homem e da mulher e assegurar por lei outros meios apropriados a realização prática desse princípio;")

add_item(17, 61, "art. 2", "d4377", "OK",
    "b) Adotar medidas adequadas, legislativas e de outro caráter, com as sanções cabíveis e que proíbam toda discriminação contra a mulher;")

add_item(18, 62, "art. 2", "d4377", "OK",
    "c) Estabelecer a proteção jurídica dos direitos da mulher numa base de igualdade com os do homem e garantir, por meio dos tribunais nacionais competentes e de outras instituições públicas, a proteção efetiva da mulher contra todo ato de discriminação;")

add_item(19, 63, "art. 2", "d4377", "OK",
    "d) Abster-se de incorrer em todo ato ou prática de discriminação contra a mulher e zelar para que as autoridades e instituições públicas atuem em conformidade com esta obrigação;")

add_item(20, 64, "art. 2", "d4377", "OK",
    "e) Tomar as medidas apropriadas para eliminar a discriminação contra a mulher praticada por qualquer pessoa, organização ou empresa;")

add_item(21, 65, "art. 2", "d4377", "OK",
    "f) Adotar todas as medidas adequadas, inclusive de caráter legislativo, para modificar ou derrogar leis, regulamentos, usos e práticas que constituam discriminação contra a mulher; g) Derrogar todas as disposições penais nacionais que constituam discriminação contra a mulher.")

add_item(22, 67, "art. 4", "d4377", "OK",
    "Artigo 4o 1. A adoção pelos Estados-Partes de medidas especiais de caráter temporário destinadas a acelerar a igualdade de fato entre o homem e a mulher não se considerará discriminação na forma definida nesta Convenção")

add_item(23, 69, "art. 4", "d4377", "OK",
    "2. A adoção pelos Estados-Partes de medidas especiais, inclusive as contidas na presente Convenção, destinadas a proteger a maternidade, não se considerará discriminatória.")

add_item(24, 73, "art. 4", "d4377", "OK",
    "mas de nenhuma maneira implicará, como conseqüência, a manutenção de normas desiguais ou separadas; essas medidas cessarão quando os objetivos de igualdade de oportunidade e tratamento houverem sido alcançados.")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c01-s01-p1",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c01-s01-p1.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
