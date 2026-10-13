---
id: S0440
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s05
paginas_lidas: 50-61
---
# ANALÍTICO

O desvio-padrão é a medida de dispersão mais usada em provas: resume, numa única medida e na unidade dos dados, o quanto os valores se afastam da média. O trecho define a medida, apresenta as fórmulas populacional e amostral, ensina o cálculo para dados soltos, em tabela de frequências e em classes, e mostra como ela se comporta quando os dados são somados ou multiplicados por uma constante.

### Conceito e leitura da medida

O **desvio-padrão** é a **raiz quadrada da variância**, isto é, a raiz da média dos quadrados dos desvios em relação à média. Elevar ao quadrado elimina o sinal dos desvios (que, somados, dariam zero) e a raiz devolve o resultado à unidade original dos dados.

- Valores concentrados perto da média produzem desvio-padrão pequeno; valores espalhados produzem desvio-padrão grande.
- É **sempre maior ou igual a zero** (não existe desvio-padrão negativo).
- É **igual a zero apenas quando todos os valores são iguais**: nesse caso a média coincide com o valor repetido e todos os desvios são nulos.
- Tem a **mesma unidade** dos dados (a variância fica na unidade ao quadrado).
- Serve para comparar a variabilidade de dois conjuntos quando as **médias são aproximadamente iguais** e as **unidades de medida são idênticas**.

> ⚠️ **Pegadinha:** variância igual a zero implica desvio-padrão igual a zero (e vice-versa), mas **não** implica média, mediana ou moda iguais a zero. Se todos os dados valem 7, variância e desvio-padrão são 0, e a média, a mediana e a moda valem 7.

### Fórmulas: população × amostra

| Situação | Símbolo | Fórmula | Divisor |
| --- | --- | --- | --- |
| População (todos os elementos) | σ (sigma) | raiz de [soma de (x_i − μ)² / n] | n |
| Amostra (parte da população) | s | raiz de [soma de (x_i − x̄)² / (n − 1)] | n − 1 |

Na população usa-se a média populacional μ; na amostra, a média amostral x̄. O divisor **n − 1** na amostra produz uma estimativa melhor do parâmetro populacional. Há também uma justificativa intuitiva: como a soma dos desvios em torno da média é sempre zero, apenas n − 1 desvios são independentes, pois os n − 1 primeiros determinam o último.

A relação entre as duas variâncias: variância amostral = variância populacional × n/(n − 1). Assim, para os mesmos dados, **s é sempre um pouco maior do que σ**, e a diferença diminui quanto maior for n.

> ⚠️ **Pegadinha:** a primeira decisão em toda questão é ler se os dados são "população" ou "amostra". Sem essa informação, o divisor correto não pode ser escolhido.

### Dados não agrupados

Passos: (1) média; (2) desvio de cada valor; (3) quadrado de cada desvio; (4) soma dos quadrados; (5) divisão por n (população) ou n − 1 (amostra); (6) raiz quadrada.

> 💡 **Exemplo:** conjunto {2, 4, 4, 6, 9}. Média = 25/5 = 5. Desvios: −3, −1, −1, 1, 4. Quadrados: 9, 1, 1, 1, 16; soma = 28. Como população: σ² = 28/5 = 5,6 e σ ≈ 2,37. Como amostra: s² = 28/4 = 7 e s ≈ 2,65.

**Atalho para a variância**: variância populacional = (média dos quadrados dos valores) − (quadrado da média). Útil quando os valores são grandes e os desvios, trabalhosos. No exemplo: quadrados dos valores 4, 16, 16, 36, 81, soma 153; média dos quadrados = 30,6; quadrado da média = 25; variância = 5,6. Para passar à amostral, multiplique por n/(n − 1) (5,6 × 5/4 = 7).

> 💡 **Raciocínio de prova sem calculadora:** para julgar "o desvio-padrão é inferior a 7", basta calcular a variância e comparar com 7² = 49. Se a variância é 44, a raiz é menor do que 7. Evite extrair a raiz quando uma comparação com um quadrado perfeito resolve.

### Dados agrupados sem intervalo de classe

Cada valor x_i aparece f_i vezes; n é a soma das frequências. A média é ponderada e o quadrado de cada desvio é multiplicado pela frequência:

- População: σ = raiz de [soma de (x_i − μ)²·f_i / n].
- Amostra: s = raiz de [soma de (x_i − x̄)²·f_i / (n − 1)].

> 💡 **Exemplo:** notas inteiras de 10 alunos: 1 (2 alunos), 2 (5 alunos), 3 (3 alunos). Média = (2 + 10 + 9)/10 = 2,1. Desvios: −1,1; −0,1; 0,9. Quadrados vezes frequência: 1,21·2 = 2,42; 0,01·5 = 0,05; 0,81·3 = 2,43; soma = 4,90. Como população: σ² = 0,49 e σ = 0,7. Como amostra: s² = 4,9/9 ≈ 0,544 e s ≈ 0,74.

### Dados agrupados em classes

Usam-se as mesmas fórmulas, com o **ponto médio** de cada classe no papel de x_i (convenção igual à da média).

