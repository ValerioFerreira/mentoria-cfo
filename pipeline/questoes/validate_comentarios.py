"""Validador dos comentários das questões (content/questoes/comentarios/<disciplina>/<lote>.json).

    pipeline/.venv/Scripts/python pipeline/questoes/validate_comentarios.py [arquivo.json | pasta ...]   (sem args: tudo)
    ... --amostra N --saida content/questoes/comentarios/amostras/lote-01.md  arquivos...   (sorteia N para leitura do dono)

ERRO (bloqueia a publicação):
  - esquema: lote, comentarios[] com id, contentHash, gabarito, comentario e alternativas; descartes[] com id e motivo;
  - a questão tem de existir no acervo dos cadernos (docs/questoes/.extraidas) com o MESMO contentHash e gabarito;
  - múltipla escolha: uma nota para cada letra da questão, cada uma começando por "Correta:" ou "Errada:", e "Correta:"
    só na letra do gabarito; Certo/Errado: alternativas = {};
  - tamanhos: comentário de 50 a 250 palavras; nota de 6 a 70;
  - termos proibidos (professor, nome do provedor, "gabarito oficial diz"…), remissão ao material ("capítulo", "volume",
    "na página N"), nome de banca ou direcionamento a concurso (mesmas regras do material: validate_material.check_comment);
  - artigo citado que não existe na norma em cache (pipeline/check_citations.py);
  - comentário igual (mesmas 20 primeiras palavras) em duas questões;
  - originalidade contra o material-base do trecho (mesma régua dos resumos: 16 palavras seguidas ou 40 no total).
AVISO: frase de modelo repetida em 3+ comentários do arquivo; coincidência de 10 a 15 palavras com o material-base
(definição ou texto de lei: conferir); artigo citado revogado.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from check_citations import check as check_cites  # noqa: E402
from questoes.importar import Store, load_all  # noqa: E402
from validate_content import load_source_shingles, words  # noqa: E402
from validate_material import check_comment  # noqa: E402
from validate_summaries import COPY_RUN_ERROR, COPY_TOTAL_ERROR, copied_runs, is_trivial_run  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

COMMENTS = ROOT / "content" / "questoes" / "comentarios"
NOTE_START = re.compile(r"^(Correta|Errada):\s+\S")
REMETE = re.compile(
    r"\bcap[ií]tulos?\b|\b(?:neste|deste|nesse|desse|no|do)\s+(?:volume|material)\b|\bmapa mental\b|\bcomo vimos\b"
    r"|\bvimos\b|\bestudamos\b|\bnesta seção\b|\bresumo analítico\b|\bapostila\b",
    re.IGNORECASE,
)
EXTRA_FORBIDDEN = ("tec concursos", "tecconcursos", "qconcursos", "comentário do professor", "nosso curso")


def wc(s: str) -> int:
    return len(re.findall(r"\w+", s))


_ACERVO: dict[str, dict] | None = None


def acervo() -> dict[str, dict]:
    global _ACERVO
    if _ACERVO is None:
        _ACERVO = {}
        for d in load_all(Store(ROOT / "docs" / "questoes")):
            for q in d["questoes"]:
                _ACERVO[q["tecId"]] = q
    return _ACERVO


_SHINGLES: dict[str, set | None] = {}


def source_shingles(trecho: str | None) -> set | None:
    if not trecho or trecho.count("/") != 2:
        return None
    aula = trecho.rsplit("/", 1)[0]
    if re.search(r"/a1\d\d$", aula):  # complementos autorais: não há material-base
        return None
    if aula not in _SHINGLES:
        _SHINGLES[aula] = load_source_shingles(aula)
    return _SHINGLES[aula]


def citations(text: str) -> tuple[int, list[str]]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        bad = check_cites("", text, False)
    rows = [ln.strip() for ln in buf.getvalue().splitlines() if ln.strip().startswith(("INEXISTENTE", "REVOGADO"))]
    return bad, rows


def validate_file(path: Path) -> tuple[list[str], list[str], int]:
    errors: list[str] = []
    warns: list[str] = []
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"JSON inválido: {e}"], [], 0
    if not isinstance(doc, dict) or not isinstance(doc.get("comentarios"), list):
        return ["o arquivo deve ser um objeto com 'comentarios' (lista)"], [], 0
    rel = path.relative_to(COMMENTS).as_posix() if COMMENTS in path.parents else path.name
    if not doc.get("lote"):
        errors.append("falta 'lote'")
    file_trecho = doc.get("trecho")
    autor_fixacao = doc.get("autor") == "fixacao"
    acv = acervo()
    starts: dict[str, list[str]] = {}
    sents: dict[str, set[str]] = {}
    seen: set[str] = set()
    for c in doc["comentarios"]:
        qid = str(c.get("id", "?"))
        if qid in seen:
            errors.append(f"{qid}: repetida no arquivo")
        seen.add(qid)
        missing = [k for k in ("id", "contentHash", "gabarito", "comentario", "alternativas") if k not in c]
        if missing or not isinstance(c.get("alternativas"), dict):
            errors.append(f"{qid}: faltam campos {missing or ['alternativas (objeto)']}")
            continue
        src = acv.get(qid.removeprefix("tec_")) if qid.startswith("tec_") else None
        if qid.startswith("tec_") and not src:
            errors.append(f"{qid}: não está no acervo dos cadernos")
            continue
        if src:
            if src["contentHash"] != c["contentHash"]:
                errors.append(f"{qid}: contentHash não confere com a questão (texto ou gabarito mudou): refaça a partir do pacote novo")
            if str(src["answer"]) != str(c["gabarito"]):
                errors.append(f"{qid}: gabarito {c['gabarito']} difere do da questão ({src['answer']})")
            kind = src["kind"]
            letters = sorted(o["label"] for o in src["options"])
        else:
            kind = "CERTO_ERRADO" if not c["alternativas"] else "MULTIPLA_ESCOLHA"
            letters = sorted(c["alternativas"])
        alts: dict[str, str] = {k: str(v) for k, v in c["alternativas"].items()}
        if kind == "CERTO_ERRADO":
            if alts:
                errors.append(f"{qid}: Certo/Errado leva 'alternativas': {{}}")
        else:
            if sorted(alts) != letters:
                errors.append(f"{qid}: comente cada letra ({''.join(letters)}); veio {''.join(sorted(alts))}")
            for k, v in alts.items():
                m = NOTE_START.match(v.strip())
                if not m:
                    errors.append(f"{qid}: a nota {k} deve começar por 'Correta:' ou 'Errada:'")
                elif re.match(r"^(?:Correta|Errada):\s+(?:Correta|Errada|Incorreta)\s*[.:]", v.strip()):
                    errors.append(f"{qid}: a nota {k} repete o veredito ('Errada: Errada. …'); deixe só o prefixo")
                elif (m.group(1) == "Correta") != (k == str(c["gabarito"])):
                    errors.append(f"{qid}: a nota {k} diz {m.group(1)}, mas o gabarito é {c['gabarito']} (em 'assinale a incorreta', a letra do gabarito é a 'Correta:')")
        com = str(c["comentario"])
        # tamanhos, termos proibidos, remissão ao material-base e neutralidade (mesma régua da Fixação do material)
        errors += check_comment(qid, {"id": qid, "comentario": com, "alternativas": alts}, "")
        blob = com + " " + " ".join(alts.values())
        low = blob.lower()
        for bad in EXTRA_FORBIDDEN:
            if bad in low:
                errors.append(f"{qid}: expressão proibida: “{bad}”")
        for m in sorted({x.group(0).lower() for x in REMETE.finditer(blob)}):
            errors.append(f"{qid}: remete ao material (“{m}”): o comentário é lido no caderno, sem o PDF; explique ali mesmo")
        nbad, rows = citations(blob)
        if nbad:
            errors += [f"{qid}: {r}" for r in rows if r.startswith("INEXISTENTE")]
        warns += [f"{qid}: {r}" for r in rows if r.startswith("REVOGADO")]
        if not autor_fixacao:
            src_sh = source_shingles(c.get("trecho") or file_trecho)
            if src_sh:
                runs = [r for r in copied_runs(blob, src_sh) if not is_trivial_run(r)]
                total = sum(len(r) for r in runs)
                longest = max((len(r) for r in runs), default=0)
                if longest >= COPY_RUN_ERROR or total >= COPY_TOTAL_ERROR:
                    errors.append(f"{qid}: cópia do material-base ({longest} palavras seguidas, {total} no total): reescreva com suas palavras")
                elif runs:
                    warns.append(f"{qid}: coincidência de {longest} palavras com o material-base (definição ou texto de lei? confira)")
        norm = re.sub(r"\s+", " ", com).strip()
        starts.setdefault(" ".join(words(norm)[:20]), []).append(qid)
        for s in {x.strip() for x in re.split(r"[.;!?]", norm) if wc(x) >= 8}:
            sents.setdefault(s.lower(), set()).add(qid)
    for ids in starts.values():
        if len(ids) > 1:
            errors.append(f"comentário com o mesmo início em {len(ids)} questões ({', '.join(ids[:4])}): comente cada questão")
    rep = [s for s, ids in sents.items() if len(ids) >= 3]
    if rep:
        warns.append(f"{len(rep)} frase(s) de modelo repetida(s) em 3+ comentários (ex.: “{rep[0][:90]}”)")
    for d in doc.get("descartes") or []:
        if not d.get("id") or not str(d.get("motivo", "")).strip():
            errors.append(f"descarte sem id ou motivo: {d}")
    dup = seen & {d.get("id") for d in doc.get("descartes") or []}
    for qid in sorted(dup):
        errors.append(f"{qid}: está em comentarios e em descartes")
    return [f"{rel}: {e}" for e in errors], [f"{rel}: {w}" for w in warns], len(doc["comentarios"])


def sample(paths: list[Path], n: int, out: Path, seed: int) -> None:
    acv = acervo()
    pool = []
    for p in paths:
        doc = json.loads(p.read_text(encoding="utf-8"))
        for c in doc.get("comentarios", []):
            pool.append((p, c))
    rnd = random.Random(seed)
    pick = rnd.sample(pool, min(n, len(pool)))
    lines = [f"# Amostra dos comentários das questões ({len(pick)} de {len(pool)})", ""]
    lines.append("Leitura do dono antes da publicação dos lotes seguintes. Cada questão traz o enunciado, as alternativas, o gabarito, o comentário e a nota de cada letra.")
    for i, (p, c) in enumerate(pick, 1):
        q = acv.get(c["id"].removeprefix("tec_"), {})
        lines += ["", f"## {i}. {c['id']} — {p.relative_to(COMMENTS).as_posix()}", ""]
        if q.get("support"):
            lines += ["**Texto-base:**", "", "> " + str(q["support"]).replace("\n", "\n> "), ""]
        lines += [str(q.get("statement", "")).strip(), ""]
        for o in q.get("options", []):
            mark = " ✅" if o["label"] == q.get("answer") else ""
            lines.append(f"- **{o['label']})** {o['text']}{mark}")
        lines += ["", f"**Gabarito:** {c['gabarito']}", "", f"**Comentário:** {c['comentario']}", ""]
        for k, v in sorted(c["alternativas"].items()):
            lines.append(f"- **{k}:** {v}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"amostra: {out}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--amostra", type=int)
    ap.add_argument("--saida")
    ap.add_argument("--semente", type=int, default=20261116)
    ap.add_argument("-q", "--quieto", action="store_true", help="não lista os avisos")
    a = ap.parse_args()
    targets: list[Path] = []
    for p in [Path(x) for x in a.paths] or [COMMENTS]:
        p = p if p.is_absolute() else (Path.cwd() / p)
        if p.is_dir():
            targets += sorted(x for x in p.rglob("*.json") if not x.name.startswith("_") and "amostras" not in x.parts)
        else:
            targets.append(p)
    if a.amostra:
        sample(targets, a.amostra, Path(a.saida or COMMENTS / "amostras" / "amostra.md"), a.semente)
        return 0
    n_err = n_warn = n_q = 0
    for t in targets:
        e, w, n = validate_file(t)
        n_q += n
        n_err += len(e)
        n_warn += len(w)
        for x in e:
            print("ERRO ", x)
        if not a.quieto:
            for x in w:
                print("AVISO", x)
    print(f"{len(targets)} arquivo(s), {n_q} comentário(s): {n_err} erro(s), {n_warn} aviso(s)")
    return 1 if n_err else 0


if __name__ == "__main__":
    sys.exit(main())
