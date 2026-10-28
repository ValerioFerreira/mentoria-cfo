import json
import sys
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
BASELINE_FILE = ROOT / "scratch/segments_baseline.json"

def get_current_segments():
    segs = {}
    for f in sorted((ROOT / "content/segments").glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        for s in data["segments"]:
            segs[s["id"]] = {
                "startPage": s["startPage"],
                "endPage": s["endPage"],
                "pages": s["pages"]
            }
    return segs

if sys.argv[1:2] == ["--save"]:
    segs = get_current_segments()
    BASELINE_FILE.write_text(json.dumps(segs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Salvo baseline com {len(segs)} trechos em {BASELINE_FILE}")
    sys.exit(0)

if not BASELINE_FILE.exists():
    print(f"ERRO: Baseline {BASELINE_FILE} não existe. Execute com --save primeiro.")
    sys.exit(1)

baseline = json.loads(BASELINE_FILE.read_text(encoding="utf-8"))
current = get_current_segments()

errors = []
if len(baseline) != len(current):
    errors.append(f"Número de trechos mudou: antes {len(baseline)}, agora {len(current)}")

for sid, b in baseline.items():
    if sid not in current:
        errors.append(f"Trecho REMOVIDO: {sid}")
        continue
    c = current[sid]
    if b["startPage"] != c["startPage"] or b["endPage"] != c["endPage"]:
        errors.append(f"Trecho {sid} MUDOU páginas: antes {b['startPage']}-{b['endPage']}, agora {c['startPage']}-{c['endPage']}")

for sid in current:
    if sid not in baseline:
        errors.append(f"Trecho NOVO: {sid}")

if errors:
    print(f"VIOLAÇÃO DA INVARIANTE! {len(errors)} erros:")
    for e in errors[:20]:
        print("  -", e)
    sys.exit(1)
else:
    print(f"INVARIANTE PRESERVADA: todos os {len(baseline)} trechos mantiveram id, startPage e endPage.")
