import fitz  # PyMuPDF
import sys

sys.stdout.reconfigure(encoding='utf-8')

PDF_PATH = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\docs\questoes\Caderno Informática e Constitucional 1.pdf"

doc = fitz.open(PDF_PATH)
print(f"Total de páginas: {len(doc)}")

for page_num in range(min(5, len(doc))):
    page = doc[page_num]
    text = page.get_text("text")
    print(f"\n--- PÁGINA {page_num + 1} ---")
    print(text[:2500])
