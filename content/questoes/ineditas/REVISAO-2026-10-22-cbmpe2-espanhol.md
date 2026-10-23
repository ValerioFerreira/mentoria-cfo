# Revisão — inéditas CBMPE (rodada 2), Língua Espanhola (agente `espanhol2`, 2026-10-22)

Arquivo gravado: `content/questoes/ineditas/mc/lingua-espanhola.txt` (+142 questões de múltipla escolha, 5 alternativas; de 232 para 374; gabarito embaralhado pela ferramenta: A 74, B 75, C 75, D 75, E 75).
Conferências: `lacunas_cbmpe_aula.py --lista lingua-espanhola` sem nenhuma aula abaixo de 25; `ineditas_mc_nativas.py --check` com `erros 0`.

## Quantidade por aula (soma da aula = exatamente o que o CSV pedia; todas chegam a 25)

| Aula | Tema | Escritas |
|---|---|---|
| a00/s01 | Alfabeto, pontuação, maiúsculas, leitura e tradução | 18 |
| a01/s01 + s02 | Artigos (6 + 5) | 11 |
| a02/s01 + s02 | Preposições (6 + 5) | 11 |
| a03/s01 | Contrações | 18 |
| a04/s01 + s02 | Conjunções (6 + 5) | 11 |
| a05/s01 + s02 | Advérbios (6 + 5) | 11 |
| a07/s01 + s02 | Adjetivos (6 + 5) | 11 |
| a08/s01 + s02 | Pronomes (6 + 5) | 11 |
| a10 | Números (s01 = 2, s02 = 1, s03 = 1) | 4 |
| a12/s01 | Acentuação | 18 |
| c01/s01 | Complemento (grau, irregulares, impessoais, pronominais, relativos, heterográficos) | 18 |
| **Total** | | **142** |

## Método

- Conteúdo autoral: frases e textos curtos escritos para estas questões, em espanhol padrão, sem copiar prova nem material protegido. Questões de **leitura de texto** (textos de 2 a 3 frases, pergunta e alternativas em português): 22 delas, nas aulas a00 (6), a01 (1), a03 (4), a04 (2), a05 (2), a07 (2), a08 (2), a10 (1) e a12 (2), cobrindo a lacuna apontada na rodada anterior. As demais são de gramática, léxico, tradução e ortografia, cada uma em tópico diferente das 7 já gravadas no trecho.
- Conferi ortografia e gramática pela Ortografía (2010) e pela Nueva gramática da RAE, de memória de uso consolidado, evitando como distratores formas que são corretas em alguma variante regional (por exemplo, "en la mañana", "a la mañana", "tiene tres años que", "hace tres años" posposto, "una hada", "más bueno").
- Revisão cruzada: reli cada questão como revisor independente (gabarito único, distratores errados de fato, coerência do comentário com a letra correta, comentário sem citar letras). Ajustei durante a escrita o que a ferramenta ou a releitura apontaram (alternativa correta longa demais, comentário impreciso sobre porcentagem, hora e `desde hace`).

## Ocorrências e correções feitas

1. `--check` trata como repetidas alternativas que só diferem por maiúscula/minúscula. Três questões gravadas com esse defeito (duas de maiúsculas na a00 e a de "de El Salvador / de el Salvador" na a03) foram removidas do `.txt` por script, logo após a gravação, e substituídas por versões sem esse problema. Uma questão de "mañana por la mañana" (a05) também foi regravada para trocar um distrator regional ("a la mañana"). Nenhuma questão gravada precisa de troca agora.
2. O `--check` acusou durante a execução um erro em `quimica #473` (quimica/a12/s02, enunciado com 4 palavras); é de outro agente e deixou de aparecer no fim.

## Pontos que dependem do dono (nenhum bloqueia o uso)

1. **Estilo da banca.** O padrão da banca em espanhol é texto + perguntas de compreensão; as questões de leitura são curtas porque cada questão do banco é independente (não há texto compartilhado entre questões). Se o produto passar a aceitar texto-base comum, vale ampliar.
2. **a01/s02 (porcentagem).** A questão "el veinte por ciento de los candidatos fue aprobado" usa a concordância no singular; a RAE admite também o plural (`fueron aprobados`). Todas as alternativas usam o mesmo verbo, de modo que a escolha não depende dessa variação.
3. **a07/s02 (Santo Tomás).** Usa-se a lista de exceções da RAE (Santo Tomás, Santo Tomé, Santo Toribio, Santo Domingo). Se o material do curso tiver lista menor, o comentário ainda está correto.
4. **a08/s01 (voseo).** A questão trata o voseo como fato regional (Argentina, Uruguai), sem entrar na conjugação.
5. **a12 (tilde de "solo" e "guion").** Seguem a Ortografía de 2010, como na rodada anterior.
6. **a02/s02 e a08/s01 ("entre tú y yo").** Segue a RAE (entre e según regem pronomes de sujeito); o uso de "entre ti y mí" é comum na fala, mas fora da norma.

## Trocas pendentes de questão já gravada

Nenhuma.
