from pathlib import Path
import sys
sys.path.insert(0, str(Path("scratch/build_rl").resolve()))

from novas_bloco1 import QUESTOES_BLOCO1
from novas_bloco2 import QUESTOES_BLOCO2
from novas_bloco3 import QUESTOES_BLOCO3
from novas_bloco4 import QUESTOES_BLOCO4
from valida_novas import check_file

combined = QUESTOES_BLOCO1 + QUESTOES_BLOCO2 + QUESTOES_BLOCO3 + QUESTOES_BLOCO4

target_dir = Path("scratch/novas_questoes")
target_dir.mkdir(parents=True, exist_ok=True)
target_file = target_dir / "raciocinio-logico.txt"

lines = []
for q in combined:
    lines.append(f"@@ {q['seg']} | {q['ans']}")
    lines.append(q['stem'])
    for lbl, text in q['opts']:
        lines.append(f"{lbl}) {text}")
    lines.append(f"// Comentário: {q['expl']}\n")

target_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Arquivo gerado com sucesso em: {target_file}")
print(f"Total de questões gravadas: {len(combined)}")

print("\nExecutando validação completa no arquivo de destino:")
check_file(str(target_file))
