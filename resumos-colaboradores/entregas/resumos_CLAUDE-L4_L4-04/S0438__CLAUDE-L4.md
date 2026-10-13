---
id: S0438
agente: CLAUDE-L4
materia: Estatística
aula: Aula 06 — Probabilidade
trecho: estatistica/a06/s03
paginas_lidas: 29-42
---
# ANALÍTICO

Este trecho ensina a calcular probabilidades "pelo lado de fora": a probabilidade do evento complementar, as relações entre complementares, uniões e interseções (as leis de De Morgan aplicadas a probabilidades) e os axiomas de Kolmogorov, dos quais derivam as propriedades básicas de qualquer probabilidade.

### Teorema do evento complementar

O **complementar** de um evento A (indicado por A com barra, A^c ou A') reúne todos os elementos do espaço amostral U que **não** pertencem a A. Evento e complementar nunca se sobrepõem e, juntos, formam o espaço inteiro. Logo:

n(A) + n(A^c) = n(U)

Dividindo tudo por n(U), obtém-se:

- **P(A) + P(A^c) = 1**, ou seja, **P(A^c) = 1 − P(A)**.

É a ferramenta ideal para perguntas do tipo "pelo menos um", "nenhum", "não seja de tal tipo", em que contar o oposto é mais curto.

> 💡 **Exemplo:** num sorteio de um cartão numerado de 1 a 20, seja A = "número múltiplo de 5" = {5, 10, 15, 20}. P(A) = 4/20 = 1/5. A probabilidade de **não** ser múltiplo de 5 é 1 − 1/5 = 4/5 (16 cartões em 20).

> 💡 **Exemplo:** uma urna tem 10 bolas vermelhas, 3 azuis e 2 pretas (15 no total). P(vermelha) = 10/15. P(não vermelha) = 1 − 10/15 = 5/15 = 1/3, aproximadamente 33,33%. Conferindo por contagem direta: 3 + 2 = 5 bolas em 15.

> 💡 **Exemplo:** num tabuleiro com 144 casas, das quais 30 são marrons, P(marrom) = 30/144. P(não marrom) = 1 − 30/144 = 114/144 ≈ 0,79. Se a questão afirmasse que esse valor é inferior a 0,72, o item seria errado.

### Complementar da união e da interseção

O teorema vale também quando o evento é formado por combinação de outros:

- **P(complementar de A∪B) = 1 − P(A∪B)**
- **P(complementar de A∩B) = 1 − P(A∩B)**

Duas igualdades, equivalentes às leis de De Morgan da teoria dos conjuntos, são muito cobradas:

| Situação em palavras | Notação | Resultado |
| --- | --- | --- |
| **Nem A nem B** (não A **e** não B) | P(A^c ∩ B^c) | = P(complementar de A∪B) = **1 − P(A∪B)** |
| **Não A ou não B** (pelo menos um dos dois não ocorre) | P(A^c ∪ B^c) | = P(complementar de A∩B) = **1 − P(A∩B)** |

Raciocínio de "nem A nem B": quem não está em A e não está em B está fora de qualquer um dos dois, isto é, fora da união. Raciocínio de "não A ou não B": só escapa dessa condição quem está em A **e** em B ao mesmo tempo, isto é, na interseção; todos os demais satisfazem a condição.

> 💡 **Exemplo (dado):** U = {1, 2, 3, 4, 5, 6}, A = {2, 4, 6} (pares) e B = {1, 2, 3} (menores que 4). A∪B = {1, 2, 3, 4, 6}, P(A∪B) = 5/6, e então P(nem A nem B) = 1 − 5/6 = 1/6 (é o resultado {5}). Já A∩B = {2}, com probabilidade 1/6; assim P(não A ou não B) = 1 − 1/6 = 5/6, que são todos os resultados menos o 2.

Para três eventos vale o mesmo padrão:

- P(A^c ∩ B^c ∩ C^c) = 1 − P(A∪B∪C) (nenhum dos três);
- P(A^c ∪ B^c ∪ C^c) = 1 − P(A∩B∩C) (pelo menos um deles não ocorre).

> ⚠️ **Pegadinha:** não confunda "nem A nem B" com "não A ou não B". A primeira exige que **nenhum** ocorra (resultado geralmente menor); a segunda exige apenas que **algum** deixe de ocorrer (resultado geralmente maior).

### Aplicações típicas

A probabilidade da união usa a fórmula P(A∪B) = P(B) + P(A) − P(A∩B). Para três conjuntos, soma-se as três probabilidades simples, subtraem-se as três interseções duas a duas e acrescenta-se de volta a interseção tripla.

> 💡 **Exemplo (nem A nem B):** P(A) = 20%, P(B) = 30% e P(A∩B) = 10%. A união vale 20% + 30% − 10% = 40%, logo a probabilidade de nenhum ocorrer é 100% − 40% = 60%.

> 💡 **Exemplo (eventos excludentes):** em um estádio com 1000 pessoas, 440 torcem pelo time A e 320 pelo time B, e ninguém torce pelos dois. Como A∩B é vazio, P(A∪B) = 44% + 32% = 76%, e a chance de sortear alguém que não torce por nenhum é 24%.

> 💡 **Exemplo (três conjuntos):** numa pesquisa com 200 consumidores de pastas de dente, 76 usam A, 86 usam B, 140 usam C, 68 usam A e B, 34 usam A e C, 48 usam B e C e 30 usam as três. Número de usuários de ao menos uma marca = 76 + 86 + 140 − 68 − 34 − 48 + 30 = 182. Ninguém usando nenhuma: 200 − 182 = 18, ou seja, 18/200 = 9%. Também é possível montar o diagrama de Venn de dentro para fora (primeiro a interseção tripla, depois as duplas, depois as regiões só de uma marca) e somar as regiões; o resultado é o mesmo. Quando o enunciado pede "consome apenas uma marca", soma-se somente as regiões exclusivas de cada conjunto.

### Axiomas de Kolmogorov

Axiomas são afirmações básicas aceitas sem demonstração, a partir das quais tudo mais se deduz. Os três axiomas da probabilidade são:

1. **P(A) ≥ 0**: não existe probabilidade negativa.
2. **P(U) = 1**: o espaço amostral inteiro (todos os resultados possíveis) tem probabilidade 100%.
3. **Aditividade**: se A e B são **mutuamente excludentes** (A∩B = vazio), então **P(A∪B) = P(A) + P(B)**.

### Propriedades que decorrem dos axiomas

| Nº | Propriedade | Observação |
| --- | --- | --- |
| i | Se A é o evento impossível (conjunto vazio), P(A) = 0 | a volta nem sempre vale |
| ii | 0 ≤ P(A) ≤ 1 | probabilidade fica entre 0 e 100% |
| iii | P(A − B) = P(A\B) = P(A) − P(A∩B) | A **e não** B: só a parte de A fora de B |
| iv | Se A está contido em B, então P(A) ≤ P(B) | evento "menor" não é mais provável que o "maior" |
| v | P(A∪B) = P(A) − P(A∩B) + P(B) | união de eventos quaisquer |
| vi | P(A^c) = 1 − P(A) | complementar |

> ⚠️ **Pegadinha (probabilidade zero não é impossibilidade):** todo evento impossível tem probabilidade zero, mas o inverso é falso. Em situações com infinitas possibilidades, um evento possível pode ter probabilidade nula; exemplo clássico: lançar uma moeda infinitas vezes e obter cara em todos. Simetricamente, evento certo tem probabilidade 1, mas probabilidade 1 não prova que o evento seja certo. Um item que diga "probabilidade zero significa que o evento não pode ocorrer" está errado.

> ⚠️ **Pegadinha (soma só vale para excludentes):** a probabilidade da união de vários eventos só é a soma das probabilidades quando eles são mutuamente excludentes. Um enunciado que afirme "P(união de A1,...,An) = soma de P(Aj)" para eventos quaisquer está errado, pois as interseções seriam contadas em duplicidade.

> 💡 **Decomposição da união:** a união de A e B pode ser fatiada em três partes sem sobreposição: só A (A∩B^c), só B (A^c∩B) e ambos (A∩B). Portanto P(A∪B) é a soma de P(A∩B^c), P(A^c∩B) e P(A∩B). Esta igualdade é correta e já apareceu em prova.

### Distribuição de probabilidade e a soma igual a 1

Quando o enunciado apresenta uma tabela de probabilidades de todos os valores possíveis, o axioma 2 manda que a soma seja 1. Isso serve para achar uma constante desconhecida.

> 💡 **Exemplo:** um evento ocorre de 0 a 5 vezes por dia, com probabilidades 0,20; p; 2p; 3p; 2p; p (nessa ordem, de 0 a 5 ocorrências). Soma: 0,20 + 9p = 1, então p = 0,8/9 = 8/90. A chance de ocorrer ao menos uma vez e no máximo três é P(1) + P(2) + P(3) = p + 2p + 3p = 6p = 48/90 = 8/15.

### Diferença de conjuntos com dados numéricos

> 💡 **Exemplo (usando A − B):** em 100 pessoas, 80 têm celular (C), 50 têm telefone fixo (F) e 10 não têm nenhum dos dois. Logo 90 têm pelo menos um: 80 + 50 − n(C∩F) = 90, e n(C∩F) = 40. Quem tem fixo mas não celular: n(F) − n(C∩F) = 50 − 40 = 10, e a probabilidade é 10/100 = 10%.

### Para fixar
- **P(A^c) = 1 − P(A)**: use o complemento em perguntas do tipo "nenhum", "pelo menos um" e "não seja".
- **Nem A nem B** = 1 − P(A∪B); **não A ou não B** = 1 − P(A∩B). Para três eventos, o mesmo vale com A∪B∪C e A∩B∩C.
- Eventos mutuamente excludentes: P(A∪B) = P(A) + P(B); caso contrário, subtraia P(A∩B).
- Axiomas de Kolmogorov: P(A) ≥ 0; P(U) = 1; aditividade para excludentes. Daí vêm 0 ≤ P ≤ 1 e P(vazio) = 0.
- P(A − B) = P(A) − P(A∩B); se A está contido em B, então P(A) ≤ P(B).
- Evento impossível tem probabilidade 0, mas probabilidade 0 não implica evento impossível (idem para 1 e evento certo).
- Distribuição completa de probabilidades soma 1: use isso para encontrar constantes.

# SINTÉTICO

- **Complementar**: P(A^c) = 1 − P(A); evento e complemento somam 100% e juntos formam todo o espaço amostral. É o atalho para "nenhum", "pelo menos um" e "não seja".
- **Nem A nem B**: é a interseção dos complementares e vale 1 − P(A∪B); primeiro calcule a união (P(A) + P(B), menos P(A∩B)) e depois subtraia de 1.
- **Não A ou não B**: é a união dos complementares e vale 1 − P(A∩B); só fica de fora quem satisfaz A e B ao mesmo tempo.
- **Três eventos**: nenhum ocorre = 1 − P(A∪B∪C); algum falha = 1 − P(A∩B∩C). A união de três usa soma das simples, menos duplas, mais a tripla.
- **Axiomas de Kolmogorov**: P(A) ≥ 0; P(U) = 1; para eventos excludentes P(A∪B) = P(A) + P(B). De lá saem 0 ≤ P ≤ 1 e P(vazio) = 0.
- **Diferença**: P(A − B) = P(A) − P(A∩B), a parte de A fora de B; se A está contido em B, P(A) ≤ P(B).
- **Zero não é impossível**: evento impossível tem probabilidade 0, mas o inverso é falso (infinitas caras seguidas, por exemplo); do mesmo modo, probabilidade 1 não garante evento certo.
- **Soma só para excludentes**: somar probabilidades de eventos quaisquer, sem tirar as interseções, dá resposta errada.
- **Tabela de probabilidades**: a soma de todas as probabilidades é 1; monte a equação para achar a constante desconhecida e depois some só os casos pedidos.

# NOTAS

- Página 29 começa com os resquícios do diagrama de Venn de uma questão iniciada no trecho anterior (resultado 76%, soma de três regiões exclusivas); usei só o raciocínio geral ("apenas uma marca" soma as regiões exclusivas), sem reconstruir o enunciado.
- Diagramas das páginas 31 a 34, 39 e 41 não foram extraídos; o conteúdo deles é descrito pelo texto e foi reconstruído em palavras.
- Tabela de probabilidades da questão da página 40 não foi extraída; os coeficientes (0,20; p; 2p; 3p; 2p; p) foram deduzidos da equação do gabarito comentado.
- O terceiro axioma está apresentado só para dois eventos (aditividade finita), como no material; a versão formal para sequências infinitas de eventos não é tratada no trecho.
