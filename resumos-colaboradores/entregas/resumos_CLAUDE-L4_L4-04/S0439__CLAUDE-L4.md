---
id: S0439
agente: CLAUDE-L4
materia: Estatística
aula: Aula 04 — Medidas de Variabilidade ou Dispersão
trecho: estatistica/a04/s03
paginas_lidas: 27-38
---
# ANALÍTICO

O desvio absoluto médio (ou desvio médio) mede, em média, o quanto os valores de um conjunto se afastam da média aritmética. O trecho mostra por que ele usa módulos, como calculá-lo para dados soltos, para tabelas de frequência simples e para dados em classes, e como ele reage a somas e multiplicações nos dados.

### Por que usar o valor absoluto

Subtrair a média de cada observação gera os **desvios** (x_i − x̄). Alguns são positivos, outros negativos, e a soma deles é **sempre zero**, seja qual for o conjunto (propriedade da média). Por isso a média dos desvios simples não informa nada sobre a dispersão. A saída é descartar o sinal: trabalha-se com o **módulo** de cada desvio, que transforma qualquer valor negativo em positivo.

- Média: x̄ = (soma dos x_i) / n.
- **Desvio médio: Dm = (soma dos |x_i − x̄|) / n**.

Diferentemente da amplitude total e da amplitude interquartílica, o Dm **considera todos os valores** do conjunto e, por isso, é mais robusto. Sua desvantagem é a operação de módulo, que dificulta o estudo matemático da medida (por isso, em teoria estatística, a variância e o desvio-padrão são preferidos). O Dm tem a **mesma unidade dos dados** (reais, centímetros, reclamações etc.).

> ⚠️ **Pegadinha:** "média dos desvios" sem módulo vale zero; "média dos desvios em módulo" é o desvio médio. Leia com atenção qual das duas a questão pede.

### Dm para dados não agrupados

Passos: (1) calcule a média; (2) subtraia a média de cada valor; (3) tome o módulo; (4) some os módulos; (5) divida por n.

> 💡 **Exemplo:** conjunto {2, 4, 6, 8, 15}. Média = 35/5 = 7. Módulos dos desvios: |2−7| = 5; |4−7| = 3; |6−7| = 1; |8−7| = 1; |15−7| = 8. Soma = 18. Dm = 18/5 = 3,6.

Observe que o valor extremo (15) é o que mais contribui para o Dm, mas, como o desvio entra com seu valor (e não ao quadrado), seu peso é menor do que seria na variância.

Em provas, também aparecem itens sobre **o maior desvio absoluto** do conjunto: basta calcular todos os módulos e escolher o maior; isso é diferente de calcular o Dm, que é a média deles. Por exemplo, em cinco vendedores cuja média de vendas foi 50, com módulos dos desvios 30, 10, 0, 10 e 20, o maior desvio absoluto é 30 e o Dm é 70/5 = 14. Quem confunde as duas medidas erra o item.

### Dm para dados agrupados sem intervalo de classe

Quando os dados vêm em tabela de frequências (valor x_i e frequência f_i), cada módulo é **ponderado pela frequência**:

- Média: x̄ = (soma de x_i·f_i) / (soma de f_i).
- **Dm = (soma de |x_i − x̄|·f_i) / (soma de f_i)**.

Monte a tabela com colunas: x_i, f_i, x_i·f_i, |x_i − x̄|, |x_i − x̄|·f_i.

> 💡 **Exemplo:** número de irmãos de 10 colegas: 0 irmãos (3 colegas), 1 (5), 2 (1), 3 (1). Soma de f = 10; soma de x·f = 0 + 5 + 2 + 3 = 10; média = 1. Módulos ponderados: |0−1|·3 = 3; |1−1|·5 = 0; |2−1|·1 = 1; |3−1|·1 = 2. Soma = 6. Dm = 6/10 = 0,6 irmão.

### Dm para dados agrupados em classes

Com intervalos de classe, adota-se a **mesma convenção usada na média**: todos os valores de uma classe são tratados como se fossem iguais ao **ponto médio** da classe (x_i = limite inferior + limite superior, dividido por 2). Daí em diante o cálculo é o mesmo da tabela com frequências: média ponderada pelos pontos médios e depois Dm = (soma de |x_i − x̄|·f_i) / (soma de f_i).

> 💡 **Exemplo:** pesos de 10 pacotes: 10 ⊢ 20 (2 pacotes); 20 ⊢ 30 (6); 30 ⊢ 40 (2). Pontos médios: 15, 25 e 35. Média = (15·2 + 25·6 + 35·2)/10 = 250/10 = 25. Módulos ponderados: |15−25|·2 = 20; |25−25|·6 = 0; |35−25|·2 = 20. Soma = 40. Dm = 40/10 = 4.

