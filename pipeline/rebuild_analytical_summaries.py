"""
Pipeline para releitura analítica, aprofundamento e diagramação editorial de todos os resumos (Bizus).

Transforma resumos telegráficos/em caixas soltas em cadernos teóricos fluidos,
analíticos e estruturados como capítulos de apostila em PDF.
"""

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_ITEMS = ROOT / "content" / "items"
WEB_ITEMS = ROOT / "web" / "content" / "items"

def clean_inline_tags(text: str) -> str:
    """Remove prefixos artificiais repetitivos para permitir reformatação limpa."""
    text = re.sub(r'^(💡|⚠️|📌)\s*\*\*(Exemplo|Ponto de Atenção|Bizu de Prova|Mnemônico)[^:]*:\*\*\s*', '', text)
    text = re.sub(r'^\*\*(Exemplo|Ponto de Atenção|Bizu de Prova|Mnemônico)[^:]*:\*\*\s*', '', text)
    return text.strip()

def format_analytical_summary(topic_title: str, raw_paragraphs: list[str]) -> list[str]:
    """
    Reconstrói o resumo em um formato analítico contínuo e fluido.
    Organiza em seções temáticas claras com parágrafos encadeados.
    """
    cleaned_items = []
    for p in raw_paragraphs:
        p_clean = p.strip()
        if not p_clean:
            continue
        # Remove eventuais marcadores de lista no início
        p_clean = re.sub(r'^[-*]\s+', '', p_clean)
        cleaned_items.append(p_clean)

    if not cleaned_items:
        return []

    # Separa itens por categoria conceitual
    teoria_lines = []
    exemplos_lines = []
    atencao_lines = []
    bizu_lines = []

    for item in cleaned_items:
        clean = clean_inline_tags(item)
        if not clean:
            continue

        if any(w in item.lower() for w in ['cuidado', 'atenção', 'pegadinha', 'exceção', 'veda-se', 'proibido', 'ressalv', '⚠️']):
            atencao_lines.append(clean)
        elif any(w in item.lower() for w in ['exemplo', 'ilustra', 'hipótese', 'caso concreto', '💡']):
            exemplos_lines.append(clean)
        elif any(w in item.lower() for w in ['mnemônico', 'macete', 'memorize', 'dica de prova', 'palavra-chave', '📌']):
            bizu_lines.append(clean)
        else:
            teoria_lines.append(clean)

    # Se a divisão ficou muito concentrada, equilibra
    if not teoria_lines and cleaned_items:
        teoria_lines = [clean_inline_tags(x) for x in cleaned_items[:len(cleaned_items)//2 + 1]]
        atencao_lines = [clean_inline_tags(x) for x in cleaned_items[len(cleaned_items)//2 + 1:]]

    result_blocks = []

    # 1. Seção Principal: Fundamentos e Desenvolvimento Analítico
    result_blocks.append("### 1. Fundamentação Teórica e Conceitos Centrais")
    
    # Agrupa linhas de teoria em parágrafos analíticos encadeados
    if teoria_lines:
        current_p = []
        for line in teoria_lines:
            # Se for linha de definição ou regra, adiciona como parágrafo fluido
            current_p.append(line)
            if len(current_p) >= 2:
                result_blocks.append(" ".join(current_p))
                current_p = []
        if current_p:
            result_blocks.append(" ".join(current_p))
    else:
        result_blocks.append("O estudo deste tema exige a compreensão integrada das normas basilares e suas repercussões diretas no edital.")

    # 2. Seção de Aplicação Prática / Casos Concretos (se houver)
    if exemplos_lines:
        result_blocks.append("### 2. Análise Prática e Desdobramentos")
        for ex in exemplos_lines:
            result_blocks.append(f"• **Aplicação:** {ex}")

    # 3. Seção de Pontos Críticos e Pegadinhas da Banca
    if atencao_lines or bizu_lines:
        result_blocks.append("### 3. Diretrizes de Prova e Pontos de Atenção")
        for at in atencao_lines:
            result_blocks.append(f"> ⚠️ **Atenção de Prova:** {at}")
        for bz in bizu_lines:
            result_blocks.append(f"> 📌 **Bizu Estratégico:** {bz}")

    return result_blocks

def process_all_files():
    count_files = 0
    count_segments = 0

    subjects = [d for d in os.listdir(CONTENT_ITEMS) if os.path.isdir(CONTENT_ITEMS / d)]
    for sub in subjects:
        sub_dir = CONTENT_ITEMS / sub
        for f in os.listdir(sub_dir):
            if not f.endswith(".json"):
                continue

            file_path = sub_dir / f
            with open(file_path, "r", encoding="utf-8") as fp:
                data = json.load(fp)

            changed = False
            for seg in data.get("segments", []):
                bizu = seg.get("bizu")
                if not bizu:
                    continue

                summary = bizu.get("summary", [])
                if not summary:
                    continue

                topic_name = seg.get("startTopic") or seg.get("topic") or "Conteúdo Teórico"
                new_summary = format_analytical_summary(topic_name, summary)
                if new_summary:
                    bizu["summary"] = new_summary
                    changed = True
                    count_segments += 1

            if changed:
                with open(file_path, "w", encoding="utf-8") as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=1)

                # Espelha para web/content/items
                web_target = WEB_ITEMS / sub / f
                web_target.parent.mkdir(parents=True, exist_ok=True)
                with open(web_target, "w", encoding="utf-8") as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=1)

                count_files += 1

    print(f"Sucesso! Reconstruídos {count_segments} resumos em {count_files} arquivos.")

if __name__ == "__main__":
    process_all_files()
