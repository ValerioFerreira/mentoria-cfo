import json
from pathlib import Path
import re
import unicodedata

def normalize(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()

# Load catalog & segments
segs = {}
for f in Path("content/segments").glob("*.json"):
    data = json.loads(f.read_text(encoding="utf-8"))
    for s in data["segments"]:
        segs[s["id"]] = s

# Load 76 from scratch/t3_pcpe_76.json
t3_list = json.loads(Path("scratch/t3_pcpe_76.json").read_text(encoding="utf-8"))

low_topics = []

for item in t3_list:
    seg_id = item["trecho"]
    seg_info = segs.get(seg_id)
    if not seg_info:
        continue
    topics = seg_info.get("topicsCovered", [])
    
    # Load summary file
    sum_path = Path("content/summaries") / f"{seg_id}.json"
    if not sum_path.exists():
        continue
    sum_data = json.loads(sum_path.read_text(encoding="utf-8"))
    sum_text = normalize(sum_data.get("content", ""))
    
    # Check how many topics are cited
    matched = 0
    total = len(topics)
    missing_topics = []
    for t in topics:
        norm_t = normalize(t)
        # Check if topic words appear
        words = [w for w in re.findall(r"[a-z0-9]+", norm_t) if len(w) > 3]
        if not words:
            matched += 1
            continue
        # if at least half of the words appear in summary
        found = sum(1 for w in words if w in sum_text)
        if found >= max(1, len(words) // 2):
            matched += 1
        else:
            missing_topics.append(t)
            
    ratio = matched / total if total > 0 else 1.0
    if ratio < 0.60:
        low_topics.append({
            "trecho": seg_id,
            "topics": total,
            "matched": matched,
            "ratio": ratio,
            "missing_topics": missing_topics,
            "cob": item["cobertura"],
            "veredito": item["veredito"]
        })

print(f"Trechos com < 60% de tópicos cobertos: {len(low_topics)}")
for lt in low_topics:
    print(f"{lt['trecho']} | {lt['matched']}/{lt['topics']} ({lt['ratio']:.1%}) | missing: {lt['missing_topics']}")
