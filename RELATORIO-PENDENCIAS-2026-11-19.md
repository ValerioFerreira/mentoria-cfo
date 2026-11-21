# MentorIA · Relatório de entrega e pendências

Posição em **19/11/2026, à noite**. Cobre o trabalho das sessões de 16 a 19/11: comentários das questões, riscar alternativa, reprogramar atividades, PDFs do material, Termos de Uso, aviso dos PDFs e o deploy em produção.

## 1. Resumo em dez linhas

1. A `main` está em `7d1eb1f` e o deploy de produção terminou. Termos novos no ar, três migrações novas aplicadas no Neon, 71 PDFs refeitos no R2.
2. **6.983 comentários de questões** foram gravados na produção (0 falhas). Hoje 96,6% dos cadernos pendentes dos planos ativos saem inteiros comentados (eram 87,3% antes).
3. O histórico dos alunos não foi tocado: 117 sessões de caderno e 2.487 respostas iguais antes e depois.
4. **Riscar alternativa** (dois cliques) e **Reprogramar atividades atrasadas** estão em produção.
5. Os **PDFs** deixaram de carregar comentários errados da Fixação (398 comentários em 57 volumes dos PDFs estavam diferentes da versão revisada) e o cabeçalho do comentário agora é só "Comentário".
6. **Termos e Privacidade** seguem as decisões do dono de 04/11 e de 19/11 (idade mínima 16, garantia só sem PDF aberto, compartilhamento com aviso e bloqueio, e-mails de novidades só com concordância, retenção de 12 meses).
7. CPF e nome: o PDF só abre depois de o aluno informar o CPF e confirmar o nome completo, que fica em caixa alta.
8. Falta o **dono decidir** sobre 386 questões descartadas dos comentários, ler a amostra, e autorizar a aposentadoria de questões desatualizadas.
9. Falta **terminar a fila** dos comentários (268 questões, parte C) e regravá-la.
10. Falta **testar na produção** o pop-up, o PDF com carimbo e o pedido de CPF, e **atualizar o Next 16.4.0** (aviso de segurança).

---

## 2. O que foi feito

### 2.1 Comentários das questões (16–19/11)

**O que são.** Para cada questão do banco (fonte única: TecConcursos): um comentário geral (50 a 250 palavras) em `Question.explanation` e uma nota por alternativa em `QuestionOption.comment` ("Correta:" só no gabarito, "Errada:" nas demais; Certo/Errado leva só o comentário geral). Aparecem sob cada letra depois que o aluno responde, no caderno, no treino, no simulado e em `/admin/revisao`.

**Como funciona (para quem for mexer depois).**
- Fonte versionada: `content/questoes/comentarios/<disciplina>/<lote>.json`. **Só** `web/scripts/questoes-comentarios.ts` grava no banco, e só se o `contentHash` e o gabarito da questão conferem.
- Padrão do script é simulação. Para gravar: `--aplicar`; na produção: `--remoto --aplicar --confirmo-producao`, e com mais de 300 comentários exige backup íntegro de menos de 24 h.
- Validador: `pipeline/questoes/validate_comentarios.py` (esquema, gabarito, tamanhos, neutralidade de concurso, citação de artigos contra `pipeline/leis.py`, originalidade). Hoje: 743 arquivos, 6.983 comentários, 0 erros, 324 avisos (coincidências de 10 a 15 palavras com texto de lei ou definição).
- O sorteio do caderno **prefere questões comentadas** (`pickPreferCommented`): própria comentada, extra comentada, própria sem comentário, extra sem, reforço. Isso reduziu a fila de comentários de 13.331 para cerca de 4.100 questões, porque cada caderno só precisa de "o que pede + 10" comentadas no seu pool.

**Produção, depois de gravar.**

| Medida | Antes | Depois |
|---|---|---|
| Questões já sorteadas nos cadernos (808) com comentário | 782 (96,8%) | 782 (96,8%), todas já no banco |
| Cadernos pendentes (2.585) inteiros comentados | 2.257 (87,3%) | **2.497 (96,6%)** |
| Cadernos pendentes cobertos também com margem de 10 | 1.907 | 2.010 |
| Cadernos com alguma questão sem comentário | 328 | **88** (cerca de 522 questões; 2 sem nenhuma comentada) |

**Divisão do trabalho.** A fila foi dividida em três partes sem lote em comum: A (esta sessão, concluída), B (outro agente, concluída) e C (outro agente, **268 questões em 49 lotes ainda pendentes**).

**Defeitos achados e corrigidos.**
- **Comentários da Fixação do material escritos para outra questão ou com erro** (volumes inteiros de Inglês, Biologia, Informática, Direito Constitucional, Espanhol; erros de artigo, de conta e de conceito). Os 1.993 comentários aproveitados foram revisados um a um por 17 listas de agentes (`revisaoNotas`: 578 ajustes, 156 erros, 95 trocados, 21 descartes).
- **Prefixo duplicado**: 1.129 notas em 55 arquivos apareciam na tela como "Errada: Errada. …". Corrigido nos arquivos, regravado, e o validador agora recusa a repetição. Três notas ficaram curtas demais depois da correção e foram ampliadas.

