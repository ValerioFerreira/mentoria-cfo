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
1. **Refazer resumos e bizus fracos — EM ANDAMENTO** (seção 5).
2. Espelhar conteúdo em `web/content/` (items, summaries, overrides, complements com `onlyContests`, structure, segments) sem tocar nos arquivos de outras frentes; rodar `apply_synthetic.py`; conferir que os 657 trechos do PCPE têm bizu + resumo em `web/content`.
3. Edital PCPE por concurso: coluna/filtro por concurso em `EditalItem` (migração), semear `content/edital/pcpe/*.json`, ajustar onboarding/páginas de questões/persistência.
4. Limpezas e lacunas: títulos com "Prof." (biologia a16/a17, direito-constitucional a18), `category:""` do cartão PCPE, lacunas (conjuntos, matrizes, tamanho amostral), `docs/inventario_pcpe.json`, `HISTORICO.md`.
5. Rodar testes, build e seed: `pipeline/test_plan_pcpe.ts` (24 cenários), `compare-plans-main.ts` (zero regressão), vitest, pytest, tsc, `npm run build`, seed local (prisma dev).
6. Lista de cadernos do TEC a montar (planilha/relatório; ver seção 6).
7. Commit de liberação (`available: true` + `export-contests.ts`), local.
- Ao final: informar ao dono que o importador de questões por concurso (task_62791f17) segue pendente; chamar `mcp__ccd_turn__wrap_up` antes da mensagem final.

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

**Pendente (ordem sugerida):**
1. `direito-penal` a07–a10 (conferir se atualizações de 2024–26 entraram), a00–a03 (verificar).
2. Opcional/qualidade: `direito-processual-penal` a04–a06 (corretos mas prolixos/acentuados em excesso).
3. `legislacao-penal-especial` (29 trechos): corrigir Tema 506/RE 635.659 (porte de drogas para uso pessoal) e atualizações de leis.
4. `direito-administrativo` a20–a24/c02; `legislacao-pcpe` (12 trechos); `lingua-portuguesa` a13 (6 trechos; `bizu.summary` deve ter 6–14 tópicos).
5. `raciocinio-logico`: bizus C/E genéricos (~300 itens) a refazer + `apply_synthetic.py`.
6. Trechos com texto copiado em DA/DC/Estatística/Matemática/LP usados pelo plano do Agente (rodar `pcpe_triage.py` e `validate_summaries.py` para listar).

## 6. Cadernos do TEC (tarefa 6) — a entregar
Lista das matérias/assuntos do PCPE Agente (Cebraspe) com quantidade sugerida de questões por caderno, agrupada por disciplina do edital PCPE (ver `content/edital/pcpe/*.json` e `content/contests.json`). Ainda **não** produzida. Formato desejado: planilha/relatório com disciplina, assunto do edital, banca (CEBRASPE), filtros (ano/área) e nº de questões. Base para a especificação: `pipeline/questoes/EXTRACAO.md`, `content/questoes/mapa-assuntos.json`.

## 7. Arquivos do working tree que NÃO são meus (não tocar nem commitar)
`web/content/items/*` (ruído de CRLF), `content/questoes/*`, `pipeline/questoes/{classify,lacunas,tec_pdf}.py`, `pipeline/tests/test_questoes.py`, `content/edital/historia-pe.json` e `web/content/edital/historia-pe.json`, `web/content/overrides/*.json`, `web/public/complementos/*.pdf`, `extract_batch.py`, `resumos-colaboradores/entregas/*.zip`, `tools/estrategia-downloader/*`, `scratch/`, `web/content/questoes/`. Se aparecer algum deles em `git add`, desfaça. Esta pasta (`pipeline/pcpe_tools/`) e este arquivo são meus.

## 8. Referências rápidas
- Projeto: `CLAUDE.md` (raiz). Memória: `C:\Users\Administrador\.claude\projects\C--Users-Administrador-Documents-Projetos-CFO-BM\memory\`.
- Transcrição completa da sessão (para detalhes): `C:\Users\Administrador\.claude\projects\C--Users-Administrador-Documents-Projetos-CFO-BM\0c43eefc-d4c6-413a-a2cd-5b076462aef5.jsonl`.
- Scripts do agente anterior já versionados: `pipeline/pcpe_author.py`, `pipeline/pcpe_triage.py`; migração `20261016140000_pcpe_agente_settings`; filtros por concurso em Aulas (`onlyContests/excludeContests`); `EXAM_CONFIGS` em `simulado-rules.ts`; `banca.ts` (CEBRASPE).
- Se `ap.sh`/`aula.sh` falharem por CRLF: `sed -i 's/\r$//' pipeline/pcpe_tools/*.sh`.
