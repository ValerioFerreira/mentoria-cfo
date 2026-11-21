import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m04_c02-s01-p2/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_d6949 = (ROOT / "pipeline/.cache/leis-oficiais/leis/d6949.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_d6949 = norm(txt_d6949)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, url=None, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_check = norm(trecho_lei)[:120]
    if t_check not in norm_d6949:
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

add_item(0, 87, "art. 12, Lei nº 13.146/2015", "d6949", "OK",
    "Artigo 12 Reconhecimento igual perante a lei 1.Os Estados Partes reafirmam que as pessoas com deficiência têm o direito de ser reconhecidas em qualquer lugar como pessoas perante a lei.")

add_item(1, 94, "art. 10", "d6949", "OK",
    "Artigo 10 Direito à vida Os Estados Partes reafirmam que todo ser humano tem o inerente direito à vida e tomarão todas as medidas necessárias para assegurar o efetivo exercício desse direito pelas pessoas com deficiência")

add_item(2, 96, "art. 10, art. 11", "d6949", "OK",
    "Artigo 11 Situações de risco e emergências humanitárias Em conformidade com suas obrigações decorrentes do direito internacional, inclusive do direito humanitário internacional e do direito internacional dos direitos humanos, os Estados Partes tomarão todas")

add_item(3, 97, "art. 13", "d6949", "OK",
    "Artigo 13 Acesso à justiça 1.Os Estados Partes assegurarão o efetivo acesso das pessoas com deficiência à justiça, em igualdade de condições com as demais pessoas, inclusive mediante a provisão de adaptações processuais")

add_item(4, 98, "art. 14", "d6949", "OK",
    "Artigo 14 Liberdade e segurança da pessoa 1.Os Estados Partes assegurarão que as pessoas com deficiência, em igualdade de oportunidades com as demais pessoas: a) Gozem do direito à liberdade e à segurança da pessoa;")

add_item(5, 99, "art. 15", "d6949", "OK",
    "Artigo 15 Prevenção contra tortura ou tratamentos ou penas cruéis, desumanos ou degradantes 1.Nenhuma pessoa será submetida à tortura ou a tratamentos ou penas cruéis, desumanos ou degradantes.")

add_item(6, 100, "art. 19", "d6949", "OK",
    "Artigo 19 Vida independente e inclusão na comunidade Os Estados Partes desta Convenção reconhecem o igual direito de todas as pessoas com deficiência de viver na comunidade, com a mesma liberdade de escolha que as demais")

add_item(7, 101, "art. 23", "d6949", "OK",
    "Artigo 23 Respeito pelo lar e pela família 1.Os Estados Partes tomarão medidas efetivas e apropriadas para eliminar a discriminação contra pessoas com deficiência, em todos os aspectos relativos a casamento, família")

add_item(8, 102, "art. 24", "d6949", "OK",
    "Artigo 24 Educação 1.Os Estados Partes reconhecem o direito das pessoas com deficiência à educação. Para efetivar esse direito sem discriminação e com base na igualdade de oportunidades, os Estados Partes assegurarão")

add_item(9, 103, "art. 27", "d6949", "OK",
    "Artigo 27 Trabalho e emprego 1.Os Estados Partes reconhecem o direito das pessoas com deficiência ao trabalho, em igualdade de oportunidades com as demais pessoas.")

add_item(10, 104, "art. 29", "d6949", "OK",
    "Artigo 29 Participação na vida política e pública Os Estados Partes garantirão às pessoas com deficiência direitos políticos e oportunidade de exercê-los em condições de igualdade com as demais pessoas")

add_item(11, 106, "art. 33", "d6949", "OK",
    "Artigo 33 Implementação e monitoramento nacionais 1.Os Estados Partes, de acordo com seu sistema organizacional, designarão um ou mais de um ponto focal no âmbito do Governo para assuntos relacionados com a implementação")

add_item(12, 108, "art. 33", "d6949", "OK",
    "designarão um ou mais de um ponto focal no âmbito do Governo para assuntos relacionados com a implementação da presente Convenção")

add_item(13, 112, "art. 34", "d6949", "OK",
    "Artigo 34 Comitê sobre os Direitos das Pessoas com Deficiência 1.Um Comitê sobre os Direitos das Pessoas com Deficiência (doravante denominado \"Comitê\") será estabelecido, para desempenhar as funções aqui definidas.")

add_item(14, 114, "art. 34, art. 35", "d6949", "OK",
    "2.O Comitê será constituído, quando da entrada em vigor da presente Convenção, de 12 peritos. Quando a presente Convenção alcançar 60 ratificações ou adesões, o Comitê será acrescido em seis membros, perfazendo o total de 18 membros.")

add_item(15, 116, "art. 34", "d6949", "OK",
    "3.Os membros do Comitê atuarão a título pessoal e apresentarão elevada postura moral, competência e experiência reconhecidas no campo abrangido pela presente Convenção.")

add_item(16, 118, "art. 34", "d6949", "OK",
    "Quando a presente Convenção alcançar 60 ratificações ou adesões, o Comitê será acrescido em seis membros, perfazendo o total de 18 membros.")

add_item(17, 119, "art. 4, art. 34", "d6949", "OK",
    "4.Os membros do Comitê serão eleitos pelos Estados Partes, observando-se uma distribuição geográfica eqüitativa, representação de diferentes formas de civilização e dos principais sistemas jurídicos, representação equilibrada de gênero e participação de peritos com deficiência.")

add_item(18, 120, "art. 34", "d6949", "OK",
    "7.Os membros do Comitê serão eleitos para mandato de quatro anos, podendo ser candidatos à reeleição uma única vez.")

add_item(19, 121, "art. 35", "d6949", "OK",
    "Artigo 35 Relatórios dos Estados Partes 1.Cada Estado Parte, por intermédio do Secretário-Geral das Nações Unidas, submeterá relatório abrangente sobre as medidas adotadas em cumprimento de suas obrigações estabelecidas")

add_item(20, 122, "art. 39", "d6949", "OK",
    "Artigo 39 Relatório do Comitê A cada dois anos, o Comitê submeterá à Assembléia Geral e ao Conselho Econômico e Social um relatório de suas atividades e poderá fazer sugestões e recomendações gerais")

add_item(21, 127, "art. 1, art. 2, art. 3, art. 4", "d6949", "OK",
    "Dentro do período de seis meses, o Estado concernente submeterá ao Comitê explicações ou declarações por escrito, esclarecendo a matéria e a eventual solução adotada pelo referido Estado.")

add_item(22, 128, "art. 6, art. 8", "d6949", "OK",
    "Artigo 6 1.Se receber informação confiável indicando que um Estado Parte está cometendo violação grave ou sistemática de direitos estabelecidos na Convenção, o Comitê convidará o referido Estado Parte a colaborar com a verificação da informação")

add_item(23, 130, "art. 42", "d6949", "OK",
    "Artigo 42 Assinatura A presente Convenção será aberta à assinatura de todos os Estados e organizações de integração regional na sede das Nações Unidas em Nova York, a partir de 30 de março de 2007.")

add_item(24, 132, "art. 44", "d6949", "OK",
    "Artigo 44 Organizações de integração regional 1.\"Organização de integração regional\" será entendida como organização constituída por Estados soberanos de determinada região, à qual seus Estados membros tenham delegado")

out = {
    "unidade": "CENSO-direitos-humanos_m04_c02-s01-p2",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m04_c02-s01-p2.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
