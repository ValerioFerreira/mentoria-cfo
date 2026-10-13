---
id: S0408
agente: CLAUDE-L4
materia: Estatística
aula: Aula 06 — Probabilidade
trecho: estatistica/a06/s04
paginas_lidas: 43-58
---
# ANALÍTICO

Este trecho ensina a calcular a probabilidade de um evento quando já se sabe que outro ocorreu (probabilidade condicional), a usar essa ideia para obter a probabilidade de "A e B" (teorema da multiplicação) e a reconhecer quando um evento não altera o outro (independência).

### Probabilidade condicional

A informação de que um evento já aconteceu **reduz o universo**: passam a valer só os casos em que ele ocorre. A probabilidade de E **dado** H, escrita P(E|H), é a chance de E dentro desse universo menor:

**P(E|H) = P(E ∩ H) / P(H)**, com P(H) > 0

Em contagem, equivale a n(E ∩ H) / n(H): divide-se o número de casos em que os dois eventos ocorrem pelo número de casos do evento conhecido.

- O evento que se sabe ter ocorrido é o **evento a priori** (H, o que fica depois da barra e no denominador).
- O evento cuja probabilidade se quer é o **a posteriori** (E).
- Expressões que sinalizam a condição: "sabendo que", "dado que", "se", "entre os que".

> 💡 **Exemplo:** num concurso há 300 candidatos: 180 homens e 120 mulheres. Foram aprovados 90 homens e 45 mulheres (135 aprovados). A probabilidade de ser aprovado, sabendo que é mulher, é 45/120 = 3/8. Já a de ser mulher, sabendo que foi aprovado, é 45/135 = 1/3. **P(A|M) e P(M|A) são, em geral, diferentes**: o denominador muda.

> ⚠️ **Pegadinha:** não confunda P(E|H) com P(H|E) nem com P(E ∩ H). A interseção usa o universo inteiro (45/300 = 3/20); a condicional usa só o universo do evento conhecido.

#### Caso particular: um evento dentro do outro

Se E está contido em H, a interseção E ∩ H é o próprio E, e então P(E|H) = P(E) / P(H). No exemplo, se 8 dos 135 aprovados têm pós-graduação (P), então P(P|aprovado) = 8/135, já que todo aprovado com pós-graduação é aprovado.

#### Complementar condicional

A probabilidade condicional segue as regras comuns de probabilidade, **mantendo-se a condição**:

**P(não E | H) = 1 − P(E | H)**

No exemplo acima, a chance de não ser aprovada, sabendo que é mulher, é 1 − 3/8 = 5/8. O complemento vale só para o evento a posteriori: **P(E | não H) não é 1 − P(E|H)**. Da mesma forma, vale P(E ∪ F | H) = P(E|H) + P(F|H) − P(E ∩ F | H).

#### Obtendo a interseção a partir da condicional e da união

Em questões que dão P(A), P(B) e P(A|B), o roteiro é: primeiro P(A ∩ B) = P(A|B) × P(B); depois, a união: P(A ∪ B) = P(A) + P(B) menos a interseção recém-calculada.


> 💡 **Exemplo:** P(A) = 0,4, P(B) = 0,5 e P(A|B) = 0,2. Então P(A ∩ B) = 0,2 × 0,5 = 0,10 e P(A ∪ B) = 0,4 + 0,5 − 0,10 = 0,80.

### Teorema da multiplicação

É a fórmula da condicional "isolando" a interseção:

**P(A ∩ B) = P(B|A) × P(A)**

A probabilidade de os dois eventos ocorrerem é a do evento a priori vezes a probabilidade condicional do outro. A ordem pode ser **invertida**: P(A ∩ B) = P(A|B) × P(B) dá o mesmo resultado. No concurso acima, P(M ∩ A) = P(A|M) × P(M) = 3/8 × 120/300 = 3/8 × 2/5 = 3/20, igual a 45/300.

Para **três eventos**, a ideia se encadeia:

**P(A ∩ B ∩ C) = P(A) × P(B|A) × P(C|A ∩ B)**

Cada fator considera o que já aconteceu nas etapas anteriores. É o raciocínio de sorteios **sem reposição**.

> 💡 **Exemplo:** urna com 5 bolas pretas e 3 brancas. Duas bolas são retiradas sem reposição. A probabilidade de ambas serem pretas é 5/8 × 4/7 = 20/56 = 5/14, pois, depois da primeira preta, restam 4 pretas em 7 bolas.

#### Diagrama de árvore (etapas dependentes)

Quando o resultado de uma etapa muda as condições da seguinte, desenhe os caminhos possíveis. A regra é:
1. **ao longo de um caminho, multiplique** as probabilidades (o "e" de cada etapa);
2. **entre caminhos diferentes que levam ao resultado pedido, some** (o "ou"; os caminhos são mutuamente exclusivos).

> 💡 **Exemplo:** a caixa 1 tem 3 bolas azuis e 1 vermelha; a caixa 2 tem 2 azuis e 3 vermelhas. Escolhe-se uma caixa ao acaso e dela sai uma bola. P(azul) = 1/2 × 3/4 + 1/2 × 2/5 = 3/8 + 1/5 = 23/40.

