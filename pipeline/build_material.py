"""Gera os PDFs do material próprio MentorIA (modelo A · Prontidão). Briefing: pipeline/briefs/material-pdf.md.

Uso:
  python pipeline/build_material.py --only direito-penal-militar/m01 [--carimbo-exemplo] [--html]
  python pipeline/build_material.py --onda 1               # todos os volumes APROVADOS da onda, um processo por volume
  python pipeline/build_material.py --onda 1 --conferir    # só as conferências, sem regerar

Saída: material-pdf/<disc>/mNN.pdf (fora do git), content/material/index.json e material-pdf/_conferencia.md.
O PDF sai sem carimbo; a faixa do titular (index.json -> faixaTitular) fica vazia para o carimbo no download.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, os.path.dirname(__file__))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from material_pdf.assemble import band_rect_pt, build_html  # noqa: E402
from material_pdf.load import INDEX_JSON, OUT_DIR, ROOT, ContentError, load, volume_ids_for_wave  # noqa: E402
from material_pdf.postprocess import check, finish, sha256  # noqa: E402
from material_pdf.printpdf import EngineError, print_pdf  # noqa: E402

META_DIR = OUT_DIR / "_meta"
REPORT = OUT_DIR / "_conferencia.md"


def pdf_path(vid: str) -> Path:
    d, m = vid.split("/")
    return OUT_DIR / d / f"{m}.pdf"


def meta_path(vid: str) -> Path:
    return META_DIR / (vid.replace("/", "__") + ".json")


def build_one(vid: str, sample_stamp: bool, keep_html: bool) -> dict:
    t0 = time.time()
    v = load(vid)
    if not v.approved:
        pend = {k: s for k, s in v.statuses.items() if s != "APROVADO"}
        return {"volume": vid, "status": "PULADO", "motivo": f"não aprovado: {pend}"}
    html_, info = build_html(v)
    out = pdf_path(vid)
    html_file = META_DIR / (vid.replace("/", "__") + ".html")
    html_file.parent.mkdir(parents=True, exist_ok=True)
    html_file.write_text(html_, encoding="utf-8")
    try:
        pages = print_pdf(html_file, out)
    finally:
        if not keep_html:
            html_file.unlink(missing_ok=True)
    pm, errors, warns = finish(out, v, info, pages, sample_stamp)
    meta = {"volume": vid, "info": info, "pages": pm, "carimboExemplo": sample_stamp}
    meta_path(vid).write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    return {"volume": vid, "status": "ERRO" if errors else "OK", "paginas": pm["total"], "segundos": round(time.time() - t0, 1),
            "atualizadoEm": "-".join(reversed(info["updated"].split("/"))),
            "titulo": v.title, "numero": v.number, "disciplina": v.subject_name,
            "mb": round(out.stat().st_size / 2**20, 2), "erros": errors, "avisos": warns, "pm": pm, "carimboExemplo": sample_stamp}


def update_index(results: list[dict]) -> None:
    idx = json.loads(INDEX_JSON.read_text(encoding="utf-8")) if INDEX_JSON.exists() else {"versao": 1, "volumes": {}}
    idx["versao"] = 1
    idx["geradoEm"] = dt.datetime.now().astimezone().isoformat(timespec="seconds")
    idx["modelo"] = "A · Prontidão"
    idx["faixaTitular"] = band_rect_pt()
    idx["faixaTitularOrigem"] = "pontos PDF, origem no canto superior esquerdo da página A4 (595,28 × 841,89); vale para todas as páginas menos a capa"
    for r in results:
        if r.get("status") not in ("OK", "ERRO") or r.get("carimboExemplo"):
            continue  # amostra com carimbo de exemplo não entra no índice
        pdf = pdf_path(r["volume"])
        pm = r["pm"]
        idx["volumes"][r["volume"]] = {
            "titulo": r.get("titulo"), "numero": r.get("numero"), "disciplina": r.get("disciplina"),
            "arquivo": pdf.relative_to(ROOT).as_posix(), "paginas": pm["total"], "sha256": sha256(pdf), "bytes": pdf.stat().st_size,
            "capitulos": pm["capitulos"], "fixacao": {"pagina": pm.get("questoes")},
            "mapa": {"pagina": pm.get("mapa")}, "atualizadoEm": r.get("atualizadoEm"), "conferencia": r["status"],
        }
    idx["volumes"] = dict(sorted(idx["volumes"].items()))
    INDEX_JSON.write_text(json.dumps(idx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    # espelho para o app (o build da web lê de web/content)
    mirror = ROOT / "web" / "content" / "material" / "index.json"
    mirror.parent.mkdir(parents=True, exist_ok=True)
    mirror.write_text(INDEX_JSON.read_text(encoding="utf-8"), encoding="utf-8")


def write_report(results: list[dict]) -> None:
    lines = [f"# Conferência dos PDFs do material próprio — {dt.datetime.now():%d/%m/%Y %H:%M}", "",
             "| Volume | Situação | Páginas | MB | Tempo (s) | Erros | Avisos |", "|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r['volume']} | {r['status']} | {r.get('paginas', '')} | {r.get('mb', '')} | {r.get('segundos', '')} | "
                     f"{len(r.get('erros', []))} | {len(r.get('avisos', []))} |")
    for r in results:
        if r.get("erros") or r.get("avisos") or r.get("motivo"):
            lines += ["", f"## {r['volume']}"]
            if r.get("motivo"):
                lines.append(f"- {r['motivo']}")
            lines += [f"- ERRO: {e}" for e in r.get("erros", [])] + [f"- AVISO: {w}" for w in r.get("avisos", [])]
        if r.get("pm"):
            caps = r["pm"]["capitulos"]
            if caps:
                lines += ["", f"<details><summary>{r['volume']}: páginas por capítulo</summary>", ""]
                lines += [f"- {t}: págs. {c['pagina']} a {c['ate']}" for t, c in caps.items()]
                lines += ["", "</details>"]
    OUT_DIR.mkdir(exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_child(vid: str, args) -> dict:
    cmd = [sys.executable, __file__, "--only", vid, "--json"] + (["--carimbo-exemplo"] if args.carimbo_exemplo else [])
    env = dict(os.environ, PYTHONIOENCODING="utf-8")
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", env=env)
    try:
        return json.loads(p.stdout.strip().splitlines()[-1])
    except (json.JSONDecodeError, IndexError):
        return {"volume": vid, "status": "FALHA", "motivo": (p.stderr or p.stdout).strip().splitlines()[-1:] or ["sem saída"]}


def conferir(vids: list[str]) -> list[dict]:
    out = []
    for vid in vids:
        mp, pdf = meta_path(vid), pdf_path(vid)
        if not (mp.exists() and pdf.exists()):
            out.append({"volume": vid, "status": "SEM PDF"})
            continue
        meta = json.loads(mp.read_text(encoding="utf-8"))
        v = load(vid)
        errs, warns = check(pdf, v, meta["info"], meta["pages"], meta.get("carimboExemplo", False))
        out.append({"volume": vid, "status": "ERRO" if errs else "OK", "paginas": meta["pages"]["total"],
                    "titulo": v.title, "numero": v.number, "disciplina": v.subject_name,
                    "atualizadoEm": "-".join(reversed(meta["info"].get("updated", "").split("/"))) or None,
                    "mb": round(pdf.stat().st_size / 2**20, 2), "erros": errs, "avisos": warns, "pm": meta["pages"],
                    "carimboExemplo": meta.get("carimboExemplo", False)})
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="+", metavar="DISC/mNN")
    ap.add_argument("--onda", type=int)
    ap.add_argument("--conferir", action="store_true", help="só as conferências dos PDFs existentes")
    ap.add_argument("--carimbo-exemplo", action="store_true", help="escreve um carimbo fictício na faixa (provas visuais)")
    ap.add_argument("--mascote", choices=["chama", "foco"], help="versão do mascote nas páginas claras (padrão: foco)")
    ap.add_argument("--html", action="store_true", help="guarda o HTML em material-pdf/_meta para depurar")
    ap.add_argument("--json", action="store_true", help=argparse.SUPPRESS)
    args = ap.parse_args()
    if args.mascote:
        os.environ["MASCOTE"] = args.mascote  # vale também para os processos-filhos do lote
    vids = args.only or (volume_ids_for_wave(args.onda) if args.onda else [])
    if not vids:
        ap.error("informe --only ou --onda")

    if args.conferir:
        results = conferir(vids)
    elif args.json and len(vids) == 1:  # processo-filho do lote
        try:
            r = build_one(vids[0], args.carimbo_exemplo, args.html)
        except ContentError as e:
            r = {"volume": vids[0], "status": "ERRO DE CONTEÚDO", "motivo": str(e)}
        except EngineError as e:
            r = {"volume": vids[0], "status": "FALHA DO MOTOR", "motivo": str(e)}
        print(json.dumps(r, ensure_ascii=False))
        return 0
    elif len(vids) == 1:
        try:
            results = [build_one(vids[0], args.carimbo_exemplo, args.html)]
        except (ContentError, EngineError) as e:
            results = [{"volume": vids[0], "status": type(e).__name__, "motivo": str(e)}]
    else:
        results = []
        for vid in vids:
            r = run_child(vid, args)
            print(f"{vid}: {r['status']} {r.get('paginas', '')} págs. {r.get('segundos', '')} s", flush=True)
            results.append(r)

    update_index(results)
    write_report(results)
    print(f"\n{'Volume':<42} {'Situação':<18} {'Págs':>5} {'Tempo':>6} {'Avisos':>6}")
    for r in results:
        print(f"{r['volume']:<42} {r['status']:<18} {str(r.get('paginas', '')):>5} {str(r.get('segundos', '')):>6} {len(r.get('avisos', [])):>6}")
        for e in r.get("erros", []):
            print(f"   ERRO {e}")
        if r.get("motivo"):
            print(f"   {r['motivo']}")
    print(f"\nRelatório: {REPORT}")
    return 1 if any(r["status"] not in ("OK", "PULADO") for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
