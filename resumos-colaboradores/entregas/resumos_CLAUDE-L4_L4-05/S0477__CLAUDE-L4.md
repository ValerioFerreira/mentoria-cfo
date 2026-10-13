---
id: S0477
agente: CLAUDE-L4
materia: Estatística
aula: Aula 06 — Probabilidade
trecho: estatistica/a06/s01
paginas_lidas: 4-15
---
# ANALÍTICO

Este trecho apresenta a base da Teoria da Probabilidade: o que é um experimento aleatório, espaço amostral, ponto amostral, evento (e seus tipos) e a definição clássica de probabilidade, inclusive o uso de análise combinatória para contar casos favoráveis e totais.

### Experimento aleatório

A Teoria da Probabilidade estuda fenômenos de **resultado incerto**: lançar dado ou moeda, sortear uma carta, escolher uma pessoa ao acaso, saber se vai chover amanhã. Apesar da incerteza em cada realização, repetindo muitas vezes surge um padrão (numa moeda honesta, cerca de metade das saídas é cara).

Para um experimento ser tratado com os conceitos deste trecho, ele precisa:

1. poder ser **repetido indefinidamente, sob as mesmas condições**;
2. ter **resultado incerto, mas com padrão conhecido**.

> ⚠️ **Pegadinha:** se a repetição pode ser interrompida por algo que muda as condições (por exemplo, a moeda cai num bueiro e some), o experimento não satisfaz a exigência de repetição indefinida, e nem todos os conceitos se aplicam.

### Espaço amostral e ponto amostral

**Espaço amostral** (também chamado **universo**, símbolo U ou Ω) é o **conjunto de todos os resultados possíveis** do experimento. Cada resultado individual é um **ponto amostral**. O número de elementos do universo é n(U).

| Experimento | Espaço amostral | n(U) |
| --- | --- | --- |
| Uma moeda | {cara, coroa} | 2 |
| Um dado | {1, 2, 3, 4, 5, 6} | 6 |
| Duas moedas (ordenadas) | {(C,C), (C,K), (K,C), (K,K)} | 4 |
| Dois dados | pares (a, b), a e b de 1 a 6 | 36 |

Em lançamentos de mais de um objeto, o ponto amostral é o **par (ou trio...) ordenado**: (cara, coroa) e (coroa, cara) são pontos diferentes.

> ⚠️ **Pegadinha:** espaço amostral **não** é o tamanho da amostra, nem a soma dos resultados, nem um intervalo de probabilidades; é o conjunto dos resultados possíveis.

### Evento

**Evento é qualquer subconjunto do espaço amostral**, ao qual se atribui uma probabilidade. O número de elementos de A é n(A). Não confunda: espaço amostral é o conjunto de todos os resultados; evento é um conjunto de resultados de interesse; um evento **não** precisa ser um único elemento.

> 💡 **Exemplo:** em dois dados, o evento "soma igual a 7" é {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)}, com n = 6.

Tipos de evento:

| Tipo | Definição | n(A) | Exemplo (um dado) |
| --- | --- | --- | --- |
| Simples ou elementar | um só ponto amostral | 1 | sair o 4 |
| Impossível | conjunto vazio | 0 | sair 9 |
| Certo | igual ao espaço amostral | n(U) | sair número menor que 7 |

Pelas contas, um evento impossível tem probabilidade 0 e um evento certo tem probabilidade 1; os demais ficam entre 0 e 1.

### Definição clássica de probabilidade

**P(A) = n(A) / n(U)**, ou seja, **casos favoráveis ÷ casos totais**.

Passos práticos:

1. identifique o espaço amostral e conte n(U);
2. identifique o evento e conte n(A);
3. divida e simplifique a fração (ou converta em percentual).

> 💡 **Exemplo:** em uma turma de 30 pessoas, 12 usam óculos. Sorteando uma pessoa ao acaso, P(óculos) = 12/30 = 2/5 = 40%.

> 💡 **Exemplo (casos "restantes"):** uma urna tem 20 fichas, 8 azuis e 5 brancas; as outras são verdes. P(verde) = (20 − 8 − 5)/20 = 7/20 = 35%. Nas questões em que o enunciado dá o total e algumas categorias, as demais se obtêm por subtração.

**Condição essencial:** todos os pontos amostrais devem ser **igualmente prováveis**. Com moeda ou dado viciado, a definição clássica não vale (é preciso saber as probabilidades de cada resultado, ou estimá-las pela frequência observada, que é outra definição de probabilidade).

> ⚠️ **Pegadinha:** a soma de dois dados vai de 2 a 12, mas os 11 valores **não** são igualmente prováveis (o 7 sai de seis maneiras, o 2 de uma só). Para usar a definição clássica, o espaço amostral deve ser o conjunto dos 36 pares, que são equiprováveis.

#### Contagem com casos "ocupados"

Em questões de posição, às vezes é preciso listar os casos favoráveis um a um. Imagine 9 cadeiras em fila, com as de número 2, 6 e 7 ocupadas, e uma quarta pessoa que se senta numa das 6 livres. Qual a chance de ela ficar sem ninguém ao lado? Marque as livres que encostam em alguém (1, 3, 5 e 8); sobram a 4 e a 9. Então P = 2/6 = 1/3. Note que n(U) é o número de lugares **ainda livres**, e não 9.

