"""Gera content/questoes/overrides-questoes.json e atualiza o mapa de assuntos a partir dos resultados dos
agentes validadores da auditoria de 14/10/2026 (docs/questoes/auditoria/2026-10-14/agentes/resultados).

Só entra o que um agente conferiu questão a questão (ou categoria a categoria) com confiança alta.
    pipeline/.venv/Scripts/python pipeline/questoes/gerar_overrides.py
"""
from __future__ import annotations

import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
R = ROOT / "docs" / "questoes" / "auditoria" / "2026-10-14" / "agentes" / "resultados"
OUT = ROOT / "content" / "questoes" / "overrides-questoes.json"
MAPA = ROOT / "content" / "questoes" / "mapa-assuntos.json"
sys.stdout.reconfigure(encoding="utf-8")

segs = {s["id"] for f in glob.glob(str(ROOT / "content" / "segments" / "*.json")) for s in json.loads(Path(f).read_text(encoding="utf-8"))["segments"]}


def jl(name: str):
    p = R / f"{name}.jsonl"
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


ov: dict[str, dict] = {}
# Atualidades: o que as aulas não ensinam ou o gabarito superado sai; o que tem destino melhor muda de trecho
for g in ("D1-atualidades", "D2-atualidades"):
    for r in jl(g):
        rec, dest = r["recomendacao"], r.get("destino_sugerido")
        if rec in ("RETIRAR", "RETIRAR_DO_PLANO"):
            ov[r["tecId"]] = {"skip": f"Atualidades: {r['natureza']}; {rec.lower()} (auditoria 14/10)"}
        elif rec == "MOVER" and dest in segs:
            ov[r["tecId"]] = {"segment": dest}
        elif rec == "REVISAR_HUMANO":
            ov[r["tecId"]] = {"draft": "Atualidades: revisar gabarito/escopo (auditoria 14/10)"}
# amostra validada das demais disciplinas: trecho errado com sugestão de confiança alta; fora do catálogo sai
for g in ("B1-portugues-linguas", "B2-direito", "B3-bio-quim-fis", "B4-exatas-info"):
    for r in jl(g):
        if r["disciplina_ok"] == "nao" and r.get("disciplina_sugerida") in (None, "fora_do_catalogo") and r["confianca"] == "alta":
            ov[r["tecId"]] = {"skip": "fora do catálogo/edital (auditoria 14/10)"}
        elif r["trecho_ok"] in ("nao", "parcial") and r["confianca"] == "alta" and r.get("trecho_sugerido") in segs and r["disciplina_ok"] == "sim":
            ov[r["tecId"]] = {"segment": r["trecho_sugerido"]}
OUT.write_text(json.dumps({"_comment": "Decisões por questão (id TEC). {segment}|{skip}|{draft}. Geradas por gerar_overrides.py a partir da auditoria de 14/10/2026.", "questoes": ov}, ensure_ascii=False, indent=1), encoding="utf-8")

# mapa de assuntos: categorias técnicas além do edital, fonética (decisão do dono) e Física sem assunto
mapa = json.loads(MAPA.read_text(encoding="utf-8"))
skips = {}
for r in jl("C3-biologia-quimica"):
    if r.get("nivel") == "tecnico_alem_do_edital" and r.get("confianca") == "alta":
        skips[r["chave"]] = "técnico além do edital (auditoria 14/10)"
skips["Língua Portuguesa (Português)|Fonética (Fonemas, Dígrafos, Encontros Consonantais, Vocálicos). Separação Silábica"] = "fonética fora do edital (decisão do dono, 14/10)"
skips["Física|Outras Questões de Física"] = "radiologia/optometria fora do edital (auditoria 14/10)"
skips["Física|"] = "sem assunto: conteúdo técnico fora do edital (auditoria 14/10)"
n = 0
for k, why in skips.items():
    if "skip" not in mapa["assuntos"].get(k, {}):
        mapa["assuntos"][k] = {"skip": why, "_n": mapa["assuntos"].get(k, {}).get("_n", 0)}
        n += 1
MAPA.write_text(json.dumps(mapa, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
print("overrides:", len(ov), dict(Counter(next(iter(v)) for v in ov.values())), "| assuntos novos em skip:", n)
