# Continuação: material próprio do CFOA até o sistema local (passagem de 03/11/2026)

Briefing para o agente que continua o trabalho. Leia antes o `CLAUDE.md` (linha "Material próprio") e o `HISTORICO.md` §15. Plano aprovado pelo dono: `C:\Users\Administrador\.claude\plans\perguntei-ao-agente-o-piped-adleman.md`.

## 0. Regras (não negociáveis)

- **Nunca** abra, imprima nem edite `.env*`.
- Não grave no Neon (produção) nem rode nada com `--remoto` que escreva. A leitura remota (`directive-audit.ts --remoto`) só com OK do dono.
- Sem commit, salvo pedido do dono.
- Não leia `*.ref.json`.
- Windows: `PYTHONIOENCODING=utf-8`; nada de heredoc com regex ou `\n` no Bash (ele corrompe). Use a ferramenta Write/Edit.
- Os créditos do dono são escassos e já estouraram o limite três vezes com muitos agentes em paralelo. Use **no máximo 3 subagentes simultâneos** e os pacotes compactos (abaixo).

## 1. O que já está pronto

1. **Motor de PDF** (`pipeline/build_material.py`, `pipeline/material_pdf/`, `design/material/prontidao/`):
   - modelo A · Prontidão, aprovado pelo dono, com logo novo, mascote (FOCO nas páginas claras, CHAMA nas escuras) e site no rodapé;
   - comentário logo abaixo de cada questão;
   - sem menção a concurso;
   - quebras conferidas: pré-passo `prepass()` no template e conferências no `postprocess.py`;
   - página final com "Material atualizado em: dd/mm/aaaa" (`content/material/atualizacao/datas.json`).
2. **Neutralidade de concurso:**
   - concluída em todas as ondas e nos complementos: `pipeline/contest_mentions.py` mostra 0 direcionamento e 0 banca;
   - o validador (`DIRECIONA`, `BANCA`, `neutrality()`) dá ERRO para direcionamento e banca e AVISO para instituição;
   - briefing em `pipeline/briefs/neutralidade.md`.
3. **Atualização contínua:**
   - `pipeline/material_update_index.py` gera `content/material/atualizacao/{indice.json, INDICE.md, datas.json}`;
   - `pipeline/material_watch.py` aponta os artigos que mudaram e grava `relatorio-AAAA-MM.md`;
   - briefing do agente mensal em `pipeline/briefs/atualizacao.md`.
4. **Fixação pela média do material-base:**
   - `pipeline/material_fixacao_meta.py` gera `content/material/metrics/_fixacao.json`; o validador usa `fixacao_range()`;
   - `pipeline/material_fixacao_select.py` faz a seleção, já aplicada a todas as disciplinas da onda 1;
   - `pipeline/fixacao_pacotes.py` faz os pacotes e o aplicador.
5. **Diretrizes nos dois materiais (web):**
   - `web/src/lib/directive.ts` (funções `teoriaMentoria`, `turboMentoriaStep`, `revisaoMentoria`, `fixacaoMentoria`, `materialHref`);
   - `web/src/lib/material.ts` lê `web/content/material/index.json`; a preferência fica no cookie `material`;
   - `web/src/components/material-tabs.tsx`;
   - `web/src/app/(app)/atividade/[id]/page.tsx` com as abas "Material MentorIA" / "Material-base". A Fixação do material-base agora usa as páginas do catálogo atual: as gravadas no plano envelheciam;
   - rota `web/src/app/material/[disc]/[vol]/route.ts`, que lê `../material-pdf`, sem carimbo, só para usuário logado com acesso;
   - testes em `directive.test.ts` (11 passando); typecheck e lint limpos.
6. **Verificação amostral:**
   - `web/scripts/directive-audit.ts` (só leitura) e `pipeline/directive_check.py`;
   - rodada local no material-base: N=1921, n=321, 3,1% acusado. Na leitura manual, nenhuma página errada: são diferenças de redação do índice, rótulos descritivos e 3 trechos que começam na capa;
   - relatório em `pipeline/.cache/directive-audit/amostra-local.relatorio.md`.
7. **Banco local:** de pé (`npx prisma dev -n cfo-bm -d`), com 2.711 questões novas do TEC importadas (só local).

## 2. O que falta, nesta ordem

### Passo 1 — Terminar os comentários da Fixação (406 pendentes)

