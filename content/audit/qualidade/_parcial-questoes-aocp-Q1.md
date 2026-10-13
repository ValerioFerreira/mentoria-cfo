# Auditoria AOCP de questões — parcial Q1

- **Código**: Q1
- **Disciplinas**: direito-constitucional, direito-administrativo, direito-penal-militar, legislacoes-pe, lingua-portuguesa, lingua-inglesa, lingua-espanhola
- **Sementes**: 81000 + rodada (draw_questions.py, 25 questões por rodada, pool de 4.674 questões)
- **Data**: 2026-10-10

## Métricas acumuladas

- Rodadas: **2** · questões auditadas: **50**
- OK (sem achado): **34** (68%) · com achado: **16** (32%)
- Achados por severidade: CRÍTICO **0** · MAIOR **3** · MENOR **13**
- Taxa de gabarito errado: **0/50** (0.0%)
- Questões com achado por categoria (a principal de cada questão): distrator 7; explicação 4; fidelidade ao PDF 2; padrão AOCP 2; português 1
- Distribuição do gabarito na amostra: A 16 (32%) · B 10 (20%) · C 11 (22%) · D 4 (8%) · E 9 (18%)
- Correta estritamente a mais longa (amostra bruta, antes das correções): **22/50** (44%; ao acaso esperaria-se ≈ 20%)
- Negações sem destaque correto (comando com incorreta/errada/exceto fora de MAIÚSCULAS, ou 'NíO' corrompido): **1/2** enunciados com negação
- Explicações problemáticas: **4/50** (8.0%)

Taxa de questões com achado por disciplina:

| disciplina | auditadas | com achado | taxa |
|---|---|---|---|
| direito-administrativo | 8 | 4 | 50% |
| direito-constitucional | 10 | 4 | 40% |
| direito-penal-militar | 6 | 0 | 0% |
| legislacoes-pe | 1 | 0 | 0% |
| lingua-espanhola | 2 | 1 | 50% |
| lingua-inglesa | 5 | 3 | 60% |
| lingua-portuguesa | 18 | 4 | 22% |

Por `pattern`:

| pattern | auditadas | com achado | taxa |
|---|---|---|---|
| assertivas | 2 | 0 | 0% |
| caso | 7 | 3 | 43% |
| conceito | 13 | 4 | 31% |
| correta | 10 | 3 | 30% |
| excecao | 5 | 1 | 20% |
| incorreta | 2 | 2 | 100% |
| lacuna | 1 | 0 | 0% |
| lei-seca | 4 | 2 | 50% |
| relacao | 4 | 1 | 25% |
| texto | 2 | 0 | 0% |

## Por rodada

| rodada | questões | OK | críticos | maiores | menores |
|---|---|---|---|---|---|
| 1 | 25 | 19 | 0 | 1 | 5 |
| 2 | 25 | 15 | 0 | 2 | 8 |

## Registro de achados

### Rodada 1

**Q-01** · `direito-constitucional/a17/s05` q1 · `content/items/direito-constitucional/a17.json` · **MAIOR** · fidelidade ao PDF / padrão AOCP
- Problema: `pageRef` 44 trata só da competência do STF; a regra de objeto da ADI (norma federal/estadual pós-1988; municipal fora) está na pág. 47. O enunciado remetia a "regra geral apresentada" e as alternativas traziam muletas artificiais ("no cenário descrito", "nessa hipótese") sem cenário algum.
- Correção: `pageRef` 44 → 47; enunciado reescrito de forma autocontida ("Em regra, qual espécie de norma pode ser objeto de ADI…"); muletas removidas; gabarito (B) e explicação mantidos. Status: corrigido.

**Q-02** · `lingua-portuguesa/a07/s04` q6 · `…/lingua-portuguesa/a07.json` · **MENOR** · explicação / português
- Problema: explicação com lacuna ("alternativas B, C e (voz passiva)") e afirmação imprecisa de que particípios da voz passiva "têm valor adjetivo".
- Correção: "B, C e E (voz passiva) e D (oração reduzida)"; trecho do "valor adjetivo" removido. Status: corrigido.

