# Auditoria — Língua Portuguesa

Escopo: aulas a00–a14 (PDFs do Estratégia) e complementos c01 (figuras de linguagem), c02 (formação de palavras), c03 (funções do "que" e do "se"). Todas as páginas de todas as aulas foram varridas (primeiras linhas úteis por página e títulos em caixa-alta); páginas suspeitas foram lidas. a13 e a14 foram varridas pelos marcadores de seção.

## Números

| | Antes | Depois |
|---|---|---|
| Páginas de teoria (a00–a12, no edital) | 709 | 708 |
| Trechos (a00–a12) | 52 | 54 |
| Páginas de teoria / trechos (incl. a13, fora do edital) | 802 / 58 | 801 / 60 |
| Trechos > 17 págs. | 0 | 0 |
| Cortes no meio de tópico (relatório do segment.py) | — | 1 (a08) |

## Correções (`content/overrides/lingua-portuguesa.json`)

| Aula | Mudança | Motivo |
|---|---|---|
| a00 Nivelamento | 14 subtítulos reais adicionados (Introdução, Ortografia, Classes de palavras, Pronome, Colocação pronominal, Conjunções, Verbo, Sintaxe, Pontuação, Concordância, Regência, Crase, Semântica, Interpretação); cortes em 15, 29, 44, 58; nota reescrita | O índice só trazia "Apresentação"; os trechos cortavam no meio dos temas e tinham subtítulos falsos. Agora: 4–14 introdução+ortografia · 15–28 classes/pronomes/colocação · 29–43 conjunções+verbo · 44–57 sintaxe/pontuação/concordância/regência · 58–68 crase/semântica/interpretação. A pág. 3 (apresentação comercial) passou a abertura. |
| a01 Ortografia/Acentuação | cortes 19, 29, 41, 53 (4 → 5 trechos) | O hífen ficava partido entre dois trechos e o 4º misturava letras com expressões. Agora: acentuação geral · hiato+diferenciais · hífen · letras/maiúsculas/siglas · expressões problemáticas. |
| a02 Classes I | cortes 18, 35, 45, 59, 71, 84 (6 → 7) | O antigo s04 juntava numeral, interjeição, palavras especiais e início de pronomes; colocação pronominal (item 15 do edital) ficava misturada com pronomes pessoais. Agora: substantivo · adjetivo · advérbio · artigo/numeral/interjeição/palavras especiais · pronomes I (interrogativos a demonstrativos) · pronomes II (relativos, tratamento, pessoais) · **colocação pronominal (84–92)**. |
| a03 Preposição/Conjunção | cortes 13, 25 | Preposições (3–12) saíram do trecho de conjunções; coordenativas (13–24) e subordinativas (25–41, 17 págs.) ficaram cada uma num trecho — é o núcleo do item 4. |
| a04 Verbos | cortes 19, 35, 52, 69, 79 | O antigo s05 misturava verbos vicários/pronominais com correlação verbal. Agora: indicativo I · indicativo II+subjuntivo+imperativo · formas nominais/transitividade/impessoais/auxiliares/ligação · conjugações difíceis/defectivos/vicários/pronominais · correlação · vozes verbais. |
| a05 Sintaxe | cortes 17, 30, 40, 53, 69 | O s03 juntava fim dos termos da oração com o início do período composto, e "que"/"se" estavam partidos em dois trechos. Agora: sujeito · complementos e adjuntos · predicativo do objeto a agente da passiva · período, coordenadas, substantivas, adjetivas · adverbiais+reduzidas+paralelismo · **funções do QUE/SE/COMO (69–84)**. |
| a09 Coesão | corte 17 | Coesão referencial inteira em 3–16; sequencial+coerência+reescritura em 17–23 (7 págs., assunto autônomo). |

Sem mudança (divisão já boa ou alternativa não melhor): a06, a07, a08, a10, a11, a12, a13. Notas: a07 tem 33 págs. de sujeito simples que precisam ser cortadas em algum ponto; a08 corta a lista de verbos de regência (3–21, longa demais para um trecho); a11 divide a dissertação em 18–28 / 29–40 (descrição/injunção sozinhas ficariam curtas demais).

Vínculos `edital`/`kind`/`practiceFor` gerais: a00 `partial` (mantido), a13 `no` (confirmado: o conteúdo do 2º Tenente não traz redação oficial), a14 `practice` com vínculos corretos (conferi os 16 temas contra as seções do PDF). Não mexi no `practiceFor`.

## Cobertura do edital

| Item | Status | Onde |
|---|---|---|
| 1 Compreensão e interpretação | coberto | a11 51–69 |
| 2 Tipologias e gêneros | coberto | a11 3–40 |
| 3 Figuras de linguagem | complemento | c01 (Estratégia: só elipse/zeugma em a06 30–31, silepse em a07 30–31, denotação/conotação em a10 5–7) |
| 4 Relações semânticas entre orações | coberto | a03 13–41 (conectivos e seus valores), a05 45–58, a09 17–19, a11 33–38 |
| 5 Ortografia | coberto | a01 3–10, 29–64 |
| 6 Acentuação | coberto | a01 11–28 |
| 7 Classes de palavras | coberto | a02 3–83, a03, a04 |
| 8 Crase | coberto | a08 27–40 |
| 9 Sintaxe da oração e do período | coberto | a05 3–68 |
| 10 Funções do "que" e do "se" | coberto (**falsa lacuna**) | a05 69–81 |
| 11 Coesão | coberto | a09 3–19; a02 66–70 (anáfora/catáfora) |
| 12 Pontuação | coberto | a06 3–49 |
| 13 Concordância | coberto | a07 3–55 |
| 14 Regência | coberto | a08 3–26 |
| 15 Colocação pronominal | coberto | a02 84–92 |
| 16 Formação de palavras | complemento | c02 (Estratégia: só a02 7–8 e a01 33) |
| 17 Significação das palavras | coberto | a10 3–29 |
| 18 Variação linguística | coberto | a12 3–26 |

