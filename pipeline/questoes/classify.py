"""Classificação das questões do TecConcursos: matéria → disciplina, assunto → aula(s), questão → trecho
(atividade) e item do edital. Especificação: EXTRACAO.md, seção "Classificação".

Sinais, em ordem de força:
1. content/questoes/mapa-assuntos.json — curadoria: matéria → disciplina e "matéria|assunto" → aulas
   (ou trechos) permitidos, ou `skip` (fora do edital).
2. TF-IDF (Python puro) entre a questão e o documento de cada trecho: título da aula, tópicos do
   trecho, itens do edital que apontam para ele, bizu (resumo, ponteiros, itens C/E), resumo analítico
   e — se o cache local existir — o texto do material das páginas do trecho.
3. Voto do assunto: sem curadoria, todas as questões do mesmo assunto somam seus vetores para escolher
   a aula; a questão escolhe o trecho dentro dela.
"""
from __future__ import annotations

import json
import math
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
MAP_PATH = CONTENT / "questoes" / "mapa-assuntos.json"

# limiares da classificação automática (assunto sem curadoria), calibrados em EXTRACAO.md
AUTO_MIN_SCORE = 0.12  # similaridade mínima da melhor aula
AUTO_MIN_RATIO = 1.35  # melhor aula / segunda melhor aula
# trecho: similaridade mínima da questão com o trecho escolhido. Calibrado na amostra validada de 14/10/2026:
# abaixo de 0,05 só 19% das questões eram ensinadas pelo trecho; vão para rascunho (revisão), não para o aluno.
SEGMENT_MIN_SCORE = 0.05
# Português: interpretação de texto casa pouco com os tópicos do trecho; abaixo de 0,05 o acerto é o mesmo (≈50%)
SEGMENT_MIN_BY_SUBJECT = {"lingua-portuguesa": 0.03}
OVERRIDES_PATH = CONTENT / "questoes" / "overrides-questoes.json"

STOP = set(
    """a o as os um uma uns umas de do da dos das em no na nos nas por pelo pela pelos pelas para pra
    com sem sob sobre entre ate apos ante e ou nem mas que se ao aos à às é ser sao foi era sera esta
    este esse essa isso isto aquele aquela aquilo seu sua seus suas meu minha nosso nossa lhe lhes
    ele ela eles elas nao sim como mais menos muito muita muitos muitas ja ainda tambem quando onde
    qual quais quanto quantos cujo cuja the of and to in is are be for on with as by at an or from
    that this it its was were has have had not but which assinale alternativa correta incorreta
    afirmar afirmativa afirmativas assertiva assertivas item itens seguinte seguintes acordo conforme
    respeito considerando considere julgue questao abaixo acima texto trecho opcao resposta sobre
    certo errado verdadeiro falso apresenta apresentam correto incorreto exceto analise relacao""".split()
)

_MD_IMG = re.compile(r"!\[[^\]]*\]\([^)]*\)")
_TAGS = re.compile(r"</?[a-z]+>")


def fold(t: str) -> str:
    t = unicodedata.normalize("NFKD", t)
    return "".join(c for c in t if not unicodedata.combining(c)).lower()


def stem(w: str) -> str:
    for suf, rep in (("coes", "cao"), ("soes", "sao"), ("aes", "ao"), ("ais", "al"), ("eis", "el"), ("ois", "ol"), ("is", "il")):
        if w.endswith(suf) and len(w) > len(suf):
            return w[: -len(suf)] + rep
    if w.endswith("es") and len(w) > 5 and w[-3] in "rzl":
        return w[:-2]
    if w.endswith("s") and len(w) > 4 and not w.endswith(("ss", "us", "is")):
        return w[:-1]
    return w


def tokens(text: str) -> list[str]:
    text = _TAGS.sub(" ", _MD_IMG.sub(" ", text or "")).replace("**", " ")
    words = re.findall(r"[a-z0-9]+(?:-[a-z]+)?", fold(text))
    out = []
    for w in words:
        if w in STOP or len(w) < 2 or w.isdigit() and len(w) < 3:
            continue
        out.append(stem(w))
    return out


def features(text: str, weight: float = 1.0) -> Counter:
    tk = tokens(text)
    c: Counter = Counter()
    for w in tk:
        c[w] += weight
    for a, b in zip(tk, tk[1:]):
        c[a + "_" + b] += weight * 0.8
    return c