### 2.2 Riscar alternativa e Reprogramar atividades (16–18/11)

- **Riscar:** dois cliques riscam a alternativa (lógica pura em `lib/quiz/eliminations.ts`, memória na `sessionStorage` por caderno, também no simulado). Está em produção.
- **Reprogramar** (`/reprogramar`, botão na Missão de hoje e no banner da semana): opções espalhar, encaixar nas folgas, recalcular o restante, mover para um dia e dispensar. Todas reorganizam as dependentes (Teoria → Revisão → Fixação → Questões), não mudam minutos, não passam de D-2 e não tocam D-1. Grava `Activity.rescheduledAt` e `Plan.params.reschedules`. O verificador de planos trata excesso de carga em atividade reprogramada como aviso. 36 testes unitários do motor.
- **Limite conhecido:** planos reais estão quase 100% cheios, então "espalhar" e "encaixar" costumam deixar atividades sem lugar e a tela sugere "recalcular".
- Foi verificado só no banco local, com o usuário de teste. Na produção ainda não foi exercitado por um aluno.

### 2.3 PDFs do material (71 volumes do CFOA)

- **Fixação corrigida:** regravados os comentários e as notas revisados em 118 volumes (1.718 questões). 21 questões descartadas por qualidade saíram dos volumes. Para repor a meta entraram 10 questões novas: 2 (de DA m17 e m18) citavam a Lei 8.666/1993, revogada, e foram retiradas; as outras 8 receberam comentário novo (DA m06 e m11, DC m04, m07, m11, m12, LP m04 e m08).
- **Cabeçalho do comentário** é só "Comentário" (sem "Gabarito X"), e a frase "Cubra o comentário com uma folha…" saiu. A conferência do PDF foi ajustada para exigir o título "Comentário" abaixo de cada questão.
- Os 71 PDFs foram refeitos e conferidos e estão no **R2** (conferência por MD5 contra o ETag: 71 de 71).
- **Registro de abertura**: tabela `MaterialOpen` (aluno × volume: primeira e última abertura e contagem), gravada pela rota do PDF. Sustenta a regra de garantia dos Termos.
- **CPF e nome**: a rota leva o aluno sem CPF a `/perfil?cpf=necessario`. O cartão pede o CPF, o nome completo (pré-preenchido, vai para caixa alta e é gravado em `User.name`) e uma caixa de confirmação. O CPF é validado pelos dígitos verificadores. O carimbo do rodapé mostra "LICENCIADO PARA NOME · CPF 000.000.000-00" (verificado num PDF real).

### 2.4 Termos de Uso, Privacidade e pop-up

- **Termos e Privacidade** (atualizados em 19/11/2026): idade mínima 16 anos, com autorização do responsável de 16 a 17 (caixa obrigatória no cadastro e na inscrição, validada também no servidor); garantia de 7 dias só se nenhum PDF foi aberto (aviso também no formulário de inscrição); compartilhamento do material ou da conta = 1 aviso por e-mail e depois bloqueio sem devolução; seção nova "Comunicações" (hoje não há e-mails de novidades; se houver, pedirá concordância); retenção de 12 meses depois do encerramento; provedores citados por categoria, não por nome; CPF e confirmação do nome descritos.
- **Pop-up "Chegaram os PDFs do MentorIA"**: aparece uma vez, no primeiro acesso depois do deploy, para quem tem plano ACTIVE ou PENDING_ANALYSIS do CFOA. Sem menção a CPF. É marcado como visto assim que aparece (`User.seenNotices`), então não volta. Hoje só **2 usuários** da produção têm plano do CFOA.

### 2.5 Deploy e verificações (19/11)

1. Build de produção local: ok. 2. Backup das questões da produção em `backups/questoes-remoto-20261119-213308`: íntegro. 3. PDFs ao R2. 4. `git merge -s ours origin/main` (a árvore ficou idêntica à da branch; o único commit da `origin/main` era o revert `89f6713`). 5. Push de `material-correcoes-avaliacao` e de `main` (`89f6713` → `7d1eb1f`, fast-forward). 6. Deploy confirmado pelos Termos novos no ar e pelas migrações no Neon.

**Migrações aplicadas na produção** (todas só acrescentam coluna ou tabela): `20261103120000_cpf_e_erros_material`, `20261116120000_question_option_comment`, `20261118120000_activity_rescheduled_at`, `20261119120000_material_open_and_notices`.

