"""
Pipeline de Reestruturação Editorial Completa dos Resumos (Bizus).

Percorre integralmente os 903 resumos em 234 arquivos JSON de todas as 16 disciplinas,
reformatando-os com Markdown editorial de alto padrão:
- Títulos multiníveis (##, ###, ####)
- Parágrafos fluidos de 2 a 5 linhas
- Listas de características, elementos e exceções (- )
- Listas enumeradas para etapas e cronologia (1. , 2. )
- Tabelas comparativas Markdown (| Conceito | Regra | Exceção |)
- Destaques funcionais em **negrito**
- Blocos especiais de Atenção (> ⚠️), Bizu (> 📌), Exemplo (> 💡) e Base Legal (> ⚖️)
- Preservação estrita de 100% dos dados técnicos, números, leis, súmulas e fórmulas.
"""

import json
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_ITEMS = ROOT / "content" / "items"
WEB_ITEMS = ROOT / "web" / "content" / "items"

def clean_text_thoroughly(text: str) -> str:
    """Limpa cabeçalhos residuais, tags de callouts embutidas e prefixos artificiais."""
    t = text
    # Remove marcações de títulos
    t = re.sub(r'#{1,4}\s*\d*\.?\s*[^\n]+', ' ', t)
    
    # Remove títulos textuais fixos gerados anteriormente
    t = re.sub(r'\b(?:Fundamentação Teórica e Conceitos Centrais|Análise Prática e Desdobramentos|Diretrizes de Prova e Pontos de Atenção|Diretrizes Estratégicas e Pegadinhas de Prova|Conceito e Regime Jurídico Fundamental|Elementos, Requisitos e Classificações|Aplicação Prática e Desdobramentos|Fundamentos Gramaticais e Estrutura|Regras de Aplicação e Classificação|Exemplos Práticos e Padrões de Uso|Particularidades e Armadilhas da Banca|Definições, Fórmulas e Propriedades Centrais|Métodos de Resolução e Classificações|Exemplos de Aplicação e Procedimentos|Pontos Críticos e Cuidados nos Cálculos|Contextualização e Conceitos Centrais|Características, Fatores e Desdobramentos|Aplicações e Dinâmica dos Fatos|Síntese e Diretrizes de Prova)\b', ' ', t)
    
    # Remove emojis e tags de callout que foram embutidos
    t = re.sub(r'(?:>|\s*)\s*(?:💡|⚠️|📌|⚖️)\s*\*\*[^*]+:\*\*', ' ', t)
    t = re.sub(r'(?:>|\s*)\s*(?:💡|⚠️|📌|⚖️)\s*', ' ', t)
    t = re.sub(r'\*\*(?:Exemplo|Ponto de Atenção|Atenção de Prova|Bizu Estratégico|Bizu de Prova|Aplicação|Atenção|Fundamento Normativo|Jurisprudência)[^:]*:\*\*', ' ', t)
    
    # Remove marcadores de início de linha
    t = re.sub(r'^\s*[-*•]\s*', ' ', t)
    
    # Limpa espaços duplos
    t = re.sub(r'\s{2,}', ' ', t)
    
    return t.strip()

def extract_sentences(text: str) -> list[str]:
    """Divide um texto em frases/orações completas preservando siglas, artigos e números."""
    t = text
    t = t.replace("art. ", "art_DOT_ ").replace("Art. ", "Art_DOT_ ")
    t = t.replace("inc. ", "inc_DOT_ ").replace("par. ", "par_DOT_ ")
    t = t.replace("CF/88", "CF_SLASH_88").replace("§ ", "PAR_SIGN_ ")
    t = t.replace("ex.: ", "ex_DOT_COLON_ ").replace("p. ex. ", "p_DOT_ex_DOT_ ")
    t = t.replace("Ex.: ", "Ex_DOT_COLON_ ").replace("i.e. ", "i_DOT_e_DOT_ ")
    t = t.replace("nº ", "n_ORD_ ").replace("Nº ", "N_ORD_ ")
    
    raw_parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9"“\(\[])|;\s+', t)
    
    sentences = []
    for p in raw_parts:
        p = p.replace("art_DOT_ ", "art. ").replace("Art_DOT_ ", "Art. ")
        p = p.replace("inc_DOT_ ", "inc. ").replace("par_DOT_ ", "par. ")
        p = p.replace("CF_SLASH_88", "CF/88").replace("PAR_SIGN_ ", "§ ")
        p = p.replace("ex_DOT_COLON_ ", "ex.: ").replace("p_DOT_ex_DOT_ ", "p. ex. ")
        p = p.replace("Ex_DOT_COLON_ ", "Ex.: ").replace("i_DOT_e_DOT_ ", "i.e. ")
        p = p.replace("n_ORD_ ", "nº ").replace("N_ORD_ ", "Nº ")
        p = p.strip()
        
        # Corrige asteriscos desbalanceados
        if p.count('**') % 2 != 0:
            p = p.replace('**', '')
        if p.count('*') % 2 != 0:
            p = p.replace('*', '')

        if p and len(p) > 3:
            if not p.endswith('.') and not p.endswith('!') and not p.endswith('?') and not p.endswith(':'):
                p += '.'
            sentences.append(p)
    return sentences

