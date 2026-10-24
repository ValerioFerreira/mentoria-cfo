"""Trechos e aulas do CBMPE_CFOA abaixo das metas de questões servíveis (AOCP + reforço MC + inéditas MC).

Duas metas (seção 10.2 de pipeline/briefs/cfoa-inclusao.md):
  1. >= 7 questões servíveis por trecho elegível do CFOA;
  2. >= 25 questões servíveis na soma dos até 4 primeiros trechos de cada aula elegível do CFOA.

Base: pipeline/briefs/ineditas-cfoa-base.json (gerada por web/scripts/cfoa-cadernos-base.ts).
O que passar de `txt` em content/questoes/ineditas/mc/<disciplina>.txt conta como questão nova.

Uso:
    python pipeline/questoes/lacunas_cfoa.py                              # resumo por disciplina
    python pipeline/questoes/lacunas_cfoa.py --lista administracao        # trechos e aulas pendentes na disciplina
    python pipeline/questoes/lacunas_cfoa.py --check                      # sai com código 1 se ainda faltar em algum trecho ou aula
"""
import json, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.stdout.reconfigure(encoding="utf-8")
MIN_SEG = 7
ALVO_AULA = 25


def main() -> None:
    b = json.loads((ROOT / "pipeline/briefs/ineditas-cfoa-base.json").read_text(encoding="utf-8"))
    now = Counter()
    for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
        for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
            now[f"{f.stem}/{m.group(1)}"] += 1

    atual = {
        seg: info["efetiva"] + max(0, now[seg] - info["txt"])
        for seg, info in b["segs"].items()
    }

    # Meta 1: cada trecho >= 7
    falta_seg = {seg: max(0, MIN_SEG - q) for seg, q in atual.items() if q < MIN_SEG}

    # Meta 2: soma dos até 4 primeiros trechos de cada aula >= 25
    # Calcula quanto cada trecho precisa escrever no total (meta 1 + complemento da meta 2 distribuído nos primeiros trechos)
    alvo_seg = {seg: max(MIN_SEG, q) for seg, q in atual.items()}
    falta_aula = {}
    for aula, trechos in b["grupos"].items():
        soma_atual = sum(atual[t] for t in trechos)
        if soma_atual < ALVO_AULA:
            falta_aula[aula] = (ALVO_AULA - soma_atual, {t: atual[t] for t in trechos})
        soma_apos_min = sum(alvo_seg[t] for t in trechos)
        if soma_apos_min < ALVO_AULA:
            extra = ALVO_AULA - soma_apos_min
            n = len(trechos)
            for i, t in enumerate(trechos):
                alvo_seg[t] += extra // n + (1 if i < (extra % n) else 0)

    escrever_seg = {seg: alvo_seg[seg] - atual[seg] for seg in b["segs"] if alvo_seg[seg] > atual[seg]}

    por_disc = defaultdict(lambda: [0, 0, 0])  # [trechos < 7, aulas < 25, total a escrever]
    for seg in falta_seg:
        por_disc[seg.split("/")[0]][0] += 1
    for aula in falta_aula:
        por_disc[aula.split("/")[0]][1] += 1
    for seg, q in escrever_seg.items():
        por_disc[seg.split("/")[0]][2] += q

    if "--lista" in sys.argv:
        disc = sys.argv[sys.argv.index("--lista") + 1]
        for aula, trechos in sorted(b["grupos"].items()):
            if not aula.startswith(disc + "/"):
                continue
            all_aula_segs = [s for s in sorted(b["segs"]) if s.startswith(aula + "/")]
            if any(s in escrever_seg for s in all_aula_segs) or aula in falta_aula:
                soma4 = sum(atual[t] for t in trechos)
                partes = [
                    f"{s.split('/')[2]}={atual[s]}(+{escrever_seg.get(s, 0)}->{alvo_seg[s]})"
                    for s in all_aula_segs
                ]
                print(f"{aula} [soma4={soma4}/{ALVO_AULA}]: " + ", ".join(partes))
    else:
        for d, (ns, na, q) in sorted(por_disc.items(), key=lambda x: -x[1][2]):
            print(f"{d}: {ns} trechos < {MIN_SEG}, {na} aulas < {ALVO_AULA}, faltam {q} questões")
        print(
            f"TOTAL: {len(falta_seg)} trechos < {MIN_SEG}, "
            f"{len(falta_aula)} aulas < {ALVO_AULA}, "
            f"faltam {sum(escrever_seg.values())} questões"
        )

    pendente = bool(falta_seg or falta_aula)
    sys.exit(1 if (pendente and "--check" in sys.argv) else 0)


if __name__ == "__main__":
    main()
