# Lote 01 — Frente B (produção contínua)

Início: 2026-10-29 18:25

| Tipo | Volume | Título | Autor |
|---|---|---|---|
| NOVO | lingua-portuguesa/m06 | Sintaxe da oração e do período | AGENTE-MATB-01 |
| NOVO | direito-administrativo/m07 | Atos administrativos II | AGENTE-MATB-02 |
| NOVO | direito-constitucional/m04 | Direitos sociais, nacionalidade, direitos políticos e partidos | AGENTE-MATB-03 |
| NOVO | direito-penal-militar/m02 | Crime militar, imputabilidade e concurso de agentes | AGENTE-MATB-04 |

Seleção (uma única execução, volumes reservados com `.frente`):
`material_ficha.py --lote 4 --frente B`.

Observação de infraestrutura: esta sessão não tem a ferramenta de subagentes (só há agente de
pesquisa na web). Os quatro autores rodam na mesma sessão, um volume de cada vez, na ordem da
seleção.

## lingua-portuguesa/m06 — Sintaxe da oração e do período

Entrega em 29/10/2026 (fim do volume). Validação: 0 erros, 3 avisos.

- `a05-s04.md` cobertura 0,59: os termos que faltam são tokens colados ao número da página no
  texto-fonte (`3que`, `5nem`, `2cheguei`). O conteúdo dos tópicos está coberto.
- `a05-s06.md` cobertura 0,60.
- `a05-s05.md`: uma coincidência de 10 palavras em uma frase de exemplo de paralelismo (limite
  de aviso; nenhuma sequência de 16).
- `fixacao.json`: 20 questões, 18 AOCP, mínimo de 2 por capítulo cumprido; duas candidatas do
  banco (tec_2052533, tec_3558197) foram trocadas por questões de gabarito mais seguro.
- `check_citations.py`: 0 citações, 0 inexistentes.

Notas dos autores: o material-base trata “oração modal” como categoria não oficial, e o texto
segue essa ressalva; a nomenclatura de “complemento de objeto indireto” em tec_508116 foi
explicada pelo papel do termo em relação ao verbo. Sem dúvidas pendentes para revisão humana.

Ferramentas: sem subagentes nesta sessão, os capítulos foram escritos e revalidados pelo próprio
coordenador; duas rodadas de correção no capítulo 5 (expressão proibida e coincidências com a
fonte) e uma no capítulo 6 (tamanho, quadros e cobertura).

Custo: cerca de 1 h de sessão, com reexecução após queda; sem tokens de subagentes a registrar.

## Situação do lote 01

- `lingua-portuguesa/m06` — **entregue** (PRONTO_PARA_REVISAO).
- `direito-administrativo/m07` — **entregue** (PRONTO_PARA_REVISAO).
- `direito-constitucional/m04` — **entregue** (PRONTO_PARA_REVISAO, 7/7 capítulos).
- `direito-penal-militar/m02` — **entregue** (PRONTO_PARA_REVISAO).

O lote 01 está **fechado**: os quatro volumes da seleção inicial foram escritos e validados. A
pasta de `m04` ainda contém o arquivo `.frente` da reserva; ele pode ser apagado na próxima
seleção, porque o volume já saiu de EM_PRODUCAO no `--status`.

## Notas dos autores

- `lingua-portuguesa/m06`: o material-base trata "oração modal" como categoria não oficial; o texto segue essa
  ressalva. A nomenclatura de "complemento de objeto indireto" em tec_508116 foi explicada pelo papel do termo em
  relação ao verbo.
- `direito-administrativo/m07`: a Súmula 665 do STJ foi citada pelo sentido consolidado, sem transcrição literal,
  porque o texto integral não foi conferido na base do tribunal nesta sessão. O quadro de convalidação da fonte
  (p. 144) trata do saneamento pelo particular e está coberto em a05-s12.