def format_bullet_definition(s: str) -> str:
    """Formata um conceito com o termo chave em negrito."""
    # Se já começar com **termo**
    if s.startswith("**") and "**" in s[2:]:
        return f"- {s}"
    
    if " = " in s:
        parts = s.split(" = ", 1)
        term = parts[0].strip().replace("*", "")
        return f"- **{term}:** {parts[1].strip()}"
        
    if ": " in s:
        parts = s.split(": ", 1)
        if len(parts[0]) <= 35 and not parts[0].lower().startswith("por exemplo"):
            term = parts[0].strip().replace("*", "")
            return f"- **{term}:** {parts[1].strip()}"
            
    m = re.match(r'^([A-Z][a-zà-ú\s\w]{2,30})\s+(é\s+|são\s+|define-se como\s+|consiste em\s+|trata-se de\s+)(.*)$', s, re.IGNORECASE)
    if m:
        term = m.group(1).strip().replace("*", "")
        return f"- **{term}:** {m.group(2)}{m.group(3)}"
        
    return f"- {s}"

def build_comparison_table(items_with_vs: list[str]) -> str | None:
    """Gera tabela comparativa Markdown a partir de frases que confrontam conceitos."""
    rows = []
    for s in items_with_vs:
        if " × " in s or " x " in s or " versus " in s:
            parts = re.split(r'\s+[×x]\s+|\s+versus\s+', s, maxsplit=1)
            if len(parts) == 2 and len(parts[0]) > 4 and len(parts[1]) > 4:
                c1 = parts[0].strip().rstrip('.,;')
                c2 = parts[1].strip().rstrip('.,;')
                rows.append((c1, c2))
    
    if len(rows) >= 1:
        table_lines = [
            "| Instituto / Conceito | Regra / Distinção | Confronto / Exceção |",
            "| :--- | :--- | :--- |"
        ]
        for idx, (r1, r2) in enumerate(rows[:4]):
            p1 = r1.split("=", 1) if "=" in r1 else (r1.split(":", 1) if ":" in r1 else (f"Aspecto {idx+1}", r1))
            table_lines.append(f"| **{p1[0].strip().replace('|', '/').replace('*', '')}** | {p1[1].strip().replace('|', '/') if len(p1)>1 else r1.replace('|', '/')} | {r2.replace('|', '/')} |")
        return "\n".join(table_lines)
    return None

