# PCPE Agente — registro de andamento (retomada de sessão)

> Documento de passagem de bastão. Atualizar a cada bloco concluído. Última atualização: 2026-10-18.
> Quem retomar: leia tudo, confira `git log --oneline | head -20` e `git status`, e continue pelo item **"Onde parei"**.

## 1. Pedido do dono (mensagem 2, resumo fiel)
"Além de todas as sugestões, faça tudo o que é necessário (com exceção da parte de questões; mande somente quais cadernos tenho que montar no TEC para baixar as questões) para o sistema estar com a opção **PCPE Agente** disponível. Reveja todos os resumos e atividades feitas pelo agente anterior, determine o grau de qualidade e, se necessário, refaça."

Contexto: o concurso é **PCPE Agente de Polícia (Cebraspe, prova 07/03/2027, id `PCPE_AGENTE`)**. Um agente de IA anterior inseriu o concurso; os relatórios dele estão em `Downloads\DOCUMENTO_CONSOLIDADO_PCPE_AGENTE.md` e `Downloads\Inclusão da PCPE (Agente de Polícia) — histórico de revisões.md` (fora do repositório).

## 2. Decisões de execução (não rediscutir)
- Trabalhar **inline**, sem subagentes. Tudo **local**: sem push, sem deploy, sem Neon/produção.
- **Questões fora do escopo**: o importador por concurso (card `task_62791f17`) fica pendente; entregar só a lista de cadernos do TEC a montar.
- `available: true` do PCPE em `web/src/lib/contests.ts` + `web/scripts/export-contests.ts` entram **num commit separado, local, por último**.
- Commitar **só os meus arquivos** (por aula: `content/summaries/<disc>/aNN.json` + `content/items/<disc>/aNN.json`). Não tocar no que é de outras frentes (ver seção 7).
- Mensagem de commit: `fix(content): reescreve resumos e bizus de <disc> aNN` (+ resumo curto do que mudou) e o trailer `Co-Authored-By: Claude Sonnet 5.5 <noreply@anthropic.com>`.
- Textos definidos pelo dono (opção Turbo, cartão de pagamento) **não** se reescrevem. `.env*` nunca se imprime nem se sobrescreve. `docs/` é protegido: nunca copiar texto verbatim para `content/`.

## 3. Lista de tarefas (status em 2026-10-18)
1. **Refazer resumos e bizus fracos — EM ANDAMENTO** (seção 5). Decisão: infraestrutura primeiro (tarefas 2–7), depois continuar a reescrita por severidade.
2. **Espelhar conteúdo em `web/content` — FEITO** com `pipeline/pcpe_tools/mirror_web.py` (copia só arquivo ausente/diferente das 12 disciplinas do PCPE; idempotente). **Repetir no fim** (e rodar `python pipeline/apply_synthetic.py` antes: grava o sintético no `bizu.summary` e espelha summaries/importance/contests) e conferir com `python pipeline/pcpe_tools/audit_pcpe.py .` (os 657 trechos precisam ter bizu e resumo em `web/content`).
3. **Edital PCPE por concurso — FEITO**: `EditalItem.onlyContests/excludeContests` (migração `20261018120000_edital_item_contests`, aplicada no dev local), seed (`prisma/seed-structure.ts`: `content/edital/pcpe/<disc>.json` → itens `<disc>/p<código>` só do PCPE; os `<disc>/e<código>` padrão ganham `excludeContests PCPE_AGENTE` nas 7 disciplinas compartilhadas), helper `editalItemApplies` (`src/lib/contests.ts`, com teste), filtros em `onboarding/page.tsx` e `plan/persist.ts`. Seed rodado no dev local sem erro.
4. **Limpezas — PARCIAL**: títulos com "Prof." corrigidos (`title` em `content/overrides.json`, `build_catalog.py`, patch em `catalog.json` e espelho). `category:""` do cartão PCPE **não é defeito** (o card só mostra a categoria se houver; a categoria comercial `PCPE` vem de `ContestSetting`). **Lacunas ainda abertas** (3, severidade média): `rl-operacoes-conjuntos`, `rl-matrizes-determinantes` (raciocínio lógico) e `est-tamanho-amostral` (estatística): precisam de complementos autorais (`content/complements/*.md` com `onlyContests: "PCPE_AGENTE"`, `resolves: <id da lacuna>`, depois `build_complements.py`, bizu/resumo/importância do novo trecho e atualização do edital PCPE). `docs/inventario_pcpe.json` está em `docs/` (protegido, fora do git): ignorar. Falta registrar em `HISTORICO.md`.
5. **Testes/build/seed — PARCIAL**: `pipeline/test_plan_pcpe.ts` (24 cenários, todos LIBERAR, 0 erros), vitest (533 ok; 6 falhas de integração de preço em `commerce/*` **já existiam sem as minhas mudanças**), tsc ok, seed local ok. Pendentes: `compare-plans-main.ts`, lint, `next build`. Falhas conhecidas fora do meu escopo: `pytest::test_authored_items_pass_validator` (atualidades, de outra frente).
6. **Lista de cadernos do TEC — FEITO**: `PCPE-CADERNOS-TEC.md` e `.csv` (34 cadernos, meta ~5.250 questões Cebraspe), gerados por `pipeline/pcpe_tools/gen_cadernos_tec.py`. Enviar ao dono.
7. **Commit de liberação — PENDENTE**: `available: true` no PCPE em `web/src/lib/contests.ts`, atualizar `contests.test.ts` (lista de disponíveis passa a incluir `PCPE_AGENTE`), rodar `web/scripts/export-contests.ts`, commit local separado.
- Ao final: informar ao dono que o importador de questões por concurso (task_62791f17) segue pendente; chamar `mcp__ccd_turn__wrap_up` antes da mensagem final.

