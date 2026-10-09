import json
import sys
from pathlib import Path

# Força stdout para utf-8
sys.stdout.reconfigure(encoding='utf-8')

p = Path(r"C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits\consolidated_audit.json")
data = json.loads(p.read_text(encoding="utf-8"))

print("="*80)
print("AUDITORIA CONSOLIDADA DE DIRETRIZES E QUESTÕES - CFO-BM MENTORIA (PÓS-SANEAMENTO)")
print("="*80)

print("\n1. RESUMO DAS QUESTÕES POR AMOSTRAGEM (1.000 questões)")
tot_sampled_q = sum(v["total_sampled"] for v in data["questoes_amostra"].values())
tot_ok_q = sum(v["total_ok"] for v in data["questoes_amostra"].values())
print(f"Total: {tot_sampled_q} | 100% Conformes: {tot_ok_q} ({tot_ok_q/tot_sampled_q*100:.1f}%) | Apontamentos: {tot_sampled_q - tot_ok_q}")
for k, v in data["questoes_amostra"].items():
    print(f" - {v['title']}: {v['total_ok']}/{v['total_sampled']} OK ({v['total_ok']/v['total_sampled']*100:.1f}%). Issues: {v['summary_by_category']}")

print("\n2. RESUMO DA VARREDURA GLOBAL (10.332 QUESTÕES)")
vg = data["varredura_global"]
print(f"Total de questões: {vg['total_questions_scanned']}")
print(f"Total de não-conformidades: {vg['total_issues_found']}")
for cat, cnt in vg["issues_by_category"].items():
    print(f" - {cat}: {cnt} ocorrências")
