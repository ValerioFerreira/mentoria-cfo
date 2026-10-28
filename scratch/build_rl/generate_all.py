"""Script para compilar e validar todas as questoes de raciocinio logico."""
from pathlib import Path
import subprocess
import sys

# Importa lotes disponiveis
from lote1 import QUESTOES as LOTE1
from lote2 import QUESTOES as LOTE2
from lote3 import QUESTOES as LOTE3
from lote4 import QUESTOES as LOTE4
from lote5 import QUESTOES as LOTE5

ALL_QUESTOES = []
ALL_QUESTOES.extend(LOTE1)
ALL_QUESTOES.extend(LOTE2)
ALL_QUESTOES.extend(LOTE3)
ALL_QUESTOES.extend(LOTE4)
ALL_QUESTOES.extend(LOTE5)

lines = []
for q in ALL_QUESTOES:
    lines.append(f"@@ {q['seg']} | {q['ans']}")
    lines.append(q['stem'])
    for lbl, text in q['opts']:
        lines.append(f"{lbl}) {text}")
    lines.append(f"// Comentário: {q['expl']}\n")

out_file = Path('content/questoes/ineditas/mc/raciocinio-logico.txt')
out_file.write_text("\n".join(lines), encoding="utf-8")
print(f"Arquivo gerado com {len(ALL_QUESTOES)} questoes em {out_file}")

# Executa validacao
res = subprocess.run(
    [sys.executable, "pipeline/questoes/ineditas_mc_nativas.py", "--check"],
    capture_output=True,
    text=True,
    encoding="utf-8"
)
print("--- VALIDACAO ineditas_mc_nativas.py ---")
print(res.stdout)
if res.stderr:
    print("STDERR:", res.stderr)
