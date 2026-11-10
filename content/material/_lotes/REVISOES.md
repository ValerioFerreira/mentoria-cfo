# Revisões dos lotes do material próprio

Registro do revisor. Cada rodada revisa os lotes concluídos desde a anterior. O detalhe de cada volume fica no `REVISAO.md` da pasta do volume. Volume DEVOLVIDO volta sozinho no próximo lote do coordenador.

## Lote 1 — revisado em 29/10/2026

| Volume | Decisão | Motivo principal |
| --- | --- | --- |
| lingua-portuguesa/m02 | DEVOLVIDO | contagem fonética errada ("quinhentos", "cantam"); questão IF-MS atribuída à AOCP |
| direito-administrativo/m01 | APROVADO | — |
| legislacoes-pe/m02 | APROVADO | — |
| administracao/m01 | APROVADO | — |

## Lotes 2 e 3 — revisados em 29/10/2026

Os 8 volumes saíram com 0 erros e 0 avisos no validador e nenhum artigo inexistente. Todos foram **APROVADOS**, 5 deles com correções pontuais feitas pelo revisor no próprio texto (listadas no `REVISAO.md` de cada volume). Nenhum volume volta para o autor.

| Lote | Volume | Decisão | O que o revisor corrigiu |
| --- | --- | --- | --- |
| 2 | lingua-portuguesa/m02 (rodada 2) | APROVADO | as 6 correções da rodada 1 conferidas; mais 1 atribuição à AOCP sem fonte e 2 exemplos tirados da fonte |
| 2 | direito-administrativo/m02 | APROVADO | Tema 535 → Tema 531 (dias parados); princípios "implícitos" que estão expressos na Lei 9.784 |
| 2 | legislacoes-pe/m03 | APROVADO | art. 4º da Lei 13.314 não fala de regulamentos militares |
| 2 | administracao/m02 | APROVADO | — |
| 3 | lingua-portuguesa/m03 | APROVADO | *paulista* no sufixo -ita; regra de "mais pequeno"; frase de enchimento; 3 itens atribuídos ao Cebraspe sem fonte |
| 3 | direito-administrativo/m03 | APROVADO | — |
| 3 | legislacoes-pe/m04 | APROVADO | 3 números de artigo errados na LC 470/2021 (competência, carta patente, calendário) |
| 3 | administracao/m03 | APROVADO | — |

**Padrões que voltaram:** número de artigo trocado (o erro mais comum do piloto), item atribuído a banca sem questão real e exemplo copiado de questão da fonte. Foram acrescentados à seção 18 do briefing do autor (`pipeline/briefs/material.md`), que vale para os próximos lotes.

**Ferramenta:** `check_citations.py` passou a ignorar o ADCT ao procurar artigos da CF e a não confundir "art. 2º" com "art. 2º-C".

**Custo informado pelo coordenador:** lote 2 ≈ 45 milhões de tokens (92% em cache), lote 3 ≈ 73 milhões (96% em cache); o volume de LP m03 (8 capítulos) sozinho custou 31,5 milhões.

## Lotes 4 e 5 — revisados em 29/10/2026

| Volume | Decisão | Correções do revisor |
|---|---|---|
| legislacoes-pe/m05 | APROVADO | 6 (Lei 14.751, art. 18, p. único e art. 22; reincidência no Decreto 50.014; art. 93 da Lei 15.187) |
| direito-administrativo/m04 | APROVADO | 3 + 10 frases de tabela em dobro removidas |
| direito-administrativo/m05 | APROVADO | 7 (Súmulas 434, 467, 591, 650 e 651 do STJ; Lei 9.873 nos Estados; convalidação) |
| direito-constitucional/m02 | APROVADO | 2 (Tema 977 sobre celular apreendido; ADPF 130) |
| lingua-portuguesa/m04 | APROVADO | 5 (conector modal, redimir, particípios, 2 alternativas truncadas na Fixação) |
| administracao/m04 | APROVADO | 1 (nota sobre o octante VII de Fiedler) |
| administracao/m05 | APROVADO | 0 |

