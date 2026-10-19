import json
import subprocess
import sys

def main():
    main_raw = subprocess.check_output(["git", "show", "main:content/importance/segments.json"], encoding="utf-8")
    main_doc = json.loads(main_raw)
    
    with open("content/importance/segments.json", encoding="utf-8") as f:
        curr_doc = json.load(f)
    
    main_contests = ["CBMPE_OFICIAL", "CBMPE_SOLDADO", "PMPE_OFICIAL", "PMPE_SOLDADO"]
    main_segs = main_doc["segments"]
    curr_segs = curr_doc["segments"]
    
    print(f"Total trechos na main: {len(main_segs)}")
    print(f"Total trechos no curr: {len(curr_segs)}")
    
    # 1. Verifica os 897 trechos antigos para cada concurso da main
    mismatches = []
    for sid, m_rec in main_segs.items():
        if sid not in curr_segs:
            mismatches.append(f"{sid}: ausente no curr")
            continue
        c_rec = curr_segs[sid]
        for c in main_contests:
            m_c = m_rec["contests"].get(c, {})
            c_c = c_rec["contests"].get(c, {})
            
            if m_c.get("appears") != c_c.get("appears"):
                mismatches.append(f"{sid} [{c}] appears: main={m_c.get('appears')} curr={c_c.get('appears')}")
            elif m_c.get("expected") != c_c.get("expected"):
                mismatches.append(f"{sid} [{c}] expected: main={m_c.get('expected')} curr={c_c.get('expected')}")
            elif m_c.get("score") != c_c.get("score"):
                mismatches.append(f"{sid} [{c}] score: main={m_c.get('score')} curr={c_c.get('score')}")
    
    print(f"Discrepâncias nos 897 trechos antigos para CBMPE e PMPE: {len(mismatches)}")
    if mismatches:
        for m in mismatches[:20]:
            print("  ", m)
        return 1

    # 2. Verifica se os 245 trechos novos aparecem como appears: False em CBMPE e PMPE
    new_leaks = []
    for sid, c_rec in curr_segs.items():
        if sid not in main_segs:
            for c in main_contests:
                if c_rec["contests"].get(c, {}).get("appears") is True:
                    new_leaks.append(f"{sid} vazou para {c}")
    
    print(f"Trechos novos vazando para CBMPE/PMPE: {len(new_leaks)}")
    if new_leaks:
        for leak in new_leaks[:20]:
            print("  ", leak)
        return 1
    
    # 3. Estatísticas de PCPE_AGENTE
    pcpe_segs = [sid for sid, r in curr_segs.items() if r["contests"].get("PCPE_AGENTE", {}).get("appears")]
    print(f"Trechos ativos em PCPE_AGENTE: {len(pcpe_segs)}")
    
    print("VERIFICAÇÃO DE IMPORTÂNCIA 100% APROVADA: IDÊNTICA À MAIN PARA CBMPE E PMPE!")
    return 0

if __name__ == "__main__":
    sys.exit(main())
