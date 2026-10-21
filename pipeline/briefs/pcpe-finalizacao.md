# Briefing — Finalização do PCPE Agente de Polícia (resumos, questões, TEC e liberação)

Você é um agente de engenharia de conteúdo do MentorIA, trabalhando no repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM`
(branch `pcpe`; a `main` está em `536ab25`, e `pcpe` tem à frente o commit `bfb4639`). Leia `CLAUDE.md` e `README.md` antes de tudo: eles
trazem as convenções do projeto, os comandos e as armadilhas. Idioma de tudo: **português do Brasil**. Windows: use a ferramenta Write para
arquivos grandes (heredoc longo no Bash quebra com aspas) e defina `PYTHONIOENCODING=utf-8` ao imprimir acentos.

## 0. Regras de segurança (valem para toda a tarefa)

- **Nunca** imprima nem altere `web/.env*`. **Nunca** tente senhas de banco. `docs/` (PDFs do Estratégia, cadernos do TEC) é **protegida**: não versione, não publique, não copie texto verbatim para `content/`.
- **Produção (Neon)**: só escreva depois de um **backup íntegro de menos de 24 h** (`cd web && npx tsx scripts/questoes-backup.ts --remoto`, que deve terminar em `BACKUP ÍNTEGRO`). Gravação em massa de questões do TEC exige `--confirmo-producao` (ver `pipeline/questoes/EXTRACAO.md`). Nunca rode `--limpar-estrategia` (apaga as inéditas `mentoria_*`).
- Commits só com `git add` explícito (nunca `git add -A`), terminando com a linha `Co-Authored-By: <seu modelo> <noreply@anthropic.com>`. O push para `main` é feito por um worktree temporário a partir de `origin/main` (`git worktree add --detach <pasta> origin/main`, `git merge --no-ff pcpe`, `git push origin HEAD:main`, `git worktree remove`). Peça confirmação ao dono antes de qualquer push e de qualquer gravação na produção, a menos que ele já tenha autorizado na conversa.
- Ao terminar cada etapa, relate: o que fez, números, o que não conseguiu e por quê, dúvidas para o dono, hashes dos commits.

## 1. Estado atual (2026-10-21)

Já feito e já na `main` (`536ab25`): PCPE disponível; 2.013 questões inéditas de múltipla escolha revisadas e gravadas na produção (2.590 inéditas no total, contando as de certo/errado); planos do PCPE nascem "em análise até 24 h".

Já feito e **só em `pcpe`** (commit `bfb4639`), **ainda não gravado na produção**:
- `web/src/lib/quiz/pool.ts` + `actions.ts` + páginas do caderno/atividade: o caderno que não soma o pedido (25; 15 no Turbo) nos próprios trechos passa a **completar com questões de trechos da mesma disciplina cuja Teoria vem antes no plano** (nunca de trecho não estudado). Testes em `logic.test.ts`.
- 409 inéditas novas em `content/questoes/ineditas/mc/*.txt` (total 2.422 de múltipla escolha) para os 46 trechos em que o caderno ainda ficava curto.
- Ferramentas: `web/scripts/pcpe-plan-grid.ts` (grade de 92 planos), `pipeline/pcpe_tools/cadernos_sim.py`, `ineditas_append.py`, `res_ctx.py`, `res_qs.py`.

**Pendências, em ordem de execução:** (A) gravar as 409 inéditas na produção; (B) corrigir os 76 resumos analíticos em rascunho; (C) importar as questões reais do TecConcursos quando o dono avisar e aposentar as inéditas redundantes; (D) verificação final e liberação dos planos; (E) documentação e memória.

## Etapa A — Publicar as 409 inéditas

1. `git status` limpo para `content/questoes/ineditas/mc/` e `web/src`; rode `pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check` (esperado: `TOTAL 2422 · erros 0`), `lacunas_pcpe.py --check` (saída 0) e `ineditas.py --check` (erros 0).
2. Faça o merge `pcpe` → `main` com push (worktree temporário, ver §0), com autorização do dono.
3. Backup novo da produção; depois: `pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --json web/lote-mcn.json` e, em `web/`, `npx tsx scripts/questoes-ineditas.ts lote-mcn.json --retirar-ausentes --remoto` (demora vários minutos; rode em segundo plano e acompanhe). Confirme com `npx tsx scripts/questoes-ineditas.ts --contar --remoto` (esperado: ≈ 2.590 + 409 = ≈ 3.000 inéditas no total) e apague `web/lote-mcn.json`.
4. Depois do deploy, confirme no app (Browser pane ou `preview_start`) que um caderno curto abre com 25 questões. A regra de completar usa `Activity.dayIndex`/`week.index`; planos antigos sem `dayIndex` não completam (comportamento esperado).

## Etapa B — Corrigir os 76 resumos analíticos em rascunho

**Contexto.** Os resumos analíticos (`content/summaries/<disc>/<aula>.json`, campos `analytic` e `synthetic`) dos trechos do PCPE estão `DRAFT` e aparecem ao aluno com o selo "rascunho". A triagem automática (`pipeline/summary_coverage.py`) marcou **76 trechos** como REVISAR (67) ou REFAÇÃO (9); a lista está em `pipeline/briefs/pcpe-resumos-76.json` (campos `trecho`, `cobertura`, `palavras`, `veredito`, `faltam`). O relatório anterior (`content/audit/pcpe-resumos.md`) concluiu, de forma genérica, que "os termos faltantes são ruído": **não confie nele**. Eu verifiquei amostras e há lacunas reais.

**O que NÃO fazer.** Não mude o `status` para `APPROVED` (decisão do dono, depois de amostragem pedagógica). Não altere `fingerprint` (impressão digital do trecho). Não edite `content/items/` nem `structure/`/`segments/`. Não copie texto do material-base: o validador reprova 16 palavras seguidas iguais à fonte (aviso de 10 a 15). Nada de "a aula", "o curso", "o PDF", páginas ou nome do provedor no texto.

**Ferramentas.**
- `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/pcpe_tools/res_ctx.py <trecho> [N]`: mostra cobertura, seções do resumo atual, os N termos específicos da fonte que faltam e um trecho de contexto de cada um.
- `pipeline/pcpe_tools/res_qs.py <trecho>...`: lista os enunciados das questões de uma seção de exercícios.
- `pipeline/summary_source.py <trecho>` (texto-fonte protegido: só para entender), `pipeline/pcpe_tools/seg_summary.py <trecho>` (resumo atual), `pipeline/briefs/summary.md` (**norma de escrita; leia inteiro**).

**Método, por trecho (um de cada vez):**
1. Leia o resumo atual e a fonte (`summary_source.py`), não só a lista de termos. Classifique o trecho:
   - **(a) Seção de exercícios/gabaritos** (a lista abaixo): o resumo atual descreve "blocos de questões" e **lista gabaritos de questões que o aluno não vê** (`A, E, B...`), o que não ensina nada. Reescreva como **guia de método**: regras, passo a passo, 3 a 5 exemplos resolvidos **autorais** (troque nomes e números), pegadinhas recorrentes e como a banca cobra (use os enunciados de `res_qs.py` para saber quais tipos aparecem). Nada de gabarito por letra.
   - **(b) Conteúdo com omissão real** (classificações, tabelas, exceções, números, súmulas que a fonte trata e o resumo não): complemente. Mantenha o que está correto e **acrescente seções** ou itens; reescreva só o que estiver errado ou vago.
   - **(c) Termos faltantes são ruído** (nomes de personagens de exemplos, números de questões, "vídeos/dúvidas" de abertura de curso): não mexa; registre o trecho e o motivo em `content/audit/pcpe-resumos.md`.
2. **Verifique cada fato** que escrever: leis na fonte oficial (Planalto etc.), valores na norma vigente em out/2026 (o material do curso já inclui alterações de 2024–2026; quando o material estiver desatualizado, siga a lei e **registre em `notes`** do arquivo da aula para revisão humana). Não cite súmula, tema, ADI ou HC que não consiga confirmar.
3. **Contas**: refaça todas à mão (Matemática, Estatística, Contabilidade, Raciocínio Lógico) e mostre o passo a passo no exemplo.
4. **Formato do `analytic`**: abertura de 1–2 frases; ≥ 3 seções `###`; tabelas markdown (sempre com `| --- |`) para classificações e comparações; blocos `> 💡 Exemplo:`, `> ⚖️ Base normativa:`, `> ⚠️ Pegadinha:`; termina com `### Para fixar` com **5 a 8 itens em lista**. Alvo de tamanho: o que o conteúdo pede, até o teto de `targetWords` em `content/summaries/_queue.json` (+25% bloqueia; mínimo ≈ 250 palavras; ≤ 20 min de leitura ≈ 2.000 palavras).
5. **Formato do `synthetic`** (a seção Bizu): 6 a 12 pontos, cada um `**Ponto**: regra + exceção/número/exemplo` (110 a 320 palavras no total), diferente do analítico. Reescreva o sintético dos trechos do tipo (a): hoje ele diz coisas como "Bloco 1 concentra negações".
6. Grave com a ferramenta Write/um script Python que altera **só** o `analytic`/`synthetic` do trecho no JSON da aula (preserve o resto do arquivo e a codificação UTF-8).
7. Valide **a cada aula**: `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_summaries.py content/summaries/<disc>/<aNN>.json` (sem erro de tamanho, seções, originalidade, impressão digital) e `pipeline/summary_coverage.py --subject <disc>` (a cobertura do trecho deve subir ou o motivo do ruído deve estar documentado). Meta de qualidade: nenhum trecho do tipo (b) abaixo de **0,55** de cobertura sem justificativa, e leitura final como aluno: "dá para responder as questões do assunto só com isto?".
8. Ao fechar uma disciplina: `pipeline/.venv/Scripts/python pipeline/apply_synthetic.py` (grava o sintético em `bizu.summary` de `content/items` e `web/content/items` e **espelha** `summaries/importance/contests` em `web/content`) e, em `web/`, `npx tsx prisma/seed-structure.ts` no banco **local**; confira o trecho no app. Nenhuma gravação na produção sem backup e autorização (o seed de produção roda no build da Vercel).

**Prioridade e carga (76 trechos; ordem por pior cobertura/relevância):**
- **Tipo (a), guias de método** (10, Raciocínio Lógico): `raciocinio-logico/a02/s11`, `a02/s10` (já tem boa parte; completar), `a04/s11`, `a04/s12`, `a05/s09`, `a05/s10`, `a00/s10`, `a00/s11`, `a01/s08`, `a04/s01`. Temas: proposições e negação em linguagem natural; conectivos e valoração; tautologia/contradição/contingência e precedência; equivalências e negações (contrapositiva, "ou" em condicional, De Morgan, negação de condicional e bicondicional); questões clássicas de conectivos (formatos fáceis, cadeias de condicionais); argumentos (validade × veracidade, modus ponens/tollens, silogismo hipotético, dilemas, falácias formais e informais, dedução/indução/abdução/analogia).
- **Tipo (b) provável, conteúdo faltando** (prioridade alta): `direito-penal/a02/s04, a02/s03, a02/s08, a02/s01, a00/s01, a00/s02, a04/s01` (classificações dos crimes: habitual, complexo, multitudinário, de impressão, vagos, olvido, de tendência interna...); `direito-processual-penal/a04/s02..s05, s07, a06/s03..s05`; `lingua-portuguesa/a13/s03..s06` (Manual de Redação: siglas, abreviaturas, expedientes) e `a07/s02, a04/s05, a11/s05`; `estatistica/a01/s03, a01/s04, a03/s01, a03/s02`; `contabilidade-geral/a00/s01, a01/s01, a02/s01, a05/s01, a07/s01`; `legislacao-penal-especial/a20/s04, a21/s03, a12/s01`.
- **Triar com cuidado (muitos são ruído; só mexa se achar omissão real):** `matematica/*` (8), `informatica/*` (6), `direito-administrativo/*` (12), `direito-constitucional/*` (6).
- Relatório final da etapa: tabela trecho → tipo (a/b/c) → ação → cobertura antes/depois, em `content/audit/pcpe-resumos.md` (substitua o conteúdo genérico atual).

## Etapa C — Questões reais do TecConcursos (quando o dono avisar)

O dono está baixando os cadernos e avisará quando estiverem em `docs/questoes/`. **Não comece esta etapa antes do aviso.** Quando ele avisar:

1. Leia `pipeline/questoes/EXTRACAO.md` (e `docs/questoes/COMO-EXTRAIR-QUESTOES.md`). Os cadernos a montar estão em `PCPE-CADERNOS-TEC.md/.csv` (34 cadernos, filtro **Cebraspe**). **Importante:** o `importar.py` hoje classifica as matérias do CBMPE/PMPE; para as matérias do PCPE (Legislação PCPE, Raciocínio Lógico, Contabilidade, Estatística, Legislação Penal Especial etc.) é preciso **curar `content/questoes/mapa-assuntos.json`** (matéria/assunto do TEC → disciplina/aulas, ou `skip`) usando `content/edital/pcpe/*.json`. Questão de assunto sem curadoria e de baixa confiança entra `DRAFT`; as decisões de `/admin/revisao` marcam `classifiedBy = MANUAL` e são preservadas.
2. Rode a extração/importação **primeiro no banco local**: `pipeline/.venv/Scripts/python pipeline/questoes/importar.py --so-extrair` e depois sem a flag; confira o relatório (contagens por trecho/item, `kind` múltipla escolha e Certo/Errado, anuladas descartadas, figuras em `QuestionImage`). Rode `pipeline/questoes/auditoria.py` (só leitura) e corrija divergências antes de qualquer escrita remota.
3. Produção: backup íntegro < 24 h; `importar.py --remoto --confirmo-producao` (gravação em massa); `web/scripts/questoes-contagem.ts --remoto` para conferir.
4. **Aposentar as inéditas redundantes**: `cd web && npx tsx scripts/questoes-ineditas.ts --aposentar --remoto --minimo N` (inéditas de assunto que já tem N reais viram `RETIRED`). Escolha N com o dono (sugestão: 8 por trecho). Cuidado para não deixar cadernos curtos: a aposentadoria só é segura se as reais cobrirem o mínimo.
5. **Refaça a simulação de cadernos com os números reais**: `cd web && npx tsx scripts/pcpe-segcounts.ts --remoto` (grava `pipeline/.cache/pcpe-segcounts.json`), `npx tsx scripts/pcpe-plan-grid.ts`, `npx tsx scripts/pcpe-plan-test.ts` e `pipeline/.venv/Scripts/python pipeline/pcpe_tools/cadernos_sim.py --so-banco`. Meta: **0 cadernos curtos**; se sobrar algum, acrescente inéditas (Etapa C.6).
6. Escrevendo inéditas novas (se necessário): rascunho em `pipeline/briefs`-style (`@@ aNN/sMM | A [| item=cod]`, enunciado, `A)`..`E)` com a **correta sempre como A)**, `// Comentário:`), depois `pipeline/.venv/Scripts/python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <disciplina> [--dry]`, que embaralha a posição da correta (balanceando as letras) e anexa a `content/questoes/ineditas/mc/<disciplina>.txt`. Regras de qualidade: ver `pipeline/briefs/ineditas-cobertura.md` e `pipeline/briefs/pcpe-correcoes.md` (T1): 5 alternativas homogêneas e plausíveis, uma correta indiscutível; correta **não pode ser a mais longa** (o validador acusa > 1,8× a média das demais); comentário explica o conteúdo e **não cita letras das erradas**; refaça contas à mão; confira a lei na fonte oficial; nada de súmula/tema/ADI não confirmado; sem "a aula/o curso". `ineditas_mc_nativas.py --check` deve terminar com `erros 0`. Em `lingua-portuguesa/a00/s01` use `| item=3`.
7. Atualize `PCPE-CADERNOS-TEC.md` marcando o que já foi importado e **gere `PCPE-PRIORIDADE-TEC.md/.csv`** só se o dono ainda precisar baixar mais: ordem de prioridade = peso esperado do assunto na prova do PCPE (`content/importance/segments.json`, `contests.PCPE_AGENTE.expected`, e o nº de questões da prova por disciplina em `content/contests.json`) × déficit de questões **reais Cebraspe** por trecho; colunas: posição, caderno, matéria no TEC, assunto, trechos, peso, reais hoje, meta, acumulado.

## Etapa D — Verificação final e liberação

1. `cd web && npm run typecheck && npx vitest run` (576+ testes passando); `npx eslint` nos arquivos alterados (o erro de `practice-actions.ts:46` é anterior e não é seu).
2. Planos de teste: `npx tsx scripts/pcpe-plan-test.ts` e `pipeline/.venv/Scripts/python pipeline/pcpe_tools/audit_planos.py`: 0 cadernos que não abrem, rótulos sem pendência, resumos sem impressão digital divergente. `npx tsx scripts/verify-plans.ts --remoto` para os planos reais pendentes (relatório LIBERAR/BLOQUEAR em `web/reports`; **só** `--apply` com autorização do dono).
3. `cd web && npx tsx scripts/compare-plans-main.ts` deve manter **0 divergências** de CBMPE/PMPE.
4. Pendências conhecidas que o dono decide (não faça sozinho): aprovar resumos (`APPROVED`), reativar o simulado do PCPE, liberar planos em análise.

## Etapa E — Documentação e memória

Atualize `PCPE-PROGRESSO.md` (topo), `HISTORICO.md` (seção 8) e `content/questoes/ineditas/REVISAO-AAAA-MM-DD-*.md` com: números por etapa, dúvidas do material para revisão humana (norma desatualizada, ambiguidades), e os comandos exatos executados. Commits por etapa, mensagens em português, sem `git add -A`.

## Critérios de aceite (o dono vai conferir)

- Produção com as 409 inéditas e a regra de completar caderno ativa; nenhum caderno do PCPE abaixo do pedido nas simulações.
- Os 76 trechos tratados e documentados (tipo a/b/c), validadores sem erro, nenhum gabarito por letra dentro de resumo, nenhuma cópia do material-base, status ainda `DRAFT`.
- Questões do TEC importadas e auditadas, com as inéditas redundantes aposentadas **sem** reabrir cadernos curtos.
- Testes e lint verdes; CBMPE/PMPE sem divergência; nada de segredo ou texto protegido versionado.
