import json
import sys
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from textutil import aula_key_map, load_pages

data = json.load(open(ROOT / "scratch/rotulos_analysis.json", encoding="utf-8"))
keymap = aula_key_map()

out = []
for item in data:
    sid = item["sid"]
    disc, aula, s_num = sid.split("/")
    aula_id = f"{disc}/{aula}"
    sp = item["sp"]
    k = keymap.get(aula_id)
    if not k:
        continue
    p_data = load_pages(k)
    p_map = {p["n"]: p["text"] for p in p_data.get("pages", [])}
    
    out.append(f"==================================================")
    out.append(f"ID: {sid} | Pág: {sp}-{item['ep']} | Score: {item['score']}")
    out.append(f"START_TOPIC ATUAL: {item['current_startTopic']}")
    out.append(f"TOPICS NO INTERVALO [{sp-1}..{sp+2}]:")
    for t in item["topics_around"]:
        out.append(f"   p.{t[0]} (lvl {t[1]}): {t[2]}")
    out.append(f"--- TEXTO PÁG {sp} (primeiras 12 linhas) ---")
    lines_sp = [l.strip() for l in p_map.get(sp, "").splitlines() if l.strip()]
    for l in lines_sp[:12]:
        out.append(f"   {l}")
    out.append(f"--- TEXTO PÁG {sp+1} (primeiras 8 linhas) ---")
    lines_sp1 = [l.strip() for l in p_map.get(sp+1, "").splitlines() if l.strip()]
    for l in lines_sp1[:8]:
        out.append(f"   {l}")

(ROOT / "scratch/candidates_detail.txt").write_text("\n".join(out), encoding="utf-8")
print("Escrito com sucesso em UTF-8.")