### Independência de eventos

Dois eventos são **independentes** quando a ocorrência de um não altera a probabilidade do outro. Lançamentos sucessivos de um dado são o exemplo clássico. Em símbolos, a condição equivale a:

**P(B|A) = P(B)** (e, simetricamente, P(A|B) = P(A))

Consequência importante: se A e B são independentes, também são independentes os pares A e não B, não A e B, e não A e não B. Por isso valem P(B | não A) = P(B), P(não B | A) = P(não B) e P(não B | não A) = P(não B).

No teorema da multiplicação, substituindo P(B|A) por P(B):

**P(A ∩ B) = P(A) × P(B)**

Essa relação funciona como **teste de ida e volta**: sendo independentes, a interseção é o produto; e, se a interseção é igual ao produto das probabilidades, os eventos são independentes.

> 💡 **Exemplo:** P(A) = 1/2, P(B) = 1/6 e P(A ∩ B) = 1/12. Como 1/2 × 1/6 = 1/12, A e B são independentes (cara numa moeda e face 6 num dado, por exemplo). Se P(A ∩ B) fosse 1/10, seriam dependentes.

> ⚠️ **Pegadinha:** **independente não é o mesmo que mutuamente exclusivo**. Se A e B são mutuamente exclusivos, P(A ∩ B) = 0; com P(A) e P(B) positivas, o produto não é zero, logo os eventos são **dependentes** (ocorrer um impede o outro). Outra armadilha: só se pode usar P(A ∪ B) = P(A) + P(B) − P(A)·P(B) quando há independência garantida pelo enunciado.

#### "Pelo menos um": use o complementar

Em sequências de eventos independentes, a chance de **pelo menos um** ocorrer é 1 menos a chance de **nenhum** ocorrer.

> 💡 **Exemplo:** um atirador acerta o alvo com probabilidade 0,7 a cada disparo, de modo independente. Em 3 disparos, P(nenhum acerto) = 0,3 × 0,3 × 0,3 = 0,027, logo P(pelo menos um acerto) = 1 − 0,027 = 0,973.

### Para fixar

- P(E|H) = P(E ∩ H) / P(H): o universo passa a ser o evento conhecido (a priori), que vai no denominador.
- P(E|H) e P(H|E) geralmente são diferentes; não confundir com a interseção.
- Complementar condicional: P(não E | H) = 1 − P(E|H), com a mesma condição.
- Teorema da multiplicação: P(A ∩ B) = P(A) × P(B|A); com três eventos, P(A) × P(B|A) × P(C|A ∩ B).
- Em árvores, multiplica-se ao longo do caminho e somam-se os caminhos favoráveis.
- Independência: P(B|A) = P(B) e P(A ∩ B) = P(A) × P(B); vale a ida e a volta, e os complementares também são independentes.
- Eventos mutuamente exclusivos (com probabilidade positiva) não são independentes.
- "Pelo menos um" = 1 − P(nenhum).

# SINTÉTICO

- **Probabilidade condicional**: P(E|H) = P(E ∩ H) / P(H); o evento conhecido (a priori) reduz o universo e fica no denominador.
- **Ordem importa**: P(E|H) e P(H|E) em geral diferem, pois o denominador muda; a interseção, sem condição, usa o universo inteiro.
- **Caso contido**: se E está dentro de H, P(E|H) = P(E) / P(H).
- **Complementar condicional**: P(não E | H) = 1 − P(E|H); a condição H permanece.
- **Teorema da multiplicação**: P(A ∩ B) = P(A) × P(B|A), com a ordem trocável; para três eventos, P(A) × P(B|A) × P(C|A ∩ B), típico de sorteio sem reposição.
- **Árvore de probabilidades**: multiplica-se ao longo de cada caminho e somam-se os caminhos que levam ao resultado pedido.
- **Independência**: P(B|A) = P(B) e P(A ∩ B) = P(A) × P(B); a relação vale nos dois sentidos e os complementares também são independentes.
- **Independente × exclusivo**: exclusivos com probabilidades positivas são dependentes, pois P(A ∩ B) = 0 difere do produto.
- **Pelo menos um**: calcule 1 − P(nenhum); com independência, a chance de nenhum é o produto das chances de não ocorrer em cada tentativa.

# NOTAS

- O texto original traz muitas questões comentadas (págs. 45–48, 50–53, 55–58); só a teoria foi aproveitada. As figuras e gráficos (tabela de enfermeiros e dentistas, gráfico de candidatos, quadro das famílias, diagrama de urnas) foram descartados; os exemplos do resumo são próprios.
- A pág. 58 termina cortada (questão da tuberculose com "pelo menos um"); o método do complementar foi reconstruído com exemplo próprio, sem usar o resultado da questão.
- Acrescentados por conhecimento padrão e não constantes do trecho: a ressalva P(H) > 0, a diferença entre independência e exclusão mútua, e o aviso de que P(E | não H) não é 1 − P(E|H).
