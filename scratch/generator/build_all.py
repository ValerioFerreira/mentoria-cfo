import sys
from pathlib import Path
from collections import Counter

# Add scratch/generator to sys.path
sys.path.insert(0, str(Path(__file__).parent))
from batch1 import QUESTIONS_BATCH_1
from batch2 import QUESTIONS_BATCH_2
from batch3 import QUESTIONS_BATCH_3

all_questions = QUESTIONS_BATCH_1 + QUESTIONS_BATCH_2 + QUESTIONS_BATCH_3
print(f"Total questions loaded: {len(all_questions)}")

target_file = Path("content/questoes/ineditas/mc/direito-penal.txt")
target_file.parent.mkdir(parents=True, exist_ok=True)

blocks = []
for i, q in enumerate(all_questions, 1):
    seg = q["seg"]
    ans = q["ans"]
    stem = q["stem"].strip()
    opts = q["opts"]
    expl = q["expl"].strip()
    
    # Validation checks
    assert len(opts) == 5, f"Q{i} does not have 5 options"
    letters = [o[:2] for o in opts]
    assert letters == ["A)", "B)", "C)", "D)", "E)"], f"Q{i} option prefixes incorrect: {letters}"
    
    # Strip prefixes for content check
    clean_opts = [o[3:].strip() for o in opts]
    ln = [len(c) for c in clean_opts]
    idx = "ABCDE".index(ans)
    right_len = ln[idx]
    avg_dist = (sum(ln) - right_len) / 4
    if right_len > 80 and right_len > 1.8 * avg_dist:
        print(f"WARNING: Q{i} ({seg}) correct option {ans} may be too long: len={right_len}, avg_dist={avg_dist:.1f}")

    opt_lines = "\n".join(opts)
    block = f"@@ {seg} | {ans}\n{stem}\n{opt_lines}\n// Comentário: {expl}\n"
    blocks.append(block)

content = "\n".join(blocks)
target_file.write_text(content, encoding="utf-8")
print(f"Successfully wrote {len(blocks)} questions to {target_file}")

# Check gabarito counts
counter = Counter(q["ans"] for q in all_questions)
print("Gabarito counts:", dict(counter))
