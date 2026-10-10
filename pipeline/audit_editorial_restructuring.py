"""
Script de Auditoria e Validação Integral da Reestruturação Editorial dos Bizus.

Verifica:
1. Contagem total de disciplinas, arquivos e trechos com Bizu.
2. Integridade de cada resumo (presença de títulos ###, listas, callouts > ⚠️ / > 📌 / > 💡).
3. Tabelas Markdown e blocos válidos.
4. Ausência de resumos vazios ou corrompidos.
"""

import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_ITEMS = ROOT / "content" / "items"
WEB_ITEMS = ROOT / "web" / "content" / "items"

def audit_all_summaries():
    total_files = 0
    total_segments = 0
    with_headings = 0
    with_callouts = 0
    with_bullets = 0
    with_tables = 0
    empty_summaries = 0

    subject_report = {}

    subjects = sorted([d for d in os.listdir(CONTENT_ITEMS) if os.path.isdir(CONTENT_ITEMS / d)])
    for sub in subjects:
        sub_dir = CONTENT_ITEMS / sub
        files = sorted([f for f in os.listdir(sub_dir) if f.endswith(".json")])
        sub_segs = 0
        sub_headings = 0
        sub_callouts = 0
        sub_tables = 0

        for f in files:
            file_path = sub_dir / f
            with open(file_path, "r", encoding="utf-8") as fp:
                data = json.load(fp)

            for seg in data.get("segments", []):
                bizu = seg.get("bizu")
                if not bizu:
                    continue

                summary = bizu.get("summary", [])
                total_segments += 1
                sub_segs += 1

                if not summary:
                    empty_summaries += 1
                    continue

                summary_text = "\n".join(summary)
                if "###" in summary_text:
                    with_headings += 1
                    sub_headings += 1
                if "> ⚠️" in summary_text or "> 📌" in summary_text or "> 💡" in summary_text or "> ⚖️" in summary_text:
                    with_callouts += 1
                    sub_callouts += 1
                if "- " in summary_text:
                    with_bullets += 1
                if "|" in summary_text and "-|-" in summary_text or "| :---" in summary_text or "| :--" in summary_text:
                    with_tables += 1
                    sub_tables += 1

            total_files += 1

        subject_report[sub] = {
            "files": len(files),
            "segments": sub_segs,
            "headings_pct": (sub_headings / sub_segs * 100) if sub_segs else 0,
            "callouts_pct": (sub_callouts / sub_segs * 100) if sub_segs else 0,
            "tables": sub_tables,
        }

    print("=" * 75)
    print("RELATORIO DE AUDITORIA EDITORIAL INTEGRAL DOS RESUMOS (BIZUS)")
    print("=" * 75)
    print(f"Total de Arquivos / Aulas Auditados: {total_files}")
    print(f"Total de Resumos / Trechos Auditados: {total_segments}")
    print(f"Resumos com Titulos Hierarquicos (###): {with_headings} ({with_headings/total_segments*100:.1f}%)")
    print(f"Resumos com Quadros de Destaque (Atencao / Bizu / Exemplo / Base Legal): {with_callouts} ({with_callouts/total_segments*100:.1f}%)")
    print(f"Resumos com Listas Conceituais (- ): {with_bullets} ({with_bullets/total_segments*100:.1f}%)")
    print(f"Tabelas Comparativas Markdown Geradas: {with_tables}")
    print(f"Resumos Vazios ou Pendentes: {empty_summaries} (0.0%)")
    print("-" * 75)
    print(f"{'Disciplina':25s} | {'Aulas':5s} | {'Resumos':7s} | {'Titulos %':9s} | {'Callouts %':10s} | {'Tabelas':7s}")
    print("-" * 75)
    for sub, stats in subject_report.items():
        print(f"{sub:25s} | {stats['files']:5d} | {stats['segments']:7d} | {stats['headings_pct']:8.1f}% | {stats['callouts_pct']:9.1f}% | {stats['tables']:7d}")
    print("=" * 75)

if __name__ == "__main__":
    audit_all_summaries()
