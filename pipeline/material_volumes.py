"""Divisão do material próprio MentorIA em volumes (Aulas MentorIA) e capítulos.

Cada trecho do catálogo (`<disc>/aNN/sNN`, = 1 atividade de Teoria) vira 1 capítulo; cada volume agrupa 2 a 8 capítulos em
sequência didática e vira 1 PDF. Esta tabela (DIVISAO) é a fonte única da divisão; o script grava
`content/material/volumes/<disciplina>.json` e acusa trechos do edital que ficaram sem volume.

Referências: "a05" = todos os trechos da aula a05; "a05[1-7]" = do 1º ao 7º trecho da aula (ordem do catálogo).
Trechos que não aparecem em nenhum concurso (importance.appears = false em todos) são descartados e listados em `foraDoEdital`.

Uso:  python pipeline/material_volumes.py            (grava e mostra o resumo)
      python pipeline/material_volumes.py --check    (só confere; código 1 se houver trecho do edital sem volume)
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MATERIAL_DIR = CONTENT_DIR / "material"
# Ordem de produção definida pelo dono (28/10/2026): a onda de um trecho é o primeiro concurso desta lista que o cobra.
WAVES = [
    ("CBMPE_CFOA", "2º Tenente CFOA (CBMPE)"),
    ("CBMPE_OFICIAL", "CFO BM (Oficial CBMPE)"),
    ("PCPE_AGENTE", "Agente PCPE"),
    ("PMPE_OFICIAL", "CFO PM (Oficial PMPE)"),
    ("CBMPE_SOLDADO", "CFHP BM (Soldado CBMPE)"),
    ("PMPE_SOLDADO", "CFHP PM (Soldado PMPE)"),
]

DIVISAO: dict[str, list[tuple[str, str]]] = {
    "lingua-portuguesa": [
        ("Nivelamento em Língua Portuguesa", "a00"),
        ("Ortografia oficial e acentuação gráfica", "a01"),
        ("Classes de palavras variáveis e formação de palavras", "a02 c02"),
        ("Verbos", "a04"),
        ("Preposição e conjunção", "a03"),
        ("Sintaxe da oração e do período", "a05"),
        ("Pontuação", "a06"),
        ("Concordância nominal e verbal", "a07"),
        ("Regência nominal e verbal e crase", "a08"),
        ("Coesão, significação das palavras e figuras de linguagem", "a09 a10 c01"),
        ("Interpretação de textos, tipologia, gêneros e variação linguística", "a11 a12"),
        ("Redação oficial", "a13"),
    ],
    "raciocinio-logico": [
        ("Estruturas lógicas", "a00 a01"),
        ("Equivalências, negações e diagramas lógicos", "a02 a03"),
        ("Lógica de argumentação", "a04"),
        ("Raciocínio crítico", "a05"),
        ("Análise combinatória", "a06"),
        ("Probabilidade", "a07"),
        ("Conjuntos, matrizes e determinantes", "c01 c02"),
    ],
    "direito-administrativo": [
        ("Noções iniciais e Administração Pública", "a01"),
        ("Princípios da Administração Pública", "a00"),
        ("Organização administrativa I", "a02"),
        ("Organização administrativa II", "a03"),
        ("Poderes administrativos", "a04"),
        ("Atos administrativos I", "a05[1-7]"),
        ("Atos administrativos II", "a05[8-13]"),
        ("Serviços públicos e intervenção do Estado", "a06 c04"),
        ("Controle da Administração Pública", "a07"),
        ("Responsabilidade civil do Estado", "a08"),
        ("Agentes públicos I", "a09[1-6]"),
        ("Agentes públicos II", "a09[7-11]"),
        ("Agentes públicos III", "a09[12-16]"),
        ("Lei 8.112/1990, processo administrativo e conselhos de disciplina", "c01 a23 c02 c03"),
        ("Licitações I", "a20[1-5]"),
        ("Licitações II", "a20[6-9]"),
        ("Licitações III", "a21[1-6]"),
        ("Licitações IV", "a21[7-12]"),
        ("Contratos administrativos I", "a22[1-5]"),
        ("Contratos administrativos II", "a22[6-10]"),
        ("Contratos administrativos III", "a22[11-14]"),
        ("Improbidade administrativa I", "a24[1-5]"),
        ("Improbidade administrativa II", "a24[6-9]"),
    ],
    "direito-constitucional": [
        ("Teoria da Constituição e princípios fundamentais", "a00 c06"),
        ("Direitos fundamentais I: teoria geral e art. 5º, I a XXXI", "a01 a02"),
        ("Direitos fundamentais II: art. 5º, XXXII a LXXIX, e remédios constitucionais", "a03"),
        ("Direitos sociais, nacionalidade, direitos políticos e partidos", "a04 a05 a06 a07"),
        ("Organização do Estado I", "a08[1-5]"),
        ("Organização do Estado II", "a08[6-9]"),
        ("Administração pública e servidores na Constituição", "a09"),
        ("Poder Legislativo", "a10"),
        ("Processo legislativo e Poder Executivo", "a11 a12"),
        ("Poder Judiciário I", "a13[1-5]"),
        ("Poder Judiciário II", "a13[6-10]"),
        ("Funções essenciais à Justiça e defesa do Estado", "a14 a15"),
        ("Ordem social", "a16"),
        ("Proteção especial: ECA, Estatuto da Juventude e Lei Maria da Penha", "c01 c02 c03"),
        ("Controle de constitucionalidade I", "a17[1-4]"),
        ("Controle de constitucionalidade II e direito intertemporal", "a17[5-8] c05"),
        ("Constituição do Estado de Pernambuco", "a18 c04"),
    ],
    "direito-penal-militar": [
        ("Aplicação da lei penal militar", "a00"),
        ("Crime militar, imputabilidade e concurso de agentes", "a01 a02 a03"),
        ("Penas, medidas de segurança, ação penal e extinção da punibilidade", "a04 a05 a06 a07"),
        ("Crimes militares em tempo de paz I", "a08"),
        ("Crimes militares em tempo de paz II", "a09"),
        ("Crimes militares em tempo de paz III e em tempo de guerra", "a10 a11"),
        ("Súmulas, parte especial complementar e crimes em licitações", "c01 c02"),
        ("Abuso de autoridade e crimes de preconceito", "a20 a21"),
    ],
    "direito-processual-penal-militar": [
        ("Lei processual penal militar, polícia judiciária militar e IPM", "a00 a01 a02"),
        ("Competência, prerrogativas, menagem e liberdade provisória", "a06 c01"),
        ("Incidentes e providências sobre coisas", "a07 a08"),
        ("Atos probatórios, deserção e processos especiais", "a10 a12"),
    ],
    "direitos-humanos": [
        ("Teoria geral e afirmação histórica dos direitos humanos", "a00 a01"),
        ("Declaração Universal dos Direitos Humanos", "a02"),
        ("Programas nacionais e direitos humanos na Constituição", "a04 a05"),
        ("Tratados: CEDAW e Convenção sobre os Direitos das Pessoas com Deficiência", "c01 c02"),
    ],
    "administracao": [
        ("Fundamentos da administração e diagnóstico organizacional", "a00 a03"),
        ("Teorias da administração", "a01"),
        ("Função organização e estrutura organizacional", "a04"),
        ("Direção e liderança", "a05"),
        ("Controle e processo decisório", "a07 c01"),
        ("Cultura e mudança organizacional", "a08"),
    ],
    "legislacoes-pe": [
        ("Estatuto dos Militares de Pernambuco", "a02 c05"),
        ("Código Disciplinar dos Militares de Pernambuco", "a01 c04"),
        ("Ética, assédio moral e sexual e acesso à informação", "c06 c09 c08"),
        ("Promoção, sindicância e investigação preliminar", "c07 c10 c11"),
        ("Decreto 50.014/2020 e Leis 15.187/2013 e 14.751/2023", "c01 c02 c03"),
    ],
    "informatica": [
        ("Internet, intranet e navegadores", "a00 a01 c01"),
        ("Segurança da informação: conceitos básicos", "a02"),
        ("Malwares", "a03"),
        ("Mecanismos de segurança e backup", "a04 a05"),
        ("Microsoft Excel I", "a06[1-6]"),
        ("Microsoft Excel II", "a06[7-12]"),
        ("LibreOffice Calc", "a07"),
        ("Microsoft Word", "a08"),
        ("LibreOffice Writer", "a09"),
        ("Apresentações: PowerPoint e Impress", "a10 a11"),
        ("Windows 11 I", "a12[1-8]"),
        ("Windows 11 II", "a12[9-15]"),
        ("Computação em nuvem", "a13"),
        ("Hardware I", "a14[1-5]"),
        ("Hardware II", "a14[6-10]"),
    ],
    "estatistica": [
        ("Apresentação de dados", "a00"),
        ("Médias e moda", "a01 a03"),
        ("Medidas separatrizes", "a02"),
        ("Medidas de dispersão, assimetria e curtose", "a04 c02"),
        ("Análise combinatória", "a05"),
        ("Probabilidade e amostragem", "a06 c01"),
        ("Variáveis aleatórias discretas", "a07"),
        ("Distribuições discretas de probabilidade", "a08"),
        ("Variáveis aleatórias contínuas", "a09"),
        ("Distribuições contínuas de probabilidade", "a10"),
        ("Testes de hipóteses", "a11"),
        ("Regressão linear simples e múltipla", "a12 a13"),
        ("Análise de variância (ANOVA)", "a14"),
    ],
    "matematica": [
        ("Conjuntos numéricos e operações fundamentais", "a00 a01"),
        ("Unidades de medida, frações, razão e proporção", "a02 a03"),
        ("Regra de três, porcentagem e divisão proporcional", "a04 a05 c03"),
        ("Juros simples e compostos", "a06 a07"),
        ("Equações e inequações", "a08"),
        ("Funções e função afim", "a09 a10"),
        ("Função quadrática", "a11"),
        ("Funções exponencial e logarítmica", "a12 a13"),
        ("Progressões e complementos do edital", "a14 c02"),
        ("Geometria plana", "a15"),
        ("Geometria espacial e analítica", "a16 c01"),
        ("Trigonometria I", "a17[1-6]"),
        ("Trigonometria II", "a17[7-12]"),
    ],
    "fisica": [
        ("Cinemática escalar: grandezas, MU e MUV", "a00 a01 a02"),
        ("Queda livre, lançamentos e movimento circular", "a03 a04"),
        ("Leis de Newton, trabalho e energia", "a05 a06"),
        ("Impulso, quantidade de movimento, estática e gravitação", "a07 a08 a09"),
        ("Hidrostática e termologia", "a10 a11 a12"),
        ("Ondas e óptica geométrica", "a13 c01"),
        ("Eletricidade, magnetismo e tópicos do edital", "a14 a15 a16 a17 c02"),
    ],
    "quimica": [
        ("Introdução à química: matéria, substâncias e transformações", "a00"),
        ("Atomística, distribuição eletrônica e tabela periódica", "a01 a02"),
        ("Ligações químicas, estados físicos e propriedades dos materiais", "a04 a05"),
        ("Reações: balanceamento, NOX, ácidos e bases", "a03 a06"),
        ("Estequiometria e separação de misturas", "a07 a08"),
        ("Soluções: dispersões, preparo e padronização", "a09 a10"),
        ("Equilíbrio, titulação, termoquímica e cinética", "a11 a12 a13"),
        ("Eletroquímica e radioatividade", "a14 a15"),
        ("Química orgânica I: carbono e hidrocarbonetos", "a16 a17"),
        ("Química orgânica II: funções orgânicas e isomeria", "a18 a19"),
        ("Química orgânica III: propriedades e reações de adição e eliminação", "a20 a21"),
        ("Química orgânica IV: substituição, oxirredução e reações específicas", "a22"),
        ("Química aplicada: petroquímica, fogo, polímeros, siderurgia e água", "a23 c01"),
    ],
    "biologia": [
        ("Citologia", "a00"),
        ("Histologia e embriologia", "a01 a12"),
        ("Genética e biologia molecular", "a02 a03"),
        ("Evolução e biotecnologia", "a04 c02"),
        ("Corpo humano I: sistemas tegumentar e esquelético", "a05 a06"),
        ("Corpo humano II: músculos, articulações e sistema nervoso", "a07 a10"),
        ("Corpo humano III: sistema cardiovascular", "a08"),
        ("Corpo humano IV: sistemas digestório, endócrino e imunitário", "a09 a11"),
        ("Ecologia", "a13"),
        ("Ecologia da conservação e qualidade de vida", "a14 c01"),
        ("Saúde, higiene e parasitologia", "a15"),
        ("Primeiros socorros", "a16 a17"),
    ],
    "lingua-inglesa": [
        ("Leitura em inglês: cognatos, phrasal verbs e idioms", "a00 a03 a06"),
        ("Substantivos, artigos, pronomes e preposições", "a01"),
        ("Adjetivos, advérbios, afixos e estruturas complementares", "a02 c01"),
        ("Tempos verbais", "a04 a05"),
    ],
    "lingua-espanhola": [
        ("Leitura em espanhol: alfabeto, pontuação e acentuação", "a00 a11 a12"),
        ("Vocabulário: silabeo, sinonímia, heterosemánticos e heterográficos", "a13 c01"),
        ("Artigos, contrações, preposições e conjunções", "a01 a03 a02 a04"),
        ("Substantivos e adjetivos", "a06 a07"),
        ("Pronomes, advérbios e números", "a05 a08 a10"),
        ("Verbos", "a09"),
    ],
    "direito-penal": [
        ("Princípios e aplicação da lei penal", "a00 a01"),
        ("Teoria do crime I", "a02[1-5]"),
        ("Teoria do crime II", "a02[6-8] a03"),
        ("Crimes contra a pessoa I", "a04[1-5]"),
        ("Crimes contra a pessoa II", "a04[6-10]"),
        ("Crimes contra a pessoa III", "a04[11-14]"),
        ("Crimes contra o patrimônio I", "a05[1-5]"),
        ("Crimes contra o patrimônio II", "a05[6-10]"),
        ("Crimes contra o patrimônio III", "a05[11-14]"),
        ("Crimes contra a dignidade sexual I", "a06[1-4]"),
        ("Crimes contra a dignidade sexual II", "a06[5-8]"),
        ("Crimes contra a administração pública I", "a07 a08[1-2]"),
        ("Crimes contra a administração pública II", "a08[3-5] a09[1-2]"),
        ("Crimes contra a administração pública III", "a09[3-5] a10"),
    ],
    "legislacao-penal-especial": [
        ("Crimes hediondos, tortura e crimes de preconceito", "a11 a14 a12"),
        ("Abuso de autoridade e organizações criminosas", "a13 a15"),
        ("Crimes de trânsito e Estatuto do Desarmamento", "a16 a21"),
        ("Violência doméstica e familiar e ECA (crimes)", "a17 a19 c01"),
        ("Lei de Drogas", "a18"),
        ("Crimes ambientais", "a20"),
    ],
    "direito-processual-penal": [
        ("Lei processual penal no tempo, no espaço e quanto às pessoas", "a00"),
        ("Inquérito policial e investigação criminal", "a01"),
        ("Provas I: teoria geral, corpo de delito e perícias", "a02 a03[1-4]"),
        ("Provas II: meios de prova em espécie", "a03[5-9]"),
        ("Prisões", "a04"),
        ("Liberdade provisória e medidas cautelares", "a05"),
        ("Juizados Especiais Criminais", "a06"),
    ],
    "contabilidade-geral": [
        ("Conceitos básicos, patrimônio e atos e fatos administrativos", "a00 a01"),
        ("Contas, plano de contas, escrituração e balancete", "a02 a03 a04"),
        ("Regimes contábeis, operações e estoques", "a05 a07"),
        ("Demonstrações contábeis: Lei 6.404/1976, balanço e DRE", "a06 a16"),
        ("Ativo imobilizado, impairment e intangível", "a08 a09 a10"),
        ("Passivo, provisões e operações financeiras", "a11 a12 a13"),
        ("Patrimônio líquido e reservas", "a14 a15"),
        ("Princípios contábeis, CPC 00 e CPC 26", "a17 a18 a19"),
    ],
    "legislacao-pcpe": [
        ("Estatuto do Policial Civil de Pernambuco", "a03 a04"),
        ("Estatuto do Servidor do Estado de Pernambuco", "a05 a06 a07"),
        ("Leis Complementares 137/2008 e 317/2015 e segurança pública na CE-PE", "a01 a02 c01"),
    ],
    "historia-pe": [
        ("História de Pernambuco", "a00"),
    ],
    "atualidades": [
        ("Panorama internacional I", "a00 a01"),
        ("Panorama internacional II", "a02"),
        ("Panorama nacional I", "a03 a04"),
        ("Panorama nacional II e desenvolvimento sustentável", "a05 a06"),
        ("Retrospectiva de março de 2026", "a07"),
        ("Retrospectiva de abril de 2026", "a09"),
        ("Retrospectiva de maio de 2026", "a11"),
        ("Retrospectiva de junho de 2026", "a13"),
        ("Retrospectiva de julho de 2026", "a15"),
        ("Retrospectiva de agosto de 2026", "a17"),
        ("Retrospectiva de setembro de 2026", "a19"),
    ],
}

# Mesmo assunto em duas disciplinas: o segundo volume reaproveita o primeiro (mesma base, foco ajustado ao concurso).
PARES = [
    ("raciocinio-logico/m05", "estatistica/m05", "Análise combinatória"),
    ("raciocinio-logico/m06", "estatistica/m06", "Probabilidade"),
    ("direito-penal-militar/m08", "legislacao-penal-especial/m02", "Abuso de autoridade (Lei 13.869/2019)"),
    ("direito-penal-militar/m08", "legislacao-penal-especial/m01", "Crimes de preconceito (Lei 7.716/1989)"),
    ("direito-constitucional/m14", "legislacao-penal-especial/m04", "Lei Maria da Penha e ECA"),
]

REF = re.compile(r"^([ac]\d{2})(?:\[(\d+)-(\d+)\])?$")


def load_segments() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    for f in sorted((CONTENT_DIR / "segments").glob("*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        out[d["subject"]] = d["segments"]
    return out


def load_importance() -> dict[str, dict]:
    return json.loads((CONTENT_DIR / "importance" / "segments.json").read_text(encoding="utf-8"))["segments"]


def wave_of(contests: dict) -> int:
    for i, (key, _) in enumerate(WAVES, start=1):
        if contests.get(key, {}).get("appears"):
            return i
    return 0


def build() -> tuple[dict[str, dict], list[str]]:
    segs = load_segments()
    imp = load_importance()
    problems: list[str] = []
    result: dict[str, dict] = {}
    for subject, vols in DIVISAO.items():
        by_aula: dict[str, list[dict]] = defaultdict(list)
        for s in segs[subject]:
            by_aula[s["aula"].split("/")[1]].append(s)
        used: set[str] = set()
        out_vols = []
        out_of_edital: list[str] = []
        for n, (title, refs) in enumerate(vols, start=1):
            trechos: list[str] = []
            for ref in refs.split():
                m = REF.match(ref)
                if not m:
                    problems.append(f"{subject}: referência inválida {ref!r}")
                    continue
                aula, a, b = m.group(1), m.group(2), m.group(3)
                lst = by_aula.get(aula, [])
                if not lst:
                    problems.append(f"{subject}: aula {aula} sem trechos")
                    continue
                pick = lst[int(a) - 1 : int(b)] if a else lst
                if a and len(pick) != int(b) - int(a) + 1:
                    problems.append(f"{subject}: {ref} fora do intervalo (a aula tem {len(lst)} trechos)")
                for s in pick:
                    if s["id"] in used:
                        problems.append(f"{subject}: trecho {s['id']} em dois volumes")
                    used.add(s["id"])
                    if wave_of(imp.get(s["id"], {}).get("contests", {})):
                        trechos.append(s["id"])
                    else:
                        out_of_edital.append(s["id"])
            waves = [wave_of(imp[t]["contests"]) for t in trechos]
            contests = sorted({c for t in trechos for c, v in imp[t]["contests"].items() if v.get("appears") and c in dict(WAVES)},
                              key=[w[0] for w in WAVES].index)
            if not trechos:
                problems.append(f"{subject}: volume {n} ({title}) sem trechos do edital")
            out_vols.append({
                "id": f"{subject}/m{n:02d}",
                "number": n,
                "title": title,
                "refs": refs,
                "wave": min(waves) if waves else 0,
                "contests": contests,
                "chapters": len(trechos),
                "trechos": trechos,
            })
        for s in segs[subject]:
            if s["id"] not in used:
                if wave_of(imp.get(s["id"], {}).get("contests", {})):
                    problems.append(f"{subject}: trecho do edital sem volume: {s['id']}")
                else:
                    out_of_edital.append(s["id"])
        for v in out_vols:
            if not 1 <= v["chapters"] <= 8:
                problems.append(f"{v['id']}: {v['chapters']} capítulos (o volume deve ter de 2 a 8; 1 só quando o assunto é único)")
        pares = [{"volumes": [a, b], "assunto": t} for a, b, t in PARES if a.startswith(subject + "/") or b.startswith(subject + "/")]
        result[subject] = {
            "subject": subject,
            "_comment": "Gerado por pipeline/material_volumes.py (não edite à mão: altere DIVISAO no script).",
            "volumes": out_vols,
            "foraDoEdital": sorted(set(out_of_edital)),
            "pares": pares,
        }
    for subject in segs:
        if subject not in DIVISAO:
            problems.append(f"{subject}: disciplina sem divisão")
    return result, problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    result, problems = build()
    total_v = sum(len(r["volumes"]) for r in result.values())
    total_c = sum(v["chapters"] for r in result.values() for v in r["volumes"])
    for subject, r in result.items():
        waves = sorted({v["wave"] for v in r["volumes"]})
        print(f"{subject:34s} {len(r['volumes']):3d} volumes {sum(v['chapters'] for v in r['volumes']):4d} capítulos  ondas {waves}  fora do edital {len(r['foraDoEdital'])}")
    print(f"TOTAL: {total_v} volumes, {total_c} capítulos")
    for p in problems:
        print("PROBLEMA:", p)
    if not args.check:
        out = MATERIAL_DIR / "volumes"
        out.mkdir(parents=True, exist_ok=True)
        for subject, r in result.items():
            (out / f"{subject}.json").write_text(json.dumps(r, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return 1 if any("sem volume" in p or "dois volumes" in p or "inválida" in p for p in problems) else 0


if __name__ == "__main__":
    raise SystemExit(main())
