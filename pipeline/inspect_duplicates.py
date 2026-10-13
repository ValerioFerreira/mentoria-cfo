#!/usr/bin/env python3
"""Diagnóstico detalhado das 852 questões com alternativas duplicadas.
"""
import json
import re
from pathlib import Path
from collections import defaultdict, Counter

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
ITEMS_DIR = ROOT / "content" / "items"

def normalize(s):
    if not s:
        return ""
    return re.sub(r"\s+", " ", s.strip().lower())

def main():
    dup_cases = []
    by_subject = Counter()
    patterns = Counter()

    for fpath in sorted(ITEMS_DIR.glob("*/*.json")):
        sub = fpath.parent.name
        data = json.loads(fpath.read_text(encoding="utf-8"))
        for seg in data.get("segments", []):
            for qidx, q in enumerate(seg.get("questions", [])):
                opts = q.get("options", [])
                ans = q.get("answer", "")
                norm_opts = [normalize(o) for o in opts]
                
                # Procura índices duplicados
                seen = {}
                dups = []
                for idx, o in enumerate(norm_opts):
                    if o in seen:
                        dups.append((seen[o], idx, opts[idx]))
                    else:
                        seen[o] = idx
                
                if dups:
                    by_subject[sub] += 1
                    dup_cases.append({
                        "id": f"{seg['id']}#q{qidx+1:02d}",
                        "subject": sub,
                        "file": str(fpath),
                        "statement": q.get("statement", "")[:100],
                        "options": opts,
                        "answer": ans,
                        "dups": dups
                    })

    print(f"Total de questões com alternativas duplicadas: {len(dup_cases)}")
    print("Distribuição por disciplina:")
    for s, c in by_subject.most_common():
        print(f" - {s}: {c}")

    print("\nExemplos de casos:")
    for c in dup_cases[:10]:
        print(f"\nID: {c['id']} ({c['subject']}) | Gabarito: {c['answer']}")
        print(f"Enunciado: {c['statement']}")
        for i, o in enumerate(c['options']):
            print(f"  {chr(65+i)}) {o}")

if __name__ == "__main__":
    main()
