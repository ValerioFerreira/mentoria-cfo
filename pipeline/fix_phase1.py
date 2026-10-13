#!/usr/bin/env python3
"""Fase 1: Correção de Encoding Corrompido, Palavras Duplicadas e Itens C/E
"""
import os
import json
import re
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
ITEMS_DIR = ROOT / "content" / "items"

# Mapeamentos comuns de caracteres corrompidos
ENCODING_REPLACEMENTS = {
    "\ufffd": "", # caractere de substituição desconhecido
    "Ã©": "é",
    "Ã£": "ã",
    "Ã§": "ç",
    "Ã¡": "á",
    "Ã³": "ó",
    "Ãº": "ú",
    "Ãª": "ê",
    "Ã": "í",
    "â\x80\x93": "–",
    "â\x80\x94": "—",
    "â\x80\x9c": '"',
    "â\x80\x9d": '"',
    "â\x80\x98": "'",
    "â\x80\x99": "'",
}

# Regex para duplicidades de palavras
DUPLICATE_WORDS_RE = re.compile(
    r"\b(o|a|os|as|um|uma|de|do|da|dos|das|em|no|na|nos|nas|por|para|com|que|e|ou|se)\s+\1\b",
    re.IGNORECASE
)

def clean_text(text):
    if not isinstance(text, str):
        return text
    
    res = text
    for bad, good in ENCODING_REPLACEMENTS.items():
        if bad in res:
            res = res.replace(bad, good)
            
    # Corrige duplicações de conectivos ("de de" -> "de", "o o" -> "o")
    # Cuidado para não quebrar casos intencionais em linguística se houver
    def repl(m):
        return m.group(1)
    
    res = DUPLICATE_WORDS_RE.sub(repl, res)
    return res

def clean_ce_explanation(stmt, is_true, expl):
    if not isinstance(expl, str):
        return expl
    # Se is_true é False e a explicação começa direto com "O correto é...", ajusta para "Incorreto. O correto é..." ou "Item falso. O correto é..."
    expl_clean = expl.strip()
    if is_true is False:
        if re.match(r"^(O correto [eé]|A forma correta [eé]|O desenvolvimento correto [eé]|O certo [eé]|Correto [eé]|A correspond[eê]ncia exata [eé])\b", expl_clean, re.I):
            expl_clean = f"Item falso. {expl_clean}"
    return expl_clean

def main():
    print("Iniciando Fase 1: Saneamento de Encoding, Duplicações de Texto e Clarificação C/E...")
    total_files = 0
    modified_files = 0
    total_cleaned_enc = 0
    total_cleaned_dup = 0
    total_cleaned_ce = 0

    for fpath in sorted(ITEMS_DIR.glob("*/*.json")):
        total_files += 1
        raw_text = fpath.read_text(encoding="utf-8")
        data = json.loads(raw_text)
        is_modified = False

        for seg in data.get("segments", []):
            # 1. Limpa Bizu
            bizu = seg.get("bizu", {})
            if "summary" in bizu:
                new_sum = []
                for s in bizu["summary"]:
                    c = clean_text(s)
                    if c != s:
                        is_modified = True
                        total_cleaned_dup += 1
                    new_sum.append(c)
                bizu["summary"] = new_sum

            for set_name in ["teoria", "revisao"]:
                for item in bizu.get(set_name, []):
                    st = item.get("statement", "")
                    ex = item.get("explanation", "")
                    is_tr = item.get("isTrue")
                    
                    new_st = clean_text(st)
                    new_ex = clean_text(ex)
                    new_ex = clean_ce_explanation(new_st, is_tr, new_ex)

                    if new_st != st or new_ex != ex:
                        is_modified = True
                        if new_ex != ex:
                            total_cleaned_ce += 1
                        item["statement"] = new_st
                        item["explanation"] = new_ex

            # 2. Limpa Questões
            for q in seg.get("questions", []):
                st = q.get("statement", "")
                ex = q.get("explanation", "")
                sup = q.get("support")
                opts = q.get("options", [])

                new_st = clean_text(st)
                new_ex = clean_text(ex)
                new_sup = clean_text(sup) if sup else None
                new_opts = [clean_text(o) for o in opts]

                if new_st != st:
                    is_modified = True
                    total_cleaned_dup += 1
                    q["statement"] = new_st
                if new_ex != ex:
                    is_modified = True
                    q["explanation"] = new_ex
                if new_sup != sup:
                    is_modified = True
                    q["support"] = new_sup
                if new_opts != opts:
                    is_modified = True
                    total_cleaned_dup += 1
                    q["options"] = new_opts

        if is_modified:
            modified_files += 1
            fpath.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Arquivos processados: {total_files} | Arquivos modificados: {modified_files}")
    print(f"Duplicações/Encodings corrigidos: {total_cleaned_dup}")
    print(f"Explicações C/E clarificadas: {total_cleaned_ce}")

if __name__ == "__main__":
    main()
