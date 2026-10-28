import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from pipeline.questoes.ineditas_mc_nativas import parse, check

def validate_text(text: str, label: str = "Test"):
    tmp_dir = Path("scratch/temp_informatica")
    tmp_dir.mkdir(parents=True, exist_ok=True)
    tmp = tmp_dir / "informatica.txt"
    tmp.write_text(text.strip() + "\n", encoding="utf-8")
    qs = parse(tmp)
    print(f"[{label}] Parsed {len(qs)} questions")
    
    # Run standard check
    errs = check(qs)
    
    # Check extra rule: comments must not cite letters of options!
    # Pattern: "A alternativa A/B/C/D/E", "As alternativas...", "A opção A/B/C/D/E", "letra A/B/C/D/E", etc.
    forbidden_letter_pattern = re.compile(r"\b(?:alternativas?|opç(?:ão|ões)|letras?)\s+[A-E]\b", re.I)
    
    for q in qs:
        expl = q["explanation"]
        matches = forbidden_letter_pattern.findall(expl)
        if matches:
            errs.append(f"Q#{q['n']} ({q['segment']}): Comentário cita letra de opção errada: {matches} -> {expl[:80]}...")
            
    for e in errs:
        print("  ERRO:", e)
    print(f"[{label}] Total errors: {len(errs)}")
    return len(errs) == 0

if __name__ == "__main__":
    from scratch.novas_p1 import NOVAS_P1
    from scratch.novas_p2 import NOVAS_P2
    ok1 = validate_text(NOVAS_P1, "Part 1 (Q1-Q30)")
    ok2 = validate_text(NOVAS_P2, "Part 2 (Q31-Q59)")
    ok_both = validate_text(NOVAS_P1 + "\n\n" + NOVAS_P2, "Parts 1+2 (Q1-Q59)")
    print(f"Results: P1={ok1}, P2={ok2}, Both={ok_both}")
