import json
import re
from pathlib import Path
import sys

sys.path.insert(0, "material-pdf/_avaliacao/2026-11-11/ferramentas")
import validar_v3 as V

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c01-s01-p3/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")
txt_d4377 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d4377.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_cf = norm(txt_cf)
norm_d4377 = norm(txt_d4377)

url_4316 = "http://www.planalto.gov.br/ccivil_03/decreto/2002/d4316.htm"

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    if lei == "cf":
        t_clean = norm_cf
    elif lei == "d4377":
        t_clean = norm_d4377
    else:
        t_clean = None
    
    if t_clean is not None:
        t_check = norm(trecho_lei)[:120]
        if t_check not in t_clean:
            print(f"ERROR: item {idx} (linha {linha}): trecho_lei not in {lei}!")
            print("Trecho:", t_check)
    elif url:
        err = V.V.checar_trecho_url(url, trecho_lei)
        if err:
            print(f"ERROR URL item {idx} (linha {linha}): {err}")
    
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

add_item(0, 124, "art. 21", "d4377", "OK",
    "Artigo 21 1. O Comitê, através do Conselho Econômico e Social das Nações Unidas, informará anualmente a Assembléia Geral das Nações Unidas de suas atividades")

add_item(1, 128, "art. 18", "d4377", "OK",
    "Artigo 18 1. Os Estados-Partes comprometem-se a submeter ao Secretário-Geral das Nações Unidas, para exame do Comitê, um relatório sobre as medidas legislativas")

add_item(2, 130, "art. 1", "d4316", "OK",
    "para receber e considerar comunicaes apresentadas de acordo com o artigo 2 deste protocolo",
    url=url_4316)

add_item(3, 131, "art. 2", "d4316", "OK",
    "artigo 2 as comunicaes podem ser apresentadas por indivduos ou grupos de indivduos",
    url=url_4316)

add_item(4, 132, "art. 3", "d4316", "OK",
    "artigo 3 as comunicaes devero ser feitas por escrito e no podero ser annimas",
    url=url_4316)

add_item(5, 133, "art. 5", "d4316", "OK",
    "solicitao no sentido de que o estado parte tome as medidas antecipatrias necessrias",
    url=url_4316)

add_item(6, 134, "art. 6, art. 7", "d4316", "OK",
    "2 dentro de seis meses o estado parte que receber a comunicao apresentar ao comit explicaes ou declaraes por escrito",
    url=url_4316)

add_item(7, 136, "art. 8", "d4316", "OK",
    "artigo 8 1 caso o comit receba informao fidedigna indicando graves ou sistemticas violaes",
    url=url_4316)

add_item(8, 137, "art. 8", "d4316", "OK",
    "convidar o estado parte a cooperar no exame da informao e para esse fim a apresentar observaes",
    url=url_4316)

add_item(9, 139, "art. 8", "d4316", "OK",
    "4 o estado parte em questo dever dentro de seis meses do recebimento dos resultados comentrios e recomendaes do comit apresentar suas observaes",
    url=url_4316)

add_item(10, 140, "art. 8, art. 10, art. 17", "d4316", "OK",
    "declarar que no reconhece a competncia do comit disposta nos artigos 8 e 9 deste protocolo",
    url=url_4316)

add_item(11, 142, "art. 29", "d4377", "OK",
    "1. Qualquer controvérsia entre dois ou mais Estados-Partes relativa à interpretação ou aplicação desta Convenção e que não for resolvida por negociações será, a pedido de qualquer das Partes na controvérsia, submetida a arbitragem.")

add_item(12, 144, "art. 29", "d4377", "OK",
    "Se no prazo de seis meses a partir da data do pedido de arbitragem as Partes não acordarem sobre a forma da arbitragem, qualquer das Partes poderá submeter a controvérsia à Corte Internacional de Justiça")

add_item(13, 149, "art. 1, art. 17", "d4377", "OK",
    "Com o fim de examinar os progressos alcançados na aplicação desta Convenção, será estabelecido um Comitê sobre a Eliminação da Discriminação contra a Mulher")

add_item(14, 152, "art. 4", "d4377", "OK",
    "Artigo 4o 1. A adoção pelos Estados-Partes de medidas especiais de caráter temporário destinadas a acelerar a igualdade de fato entre o homem e a mulher não se considerará discriminação")

add_item(15, 155, "EC 45", "cf", "OK",
    "Os tratados e convenções internacionais sobre direitos humanos que forem aprovados, em cada Casa do Congresso Nacional, em dois turnos, por três quintos dos votos dos respectivos membros, serão equivalentes às emendas constitucionais.")

add_item(16, 161, "art. 10", "d4316", "OK",
    "artigo 10 1 cada estado parte poder no momento da assinatura ou ratificao do presente protocolo",
    url=url_4316)

add_item(17, 164, "art. 1", "d4377", "OK",
    "Para os fins da presente Convenção, a expressão \"discriminação contra a mulher\" significará toda a distinção, exclusão ou restrição baseada no sexo e que tenha por objeto ou resultado prejudicar ou anular o reconhecimento")

add_item(18, 171, "art. 1", "d4377", "OK",
    "significará toda a distinção, exclusão ou restrição baseada no sexo e que tenha por objeto ou resultado prejudicar ou anular o reconhecimento, gozo ou exercício pela mulher, independentemente de seu estado civil")

add_item(19, 172, "art. 4", "d4377", "OK",
    "2. A adoção pelos Estados-Partes de medidas especiais, inclusive as contidas na presente Convenção, destinadas a proteger a maternidade, não se considerará discriminatória.")

add_item(20, 180, "art. 1", "d4377", "OK",
    "toda a distinção, exclusão ou restrição baseada no sexo e que tenha por objeto ou resultado prejudicar ou anular o reconhecimento")

add_item(21, 182, "art. 4", "d4377", "OK",
    "essas medidas cessarão quando os objetivos de igualdade de oportunidade e tratamento houverem sido alcançados.")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c01-s01-p3",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c01-s01-p3.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
