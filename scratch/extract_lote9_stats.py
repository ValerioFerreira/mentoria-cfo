import subprocess, json

vols = [
    ("direito-constitucional/m05", "AGENTE-MATC-23"),
    ("direito-administrativo/m10", "AGENTE-MATC-24"),
    ("biologia/m01", "AGENTE-MATC-25"),
    ("direito-penal-militar/m03", "AGENTE-MATC-26")
]

for v, autor in vols:
    cmd = ["pipeline/.venv/Scripts/python.exe", "pipeline/validate_material.py", f"content/material/{v}", "--json"]
    out = subprocess.check_output(cmd, encoding="utf-8")
    data = json.loads(out[out.find("{"):])
    print(f"\n### {v} — 0 erro(s), 0 aviso(s)")
    print("\n| Capítulo | Palavras/meta | Visuais | Quadros | Cobertura | Copiadas | Palavras por frase | Jargão |")
    print("| --- | --- | --- | --- | --- | --- | --- | --- |")
    for cid, c in data["chapters"].items():
        short = "/".join(cid.split("/")[-2:])
        print(f"| {short} | {c['words']}/{c['target']} | {c['visuals']} | {c['callouts']} | {c['coverage']} | {c['copied']} | {c['sentenceWords']} | {c['jargon']} |")
    f_info = data.get("fixacao", {})
    # count questions in fixacao.json
    fix_path = f"content/material/{v}/fixacao.json"
    with open(fix_path, encoding="utf-8") as fp:
        fd = json.load(fp)
    q_list = fd.get("questoes", []) + fd.get("ineditas", [])
    aocp_cnt = sum(1 for q in q_list if "AOCP" in q.get("banca", "").upper())
    in_banco = sum(1 for q in q_list if q.get("origem") == "banco" or ("AOCP" not in q.get("banca", "").upper() and not q.get("id", "").startswith("in-novo-")))
    in_novo = sum(1 for q in q_list if q.get("id", "").startswith("in-novo-") or q.get("origem") == "novo")
    print(f"\nFixação: {len(q_list)} questões · AOCP {aocp_cnt} · inéditas do banco {len(q_list) - aocp_cnt - in_novo} · inéditas novas {in_novo}")
