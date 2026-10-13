---
id: S0560
agente: CLAUDE-L4
materia: Estatística
aula: Aula 10 — Distribuições Aleatórias Contínuas
trecho: estatistica/a10/s03
paginas_lidas: 25-31
---
# ANALÍTICO

O trecho tem duas partes. Primeiro, como calcular probabilidades quando os objetos sorteados seguem exponenciais diferentes (Teorema da Probabilidade Total). Depois, como a exponencial se relaciona com outras distribuições contínuas: gama, Erlang (hipoexponencial), hiperexponencial, Laplace, Weibull e beta.

### Duas ou mais exponenciais: probabilidade total

Quando um lote mistura objetos de tipos diferentes, cada tipo com sua exponencial (parâmetros λX e λY) e uma proporção P(X) e P(Y) = 1 − P(X) de cada tipo, o objeto sorteado ao acaso não é exponencial: a chance de um evento A é uma **média ponderada** das condicionais.

**P(A) = P(A|X) · P(X) + P(A|Y) · P(Y)**

Cada condicional vem das fórmulas da exponencial: **P(T > t) = e^(−λ·t)** e **P(T < t) = 1 − e^(−λ·t)**. Lembre que a **média** é 1/λ, então, quando o enunciado dá a média, calcule λ = 1/média.

> 💡 **Exemplo próprio:** 60% das lâmpadas têm vida exponencial com λ = 0,02 e 40% com λ = 0,1 (tempo em dias). P(durar mais de 10 dias) = 0,6 · e^(−0,2) + 0,4 · e^(−1) ≈ 0,6 · 0,8187 + 0,4 · 0,3679 ≈ 0,638.

**Passo a passo:** (1) defina o evento; (2) calcule as proporções de cada tipo (por contagem, se vierem como quantidades); (3) obtenha cada λ pela média; (4) calcule a condicional de cada tipo; (5) pondere. O raciocínio vale para outras distribuições, não só a exponencial.

> 💡 **Exemplo próprio (contagem):** 30 peças do tipo A (média 100 h) e 20 do tipo B (média 50 h): P(A) = 0,6 e P(B) = 0,4; P(vida < 100 h) = 0,6 · (1 − e^(−1)) + 0,4 · (1 − e^(−2)).

### Gama e exponencial

A **gama** tem parâmetros α (forma) e β (taxa) e densidade proporcional a x^(α−1) · e^(−β·x) para x ≥ 0. Média e variância:

**E(X) = α / β   e   Var(X) = α / β²**

A exponencial é a gama com **α = 1 e β = λ** (daí E = 1/λ e Var = 1/λ²).

### Soma de exponenciais: Erlang (hipoexponencial)

A soma de **n exponenciais independentes com o mesmo λ** é um caso particular da gama, com **α = n e β = λ** (distribuição de Erlang, tratada no material também como hipoexponencial). Sua média é n/λ e a variância é n/λ². A diferença para a gama geral: em Erlang, α = n é **inteiro**; na gama, pode ser qualquer real positivo.

Chama-se hipoexponencial porque o **coeficiente de variação (CV = desvio padrão / média)** é **menor que 1**, enquanto na exponencial o CV é exatamente 1 (desvio padrão igual à média).

> 💡 **Exemplo próprio:** soma de 3 exponenciais independentes, cada uma com média 4 (λ = 0,25): média = 3 · 4 = 12; variância = 3 · 16 = 48 (ou α/β² = 3/0,0625). Uma soma de variáveis independentes tem variância igual à soma das variâncias.

### Hiperexponencial

É a mistura de exponenciais com probabilidades: sua densidade é a soma das densidades exponenciais, cada uma multiplicada pela proporção do respectivo tipo (como no lote de lâmpadas: 0,02 · e^(−0,02x) · 0,6 + 0,1 · e^(−0,1x) · 0,4). Seu **CV é maior que 1**.

### Diferença de duas exponenciais: Laplace

Y = X1 − X2, com X1 e X2 exponenciais independentes, segue a **distribuição de Laplace** (exponencial dupla) e pode ser positiva ou negativa.

- Se X1 e X2 têm o **mesmo λ**: simétrica em torno de μ = 0, com pico agudo (não suave como a normal) e caudas mais pesadas, que decaem mais devagar. É a união de duas caudas exponenciais. Densidade geral: f(y) = (1/2b) · e^(−|y−μ|/b); aqui μ = 0 e b = 1/λ, logo f(y) = (λ/2) · e^(−λ·|y|). μ é média, moda e mediana; b mede a dispersão.
- Se têm **λ diferentes** (λ1, λ2): Laplace **assimétrica**, com densidade [λ1·λ2/(λ1+λ2)] · e^(−λ1·y) para y ≥ 0 e [λ1·λ2/(λ1+λ2)] · e^(λ2·y) para y < 0.

