---
id: S0478
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s02
paginas_lidas: 13-24
---
# ANALÍTICO

A distribuição exponencial modela o tempo até um evento acontecer (falha, chegada, decaimento) quando a taxa de ocorrência é constante. O trecho cobre a função densidade, o cálculo de probabilidades, a esperança e a variância, a ligação com Poisson e as propriedades que mais caem em prova: a falta de memória, a escala e o mínimo de exponenciais.

### Função densidade e parâmetro

Uma variável contínua X tem distribuição exponencial com parâmetro **λ > 0** (a **taxa** de falha ou de ocorrência por unidade de tempo) quando:

- f(x) = λ · e^(−λx), para x ≥ 0;
- f(x) = 0, para x < 0.

O número e vale aproximadamente 2,718, e é comum escrever e^(−λx) como exp{−λx}. Como o tempo não pode ser negativo, a densidade só é diferente de zero na parte positiva do eixo. O gráfico é **sempre decrescente**: o valor mais provável fica perto de zero, e a curva cai de forma suave rumo ao infinito. λ é o único parâmetro: conhecendo-o, a distribuição inteira fica determinada.

> 💡 **Exemplo:** se um servidor falha, em média, a cada 50 horas, a taxa é λ = 1/50 = 0,02 por hora. Já uma bactéria com λ = 1/4 por dia tem taxa de uma "falha" a cada 4 dias.

### Probabilidades e função de distribuição acumulada

Integrando a densidade, obtêm-se três fórmulas que resolvem quase todas as questões de cálculo:

| Quero | Fórmula |
| --- | --- |
| P(X < x) (também vale com ≤) | 1 − e^(−λx) |
| P(X > x) (também vale com ≥) | e^(−λx) |
| P(a < X < b) | e^(−λa) − e^(−λb) |

A primeira é a própria **função de distribuição acumulada**: F(x) = 1 − e^(−λx). Em variável contínua, a probabilidade de um ponto isolado é zero, então "menor que" e "menor ou igual" dão o mesmo resultado. Na terceira fórmula, o limite **menor (a) vem primeiro** porque a função e^(−λx) é decrescente: e^(−λa) é maior que e^(−λb), e a diferença sai positiva. Para P(X < b) basta fazer a = 0, o que reproduz 1 − e^(−λb).

> 💡 **Exemplo:** o tempo de resposta de um atendimento tem média de 8 minutos, logo λ = 1/8. A chance de passar de 16 minutos é e^(−16/8) = e^(−2) ≈ 0,135. A chance de terminar em menos de 4 minutos é 1 − e^(−1/2) ≈ 0,39.

> ⚠️ **Pegadinha:** λ e x precisam estar na **mesma unidade de tempo**. Com λ = 1/12 por dia e x = 6 horas, converta: 6 h = 1/4 de dia, e P(X < 1/4) = 1 − e^(−(1/12)·(1/4)) = 1 − e^(−1/48). Se a questão der a média em minutos e pedir horas, ajuste antes de aplicar a fórmula.

### Resolvendo para o tempo desconhecido (uso do logaritmo)

Quando a probabilidade é dada e o tempo é a incógnita (percentil), isola-se o expoente e aplica-se o logaritmo natural, usando ln(e^y) = y:

- Se P(X ≤ d) = 0,75 com λ = 2: 1 − e^(−2d) = 0,75, então e^(−2d) = 0,25 e d = −ln(0,25)/2 = ln(4)/2 ≈ 0,69.
- Se a exigência é "cumprir o limite de T minutos em pelo menos 90% dos casos", escreve-se 1 − e^(−λT) ≥ 0,9, ou seja, e^(−λT) ≤ 0,1; aplicando ln, −λT ≤ −ln(10), e portanto **λ ≥ ln(10)/T**. Ao multiplicar ou dividir por número negativo, o sentido da desigualdade se inverte.
- Quando a taxa é desconhecida mas há um dado de um instante, descubra e^(−λ) e eleve a potências. Se 60% já decaíram em 1 ano, e^(−λ) = 0,4; em 2 anos o que sobra é (e^(−λ))² = 0,16 e a fração decaída é 1 − 0,16 = 84%.

### Função de confiabilidade e sistemas redundantes

Quando X representa o tempo até a falha, a **confiabilidade** é a probabilidade de o sistema **não falhar** até x: R(x) = 1 − F(x) = e^(−λx).

Se um sistema tem várias unidades independentes e **redundantes** (basta uma funcionar; o sistema só falha se todas falharem), a probabilidade de o sistema ter falhado até x é o **produto** das probabilidades individuais (interseção de eventos independentes): F_sistema(x) = F1(x) · F2(x) · ... · Fn(x). A confiabilidade do sistema é o complemento desse produto.

### Esperança, variância e desvio padrão

Com a parametrização pela taxa λ:

| Medida | Valor |
| --- | --- |
| Esperança E(X) | 1/λ |
| Variância Var(X) | 1/λ² |
| Desvio padrão | 1/λ |
| Coeficiente de variação (desvio ÷ média) | 1 |

O desvio padrão é igual à média, então o coeficiente de variação vale **1 para qualquer exponencial**, seja qual for λ. Exemplo: com λ = 0,05 por hora, E(X) = 20 h, Var(X) = 400 e desvio padrão = 20 h.

#### Parametrização alternativa pela escala

