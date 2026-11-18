"""Aproveita os comentários da Fixação do material próprio (content/material/**/fixacao.json) como comentários das
questões do banco (content/questoes/comentarios/<disciplina>/fixacao-mNN.json, autor "fixacao").

    pipeline/.venv/Scripts/python pipeline/questoes/comentarios_da_fixacao.py [--dry-run]

Para cada questão tec_* com comentário na Fixação:
  - confere o gabarito e as letras contra o acervo extraído dos cadernos (docs/questoes/.extraidas, o mesmo que o
    importador grava no banco) e copia o contentHash de lá;
  - normaliza as notas por letra para "Correta: …" / "Errada: …" (a Fixação usa "Correta." / "Incorreta.");
  - NÃO converte (e lista no relatório) quando o gabarito diverge, as letras não conferem, a nota "Correta" não está no
    gabarito, ou o texto remete ao material ("capítulo", "volume", "acima"…): no caderno o aluno não está lendo o PDF;
    essas questões voltam para a fila e são comentadas do zero.
Os arquivos saem com "revisao": "pendente" e o aplicador (web/scripts/questoes-comentarios.ts) só os publica depois da
revisão por agente (pipeline/briefs/questoes-comentarios-revisao.md), que troca o campo pelo nome do revisor. Arquivo já
revisado não é sobrescrito. Relatório: pipeline/.cache/questoes-comentar/fixacao-relatorio.md.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))

from questoes.importar import Store, load_all  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

MATERIAL = ROOT / "content" / "material"
OUT = ROOT / "content" / "questoes" / "comentarios"
REPORT = ROOT / "pipeline" / ".cache" / "questoes-comentar" / "fixacao-relatorio.md"

# remissões ao material: fora do PDF não fazem sentido
REMETE = re.compile(
    r"\bcap[ií]tulos?\b|\b(?:neste|deste|nesse|desse|no|do)\s+(?:volume|material)\b|\bmapa mental\b|\bcomo vimos\b"
    r"|\bvimos\b|\bestudamos\b|\b(?:quadro|esquema|seção|tabela)\s+(?:acima|anterior|seguinte)\b|\bnesta seção\b",
    re.IGNORECASE,
)
VERDICT = re.compile(r"^\s*(Correta|Incorreta|Errada)\s*[.:,\-–—]\s*", re.IGNORECASE)
# "Incorreta, pois …" vira "Errada: …" (o conectivo sobra depois dos dois-pontos)
CONECTIVO = re.compile(r"^(?:pois|porque|visto que|já que|uma vez que|dado que|porquanto)\s+", re.IGNORECASE)


def acervo() -> dict[str, dict]:
    store = Store(ROOT / "docs" / "questoes")
    out: dict[str, dict] = {}
    for d in load_all(store):
        for q in d["questoes"]:
            out[q["tecId"]] = q
    return out


def normalize(note: str) -> tuple[str | None, str]:
    m = VERDICT.match(note)
    if not m:
        return None, note.strip()
    v = "Correta" if m.group(1).lower() == "correta" else "Errada"
    body = CONECTIVO.sub("", note[m.end():].strip())
    # variável lógica ("p ∧ q", "b → d") não ganha maiúscula: viraria outra variável (achado da revisão do Raciocínio Lógico)
    if re.match(r"^[A-Za-z]\s+[^\w\s]", body):
        return v, f"{v}: {body}"
    return v, f"{v}: {body[:1].upper()}{body[1:]}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    acv = acervo()
    today = date.today().isoformat()
    ok_total = 0
    problems: list[tuple[str, str, str]] = []
    per_file: dict[Path, list[dict]] = {}
    for f in sorted(MATERIAL.glob("*/m*/fixacao.json")):
        disc, vol = f.parent.parent.name, f.parent.name
        d = json.loads(f.read_text(encoding="utf-8"))
        for q in d.get("questoes", []):
            qid = q.get("id", "")
            com = str(q.get("comentario", "")).strip()
            if not qid.startswith("tec_") or not com:
                continue
            src = acv.get(qid[4:])
            where = f"{disc}/{vol}"
            if not src:
                problems.append((qid, where, "não está no acervo extraído"))
                continue
            if src.get("anulada"):
                problems.append((qid, where, "anulada no acervo"))
                continue
            if str(q.get("gabarito")) != str(src["answer"]):
                problems.append((qid, where, f"gabarito da Fixação {q.get('gabarito')} × acervo {src['answer']}"))
                continue
            letters = sorted(o["label"] for o in src["options"])
            alts_in = q.get("alternativas") or {}
            if src["kind"] == "CERTO_ERRADO":
                alts: dict[str, str] = {}
            else:
                if sorted(alts_in) != letters:
                    problems.append((qid, where, f"letras comentadas {''.join(sorted(alts_in))} × questão {''.join(letters)}"))
                    continue
                alts = {}
                bad = None
                for k in letters:
                    v, txt = normalize(str(alts_in[k]))
                    if v is None:
                        bad = bad or f"nota {k} sem 'Correta'/'Incorreta' no início"
                    elif (v == "Correta") != (k == src["answer"]):
                        bad = bad or f"nota {k} diz {v}, gabarito {src['answer']}"
                    alts[k] = txt
                if bad:
                    problems.append((qid, where, bad))
                    continue
            rem = sorted({m.group(0).lower() for m in REMETE.finditer(com + " " + " ".join(alts.values()))})
            if rem:
                problems.append((qid, where, "remete ao material: " + ", ".join(rem)))
                continue
            per_file.setdefault(OUT / disc / f"fixacao-{vol}.json", []).append(
                {"id": qid, "contentHash": src["contentHash"], "gabarito": src["answer"], "comentario": com, "alternativas": alts}
            )
            ok_total += 1
    kept_reviewed = 0
    if not args.dry_run:
        for path, entries in per_file.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            if path.exists() and json.loads(path.read_text(encoding="utf-8")).get("revisao", "pendente") != "pendente":
                kept_reviewed += 1  # já revisado por um agente: não sobrescreve
                continue
            body = {
                "lote": f"{path.parent.name}/{path.stem}",
                "origem": f"content/material/{path.parent.name}/{path.stem.removeprefix('fixacao-')}/fixacao.json",
                "autor": "fixacao",
                "data": today,
                # o aplicador só publica depois da revisão (pipeline/briefs/questoes-comentarios-revisao.md): na conversão
                # de 16/11/2026 apareceram comentários da Fixação escritos para OUTRA questão
                "revisao": "pendente",
                "comentarios": entries,
                "descartes": [],
            }
            path.write_text(json.dumps(body, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        f"# Comentários da Fixação → questões ({today})",
        "",
        f"Convertidos: {ok_total} em {len(per_file)} arquivos. Não convertidos: {len(problems)} (voltam para a fila).",
        "",
        "| questão | volume | motivo |",
        "|---|---|---|",
        *[f"| {a} | {b} | {c} |" for a, b, c in problems],
    ]
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    from collections import Counter

    kinds = Counter(c.split(":")[0].split(" ")[0] for _, _, c in problems)
    print(json.dumps({"convertidos": ok_total, "arquivos": len(per_file), "naoConvertidos": len(problems), "motivos": kinds, "arquivosJaRevisadosMantidos": kept_reviewed, "relatorio": str(REPORT)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