Em ambos os casos: **E(Y) = 1/λ1 − 1/λ2** e **Var(Y) = 1/λ1² + 1/λ2²**. A variância **soma** (nunca subtrai), mesmo na diferença de variáveis independentes. Se λ1 < λ2 (X1 tem média maior), a cauda direita é maior (assimetria positiva); no caso contrário, a esquerda.

### Weibull e beta

**Weibull** (parâmetros k e λ, z ≥ 0) tem F(z) = 1 − e^(−(z/λ)^k). Comparando com a exponencial, se Z é Weibull, então X = (Z/λ)^k segue exponencial com λ = 1. Com k = 1, a Weibull reduz-se à exponencial. Weibull e beta pertencem à família exponencial.

**Beta** (parâmetros α e β) vive no intervalo **0 ≤ x ≤ 1**, com densidade proporcional a x^(α−1) · (1 − x)^(β−1); a função beta B(α, β) é a constante que faz a área total valer 1. Média: **E(X) = α / (α + β)**.

### Aplicações cobradas em questões

- **Soma de n exponenciais iguais**: segue gama/Erlang (α = n); a variância é n vezes a de cada uma, não a de uma exponencial.
- **Multiplicar uma exponencial por constante k > 0** mantém a exponencial, mas **somar** duas exponenciais independentes (mesmo λ) **não**: dá Erlang. Assim, 2(V + W) tem variância 4 · (Var V + Var W), mas não é exponencial.
- **Diferença** de exponenciais independentes não é exponencial: é Laplace, mesmo que a variância (soma das variâncias) esteja correta.

> ⚠️ **Pegadinha:** o item pode acertar a variância e errar o **nome** da distribuição. Confira as duas coisas separadamente.

### Para fixar
- Mistura de tipos: P(A) = soma de P(A|tipo) · P(tipo); cada condicional usa e^(−λ·t) com λ = 1/média.
- Gama: E = α/β, Var = α/β²; exponencial = gama com α = 1 e β = λ.
- Soma de n exponenciais iguais: Erlang (α = n, β = λ), CV < 1.
- Hiperexponencial: mistura ponderada de exponenciais, CV > 1.
- Diferença de exponenciais independentes: Laplace; E = 1/λ1 − 1/λ2, Var = 1/λ1² + 1/λ2².
- Weibull: F = 1 − e^(−(z/λ)^k); X = (Z/λ)^k é exponencial com λ = 1.
- Beta: definida em [0, 1], E = α/(α + β).

# SINTÉTICO

- **Mistura de exponenciais**: P(A) = P(A|X)·P(X) + P(A|Y)·P(Y), com P(T > t) = e^(−λt) em cada condicional e λ = 1/média.
- **Gama**: parâmetros α (forma) e β (taxa); E = α/β e Var = α/β²; a exponencial é o caso α = 1, β = λ.
- **Soma de n exponenciais iguais**: dá Erlang (gama com α = n e β = λ), de média n/λ e variância n/λ²; α inteiro.
- **Hipo × hiperexponencial**: a hipoexponencial tem coeficiente de variação menor que 1; a hiperexponencial (mistura ponderada de densidades) tem CV maior que 1; a exponencial tem CV = 1.
- **Laplace**: é a distribuição de X1 − X2 (exponenciais independentes); simétrica, de pico agudo e caudas pesadas, quando os λ são iguais, e assimétrica quando diferem.
- **Média e variância da diferença**: E(Y) = 1/λ1 − 1/λ2, mas Var(Y) = 1/λ1² + 1/λ2² (as variâncias se somam).
- **Weibull**: F(z) = 1 − e^(−(z/λ)^k); X = (Z/λ)^k é exponencial com λ = 1.
- **Beta**: definida em [0, 1], com E = α/(α + β); a função beta normaliza a área para 1.
- **Pegadinha**: multiplicar exponencial por constante mantém exponencial; somar ou subtrair duas independentes não.

# NOTAS

Divergências com o material: (1) a questão sobre a soma de n exponenciais "com média 2" trata o valor 2 como o parâmetro λ (e não como a média, o que daria λ = 1/2). O gabarito (Errado) se mantém nos dois casos e o resumo usa a regra correta (λ = 1/média). (2) O material chama de hipoexponencial a soma de exponenciais de mesmo λ, que na literatura costuma ser Erlang (a hipoexponencial formal é a soma de exponenciais com λ distintos); o resumo registra os dois nomes, como no material. Acrescentado fora do trecho: Weibull com k = 1 reduz-se à exponencial (consequência da fórmula dada). As figuras de Laplace foram descartadas por apenas ilustrarem o texto.
