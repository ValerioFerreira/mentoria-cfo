"""Amostra estratificada das questões APROVADAS (classificação atual) para validação independente.
    pipeline/.venv/Scripts/python pipeline/questoes/pacotes_validacao.py [--n 180] [--semente 20261016]
Grava docs/questoes/classificacao-agentes/<data>/validacao/V-<grupo>.json (mesmo esquema do B1..B4 da auditoria)."""
import argparse, glob, json, random, re, sys
from collections import defaultdict
from datetime import date
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "pipeline")); sys.stdout.reconfigure(encoding="utf-8")
from questoes.classify import Classifier, load_catalog, load_map

ap = argparse.ArgumentParser(); ap.add_argument("--n", type=int, default=180); ap.add_argument("--semente", type=int, default=20261016)
a = ap.parse_args()
IMG = ROOT / "docs/questoes/.extraidas/img"; MD = re.compile(r"!\[([^\]]*)\]\(/q-img/([0-9a-f]{64})\)")
im = lambda t: MD.sub(lambda m: f"[{m.group(1)}: {IMG / (m.group(2) + '.png')}]", t or "")
man = json.loads((ROOT / "docs/questoes/.importadas.json").read_text(encoding="utf-8"))
ac = {}
for sha in man["cadernos"]:
    for q in json.loads((ROOT / f"docs/questoes/.extraidas/{sha}.json").read_text(encoding="utf-8"))["questoes"]: ac[q["tecId"]] = q
cat = load_catalog(); clf = Classifier(cat, load_map())
valid = {k: q for k, q in ac.items() if not q["problems"] and not q["anulada"]}; clf.vote_assuntos(list(valid.values()))
segs = {s["id"]: s for f in glob.glob(str(ROOT / "content/segments/*.json")) for s in json.loads(Path(f).read_text(encoding="utf-8"))["segments"]}
by = defaultdict(list)
for t, q in valid.items():
    r = clf.classify(q)
    if r.status == "APPROVED": by[r.subjectId].append((t, q, r))
rnd = random.Random(a.semente); tot = sum(len(v) for v in by.values()); out = defaultdict(list)
G = {"V1-linguas-exatas": {"lingua-portuguesa","lingua-inglesa","lingua-espanhola","matematica","estatistica","raciocinio-logico","informatica"},
     "V2-direito": {"direito-constitucional","direito-administrativo","direito-penal-militar","legislacoes-pe","atualidades","historia-pe"},
     "V3-ciencias": {"biologia","quimica","fisica"}}
for s, v in by.items():
    k = max(6, round(a.n * len(v) / tot)); g = next((n for n, ss in G.items() if s in ss), None)
    if not g: continue
    for t, q, r in rnd.sample(v, min(k, len(v))):
        sg = segs.get(r.segmentId, {})
        sup = im(q.get("support") or "")
        out[g].append({"tecId": t, "ano": q.get("ano"), "materiaTEC": q["materia"], "assuntoTEC": q["assunto"], "tipo": q["kind"], "textoBase": sup[:900],
            "enunciado": im(q["statement"]), "alternativas": [f"{o['label']}) {im(o['text'])}" for o in q["options"]], "gabarito": q.get("answer"),
            "classificacaoAtual": {"disciplina": r.subjectId, "trecho": r.segmentId, "topicosDoTrecho": [x for x in [sg.get("startTopic")] + (sg.get("topicsCovered") or []) if x][:12], "itemEdital": r.editalItemId, "motivo": r.reason}})
d = ROOT / "docs/questoes/classificacao-agentes" / date.today().isoformat() / "validacao"; d.mkdir(parents=True, exist_ok=True)
for g, v in out.items():
    (d / f"{g}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
print({g: len(v) for g, v in out.items()}, "de", tot, "aprovadas")
