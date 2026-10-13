"""Validador dos resumos (content/summaries/<disciplina>/<aula>.json).

Cada arquivo guarda, por trecho de teoria (= atividade de Teoria):
  "analytic":  resumo analítico em markdown, lido em ≤ 20 min no lugar da atividade (≈ 100 palavras/min de estudo)
  "synthetic": resumo sintético do Bizu: lista de linhas (pontos-chave + explicação breve, COM conteúdo)
Regras (erro = bloqueia; aviso = revisar): esquema e impressão digital do trecho; tamanho do analítico em relação ao alvo do
trecho (summary_queue.target_words); estrutura (≥ 3 seções "###"); sintético com 6–12 pontos e 110–320 palavras;
sem placeholders/frases genéricas; sem caractere de substituição; markdown íntegro; ORIGINALIDADE (nenhuma sequência de
10 palavras igual ao material-base; os complementos autorais cNN são isentos).

Uso:  python pipeline/validate_summaries.py [content/summaries/<disc>/aNN.json ...]   (sem args: valida tudo)
      python pipeline/validate_summaries.py --coverage [--subject <disc>]          (trechos sem resumo)
Formato do arquivo:
  {"aula": "<disc>/a05", "batch": "w1-<disc>", "status": "DRAFT",
   "segments": [{"id": "<disc>/a05/s01", "fingerprint": {"startPage": 3, "endPage": 17, "startTopic": "..."},
                 "analytic": "### Tema\\n...", "synthetic": ["**Ponto**: explicação", "..."]}]}
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402
from summary_queue import target_words  # noqa: E402
from summary_coverage import rate as coverage_rate  # noqa: E402
from validate_content import SHINGLE_N, is_authored, load_segments, load_source_shingles, words  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

SUMMARIES_DIR = CONTENT_DIR / "summaries"
FORBIDDEN = [
    "aspecto 1", "aspecto 2", "priorize a fixa", "lorem ipsum", "todo:", "tbd", "[inserir", "preencher", "a completar",
    "conforme o material", "de acordo com a aula", "segundo o professor", "no pdf", "estratégia concursos", "estrategia concursos",
    "nesta aula", "nessa aula", "nesta página", "visto na aula",
]
HEADING = re.compile(r"^#{2,4}\s+\S", re.M)
FIXAR = re.compile(r"^#{2,4}\s*Para fixar\s*$", re.M | re.I)
ITEM = re.compile(r"^\s*(?:[-*]|\d+[.)])\s+\S", re.M)
FIXAR_MIN, FIXAR_MAX = 5, 8
# Originalidade: uma coincidência de 10 palavras pode ser definição consagrada ou texto de lei (ninguém reescreve o art. 14 da CF);
# cópia de verdade vem em trechos longos. Trechos copiados de 10 a COPY_RUN_ERROR-1 palavras viram AVISO (conferir se é citação de
# norma/definição); a partir de COPY_RUN_ERROR palavras seguidas, ou COPY_TOTAL_ERROR palavras copiadas no total, é ERRO.
# Sequências quase só de números/siglas (progressões, tabelas, fórmulas) não contam: não há outro jeito de escrevê-las.
COPY_RUN_ERROR = 16
COPY_TOTAL_ERROR = 40


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", re.sub(r"[|*#>`_-]+", " ", text)))


def copied_runs(text: str, source: set) -> list[list[str]]:
    """Trechos de `text` copiados do material: sequências contínuas de palavras cobertas por alguma janela de SHINGLE_N igual à fonte."""
    w = words(text)
    covered = [False] * len(w)
    for i in range(len(w) - SHINGLE_N + 1):
        if tuple(w[i : i + SHINGLE_N]) in source:
            for j in range(i, i + SHINGLE_N):
                covered[j] = True
    runs: list[list[str]] = []
    cur: list[str] = []
    for word, c in zip(w, covered):
        if c:
            cur.append(word)
        elif cur:
            runs.append(cur)
            cur = []
    if cur:
        runs.append(cur)
    return runs


def is_trivial_run(run: list[str]) -> bool:
    """Sequência de números/símbolos curtos (progressão, tabela, fórmula) ou de palavras que quase só se repetem."""
    short = sum(1 for x in run if x.isdigit() or len(x) <= 2)
    return short / len(run) >= 0.5 or len(set(run)) / len(run) < 0.5


def check_fixar(sid: str, analytic: str, errors: list[str]) -> None:
    """`### Para fixar` fecha o analítico com 5 a 8 pontos em lista (parágrafo corrido não serve para revisão rápida)."""
    m = FIXAR.search(analytic)
    if not m:
        errors.append(f"{sid}: falta a seção final “### Para fixar”")
        return
    n = len(ITEM.findall(analytic[m.end():]))
    if not FIXAR_MIN <= n <= FIXAR_MAX:
        errors.append(f"{sid}: “Para fixar” com {n} itens em lista (use {FIXAR_MIN} a {FIXAR_MAX}, um por linha com “- ”)")


def check_markdown(where: str, text: str, errors: list[str]) -> None:
    if text.count("**") % 2:
        errors.append(f"{where}: negrito (**) não fechado")
    # cada tabela (linhas "|" consecutivas) é checada separadamente: colunas iguais e linha separadora
    tables: list[list[str]] = []
    cur: list[str] = []
    for ln in text.splitlines():
        if ln.strip().startswith("|"):
            cur.append(ln.strip())
        elif cur:
            tables.append(cur)
            cur = []
    if cur:
        tables.append(cur)
    for rows in tables:
        if len({r.count("|") for r in rows}) > 1:
            errors.append(f"{where}: tabela com número de colunas inconsistente")
        if not any(set(r.replace("|", "").replace(":", "").strip()) <= {"-", " "} and "-" in r for r in rows):
            errors.append(f"{where}: tabela sem linha separadora (| --- |)")


def validate_file(path: Path) -> tuple[list[str], list[str], dict]:
    errors: list[str] = []
    warns: list[str] = []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        return [f"JSON inválido: {e}"], warns, {}
    aula = doc.get("aula", "")
    subject = aula.split("/")[0]
    try:
        segs = load_segments(subject)
    except FileNotFoundError:
        return [f"disciplina desconhecida: {subject}"], warns, {}
    if doc.get("status", "DRAFT") not in ("DRAFT", "APPROVED"):
        errors.append(f"status inválido: {doc.get('status')!r}")
    if not str(doc.get("batch", "")).strip():
        errors.append("batch ausente")
    authored = is_authored(aula)
    source = None if authored else load_source_shingles(aula)
    if source is None and not authored:
        warns.append("cache do texto-fonte ausente: originalidade NÃO verificada")
    queue = {r["id"]: r for r in json.loads((SUMMARIES_DIR / "_queue.json").read_text(encoding="utf-8"))["queue"]} if (SUMMARIES_DIR / "_queue.json").exists() else {}
    stats = {"segments": 0, "words": 0}
    seen: set[str] = set()
    for seg in doc.get("segments", []):
        sid = seg.get("id", "?")
        stats["segments"] += 1
        if sid in seen:
            errors.append(f"{sid}: repetido no arquivo")
        seen.add(sid)
        ref = segs.get(sid)
        if not ref:
            errors.append(f"{sid}: segmento inexistente em content/segments")
            continue
        if ref["aula"] != aula:
            errors.append(f"{sid}: trecho de outra aula")
        fp = seg.get("fingerprint") or {}
        want = {"startPage": ref["startPage"], "endPage": ref["endPage"], "startTopic": ref.get("startTopic")}
        if fp != want:
            errors.append(f"{sid}: impressão digital diferente do trecho atual (esperado {want}, veio {fp}) — o trecho foi resegmentado?")

        analytic = seg.get("analytic")
        synthetic = seg.get("synthetic")
        if not isinstance(analytic, str) or not analytic.strip():
            errors.append(f"{sid}: analytic ausente")
            analytic = ""
        if not isinstance(synthetic, list) or not all(isinstance(x, str) and x.strip() for x in synthetic or []):
            errors.append(f"{sid}: synthetic deve ser uma lista de linhas de texto")
            synthetic = []

        # tamanho do analítico em relação ao alvo (≈ 20 min de leitura para 1 h de teoria)
        n = word_count(analytic)
        stats["words"] += n
        pages = ref["pages"]
        tgt = queue.get(sid, {}).get("targetWords") or target_words(ref.get("minutes", 60), pages)
        if analytic:
            # o tamanho é o que o conteúdo pedir: só há teto (≈ 20 min de leitura) e um piso mínimo contra resumos vazios
            floor = max(250, int(tgt * 0.2))
            if n > tgt * 1.25:
                errors.append(f"{sid}: analítico com {n} palavras, acima do teto de ≈ 20 min de leitura ({int(tgt * 1.25)})")
            elif n < floor:
                errors.append(f"{sid}: analítico com {n} palavras, abaixo do mínimo ({floor})")
            elif n < tgt * 0.45:
                warns.append(f"{sid}: analítico com {n} palavras (alvo {tgt}): confira se não faltou conteúdo")
            if len(HEADING.findall(analytic)) < 3 and pages >= 5:
                errors.append(f"{sid}: use ao menos 3 seções (### Título) no analítico")
            check_fixar(sid, analytic, errors)
        # sintético
        if synthetic:
            sn = sum(word_count(x) for x in synthetic)
            bullets = [x for x in synthetic if not x.lstrip().startswith("#")]
            if not 6 <= len(bullets) <= 12:
                errors.append(f"{sid}: sintético com {len(bullets)} pontos (use 6 a 12)")
            if sn < 110 or sn > 320:
                errors.append(f"{sid}: sintético com {sn} palavras (use 110 a 320)")
            if any(word_count(x) < 8 for x in bullets):
                warns.append(f"{sid}: ponto do sintético muito curto (sem explicação)")
        elif "synthetic" in seg:
            errors.append(f"{sid}: synthetic vazio")

        blob = analytic + "\n" + "\n".join(synthetic)
        low = blob.lower()
        for bad in FORBIDDEN:
            if bad in low:
                errors.append(f"{sid}: expressão proibida/genérica: “{bad}”")
        if "�" in blob or "�" in blob:
            errors.append(f"{sid}: caractere de substituição (�) — corrija a codificação")
        check_markdown(f"{sid} analítico", analytic, errors)
        check_markdown(f"{sid} sintético", "\n".join(synthetic), errors)
        # originalidade
        if source is not None:
            runs = [r for r in copied_runs(blob, source) if not is_trivial_run(r)]
            total = sum(len(r) for r in runs)
            for r in runs:
                where = f"“{' '.join(r[:14])}{'…' if len(r) > 14 else ''}” ({len(r)} palavras)"
                if len(r) >= COPY_RUN_ERROR:
                    errors.append(f"{sid}: trecho copiado do material: {where}")
                elif total < COPY_TOTAL_ERROR:
                    warns.append(f"{sid}: coincidência com o material, confira se é citação de norma/definição: {where}")
            if runs and total >= COPY_TOTAL_ERROR and all(len(r) < COPY_RUN_ERROR for r in runs):
                errors.append(f"{sid}: {len(runs)} trechos curtos copiados do material somam {total} palavras (limite {COPY_TOTAL_ERROR})")
        # cobertura: triagem (só aviso; nota e veredito em summary_coverage.py)
        if analytic and synthetic:
            cov = coverage_rate({"analytic": analytic, "synthetic": synthetic}, ref, n / tgt if tgt else None)
            if cov:
                stats["coverage"] = cov["score"]
                if cov["verdict"] != "OK":
                    warns.append(
                        f"{sid}: cobertura {cov['verdict']} (nota {cov['score']:.2f}; mais pesados que faltam: {', '.join(cov['missing'][:8])})"
                    )
    return errors, warns, stats


def coverage(subject: str | None) -> int:
    queue = json.loads((SUMMARIES_DIR / "_queue.json").read_text(encoding="utf-8"))["queue"]
    done: set[str] = set()
    for f in SUMMARIES_DIR.glob("*/*.json"):
        for s in json.loads(f.read_text(encoding="utf-8")).get("segments", []):
            if s.get("analytic") and s.get("synthetic"):
                done.add(s["id"])
    by: dict[str, list[int]] = {}
    for r in queue:
        if subject and r["subject"] != subject:
            continue
        d = by.setdefault(r["subject"], [0, 0])
        d[1] += 1
        d[0] += r["id"] in done
    tot = [0, 0]
    for k, (a, b) in sorted(by.items()):
        print(f"  {k:<26} {a:>4}/{b:<4}")
        tot[0] += a
        tot[1] += b
    print(f"TOTAL {tot[0]}/{tot[1]} trechos com resumo")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--coverage", action="store_true")
    ap.add_argument("--subject")
    args = ap.parse_args()
    if args.coverage:
        return coverage(args.subject)
    files = [Path(f) for f in args.files] or sorted(p for p in SUMMARIES_DIR.glob("*/*.json"))
    bad = 0
    total_words = 0
    for f in files:
        errs, warns, stats = validate_file(f)
        total_words += stats.get("words", 0)
        tag = "ERRO" if errs else "ok"
        print(f"[{tag}] {f.as_posix()} — {stats.get('segments', 0)} trechos, {stats.get('words', 0)} palavras")
        for e in errs:
            print(f"   ✗ {e}")
        for w in warns:
            print(f"   ! {w}")
        bad += bool(errs)
    print(f"{len(files)} arquivos, {bad} com erro, {total_words:,} palavras de resumo analítico")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