**Integridade depois do deploy:** 117 sessões e 2.487 respostas iguais; as atividades concluídas (355) e os tempos lançados (401) só cresceram, porque os alunos estudaram durante o dia.

### 2.6 Commits desta rodada (branch `material-correcoes-avaliacao`, já na `main`)

`1256fd9` comentários, riscar e reprogramar · `3a0864c` Fixação revisada e 6.091 comentários · `f38d64b` lotes de B e C · `0c3a9b2` Termos, pop-up, registro de abertura e CPF · `98e715b` aviso marcado ao aparecer e usuário de teste · `fc1d0f1` script do usuário de teste · `8c54f83` cabeçalho do comentário · `7d1eb1f` merge.

### 2.7 Ferramentas novas (para reaproveitar)

- `web/scripts/comentarios-cobertura.ts [--remoto]`: mede a cobertura de comentários nos cadernos dos planos (só leitura).
- `web/scripts/create-cfoa-test-user.ts [--atrasadas]`: usuário local `cfoa@teste.com` (senha `teste`), plano ativo do CFOA, sem CPF; com `--atrasadas` o plano começa ontem.
- `web/src/lib/person-name.ts`: normaliza o nome completo em caixa alta.
- `pipeline/questoes/dividir_partes.py --status`: andamento das partes A, B e C.

---

## 3. O que falta concluir

Legenda de prioridade: **P1** antes de divulgar aos alunos · **P2** próximos dias · **P3** quando houver tempo.

### 3.1 Decisões do dono

| # | Pendência | Detalhe | Prioridade |
|---|---|---|---|
| D1 | **386 questões descartadas dos comentários** | Descartadas pelos autores por problema da questão. Nenhuma foi rebaixada no banco; elas continuam servidas, só sem comentário. Distribuição por disciplina: Direito Administrativo 165, Direito Constitucional 44, Estatística 43, Biologia 28, Direito Penal Militar 27, Língua Portuguesa 16, Administração 15, Química 15, Física 9, Informática 9, Contabilidade 6, Matemática 4. Por motivo (classificação automática pelas palavras do motivo, aproximada): cerca de 159 gabarito duvidoso ou divergente da norma, 91 licitações e Lei 8.666, 41 outras normas revogadas, 17 dependem de figura ausente, 11 abuso de autoridade (Lei 4.898/65), 6 improbidade antes da Lei 14.230/2021, 61 outros. Escolher, por grupo: manter, corrigir o gabarito, ou aposentar. | P2 |
| D2 | **Questões da Lei 8.666 com gabarito ainda válido** | Foram comentadas com aviso de que a lei foi revogada. Decidir se todas viram descarte. | P2 |
| D3 | **Amostra de leitura** | `content/questoes/comentarios/amostras/lote-01.md`: o dono leu? Se houver ajuste de estilo, vale para os lotes seguintes. | P2 |
| D4 | **Aposentar questões desatualizadas na produção** | No banco local há 1.853 questões aposentadas (1.789 existem na produção). Na produção já há 1.607 aposentadas; aplicar a lista retiraria cerca de 250 que lá ainda estão aprovadas. Há 21 respostas de alunos nelas (o histórico fica) e 2 em cadernos abertos. **Antes de aplicar**, tirar da lista as questões que estão em caderno aberto de aluno. Precisa de backup novo e `--confirmo-producao`. | P2 |
| D5 | **Leitura de advogado** | A regra "abrir qualquer PDF encerra a garantia de 7 dias" é mais restritiva que o art. 49 do Código de Defesa do Consumidor. Também validar a idade de 16 a 17 anos e a retenção de 12 meses. | **P1** |
| D6 | **Parceiro "vê só o nome"** | A decisão de 04/11 falava nisso, mas o painel do parceiro mostra só totais (e a Política diz isso). Mostrar o nome do indicado exigiria mudar o painel e a Política. | P3 |
| D7 | **Reembolso de 7 dias: quem confere?** | O pedido é por e-mail e a conferência exige olhar `MaterialOpen`. Hoje não existe tela; seria consulta direta. Decidir se vale uma tela no `/admin/financeiro`. | P2 |

### 3.2 Trabalho técnico

