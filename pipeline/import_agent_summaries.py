"""Importa os resumos devolvidos pelos colaboradores externos (pastas `resumos_<AGENTE>_<ini>-<fim>/` com arquivos `Sxxxx__AGENTE.md`).

Para cada arquivo: lê o cabeçalho, confere o ID no índice (resumos-colaboradores/indice.json), converte para o formato interno e
grava em content/summaries/<disciplina>/<aula>.json, guardando o AGENTE em cada trecho (auditoria). Cada resumo é validado
isoladamente com validate_summaries.py: o que falhar vai para resumos-colaboradores/rejeitados/ (com os motivos) e NÃO é importado.
Depois sorteia N resumos por agente (padrão 5) para a análise amostral e gera resumos-colaboradores/amostras/<AGENTE>.md.

Uso:  python pipeline/import_agent_summaries.py <pasta> [--dry-run] [--sample 5] [--overwrite] [--relatorio arquivo.md]
  (--relatorio lista todos os rejeitados com os motivos e os válidos com cobertura baixa; combine com --dry-run para ver antes de gravar)
  <pasta>: uma pasta de agente ou a pasta-mãe com várias (busca recursiva). Depois: python pipeline/apply_synthetic.py e o seed.
"""
from __future__ import annotations

import argparse
import json
import os
import random
import re
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR, ROOT  # noqa: E402
from validate_summaries import validate_file, word_count  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

COLAB = ROOT / "resumos-colaboradores"
NAME = re.compile(r"^(S\d{4})__([A-Za-z0-9_-]+)\.md$")


def parse(text: str) -> tuple[dict, dict]:
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.S)
    if not m:
        return {}, {}
    head = {}
    for ln in m.group(1).splitlines():
        if ":" in ln:
            k, v = ln.split(":", 1)
            head[k.strip()] = v.strip()
    parts = re.split(r"^# (ANALÍTICO|SINTÉTICO|NOTAS)\s*$", m.group(2), flags=re.M)
    return head, {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}


