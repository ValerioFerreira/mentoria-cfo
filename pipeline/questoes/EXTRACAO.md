# Como extrair as questões dos cadernos do TecConcursos

> Documento versionado em `pipeline/questoes/EXTRACAO.md`. O importador copia este arquivo para
> `docs/questoes/COMO-EXTRAIR-QUESTOES.md` a cada execução. Edite sempre o original.

A **única fonte de questões objetivas do site** são os cadernos em PDF colocados em `docs/questoes/`.
Eles são exportados do TecConcursos pela opção **"imprimir caderno"**. Questões do material-base
(Estratégia) e questões autorais não entram mais no banco.

## 1. Rotina (comando manual)

```bash
# na raiz do projeto
pipeline/.venv/Scripts/python pipeline/questoes/importar.py            # cadernos novos -> banco local
pipeline/.venv/Scripts/python pipeline/questoes/importar.py --remoto   # idem + banco de produção (Neon)
```

| Opção | Efeito |
|---|---|
| `--remoto` | grava também no banco de produção. A URL fica em `web/.env.remote` (fora do git), na linha `REMOTE_DATABASE_URL="postgresql://..."` (URL do Neon, a mesma do `DATABASE_URL` da Vercel). |
| `--so-remoto` | grava só no remoto (o local já está em dia). |
| `--reclassificar` | reenvia todo o acervo já extraído, sem reler os PDFs. Use depois de mudar `content/questoes/mapa-assuntos.json`, o catálogo ou a segmentação. |
| `--forcar` | reextrai todos os PDFs. |
| `--so-extrair` | extrai, classifica e gera o relatório, sem gravar em banco nenhum. |
| `--confirmo-producao` | autoriza gravação **em massa** no remoto (mais de 300 questões, `--reclassificar`, `--forcar` ou reextração por versão nova do extrator). Sem ela, ou sem backup íntegro de menos de 24 h (`npx tsx scripts/questoes-backup.ts --remoto`, em `web/`), o importador para antes de gravar. |
| `--limpar-estrategia` | apaga do(s) banco(s) toda questão cujo id não começa com `tec_` (com respostas e denúncias) e os cadernos que ficarem vazios. Foi usado uma vez, na migração; é idempotente. |

**O que a rotina faz:**

1. Copia este documento para `docs/questoes/`.
2. Calcula o sha256 de cada PDF. Os já conhecidos estão em `docs/questoes/.importadas.json`. Um PDF repetido com outro nome é ignorado; um PDF extraído por versão antiga do extrator (`EXTRACTOR_VERSION` em `tec_pdf.py`) é reextraído.
3. Extrai cada PDF novo para `docs/questoes/.extraidas/<sha>.json`, com as figuras em `.extraidas/img/<sha-da-figura>.png`.
4. Junta todos os cadernos extraídos em um **acervo**: uma questão por número do TEC, e vale a versão do caderno mais recente.
5. Classifica cada questão (seção 6).
6. Monta o lote `.extraidas/lotes/<data>-<destino>.jsonl` só com as questões dos cadernos ainda não gravados naquele destino (com `--reclassificar`, o acervo inteiro).
7. Grava o lote com `web/scripts/questoes-sync.ts` (seção 7).
8. Escreve o relatório `docs/questoes/relatorios/AAAA-MM-DD-HHMM.md` com:
   - contagens por caderno e por disciplina;
   - anuladas;
   - quarentena;
   - questões fora do edital;
   - assuntos sem curadoria;
   - resultado da gravação.

Rodar de novo sem PDF novo não faz nada (≈ 2 s). O índice do classificador fica em cache
(`pipeline/.cache/questoes/catalog.pkl`). Ele é refeito sozinho, em ≈ 3 a 4 min, quando o conteúdo
do curso muda.

Para conferir o banco, só leitura: `npx tsx scripts/questoes-contagem.ts [--remoto]`, rodado em `web/`.

## 2. Anatomia do PDF

Página A4 (595 × 842 pt). Tudo é lido com PyMuPDF em `get_text("rawdict")`, caractere a caractere,
com posição, fonte, tamanho, cor e flags. A tabela vale para todos os cadernos vistos até
12/10/2026 (17 cadernos, 2.999 questões).