Padrões novos: súmula citada com o número certo e o conteúdo errado (DA m05, 3 casos); súmula específica apresentada como regra geral (434 é de trânsito, 467 é ambiental); frase de apresentação de tabela em dobro (DA m04). Os três entraram no briefing do autor.

Frentes paralelas: B e C começaram às 18h25 do dia 29/10 na mesma fila do CFOA; as reservas `.frente` não mostraram colisão. A frente B informou que a sessão dela não tem subagentes e escreve os 4 volumes do lote em sequência (mais lenta).

## Frente C, lotes 1 e 2 — revisados em 29/10/2026

| Volume | Decisão | Correções |
|---|---|---|
| lingua-portuguesa/m05 | APROVADO | — |
| direito-administrativo/m06 | DEVOLVIDO | Fixação: 11 questões com o mesmo comentário de modelo (capítulos corretos) |
| administracao/m06 | APROVADO | — (Fixação com frases repetidas e poucas AOCP: melhorar depois) |
| direito-constitucional/m03 | APROVADO | — |
| lingua-portuguesa/m08 | APROVADO | — |
| direito-administrativo/m09 | APROVADO | 3 do revisor (Tema 698, composição do TCU, citação não conferida) |
| direito-constitucional/m11 | APROVADO | — (EC 136/2025 conferida) |
| direito-penal-militar/m06 | DEVOLVIDO | 3 do revisor nos capítulos (art. 291 do CPM dito revogado, insignificância no art. 290, art. 298); Fixação: 8 comentários de modelo |

A frente C escreve rápido (8 volumes em 40 minutos) e acerta as atualizações legislativas recentes (EC 136/2025, EC 139/2026, Lei 14.688/2023), mas os comentários da Fixação saíram de modelo em 2 volumes e a leitura do texto compilado falhou no art. 291 do CPM (a redação antiga aparece marcada como revogada logo antes da nova).

Ferramentas: o validador passou a dar ERRO quando duas questões têm o mesmo comentário e AVISO quando uma frase se repete em 3 ou mais comentários; o aviso de linguagem rebuscada deixou de casar "de escol" com "de escolha" e "plexo" com "complexo".

Frente A: o lote 6 parou às 19h por cota esgotada (RESOURCE_EXHAUSTED); os 4 volumes ficaram como rascunho e voltam como RETOMAR quando a cota renovar (o coordenador estima cerca de 26 h).

## Frente B, lote 1, e volumes prontos da frente C, lote 3 — revisados em 29/10/2026 (21h40)

| Volume | Frente | Decisão | Correções do revisor |
|---|---|---|---|
| lingua-portuguesa/m06 | B | APROVADO | 3 (critério explicativa × causal; frase solta; comentário de tec_508116 com "que" ora objeto, ora sujeito) |
| direito-administrativo/m07 | B | APROVADO | — |
| direito-penal-militar/m02 | B | APROVADO | 3 (agravante da embriaguez do art. 70, II, c; digitação; "acessoriedade limitada" mal aplicada) |
| lingua-portuguesa/m09 | C | APROVADO | 2 (funções em "informar algo a alguém"; quando "à que" leva acento) |
| direito-constitucional/m12 | C | APROVADO | 1 (acumulação do militar estadual: art. 42, § 3º, vale para todo o art. 37, XVI, não só saúde) |

O lote 1 da frente B não fechou: direito-constitucional/m04 continua reservado (`.frente` B) sem capítulos e volta como RETOMAR. O lote 3 da frente C está parado desde 19h13; os dois volumes prontos foram revisados antes do relatório de validação para não esperar. Quando o relatório sair, só faltarão direito-administrativo/m11 e direito-penal-militar/m07.

Padrão novo: afirmação constitucional certa para um grupo e estendida a outro (acumulação das Forças Armadas aplicada aos militares estaduais). Vale para o briefing: conferir sempre se a regra é do art. 42 (estaduais) ou do art. 142 (Forças Armadas).

