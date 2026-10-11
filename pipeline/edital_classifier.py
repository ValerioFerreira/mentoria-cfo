"""Classificador inteligente de questões para o Edital Unificado CBMPE 2026.

Mapeia:
- Matéria do TecConcursos -> Uma das 16 disciplinas oficiais
- Assunto do TecConcursos + Enunciado -> Item específico do edital (content/edital/*.json)
- Atribui aulaId e segmentId para permitir a montagem dos cadernos de questões (Quiz/QuizActivity)
- Gera fila de revisão estruturada para casos de baixa confiança ou matérias de fronteira
"""
from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from pipeline.tec_extractor import TecQuestion

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / "content"
EDITAL_DIR = CONTENT_DIR / "edital"
SEGMENTS_DIR = CONTENT_DIR / "segments"

# Mapeamento canônico das matérias do TecConcursos para os slugs do sistema
SUBJECT_MAP: dict[str, str] = {
    "língua portuguesa (português)": "lingua-portuguesa",
    "lingua portuguesa": "lingua-portuguesa",
    "português": "lingua-portuguesa",
    "língua inglesa (inglês)": "lingua-inglesa",
    "lingua inglesa": "lingua-inglesa",
    "inglês": "lingua-inglesa",
    "língua espanhola (espanhol)": "lingua-espanhola",
    "lingua espanhola": "lingua-espanhola",
    "espanhol": "lingua-espanhola",
    "informática": "informatica",
    "informatica": "informatica",
    "estatística": "estatistica",
    "estatistica": "estatistica",
    "matemática": "matematica",
    "matematica": "matematica",
    "física": "fisica",
    "fisica": "fisica",
    "química e engenharia química": "quimica",
    "química": "quimica",
    "quimica": "quimica",
    "biologia e biomedicina": "biologia",
    "biologia": "biologia",
    "direito constitucional (cf/1988 e doutrina)": "direito-constitucional",
    "direito constitucional": "direito-constitucional",
    "direito administrativo (doutrina e leis federais)": "direito-administrativo",
    "direito administrativo": "direito-administrativo",
    "direito penal militar": "direito-penal-militar",
    "legislação penal e processual penal especial": "direito-penal-militar",
    "raciocínio lógico": "raciocinio-logico",
    "raciocinio logico": "raciocinio-logico",
    "atualidades e conhecimentos gerais": "atualidades",
    "atualidades": "atualidades",
    "história de pernambuco": "historia-pe",
    "historia de pernambuco": "historia-pe",
    "legislações pertinentes aos militares do estado de pernambuco": "legislacoes-pe",
    "legislação militar pe": "legislacoes-pe",
    "direito da criança e do adolescente": "direito-constitucional",
}

STOPWORDS = {
    "a", "o", "as", "os", "de", "da", "do", "das", "dos", "em", "no", "na",
    "nos", "nas", "e", "ou", "com", "para", "por", "sobre", "entre", "sem",
    "sob", "art", "arts", "lei", "n", "no", "que", "se", "um", "uma", "uns",
    "umas", "como", "ao", "aos", "à", "às", "pelo", "pela", "pelos", "pelas",
    "seu", "sua", "seus", "suas", "este", "esta", "estes", "estas", "esse",
    "essa", "esses", "essas", "aquele", "aquela", "aqueles", "aquelas", "qual",
    "quais", "onde", "quando", "quem", "cujo", "cuja", "cujos", "cujas"
}