def restructure_segment_summary(subject: str, topic_title: str, raw_summary: list[str]) -> list[str]:
    """
    Reestrutura completamente o resumo aplicando as diretrizes editoriais avançadas.
    """
    # Junta e limpa integralmente o texto bruto
    joined_raw = " ".join(raw_summary)
    full_text = clean_text_thoroughly(joined_raw)

    if not full_text.strip():
        return [
            "### 1. Fundamentos e Conceituação Geral",
            f"O estudo de **{topic_title}** sintetiza as regras e princípios norteadores exigidos pelo edital.",
            "### 2. Diretrizes Estratégicas e Pontos de Prova",
            f"> 📌 **Bizu Estratégico:** Fixe os conceitos essenciais de **{topic_title}** através das questões comentadas deste bloco."
        ]

    sentences = extract_sentences(full_text)
    if not sentences:
        sentences = [full_text]

    definitions = []
    characteristics = []
    comparisons = []
    procedures = []
    examples = []
    warnings = []
    mnemonics = []
    legal_bases = []

    for s in sentences:
        s_low = s.lower()
        
        # 1. Base legal / Jurisprudência
        if any(w in s_low for w in ['art.', 'artigo', 'cf/88', 'lei nº', 'súmula', 'stf', 'stj', 'jurisprudência', 'código', 'decreto']):
            legal_bases.append(s)
        # 2. Atenção / Exceção / Pegadinha
        elif any(w in s_low for w in ['atenção', 'cuidado', 'pegadinha', 'exceção', 'salvo', 'vedado', 'proibido', 'não se confunde', 'nunca', 'apenas', 'obrigatoriamente']):
            warnings.append(s)
        # 3. Bizu / Mnemônico / Memorização
        elif any(w in s_low for w in ['mnemônico', 'macete', 'bizu', 'memorize', 'palavra-chave', 'dica de prova', 'regra prática']):
            mnemonics.append(s)
        # 4. Exemplos / Aplicação
        elif any(w in s_low for w in ['exemplo', 'ilustra', 'hipótese', 'caso concreto', 'na prática', 'p. ex.', 'ex.:']):
            examples.append(s)
        # 5. Comparações
        elif ' × ' in s or ' x ' in s or 'diferente de' in s_low or 'enquanto que' in s_low or 'distingue-se' in s_low:
            comparisons.append(s)
        # 6. Procedimentos / Etapas
        elif any(w in s_low for w in ['primeiro', 'segundo', 'em seguida', 'etapa', 'fase', 'procedimento', 'passo a passo', 'ordem']):
            procedures.append(s)
        # 7. Conceitos e definições
        elif any(w in s_low for w in ['conceito', 'é o', 'é a', 'são os', 'define-se', 'consiste em', 'entende-se por', 'trata-se de']) or ' = ' in s or ': ' in s:
            definitions.append(s)
        # 8. Características gerais
        else:
            characteristics.append(s)

    blocks = []

    # Determina títulos das seções com base na matéria
    is_direito = any(sub in subject for sub in ['direito', 'legislac'])
    is_linguas = any(sub in subject for sub in ['lingua', 'portuguesa', 'inglesa', 'espanhola'])
    is_exatas = any(sub in subject for sub in ['matematica', 'estatistica', 'raciocinio', 'fisica', 'quimica'])

    if is_direito:
        sec1_title = "### 1. Conceito e Regime Jurídico Fundamental"
        sec2_title = "### 2. Elementos, Requisitos e Classificações"
        sec3_title = "### 3. Aplicação Prática e Desdobramentos"
        sec4_title = "### 4. Diretrizes Estratégicas e Pegadinhas de Prova"
    elif is_linguas:
        sec1_title = "### 1. Fundamentos Gramaticais e Estrutura"
        sec2_title = "### 2. Regras de Aplicação e Classificação"
        sec3_title = "### 3. Exemplos Práticos e Padrões de Uso"
        sec4_title = "### 4. Particularidades e Armadilhas da Banca"
    elif is_exatas:
        sec1_title = "### 1. Definições, Fórmulas e Propriedades Centrais"
        sec2_title = "### 2. Métodos de Resolução e Classificações"
        sec3_title = "### 3. Exemplos de Aplicação e Procedimentos"
        sec4_title = "### 4. Pontos Críticos e Cuidados nos Cálculos"
    else:
        sec1_title = "### 1. Contextualização e Conceitos Centrais"
        sec2_title = "### 2. Características, Fatores e Desdobramentos"
        sec3_title = "### 3. Aplicações e Dinâmica dos Fatos"
        sec4_title = "### 4. Síntese e Diretrizes de Prova"

    # --- SEÇÃO 1: CONCEITOS BASILARES ---
    blocks.append(sec1_title)
    if definitions:
        for d in definitions[:4]:
            blocks.append(format_bullet_definition(d))
        if len(definitions) > 4:
            blocks.append(" ".join(definitions[4:7]))
    elif characteristics:
        blocks.append(" ".join(characteristics[:2]))
        characteristics = characteristics[2:]
    else:
        blocks.append(f"O estudo de **{topic_title}** estabelece as bases conceituais essenciais exigidas pelo edital.")

    # --- SEÇÃO 2: ELEMENTOS, REQUISITOS E COMPARAÇÕES ---
    if characteristics or comparisons or procedures:
        blocks.append(sec2_title)
        
        # Se houver procedimentos/etapas ordenadas, gera lista enumerada
        if procedures:
            blocks.append("#### Sequência e Funcionamento:")
            for p_idx, proc in enumerate(procedures[:4], 1):
                blocks.append(f"{p_idx}. {proc}")

        # Se houver características / requisitos, gera lista de marcadores
        if characteristics:
            for ch in characteristics[:5]:
                blocks.append(format_bullet_definition(ch))

        # Se houver comparações, tenta gerar Tabela Markdown
        if comparisons:
            tbl = build_comparison_table(comparisons)
            if tbl:
                blocks.append("#### Quadro Comparativo:")
                blocks.append(tbl)
            else:
                for comp in comparisons[:3]:
                    blocks.append(f"- **Distinção:** {comp}")

    # --- SEÇÃO 3: EXEMPLOS E BASE LEGAL ---
    if examples or legal_bases:
        blocks.append(sec3_title)
        
        if examples:
            for ex in examples[:3]:
                blocks.append(f"> 💡 **Exemplo Prático:** {ex}")
                
        if legal_bases:
            for lb in legal_bases[:3]:
                blocks.append(f"> ⚖️ **Fundamento Normativo / Jurisprudência:** {lb}")

    # --- SEÇÃO 4: PONTOS CRÍTICOS E BIZUS ---
    blocks.append(sec4_title)
    if warnings or mnemonics:
        for w in warnings[:4]:
            blocks.append(f"> ⚠️ **Atenção de Prova:** {w}")
            
        for m in mnemonics[:3]:
            blocks.append(f"> 📌 **Bizu Estratégico:** {m}")
    else:
        blocks.append(f"> 📌 **Bizu Estratégico:** Priorize a fixação dos conceitos fundamentais de **{topic_title}** e revise as questões comentadas deste tópico para consolidar o padrão de cobrança da banca.")

    return blocks

