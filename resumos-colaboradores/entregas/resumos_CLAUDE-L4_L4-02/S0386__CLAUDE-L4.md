---
id: S0386
agente: CLAUDE-L4
materia: Estatística
aula: Aula 12 — Regressão Linear Simples
trecho: estatistica/a12/s01
paginas_lidas: 3-18
---
# ANALÍTICO

Este trecho apresenta a correlação linear: como saber se duas variáveis caminham juntas, como classificar essa relação (positiva, negativa, nula ou perfeita) e como medi-la com o coeficiente de correlação de Pearson (r), nas fórmulas tradicional, simplificada e em função de covariância.

### Correlação e gráfico de dispersão

**Correlação** indica a força com que dois conjuntos de valores se associam, isto é, se mudanças em uma variável vêm acompanhadas de mudanças na outra. A primeira checagem é visual, pelo **gráfico (diagrama) de dispersão**: cada par de observações (x, y) é um ponto no plano cartesiano, com X no eixo horizontal (abscissa) e Y no vertical (ordenada).

- Se os pontos se agrupam em torno de uma reta (reta de tendência), há relação linear.
- Quando os pontos estão muito espalhados, o desenho não basta e se recorre ao coeficiente de Pearson, **r**.

### Tipos de correlação linear

| Tipo | Comportamento | Valor de r |
| --- | --- | --- |
| Direta ou **positiva** | as variáveis variam no mesmo sentido (uma sobe, a outra sobe) | r > 0 |
| Inversa ou **negativa** | variam em sentidos opostos (uma sobe, a outra cai) | r < 0 |
| **Nula** (inexistente) | não há relação linear | r = 0 ou r ≈ 0 |
| **Perfeita** | todos os pontos exatamente sobre uma reta | r = +1 ou r = −1 |

> 💡 **Exemplo:** horas de estudo e nota tendem a ter correlação positiva; velocidade média e tempo de viagem num mesmo trecho, negativa; altura de uma pessoa e o dia do mês em que nasceu, nula.

Quanto mais perto de 1 em módulo (|r|), mais forte é a relação linear; quanto mais perto de 0, mais fraca. Exemplos de ordem de grandeza: r = 0,99 indica correlação positiva fortíssima, r = −0,99 negativa fortíssima, r = 0,11 praticamente nula.

> ⚠️ **Pegadinha:** r mede apenas relação **linear**. Um r próximo de zero afasta a ligação em linha reta, mas não prova ausência de qualquer relação (pode haver uma curva). E correlação não demonstra relação de causa e efeito.

### Coeficiente de correlação de Pearson

O coeficiente assume valores no intervalo **−1 ≤ r ≤ +1**.

**Fórmula tradicional (por desvios):**

r = Σ[(Xi − X̅)(Yi − Y̅)] / raiz de { Σ(Xi − X̅)² · Σ(Yi − Y̅)² }

O numerador soma os produtos dos desvios de X e Y; o denominador é a raiz do produto das somas dos quadrados dos desvios. Pode ser escrita com as variáveis centradas xi = Xi − X̅ e yi = Yi − Y̅: r = Σ(xi · yi) / (raiz de Σxi² · raiz de Σyi²). Também aparece como r = Sxy / raiz de (Sxx · Syy), em que Sxx = Σ(Xi − X̅)², Syy = Σ(Yi − Y̅)² e Sxy = Σ(Xi − X̅)(Yi − Y̅).

**Fórmulas simplificadas (sem calcular desvios um a um):**

- Numerador: Σ(Xi − X̅)(Yi − Y̅) = Σ(Xi · Yi) − n · X̅ · Y̅
- Soma dos quadrados dos desvios de X: Σ(Xi − X̅)² = ΣXi² − n · X̅²
- Soma dos quadrados dos desvios de Y: Σ(Yi − Y̅)² = ΣYi² − n · Y̅²

Portanto: **r = [ΣXiYi − n · X̅ · Y̅] / raiz de { [ΣXi² − n · X̅²] · [ΣYi² − n · Y̅²] }**, com n igual ao número de pares ordenados.

**Forma com somas diretas:** r = [n · ΣXiYi − ΣXi · ΣYi] / (raiz de [n · ΣXi² − (ΣXi)²] · raiz de [n · ΣYi² − (ΣYi)²]). Aqui o numerador compara n vezes a soma dos produtos com o produto das somas, e cada termo do denominador é n vezes a "variância" da respectiva variável.

**Forma com covariância:** r = Cov(X, Y) / (σX · σY), em que a covariância é a esperança do produto menos o produto das esperanças, Cov(X, Y) = E(XY) − E(X) · E(Y). Dividir por n ou por n − 1 nos três termos (covariância e desvios padrão) não altera o quociente, pois o fator se cancela.