- `direito-penal-militar/m02`: mantida a divergência STM × STF sobre insignificância em crime militar, com a
  posição a adotar na objetiva. O art. 41 do CPM, de redação confusa, foi explicado pela leitura doutrinária. As
  seis inéditas usadas na Fixação foram conferidas no CPM antes do uso.
- `direito-constitucional/m04`: o capítulo 4 já trata a perda da nacionalidade com a redação da Emenda 131/2023, que
  retirou a hipótese de perda por aquisição de outra nacionalidade; questões antigas do material-base podem estar
  desatualizadas nesse ponto. O capítulo 7 descreve a Emenda 133/2024 a partir do texto da emenda (30% dos recursos
  de campanha para candidaturas de pessoas pretas e pardas, Refis partidário e reforço da imunidade). A única
  coincidência de 10+ palavras que sobrou está dentro de um quadro `[!lei]` (art. 7º, caput), citação literal.
  Ficaram fora do volume os detalhes de processo eleitoral (registro de candidatura, prazos de convenção).
- `direito-constitucional/m04`, correção de vigência: a fonte estava com a contagem dos prazos da Ficha Limpa anterior
  à Lei Complementar 219/2025. O capítulo 6 foi reescrito com a regra vigente (oito anos contados, em regra, da
  condenação; oito anos após o cumprimento da pena nos crimes contra a administração pública e nos itens 6 a 10 do
  rol), com registro de que a mudança está sob análise do STF em ação direta pendente. Conferido no texto da LC
  219/2025 no Planalto. Também foi corrigido o requisito da improbidade, que exige dolo e, ao mesmo tempo, prejuízo
  ao erário e enriquecimento ilícito.

## Ferramentas

- Sem subagentes nesta sessão: os volumes foram escritos e revalidados pelo próprio coordenador, um por vez.
- `validate_material.py` e `check_citations.py` rodados ao fim de cada capítulo e no fechamento de cada volume.
- Correções feitas por rodada: m07 (expressão proibida "preencher", tamanhos, cobertura de s11 e s13, citações
  sem norma no quadro da Lei 14.133); m02 (impressão digital com caracteres bidirecionais em a01-s02, expressões
  proibidas "preencher"/"a completar", tamanhos e coincidências com a fonte).
- `check_citations.py` fechou com 0 inexistentes nos quatro volumes (m04: 30 citações, 0 inexistentes).
- Um erro do validador em m04 foi corrigido, não contornado: a Fixação estava com 25 questões e o padrão do volume
  é 20, então cinco candidatas foram retiradas (as de menor cobertura de assunto), sem afrouxar a regra.
- Em m04, o `--relatorio` foi reexecutado depois do ajuste da tabela de idades do a06-s01, que era a última
  coincidência evitável.

## Custo

Tempo total de sessão: cerca de 1 h 45 para os volumes m07 e m02 (18:25–20:07) e cerca de 2 h 30 adicionais para
o m04 (fechamento em 30/10/2026), incluindo a retomada após a queda anterior. Sem tokens de subagentes a
registrar. Nenhum commit e nenhuma gravação no banco.

## Validação (4 volumes)

### lingua-portuguesa/m06 — 0 erro(s), 3 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a05/s01 | ALTA (91) | 3574/3266 | 8/4 | 12/6 | 0.61 | 0 | 14.9 | 0 |
| a05/s02 | ALTA (89) | 2958/3126 | 7/4 | 9/6 | 0.61 | 0 | 15.1 | 0 |
| a05/s03 | ALTA (80) | 2010/2182 | 7/2 | 5/4 | 0.66 | 0 | 17.1 | 0 |
| a05/s04 | ALTA (89) | 2361/2551 | 5/3 | 6/5 | 0.59 | 0 | 15.1 | 0 |
| a05/s05 | ALTA (94) | 3389/3712 | 11/3 | 7/7 | 0.68 | 10 | 15.0 | 1 |
| a05/s06 | ALTA (94) | 3691/3608 | 13/3 | 7/7 | 0.6 | 0 | 15.9 | 0 |