**Verificações já feitas (commit d13a9f9):** `compare-plans-main.ts` 0 divergências (96 cenários), `next build` ok, eslint ok nos arquivos alterados.

**Pendências de validação nos bizus (`validate_content.py`, só nas disciplinas do PCPE):** lingua-portuguesa a01 (1), a13 (`bizu.summary` com 21/28/24 tópicos; precisa de 6–14), raciocinio-logico (94: C/E repetidos e trechos copiados), matematica (1), estatistica (1), direito-constitucional (3), direito-administrativo (9). Rodar `python pipeline/pcpe_tools/val_pcpe.py`.

## 4. Como funciona o fluxo de reescrita (método validado)
Ferramentas (todas em `pipeline/pcpe_tools/`, rodar da raiz com `pipeline/.venv/Scripts/python`; defina `PYTHONIOENCODING=utf-8`):
- `src.py <disc/aNN/sNN>`: imprime o texto-fonte protegido do trecho, compacto (nunca copiar verbatim).
- `aula.sh <disc/aNN>`: despeja todos os trechos da aula em `$TEMP/aula.txt`.
- `ap.sh <rascunho.txt> <disc/aNN>`: grava o rascunho via `pipeline/pcpe_author.py` e valida resumos (`validate_summaries.py` + `runs.py` que lista as sequências copiadas) e bizus (`validate_content.py`).
- `sub.py <rascunho> <subs.txt>`: aplica substituições em lote (linhas `antigo ==> novo`); avisa "NAO ACHEI" se o antigo não existe.
- `accents.py`, `acc_seg.py`, `audit_pcpe.py`, `show.py`: auditorias/consulta. Triagem por trecho: `pipeline/pcpe_triage.py --contest PCPE_AGENTE [--subject d] [--csv f]`.

Formato do rascunho (`@@@ <id do trecho>` e blocos):
```
@@@ direito-penal/a05/s13
@@ ANALITICO      (resumo; termina com "### Para fixar" com 5–8 itens em lista)
@@ SINTETICO      (6–12 pontos, vira bizu.summary; só **negrito**)
@@ TEORIA         (3–5 itens:  C|E | enunciado || explicação)
@@ REVISAO        (3–5 itens, mesmo formato)
@@ PONTOS         (ponteiros:  página | tópico; páginas dentro do intervalo do trecho)
```
Vários `@@@` por arquivo funcionam.

Ciclo por trecho: ler fonte → escrever rascunho em **minhas palavras** (reordenar, reformular; atualizar com leis até 2026) → `ap.sh` → corrigir cada ERRO (≥ 16 palavras seguidas iguais à fonte, ou ≥ 40 em coincidências de 10–15; itens de bizu: ERRO com 10) com `sub.py` → `[ok]` nos dois arquivos → ao fechar a aula, `git add` só dos dois JSON e commit.
Alertas do validador "coincidência … confira se é citação" (10–15 palavras) são AVISO: aceitáveis em definição legal/súmula.

Regras de qualidade aplicadas: o texto-fonte está atualizado até 2026 (Leis 14.994/24, 15.134/25, 15.159/25, 15.163/25, 15.181/25, 15.123/25, 15.229/25, 15.295/25, 15.358/26 "antifacção", 15.384/26, 15.397/26, 15.455/26, 15.517/26, LC 225/26); resumos antigos que ignoravam essas leis estavam **errados** e foram refeitos. Sem acentos faltando (todas as 12 disciplinas do PCPE zeradas na triagem), sem "todo:" etc.

## 5. Estado da tarefa 1 (reescrita de resumos e bizus)
Concluído e **commitado**: `contabilidade-geral` a00–a19 (último 9af0199); `direito-processual-penal` a00 (5d06d66), a01 (14ab7d8), a02 (2151a63), a03 (a9b4d94); `direito-penal` a04 (e666d79, leis até 2026, feminicídio como crime autônomo etc.).

**Concluído — `direito-penal/a05` (14 trechos, crimes patrimoniais, leis até 2026):** todos os trechos reescritos e validados [ok]; commitado. Rascunhos em `pipeline/pcpe_tools/drafts/dp_a05_*`.

