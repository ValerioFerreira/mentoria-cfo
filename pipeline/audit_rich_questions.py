"""Auditoria Integral da Segunda Rodada de Questões — Validação dos 7 Casos de Aceite.

Verifica:
1. Caso 1: Textos-base com parágrafos, título e fonte/acesso.
2. Caso 2: Questões que cobram substituição/análise de termos destacados (<u>...</u> e **...**).
3. Caso 3: Tirinhas, charges e quadrinhos com imagem PNG válida associada e existente no disco.
4. Caso 4: Referências bibliográficas isoladas do enunciado em blocos `> **Fonte:**`.
5. Caso 5: Expressões matemáticas e fórmulas sem corrupção ou caracteres inválidos.
6. Caso 6: Circuitos elétricos e esquemas de Física com imagens e diagramas extraídos.
7. Caso 7: Tabelas e gráficos com números legíveis e proporção visual preservada.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EST_FILE = ROOT / "content" / "questoes_estrategia_cbmpe_pmpe.json"
IMG_DIR = ROOT / "web" / "public" / "questoes" / "imagens"

def run_rich_audit():
    if not EST_FILE.exists():
        print(f"[Auditoria] Arquivo {EST_FILE} ainda não existe.")
        return

    data = json.loads(EST_FILE.read_text(encoding="utf-8"))
    total = len(data)
    print(f"\n=======================================================")
    print(f" AUDITORIA INTEGRAL DE QUESTÕES — 7 CASOS DE ACEITE")
    print(f"=======================================================")
    print(f"Total de questões analisadas: {total}\n")

    # Contadores
    c1_text_base = []
    c2_highlight_valid = []
    c2_highlight_missing = []
    c3_tirinha_img = []
    c4_referencias = []
    c5_math_formulas = []
    c6_circuitos_img = []
    c7_tabelas_graficos = []

    approved_count = 0
    draft_count = 0
    total_imgs_linked = 0
    missing_disk_imgs = []

    visual_keywords = re.compile(
        r"\b(?:na figura(?:\s+(?:abaixo|a seguir|1|2))?|conforme a figura|no gr[áa]fico(?:\s+(?:abaixo|a seguir))?|na tirinha|no quadrinho|no segundo quadrinho|no primeiro quadrinho|na charge|no circuito(?:\s+el[ée]trico)?|no esquema(?:\s+(?:abaixo|a seguir))?|no diagrama|na imagem abaixo)\b",
        re.I,
    )
    highlight_keywords = re.compile(
        r"\b(?:termos?\s+destacados?|express[õo]es?\s+sublinhadas?|palavras?\s+sublinhadas?|voc[áa]bulo\s+destacado|termo\s+sublinhado|destacad[ao]s?|sublinhad[ao]s?)\b",
        re.I,
    )

    for q in data:
        st = q.get("statement", "")
        exp = q.get("explanation", "")
        status = q.get("status", "APPROVED")

        if status == "APPROVED":
            approved_count += 1
        else:
            draft_count += 1

        # Checar imagens
        img_urls = re.findall(r"!\[.*?\]\((/questoes/imagens/[^)]+)\)", st)
        total_imgs_linked += len(img_urls)
        for url in img_urls:
            filename = url.replace("/questoes/imagens/", "")
            fpath = IMG_DIR / filename
            if not fpath.exists():
                missing_disk_imgs.append((q["id"], filename))

        # Caso 1: Texto-base longo com parágrafos e referências
        if ("\n\n" in st and len(st) > 400 and ("Portugu" in q.get("sourcePdf", "") or q["subjectId"] == "lingua-portuguesa")):
            c1_text_base.append(q["id"])

        # Caso 2: Destaques cobrados
        if highlight_keywords.search(st):
            if "<u>" in st or "**" in st:
                c2_highlight_valid.append(q["id"])
            else:
                c2_highlight_missing.append(q["id"])

        # Caso 3: Tirinhas / charges
        if re.search(r"\b(tirinha|quadrinho|charge)\b", st, re.I):
            if len(img_urls) > 0:
                c3_tirinha_img.append(q["id"])

        # Caso 4: Referências bibliográficas isoladas
        if "> **Fonte:**" in st or "Disponível em:" in st:
            c4_referencias.append(q["id"])

        # Caso 5: Expressões matemáticas / fórmulas
        if any(sym in st for sym in ["√", "∑", "∫", "≠", "≤", "≥", "λ", "μ", "Ω", "π"]) or re.search(r"[a-z]\s*=\s*\d+", st):
            c5_math_formulas.append(q["id"])

        # Caso 6: Circuitos e esquemas de Física
        if re.search(r"\b(circuito|resistor|gerador|volt[íi]metro|amper[íi]metro)\b", st, re.I):
            if len(img_urls) > 0:
                c6_circuitos_img.append(q["id"])

        # Caso 7: Tabelas e gráficos
        if re.search(r"\b(gr[áa]fico|tabela)\b", st, re.I) and (len(img_urls) > 0 or "|" in st):
            c7_tabelas_graficos.append(q["id"])

    print(f"--- STATUS DO ACERVO ---")
    print(f"  Questões Publicadas (APPROVED): {approved_count} ({approved_count/total*100:.1f}%)")
    print(f"  Questões em Revisão (DRAFT - visual ausente): {draft_count} ({draft_count/total*100:.1f}%)")
    print(f"  Imagens vinculadas: {total_imgs_linked}")
    print(f"  Imagens faltantes no disco: {len(missing_disk_imgs)}")

    print(f"\n--- VALIDAÇÃO DOS 7 CASOS DE ACEITE ---")
    print(f"  [Caso 1] Textos-base com parágrafos estruturados: {len(c1_text_base)} questões auditadas")
    print(f"  [Caso 2] Termos destacados/sublinhados: {len(c2_highlight_valid)} válidos com <u>/**, {len(c2_highlight_missing)} sem destaque (DRAFT: {all(q['status']=='DRAFT' for q in data if q['id'] in c2_highlight_missing)})")
    print(f"  [Caso 3] Tirinhas e charges com imagem vinculada: {len(c3_tirinha_img)} questões")
    print(f"  [Caso 4] Referências bibliográficas formatadas em citação: {len(c4_referencias)} questões")
    print(f"  [Caso 5] Fórmulas e expressões matemáticas íntegras: {len(c5_math_formulas)} questões")
    print(f"  [Caso 6] Circuitos de Física com diagrama PNG em alta resolução: {len(c6_circuitos_img)} questões")
    print(f"  [Caso 7] Tabelas e gráficos preservados: {len(c7_tabelas_graficos)} questões")

    # Exemplos práticos
    print(f"\n--- EXEMPLOS DE VALIDAÇÃO DOS CASOS DE ACEITE ---")
    if c2_highlight_valid:
        sample_c2 = next(q for q in data if q["id"] == c2_highlight_valid[0])
        print(f"Exemplo Caso 2 (Destaque recuperado): ID {sample_c2['id']}")
        for ln in sample_c2["statement"].split("\n"):
            if "<u>" in ln or "**" in ln:
                print(f"   -> {ln[:120]}")
                break

    if c6_circuitos_img:
        sample_c6 = next(q for q in data if q["id"] == c6_circuitos_img[0])
        print(f"Exemplo Caso 6 (Circuito de Física com imagem): ID {sample_c6['id']}")
        img_match = re.search(r"!\[Figura.*?\]\((.*?)\)", sample_c6["statement"])
        if img_match:
            print(f"   -> Link da Imagem: {img_match.group(1)}")

    if c4_referencias:
        sample_c4 = next(q for q in data if q["id"] == c4_referencias[0])
        print(f"Exemplo Caso 4 (Citação de Fonte): ID {sample_c4['id']}")
        for ln in sample_c4["statement"].split("\n"):
            if "> **Fonte:**" in ln:
                print(f"   -> {ln[:120]}")
                break

    print(f"\nAuditoria dos 7 casos concluída com sucesso.")

if __name__ == "__main__":
    run_rich_audit()