### Probabilidade com análise combinatória

Quando há muitos casos, contam-se n(A) e n(U) com combinação (ordem não importa) ou arranjo (ordem importa):

- **Combinação** C(n, p) = n! / [p! × (n − p)!]
- **Arranjo** A(n, p) = n! / (n − p)!

> 💡 **Exemplo (sem ordem):** uma caixa tem 4 bolas azuis e 6 vermelhas; retiram-se 2 ao mesmo tempo. P(2 azuis) = C(4,2) / C(10,2) = 6/45 = 2/15.

> 💡 **Exemplo (com ordem):** com as mesmas bolas, retiradas em sequência como "1ª" e "2ª", P(2 azuis) = A(4,2) / A(10,2) = 12/90 = 2/15.

O ponto importante: **o resultado é o mesmo**, desde que se use o **mesmo critério (com ou sem ordem) no numerador e no denominador**. Escolha o mais simples. Em geral é mais cômodo usar combinação, pois os números ficam menores. O erro é misturar: combinação nos favoráveis e arranjo nos totais.

> 💡 **Exemplo (comissão):** de 8 pessoas, 5 de um grupo X e 3 de um grupo Y, sorteiam-se 2. P(os dois serem de X) = C(5,2) / C(8,2) = 10/28 = 5/14.

Se os cargos são distintos e o enunciado quer uma **ordem específica ou qualquer ordem**, conte com cuidado: com coordenador e assistente escolhidos entre 6 agentes, n(U) = A(6,2) = 30; a chance de dois agentes específicos ocuparem os dois cargos, em qualquer ordem, é 2/30 = 1/15 (cerca de 6,7%).

### Para fixar
- Experimento aleatório: resultado incerto, padrão conhecido, repetível indefinidamente sob as mesmas condições.
- Espaço amostral (universo) é o conjunto de todos os resultados possíveis; cada resultado é um ponto amostral.
- Evento é qualquer subconjunto do espaço amostral; pode ser elementar (1 ponto), impossível (vazio) ou certo (todo o espaço).
- Definição clássica: P(A) = n(A) / n(U), válida só com pontos amostrais igualmente prováveis.
- Cuidado ao definir n(U): remova casos já ocupados ou excluídos; some apenas casos equiprováveis (pares de dados, não a soma).
- Em combinatória, use o mesmo critério (com ou sem ordem) nos favoráveis e nos totais; o resultado não muda.
- Probabilidade de evento impossível é 0 e de evento certo é 1.

# SINTÉTICO

- **Experimento aleatório**: resultado incerto com padrão conhecido, repetível indefinidamente sob as mesmas condições; se a repetição se interrompe, os conceitos não se aplicam por inteiro.
- **Espaço amostral**: conjunto de todos os resultados possíveis (universo U ou Ω); cada resultado é um ponto amostral. Dois dados geram 36 pontos.
- **Evento**: qualquer subconjunto do espaço amostral, com n(A) elementos; não é "um único elemento".
- **Tipos de evento**: elementar (n = 1), impossível (conjunto vazio, n = 0) e certo (igual ao espaço amostral).
- **Definição clássica**: P(A) = n(A) / n(U), ou casos favoráveis sobre casos totais.
- **Condição**: os pontos amostrais precisam ser igualmente prováveis; com moeda ou dado viciado a fórmula não vale.
- **Pegadinha da soma de dois dados**: os valores 2 a 12 não são equiprováveis; use os 36 pares.
- **Contagem**: ajuste n(U) aos casos realmente possíveis (por exemplo, só as cadeiras livres) e liste os favoráveis um a um quando forem poucos.
- **Combinatória**: C(n, p) quando a ordem não importa e A(n, p) quando importa; use o mesmo critério em cima e embaixo, e o resultado é igual.
- **Limites**: P do evento impossível é 0 e P do evento certo é 1.

# NOTAS

- Pág. 15: no comentário da questão da PM-MA, o material escreve "Bruno como coordenador e Bruno como assistente"; é erro de digitação (deveria ser André como assistente). Não afeta o resultado (2/30 = 1/15, cerca de 6,7%, item Errado).
- Pág. 11: a tabela do enunciado sobre dengue não foi extraída; usei apenas o método (casos favoráveis sobre o total). Pág. 12: a figura das cadeiras (P e X) também não; reconstruí o raciocínio em texto com números próprios (o do material, 4 cadeiras favoráveis em 10, confere com o gabarito).
- Pág. 8: o material anuncia a definição frequentista como alternativa, mas ela não faz parte deste trecho; mencionei apenas que existe, sem desenvolvê-la.
- Acrescentado fora do trecho: fórmulas de combinação e arranjo (revisão de análise combinatória, necessárias para os exemplos do próprio trecho) e a observação de que P do evento impossível é 0 e P do evento certo é 1 (decorre da fórmula n(A)/n(U)).
- Mais da metade do trecho é questão comentada; resumi o que elas ensinam (contagem, casos restantes, mesma regra de ordem em arranjo e combinação).
