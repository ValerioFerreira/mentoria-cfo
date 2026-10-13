# Fluxo de trabalho com colaboradores e agentes

Guia único para quem produz conteúdo no projeto (pessoas ou agentes do Claude Code). Convenções gerais e arquitetura: `CLAUDE.md`. O que já foi feito e as dúvidas do material: `HISTORICO.md`.

## 1. Frentes de trabalho

| Frente | Quem recebe | Instruções | Onde se escreve |
|---|---|---|---|
| **Resumos analíticos e sintéticos** (ativa) | colaboradores externos e agentes internos, por lote/sublote do índice | `resumos-colaboradores/INSTRUCOES.md` (autossuficiente), `PLANO-DE-EXECUCAO.md`, `PROMPTS-COLABORADORES.md`, índice `INDICE-RESUMOS.xlsx/.csv`, autoverificação `verificar_resumos.py`; briefing `pipeline/briefs/summary.md` | `content/summaries/<disc>/<aula>.json` (via `pipeline/import_agent_summaries.py`) |
| **Bizus** (resumo + itens C/E + pointers) | por disciplina | `pipeline/briefs/bizu.md` (e `content.md`, o briefing geral) | `content/items/<disc>/<aNN\|cNN>.json`, sempre `DRAFT` |
| **Complementos autorais** (lacunas do edital) | por disciplina | `pipeline/briefs/complement.md` | `content/complements/*.md` → `build_complements.py` |
| **Auditoria estrutural** | agente por disciplina | `pipeline/briefs/audit.md` | `content/overrides/<disc>.json` (nunca `structure/` nem `segments/` à mão) |
| **Questões** | — | **Questões autorais foram descontinuadas** (2026-10-11). A fonte única são os cadernos do TecConcursos em `docs/questoes/`, importados por `pipeline/questoes/importar.py` (ver `pipeline/questoes/EXTRACAO.md`) | banco, não `content/items` |

Os arquivos de `resumos-colaboradores/` e `pipeline/briefs/` são entregues a agentes que podem não ver o resto do repositório; por isso ficam autossuficientes e **não** foram fundidos neste guia.

## 2. Regras que valem para todas as frentes

- **Cada pessoa escreve só nos arquivos das suas disciplinas/lotes.** Pastas disjuntas ⇒ o merge não tem conflito. Branch própria por frente; PRs para a `main`.
- **Congelado para colaboradores**: `content/structure`, `segments`, `catalog.json`, `gaps.json`, `overrides`, `edital`, `audit`, `complements`, `pipeline/*.py`, `web/`, `CLAUDE.md`. Problema nesses arquivos: anotar e avisar o dono do repositório (Valério), que corrige em commit separado na `main`.
- **Não rodar** `segment.py`, `build_catalog.py`, `build_complements.py`, `edital_map.py` nem o seed. Os ids de trecho (`<disc>/aNN/sNN`) são posicionais; regenerar muda os ids de todos.
- **`docs/` (PDFs do material) é protegido**: tem marca d'água com nome/CPF. Fica fora do Git (`.gitignore`), vai para a máquina do colaborador por fora, e **nunca** se commita, envia ou cola em texto. Não versionar `pipeline/.cache/`.
- **Originalidade**: escrever com as próprias palavras. `validate_content.py` rejeita 10 palavras seguidas iguais ao material (em lei seca: trocar verbos e ordem, quebrar as listas legais). Marcação: o resumo do bizu só renderiza **negrito**; C/E, enunciados e explicações são texto puro.
- Todo conteúdo novo entra como `DRAFT`; `APPROVED` é decisão humana em `/admin/revisao`.
- Não escrever sobre os pontos duvidosos do material listados no Apêndice B de `HISTORICO.md`; achado novo vai no relatório de entrega.
- Commits pequenos e frequentes (a cada 1–3 aulas), mensagem em português; agentes **não** rodam `git` (o orquestrador commita). Heredocs longos no Bash quebram: usar a ferramenta de escrita de arquivos.
- Janela de uso do Claude (plano Pro): no máximo **2–3 agentes em paralelo**, uma aula/arquivo por agente, gravando a cada aula.

## 3. Preparar a máquina (uma vez)

1. `git clone https://github.com/ValerioFerreira/mentoria-cfo.git`; criar a branch da sua frente (`git switch -c <frente>`).
2. Python 3.13: `python -m venv pipeline/.venv` e `pipeline/.venv/Scripts/python -m pip install -r pipeline/requirements.txt` (Linux/Mac: `bin/` no lugar de `Scripts/`).
3. Copiar a pasta `docs/` (só os PDFs das suas disciplinas, mais `docs/indice_topicos_curso.xlsx`) para a raiz, mantendo a estrutura `docs/<NN - …>/<NNN - Aula XX ….pdf>`.
4. Gerar o cache de texto: `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/extract.py [--only <NN>]`.
5. Conferir: `pipeline/.venv/Scripts/python -m pytest pipeline/tests -q` (o teste de originalidade só roda com o cache) e `pipeline/inspect_aula.py <disc>/aNN`.

## 4. Fluxo por aula (bizus)

1. `inspect_aula.py <disc>/aNN` lista os trechos (`startPage`–`endPage`); `--pages 10-22` mostra o texto; `--grep "regex"` busca.
2. Ler as páginas do trecho e escrever `content/items/<disc>/aNN.json` com **todos** os trechos da aula, no formato de `pipeline/briefs/bizu.md` (`"stage": "bizu"`, `summary` com 6–14 tópicos, `teoria` e `revisao` com 3–5 itens C/E cada, `pointers` ≥ 4 pontos-chave com a página).
3. `validate_content.py content/items/<disc>/aNN.json` — corrigir todos os erros; fazer a segunda passada de qualidade do briefing.
4. Commit na branch da frente e `git push -u origin <frente>`; acompanhar o que falta com `validate_content.py --coverage --stage bizu --subject <disc>`.

Qualidade em resumo: só o que o trecho ensina; nada inventado (se o material tem erro evidente, não usar o ponto e anotar); C/E com uma afirmação objetiva e inequívoca por item, conjuntos `teoria` e `revisao` diferentes, com certos e errados; exatas: fórmulas, condições de validade, unidades e propriedades (sem contas longas); Informática: recursos e atalhos **como o material apresenta** (Office 2019, LibreOffice 7, Windows 11), sem usar pontos desatualizados.

## 5. Comandos de referência

```bash
export PYTHONIOENCODING=utf-8
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN [--heads|--pages 10-22|--grep "regex"]
pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json
pipeline/.venv/Scripts/python pipeline/validate_content.py --coverage [--stage bizu] [--subject <disc>]
pipeline/.venv/Scripts/python pipeline/summary_queue.py --pending            # fila de resumos analíticos
pipeline/.venv/Scripts/python pipeline/summary_source.py <disc>/aNN/sNN      # texto-fonte de um trecho (protegido)
pipeline/.venv/Scripts/python -m pytest pipeline/tests -q
```