1. **Aplique primeiro as respostas já escritas e não aplicadas:**
   ```
   pipeline/.venv/Scripts/python pipeline/fixacao_pacotes.py aplicar pipeline/.cache/material/pacotes/raciocinio-logico__m02.resp.json
   pipeline/.venv/Scripts/python pipeline/fixacao_pacotes.py aplicar pipeline/.cache/material/pacotes/raciocinio-logico__m05.resp.json
   ```
   Se o aplicador listar ERRO nas questões, corrija o `.resp.json` e aplique de novo. Acrescente o bloco "Fixação ampliada" no `REVISAO.md` dos dois volumes.
2. **Remonte os pacotes do que ainda falta:** `pipeline/.venv/Scripts/python pipeline/fixacao_pacotes.py montar` (só gera pacote de volume com questão sem comentário).
3. **Lotes restantes**, no máximo 3 subagentes por vez, com o prompt do §4:
   - RL m04, m06;
   - DC m02, m03;
   - DC m04, m07;
   - DC m11, m12, m17 + DPPM m01, m03 + DH m01;
   - DH m02, m03.

   Volumes de RL m05 com 1 questão pendente entram no lote de RL.
4. **Conferência por amostra (você):**
   - leia 3 comentários por volume contra o gabarito;
   - rode `pipeline/check_citations.py content/material/<disc>/<mNN>/fixacao.json`. "Inexistente" com "(norma mais citada)" costuma ser citação da CF sem sigla: confira o contexto.

### Passo 2 — Repor as questões descartadas

1. Os descartes por qualidade ficam em `fixacao.json` → `descartes` (motivo "QUALIDADE: …"; o seletor também reconhece "gabarito", "desatualiz", "revogad", "sem texto", "norma interna").
2. Rode:
   - `pipeline/.venv/Scripts/python pipeline/material_fixacao_select.py --onda 1` (simulação) e depois `--aplicar`. Ele mantém as comentadas e completa a meta com as próximas candidatas do cache;
   - `fixacao_pacotes.py montar` e uma rodada curta de comentários;
   - repita até o validador não acusar "N questões (use X a Y)".
3. Se o cache de candidatas acabar num capítulo, exporte mais (só leitura): `cd web && npx tsx scripts/material-questoes.ts --volume <id> --max-por-capitulo 60`.
4. **Licitações** (DA m15, m16, m18): muitas questões do banco são da Lei 8.666/1993, revogada. Prefira as posteriores a 2021 e as que citam a Lei 14.133/2021.

### Passo 3 — Validar a onda 1

- `pipeline/.venv/Scripts/python pipeline/validate_material.py --all --wave 1`: 0 erros.
- `pipeline/.venv/Scripts/python pipeline/contest_mentions.py`: 0 direcionamento e 0 banca.
- `pipeline/.venv/Scripts/python pipeline/material_update_index.py`: atualiza o índice e o `datas.json`; as datas novas vêm das seções do `REVISAO.md`.
- `pipeline/.venv/Scripts/python -m pytest pipeline/tests -q`: os testes do motor e de atualização passam. Quatro testes antigos já falhavam: Estatística, Atualidades e um complemento de DC.

### Passo 4 — Gerar os 71 PDFs do CFOA

- Diagramas com letra abaixo de 6 pt aparecem como AVISO. Os conhecidos: DPM m01 fig. 1.1 e 2.1, ADM m04 fig. 2.2 e 2.3. Corrija o mermaid no `.md` (dividir ou reorganizar) e registre no `REVISAO.md`.
- `pipeline/.venv/Scripts/python pipeline/build_material.py --onda 1`, depois `--onda 1 --conferir`. Esperado: 71 OK.
  - O comando grava `content/material/index.json` e o espelho `web/content/material/index.json`, de que o app depende.
  - **Não** use `--carimbo-exemplo` na geração final.

### Passo 5 — Verificação amostral das diretrizes (95%)

- `cd web && npx tsx scripts/directive-audit.ts`, depois `pipeline/.venv/Scripts/python pipeline/directive_check.py pipeline/.cache/directive-audit/amostra-local.json`. Agora com o material MentorIA no índice, os estratos "·mentoria" entram.
- Com o OK do dono, repita com `--remoto` (só leitura) para a população dos planos reais.
- Leia 30 diretrizes sorteadas e classifique os erros acusados: real ou limitação do conferidor.
- Erro real se corrige no código e a amostra roda de novo.

### Passo 6 — Sistema local

