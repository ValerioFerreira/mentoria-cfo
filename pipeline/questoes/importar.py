"""Importa os cadernos do TecConcursos de docs/questoes para o banco do site.

    pipeline/.venv/Scripts/python pipeline/questoes/importar.py            # cadernos novos -> banco local
    pipeline/.venv/Scripts/python pipeline/questoes/importar.py --remoto   # idem + banco de produção (Neon)

Opções:
    --remoto             também grava no banco remoto (web/.env.remote: REMOTE_DATABASE_URL=...)
    --so-remoto          grava só no remoto (o local já está em dia)
    --reclassificar      reenvia o acervo inteiro já extraído (após mudar o mapa de assuntos, o catálogo
                         ou a segmentação); não relê os PDFs
    --forcar             reextrai todos os PDFs (mesmo os já conhecidos)
    --so-extrair         extrai e classifica, gera o relatório, mas não grava em banco nenhum
    --limpar-estrategia  apaga do(s) banco(s) toda questão que não veio dos cadernos (id fora de tec_*)
    --pasta DIR          pasta dos cadernos (padrão: docs/questoes)

Especificação completa: pipeline/questoes/EXTRACAO.md (copiada para docs/questoes/COMO-EXTRAIR-QUESTOES.md).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from questoes.classify import Classifier, assunto_key, load_catalog, load_map  # noqa: E402
from questoes.tec_pdf import EXTRACTOR_VERSION, content_hash, read_caderno  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DOC_SRC = Path(__file__).resolve().parent / "EXTRACAO.md"
WEB = ROOT / "web"


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


class Store:
    """docs/questoes/.importadas.json (manifesto) + docs/questoes/.extraidas/ (acervo extraído)."""

    def __init__(self, folder: Path):
        self.folder = folder
        self.manifest_path = folder / ".importadas.json"
        self.dir = folder / ".extraidas"
        self.img_dir = self.dir / "img"
        self.dir.mkdir(exist_ok=True)
        self.img_dir.mkdir(exist_ok=True)
        if self.manifest_path.exists():
            self.manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        else:
            self.manifest = {"_comment": "Cadernos já extraídos (chave = sha256 do PDF). Não editar à mão.", "cadernos": {}}

    def save(self) -> None:
        self.manifest_path.write_text(json.dumps(self.manifest, ensure_ascii=False, indent=1), encoding="utf-8")

    def entry(self, sha: str) -> dict | None:
        return self.manifest["cadernos"].get(sha)

    def data_path(self, sha: str) -> Path:
        return self.dir / f"{sha}.json"


def extract(pdf: Path, sha: str, store: Store) -> dict:
    c = read_caderno(pdf)
    for a in c.assets.values():
        out = store.img_dir / f"{a.sha}.png"
        if not out.exists():
            out.write_bytes(a.data)
    qs = []
    for q in c.questions:
        d = dict(q.__dict__)
        d["contentHash"] = content_hash(q)
        d["images"] = {s: [c.assets[s].width, c.assets[s].height] for s in q.assets}
        qs.append(d)
    data = {
        "arquivo": pdf.name,
        "sha256": sha,
        "titulo": c.title,
        "paginas": c.pages,
        "extrator": EXTRACTOR_VERSION,
        "extraidoEm": now_iso(),
        "anomalias": c.anomalies,
        "questoes": qs,
    }
    store.data_path(sha).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return data


def load_all(store: Store) -> list[dict]:
    """Todos os cadernos extraídos, do mais antigo para o mais recente (o mais recente vence na dedup)."""
    out = []
    for sha, e in store.manifest["cadernos"].items():
        p = store.data_path(sha)
        if p.exists():
            d = json.loads(p.read_text(encoding="utf-8"))
            d["_ordem"] = e.get("extraidoEm", "")
            out.append(d)
    out.sort(key=lambda d: d["_ordem"])
    return out


def build_rows(acervo: dict[str, dict], cls: dict[str, object], batch: str) -> tuple[list[dict], set[str]]:
    rows: list[dict] = []
    imgs: set[str] = set()
    for tec_id, q in acervo.items():
        r = cls.get(tec_id)
        qid = f"tec_{tec_id}"
        if q["anulada"] or r is None or r.status == "SKIP":
            rows.append({"type": "retire", "id": qid})
            continue
        opts = [{"label": o["label"], "text": o["text"], "isCorrect": o["label"] == q["answer"]} for o in q["options"]]
        note = r.reason
        if r.status == "DRAFT" and r.candidates:
            note += " · candidatos: " + ", ".join(f"{s} ({x})" for s, x in r.candidates)
        rows.append(
            {
                "type": "question",
                "id": qid,
                "externalId": tec_id,
                "subjectId": r.subjectId,
                "aulaId": r.aulaId,
                "segmentId": r.segmentId,
                "editalItemId": r.editalItemId,
                "topic": q["assunto"] or None,
                "support": q["support"] or None,
                "statement": q["statement"],
                "explanation": "",
                "difficulty": 2,
                "pattern": q["banca"] or "AOCP",
                "status": r.status,
                "batch": batch,
                "banca": q["banca"] or "AOCP",
                "kind": q["kind"],
                "tecMateria": q["materia"],
                "tecAssunto": q["assunto"],
                "orgao": q["orgao"] or None,
                "cargo": q["cargo"] or None,
                "ano": q["ano"],
                "sourceFile": q["_arquivo"],
                "contentHash": q["contentHash"],
                "classifyScore": r.score,
                "classifyNote": note,
                "options": opts,
            }
        )
        imgs.update(q.get("images", {}).keys())
    return rows, imgs


def write_lote(store: Store, rows: list[dict], imgs: set[str], acervo_imgs: dict[str, list[int]], tag: str) -> Path:
    lotes = store.dir / "lotes"
    lotes.mkdir(exist_ok=True)
    p = lotes / f"{datetime.now():%Y%m%d-%H%M%S}-{tag}.jsonl"
    with p.open("w", encoding="utf-8") as f:
        for s in sorted(imgs):
            w, h = acervo_imgs[s]
            f.write(json.dumps({"type": "image", "id": s, "path": f"../img/{s}.png", "width": w, "height": h}) + "\n")
        for r in rows:
            # rede de segurança: o Postgres recusa NUL em texto
            f.write(json.dumps(r, ensure_ascii=False).replace("\\u0000", "") + "\n")
    return p


def run_sync(lote: Path | None, remote: bool, purge: bool) -> dict:
    cmd = ["npx", "tsx", "scripts/questoes-sync.ts"]
    if lote is not None:
        cmd.append(str(lote))
    if remote:
        cmd.append("--remoto")
    if purge:
        cmd.append("--limpar-estrategia")
    proc = subprocess.run(cmd, cwd=WEB, capture_output=True, text=True, encoding="utf-8", shell=sys.platform == "win32")
    if proc.returncode != 0:
        raise SystemExit(f"falha ao gravar no banco {'remoto' if remote else 'local'}:\n{proc.stdout}\n{proc.stderr}")
    last = [ln for ln in proc.stdout.strip().splitlines() if ln.startswith("{")]
    return json.loads(last[-1]) if last else {}


def report(path: Path, ctx: dict) -> None:
    L = []
    L.append(f"# Importação de questões — {ctx['quando']}\n")
    L.append(f"Extrator {EXTRACTOR_VERSION}. Especificação: `COMO-EXTRAIR-QUESTOES.md`.\n")
    L.append("## Cadernos processados agora\n")
    if ctx["novos"]:
        L.append("| Caderno | Questões | Anuladas | Quarentena | Anomalias |")
        L.append("|---|---:|---:|---:|---|")
        for d in ctx["novos"]:
            qs = d["questoes"]
            L.append(
                f"| {d['arquivo']} | {len(qs)} | {sum(q['anulada'] for q in qs)} | "
                f"{sum(1 for q in qs if q['problems'])} | {'; '.join(d['anomalias']) or '—'} |"
            )
    else:
        L.append("Nenhum caderno novo.")
    L.append("\n## Acervo\n")
    a = ctx["acervo_stats"]
    L.append(f"- Questões únicas extraídas: **{a['unicas']}** (de {a['total']} em {a['cadernos']} cadernos)")
    L.append(f"- Anuladas (descartadas): {a['anuladas']}")
    L.append(f"- Quarentena (extração com problema, não importadas): {a['quarentena']}")
    L.append(f"- Fora do edital / sem disciplina (não importadas): {a['skip']}")
    L.append(f"- Aprovadas: **{a['APPROVED']}** · Rascunho (revisar em /admin/revisao): **{a['DRAFT']}**\n")
    L.append("### Por disciplina\n")
    L.append("| Disciplina | Aprovadas | Rascunho |")
    L.append("|---|---:|---:|")
    for subj, c in sorted(ctx["por_disc"].items()):
        L.append(f"| {subj} | {c['APPROVED']} | {c['DRAFT']} |")
    if ctx["sem_mapa"]:
        L.append("\n## Assuntos sem curadoria (classificação automática)\n")
        L.append("Inclua-os em `content/questoes/mapa-assuntos.json` e rode `importar.py --reclassificar`.\n")
        L.append("| Matéria | Assunto | Questões | Situação | Sugestão |")
        L.append("|---|---|---:|---|---|")
        for (m, s), (n, st, sug) in sorted(ctx["sem_mapa"].items()):
            L.append(f"| {m} | {s or '(vazio)'} | {n} | {st} | {sug} |")
    if ctx["skips"]:
        L.append("\n## Não importadas por classificação\n")
        L.append("| Motivo | Matéria | Assunto | Questões |")
        L.append("|---|---|---|---:|")
        for (motivo, m, s), n in sorted(ctx["skips"].items(), key=lambda t: -t[1]):
            L.append(f"| {motivo} | {m} | {s or '(vazio)'} | {n} |")
    if ctx["quarentena"]:
        L.append("\n## Quarentena\n")
        for q in ctx["quarentena"][:300]:
            L.append(f"- {q['tecId']} (nº {q['numero']}, {q['_arquivo']}, pág. {q['page']}): {'; '.join(q['problems'])}")
    if ctx["sync"]:
        L.append("\n## Gravação\n")
        for s in ctx["sync"]:
            L.append(f"- `{json.dumps(s, ensure_ascii=False)}`")
    path.write_text("\n".join(L) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--remoto", action="store_true")
    ap.add_argument("--so-remoto", action="store_true")
    ap.add_argument("--reclassificar", action="store_true")
    ap.add_argument("--forcar", action="store_true")
    ap.add_argument("--so-extrair", action="store_true")
    ap.add_argument("--limpar-estrategia", action="store_true")
    ap.add_argument("--pasta", default=str(ROOT / "docs" / "questoes"))
    args = ap.parse_args()

    folder = Path(args.pasta)
    if not folder.exists():
        raise SystemExit(f"pasta não encontrada: {folder}")
    if DOC_SRC.exists():
        shutil.copyfile(DOC_SRC, folder / "COMO-EXTRAIR-QUESTOES.md")
    store = Store(folder)
    t0 = time.time()

    # 1. extração dos PDFs novos (ou de versão antiga do extrator)
    novos: list[dict] = []
    for pdf in sorted(folder.glob("*.pdf"), key=lambda p: p.stat().st_mtime):
        sha = sha256_file(pdf)
        e = store.entry(sha)
        if e and not args.forcar and e.get("extrator") == EXTRACTOR_VERSION and store.data_path(sha).exists():
            if e.get("arquivo") != pdf.name:
                e.setdefault("outrosNomes", [])
                if pdf.name not in e["outrosNomes"]:
                    e["outrosNomes"].append(pdf.name)
            continue
        print(f"extraindo {pdf.name} …", flush=True)
        d = extract(pdf, sha, store)
        novos.append(d)
        old = e or {}
        store.manifest["cadernos"][sha] = {
            "arquivo": pdf.name,
            "extraidoEm": d["extraidoEm"],
            "extrator": EXTRACTOR_VERSION,
            "questoes": len(d["questoes"]),
            # reextração muda o conteúdo: precisa regravar nos bancos
            "local": None,
            "remoto": None,
            **({"outrosNomes": old["outrosNomes"]} if old.get("outrosNomes") else {}),
        }
        store.save()

    # 2. acervo deduplicado (versão mais recente de cada questão)
    cadernos = load_all(store)
    acervo: dict[str, dict] = {}
    origem: dict[str, str] = {}
    total = 0
    imgs_dims: dict[str, list[int]] = {}
    for d in cadernos:
        for q in d["questoes"]:
            total += 1
            q["_arquivo"] = d["arquivo"]
            acervo[q["tecId"]] = q
            origem[q["tecId"]] = d["sha256"]
            imgs_dims.update(q.get("images", {}))
    quarentena = [q for q in acervo.values() if q["problems"]]
    valid = {k: q for k, q in acervo.items() if not q["problems"]}
    print(f"acervo: {len(acervo)} questões únicas ({total} no total) · quarentena {len(quarentena)}", flush=True)

    # 3. classificação
    print("carregando índice do classificador …", flush=True)
    cat = load_catalog()
    mapa = load_map()
    clf = Classifier(cat, mapa)
    clf.vote_assuntos([q for q in valid.values() if not q["anulada"]])
    cls = {k: clf.classify(q) for k, q in valid.items() if not q["anulada"]}

    stats = Counter()
    por_disc: dict[str, Counter] = defaultdict(Counter)
    skips: Counter = Counter()
    sem_mapa: dict[tuple[str, str], tuple[int, str, str]] = {}
    known = set(mapa.get("assuntos", {}))
    for k, q in valid.items():
        if q["anulada"]:
            stats["anuladas"] += 1
            continue
        r = cls[k]
        if r.status == "SKIP":
            stats["skip"] += 1
            skips[(r.reason, q["materia"], q["assunto"])] += 1
            continue
        stats[r.status] += 1
        por_disc[r.subjectId][r.status] += 1
        key = assunto_key(q["materia"], q["assunto"])
        if key not in known:
            n, st, sug = sem_mapa.get((q["materia"], q["assunto"]), (0, "", ""))
            sugs = clf._assunto_votes.get(key, [])
            sug = ", ".join(f"{a} ({s:.2f})" for a, s in sugs[:3])
            sem_mapa[(q["materia"], q["assunto"])] = (n + 1, r.status, sug)

    # 4. gravação
    sync_results: list[dict] = []
    targets: list[str] = []
    if not args.so_extrair:
        if not args.so_remoto:
            targets.append("local")
        if args.remoto or args.so_remoto:
            targets.append("remoto")
    batch = f"tec-{datetime.now():%Y%m%d}"
    for target in targets:
        if args.reclassificar or args.forcar:
            ids = set(acervo)
        else:
            pend = {sha for sha, e in store.manifest["cadernos"].items() if not e.get(target)}
            ids = {k for k, sha in origem.items() if sha in pend}
        sub = {k: acervo[k] for k in ids if k in acervo and not acervo[k]["problems"]}
        if not sub and not args.limpar_estrategia:
            print(f"{target}: nada a gravar", flush=True)
            continue
        rows, imgs = build_rows(sub, cls, batch)
        lote = write_lote(store, rows, imgs, imgs_dims, target) if rows else None
        print(f"{target}: gravando {sum(r['type'] == 'question' for r in rows)} questões e {len(imgs)} figuras …", flush=True)
        res = run_sync(lote, target == "remoto", args.limpar_estrategia)
        sync_results.append(res)
        print(f"{target}: {json.dumps(res, ensure_ascii=False)}", flush=True)
        stamp = now_iso()
        for sha in {origem[k] for k in ids if k in origem}:
            store.manifest["cadernos"][sha][target] = stamp
        store.save()

    # 5. relatório
    rel_dir = folder / "relatorios"
    rel_dir.mkdir(exist_ok=True)
    rel = rel_dir / f"{datetime.now():%Y-%m-%d-%H%M}.md"
    report(
        rel,
        {
            "quando": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "novos": novos,
            "acervo_stats": {
                "unicas": len(acervo),
                "total": total,
                "cadernos": len(cadernos),
                "anuladas": stats["anuladas"],
                "quarentena": len(quarentena),
                "skip": stats["skip"],
                "APPROVED": stats["APPROVED"],
                "DRAFT": stats["DRAFT"],
            },
            "por_disc": por_disc,
            "skips": skips,
            "sem_mapa": sem_mapa,
            "quarentena": quarentena,
            "sync": sync_results,
        },
    )
    print(
        f"pronto em {time.time() - t0:.0f}s · aprovadas {stats['APPROVED']} · rascunho {stats['DRAFT']} · "
        f"fora do edital {stats['skip']} · anuladas {stats['anuladas']} · quarentena {len(quarentena)}\n"
        f"relatório: {rel}",
        flush=True,
    )


if __name__ == "__main__":
    main()