## O que a a00 (Nivelamento) cobre que as outras não cobrem

Nada que esteja no edital. Só tem de próprio a introdução conceitual (língua × linguagem, elementos da comunicação, norma-padrão, divisão da gramática, págs. 4–8). Todo o resto é uma versão curta das Aulas 01–12, com cerca de 44 questões comentadas no meio do texto. Serve ao aluno iniciante; para os outros é redundante (≈ 5 trechos).

## Auditoria inversa (resumo; lista completa em `content/edital/lingua-portuguesa.json`)

- **a05 69–81 — funções do QUE/SE: já corretamente indexada, lacuna falsa.** São 13 páginas de teoria completa: todas as classes do "que", a função sintática do relativo, todas as funções do "se" e critérios para separar apassivador, reflexivo e pronominal, com questões. A "lista curta da pág. 90" citada antes é só o resumo.
- a02 84–92 colocação pronominal: subindexada (no fim da aula de classes); agora é trecho próprio.
- a00 pág. 51: falso subtítulo automático (exemplo de vírgula) que o `dropHeadings` não remove — ver pedidos.
- a14 463–538 (lista de Compreensão textual, 76 págs.): subindexada; não alimenta nenhuma Fixação.
- a06 50–53 tipos de frase e a11 41–50 funções da linguagem: fora do texto do edital, mas ligados aos itens 12 e 1/2; mantidos.
- a06 77–87: a lista repete páginas comentadas (com comentários); não afeta a teoria.
- a13 inteira e a14 543–549/856–862 (redação oficial): fora do escopo.
- Não achei teoria classificada como C/L/S, nem questões ou resumo classificados como T fora do padrão (as questões comentadas no meio da teoria são o formato do Estratégia em todas as aulas).

## Lacunas e complementos

- **c01 Figuras de linguagem — necessário, suficiente para o peso (Português = 5 questões).** Correções: antonomásia apresentada como caso de perífrase (antes aparecia como sinônimo de perífrase e de novo como figura separada); exemplo de silepse de número trocado (o antigo, com verbo colado no sujeito, seria tratado como erro de concordância); exemplo de assonância trocado (era adaptação de letra de música); exemplo de apóstrofe trocado por um original.
- **c02 Formação de palavras — necessário e suficiente.** Correções: "superhomem" → supermercado (pela regra atual o certo é super-homem), "antesala" → prever (o certo é antessala); radical "pirô" → "piro"; tirei "drive" (abreviação) e "fofoca" (reduplicação), que eram exemplos errados; "4 passos" → "5 passos".
- **c03 Funções do "que" e do "se" — redundante** (a05 69–81 cobre o tema). Mesmo assim corrigi: na tabela da conjunção subordinativa, "embora" e "conforme" (não têm "que") deram lugar a locuções com "que"; exemplo interrogativo usado como exclamativo; exemplos de "que" adversativo/alternativo e de "se"/"que" expletivo que não eram naturais; incluí o "se" causal, que era citado sem explicação; título com aspas tipográficas (o título no catálogo estava cortado: `Funções do "que" e do "se`).
- Os PDFs dos complementos precisam ser regerados (`build_complements.py`) para refletir as correções.

## Pendências

1. Decidir sobre o c03: tirar do plano (a lacuna é falsa) ou mantê-lo só como revisão/aprofundamento. Hoje ele ocupa um trecho no Essencial.
2. a00 `partial` entra no Essencial com metade da incidência (≈ 5 h). Avaliar se deve ser só para nível iniciante.
3. Corrigir o falso subtítulo automático na a00, pág. 51 (só cosmético em `topicsCovered`).
4. a08: o corte em 15 cai no meio da lista de verbos de regência (inevitável com o teto de 17 págs.).

## Pedidos ao orquestrador

1. `content/gaps.json`: marcar a parte "funções do que/se" de `port-figuras-formacao` como **falsa lacuna** (coberta por a05 69–81) e decidir se o c03 sai do plano ou vira opcional.
2. `practiceLinks`: ligar a14 463–538 (Lista de Questões — Compreensão textual) à a11. Hoje o `build_catalog` parece ligar só as seções C; o tema "Compreensão textual" do `practiceFor` não gera link.
3. `segment.py`: aplicar `dropHeadings` também aos subtítulos automáticos (`auto_headings`), ou filtrar linhas de exemplo com "___"; caso a00 pág. 51.
4. `build_complements.py`: o parser do frontmatter corta a aspa final dos títulos (`Funções do "que" e do "se`). Contornei usando aspas tipográficas no .md, mas o parser deve ser corrigido.
5. Rodar `build_complements.py` + `build_catalog.py` + seed para publicar os novos trechos e os complementos corrigidos.
