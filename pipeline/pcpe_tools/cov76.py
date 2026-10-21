"""Cobertura atual × anterior dos 76 trechos da Etapa B (pipeline/briefs/pcpe-resumos-76.json).

Uso: python pipeline/pcpe_tools/cov76.py [prefixo-da-disciplina] [--json saida.json]
"""
import json
import sys

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, "pipeline")
import summary_coverage as sc  # noqa: E402

lst = json.load(open("pipeline/briefs/pcpe-resumos-76.json", encoding="utf-8"))
pref = next((a for a in sys.argv[1:] if not a.startswith("--") and not a.endswith(".json")), "")
out = {}
segcache, doccache = {}, {}
for x in lst:
    tid = x["trecho"]; x["cobertura"] = float(x["cobertura"]); x["palavras"] = int(x["palavras"])
    if not tid.startswith(pref):
        continue
    disc, aula, _ = tid.split("/")
    if disc not in segcache:
        segcache[disc] = {s["id"]: s for s in json.load(open(f"content/segments/{disc}.json", encoding="utf-8"))["segments"]}
    key = f"{disc}/{aula}"
    if key not in doccache:
        doccache[key] = json.load(open(f"content/summaries/{disc}/{aula}.json", encoding="utf-8"))
    seg = next(s for s in doccache[key]["segments"] if s["id"] == tid)
    r = sc.segment_score(seg, segcache[disc][tid])
    words = len(seg["analytic"].split())
    out[tid] = {"antes": x["cobertura"], "depois": round(r["score"], 3), "palavras_antes": x["palavras"], "palavras": words}
    print(f"{tid:42s} {x['cobertura']:.2f} -> {r['score']:.2f}   {x['palavras']:5d} -> {words:5d} palavras")
if "--json" in sys.argv:
    json.dump(out, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
