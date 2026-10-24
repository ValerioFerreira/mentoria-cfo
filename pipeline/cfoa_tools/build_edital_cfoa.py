"""Gera o mapa do edital do 2º Tenente CFOA CBMPE (Instituto AOCP) para todas as 9 disciplinas.

- Disciplinas novas (administracao, direitos-humanos, direito-processual-penal-militar):
  gravadas diretamente em content/edital/<disciplina>.json.
- Disciplinas compartilhadas (lingua-portuguesa, raciocinio-logico, direito-constitucional,
  direito-administrativo, direito-penal-militar, legislacoes-pe):
  gravadas em content/edital/cfoa/<disciplina>.json para não sobrescrever os mapas do CBMPE Oficial/Praça nem da PCPE.
"""
from __future__ import annotations

import collections
import json
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
CONTENT_DIR = ROOT / "content"
EDITAL_DIR = CONTENT_DIR / "edital"
CFOA_EDITAL_DIR = EDITAL_DIR / "cfoa"


def page_range(spec) -> tuple[int, int] | None:
    if spec in (None, ""):
        return None
    a, _, b = str(spec).replace("–", "-").partition("-")
    try:
        lo = int(a)
        return lo, int(b or a)
    except ValueError:
        return None


def all_segments() -> dict[str, list[dict]]:
    by_aula: dict[str, list[dict]] = collections.defaultdict(list)
    for f in (CONTENT_DIR / "segments").glob("*.json"):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            by_aula[s["aula"]].append(s)
    return by_aula


def resolve_segments(doc: dict, segs_by_aula: dict[str, list[dict]]) -> None:
    for it in doc.get("items", []):
        for w in it.get("where", []):
            aula = w.get("aula")
            rng = page_range(w.get("pages"))
            cand = segs_by_aula.get(aula, [])
            if rng:
                lo, hi = rng
                hit = [s["id"] for s in cand if s["startPage"] <= hi and s["endPage"] >= lo]
            else:
                hit = [s["id"] for s in cand]
            w["segments"] = hit


