---
id: S0470
agente: CLAUDE-L4
materia: Estatística
aula: Aula 01 — Médias
trecho: estatistica/a01/s05
paginas_lidas: 59-69
---
# ANALÍTICO

Este trecho trata da média harmônica (definição, fórmula, aplicações em velocidade e tempo de trabalho) e da desigualdade que ordena as três médias clássicas: aritmética, geométrica e harmônica.

### Média harmônica: ideia e fórmula

A **média harmônica (H)** é a média adequada quando as grandezas envolvidas são **inversamente proporcionais**, como velocidade e tempo (para uma distância fixa) ou vazão e tempo de enchimento. É definida para conjuntos de números **positivos** e vale o **inverso da média aritmética dos inversos**.

A lógica é a mesma das outras médias: H é o número que, colocado no lugar de todos os elementos, mantém igual a **soma dos inversos**. Para n valores x1, x2, ..., xn:

**n / H = 1/x1 + 1/x2 + ... + 1/xn**, logo **H = n / (1/x1 + 1/x2 + ... + 1/xn)**

Em palavras: some os inversos, divida n por essa soma. Ou, como diz a definição, tire a média aritmética dos inversos e inverta o resultado.

> 💡 **Exemplo:** H de 10 e 40. Soma dos inversos: 1/10 + 1/40 = 4/40 + 1/40 = 5/40 = 1/8. H = 2 / (1/8) = 16. Conferência da propriedade: 1/16 + 1/16 = 1/8, a mesma soma de inversos da lista original.

**Atalho para dois números a e b:** H = 2·a·b / (a + b), isto é, o dobro do produto dividido pela soma. Com 10 e 40: 2 × 400 / 50 = 16. Para três ou mais números, o atalho não existe e é preciso somar os inversos com MMC.

**Restrição de domínio:** os valores precisam ser positivos. Com zero haveria divisão por zero (1/0); com valores positivos e negativos misturados, a soma dos inversos pode dar zero (por exemplo, 1 e −1), e H deixaria de existir. Por isso a definição se limita a números positivos.

### Aplicação 1: velocidade média

Se um veículo percorre **distâncias iguais** em velocidades diferentes, a velocidade média do trajeto inteiro é a **média harmônica** das velocidades. Quanto maior a velocidade, menor o tempo gasto para a mesma distância; as grandezas são inversamente proporcionais.

> 💡 **Exemplo:** ida a 60 km/h e volta a 90 km/h (mesma distância). v_méd = 2·60·90 / (60 + 90) = 10800/150 = 72 km/h. Repare que não é a média aritmética (75 km/h): na velocidade menor se gasta mais tempo, e isso puxa a média para baixo.

> ⚠️ **Pegadinha:** a média harmônica só serve para velocidade média quando as **distâncias** parciais são iguais. Se o veículo ficasse tempos iguais em cada velocidade, a velocidade média seria a aritmética. Em caso de dúvida, use a definição física: distância total ÷ tempo total.

### Aplicação 2: tempo de trabalho conjunto (torneiras)

Quando um agente leva t1 e outro leva t2 para fazer a mesma tarefa, o tempo médio individual é a harmônica dos dois. Mas, trabalhando **juntos**, o tempo é esse valor dividido pelo número de agentes (porque juntos eles produzem n vezes mais rápido que um agente médio).

Passos: calcular H dos tempos; dividir por n.

> 💡 **Exemplo:** uma torneira enche um tanque em 10 h e outra em 15 h. H = 2·10·15 / (10 + 15) = 300/25 = 12 h. Juntas: 12 / 2 = 6 h. Conferência pela soma das vazões: 1/10 + 1/15 = 1/6 do tanque por hora, ou seja, 6 horas.

### Resolvendo questões que misturam as médias

Quando a prova pede comparações ou cálculos com mais de uma média, calcule cada uma separadamente:

- **aritmética:** soma ÷ n;
- **geométrica:** raiz n-ésima do produto (raiz cúbica de três valores, por exemplo);
- **harmônica:** n ÷ soma dos inversos.

Para raízes não exatas, teste valores próximos (por exemplo, 3,3³ ≈ 35,9 mostra que a raiz cúbica de 36 é cerca de 3,3). Muitas vezes a alternativa tem diferença grande e a aproximação basta.

> 💡 **Exemplo:** para 2, 8 e 4, a média aritmética vale 14/3 ≈ 4,67; a geométrica é a raiz cúbica de 64, igual a 4; a harmônica é 3 / (1/2 + 1/8 + 1/4) = 3 / (7/8) = 24/7 ≈ 3,43.

### Desigualdade das médias

Para uma lista de números **positivos**:

**média aritmética ≥ média geométrica ≥ média harmônica** (x̄ ≥ G ≥ H)

