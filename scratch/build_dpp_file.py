# Generator script for 108 questions of Direito Processual Penal
import os
from pathlib import Path

target = Path("content/questoes/ineditas/mc/direito-processual-penal.txt")
target.parent.mkdir(parents=True, exist_ok=True)
print("Target file ready for creation.")
