import json
import re
from part4 import QUESTIONS_PART_4

with open('scratch/plan_123.json', 'r', encoding='utf-8') as f:
    plan = json.load(f)

plan_part4 = [q for q in plan if 93 <= q['idx'] <= 123]
assert len(QUESTIONS_PART_4) == len(plan_part4), f"Expected {len(plan_part4)}, got {len(QUESTIONS_PART_4)}"

command_words = ["assinale", "julgue", "indique", "marque", "escolha"]
errors = []

for i, (q, p) in enumerate(zip(QUESTIONS_PART_4, plan_part4)):
    idx = p['idx']
    seg = p['seg']
    ans = p['ans']
    
    if q['seg'] != seg:
        errors.append(f"Q{idx}: segment mismatch {q['seg']} != {seg}")
    if q['ans'] != ans:
        errors.append(f"Q{idx}: answer mismatch {q['ans']} != {ans}")
        
    stem = q['stem']
    words = stem.split()
    if not (6 <= len(words) <= 140):
        errors.append(f"Q{idx}: stem word count {len(words)} not in [6, 140]")
    if not any(cw in stem.lower() for cw in command_words):
        errors.append(f"Q{idx}: stem missing command word")
        
    opts = q['opts']
    if len(opts) != 5:
        errors.append(f"Q{idx}: options count {len(opts)} != 5")
    
    letters = [opt[0] for opt in opts]
    if letters != ['A', 'B', 'C', 'D', 'E']:
        errors.append(f"Q{idx}: options letters wrong: {letters}")
        
    ans_idx = ord(ans) - ord('A')
    certa = opts[ans_idx][3:].strip()
    distratores = [opts[k][3:].strip() for k in range(5) if k != ans_idx]
    
    avg_dist = sum(len(d) for d in distratores) / 4.0
    if len(certa) > 80:
        ratio = len(certa) / avg_dist
        if ratio > 1.8:
            errors.append(f"Q{idx}: length ratio {ratio:.2f} > 1.8 (certa={len(certa)}, avg={avg_dist:.1f})")
            
    # Check expl does not mention option letters
    expl = q['expl']
    bad_expl = re.findall(r'\b(?:letra|alternativa|op[çc][ãa]o|item)\s+[A-Ea-e]\b', expl, re.IGNORECASE)
    if bad_expl:
        errors.append(f"Q{idx}: expl mentions option letters: {bad_expl}")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print(" -", e)
else:
    print(f"Part 4 validation PASSED successfully! 31 questions verified.")
