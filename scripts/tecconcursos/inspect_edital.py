import os
import json

EDITAL_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "content", "edital")

def main():
    files = sorted(os.listdir(EDITAL_DIR))
    summary = {}
    total_topics = 0
    for f in files:
        if not f.endswith(".json"):
            continue
        subj_name = f.replace(".json", "")
        with open(os.path.join(EDITAL_DIR, f), "r", encoding="utf-8") as fp:
            data = json.load(fp)
        
        # Pode ter estrutura de itens, topicos ou array
        topics = []
        if isinstance(data, list):
            topics = data
        elif isinstance(data, dict):
            topics = data.get("items") or data.get("topicos") or data.get("topics") or []
        
        summary[subj_name] = {
            "count": len(topics),
            "sample": [t.get("title") or t.get("name") or str(t)[:40] for t in topics[:3]] if isinstance(topics, list) and topics and isinstance(topics[0], dict) else topics[:3]
        }
        total_topics += len(topics)
        
    print(f"Total de disciplinas mapeadas: {len(summary)} | Total de tópicos: {total_topics}")
    for k, v in summary.items():
        print(f" - {k}: {v['count']} tópicos (Exemplos: {v['sample']})")

if __name__ == "__main__":
    main()