def validate_segment(aula: str, seg: dict) -> tuple[list[str], list[str]]:
    """Valida UM trecho isoladamente (monta um arquivo temporário só com ele)."""
    doc = {"aula": aula, "batch": "importacao", "status": "DRAFT", "segments": [seg]}
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "t.json"
        f.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")
        errors, warns, _stats = validate_file(f)
    return errors, warns


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--sample", type=int, default=5)
    ap.add_argument("--overwrite", action="store_true")
    ap.add_argument("--relatorio", help="grava em markdown TODOS os rejeitados (com os motivos) e os válidos com cobertura baixa")
    args = ap.parse_args()

    index = {r["id"]: r for r in json.loads((COLAB / "indice.json").read_text(encoding="utf-8"))["rows"]}
    seg_info: dict[str, dict] = {}
    for f in (CONTENT_DIR / "segments").glob("*.json"):
        for s in json.loads(f.read_text(encoding="utf-8"))["segments"]:
            seg_info[s["id"]] = s

    files = sorted(p for p in Path(args.folder).rglob("*.md") if NAME.match(p.name))
    ok_by_agent: dict[str, list[dict]] = {}
    rejected: list[tuple[str, str, list[str]]] = []
    to_review: list[tuple[str, str, str]] = []  # válidos, mas com cobertura baixa: ler antes de aprovar (summary_coverage.py)
    skipped = 0
    by_file: dict[Path, dict] = {}
    touched: set[Path] = set()
    for p in files:
        sid, agent = NAME.match(p.name).groups()  # type: ignore[union-attr]
        problems: list[str] = []
        try:
            head, sec = parse(p.read_text(encoding="utf-8"))
        except UnicodeDecodeError:
            rejected.append((p.name, agent, ["arquivo não está em UTF-8"]))
            continue
        row = index.get(sid)
        if not row:
            rejected.append((p.name, agent, [f"ID {sid} não existe no índice"]))
            continue
        if head.get("trecho") != row["trecho"]:
            problems.append(f"trecho do cabeçalho ({head.get('trecho')}) difere do índice ({row['trecho']})")
        if head.get("agente") != agent:
            problems.append("agente do cabeçalho difere do nome do arquivo")
        for s in ("ANALÍTICO", "SINTÉTICO", "NOTAS"):
            if not sec.get(s):
                problems.append(f"seção '# {s}' ausente ou vazia")
        if problems:
            rejected.append((p.name, agent, problems))
            continue
        info = seg_info[row["trecho"]]
        bullets = [re.sub(r"^\s*[-*]\s+", "", ln).strip() for ln in sec["SINTÉTICO"].splitlines() if ln.strip()]
        seg = {
            "id": row["trecho"],
            "fingerprint": {"startPage": info["startPage"], "endPage": info["endPage"], "startTopic": info.get("startTopic")},
            "analytic": sec["ANALÍTICO"],
            "synthetic": bullets,
            "agent": agent,
            "sourceFile": p.name,
            **({} if sec["NOTAS"].strip().lower() in ("nenhuma", "nenhum", "-") else {"notes": sec["NOTAS"]}),
        }
        errs, warns = validate_segment(row["aula"], seg)
        if errs:
            rejected.append((p.name, agent, errs))
            continue
        flagged = [w for w in warns if "cobertura REFAÇÃO" in w or "cobertura REVISAR" in w]
        if flagged:
            to_review.append((sid, agent, flagged[0].split(": ", 1)[1]))
        ok_by_agent.setdefault(agent, []).append({**seg, "_aula": row["aula"], "_row": row})

    # grava
    written = 0
    for agent, segs in ok_by_agent.items():
        for seg in segs:
            aula = seg["_aula"]
            target = CONTENT_DIR / "summaries" / aula.split("/")[0] / f"{aula.split('/')[1]}.json"
            doc = by_file.get(target)
            if doc is None:
                doc = json.loads(target.read_text(encoding="utf-8")) if target.exists() else {"aula": aula, "batch": f"externo-{agent}", "status": "DRAFT", "segments": []}
                by_file[target] = doc
            clean = {k: v for k, v in seg.items() if not k.startswith("_")}
            existing = next((s for s in doc["segments"] if s["id"] == clean["id"]), None)
            if existing and not args.overwrite:
                skipped += 1
                continue
            if existing:
                doc["segments"].remove(existing)
            doc["segments"].append(clean)
            doc["segments"].sort(key=lambda s: s["id"])
            touched.add(target)
            written += 1
    if not args.dry_run:
        for target, doc in by_file.items():
            if target not in touched:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        if rejected:
            (COLAB / "rejeitados").mkdir(exist_ok=True)
            (COLAB / "rejeitados" / "rejeitados.md").write_text(
                "# Resumos rejeitados na importação\n\n" + "\n".join(f"## {n} ({a})\n" + "\n".join(f"- {e}" for e in errs) + "\n" for n, a, errs in rejected),
                encoding="utf-8",
            )
        log = COLAB / "importados.json"
        prev = json.loads(log.read_text(encoding="utf-8")) if log.exists() else {}
        for agent, segs in ok_by_agent.items():
            for s in segs:
                prev[s["_row"]["id"]] = {"agente": agent, "trecho": s["id"], "arquivo": s["sourceFile"]}
        log.write_text(json.dumps(prev, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

        # amostragem: N resumos por agente (sorteio reprodutível por agente)
        (COLAB / "amostras").mkdir(exist_ok=True)
        for agent, segs in ok_by_agent.items():
            rng = random.Random(agent)
            pick = rng.sample(segs, min(args.sample, len(segs)))
            lines = [f"# Amostra de qualidade — {agent}", f"{len(segs)} resumos importados; {len(pick)} sorteados. Conferir cada um contra o PDF indicado.", ""]
            for s in sorted(pick, key=lambda x: x["_row"]["id"]):
                r = s["_row"]
                lines += [
                    f"## {r['id']} · {r['subjectName']} · {r['aulaLabel']}",
                    f"Trecho `{s['id']}` · PDF: {r['pdf']} · págs. {r['startPage']}–{r['endPage']} · analítico: {word_count(s['analytic'])} palavras (teto {r['targetWords']}) · sintético: {len(s['synthetic'])} pontos",
                    "",
                    "**Analítico (início):**",
                    s["analytic"][:1500] + ("…" if len(s["analytic"]) > 1500 else ""),
                    "",
                    "**Sintético:**",
                    *[f"- {b}" for b in s["synthetic"]],
                    "",
                    f"**Notas do agente:** {s.get('notes', 'nenhuma')}",
                    "",
                    "Critérios: [ ] cobertura  [ ] correção  [ ] originalidade  [ ] clareza  [ ] tamanho/formato",
                    "",
                ]
            (COLAB / "amostras" / f"{agent}.md").write_text("\n".join(lines), encoding="utf-8")

    if args.relatorio:
        out = ["# Relatório da importação", "", f"## Rejeitados ({len(rejected)})", ""]
        out += [f"- {n} ({a}): " + " | ".join(errs) for n, a, errs in rejected]
        out += ["", f"## Válidos com cobertura baixa ({len(to_review)})", ""]
        out += [f"- {sid} ({a}): {why}" for sid, a, why in to_review]
        Path(args.relatorio).write_text("\n".join(out) + "\n", encoding="utf-8")

    tot_ok = sum(len(v) for v in ok_by_agent.values())
    print(f"{len(files)} arquivos lidos: {tot_ok} válidos ({written} gravados, {skipped} já existiam), {len(rejected)} rejeitados" + (" [dry-run]" if args.dry_run else ""))
    for agent, segs in sorted(ok_by_agent.items()):
        print(f"  {agent}: {len(segs)} resumos válidos")
    for n, a, errs in rejected[:20]:
        print(f"  ✗ {n} ({a}): {errs[0]}")
    if to_review:
        print(f"  ! {len(to_review)} válidos com cobertura baixa (REVISAR/REFAÇÃO), ler contra a fonte antes de aprovar:")
        for sid, a, why in to_review[:20]:
            print(f"    {sid} ({a}): {why[:140]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
