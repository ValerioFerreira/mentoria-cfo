"""Validador do conteúdo autoral (bizus e questões) em content/items/<disciplina>/<aula>.json.

Regras (falha = erro; aviso = revisar):
  esquema, 5 alternativas distintas, gabarito A–E, distribuição de gabarito equilibrada, sem duplicatas (no arquivo e
  entre arquivos da mesma disciplina), tópico e página obrigatórios, nº mínimo de questões pelo tamanho do trecho,
  bizu com 6–14 tópicos e 3–5 itens C/E (TEORIA e REVISAO, com certo e errado, sem repetir afirmação),
  pageRef dentro do trecho, padrões AOCP conhecidos e ORIGINALIDADE (sem trechos longos copiados do material).

Uso:  python pipeline/validate_content.py [content/items/.../a00.json ...]   (sem args: valida tudo)
      python pipeline/validate_content.py --coverage [--subject <disc>]    (trechos sem bizu/questões, por disciplina)
"""
from __future__ import annotations

import argparse
import collections
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from textutil import norm  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ITEMS_DIR = CONTENT_DIR / "items"
PATTERNS = {
    "correta", "incorreta", "assertivas", "lacuna", "caso", "lei-seca", "conceito", "calculo", "texto", "relacao", "excecao",
}
LETTERS = "ABCDE"
SHINGLE_N = 10  # nº de palavras de um trecho considerado "copiado"


def min_questions(pages: int) -> int:
    """Piso de questões por trecho (o alvo do briefing é maior; abaixo disto o caderno fica pobre)."""
    return 5 if pages < 6 else 8


def words(s: str) -> list[str]:
    return re.findall(r"\w+", s.lower())


def shingles(s: str, n: int = SHINGLE_N) -> set[tuple[str, ...]]:
    w = words(s)
    return {tuple(w[i : i + n]) for i in range(max(0, len(w) - n + 1))}


def jaccard(a: set, b: set) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def is_authored(aula_id: str) -> bool:
    return bool(re.search(r"/c\d+$", aula_id))


def load_source_shingles(aula_id: str) -> set[tuple[str, ...]] | None:
    try:
        from textutil import aula_key_map, load_pages
        key = aula_key_map().get(aula_id)
        if not key:
            return None
        data = load_pages(key)
        out: set[tuple[str, ...]] = set()
        for p in data["pages"]:
            out |= shingles(p["text"])
        return out
    except Exception:  # cache local ausente (ex.: CI): pula a checagem de originalidade
        return None


def load_segments(subject_id: str) -> dict[str, dict]:
    segs = json.loads((CONTENT_DIR / "segments" / f"{subject_id}.json").read_text(encoding="utf-8"))["segments"]
    return {s["id"]: s for s in segs}