**Q-03** · `lingua-inglesa/a00/s01` q6 · `…/lingua-inglesa/a00.json` · **MENOR** · explicação / português
- Problema: "D e atribuem sentidos…" (alternativa E omitida). Distratores com absolutizantes ("apenas", "exclusivamente") que denunciam o erro (não alterado: o texto das alternativas é coerente com o PDF, pág. 12).
- Correção: "D e E atribuem…". Status: corrigido (parcial).

**Q-04** · `direito-administrativo/a06/s03` q9 · `…/direito-administrativo/a06.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (E) com 89 caracteres contra 52–61 nas demais.
- Correção: E → "dispensa-se na emergência e exige-se nos demais casos." Gabarito mantido. Status: corrigido.

**Q-05** · `lingua-portuguesa/a02/s02` q23 · `…/lingua-portuguesa/a02.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (C) com 77 caracteres contra 39–56.
- Correção: C → "todos têm papel adjetivo, mas só "novos" é adjetivo." Status: corrigido.

**Q-06** · `lingua-espanhola/a01/s01` q10 · `…/lingua-espanhola/a01.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (B) com 70 caracteres contra 35–54.
- Correção: B → "Ele varia em gênero e número, concordando com o substantivo." Status: corrigido.

Observação de infraestrutura (sem correção em conteúdo): o texto em cache de `direito-penal-militar/a01` (págs. 8 e seguintes) vem com letras perdidas (fonte do PDF); a verificação teve de usar o PDF original via PyMuPDF. Questões de DPM não podem ser conferidas pelo cache.

### Rodada 2

**Q-07** · `direito-administrativo/a09/s02` q3 · `…/direito-administrativo/a09.json` · **MAIOR** · fidelidade ao PDF / ambiguidade
- Problema: enunciado dependia de "atualização jurisprudencial relatada" (texto que o aluno não vê); a correta (D) afirmava que "o estatutário ainda predomine", ponto que o trecho (pág. 15) não sustenta (a pág. diz só que o regime único deixou de ser obrigatório e que cabem estatutário ou emprego público).
- Correção: enunciado autocontido ("Após o julgamento definitivo do STF sobre a EC 19/1998…"); D → "A obrigatoriedade geral de regime jurídico único deixou de existir."; explicação reescrita sem o "predomínio". Status: corrigido.

**Q-08** · `direito-constitucional/a10/s07` q0 · `…/direito-constitucional/a10.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (E) com 133 caracteres contra 85–113.
- Correção: E encurtada (≈110). Status: corrigido.

