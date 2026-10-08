# MentorIA / CFO-BM — Instruções para o colaborador

Objetivo desta fase: produzir o **Bizu** (resumo + itens Certo/Errado) de cada trecho de estudo das disciplinas atribuídas a você. As **questões AOCP** ficam para a fase seguinte, só depois de todos os bizus (nossas duas partes) estarem prontos.

Leia, nesta ordem: este arquivo → `CLAUDE.md` (convenções do projeto) → `pipeline/briefs/bizu.md` (o briefing detalhado do que escrever). Estado geral da missão: `PROGRESSO-AUDITORIA.txt`.

## 1. O que já está pronto (não refazer)
- **Estrutura**: 13 disciplinas auditadas aula a aula; trechos, catálogo e 25 complementos autorais fechados e testados (`content/structure`, `content/segments`, `content/catalog.json`, `content/overrides`, `content/edital`, `content/audit`).
- **Bizu + questões dos 29 trechos de complementos autorais** (aulas `cNN`) — todos `DRAFT`.
- **Faltam 730 trechos** (as aulas do Estratégia, `aNN`), sem nenhum bizu nem questão.

## 2. Divisão de disciplinas

| Quem | Disciplinas (trechos a fazer) | Total |
|---|---|---:|
| **Valério + Claude (máquina principal)** | Legislações PE (4), Dir. Penal Militar (34), Dir. Constitucional (87), Dir. Administrativo (67), Língua Portuguesa (54), Inglês (23), Espanhol (36), Biologia (68) | **373** |
| **Colaborador (você)** | **Informática (91), Estatística (75), Matemática (74), Física (39), Química (78)** | **357** |

**Cada um escreve SOMENTE nos arquivos das suas disciplinas** (`content/items/<disciplina>/`). Assim os dois lados nunca editam o mesmo arquivo e o merge final não tem conflito.

Seus trechos, por aula (conferir sempre com `pipeline/.venv/Scripts/python pipeline/validate_content.py --coverage --stage bizu --subject <disciplina>`, que lista os trechos sem bizu):
- `informatica`: a00–a14 (91 trechos; a06 Excel e a12 Windows são as maiores)
- `estatistica`: a00–a14 (75)
- `matematica`: a00–a17 (74)
- `fisica`: a00–a17 (39)
- `quimica`: a00–a23 (78; a17 é a Aula 17 de Hidrocarbonetos)
As aulas `cNN` (complementos) dessas disciplinas já estão prontas.