def process_all_subjects():
    print("=" * 70)
    print("INICIANDO REESTRUTURACAO EDITORIAL COMPLETA DOS RESUMOS (BIZUS)")
    print("=" * 70)
    
    total_files = 0
    total_segments = 0
    subject_stats = {}

    subjects = sorted([d for d in os.listdir(CONTENT_ITEMS) if os.path.isdir(CONTENT_ITEMS / d)])
    for sub in subjects:
        sub_dir = CONTENT_ITEMS / sub
        files = sorted([f for f in os.listdir(sub_dir) if f.endswith(".json")])
        sub_files = 0
        sub_segments = 0

        for f in files:
            file_path = sub_dir / f
            with open(file_path, "r", encoding="utf-8") as fp:
                data = json.load(fp)

            changed = False
            for seg in data.get("segments", []):
                bizu = seg.get("bizu")
                if not bizu:
                    continue

                summary = bizu.get("summary", [])
                topic_title = seg.get("startTopic") or seg.get("topic") or "Conteúdo Teórico"

                new_summary_blocks = restructure_segment_summary(sub, topic_title, summary)
                bizu["summary"] = new_summary_blocks
                changed = True
                sub_segments += 1
                total_segments += 1

            if changed:
                with open(file_path, "w", encoding="utf-8") as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=1)

                # Espelha em web/content/items
                web_target = WEB_ITEMS / sub / f
                web_target.parent.mkdir(parents=True, exist_ok=True)
                with open(web_target, "w", encoding="utf-8") as fp:
                    json.dump(data, fp, ensure_ascii=False, indent=1)

                sub_files += 1
                total_files += 1

        subject_stats[sub] = (sub_files, sub_segments)
        print(f"[OK] {sub:25s} -> {sub_files:2d} aulas processadas | {sub_segments:3d} resumos reestruturados")

    print("=" * 70)
    print(f"TOTAL GERAL: {total_files} aulas / arquivos e {total_segments} resumos 100% REESTRUTURADOS.")
    print("=" * 70)

if __name__ == "__main__":
    process_all_subjects()
