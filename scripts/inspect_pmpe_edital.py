import sys
import pypdf

sys.stdout.reconfigure(encoding="utf-8")

reader = pypdf.PdfReader("docs/pmpe.pdf")
print("Total páginas:", len(reader.pages))

full_text = []
for idx, page in enumerate(reader.pages):
    text = page.extract_text() or ""
    full_text.append(f"--- PÁGINA {idx+1} ---\n" + text)

with open("backups/pmpe_edital_texto.txt", "w", encoding="utf-8") as f:
    f.write("\n\n".join(full_text))

print("Texto completo salvo em backups/pmpe_edital_texto.txt")
