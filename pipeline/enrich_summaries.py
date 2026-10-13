import json
import glob
import os
import re
from pathlib import Path

def enrich_summary_line(line: str, idx: int, total: int) -> str:
    line = line.strip()
    if line.startswith("- "):
        line = line[2:].strip()
    if line.startswith("* "):
        line = line[2:].strip()

    # If line already has an icon/callout marker, keep it clean
    if any(line.startswith(p) for p in ["###", "⚠️", "💡", "📌"]):
        return line

    lower = line.lower()

    # 1. Check for Attention / Caution / Warning signals
    is_attention = any(k in lower for k in [
        "cuidado", "atenção", "não confunda", "pegadinha", "exceção", "proibido",
        "vedado", "salvo", "exceto", "diferencial", "atrativa", "inversão", "anulação"
    ]) and not line.startswith("💡") and not line.startswith("📌")

    # 2. Check for Examples / Applications
    is_example = any(k in lower for k in [
        "exemplo", "exemplos", "ex.:", "como em \"", "como em '", "como no caso",
        "a exemplo de", "ilustra", "aplica-se a"
    ]) and not is_attention

    # 3. Check for Bizus / Mnemonics / Memory rules
    is_bizu = any(k in lower for k in [
        "bizu", "mnemônico", "memorize", "lembre-se", "regra de ouro",
        "dica de prova", "lista para memorizar", "macete"
    ])

    if is_bizu:
        if not re.search(r"^\*\*(Bizu|Mnemônico|Memorize|Dica)", line, re.I):
            return f"📌 **Bizu de Prova:** {line}"
        return f"📌 {line}"

    if is_attention and (idx >= total - 3 or "não confunda" in lower or "cuidado" in lower or "exceção" in lower):
        if not re.search(r"^\*\*(Atenção|Cuidado|Pegadinha|Importante)", line, re.I):
            # If line starts with **Termo**, convert to Attention
            return f"⚠️ **Ponto de Atenção:** {line}"
        return f"⚠️ {line}"

    if is_example and not line.startswith("💡"):
        if not re.search(r"^\*\*(Exemplo|Aplicação)", line, re.I):
            return f"💡 **Exemplo Prático:** {line}"
        return f"💡 {line}"

    return line

def process_file(file_path: str):
    data = json.load(open(file_path, "r", encoding="utf-8"))
    changed = False

    for seg in data.get("segments", []):
        bizu = seg.get("bizu")
        if not bizu:
            continue
        summary = bizu.get("summary", [])
        if not summary or not isinstance(summary, list):
            continue

        new_summary = []
        n = len(summary)
        for i, line in enumerate(summary):
            new_line = enrich_summary_line(str(line), i, n)
            new_summary.append(new_line)

        if new_summary != summary:
            bizu["summary"] = new_summary
            changed = True

    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
            f.write("\n")
    return changed

def main():
    root = Path(__file__).resolve().parents[1]
    items_dir = root / "content" / "items"
    files = sorted(items_dir.glob("*/*.json"))
    print(f"Processando {len(files)} arquivos de conteúdo...")

    updated = 0
    for f in files:
        if process_file(str(f)):
            updated += 1

    print(f"Concluído: {updated} arquivos atualizados em content/items.")

    # Sincronizar para web/content/items
    web_items = root / "web" / "content" / "items"
    if web_items.exists():
        import shutil
        shutil.rmtree(web_items)
    import shutil
    shutil.copytree(items_dir, web_items)
    print(f"Sincronizado com sucesso para web/content/items.")

if __name__ == "__main__":
    main()
