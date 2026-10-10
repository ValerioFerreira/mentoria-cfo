# Auditoria por amostragem S2: diretrizes, resumos de bizu, ponteiros e itens C/E x PDF

- Código: **S2**  
- Disciplinas: biologia, quimica, fisica, direito-administrativo  
- Semente: **72002** (amostra de 100 trechos de teoria, 10 rodadas de 10)  
- Data: 2026-10-10  
- Método: leitura das páginas do PDF (texto de `pipeline/.cache/pages` via `pgread.py`) de cada trecho, sem consultar índice, estrutura, segmentos, overrides nem edital.

## Métricas acumuladas

Trechos auditados: **20** de 100.

| Dimensão | OK | PEQUENO | ERRO | Taxa PEQUENO+ERRO | Taxa ERRO |
|---|---|---|---|---|---|
| Diretriz | 19 | 1 | 0 | 5% | 0% |
| Resumo | 12 | 8 | 0 | 40% | 0% |
| Ponteiros | 19 | 1 | 0 | 5% | 0% |
| C/E (por trecho) | 18 | 2 | 0 | 10% | 0% |

Itens C/E avaliados: **182**; com gabarito errado: **0** (0%).

Achados: **10** (corrigidos: 8; propostos: 1; falsos positivos: 0).

### Por disciplina

| Disciplina | Trechos | Diretriz P/E | Resumo P/E | Ponteiros P/E | C/E P/E | Itens C/E (gab. errado) |
|---|---|---|---|---|---|---|
| biologia | 3 | 0/0 | 0/0 | 0/0 | 0/0 | 30 (0) |
| quimica | 8 | 1/0 | 4/0 | 1/0 | 0/0 | 68 (0) |
| fisica | 5 | 0/0 | 1/0 | 0/0 | 1/0 | 44 (0) |
| direito-administrativo | 4 | 0/0 | 3/0 | 0/0 | 1/0 | 40 (0) |

(P/E = quantidade de trechos com PEQUENO / quantidade com ERRO.)

## Tabela por rodada

### Rodada 1 (n = 1 a 10)

| n | segmentId | diretriz | resumo | ponteiros | C/E |
|---|---|---|---|---|---|
| 1 | quimica/a17/s05 | OK | PEQUENO | OK | OK |
| 2 | biologia/a05/s01 | OK | OK | OK | OK |
| 3 | fisica/a03/s01 | OK | OK | OK | OK |
| 4 | fisica/a11/s04 | OK | PEQUENO | OK | PEQUENO |
| 5 | quimica/a11/s02 | OK | PEQUENO | PEQUENO | OK |
| 6 | quimica/a03/s01 | OK | PEQUENO | OK | OK |
| 7 | quimica/a02/s01 | PEQUENO | OK | OK | OK |
| 8 | direito-administrativo/a01/s03 | OK | PEQUENO | OK | OK |
| 9 | quimica/a22/s03 | OK | PEQUENO | OK | OK |
| 10 | quimica/a04/s04 | OK | OK | OK | OK |

### Rodada 2 (n = 11 a 20)

| n | segmentId | diretriz | resumo | ponteiros | C/E |
|---|---|---|---|---|---|
| 11 | quimica/a07/s02 | OK | OK | OK | OK |
| 12 | direito-administrativo/a08/s02 | OK | PEQUENO | OK | OK |
| 13 | direito-administrativo/a09/s16 | OK | OK | OK | OK |
| 14 | fisica/a03/s03 | OK | OK | OK | OK |
| 15 | fisica/a02/s02 | OK | OK | OK | OK |
| 16 | fisica/a17/s01 | OK | OK | OK | OK |
| 17 | quimica/a06/s03 | OK | OK | OK | OK |
| 18 | biologia/a02/s03 | OK | OK | OK | OK |
| 19 | direito-administrativo/a07/s03 | OK | PEQUENO | OK | PEQUENO |
| 20 | biologia/a08/s01 | OK | OK | OK | OK |

## Registro de achados

**A-01** · `quimica/a17/s05` · Resumo · PEQUENO  
- O site diz: Parágrafo 'Impactos ambientais dos fósseis' cita aquecimento global, chuva ácida e óxidos de enxofre.
- O PDF mostra: Págs. 57-58: o trecho trata da alteração do ciclo do carbono/efeito estufa, fuligem e óxidos de nitrogênio do diesel e vazamentos de petróleo. Chuva ácida e óxidos de enxofre não aparecem em 53-60.
- Correção / proposta: content/items/quimica/a17.json: parágrafo reescrito só com o que o trecho traz (ciclo do carbono, fuligem e NOx do diesel, vazamentos).
- Status: **corrigido**

**A-02** · `fisica/a11/s04` · C/E + Resumo · PEQUENO  
- O site diz: Item C/E 'Carnot ... temperaturas em graus Celsius' (falso, 'devem estar em kelvin') e resumo '(kelvin)'.
- O PDF mostra: Págs. 52-53: a fórmula 1 − T2/T1 é dada sem qualquer menção à escala kelvin; o que o trecho sustenta sobre Carnot é o teorema (nenhuma máquina supera a de Carnot entre as mesmas fontes).
- Correção / proposta: content/items/fisica/a11.json: item C/E trocado por afirmação falsa sobre o teorema de Carnot (gabarito continua falso); resumo '(kelvin)' trocado por '(T2 da fonte fria e T1 da quente)'.
- Status: **corrigido**

