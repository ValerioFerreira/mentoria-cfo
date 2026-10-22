# Revisão — inéditas MentorIA de múltipla escolha, Física (CBMPE Oficial), 2026-10-21

Arquivo gravado: `content/questoes/ineditas/mc/fisica.txt` (151 questões novas, antes vazio; `ineditas_mc_nativas.py --check` sem erro na Física; letras A 30, B 30, C 30, D 30, E 31).
`lacunas_cbmpe.py --lista fisica`: nenhum trecho abaixo de 7.

## Quantidade por aula

| Aula | Questões | Trechos |
|---|---|---|
| a00 (vetores; grandezas, análise dimensional, SI) | 14 | s01 7, s02 7 |
| a01 (cinemática, MRU) | 2 | s01 1, s02 1 |
| a02 (MRUV) | 11 | s01 5, s02 6 |
| a03 (queda livre, projéteis) | 4 | s02 1, s03 3 |
| a04 (movimento relativo, MCU) | 11 | s01 6, s02 5 |
| a05 (leis de Newton, atrito, centrípeta) | 6 | s01 1, s03 5 |
| a06 (trabalho, potência, energia) | 10 | s01 6, s02 4 |
| a07 (colisões, centro de massa) | 6 | s02 6 |
| a08 (estática, torque) | 10 | s01 3, s02 7 |
| a09 (gravitação) | 6 | s01 6 |
| a10 (hidrostática, Stevin) | 5 | s01 5 |
| a11 (gases) | 3 | s03 3 |
| a12 (propagação do calor) | 1 | s01 1 |
| a13 (MHS, pêndulo, massa-mola) | 14 | s04 7, s05 7 |
| a14 (Coulomb, campo, potencial, capacitância) | 10 | s01 4, s02 6 |
| a15 (corrente, Ohm, associação, Joule) | 7 | s01 7 |
| a16 (geradores, receptores, capacitores) | 14 | s01 7, s02 7 |
| a17 (magnetismo) | 5 | s01 5 |
| c01 (óptica geométrica) | 5 | s01 5 |
| c02 (tópicos sem cobertura) | 7 | s01 7 (cobertura dos seis tópicos; 2 além do mínimo) |

## Método

Cada conta foi feita por dois caminhos (fórmula direta e verificação por outra via: energia × cinemática, soma de momentos em outro apoio, associação por produto/soma × inverso etc.) e mostrada no comentário. Dados fictícios e simples, SI, g = 10 m/s² e k = 9·10^9 N·m²/C² declarados no enunciado quando usados; sem figuras (tudo descrito em texto). Os distratores reproduzem erros típicos (esquecer de converter unidades, não elevar ao quadrado, trocar seno por cosseno, somar em vez de subtrair, usar paralelo no lugar de série). Revisão cruzada feita relendo cada questão como revisor independente.

## Pontos que dependem do dono / do orquestrador

1. **a13/s04 e a13/s05 (MHS) não estão ligados a nenhum assunto do edital** em `content/edital/fisica.json` (os itens 6.x só citam `a13/s01` a `a13/s03`). O `--check` acusava "trecho sem assunto do edital do PCPE" nas 14 questões. Solução aplicada: os 14 cabeçalhos receberam `| item=6.8` ("Período, frequência, ciclo"), por meio de edição programática dos cabeçalhos desses 14 blocos no `.txt` (backup antes; nada mais foi alterado). O ideal é o dono decidir se o MHS entra no mapa do edital (por exemplo, no item 6.8) e então remover o `item=` ou mantê-lo.
2. **c02 (tópicos do edital sem cobertura)**: as questões sobre história força × movimento, marés, origem do universo (idade ≈ 13,8 bilhões de anos), para-raios e gaiola de Faraday são conceituais e seguem a literatura-padrão de Física do ensino médio; conviria uma leitura do dono sobre o nível de profundidade esperado pela banca.
3. **Questões "INCORRETA"** (a02/s02, a04/s01, a17/s01): o gabarito é a afirmação falsa; o enunciado traz "INCORRETA" em maiúsculas.
4. Nenhuma questão depende de norma, valor desatualizado ou divergência do material-base.
