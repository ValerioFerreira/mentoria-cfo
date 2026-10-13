# Análise de questões no padrão AOCP — parcial Q2

- Código: **Q2** · Disciplinas: biologia, estatística, física, informática, matemática, química
- Sementes: 82000 + R (R = nº da rodada) · Atualizado em 2026-10-10
- Método: rodadas de 25 questões sorteadas de todo o banco da fatia (pool = 5.658 questões); cada questão conferida contra o PDF (pageRef) ou recalculada; correções aplicadas direto em `content/items/`.

## Métricas acumuladas

- Rodadas: **6** · Questões auditadas: **150**
- OK (sem achado): **123** (82%) · Com achado: **27** (18%)
- Achados: **27** — CRÍTICO 0 · MAIOR 2 · MENOR 25
- Taxa de gabarito errado: **0/150 = 0.0%**
- Distribuição do gabarito na amostra: A 26 (17%) · B 30 (20%) · C 27 (18%) · D 31 (21%) · E 36 (24%)
- Correta estritamente a mais longa: 40/150 (27%)
- Enunciados com negação: 4; sem destaque em maiúsculas: 1 (25%) (contagem automática por regex, aproximada)
- Explicações com problema: 3/150 (2.0%)

### Por disciplina

| disciplina | questões | com achado | com CRÍTICO |
|---|---|---|---|
| biologia | 34 | 17 (50%) | 0 |
| estatistica | 18 | 4 (22%) | 0 |
| fisica | 15 | 1 (7%) | 0 |
| informatica | 31 | 4 (13%) | 0 |
| matematica | 23 | 0 (0%) | 0 |
| quimica | 29 | 1 (3%) | 0 |

### Por `pattern`

| pattern | questões | com achado | com CRÍTICO |
|---|---|---|---|
| calculo | 41 | 2 (5%) | 0 |
| conceito | 36 | 3 (8%) | 0 |
| caso | 25 | 7 (28%) | 0 |
| correta | 22 | 8 (36%) | 0 |
| relacao | 17 | 5 (29%) | 0 |
| assertivas | 5 | 0 (0%) | 0 |
| incorreta | 3 | 1 (33%) | 0 |
| lacuna | 1 | 1 (100%) | 0 |

## Tabela por rodada

| rodada | questões | OK | críticos | maiores | menores |
|---|---|---|---|---|---|
| 1 | 25 | 17 | 0 | 0 | 8 |
| 2 | 25 | 19 | 0 | 1 | 5 |
| 3 | 25 | 22 | 0 | 0 | 3 |
| 4 | 25 | 22 | 0 | 0 | 3 |
| 5 | 25 | 21 | 0 | 0 | 4 |
| 6 | 25 | 22 | 0 | 1 | 2 |

## Registro de achados

### Q-01 — MENOR — distrator
- Rodada 1, questão 2 · `biologia/a14/s04` #2 · `biologia/a14.json`
- Problema: Distratores B e E absurdos (restritos a 'cupinzeiros', 'vegetais de clareira'), reconhecíveis sem estudar; pág. 45 define bandeira x guarda-chuva.
- Correção: B reescrita como troca de conceito (bandeira com nicho abrangente) e E como 'espécies extintas na natureza'; explicação ajustada.
- Status: corrigido

### Q-02 — MENOR — português
- Rodada 1, questão 13 · `biologia/a07/s03` #4 · `biologia/a07.json`
- Problema: Explicação: 'As alternativas A, B, C e contradizem' — letra E omitida (erro sistemático do gerador).
- Correção: Inserida a letra E.
- Status: corrigido

### Q-03 — MENOR — português
- Rodada 1, questão 19 · `biologia/a13/s02` #13 · `biologia/a13.json`
- Problema: Explicação: 'B, C, D e contêm' — letra E omitida; 'erros marcantes' vago.
- Correção: Inserida a letra E; texto enxugado.
- Status: corrigido

### Q-04 — MENOR — explicação
- Rodada 1, questão 20 · `fisica/a09/s01` #8 · `fisica/a09.json`
- Problema: Explicação cita o valor 80 como erro típico, mas 80 não é alternativa; falta explicar o distrator 2,5.
- Correção: Troca por 'o valor 2,5 vem de considerar só o raio'.
- Status: corrigido

