import json
import re
from pathlib import Path

ROOT = Path(".")
u_path = ROOT / "material-pdf/_avaliacao/2026-11-11/unidades/CENSO-direito-administrativo_m23_a24-s09-p1/unidade.json"
u = json.loads(u_path.read_text(encoding="utf-8"))

md_path = ROOT / u["md"]
md_lines = md_path.read_text(encoding="utf-8").splitlines()

txt_l8429 = (ROOT / "pipeline/.cache/leis-oficiais/leis/l8429.clean.txt").read_text(encoding="utf-8")
txt_cf = (ROOT / "pipeline/.cache/leis-oficiais/leis/cf.clean.txt").read_text(encoding="utf-8")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

norm_l8429 = norm(txt_l8429)
norm_cf = norm(txt_cf)

censo = []

def add_item(idx, linha, citacao, lei, resultado, trecho_lei, frase_capitulo=None, severidade=None, diferenca=None, texto_novo=None):
    raw_line = md_lines[linha - 1]
    if frase_capitulo is None:
        frase_capitulo = raw_line.strip()
    
    t_clean = norm_cf if lei == "cf" else norm_l8429
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

# Item 0 (linha 14)
# A segurança jurídica exige limites temporais...
add_item(
    0, 14, "Lei nº 14.230/2021, Lei nº 8.429/1992", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 1 (linha 17)
# > - Dominar a disciplina da prescrição geral de oito anos...
add_item(
    1, 17, "art. 23", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato"
)

# Item 2 (linha 18)
# > - Compreender os cinco marcos interruptivos do art. 23, § 4º...
add_item(
    2, 18, "art. 23", "l8429", "OK",
    "O prazo da prescrição referido no caput deste artigo interrompe-se:"
)

# Item 3 (linha 20)
# > - Examinar as regras de solidariedade no ressarcimento...
add_item(
    3, 20, "art. 17, Lei nº 8.429/1992, Súmula 634", "l8429", "OK",
    "Na hipótese de litisconsórcio passivo, a condenação ocorrerá no limite da participação e dos benefícios diretos, vedada qualquer solidariedade na fixação das multas civis."
)

# Item 4 (linha 25)
# Na vigência da redação original da Lei nº 8.429/1992...
add_item(
    4, 25, "Lei nº 8.429/1992", "l8429", "OK",
    "I - até cinco anos após o término do exercício de mandato, de cargo em comissão ou de função de confiança;"
)

# Item 5 (linha 27)
# A Lei nº 14.230/2021 unificou a matéria de forma categórica no art. 23, caput:
add_item(
    5, 27, "art. 23, Lei nº 14.230/2021", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 6 (linha 29)
# > [!lei] Art. 23, caput, da Lei nº 8.429/1992
add_item(
    6, 29, "art. 23, Lei nº 8.429/1992", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 7 (linha 44)
# C -- Sim --> D["Suspensão do Prazo por até 180 Dias Corridos (art. 23, § 1º)"]
add_item(
    7, 44, "art. 23", "l8429", "OK",
    "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos referidos nesta Lei suspende o curso do prazo prescricional por, no máximo, 180 (cento e oitenta) dias corridos,"
)

# Item 8 (linha 55)
# > [!lei] Art. 23, § 1º, da Lei nº 8.429/1992
add_item(
    8, 55, "art. 23, Lei nº 8.429/1992", "l8429", "OK",
    "A instauração de inquérito civil ou de processo administrativo para apuração dos ilícitos referidos nesta Lei suspende o curso do prazo prescricional por, no máximo, 180 (cento e oitenta) dias corridos, recomeçando a correr após a sua conclusão ou, caso não concluído o processo, esgotado o prazo de suspensão."
)

# Item 9 (linha 63)
# É essencial distinguir a causa suspensiva da prescrição...
add_item(
    9, 63, "art. 23", "l8429", "OK",
    "O inquérito civil para apuração do ato de improbidade será concluído no prazo de 365 (trezentos e sessenta e cinco) dias corridos, prorrogável uma única vez por igual período, mediante ato fundamentado submetido à revisão da instância competente do órgão ministerial, conforme dispuser a respectiva lei orgânica."
)

# Item 10 (linha 67)
# A inovação processual mais debatida da Lei nº 14.230/2021...
add_item(
    10, 67, "art. 23, Lei nº 14.230/2021", "l8429", "OK",
    "O prazo da prescrição referido no caput deste artigo interrompe-se:"
)

# Item 11 (linha 71)
# A interrupção zera a contagem do prazo prescricional. O art. 23, § 4º...
add_item(
    11, 71, "art. 23", "l8429", "OK",
    "I - pelo ajuizamento da ação de improbidade administrativa;"
)

# Item 12 (linha 73)
# > [!lei] Art. 23, § 4º, da Lei nº 8.429/1992
add_item(
    12, 73, "art. 23, Lei nº 8.429/1992", "l8429", "OK",
    "III - pela publicação de decisão ou acórdão de Tribunal de Justiça ou Tribunal Regional Federal que confirma sentença condenatória ou que reforma sentença de improcedência;"
)

# Item 13 (linha 92)
# > Pronunciamentos judiciais de **improcedência**...
add_item(
    13, 92, "art. 23", "l8429", "OK",
    "IV - pela publicação de decisão ou acórdão do Superior Tribunal de Justiça que confirma acórdão condenatório ou que reforma acórdão de improcedência;"
)

# Item 14 (linha 96)
# A redação original do art. 23, § 5º, dada pela Lei nº 14.230/2021...
add_item(
    14, 96, "art. 23, Lei nº 14.230/2021", "l8429", "OK",
    "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput deste artigo."
)

# Item 15 (linha 98)
# Contudo, ao julgar em definitivo o mérito das **ADIs 7156 e 7236**...
add_item(
    15, 98, "art. 23", "l8429", "OK",
    "pela metade do prazo previsto no caput deste artigo."
)

# Item 16 (linha 101)
# - Além disso, o STF ratificou o **teto total de 20 (vinte) anos**...
add_item(
    16, 101, "art. 23", "l8429", "OK",
    "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput deste artigo."
)

# Item 17 (linha 113)
# I --> J["Trânsito em Julgado (Teto Global Máximo de 20 Anos pelo art. 23, § 5º)"]
add_item(
    17, 113, "art. 23", "l8429", "OK",
    "Interrompida a prescrição, o prazo recomeça a correr do dia da interrupção, pela metade do prazo previsto no caput deste artigo."
)

# Item 18 (linha 116)
# ## O julgamento do Tema 1.199 do Supremo Tribunal Federal
add_item(
    18, 116, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 19 (linha 118)
# A entrada em vigor da Lei nº 14.230/2021...
add_item(
    19, 118, "art. 10, Lei nº 14.230/2021", "l8429", "OK",
    "Constitui ato de improbidade administrativa que causa lesão ao erário qualquer ação ou omissão dolosa, que enseje, efetiva e comprovadamente, perda patrimonial, desvio, apropriação, malbaratamento ou dilapidação dos bens ou haveres das entidades referidas no art. 1º desta Lei"
)

# Item 20 (linha 120)
# Para pacificar em definitivo a matéria...
add_item(
    20, 120, "Tema 1199", "cf", "OK",
    "Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

# Item 21 (linha 122)
# > [!jurisprudencia] STF, Tema 1.199 da Repercussão Geral (ARE 843.989)
add_item(
    21, 122, "Tema 1199", "cf", "OK",
    "São crimes de responsabilidade os atos do Presidente da República que atentem contra a Constituição Federal e, especialmente, contra: V - a probidade na administração;"
)

# Item 22 (linha 123)
# > 1. A configuração dos atos de improbidade dos arts. 9º, 10 e 11...
add_item(
    22, 123, "art. 9, art. 10", "l8429", "OK",
    "Consideram-se atos de improbidade administrativa as condutas dolosas tipificadas nos arts. 9º, 10 e 11 desta Lei, ressalvados os tipos previstos em leis especiais."
)

# Item 23 (linha 125)
# > 3. O novo regime prescricional instituído pela Lei nº 14.230/2021...
add_item(
    23, 125, "Lei nº 14.230/2021", "l8429", "OK",
    "A ação para a aplicação das sanções previstas nesta Lei prescreve em 8 (oito) anos, contados a partir da ocorrência do fato ou, no caso de infrações permanentes, do dia em que cessou a permanência."
)

# Item 24 (linha 128)
# A tabela a seguir sistematiza a aplicação prática das diretrizes do Tema 1.199:
add_item(
    24, 128, "Tema 1199", "cf", "OK",
    "§ 4º Os atos de improbidade administrativa importarão a suspensão dos direitos políticos, a perda da função pública, a indisponibilidade dos bens e o ressarcimento ao erário, na forma e gradação previstas em lei, sem prejuízo da ação penal cabível."
)

out = {
    "unidade": "CENSO-direito-administrativo_m23_a24-s09-p1",
    "agente": "B",
    "materia": "direito-administrativo",
    "censo": censo
}

out_path = ROOT / "material-pdf/_avaliacao/2026-11-11/rascunho/CENSO-direito-administrativo_m23_a24-s09-p1.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Draft saved with {len(censo)} records.")
