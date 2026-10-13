# Resumos analíticos — estado da produção e da inserção no sistema

Posição em **13/10/2026** (branch `resumos-agentes`, a partir de `mercadopago`). Gerado a partir do que existe em `content/summaries`, `resumos-colaboradores/indice.json` e das rotinas de validação do `pipeline/`. Para continuar de outro computador, leia primeiro a seção 5 (limitações) e a 4 (próximos passos).

## 1. Resumo em números

| Item | Valor |
| --- | --- |
| Trechos no índice (`indice.json`) | **897** (Fase 1 = edital do CFO CBMPE: 761 · Fase 2 = fora do edital do CFO: 136) |
| Trechos com resumo gravado em `content/summaries` | **761 (85%)** — 210 arquivos, ~703 mil palavras de resumo analítico |
| Resumos analíticos **e** sintéticos (Bizu) | 761 de 761 (todos trazem os dois) |
| Fase 1 concluída | **761 de 761 (100%)** — os 27 últimos foram importados em 13/10/2026 (ver 4.1) |
| Fase 2 concluída | **0 de 136** (Atualidades 0/63, Raciocínio Lógico 0/70, História de PE 0/3) |
| Status de todos os arquivos | `DRAFT` (nenhum aprovado) |
| `apply_synthetic.py --dry-run` | 734 trechos (rodar de novo: agora são 761) aplicáveis, 0 sem arquivo de itens |
| Testes (`pytest pipeline/tests/test_summaries.py`) | 7 passam |
| Validador (`validate_summaries.py`) | 205 arquivos, **0 com erro** |

Os 27 trechos que estavam pendentes foram importados (14 Biologia, 5 Direito Administrativo EXT-L2, 2 Direito Administrativo CODEX-L1, 1 Biologia CODEX-L3D, 4 Espanhol, 1 Física).

## 2. Situação por disciplina (Fase 1)

| Disciplina | Trechos | Com resumo | Palavras | Quem produziu |
| --- | --- | --- | --- | --- |
| Direito Constitucional | 93 | 93 | 135.436 | CLAUDE-L1, CODEX-L1, pilotos |
| Direito Administrativo | 71 | **64** | 81.976 | CLAUDE-L1, CODEX-L1, EXT-L2 (faltam 7 — entregues) |
| Direito Penal Militar | 36 | 36 | 46.597 | CLAUDE-L4 |
| Estatística | 76 | 76 | 94.751 | CLAUDE-L4 |
| Informática | 92 | 92 | 77.482 | EXT-L2, pilotos |
| Língua Inglesa | 24 | 24 | 16.113 | EXT-L2 |
| Língua Portuguesa | 56 | 56 | 67.893 | EXT-L3, CODEX-L3, pilotos |
| Biologia | 71 | **56** | 32.003 | EXT-L3, CODEX-BIO-1/2/3, CODEX-L3B/L3D (faltam 15 — entregues) |
| Matemática | 76 | 76 | 41.051 | EXT-L5 |
| Física | 41 | **40** | 24.824 | EXT-L5 (falta 1 — entregue) |
| Química | 79 | 79 | 56.961 | EXT-L6 |
| Língua Espanhola | 37 | **33** | 20.491 | EXT-L6 (faltam 4 — entregues) |
| Legislações PE (complementos) | 9 | 9 | 9.364 | pilotos |
| **Fase 2** — Atualidades | 63 | 0 | — | ninguém |
| **Fase 2** — Raciocínio Lógico | 70 | 0 | — | ninguém |
| **Fase 2** — História de Pernambuco | 3 | 0 | — | ninguém |

Lotes do `PLANO-DE-EXECUCAO.md`: 1 (Constitucional + Administrativo) 157/164, 2 (Informática + Inglês) 116/116, 3 (Biologia + Português) 112/127, 4 (Estatística + DPM) 112/112, 5 (Matemática + Física) 116/117, 6 (Química + Espanhol) 112/116, F2-A 0/63, F2-B 9/82. (A contagem por lote inclui complementos e trechos compartilhados que o índice atribui a outro lote.)

## 3. O que já está pronto

