"""Reanálise do material do Estratégia contra o Anexo II do edital (2º Tenente).

Para cada item do edital há uma ou mais expressões regulares (sem acento, minúsculas). O script conta em quantas
páginas e em quantas aulas cada item aparece e classifica: COBERTO (>= 3 páginas), INCIDENTAL (1–2) ou AUSENTE (0).
Saída: pipeline/.cache/reports/edital_audit.md  (e resumo no stdout).
Uso: python pipeline/edital_audit.py [--subject legislacoes-pe]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import defaultdict

from config import CACHE_DIR, PAGES_DIR

COVERED_MIN = 3

# (item do edital, [regex...])  — regex aplicado em texto normalizado
ITEMS: dict[str, list[tuple[str, list[str]]]] = {
    "lingua-portuguesa": [
        ("Compreensão e interpretação de textos", [r"interpretacao de texto", r"compreensao de texto"]),
        ("Tipologias e gêneros textuais", [r"tipologia textual", r"generos textuais", r"tipos textuais"]),
        ("Figuras de linguagem", [r"figuras? de linguagem", r"\bmetafora\b", r"\bmetonimia\b", r"\bprosopopeia\b", r"\bhiperbole\b", r"\bantitese\b", r"\beufemismo\b"]),
        ("Relações semânticas entre orações (oposição, conclusão, concessão…)", [r"concessiv", r"conclusiv", r"adversativ"]),
        ("Ortografia oficial", [r"ortografia", r"acordo ortografico"]),
        ("Acentuação gráfica", [r"acentuacao grafica", r"\bparoxitona", r"\boxitona"]),
        ("Classes de palavras", [r"classes? de palavras", r"\bsubstantivo", r"\badjetivo", r"\badverbio"]),
        ("Crase", [r"\bcrase\b"]),
        ("Sintaxe da oração e do período", [r"sujeito simples", r"\bpredicado\b", r"periodo composto", r"coordenacao", r"subordinacao"]),
        ("Funções do “que” e do “se”", [r"funcoes? do que", r"funcoes? do se\b", r"\bque expletivo", r"\bse apassivador", r"particula de realce", r"indice de indeterminacao", r"pronome apassivador", r"conjuncao integrante"]),
        ("Mecanismos de coesão textual", [r"coesao textual", r"coesao referencial", r"elementos coesivos", r"\bcoesao\b"]),
        ("Pontuação", [r"sinais de pontuacao", r"\bvirgula\b"]),
        ("Concordância nominal e verbal", [r"concordancia verbal", r"concordancia nominal"]),
        ("Regência nominal e verbal", [r"regencia verbal", r"regencia nominal"]),
        ("Colocação pronominal", [r"colocacao pronominal", r"\bproclise", r"\benclise", r"\bmesoclise"]),
        ("Processos de formação de palavras", [r"formacao de palavras", r"processos? de formacao", r"\bderivacao", r"\bcomposicao por (justaposicao|aglutinacao)", r"\bparassintese", r"\bhibridismo", r"\bonomatopeia", r"\bprefixacao", r"\bsufixacao", r"\bderivacao regressiva"]),
        ("Significação das palavras", [r"significacao das palavras", r"\bsinonimia", r"\bantonimia", r"\bhomonimia", r"\bpolissemia", r"\bdenotacao", r"\bconotacao"]),
        ("Variação linguística", [r"variacao linguistica", r"variedades? linguistica"]),
    ],
    "lingua-inglesa": [
        ("Interpretação de gêneros textuais", [r"reading comprehension", r"interpretacao de texto", r"compreensao de texto"]),
        ("Vocabulário aplicado", [r"vocabulary", r"vocabulario", r"false cognates", r"falsos cognatos", r"cognates"]),
        ("Substantivos: plural; contável × incontável", [r"countable", r"uncountable", r"\bplural\b"]),
        ("Adjetivos: comparativo e superlativo", [r"comparative", r"superlative", r"comparativo"]),
        ("Advérbios", [r"\badverbs?\b", r"\badverbio"]),
        ("Preposições", [r"\bprepositions?\b", r"\bpreposicao"]),
        ("Artigos", [r"\barticles?\b", r"\ban\b.*\bthe\b"]),
        ("Pronomes (personal, object, possessive, reflexive…)", [r"reflexive pronouns?", r"possessive pronouns?", r"object pronouns?", r"personal pronouns?"]),
        ("Phrasal verbs", [r"phrasal verbs?"]),
        ("Present Simple / Continuous", [r"present simple", r"present continuous", r"simple present", r"present progressive"]),
        ("Present Perfect (simple e continuous)", [r"present perfect"]),
        ("Past Simple / Continuous / Perfect", [r"past simple", r"past continuous", r"past perfect", r"simple past"]),
        ("Futuros (simple, continuous, perfect)", [r"future perfect", r"future continuous", r"future simple", r"simple future", r"\bwill\b.*\bgoing to\b"]),
        ("Verbos modais", [r"modal verbs?", r"verbos? modais", r"\bhad better\b", r"\bmust\b.*\bhave to\b"]),
        ("Voz ativa e passiva", [r"passive voice", r"voz passiva", r"active voice"]),
        ("Orações adverbiais (time, place, reason, manner, contrast, purpose, result)", [r"adverbial clauses?", r"clauses? of (time|place|reason|manner|contrast|purpose|result)", r"oracoes adverbiais"]),
        ("Orações condicionais", [r"conditional", r"if clauses?", r"oracoes condicionais"]),
        ("Orações relativas", [r"relative clauses?", r"relative pronouns?", r"defining", r"oracoes relativas"]),
        ("Padrões verbais (to + inf; bare inf; gerund)", [r"gerund", r"bare infinitive", r"full infinitive", r"verb \+ (ing|gerund|infinitive)"]),
        ("Question tags", [r"question tags?", r"tag questions?"]),
    ],
    "direito-constitucional": [
        ("Constituição: conceito, classificação, histórico, elementos", [r"classificacao das constituicoes", r"elementos da constituicao", r"conceito de constituicao"]),
        ("Estrutura da constituição / hermenêutica", [r"estrutura da constituicao", r"preambulo", r"interpretacao constitucional"]),
        ("Poder constituinte", [r"poder constituinte"]),
        ("Eficácia e aplicabilidade das normas", [r"eficacia plena", r"aplicabilidade das normas", r"normas de eficacia"]),
        ("Controle de constitucionalidade", [r"controle de constitucionalidade", r"\badi\b", r"\badpf\b", r"\badc\b"]),
        ("Direitos e garantias fundamentais", [r"direitos e garantias fundamentais", r"direitos individuais", r"remedios? constitucionais?", r"habeas corpus", r"mandado de seguranca"]),
        ("Nacionalidade / direitos políticos / partidos", [r"nacionalidade", r"direitos politicos", r"partidos politicos"]),
        ("Organização do Estado e repartição de competências", [r"repartição de competencias|reparticao de competencias", r"organizacao politico-administrativa", r"intervencao federal"]),
        ("Administração pública e servidores (CF, arts. 37–41)", [r"art\. ?37", r"servidores publicos"]),
        ("Militares dos Estados (art. 42)", [r"militares dos estados", r"art\. ?42"]),
        ("Poderes Legislativo, Executivo e Judiciário", [r"poder legislativo", r"poder executivo", r"poder judiciario"]),
        ("Funções essenciais à Justiça", [r"funcoes essenciais a justica", r"ministerio publico", r"defensoria publica"]),
        ("Defesa do Estado e das instituições democráticas", [r"estado de defesa", r"estado de sitio", r"forcas armadas", r"seguranca publica"]),
        ("Ordem social", [r"ordem social", r"seguridade social", r"art\. ?19[4-9]"]),
        ("Constituição do Estado de Pernambuco", [r"constituicao (do estado )?de pernambuco", r"constituicao estadual de pernambuco", r"\bcepe\b"]),
        ("Súmulas e jurisprudência", [r"sumula vinculante", r"\bstf\b"]),
        ("ECA — Lei 8.069/1990", [r"8\.069", r"estatuto da crianca e do adolescente", r"\beca\b"]),
        ("Estatuto da Juventude — Lei 12.852/2013", [r"12\.852", r"estatuto da juventude"]),
        ("Lei Maria da Penha — Lei 11.340/2006", [r"11\.340", r"maria da penha"]),
    ],
    "direito-administrativo": [
        ("Estado, governo e administração pública", [r"administracao publica", r"elementos do estado"]),
        ("Princípios do Direito Administrativo", [r"principio da legalidade", r"principio da impessoalidade", r"supremacia do interesse"]),
        ("Organização administrativa", [r"descentralizacao", r"desconcentracao", r"administracao indireta"]),
        ("Agentes públicos: espécies e classificação; cargo, emprego e função", [r"agentes publicos", r"cargo, emprego e funcao|cargos, empregos e funcoes"]),
        # "agentes publicos", "provimento" e a mera citação da Lei 8.112 aparecem em toda aula; o RJU só conta com institutos próprios do estatuto
        ("Regime jurídico único (Lei 8.112/1990): provimento, vacância, remoção, redistribuição, substituição, vantagens, regime disciplinar", [r"redistribuicao", r"vacancia", r"readaptacao", r"reversao", r"sindicancia"]),
        ("Poderes administrativos / poder de polícia", [r"poder de policia", r"poder hierarquico", r"poder disciplinar", r"poder regulamentar", r"abuso de poder"]),
        ("Ato administrativo", [r"ato administrativo", r"atributos do ato", r"anulacao e revogacao"]),
        ("Serviços públicos e delegação", [r"servicos publicos", r"concessao", r"permissao"]),
        ("Controle e responsabilidade civil do Estado", [r"responsabilidade civil do estado", r"controle da administracao", r"controle judicial"]),
    ],
    "direito-penal-militar": [
        ("Aplicação da lei penal militar", [r"aplicacao da lei penal militar", r"lei penal militar no tempo", r"territorialidade"]),
        ("Crime", [r"conceito de crime", r"\bcrime militar\b", r"\btipicidade"]),
        ("Imputabilidade", [r"imputabilidade"]),
        ("Concurso de agentes", [r"concurso de agentes", r"coautoria"]),
        ("Penas", [r"penas principais", r"pena de reclusao", r"aplicacao da pena"]),
        ("Medidas de segurança", [r"medidas? de seguranca"]),
        ("Ação penal", [r"acao penal"]),
        ("Extinção da punibilidade", [r"extincao da punibilidade", r"prescricao"]),
        ("Crimes militares em tempo de paz", [r"tempo de paz", r"motim", r"revolta", r"desercao", r"insubordinacao"]),
        ("Crimes militares em tempo de guerra", [r"tempo de guerra", r"traicao", r"espionagem"]),
    ],
    "legislacoes-pe": [
        ("Lei 11.817/2000 — Código Disciplinar", [r"11\.817"]),
        ("Decreto 50.014/2020", [r"50\.014"]),
        ("Lei 6.783/1974 — Estatuto dos Militares", [r"6\.783"]),
        ("Lei 15.187/2013 — Organização Básica do CBMPE", [r"15\.187"]),
        ("Lei 14.751/2023 — Lei Orgânica Nacional", [r"14\.751"]),
    ],
    "quimica": [
        ("Estrutura da matéria: substâncias, misturas, separação", [r"metodos? de separacao", r"destilacao", r"decantacao"]),
        ("Átomos e moléculas / isótopos / Avogadro", [r"isotopos?", r"numero de avogadro", r"constante de avogadro"]),
        ("Classificação periódica", [r"tabela periodica", r"propriedades periodicas", r"eletronegatividade"]),
        ("Ligações químicas e forças intermoleculares", [r"ligacao ionica", r"ligacao covalente", r"forcas intermoleculares", r"ligacao metalica"]),
        ("Fórmulas, Lewis, Nox, nomenclatura", [r"estruturas? de lewis", r"numero de oxidacao", r"\bnox\b"]),
        ("Funções inorgânicas (óxidos, ácidos, bases, sais)", [r"oxidos?", r"arrhenius", r"bronsted"]),
        ("Estados da matéria / gases", [r"gas ideal", r"volume molar", r"equacao de clapeyron"]),
        ("Soluções e concentração", [r"concentracao comum", r"molaridade", r"diluicao", r"fracao molar"]),
        ("Radioatividade e estrutura nuclear", [r"radioatividade", r"meia-vida|meia vida", r"fissao nuclear", r"fusao nuclear"]),
        ("Reações e estequiometria", [r"estequiometria", r"balanceamento", r"rendimento da reacao"]),
        ("Termoquímica", [r"entalpia", r"termoquimica", r"energia de ligacao"]),
        ("Cinética química", [r"cinetica quimica", r"energia de ativacao", r"catalisador"]),
        ("Equilíbrio químico e iônico (pH, Kps, tampão)", [r"equilibrio quimico", r"le chatelier", r"produto de solubilidade", r"solucao tampao", r"\bph\b"]),
        ("Eletroquímica (pilhas, eletrólise, corrosão)", [r"eletrolise", r"pilha", r"corrosao", r"potencial de reducao"]),
        ("Química orgânica: funções, nomenclatura, isomeria", [r"hidrocarboneto", r"isomeria", r"nomenclatura iupac", r"funcoes organicas"]),
        ("Reações orgânicas", [r"reacoes organicas", r"adicao", r"substituicao", r"esterificacao"]),
        ("Petróleo e combustíveis", [r"petroleo", r"combustiveis?"]),
        ("Polímeros", [r"polimeros?", r"\bpvc\b", r"polietileno"]),
        ("Siderurgia", [r"siderurgia", r"ferro gusa", r"alto-forno|alto forno"]),
        ("Aspectos químicos do fogo e da combustão", [r"tetraedro do fogo", r"triangulo do fogo", r"combustao", r"ponto de fulgor"]),
        ("Produtos químicos perigosos / FDS", [r"fichas? de (dados de )?seguranca", r"\bfds\b", r"fispq", r"substancias inflamaveis", r"incompatibilidade"]),
        ("Água: propriedades e tratamento", [r"tratamento de agua", r"agua potavel", r"\bfloculacao", r"cloracao", r"propriedades da agua"]),
    ],
    "biologia": [
        ("Células: membrana, citoplasma, núcleo", [r"membrana plasmatica", r"citoplasma", r"nucleo celular"]),
        ("Divisão celular", [r"mitose", r"meiose"]),
        ("Metabolismo: fotossíntese e respiração", [r"fotossintese", r"respiracao celular"]),
        ("Código genético e síntese proteica", [r"sintese proteica", r"codigo genetico", r"transcricao"]),
        ("Tecidos animais e vegetais", [r"tecido epitelial", r"tecido conjuntivo", r"meristema"]),
        ("Células-tronco, clonagem, DNA recombinante, terapia gênica", [r"celulas?-tronco", r"clonagem", r"dna recombinante", r"terapia genica", r"transgenic"]),
        ("Biotecnologia: alimentos, fármacos; DNA forense, paternidade", [r"biotecnologia", r"paternidade", r"impressao digital de dna|dna fingerprint", r"pcr"]),
        ("Evolução e classificação dos seres vivos", [r"selecao natural", r"taxonomia", r"filogenia"]),
        ("Embriologia, anatomia e fisiologia humana", [r"embriologia", r"sistema circulatorio", r"sistema digestorio", r"sistema nervoso"]),
        ("Ecologia (cadeias, ciclos, populações, biomas)", [r"cadeia alimentar|teia alimentar", r"ciclos? biogeoquimicos?", r"biomas", r"sucessao ecologica"]),
        ("Problemas ambientais e legislação ambiental", [r"efeito estufa", r"desmatamento", r"unidades? de conservacao", r"microplasticos?"]),
        ("Saneamento básico", [r"saneamento"]),
        ("Qualidade de vida: doenças, IDH, Saúde Única", [r"\bidh\b|indice de desenvolvimento humano", r"saude unica", r"profilaxia"]),
        ("Primeiros socorros", [r"primeiros socorros"]),
        ("IST, drogas, obesidade, saúde mental", [r"\bist\b|infeccoes sexualmente", r"drogas", r"obesidade", r"saude mental"]),
    ],
    "fisica": [
        ("Grandezas, SI, vetores", [r"sistema internacional", r"notacao cientifica", r"grandezas vetoriais", r"ordem de grandeza"]),
        ("Cinemática", [r"movimento uniforme", r"movimento uniformemente", r"queda livre", r"lancamento"]),
        ("Dinâmica: leis de Newton, atrito, centrípeta", [r"leis de newton", r"forca de atrito", r"forca centripeta"]),
        ("Quantidade de movimento e impulso; centro de massa", [r"quantidade de movimento", r"impulso", r"centro de massa"]),
        ("Estática e torque", [r"torque|momento de uma forca", r"equilibrio estatico|estatica"]),
        ("Hidrostática", [r"empuxo", r"stevin", r"pascal", r"arquimedes"]),
        ("Energia, trabalho, potência", [r"energia cinetica", r"energia potencial", r"conservacao da energia", r"\btrabalho\b"]),
        ("Gravitação e Kepler", [r"gravitacao universal", r"leis de kepler"]),
        ("Eletrostática e eletrodinâmica", [r"lei de coulomb", r"campo eletrico", r"lei de ohm", r"capacitor", r"efeito joule"]),
        ("Magnetismo", [r"campo magnetico", r"imas?"]),
        ("Ondas e óptica", [r"reflexao", r"refracao", r"espelhos?", r"lentes?", r"ondas?"]),
        ("Termologia e termodinâmica", [r"calor especifico", r"dilatacao", r"ciclo de carnot", r"leis da termodinamica", r"gases ideais"]),
    ],
    "informatica": [
        ("Internet e intranet / navegadores / nuvem", [r"intranet", r"navegadores?", r"computacao em nuvem"]),
        ("Segurança da informação", [r"malware", r"phishing", r"criptografia", r"autenticacao"]),
        ("Backup e armazenamento", [r"\bbackup", r"tipos de backup"]),
        ("Arquivos e pastas", [r"pastas?", r"renomear|renomeacao"]),
        ("Organização de computadores / periféricos", [r"processador", r"memoria ram", r"perifericos?"]),
        ("Windows 11 / Prompt de comando", [r"windows 11", r"prompt de comando", r"painel de controle"]),
        ("Word / Writer", [r"\bword\b", r"\bwriter\b"]),
        ("Excel / Calc", [r"\bexcel\b", r"\bcalc\b"]),
        ("PowerPoint / Impress", [r"powerpoint", r"\bimpress\b"]),
    ],
    "matematica": [
        ("Conjuntos numéricos, divisibilidade, fatoração", [r"conjuntos numericos", r"divisibilidade", r"\bmdc\b|\bmmc\b"]),
        ("Razões, proporções, porcentagem, juros", [r"razao e proporcao|razoes e proporcoes", r"porcentagem", r"juros (simples|compostos)"]),
        ("Sequências e progressões", [r"progressao aritmetica", r"progressao geometrica"]),
        ("Contagem e probabilidade", [r"principio fundamental da contagem|principio multiplicativo", r"permutac", r"combinac", r"probabilidade"]),
        ("Geometria plana e espacial", [r"area do (triangulo|circulo)", r"volume", r"prisma|piramide|cilindro|cone|esfera"]),
        ("Semelhança, Tales, relações métricas, trigonometria", [r"teorema de tales", r"semelhanca de triangulos", r"relacoes metricas", r"trigonometria"]),
        ("Estatística básica e medidas de tendência", [r"media aritmetica", r"mediana", r"\bmoda\b", r"desvio padrao"]),
        ("Funções (1º, 2º grau, exponencial, log, trig.)", [r"funcao (afim|quadratica|exponencial|logaritmica)", r"funcoes trigonometricas"]),
        ("Geometria analítica / sistemas", [r"plano cartesiano", r"equacao da reta", r"sistemas? de equacoes"]),
    ],
    "estatistica": [
        ("População, censo, amostra", [r"populacao", r"\bcenso\b", r"amostra"]),
        ("Probabilidade (clássica, geométrica, axiomática)", [r"definicao classica", r"probabilidade geometrica", r"axiomas? de kolmogorov|definicao axiomatica"]),
        ("Variáveis aleatórias e distribuições", [r"variavel aleatoria", r"distribuicao binomial", r"distribuicao normal", r"funcao densidade"]),
        ("Descrição de dados, histograma, boxplot", [r"histograma", r"boxplot|box plot|caixa e bigodes", r"medidas de dispersao"]),
        ("Testes de hipóteses, t, F, ANOVA", [r"teste de hipoteses?", r"teste t\b|teste \"t\"", r"anova|analise da variancia"]),
        ("Regressão linear", [r"regressao linear", r"ajuste da reta|minimos quadrados"]),
    ],
    "lingua-espanhola": [
        ("Artigos e determinantes", [r"articulos?", r"posesivos", r"demostrativos"]),
        ("Substantivos e adjetivos (gênero, número, grau)", [r"sustantivos?", r"adjetivos?"]),
        ("Pronomes", [r"pronombres?"]),
        ("Verbos (regulares, irregulares, perífrases)", [r"verbos? irregulares", r"perifrasis", r"gerundio"]),
        ("Advérbios, preposições, conjunções", [r"adverbios?", r"preposiciones", r"conjunciones"]),
        ("Acentuação, sinônimos e antônimos", [r"acentuacion|tilde", r"sinonimos", r"antonimos"]),
        ("Heterogenéricos, heterossemânticos, heterotônicos, heterográficos", [r"heterogenericos?", r"heterosemanticos?", r"heterotonicos?|heteroprosodicos?", r"heterograficos?"]),
    ],
}


def norm(s: str) -> str:
    s = (s or "").replace("ﬁ", "fi").replace("ﬂ", "fl").replace("ﬀ", "ff").replace("ﬃ", "ffi")
    s = unicodedata.normalize("NFKD", s)
    return "".join(c for c in s if not unicodedata.combining(c)).lower()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--subject")
    args = ap.parse_args()

    by_subject: dict[str, list[tuple[str, int, str, str]]] = {}
    pages_by_subject: dict[str, list[tuple[str, int, str]]] = defaultdict(list)
    for f in sorted(PAGES_DIR.glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for p in d["pages"]:
            pages_by_subject[d["subject"]].append((d["aula"], p["n"], norm(p["text"])))

    out = ["# Reanálise do material × edital (2º Tenente CBMPE)\n"]
    for subject, items in ITEMS.items():
        if args.subject and subject != args.subject:
            continue
        pages = pages_by_subject.get(subject, [])
        out.append(f"\n## {subject} ({len(pages)} páginas)\n")
        out.append("| Item do edital | Págs. | Aulas | Situação |\n|---|---:|---|---|")
        for label, regexes in items:
            rx = [re.compile(r) for r in regexes]
            hit_pages = 0
            aulas: dict[str, int] = defaultdict(int)
            for aula, _n, text in pages:
                if any(r.search(text) for r in rx):
                    hit_pages += 1
                    aulas[aula.split("/")[-1]] += 1
            status = "COBERTO" if hit_pages >= COVERED_MIN else ("INCIDENTAL" if hit_pages else "AUSENTE")
            top = ", ".join(f"{a}:{n}" for a, n in sorted(aulas.items(), key=lambda kv: -kv[1])[:4])
            out.append(f"| {label} | {hit_pages} | {top} | {status} |")
    text = "\n".join(out)
    (CACHE_DIR / "reports").mkdir(exist_ok=True)
    (CACHE_DIR / "reports" / "edital_audit.md").write_text(text, encoding="utf-8")
    sys.stdout.buffer.write((text + "\n").encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
