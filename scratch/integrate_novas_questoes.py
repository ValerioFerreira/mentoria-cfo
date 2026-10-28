import re
import sys
from pathlib import Path

MC_DIR = Path("content/questoes/ineditas/mc")
NOVAS_DIR = Path("scratch/novas_questoes")

EXISTING_DISCS = [
    "contabilidade-geral",
    "informatica",
    "lingua-portuguesa",
    "estatistica",
    "matematica",
    "raciocinio-logico",
    "direito-administrativo",
    "direito-constitucional",
    "direito-penal",
]

NEW_DISCS = [
    "legislacao-pcpe",
    "direito-processual-penal",
    "legislacao-penal-especial",
]

def check_status():
    print("=== STATUS DAS DISCIPLINAS ===")
    for d in EXISTING_DISCS:
        f_nova = NOVAS_DIR / f"{d}.txt"
        if f_nova.exists():
            text = f_nova.read_text(encoding="utf-8")
            blocks = len(re.findall(r"^@@", text, re.M))
            print(f"  [PRONTO] {d}: {blocks} questões novas em {f_nova.name}")
        else:
            print(f"  [AGUARDANDO] {d}: arquivo novo ainda não gerado")
            
    for d in NEW_DISCS:
        f_mc = MC_DIR / f"{d}.txt"
        if f_mc.exists():
            text = f_mc.read_text(encoding="utf-8")
            blocks = len(re.findall(r"^@@", text, re.M))
            print(f"  [PRONTO] {d}: {blocks} questões geradas diretamente em {f_mc.name}")
        else:
            print(f"  [AGUARDANDO] {d}: arquivo ainda não gerado")

def apply_appends():
    for d in EXISTING_DISCS:
        f_nova = NOVAS_DIR / f"{d}.txt"
        if f_nova.exists():
            new_text = f_nova.read_text(encoding="utf-8").strip()
            if not new_text:
                continue
            target = MC_DIR / f"{d}.txt"
            cur_text = target.read_text(encoding="utf-8").strip()
            
            # Check if already appended
            first_block = new_text.split("@@")[1].strip() if "@@" in new_text else ""
            if first_block and first_block[:50] in cur_text:
                print(f"  [PULADO] {d}: conteúdo novo já parece constar em {target.name}")
                continue
                
            combined = cur_text + "\n\n" + new_text + "\n"
            target.write_text(combined, encoding="utf-8")
            print(f"  [ANEXADO] {d}: novas questões anexadas a {target.name}")

if __name__ == "__main__":
    if "--apply" in sys.argv:
        apply_appends()
    else:
        check_status()