## Frente B, lote 1 (fechamento) — revisado em 30/10/2026

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-constitucional/m04 | APROVADO | 2 (causa de cancelamento da naturalização antes da EC 131/2023; quem declara a perda no pedido expresso) |

Pendência antes de publicar: conferir o julgamento da ADI 7881 (LC 219/2025, Ficha Limpa) e ajustar a06-s02 se preciso. O coordenador original da frente B não será mais usado; a frente passa a um novo agente com o mesmo identificador (B), que retoma a fila a partir do lote 02.

## Frente B, lote 2 (novo coordenador) — revisado em 30/10/2026

| Volume | Decisão | Correções |
|---|---|---|
| lingua-portuguesa/m10 | APROVADO | 3 do revisor (exemplo de este/aquele com os referentes trocados; exceção de "senhora" na crase; definição de zeugma) |
| direito-administrativo/m12 | APROVADO | 1 do revisor (art. 142, § 3º, VIII); todos os temas do STF que o autor pediu para conferir estão certos |
| direito-constitucional/m17 | APROVADO | 1 do revisor (cargo civil permanente → reserva, salvo acumulação lícita); Emendas 70 e 71/2026 da CE-PE conferidas na Alepe |
| direito-penal-militar/m08 | APROVADO | 1 do revisor: a Súmula 172 do STJ (abuso de autoridade de militar na Justiça comum) estava como vigente; desde a Lei 13.491/2017 é tida como superada (crime militar por extensão) |

O novo coordenador da frente B trabalhou sem subagentes, entregou um lote completo com notas úteis (sinalizou ele mesmo os pontos duvidosos) e deixou o lote 03 com relatório de andamento para retomar. Corrigiu-se no `material_ficha.py` a quebra da reserva quando a pasta da disciplina não existe.

**Correção transversal (EC 138/2025).** O art. 37, XVI, b, da CF passou a ser "um cargo de professor com outro de qualquer natureza" (antes: "técnico ou científico"), conferido no texto compilado. A redação antiga foi corrigida em: direito-constitucional/m12 (a15-s02, correção feita por esta revisão em 29/10), direito-administrativo/m03 (a02-s04), direito-administrativo/m04 (a03-s03) e, no rascunho da frente A, direito-constitucional/m07 (a09-s03 e a09-s04: lei, lista, tabela, esquema e Para fixar; a regra do militar estadual também estava errada e foi reescrita). O m07 continua RASCUNHO, com os erros do validador que já tinha.

## Frente B, lotes 3 e 4 — revisados em 30/10/2026 (fim da tarde)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| lingua-portuguesa/m11 | APROVADO | 1 (exemplos de sotaque trocados entre regiões) |
| direito-administrativo/m13 | APROVADO | 2 (lei da licença-paternidade de 31/03/2026 dada como inexistente; frase contraditória sobre compulsória dos vitalícios) |
| direito-processual-penal-militar/m01 | APROVADO | 0 |
| direitos-humanos/m01 | APROVADO | 1 (conteúdo da Bill of Rights de 1689) |
| direitos-humanos/m02 | APROVADO | 0 |
| direito-processual-penal-militar/m02 | APROVADO | 0 |
| lingua-portuguesa/m12 | APROVADO | 1 (regra de grafia das horas atribuída ao Manual) |
| direito-administrativo/m14 | APROVADO | 0 |

A frente B, com o novo coordenador, entregou 12 volumes em um dia, todos aprovados, com poucos erros e bem sinalizados nas notas. Padrão novo: lei recente que o autor desconhece (licença-paternidade de 2026); entrou no briefing.

## Frentes A, B e C (dois coordenadores) — revisados em 31/10/2026 (manhã)

Lotes: A/lote-06 (retomada), B/lote-05, B/lote-06, B/lote-07, C/lote-04, C/lote-05 e C/lote-06. 23 volumes, todos aprovados.