def validate_file(path: Path, subject_seen: list | None = None) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warns: list[str] = []
    doc = json.loads(path.read_text(encoding="utf-8"))
    aula = doc.get("aula", "")
    subject_id = aula.split("/")[0]
    segs = load_segments(subject_id)
    authored = is_authored(aula)
    source = None if authored else load_source_shingles(aula)
    if source is None and not authored:
        warns.append("cache do texto-fonte ausente: originalidade NÃO verificada")
    if doc.get("status", "DRAFT") not in ("DRAFT", "APPROVED"):
        errors.append(f"status inválido: {doc.get('status')!r}")
    if not str(doc.get("batch", "")).strip():
        errors.append("batch ausente")

    stats = {"segments": 0, "questions": 0, "bizuItems": 0}
    seen_stmt: list[tuple[str, set]] = []
    seen_ce: set[str] = set()
    letters = collections.Counter()
    longest_hits = 0
    longest_where: list[str] = []
    n_q = 0
    seg_ids = [s.get("id") for s in doc.get("segments", [])]
    if len(seg_ids) != len(set(seg_ids)):
        errors.append("trecho repetido no arquivo")

    def check_text(where: str, text: str, allow_literal: bool = False) -> None:
        if source is None or allow_literal:
            return
        copied = shingles(text) & source
        if copied:
            sample = " ".join(next(iter(copied)))
            errors.append(f"{where}: trecho copiado do material ({len(copied)} sequências de {SHINGLE_N} palavras; ex.: “{sample}…”)")

    for seg in doc.get("segments", []):
        sid = seg.get("id", "?")
        stats["segments"] += 1
        if sid not in segs:
            errors.append(f"{sid}: segmento inexistente em content/segments")
            continue
        if segs[sid]["aula"] != aula:
            errors.append(f"{sid}: trecho de outra aula")
        lo, hi = segs[sid]["startPage"], segs[sid]["endPage"]

        bizu = seg.get("bizu")
        if not bizu:
            errors.append(f"{sid}: trecho sem bizu")
        else:
            summ = bizu.get("summary", [])
            if not 6 <= len(summ) <= 14:
                errors.append(f"{sid}: bizu.summary deve ter 6–14 tópicos (tem {len(summ)})")
            for i, b in enumerate(summ):
                if not str(b).strip():
                    errors.append(f"{sid}: bizu.summary[{i}] vazio")
                check_text(f"{sid} bizu.summary[{i}]", b)
            for kind in ("teoria", "revisao"):
                items = bizu.get(kind, [])
                if not 3 <= len(items) <= 5:
                    errors.append(f"{sid}: bizu.{kind} deve ter 3–5 itens (tem {len(items)})")
                if items and len({bool(i.get("isTrue")) for i in items}) < 2:
                    errors.append(f"{sid}: bizu.{kind} precisa ter itens certos E errados")
                for i, it in enumerate(items):
                    stats["bizuItems"] += 1
                    for f in ("statement", "explanation"):
                        if not str(it.get(f, "")).strip():
                            errors.append(f"{sid}: bizu.{kind}[{i}].{f} vazio")
                    if not isinstance(it.get("isTrue"), bool):
                        errors.append(f"{sid}: bizu.{kind}[{i}].isTrue deve ser booleano")
                    key = norm(it.get("statement", ""))
                    if key in seen_ce:
                        errors.append(f"{sid}: bizu.{kind}[{i}] repete outra afirmação C/E do arquivo")
                    seen_ce.add(key)
                    check_text(f"{sid} bizu.{kind}[{i}]", it.get("statement", "") + " " + it.get("explanation", ""))

        qs = seg.get("questions", [])
        if len(qs) < min_questions(segs[sid]["pages"]):
            errors.append(f"{sid}: só {len(qs)} questões (mínimo {min_questions(segs[sid]['pages'])} para {segs[sid]['pages']} págs.)")
        for qi, q in enumerate(qs):
            n_q += 1
            stats["questions"] += 1
            where = f"{sid} q{qi + 1}"
            opts = q.get("options", [])
            if len(opts) != 5 or any(not str(o).strip() for o in opts):
                errors.append(f"{where}: precisa de exatamente 5 alternativas não vazias")
                continue
            if len({norm(o) for o in opts}) != 5:
                errors.append(f"{where}: alternativas repetidas")
            ans = q.get("answer")
            if ans not in LETTERS:
                errors.append(f"{where}: gabarito inválido ({ans!r})")
                continue
            letters[ans] += 1
            if q.get("pattern") not in PATTERNS:
                errors.append(f"{where}: pattern desconhecido ({q.get('pattern')!r})")
            if q.get("difficulty") not in (1, 2, 3):
                errors.append(f"{where}: difficulty deve ser 1, 2 ou 3")
            if not str(q.get("topic", "")).strip():
                errors.append(f"{where}: topic ausente")
            stmt = str(q.get("statement", "")).strip()
            wc = len(words(stmt))
            if not 6 <= wc <= 220:
                warns.append(f"{where}: enunciado com {wc} palavras (fora de 6–220)")
            if len(str(q.get("explanation", "")).strip()) < 40:
                errors.append(f"{where}: explicação curta demais")
            pr = q.get("pageRef")
            if pr is None and not authored:
                errors.append(f"{where}: pageRef ausente")
            elif pr is not None and not (lo - 1 <= pr <= hi + 1):
                errors.append(f"{where}: pageRef {pr} fora do trecho {lo}–{hi}")
            for o in opts:
                if re.search(r"\b(todas as (anteriores|alternativas)|nenhuma das (anteriores|alternativas))\b", o, re.I):
                    warns.append(f"{where}: alternativa do tipo 'todas/nenhuma' (raro na AOCP)")
            # "literal": true = cita texto de norma (lei, súmula, CF: domínio público); a citação fica registrada e auditável
            allow = bool(q.get("literal"))
            if allow:
                stats["literal"] = stats.get("literal", 0) + 1
            # cada campo é checado separadamente (evita falsos positivos na fronteira enunciado/alternativa)
            for field_name, text in [("enunciado", stmt), *[(f"alt. {LETTERS[i]}", o) for i, o in enumerate(opts)], ("explicação", q.get("explanation", ""))]:
                check_text(f"{where} {field_name}", text, allow_literal=allow)
            if q.get("support"):
                check_text(f"{where} texto-base", q["support"], allow_literal=allow)
            # duplicatas (o enunciado + alternativas identificam a questão; enunciados genéricos iguais são comuns)
            body = stmt + " " + " ".join(opts)
            sh = shingles(body, 4)
            for other, osh in seen_stmt:
                if norm(body) == other or jaccard(sh, osh) > 0.8:
                    errors.append(f"{where}: questão duplicada/quase igual a outra do arquivo")
                    break
            seen_stmt.append((norm(body), sh))
            if subject_seen is not None:
                for ofile, oid, osh in subject_seen:
                    if ofile != path.name and jaccard(sh, osh) > 0.8:
                        errors.append(f"{where}: questão quase igual a {oid} ({ofile})")
                        break
                subject_seen.append((path.name, where, sh))
            lens = [len(o) for o in opts]
            if lens.index(max(lens)) == LETTERS.index(ans) and max(lens) > 1.3 * sorted(lens)[-2]:
                longest_hits += 1
                longest_where.append(f"{sid.split('/')[-1]}q{qi + 1}")

    if n_q >= 20:
        for L in LETTERS:
            share = letters[L] / n_q
            if share > 0.35 or share < 0.08:
                errors.append(f"distribuição do gabarito desequilibrada: {L}={share:.0%} (esperado ~20%)")
    if n_q >= 10 and longest_hits / n_q > 0.35:
        warns.append(f"em {longest_hits}/{n_q} questões a alternativa correta é muito mais longa que as demais (dica de gabarito): {', '.join(longest_where)}")
    stats["letters"] = dict(letters)
    return errors, warns, stats