CFOA_NEW_MAPS: dict[str, dict] = {
    "administracao": {
        "subject": "administracao",
        "block": "II",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Teorias administrativas clássicas",
                "status": "covered",
                "where": [{"aula": "administracao/a01", "pages": "6-22"}],
            },
            {
                "id": "1.2",
                "title": "O ambiente externo e a organização",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a01", "pages": "50-60"},
                    {"aula": "administracao/a03", "pages": "6-16"},
                ],
            },
            {
                "id": "1.3",
                "title": "A organização burocrática",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a01", "pages": "23-37"},
                    {"aula": "administracao/a04", "pages": "74-88"},
                ],
            },
            {
                "id": "1.4",
                "title": "Abordagem mecanicista da organização",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a01", "pages": "50-60"},
                    {"aula": "administracao/a04", "pages": "57-73"},
                ],
            },
            {
                "id": "1.5",
                "title": "A estrutura formal da organização",
                "status": "covered",
                "where": [{"aula": "administracao/a04", "pages": "7-42"}],
            },
            {
                "id": "1.6",
                "title": "Abordagens recentes da organização",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a01", "pages": "38-60"},
                    {"aula": "administracao/a04", "pages": "74-100"},
                ],
            },
            {
                "id": "1.7",
                "title": "Linha e assessoria",
                "status": "covered",
                "where": [{"aula": "administracao/a04", "pages": "57-73"}],
            },
            {
                "id": "1.8",
                "title": "Autoridade e responsabilidade",
                "status": "covered",
                "where": [{"aula": "administracao/a04", "pages": "43-56"}],
            },
            {
                "id": "1.9",
                "title": "Direção",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a00", "pages": "21-35"},
                    {"aula": "administracao/a05", "pages": "6-59"},
                ],
            },
            {
                "id": "1.10",
                "title": "Processo decisório",
                "status": "complement",
                "where": [
                    {"aula": "administracao/a01", "pages": "38-49"},
                    {"aula": "administracao/a04", "pages": "43-56"},
                    {"aula": "administracao/c01", "pages": "1-6"},
                ],
                "gap": "cfoa-adm-lacunas",
                "note": "Coberto pelas aulas base e pelo complemento autoral sobre processo decisório e mudança organizacional (administracao/c01).",
            },
            {
                "id": "1.11",
                "title": "Controle: elementos e princípios gerais aplicados ao controle",
                "status": "covered",
                "where": [
                    {"aula": "administracao/a00", "pages": "21-35"},
                    {"aula": "administracao/a07", "pages": "7-27"},
                ],
            },
            {
                "id": "1.12",
                "title": "Mudança organizacional",
                "status": "complement",
                "where": [
                    {"aula": "administracao/a01", "pages": "38-49"},
                    {"aula": "administracao/a08", "pages": "46-59"},
                    {"aula": "administracao/c01", "pages": "1-6"},
                ],
                "gap": "cfoa-adm-lacunas",
                "note": "Coberto pelas aulas base e pelo complemento autoral sobre processo decisório e mudança organizacional (administracao/c01).",
            },
            {
                "id": "1.13",
                "title": "Cultura organizacional",
                "status": "covered",
                "where": [{"aula": "administracao/a08", "pages": "7-59"}],
            },
        ],
    },
    "direitos-humanos": {
        "subject": "direitos-humanos",
        "block": "II",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Fundamentos históricos dos Direitos Humanos",
                "status": "covered",
                "where": [{"aula": "direitos-humanos/a01", "pages": "3-10"}],
            },
            {
                "id": "1.2",
                "title": "Conceito de Direitos Humanos, cidadania e democracia",
                "status": "covered",
                "where": [
                    {"aula": "direitos-humanos/a00", "pages": "6-26"},
                    {"aula": "direitos-humanos/a05", "pages": "4-36"},
                ],
            },
            {
                "id": "1.3",
                "title": "Declaração Universal dos Direitos Humanos (ONU, 1948)",
                "status": "covered",
                "where": [{"aula": "direitos-humanos/a02", "pages": "6-40"}],
            },
            {
                "id": "2",
                "title": "Convenção sobre a Eliminação de Todas as Formas de Discriminação contra a Mulher (CEDAW, 1979)",
                "status": "complement",
                "where": [{"aula": "direitos-humanos/c01", "pages": "1-6"}],
                "gap": "cfoa-dh-cedaw",
                "note": "Coberto pelo complemento autoral MentorIA sobre a CEDAW e seu Protocolo Facultativo (direitos-humanos/c01).",
            },
            {
                "id": "3",
                "title": "Convenção Internacional sobre os Direitos das Pessoas com Deficiência (ONU, 2006 / Decreto nº 6.949/2009)",
                "status": "complement",
                "where": [{"aula": "direitos-humanos/c02", "pages": "1-6"}],
                "gap": "cfoa-dh-convencao-pcd",
                "note": "Coberto pelo complemento autoral MentorIA sobre a Convenção Internacional sobre os Direitos das Pessoas com Deficiência (direitos-humanos/c02).",
            },
            {
                "id": "4",
                "title": "A legislação e os Direitos Humanos no Brasil",
                "status": "covered",
                "where": [
                    {"aula": "direitos-humanos/a04", "pages": "4-26"},
                    {"aula": "direitos-humanos/a05", "pages": "4-36"},
                ],
            },
        ],
    },
    "direito-processual-penal-militar": {
        "subject": "direito-processual-penal-militar",
        "block": "III",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Da Lei de Processo Penal Militar e da sua aplicação",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a00", "pages": "3-17"}],
            },
            {
                "id": "1.2",
                "title": "Prerrogativas do posto ou da função",
                "status": "complement",
                "where": [
                    {"aula": "direito-processual-penal-militar/a06", "pages": "3-18"},
                    {"aula": "direito-processual-penal-militar/a08", "pages": "29-36"},
                    {"aula": "direito-processual-penal-militar/c01", "pages": "1-6"},
                ],
                "gap": "cfoa-dppm-lacunas",
                "note": "Coberto pelas aulas base e pelo complemento autoral sobre prerrogativas do posto ou função no CPPM (direito-processual-penal-militar/c01).",
            },
            {
                "id": "1.3",
                "title": "Delito flagrante",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a08", "pages": "29-36"}],
            },
            {
                "id": "1.4",
                "title": "Comparecimento espontâneo do indiciado ou acusado",
                "status": "complement",
                "where": [
                    {"aula": "direito-processual-penal-militar/a08", "pages": "37-43"},
                    {"aula": "direito-processual-penal-militar/c01", "pages": "1-6"},
                ],
                "gap": "cfoa-dppm-lacunas",
                "note": "Coberto pela aula 08 e pelo complemento autoral sobre os arts. 226 e 262 do CPPM (direito-processual-penal-militar/c01).",
            },
            {
                "id": "1.5",
                "title": "Interrogatório do indiciado ou acusado",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a10", "pages": "3-10"}],
            },
            {
                "id": "1.6",
                "title": "Inquirição de testemunhas",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a10", "pages": "11-17"}],
            },
            {
                "id": "1.7",
                "title": "Reconhecimento de pessoa ou coisa",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a10", "pages": "11-17"}],
            },
            {
                "id": "2.1",
                "title": "Polícia Judiciária Militar",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a01", "pages": "3-11"}],
            },
            {
                "id": "2.2",
                "title": "Inquérito Policial Militar",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a02", "pages": "3-26"}],
            },
            {
                "id": "2.3",
                "title": "Auto de prisão em flagrante delito",
                "status": "covered",
                "where": [
                    {"aula": "direito-processual-penal-militar/a02", "pages": "16-26"},
                    {"aula": "direito-processual-penal-militar/a08", "pages": "29-36"},
                ],
            },
            {
                "id": "2.4",
                "title": "Instrução provisória de deserção",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a12", "pages": "3-11"}],
            },
            {
                "id": "2.5",
                "title": "Medidas preventivas e assecuratórias",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a08", "pages": "3-43"}],
            },
            {
                "id": "2.6",
                "title": "Incidente de insanidade mental",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a07", "pages": "3-7"}],
            },
            {
                "id": "2.7",
                "title": "Providências que recaem sobre coisas: busca e apreensão, restituição, arresto, sequestro, hipoteca legal",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a08", "pages": "3-28"}],
            },
            {
                "id": "2.8",
                "title": "Perícias e exames",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a10", "pages": "3-10"}],
            },
            {
                "id": "2.9",
                "title": "Documentos",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a10", "pages": "11-17"}],
            },
            {
                "id": "3.1",
                "title": "Providências que recaem sobre pessoas: prisão provisória (disposições gerais) e prisão em flagrante",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a08", "pages": "29-36"}],
            },
            {
                "id": "3.2",
                "title": "Prisão preventiva",
                "status": "covered",
                "where": [{"aula": "direito-processual-penal-militar/a08", "pages": "37-43"}],
            },
            {
                "id": "3.3",
                "title": "Menagem e liberdade provisória",
                "status": "complement",
                "where": [
                    {"aula": "direito-processual-penal-militar/a08", "pages": "37-43"},
                    {"aula": "direito-processual-penal-militar/c01", "pages": "1-6"},
                ],
                "gap": "cfoa-dppm-lacunas",
                "note": "Coberto pela aula 08 e pelo complemento autoral sobre menagem e liberdade provisória (arts. 263 a 271 do CPPM) em direito-processual-penal-militar/c01.",
            },
        ],
    },
}


