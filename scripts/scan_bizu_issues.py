import glob
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

patterns = {
    "metalinguagem_questao": r"\b(quando\s+a\s+quest[aã]o|se\s+a\s+quest[aã]o|na\s+quest[aã]o|conforme\s+a\s+quest[aã]o|o\s+examinador|a\s+banca|o\s+item\s+a\s+seguir|assinale|marque)\b",
    "referencia_a_texto_ausente": r"^(segundo\s+o\s+texto|conforme\s+o\s+texto|de\s+acordo\s+com\s+o\s+texto|no\s+texto|o\s+autor\s+afirma|o\s+texto\s+defende)\b",
    "termina_com_dois_pontos": r":$",
    "inicia_com_minuscula": r"^[a-z]",
    "truncamento_ou_reticencias": r"(\.\.\.|\.\s*$|;\s*$)",
}

findings = {k: [] for k in patterns}
total_items = 0

for f in sorted(glob.glob("content/items/*/*.json")):
    d = json.load(open(f, encoding="utf-8"))
    for seg in d.get("segments", []):
        seg_id = seg.get("id", "")
        bizu = seg.get("bizu", {})
        for s_name in ["teoria", "revisao"]:
            items = bizu.get(s_name, [])
            for idx, it in enumerate(items):
                total_items += 1
                st = it.get("statement", "").strip()
                exp = it.get("explanation", "").strip()
                is_true = it.get("isTrue", True)

                for k, pat in patterns.items():
                    flags = 0 if k == "inicia_com_minuscula" else re.IGNORECASE
                    if re.search(pat, st, flags):
                        findings[k].append({
                            "id": f"{seg_id}#{s_name}#{idx}",
                            "file": f,
                            "statement": st,
                            "isTrue": is_true,
                            "explanation": exp,
                        })

print(f"Total de itens inspecionados: {total_items}")
for k, flist in findings.items():
    print(f"  {k:30s}: {len(flist)} ocorrências")

# Salvar detalhamento dos itens encontrados para cruzar com subagentes
with open("pipeline/.cache/preliminary_bizu_flaws.json", "w", encoding="utf-8") as out:
    json.dump(findings, out, ensure_ascii=False, indent=2)

print("\nRelatório preliminar salvo em pipeline/.cache/preliminary_bizu_flaws.json")
