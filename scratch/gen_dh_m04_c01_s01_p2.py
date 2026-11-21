import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c01-s01-p2/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_d4377 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d4377.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_d4377 = norm(txt_d4377)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_check = norm(trecho_lei)[:120]
    if t_check not in norm_d4377:
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

add_item(0, 74, "art. 4", "d4377", "OK",
    "2. A adoção pelos Estados-Partes de medidas especiais, inclusive as contidas na presente Convenção, destinadas a proteger a maternidade, não se considerará discriminatória.")

add_item(1, 76, "art. 5", "d4377", "OK",
    "a) Modificar os padrões sócio-culturais de conduta de homens e mulheres, com vistas a alcançar a eliminação dos preconceitos e práticas consuetudinárias")

add_item(2, 78, "art. 5", "d4377", "OK",
    "Garantir que a educação familiar inclua uma compreensão adequada da maternidade como função social")

add_item(3, 81, "art. 6", "d4377", "OK",
    "Artigo 6o Os Estados-Partes tomarão todas as medidas apropriadas, inclusive de caráter legislativo, para suprimir todas as formas de tráfico de mulheres e exploração da prostituição da mulher.")

add_item(4, 84, "art. 7", "d4377", "OK",
    "Artigo 7o Os Estados-Partes tomarão todas as medidas apropriadas para eliminar a discriminação contra a mulher na vida política e pública do país")

add_item(5, 86, "art. 7", "d4377", "OK",
    "a) Votar em todas as eleições e referenda públicos e ser elegível para todos os órgãos cujos membros sejam objeto de eleições públicas;")

add_item(6, 88, "art. 7", "d4377", "OK",
    "b) Participar na formulação de políticas governamentais e na execução destas, e ocupar cargos públicos e exercer todas as funções públicas em todos os planos governamentais; c) Participar em organizações e associações não-governamentais que se ocupem da vida pública e política do país.")

add_item(7, 89, "art. 8", "d4377", "OK",
    "Artigo 8o Os Estados-Partes tomarão todas as medidas apropriadas para garantir, à mulher, em igualdade de condições com o homem e sem discriminação alguma, a oportunidade de representar seu governo no plano internacional e de participar no trabalho das organizações internacionais.")

add_item(8, 90, "art. 9", "d4377", "OK",
    "Artigo 9o 1. Os Estados-Partes outorgarão às mulheres direitos iguais aos dos homens para adquirir, mudar ou conservar sua nacionalidade.")

add_item(9, 94, "art. 10", "d4377", "OK",
    "Artigo 10 Os Estados-Partes adotarão todas as medidas apropriadas para eliminar a discriminação contra a mulher, a fim de assegurar-lhe a igualdade de direitos com o homem na esfera da educação")

add_item(10, 96, "art. 10", "d4377", "OK",
    "f) A redução da taxa de abandono feminino dos estudos e a organização de programas para aquelas jovens e mulheres que tenham deixado os estudos prematuramente; g) As mesmas oportunidades para participar ativamente nos esportes e na educação física; h) Acesso a material informativo específico que contribua para assegurar a saúde e o bem-estar da família, incluída a informação e o assessoramento sobre planejamento da família.")

add_item(11, 97, "art. 11", "d4377", "OK",
    "Artigo 11 1. Os Estados-Partes adotarão todas as medidas apropriadas para eliminar a discriminação contra a mulher na esfera do emprego a fim de assegurar, em condições de igualdade entre homens e mulheres, os mesmos direitos, em particular: a) O direito ao trabalho como direito inalienável de todo ser humano;")

add_item(12, 98, "art. 11", "d4377", "OK",
    "b) O direito às mesmas oportunidades de emprego, inclusive a aplicação dos mesmos critérios de seleção em questões de emprego; c) O direito de escolher livremente profissão e emprego")

add_item(13, 99, "art. 12", "d4377", "OK",
    "Artigo 12 1. Os Estados-Partes adotarão todas as medidas apropriadas para eliminar a discriminação contra a mulher na esfera dos cuidados médicos a fim de assegurar, em condições de igualdade entre homens e mulheres, o acesso a serviços médicos")

add_item(14, 100, "art. 13", "d4377", "OK",
    "Artigo 13 Os Estados-Partes adotarão todas as medidas apropriadas para eliminar a discriminação contra a mulher em outras esferas da vida econômica e social a fim de assegurar, em condições de igualdade entre homens e mulheres, os mesmos direitos")

add_item(15, 101, "art. 14", "d4377", "OK",
    "Artigo 14 1. Os Estados-Partes levarão em consideração os problemas específicos enfrentados pela mulher rural e o importante papel que desempenha na subsistência econômica de sua família, incluído seu trabalho em setores não-monetários da economia")

add_item(16, 103, "art. 15", "d4377", "OK",
    "Artigo 15 1. Os Estados-Partes reconhecerão à mulher a igualdade com o homem perante a lei.")

add_item(17, 105, "art. 15", "d4377", "OK",
    "4. Os Estados-Partes concederão ao homem e à mulher os mesmos direitos no que respeita à legislação relativa ao direito das pessoas à liberdade de movimento e à liberdade de escolha de residência e domicílio.")

add_item(18, 109, "art. 16", "d4377", "OK",
    "Artigo 16 1. Os Estados-Partes adotarão todas as medidas adequadas para eliminar a discriminação contra a mulher em todos os assuntos relativos ao casamento")

add_item(19, 113, "art. 17", "d4377", "OK",
    "Artigo 17 1. Com o fim de examinar os progressos alcançados na aplicação desta Convenção, será estabelecido um Comitê sobre a Eliminação da Discriminação contra a Mulher")

add_item(20, 115, "art. 17", "d4377", "OK",
    "Os peritos serão eleitos pelos Estados-Partes entre seus nacionais e exercerão suas funções a título pessoal; será levada em conta uma repartição geográfica eqüitativa")

add_item(21, 117, "art. 17", "d4377", "OK",
    "composto, no momento da entrada em vigor da Convenção, de dezoito e, após sua ratificação ou adesão pelo trigésimo-quinto Estado-Parte, de vinte e três peritos de grande prestígio moral e competência na área abarcada pela Convenção.")

add_item(22, 119, "art. 17", "d4377", "OK",
    "5. Os membros do Comitê serão eleitos para um mandato de quatro anos. Entretanto, o mandato de nove dos membros eleitos na primeira eleição expirará ao fim de dois anos;")

add_item(23, 120, "art. 20", "d4377", "OK",
    "Artigo 20 1. O Comitê se reunirá normalmente todos os anos por um período não superior a duas semanas para examinar os relatórios que lhe sejam submetidos em conformidade com o Artigo 18 desta Convenção.")

add_item(24, 121, "art. 18", "d4377", "OK",
    "Artigo 18 1. Os Estados-Partes comprometem-se a submeter ao Secretário-Geral das Nações Unidas, para exame do Comitê, um relatório sobre as medidas legislativas, judiciárias, administrativas ou outras que adotarem para tornarem efetivas as disposições")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c01-s01-p2",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c01-s01-p2.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