**Q-09** · `direito-constitucional/a10/s04` q0 · `…/direito-constitucional/a10.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (B) com 141 caracteres contra 101–112.
- Correção: B → "São garantias funcionais de ordem pública, irrenunciáveis e não extensivas aos suplentes." Status: corrigido.

**Q-10** · `lingua-inglesa/a05/s03` q8 · `…/lingua-inglesa/a05.json` · **MENOR** · explicação / português
- Problema: "As alternativas C, D e desorganizam…" (E omitida).
- Correção: "C, D e E". Status: corrigido.

**Q-11** · `direito-constitucional/a13/s07` q0 · `…/direito-constitucional/a13.json` · **MENOR** · padrão AOCP / viés
- Problema: distratores com muletas artificiais ("nessa hipótese", "conforme o texto constitucional", "segundo a regra indicada") que não existem em prova real e deixam a correta (103) visivelmente mais longa e "limpa".
- Correção: distratores reescritos sem muletas, com tamanho equiparado (78–92 contra 98). Status: corrigido.

**Q-12** · `lingua-portuguesa/a05/s02` q1 · `…/lingua-portuguesa/a05.json` · **MENOR** · explicação / português
- Problema: "…D, um único objeto direto, e, uma oração com objeto indireto" (E omitida).
- Correção: "e E, uma oração…". Status: corrigido.

**Q-13** · `lingua-portuguesa/a07/s03` q6 · `…/lingua-portuguesa/a07.json` · **MENOR** · distrator (dica gramatical) / explicação
- Problema: a correta era a única com verbo no plural (A, B, D e E com verbo no singular), o que a entrega sem exigir análise; explicação com "A, B, D e," (E omitida).
- Correção: D passa a ter verbo no plural mas particípio sem concordância ("foram aprovado"); explicação ajustada e completa. Status: corrigido.

**Q-14** · `lingua-inglesa/a00/s01` q11 · `…/lingua-inglesa/a00.json` · **MENOR** · padrão AOCP / distrator / explicação
- Problema: pergunta metodológica ("reconhecer sujeito e verbo é o passo essencial") com `support` inventado e distratores marcados por absolutos ("impede qualquer", "invariavelmente", "dispensam"); explicação com "D e contradizem" (E omitida). pageRef 20 sustenta o ponto (sujeito + verbo + complemento).
- Correção: apenas a explicação ("D e E"). Questão mantida; recomenda-se reescrever em formato de leitura real. Status: parcial.

**Q-15** · `direito-administrativo/c01/s02` q0 · `…/direito-administrativo/c01.json` · **MAIOR** · português
- Problema: negação em destaque escrita "NíO" no lugar de "NÃO" no comando da questão (corrupção de caractere; ver S-01).
- Correção: "NÃO". Status: corrigido (a ocorrência sistêmica em outras questões fica para a consolidação).

**Q-16** · `direito-administrativo/a00/s05` q12 · `…/direito-administrativo/a00.json` · **MENOR** · distrator (viés de tamanho)
- Problema: correta (C) com 137 caracteres contra 83–103.
- Correção: C → "viola a Constituição, pois a vedação alcança parentes colaterais até o terceiro grau de quem exerce chefia." Status: corrigido.


## Padrões recorrentes e recomendações

(Seção atualizada a cada rodada; versão final no fim da missão.)

**S-01 — "NÃO" gravado como "NíO" (sistêmico, MAIOR).** Em `content/items` há "NíO" (bytes C3 AD) no lugar de "NÃO" em ≈ 115 pontos, quase sempre no comando de questões do tipo "assinale a alternativa que NÃO…": direito-administrativo 13, direito-constitucional 20, direito-penal-militar 7, legislacoes-pe 1, lingua-espanhola 6, lingua-inglesa 4, lingua-portuguesa 11 (e ainda biologia 5, estatistica 6, fisica 2, informatica 29, quimica 9). Corrigi só a ocorrência sorteada (Q-15). Recomendação: substituição global `NíO` → `NÃO` em um único passe, com os demais agentes parados.

**S-02 — letra "E" omitida na explicação (sistêmico, MENOR).** Explicações dizem "as alternativas C, D e trazem…" / "B e descrevem…" (a letra E sumiu depois do "e"). ≈ 300 ocorrências (biologia ≈ 200; lingua-inglesa 80; lingua-portuguesa 28; direito-penal-militar 7; direito-administrativo 1). Corrigi as sorteadas (Q-02, Q-03, Q-10, Q-12, Q-13, Q-14). Recomendação: varredura determinística (regex sobre "alternativas|opções … <letra> e <verbo>") e correção em lote, com revisão da letra omitida (quase sempre E, mas pode ser outra).

**S-03 — texto em cache de DPM com letras perdidas.** Em `direito-penal-militar` (ex.: a01 págs. 8 e seguintes, a08 pág. 15) o texto de `pipeline/.cache/pages` vem sem várias letras ("rime", "onsma"); o conferência exige abrir o PDF com PyMuPDF. Convém reextrair essas páginas (OCR/outro modo de extração) antes de usar o cache como fonte de verdade.

**S-04 — viés de tamanho da alternativa correta.** A correta é a mais longa em proporção bem acima dos 20% do acaso (ver métricas), sobretudo em Direito (A–E com 90–150 caracteres). Recomendação: etapa automática no validador que penalize razão correta/média das erradas > 1,3 e force reescrita.

**S-05 — muletas artificiais em enunciados/alternativas** ("no cenário descrito", "nessa hipótese", "conforme a regra apresentada", "relatada"): aparecem em itens de lei seca gerados em lote e não existem em prova real. Recomendação: proibir essas expressões no validador e deixar o enunciado autossuficiente.

