"""Leitura de um volume do material próprio: volume.md, capítulos, fixacao.json, cache de questões e metadados.

Reaproveita o parser do validador (parse_front_matter, chapter_file, load_volume) para ler o markdown do mesmo jeito.
"""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from config import CONTENT_DIR, load_subjects
from validate_material import MATERIAL_DIR, QUESTIONS_DIR, ROOT, chapter_file, load_metrics, load_volume, parse_front_matter

CONTESTS_TS = ROOT / "web" / "src" / "lib" / "contests.ts"
DESIGN_DIR = ROOT / "design" / "material" / "prontidao"
QIMG_DIR = ROOT / "pipeline" / ".cache" / "material" / "q-img"
OUT_DIR = ROOT / "material-pdf"
INDEX_JSON = MATERIAL_DIR / "index.json"
ALTA_SCORE = 67  # mesma régua do validador (tier ALTA)


class ContentError(Exception):
    """Erro no conteúdo ou nos dados de entrada (não no motor): vai para o relatório do revisor."""


@dataclass
class Chapter:
    trecho: str
    number: int
    title: str
    path: Path
    meta: dict
    body: str
    importance: int = 0
    tier: str = ""


@dataclass
class Question:
    id: str
    number: int
    chapter: str  # trecho
    kind: str  # MULTIPLA_ESCOLHA | CERTO_ERRADO
    origin: str
    base_text: str | None
    statement: str
    options: list[tuple[str, str]]
    answer: str
    comment: str
    option_comments: dict[str, str]
    has_figure: bool = False


@dataclass
class Volume:
    id: str
    subject: str
    subject_name: str
    number: int
    title: str
    subtitle: str
    wave: int
    contests: list[str]
    contest_labels: list[str]
    dir: Path
    intro: dict  # seções do volume.md
    chapters: list[Chapter] = field(default_factory=list)
    questions: list[Question] = field(default_factory=list)
    statuses: dict[str, str] = field(default_factory=dict)

    @property
    def label(self) -> str:
        return f"Volume {self.number:02d}"

    @property
    def approved(self) -> bool:
        return bool(self.statuses) and all(s == "APROVADO" for s in self.statuses.values())


def contest_labels() -> dict[str, str]:
    """Chave do concurso -> 'role · org' (de web/src/lib/contests.ts)."""
    src = CONTESTS_TS.read_text(encoding="utf-8")
    out = {}
    for m in re.finditer(r'key:\s*"([A-Z_]+)",\s*org:\s*"([A-Z]+)",\s*role:\s*"([^"]+)"', src):
        out[m.group(1)] = f"{m.group(3)} · {m.group(2)}"
    return out


def subject_names() -> dict[str, str]:
    return {s.id: s.name for s in load_subjects()}


def _sections(body: str) -> dict[str, str]:
    """'## Título' -> texto, na ordem do arquivo."""
    out: dict[str, str] = {}
    cur = None
    buf: list[str] = []
    for ln in body.splitlines():
        m = re.match(r"^##\s+(.+?)\s*$", ln)
        if m:
            if cur is not None:
                out[cur] = "\n".join(buf).strip()
            cur, buf = m.group(1), []
        elif cur is not None:
            buf.append(ln)
    if cur is not None:
        out[cur] = "\n".join(buf).strip()
    return out


def _origin(q: dict) -> str:
    parts = [p for p in (q.get("banca"), str(q.get("ano") or ""), q.get("orgao")) if p]
    if not parts:
        return "Inédita MentorIA"
    head = " ".join(parts[:2]) if len(parts) >= 2 else parts[0]
    return f"{head} · {parts[2]}" if len(parts) == 3 else head


def _norm_answer(ans: str, kind: str) -> str:
    a = str(ans).strip().upper()
    if kind == "CERTO_ERRADO":
        return {"C": "Certo", "CERTO": "Certo", "E": "Errado", "ERRADO": "Errado"}.get(a, a)
    return a


