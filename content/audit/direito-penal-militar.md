# Auditoria estrutural: Direito Penal Militar

Escopo: aulas a00 a a11 (12 PDFs, 504 páginas). Foram varridas todas as páginas com `--heads`, e lidas as páginas suspeitas (limites de aula, cortes propostos, aulas curtas, páginas T com marcas de questão). Nenhum texto do PDF foi copiado para `content/`.

## Números

| | Antes | Depois |
|---|---|---|
| Páginas de teoria | 289 | 287 |
| Trechos de Teoria | 30 | 34 |
| Trechos com corte no meio de tópico | 7 | 0 |
| Menor trecho | 2 págs. (a03/s02) | 2 págs. (a06/s01, aula inteira) |
| Maior trecho | 14 págs. | 13 págs. |

Teto de 17 págs.: sem violações. JSON dos três arquivos válido; `segment.py --subject direito-penal-militar` rodado por último.

## Correções feitas (`content/overrides/direito-penal-militar.json`)

| Aula | Correção | Motivo |
|---|---|---|
| a03 | págs. 10-11 viraram LIST | "Lista de Questões" estava marcada como T e gerava um trecho de teoria de 2 págs. (sem conteúdo). Aula passa a ter só o trecho 3-7. |
| a00 | cortes em 15, 24, 30 (+ títulos) | O art. 9º ficava dividido no meio. Agora: 3-14 (conceito, arts. 1-8, art. 9º caput, I e II), 15-23 (art. 9º, III), 24-29 (§§ do art. 9º, Lei 13.491/2017, Júri e GLO), 30-36 (arts. 10 a 28). |
| a04 | cortes em 9, 19, 25 (+ título em 19) | Antes: 3-13 misturava Penas Principais com início de Aplicação, e 14-24 começava no meio de atenuantes. Agora: Penas principais (3-8), Dosimetria (9-18), Concurso de crimes e unificação (19-24), Sursis e livramento (25-32), Acessórias e efeitos (33-43). |
| a08 | cortes em 9, 19, 26, 37, 47 (+ 9 títulos de capítulo) | A teoria de 52 págs. tinha três cortes no meio de tópico. Agora cada trecho segue capítulos do CPM: Segurança externa (3-8), Motim a violência contra superior (9-18), Desrespeito e insubordinação (19-25), Usurpação, resistência e fuga de presos (26-36), Insubmissão e deserção (37-46), Crimes em serviço e comércio (47-54). |
| a09 | cortes em 11 e 43 | O trecho de crimes sexuais (35-44) engolia o início do furto e o seguinte começava em "Furto atenuado". Agora: Homicídio e genocídio (3-10), Lesão, rixa e periclitação (11-19), Honra (20-27), Liberdade (28-34), Sexuais, ofensa às FA e duelo (35-42), Patrimônio (43-55). Também separa o homicídio (tema mais cobrado) do resto de 14 págs. |
| a10 | cortes em 22 e 30 (+ título em 22) | Administração Militar tinha corte no meio e a Justiça Militar (5 págs.) ficava colada no fim dela. Agora: Incolumidade (3-11), Peculato, concussão, corrupção, falsidade (12-21), Prevaricação e demais crimes funcionais (22-29), Administração da Justiça (30-34). |
| a11 | corte em 14 | O corte antigo (pág. 12) partia o capítulo "Da inobservância do dever militar" (págs. 10-14). Agora: 3-13 e 14-21 (a partir de "Do Dano"). |

Sem alteração: a01 (3-15 e 16-28 já separam fato típico/ilicitude de culpabilidade), a02, a05, a06, a07. Nenhuma aula foi marcada `edital: no`: todas as 12 aulas correspondem a itens do edital (1 a 10). Nenhuma aula é só prova.

## Aulas minúsculas: os trechos fazem sentido?

