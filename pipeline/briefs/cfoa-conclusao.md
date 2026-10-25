# Briefing de passagem: concluir a inclusão do 2º Tenente CFOA CBMPE e importar as questões novas

Você assume um trabalho em andamento. **Leia este documento inteiro antes de agir.** Ele foi escrito em 24/10/2026 por quem
conduziu a inclusão; tudo o que está marcado como "feito" foi verificado, e o que está em "pendente" **não foi feito**.
Repositório: `C:\Users\Administrador\Documents\Projetos\CFO-BM` (Windows; use `pipeline/.venv/Scripts/python`, defina
`PYTHONIOENCODING=utf-8`). Leia também `CLAUDE.md` (convenções), a seção 13 e 14 do `HISTORICO.md`, `CFOA-CADERNOS-TEC.md` e
`pipeline/briefs/cfoa-inclusao.md`.

## 0. Regras que valem o tempo todo (não negociáveis)

1. **Nunca grave em produção (Neon) sem a autorização explícita do dono, dada no chat, para aquela operação.** Gravação em massa
   exige backup íntegro de menos de 24 h (`npx tsx web/scripts/questoes-backup.ts --remoto`) e `--confirmo-producao` no importador.
   O dono já autorizou, em 24/10, a gravação das **inéditas** do CFOA; **qualquer outra gravação precisa de nova autorização**.
