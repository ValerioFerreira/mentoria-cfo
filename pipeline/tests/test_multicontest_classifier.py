"""Demonstração e testes da arquitetura do classificador multiconcurso (Item 3 da Rodada 5).

Garante que:
1. Questões da AOCP (CBMPE) são classificadas nas aulas de CBMPE (sem vazar para aulas exclusivas da PCPE).
2. Questões do Cebraspe (PCPE) sobre a Lei 14.133/2021 caem em direito-administrativo/a20 ou a21 (e não nas aulas legadas).
3. Matérias compartilhadas (ex.: ECA / Legislação Especial) direcionam para a disciplina correta de cada concurso.
"""
import json
import sys
from pathlib import Path
import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))
CONTENT = ROOT / "content"

from questoes.classify import (
    Classifier,
    load_catalog,
    assunto_key,
    question_text,
    _tfidf,
    features,
    _cos,
    Result
)



def is_aula_in_contest(aula_meta: dict, contest: str | None) -> bool:
    """Verifica se uma aula é elegível para o concurso informado."""
    if not contest:
        return True
    if not aula_meta.get("selectable", True):
        return False
    if aula_meta.get("onlyContests") and contest not in aula_meta["onlyContests"]:
        return False
    if aula_meta.get("excludeContests") and contest in aula_meta["excludeContests"]:
        return False
    return True


class MultiContestClassifier:
    """Wrapper / Proposta de arquitetura que torna o classificador sensível ao concurso do lote."""

    def __init__(self, base_classifier: Classifier, contest_maps: dict[str, dict] | None = None):
        self.base = base_classifier
        self.cat = base_classifier.cat
        # Sobreposições específicas por concurso (ex.: PCPE_AGENTE)
        self.contest_maps = contest_maps or {}

    def subject_for(self, materia: str, assunto: str, contest: str | None) -> tuple[str | None, dict]:
        # 1. Consulta mapa específico do concurso, se existir
        if contest and contest in self.contest_maps:
            c_map = self.contest_maps[contest]
            akey = assunto_key(materia, assunto)
            if akey in c_map.get("assuntos", {}):
                entry = c_map["assuntos"][akey]
                subj = entry.get("subject") or c_map.get("materias", {}).get(materia)
                return subj, entry
            if materia in c_map.get("materias", {}):
                m_entry = c_map["materias"][materia]
                if isinstance(m_entry, dict):
                    return m_entry.get("subject"), m_entry
                return m_entry, {}

        # 2. Fallback para o mapa base (legado)
        return self.base.subject_for(materia, assunto)

    def candidate_aulas(self, subject: str, entry: dict, contest: str | None) -> list[str]:
        catalog_json = json.loads((CONTENT / "catalog.json").read_text(encoding="utf-8"))
        aulas_meta = {a["id"]: a for s in catalog_json["subjects"] for a in s["aulas"]}

        if entry.get("aulas"):
            cands = [a for a in entry["aulas"] if a in self.cat.aulas]
        else:
            cands = [aid for aid, a in self.cat.aulas.items() if a["subject"] == subject and a["selectable"] and a["segments"]]

        # Filtro de elegibilidade por concurso (is_aula_in_contest)
        if contest:
            cands = [a for a in cands if is_aula_in_contest(aulas_meta.get(a, {}), contest)]
        return cands

    def classify(self, q: dict, contest: str | None = None) -> Result:
        materia = q.get("materia", "")
        assunto = q.get("assunto", "")

        subject, entry = self.subject_for(materia, assunto, contest)
        if entry.get("skip"):
            return Result(subject, None, None, None, 0.0, "manual", "SKIP", str(entry["skip"]))
        if not subject:
            return Result(None, None, None, None, 0.0, "baixa", "SKIP", f"matéria sem mapa: {materia}")

        v = self.base.qvec(q, subject)
        aulas = self.candidate_aulas(subject, entry, contest)

        if not aulas:
            return Result(subject, None, None, None, 0.0, "baixa", "SKIP", "sem aulas candidatas no concurso")

        seg_cands = [s for a in aulas for s in self.cat.aulas[a]["segments"]]
        if not seg_cands:
            return Result(subject, None, None, None, 0.0, "baixa", "SKIP", "sem trechos candidatos no concurso")

        scored = sorted(((s, _cos(v, self.cat.vec.get(s, {}))) for s in seg_cands), key=lambda t: -t[1])
        best, score = scored[0]
        seg = self.cat.segments[best]
        return Result(subject, seg.aula, best, None, score, "alta", "APPROVED", f"classificado para {contest or 'padrao'}")


