"""Gera content/edital/pcpe/<disciplina>.json (itens do edital do Agente de Polícia da PCPE → aulas/trechos reais).

Fonte dos itens: edital oficial (pipeline/.cache/pcpe-baseline/edital_extract.txt, seção 22.2.3). Cada item aponta:
  - `refs`: ids de itens de content/edital/<disciplina>.json (mapa padrão já auditado); reaproveita aulas/páginas/trechos,
    descartando aulas que não valem para o PCPE (excludeContests/onlyContests no catálogo);
  - `segs`: [(rótulo, "aNN:1-3" | "cNN" | "aNN")] trechos reais (content/segments), páginas impressas calculadas aqui.
O status é 'complement' se alguma localização é aula complementar (cNN), senão o informado (padrão 'covered');
sem localização vira 'gap' (ou 'elsewhere', se informado). Uso: python pipeline/pcpe_tools/build_edital_pcpe.py [disciplina ...]
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "content"
CONTEST = "PCPE_AGENTE"

CAT = json.loads((C / "catalog.json").read_text(encoding="utf-8"))
AULA = {a["id"]: a for s in CAT["subjects"] for a in s["aulas"]}


def valid_for_pcpe(aula_id: str) -> bool:
    a = AULA.get(aula_id)
    if not a or not a.get("selectable"):
        return False
    if CONTEST in (a.get("excludeContests") or []):
        return False
    only = a.get("onlyContests")
    return not only or CONTEST in only


_seg_cache: dict[str, dict[str, dict]] = {}


def segments(subject: str) -> dict[str, dict]:
    if subject not in _seg_cache:
        doc = json.loads((C / "segments" / f"{subject}.json").read_text(encoding="utf-8"))
        _seg_cache[subject] = {g["id"]: g for g in doc["segments"]}
    return _seg_cache[subject]


def expand(subject: str, spec: str) -> tuple[str, list[str]]:
    """'a06:1-8' -> ('<subject>/a06', ids); 'a06' -> todos os trechos; 'a06:3' -> um."""
    aula, _, rng = spec.partition(":")
    aula_id = f"{subject}/{aula}"
    ids = sorted(i for i in segments(subject) if segments(subject)[i]["aula"] == aula_id)
    if rng:
        lo, _, hi = rng.partition("-")
        lo, hi = int(lo), int(hi or lo)
        ids = [i for i in ids if lo <= int(i.rsplit("/s", 1)[1]) <= hi]
    if not ids:
        raise SystemExit(f"sem trechos para {subject} {spec}")
    return aula_id, ids


def pages_of(subject: str, ids: list[str]) -> str:
    segs = [segments(subject)[i] for i in ids]
    lo = min(s["startPrinted"] for s in segs)
    hi = max(s["endPrinted"] for s in segs)
    return f"{lo}-{hi}" if hi != lo else str(lo)


def build_where(subject: str, item: dict, default: dict[str, dict]) -> list[dict]:
    where: list[dict] = []
    seen: set[tuple] = set()

    def add(w: dict) -> None:
        key = (w["aula"], w["pages"], w["topic"])
        if key not in seen:
            seen.add(key)
            where.append(w)

    for ref in item.get("refs", []):
        d = default.get(ref)
        if not d:
            raise SystemExit(f"{subject}: ref inexistente {ref}")
        for w in d["where"]:
            if valid_for_pcpe(w["aula"]) and w["aula"].startswith(subject + "/"):
                add({"aula": w["aula"], "pages": str(w["pages"]), "topic": w["topic"], "segments": list(w.get("segments") or [])})
    for label, spec in item.get("segs", []):
        aula_id, ids = expand(subject, spec)
        if not valid_for_pcpe(aula_id):
            raise SystemExit(f"{subject}: aula {aula_id} não vale para o PCPE")
        add({"aula": aula_id, "pages": pages_of(subject, ids), "topic": label, "segments": ids})
    return where


def finish(subject: str, spec: list[dict]) -> dict:
    default_path = C / "edital" / f"{subject}.json"
    default = {i["id"]: i for i in json.loads(default_path.read_text(encoding="utf-8"))["items"]} if default_path.exists() else {}
    items = []
    for it in spec:
        where = build_where(subject, it, default)
        status = it.get("status", "covered")
        if not where:
            status = "elsewhere" if status == "elsewhere" else "gap"
        elif any(re.search(r"/c\d+$", w["aula"]) for w in where):
            status = "complement"
        out = {"id": it["id"], "item": it["item"], "status": status, "where": where}
        if it.get("notes"):
            out["notes"] = it["notes"]
        items.append(out)
    return {"subject": subject, "contest": CONTEST, "items": items}


# ------------------------------------------------------------------ especificação
SPEC: dict[str, list[dict]] = {}

SPEC["raciocinio-logico"] = [
    {"id": "7", "item": "Princípios de contagem", "segs": [("Princípios de contagem, permutações, arranjos e combinações", "a06")]},
    {"id": "9", "item": "Compreensão de estruturas lógicas", "segs": [("Proposições e conectivos lógicos", "a00"), ("Linguagem proposicional, tabelas-verdade e implicação", "a01")]},
    {"id": "10", "item": "Lógica de argumentação: analogias, inferências, deduções e conclusões", "segs": [("Argumentos dedutivos, silogismos e métodos de validade", "a04"), ("Estrutura dos argumentos, indução, abdução e falácias", "a05")]},
    {"id": "11.1", "item": "Lógica sentencial (ou proposicional): proposições simples e compostas", "segs": [("Proposições simples e compostas e conectivos", "a00")]},
    {"id": "11.2", "item": "Lógica sentencial: tabelas-verdade", "segs": [("Tabela-verdade, tautologia, contradição e contingência", "a01:2-7")]},
    {"id": "11.3", "item": "Lógica sentencial: equivalências", "segs": [("Equivalências lógicas", "a02")]},
    {"id": "11.4", "item": "Lógica sentencial: leis de De Morgan", "segs": [("Negações lógicas e leis de De Morgan", "a02:2-4")]},
    {"id": "11.5", "item": "Lógica sentencial: diagramas lógicos", "segs": [("Proposições categóricas e diagramas lógicos", "a03")]},
    {"id": "12", "item": "Lógica de primeira ordem", "segs": [("Proposições quantificadas e categóricas", "a03")]},
    {"id": "13", "item": "Princípios de contagem e probabilidade", "segs": [("Análise combinatória", "a06"), ("Probabilidade", "a07")]},
    {"id": "14", "item": "Operações com conjuntos", "segs": [("Operações com conjuntos (material complementar MentorIA)", "c01")],
     "notes": "Resolvido por complemento autoral (lacuna rl-operacoes-conjuntos)."},
    {"id": "15", "item": "Raciocínio lógico envolvendo problemas matriciais (a parte aritmética e geométrica do item está em Matemática)",
     "segs": [("Matrizes e determinantes (material complementar MentorIA)", "c02")],
     "notes": "Resolvido por complemento autoral (lacuna rl-matrizes-determinantes)."},
]

SPEC["matematica"] = [
    {"id": "1", "item": "Conjuntos numéricos: números inteiros, racionais e reais", "segs": [("Conjuntos numéricos", "a00"), ("Operações fundamentais", "a01:1-2")]},
    {"id": "2", "item": "Sistema legal de medidas", "segs": [("Unidades de medida", "a02")]},
    {"id": "3", "item": "Razões e proporções", "segs": [("Frações, razão e proporção", "a03")]},
    {"id": "3.1", "item": "Divisão proporcional", "segs": [("Divisão proporcional (material complementar MentorIA)", "c03"), ("Razão e proporção", "a03:4-5")],
     "notes": "Resolvido por complemento autoral (lacuna mat-divisao-proporcional)."},
    {"id": "3.2", "item": "Regras de três simples e compostas", "segs": [("Regra de três simples e composta", "a04")]},
    {"id": "3.3", "item": "Porcentagens", "segs": [("Porcentagem, aumentos, descontos e variação", "a05")]},
    {"id": "4", "item": "Equações e inequações de 1º e de 2º graus", "segs": [("Equações e inequações", "a08")]},
    {"id": "5", "item": "Sistemas lineares", "segs": [("Sistemas de equações", "a08:1")], "status": "partial",
     "notes": "Sistemas de equações do 1º grau em Matemática; a escrita matricial, a inversa e a regra de Cramer estão no complemento de matrizes de Raciocínio Lógico (item 15)."},
    {"id": "6", "item": "Funções e gráficos", "segs": [("Introdução ao estudo das funções", "a09"), ("Função afim", "a10"), ("Função quadrática", "a11")]},
    {"id": "8", "item": "Progressões aritméticas e geométricas", "segs": [("Sequências, progressão aritmética e geométrica", "a14")]},
    {"id": "15", "item": "Raciocínio lógico envolvendo problemas aritméticos e geométricos (a parte matricial do item está em Raciocínio Lógico)",
     "segs": [("Situações-problema e expressões", "a01:4"), ("Geometria plana", "a15")]},
]

SPEC["estatistica"] = [
    {"id": "1", "item": "Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medidas descritivas (posição, dispersão, assimetria e curtose)",
     "segs": [("Apresentação de dados, tabelas e gráficos", "a00"), ("Médias", "a01"), ("Medidas separatrizes e box plot", "a02"), ("Moda", "a03"),
              ("Medidas de dispersão", "a04"), ("Assimetria e curtose (material complementar MentorIA)", "c02:1"), ("Normas de apresentação de dados", "c01")],
     "notes": "Assimetria e curtose resolvidas por complemento autoral (lacuna est-assimetria-curtose)."},
    {"id": "2.1", "item": "Probabilidade: definições básicas e axiomas", "segs": [("Noções, definição clássica, união e complementar, axiomas", "a06:1-3")]},
    {"id": "2.2", "item": "Probabilidade: probabilidade condicional e independência", "segs": [("Probabilidade condicional, multiplicação, independência e Bayes", "a06:4-5")]},
    {"id": "3.1", "item": "Técnicas de amostragem: amostragem aleatória simples, estratificada, sistemática e por conglomerados",
     "segs": [("Tipos de amostragem", "c01"), ("Estratos e amostragem sistemática (material complementar MentorIA)", "c02")]},
    {"id": "3.2", "item": "Técnicas de amostragem: tamanho amostral", "segs": [("Tamanho da amostra (material complementar MentorIA)", "c02")],
     "notes": "Resolvido por complemento autoral (lacuna est-tamanho-amostral)."},
]

SPEC["direito-constitucional"] = [
    {"id": "1.1", "item": "Constituição da República Federativa do Brasil de 1988: princípios fundamentais", "segs": [("Princípios fundamentais, arts. 1º a 4º (material complementar MentorIA)", "c06")],
     "notes": "Resolvido por complemento autoral (lacuna dc-principios-fundamentais)."},
    {"id": "1.2", "item": "Poderes constituintes originário, derivado e decorrente", "refs": ["3.1", "3.2", "3.3"]},
    {"id": "2", "item": "Aplicabilidade das normas constitucionais", "refs": ["4"]},
    {"id": "3", "item": "Direitos e garantias fundamentais", "refs": ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7"]},
    {"id": "4", "item": "Organização político-administrativa do Estado: Estado federal brasileiro, União, estados, Distrito Federal, municípios e territórios", "refs": ["7.1", "7.2", "7.3", "7.4"]},
    {"id": "5", "item": "Administração pública: disposições gerais e servidores públicos", "refs": ["7.5", "7.6"]},
    {"id": "6", "item": "Poder Executivo", "refs": ["8.2"]},
    {"id": "7", "item": "Poder Legislativo", "refs": ["8.1"]},
    {"id": "8", "item": "Poder Judiciário", "refs": ["8.3"]},
    {"id": "9.1", "item": "Funções essenciais à justiça: Ministério Público", "segs": [("Ministério Público", "a14:1-2")]},
    {"id": "9.2", "item": "Funções essenciais à justiça: advocacia pública", "segs": [("Advocacia pública", "a14:3")]},
    {"id": "9.3", "item": "Funções essenciais à justiça: Defensoria Pública", "segs": [("Defensoria Pública", "a14:3")]},
    {"id": "10", "item": "Defesa do Estado e das instituições democráticas", "refs": ["10"]},
    {"id": "11", "item": "Segurança pública na Constituição do Estado de Pernambuco", "status": "elsewhere",
     "notes": "Tratado na disciplina Legislação da PCPE (Constituição do Estado de Pernambuco, arts. 101 a 105-B)."},
]

SPEC["direito-administrativo"] = [
    {"id": "1", "item": "Estado, governo e administração pública", "refs": ["1.1", "1.2", "1.3"]},
    {"id": "2", "item": "Direito administrativo", "refs": ["2.1", "2.2"]},
    {"id": "3", "item": "Ato administrativo", "refs": ["6.1", "6.2", "6.3", "6.4", "6.5", "6.6", "6.7", "6.8", "6.9", "6.10"]},
    {"id": "4.1", "item": "Poderes da administração pública: hierárquico, disciplinar, regulamentar e de polícia", "refs": ["5.1", "5.2", "5.3", "5.4", "5.5"]},
    {"id": "4.2", "item": "Poderes da administração pública: uso e abuso do poder", "refs": ["5.6"]},
    {"id": "5.1", "item": "Regime jurídico-administrativo: conceito", "segs": [("Regime jurídico administrativo", "a00:1")]},
    {"id": "5.2", "item": "Regime jurídico-administrativo: princípios expressos e implícitos da administração pública", "refs": ["2.3"]},
    {"id": "6", "item": "Responsabilidade civil do Estado", "refs": ["8.4"]},
    {"id": "7", "item": "Serviços públicos", "refs": ["7.1", "7.2", "7.3"]},
    {"id": "8.1", "item": "Organização administrativa: centralização, descentralização, concentração e desconcentração", "refs": ["3.1"]},
    {"id": "8.2", "item": "Organização administrativa: administração direta e indireta", "refs": ["3.2", "3.3"]},
    {"id": "9.1", "item": "Controle da administração pública: controle exercido pela administração pública", "refs": ["8.1"]},
    {"id": "9.2", "item": "Controle da administração pública: controle judicial", "refs": ["8.3"]},
    {"id": "9.3", "item": "Controle da administração pública: controle legislativo", "refs": ["8.2"]},
    {"id": "9.4", "item": "Controle da administração pública: improbidade administrativa", "refs": ["9.4"]},
    {"id": "10", "item": "Processo administrativo", "refs": ["10"]},
    {"id": "11", "item": "Licitações e contratos administrativos", "refs": ["11.1", "11.2"]},
    {"id": "12.1", "item": "Agente público: legislação pertinente", "refs": ["4.1", "4.2", "4.12"],
     "notes": "A legislação estadual aplicável (Lei nº 6.123/1968 e leis do Policial Civil) está na disciplina Legislação da PCPE."},
    {"id": "12.2", "item": "Agente público: disposições constitucionais aplicáveis", "status": "elsewhere",
     "notes": "Tratado em Direito Constitucional (Administração pública: servidores públicos, arts. 37 a 41)."},
    {"id": "13", "item": "Cargo, emprego e função pública", "refs": ["4.3", "4.4", "4.5"]},
]

SPEC["lingua-portuguesa"] = [
    {"id": "1", "item": "Compreensão e interpretação de textos de gêneros variados", "refs": ["1"]},
    {"id": "2", "item": "Reconhecimento de tipos e gêneros textuais", "refs": ["2"]},
    {"id": "3", "item": "Domínio da ortografia oficial", "refs": ["5", "6"]},
    {"id": "4.1", "item": "Mecanismos de coesão textual: elementos de referenciação, substituição e repetição, conectores e sequenciação textual", "refs": ["11", "4"]},
    {"id": "4.2", "item": "Mecanismos de coesão textual: emprego de tempos e modos verbais", "segs": [("Verbos: tempos, modos e conjugação", "a04")]},
    {"id": "5.1", "item": "Estrutura morfossintática do período: emprego das classes de palavras", "refs": ["7"]},
    {"id": "5.2", "item": "Estrutura morfossintática do período: relações de coordenação entre orações e entre termos da oração", "refs": ["9.1", "9.2", "9.3", "9.4"]},
    {"id": "5.3", "item": "Estrutura morfossintática do período: relações de subordinação entre orações e entre termos da oração", "refs": ["9.4", "10"]},
    {"id": "5.4", "item": "Estrutura morfossintática do período: emprego dos sinais de pontuação", "refs": ["12"]},
    {"id": "5.5", "item": "Estrutura morfossintática do período: concordância verbal e nominal", "refs": ["13"]},
    {"id": "5.6", "item": "Estrutura morfossintática do período: regência verbal e nominal", "refs": ["14"]},
    {"id": "5.7", "item": "Estrutura morfossintática do período: emprego do sinal indicativo de crase", "refs": ["8"]},
    {"id": "5.8", "item": "Estrutura morfossintática do período: colocação dos pronomes átonos", "refs": ["15"]},
    {"id": "6.1", "item": "Reescrita de frases e parágrafos do texto: significação das palavras", "refs": ["17"]},
    {"id": "6.2", "item": "Reescrita de frases e parágrafos do texto: substituição de palavras ou de trechos de texto", "refs": ["17", "4"]},
    {"id": "6.3", "item": "Reescrita de frases e parágrafos do texto: reorganização da estrutura de orações e de períodos", "refs": ["9.4", "4"]},
    {"id": "6.4", "item": "Reescrita de frases e parágrafos do texto: reescrita de textos de diferentes gêneros e níveis de formalidade", "refs": ["2"], "segs": [("Redação oficial e níveis de formalidade", "a13")]},
    {"id": "7.1", "item": "Correspondência oficial: aspectos gerais da redação oficial", "segs": [("Manual de Redação da Presidência da República", "a13")]},
    {"id": "7.2", "item": "Correspondência oficial: finalidade dos expedientes oficiais", "segs": [("Manual de Redação da Presidência da República", "a13")]},
    {"id": "7.3", "item": "Correspondência oficial: adequação da linguagem ao tipo de documento", "segs": [("Manual de Redação da Presidência da República", "a13")]},
    {"id": "7.4", "item": "Correspondência oficial: adequação do formato do texto ao gênero", "segs": [("Manual de Redação da Presidência da República", "a13")]},
]

SPEC["informatica"] = [
    {"id": "1.1", "item": "Sistema operacional Windows: fundamentos (janelas, menus, barra de tarefas, área de trabalho)", "refs": ["6.1"]},
    {"id": "1.2", "item": "Sistema operacional Windows: trabalho com pastas e arquivos", "refs": ["6.2", "5.1"]},
    {"id": "1.3", "item": "Sistema operacional Windows: configurações básicas (resolução da tela, cores, fontes, impressoras, aparência, segundo plano, protetor de tela)", "refs": ["6.3", "6.4"]},
    {"id": "1.4", "item": "Sistema operacional Windows: Windows Explorer", "refs": ["6.2"]},
    {"id": "2.1", "item": "Microsoft 365: processador de textos Word", "refs": ["7.1"]},
    {"id": "2.2", "item": "Microsoft 365: planilha eletrônica Excel", "refs": ["7.2"]},
    {"id": "2.3", "item": "Microsoft 365: software de apresentação PowerPoint", "refs": ["7.3"]},
    {"id": "3.1", "item": "Redes de computadores: conceitos básicos, ferramentas, aplicativos e procedimentos de Internet e intranet, grupos de discussão, redes sociais, computação na nuvem, programas de navegação, deep web e dark web",
     "refs": ["1.1", "1.2", "2.1", "2.3", "2.4"]},
    {"id": "3.2", "item": "Redes de computadores: correio eletrônico, endereços e utilização de recursos típicos", "refs": ["2.3"]},
    {"id": "3.3", "item": "Redes de computadores: navegadores, sítios de busca e pesquisa na Internet", "refs": ["2.2"]},
    {"id": "3.4", "item": "Redes de computadores: conceitos de segurança, procedimentos e segurança de acessos, programas maliciosos, ferramentas antivírus e criptografia",
     "refs": ["3.1", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7"]},
    {"id": "3.5", "item": "Redes de computadores: procedimentos de backup e armazenamento de dados na nuvem", "refs": ["4.1", "4.2", "4.3", "2.4"]},
]


def main(argv: list[str]) -> None:
    out_dir = C / "edital" / "pcpe"
    out_dir.mkdir(parents=True, exist_ok=True)
    subjects = argv or list(SPEC)
    for subject in subjects:
        doc = finish(subject, SPEC[subject])
        (out_dir / f"{subject}.json").write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        by = {}
        for it in doc["items"]:
            by[it["status"]] = by.get(it["status"], 0) + 1
        print(f"{subject}: {len(doc['items'])} itens {by}")


if __name__ == "__main__":
    main(sys.argv[1:])
