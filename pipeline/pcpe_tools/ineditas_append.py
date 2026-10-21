"""Acrescenta rascunhos de questões a content/questoes/ineditas/mc/<disciplina>.txt embaralhando as alternativas.

Rascunho: blocos '@@ trecho [| item=cod]' + enunciado + 5 alternativas 'A)'..'E)' (a CORRETA é sempre a A) + '// Comentário: ...'.
O script sorteia a posição da correta (balanceando as letras, também em relação ao que já existe no arquivo) e reescreve o cabeçalho.
Uso: python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <disciplina> [--dry]
"""
import random, re, sys
sys.stdout.reconfigure(encoding="utf-8")
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
draft = Path(sys.argv[1]).read_text(encoding="utf-8").replace("\r\n", "\n")
disc = sys.argv[2]
target = ROOT / "content/questoes/ineditas/mc" / f"{disc}.txt"
raw = target.read_bytes()
crlf = b"\r\n" in raw
cur = raw.decode("utf-8").replace("\r\n", "\n")
have = Counter(re.findall(r"^@@ [^|\n]+\| ([A-E])", cur, re.M))

blocks = [b.strip("\n") for b in re.split(r"\n(?=@@ )", draft.strip("\n")) if b.strip()]
rnd = random.Random(sum(map(ord, disc)) * 7919 + len(cur))
out = []
problems = []
# fila de letras-alvo: sempre completa a menos frequente
for b in blocks:
    lines = b.split("\n")
    head = lines[0]
    m = re.match(r"@@ (\S+)\s*(\|\s*item=\S+)?\s*$", head) or re.match(r"@@ (\S+)\s*\|\s*A\s*(\|\s*item=\S+)?\s*$", head)
    if not m:
        sys.exit(f"cabeçalho inválido: {head}")
    seg = m.group(1)
    item = m.group(2) or ""
    body = lines[1:]
    ci = next(i for i, l in enumerate(body) if l.startswith("A) "))
    stem = "\n".join(body[:ci]).strip()
    opts = []
    for l in body[ci:]:
        if l.startswith("// Comentário:"):
            break
        mm = re.match(r"([A-E])\) (.*)", l)
        if not mm:
            sys.exit(f"alternativa inválida em {seg}: {l}")
        opts.append(mm.group(2))
    if len(opts) != 5:
        sys.exit(f"{seg}: {len(opts)} alternativas")
    comment = next(l for l in body if l.startswith("// Comentário:"))
    if not re.search(r"assinale|julgue|indique|aponte", stem, re.I):
        if re.search(r"[.?:]\s*$", stem):
            problems.append(f"{seg}: enunciado sem comando: {stem[:60]}")
        else:
            stem = "Assinale a opção que completa corretamente a afirmação: " + stem[0].lower() + stem[1:]
    ln = [len(t) for t in opts]
    if ln[0] > 80 and ln[0] > 1.8 * sum(ln[1:]) / 4:
        problems.append(f"{seg}: correta longa demais ({ln[0]} vs média {sum(ln[1:])//4}): {opts[0][:50]}")
    least = min("ABCDE", key=lambda L: (have[L], rnd.random()))
    pos = "ABCDE".index(least)
    correct, wrong = opts[0], opts[1:]
    rnd.shuffle(wrong)
    final = wrong[:pos] + [correct] + wrong[pos:]
    have[least] += 1
    hdr = f"@@ {seg} | {least}" + (f" {item}" if item else "")
    out.append("\n".join([hdr, stem] + [f"{'ABCDE'[i]}) {t}" for i, t in enumerate(final)] + [comment]))

if problems:
    print(chr(10).join(problems)); sys.exit(f"{len(problems)} problemas; corrija o rascunho")
text = cur.rstrip("\n") + "\n\n" + "\n\n".join(out) + "\n"
if "--dry" in sys.argv:
    print(f"{len(out)} questões; letras agora: {dict(have)}")
else:
    target.write_bytes((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
    print(f"{disc}: +{len(out)} questões; letras: {dict(sorted(have.items()))}")
