import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direitos-humanos_m02_a02-s02/unidade.json"
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
    
    if lei == "cf":
        t_clean = norm_cf
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

# Item 0 (linha 14)
# Os 21 primeiros artigos da Declaração reúnem os direitos de liberdade e as garantias... reproduziu quase todos eles no art. 5º...
add_item(
    0, 14, "art. 5", "cf", "OK",
    "Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade"
)

# Item 1 (linha 71)
# Em conjunto com os artigos 1º e 2º... mesma lista do caput do art. 5º da Constituição brasileira.
add_item(
    1, 71, "art. 5", "cf", "OK",
    "inviolabilidade do direito à vida, à liberdade, à igualdade, à segurança e à propriedade"
)

# Item 2 (linha 73)
# > [!lei] CF, art. 5º, caput
add_item(
    2, 73, "art. 5", "cf", "OK",
    "Todos são iguais perante a lei, sem distinção de qualquer natureza, garantindo-se aos brasileiros e aos estrangeiros residentes no País a inviolabilidade do direito à vida"
)

# Item 3 (linha 82)
# Costuma-se dizer que não existe direito fundamental absoluto... art. 5º, III...
add_item(
    3, 82, "art. 5", "cf", "OK",
    "III - ninguém será submetido a tortura nem a tratamento desumano ou degradante;"
)

# Item 4 (linha 105)
# A["Art. 8º<br/>recurso efetivo"] --> B["Art. 9º<br/>sem prisão arbitrária"]
add_item(
    4, 105, "art. 8, art. 9", "dudh", "OK",
    "todo ser humano tem direito a receber dos tribunais nacionais competentes remedio efetivo para os atos que violem os direitos fundamentais",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 5 (linha 106)
# B --> C["Art. 10<br/>igualdade, imparcialidade, publicidade"]
add_item(
    5, 106, "art. 10", "dudh", "OK",
    "todo ser humano tem direito em plena igualdade a uma justa e publica audiencia por parte de um tribunal independente e imparcial",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 6 (linha 107)
# C --> D["Art. 11<br/>inocência e irretroatividade"]
add_item(
    6, 107, "art. 11", "dudh", "OK",
    "todo ser humano acusado de um ato delituoso tem o direito de ser presumido inocente ate que a sua culpabilidade tenha sido provada",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 7 (linha 110)
# > [!lei] CF, art. 5º, LXI
add_item(
    7, 110, "art. 5", "cf", "OK",
    "ninguém será preso senão em flagrante delito ou por ordem escrita e fundamentada de autoridade judiciária competente, salvo nos casos de transgressão militar ou crime propriamente militar, definidos em lei;"
)

# Item 8 (linha 121)
# O artigo 11, 2... CF, art. 5º, XL...
add_item(
    8, 121, "art. 5", "cf", "OK",
    "XL - a lei penal não retroagirá, salvo para beneficiar o réu;"
)

# Item 9 (linha 126)
# | Retroatividade da lei benéfica | Não consta do texto | Admitida (art. 5º, XL) |
add_item(
    9, 126, "art. 5", "cf", "OK",
    "a lei penal não retroagirá, salvo para beneficiar o réu;"
)

# Item 10 (linha 151)
# A Constituição brasileira prevê a **concessão de asilo político**... (art. 4º, X).
add_item(
    10, 151, "art. 4", "cf", "OK",
    "X - concessão de asilo político."
)

# Item 11 (linha 160)
# Toda pessoa tem direito a uma nacionalidade... arts. 12 e 13 da Constituição.
add_item(
    11, 160, "art. 12", "cf", "OK",
    "São brasileiros: I - natos: a) os nascidos na República Federativa do Brasil, ainda que de pais estrangeiros, desde que estes não estejam a serviço de seu país;"
)

# Item 12 (linha 174)
# Na Constituição, aparecem nos incisos VI... e IX... do art. 5º.
add_item(
    12, 174, "art. 5", "cf", "OK",
    "VI - é inviolável a liberdade de consciência e de crença, sendo assegurado o livre exercício dos cultos religiosos e garantida, na forma da lei, a proteção aos locais de culto e a suas liturgias;"
)

# Item 13 (linha 178)
# O artigo 20 garante a reunião e a associação pacíficas... incisos XVI a XX do art. 5º.
add_item(
    13, 178, "art. 5", "cf", "OK",
    "XVI - todos podem reunir-se pacificamente, sem armas, em locais abertos ao público, independentemente de autorização, desde que não frustrem outra reunião anteriormente convocada para o mesmo local, sendo apenas exigido prévio aviso à autoridade competente;"
)

# Item 14 (linha 205)
# 3. As vedações da escravidão (art. 4º) e da tortura e do tratamento cruel, desumano ou degradante (art. 5º) são absolutas...
add_item(
    14, 205, "art. 4, art. 5", "dudh", "OK",
    "ninguem sera mantido em escravidao ou servidao a escravidao e o trafico de escravos serao proibidos em todas as suas formas",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

# Item 15 (linha 208)
# 6. A Constituição vai além da DUDH ao admitir a retroatividade da lei penal que beneficia o réu (art. 5º, XL).
add_item(
    15, 208, "art. 5", "cf", "OK",
    "a lei penal não retroagirá, salvo para beneficiar o réu;"
)

# Item 16 (linha 209)
# 7. O direito de asilo (art. 14) não se aplica à perseguição legítima por crime de direito comum nem a atos contrários aos propósitos e princípios da ONU.
add_item(
    16, 209, "art. 14", "dudh", "OK",
    "todo ser humano vitima de perseguicao tem o direito de procurar e de gozar asilo em outros paises",
    url="https://www.unicef.org/brazil/declaracao-universal-dos-direitos-humanos"
)

out = {
    "unidade": "CENSO-direitos-humanos_m02_a02-s02",
    "agente": "B",
    "materia": "direitos-humanos",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direitos-humanos_m02_a02-s02.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