> ⚠️ **Pegadinha:** o ponto médio é usado tanto na média quanto nos desvios. Não esqueça a multiplicação pelas frequências: sem ela, o resultado fica errado. O divisor é a soma das frequências (n), não o número de classes.

Erros comuns nas questões: (a) usar a amplitude da classe no lugar do ponto médio; (b) esquecer que a média precisa ser calculada antes dos desvios; (c) deixar de aplicar o módulo e obter soma zero.

### Propriedades do desvio médio

Considere um conjunto cujo Dm é conhecido e uma constante c.

| Operação sobre todos os valores | Efeito no desvio médio |
| --- | --- |
| Somar (ou subtrair) uma constante c | **Não muda** |
| Multiplicar (ou dividir) por uma constante c | Fica **multiplicado (ou dividido) por c** (em módulo, se c for negativo) |

Raciocínio: somar c desloca todos os valores e a média na mesma quantidade, e as distâncias entre cada valor e a média permanecem as mesmas. Multiplicar por c estica ou encolhe todas as distâncias na mesma proporção.

> 💡 **Exemplo:** o conjunto {1, 3, 5, 7, 9} tem média 5 e Dm = (4+2+0+2+4)/5 = 12/5 = 2,4. Somando 5 a cada valor, obtém-se {6, 8, 10, 12, 14}, média 10, e o Dm continua 2,4. Multiplicando o conjunto original por 5, obtém-se {5, 15, 25, 35, 45}, média 25, e o Dm passa a 60/5 = 12, isto é, 5 vezes 2,4.

Isso explica por que uma mudança de origem (acréscimo de um valor fixo a todos, como um reajuste em reais iguais para todos) não altera a dispersão, ao passo que mudança de escala (reajuste percentual, conversão de unidade) altera a dispersão na mesma proporção.

### Para fixar
- Soma dos desvios simples (x_i − x̄) é sempre zero; por isso o desvio médio usa o módulo.
- Dm = soma de |x_i − x̄| dividida por n, medida na mesma unidade dos dados.
- Dados agrupados: pondere cada módulo pela frequência e divida pela soma das frequências.
- Em classes, use o ponto médio de cada classe como valor da classe, na média e nos desvios.
- Maior desvio absoluto é o maior dos módulos; Dm é a média dos módulos. Não são a mesma coisa.
- Somar ou subtrair constante: Dm não muda. Multiplicar ou dividir por constante: Dm é multiplicado ou dividido por ela.
- O Dm considera todos os valores (mais robusto que amplitude total e amplitude interquartílica), mas é mais difícil de tratar matematicamente por causa do módulo.

# SINTÉTICO

- **Desvio médio (Dm)**: média dos módulos dos desvios em relação à média aritmética, Dm = soma de |x_i − x̄| dividida por n; é medido na unidade dos dados.
- **Por que módulo**: a soma dos desvios simples em torno da média é sempre zero, então os sinais precisam ser eliminados para medir dispersão.
- **Dados soltos**: calcule a média, tire o módulo de cada diferença, some e divida por n. Ex.: {2, 4, 6, 8, 15} tem média 7 e Dm = 18/5 = 3,6.
- **Tabela de frequências**: Dm = soma de |x_i − x̄|·f_i dividida pela soma de f_i; a média também é ponderada.
- **Dados em classes**: trate cada classe pelo seu ponto médio (média das duas extremidades) e aplique o mesmo cálculo ponderado.
- **Maior desvio × Dm**: o maior desvio absoluto é o maior dos módulos; o Dm é a média de todos eles. Itens de prova trocam uma pela outra.
- **Propriedade da soma**: somar ou subtrair uma constante de todos os valores deixa o Dm igual, pois as distâncias à média não mudam.
- **Propriedade do produto**: multiplicar ou dividir todos os valores por uma constante multiplica ou divide o Dm pela mesma constante (em módulo).
- **Vantagem e limite**: usa todos os valores (mais robusto que amplitude total e interquartílica), mas o módulo dificulta o estudo matemático da medida.

# NOTAS

- Tabelas das páginas 29, 30, 32 a 36 vieram embaralhadas ou parcialmente vazias (a tabela de reclamações da página 30 e a de estaturas das páginas 35 e 36 não foram extraídas por completo). Usei os números dos comentários resolvidos apenas para entender o método e escrevi exemplos próprios com outros dados.
- Na página 29 a fórmula do exemplo traz o índice de soma "K" em vez de "n", e a página 28 cita "f_i" na legenda da fórmula sem ela aparecer na fórmula do dado não agrupado; tratei como erros de digitação do material.
- A página 28 chama a soma zero dos desvios de "1.ª propriedade dos desvios" e fala em "soma de todos os desvios médios"; entendi como soma dos desvios simples (x_i − x̄), que é o correto.
- A propriedade do produto no material é enunciada para a constante c sem restrição de sinal; para c negativo o Dm é multiplicado pelo módulo de c (acrescentei isso por correção matemática).