- a02 (7 págs.), a05 (5), a06 (2), a03 (5 depois da correção): a teoria é completa para o que o CPM trata (a05: arts. 110-113; a06: arts. 121-122; a03: arts. 53-54). Não há teoria faltando nas páginas C/L: todas as páginas C começam em "Questões Comentadas" ou comentários de questão.
- Como o planejador só junta trechos curtos da mesma aula, a06 (2 págs.) e a03/a05 (5 págs.) viram atividades de Teoria isoladas e curtas. Ver pedido ao orquestrador (agrupar a02+a03 e a05+a06).
- a07 (11 págs.) está bem como trecho único (extinção e prescrição). Poderia separar as págs. 3-4 (rol de causas) das 5-13 (prescrição), mas o ganho é pequeno.

## Cobertura do edital

| Item | Status | Onde |
|---|---|---|
| 1 Aplicação da lei penal militar | covered | a00 3-36 (lei no tempo 4-6, lugar 6-7, crime militar/art. 9º 8-23, §§ 24-29, arts. 10-28 em 30-36) |
| 2 Do crime | covered | a01 3-28 |
| 3 Imputabilidade penal | covered | a02 3-9 |
| 4 Concurso de agentes | covered | a03 3-7 |
| 5 Das penas | covered | a04 3-43 |
| 6 Medidas de segurança | covered | a05 3-7 |
| 7 Ação penal | covered | a06 3-4 (2 págs.) |
| 8 Extinção da punibilidade | covered | a07 3-13 |
| 9 Crimes em tempo de paz | partial | a08 (segurança externa, autoridade/disciplina, serviço/dever militar: completos), a09 (pessoa e patrimônio: parcial), a10 (incolumidade: parcial; administração militar: completo; justiça militar: parcial) |
| 10 Crimes em tempo de guerra | partial | a11 3-21 |
| 11 Súmulas e jurisprudência dominante | partial | diluída em ementas (a00, a01, a04, a08, a10) |

Mapa detalhado, item a item: `content/edital/direito-penal-militar.json`. Não há lacunas em `content/gaps.json` nem complementos para esta disciplina.

## Atualização legislativa

- **Lei 14.688/2023 (minirreforma do CPM):** refletida de forma ampla. Há comparação "redação anterior × nova" em arts. 50, 77, 110, 121-122, 124-125, 232-237, 240, 290, entre outros, e menção à revogação dos arts. 78 e 233. Estupro/atentado ao pudor, hediondez (Lei 8.072, art. 1º, par. único, VI), reabilitação (retirada), graça e perdão judicial estão presentes.
- **Lei 13.491/2017 (crimes militares por extensão):** presente em a00 págs. 12-29 (art. 9º, II, e §§ 1º e 2º, com ementas do STM/STF). Adequado.
- Conferido: o § 1º do art. 9º, na redação da 14.688/2023, aparece como vetado (a00, págs. 24-25), e o texto da 13.491/2017 segue valendo.
- A a11 (tempo de guerra) não menciona a Lei 14.688/2023 em nenhum ponto.

## Auditoria inversa

| Aula/págs. | Classe | Observação |
|---|---|---|
| a03 10-11 | indexada no lugar errado | Lista de questões marcada como T. Corrigida. |
| a00 23; a01 22-23 | conteúdo complementar | Questões comentadas embutidas na teoria. Mantidas (não dá para cortar por página). |
| a02 9 | indexada no lugar errado | Art. 47 (elementos não constitutivos) é de "Do crime". Sem impacto. |
| a09 32 e 42-43 | superfragmentada | Art. 224 (duelo) explicado duas vezes. Mantido. |
| a09 37 | conteúdo complementar | Digressão ECA art. 240 × estupro. |
| a11 19-21 | já corretamente indexada | Caso histórico (FEB, 1945) que ensina os arts. 400 e 408. |
| a08 3-8 | já corretamente indexada | Segurança externa: baixo rendimento previsto, mas é item do edital. |
| a04 31; a03 10 | extração de texto | Títulos "não localizados" por palavras coladas na extração; não afetam as páginas. |