2. **Nunca** versione, publique nem copie texto verbatim de `docs/` (PDFs com marca d'água do aluno). Só dados derivados.
3. **Nunca** imprima, edite ou sobrescreva `.env*`. Não digite senhas do dono: o login no TecConcursos é sempre feito por ele.
4. **Não baixe nem imprima nada no TecConcursos.** O dono monta os cadernos e baixa os PDFs; você só processa o que está em
   `docs/questoes/`.
5. **Nunca** rode `importar.py --limpar-estrategia` sem poupar os ids `mentoria_*`. Nunca `prisma migrate reset`.
6. Commits e push **só na `main`** (instrução do dono) e **só dos seus arquivos** (`git add` explícito). A árvore de trabalho tem
   mudanças de outros agentes (usuário de teste, páginas de pagamento, layout, `initial-status.ts`, `persist.ts`): **não as
   inclua**, não use `git add -A`, `checkout`, `stash` nem `reset`. Para commitar na `main` sem tocar nessas mudanças, use um
   worktree limpo (`git worktree add ../CFO-BM-main-merge main`), faça o merge/cherry-pick ali, dê push e remova o worktree.
   Termine as mensagens de commit com `Co-Authored-By: <seu modelo> <noreply@anthropic.com>`.
7. Idioma pt-BR. Relate o resultado com honestidade: falha de teste se diz, passo pulado se diz.
8. Créditos do dono são escassos: **não dispare dezenas de subagentes sem necessidade**; o limite é 20 simultâneos. Prefira scripts.

## 1. Estado atual (24/10/2026)

**Publicado em produção (main, merge `a33ed64` e seguintes):**
- Concurso `CBMPE_CFOA` (enum, migrações `20261024120000_cfoa_enum` e `..._cfoa_settings`, `ContestSetting` com categoria OFICIAL e
  `examDate` nulo), 9 disciplinas, 365 trechos, resumos, bizus, 7 complementos autorais, planos retidos para análise
  (`CONTESTS_HELD_FOR_REVIEW`).
- **1.333 inéditas de múltipla escolha** do CFOA gravadas no Neon (lote total de 6.509; criadas 1.333, atualizadas 5.176).
- **Acesso sem prazo até a data da prova ser cadastrada** (`grantAccessUntilExam` libera com `accessUntil = null`;
  `applyExamDateToContracts` aplica o limite a todos os contratantes quando a data é salva). Página **Administração › Concursos**
  (`/admin/concursos`) para editar categoria, data, preço e desconto.
- Classificação das questões do TecConcursos baixadas em 23/10 (881 decisões de agentes; commit `9fc8793`), **só no banco local**.

**Só na branch `cfoa`/árvore local (ainda não na `main`):**
- Redesenho de `/concursos` (contêineres por órgão, tom por órgão, brasão cortado) — commits `082bcaf`, `bcd6d5e`, `497b725`.
- Correções da **revisão por amostra** (ver §3), no working tree, **sem commit**: `content/questoes/ineditas/mc/{direito-administrativo,
  direito-penal-militar,direito-processual-penal-militar,legislacoes-pe}.txt`, `content/complements/{leg-lei-12527-lai,
  leg-pe-lei-6783-lacunas}.md` e o relatório `content/questoes/ineditas/REVISAO-2026-10-24-cfoa-amostral.md`.

**Não gravado em nenhum banco:** as correções acima e a classificação de 23/10 (nem local, nem Neon, além do que está dito).

## 2. Ordem de execução

### Etapa A — Fechar a revisão de conteúdo do CFOA (prioridade alta)

1. **Direito Penal Militar: revisar as 110 questões do CFOA que ficaram fora da amostra.** A amostra (48 questões) teve 8,33% de
   erro de fato (4), acima do limite de 8%, e o parecer é "REVISAR TUDO ANTES". Identifique as questões do CFOA em
   `content/questoes/ineditas/mc/direito-penal-militar.txt` com `git show f0b5310 -- content/questoes/ineditas/mc/direito-penal-militar.txt`
   (linhas `+@@`). Siga **integralmente** `pipeline/briefs/revisao-amostral-cfoa.md` (§6 e §7: resolver cego, testar cada alternativa,
   conferir números de artigo, pena e inciso na fonte oficial). Os erros achados até aqui eram **capitulação** (artigo/inciso
   inexistente ou trocado, ex.: arts. 20-A/20-C da Lei 7.716, art. 12 da Lei 13.869, art. 191 do CPM), então dê atenção especial a
   número de artigo, inciso, pena e prazo.
2. **Conferir três pontos que a revisão não conseguiu ler na fonte oficial** (o Planalto recusou a leitura): texto do **art. 191, II,
   do CPM** (modalidade complexa: reclusão de 2 a 4 anos?) e do **art. 12, parágrafo único, III e IV, da Lei 13.869/2019** (III = nota
   de culpa em 24 h; IV = prolongar a prisão). As correções feitas assumem isso; se a fonte disser outra coisa, corrija o `.txt`.
   Fontes aceitas: Planalto, ALEPE/legislação estadual, STF/STJ/STM. Use `WebFetch` ou `WebSearch`; o Firecrawl do dono está sem
   créditos.
3. **Ampliar a conferência de capitulação** em Direito Processual Penal Militar, Legislações PE e Direito Administrativo (taxas de
   3,4% a 3,6% na amostra, mas os erros eram do mesmo tipo): faça uma varredura **automatizada** por regex de todas as menções
   "art. N", "§", "inciso" nas inéditas dessas disciplinas e confira as citações mais cobradas na fonte oficial, em vez de reler
   questão por questão.
4. Rode os validadores até zerar erros: `pipeline/questoes/ineditas_mc_nativas.py --check`, `pipeline/questoes/lacunas_cfoa.py --check`,
   `pipeline/validate_content.py`, `pipeline/validate_summaries.py`.
5. Se editou complementos (`content/complements/*.md`), regenere os PDFs com `pipeline/.venv/Scripts/python pipeline/build_complements.py`
   (**depois** de `segment.py`/`build_catalog.py`, se a estrutura mudou; senão, só `--only <id> --no-merge`), e depois o espelho
   `web/public/complementos/` entra no commit. Edições de resumo/bizu pedem `pipeline/apply_synthetic.py` (nunca edite `web/content/` à mão).
6. Atualize `content/questoes/ineditas/REVISAO-2026-10-24-cfoa-amostral.md` com o resultado da revisão integral de DPM.
7. **Commit na `main`** (worktree limpo) com as correções + relatório.
8. **Peça ao dono a autorização** para regravar as inéditas corrigidas no Neon. Com ela:
   ```bash
   pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --json web/lote-mc-cfoa.json
   cd web && npx tsx scripts/questoes-backup.ts --remoto            # backup íntegro (< 24 h)
   npx tsx scripts/questoes-ineditas.ts lote-mc-cfoa.json --retirar-ausentes --remoto
   ```
   **Atenção:** o id de cada questão depende de um hash do texto; texto editado = id novo, e a antiga fica no banco. Por isso aqui
   (e só aqui) use `--retirar-ausentes`, que aposenta (`RETIRED`) as do mesmo batch que saíram do lote. Confira o relatório
   (`retired` deve ser igual ao número de questões editadas). A gravação leva ~40 minutos; rode em segundo plano. Apague `web/lote-mc-cfoa.json` depois.
   Grave também localmente (sem `--remoto`) para os dois bancos ficarem iguais.

### Etapa B — Extrair e inserir as questões novas dos PDFs (pedido do dono)

O dono baixou **11 cadernos novos** em `docs/questoes/` em 24/10/2026 (arquivos com data de modificação 24/10 23:43 a 23:45):
`Caderno Física, Química, Estat e Info 9`, `Caderno Raciocínio lógico 2, 3 e 4`, `Caderno Direito Administrativo Atualidades Espanhol
Direito Penal Militar Inglês Física 11`, `Caderno Estatística Química Biologia Legislação AOCP 9`, `Caderno Informática e Constitucional 6 e 7`,
`Caderno Matemática e Português 8`, `Caderno Falta Matemática, Consti, Penal, Racio e Adm 21 e 22`. Leia
`docs/questoes/COMO-EXTRAIR-QUESTOES.md` (cópia de `pipeline/questoes/EXTRACAO.md`).

Siga **exatamente** o fluxo que já funcionou na rodada de 23/10 (relatório `docs/questoes/relatorios/2026-10-24-0021.md` e `HISTORICO.md`
§14):

1. **Extrair sem tocar em banco:**
   ```bash
   pipeline/.venv/Scripts/python pipeline/questoes/importar.py --so-extrair
   ```
   Ele extrai só os PDFs novos (por hash), classifica com `classify.py` (TF-IDF + `content/questoes/mapa-assuntos.json` +
   `overrides-questoes.json`) e grava um relatório em `docs/questoes/relatorios/`. Leia o relatório: totais, quantas ficaram `DRAFT`
   (rascunho = sem assunto confiável), fora do edital, anuladas, em quarentena e **erros de extração** (se houver PDF com falha,
   investigue com `pipeline/questoes/auditoria.py`, nunca "conserte" pulando a questão).
2. **Classificar os rascunhos com agentes** (o que reduziu 1.430 rascunhos para 168 na rodada anterior), só se o número de rascunhos
   novos justificar (> ~150):
   ```bash
   pipeline/.venv/Scripts/python pipeline/questoes/pacotes_rascunhos.py     # gera pacotes em docs/questoes/classificacao-agentes/<data>/pacotes
   ```
   Siga `docs/questoes/classificacao-agentes/2026-10-24/INSTRUCOES.md` (copie para a pasta nova). Cada agente lê um pacote, consulta a
   taxonomia da disciplina (`taxonomia/`) e grava `resultados/<pacote>.jsonl` com uma linha por questão:
   `{"tecId","acao":"classificar|skip","segment","itemEdital","confianca":"alta|media|baixa","motivo"}`. Regras: `skip` quando o assunto
   está fora do edital; confiança baixa continua rascunho; **o agente nunca sobrescreve decisão existente**. Limite de 20 agentes
   simultâneos; prefira poucos pacotes grandes. Depois confira integridade (todo `tecId` do pacote tem resultado, sem repetição) e rode
   `pipeline/questoes/aplicar_agentes.py <pasta>` (grava em `content/questoes/overrides-questoes.json`).
3. **Corrigir o mapa quando o erro for sistemático** (não questão por questão): ajuste `content/questoes/mapa-assuntos.json`.
   Pendências conhecidas do mapa (do §14 do `HISTORICO.md`): Lei 9.099/1995 (80 questões em `skip`, deveriam ir para
   `direito-processual-penal/a06`), 14 questões de conjuntos (matemática → `raciocinio-logico/c01/s01`, mas o consumidor pode não
   aceitar trecho de outra disciplina), uma questão de licitações caída em `direito-administrativo/a22/s03` (licitações estão fora do edital). **Não aplique
   remapeamentos sem confirmar com o dono** — proponha no relatório.
4. **Reimportar localmente** (`importar.py` sem `--so-extrair`, **só banco local**, URL em `web/.env`) e confira:
   `npx tsx web/scripts/questoes-contagem.ts` (só leitura). Rode `pipeline/.venv/Scripts/python pipeline/questoes/lacunas.py` e
   `lacunas_cfoa.py` e compare com a tabela de lacunas do `HISTORICO.md` §14.
5. **Commit na `main`** (worktree limpo) de `content/questoes/mapa-assuntos.json` e `overrides-questoes.json` e do que mais for do
   repositório (nunca `docs/`, que está no `.gitignore`).
6. **Produção:** só com autorização do dono. Procedimento: backup novo (`questoes-backup.ts --remoto`, depois `--verificar <pasta>`),
   simulação, e só então `importar.py --remoto --confirmo-producao`. Consulte `CLAUDE.md` (convenção de questões) e a auditoria de
   14/10 antes: o que mudou de `classifiedBy` (decisões `MANUAL` em `/admin/revisao` são preservadas pelo importador). **Nunca**
   use `--reclassificar` ou `--forcar` sem pedir.
7. Atualize `HISTORICO.md` (nova linha em §14 com os números desta rodada) e entregue um relatório ao dono: totais por situação,
   tabela de lacunas por disciplina, achados dos agentes, decisões pendentes.

### Etapa C — Itens menores

1. **Liberar os planos do CFOA** quando o dono pedir (hoje nascem em `PENDING_ANALYSIS`): remover `CBMPE_CFOA` de
   `CONTESTS_HELD_FOR_REVIEW` em `web/src/lib/plan/initial-status.ts`. **Esse arquivo tem alterações não commitadas de outro agente**
   (parâmetro `testUser`): não inclua essas alterações; combine com o dono antes de mexer.
2. **Verificar planos** com `npx tsx web/scripts/verify-plans.ts --remoto --status PENDING_ANALYSIS` (somente leitura) quando houver planos de
   CFOA na produção, e só então `--apply` com a aprovação do dono.
3. Quando sair o edital: o dono cadastra a data em **Administração › Concursos**; o sistema aplica o limite aos contratantes. Conferir
   uma contratação de teste depois, no ambiente local.
4. Decretos estaduais não encontrados (17.589/1994, 19.896/1997, 28.486/2005, 43.195/2016): se o dono achar os textos, criar
   complementos conforme `pipeline/briefs/complement.md`.
5. Aviso de segurança do Next.js (`next upgrade --agent=security`): tarefa **separada**, não parte da inclusão do CFOA. Só com pedido do dono.
6. Quando as questões reais do TecConcursos cobrirem um assunto, `questoes-ineditas.ts --aposentar --simular` mostra o que seria
   aposentado. **Não aposente sem o dono**: o CBMPE Oficial usa inéditas como reforço (exige `--sei-do-cbmpe`).

## 3. Resultado da revisão por amostra (resumo; detalhes em `content/questoes/ineditas/REVISAO-2026-10-24-cfoa-amostral.md`)

325 de 1.333 inéditas auditadas (seed 20261024). Taxa de erro de fato: Administração 0%, Direitos Humanos 0%, Dir. Constitucional 0%,
Língua Portuguesa 0%, Raciocínio Lógico 0%, Dir. Processual Penal Militar 3,5%, Legislações PE 3,6%, Dir. Administrativo 3,4%,
**Direito Penal Militar 8,3% (parecer: revisar tudo)**. 7 questões corrigidas, 2 reescritas, 2 complementos ajustados. Resumos e bizus
amostrados (33 trechos e 12 arquivos): sem erro de fato. Correções verificadas pelo autor deste briefing contra o Planalto:
Lei 7.716 (arts. 20 §2º-A, 20-B, 20-C), CPM art. 132 e art. 191 inciso I, Lei 8.457 art. 30 I-B, Lei 13.869 arts. 7º e 8º, Lei 14.133 art. 39.
**Não verificadas na fonte oficial** (ver Etapa A.2): CPM art. 191 II e Lei 13.869 art. 12, parágrafo único.

## 4. Como validar que terminou

- `ineditas_mc_nativas.py --check` e `lacunas_cfoa.py --check` sem erros; `validate_content.py` e `validate_summaries.py` sem erros.
- `cd web && npm run typecheck && npm run lint` sem erro novo; `npx vitest run --project unit` passando; os testes de integração de
  comércio (`npx vitest run --project integration src/lib/commerce`) levam ~6 min e passaram em 24/10 (rode em segundo plano).
- `git status` sem arquivos seus esquecidos; `main` enviada ao GitHub; nenhuma gravação em produção sem a autorização registrada no chat.
- Entregue ao dono: o que mudou, os números, o que ficou pendente e as decisões de que ele precisa (remapeamentos, liberação dos planos,
  autorizações de gravação).
