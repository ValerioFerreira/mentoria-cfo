# Revisão — inéditas CBMPE de Química (agente quimica-2), 2026-10-21

Parte: `quimica/a14/s04` até o último trecho (`quimica/c01/s01`). Gravadas em `content/questoes/ineditas/mc/quimica.txt`
(múltipla escolha, 5 alternativas, Instituto AOCP). Total desta parte: **208 questões**, exatamente o que o CSV pedia em `faltam`.
`ineditas_mc_nativas.py --check` terminou com `erros 0`, e `lacunas_cbmpe.py --lista quimica` já não lista nenhum trecho da minha parte
(restam só `a14/s01`, `a14/s02` e `a14/s03`, do agente quimica-1).

## Quantidade por aula

| Aula | Assunto | Questões |
| --- | --- | --- |
| a14/s04 | Balanceamento redox, agente oxidante/redutor | 7 |
| a15 (s01 a s03) | Radioatividade (emissões, meia-vida, C-14, fissão, fusão, transmutação) | 1 + 6 + 6 = 13 |
| a16 (s01 a s03) | Carbono, hibridização, classificação de carbonos e cadeias | 5 + 7 + 6 = 18 |
| a17 (s01 a s05) | Hidrocarbonetos (fórmulas gerais, nomenclatura, propriedades, reatividade, petróleo, gás natural, carvão, biogás) | 5 + 7 + 7 + 7 + 7 = 33 |
| a18 (s01 a s04) | Funções orgânicas, nomenclatura, propriedades, aminas, amidas, carbonilas, haletos | 6 + 7 + 7 + 7 = 27 |
| a19 (s01 a s04) | Isomeria plana e espacial, quiralidade, R/S, Fischer, meso, conformações | 7 + 7 + 7 + 7 = 28 |
| a20 (s01 e s02) | Acidez e basicidade, nucleófilos e eletrófilos | 7 + 7 = 14 |
| a21 (s01 a s03) | Adição e eliminação | 7 + 7 + 7 = 21 |
| a22 (s01 a s05) | Substituição, oxirredução orgânica, Grignard, Wurtz, biodiesel | 7 + 7 + 7 + 5 + 6 = 32 |
| a23 (s01 e s02) | Petroquímica, combustíveis e derivados do petróleo | 6 + 7 = 13 |
| c01/s01 | Complemento (Hommel, gases de incêndio) | 2 |

## Método de conferência

- Todas as contas (balanceamentos, estequiometria, meia-vida, pH de ácido/base fraca, excesso enantiomérico, rendimento) foram
  refeitas por dois caminhos, e os dois aparecem no comentário.
- Nomenclatura IUPAC conferida caso a caso (menor localizador, prioridade de função, ordem alfabética dos prefixos). Um erro
  de ordem alfabética (2-cloro-3-bromobutano) foi corrigido para 2-bromo-3-clorobutano antes da gravação.
- Duas correções feitas na revisão cruzada, ainda no rascunho: a alternativa sobre Wöhler que citava isomeria (histórica e
  discutível) foi trocada por uma claramente falsa, e os comentários passaram a deixar de fora detalhes duvidosos.
- Não há figuras: toda estrutura é descrita em fórmula condensada ou por texto.

## Dúvidas e observações para o dono

1. **Teor de etanol anidro na gasolina**: não cito percentual da mistura obrigatória (muda por decreto/CNPE), só a distinção
   anidro × hidratado. A questão do "teste da proveta" (a23/s02) usa o cálculo simplificado (aumento da fase aquosa ÷ volume de
   gasolina), com a premissa explícita de que a gasolina não se dissolve na fase aquosa; o procedimento oficial da ANP aplica um
   fator de correção, por isso o enunciado traz os dados fictícios e a premissa.
2. **Reatividade relativa 4:1** (hidrogênio secundário × primário, cloração do propano, a22/s02) é um dado do enunciado
   ("admita"), próximo do valor experimental, e não um valor de norma.
3. **Pontos de ebulição, pKa e ponto de fulgor** aparecem como valores aproximados ("cerca de") e não como dado exato.
4. Algumas questões de a15 usam meia-vida de 5.700 anos para o C-14 (valor aproximado de 5.730), declarada no enunciado.
5. Nenhuma questão foi trocada depois de gravada; não há pedido de substituição ao orquestrador.
6. Observação do formato: o `ineditas_append.py` exige no enunciado uma das palavras "assinale/julgue/indique/aponte"; nos
   enunciados que terminavam em dois-pontos ou pergunta inseri "Assinale a opção ..." por um passo automático no rascunho.
