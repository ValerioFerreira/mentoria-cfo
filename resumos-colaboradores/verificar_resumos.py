#!/usr/bin/env python3
"""Autoverificação dos resumos (formato, tamanhos, expressões proibidas). Python 3, sem dependências.

Uso:  python verificar_resumos.py <pasta_com_os_arquivos.md> [--indice INDICE-RESUMOS.csv]

NÃO compara com o PDF: originalidade (nenhuma sequência de 10 palavras igual ao material) e exatidão de números/artigos
continuam sendo responsabilidade de quem escreve. Código de saída 1 se houver erro.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

NAME = re.compile(r"^(S\d{4})__([A-Za-z0-9_-]+)\.md$")
KEYS = ["id", "agente", "materia", "aula", "trecho", "paginas_lidas"]
FORBIDDEN = [
    "aspecto 1", "aspecto 2", "priorize a fixa", "lorem ipsum", "todo:", "tbd", "[inserir", "preencher", "a completar",
    "conforme o material", "de acordo com a aula", "segundo o professor", "no pdf", "estratégia concursos", "estrategia concursos",
    "nesta aula", "nessa aula", "nesta página", "visto na aula",
]


def words(text: str) -> int:
    return len(re.findall(r"\w+", re.sub(r"[|*#>`_-]+", " ", text)))


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
    sections = {parts[i]: parts[i + 1].strip() for i in range(1, len(parts) - 1, 2)}
    return head, sections


def tables_ok(text: str) -> str | None:
    blocks, cur = [], []
    for ln in text.splitlines():
        if ln.strip().startswith("|"):
            cur.append(ln.strip())
        elif cur:
            blocks.append(cur)
            cur = []
    if cur:
        blocks.append(cur)
    for rows in blocks:
        if len({r.count("|") for r in rows}) > 1:
            return "tabela com número de colunas inconsistente"
        if not any(set(r.replace("|", "").replace(":", "").strip()) <= {"-", " "} and "-" in r for r in rows):
            return "tabela sem linha separadora (| --- |)"
    return None


def check(path: Path, index: dict[str, dict]) -> tuple[list[str], list[str], int]:
    errs: list[str] = []
    warns: list[str] = []
    m = NAME.match(path.name)
    if not m:
        return [f"nome fora do padrão ID__AGENTE.md: {path.name}"], warns, 0
    sid, agent = m.groups()
    raw = path.read_bytes()
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        return ["arquivo não está em UTF-8"], warns, 0
    if "�" in text:
        errs.append("caractere de substituição (�): corrija a codificação")
    head, sec = parse(text)
    for k in KEYS:
        if not head.get(k):
            errs.append(f"cabeçalho sem a chave '{k}'")
    if head.get("id") and head["id"] != sid:
        errs.append(f"id do cabeçalho ({head['id']}) difere do nome do arquivo ({sid})")
    if head.get("agente") and head["agente"] != agent:
        errs.append(f"agente do cabeçalho ({head['agente']}) difere do nome do arquivo ({agent})")
    for s in ("ANALÍTICO", "SINTÉTICO", "NOTAS"):
        if s not in sec or not sec[s].strip():
            errs.append(f"seção '# {s}' ausente ou vazia")
    row = index.get(sid)
    if index and not row:
        errs.append(f"ID {sid} não existe no índice")
    if row and head.get("trecho") and head["trecho"] != row["Trecho"]:
        errs.append(f"trecho do cabeçalho ({head['trecho']}) difere do índice ({row['Trecho']})")
    n = words(sec.get("ANALÍTICO", ""))
    if sec.get("ANALÍTICO"):
        ceiling = int(float(row["Alvo máx. (palavras)"]) * 1.25) if row else 2500
        if n < 250:
            errs.append(f"analítico com {n} palavras (mínimo 250)")
        if n > ceiling:
            errs.append(f"analítico com {n} palavras, acima do teto ({ceiling})")
        pages = int(row["Págs."]) if row else 5
        if pages >= 5 and len(re.findall(r"^#{3,4}\s+\S", sec["ANALÍTICO"], re.M)) < 3:
            errs.append("use ao menos 3 seções (### Título) no analítico")
        if re.search(r"^#{1,2}\s", sec["ANALÍTICO"], re.M):
            errs.append("dentro do analítico use só ### e ####")
        if "Para fixar" not in sec["ANALÍTICO"]:
            warns.append("falta a seção '### Para fixar'")
    syn = sec.get("SINTÉTICO", "")
    if syn:
        bullets = [ln for ln in syn.splitlines() if ln.strip() and not ln.lstrip().startswith("#")]
        sn = words(syn)
        if not 6 <= len(bullets) <= 12:
            errs.append(f"sintético com {len(bullets)} pontos (use 6 a 12)")
        if not 110 <= sn <= 320:
            errs.append(f"sintético com {sn} palavras (use 110 a 320)")
        if any(words(b) < 8 for b in bullets):
            warns.append("há ponto do sintético muito curto (sem explicação)")
    low = (sec.get("ANALÍTICO", "") + "\n" + syn).lower()
    for bad in FORBIDDEN:
        if bad in low:
            errs.append(f"expressão proibida: “{bad}”")
    for name, t in (("analítico", sec.get("ANALÍTICO", "")), ("sintético", syn)):
        if t.count("**") % 2:
            errs.append(f"{name}: negrito (**) não fechado")
        bad = tables_ok(t)
        if bad:
            errs.append(f"{name}: {bad}")
    return errs, warns, n


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    folder = Path(args[0])
    index: dict[str, dict] = {}
    if "--indice" in args:
        with open(args[args.index("--indice") + 1], encoding="utf-8-sig", newline="") as f:
            index = {r["ID"]: r for r in csv.DictReader(f, delimiter=";")}
    files = sorted(p for p in folder.glob("*.md") if not p.name.startswith("RELATORIO"))
    bad = 0
    total = 0
    for p in files:
        errs, warns, n = check(p, index)
        total += n
        print(f"[{'ERRO' if errs else 'ok'}] {p.name} — {n} palavras no analítico")
        for e in errs:
            print(f"   ✗ {e}")
        for w in warns:
            print(f"   ! {w}")
        bad += bool(errs)
    if not any(p.name.startswith("RELATORIO") for p in folder.glob("*.md")):
        print("! falta o RELATORIO_AGENTE.md na pasta")
    print(f"{len(files)} arquivos, {bad} com erro, {total:,} palavras de resumo analítico")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
