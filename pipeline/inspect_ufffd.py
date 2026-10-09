import json
import glob

for f in sorted(glob.glob("content/items/*/*.json")):
    data = json.load(open(f, encoding="utf-8"))
    for seg in data.get("segments", []):
        for qidx, q in enumerate(seg.get("questions", [])):
            txt = f"{q.get('statement','')} {' '.join(q.get('options',[]))} {q.get('explanation','')}"
            if "\ufffd" in txt:
                print(f"{f} -> {seg['id']}#q{qidx+1:02d}")
                for k in ["statement", "options", "explanation"]:
                    val = q.get(k)
                    if isinstance(val, list):
                        for idx, opt in enumerate(val):
                            if "\ufffd" in opt:
                                print(f"  opt[{chr(65+idx)}]: {repr(opt)}")
                    elif isinstance(val, str) and "\ufffd" in val:
                        print(f"  {k}: {repr(val)}")
