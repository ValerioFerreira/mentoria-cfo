# Revisão final G3 — Inglês, Espanhol, Estatística, Direito Penal Militar

## Estado final
- Validador nos 51 arquivos do grupo: **0 erros** (antes: 9 arquivos com erro, 24+ "Para fixar" inválidos em Inglês e 1 em DPM).
- 4 entregas rejeitadas do Espanhol (S0319, S0351, S0402, S0443) corrigidas em `resumos-colaboradores/entregas/`; `import_agent_summaries.py --dry-run`: 4 válidos, 0 rejeitados. Não foi gravado no content (importação real fica com o orquestrador).
- A classificação de cobertura é relativa (sempre sobra uma faixa REVISAR/ATENÇÃO). Final: Inglês REVISAR 3/ATENÇÃO 3; Espanhol REVISAR 4/ATENÇÃO 5; Estatística REVISAR 9/ATENÇÃO 12 (inalterada); DPM REVISAR 4/ATENÇÃO 5 (inalterada).

## A) Para fixar
- Inglês: todos os trechos (a00 a a06, c01) com 5–8 itens (itens 5º acrescentados; parágrafos de a00/s01, a00/s02, a03/s02, c01/s01 viraram listas).
- DPM a08/s01: 5º item acrescentado.

## B) Trechos reescritos ou ampliados (analítico e, em Inglês, sintético)
Inglês (reescrita completa, com tabelas e pontos cobrados; sintéticos antes genéricos): a00/s01 (S0260), a01/s01 (S0269), a01/s03 (S0291), a01/s04 (S0301), a01/s05 (S0292), a02/s02 (S0264), a03/s01 (S0286), a03/s02 (S0259), a04/s03 (S0305), a06/s01 (S0270).
Espanhol (seções acrescentadas): a01/s01 (S0274), a01/s02 (S0326), a05/s01 (S0315), a05/s02 (S0285), a06/s01 (S0332), a09/s05 (S0297), a11/s01 (S0307), a11/s02 (S0296).
Estatística: ver segunda rodada (todos os REVISAR relidos; correções mínimas em a01/s02 e a10/s04).
DPM: leitura de a00/s01, a00/s02, a09/s02, a09/s05; conteúdo denso (razão 0,8–0,9), sem alteração.
Vereditos antes→depois (Inglês): REFAÇÃO a01/s04, a01/s05 → OK; REVISAR a04/s03 → OK. Espanhol REFAÇÃO a01/s02, a05/s02, a05/s01, a11/s01 → ATENÇÃO/REVISAR/OK (as palavras que "faltam" são do vocabulário dos textos de prática).

## C) Entregas Espanhol
S0319 (preposições, ampliado e lista de 23 preposições reordenada), S0351 (divergências léxicas, ampliado), S0402 (exemplos trocados), S0443 (exemplo numérico trocado, escalas billón/trillón explicadas).

## Segunda rodada (Inglês completo, releitura de Estatística e DPM)
- Inglês: os 13 trechos pendentes foram reescritos (analítico com tabelas, regras e pegadinhas da fonte; sintético concreto): a00/s02, a01/s02, a02/s01, a02/s03, a02/s04, a04/s01, a04/s02, a05/s01, a05/s02, a05/s03, a05/s04, a06/s02, a06/s03; c01/s01 (complemento) teve o sintético refeito. Com isso os 23 trechos de Inglês estão no novo padrão. Mediana da nota de cobertura: 0,29 -> 0,43. O veredito é relativo (sempre sobra uma faixa REFAÇÃO/REVISAR); o que restou (a05/s02, a06/s01, a01/s04, a04/s01) tem "faltam" formados por traduções e nomes dos exemplos, não por conteúdo gramatical omitido.
- Estatística: relidos contra a fonte a02/s01, a02/s05, a03/s03, a04/s03, a06/s04 e a06/s05 (além de a00/s03, a01/s02, a10/s04 na primeira rodada). Fórmulas, exemplos numéricos e pegadinhas conferem com o material; nenhum erro encontrado. A nota baixa vem de valores numéricos dos enunciados.
- DPM a09/s02 relido contra a fonte (penas, causas de aumento e redução, §§ 3º-A, 4º, 5º, 6º do art. 209; arts. 210 a 213): confere. Sem alteração.
- Validador final: 51 arquivos, 0 erros. Dry-run das 4 entregas do Espanhol: 0 rejeitados.

## Pendências
- Nenhuma de conteúdo no grupo. Os trechos de Espanhol a00/s01 e a01/s02 seguem com cobertura baixa por vocabulário dos textos de leitura.
- Cuidado ao escrever: o validador acusa "todo:" (ex.: "método:"), "preencher" e trechos curtos copiados somando mais de 40 palavras (trocar exemplos em inglês por exemplos próprios).

## Dúvidas para revisão humana
1. Inglês a06/s01: o material diz que *a slap on the wrist* é punição severa; o consenso é punição leve (resumo registra o consenso). Material também traduz *stop yanking my chain* de forma incorreta (omitido).
2. Inglês a04/s03: o material classifica *Where are you going?* como futuro; gramaticalmente é present continuous (com valor de futuro próximo).
3. Inglês a01/s01: compostos com hífen (*mothers-in-law*) acrescentado por conhecimento gramatical, não está no material.
4. Espanhol a05/s02: exemplos do material usam subjuntivo após *a lo mejor*; a norma pede indicativo (resumo segue a norma).
5. Espanhol a05/s01: "apenas" como falso amigo (mal, quase não / assim que), acrescentado; a09/s05: quadro das 22 formas conferido com o material, mas terminações de futuro de subjuntivo são de uso restrito.
6. Espanhol a11/s02 e S0443: tabela do material grafa *trillón* como 10^15 (correto 10^18) e traz *decimosegundo* no feminino.
7. DPM a00/s01: posição STM × STF sobre "atividade" no art. 9º, II, a; decisão do TJM-SP sobre viatura como lugar sujeito à administração militar.
8. DPM a00/s02: "posição unânime hoje" sobre civil agressor de militar em GLO; Lei 14.688/2023 e nova redação do art. 9º, III, b.
9. DPM a09/s05: lista de crimes do CPM incluídos na Lei 8.072/1990 pela Lei 14.688/2023, aumento do art. 237 e concurso homicídio + vilipêndio a cadáver; confirmar contra o texto vigente.
10. Figuras (cartuns, infográficos, gráficos do Estatística) não reconstruídas; resumos usam o texto que descreve as figuras.