def load(volume_id: str) -> Volume:
    subject, mm = volume_id.split("/")
    vmeta = load_volume(volume_id)
    if not vmeta:
        raise ContentError(f"{volume_id}: não está em content/material/volumes/{subject}.json")
    vdir = MATERIAL_DIR / subject / mm
    if not vdir.is_dir():
        raise ContentError(f"{volume_id}: pasta {vdir} não existe")
    labels = contest_labels()
    statuses: dict[str, str] = {}

    intro_path = vdir / "volume.md"
    if not intro_path.exists():
        raise ContentError(f"{volume_id}: falta volume.md")
    imeta, ibody, ierr = parse_front_matter(intro_path.read_text(encoding="utf-8"))
    if ierr:
        raise ContentError(f"{intro_path}: {'; '.join(ierr)}")
    statuses["volume.md"] = imeta.get("status", "")

    vol = Volume(
        id=volume_id, subject=subject, subject_name=subject_names().get(subject, subject), number=int(vmeta["number"]),
        title=imeta.get("titulo") or vmeta["title"], subtitle=imeta.get("subtitulo", ""), wave=int(vmeta.get("wave", 0)),
        contests=list(vmeta.get("contests", [])), contest_labels=[labels.get(c, c) for c in vmeta.get("contests", [])],
        dir=vdir, intro=_sections(ibody), statuses=statuses,
    )

    metrics = load_metrics(subject)
    for n, trecho in enumerate(vmeta["trechos"], start=1):
        p = chapter_file(vdir, trecho)
        if not p.exists():
            raise ContentError(f"{volume_id}: falta o capítulo {p.name} ({trecho})")
        meta, body, err = parse_front_matter(p.read_text(encoding="utf-8"))
        if err:
            raise ContentError(f"{p}: {'; '.join(err)}")
        statuses[p.name] = meta.get("status", "")
        imp = metrics.get(trecho, {}).get("importance", {})
        vol.chapters.append(Chapter(trecho=trecho, number=n, title=meta.get("titulo", ""), path=p, meta=meta, body=body,
                                    importance=int(imp.get("score") or 0), tier=imp.get("tier", "")))

    fx_path = vdir / "fixacao.json"
    if not fx_path.exists():
        raise ContentError(f"{volume_id}: falta fixacao.json")
    fx = json.loads(fx_path.read_text(encoding="utf-8"))
    statuses["fixacao.json"] = fx.get("status", "")
    vol.questions = _questions(volume_id, fx, vol)
    return vol


def _questions(volume_id: str, fx: dict, vol: Volume) -> list[Question]:
    subject, mm = volume_id.split("/")
    cache_path = QUESTIONS_DIR / f"{subject}__{mm}.json"
    cache = {}
    if fx.get("questoes"):
        if not cache_path.exists():
            raise ContentError(f"{volume_id}: falta o cache de questões {cache_path.name}; rode (em web/) "
                               f"npx tsx scripts/material-questoes.ts --volume {volume_id}")
        cache = {q["id"]: q for q in json.loads(cache_path.read_text(encoding="utf-8"))["questoes"]}
    order = {c.trecho: c.number for c in vol.chapters}
    items: list[tuple[int, int, Question]] = []
    for i, q in enumerate(fx.get("questoes", [])):
        src = cache.get(q["id"])
        if not src:
            raise ContentError(f"{volume_id}: a questão {q['id']} do fixacao.json não está no cache {cache_path.name}")
        kind = src.get("tipo", "MULTIPLA_ESCOLHA")
        opts = [(a["letra"], a["texto"]) for a in (src.get("alternativas") or [])] if kind != "CERTO_ERRADO" else []
        items.append((order.get(q["capitulo"], 99), i, Question(
            id=q["id"], number=0, chapter=q["capitulo"], kind=kind, origin=_origin(src), base_text=src.get("textoBase"),
            statement=src.get("enunciado") or "", options=opts, answer=_norm_answer(q["gabarito"], kind),
            comment=q.get("comentario", ""), option_comments=q.get("alternativas") or {}, has_figure=bool(src.get("temFigura")))))
        if _norm_answer(src.get("gabarito", q["gabarito"]), kind) != _norm_answer(q["gabarito"], kind):
            raise ContentError(f"{volume_id}: gabarito de {q['id']} diverge entre fixacao.json ({q['gabarito']}) e o banco ({src.get('gabarito')})")
    for i, q in enumerate(fx.get("ineditas", []), start=len(items)):
        kind = q.get("tipo", "MULTIPLA_ESCOLHA")
        opts = sorted((q.get("alternativas_texto") or {}).items()) if kind != "CERTO_ERRADO" else []
        items.append((order.get(q["capitulo"], 99), i, Question(
            id=q["id"], number=0, chapter=q["capitulo"], kind=kind, origin="Inédita MentorIA", base_text=q.get("textoBase"),
            statement=q.get("enunciado", ""), options=opts, answer=_norm_answer(q["gabarito"], kind), comment=q.get("comentario", ""),
            option_comments=q.get("alternativas") or {})))
    items.sort(key=lambda t: (t[0], t[1]))
    out = []
    for n, (_, _, q) in enumerate(items, start=1):
        q.number = n
        out.append(q)
    return out


def volume_ids_for_wave(wave: int) -> list[str]:
    ids = []
    for f in sorted((MATERIAL_DIR / "volumes").glob("*.json")):
        for v in json.loads(f.read_text(encoding="utf-8"))["volumes"]:
            if int(v.get("wave", 0)) == wave:
                ids.append(v["id"])
    return ids


__all__ = ["ALTA_SCORE", "CONTENT_DIR", "Chapter", "ContentError", "DESIGN_DIR", "INDEX_JSON", "OUT_DIR", "QIMG_DIR", "Question",
           "Volume", "load", "volume_ids_for_wave"]