> 💡 **Exemplo resolvido:** pares (X, Y): (1, 2), (2, 3), (3, 5), (4, 4), (5, 6). Então n = 5, X̅ = 3, Y̅ = 4. Calcule ΣXY = 2 + 6 + 15 + 16 + 30 = 69; ΣX² = 55; ΣY² = 4 + 9 + 25 + 16 + 36 = 90.
> Numerador: 69 − 5 · 3 · 4 = 9. Termo em X: 55 − 5 · 9 = 10. Termo em Y: 90 − 5 · 16 = 10.
> r = 9 / raiz de (10 · 10) = 9/10 = **0,9**, correlação positiva forte. Pela forma com somas diretas: (5 · 69 − 15 · 20) / (raiz de 50 · raiz de 50) = 45/50 = 0,9, o mesmo resultado.

Na prova, o enunciado costuma dar os somatórios prontos (ΣXY, ΣX², ΣY², médias e n): basta aplicar a fórmula simplificada com cuidado nas contas. Os dois caminhos (tradicional e simplificado) sempre dão o mesmo valor.

### Como ler o resultado

- Sinal de r: positivo se Y tende a acompanhar X no mesmo sentido; negativo se em sentido contrário.
- r = +1 ou −1: todos os pontos sobre uma reta (perfeita), crescente ou decrescente.
- Valores próximos de 0: correlação linear fraca ou nula.
- Valores como 0,98 (forte positiva) ou −0,99 (forte negativa) descrevem pontos quase alinhados.

### Para fixar
- Correlação mede a força da associação entre duas variáveis; o diagrama de dispersão mostra os pares (x, y).
- Tipos: positiva (mesmo sentido), negativa (sentidos opostos), nula (r ≈ 0) e perfeita (r = ±1).
- Pearson: r = Cov(X, Y) / (σX · σY), sempre entre −1 e +1.
- Forma prática: r = (ΣXY − n · X̅ · Y̅) / raiz de [(ΣX² − n · X̅²)(ΣY² − n · Y̅²)].
- Quanto mais |r| se aproxima de 1, mais forte a relação linear; perto de 0, mais fraca.
- r mede só relação linear e não prova causa e efeito.
- As formas por desvios e simplificada sempre dão o mesmo resultado.

# SINTÉTICO

- **Correlação linear**: mede a associação entre duas variáveis; o gráfico de dispersão (pares x, y no plano) sugere se os pontos seguem uma reta.
- **Tipos**: positiva (variam no mesmo sentido), negativa (sentidos opostos), nula (sem relação linear, r ≈ 0) e perfeita (todos os pontos sobre uma reta).
- **Intervalo de r**: fica sempre entre −1 e +1; perto de ±1, relação linear forte; perto de 0, fraca.
- **Fórmula de Pearson**: r = Σ(Xi − X̅)(Yi − Y̅) / raiz de [Σ(Xi − X̅)² · Σ(Yi − Y̅)²].
- **Forma simplificada**: numerador ΣXY − n · X̅ · Y̅; cada soma de quadrados dos desvios vira ΣX² − n · X̅² (e igual para Y), evitando calcular desvios um a um.
- **Forma com somas**: r = (n · ΣXY − ΣX · ΣY) / (raiz de [n · ΣX² − (ΣX)²] · raiz de [n · ΣY² − (ΣY)²]).
- **Forma com covariância**: r = Cov(X, Y) / (σX · σY), com Cov = E(XY) − E(X) · E(Y).
- **Exemplo**: ΣXY = 69, ΣX² = 55, ΣY² = 90, X̅ = 3, Y̅ = 4, n = 5 dá r = 9/10 = 0,9.
- **Limites da leitura**: r mede só relação linear e correlação não implica causalidade.

# NOTAS

- Págs. 3 a 6, 10 a 12 e 15: o texto traz vários gráficos de dispersão (e a reta de tendência y = 0,0992x + 0,5441) e tabelas de dados cujas imagens/valores não foram usados; o resumo substituiu-os por exemplos próprios e descreveu as conclusões em texto.
- Pág. 15: o texto-fonte calcula r ≈ 0,9805 para 5/raiz(26); o valor arredondado exato é 0,9806. O resumo usa exemplo próprio e não reproduz esse número.
- O alerta de que r só mede relação linear e de que correlação não implica causa não consta literalmente no trecho; foi incluído como esclarecimento conceitual padrão. O mesmo vale para a observação de que dividir por n ou n − 1 se cancela no quociente.
- Págs. 3 e 4: as tabelas de dados (aluno × questões × nota) foram extraídas de modo embaralhado; não afetam o conteúdo teórico.
