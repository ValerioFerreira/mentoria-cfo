import re
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")

def check_file(path_str: str):
    path = Path(path_str)
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    blocks = re.split(r"(?m)^@@ ", text)[1:]
    print(f"Total de blocos encontrados: {len(blocks)}")
    
    errs = []
    gabs = []
    seen = {}
    
    for n, block in enumerate(blocks, 1):
        head, _, body = block.partition("\n")
        m = re.fullmatch(r"\s*(\S+)\s*\|\s*([A-E])\s*(?:\|\s*item=(\S+)\s*)?", head)
        if not m:
            errs.append(f"#{n}: cabeçalho inválido: {head!r}")
            continue
        seg, ans, item = m.groups()
        gabs.append(ans)
        
        main, _, expl = body.partition("\n//")
        parts = re.split(r"(?m)^([A-E])\)\s*", main.strip())
        stem = parts[0].strip()
        opts = [(parts[i], " ".join(parts[i + 1].split())) for i in range(1, len(parts) - 1, 2)]
        
        tag = f"#{n} ({seg})"
        
        if [l for l, _ in opts] != list("ABCDE"):
            errs.append(f"{tag}: precisa de exatamente 5 alternativas A) a E) em ordem")
            continue
        
        if not re.search(r"assinale|julgue|indique", stem, re.I):
            errs.append(f"{tag}: enunciado sem comando ('assinale', 'julgue', 'indique')")
        
        w = len(stem.split())
        if not 6 <= w <= 140:
            errs.append(f"{tag}: enunciado com {w} palavras (esperado 6-140)")
        
        texts = [t for _, t in opts]
        if any(len(t.split()) < 1 for t in texts) or len({t.lower() for t in texts}) < 5:
            errs.append(f"{tag}: alternativas vazias ou repetidas")
        
        if len(expl.split()) < 5:
            errs.append(f"{tag}: comentário ausente ou curto (< 5 palavras)")
        
        # Verificar mencao a letras no comentario
        if re.search(r"\b(letra\s+[A-E]|alternativa\s+[A-E]|opção\s+[A-E])\b", expl, re.I):
            errs.append(f"{tag}: comentário cita letra de alternativa ({re.findall(r'\b(?:letra|alternativa|opção)\s+[A-E]\b', expl, re.I)})")
        
        # Tamanho da correta
        ln = [len(t) for t in texts]
        right = ln["ABCDE".index(ans)]
        avg_dist = (sum(ln) - right) / 4
        if right > 1.8 * avg_dist and right > 80:
            errs.append(f"{tag}: alternativa correta muito longa ({right} > 1.8 * {avg_dist:.1f})")
            
        key = re.sub(r"\W+", " ", stem.lower()).strip()
        if key in seen:
            errs.append(f"{tag}: enunciado repetido com {seen[key]}")
        seen[key] = tag

    print("\n--- RESUMO DA VALIDAÇÃO ---")
    print(f"Total de questões: {len(blocks)}")
    print("Contagem de gabaritos:", Counter(gabs))
    if errs:
        print(f"\nENCONTRADOS {len(errs)} ERROS:")
        for e in errs[:30]:
            print("ERRO:", e)
        if len(errs) > 30:
            print(f"... e mais {len(errs) - 30} erros")
    else:
        print("ZERO ERROS! Arquivo 100% em conformidade com as regras.")

if __name__ == "__main__":
    p = sys.argv[1] if len(sys.argv) > 1 else "scratch/novas_questoes/raciocinio-logico.txt"
    check_file(p)
