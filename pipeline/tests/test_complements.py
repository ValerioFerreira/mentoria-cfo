"""Materiais complementares do MentorIA (content/complements): integridade e originalidade."""
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

CONTENT = ROOT / "content"
SRC = CONTENT / "complements"
PDF_DIR = ROOT / "web" / "public" / "complementos"
PAGES_CACHE = ROOT / "pipeline" / ".cache" / "pages"


def _meta(path: Path) -> dict[str, str]:
    m = re.match(r"^---\n(.*?)\n---\n", path.read_text(encoding="utf-8").replace("\r\n", "\n"), re.S)
    assert m, f"{path.name}: front matter ausente"
    out = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            out[k.strip()] = v.strip().strip('"')
    return out


FILES = sorted(SRC.glob("*.md"))


@pytest.fixture(scope="module")
def catalog():
    return json.loads((CONTENT / "catalog.json").read_text(encoding="utf-8"))


def test_there_are_complements():
    assert len(FILES) >= 11


@pytest.mark.parametrize("path", FILES, ids=lambda p: p.stem)
def test_front_matter_pdf_and_catalog(path, catalog):
    meta = _meta(path)
    for key in ("id", "subject", "title", "short", "subtitle", "weight", "order"):
        assert meta.get(key), f"{path.name}: falta '{key}'"
    assert meta["id"] == path.stem
    subj = next((s for s in catalog["subjects"] if s["id"] == meta["subject"]), None)
    assert subj, f"disciplina inexistente: {meta['subject']}"
    aula = next((a for a in subj["aulas"] if a.get("source") == "authored" and a["id"] == f"{meta['subject']}/c{int(meta['order']):02d}"), None)
    assert aula, f"{path.name}: aula authored ausente no catálogo (rode build_complements.py)"
    assert aula["materialPath"] == f"complementos/{meta['id']}.pdf"
    pdf = PDF_DIR / f"{meta['id']}.pdf"
    assert pdf.exists() and pdf.stat().st_size > 5_000, f"PDF ausente: {pdf.name}"
    segs = json.loads((CONTENT / "segments" / f"{meta['subject']}.json").read_text(encoding="utf-8"))["segments"]
    mine = sorted((s for s in segs if s["aula"] == aula["id"]), key=lambda s: s["order"])
    assert mine, "sem segmentos"
    assert mine[0]["startPage"] == 1 and mine[-1]["endPage"] == aula["theoryPages"]
    for a, b in zip(mine, mine[1:]):
        assert b["startPage"] in (a["endPage"], a["endPage"] + 1)
    assert all(1 <= s["pages"] <= 17 for s in mine)


def test_resolved_gaps_reference_existing_gaps():
    gaps = {g["id"]: g for g in json.loads((CONTENT / "gaps.json").read_text(encoding="utf-8"))["gaps"]}
    for path in FILES:
        for gid in [x.strip() for x in _meta(path).get("resolves", "").split(",") if x.strip()]:
            assert gid in gaps, f"{path.name} resolve lacuna inexistente: {gid}"
            assert gaps[gid].get("resolved") is True


def test_subject_incidence_sum_is_preserved(catalog):
    for subj in catalog["subjects"]:
        if not any(a.get("source") == "authored" for a in subj["aulas"]):
            continue
        base = sum(a.get("incidenceBase", a["incidence"]) for a in subj["aulas"] if a.get("selectable") and a.get("source") != "authored")
        total = sum(a["incidence"] for a in subj["aulas"] if a.get("selectable"))
        assert abs(total - base) < 0.005, (subj["id"], total, base)


def _words(s: str) -> list[str]:
    return re.findall(r"\w+", s.lower())


def _shingles(ws: list[str], n: int = 10) -> set[tuple[str, ...]]:
    return {tuple(ws[i : i + n]) for i in range(len(ws) - n + 1)}


@pytest.mark.skipif(not PAGES_CACHE.exists(), reason="cache do Estratégia ausente (docs/ não versionado)")
def test_no_ten_word_sequence_copied_from_estrategia():
    """Texto autoral: nenhuma sequência de 10 palavras igual ao material do Estratégia (a norma citada literalmente é permitida)."""
    import unicodedata

    def norm(t: str) -> list[str]:
        t = unicodedata.normalize("NFKD", t.replace("ﬁ", "fi"))
        return _words("".join(c for c in t if not unicodedata.combining(c)))

    by_subject: dict[str, set] = {}
    for f in PAGES_CACHE.glob("*.json"):
        d = json.loads(f.read_text(encoding="utf-8"))
        text = " ".join(p["text"] for p in d["pages"])
        by_subject.setdefault(d["subject"], set()).update(_shingles(norm(text)))
    problems = []
    for path in FILES:
        meta = _meta(path)
        body = path.read_text(encoding="utf-8").replace("\r\n", "\n")
        body = re.sub(r"^---\n.*?\n---\n", "", body, flags=re.S)
        hits = _shingles(norm(body)) & by_subject.get(meta["subject"], set())
        if len(hits) > 12:  # tolerância: nomes de leis e fórmulas curtas coincidem
            problems.append((path.name, len(hits), " ".join(next(iter(hits)))))
    assert not problems, problems