### Q-05 — MENOR — padrão AOCP
- Rodada 1, questão 10 · `estatistica/a06/s01` #11 · `estatistica/a06.json`
- Problema: Alternativa correta traz o esclarecimento '(possíveis)', único parêntese entre as opções (denuncia a correta) e mistura 'totais/possíveis'.
- Correção: Correta passou a 'favoráveis; possíveis'.
- Status: corrigido

### Q-06 — MENOR — padrão AOCP
- Rodada 1, questão 21 · `estatistica/a07/s03` #10 · `estatistica/a07.json`
- Problema: Enunciado truncado/mal formado ('valem, respectivamente, e a distribuição é'); mediana de VA discreta por convenção (1,5), conforme relação moda<mediana<média da pág. 35.
- Correção: Enunciado reescrito: 'Os valores da moda, da mediana e da esperança de X, nessa ordem, e o tipo de assimetria ... são'.
- Status: corrigido

### Q-07 — MENOR — distrator
- Rodada 1, questão 23 · `quimica/c01/s01` #13 · `quimica/c01.json`
- Problema: Correta é a alternativa mais longa (explica '(cloreto de vinila)') — viés de tamanho.
- Correção: Removido o parêntese.
- Status: corrigido

### Q-08 — MENOR — distrator
- Rodada 1, questão 6 · `biologia/a10/s01` #2 · `biologia/a10.json`
- Problema: Distrator A com 'de forma exclusiva' (absoluto que o denuncia) e demais distratores com 'unicamente'; pág. 5.
- Correção: A reescrita sem absoluto ('constituem, juntos').
- Status: corrigido

### Q-09 — MAIOR — fidelidade ao PDF
- Rodada 2, questão 6 · `biologia/a15/s02` #3 · `biologia/a15.json`
- Problema: pageRef 19 aponta a página de leptospirose; o tétano (agente, exotoxina, sintomas) está na pág. 18. Explicação também com marcação *itálico* crua (texto puro no banco).
- Correção: pageRef 19 -> 18; asteriscos removidos.
- Status: corrigido

### Q-10 — MENOR — distrator
- Rodada 2, questão 8 · `biologia/a03/s01` #3 · `biologia/a03.json`
- Problema: Distratores biologicamente absurdos (RNAm 'liga-se covalentemente aos lipídios de membrana'); só D é plausível.
- Correção: E reescrita como troca de papéis entre RNAm e RNAt.
- Status: corrigido

### Q-11 — MENOR — distrator
- Rodada 2, questão 12 · `biologia/a00/s04` #14 · `biologia/a00.json`
- Problema: Quatro distratores absurdos (cloroplastos formando celulose, peroxissomos gerando ozônio, queratina cortical) e a correta é a mais longa; pág. 53.
- Correção: A, B e E trocadas por alternativas plausíveis (vacúolo central, lisossomos, parede de celulose).
- Status: corrigido

### Q-12 — MENOR — distrator
- Rodada 2, questão 15 · `biologia/a08/s02` #4 · `biologia/a08.json`
- Problema: Distratores A e D absurdos ('vapor gasoso', 'novo oxigênio molecular').
- Correção: Reescritos como erros plausíveis (ferro pela bile; transferrina levando bilirrubina aos rins).
- Status: corrigido

### Q-13 — MENOR — português
- Rodada 2, questão 16 · `biologia/a07/s01` #6 · `biologia/a07.json`
- Problema: Explicação: 'As alternativas A, C, D e contradizem' — letra E omitida.
- Correção: Inserida a letra E.
- Status: corrigido

### Q-14 — MENOR — distrator
- Rodada 2, questão 21 · `estatistica/a02/s01` #4 · `estatistica/a02.json`
- Problema: Correta A é de longe a mais longa (traz '10.700' e '3.500'), distratores curtíssimos: viés de tamanho.
- Correção: A -> 'A média aumenta bastante e a mediana permanece a mesma.' (números permanecem na explicação).
- Status: corrigido

### Q-15 — MENOR — explicação
- Rodada 3, questão 8 · `estatistica/a08/s01` #4 · `estatistica/a08.json`
- Problema: Explicação diz que a binomial 'ocorre no primeiro caso', mas a correta é a alternativa B (o primeiro caso é a urna sem reposição, que a própria explicação descarta); correta B também muito mais longa.
- Correção: Explicação aponta a alternativa B; B enxugada.
- Status: corrigido

