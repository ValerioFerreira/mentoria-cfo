from pathlib import Path
import sys
sys.path.insert(0, str(Path("scratch/build_rl").resolve()))

from novas_bloco1 import QUESTOES_BLOCO1
from novas_bloco2 import QUESTOES_BLOCO2
from novas_bloco3 import QUESTOES_BLOCO3
from novas_bloco4 import QUESTOES_BLOCO4
from valida_novas import check_file

combined = QUESTOES_BLOCO1 + QUESTOES_BLOCO2 + QUESTOES_BLOCO3 + QUESTOES_BLOCO4
print(f"Bloco 1: {len(QUESTOES_BLOCO1)}")
print(f"Bloco 2: {len(QUESTOES_BLOCO2)}")
print(f"Bloco 3: {len(QUESTOES_BLOCO3)}")
print(f"Bloco 4: {len(QUESTOES_BLOCO4)}")
print(f"Total combinado: {len(combined)}")

lines = []
for q in combined:
    lines.append(f"@@ {q['seg']} | {q['ans']}")
    lines.append(q['stem'])
    for lbl, text in q['opts']:
        lines.append(f"{lbl}) {text}")
    lines.append(f"// Comentário: {q['expl']}\n")

tmp_path = Path("scratch/build_rl/tmp_test.txt")
tmp_path.write_text("\n".join(lines), encoding="utf-8")
print(f"\nGerado {tmp_path} com {len(combined)} questões.")
check_file(str(tmp_path))
