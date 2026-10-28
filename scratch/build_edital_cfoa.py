import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
EDITAL_DIR = ROOT / "content" / "edital"
STRUCTURE_DIR = ROOT / "content" / "structure"

for subject_id in ["administracao", "direitos-humanos", "direito-processual-penal-militar"]:
    struct_file = STRUCTURE_DIR / f"{subject_id}.json"
    data = json.loads(struct_file.read_text(encoding="utf-8"))
    
    items = []
    for idx, aula in enumerate(data["aulas"], 1):
        items.append({
            "id": str(idx),
            "item": aula["title"],
            "status": "covered",
            "where": [
                {
                    "aula": aula["id"]
                }
            ]
        })
        
    out_doc = {
        "subject": subject_id,
        "items": items
    }
    
    out_file = EDITAL_DIR / f"{subject_id}.json"
    out_file.write_text(json.dumps(out_doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Gerado {out_file} com {len(items)} itens.")