Fixação: 20 questões · AOCP 17 · inéditas do banco 0 · inéditas novas 0
- AVISO a05-s04.md: cobertura da fonte 0.59 (esperado ≥ 0.6); faltam: 3que, line, peri, fulana, 3sem, 1acordei, 5nem, 4porque, 2percebi, 2cheguei, 1assim, 1apesar
- AVISO a05-s05.md: coincidência com a fonte (definição/norma? reescreva se puder): “manobras de minha tia e se meu tio encontrou os” (10 palavras)
- AVISO a05-s06.md: cobertura da fonte 0.60 (esperado ≥ 0.6); faltam: colica, culminaria, pacificadas, vacinou, rendendo, atacado, tronco, orgulhar, mergulhar, afogar, diabo, externo

### direito-administrativo/m07 — 0 erro(s), 0 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a05/s08 | MEDIA (57) | 3145/3123 | 6/3 | 11/6 | 0.72 | 0 | 16.1 | 0 |
| a05/s09 | ALTA (78) | 2929/3268 | 9/8 | 9/6 | 0.7 | 0 | 16.1 | 0 |
| a05/s10 | MEDIA (57) | 2513/2884 | 5/5 | 8/5 | 0.73 | 0 | 15.4 | 0 |
| a05/s11 | ALTA (73) | 3027/3523 | 11/8 | 11/6 | 0.64 | 0 | 14.9 | 0 |
| a05/s12 | BASE (27) | 2121/1840 | 6/4 | 7/4 | 0.67 | 0 | 14.6 | 0 |
| a05/s13 | MEDIA (57) | 2199/2215 | 5/5 | 9/4 | 0.71 | 0 | 15.7 | 0 |

Fixação: 18 questões · AOCP 12 · inéditas do banco 6 · inéditas novas 0

### direito-penal-militar/m02 — 0 erro(s), 0 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a01/s01 | ALTA (93) | 3316/3872 | 5/3 | 13/7 | 0.66 | 0 | 16.8 | 0 |
| a01/s02 | ALTA (93) | 3147/3671 | 6/4 | 14/7 | 0.77 | 0 | 15.5 | 0 |
| a02/s01 | ALTA (89) | 1548/1684 | 4/3 | 6/3 | 0.66 | 0 | 14.1 | 0 |
| a03/s01 | MEDIA (63) | 1447/1323 | 4/2 | 6/3 | 0.71 | 0 | 15.8 | 0 |

Fixação: 12 questões · AOCP 6 · inéditas do banco 6 · inéditas novas 0

### direito-constitucional/m04 — 0 erro(s), 1 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a04/s01 | MEDIA (36) | 2933/2446 | 5/3 | 10/5 | 0.63 | 0 | 18.1 | 1 |
| a04/s02 | ALTA (77) | 3555/3944 | 8/6 | 14/7 | 0.74 | 11 | 19.3 | 0 |
| a04/s03 | ALTA (77) | 3071/3598 | 8/8 | 12/6 | 0.62 | 0 | 17.1 | 0 |
| a05/s01 | ALTA (94) | 3371/3915 | 9/6 | 11/7 | 0.67 | 0 | 17.6 | 0 |
| a06/s01 | ALTA (88) | 2129/2431 | 7/6 | 9/5 | 0.63 | 0 | 15.5 | 0 |
| a06/s02 | ALTA (90) | 3117/3415 | 7/5 | 12/6 | 0.61 | 0 | 18.7 | 0 |
| a07/s01 | ALTA (88) | 3021/3508 | 11/2 | 12/6 | 0.76 | 0 | 18.4 | 0 |

Fixação: 20 questões · AOCP 20 · inéditas do banco 0 · inéditas novas 0
- AVISO a04-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “além de outros que visem à melhoria de sua condição social” (11 palavras)

