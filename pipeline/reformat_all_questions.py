#!/usr/bin/env python3
"""
pipeline/reformat_all_questions.py
Reestruturação textual de todas as questões do sistema:
- Separação visual de assertivas/itens enumerados (I., II., III., IV., V.) em parágrafos estruturados (**I.** ...)
- Isolamento do comando de resposta (ex: "Assinale a alternativa...", "Está correto...") em parágrafo próprio
- Preservação estrita de números, fórmulas, alternativas e gabaritos
- Atualização em content/items e web/content/items
"""

import os
import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

COMMAND_PATTERNS = [
    r'Assinale a alternativa (?:correta|incorreta|que|com)',
    r'É correto o que se afirma em',
    r'Está correto o que se afirma em',
    r'Está\(ão\) correta\(s\)',
    r'Estão corretas apenas',
    r'São corretas as afirmativas',
    r'Quais afirmativas estão corretas',
    r'Quais assertivas estão corretas',
    r'Assinale a sequência correta',
    r'Em relação ao exposto, assinale',
    r'Com base no exposto, assinale',
    r'Considerando o exposto, assinale',
    r'Sobre o assunto, assinale',
    r'Acerca do assunto, assinale',
    r'Diante do exposto, assinale'
]

COMMAND_REGEX = re.compile(
    r'([^\n])\s+(' + '|'.join(COMMAND_PATTERNS) + r')(?:\:|\.|\s*)*$',
    re.I
)

COMMAND_MID_REGEX = re.compile(
    r'([^\n])\s+(' + '|'.join(COMMAND_PATTERNS) + r')(?:\:|\.|\s*)',
    re.I
)

def reformat_statement(text: str) -> str:
    if not text:
        return text

    st = text.strip()

    # 1. Não alterar se já estiver formatado com **I.**
    if '**I.**' not in st and '**I**' not in st:
        # Evita termos como 'graus (I, II e III)', 'tipos I e II', 'fase I', 'meiose I'
        is_classification = bool(
            re.search(r'\b(?:graus|tipos|fases|classes|meiose|anexos)\s*\([I|V|X\s\,e]+\)', st, re.I) or
            re.search(r'\b(?:graus|tipos|fases|classes|meiose)\s+[I|V|X]+\s+e\s+[I|V|X]+', st, re.I)
        )

        if not is_classification:
            # Padrão A: I. ... II. ... III. ... ou I) / I -
            if re.search(r'(?:[:\.]\s*|^)\s*I[\.\-\)]\s+.+?\bII[\.\-\)]\s+', st):
                st = re.sub(r'([:\.]\s*|^)\s*I[\.\-\)]\s+', r':\n\n**I.** ', st)
                st = re.sub(r'([;\.]\s*)\b(II|III|IV|V|VI)[\.\-\)]\s+', r'\1\n\n**\2.** ', st)

            # Padrão B: (I) ... (II) ... (III) ...
            elif re.search(r'[:\.]\s*\(I\)\s+.+?\(II\)\s+', st):
                st = re.sub(r'([:\.]\s*)\(I\)\s+', r':\n\n**I.** ', st)
                st = re.sub(r'([;\.]\s*|\,\s*)\((II|III|IV|V|VI)\)\s+', r'\n\n**\2.** ', st)

    # 2. Isolar comandos finais em parágrafo próprio
    # Procura se há comando final no fim do texto ou precedendo assertivas/questão
    lines = st.split('\n')
    last_block = lines[-1]
    m_cmd = COMMAND_MID_REGEX.search(last_block)
    if m_cmd and not last_block.strip().startswith(m_cmd.group(2)):
        # Quebra antes do comando
        prefix = last_block[:m_cmd.start(2)].rstrip()
        cmd = last_block[m_cmd.start(2):].strip()
        if not cmd.endswith(':') and not cmd.endswith('.'):
            cmd += ':'
        lines[-1] = f'{prefix}\n\n{cmd}'
        st = '\n'.join(lines)

    # Limpeza de múltiplos \n excessivos (> 2)
    st = re.sub(r'\n{3,}', '\n\n', st)
    return st.strip()

def process_all():
    base_dirs = ['content/items', 'web/content/items']
    total_processed = 0
    total_reformatted = 0
    files_modified = 0

    for base in base_dirs:
        if not os.path.exists(base):
            continue
        print(f"Processando diretório: {base}")
        for subj in sorted(os.listdir(base)):
            subj_path = os.path.join(base, subj)
            if not os.path.isdir(subj_path):
                continue
            for f in sorted(os.listdir(subj_path)):
                if not f.endswith('.json'):
                    continue
                file_path = os.path.join(subj_path, f)
                with open(file_path, 'r', encoding='utf-8') as fp:
                    data = json.load(fp)

                modified = False
                for seg in data.get('segments', []):
                    for q in seg.get('questions', []):
                        total_processed += 1
                        old_st = q.get('statement', '')
                        new_st = reformat_statement(old_st)
                        if new_st != old_st:
                            q['statement'] = new_st
                            modified = True
                            total_reformatted += 1

                if modified:
                    files_modified += 1
                    with open(file_path, 'w', encoding='utf-8') as fp:
                        json.dump(data, fp, ensure_ascii=False, indent=2)

    print("=" * 60)
    print(f"Total de questões processadas: {total_processed}")
    print(f"Total de questões reformatadas: {total_reformatted}")
    print(f"Total de arquivos atualizados: {files_modified}")
    print("=" * 60)

if __name__ == "__main__":
    process_all()