> 💡 **Exemplo:** 0 ⊢ 10 (3 observações), 10 ⊢ 20 (4) e 20 ⊢ 30 (3). Pontos médios 5, 15 e 25; n = 10; média = 15. Soma de (PM − média)²·f = 100·3 + 0·4 + 100·3 = 600. População: σ² = 60, σ ≈ 7,75. Amostra: s² = 600/9 ≈ 66,7, s ≈ 8,16.

Comparação útil entre medidas: para a mesma distribuição, o desvio-padrão costuma ser **maior** que o desvio médio absoluto, porque o quadrado dá mais peso aos desvios grandes. No exemplo das classes acima, o desvio médio é (10·3 + 0·4 + 10·3)/10 = 6, enquanto o desvio-padrão populacional é 7,75.

### Propriedades do desvio-padrão

| Operação sobre todos os valores | Efeito no desvio-padrão | Efeito na variância |
| --- | --- | --- |
| Somar ou subtrair uma constante c | **Não muda** | não muda |
| Multiplicar ou dividir por uma constante c | Multiplicado ou dividido por c (em módulo) | multiplicada ou dividida por c² |

Somar c desloca os valores e a média igualmente; as distâncias à média ficam as mesmas. Multiplicar por c estica todas as distâncias na mesma proporção, e o quadrado delas por c².

> 💡 **Exemplo:** {2, 4, 4, 6} tem média 4, quadrados dos desvios 4, 0, 0, 4 e σ = raiz de (8/4) = raiz de 2. Somando 10 a cada valor, o desvio-padrão continua sendo raiz de 2. Multiplicando cada valor por 3, obtém-se {6, 12, 12, 18}; o desvio-padrão passa a 3·raiz de 2, e a variância passa de 2 para 18.

Aplicação típica: um reajuste de valor fixo para todos não altera a dispersão dos salários; um reajuste percentual (multiplicação) altera o desvio-padrão na mesma proporção.

### Para fixar
- Desvio-padrão = raiz quadrada da variância; mesma unidade dos dados; sempre maior ou igual a zero.
- É zero somente quando todos os valores são iguais (e então a variância também é zero).
- População: divisor n e média μ (símbolo σ). Amostra: divisor n − 1 e média x̄ (símbolo s). Para os mesmos dados, s > σ.
- Tabela de frequências ou classes: pondere o quadrado de cada desvio pela frequência; em classes use o ponto médio.
- Atalho: variância populacional = média dos quadrados − quadrado da média; variância amostral = populacional × n/(n − 1).
- Somar ou subtrair constante não altera o desvio-padrão; multiplicar ou dividir por constante o multiplica ou divide por essa constante (variância: pelo quadrado).
- Comparação entre dois conjuntos só é direta se as médias forem parecidas e as unidades, iguais.

# SINTÉTICO

- **Definição**: desvio-padrão é a raiz quadrada da variância (raiz da média dos quadrados dos desvios); usa a mesma unidade dos dados e nunca é negativo.
- **Valor zero**: só ocorre quando todos os elementos são iguais; nesse caso variância e desvio-padrão são nulos, mas a média continua igual ao valor repetido.
- **População × amostra**: população usa μ e divisor n (símbolo σ); amostra usa x̄ e divisor n − 1 (símbolo s). Para os mesmos dados, s é maior do que σ.
- **Roteiro de cálculo**: média, desvios, quadrados, soma, divisão por n ou n − 1 e raiz. Para comparar com um limite, compare a variância com o quadrado do limite.
- **Atalho**: variância populacional = média dos quadrados − quadrado da média; multiplique por n/(n − 1) para obter a amostral.
- **Tabela de frequências**: cada quadrado de desvio é multiplicado pela frequência; n é a soma das frequências.
- **Dados em classes**: use o ponto médio de cada classe como valor da classe e aplique as mesmas fórmulas.
- **Somar uma constante**: não altera o desvio-padrão, pois as distâncias à média permanecem as mesmas.
- **Multiplicar por uma constante**: multiplica o desvio-padrão por essa constante (em módulo) e a variância pelo quadrado dela.
- **Comparação entre grupos**: só é direta quando as médias são parecidas e a unidade de medida é a mesma.

# NOTAS

- Tabelas das páginas 54, 56, 57 e 58 chegaram truncadas ou embaralhadas; para entender o método usei os comentários resolvidos e escrevi exemplos próprios com outros números.
- Páginas 57 e 58: o exemplo da quantidade de filhos é rotulado "pesquisa populacional" na tabela, mas calculado como desvio-padrão amostral (divisor 19); do mesmo modo, a tabela de estaturas da página 59 traz o rótulo "populacional" enquanto o texto aplica a fórmula amostral (divisor 39). Tratei como inconsistência de rótulo do material, sem impacto no método.
- O material cita desvio médio de 4,63 cm para as estaturas, mas o cálculo do desvio médio (184/40) dá exatamente 4,6; usei apenas a ordem de grandeza.
- A frase "sempre tem valor positivo" (página 51) deve ser lida como "maior ou igual a zero", como a própria página diz antes.
- A propriedade do produto no material não restringe o sinal da constante; para c negativo o desvio-padrão é multiplicado pelo módulo de c (acrescentado por correção matemática).
