"""Copia arquivos alterados em content/items para web/content/items."""

import subprocess
import os
import shutil

def main():
    res = subprocess.run(
        ['git', 'status', '--porcelain', 'content/items'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    copied = []
    for line in res.stdout.splitlines():
        path = line[3:].strip().strip('"')
        if os.path.isfile(path) and path.replace('\\', '/').startswith('content/items/'):
            rel = os.path.relpath(path, 'content/items')
            dest = os.path.join('web', 'content', 'items', rel)
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(path, dest)
            copied.append((path, dest))

    print(f'Total copiado: {len(copied)} arquivos de content/items para web/content/items')
    with open('pipeline/.cache/auditoria-resumos/copied_items.txt', 'w', encoding='utf-8') as fp:
        for p, d in copied:
            fp.write(f'{p} -> {d}\n')

if __name__ == '__main__':
    main()
