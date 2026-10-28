import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(".").resolve()))

from scratch.novas_p1 import NOVAS_P1
from scratch.novas_p2 import NOVAS_P2
from scratch.novas_p3 import NOVAS_P3
from scratch.novas_p4 import NOVAS_P4
from scratch.novas_p5 import NOVAS_P5

from pipeline.questoes.ineditas_mc_nativas import parse, check

def main():
    parts = [
        NOVAS_P1.strip(),
        NOVAS_P2.strip(),
        NOVAS_P3.strip(),
        NOVAS_P4.strip(),
        NOVAS_P5.strip(),
    ]
    full_text = "\n\n".join(parts) + "\n"
    
    out_dir = Path("scratch/novas_questoes")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / "informatica.txt"
    out_file.write_text(full_text, encoding="utf-8")
    print(f"Written to {out_file} ({len(full_text.splitlines())} lines)")
    
    # Parse and check
    qs = parse(out_file)
    print(f"Parsed {len(qs)} questions")
    
    # Gabarito distribution check
    from collections import Counter
    gabs = Counter(q["answer"] for q in qs)
    print("Gabarito counts:", sorted(gabs.items()))
    
    # Rule check
    errs = check(qs)
    
    # Check extra rule: comments must not cite letters of options!
    forbidden_letter_pattern = re.compile(r"\b(?:alternativas?|opç(?:ão|ões)|letras?)\s+[A-E]\b", re.I)
    for q in qs:
        expl = q["explanation"]
        matches = forbidden_letter_pattern.findall(expl)
        if matches:
            errs.append(f"Q#{q['n']} ({q['segment']}): Comentário cita letra de opção errada: {matches} -> {expl[:80]}...")
            
    print(f"Total errors: {len(errs)}")
    for e in errs:
        print("  ERRO:", e)
        
    # Check segments count
    seg_counts = Counter(q["segment"] for q in qs)
    print(f"Distinct segments covered: {len(seg_counts)}")
    
    # Verify against scratch/trechos_fracos/informatica.json
    import json
    with open("scratch/trechos_fracos/informatica.json", encoding="utf-8") as f:
        target_segs = json.load(f)
    target_counts = {item['trecho']: item['faltam'] for item in target_segs}
    print(f"Target segments in json: {len(target_counts)}")
    
    diff_segs = set(target_counts.keys()) ^ set(seg_counts.keys())
    if diff_segs:
        print("Mismatch in segments:", diff_segs)
    else:
        print("All 30 segments matched perfectly!")

    # Check counts per segment
    count_mismatches = []
    for seg, expected in target_counts.items():
        actual = seg_counts.get(seg, 0)
        if actual != expected:
            count_mismatches.append(f"{seg}: expected {expected}, got {actual}")
    if count_mismatches:
        print("Count mismatches:", count_mismatches)
    else:
        print("All 30 segments have EXACT target counts!")

if __name__ == "__main__":
    main()
