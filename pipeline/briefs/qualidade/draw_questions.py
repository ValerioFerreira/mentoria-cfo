"""Uso: python draw_questions.py <saida.json> <n> <seed> <disc1,disc2,...>
Sorteia n questões (com contexto do trecho) de content/items/<disc>/*.json."""
import json, glob, os, random, sys
sys.stdout.reconfigure(encoding="utf-8")
out, n, seed, subs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), sys.argv[4].split(",")
root = r"C:\Users\Administrador\Documents\Projetos\CFO-BM\content"
pool = []
for d in subs:
    for f in sorted(glob.glob(os.path.join(root, "items", d, "*.json"))):
        j = json.load(open(f, encoding="utf-8"))
        for s in j["segments"]:
            for i, q in enumerate(s.get("questions", [])):
                pool.append({"file": os.path.relpath(f, os.path.dirname(root)).replace("\\", "/"), "segmentId": s["id"], "qIndex": i, **q})
random.Random(seed).shuffle(pool)
sample = [{"n": k + 1, **q} for k, q in enumerate(pool[:n])]
json.dump(sample, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"pool={len(pool)} amostra={len(sample)}")