CFOA_SHARED_MAPS: dict[str, dict] = {
    "lingua-portuguesa": {
        "subject": "lingua-portuguesa",
        "contest": "CBMPE_CFOA",
        "block": "I",
        "examQuestions": 10,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1",
                "title": "Compreensão e interpretação de texto",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a01", "pages": "4-65"}],
            },
            {
                "id": "2",
                "title": "Tipologia e gêneros textuais",
                "status": "covered",
                "where": [
                    {"aula": "lingua-portuguesa/a01", "pages": "4-65"},
                    {"aula": "lingua-portuguesa/a11", "pages": "3-22"},
                ],
            },
            {
                "id": "3",
                "title": "Ortografia oficial",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a03", "pages": "3-31"}],
            },
            {
                "id": "4",
                "title": "Acentuação gráfica",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a02", "pages": "3-90"}],
            },
            {
                "id": "5",
                "title": "Emprego das classes de palavras",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a04", "pages": "3-87"}],
            },
            {
                "id": "6",
                "title": "Emprego do sinal indicativo de crase",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a09", "pages": "3-25"}],
            },
            {
                "id": "7",
                "title": "Sintaxe da oração e do período",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a05", "pages": "3-77"}],
            },
            {
                "id": "8",
                "title": "Pontuação",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a06", "pages": "3-30"}],
            },
            {
                "id": "9",
                "title": "Concordância nominal e verbal",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a07", "pages": "3-41"}],
            },
            {
                "id": "10",
                "title": "Regência nominal e verbal",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a08", "pages": "3-33"}],
            },
            {
                "id": "11",
                "title": "Significação das palavras",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a10", "pages": "3-18"}],
            },
            {
                "id": "12",
                "title": "Redação Oficial: Manual de Redação da Presidência da República (aspectos gerais, características fundamentais, padrões, emprego e concordância dos pronomes de tratamento, ofício, requerimento, parecer)",
                "status": "covered",
                "where": [{"aula": "lingua-portuguesa/a13", "pages": "3-91"}],
            },
        ],
    },
    "raciocinio-logico": {
        "subject": "raciocinio-logico",
        "contest": "CBMPE_CFOA",
        "block": "I",
        "examQuestions": 10,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1",
                "title": "Compreensão de estruturas lógicas",
                "status": "covered",
                "where": [
                    {"aula": "raciocinio-logico/a00", "pages": "5-83"},
                    {"aula": "raciocinio-logico/a01", "pages": "5-96"},
                    {"aula": "raciocinio-logico/a02", "pages": "5-79"},
                ],
            },
            {
                "id": "2.1",
                "title": "Lógica de argumentação: analogias",
                "status": "covered",
                "where": [{"aula": "raciocinio-logico/a05", "pages": "5-100"}],
            },
            {
                "id": "2.2",
                "title": "Lógica de argumentação: inferências, deduções e conclusões",
                "status": "covered",
                "where": [
                    {"aula": "raciocinio-logico/a04", "pages": "5-94"},
                    {"aula": "raciocinio-logico/a05", "pages": "5-100"},
                ],
            },
            {
                "id": "3",
                "title": "Diagramas lógicos",
                "status": "covered",
                "where": [
                    {"aula": "raciocinio-logico/a03", "pages": "5-90"},
                    {"aula": "raciocinio-logico/a04", "pages": "5-94"},
                ],
            },
            {
                "id": "4.1",
                "title": "Princípios de contagem",
                "status": "covered",
                "where": [{"aula": "raciocinio-logico/a06", "pages": "5-93"}],
            },
            {
                "id": "4.2",
                "title": "Probabilidade",
                "status": "covered",
                "where": [{"aula": "raciocinio-logico/a07", "pages": "5-96"}],
            },
        ],
    },
    "direito-constitucional": {
        "subject": "direito-constitucional",
        "contest": "CBMPE_CFOA",
        "block": "II",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Dos direitos e deveres individuais e coletivos",
                "status": "covered",
                "where": [
                    {"aula": "direito-constitucional/a02", "pages": "3-56"},
                    {"aula": "direito-constitucional/a03", "pages": "3-56"},
                ],
            },
            {
                "id": "1.2",
                "title": "Dos direitos políticos",
                "status": "covered",
                "where": [{"aula": "direito-constitucional/a06", "pages": "3-68"}],
            },
            {
                "id": "2.1",
                "title": "Dos militares dos Estados, do Distrito Federal e dos Territórios",
                "status": "covered",
                "where": [{"aula": "direito-constitucional/a09", "pages": "66-85"}],
            },
            {
                "id": "2.2",
                "title": "Disposições constitucionais estaduais aplicáveis aos militares (art. 100 a 105-B da Constituição do Estado de Pernambuco)",
                "status": "covered",
                "where": [
                    {"aula": "direito-constitucional/a18", "pages": "4-15"},
                    {"aula": "direito-constitucional/a09", "pages": "66-85"},
                    {"aula": "direito-constitucional/a15", "pages": "14-29"},
                ],
            },
            {
                "id": "3",
                "title": "Do Poder Judiciário: Dos Tribunais e Juízes Militares; Dos Tribunais e Juízes dos Estados",
                "status": "covered",
                "where": [{"aula": "direito-constitucional/a13", "pages": "74-81"}],
            },
            {
                "id": "4.1",
                "title": "Das Forças Armadas",
                "status": "covered",
                "where": [{"aula": "direito-constitucional/a15", "pages": "3-13"}],
            },
            {
                "id": "4.2",
                "title": "Da Segurança Pública",
                "status": "covered",
                "where": [{"aula": "direito-constitucional/a15", "pages": "14-29"}],
            },
        ],
    },
    "direito-administrativo": {
        "subject": "direito-administrativo",
        "contest": "CBMPE_CFOA",
        "block": "II",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Conceito de administração pública sob os aspectos orgânico, formal e material",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a01", "pages": "58-65"}],
            },
            {
                "id": "1.2",
                "title": "Conceito de direito administrativo",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a01", "pages": "4-25"}],
            },
            {
                "id": "1.3",
                "title": "Fontes do direito administrativo: doutrina e jurisprudência na formação do direito administrativo; lei formal; regulamentos administrativos, estatutos e regimentos; instruções; tratados internacionais; costume",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a01", "pages": "26-38"}],
            },
            {
                "id": "1.4",
                "title": "Relações do direito administrativo com outros ramos do direito",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a01", "pages": "4-25"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 01 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "1.5",
                "title": "Sistemas administrativos: sistema inglês, sistema francês e sistema adotado no Brasil",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a01", "pages": "34-42"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 01 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "2.1",
                "title": "Administração pública direta e indireta; órgãos e entidades; centralização e descentralização da atividade administrativa do Estado",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a02", "pages": "4-62"}],
            },
            {
                "id": "2.2",
                "title": "Administração pública direta: órgãos públicos (conceito, espécies, regime), hierarquia, poder hierárquico e suas manifestações; distribuição de competências: centralização, desconcentração, delegação e avocação",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a02", "pages": "14-33"},
                    {"aula": "direito-administrativo/a04", "pages": "3-25"},
                ],
            },
            {
                "id": "2.3",
                "title": "Administração pública indireta: autarquias, fundações públicas, sociedades de economia mista e empresas públicas",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a02", "pages": "34-62"},
                    {"aula": "direito-administrativo/a03", "pages": "4-38"},
                ],
            },
            {
                "id": "2.4",
                "title": "Administração pública de controle: Tribunal de Contas e Ministério Público",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a07", "pages": "25-45"}],
            },
            {
                "id": "3.1",
                "title": "Princípios informativos do regime jurídico-administrativo: legalidade, supremacia do interesse público, impessoalidade, moralidade, publicidade, eficiência, razoabilidade, motivação, autotutela, continuidade do serviço público",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a00", "pages": "5-50"}],
            },
            {
                "id": "3.2",
                "title": "Princípios da boa administração e da tutela",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a00", "pages": "36-38"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 00 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "3.3",
                "title": "Princípio da presunção de legitimidade ou de veracidade",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a05", "pages": "60-68"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 05 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "4.1",
                "title": "Poderes da Administração Pública: vinculado e discricionário, hierárquico, disciplinar e regulamentar",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a04", "pages": "3-40"}],
            },
            {
                "id": "4.2",
                "title": "Poder de polícia: conceito, polícia administrativa e polícia judiciária, características, limites, meios de atuação, sanções",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a04", "pages": "41-75"}],
            },
            {
                "id": "4.3",
                "title": "Deveres dos administradores públicos: dever de agir, dever de eficiência, dever de probidade, dever de prestar contas",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a04", "pages": "3-15"}],
            },
            {
                "id": "4.4",
                "title": "Uso e abuso do poder: excesso de poder, desvio de poder, omissão da Administração",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a04", "pages": "10-20"}],
            },
            {
                "id": "5.1",
                "title": "Atos administrativos: conceito, fatos da Administração, atos da Administração e atos administrativos",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a05", "pages": "4-30"}],
            },
            {
                "id": "5.2",
                "title": "Requisitos ou elementos do ato administrativo: competência, finalidade, forma, motivo e objeto",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a05", "pages": "31-59"}],
            },
            {
                "id": "5.3",
                "title": "Mérito do ato administrativo",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a05", "pages": "47-59"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 05 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "5.4",
                "title": "Atributos do ato administrativo: presunção de legitimidade, imperatividade, exigibilidade e autoexecutoriedade",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a05", "pages": "60-77"}],
            },
            {
                "id": "5.5",
                "title": "Classificação dos atos administrativos; espécies: normativos, ordinatórios, negociais, enunciativos e punitivos",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a05", "pages": "78-115"}],
            },
            {
                "id": "5.6",
                "title": "Motivação e invalidação dos atos administrativos: revogação, anulação, convalidação e teoria dos motivos determinantes",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a05", "pages": "47-55"},
                    {"aula": "direito-administrativo/a05", "pages": "116-152"},
                ],
            },
            {
                "id": "6.1",
                "title": "Agentes públicos: conceito e categorias (agentes políticos, administrativos, honoríficos, delegados e credenciados)",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a09", "pages": "4-25"}],
            },
            {
                "id": "6.2",
                "title": "Cargo, emprego e função: normas constitucionais, provimento, vacância, direitos e deveres, responsabilidade, acumulação, estabilidade e vitaliciedade",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a09", "pages": "26-172"}],
            },
            {
                "id": "7.1",
                "title": "Processos administrativos: conceito, princípios, fases e modalidades",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a23", "pages": "3-26"}],
            },
            {
                "id": "7.2",
                "title": "Processo Administrativo Disciplinar: sindicância, processo sumário",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a09", "pages": "164-172"},
                    {"aula": "direito-administrativo/a23", "pages": "3-26"},
                ],
            },
            {
                "id": "7.3",
                "title": "Conselhos de Disciplina e de Justificação",
                "status": "complement",
                "where": [{"aula": "direito-administrativo/c03", "pages": "1-7"}],
                "gap": "cfoa-da-conselhos",
                "note": "Coberto pelo complemento autoral MentorIA sobre o Decreto Estadual nº 3.639/1975 e a Lei Federal nº 5.836/1972 (direito-administrativo/c03).",
            },
            {
                "id": "7.4",
                "title": "Enriquecimento ilícito e abuso de autoridade (Lei de Improbidade Administrativa)",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a24", "pages": "3-111"}],
            },
            {
                "id": "8.1",
                "title": "Serviços públicos: conceito, caracteres jurídicos, classificação e garantias; usuário do serviço público",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a06", "pages": "3-22"}],
            },
            {
                "id": "8.2",
                "title": "Concessão, permissão e autorização de serviço público; convênios e consórcios administrativos",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a06", "pages": "23-55"},
                    {"aula": "direito-administrativo/a22", "pages": "27-39"},
                ],
            },
            {
                "id": "9.1",
                "title": "Intervenção do Estado no domínio econômico: monopólio, repressão ao abuso do poder econômico, controle de abastecimento e tabelamento de preços",
                "status": "complement",
                "where": [{"aula": "direito-administrativo/c04", "pages": "1-9"}],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pelo complemento autoral MentorIA em direito-administrativo/c04.",
            },
            {
                "id": "9.2",
                "title": "Desapropriação: conceito, características, fundamentos, requisitos constitucionais, objeto, competência, desapropriação indireta, por zona, retrocessão e processo",
                "status": "complement",
                "where": [{"aula": "direito-administrativo/c04", "pages": "1-9"}],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pelo complemento autoral MentorIA em direito-administrativo/c04.",
            },
            {
                "id": "10.1",
                "title": "Licitações (Lei nº 14.133/2021): conceito, finalidades, princípios e objeto; obrigatoriedade, dispensa, inexigibilidade e vedação",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a20", "pages": "3-42"},
                    {"aula": "direito-administrativo/a21", "pages": "3-55"},
                ],
            },
            {
                "id": "10.2",
                "title": "Modalidades, procedimentos, fases, revogação, anulação, desistência e recursos administrativos na licitação",
                "status": "covered",
                "where": [
                    {"aula": "direito-administrativo/a20", "pages": "43-116"},
                    {"aula": "direito-administrativo/a21", "pages": "71-113"},
                ],
            },
            {
                "id": "10.3",
                "title": "Contratos administrativos: conceito, características, cláusulas exorbitantes e de privilégio; formalização, execução, fiscalização, alteração, extinção, inexecução e revisão",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a22", "pages": "3-146"}],
            },
            {
                "id": "10.4",
                "title": "Modalidades de contratos administrativos e figuras afins; convênios administrativos",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a22", "pages": "3-39"}],
            },
            {
                "id": "10.5",
                "title": "Sistema de Cadastramento Unificado de Fornecedores (SICAF) e Sistema de Rating de Fornecedores",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a21", "pages": "114-129"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 21 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "10.6",
                "title": "Contratação compartilhada e compras centralizadas",
                "status": "complement",
                "where": [
                    {"aula": "direito-administrativo/a21", "pages": "130-144"},
                    {"aula": "direito-administrativo/c04", "pages": "1-9"},
                ],
                "gap": "cfoa-da-lacunas",
                "note": "Coberto pela aula 21 e pelo complemento autoral em direito-administrativo/c04.",
            },
            {
                "id": "10.7",
                "title": "Sanções administrativas e tutela judicial na Lei de Licitações; crimes em licitações e contratos administrativos",
                "status": "covered",
                "where": [{"aula": "direito-administrativo/a22", "pages": "147-189"}],
            },
        ],
    },
    "direito-penal-militar": {
        "subject": "direito-penal-militar",
        "contest": "CBMPE_CFOA",
        "block": "III",
        "examQuestions": 5,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1.1",
                "title": "Da aplicação da lei penal militar: princípio da legalidade, lei supressiva de incriminação, retroatividade de lei mais benigna",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a00", "pages": "4-14"}],
            },
            {
                "id": "1.2",
                "title": "Tempo do crime, lugar do crime, territorialidade e extraterritorialidade",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a00", "pages": "4-14"}],
            },
            {
                "id": "1.3",
                "title": "Pena cumprida no estrangeiro e contagem de prazo",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a00", "pages": "4-14"}],
            },
            {
                "id": "1.4",
                "title": "Crimes militares em tempo de paz",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a00", "pages": "15-29"}],
            },
            {
                "id": "1.5",
                "title": "Equiparação a comandante, conceito de superior, crime praticado em presença do inimigo, pessoa considerada militar e assemelhado, defeito de incorporação e militares estrangeiros",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a00", "pages": "30-42"}],
            },
            {
                "id": "2.1",
                "title": "Do crime: relação de causalidade, consumação e tentativa",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a01", "pages": "4-22"}],
            },
            {
                "id": "2.2",
                "title": "Desistência voluntária e arrependimento eficaz, crime impossível",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a01", "pages": "4-22"}],
            },
            {
                "id": "2.3",
                "title": "Culpabilidade: dolo e culpa, excepcionalidade do crime culposo, erro de direito e erro de fato",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a01", "pages": "23-49"}],
            },
            {
                "id": "2.4",
                "title": "Exclusão de crime: estado de necessidade e legítima defesa",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a01", "pages": "50-65"}],
            },
            {
                "id": "3.1",
                "title": "Dos crimes contra a autoridade ou disciplina militar: motim e revolta",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "4-13"}],
            },
            {
                "id": "3.2",
                "title": "Conspiração, aliciação para motim ou revolta e incitamento",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "14-18"}],
            },
            {
                "id": "3.3",
                "title": "Violência contra superior ou militar de serviço",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "16-18"}],
            },
            {
                "id": "3.4",
                "title": "Desrespeito a superior, a símbolo nacional ou à farda",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "19-21"}],
            },
            {
                "id": "3.5",
                "title": "Recusa de obediência, oposição a ordem de sentinela, reunião ilícita e publicação ou crítica indevida",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "22-25"}],
            },
            {
                "id": "3.6",
                "title": "Resistência mediante ameaça ou violência",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "32-36"}],
            },
            {
                "id": "4.1",
                "title": "Dos crimes contra o serviço militar e o dever militar: deserção, casos assimilados e modalidades",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "40-46"}],
            },
            {
                "id": "4.2",
                "title": "Abandono de posto, descumprimento de missão, dormir em serviço e embriaguez em serviço",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a08", "pages": "47-55"}],
            },
            {
                "id": "5.1",
                "title": "Dos crimes contra a Administração Militar: desacato, desobediência, ingresso clandestino",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a10", "pages": "4-10"}],
            },
            {
                "id": "5.2",
                "title": "Peculato, peculato-furto, peculato mediante aproveitamento do erro de outrem e apropriação de coisa achada",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a10", "pages": "11-21"}],
            },
            {
                "id": "5.3",
                "title": "Concussão, excesso de exação e desvio",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a10", "pages": "11-21"}],
            },
            {
                "id": "5.4",
                "title": "Corrupção passiva e ativa, participação ilícita, prevaricação e condescendência criminosa",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a10", "pages": "22-29"}],
            },
            {
                "id": "5.5",
                "title": "Inobservância de lei, regulamento ou instrução e violação de sigilo funcional",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a10", "pages": "22-37"}],
            },
            {
                "id": "6.1",
                "title": "Crimes previstos na Lei de Licitações (arts. 337-E a 337-P do Código Penal, incluídos pela Lei nº 14.133/2021)",
                "status": "complement",
                "where": [{"aula": "direito-penal-militar/c02", "pages": "1-6"}],
                "gap": "cfoa-dpm-crimes-licitacoes",
                "note": "Coberto pelo complemento autoral MentorIA sobre os crimes em licitações e contratos administrativos (arts. 337-E a 337-P do CP) em direito-penal-militar/c02.",
            },
            {
                "id": "6.2",
                "title": "Crimes de Abuso de Autoridade (Lei nº 13.869/2019)",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a20", "pages": "3-24"}],
            },
            {
                "id": "6.3",
                "title": "Crimes resultantes de preconceito de raça ou de cor (Lei nº 7.716/1989)",
                "status": "covered",
                "where": [{"aula": "direito-penal-militar/a21", "pages": "3-15"}],
            },
        ],
    },
    "legislacoes-pe": {
        "subject": "legislacoes-pe",
        "contest": "CBMPE_CFOA",
        "block": "III",
        "examQuestions": 10,
        "source": "Edital CBMPE CFOA — Quadro de Oficiais de Administração (Instituto AOCP)",
        "items": [
            {
                "id": "1",
                "title": "Código Disciplinar dos Militares do Estado de Pernambuco (Lei Estadual nº 11.817/2000)",
                "status": "covered",
                "where": [
                    {"aula": "legislacoes-pe/a01", "pages": "5-23"},
                    {"aula": "legislacoes-pe/c01", "pages": "1-4"},
                    {"aula": "legislacoes-pe/c04", "pages": "1-6"},
                ],
            },
            {
                "id": "2",
                "title": "Estatuto dos Militares do Estado de Pernambuco (Lei Estadual nº 6.783/1974)",
                "status": "covered",
                "where": [
                    {"aula": "legislacoes-pe/a02", "pages": "5-25"},
                    {"aula": "legislacoes-pe/c05", "pages": "1-4"},
                ],
            },
            {
                "id": "3",
                "title": "Código de Ética dos Militares do Estado de Pernambuco (Decreto Estadual nº 22.114/2000)",
                "status": "complement",
                "where": [{"aula": "legislacoes-pe/c06", "pages": "1-5"}],
                "gap": "cfoa-leg-dec-22114",
                "note": "Coberto pelo complemento autoral MentorIA sobre o Decreto Estadual nº 22.114/2000 (legislacoes-pe/c06).",
            },
            {
                "id": "4",
                "title": "Lei de Promoção de Oficiais e Praças da PMPE e do CBMPE (Lei Complementar Estadual nº 470/2021)",
                "status": "complement",
                "where": [{"aula": "legislacoes-pe/c07", "pages": "1-7"}],
                "gap": "cfoa-leg-lc-470",
                "note": "Coberto pelo complemento autoral MentorIA sobre a Lei Complementar Estadual nº 470/2021 (legislacoes-pe/c07).",
            },
            {
                "id": "5",
                "title": "Processo Administrativo no âmbito da Administração Pública Estadual (Lei Estadual nº 11.781/2000)",
                "status": "elsewhere",
                "where": [{"aula": "direito-administrativo/a23", "pages": "3-26"}],
                "note": "Coberto integralmente em Direito Administrativo (direito-administrativo/a23).",
            },
            {
                "id": "6",
                "title": "Lei de Improbidade Administrativa (Lei Federal nº 8.429/1992 e alterações da Lei nº 14.230/2021)",
                "status": "elsewhere",
                "where": [{"aula": "direito-administrativo/a24", "pages": "3-111"}],
                "note": "Coberto integralmente em Direito Administrativo (direito-administrativo/a24).",
            },
            {
                "id": "7",
                "title": "Lei de Acesso à Informação (Lei Federal nº 12.527/2011)",
                "status": "complement",
                "where": [{"aula": "legislacoes-pe/c08", "pages": "1-6"}],
                "gap": "cfoa-leg-lai-12527",
                "note": "Coberto pelo complemento autoral MentorIA sobre a Lei Federal nº 12.527/2011 (legislacoes-pe/c08).",
            },
            {
                "id": "8",
                "title": "Prevenção e punição ao assédio moral na Administração Pública Estadual (Lei Estadual nº 13.314/2007)",
                "status": "complement",
                "where": [{"aula": "legislacoes-pe/c09", "pages": "1-5"}],
                "gap": "cfoa-leg-assedio-13314",
                "note": "Coberto pelo complemento autoral MentorIA sobre a Lei Estadual nº 13.314/2007 e alterações (legislacoes-pe/c09).",
            },
            {
                "id": "9",
                "title": "Sindicância Policial Militar (Portaria Normativa SDS nº 395, de 03/02/2015)",
                "status": "gap",
                "where": [],
                "gap": "cfoa-leg-portaria-395",
                "note": "Portaria Normativa SDS nº 395/2015 (Boletim Geral SDS nº 022/2015) sem texto integral disponível em portal legislativo público oficial; pendente de fornecimento do texto oficial pelo dono.",
            },
            {
                "id": "10",
                "title": "Investigação Preliminar (Provimento Correicional nº 21/2021 — Corregedoria Geral da SDS/PE)",
                "status": "gap",
                "where": [],
                "gap": "cfoa-leg-provimento-21",
                "note": "Provimento Correicional nº 21/2021 da Corregedoria Geral da SDS/PE sem texto integral disponível em portal legislativo público oficial; pendente de fornecimento do texto oficial pelo dono.",
            },
        ],
    },
}


def main() -> int:
    segs = all_segments()
    EDITAL_DIR.mkdir(parents=True, exist_ok=True)
    CFOA_EDITAL_DIR.mkdir(parents=True, exist_ok=True)

    for sid, doc in CFOA_NEW_MAPS.items():
        resolve_segments(doc, segs)
        out = EDITAL_DIR / f"{sid}.json"
        out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"Gerado {out.relative_to(ROOT)} ({len(doc['items'])} itens)")

    for sid, doc in CFOA_SHARED_MAPS.items():
        resolve_segments(doc, segs)
        out = CFOA_EDITAL_DIR / f"{sid}.json"
        out.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"Gerado {out.relative_to(ROOT)} ({len(doc['items'])} itens)")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