Nenhuma teoria perdida em páginas C/L/S/F/B e nenhum gabarito/lista dentro de trecho de teoria, exceto a03 10-11 (corrigido).

## Pendências

1. **P1, item 11 do edital (súmulas e jurisprudência).** Não há trecho dedicado. Existem ementas dentro de cada tema e citações isoladas: Súmula 711 STF (a00, lei no tempo; a08), SV 11 (a01), Súmulas 231, 241 e 269 do STJ (a04), Súmula 75 do STJ (a08 pág. 34), Súmula 14 do STM (a10 pág. 4). Faltam as súmulas de competência entre Justiça Militar e comum, que são as mais cobradas. Candidatas a conferir no texto oficial, sem verificação por mim: STJ 6, 53, 78, 90 e 172; STF 297 e 298. Recomendação: complemento autoral "Súmulas e jurisprudência de Direito Penal Militar", parafraseado a partir das fontes oficiais. Decisão do orquestrador.
2. **P2, art. 9º, § 1º (a00 págs. 24-25).** O material trata a redação da 14.688/2023 como vetada. Confirmar se o veto (Veto nº 26/2023) foi mantido ou derrubado, no site do Congresso, antes de fechar a questão.
3. **P3, art. 408 do CPM (a11 pág. 20).** O dispositivo remete aos arts. 232 e 233, e o art. 233 foi revogado pela Lei 14.688/2023. Pelas fontes públicas consultadas, o art. 408 não foi reescrito pela lei. Conferir o texto consolidado do Planalto e a doutrina sobre a leitura atual (provavelmente o art. 232).
4. **P4, art. 232, § 3º (a09 págs. 35-37).** A ADI 7555 (PGR) e a Recomendação 25/2024 da CCR/MPM questionam o § 3º do art. 232 (estupro de vulnerável sem a qualificadora de lesão grave). O material não menciona. Relevância baixa para o CBMPE; só registrar.
5. **P5, partes especiais sem teoria** (busca textual; confirmar contra o CPM oficial):
   - a09, contra a pessoa: arts. 226 a 231 e 238 a 239.
   - a09, patrimônio: arts. 245 a 253 e 257 a 267 (estelionato, apropriação indébita, dano e afins).
   - a10, incolumidade pública: os demais artigos do capítulo (268 a 289 e 292 a 297); o professor declara que só vale o art. 290 e o 291.
   - a10, administração da justiça: denunciação caluniosa, falso testemunho, fraude processual e outros (arts. 343 a 348, 351, 352 e 354).
   - a11, guerra: arts. 398, 399 e 401 a 407.
   Decisão do orquestrador: aceitar a escolha do professor ou pedir complemento. A AOCP cobra o texto da lei, então o risco existe, mas o volume esperado de questões é pequeno.
6. **P6, a11 e a Lei 14.688/2023.** Não verifiquei se a lei alterou algum dispositivo do tempo de guerra além da remissão do art. 408. Conferir o texto consolidado.
7. **P7, tabelas e figuras.** A tabela de embriaguez (a02 págs. 5-7) e as tabelas de prescrição (a07 pág. 6) saem fragmentadas na extração de texto. O PDF está correto; vale uma olhada humana na página se o aluno reclamar de lacuna.

## Pedidos ao orquestrador

- Permitir que o planejador junte trechos curtos consecutivos de aulas diferentes da mesma disciplina, sugerindo os pares a02+a03 (12 págs., Imputabilidade e Concurso de agentes) e a05+a06 (7 págs., Medidas de segurança e Ação penal). Isso evita atividades de Teoria de 2 a 5 págs.
- Decidir P1 (complemento de súmulas) e P5 (complementos de partes especiais).
- Sem mudanças de código ou arquivos globais necessárias.