| Volume | Decisão | Correções do revisor |
|---|---|---|
| lingua-portuguesa/m07 | APROVADO | 1 (duas regras de vírgula atribuídas à Academia Brasileira de Letras sem base) |
| direito-administrativo/m06 | APROVADO (rodada 2) | 0 (Fixação refeita como pedido) |
| direito-administrativo/m08 | APROVADO | 0 |
| direito-administrativo/m11 | APROVADO | 0 (atualizou as cotas para a Lei 15.142/2025) |
| direito-administrativo/m15 | APROVADO | 0 (valores do Decreto 12.807/2025 conferidos) |
| direito-administrativo/m16 | APROVADO | 0 |
| direito-administrativo/m17 | APROVADO | 0 |
| direito-administrativo/m18 | APROVADO | 0 |
| direito-administrativo/m19 | APROVADO | 0 |
| direito-constitucional/m07 | APROVADO | 0 (correções da EC 138/2025 preservadas) |
| direito-penal-militar/m04 | APROVADO | 0 |
| direito-penal-militar/m06 | APROVADO (rodada 2) | 3 (cópia do art. 298 vinda da própria correção da rodada 1; art. 302 com "permanecer"; comentário do art. 408 com hipótese inventada) |
| direito-penal-militar/m07 | APROVADO | 0 |
| direito-processual-penal-militar/m03 | APROVADO | 0 |
| direito-processual-penal-militar/m04 | APROVADO | 1 (quadro sobre Juiz-Auditor × juiz federal da Justiça Militar, Lei 13.774/2018) |
| direitos-humanos/m03 | APROVADO | 0 (Lei 12.528/2011 conferida) |
| direitos-humanos/m04 | APROVADO | 0 |
| raciocinio-logico/m01 a m05 | APROVADO | 0 (contas dos lemas de Kaplansky refeitas) |
| direito-constitucional/m01 | APROVADO | 0 (onda 2) |

Observações: (1) as retomadas da frente A saíram em 7 a 17 minutos por volume; a leitura por amostra não achou erro de conteúdo, mas o relatório de DC m07 descreve temas que não estão nos capítulos (o conteúdo está certo). (2) Três padrões novos entraram na seção 18 do briefing. (3) O conferidor de citações segue com falsos "inexistentes" quando o capítulo cita artigos de duas normas (Lei 14.133 e CP; CPPM e CF).

