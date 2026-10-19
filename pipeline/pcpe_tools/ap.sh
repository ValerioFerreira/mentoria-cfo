#!/bin/bash
# uso (a partir de qualquer pasta): pipeline/pcpe_tools/ap.sh <rascunho.txt> <disc/aula>...
# grava o rascunho (pcpe_author.py) e valida resumos (validate_summaries + runs.py) e itens (validate_content)
cd "$(dirname "$0")/../.."
export PYTHONIOENCODING=utf-8
D="$1"; shift
pipeline/.venv/Scripts/python pipeline/pcpe_author.py "$D" --batch pcpe-revisao || exit 1
for a in "$@"; do
  pipeline/.venv/Scripts/python pipeline/validate_summaries.py content/summaries/$a.json 2>&1 | grep -v "alvo [0-9]*): confira" | grep -vE "^1 arquivos"
  pipeline/.venv/Scripts/python pipeline/pcpe_tools/runs.py content/summaries/$a.json
  pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/$a.json 2>&1 | grep -E "ERRO|FALHA|AVISO|ok\]" | cut -c1-260
done
