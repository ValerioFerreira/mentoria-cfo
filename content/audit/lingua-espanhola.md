# Auditoria estrutural — Língua Espanhola

Material: 17 aulas (a00–a16), Prof. Adinoél e Profa. Elenice. Edital: item "Língua Estrangeira – Espanhol" (itens 1–11), em `pipeline/.cache/edital_2ten.txt`.
Correções em `content/overrides/lingua-espanhola.json`; mapa edital → material em `content/edital/lingua-espanhola.json`.

## Números

| | Antes (pós-correção global) | Depois |
|---|---|---|
| Páginas de teoria | 859 | 466 |
| Trechos de Teoria | 64 | 36 |
| Trechos > 17 págs. | 0 | 0 |
| Cortes no meio de tópico | 16 | 1 (a10, cardinais: tópico único de 25 págs.) |

Todas as aulas foram varridas página a página (`--heads`), com leitura das páginas suspeitas.

## Correções por aula

| Aula | Correção | Motivo |
|---|---|---|
| a00 Pontuação/Alfabeto | 18-20 → C; `edital: partial` | 18-20 são 2 questões comentadas. Pontuação e alfabeto não estão no edital; a aula fica como introdução à leitura. |
| a01, a02, a03, a04, a05, a07, a12 | sem mudança | Mapa e trechos corretos; cortes em início de tópico. |
| a06 Substantivos | 81-87 → L, 88 → K, 89-126 → B; cortes 21, 30 | Lista, gabarito e apêndice estavam todos como C. Trechos: gênero (5-20), casos especiais de gênero + número + classificação (21-29), vocabulário temático (30-41, 42-54). Assim a gramática fica separada do vocabulário. |
| a08 Pronomes | 56-86 → C, 109-115 → L; corte 22 | As questões 10-20 (rótulos "10.(CEPERJ_2014/Q_32)") reabriam a teoria: eram 3 trechos falsos. O corte em 22 deixa todos os possessivos (13-21) num trecho só. |
| a09 Verbos | 86-160 → C, 161-179 → L, 180-181 → K, 182-185 → B; subtítulos 78/81/83/85 (do sumário) e 42/48; cortes 18, 31, 42, 55, 72 | Sem marcador de fim de teoria: 180 págs. viravam 11 trechos. Agora são 80 págs. em 6 trechos: conjugação/formas não pessoais · formas pessoais/modos/tempos · significado dos tempos do indicativo · subjuntivo + imperativo · desinências · compostos + perífrases + passiva. |
| a10 Números | 77-105 → B; cortes 16, 31 | Os textos de treino de leitura viravam 2 trechos; nas outras aulas esse bloco é B. O corte em 16 começa no passo das centenas (100-999). |
| a11 Interpretação | 26-27 → T, 28-84 → C, 85-111 → L, 112 → B, 113-118 → T (subtítulo novo), 119-153 → B; corte 16 | Rótulos "CEBRASPE_…_QUESTÃO_77" reabriam a teoria (8 trechos falsos). "Vocabulário" (26-27) é explicação, não resumo. A leitura complementar 113-118 é conteúdo novo e central para o item 1 (tipos de leitura, tipologia, estratégias de prova): entrou como trecho próprio de 6 págs. Trechos: frase/oração/período/parágrafo (5-15); tipos de texto → coesão/coerência (16-27); estratégias (113-118). |
| a13 Silabeo/Sinonímia/Divergências | 34-40 → T, 85-88 → L, 89 → K, 90-117 → B; cortes 17, 27, 44, 56 | 34-40 é a lista de palavras heterossemânticas (vocabulário, não questões). Trechos: silabeo · sinônimos/antônimos · divergências léxicas (heterotônicos, heterossemânticos, heterogenéricos) · falsos cognatos · marcadores temporais. |
| a14 Prova comentada AOCP 2015 | F 4, C 5-55, L 56-66, K 67-68 | A "Tradução livre" (50-55) virava teoria. Agora a aula não tem teoria. |
| a15 Prova comentada AOCP PM-PE 2023 | F 3, L 4-9, C 10-23; nota | Os textos da prova viravam 3 trechos (1-6 págs.). **É a mesma banca, com cargo de oficial em PE: a prática mais valiosa da disciplina.** |
| a16 Prova comentada Cebraspe SEE-PE | F 5, C 6-95, L 96-101, K 102-103 | Os "ITEM 51…91" e uma tabela de artigos (subtítulos automáticos) viravam 7 trechos. Sem teoria. |

## Cobertura do edital (resumo)