def coverage(subject: str | None) -> int:
    """Trechos de aulas selecionáveis sem arquivo de itens / sem bizu / abaixo do mínimo de questões."""
    catalog = json.loads((CONTENT_DIR / "catalog.json").read_text(encoding="utf-8"))
    total = {"seg": 0, "ok": 0, "q": 0, "ce": 0, "bizu": 0}
    missing_all = 0
    for s in catalog["subjects"]:
        if subject and s["id"] != subject:
            continue
        segs = load_segments(s["id"])
        have: dict[str, dict] = {}
        for f in sorted((ITEMS_DIR / s["id"]).glob("*.json")) if (ITEMS_DIR / s["id"]).exists() else []:
            for seg in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
                have[seg["id"]] = seg
        selectable = {a["id"] for a in s["aulas"] if a["selectable"]}
        want = [g for g in segs.values() if g["aula"] in selectable]
        missing, thin = [], []
        q = ce = bz = 0
        for g in want:
            it = have.get(g["id"])
            if not it:
                missing.append(g["id"].split("/", 1)[1])
                continue
            nq = len(it.get("questions", []))
            q += nq
            if it.get("bizu"):
                bz += 1
                ce += len(it["bizu"].get("teoria", [])) + len(it["bizu"].get("revisao", []))
            if not it.get("bizu") or nq < min_questions(g["pages"]):
                thin.append(f"{g['id'].split('/', 1)[1]}({nq}q{'' if it.get('bizu') else ', sem bizu'})")
        stale = sorted(set(have) - set(segs))
        ok = len(want) - len(missing) - len(thin)
        total["seg"] += len(want)
        total["ok"] += ok
        total["q"] += q
        total["ce"] += ce
        total["bizu"] += bz
        missing_all += len(missing) + len(thin) + len(stale)
        print(f"{s['id']:24s} trechos {len(want):4d} · completos {ok:4d} · questões {q:5d} · bizus {bz:4d} · C/E {ce:5d}")
        if missing:
            print(f"   sem itens ({len(missing)}): {', '.join(missing[:60])}{' …' if len(missing) > 60 else ''}")
        if thin:
            print(f"   incompletos ({len(thin)}): {', '.join(thin[:40])}")
        if stale:
            print(f"   ITENS ÓRFÃOS (trecho não existe mais): {', '.join(stale)}")
    print(f"TOTAL trechos {total['seg']} · completos {total['ok']} · questões {total['q']} · bizus {total['bizu']} · C/E {total['ce']}")
    return 1 if missing_all else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--subject")
    ap.add_argument("--quiet", action="store_true", help="não lista avisos")
    args = ap.parse_args()
    if args.coverage:
        return coverage(args.subject)
    files = [Path(a) for a in args.files] or sorted(ITEMS_DIR.glob(f"{args.subject or '*'}/*.json"))
    bad = 0
    by_subject: dict[str, list] = collections.defaultdict(list)
    for f in files:
        subj = json.loads(f.read_text(encoding="utf-8")).get("aula", "").split("/")[0]
        errs, warns, st = validate_file(f, by_subject[subj])
        status = "FALHA" if errs else "ok"
        print(f"[{status}] {f.relative_to(CONTENT_DIR.parent) if f.is_absolute() else f}: {st['segments']} trechos, {st['questions']} questões, {st['bizuItems']} itens C/E, gabaritos {st['letters']}")
        for e in errs:
            print("   ERRO:", e)
        if not args.quiet:
            for w in warns:
                print("   aviso:", w)
        bad += bool(errs)
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
