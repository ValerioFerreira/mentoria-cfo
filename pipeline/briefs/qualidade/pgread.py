"""Uso: python pgread.py <aula> <pagina> [<pagina_final>]   ex.: python pgread.py quimica/a17 29 31
Imprime o texto (limpo, do cache) das páginas do PDF dessa aula. Página = a do leitor de PDF (a da diretriz)."""
import json, sys, glob
sys.stdout.reconfigure(encoding="utf-8")
aula, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]) if len(sys.argv) > 3 else int(sys.argv[2])
root = r"C:\Users\Administrador\Documents\Projetos\CFO-BM\pipeline\.cache\pages"
for f in glob.glob(root + r"\*.json"):
    d = json.load(open(f, encoding="utf-8"))
    if d["aula"] == aula:
        for p in d["pages"]:
            if a <= p["n"] <= b:
                print(f"\n===== {aula} pág. {p['n']} =====\n{p['text']}")
        break
else:
    print("aula não encontrada no cache")
