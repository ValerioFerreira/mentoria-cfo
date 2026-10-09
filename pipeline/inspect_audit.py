import json
from pathlib import Path

p = Path(r"C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits\consolidated_audit.json")
data = json.loads(p.read_text(encoding="utf-8"))

print("="*80)
print("AUDITORIA CONSOLIDADA DE DIRETRIZES E QUESTÕES - CFO-BM MENTORIA")
print("="*80)

print("\n1. RESUMO DOS 5 LOTES DE DIRETRIZES (500 trechos amostrados confrontados com PDFs)")
tot_sampled_d = sum(v["total_sampled"] for v in data["diretrizes"].values())
tot_ok_d = sum(v["total_ok"] for v in data["diretrizes"].values())
print(f"Total Auditado: {tot_sampled_d} trechos | Conformes: {tot_ok_d} ({tot_ok_d/tot_sampled_d*100:.1f}%) | Com Apontamentos: {tot_sampled_d - tot_ok_d}")

for k, v in data["diretrizes"].items():
    print(f" - {v['title']}: {v['total_ok']}/{v['total_sampled']} conformes ({v['total_ok']/v['total_sampled']*100:.1f}%). Categorias: {v['summary_by_category']}")

print("\n2. RESUMO DOS 5 LOTES DE QUESTÕES (1.000 questões amostradas)")
tot_sampled_q = sum(v["total_sampled"] for v in data["questoes_amostra"].values())
tot_ok_q = sum(v["total_ok"] for v in data["questoes_amostra"].values())
print(f"Total Auditado: {tot_sampled_q} questões | Conformes: {tot_ok_q} ({tot_ok_q/tot_sampled_q*100:.1f}%) | Com Apontamentos: {tot_sampled_q - tot_ok_q}")

for k, v in data["questoes_amostra"].items():
    print(f" - {v['title']}: {v['total_ok']}/{v['total_sampled']} conformes ({v['total_ok']/v['total_sampled']*100:.1f}%). Categorias: {v['summary_by_category']}")

print("\n3. RESUMO DA VARREDURA GLOBAL DAS 10.332 QUESTÕES")
vg = data["varredura_global"]
print(f"Total de questões escaneadas: {vg['total_questions_scanned']}")
print(f"Total de não-conformidades encontradas: {vg['total_issues_found']}")
for cat, cnt in vg["issues_by_category"].items():
    print(f" - {cat}: {cnt} ocorrências")

print("\n4. EXEMPLOS DOS ACHADOS MAIS RELEVANTES")
print("\n[A] Itens C/E com possível inconsistência de gabarito/explicação:")
ce_count = 0
for k, v in data["diretrizes"].items():
    for f in v["findings"]:
        if f["category"] == "ce_gabarito" and ce_count < 8:
            print(f" -> {f['segmentId']} ({f['pages']}): {f['evidence']}")
            ce_count += 1

print("\n[B] Questões com encoding corrompido:")
for s in vg["samples"].get("encoding_corrompido", [])[:6]:
    print(f" -> {s['id']} [{s['subject']}]: {s['evidence']}")

print("\n[C] Questões com alternativas duplicadas (amostra):")
for s in vg["samples"].get("alternativas_duplicadas", [])[:6]:
    print(f" -> {s['id']} [{s['subject']}]: {s['evidence']}")
