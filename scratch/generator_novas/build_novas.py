import json
import re
from collections import Counter
from pathlib import Path

from part1 import QUESTIONS_PART_1
from part2 import QUESTIONS_PART_2
from part3 import QUESTIONS_PART_3
from part4 import QUESTIONS_PART_4

ALL_QUESTIONS = QUESTIONS_PART_1 + QUESTIONS_PART_2 + QUESTIONS_PART_3 + QUESTIONS_PART_4

print(f"Total questions loaded: {len(ALL_QUESTIONS)}")
assert len(ALL_QUESTIONS) == 123, f"Expected 123, got {len(ALL_QUESTIONS)}"

with open('scratch/plan_123.json', 'r', encoding='utf-8') as f:
    plan = json.load(f)

with open('scratch/trechos_fracos/direito-penal.json', 'r', encoding='utf-8') as f:
    trechos_fracos = json.load(f)

expected_counts_per_seg = {item['seg']: item['faltam'] for item in trechos_fracos}

command_words = ["assinale", "julgue", "indique", "marque", "escolha"]
errors = []

actual_counts_per_seg = Counter()
gabarito_counts = Counter()
consecutive_ans = []

for i, (q, p) in enumerate(zip(ALL_QUESTIONS, plan)):
    idx = p['idx']
    seg = p['seg']
    ans = p['ans']
    
    actual_counts_per_seg[q['seg']] += 1
    gabarito_counts[q['ans']] += 1
    consecutive_ans.append(q['ans'])
    
    if q['seg'] != seg:
        errors.append(f"Q{idx}: segment mismatch {q['seg']} != {seg}")
    if q['ans'] != ans:
        errors.append(f"Q{idx}: answer mismatch {q['ans']} != {ans}")
        
    stem = q['stem'].strip()
    words = stem.split()
    if not (6 <= len(words) <= 140):
        errors.append(f"Q{idx}: stem word count {len(words)} not in [6, 140]")
    if not any(cw in stem.lower() for cw in command_words):
        errors.append(f"Q{idx}: stem missing command word")
        
    opts = q['opts']
    if len(opts) != 5:
        errors.append(f"Q{idx}: options count {len(opts)} != 5")
    
    letters = [opt[:2] for opt in opts]
    if letters != ['A)', 'B)', 'C)', 'D)', 'E)']:
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
    expl = q['expl'].strip()
    bad_expl = re.findall(r'\b(?:letra|alternativa|op[çc][ãa]o|item)\s+[A-Ea-e]\b', expl, re.IGNORECASE)
    if bad_expl:
        errors.append(f"Q{idx}: expl mentions option letters: {bad_expl}")

# Check consecutive answers
max_consec = 1
curr_consec = 1
for i in range(1, len(consecutive_ans)):
    if consecutive_ans[i] == consecutive_ans[i-1]:
        curr_consec += 1
        if curr_consec > max_consec:
            max_consec = curr_consec
    else:
        curr_consec = 1
if max_consec > 2:
    errors.append(f"Max consecutive identical answers {max_consec} > 2")

# Check segment counts
for s, expected in expected_counts_per_seg.items():
    actual = actual_counts_per_seg.get(s, 0)
    if actual != expected:
        errors.append(f"Segment {s}: count mismatch (actual={actual}, expected={expected})")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print(" -", e)
    raise SystemExit(1)

print("All validations PASSED!")
print(f"Gabarito counts: {dict(gabarito_counts)}")
print(f"Segments matched: {len(actual_counts_per_seg)} / {len(expected_counts_per_seg)}")
print(f"Max consecutive identical answers: {max_consec}")

# Assemble into scratch/novas_questoes/direito-penal.txt
out_dir = Path("scratch/novas_questoes")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "direito-penal.txt"

lines = []
for q in ALL_QUESTIONS:
    lines.append(f"@@ {q['seg']} | {q['ans']}")
    lines.append(q['stem'].strip())
    for opt in q['opts']:
        lines.append(opt.strip())
    lines.append(f"// Comentário: {q['expl'].strip()}")
    lines.append("") # blank line between questions

content = "\n".join(lines).strip() + "\n"

with open(out_file, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Successfully generated {out_file} with {len(ALL_QUESTIONS)} questions!")