- **Pipeline completo** de ponta a ponta: índice com IDs estáveis (`build_summary_index.py`), instruções para agentes sem acesso ao sistema (`INSTRUCOES.md`, `PROMPTS-COLABORADORES.md`), autoverificação (`verificar_resumos.py`), importador com validação (`import_agent_summaries.py`: tamanho, `### Para fixar` com 5–8 itens, impressão digital do trecho, originalidade — erro a partir de 16 palavras seguidas iguais à fonte), nota de cobertura automática (`summary_coverage.py`), coleta das notas dos agentes (`collect_review_notes.py`), aplicação do sintético ao Bizu (`apply_synthetic.py`) e seed (`seedSummaries` em `web/prisma/seed-structure.ts`).
- **Banco e tela**: tabelas `AnalyticSummary` e `SegmentImportance`; página da atividade mostra o resumo (Teoria alterna diretriz × resumo; Revisão alterna "Meus resumos" × resumo; resumo `DRAFT` mostra o selo "rascunho"). O planejador (Turbo) usa **qualquer** resumo existente no banco, inclusive `DRAFT` (`web/src/lib/data/contest-data.ts`).
- **Importância por concurso** (`content/importance/segments.json`) cobre os 897 trechos do índice.
- **Avaliações por amostra** (`resumos-colaboradores/avaliacao/`): `AVALIACAO-EXT-L2-L3.md`, `AVALIACAO-EXT-L5-L6.md`, `AVALIACAO-COMPLEMENTAR.md` (todos "aprovado com ressalvas"), revisões finais por grupo (`REVISAO-FINAL-G1…G6`, `REVISAO-CODEX-BIO-1/2`) e amostras sorteadas por agente (`amostras/`).
- **Correções já aplicadas direto nos JSON** após as revisões: erros de "Para fixar" em Direito, erros de conteúdo em Direito Administrativo (responsabilidade do Estado, acumulação de cargos, critérios de licitação de concessões) e ajustes em Informática e Português.
- Relatórios regenerados hoje: `avaliacao/COBERTURA.md|csv` e `REVISAO-HUMANA-NOTAS.md`.

## 4. O que falta para concluir a inserção no sistema

### 4.1 Importação dos 27 trechos da Fase 1 — CONCLUÍDA em 13/10/2026 (o texto abaixo fica como registro)

Teste a seco (`--dry-run`) feito hoje: todos os 27 são válidos.

| Pasta em `entregas/` | Trechos que entram |
| --- | --- |
| `resumos_EXT-L3_L3-03` | 14 de Biologia (S0253, S0257, S0300, S0318, S0329, S0333, S0340, S0355, S0356, S0359, S0362, S0369, S0380, S0381) |
| `resumos_EXT-L6_L6-01` | S0319 (Espanhol) |
| `resumos_EXT-L6_L6-02` | S0351, S0402, S0443 (Espanhol) |
| `resumos_EXT-L2_L1-06` | S0372, S0373, S0374, S0375, S0388 (Direito Administrativo; já corrigidos na revisão G5) |
| `resumos_CODEX-L1_L1-DA-01` | S0473, S0491 (Direito Administrativo; reescritos na revisão G5) |
| `resumos_CODEX-L3D_S0519-S0562` | S0543 (Biologia) |
| `resumos_EXT-L5_L5-01` | S0575 (Física) |

Comando (por pasta, na raiz, com `PYTHONIOENCODING=utf-8`): `pipeline/.venv/Scripts/python pipeline/import_agent_summaries.py resumos-colaboradores/entregas/<pasta>`. **Não use `--overwrite`**: muitos resumos já foram corrigidos direto em `content/summaries` e o `.md` antigo em `entregas/` os desfaria (e ainda seria rejeitado, p. ex. 11 arquivos da `EXT-L5_L5-01` com 9 itens em "Para fixar"). Depois rode `validate_summaries.py` e `summary_coverage.py`.

### 4.2 Produzir a Fase 2 (136 trechos, fora do edital do CFO CBMPE)

Atualidades (63, sublotes F2-A-01 a 04, S0835–S0897), Raciocínio Lógico (70) e História de Pernambuco (3) (F2-B, S0762–S0834). Ninguém começou. Só vale para os alunos de concursos do catálogo que cobram essas matérias; priorizar após decidir o valor para o produto. `PLANO-DE-EXECUCAO.md` e `PROMPTS-COLABORADORES.md` já descrevem como distribuir.