def _normalize(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("ASCII").lower()
    return re.sub(r"[^a-z0-9\s]", " ", text)


def _tokenize(text: str) -> set[str]:
    words = _normalize(text).split()
    return {w for w in words if len(w) > 2 and w not in STOPWORDS}


@dataclass
class ClassificationResult:
    subject_id: str
    aula_id: str
    segment_id: str
    edital_item_id: str
    edital_topic: str
    confidence: float  # 0.0 a 1.0
    needs_review: bool
    review_reason: str | None


class EditalClassifier:
    def __init__(self) -> None:
        self.edital_cache: dict[str, list[dict[str, Any]]] = {}
        self.segments_cache: dict[str, list[dict[str, Any]]] = {}
        self.load_all_edital_data()

    def load_all_edital_data(self) -> None:
        for p in EDITAL_DIR.glob("*.json"):
            subj = p.stem
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                self.edital_cache[subj] = data.get("items", [])
            except Exception as e:
                print(f"Erro ao carregar edital {p}: {e}")

        for p in SEGMENTS_DIR.glob("*.json"):
            subj = p.stem
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                self.segments_cache[subj] = data.get("segments", [])
            except Exception as e:
                print(f"Erro ao carregar segmentos {p}: {e}")

    def resolve_subject(self, raw_subject: str) -> str:
        norm = raw_subject.strip().lower()
        if norm in SUBJECT_MAP:
            return SUBJECT_MAP[norm]
        for k, v in SUBJECT_MAP.items():
            if k in norm or norm in k:
                return v
        return "outros"

    def classify_question(self, q: TecQuestion) -> ClassificationResult:
        subj_id = self.resolve_subject(q.raw_subject)

        # Se não mapeou para disciplina conhecida, fallback
        if subj_id not in self.edital_cache or not self.edital_cache[subj_id]:
            # Tentativa de busca por palavras-chave do assunto em todas as disciplinas
            best_sub = "lingua-portuguesa"
            return ClassificationResult(
                subject_id=best_sub,
                aula_id=f"{best_sub}/a00",
                segment_id=f"{best_sub}/a00/s01",
                edital_item_id="fallback",
                edital_topic=q.raw_topic or q.raw_subject,
                confidence=0.1,
                needs_review=True,
                review_reason=f"Disciplina original '{q.raw_subject}' não mapeada diretamente",
            )

        items = self.edital_cache[subj_id]
        raw_topic_tokens = _tokenize(q.raw_topic)
        statement_tokens = _tokenize(q.statement[:300])
        q_tokens = raw_topic_tokens | set(list(statement_tokens)[:15])

        best_item: dict[str, Any] | None = None
        best_score = -1.0

        for it in items:
            it_tokens = _tokenize(it["item"])
            for w in it.get("where", []):
                it_tokens.update(_tokenize(w.get("topic", "")))

            if not raw_topic_tokens:
                overlap = len(statement_tokens.intersection(it_tokens))
                score = overlap / (len(it_tokens) or 1)
            else:
                topic_overlap = len(raw_topic_tokens.intersection(it_tokens))
                statement_overlap = len(statement_tokens.intersection(it_tokens))
                score = (topic_overlap * 2.5 + statement_overlap * 0.5) / (len(raw_topic_tokens) * 2.5 + 1)

            if score > best_score:
                best_score = score
                best_item = it

        if best_item is None or best_score < 0.1:
            # Fallback para o primeiro item do edital
            best_item = items[0]
            confidence = 0.25
            needs_review = True
            review_reason = "Baixa similaridade léxica com tópicos do edital"
        else:
            confidence = min(1.0, round(best_score, 2))
            needs_review = confidence < 0.35
            review_reason = "Confiança moderada/baixa" if needs_review else None

        # Obter aulaId e segmentId
        where_list = best_item.get("where", [])
        aula_id = f"{subj_id}/a00"
        segment_id = f"{subj_id}/a00/s01"

        if where_list:
            w0 = where_list[0]
            aula_id = w0.get("aula", aula_id)
            segs = w0.get("segments", [])
            if segs:
                # Escolher segmento com maior afinidade léxica entre os tópicos do segmento
                segment_id = segs[0]
                if len(segs) > 1 and subj_id in self.segments_cache:
                    subj_segs = {s["id"]: s for s in self.segments_cache[subj_id]}
                    best_seg_score = -1
                    for sid in segs:
                        s_data = subj_segs.get(sid)
                        if s_data:
                            s_tokens = _tokenize(" ".join(s_data.get("topicsCovered", [])))
                            s_score = len(q_tokens.intersection(s_tokens))
                            if s_score > best_seg_score:
                                best_seg_score = s_score
                                segment_id = sid

        return ClassificationResult(
            subject_id=subj_id,
            aula_id=aula_id,
            segment_id=segment_id,
            edital_item_id=str(best_item.get("id", "1")),
            edital_topic=best_item.get("item", q.raw_topic),
            confidence=confidence,
            needs_review=needs_review,
            review_reason=review_reason,
        )