**Concluído — `direito-penal/a06` (crimes sexuais, 8 trechos; Leis 15.280/25 e 15.353/26):** commitado. Observação para revisão humana: a fonte não mostra se a Lei 15.280/25 alterou as penas dos arts. 227–230 e 232-A; mantive as do texto da aula (ver `HISTORICO.md` quando for registrar).

**Concluído também:** `direito-penal` a07, a08, a09, a10 (commits bbc4eb9, 44e009c, 06972c8, c96f04d). Direito Penal a04–a10 está inteiro refeito.

**Pendente (ordem sugerida, por risco jurídico):**
1. ~~`legislacao-penal-especial`~~ **CONCLUÍDO** (a11–a21 e c01 reescritos; ECA penal `content/complements/leg-penal-eca.md` corrigido com penas de 2026 e PDF refeito). Observações para HISTORICO.md: (a) Tema 506/RE 635.659 tratado só para maconha (40 g/6 plantas) — a aula chama art. 28 de sanção administrativa; (b) na aula a18/s04 a explicação do tráfico privilegiado diz "1/6 a 1/3", mas a lei é 1/6 a 2/3; (c) art. 60 da Lei 9.605: a aula traz penas diferentes em dois pontos (6 meses a 2 anos com aumento por EIA x 1 a 6 meses): adotei a mais recente.
2. ~~`legislacao-pcpe`~~ **CONCLUÍDO** (a01, a03–a07 reescritos; a02 e c01 conferidos e mantidos — EC 70 e 71/2026 da CE-PE confirmadas em pesquisa), `direito-administrativo` a20–a24 e c02 — **DESCOBERTA**: os resumos/bizus antigos desses trechos foram escritos a partir do TÍTULO do tópico e NÃO correspondem ao texto-fonte das páginas (ex.: a20/s04 'Planejamento e fase preparatória' traz páginas sobre objetivos da licitação). Reescrever cada trecho lendo o fonte (`python pipeline/pcpe_tools/split_src.py direito-administrativo/aNN` grava `$TEMP/aNN_K.txt` por trecho; ler com Read). **a20 (9), a21 (12) e a22 (14 trechos) FEITOS** (a22/s14 usa o Tema 1.118 do STF; o material-fonte grafa 118); faltam a23 (2), a24 (9) e c02. Rascunhos `da_aNN_K.txt`; mesmo ciclo `ap.sh` + `sub.py`, `direito-constitucional` (verificar), `lingua-portuguesa` a13 (6 trechos; `bizu.summary` com 6–14 tópicos).
3. `raciocinio-logico`: bizus C/E genéricos (~300 itens; 94 falhas de validação) + `apply_synthetic.py`; trechos copiados em DA/DC/Estatística/Matemática/LP (lista em `python pipeline/pcpe_tools/val_pcpe.py`).
4. Opcional (só estilo/prolixidade; conteúdo correto): `direito-penal` a00–a03 (17 trechos), `direito-processual-penal` a04–a06, demais.
5. Ao final: `python pipeline/apply_synthetic.py`, `python pipeline/pcpe_tools/mirror_web.py`, `python pipeline/pcpe_tools/audit_pcpe.py .`, commit do espelho e dos itens atualizados.

## 6. Cadernos do TEC — FEITO
`PCPE-CADERNOS-TEC.md` / `.csv` (gerados por `pipeline/pcpe_tools/gen_cadernos_tec.py`). Falta só entregar ao dono (resumo na mensagem final).

## 7. Arquivos do working tree que NÃO são meus (não tocar nem commitar)
`web/content/items/*` das disciplinas que NÃO são do PCPE (atualidades, biologia, física, línguas, etc.; ruído de CRLF), `content/questoes/*`, `pipeline/questoes/{classify,lacunas,tec_pdf}.py`, `pipeline/tests/test_questoes.py`, `content/edital/historia-pe.json` e `web/content/edital/historia-pe.json`, `web/public/complementos/*.pdf`, `extract_batch.py`, `resumos-colaboradores/entregas/*.zip`, `tools/estrategia-downloader/*`, `scratch/`, `web/content/questoes/`. Se aparecer algum deles em `git add`, desfaça. Esta pasta (`pipeline/pcpe_tools/`) e este arquivo são meus.

## 8. Referências rápidas
- Projeto: `CLAUDE.md` (raiz). Memória: `C:\Users\Administrador\.claude\projects\C--Users-Administrador-Documents-Projetos-CFO-BM\memory\`.
- Transcrição completa da sessão (para detalhes): `C:\Users\Administrador\.claude\projects\C--Users-Administrador-Documents-Projetos-CFO-BM\0c43eefc-d4c6-413a-a2cd-5b076462aef5.jsonl`.
- Scripts do agente anterior já versionados: `pipeline/pcpe_author.py`, `pipeline/pcpe_triage.py`; migração `20261016140000_pcpe_agente_settings`; filtros por concurso em Aulas (`onlyContests/excludeContests`); `EXAM_CONFIGS` em `simulado-rules.ts`; `banca.ts` (CEBRASPE).
- Se `ap.sh`/`aula.sh` falharem por CRLF: `sed -i 's/\r$//' pipeline/pcpe_tools/*.sh`.