# ───────────────────────── catálogo ─────────────────────────


@dataclass
class SegInfo:
    id: str
    aula: str
    subject: str
    order: int
    doc: Counter = field(default_factory=Counter)
    edital: list[tuple[str, str]] = field(default_factory=list)  # (editalItemId, texto)


@dataclass
class Catalog:
    segments: dict[str, SegInfo]
    aulas: dict[str, dict]  # id -> {title, subject, selectable, segments: [...]}
    edital_items: dict[str, dict]  # editalItemId -> {subject, title, aulas, segments}
    idf: dict[str, dict[str, float]]  # subject -> termo -> idf
    vec: dict[str, dict[str, float]]  # segmento -> vetor tf-idf normalizado
    aula_vec: dict[str, dict[str, float]]


def _jload(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def _bizu_text(seg_id: str, items_cache: dict) -> tuple[str, str]:
    subj, aula, _ = seg_id.split("/")
    key = f"{subj}/{aula}"
    if key not in items_cache:
        p = CONTENT / "items" / subj / f"{aula}.json"
        items_cache[key] = {s["id"]: s for s in _jload(p)["segments"]} if p.exists() else {}
    s = items_cache[key].get(seg_id)
    if not s or "bizu" not in s:
        return "", ""
    b = s["bizu"]
    strong = " ".join(b.get("summary") or []) + " " + " ".join(p.get("topic", "") for p in b.get("pointers") or [])
    weak = " ".join(x.get("statement", "") for x in (b.get("teoria") or []) + (b.get("revisao") or []))
    return strong, weak


def _analytic(seg_id: str, cache: dict) -> str:
    subj, aula, _ = seg_id.split("/")
    key = f"{subj}/{aula}"
    if key not in cache:
        p = CONTENT / "summaries" / subj / f"{aula}.json"
        cache[key] = {s["id"]: s for s in _jload(p).get("segments", [])} if p.exists() else {}
    s = cache[key].get(seg_id)
    if not s:
        return ""
    syn = s.get("synthetic") or []
    return (s.get("analytic") or "") + " " + (" ".join(syn) if isinstance(syn, list) else str(syn))


def _material_text(seg_ids: list[str]) -> dict[str, str]:
    """Texto do material por trecho, do cache local (pipeline/.cache/pages). Ausente → vazio."""
    out: dict[str, str] = {}
    try:
        sys.path.insert(0, str(ROOT / "pipeline"))
        from summary_source import source_text  # type: ignore
    except Exception:  # noqa: BLE001
        return out
    for sid in seg_ids:
        try:
            _, txt = source_text(sid)
            out[sid] = txt
        except BaseException:  # noqa: BLE001 - SystemExit quando falta cache
            continue
    return out


CACHE_DIR = ROOT / "pipeline" / ".cache" / "questoes"
CATALOG_VERSION = 1


def _catalog_fingerprint() -> str:
    """Muda quando o conteúdo que alimenta o índice muda (catálogo, trechos, edital, bizus, resumos,
    texto do material em cache)."""
    import hashlib

    h = hashlib.sha256(str(CATALOG_VERSION).encode())
    globs = [
        (CONTENT, "catalog.json"),
        (CONTENT / "segments", "*.json"),
        (CONTENT / "edital", "*.json"),
        (CONTENT / "items", "*/*.json"),
        (CONTENT / "summaries", "*/*.json"),
        (CONTENT / "complements", "*.md"),
        (ROOT / "pipeline" / ".cache" / "pages", "*.json"),
        (Path(__file__).resolve().parent, "classify.py"),  # mudança no tokenizador refaz o índice
    ]
    for base, pat in globs:
        for f in sorted(base.glob(pat)):
            st = f.stat()
            h.update(f"{f.relative_to(ROOT)}:{st.st_size}:{int(st.st_mtime)}".encode())
    return h.hexdigest()


def load_catalog(use_material: bool = True, cache: bool = True) -> Catalog:
    """Índice do classificador. Montá-lo leva alguns minutos (texto do material); por isso fica em
    pipeline/.cache/questoes/catalog.pkl e só é refeito quando o conteúdo muda."""
    import pickle

    if cache:
        fp = _catalog_fingerprint() + f":{use_material}"
        pk = CACHE_DIR / "catalog.pkl"
        if pk.exists():
            try:
                saved_fp, cat = pickle.loads(pk.read_bytes())
                if saved_fp == fp:
                    return cat
            except Exception:  # noqa: BLE001 - cache corrompido: refaz
                pass
        cat = _build_catalog(use_material)
        CACHE_DIR.mkdir(parents=True, exist_ok=True)
        pk.write_bytes(pickle.dumps((fp, cat)))
        return cat
    return _build_catalog(use_material)


def _build_catalog(use_material: bool = True) -> Catalog:
    cat = _jload(CONTENT / "catalog.json")
    aulas: dict[str, dict] = {}
    for s in cat["subjects"]:
        for a in s["aulas"]:
            aulas[a["id"]] = {
                "title": a.get("title", ""),
                "short": a.get("shortTitle", ""),
                "subject": s["id"],
                "selectable": a.get("selectable", True) and a.get("kind", "theory") == "theory",
                "segments": [],
            }
    segments: dict[str, SegInfo] = {}
    seg_topics: dict[str, str] = {}
    for f in sorted((CONTENT / "segments").glob("*.json")):
        d = _jload(f)
        for sg in d["segments"]:
            si = SegInfo(id=sg["id"], aula=sg["aula"], subject=d["subject"], order=sg.get("order", 0))
            segments[si.id] = si
            if sg["aula"] in aulas:
                aulas[sg["aula"]]["segments"].append(si.id)
            seg_topics[si.id] = " ".join(
                [sg.get("startTopic") or "", sg.get("endTopic") or "", " ".join(sg.get("topicsCovered") or [])]
            )
    edital_items: dict[str, dict] = {}
    for f in sorted((CONTENT / "edital").glob("*.json")):
        d = _jload(f)
        subj = d["subject"]
        for it in d["items"]:
            eid = f"{subj}/e{it['id']}"
            segs = [x for w in it.get("where", []) for x in w.get("segments", [])]
            auls = [w.get("aula") for w in it.get("where", []) if w.get("aula")]
            txt = (it.get("item") or it.get("title") or "") + " " + " ".join(w.get("topic", "") for w in it.get("where", []))
            edital_items[eid] = {"subject": subj, "title": (it.get("item") or it.get("title") or ""), "segments": segs, "aulas": auls, "text": txt}
            for sid in segs:
                if sid in segments:
                    segments[sid].edital.append((eid, txt))
    items_cache: dict = {}
    sum_cache: dict = {}
    material = _material_text(list(segments)) if use_material else {}
    for sid, si in segments.items():
        a = aulas.get(si.aula, {})
        doc: Counter = Counter()
        doc.update(features(a.get("title", "") + " " + a.get("short", ""), 3.0))
        doc.update(features(seg_topics.get(sid, ""), 3.0))
        for _, txt in si.edital:
            doc.update(features(txt, 2.5))
        strong, weak = _bizu_text(sid, items_cache)
        doc.update(features(strong, 1.5))
        doc.update(features(weak, 1.0))
        doc.update(features(_analytic(sid, sum_cache), 1.0))
        if sid in material:
            doc.update(features(material[sid], 0.6))
        si.doc = doc
    # idf por disciplina
    idf: dict[str, dict[str, float]] = {}
    by_subj: dict[str, list[SegInfo]] = defaultdict(list)
    for si in segments.values():
        by_subj[si.subject].append(si)
    for subj, segs in by_subj.items():
        df: Counter = Counter()
        for si in segs:
            df.update(set(si.doc))
        n = len(segs)
        idf[subj] = {t: math.log((n + 1) / (c + 0.5)) + 1.0 for t, c in df.items()}
    vec = {sid: _tfidf(si.doc, idf[si.subject]) for sid, si in segments.items()}
    aula_vec: dict[str, dict[str, float]] = {}
    for aid, a in aulas.items():
        acc: Counter = Counter()
        for sid in a["segments"]:
            acc.update(segments[sid].doc)
        if acc:
            aula_vec[aid] = _tfidf(acc, idf.get(a["subject"], {}))
    return Catalog(segments, aulas, edital_items, idf, vec, aula_vec)


def _tfidf(c: Counter, idf: dict[str, float]) -> dict[str, float]:
    v = {t: (1 + math.log(w)) * idf.get(t, 0.0) for t, w in c.items() if w > 0 and t in idf}
    n = math.sqrt(sum(x * x for x in v.values())) or 1.0
    return {t: x / n for t, x in v.items()}


def _cos(q: dict[str, float], d: dict[str, float]) -> float:
    if len(q) > len(d):
        q, d = d, q
    return sum(x * d.get(t, 0.0) for t, x in q.items())


# ───────────────────────── mapa curado ─────────────────────────


def load_map() -> dict:
    if MAP_PATH.exists():
        return _jload(MAP_PATH)
    return {"materias": {}, "assuntos": {}}


def load_overrides() -> dict:
    if OVERRIDES_PATH.exists():
        return _jload(OVERRIDES_PATH).get("questoes", {})
    return {}


def assunto_key(materia: str, assunto: str) -> str:
    return f"{materia}|{assunto}"


# ───────────────────────── classificação ─────────────────────────


@dataclass
class Result:
    subjectId: str | None
    aulaId: str | None
    segmentId: str | None
    editalItemId: str | None
    score: float
    confidence: str  # manual | alta | baixa
    status: str  # APPROVED | DRAFT | SKIP
    reason: str
    candidates: list[tuple[str, float]] = field(default_factory=list)


def question_text(q: dict) -> str:
    opts = " ".join(o.get("text", "") for o in q.get("options", []))
    return f"{q.get('statement', '')} {opts} {q.get('support', '')[:1500]}"


class Classifier:
    def __init__(self, catalog: Catalog | None = None, mapa: dict | None = None):
        self.cat = catalog or load_catalog()
        self.map = mapa or load_map()
        self._assunto_votes: dict[str, list[tuple[str, float]]] = {}
        self.overrides = load_overrides()

    def subject_for(self, materia: str, assunto: str) -> tuple[str | None, dict]:
        entry = self.map.get("assuntos", {}).get(assunto_key(materia, assunto), {})
        if entry.get("subject"):
            return entry["subject"], entry
        m = self.map.get("materias", {}).get(materia)
        if isinstance(m, dict):
            return m.get("subject"), {**m, **entry}
        return m, entry

    def qvec(self, q: dict, subject: str) -> dict[str, float]:
        c = features(q.get("assunto", ""), 3.0)
        c.update(features(question_text(q), 1.0))
        return _tfidf(c, self.cat.idf.get(subject, {}))

    def candidate_aulas(self, subject: str, entry: dict) -> list[str]:
        if entry.get("aulas"):
            return [a for a in entry["aulas"] if a in self.cat.aulas]
        return [aid for aid, a in self.cat.aulas.items() if a["subject"] == subject and a["selectable"] and a["segments"]]

    def vote_assuntos(self, questions: list[dict]) -> None:
        """Escolha automática de aula por assunto sem curadoria: soma das similaridades de todas as
        questões do assunto (mais o próprio nome do assunto, com peso)."""
        groups: dict[str, list[dict]] = defaultdict(list)
        for q in questions:
            groups[assunto_key(q["materia"], q["assunto"])].append(q)
        for key, qs in groups.items():
            materia, assunto = key.split("|", 1)
            subject, entry = self.subject_for(materia, assunto)
            if not subject or entry.get("aulas") or entry.get("segments") or entry.get("skip"):
                continue
            cands = self.candidate_aulas(subject, entry)
            tot: Counter = Counter()
            name_vec = _tfidf(features(assunto, 1.0), self.cat.idf.get(subject, {}))
            for aid in cands:
                av = self.cat.aula_vec.get(aid, {})
                tot[aid] += 2.0 * _cos(name_vec, av)
            for q in qs:
                v = self.qvec(q, subject)
                for aid in cands:
                    tot[aid] += _cos(v, self.cat.aula_vec.get(aid, {})) / len(qs)
            self._assunto_votes[key] = tot.most_common(5)

    def classify(self, q: dict) -> Result:
        materia, assunto = q.get("materia", ""), q.get("assunto", "")
        ov = self.overrides.get(str(q.get("tecId", "")))
        if ov:
            if ov.get("skip"):
                return Result(None, None, None, None, 0.0, "manual", "SKIP", str(ov["skip"]))
            sid = ov.get("segment")
            if sid in self.cat.segments:
                seg = self.cat.segments[sid]
                subj = seg.subject
                return Result(subj, seg.aula, sid, self.edital_item(sid, self.qvec(q, subj)), 1.0, "manual", "APPROVED", "decisão da auditoria (14/10/2026)")
        subject, entry = self.subject_for(materia, assunto)
        # curadoria por banca: AOCP segue o destino do CBMPE/PMPE; as demais bancas (ex.: Cebraspe, para o PCPE) vão para
        # o destino alternativo, porque cada questão só pode ficar em um trecho
        alt = entry.get("outras_bancas")
        if alt and q.get("banca") != "AOCP":
            entry = {**entry, **alt}
            subject = entry.get("subject", subject)
        if entry.get("skip"):
            return Result(subject, None, None, None, 0.0, "manual", "SKIP", str(entry["skip"]))
        if not subject:
            return Result(None, None, None, None, 0.0, "baixa", "SKIP", f"matéria sem mapa: {materia}")
        v = self.qvec(q, subject)
        manual = bool(entry.get("aulas") or entry.get("segments"))
        if entry.get("segments"):
            seg_cands = [s for s in entry["segments"] if s in self.cat.segments]
        else:
            aulas = self.candidate_aulas(subject, entry)
            if not manual:
                votes = self._assunto_votes.get(assunto_key(materia, assunto))
                if votes is None:
                    self.vote_assuntos([q])
                    votes = self._assunto_votes.get(assunto_key(materia, assunto), [])
                ranked = [a for a, _ in votes]
                aulas = ranked[:1] or aulas
            seg_cands = [s for a in aulas for s in self.cat.aulas[a]["segments"]]
        if not seg_cands:
            return Result(subject, None, None, None, 0.0, "baixa", "SKIP", "sem trechos candidatos")
        scored = sorted(((s, _cos(v, self.cat.vec.get(s, {}))) for s in seg_cands), key=lambda t: -t[1])
        best, score = scored[0]
        if score <= 0:
            # nenhuma palavra em comum: primeiro trecho da aula (ordem do material)
            best = min(seg_cands, key=lambda s: (self.cat.segments[s].aula, self.cat.segments[s].order))
        seg = self.cat.segments[best]
        if manual:
            conf, status, reason = "manual", "APPROVED", "assunto mapeado"
        else:
            votes = self._assunto_votes.get(assunto_key(materia, assunto), [])
            s1 = votes[0][1] if votes else 0.0
            s2 = votes[1][1] if len(votes) > 1 else 0.0
            ok = s1 >= AUTO_MIN_SCORE and (s2 <= 0 or s1 / s2 >= AUTO_MIN_RATIO)
            conf = "alta" if ok else "baixa"
            status = "APPROVED" if ok else "DRAFT"
            reason = f"automático (aula {s1:.2f} vs {s2:.2f})"
        if score < SEGMENT_MIN_BY_SUBJECT.get(subject, SEGMENT_MIN_SCORE) and status == "APPROVED":
            status, conf = "DRAFT", "baixa"
            reason = f"{reason} · trecho de baixa similaridade ({score:.2f})"
        if ov and ov.get("draft"):
            status, conf, reason = "DRAFT", "baixa", str(ov["draft"])
        return Result(
            subjectId=subject,
            aulaId=seg.aula,
            segmentId=best,
            editalItemId=self.edital_item(best, v),
            score=round(score, 4),
            confidence=conf,
            status=status,
            reason=reason,
            candidates=[(s, round(x, 4)) for s, x in scored[:3]],
        )

    def edital_item(self, seg_id: str, v: dict[str, float]) -> str | None:
        seg = self.cat.segments[seg_id]
        # só itens da própria disciplina: um item de Matemática pode apontar (relação cruzada) para um
        # trecho de Estatística, mas a questão continua sendo de Estatística (e o item, de outra disciplina,
        # nem existe para ela na página de questões)
        own = lambda eid: eid.split("/", 1)[0] == seg.subject  # noqa: E731
        items = [it for it in seg.edital if own(it[0])]
        if not items:
            items = [
                (eid, it["text"])
                for eid, it in self.cat.edital_items.items()
                if seg.aula in it["aulas"] and own(eid)
            ]
        if not items:
            return None
        if len(items) == 1:
            return items[0][0]
        idf = self.cat.idf.get(seg.subject, {})
        return max(items, key=lambda it: _cos(v, _tfidf(features(it[1], 1.0), idf)))[0]