Muitas provas escrevem a densidade como f(x) = (1/β) · e^(−x/β), para x ≥ 0, com β = 1/λ. O parâmetro **β é a escala**, medido em unidade de tempo, e coincide com a média: **E(X) = β** e **Var(X) = β²**. Cuidado ao identificar qual versão a questão usa: se o enunciado diz "média β = 15 anos", então λ = 1/15.

### Relação com a distribuição de Poisson

Se o número de ocorrências por unidade de tempo segue Poisson com parâmetro λ, então o **tempo entre duas ocorrências consecutivas** segue exponencial com o **mesmo λ**. Chegadas de clientes em média 2 por hora (Poisson) implicam tempo entre chegadas exponencial de parâmetro 2 por hora, com média 1/2 hora (30 minutos). Poisson conta eventos; a exponencial mede a espera entre eles.

### Propriedades

#### Mudança de escala
Se X é exponencial com parâmetro λ e k > 0 é constante, então **Y = k·X** é exponencial com parâmetro **λ/k**. Exemplo: X com λ = 3 e Y = 6X resultam em λ_Y = 0,5, média 2, que é exatamente 6 vezes a média de X (1/3).

#### Mínimo de exponenciais independentes
O menor valor entre n exponenciais independentes, Z = min{X1, ..., Xn}, é exponencial com parâmetro igual à **soma** dos parâmetros: λ_Z = λ1 + ... + λn. Intuição: quanto mais "relógios" correndo, mais cedo o primeiro toca. Exemplo: duas peças com λ = 0,3 e λ = 0,2 por hora; o tempo até a primeira falha tem λ = 0,5 e média de 2 horas. Se duas exponenciais independentes têm variância 1, então λ = 1 em cada uma (Var = 1/λ² = 1, com λ positivo); o mínimo tem λ = 2 e média 0,5.

> ⚠️ **Pegadinha:** a soma de parâmetros vale para o **mínimo**, não para o máximo, e não para a soma das variáveis.

#### Falta de memória
É a propriedade mais cobrada: **P(X > t + s | X > s) = P(X > t)**. Ter esperado s unidades sem o evento não muda a probabilidade de esperar mais t. O processo "esquece" o passado.

> 💡 **Exemplo:** um componente com vida exponencial de média 15 anos já durou 3 anos. A chance de durar ao menos mais 9 (até 12 no total) é P(X > 9) = e^(−9/15) = e^(−0,6). A chance de falhar antes dos 12 anos, dado que sobreviveu aos 3, é 1 − e^(−0,6).

> ⚠️ **Pegadinha:** a probabilidade condicional depende apenas do tempo **adicional** (t), nunca do tempo já decorrido (s) nem do total t + s. Na questão, é preciso identificar quanto tempo "a mais" se pede.

### Para fixar
- Densidade λ·e^(−λx) para x ≥ 0; λ > 0 é a taxa por unidade de tempo e é o único parâmetro.
- P(X > x) = e^(−λx); P(X < x) = 1 − e^(−λx); P(a < X < b) = e^(−λa) − e^(−λb).
- E(X) = 1/λ; Var(X) = 1/λ²; desvio = média, logo CV = 1.
- Com parametrização pela escala β = 1/λ: E(X) = β e Var(X) = β².
- Tempo entre eventos de um Poisson de parâmetro λ é exponencial com o mesmo λ.
- Y = kX tem parâmetro λ/k; mínimo de exponenciais independentes tem parâmetro igual à soma.
- Sem memória: P(X > t+s | X > s) = P(X > t); só conta o tempo adicional.
- Antes de calcular, alinhe as unidades de x e λ; para achar tempos, use o logaritmo natural.

# SINTÉTICO

- **Modelo**: a exponencial descreve o tempo até um evento com taxa constante λ > 0; f(x) = λ·e^(−λx) para x ≥ 0, decrescente.
- **Probabilidades**: P(X > x) = e^(−λx); P(X < x) = 1 − e^(−λx), que é a função acumulada; P(a < X < b) = e^(−λa) − e^(−λb).
- **Unidades**: x e λ devem estar na mesma unidade de tempo; converta antes de aplicar as fórmulas.
- **Média e variância**: E(X) = 1/λ e Var(X) = 1/λ², então desvio padrão igual à média e coeficiente de variação sempre 1.
- **Parametrização por escala**: com β = 1/λ, a densidade é (1/β)·e^(−x/β), E(X) = β e Var(X) = β².
- **Poisson**: se as ocorrências são Poisson com taxa λ, o tempo entre elas é exponencial com o mesmo λ.
- **Confiabilidade e redundância**: R(x) = 1 − F(x) = e^(−λx); em sistema redundante, a probabilidade de falha é o produto das acumuladas das unidades.
- **Escala**: Y = k·X (k > 0) é exponencial com parâmetro λ/k.
- **Mínimo**: o mínimo de exponenciais independentes é exponencial com parâmetro igual à soma dos parâmetros.
- **Sem memória**: P(X > t+s | X > s) = P(X > t); o passado não altera a espera futura, só o tempo adicional importa.

# NOTAS

nenhuma. O trecho tem a continuação de questões comentadas nas págs. 16–24 (usadas apenas para os métodos: percentil com logaritmo, condição de 90% e uso da falta de memória). Páginas todas legíveis; as fórmulas foram conferidas contra as resoluções das questões.