**A-03** · `quimica/a11/s02` · Resumo · PEQUENO  
- O site diz: 'Capacidade do tampão: máxima quando [A⁻] = [HA]'.
- O PDF mostra: Págs. 24-28: o trecho só mostra que, com concentrações iguais, log 1 = 0 e pH = pKa; a noção de 'capacidade máxima' não é apresentada.
- Correção / proposta: content/items/quimica/a11.json: parágrafo reescrito para 'Tampão com [A⁻] = [HA]: log 1 = 0, então pH = pKa'.
- Status: **corrigido**

**A-04** · `quimica/a11/s02` · Ponteiros · PEQUENO  
- O site diz: 'Neutralização parcial de ácido fraco' → pág. 19.
- O PDF mostra: Pág. 19 traz só o enunciado da questão (ácido acético + NaOH); a explicação (reação completa, formação do acetato) está na pág. 20.
- Correção / proposta: content/items/quimica/a11.json: pageRef 19 → 20.
- Status: **corrigido**

**A-05** · `quimica/a03/s01` · Resumo · PEQUENO  
- O site diz: 'Em geral, equação com coeficientes apresentados já vem balanceada.'
- O PDF mostra: Pág. 4: o texto só manda verificar o balanceamento antes de qualquer cálculo; não afirma que equações com coeficientes já vêm balanceadas.
- Correção / proposta: content/items/quimica/a03.json: frase trocada por 'com equação desbalanceada, todos os resultados saem errados' (pág. 4).
- Status: **corrigido**

**A-06** · `quimica/a02/s01` · Diretriz · PEQUENO  
- O site diz: 'Comece na pág. 3, no tópico Distribuição Eletrônica e Números Quânticos - Teoria'.
- O PDF mostra: Pág. 3 é só a introdução da aula (Considerações Iniciais) e o título citado não existe no PDF; a teoria começa na pág. 4 com 'Distribuição eletrônica de Linus Pauling'.
- Correção / proposta: PROPOSTA: no override de quimica, aula 02, primeiro trecho: startPage 3 → 4 e título 'Distribuição eletrônica de Linus Pauling' (sem sufixo '- Teoria').
- Status: **proposto**

**A-07** · `direito-administrativo/a01/s03` · Resumo · PEQUENO  
- O site diz: Resumo não cobre o tópico 'Doutrina' (final da pág. 33 e início da 34), que está dentro do intervalo.
- O PDF mostra: Págs. 33-34: Doutrina não vincula, mas orienta decisões administrativas e judiciais e a criação de leis.
- Correção / proposta: content/items/direito-administrativo/a01.json: frase sobre doutrina acrescentada ao parágrafo das fontes secundárias.
- Status: **corrigido**

**A-08** · `quimica/a22/s03` · Resumo · PEQUENO  
- O site diz: Sulfonação com 'H₂SO₄ concentrado/fumegante' e eliminação 'com base forte e aquecimento'.
- O PDF mostra: Págs. 27, 34: sulfonação usa H₂SO₄ concentrado com aquecimento (Δ); eliminação é favorecida por base forte em meio alcoólico, substituição por base fraca ou forte diluída. 'Fumegante' não aparece.
- Correção / proposta: content/items/quimica/a22.json: duas frases reescritas conforme as páginas 27 e 34.
- Status: **corrigido**

**A-09** · `direito-administrativo/a08/s02` · Resumo · PEQUENO  
- O site diz: 'policial que atira em desafeta, RE 363.423'.
- O PDF mostra: Pág. 13: o policial atirou por sentimento pessoal em quem mantinha relacionamento amoroso com ele (companheira); 'desafeta' sugere inimizade e não aparece.
- Correção / proposta: content/items/direito-administrativo/a08.json: trecho trocado por 'policial que atira em sua companheira por sentimento pessoal, RE 363.423'.
- Status: **corrigido**

**A-10** · `direito-administrativo/a07/s03` · Resumo + C/E (10º item) · PEQUENO (divergência com o PDF)  
- O site diz: Resumo: a pretensão de ressarcimento fundada em decisão de Tribunal de Contas é prescritível (STF, Tema 899), só sendo imprescritível o ressarcimento por improbidade dolosa (Tema 897). O 10º item C/E marca como FALSO que 'a cobrança de qualquer débito imputado pelo Tribunal de Contas é imprescritível'.
- O PDF mostra: Pág. 27: o material diz que a multa prescreve, mas que 'a ação de ressarcimento é imprescritível' (art. 37, § 5º). Os Temas 899 e 897 não aparecem em nenhuma página do intervalo.
- Correção / proposta: Mantido sem alteração: o site segue a tese vigente do STF (Tema 899 do RE 636.886), e o texto do PDF está desatualizado. Decisão para o dono do produto: manter e, se quiser, acrescentar na explicação do item que o material-base ainda traz a tese antiga (a explicação já cita o Tema 899).
- Status: **mantido (divergência intencional; decidir)**

## Padrões recorrentes e recomendações

(a preencher ao final)
