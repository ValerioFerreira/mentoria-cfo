import json
from pathlib import Path
import re
import unicodedata

def norm(s):
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()

segs = {}
for f in Path("content/segments").glob("*.json"):
    data = json.loads(f.read_text(encoding="utf-8"))
    for s in data["segments"]:
        segs[s["id"]] = s

t3_list = json.loads(Path("scratch/t3_pcpe_76.json").read_text(encoding="utf-8"))

summaries_data = {}
for f in Path("content/summaries").glob("*/*.json"):
    data = json.loads(f.read_text(encoding="utf-8"))
    for s in data.get("segments", []):
        summaries_data[s["id"]] = (data, s, f)

audit_results = []

for item in t3_list:
    sid = item["trecho"]
    seg_info = segs.get(sid, {})
    entry = summaries_data.get(sid)
    if not entry:
        audit_results.append({
            "trecho": sid,
            "status": "SEM_RESUMO",
            "veredito": item["veredito"],
            "cob": item["cobertura"],
        })
        continue
    file_doc, seg_sum, file_path = entry
    analytic = seg_sum.get("analytic", "")
    synthetic = seg_sum.get("synthetic", [])
    
    words = len(re.findall(r"\w+", analytic))
    topics = seg_info.get("topicsCovered", [])
    
    # Check sections (###)
    sections = re.findall(r"^###\s+(.+)$", analytic, re.M)
    has_para_fixar = any("para fixar" in s.lower() for s in sections)
    
    # Missing salient terms from cov.csv
    faltam_terms = item["faltam"].split()[:8]
    
    audit_results.append({
        "trecho": sid,
        "disciplina": item["disciplina"],
        "veredito": item["veredito"],
        "cobertura": float(item["cobertura"]) if item["cobertura"] else 0.0,
        "palavras": words,
        "num_secoes": len(sections),
        "has_para_fixar": has_para_fixar,
        "num_sintetico": len(synthetic),
        "topics": topics,
        "faltam_terms": faltam_terms,
        "file_path": str(file_path),
    })

print(f"Total auditados: {len(audit_results)}")
by_ver = {}
for a in audit_results:
    by_ver[a["veredito"]] = by_ver.get(a["veredito"], 0) + 1
print("Por veredito:", by_ver)

# Save to scratch/audit_t3_details.json
Path("scratch/audit_t3_details.json").write_text(json.dumps(audit_results, indent=2, ensure_ascii=False), encoding="utf-8")
