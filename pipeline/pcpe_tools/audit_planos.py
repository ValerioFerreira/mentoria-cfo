"""Audita os planos de teste do PCPE (gerados por web/scripts/pcpe-plan-test.ts) contra o material e as regras.

    cd web && npx tsx scripts/pcpe-plan-test.ts          # gera pipeline/.cache/pcpe-planos.json (10 planos)
    pipeline/.venv/Scripts/python pipeline/pcpe_tools/audit_planos.py

Confere: (1) a diretriz × o PDF (rótulo do tópico inicial nas 2 primeiras págs. do trecho), (2) o resumo × o trecho (impressão
digital e cobertura de tópicos), (3) a ordem T→R→F→Q, (4) a congruência das Revisões, (5) cadernos de Questões só com trechos já
estudados e com questões suficientes (abre com 5; o pedido é 25 ou 15). Questões servíveis = base de produção + inéditas
de content/questoes/ineditas/mc (mesma conta de pipeline/questoes/lacunas_pcpe.py)."""
import json, re, sys, unicodedata, collections
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline"))
sys.stdout.reconfigure(encoding="utf-8")
from textutil import aula_key_map, load_pages  # noqa: E402

PLANOS = ROOT / "pipeline/.cache/pcpe-planos.json"
STOPW = set("de da do das dos para com por que uma nos nas ao aos ou lei".split())


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.replace("​", ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "", s)


planos = json.loads(PLANOS.read_text(encoding="utf-8"))
keymap = aula_key_map()
_cache: dict = {}


def pages(aula):
    if aula not in _cache:
        k = keymap.get(aula)
        _cache[aula] = {p["n"]: norm(p["text"]) for p in load_pages(k)["pages"]} if k else None
    return _cache[aula]


def frac(topic, pg, rng):
    words = [norm(w) for w in re.findall(r"[A-Za-zÀ-ú]{4,}", topic) if norm(w) not in STOPW]
    if not words:
        return 1.0
    blob = "".join(pg.get(i, "") for i in rng)
    return sum(w in blob for w in words) / len(words)


segs = {}
for f in (ROOT / "content/segments").glob("*.json"):
    for g in json.loads(f.read_text(encoding="utf-8"))["segments"]:
        segs[g["id"]] = g
summ = {}
for f in (ROOT / "content/summaries").glob("*/*.json"):
    d = json.loads(f.read_text(encoding="utf-8"))
    for s in d["segments"]:
        summ[s["id"]] = (s, d["status"])

avail = collections.Counter()
for r in json.loads((ROOT / "pipeline/briefs/ineditas-base-segcounts.json").read_text(encoding="utf-8")):
    u = r["banca"].upper()
    if "CEBRASPE" in u or "CESPE" in u or "AOCP" in u or r["banca"] == "Inédita MentorIA":
        avail[r["seg"]] += r["n"]
for f in (ROOT / "content/questoes/ineditas/mc").glob("*.txt"):
    for m in re.finditer(r"^@@\s*(\S+)\s*\|", f.read_text(encoding="utf-8"), re.M):
        avail[f"{f.stem}/{m.group(1)}"] += 1

used = sorted({s for p in planos for a in p["acts"] if a["type"] == "TEORIA" for s in a["segmentIds"]})
print(f"{len(planos)} planos; {len(used)} trechos de Teoria usados\n")

# 1) rótulos da diretriz
sus = {}
for sid in used:
    g = segs.get(sid)
    pg = pages(g["aula"]) if g else None
    if not g or not pg or not g.get("startTopic") or g["startsMidTopic"]:
        continue
    sp = g["startPage"]
    f = frac(g["startTopic"], pg, [sp, sp + 1])
    if f < 0.4:
        sus[sid] = (round(f, 2), g["startTopic"][:70], sp)
print(f"[1] DIRETRIZ × PDF: {len(sus)} trechos cujo tópico inicial não aparece nas 2 primeiras págs. (lista em pipeline/.cache/pcpe-rotulos-suspeitos.json)")
(ROOT / "pipeline/.cache/pcpe-rotulos-suspeitos.json").write_text(json.dumps(sus, ensure_ascii=False, indent=1), encoding="utf-8")
bypass = collections.Counter(k.split("/")[0] for k in sus)
print("    por disciplina:", dict(bypass))

# 2) resumos
bad_fp = low = 0
for sid in used:
    if sid not in summ:
        print("    sem resumo:", sid); continue
    s, st = summ[sid]; g = segs[sid]; fp = s["fingerprint"]
    if (fp["startPage"], fp["endPage"]) != (g["startPage"], g["endPage"]):
        bad_fp += 1
print(f"[2] RESUMOS: {bad_fp} com impressão digital divergente; status usados: {collections.Counter(summ[s][1] for s in used if s in summ)}")

# 3-5) por plano
print("\n[3-5] ORDEM, REVISÕES e CADERNOS")
tot_zero = 0
for p in planos:
    acts = p["acts"]; byk = {a["key"]: a for a in acts}
    content = [a for a in acts if a.get("scope") != "FINAL"]
    studied = {}
    for a in sorted((x for x in acts if x["type"] == "TEORIA"), key=lambda x: x["ord"]):
        for s in a["segmentIds"]: studied.setdefault(s, a["ord"])
    ordem = rev = unseen = zero = short = 0
    by = collections.defaultdict(list)
    for a in content: by[a["aulaId"]].append(a)
    for l in by.values():
        T = [a["ord"] for a in l if a["type"] == "TEORIA"]; R = [a for a in l if a["type"] == "REVISAO"]
        if T and R and min(r["ord"] for r in R) <= min(T): ordem += 1
    for r in content:
        if r["type"] != "REVISAO": continue
        refs = [byk[k] for k in r["refKeys"] if k in byk]
        if not refs or any(t["ord"] >= r["ord"] or t["type"] != "TEORIA" for t in refs) or set(r["segmentIds"]) != {s for t in refs for s in t["segmentIds"]}:
            rev += 1
    for q in acts:
        if q["type"] != "QUESTOES": continue
        for s in q["segmentIds"]:
            if studied.get(s, 10**9) >= q["ord"]: unseen += 1
        n = sum(avail[s] for s in q["segmentIds"]); need = (q.get("quiz") or {}).get("questions", 0)
        if n < 5: zero += 1
        elif need and n < need: short += 1
    tot_zero += zero
    print(f"• {p['name']} → {p['verdict']}: ordem {ordem} | revisões incongruentes {rev} | questões de trecho não visto {unseen} | cadernos que NÃO abrem {zero} | cadernos menores que o pedido {short}")
print(f"\nTOTAL de cadernos que não abrem nos {len(planos)} planos: {tot_zero}")
sys.exit(1 if tot_zero or sus else 0)