| Item | Status | Onde |
|---|---|---|
| 1 Leitura e compreensão | covered | a11 5-27, 113-118; prática: a11, a14, a15, a16 |
| 1 Artigos definidos/contrações | covered | a01 11-23; a03 4-11 |
| 1 Artigos indefinidos | covered | a01 14-15, 22-23 |
| 1 Possessivos | covered | a08 13-21 |
| 1 Demonstrativos | covered | a08 26-29 |
| 1 Numerais | covered | a10 4-39; a07 11 |
| 1 Indefinidos | covered (curto) | a07 11; a08 30-31 |
| 1 Relativos | partial | a08 32-33 (2 págs.) |
| 1 Interrogativos/exclamativos | covered | a07 11-12; a08 24-25; a05 26-29 |
| 2 Substantivos: gênero / número | covered (número: 1 pág.) | a06 11-27 |
| 2 Substantivos: **grau** | **gap** | — |
| 3 Adjetivos: gênero, número, grau | covered | a07 13-30 |
| 4 Pronomes (todas as classes) | covered (relativos: partial) | a08 9-36 |
| 5 Verbos auxiliares / regulares | covered | a09 8-11, 23-24, 55-77, 81-84 |
| 5 Irregulares (comum × própria) | **partial** | a09 12-13 (sem classificação nem modelos de irregularidade) |
| 5 Impessoais | **partial** | a09 79-80 (só "hay que") |
| 5 Pronominais | **partial** | a09 52; a08 22-23; o resto só em questões |
| 5 Perífrases | covered | a09 78-80 |
| 6 Advérbios e locuções | covered | a05 5-29; a13 56-67 |
| 7 Preposições | covered | a02 5-35 |
| 8 Conjunções coord./subord. | covered | a04 9-33 |
| 9 Acentuação | covered | a12 4-20; a13 4-16 |
| 10 Sinônimos/antônimos | covered | a13 17-26 |
| 11 Heterográficos | **gap** | — (o termo só aparece no edital transcrito, a00 pág. 3) |
| 11 Heteroprosódicos/heterotônicos | covered | a13 28-30 |
| 11 Heterogenéricos | covered | a13 41-43; a06 25-26 |
| 11 Heterossemânticos | covered | a13 31-40, 44-55 |

## Auditoria inversa (principais achados)
- **Indexada no lugar errado**: questões, listas, gabaritos e textos de leitura classificados como teoria em a00, a08, a09, a10, a11, a14, a15 e a16, e o contrário em a06 e a13 (L/K/B como C; lista de vocabulário como L). Todos corrigidos.
- **Subindexada**: a09, perífrases, voz passiva e "Verbos e tradução livre" (estão no sumário do PDF, faltavam no índice). Subtítulos adicionados.
- **Conteúdo complementar mantido fora do plano (B)**: (1) "Leitura complementar" bilíngue em a01, a02, a04, a05, a07, a08, a10 e a12, que repete a teoria em espanhol; (2) "Textos para treinamento de leitura e tradução" em quase todas as aulas (≈25-30 págs. cada, com questões comentadas de interpretação). Exceção: a leitura complementar de a11 entrou como teoria (conteúdo novo).
- **Possível fora do escopo**: a00 (pontuação, alfabeto); a06 30-54 (vocabulário temático); a13 56-67 (marcadores temporais), que é útil para advérbios e preposições.

## Lacunas e complementos
- `gaps.json` não registra nenhuma lacuna de Espanhol, e a nota de Inglês diz que o material de Espanhol "cobre o edital de forma completa". **Isso não se confirma**: há 2 lacunas (grau do substantivo; heterográficos) e 3 itens rasos de verbos (irregularidade comum × própria; impessoais; pronominais).
- Não existe complemento de Espanhol. Não criei nenhum (o orquestrador decide; ver pedidos).

## Pendências / validação humana
1. Decidir se os "Textos para treinamento de leitura e tradução" (B) devem virar prática de interpretação (C). Contra: alongam muito a Fixação de cada aula. A favor: o item 1 é o mais cobrado pela AOCP.
2. a11 113-118 foi promovido a teoria por julgamento pedagógico: confirmar.
3. a00 ficou `edital: partial`. Se o planejador tratar "partial" como baixa prioridade, a introdução à leitura (págs. 6-8) perde peso.
4. a10 s01/s02 cortam o tópico único "Números cardinais" (25 págs., sem subtítulos). É inevitável com teto de 17.
5. A nota do override de a15 substitui a nota geral ("Prova comentada (somente PDF)") por uma que destaca a banca AOCP.

## Pedidos ao orquestrador
- Atualizar `content/gaps.json` (Espanhol) e a observação do remédio de Inglês: o material de Espanhol tem lacunas.
- Avaliar um complemento curto `esp-complementos` (original) com: grau do substantivo (aumentativos/diminutivos/superlativos sintéticos); heterográficos (ex.: grafias com ll/ñ/z × lh/nh/ç); modelos de irregularidade verbal (comum: e→ie, o→ue, e→i, c→zc, -uir→y; própria: ser, ir, haber, tener, pretéritos fortes); verbos impessoais (fenômenos naturais, haber/hacer impessoais); verbos pronominais (gustar e semelhantes, verbos de mudança).
- Pipeline (opcional): o detector de rótulos de questão ainda deixa passar formatos "ITEM nn" (a16), "QUESTÃO nn" isolado em prova comentada e "Tradução livre"; e não detecta o fim da teoria quando falta o marcador (a09). Nesta disciplina os overrides já resolvem.