### Q-16 — MENOR — português
- Rodada 3, questão 19 · `biologia/a13/s03` #8 · `biologia/a13.json`
- Problema: Explicação: 'A, B, C e contêm' (letra E omitida); distratores absurdos (pneus gerando N2O, ozônio em aerossóis).
- Correção: Letra E inserida; distratores mantidos (baixo risco).
- Status: corrigido

### Q-17 — MENOR — português
- Rodada 3, questão 20 · `biologia/a05/s03` #7 · `biologia/a05.json`
- Problema: Explicação: 'A, B, C e trazem' (letra E omitida). Enunciado em formato 'devido a:' com opções iniciadas em maiúscula, diferente do restante do banco.
- Correção: Letra E inserida; formato do enunciado mantido.
- Status: corrigido

### Q-18 — MENOR — português
- Rodada 4, questão 11 · `biologia/a14/s03` #2 · `biologia/a14.json`
- Problema: Explicação: 'As alternativas B, C, D e distorcem' (letra E omitida).
- Correção: Letra E inserida.
- Status: corrigido

### Q-19 — MENOR — português
- Rodada 4, questão 23 · `biologia/a07/s03` #11 · `biologia/a07.json`
- Problema: Explicação: 'As alternativas C, D e trazem' (letra E omitida; também omite B no fecho).
- Correção: Letra E inserida.
- Status: corrigido

### Q-20 — MENOR — distrator
- Rodada 4, questão 10 · `informatica/a09/s02` #11 · `informatica/a09.json`
- Problema: Correta D muito mais longa que as demais (cópia quase literal da frase do material, pág. 29): viés de tamanho.
- Correção: D resumida, mantendo o conteúdo.
- Status: corrigido

### Q-21 — MENOR — português
- Rodada 5, questão 13 · `biologia/a08/s05` #6 · `biologia/a08.json`
- Problema: Explicação: 'As alternativas B, C, D e trazem' (letra E omitida).
- Correção: Letra E inserida.
- Status: corrigido

### Q-22 — MENOR — padrão AOCP
- Rodada 5, questão 15 · `informatica/a06/s01` #6 · `informatica/a06.json`
- Problema: Explicação abre com 'Segundo o material', referência ao material-base que as convenções do projeto vetam fora da Diretriz.
- Correção: Removida a expressão.
- Status: corrigido

### Q-23 — MENOR — padrão AOCP
- Rodada 5, questão 18 · `informatica/a12/s06` #0 · `informatica/a12.json`
- Problema: Enunciado contém 'Segundo o material, ele pode...': referência indevida ao material-base e estilo que não existe em prova.
- Correção: Removida a expressão.
- Status: corrigido

### Q-24 — MENOR — fidelidade
- Rodada 5, questão 21 · `biologia/a17/s02` #9 · `biologia/a17.json`
- Problema: Explicação diz que a vítima de espessura total sente 'dor intensa'; o material (pág. 19) fala em 'vários graus de dor' nas bordas.
- Correção: Trocado por 'algum grau de dor'.
- Status: corrigido

### Q-25 — MAIOR — explicação
- Rodada 6, questão 23 · `informatica/a12/s01` #3 · `informatica/a12.json`
- Problema: Explicação aponta 'a quarta' como a que tem menos de 64 GB livres, mas a quarta (D) é a correta; a falha de 32 GB é da última (E) — explicação contraditória com o gabarito. Enunciado cita 'requisitos ... apresentados no material'.
- Correção: 'a quarta' -> 'a última'; enunciado passa a 'requisitos mínimos do Windows 11'.
- Status: corrigido

### Q-26 — MENOR — português
- Rodada 6, questão 18 · `biologia/a14/s03` #3 · `biologia/a14.json`
- Problema: Explicação: 'As alternativas A, C, D e falseiam' (letra E omitida).
- Correção: Letra E inserida.
- Status: corrigido

### Q-27 — MENOR — português
- Rodada 6, questão 20 · `biologia/a15/s03` #8 · `biologia/a15.json`
- Problema: Explicação com marcação *itálico* crua nos nomes científicos (o banco usa texto puro).
- Correção: Asteriscos removidos.
- Status: corrigido

## Padrões recorrentes e recomendações

(a preencher)
