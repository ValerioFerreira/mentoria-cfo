import json
import re
import sys
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from validate_content import load_source_shingles, shingles, words, SHINGLE_N

path = ROOT / "content" / "items" / "direito-constitucional" / "a09.json"
doc = json.loads(path.read_text(encoding="utf-8"))
aula = doc["aula"]
source = load_source_shingles(aula)

print(f"Total de shingles da fonte: {len(source) if source else 0}")

conflicts = []

for seg in doc.get("segments", []):
    sid = seg["id"]
    for qidx, q in enumerate(seg.get("questions", [])):
        q_label = f"{sid} q{qidx+1}"
        
        # Statement
        stmt = q.get("statement", "")
        stmt_shingles = shingles(stmt) & source
        if stmt_shingles:
            conflicts.append((q_label, "statement", stmt, stmt_shingles))
            
        # Options
        for oidx, opt in enumerate(q.get("options", [])):
            opt_shingles = shingles(opt) & source
            if opt_shingles:
                conflicts.append((q_label, f"opt_{chr(65+oidx)}", opt, opt_shingles))
                
        # Explanation
        expl = q.get("explanation", "")
        expl_shingles = shingles(expl) & source
        if expl_shingles:
            conflicts.append((q_label, "explanation", expl, expl_shingles))

print(f"Total de conflitos encontrados: {len(conflicts)}")
for q_label, field, text, sh in conflicts:
    print(f"\n--- {q_label} [{field}] ({len(sh)} shingles) ---")
    print(f"Texto atual: {text}")
    print(f"Exemplo de 10 palavras coincidentes: {' '.join(list(sh)[0])}")