## 3. Preparar a máquina (uma vez)
1. `git clone https://github.com/ValerioFerreira/mentoria-cfo.git` (ou `git pull`) e crie a sua branch: `git switch -c bizus-exatas`.
2. Python 3.13: `python -m venv pipeline/.venv` e `pipeline/.venv/Scripts/python -m pip install -r pipeline/requirements.txt` (Windows; em Linux/Mac use `bin/` no lugar de `Scripts/`).
3. **Coloque a pasta `docs/` na raiz do projeto** (cópia recebida de Valério FORA do Git: os PDFs têm marca d'água com nome/CPF e são material pago; `docs/` está no `.gitignore` e **nunca** deve ser commitada, enviada ou colada em texto). Estrutura esperada: `docs/01 - CBM-PE (Oficial) Língua Inglesa/...` etc., mais `docs/indice_topicos_curso.xlsx`.
4. Gere o cache de texto por página (não versionado): `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/extract.py` (alguns minutos; cria `pipeline/.cache/pages`, que o `inspect_aula.py` e o teste de originalidade usam).
5. Confira: `pipeline/.venv/Scripts/python -m pytest pipeline/tests -q` (deve passar tudo, inclusive o teste de originalidade, que sem o cache fica "skipped") e `pipeline/.venv/Scripts/python pipeline/inspect_aula.py matematica/a05` (mostra páginas, tópicos e trechos).

## 4. O que NÃO fazer
- **Não rodar** `segment.py`, `build_catalog.py`, `build_complements.py`, `edital_map.py`, nem o seed. Os ids dos trechos (`<disc>/aNN/sNN`) são posicionais; regenerar mudaria os ids de todo mundo.
- **Não editar**: `content/structure`, `content/segments`, `content/catalog.json`, `content/gaps.json`, `content/overrides`, `content/edital`, `content/audit`, `content/complements`, `pipeline/*.py`, `web/`, `CLAUDE.md`, `PROGRESSO-AUDITORIA.txt`, nem itens de outras disciplinas. Se achar um problema nesses arquivos (trecho mal cortado, lacuna, erro do material), **anote em `PROGRESSO-COLABORADOR.txt`** e avise Valério; ele corrige do lado dele.
- Não copiar texto do PDF para os arquivos (o validador rejeita 10 palavras iguais). Não versionar `docs/` nem `pipeline/.cache/`.

## 5. Fluxo de trabalho (por aula)
1. Veja os trechos da aula: `inspect_aula.py <disc>/aNN` (cada trecho tem `startPage`–`endPage`).
2. Leia as páginas do trecho (`--pages 10-22`) e escreva `content/items/<disc>/aNN.json` com **todos** os trechos da aula, no formato de `pipeline/briefs/bizu.md` (`"stage": "bizu"`, `summary` 6–14 tópicos só com **negrito**, `teoria` e `revisao` com 3–5 itens C/E cada, `pointers` ≥ 4 pontos-chave com a página). Use a ferramenta de escrita de arquivos (não heredoc no Bash).
3. Valide: `pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json` — corrija TODOS os erros. Faça a segunda passada de qualidade descrita no briefing.
4. Commit pequeno e frequente (a cada 1–3 aulas), na sua branch: `git add content/items/<disc> && git commit -m "Bizus <disciplina> aNN-aMM (DRAFT)"` e `git push -u origin bizus-exatas`.
5. Registre o progresso em `PROGRESSO-COLABORADOR.txt` (crie o arquivo): aulas concluídas, problemas encontrados no material, dúvidas para revisão humana. Esse é o único arquivo "de estado" que você edita.

Dica de produtividade com o Claude Code: peça "Leia `pipeline/briefs/bizu.md` e produza o bizu das aulas aNN–aMM de `<disciplina>`"; **no máximo 2–3 agentes em paralelo** (a janela de uso do plano Pro esgota rápido com muitos agentes) e **sempre uma aula por arquivo por agente**.

## 6. Qualidade (resumo; detalhes no briefing)
- Conteúdo só do que o trecho ensina; nada inventado; se o material tiver erro evidente, não use o ponto e anote.
- Itens C/E: uma afirmação por item, objetiva, inequívoca, com explicação; conjuntos `teoria` e `revisao` diferentes, cada um com certos e errados; nenhuma afirmação repetida.
- Exatas: C/E sobre fórmulas, condições de validade, unidades, sinais, propriedades e definições (sem contas longas).
- Informática: recursos/atalhos/menus **como o material apresenta** (Office 2019, LibreOffice 7, Windows 11); onde o material estiver desatualizado (ex.: DELTREE, WordPad no Windows 11), não use o ponto.
- Tudo entra como `DRAFT`; a aprovação (`APPROVED`) é humana, depois, em `/admin/revisao`.

## 7. Como será o merge
Quando você e Valério terminarem os bizus: cada um abre um Pull Request da sua branch para `main` (as pastas `content/items/<disciplina>/` são disjuntas, então não há conflito), roda-se `pytest` e `validate_content.py --coverage --stage bizu` (meta: 761 trechos com bizu) e só então começa a **fase 2 (questões)** com a mesma divisão de disciplinas, usando `pipeline/briefs/content.md` e os `pointers` dos bizus para não reler o trecho inteiro.

## 8. Referência rápida de comandos
```bash
PYTHONIOENCODING=utf-8
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN                  # trechos da aula
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --pages 10-22    # texto das páginas
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --grep "regex"   # buscar nas páginas
pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json
pipeline/.venv/Scripts/python pipeline/validate_content.py --coverage --stage bizu --subject <disc>
pipeline/.venv/Scripts/python -m pytest pipeline/tests -q
```
