---
id: S0395
agente: CLAUDE-L4
materia: Estatística
aula: Aula 09 — Variáveis Aleatórias Contínuas
trecho: estatistica/a09/s02
paginas_lidas: 16-27
---
# ANALÍTICO

Este trecho trata de três ferramentas para variáveis aleatórias contínuas: a função de distribuição acumulada (f.d.a.), obtida integrando a f.d.p.; a mediana, achada a partir da f.d.a.; e a moda, achada observando o gráfico ou derivando a f.d.p.

### Função de distribuição acumulada (f.d.a.)

A f.d.a. é a probabilidade acumulada desde o início da distribuição até o ponto x:

**FA(x) = P(X ≤ x)**

Para variável contínua, é a integral da f.d.p. do limite inferior xI até x. Chamando de F(x) a integral (primitiva) de f(x), tem-se **FA(x) = F(x) − F(xI)**. Em rigor, a integral parte de −∞, mas o que importa é o valor mínimo em que a densidade é positiva. Só quando F(xI) = 0 a f.d.a. coincide com a primitiva F(x); isso não ocorre sempre.

> 💡 **Exemplo:** f(x) = 4x³ para x em [0, 1]. A primitiva é F(x) = x⁴, com F(0) = 0, logo FA(x) = x⁴. Daí P(X ≤ 0,5) = 0,5⁴ = 0,0625.

**Propriedades da f.d.a.:**

- é **não decrescente** (as probabilidades só se acumulam);
- fica entre 0 e 1;
- vale **0** para x ≤ xI (extremo inferior) e **1** para x ≥ xS (extremo superior); no caso geral, tende a 0 em −∞ e a 1 em +∞.

Para achar o extremo superior quando ele não é dado, resolve-se FA(xS) = 1. A f.d.a. completa é escrita por partes: 0 abaixo do mínimo, a expressão calculada no meio e 1 acima do máximo. Também vale P(a < X < b) = FA(b) − FA(a), e a f.d.p. é a derivada da f.d.a.

### F.d.a. quando a f.d.p. é definida por partes

Calcula-se uma f.d.a. diferente para cada faixa. Na **primeira faixa**, integra-se do menor valor até x. Nas **seguintes**, soma-se o valor que a f.d.a. já atingiu no fim da faixa anterior (a probabilidade acumulada) à integral que vai do início da faixa atual até x.

> 💡 **Exemplo:** f(x) = 0,5x se 0 ≤ x < 1; f(x) = 0,5 se 1 ≤ x ≤ 2,5; zero fora. Na primeira faixa, FA(x) = x²/4, e FA(1) = 1/4. Na segunda, FA(x) = 1/4 + 0,5 · (x − 1) = 0,5x − 0,25. Conferência: FA(2,5) = 1,25 − 0,25 = 1. A f.d.a. completa é 0 para x < 0, x²/4 em [0, 1), 0,5x − 0,25 em [1, 2,5) e 1 a partir de 2,5.

Em algumas primitivas é preciso integrar por partes: ∫u dv = u·v − ∫v du. Por exemplo, ∫x·eˣ dx: com u = x e dv = eˣ dx, resulta x·eˣ − eˣ = eˣ(x − 1).

### Mediana

A mediana divide a distribuição ao meio: metade da probabilidade abaixo dela e metade acima. Portanto, ela é o ponto em que a f.d.a. vale 0,5:

**FA(xMd) = P(X ≤ xMd) = 0,5**

Basta igualar a f.d.a. a 0,5 e resolver para x. Em f.d.p. por partes, descubra primeiro em qual faixa a f.d.a. cruza 0,5 (compare com os valores acumulados no fim de cada faixa) e resolva nessa faixa.

> 💡 **Exemplo:** com FA(x) = x⁴ (acima), x⁴ = 0,5 dá x = 0,5^(1/4) ≈ 0,84. No exemplo por partes, FA(1) = 0,25 < 0,5, então a mediana está na segunda faixa: 0,5x − 0,25 = 0,5, logo x = 1,5.

**Efeito de constantes:** somar, subtrair, multiplicar ou dividir todos os valores por uma constante faz a mediana sofrer a mesma operação:

- Md(X + a) = Md(X) + a e Md(X − a) = Md(X) − a;
- Md(X · a) = Md(X) · a e Md(X ÷ a) = Md(X) ÷ a.

> ⚠️ **Pegadinha:** afirmar que Md(X + a) = Md(X) é erro; a mediana acompanha o deslocamento.

### Moda

A moda é o valor de maior probabilidade. Numa variável contínua, é o x em que a **densidade f(x) é máxima** (no gráfico da f.d.p., o ponto mais alto, e não da f.d.a.). Como achar:

| Formato da f.d.p. | Moda |
| --- | --- |
| Decrescente no intervalo | o menor valor do intervalo |
| Crescente no intervalo | o maior valor do intervalo |
| Parábola com concavidade para cima | um dos extremos do intervalo (ou os dois, se f valer o mesmo em ambos, o que dá duas modas); teste os dois |
| Parábola com concavidade para baixo | a média entre as duas raízes (valores de x em que f = 0) |
| Outros casos | derivar f(x), igualar a zero e confirmar que é ponto de máximo |

A derivada mostra o quanto a função cresce ou decresce em cada ponto. Onde ela é zero, a função não sobe nem desce: pode ser máximo ou mínimo, e só o máximo é a moda.

**Regras de derivação usadas:**

- d(xᵃ)/dx = a · xᵃ⁻¹ (por exemplo, a derivada de x⁴ é 4x³);
- a derivada de uma constante é 0;
- constante multiplicando: d(a·xᵇ)/dx = a · b · xᵇ⁻¹;
- d(eˣ)/dx = eˣ (para base b qualquer, d(bˣ)/dx = bˣ · ln b);
- a derivada de uma soma é a soma das derivadas.

> 💡 **Exemplo:** f(x) = 6x · (1 − x) = 6x − 6x² para x em [0, 1]. A derivada é 6 − 12x; igualando a zero, x = 0,5. Como o termo em x² é negativo (concavidade para baixo), é um máximo, logo a moda é 0,5 (também a média das raízes 0 e 1).

> 💡 **Moda e f.d.a. juntas:** no exemplo anterior, P(X ≤ moda) = FA(0,5), com FA(x) = 3x² − 2x³ (integral de 6x − 6x² a partir de 0), que vale 0,75 − 0,25 = 0,5. A mesma estratégia aparece em questões que pedem a probabilidade até a moda.

### Para fixar

- FA(x) = P(X ≤ x) = F(x) − F(xI); é não decrescente, vai de 0 a 1 e é 1 a partir do extremo superior.
- Em f.d.p. por partes, a f.d.a. é montada faixa por faixa, somando o acumulado da faixa anterior.
- Mediana: resolver FA(x) = 0,5; ela acompanha somas, subtrações, produtos e divisões por constante.
- Moda: ponto de maior f(x); crescente → extremo superior; decrescente → inferior; parábola para baixo → média das raízes; caso geral → f'(x) = 0 e conferir máximo.
- Derivada de xᵃ é a·xᵃ⁻¹, de constante é zero e de eˣ é eˣ.

# SINTÉTICO

- **F.d.a.**: FA(x) = P(X ≤ x) = F(x) − F(xI), em que F é a primitiva da f.d.p.; é não decrescente, vale 0 até o mínimo e 1 a partir do máximo.
- **Extremo superior**: quando não é dado, resolve-se FA(xS) = 1.
- **F.d.p. por partes**: a f.d.a. é calculada faixa a faixa, somando o acumulado atingido no fim da faixa anterior.
- **Mediana**: é o x que resolve FA(x) = 0,5; Md(X ± a) = Md(X) ± a, e o mesmo vale para multiplicar ou dividir.
- **Moda**: é o x de maior densidade f(x), lido no gráfico da f.d.p., não da f.d.a.
- **Atalhos geométricos para a moda**: crescente, extremo superior; decrescente, extremo inferior; parábola para baixo, média das raízes; parábola para cima, teste os extremos.
- **Caso geral**: f'(x) = 0, confirmando que o ponto é máximo; d(xᵃ)/dx = a·xᵃ⁻¹ e a derivada da constante é zero.

# NOTAS

- Nenhuma página vazia ou ilegível. Os gráficos foram descartados por apenas ilustrarem o texto.
- O trecho abre a seção de "tendência central e dispersão" mas só desenvolve mediana e moda; média, variância e desvio padrão não estão neste intervalo de páginas e não foram incluídos.
- Os exemplos do resumo são originais; os do material (f.d.p. 9x², f.d.p. por partes com 2x/3, questões de concursos sobre F(2), f.d.a. alternativa e P[X ≤ Mo]) não foram reproduzidos.
- Acrescentei por conta própria que a f.d.p. é a derivada da f.d.a. e que P(a < X < b) = FA(b) − FA(a), fatos padrão e coerentes com o texto.
- Na p. 19 do material, a fórmula da f.d.a. da segunda faixa aparece com a tipografia ambígua ("(x² − 1)/8"); conferi o resultado integrando e F(3) = 1.