A **igualdade só ocorre quando todos os números são iguais**; se ao menos um for diferente, as desigualdades são estritas.

| Lista | Aritmética | Geométrica | Harmônica |
| --- | --- | --- | --- |
| 1, 2, 4 | 2,33 | 2 | 1,71 |
| 2, 8 | 5 | 4 | 3,2 |
| 7, 7, 7 | 7 | 7 | 7 |

A ordem x̄ ≥ G ≥ H serve para julgar afirmativas sem calcular (por exemplo, "a média harmônica de números positivos e distintos nunca supera a aritmética") e para resolver questões de desigualdade com letras.

> 💡 **Curiosidade útil:** para apenas **dois** números positivos, vale G² = x̄ · H, isto é, a geométrica é a média geométrica entre a aritmética e a harmônica. Com 2 e 8: 5 × 3,2 = 16 = 4².

#### Raciocínio com a desigualdade

Em questões com a, b, c positivos, usam-se ao mesmo tempo três ideias: (1) a média geométrica de dois números fica **entre** eles; (2) a média aritmética supera a geométrica dos mesmos números; (3) se raiz de uma coisa é menor que raiz de outra, elevar ao quadrado mantém o sentido (todos positivos). Combinando, obtém-se a ordem entre as letras. A alternativa é testar valores numéricos coerentes com as condições dadas e eliminar as afirmações falsas.

### Para fixar
- Média harmônica: H = n / (soma dos inversos); é o inverso da média aritmética dos inversos.
- Só vale para números positivos; para dois números, H = 2ab / (a + b).
- Aplica-se a grandezas inversamente proporcionais: velocidade média com distâncias iguais; tempo médio de agentes que realizam a mesma tarefa.
- Trabalhando em conjunto, o tempo total é a média harmônica dos tempos dividida pelo número de agentes.
- Desigualdade das médias: aritmética ≥ geométrica ≥ harmônica, com igualdade apenas quando todos os valores são iguais.
- Para dois números, G² = aritmética × harmônica.
- Em questões de médias, calcule cada média com cuidado e use valores numéricos de teste para checar alternativas.

# SINTÉTICO

- **Definição**: H = n / (1/x1 + ... + 1/xn), o inverso da média aritmética dos inversos; preserva a soma dos inversos da lista.
- **Domínio**: apenas números positivos; zero ou valores que anulem a soma dos inversos tornam a conta impossível.
- **Atalho para dois números**: H = 2ab / (a + b), o dobro do produto dividido pela soma; com 10 e 40, H = 16.
- **Velocidade média**: com distâncias iguais, é a harmônica das velocidades; 60 e 90 km/h dão 72 km/h, abaixo da aritmética (75).
- **Tempo conjunto**: tarefas de 10 h e 15 h têm H = 12 h; juntos gastam 12/2 = 6 h (confira somando as vazões 1/10 + 1/15).
- **Quando usar**: grandezas inversamente proporcionais; se o tempo em cada velocidade for igual, a média é a aritmética.
- **Desigualdade das médias**: para números positivos, aritmética ≥ geométrica ≥ harmônica, o que permite julgar afirmativas sem calcular.
- **Igualdade**: as três médias coincidem somente quando todos os números da lista são iguais; basta um diferente para a desigualdade ser estrita.
- **Exemplo numérico**: para 1, 2 e 4, as médias aritmética, geométrica e harmônica valem 2,33, 2 e 1,71, nessa ordem decrescente.
- **Relação entre três médias**: só para dois números, o quadrado da geométrica é o produto da aritmética pela harmônica; com 2 e 8, 4² = 5 × 3,2.

# NOTAS

- Pág. 63: o material diz que a média harmônica é definida para números "não-negativos" e que não seria possível calcular "a média geométrica de 1 e -1"; o correto é positivos (o zero também inviabiliza a conta) e o exemplo se refere à harmônica (soma dos inversos de 1 e −1 é zero). No resumo usei "positivos" e a harmônica.
- A propriedade G² = x̄·H para dois números, o atalho H = 2ab/(a+b) (este está no material, pág. 64) e a ressalva sobre tempos iguais na velocidade média: a primeira e a última foram acrescentadas fora do trecho, regras estáveis.
- Pág. 62: o exemplo das torneiras calcula primeiro a média harmônica dos tempos (8 h) e divide por 2 (4 h), coerente com a soma das vazões (1/12 + 1/6 = 1/4). Conferido.
- Pág. 65: no exercício da raiz cúbica de 36, a aproximação 3,3 foi usada; o gabarito do material (6,3) depende dela.
- Mais da metade do trecho é questão comentada; resumi os métodos (atalho para dois números, aproximação de raízes, uso da desigualdade com letras). Nenhuma página vazia.
