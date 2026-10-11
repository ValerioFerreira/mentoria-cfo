"""Fila de produção dos resumos analíticos (ordem de prioridade definida pelo dono do produto).

Prioridade (definida pelo dono do produto): 1º os assuntos do EDITAL DO CFO CBMPE (Oficial); dentro dele, 2º os comuns a mais
concursos (os 4 primeiro) e 3º os de maior importância no CBMPE Oficial (questões esperadas). Depois vêm os assuntos que não
constam no CBMPE Oficial (só Soldado/PMPE), pela mesma lógica.
Sai em content/summaries/_queue.json, com o alvo de palavras de cada resumo analítico:
  alvo = minutos da atividade ÷ 3 de leitura (20 min para 1 h de teoria) × 100 palavras/min de estudo.

Uso:
  python pipeline/summary_queue.py                     # gera a fila
  python pipeline/summary_queue.py --pending [--top N] [--subject disc] # lista o que ainda não tem resumo
  python pipeline/summary_queue.py --batch N --subject disc           # N próximos trechos pendentes (JSON) de uma disciplina
  python pipeline/summary_queue.py --claim NOME --count N              # reserva AULAS inteiras (≥ N trechos pendentes) para um agente
  python pipeline/summary_queue.py --claims                            # mostra as reservas ativas
  python pipeline/summary_queue.py --release NOME                      # libera as reservas de um agente
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SUMMARIES_DIR = CONTENT_DIR / "summaries"
QUEUE = SUMMARIES_DIR / "_queue.json"
CLAIMS = SUMMARIES_DIR / "_claims.json"
PRIMARY = "CBMPE_OFICIAL"
WORDS_PER_MIN = 100  # leitura de estudo (material denso), não leitura corrida
MAX_READ_MIN = 20


def target_words(minutes: float, pages: int | None = None) -> int:
    """Alvo do resumo analítico: ≤ 20 min de leitura (minutos da atividade ÷ 3) e ≈ 150 palavras por página do trecho."""
    read = min(MAX_READ_MIN, max(5.0, minutes / 3))
    words = read * WORDS_PER_MIN
    if pages is not None:
        words = min(words, max(500, pages * 150))
    return int(round(words, -1))


def done_ids() -> set[str]:
    out: set[str] = set()
    for f in SUMMARIES_DIR.glob("*/*.json"):
        doc = json.loads(f.read_text(encoding="utf-8"))
        for s in doc.get("segments", []):
            if s.get("analytic"):
                out.add(s["id"])
    return out


def build() -> list[dict]:
    imp = json.loads((CONTENT_DIR / "importance" / "segments.json").read_text(encoding="utf-8"))
    contests = json.loads((CONTENT_DIR / "contests.json").read_text(encoding="utf-8"))
    rows = []
    seg_info: dict[str, dict] = {}
    for f in (CONTENT_DIR / "segments").glob("*.json"):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            seg_info[s["id"]] = s
    for sid, rec in imp["segments"].items():
        s = seg_info.get(sid)
        if not s:
            continue
        oficial = sum(
            c["expected"] / (contests[k]["totalQuestions"] or 1)
            for k, c in rec["contests"].items()
            if c["appears"] and (contests[k].get("category") == "Oficial")
        )
        prim = rec["contests"].get(PRIMARY, {})
        rows.append(
            {
                "id": sid,
                "inPrimary": bool(prim.get("appears")),
                "primaryExpected": prim.get("expected", 0.0),
                "aula": s["aula"],
                "subject": sid.split("/")[0],
                "pages": s["pages"],
                "minutes": s.get("minutes", 60),
                "targetWords": target_words(s.get("minutes", 60), s["pages"]),
                "shared": rec["shared"],
                "sharedShare": rec["sharedShare"],
                "oficialShare": round(oficial, 6),
                "order": s["order"],
            }
        )
    rows.sort(key=lambda r: (not r["inPrimary"], -r["shared"], -r["primaryExpected"], -r["sharedShare"], r["id"]))
    for i, r in enumerate(rows, 1):
        r["rank"] = i
    return rows


def load_claims() -> dict:
    return json.loads(CLAIMS.read_text(encoding="utf-8")) if CLAIMS.exists() else {}


def claim(name: str, count: int) -> list[dict]:
    """Reserva aulas inteiras (todos os trechos pendentes de cada uma) na ordem da fila, até somar `count` trechos."""
    rows = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
    done = done_ids()
    claims = load_claims()
    taken = {a for a, c in claims.items() if any(i not in done for i in c["ids"])}
    out: list[dict] = []
    seen: set[str] = set()
    for r in rows:
        if r["id"] in done or r["aula"] in taken or r["aula"] in seen:
            continue
        seen.add(r["aula"])
        pend = [x for x in rows if x["aula"] == r["aula"] and x["id"] not in done]
        out.extend(pend)
        claims[r["aula"]] = {"agent": name, "ids": [x["id"] for x in pend]}
        if len(out) >= count:
            break
    CLAIMS.write_text(json.dumps(claims, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pending", action="store_true")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--subject")
    ap.add_argument("--batch", type=int)
    ap.add_argument("--claim")
    ap.add_argument("--count", type=int, default=8)
    ap.add_argument("--claims", action="store_true")
    ap.add_argument("--release")
    args = ap.parse_args()
    if args.claims:
        done = done_ids()
        for a, c in load_claims().items():
            left = [i for i in c["ids"] if i not in done]
            print(f"{c['agent']:<14} {a:<34} {len(c['ids']) - len(left)}/{len(c['ids'])} feitos")
        return
    if args.release:
        cl = {a: c for a, c in load_claims().items() if c["agent"] != args.release}
        CLAIMS.write_text(json.dumps(cl, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"reservas de {args.release} liberadas")
        return
    if args.claim:
        print(json.dumps(claim(args.claim, args.count), ensure_ascii=False, indent=1))
        return
    if args.pending or args.batch:
        rows = json.loads(QUEUE.read_text(encoding="utf-8"))["queue"]
        done = done_ids()
        rows = [r for r in rows if r["id"] not in done and (not args.subject or r["subject"] == args.subject)]
        rows = rows[: args.batch or args.top]
        if args.batch:
            print(json.dumps(rows, ensure_ascii=False, indent=1))
        else:
            for r in rows:
                print(f"#{r['rank']:>4} {r['id']:<34} cbmpe={'S' if r['inPrimary'] else 'n'} shared={r['shared']} exp={r['primaryExpected']:.3f} ~{r['targetWords']}p")
            print(f"{len(rows)} listados")
        return
    rows = build()
    SUMMARIES_DIR.mkdir(parents=True, exist_ok=True)
    total = sum(r["targetWords"] for r in rows)
    QUEUE.write_text(json.dumps({"version": 1, "count": len(rows), "totalTargetWords": total, "queue": rows}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{len(rows)} trechos na fila ({total:,} palavras-alvo) -> {QUEUE}")
    by: dict[int, list[int]] = {}
    for r in rows:
        by.setdefault(r["shared"], []).append(r["targetWords"])
    for k in sorted(by, reverse=True):
        print(f"  em {k} concursos: {len(by[k])} trechos, {sum(by[k]):,} palavras")


if __name__ == "__main__":
    main()
