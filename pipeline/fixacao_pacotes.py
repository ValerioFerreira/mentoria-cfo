"""Pacotes compactos para escrever os comentários das questões novas da Fixação, e o aplicador das respostas.

  python pipeline/fixacao_pacotes.py montar [volumes...]   # grava pipeline/.cache/material/pacotes/<disc>__mNN.md (só o pendente)
  python pipeline/fixacao_pacotes.py aplicar <arquivo.json> # aplica as respostas ao fixacao.json e valida o volume

Pacote: para cada questão sem comentário, o id, o capítulo (título e o "Para fixar"), o texto-base, o enunciado, as
alternativas e o gabarito oficial. Resposta: JSON {"volume": "<disc>/mNN", "comentarios": {"<id>": {"comentario": "...",
"alternativas": {"A": "...", ...}}}, "descartes": [{"id": "...", "motivo": "QUALIDADE: ..."}]}.
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from validate_material import MATERIAL_DIR, QUESTIONS_DIR, chapter_file, load_volume, parse_front_matter  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

OUT = QUESTIONS_DIR.parent / "pacotes"


def _fixar(path: Path) -> tuple[str, list[str]]:
    meta, body, _ = parse_front_matter(path.read_text(encoding="utf-8"))
    m = re.search(r"^###\s+Para fixar\s*$\n(.*?)(?=^##|\Z)", body, re.M | re.S)
    items = [re.sub(r"^\s*(?:[-*]|\d+[.)])\s+", "", ln).strip() for ln in (m.group(1).splitlines() if m else []) if ln.strip()]
    return meta.get("titulo", ""), items


def montar(vols: list[str]) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    if not vols:
        vols = [str(p.parent.relative_to(MATERIAL_DIR)).replace("\\", "/") for p in MATERIAL_DIR.glob("*/m*/fixacao.json")]
    for vid in sorted(vols):
        fx = json.loads((MATERIAL_DIR / vid / "fixacao.json").read_text(encoding="utf-8"))
        pend = [q for q in fx.get("questoes", []) if not str(q.get("comentario", "")).strip()]
        if not pend:
            continue
        cache = {q["id"]: q for q in json.loads((QUESTIONS_DIR / (vid.replace("/", "__") + ".json")).read_text(encoding="utf-8"))["questoes"]}
        vol = load_volume(vid)
        lines = [f"# Pacote {vid} · {len(pend)} questões a comentar", ""]
        caps_done = set()
        for q in pend:
            src = cache[q["id"]]
            t = q["capitulo"]
            if t not in caps_done:
                titulo, fixar = _fixar(chapter_file(MATERIAL_DIR / vid, t))
                lines += [f"## Capítulo {vol['trechos'].index(t) + 1} · {titulo} ({t})", "Para fixar do capítulo:"] + [f"- {x}" for x in fixar] + [""]
                caps_done.add(t)
            lines.append(f"### {q['id']} · {src['tipo']} · gabarito oficial: {src['gabarito']}")
            if src.get("textoBase"):
                lines.append(f"Texto-base: {src['textoBase']}")
            lines.append(f"Enunciado: {src['enunciado']}")
            for a in src.get("alternativas") or []:
                if src["tipo"] != "CERTO_ERRADO":
                    lines.append(f"{a['letra']}) {a['texto']}")
            lines.append("")
        (OUT / (vid.replace("/", "__") + ".md")).write_text("\n".join(lines), encoding="utf-8")
        print(f"{vid}: {len(pend)}")


def aplicar(path: Path) -> int:
    resp = json.loads(path.read_text(encoding="utf-8"))
    vid = resp["volume"]
    fx_path = MATERIAL_DIR / vid / "fixacao.json"
    fx = json.loads(fx_path.read_text(encoding="utf-8"))
    by = {q["id"]: q for q in fx["questoes"]}
    n = 0
    for qid, c in resp.get("comentarios", {}).items():
        if qid in by:
            by[qid]["comentario"] = c["comentario"].strip()
            by[qid]["alternativas"] = {k: v.strip() for k, v in (c.get("alternativas") or {}).items()}
            n += 1
    gone = {d["id"] for d in resp.get("descartes", [])}
    if gone:
        fx["questoes"] = [q for q in fx["questoes"] if q["id"] not in gone]
        fx.setdefault("descartes", []).extend(resp["descartes"])
    fx_path.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{vid}: {n} comentários aplicados, {len(gone)} descartadas")
    r = subprocess.run([sys.executable, str(Path(__file__).parent / "validate_material.py"), str(MATERIAL_DIR / vid)],
                       capture_output=True, text=True, encoding="utf-8")
    errs = [ln for ln in r.stdout.splitlines() if "ERRO" in ln and ("fixacao" in ln or any(q in ln for q in resp.get("comentarios", {})))]
    for ln in errs:
        print(ln)
    return 1 if errs else 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "montar":
        montar(sys.argv[2:])
        sys.exit(0)
    if len(sys.argv) == 3 and sys.argv[1] == "aplicar":
        sys.exit(aplicar(Path(sys.argv[2])))
    print(__doc__)
    sys.exit(2)