| Elemento | Assinatura | Tratamento |
|---|---|---|
| Cabeçalho e rodapé do navegador | fonte **ArialMT 8,0**: data/hora, título do caderno, URL `.../cadernos/<id>/imprimir`, "n/N" | descartar |
| Capa (pág. 1, antes da 1ª questão) | logo 116×116 em (28, 69); título em SourceSansPro 12,1; link `tecconcursos.com.br/s/...`; "Ordenação: ..." em Tahoma 8,3 | descartar (o título vira `titulo` do caderno) |
| **Início de questão** | linha `www.tecconcursos.com.br/questoes/<número>` em **Tahoma-Bold 6,6**, x ≈ 28 | abre a questão; `<número>` é o id TEC (`tec_<número>` no banco) |
| Linha(s) de banca | **Tahoma 8,8**: `Banca - Cargo (Órgão)/Órgão[/Área/...]/AAAA`. Pode quebrar em duas linhas e até mudar de página; termina sempre em `/AAAA` | `banca` = antes do 1º " - " ("Instituto AOCP" e "AOCP" → `AOCP`); depois, separado por "/": cargo, órgão, área..., ano |
| Linha(s) de matéria | Tahoma 8,8 logo após a banca: `Matéria - Assunto` (quebra em ≈ 3% dos casos; o assunto pode vir vazio) | separar no **primeiro** " - " (o assunto pode conter " - ") |
| **Número no caderno** | `NNNN)` em **Tahoma-Bold 7,2**, x ≈ 28, na altura da 1ª linha do corpo (o texto começa em x 48–52); no topo de página pode vir no mesmo bloco que o enunciado | chave do gabarito; não entra no texto (o span é separado do resto da linha) |
| Corpo (enunciado) | Tahoma 7,2, x ≈ 28 | texto (seção 3) |
| Texto-base | trechos longos antes do comando, terminando numa linha de **fonte** (Tahoma ≤ 6,7, em geral alinhada à direita: "Disponível em...", "Adaptado de...") | tudo até a última linha de fonte que ainda tem enunciado depois vai para `support` |
| Alternativas | x ≈ 46: `a)`…`e)` em sequência (4 ou 5); a continuação fica no mesmo recuo | `options` A–E. Vale a **última** sequência `a), b), c), d)[, e)]` (o enunciado pode ter listas "a) ..." próprias) |
| Certo/Errado | duas últimas linhas exatamente "Certo" e "Errado", em x ≈ 46 | `kind = CERTO_ERRADO`; opções `C` ("Certo") e `E` ("Errado") |
| Separador | pontilhado de quadradinhos 1×1 pt (≈ 490 desenhos por questão) | ignorar |
| Marcador de lista desenhado | forma preenchida ≤ 4,5 pt e com altura ≥ 1,5 pt | vira "•" (traço curto mais fino é sublinhado de letra destacada, não marcador) |
| Fundo branco invisível | retângulo preenchido de branco, sem contorno, atrás do texto | ignorado (antes transformava parágrafos comuns em imagem) |
| Lacuna de preencher | sequência de ≥ 3 espaços sublinhados | `______` (lacunas vizinhas ou partidas entre linhas viram uma só) |
| Sublinhado | traço horizontal ≤ 1,3 pt logo abaixo da baseline do texto | `<u>` só nos caracteres cobertos |
| Texto colorido | cor ≠ preto (vermelho e similares: "palavras destacadas") | `<mark>` (URLs coloridas ficam sem marca) |
| Negrito | Tahoma-Bold (flag 16) | `**...**` |
| Monoespaçado | Courier/Consolas (fórmulas de planilha) | `` `...` `` |
| Sobrescrito/subscrito | span menor (≤ 85% do tamanho da linha) acima/abaixo da baseline | `<sup>` / `<sub>` (ex.: CO<sub>2</sub>, Pb<sup>2+</sup>) |
| Fórmulas MathJax | fontes **Type3** (5,5–13,3 pt) | seção 4 |
| Tabelas e figuras vetoriais | traços (linhas, retângulos) que não são separador nem sublinhado | recorte PNG |
| Figuras | imagens embutidas na região da questão (≈ 5,5% das questões) | PNG (seção 4) |
| **Gabarito** | última(s) página(s): título "Gabarito" em Tahoma 11,0 e depois `N) X`, com X ∈ {A–E, Certo, Errado, Anulada} | liga ao número do caderno |
| Comentários | **não aparecem** nos cadernos atuais | `explanation` fica vazia; a tela esconde o bloco |

Uma questão pode atravessar páginas. A região dela vai do seu link até o link da próxima questão ou
até o título "Gabarito".

## 3. Montagem do texto

