import json
from pathlib import Path

# a02
with open("content/summaries/biologia/a02.json", "r", encoding="utf-8") as f:
    a02 = json.load(f)

for s in a02.get("segments", []):
    sid = s["id"]
    fname = sid.split("/")[-1] # s01, s02, etc.
    out = Path(f"scratch/bio_a02_{fname}.txt")
    text = f"ID: {sid}\nFingerprint: {s.get('fingerprint')}\nNOTES: {s.get('notes')}\nANALYTIC:\n{s.get('analytic')}"
    out.write_text(text, encoding="utf-8")
    print(f"Written scratch/bio_a02_{fname}.txt")

# a03
with open("content/summaries/biologia/a03.json", "r", encoding="utf-8") as f:
    a03 = json.load(f)

for s in a03.get("segments", []):
    sid = s["id"]
    fname = sid.split("/")[-1] # s01, s02, etc.
    out = Path(f"scratch/bio_a03_{fname}.txt")
    text = f"ID: {sid}\nFingerprint: {s.get('fingerprint')}\nNOTES: {s.get('notes')}\nANALYTIC:\n{s.get('analytic')}"
    out.write_text(text, encoding="utf-8")
    print(f"Written scratch/bio_a03_{fname}.txt")
