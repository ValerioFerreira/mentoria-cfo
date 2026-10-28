import sys
from pathlib import Path
sys.path.insert(0, str(Path("scratch/build_rl").resolve()))
from novas_bloco2 import QUESTOES_BLOCO2

# Combined index 62 -> Bloco 2 index 62 - 44 = 18 (since bloco 1 has 43 questions, 1-based #62 is combined[61], so bloco2[61-43 = 18])
indices = [18, 22, 28, 30, 31, 32, 33]
for idx in indices:
    if idx < len(QUESTOES_BLOCO2):
        q = QUESTOES_BLOCO2[idx]
        print(f"=== IDX {idx} (Q#{43 + idx + 1}, seg {q['seg']}) ===")
        print("STEM:", q["stem"])
        print("EXPL:", q["expl"])
