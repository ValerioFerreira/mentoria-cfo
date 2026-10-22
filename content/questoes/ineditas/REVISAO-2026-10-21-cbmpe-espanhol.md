# Revisão — inéditas CBMPE, Língua Espanhola (agente `espanhol`, 2026-10-21)

Arquivo gravado: `content/questoes/ineditas/mc/lingua-espanhola.txt` (232 questões de múltipla escolha, 5 alternativas, gabarito embaralhado: A 47, B 46, C 47, D 46, E 46).
Conferências: `lacunas_cbmpe.py --lista lingua-espanhola` sem nenhum trecho abaixo de 7; `ineditas_mc_nativas.py --check` sem erro em Língua Espanhola.

## Quantidade por aula (todos os 35 trechos chegaram exatamente ao que o CSV pedia)

| Aula | Tema | Questões |
|---|---|---|
| a00 | Alfabeto, pontuação, leitura | 7 |
| a01 | Artigos (s01, s02) | 14 |
| a02 | Preposições (s01 = 6, s02 = 7) | 13 |
| a03 | Contrações | 7 |
| a04 | Conjunções (s01 = 7, s02 = 6) | 13 |
| a05 | Advérbios | 14 |
| a06 | Substantivos (s01 = 5; s02, s03, s04 = 7) | 26 |
| a07 | Adjetivos | 14 |
| a08 | Pronomes (s01 = 6, s02 = 5) | 11 |
| a09 | Verbos (s01 = 5, s02 = 7, s04 = 5, s05 = 7, s06 = 6) | 30 |
| a10 | Números | 21 |
| a11 | Interpretação de textos (s01 = 7, s02 = 6) | 13 |
| a12 | Acentuação | 7 |
| a13 | Silabeo, sinonímia, heterotônicos/semânticos/genéricos, falsos cognatos, marcadores temporais | 35 |
| c01 | Complemento (grau, irregulares, impessoais, pronominais, relativos, heterográficos) | 7 |
| **Total** | | **232** |

## Método

Cada questão foi escrita com exemplos autorais (nada de texto de provas ou do material protegido), com uma só alternativa correta e distratores que trocam um elemento (forma verbal, gênero, apócope, acento, preposição). Na revisão cruzada reli todas as questões como revisor independente: conferi gabarito, grafia e acentuação em espanhol (RAE, Ortografía de 2010 e Nueva gramática), gênero e número de cada exemplo e a coerência entre comentário e gabarito. Corrigi duas questões da aula a00 (Maiúsculas) logo no início, porque tinham alternativas que só diferiam por maiúsculas (o `--check` as acusou como repetidas): as versões defeituosas foram removidas do `.txt` por script (antes de qualquer outro agente depender delas) e regravadas pela ferramenta.

## Pontos que dependem do dono (nenhum bloqueia o uso)

1. **Estilo da banca.** O Instituto AOCP costuma apresentar um texto em espanhol e perguntas sobre ele; como o catálogo do plano é por tópico gramatical, a maioria das questões é de gramática e léxico com enunciado em português. Só as aulas a00, a11 e algumas de léxico trazem textos curtos. Se quiser mais questões de leitura de texto, precisam ser escritas à parte.
2. **a09/s01 a s05 e c01 (verbos).** Em "irregularidade comum × própria" (c01/s01) adotei a classificação usual de cursos: comum = padrões compartilhados (e→ie, o→ue, e→i, -zco, -go); própria = verbos com irregularidade exclusiva (ser, ir, estar, dar, ver...). Se o material do curso usa outra terminologia, ajuste o comentário dessa questão.
3. **Variantes regionais.** Evitei usar como distratores formas que são corretas em alguma região (fresa/frutilla, melocotón/durazno, falda/pollera, billete/boleto/pasaje, camioneta, "vivo aquí hace tres años" na América). Em a13/s02 a sinonímia regional (coche/carro/auto) é pergunta explícita.
4. **a10/s03 e a13/s03.** Os itens "dois bilhões = dos mil millones" (billón = 10^12 em espanhol) e os heterotônicos (oxígeno, hidrógeno, burócrata, misántropo) seguem a norma da RAE; `millardo` existe como alternativa a "mil millones", mas não foi usado como distrator.
5. **a12/s01.** A questão sobre "solo" e demonstrativos sem tilde segue a Ortografía de 2010 (a norma anterior admitia tilde em caso de ambiguidade).
6. **a06/s03 e s04 (vocabulário).** São questões de tradução português → espanhol; palavras como "calcetines/medias" e "abrigo/chaqueta" variam por região, por isso cada item pede só uma tradução e os distratores são palavras de outro campo semântico.

## Trocas pendentes de questão já gravada

Nenhuma. Não há questão gravada que precise ser trocada.
