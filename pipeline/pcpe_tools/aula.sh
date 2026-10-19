#!/bin/bash
# uso: aula.sh disc/aNN  -> grava fonte compacta de todos os trechos em $TEMP/aula.txt e informa tamanho e trechos
cd "$(dirname "$0")/../.."
export PYTHONIOENCODING=utf-8
S="pipeline/pcpe_tools/src.py"
IDS=$(pipeline/.venv/Scripts/python -c "
import json,sys
d,a=sys.argv[1].split('/')
for s in json.load(open(f'content/segments/{d}.json',encoding='utf-8'))['segments']:
    if s['aula']==sys.argv[1]: print(s['id'], s['startPage'], s['endPage'])
" "$1")
echo "$IDS"
: > "$TEMP/aula.txt"
echo "$IDS" | while read id a b; do python $S $id >> "$TEMP/aula.txt"; done
wc -c "$TEMP/aula.txt"