Fonte dos valores de 2026: [Decreto 12.807, de 29/12/2025 (Câmara dos Deputados)](https://www2.camara.leg.br/legin/fed/decret/2025/decreto-12807-29-dezembro-2025-798615-norma-pe.html).

## Frente B lote 8 e frente C lote 7 — revisados em 31/10/2026 (manhã)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-administrativo/m20 | APROVADO | 1 (quadro de jurisprudência colado a um parágrafo, sem tribunal no título; acrescentado o Tema 1.118 do STF, de 2025) |
| direito-administrativo/m21 | APROVADO | 0 |
| raciocinio-logico/m06 | APROVADO | 0 (contas de probabilidade total e Bayes refeitas) |

Ferramenta: `validate_material.py` passou a dar ERRO quando um `> [!...]` está no fim de um parágrafo (o quadro não renderiza); nenhum outro volume tem o problema.

## Frente B lote 9 e frente C lote 8 — revisados em 31/10/2026 (tarde)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-administrativo/m22 | APROVADO | 4 (6 remissões ao "texto de apoio" trocadas pela decisão conferida das ADIs 7156 e 7236; prescrição intercorrente atualizada: o prazo recomeça por oito anos) |
| direito-administrativo/m23 | DEVOLVIDO à frente C | 15 itens: volume escrito sem o julgamento das ADIs 7156 e 7236 (intercorrente de quatro anos, art. 21, § 4º, oitiva do Tribunal de Contas no ANPC), três quadros de lei com texto inexistente, art. 13 pela redação revogada, ordem de preferência da indisponibilidade invertida, dispositivos trocados (17-C × 12, § 1º, e 18, § 4º), súmulas do STJ inexistentes |

O STF concluiu em 1º/7/2026 o julgamento de mérito das ADIs 7156 e 7236 sobre a Lei 14.230/2021. Fontes: [notícia do MPF](https://www.mpf.mp.br/o-mpf/unidades/procuradoria-geral-da-republica-pgr/noticias/supremo-segue-mpf-ao-analisar-acoes-contra-nova-lei-de-improbidade-administrativa) e [resumo do julgamento](https://blog.mege.com.br/lei-de-improbidade-administrativa-adis-7156-7236/). Cassação de aposentadoria: [STJ, Informativo 870](https://informativos.trilhante.com.br/julgados/stj-processo-em-segredo-de-justica-v49).

Ferramenta: `validate_material.py` passou a acusar "texto de apoio", "material de apoio" e "texto-base". A varredura achou só um caso já aprovado, em direito-constitucional/m03 (a03-s03, quadro sobre a extradição), corrigido pelo revisor.

Onda 1: 70 de 71 aprovados; falta só direito-administrativo/m23, de volta à frente C como CORRECAO.

## Frente B lote 10 e frente C lotes 9, 10 e 11 (parte) — revisados em 31/10/2026 (noite)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-administrativo/m23 (rodada 2) | APROVADO | 2 (quadro do art. 16, § 11, com incisos que a lei não tem; quadro do art. 17-C, § 2º, com redação inexistente, agora literal e com a leitura do STF) |
| direito-constitucional/m05 | APROVADO | 3 (Tema 272, e não 247; ADI 2240, e não 2248; corte de energia: jurisprudência dividida entre a ADI 5798 e a ADI 5961) |
| direito-constitucional/m06 | APROVADO | 1 (quadro do art. 24, § 4º, literal) |
| direito-constitucional/m08 | APROVADO | 1 ("\n" literal no fim de 4 capítulos) |
| direito-constitucional/m09 | APROVADO | 0 |
| direito-administrativo/m10 | APROVADO | 1 (Tema 366 é o RE 136.861) |
| direito-penal-militar/m03 | DEVOLVIDO à frente C | 20 quadros [!lei] com paráfrase no lugar do texto legal (o conteúdo está certo) |
| direito-penal-militar/m05 | APROVADO | 2 (quadros dos arts. 222 e 225 literais; "Supremo Tribunal Federal") |
| biologia/m01, m02, m04 | APROVADO | 0 |
| biologia/m03 | APROVADO | 1 ("\n" literal) |
| estatistica/m01 e m02, fisica/m02 | APROVADO | 0 (exercícios resolvidos refeitos por amostra) |

Fontes conferidas: [Tema 1200 do STF (TRF1, Boletim NUGEPNAC 21/2023)](https://www.trf1.jus.br/trf1/conteudo/files/Boletim%20NUGEPNAC%2021%202023.pdf), [Tema 272 do STF](https://informativos.trilhante.com.br/temas-stf/tema-272-stf), [Tema 366 do STF](https://informativos.trilhante.com.br/temas-stf/tema-366-stf), [ADI 5798 (Tocantins, corte de energia)](https://www.sedep.com.br/?p=125911).

Ferramentas:
- `validate_material.py` passou a comparar cada `[!lei]` com a norma em cache (`pipeline/leis.py`) e dá ERRO abaixo de 60% de coincidência. O motivo: o quadro fica fora da checagem de originalidade, então paráfrase dentro dele é texto "de lei" falso e poderia esconder cópia do material-base. **A varredura achou 91 quadros parafraseados em 24 volumes já aprovados** (DA m01, m05, m06, m07, m09, m11, m14, m15, m16, m21, m22; DC m01, m03, m07, m11, m12; DPM m02, m04, m06, m07; DPPM m03; DH m01, m03; LegPE m04). Eles aparecem como erro no `--all` e precisam de uma rodada de correção mecânica (transcrever o dispositivo ou tirar a paráfrase do quadro): decisão do dono sobre quem faz.
- `check_citations.py`: a frente C tinha alterado a ferramenta de modo que artigos inteiramente revogados passavam como vigentes. Agora eles aparecem como "REVOGADO" (sem contar como erro), para o revisor conferir se o texto os trata como revogados.
- Briefing, seção 18: dois padrões novos (paráfrase dentro de `[!lei]`; número de precedente trocado).

Onda 1 (CFOA): 71 de 71 aprovados. Onda 2: 14 aprovados; direito-penal-militar/m03 devolvido; C/lote-11 segue com fisica/m01 em produção (DC m08, biologia/m03 e estatistica/m01 desse lote já foram revisados).

## Frente B lotes 11 e 12 — revisados em 31/10/2026 (noite)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-constitucional/m13 | APROVADO | 1 (a equidade no custeio vale para toda a seguridade, não só para a previdência: art. 195, § 9º) |
| direito-constitucional/m15 | APROVADO | 0 |
| biologia/m06 e m08 | APROVADO | 0 |
| estatistica/m04 e m06 | APROVADO | 0 (exercícios refeitos por amostra) |
| fisica/m03 e m05 | APROVADO | 0 (exercícios refeitos por amostra) |

Os 8 volumes passam na nova checagem dos quadros [!lei]. Duas questões do banco com gabarito suspeito, descartadas pelos autores, merecem revisão em /admin/revisao: tec_2052701 (variância) e tec_3140993 (entropia na isotérmica).

## Frente C lotes 11, 12 e 13 (parte) — revisados em 31/10/2026 (noite)

| Volume | Decisão | Correções do revisor |
|---|---|---|
| direito-penal-militar/m03 (rodada 2) | APROVADO | 1 (§ 6º do art. 125 completado no quadro de lei) |
| direito-constitucional/m10 | DEVOLVIDO à frente C | escrito pela redação anterior à EC 103/2019: remoção por interesse público exige maioria absoluta (não dois terços) e a aposentadoria compulsória como sanção saiu da Constituição (art. 93, VIII, e art. 103-B, § 4º, III; hoje só na LOMAN) |
| direito-constitucional/m14 | APROVADO | 0 |
| biologia/m05 e m07 | APROVADO | 1 cada (colo do fêmur; válvulas das veias) |
| estatistica/m03 | APROVADO | 1 (acentos) |
| fisica/m01 | APROVADO | 0 |

estatistica/m05 (C/lote-13) estava em produção na hora da revisão e fica para a próxima rodada. Os relatórios da frente C deixaram de trazer a seção de validação; o observador agora também confere os volumes pelo status, não só pelos relatórios.

## Frente C lotes 12 a 17 — revisados em 01/11/2026 (madrugada)

17 volumes, todos aprovados: direito-constitucional/m10 (rodada 2) e m16; biologia/m09 a m12; estatistica/m05 e m07 a m10; fisica/m04, m06 e m07; informatica/m01 e m02; lingua-espanhola/m01.

Correções do revisor: estatistica/m10 (notação por extenso trocada por símbolos: μ, σ, λ, ×, %, cerca de 400 ocorrências) e direito-constitucional/m16 (ressalva dos embargos de declaração no art. 26 da Lei 9.868/1999). Os 17 passam no validador, nos quadros [!lei] e no conferidor de citações; as contas conferidas por amostra estão certas.

lingua-espanhola/m02 (lote 17) estava em produção.

### Avaliação das frentes A e C (01/11/2026)

| | Frente A | Frente C |
|---|---|---|
| Volumes entregues | 19 (lotes 02 a 06, de 29/10 a 31/10, 00h37) | 51 (de 29/10 até agora; 17 só entre 18h e 0h de 31/10) |
| Situação | parada há cerca de 23 h (lote 6 interrompido por cota; retomadas concluídas às 00h37 de 31/10) | ativa, ritmo de ~20 min por volume |
| Devolvidos | 0 de 19 | 5 de 51; todos jurídicos (5 de 20 jurídicos = 25%; 0 de 31 nas demais matérias) |
| Correções do revisor | 37, em 12 dos 19 volumes (mais em DA m05 e LegPE m05) | 31 em 17 volumes, a maioria de forma (\n literal, acentos, notação) |
| Quadros [!lei] parafraseados nos aprovados | 5 | 62 (de 91 no total) |
| Erros jurídicos graves | nenhum | DA m23 (STF de 2026 ignorado, quadros de lei inventados, súmulas inexistentes), DC m10 (redação anterior à EC 103/2019), números de precedentes trocados |
| Ferramentas | sem alterações | alterou o conferidor de citações (revogados passavam como vigentes; desfeito); deixa scripts em pipeline/ (make_fix_inf02.py); relatórios sem a seção de validação |

lingua-espanhola/m02 (C/lote-17): APROVADO em 01/11/2026, sem correções.

**Decisão do dono (01/11/2026):** a correção dos 91 quadros [!lei] parafraseados nos volumes já aprovados fica para depois. Até lá eles seguem APROVADOS e aparecem como erro em `validate_material.py --all`; volumes novos já precisam passar na checagem.

## Frente C lotes 18 a 25 — revisados em 01/11/2026 (tarde)

26 volumes da onda 2, todos da frente C, feitos entre 0h e 8h30 de 01/11. A frente A ainda não começou (sem lote 07); matematica/m04 (C) estava em produção e não foi tocada.

| Decisão | Volumes |
|---|---|
| APROVADO (13) | estatistica/m11 e m13; informatica/m03, m05, m08, m09, m10; lingua-espanhola/m05; lingua-inglesa/m03; matematica/m02 e m03; quimica/m02 e m03 |
| DEVOLVIDO à frente C (13) | estatistica/m12; informatica/m04, m06, m07; lingua-espanhola/m03, m04, m06; lingua-inglesa/m01, m02, m04; lingua-portuguesa/m01; matematica/m01; quimica/m01 |

**Motivo das devoluções: remissão ao material-base.** O texto dizia "Na página 9 do manual de referência", "Ponto de Atenção da Página 22", "Exemplo da página 58" e "(Fonte, pág. 36)". Em `fontes`, citava "Apostila Base MentorIA …" e "Apostila teórica Aula NN — MentorIA", que é o material-base com outro nome. Em informatica/m07, por exemplo, são 23 ocorrências; em lingua-portuguesa/m01, 27. O conteúdo desses 13 volumes será lido na rodada 2.

**O mesmo problema em 5 volumes já aprovados**, corrigidos pelo revisor (o status não mudou): biologia/m03 e m12, estatistica/m10, informatica/m02 e lingua-espanhola/m02. No Espanhol m02, os exemplos eram os do material-base e foram trocados por exemplos próprios.

**Outras correções:**
- **Matemática em ASCII** ("x_barra", "mu_0", "sigma^2", "raiz(n)", "chi2"), convertida para Unicode em 12 volumes: estatistica/m01, m02, m08, m09, m10, m11 e m13; fisica/m04 e m05; matematica/m01; raciocinio-logico/m06.
- **Cifrão falso "＄"** trocado pelo "$" em 4 volumes.
- matematica/m01: frase errada sobre o orçamento ("quase todo executado" com 42% de saldo).

**Ferramentas:**
- `validate_material.py` passou a dar ERRO para:
  - remissão ao material-base por página, aula, "fonte teórica", "material/manual de referência" e "(Fonte, pág.)";
  - fonte com "apostila", "aula NN" ou "Estratégia";
  - matemática em ASCII nas disciplinas de cálculo.
- Deixou de confundir "R$" e referências de planilha com LaTeX.
- Os casos legítimos de Informática ("imprimir as páginas 1 a 4", "Slide 3 de 12") não são acusados.
- Briefing de autores, seção 18: três padrões novos.

**Frente C, avaliação atualizada:** fora do Direito, as contas e os conceitos conferidos estão certos. Mas metade dos volumes da madrugada citava páginas e uma "apostila" do material-base. Isso indica que o autor redige a partir do texto-fonte com os marcadores à vista e precisa reler o próprio texto antes de entregar.
