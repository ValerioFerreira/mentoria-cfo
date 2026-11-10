# Motor de PDF do material próprio MentorIA — modelo A · Prontidão

Briefing para o agente que constrói o gerador de PDFs (Etapa 2 do plano `C:\Users\Administrador\.claude\plans\vamos-agora-para-uma-inherited-barto.md`). Escrito pelo revisor em 01/11/2026. O dono escolheu o **modelo A · Prontidão**.

## 0. O que entregar

1. Um gerador, `pipeline/build_material.py`, que transforma cada volume aprovado de `content/material/<disc>/mNN/` num PDF A4 no modelo Prontidão:
   - `material-pdf/<disc>/mNN.pdf` (pasta na raiz, fora do git);
   - `content/material/index.json` (versionado), com as páginas de cada capítulo.
2. **Fase 1: três volumes de amostra, e PARE** para o dono aprovar.
3. **Fase 2, só depois da aprovação:** os 71 volumes do CFOA e um relatório de conferência.

Não faz parte deste trabalho:
- carimbo com nome e CPF do aluno, rota de download e banco de dados (Etapa 5);
- hospedagem;
- conteúdo.

O PDF sai **sem** carimbo, com a faixa do rodapé reservada e vazia.

## 1. A referência visual (arquivo correto)

- **`design/material/modelos.html`**, seção `#modelo-a`. É o mesmo conteúdo da galeria publicada que o dono aprovou (https://claude.ai/artifact/UNqo1qVABUteX592t7vsCh); só muda o invólucro.
  - Abra no navegador e amplie cada página do modelo A.
  - O CSS do modelo A são as regras `.m-a …` e `.cvA …`, mais as regras comuns: `.pg`, `.hd`, `.ft`, `.stamp`, `.tb`, `.co`, `.toc`, `.chip`, `.stats`, `.steps`, `.q`, `.alts`, `.com`, `.fix`, `.op-*`, `.bm`, `.wm` e `.brand`.
  - A marca (chama + estrela) está nas constantes `FLAME`, `STAR` e `brand()` do mesmo arquivo.
  - A galeria desenha em `cqw` para caber na tela. No PDF, converta para unidades de impressão: 1em da galeria ≈ 3,9 mm; corpo ≈ 10,5–11 pt Public Sans, entrelinha 1,42.
- **Tokens** (iguais aos do app em `web/src/app/globals.css`):
  - ink `#0e1b2e`; texto `#1b2433`; cinza `#5b6778`; linha `#d5dce6`; superfície `#f3f5f8`;
  - vermelho `#d4301f` (fundo claro `#fdece9`); dourado `#e9a90c` (texto `#8a5a00`, fundo `#fff4d1`);
  - teoria `#2563eb` / `#eaf1fe`; revisão `#7c3aed` / `#f2ecfe`; fixação `#d9640f` / `#fdf0e3`; questões `#059669` / `#e6f6f0`.
- **Fontes:**
  - Barlow Condensed 500/600/700/800 (títulos);
  - Public Sans 400/600/700 com itálico (texto);
  - IBM Plex Mono 400 (código, se houver).
  - Todas são OFL. Baixe os TTF oficiais (repositório google/fonts ou Google Fonts) para `design/material/prontidao/fonts/`, com o `OFL.txt` de cada família, e use `@font-face` local.
  - O PDF não pode depender de internet e precisa ter as fontes embutidas.
- **Sem brasões oficiais** (CBMPE, PMPE, PCPE) em lugar nenhum.

### Peças do modelo A, página a página

1. **Capa** (`.cvA`):
   - fundo ink, marca MentorIA no alto;
   - disciplina em caixa alta vermelho-claro (`#ff8a78`);
   - "VOLUME NN" em dourado;
   - título do volume em Barlow 800 caixa alta;
   - subtítulo;
   - faixa refletiva diagonal (`.tape`);
   - três números: capítulos, páginas, concursos que cobram;
   - selo "Material exclusivo MentorIA";
   - lista dos concursos.
2. **Créditos e sumário**:
   - sumário com número do capítulo em vermelho, título, linha de apoio e chip "Teoria", e número da página (contado automaticamente);
   - linhas extras: Apresentação, Questões comentadas (chip Fixação), Comentários e gabarito, Mapa de revisão (chip Revisão);
   - no pé, o aviso legal (`.legal`) do modelo, com o texto exato da galeria (Lei 9.610/1998, uso individual, "Cada cópia carrega identificação do titular e do download").
3. **Apresentação** (h2 "00 Apresentação do volume"):
   - o texto de `volume.md`;
   - três `.stat`: capítulos, páginas de teoria, concursos;
   - o bloco fixo "Como estudar este volume", com os 4 `.step` (Teoria, Revisão, Fixação, Questões) e o texto da galeria adaptado a "volume";
   - "O que você vai aprender": a lista de `volume.md`, que pode virar a tabela "Mapa do volume" (capítulo × o que domina).
4. **Abertura de cada capítulo**, sempre em página nova:
   - faixa ink `.op-band` com o número grande vazado em vermelho (`.op-num`);
   - "CAPÍTULO N"; título do capítulo; chip/linha "Atividade de Teoria";
   - faixa refletiva no pé da banda.
   - Abaixo:
     - o parágrafo de abertura do capítulo;
     - o quadro `[!objetivos]` como "Ao final do capítulo, você vai saber";
     - "Neste capítulo": as seções `##` com número N.1, N.2… e a página de cada uma.
   - Não mostre minutos (o tempo da atividade varia por aluno).
5. **Corpo**:
   - cabeçalho `.hd`: à esquerda, barra vermelha + "DISCIPLINA · VOLUME NN"; à direita, o título do capítulo corrente;
   - `h2` em Barlow caixa alta com filete vermelho embaixo e número N.M em vermelho;
   - `h3` sem número;
   - tabelas `.tb`;
   - quadros com barra lateral colorida.
6. **Mapa do capítulo**: é a última seção de cada capítulo. Destaque leve em roxo (Revisão); o "Para fixar" em lista com marcador roxo.
7. **Questões comentadas** (Fixação), no fim do volume. Por decisão de didática, em duas partes:
   - **Questões**: todas as questões, agrupadas por capítulo, só com enunciado, texto-base e alternativas (bolhas A–E de `.alts`), para o aluno resolver antes;
   - **Comentários e gabarito**: para cada questão, "Questão N · Gabarito X", o comentário e o comentário de cada alternativa, em `.com`.
   - O cabeçalho de cada questão (`.q-h`) traz o número, a origem e o tipo. Origem: "AOCP 2024 · CBMPE" (banca, ano e órgão do arquivo de questões) ou "Inédita MentorIA". Tipo: "Múltipla escolha" ou "Certo ou errado".
   - Se o dono preferir o comentário logo após cada questão, como na galeria, isso é uma opção de configuração.
8. **Mapa de revisão do volume**: um bloco por capítulo, com o título e o seu "Para fixar". É gerado do conteúdo, sem texto novo.
9. **Rodapé** de todas as páginas, menos a capa:
   - à esquerda, "MentorIA · <Disciplina> · Volume NN";
   - no centro, a **faixa do titular**, reservada e vazia: retângulo de ~95 mm × 6 mm, centralizado, sem nenhum desenho ou texto do motor;
   - à direita, "p / total";
   - acima, a régua refletiva fina (`.m-a .ft::before`).
   - Com `--carimbo-exemplo`, o motor escreve na faixa "LICENCIADO PARA **FULANO DE TAL DA SILVA** · CPF 123.456.789-09" (CPF de teste), só para as provas visuais.

### 1.1 Mascote (decisão do dono, 01/11/2026)

Os quadros de ressalva e as seções-chave levam o mascote MentorIA numa expressão própria, como o material-base faz com o mascote dele. As imagens são desenhadas pelo dono. O motor tem de funcionar já, com um **marcador provisório**: a chama da marca dentro de um círculo da cor do quadro.

Arquivos: `design/material/prontidao/mascote/<slug>.png`.
- PNG com fundo transparente, ou SVG;
- quadrado, de 1000 × 1000 px ou mais;
- corpo inteiro, centralizado, mesma escala e mesma linha de base em todas as poses;
- **sem texto dentro da imagem** (o rótulo é impresso pelo PDF);
- versão `<slug>-escuro.png` opcional, para fundo ink: o motor a usa na faixa de abertura quando existir; sem ela, aplica um contorno claro.

Se o arquivo existir, o motor usa a imagem; se não, o marcador. Trocar as imagens não exige mudar código.

**12 reações:**

| # | slug | Onde aparece | Rótulo impresso | Expressão e objeto sugeridos | Ocorrências no CFOA |
|---|---|---|---|---|---|
| 1 | `atencao` | quadro `[!atencao]` | FIQUE ATENTO! | sério, sobrancelhas franzidas; placa de alerta (!) ou dedo em riste | 472 |
| 2 | `pegadinha` | quadro `[!pegadinha]` | PEGADINHA DA BANCA | desconfiado, olhar de lado; lupa ou casca de banana | 559 |
| 3 | `bizu` | quadro `[!bizu]` | BIZU! | piscando, sorriso confiante; lâmpada acesa | 384 |
| 4 | `exemplo` | quadro `[!exemplo]` | EXEMPLIFICANDO | didático, apontando; quadro ou prancheta | 380 |
| 5 | `jurisprudencia` | quadro `[!jurisprudencia]` | JURISPRUDÊNCIA | sério e solene; beca e martelo (sem brasões) | 113 |
| 6 | `resolvido` | quadro `[!resolvido]` | PASSO A PASSO | concentrado; lápis ou calculadora | 202 |
| 7 | `missao` | faixa de abertura de cada capítulo (fundo ink) | MISSÃO DO CAPÍTULO | determinado, postura de prontidão; mapa ou prancheta | 341 capítulos |
| 8 | `cai-na-prova` | selo na abertura dos capítulos de importância ALTA | CAI MUITO NA PROVA | empolgado e alarmado; alvo acertado ou sirene | 101 capítulos |
| 9 | `praticar` | abertura de "Questões comentadas" | HORA DE PRATICAR! | esforço; halteres ou cronômetro | 71 volumes |
| 10 | `gabarito` | abertura de "Comentários e gabarito" | GABARITO COMENTADO | satisfeito; prancheta com ✓ | 71 volumes |
| 11 | `revisao` | "Mapa do capítulo" e "Mapa de revisão do volume" | HORA DA REVISÃO | tranquilo; cartões de revisão ou checklist | 341 + 71 |
| 12 | `missao-cumprida` | página final do volume (encerramento, "próximo passo no seu plano") | MISSÃO CUMPRIDA! | comemorando, braços erguidos | 71 volumes |

Regras de uso:
- `[!lei]`, `[!esquema]` e `[!objetivos]` **não** levam mascote: são blocos de conteúdo, não ressalvas.
- Nos quadros, o mascote fica à esquerda do rótulo, com cerca de 20 mm de altura, e o texto do quadro corre ao lado e abaixo. Ele nunca cobre texto e nunca empurra o quadro para outra página sozinho.
- Quando dois quadros do mesmo tipo vierem seguidos na mesma seção, só o primeiro leva o mascote.
- Nas seções (7 a 12), o mascote fica maior, com 35 a 45 mm.
- O selo `cai-na-prova` usa a importância do trecho no concurso do volume (nota ≥ 67, a mesma régua do validador). Em volume de vários concursos, vale a maior nota.
- A página final (12) é nova: marca, "Missão cumprida!", o resumo do volume (capítulos, questões) e o próximo passo no plano (Revisão → Fixação → Questões no app), sem texto autoral novo além desse modelo fixo.

Ressalvas do material-base que ficaram de fora de propósito:
- "Não confunda", "Indo mais fundo", "Esta é difícil" e "Curiosidade" dependem de marcação que os autores não fazem hoje. A pegadinha e a atenção cobrem as duas primeiras.
- "Esta cai na prova" e "Despenca na prova" viram o selo automático 8, calculado pela importância, sem depender do autor.

**Nomenclatura:** use **"Volume NN"** (o `number` do volume em `content/material/volumes/<disc>.json`), nunca "Aula NN". "Aula" no app é a aula do catálogo do material-base, e a interface não pode citar o material-base.

## 2. Os dados de entrada (formatos reais)

- **Volumes:** `content/material/volumes/<disc>.json` → `volumes[]` com `id`, `number`, `title`, `wave`, `contests` (chaves) e `trechos` (a ordem dos capítulos). Os rótulos dos concursos estão em `web/src/lib/contests.ts`; use `role` + `org`, por exemplo "2º Tenente CFOA · CBMPE".
- **Apresentação:** `content/material/<disc>/mNN/volume.md`. Front matter JSON por linha (`volume`, `titulo`, `subtitulo`, `status`…) e seções `## Apresentação`, `## O que você vai aprender` e `## Pré-requisitos` (opcional).
- **Capítulos:** `content/material/<disc>/mNN/aNN-sNN.md` (ou `cNN-sNN.md`). Front matter: `id`, `volume`, `capitulo` (número), `titulo`, `fingerprint`, `status`, `edital`, `fontes`, `notas`. Regras completas em `pipeline/briefs/material.md`, seção 5. Elementos a renderizar:
  - parágrafo de abertura, `> [!objetivos]`, seções `##` e `###`, e o fecho `## Mapa do capítulo` com `### Para fixar`;
  - quadros `> [!tipo] Título opcional` com linhas `> `. Rótulos no PDF:

    | Tipo | Rótulo | Cor |
    |---|---|---|
    | `atencao` | ATENÇÃO | vermelho |
    | `bizu` | BIZU | dourado |
    | `exemplo` | EXEMPLO | azul |
    | `lei` | LETRA DA LEI · <título> | ink; texto em itálico |
    | `jurisprudencia` | JURISPRUDÊNCIA · <título> | ink, barra dourada |
    | `pegadinha` | PEGADINHA DA BANCA | laranja |
    | `esquema` | ESQUEMA | roxo |
    | `resolvido` | EXERCÍCIO RESOLVIDO | verde |

    O título opcional vem depois do rótulo.
  - tabelas markdown;
  - negrito e itálico;
  - listas `- ` e `1. `;
  - fórmulas em Unicode (sem LaTeX);
  - blocos de figura com a legenda na linha de abertura:
    - ```` ```mermaid Legenda ````;
    - ```` ```svg Legenda ````;
    - ```` ```grafico Legenda ```` (JSON; tipos `funcao`, `linhas`, `dispersao`, `barras`, `setores`, `histograma`; especificação na seção 5.5 do briefing de autores e em `check_grafico` de `pipeline/validate_material.py`);
    - ```` ```molecula Legenda ```` (SMILES).
  - Toda figura leva "Figura N.M — legenda" embaixo.
  - O CFOA só usa `mermaid` (cerca de 310 capítulos têm). `grafico` e `svg` aparecem na onda 2 (estatistica/m02 e m04, fisica/m02, m03 e m05) e precisam funcionar também. Ninguém usou `molecula` ainda: implemente com RDKit, ou deixe um erro claro "molecula ainda não suportada" se a instalação falhar.
- **Reaproveite as funções de leitura** de `pipeline/validate_material.py` (`parse_front_matter`, `callouts`, `fences`, `tables`), para o motor ler o markdown do mesmo jeito que o validador. Não altere esse arquivo.
- **Fixação:** `content/material/<disc>/mNN/fixacao.json`:
  - `questoes[]` com `id`, `capitulo`, `gabarito`, `comentario` e `alternativas` (dicionário letra → comentário; ausente nas de Certo/Errado);
  - `ineditas[]`, que trazem o próprio `enunciado` e `alternativas_texto`.
  - O enunciado, o texto-base e as alternativas das questões do banco estão em `pipeline/.cache/material/questoes/<disc>__mNN.json` → `questoes[]` (`id`, `tipo`, `banca`, `ano`, `orgao`, `cargo`, `textoBase`, `enunciado`, `alternativas[{letra, texto}]`, `gabarito`, `temFigura`).
  - Nunca abra `*.ref.json`.
  - Os enunciados têm marcação: `**negrito**`, `<u>sublinhado</u>` e `![Figura](/q-img/<sha256>)`.
  - Se uma questão escolhida não estiver no arquivo de cache, pare e registre (não invente o enunciado). Se o cache faltar, a exportação é só leitura: `cd web && npx tsx scripts/material-questoes.ts --volume <disc>/mNN`.
- **Figuras das questões:** 17 das 2.001 questões escolhidas até agora têm imagem. O binário está no banco local, tabela `QuestionImage` (`id` = sha256, `mime`, `data`, `width`, `height`).
  - Crie `web/scripts/material-qimg.ts`, **somente leitura**, que exporte essas imagens para `pipeline/.cache/material/q-img/<sha>.<ext>`, a partir dos `fixacao.json` e do cache de questões.
  - Banco local: o Postgres do `npx prisma dev` (`web/.env`). Nunca use `--remoto` nem `web/.env.remote`, e nunca escreva no banco. Se o banco local não estiver de pé, suba-o como diz o CLAUDE.md.

## 3. Arquitetura recomendada (é como o revisor faria)

```
pipeline/build_material.py            # CLI
pipeline/material_pdf/
  __init__.py
  load.py        # lê volume.md, capítulos, fixacao.json, cache de questões, volumes/<disc>.json, contests
  render_md.py   # markdown do capítulo -> HTML (quadros, tabelas, figuras), reaproveitando o parser do validador
  figures.py     # grafico (matplotlib -> SVG), molecula (RDKit -> SVG), svg (sanitizado), mermaid (marcado para o navegador)
  assemble.py    # monta o HTML do volume com Jinja2 (capa, sumário, apresentação, capítulos, fixação, mapa)
  printpdf.py    # Playwright/Chromium: carrega o HTML, roda mermaid e Paged.js, imprime o PDF
  postprocess.py # PyMuPDF: outline (marcadores), metadados, páginas de cada capítulo, conferências
design/material/prontidao/
  template.html.j2  prontidao.css  fonts/  vendor/ (pagedjs, mermaid; com as licenças)
pipeline/tests/test_build_material.py
```

- **Por que Chromium + Paged.js, e não PyMuPDF Story** (o que `build_complements.py` usa): a identidade precisa de CSS completo (`@page` com margens nomeadas, `string-set` para o título corrente, `target-counter` para o sumário, faixas com gradiente e grids). Paged.js dá isso em cima do Chromium.
- **Dependências:**
  - instale no `pipeline/.venv` e acrescente a `pipeline/requirements.txt`: `jinja2`, `playwright`, `matplotlib`, `rdkit` (opcional) e o que mais precisar;
  - rode `python -m playwright install chromium`;
  - Paged.js (`pagedjs`, polyfill) e Mermaid (`mermaid`, versão 10 ou 11) vêm do npm, numa versão fixa, copiados para `design/material/prontidao/vendor/`, com a licença MIT de cada um. Nada de CDN na hora de gerar.
- **Mermaid:**
  - renderize no próprio Chromium, antes do Paged.js paginar: `mermaid.run()`, depois `PagedPolyfill.preview()`;
  - tema com as cores do modelo (`themeVariables`: `primaryColor #eaf1fe`, `primaryBorderColor #0e1b2e`, `lineColor #5b6778`, fonte Public Sans);
  - largura máxima da coluna; figura alta demais é reduzida para caber numa página.
  - Se um diagrama falhar, o build falha com o arquivo e a linha (mermaid escreve "Syntax error" no SVG; procure isso).
  - O texto dos rótulos usa `\n`: confira se quebra a linha. Se não quebrar, troque por `<br>` antes de renderizar, no HTML, sem tocar no `.md`.
- **Gráficos (`grafico`):** matplotlib em SVG vetorial, com a paleta do briefing de autores (seção 5.5), Public Sans, grade leve, sem moldura superior/direita e 160 mm de largura.
- **SVG autoral:** insira inline depois de sanitizar (sem `<script>`, `<foreignObject>`, `<image>` e `href` externo; o validador já recusa).
- **Quebras de página:**
  - capítulo começa em página nova; `h2`/`h3` nunca ficam sozinhos no pé da página;
  - quadros e figuras com `break-inside: avoid`; quadro maior que meia página pode quebrar;
  - tabelas longas repetem o cabeçalho.
- **Sumário e "Neste capítulo":** `target-counter(attr(href), page)` do Paged.js.
- **Marcadores do PDF (outline):** volume › capítulos › seções `##`, mais Questões, Comentários e Mapa. Faça no pós-processamento com PyMuPDF, a partir de âncoras invisíveis.
- **Metadados:** título "Disciplina · Volume NN · Título", autor "MentorIA", assunto com o id do volume, idioma pt-BR.
- **`content/material/index.json`:**
  - `{ "versao": 1, "geradoEm": …, "volumes": { "<disc>/mNN": { "arquivo": "material-pdf/<disc>/mNN.pdf", "paginas": N, "sha256": …, "bytes": …, "capitulos": { "<disc>/aNN/sNN": {"pagina": X, "ate": Y} }, "fixacao": {"pagina": …}, "comentarios": {"pagina": …}, "mapa": {"pagina": …} } } }`;
  - é dele que o app vai tirar "Abrir material MentorIA (págs. X a Y)";
  - atualize só as entradas dos volumes gerados.
- **Faixa do titular:** guarde no `index.json` o retângulo exato em pontos PDF (`"faixaTitular": [x0, y0, x1, y1]`), igual em todas as páginas. É onde a Etapa 5 vai carimbar.

### CLI

```
pipeline/.venv/Scripts/python pipeline/build_material.py --only direito-penal-militar/m01 [--carimbo-exemplo] [--html]   # um volume (--html também grava o HTML para depurar)
pipeline/.venv/Scripts/python pipeline/build_material.py --onda 1            # todos os APROVADOS da onda 1 (CFOA)
pipeline/.venv/Scripts/python pipeline/build_material.py --onda 1 --conferir # só as conferências da seção 4, sem regerar
```

- Só gera volume cujos capítulos, `volume.md` e `fixacao.json` estejam todos com status `APROVADO`. Os outros são pulados, com aviso.
- Em lote, gera cada volume num processo próprio, para um erro não derrubar os outros. Ao final, mostra a tabela: volume · páginas · tempo · avisos.

## 4. Conferências automáticas (o gerador falha ou avisa)

Rode em todo PDF gerado (`postprocess.py`):

1. Todo capítulo do volume tem âncora e página. O sumário bate com a página real de cada capítulo, e a ordem é a de `trechos`.
2. Nenhum texto fora da área útil e nenhuma página em branco no meio. Página em branco antes de abertura de capítulo só se for proposital (configurável).
3. **A faixa do titular está vazia em todas as páginas**: nenhum texto nem desenho no retângulo (PyMuPDF `get_text("words", clip=…)` e `get_drawings()`).
4. As fontes estão embutidas (`page.get_fonts()`): só Barlow Condensed, Public Sans e, se houver, IBM Plex Mono. Nenhuma Times ou Arial de fallback.
5. Nenhuma figura com erro: nada de "Syntax error", "mermaid" cru ou "```" no texto extraído.
6. O texto extraído não tem "Estratégia", "professor", "aula X", "página Y" do material-base nem "texto de apoio" (a lista `FORBIDDEN` do validador).
7. Toda questão da Fixação aparece duas vezes: em Questões e em Comentários. O gabarito impresso é igual ao do `fixacao.json`.
8. O tamanho do arquivo fica abaixo de 15 MB por volume (aviso acima de 10 MB).
9. Resumo por volume: páginas, páginas por capítulo (aviso se um capítulo passar de 30 páginas ou ficar abaixo de 4) e tempo de geração.

Grave o resultado em `material-pdf/_conferencia.md`, uma tabela por volume.

## 5. Fase 1 — amostras e PARE

Gere com `--carimbo-exemplo` estes quatro volumes. Eles cobrem os casos difíceis:
- `direito-penal-militar/m01`: jurídico, quadros de lei, jurisprudência, piloto aprovado;
- `administracao/m04`: muitos diagramas mermaid;
- `raciocinio-logico/m06`: exercícios resolvidos, fórmulas em Unicode;
- `fisica/m05`: `grafico` e `svg`. É da onda 2 e serve só para testar o motor; não entra no lote do CFOA.

Depois:
1. Rode as conferências da seção 4 e corrija o motor até passar.
2. Confira o mascote: marcador provisório em cada quadro de ressalva e nas seções da seção 1.1, e a troca automática quando houver imagem (teste com uma imagem qualquer de 1000 × 1000 px em `design/material/prontidao/mascote/atencao.png`, depois apague-a).
3. Exporte em PNG (PyMuPDF, 110 dpi) páginas de cada volume para `material-pdf/_amostras/`: capa, sumário, apresentação, uma abertura de capítulo, duas páginas de corpo (uma com tabela e outra com diagrama), a primeira página de Questões, a primeira de Comentários e o Mapa de revisão. Olhe todas: é a sua revisão visual.
4. Compare lado a lado com `design/material/modelos.html` (modelo A). Corrija o que destoar: cor, peso da fonte, filete, faixa, espaçamento.
5. Responda com:
   - os caminhos dos 4 PDFs, das imagens e do `_conferencia.md`;
   - páginas e tempo de cada volume;
   - o que ficou diferente da galeria e por quê;
   - as decisões que o dono precisa tomar, no máximo três (por exemplo: comentário junto da questão ou separado; página em branco antes do capítulo).
6. **PARE.** Não gere os 71 volumes antes de o dono aprovar as amostras.

## 6. Fase 2 — CFOA completo (só depois da aprovação)

1. Aplique o que o dono pedir. Depois rode `build_material.py --onda 1` e `--conferir`.
2. Os 71 volumes da onda 1 já estão APROVADOS. Se algum falhar na conferência, conserte o motor, nunca o conteúdo. Erro de conteúdo (diagrama mermaid inválido, SMILES errado) vai para o relatório, com volume, arquivo e linha, para o revisor.
3. Entregue o `index.json` atualizado e o `material-pdf/_conferencia.md`.

## 7. Testes

`pipeline/tests/test_build_material.py`:
- conversão de cada tipo de quadro;
- tabela; legenda de figura; lista; negrito e itálico;
- front matter;
- enunciado com `<u>` e `![Figura](/q-img/…)`;
- `grafico` com cada tipo gerando SVG;
- montagem de um volume mínimo de teste (fixture em `pipeline/tests/fixtures/material/`, conteúdo inventado, curto) até o HTML.

Um teste de integração, marcado para pular quando o Chromium não estiver instalado, gera o PDF da fixture e confere a faixa do titular vazia. `pipeline/.venv/Scripts/python -m pytest pipeline/tests -q` tem de passar inteiro (os testes que já existem também).

## 8. Regras

- **Não edite nada em `content/material/<disc>/mNN/`** (conteúdo aprovado). A única escrita em `content/` é `content/material/index.json`.
- Não altere `validate_material.py`, `check_citations.py`, `material_ficha.py`, `leis.py` nem os briefings de autores. Importar funções deles pode.
- Acrescente `/material-pdf/` ao `.gitignore`. Os PDFs nunca vão para o git.
- Arquivos novos permitidos:
  - `pipeline/build_material.py` e `pipeline/material_pdf/`;
  - `pipeline/tests/test_build_material.py` e `pipeline/tests/fixtures/material/`;
  - `design/material/prontidao/`;
  - `web/scripts/material-qimg.ts`;
  - `content/material/index.json`;
  - `pipeline/requirements.txt` (acréscimos).
  - Scripts de teste e rascunhos ficam fora do repositório (pasta temporária).
- Nunca grave no banco, nunca use `--remoto` nem `web/.env.remote`, nunca imprima nem edite `.env*`.
- Sem commit, salvo se o dono pedir.
- Windows: defina `PYTHONIOENCODING=utf-8`. Prefira a ferramenta de escrita de arquivos a heredocs longos.
- Custo: trabalhe sem subagentes. Na Fase 1 regenere só o volume que estiver ajustando (`--only`), não o lote.
- Ao terminar cada fase, acrescente uma seção curta em `HISTORICO.md` ("Material próprio: motor de PDF") e atualize a linha "Material próprio" do `CLAUDE.md`: comando do gerador, onde ficam os PDFs, `index.json` e modelo Prontidão.
