import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c02-s01-p1/unidade.json"
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

add_item(0, 18, "art. 2, art. 3", "d6949", "OK",
    "Artigo 2 Definições Para os propósitos da presente Convenção: “Comunicação” abrange as línguas, a visualização de textos, o braille")

add_item(1, 19, "art. 12", "d6949", "OK",
    "Artigo 12 Reconhecimento igual perante a lei 1.Os Estados Partes reafirmam que as pessoas com deficiência têm o direito de ser reconhecidas em qualquer lugar como pessoas perante a lei.")

add_item(2, 26, "art. 5", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(3, 27, "art. 5", "cf", "OK",
    "aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(4, 33, "art. 1", "d6949", "OK",
    "Artigo 1 Propósito O propósito da presente Convenção é promover, proteger e assegurar o exercício pleno e eqüitativo de todos os direitos humanos e liberdades fundamentais por todas as pessoas com deficiência")

add_item(5, 35, "art. 1", "d6949", "OK",
    "Pessoas com deficiência são aquelas que têm impedimentos de longo prazo de natureza física, mental, intelectual ou sensorial, os quais, em interação com diversas barreiras, podem obstruir sua participação plena e efetiva na sociedade")

add_item(6, 41, "art. 1", "d6949", "OK",
    "impedimentos de longo prazo de natureza física, mental, intelectual ou sensorial, os quais, em interação com diversas barreiras, podem obstruir sua participação plena e efetiva na sociedade em igualdades de condições com as demais pessoas.")

add_item(7, 43, "art. 2, art. 3", "d6949", "OK",
    "Artigo 3 Princípios gerais Os princípios da presente Convenção são: a) O respeito pela dignidade inerente, a autonomia individual")

add_item(8, 45, "art. 2", "d6949", "OK",
    "“Língua” abrange as línguas faladas e de sinais e outras formas de comunicação não-falada;")

add_item(9, 47, "art. 2", "d6949", "OK",
    "“Adaptação razoável” significa as modificações e os ajustes necessários e adequados que não acarretem ônus desproporcional ou indevido")

add_item(10, 49, "art. 2", "d6949", "OK",
    "“Desenho universal” significa a concepção de produtos, ambientes, programas e serviços a serem usados, na maior medida possível, por todas as pessoas, sem necessidade de adaptação ou projeto específico.")

add_item(11, 57, "art. 3", "d6949", "OK",
    "a) O respeito pela dignidade inerente, a autonomia individual, inclusive a liberdade de fazer as próprias escolhas, e a independência das pessoas;")

add_item(12, 59, "art. 3", "d6949", "OK",
    "b) A não-discriminação; c) A plena e efetiva participação e inclusão na sociedade; d) O respeito pela diferença e pela aceitação das pessoas com deficiência como parte da diversidade humana e da humanidade;")

add_item(13, 69, "art. 4", "d6949", "OK",
    "Artigo 4 Obrigações gerais 1.Os Estados Partes se comprometem a assegurar e promover o pleno exercício de todos os direitos humanos e liberdades fundamentais por todas as pessoas com deficiência")

add_item(14, 71, "art. 4", "d6949", "OK",
    "a) Adotar todas as medidas legislativas, administrativas e de qualquer outra natureza, necessárias para a realização dos direitos reconhecidos na presente Convenção;")

add_item(15, 72, "art. 4", "d6949", "OK",
    "3.Na elaboração e implementação de legislação e políticas para aplicar a presente Convenção e em outros processos de tomada de decisão relativos às pessoas com deficiência, os Estados Partes realizarão consultas estreitas e envolverão ativamente pessoas com deficiência, inclusive crianças com deficiência, por intermédio de suas organizações representativas.")

add_item(16, 73, "art. 4", "d6949", "OK",
    "2.Em relação aos direitos econômicos, sociais e culturais, cada Estado Parte se compromete a tomar medidas, tanto quanto permitirem os recursos disponíveis e, quando necessário, no âmbito da cooperação internacional, a fim de assegurar progressivamente o pleno exercício desses direitos")

add_item(17, 74, "art. 4", "d6949", "OK",
    "5.As disposições da presente Convenção se aplicam, sem limitação ou exceção, a todas as unidades constitutivas dos Estados federativos.")

add_item(18, 75, "art. 5", "d6949", "OK",
    "Artigo 5 Igualdade e não-discriminação 1.Os Estados Partes reconhecem que todas as pessoas são iguais perante e sob a lei e que fazem jus, sem qualquer discriminação, a igual proteção e igual benefício da lei.")

add_item(19, 78, "art. 6", "d6949", "OK",
    "Artigo 6 Mulheres com deficiência 1.Os Estados Partes reconhecem que as mulheres e meninas com deficiência estão sujeitas a múltiplas formas de discriminação")

add_item(20, 79, "art. 7", "d6949", "OK",
    "2.Em todas as ações relativas às crianças com deficiência, o superior interesse da criança receberá consideração primordial.")

add_item(21, 80, "art. 8", "d6949", "OK",
    "Artigo 8 Conscientização 1.Os Estados Partes se comprometem a adotar medidas imediatas, efetivas e apropriadas para: a) Conscientizar toda a sociedade, inclusive as famílias")

add_item(22, 81, "art. 9", "d6949", "OK",
    "Artigo 9 Acessibilidade 1.A fim de possibilitar às pessoas com deficiência viver de forma independente e participar plenamente de todos os aspectos da vida, os Estados Partes tomarão as medidas apropriadas para assegurar às pessoas com deficiência o acesso, em igualdade de oportunidades com as demais pessoas, ao meio físico, ao transporte, à informação e comunicação")

add_item(23, 83, "art. 10, art. 12", "d6949", "OK",
    "Artigo 10 Direito à vida Os Estados Partes reafirmam que todo ser humano tem o inerente direito à vida e tomarão todas as medidas necessárias para assegurar o efetivo exercício desse direito pelas pessoas com deficiência")

add_item(24, 85, "art. 12", "d6949", "OK",
    "2.Os Estados Partes reconhecerão que as pessoas com deficiência gozam de capacidade legal em igualdade de condições com as demais pessoas em todos os aspectos da vida.")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c02-s01-p1",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c02-s01-p1.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