| # | Pendência | Detalhe | Prioridade |
|---|---|---|---|
| T1 | **Terminar a fila de comentários (parte C)** | 268 questões em 49 lotes. Depois: validar e regravar na produção (`questoes-comentarios.ts --remoto --aplicar --confirmo-producao`, com backup de menos de 24 h; o script só escreve o que mudou). Em seguida, medir de novo com `comentarios-cobertura.ts --remoto`. Também comentar as **8 questões novas da Fixação**, que hoje só têm comentário no PDF. | P2 |
| T2 | **Testar na produção** | Pop-up para um aluno do CFOA, abrir um PDF (carimbo, CPF e nome), Reprogramar e riscar alternativa. Só foram verificados no banco local. Os 2 alunos reais do CFOA veem o pop-up no próximo acesso. | **P1** |
| T3 | **Next 16.4.0** | O build acusa vulnerabilidade conhecida e parou na primeira tentativa (passou na segunda). O aviso traz instruções para rodar um `next upgrade`; não foram seguidas. Tratar em separado, de preferência num Preview. | P2 |
| T4 | **Teste de integração com data fixa** | `access.integration.test.ts` usa `startDate` de 19/10/2026 e falha hoje; nem ele nem `persist.ts` mudaram. Tornar a data relativa. | P3 |
| T5 | **Erros de lint antigos** | 9 erros em arquivos idênticos aos da tag de 10/11 (`seed-structure.ts`, `seed.ts`, `directive-audit.ts`, `simulados/[id]/page.tsx`, `progressive-carousel.tsx`, `practice-actions.ts`). O build não roda o lint. | P3 |
| T6 | **Testes do pipeline que falham** | 4 falhas em Python: complementos (2), Estatística e bizus de Atualidades. Não foram tocados nesta rodada. | P3 |
| T7 | **PDFs fora do índice** | DPM m05 está no R2 por engano desde 16/11 e Física m05 existe no disco; ambos têm Fixação acima da meta e ainda carregam a frase antiga. Apagar do R2 só com OK. | P3 |
| T8 | **Pendências manuais do material** | Figuras, "Para fixar" órfão, cabeçalho de Legislações PE, diagramas Mermaid e a vigência da Lei PE 11.781 × 18.071 (registradas em 12–17/11). | P3 |
| T9 | **Itens de 09–10/11 não reverificados hoje** | Leitura jurídica dos comentários de DC m03, m12 e m17, DH m01 a m03 e DA m09, m11, m13, m15 e m18; 36 cadernos do TecConcursos de 04 a 06/11 não importados; 19 volumes de Fixação abaixo da meta por falta de questões no banco. Conferir se ainda valem. | P3 |
| T10 | **E-mails de novidades** | Hoje não existem. Se forem criados: pedir concordância antes e criar descadastro (preferência no Perfil e link no e-mail), conforme os Termos. | P3 |
| T11 | **CPF e nome: limites conhecidos** | O CPF é validado só pelos dígitos verificadores (rejeita 111.111.111-11), não consulta a Receita. Dois cadastros podem usar o mesmo CPF; nada bloqueia. O nome em caixa alta vale a partir do momento em que cada aluno registra o CPF. | P3 |
| T12 | **Data da prova do CFOA** | O CFOA segue sem data. Ao cadastrar em `/admin/concursos`, os planos de ciclo são refeitos até a prova (`replanCyclePlans`) e o acesso passa a vencer na data. Avisar os 2 alunos antes. | quando houver data |

---

## 4. Riscos, reversão e cuidados

- **Reverter comentários:** `npx tsx scripts/questoes-restore.ts backups/questoes-remoto-20261119-213308 --remoto --aplicar --confirmo-producao` (nunca apaga questão nem toca em respostas). Faça sempre um backup novo (`questoes-backup.ts --remoto`) antes de qualquer gravação grande.
- **Reverter código:** as colunas novas são ignoradas pelo código antigo (foi o que ocorreu em 10/11). Atenção ao **merge**: um merge comum com o revert `89f6713` apagaria o lançamento; por isso foi usado `-s ours`.
- **Banco local (PGlite) é frágil:** cai com muitas consultas ao mesmo tempo e o `search_path` fica preso em schemas de teste depois do vitest. Antes de migrar o banco local: `SET search_path TO public`. Para recuperar: `npx prisma dev stop cfo-bm` e `npx prisma dev -n cfo-bm -d`.
- **Local lê o R2 de verdade:** o `web/.env` tem as variáveis do R2, então o app local abre PDFs do bucket real (só leitura). Cuidado ao rodar `material-r2.ts`.
- **Linha apagada no banco local:** `ContestSetting` com o valor `PCPE_ESCRIVAO` (resquício de outra branch) derrubava o Perfil; foi removida só no local. A produção não tem esse valor.
- **Servidor de desenvolvimento:** o aplicativo o encerra quando fica parado; basta subir de novo (`preview_start web`).
- **Dados que nunca vão em commit:** `docs/` (PDFs protegidos), `.env*`, `backups/`, `material-pdf/`.

---

## 5. Ordem sugerida a partir daqui

1. **Testar na produção** (T2) e decidir a leitura jurídica (D5).
2. Ler a amostra (D3) e decidir os descartes (D1, D2).
3. Terminar a parte C dos comentários, validar e regravar (T1).
4. Preparar a aposentadoria de questões sem as que estão em caderno aberto (D4) e aplicar com backup.
5. Tela de conferência da garantia (D7) e, em separado, o upgrade do Next (T3).
6. Itens P3 conforme houver tempo.