1. **Linhas visuais.** Fragmentos de texto comum (Tahoma) com sobreposição vertical ≥ 40% formam
   uma linha.
   - Fórmulas (só Type3) e figuras entram na linha com que mais se sobrepõem; sem sobreposição,
     formam linha própria.
   - Linhas que passam a se sobrepor se fundem, exceto quando as duas começam texto (x ≤ 56). Assim,
     alternativas com frações altas continuam separadas.
2. **Modo de cada linha.**
   - **texto**: sem fórmula, ou com fórmula simples (todos os spans Type3 do mesmo tamanho e na mesma
     baseline, sem glifo da área privada).
   - **fórmula embutida**: texto comum + fórmula com índices, frações, raízes ou traço de fração,
     até 30 pt de altura. Só a fórmula vira imagem, no meio da frase.
   - **recorte**: linha só de fórmula (fórmula em bloco), linha com tabela/figura vetorial, figura
     encostada em texto, glifo sem texto ou fórmula alta. Recortes consecutivos viram uma imagem.
     Linhas de texto comum largas (≥ 120 pt) que só encostam na fórmula saem do recorte e voltam a
     ser texto (ex.: a frase antes de uma chave "{").
3. **Espaços.** Entre spans, entra um espaço quando a distância horizontal é > 1,2 pt e nenhum lado
   já tem espaço (não vale antes de sobrescrito/subscrito). Espaço antes de pontuação logo após uma
   fórmula é removido.
4. **Parágrafos.**
   - Linhas da mesma página separadas por > 3 pt de espaço vertical iniciam parágrafo.
   - Também inicia parágrafo a linha que começa item de lista: "•", "-", "( )", "(V)", "(F)",
     "I." a "X.", "1.", "a)" — inclusive com o numeral em negrito e a pontuação fora dele ("**IV**.").
   - Na virada de página não há espaço vertical a medir: se a linha anterior termina frase (. : ? !) e a
     nova começa com maiúscula, abre parágrafo.
   - Linhas do mesmo parágrafo são unidas com espaço. Se a anterior termina em letra + "-" e a
     seguinte começa minúscula, são unidas sem espaço ("tornou-" + "se").
   - Figura ou recorte é sempre um parágrafo próprio.