### 4.3 Revisão de qualidade (antes de tirar o selo "rascunho")

- **Cobertura automática**: 10 resumos em REFAÇÃO e 68 em REVISAR (lista em `avaliacao/COBERTURA.md`). Os 10 em REFAÇÃO: Biologia S0542, S0539, S0554, S0519 (CODEX-L3D) e S0512 (CODEX-BIO-3); Física S0583; Inglês S0275; Matemática S0708; Química S0683 e S0661. É triagem de omissão, não detecta conceito errado: ler contra a fonte.
- **Avisos do validador**: 294 de "analítico abaixo do alvo" (mais frequentes em Química, Espanhol, Física e Matemática) e 106 coincidências de 10 a 15 palavras com o material (conferir se são citação de norma/definição).
- **Notas dos agentes**: 431 de 687 resumos importados trazem pontos para revisão humana (`REVISAO-HUMANA-NOTAS.md`): figuras/tabelas não extraídas, dúvidas de atualização legislativa (p. ex. S0079, EC citada no material que não pôde ser confirmada; S0076, iniciativa do subsídio dos Ministros do STF), valores do tempo da banca etc.
- **Padrões fracos já documentados nas avaliações**: Espanhol (comprime quadros de memorização em parágrafos sem tabela), Química e Física (clareza 2,5–3,0), Biologia CODEX-L3D (13 resumos abaixo de 45% do alvo).
- **Decisão do dono**: definir critério e responsável por trocar `status` de `DRAFT` para `APPROVED` (por arquivo/trecho em `content/summaries`, campo `status`; o seed grava o que estiver no JSON). Não existe tela de aprovação de resumos em `/admin/revisao` (só de questões).

### 4.4 Aplicar ao conteúdo do site e semear

1. `pipeline/.venv/Scripts/python pipeline/apply_synthetic.py` — grava o sintético em `bizu.summary` (substitui o texto anterior; itens C/E ficam) em `content/items` e `web/content/items`, e **espelha** `summaries`, `importance` e `contests` em `web/content`, que é o que o build lê. Hoje `web/content/summaries` só tem 28 arquivos antigos; **o espelho dos 734 trechos ainda não foi gerado nem commitado**.
2. Commitar `web/content` atualizado.
3. Banco local: `cd web && npx prisma db seed` (idempotente; semeia `AnalyticSummary`/`SegmentImportance`). Conferir uma atividade de Teoria e uma de Revisão em `/atividade/[id]`.
4. Banco de produção (Neon): o seed lê `DATABASE_URL`; não há comando `--remoto` para ele (só os scripts de questões têm). Decidir/documentar como semear com segurança antes de executar.
5. Rodar `npm run typecheck`, `npm run test` e `npm run verify:plans -- --remoto` (somente leitura): com mais resumos, o Turbo troca mais Teoria por leitura do resumo, o que muda os planos gerados e a cobertura de planos ainda em análise.
6. Atualizar o `CLAUDE.md` (estado da importação) e o registro de memória do projeto ao concluir.

## 5. Limitações para continuar remotamente

- `docs/` (PDFs do Estratégia) e `pipeline/.cache/` **não estão no GitHub** (material protegido com marca d'água). Sem eles, num outro computador **não funcionam**: `summary_source.py`, `import_agent_summaries.py`, `validate_summaries.py` (originalidade e fingerprint), `summary_coverage.py`, `segment.py`. Funcionam sem eles: ler/editar os JSON e `.md`, `apply_synthetic.py`, testes do `web/`, revisão de texto e preparo dos lotes da Fase 2.
- `web/.env`, `web/.env.remote` e o Postgres local também não vão ao repositório.
- O repositório ainda traz arquivos de trabalho não relacionados a resumos, deixados de fora do commit: `extract_batch.py` (script solto na raiz), `web/docs/MERCADO-PAGO-HANDOFF.md` (preços desatualizados) e `web/src/app/api/webhooks/mercadopago/route.test.ts`.
- As seis pastas `.zip` em `entregas/` são cópias dos diretórios e não foram versionadas.