@pytest.fixture(scope="module")
def classifier():
    base = Classifier(catalog=load_catalog(use_material=False, cache=False))
    # Sobreposições específicas para a PCPE
    pcpe_overrides = {
        "PCPE_AGENTE": {
            "materias": {
                "Direito da Criança e do Adolescente": "legislacao-penal-especial",
                "Legislação Penal e Processual Penal Especial": "legislacao-penal-especial"
            },
            "assuntos": {
                "Direito Administrativo (Doutrina e Leis Federais)|Licitações (Lei 14.133/2021)": {
                    "subject": "direito-administrativo",
                    "aulas": ["direito-administrativo/a20", "direito-administrativo/a21"]
                }
            }
        }
    }
    return MultiContestClassifier(base, pcpe_overrides)


def test_cebraspe_licitacao_classifies_to_pcpe_a20_or_a21(classifier):
    """Garante que questão fictícia do Cebraspe sobre a Lei 14.133/2021 vai para a20/a21 no PCPE_AGENTE."""
    q_cebraspe = {
        "id": "q-cebraspe-001",
        "banca": "Cebraspe",
        "materia": "Direito Administrativo (Doutrina e Leis Federais)",
        "assunto": "Licitações (Lei 14.133/2021)",
        "statement": "À luz da Nova Lei de Licitações (Lei nº 14.133/2021), o diálogo competitivo é a modalidade de licitação para contratação de obras, serviços e compras em que a Administração Pública realiza diálogos com licitantes previamente selecionados.",
        "options": []
    }

    res = classifier.classify(q_cebraspe, contest="PCPE_AGENTE")
    assert res.subjectId == "direito-administrativo"
    assert res.aulaId in ["direito-administrativo/a20", "direito-administrativo/a21"], f"Deveria cair em a20/a21, caiu em {res.aulaId}"
    assert res.status == "APPROVED"


def test_aocp_question_never_leaks_to_pcpe_exclusive_aulas(classifier):
    """Garante que questão da AOCP para o CBMPE NUNCA cai nas aulas exclusivas da PCPE (a20..a24)."""
    q_aocp = {
        "id": "q-aocp-001",
        "banca": "Instituto AOCP",
        "materia": "Direito Administrativo (Doutrina e Leis Federais)",
        "assunto": "Licitações (Lei 14.133/2021)",
        "statement": "Assinale a alternativa correta acerca dos procedimentos licitatórios e contratos administrativos.",
        "options": []
    }

    res = classifier.classify(q_aocp, contest="CBMPE_OFICIAL")
    assert res.subjectId == "direito-administrativo"
    assert res.aulaId not in ["direito-administrativo/a20", "direito-administrativo/a21", "direito-administrativo/a22", "direito-administrativo/a23", "direito-administrativo/a24"]


def test_eca_question_maps_to_proper_subject_by_contest(classifier):
    """ECA no CBMPE vai para Direito Constitucional (dc-eca / c01); na PCPE vai para Legislação Penal Especial."""
    q_eca = {
        "id": "q-eca-001",
        "materia": "Direito da Criança e do Adolescente",
        "assunto": "Prática de Ato Infracional",
        "statement": "Nos termos do Estatuto da Criança e do Adolescente (Lei nº 8.069/1990), considera-se ato infracional a conduta descrita como crime ou contravenção penal.",
        "options": []
    }

    # No CBMPE: mapeia para direito-constitucional
    res_cbmpe = classifier.classify(q_eca, contest="CBMPE_OFICIAL")
    assert res_cbmpe.subjectId == "direito-constitucional"

    # Na PCPE: mapeia para legislacao-penal-especial
    res_pcpe = classifier.classify(q_eca, contest="PCPE_AGENTE")
    assert res_pcpe.subjectId == "legislacao-penal-especial"