5. **Escapes.** `*`, `` ` `` e `\` literais saem como `\*`, `` \` `` e `\\`. Caracteres de controle
   (NUL etc.) são descartados.
6. **Rótulo da alternativa.** O "a)" é retirado do texto, inclusive quando está dentro de negrito ou
   sublinhado.

**Marcação emitida.** É o único formato aceito pelo site (`web/src/components/rich-content.tsx`):

| Marcação | Uso |
|---|---|
| `**negrito**`, `<u>sublinhado</u>`, `<mark>destaque</mark>`, `<sup>`, `<sub>`, `` `código` `` | formatação de texto |
| parágrafos separados por linha em branco | quebra de parágrafo |
| `![Figura](/q-img/<sha256>)` | figura (bloco, com zoom) |
| `![Fórmula](/q-img/<sha256>)` | recorte de fórmula ou tabela (bloco) |
| `![fórmula:<altura-em-em>](/q-img/<sha256>)` | fórmula no meio da frase; a altura é relativa ao corpo do texto |

Recortes preto-sobre-branco usam a classe `q-crop`: no tema escuro são invertidos; no claro e no
sépia, o branco some no fundo.

## 4. Figuras e recortes

- **Figura embutida.** Usa os pixels originais (`Pixmap(xref)`) quando a imagem não tem máscara e
  aparece em ≈ tamanho natural; senão, renderiza a área a 200 dpi.
- **Recorte.** `page.get_pixmap(clip=…, dpi=200)` da área da linha.
  - A altura vem da "tinta provável": de 0,72 × tamanho acima da baseline até 0,24 × tamanho abaixo.
  - Antes de salvar, a tinta de linhas vizinhas que invade o recorte (frações empilhadas) é pintada
    de branco, sem tocar nas caixas da própria linha.
  - Em alternativas cujo span começa com "a)", o recorte começa 7 pt depois do rótulo.
- **Id.** sha256 do PNG. Figura repetida (inclusive entre cadernos) é gravada uma vez.
- **Limite.** Lado ≤ 1.600 px; acima disso, é reduzida.
- **No banco.** Tabela `QuestionImage`, servida por `GET /q-img/<sha256>`. Exige sessão; cache
  `immutable`. Questão nova aparece sem deploy.

## 5. Gabarito, anuladas, validação e quarentena

- `Anulada` → a questão **não entra**. Se já existir no banco, passa a `RETIRED`.
- Múltipla escolha: o gabarito deve ser uma letra presente nas alternativas.
- C/E: o gabarito deve ser Certo ou Errado (`C`/`E`).
- **Invariantes por questão.** Uma falha manda a questão para a **quarentena** (não importada e
  listada no relatório):
  - cabeçalho com ano e com "Matéria";
  - número do caderno;
  - enunciado ou texto-base não vazio;
  - alternativas `abcd`/`abcde` não vazias, ou Certo/Errado;
  - entrada no gabarito com valor conhecido e compatível.
- **Invariantes por caderno.** Uma falha vira anomalia no relatório:
  - existe a seção Gabarito;
  - nº de links = nº de números de questão = nº de entradas do gabarito, sem número repetido.
- **Conferência.** `pipeline/tests/test_questoes.py` checa as invariantes nos cadernos reais
  (`QUESTOES_TODOS=1` roda todos). Desde a criação, a extração tem 0 quarentena. A cobertura de
  palavras PDF × texto extraído é de 100% fora dos recortes.

## 6. Classificação (disciplina → atividade → assunto do edital)

Arquivo de curadoria: `content/questoes/mapa-assuntos.json` (versionado).

- **`materias`**: matéria do TEC → disciplina do site. Exemplos:
  - "Direito da Criança e do Adolescente" → `direito-constitucional` (o ECA é complemento dessa
    disciplina);
  - "Legislação Penal e Processual Penal Especial" → `direito-constitucional` (Maria da Penha).
  - Matéria sem mapa: a questão não entra e o relatório pede o mapeamento.
- **`assuntos`**: `"Matéria|Assunto"` → uma das formas:
  - `{"aulas": [...]}`: aulas permitidas; o trecho é escolhido pelo texto;
  - `{"segments": [...]}`: trechos fixos;
  - `{"subject": "...", "aulas": [...]}`: outra disciplina (ex.: Análise Combinatória de Matemática
    → `raciocinio-logico/a06`);
  - `{"skip": "motivo"}`: fora do edital, não entra.
  - O campo `_n` é só informativo (nº de questões na curadoria).

**Trecho (= atividade de Teoria do planejador).** TF-IDF em Python puro, por disciplina:

- Tratamento do texto: sem acentos, stopwords em português, radical leve (-ções → -ção, plural),
  unigramas + bigramas.
- **Documento de cada trecho:**
  - título da aula ×3;
  - tópicos do trecho (`content/segments`) ×3;
  - itens do edital que apontam para o trecho (`content/edital`) ×2,5;
  - bizu: resumo e ponteiros ×1,5, itens C/E ×1;
  - resumo analítico ×1;
  - texto do material das páginas do trecho ×0,6 (cache local `pipeline/.cache/pages`; usado só para
    classificar, nunca publicado).
- **Questão:** assunto TEC ×3 + enunciado + alternativas + início do texto-base.
- **Assunto com curadoria:** o trecho é o de maior similaridade dentro das aulas permitidas. Status
  **APPROVED**.
- **Assunto sem curadoria:** todas as questões do assunto votam na aula (soma das similaridades + 2 ×
  similaridade do nome do assunto).
  - Se a melhor aula tem score ≥ 0,12 e é ≥ 1,35 × a segunda → **APPROVED**;
  - senão → **DRAFT** com os candidatos em `classifyNote`, para revisão em `/admin/revisao`.
- **Assunto do edital (`editalItemId`):** entre os itens do edital **da própria disciplina** que listam o
  trecho escolhido, o de maior similaridade (item de outra disciplina que aponta para o trecho por relação
  cruzada não vale: deixava 130 questões de Estatística sem assunto). Sem item do trecho, um item que lista a aula. Sem nenhum, fica nulo.

**Como corrigir a classificação:**

- Assunto inteiro: edite `mapa-assuntos.json` e rode `importar.py --reclassificar` (e
  `--so-remoto --reclassificar` para a produção).
- Questão isolada: em `/admin/revisao`, escolha o trecho no seletor (aprova e marca
  `classifiedBy = MANUAL`) ou use "Aprovar assunto" para os rascunhos de um assunto. O importador
  nunca sobrescreve trecho, item do edital ou status de questão `MANUAL`.

Se a segmentação de uma disciplina mudar, os ids de trecho mudam (são posicionais): rode
`--reclassificar`.

## 7. Gravação (`web/scripts/questoes-sync.ts`)

- Lê o lote JSONL, com três tipos de linha:
  - `image`: figura, enviada primeiro;
  - `question`;
  - `retire`: anulada ou fora do edital; se existir no banco, vira `RETIRED`.
- **Upsert por id `tec_<número TEC>`.** O histórico de respostas é preservado, porque a resposta
  guarda o rótulo escolhido. Ao mudar o texto, as alternativas são recriadas.
- **Campos gravados:**
  - origem: `externalId`, `kind`, `banca`, `orgao`, `cargo`, `ano`, `tecMateria`, `tecAssunto`
    (também em `topic`), `sourceFile`;
  - classificação: `editalItemId` (só se o item existir no banco), `contentHash`, `classifyScore`,
    `classifyNote`, `importedAt`;
  - fixos: `pattern = banca`, `difficulty = 2`, `explanation = ""`, `batch = tec-AAAAMMDD`.
- Trecho inexistente no banco de destino: a questão é pulada e listada (catálogo desatualizado; rode
  o seed de estrutura).
- **Desempenho.** Criações em lotes de 300; atualizações em paralelo (8). As questões **não** são
  semeadas no build da Vercel: só este comando grava questões.

## 8. Onde as questões aparecem no site

| Lugar | Critério |
|---|---|
| **Caderno ao fim das atividades** (planejador, 25 questões) | questões dos **trechos** das Teorias revistas pela atividade (`segmentId in activity.segments`), status servível |
| **Questões** (treino livre) e **Montar caderno** | agrupadas por **assunto do edital** (`editalItemId`, ordem do edital; sem item → "Outros assuntos"), com filtro de banca |
| **Simulados** | só `MULTIPLA_ESCOLHA` da banca AOCP |
| **Fixação** | não usa o banco: continua apontando as questões comentadas do material |

## 9. Problemas conhecidos e como agir

| Situação | O que fazer |
|---|---|
| Caderno com anomalia ou questão em quarentena | Abra o relatório. Se o layout do TEC mudou, ajuste `tec_pdf.py`, aumente `EXTRACTOR_VERSION` e rode de novo (os cadernos são reextraídos sozinhos). |
| Assunto novo em "Assuntos sem curadoria" | Inclua-o no mapa e rode `--reclassificar`. |
| Muitas questões "fora do edital" | Licitações (Lei 14.133), improbidade (Lei 8.429), processo administrativo (Lei 9.784), lei anticorrupção, realidade de outros estados e técnicas de laboratório **não têm aula no curso**. Para aproveitá-las, crie um complemento (aula `AUTHORED`) e mapeie os assuntos para ele. |
| Banco remoto não grava | Confira `web/.env.remote`. Confira também se as migrações da produção estão aplicadas (o deploy da Vercel roda `prisma migrate deploy`). |

## 10. Auditoria, backup e reversão

- Auditoria somente leitura: `pipeline/.venv/Scripts/python pipeline/questoes/auditoria.py [--backup DIR] [--extraidas DIR]`.
  Relê cada PDF por um caminho independente do extrator (spans, não caracteres), compara palavra a palavra
  e figura a figura com o texto extraído, confere número e gabarito, reclassifica o acervo e compara com o
  banco (a partir do backup). Saída em `docs/questoes/auditoria/<data>/` (fora do git: contém texto de questões).
- Backup verificável (só leitura), em `web/`: `npx tsx scripts/questoes-backup.ts --remoto` grava
  `backups/questoes-remoto-<data>/` com `Question`, `QuestionOption`, `QuestionImage`, `QuizSession`,
  `QuizAnswer`, `QuestionReport`, ids de estrutura e `manifest.json` (sha256 e integridade referencial).
  `--verificar <pasta>` confere um backup.
- Reversão, em `web/`: `npx tsx scripts/questoes-restore.ts <pasta>` (simulação; mostra a diferença) e
  `--aplicar` (local) ou `--remoto --aplicar --confirmo-producao`. Devolve questões, alternativas e figuras ao
  estado do backup; questão criada depois do backup vira `RETIRED` (nunca é apagada); não toca em sessões,
  respostas, denúncias, planos nem usuários e confere, ao fim, que as contagens deles não mudaram. Testado em
  14/10/2026 no banco local: produção → local → original, sem diferenças e sem perda de respostas.
- Status ao regravar (`web/src/lib/quiz/sync-rules.ts`): anulada/fora do edital → `RETIRED`; denunciada
  continua `FLAGGED`; decisão do administrador (`MANUAL`) prevalece; questão retirada **automaticamente**
  volta quando a curadoria passa a aceitá-la (antes, `RETIRED` era definitivo).
- O caderno das atividades do plano usa só questões da banca AOCP (`activityQuizWhere` em
  `web/src/lib/quiz/banca.ts`), como os simulados; o treino livre continua aceitando as demais bancas.