- O banco local já está de pé. Se não estiver: `cd web && npx prisma dev -n cfo-bm -d`.
- Suba pelo preview do app: `.claude/launch.json` (nome `web`, porta 3000).
- Abra uma atividade de Teoria, uma de Revisão e uma de Fixação de um plano local:
  - confira as duas abas;
  - confira o botão "Abrir o PDF" na página certa (`/material/<disc>/<mNN>#page=X`);
  - tire prints.
- Mostre ao dono.

### Passo 7 — Documentar

Atualize o `HISTORICO.md` §15 e a linha "Material próprio" do `CLAUDE.md` com os números finais, e a memória `material-proprio-estado.md`.

## 3. Achados que vão para o dono (decisões pendentes)

- **Banco com questões desatualizadas** que continuam APROVADAS e podem cair nos cadernos dos alunos:
  - licitações pela Lei 8.666/1993 e Lei 10.520/2002;
  - aposentadoria compulsória aos 70 anos e regras anteriores à EC 103/2019;
  - prescrição intercorrente "pela metade" (ADIs 7156/7236);
  - art. 12, § 1º da LIA (ADI 7236);
  - Portaria MPOG 450/2002;
  - Lei 12.990/2014 (revogada pela Lei 15.142/2025);
  - redação antiga do art. 89 da Lei PE 6.783.

  Os ids estão nos `descartes` dos `fixacao.json` da onda 1. Proposta: marcá-las como `RETIRED` no banco (local e, com autorização, no Neon).
- Duas questões de LegPE m04 (`…241_1ff9a4`, `…243_d1cc61`) baseadas em parágrafo inexistente da LC 470/2021.
- **Preferência de material:** hoje fica em cookie. Passar a um campo no perfil (`User.materialPreference`) exige migração.
- Carimbo com nome e CPF, Termos e Privacidade, Cloudflare R2.
- Pendências de `pipeline/briefs/cfoa-conclusao.md`: revisão das inéditas de DPM e liberação dos planos do CFOA.
- **Pedido futuro**: "Reportar erro no PDF" com a página "Erros reportados" na Administração.

## 4. Prompt dos subagentes de comentários

Um por lote; troque a linha final pelo lote.

```
Repositório C:\Users\Administrador\Documents\Projetos\CFO-BM (Windows; Bash POSIX; PYTHONIOENCODING=utf-8). Tarefa: escrever comentários de questões da Fixação do material MentorIA. Trabalhe de forma enxuta: NÃO leia o CLAUDE.md, os caches de questões nem os capítulos inteiros; tudo o que precisa está nos pacotes.

Para cada volume do seu lote:
1. Leia o pacote `pipeline/.cache/material/pacotes/<disc>__<mNN>.md` (questões sem comentário, com gabarito oficial e o "Para fixar" do capítulo).
2. Escreva com a ferramenta Write o arquivo `pipeline/.cache/material/pacotes/<disc>__<mNN>.resp.json`:
   {"volume": "<disc>/<mNN>", "comentarios": {"<id>": {"comentario": "...", "alternativas": {"A": "Errada: ...", "B": "Correta: ...", ...}}}, "descartes": []}
   - comentario: 50 a 250 palavras, partindo do enunciado da própria questão: a regra que resolve e por que o gabarito oficial está certo. Cada comentário é único.
   - alternativas: TODAS as letras, cada uma com 6 a 70 palavras, começando por "Correta:" ou "Errada:" e dizendo o porquê. Em Certo/Errado, "alternativas": {}.
   - Português claro, frases curtas. Proibido: "professor" (use "docente"), "Estratégia" (inclusive "Estratégias"), nome de banca, nome de concurso ou órgão como destino, "gabarito oficial diz", LaTeX (use Unicode).
   - Artigo de lei: confira com `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <n>`. Contas: refaça e mostre o caminho.
   - Gabarito errado ou questão desatualizada: não comente; ponha em "descartes": [{"id": "...", "motivo": "QUALIDADE: <uma frase com o dispositivo>"}].
3. Rode `pipeline/.venv/Scripts/python pipeline/fixacao_pacotes.py aplicar <arquivo .resp.json>` e corrija até não haver ERRO nas suas questões (erro só de quantidade é esperado).
4. Acrescente ao fim de `content/material/<disc>/<mNN>/REVISAO.md`:
   # Fixação ampliada — AAAA-MM-DD
   Decisão: APROVADO (Fixação ampliada pela média do material-base)
   Comentários novos: N · Descartadas por qualidade: M
Nunca abra .env* nem *.ref.json; não grave em banco; sem commit; só mexa nos volumes do seu lote. Responda em no máximo 8 linhas.

SEU LOTE: <volumes>
```
