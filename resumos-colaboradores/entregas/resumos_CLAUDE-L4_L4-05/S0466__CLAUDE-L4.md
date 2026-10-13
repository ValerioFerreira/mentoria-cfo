---
id: S0466
agente: CLAUDE-L4
materia: Estatística
aula: Aula 08 — Distribuições Discretas de Probabilidade
trecho: estatistica/a08/s05
paginas_lidas: 53-64
---
# ANALÍTICO

A distribuição de Poisson modela a contagem de ocorrências de um evento raro em um intervalo (de tempo, espaço ou volume), quando a taxa média é constante. O trecho cobre as condições de uso, a fórmula, esperança e variância, a moda, a mudança de intervalo, a soma de variáveis de Poisson e a aproximação da binomial.

### Quando usar Poisson

Pense em contagens como chamadas por hora, falhas de um equipamento por semana, pacientes que chegam a um pronto-socorro por dia ou erros por página. O que essas situações têm em comum:

- o número de ocorrências é **inteiro** (0, 1, 2, ...), sem limite superior fixo;
- as ocorrências são **independentes** entre si;
- a **taxa média é constante** no intervalo considerado;
- em um instante qualquer, a chance de acontecer é minúscula, e dois eventos nunca acontecem exatamente no mesmo instante.

A ideia por trás disso é dividir o intervalo em um número gigantesco de instantes (n tende ao infinito), cada um com probabilidade quase nula de ocorrência (p tende a zero). Isso é uma binomial no limite: **Poisson nasce da binomial quando n → ∞ e p → 0**, com o produto n·p mantido finito.

> 💡 **Exemplo:** um lote tem n = 500 peças e cada uma sai com defeito com p = 0,4%. Calcular P(exatamente 3 defeituosas) pela binomial exigiria C(500,3) × 0,004³ × 0,996⁴⁹⁷, conta pesada. Pela aproximação de Poisson, basta usar λ = 500 × 0,004 = 2.

### Parâmetro, esperança e variância

O único parâmetro é **λ** (lambda), a **taxa média de ocorrências** no intervalo. Escreve-se X ~ Po(λ).

- Vindo da binomial: **λ = n · p**.
- **E(X) = λ**
- **Var(X) = λ**

A variância sai da fórmula binomial n·p·q: como p tende a zero, q = 1 − p tende a 1 e sobra n·p = λ. Em prova, **média igual à variância** é a assinatura da Poisson: se uma questão disser que a contagem tem média 6 e variância 6, o caminho é Poisson com λ = 6.

Outras medidas:

- **Assimetria** = 1/√λ: sempre positiva (cauda à direita), e some à medida que λ cresce, aproximando a curva de um sino simétrico.
- **Moda** (valor mais provável): se λ **não é inteiro**, a moda é a parte inteira de λ (o piso). Para λ = 2,7, a moda é 2. Se λ **é inteiro**, há **duas modas**, λ − 1 e λ, porque as duas têm a mesma probabilidade. Para λ = 5, as modas são 4 e 5.

A razão P(X = k) / P(X = k − 1) = λ / k explica isso: a probabilidade sobe enquanto k < λ, desce quando k > λ e se iguala em k = λ.

### Fórmula da probabilidade

**P(X = k) = e^(−λ) · λ^k / k!**, com k = 0, 1, 2, ... e e ≈ 2,718.

Macete para não errar: o expoente de **e** leva **sinal negativo**, o expoente de λ é o próprio **k**, e o fatorial fica no denominador, em k. Em resumo: "e com menos, lambda elevado a k, k fatorial embaixo".

Casos que viram padrão em prova:

- P(X = 0) = e^(−λ) (pois λ⁰ = 1 e 0! = 1);
- P(X = 1) = λ · e^(−λ);
- "no máximo k" = soma de P(0) até P(k);
- "mais de k" ou "pelo menos k" = **complemento**: 1 − P(X ≤ k) ou 1 − P(X ≤ k − 1).

> 💡 **Exemplo:** com λ = 2 e e^(−2) ≈ 0,1353: P(0) = 0,1353; P(1) = 2 × 0,1353 = 0,2707; P(2) = (4/2) × 0,1353 = 0,2707. Logo, P(X ≥ 1) = 1 − P(0) = 0,8647, e P(X ≤ 2) = 0,1353 + 0,2707 + 0,2707 = 0,6767.

Em geral a banca fornece o valor de e^(−λ) no enunciado ou aceita a resposta em função de e. Se a alternativa vier como "(9/2)·e^(−3)", é só montar a fórmula e simplificar a fração (3² / 2! = 9/2).

### Mudança de intervalo

A taxa λ vale para um intervalo específico. Se a questão dá a taxa por um período e pergunta sobre outro, **ajuste λ proporcionalmente** antes de usar a fórmula:

**λ_novo = λ_dado × (intervalo novo / intervalo dado)**

> 💡 **Exemplo:** um posto recebe, em média, 6 chamadas por hora. Para 20 minutos, λ = 6 × (20/60) = 2. Para 3 horas, λ = 18. A probabilidade de exatamente 3 chamadas em 20 minutos é e^(−2) · 2³/3! = (4/3) · e^(−2) ≈ 0,18.

O processo é o mesmo quando se muda de dia para semana, de mês para período de 10 dias etc. Cuidado com a unidade de tempo e com quantos dias úteis a questão considera na semana ou no mês.

Também dá para achar o **tempo médio entre ocorrências**: t = (intervalo) / λ. Com 6 chamadas por hora, o intervalo médio entre elas é 60/6 = 10 minutos.

### Soma e multiplicação por fração

Se X e Y são **independentes**, X ~ Po(λx) e Y ~ Po(λy), então **X + Y ~ Po(λx + λy)**. As taxas se somam: duas filiais que recebem, em média, 4 e 7 pedidos por dia, juntas recebem uma contagem de Poisson com λ = 11. A propriedade vale para qualquer quantidade de parcelas independentes: n variáveis de Poisson com média 1 cada somam uma Poisson de média n.

Detalhe de prova: a soma de independentes é Poisson, mas **a diferença não é** Poisson em geral. Já "soma menos uma parcela" é apenas a soma das demais: se S = X + Y + Z, então S − X = Y + Z, que continua sendo Poisson.

Também se pode tomar **uma fração** das ocorrências (por exemplo, só metade dos clientes de uma empresa migrando para outra): a taxa dessa parte fica multiplicada pela fração. Assim, se a filial A (λ = 4) e metade da filial B (λ = 8) se juntam, o total é Po(4 + 0,5 × 8) = Po(8).

> ⚠️ **Pegadinha:** não confunda esse "filtro" de uma fração das ocorrências com multiplicar a própria variável por uma constante. A taxa é que é multiplicada pela fração; E(X) = Var(X) = λ continua valendo para o resultado.

### Comparação com a binomial

| Característica | Binomial | Poisson |
| --- | --- | --- |
| Número de tentativas | fixo (n) | não definido (infinitos instantes) |
| Valores possíveis | 0 a n | 0, 1, 2, ... sem teto |
| Parâmetros | n e p | apenas λ |
| Média | n·p | λ |
| Variância | n·p·q | λ (média = variância) |
| Quando usar | n pequeno ou moderado | evento raro, n grande, p pequeno |

### Para fixar
- Poisson conta ocorrências independentes de um evento raro em um intervalo, com taxa média constante.
- É a binomial no limite (n grande, p quase zero), com λ = n·p.
- P(X = k) = e^(−λ) · λ^k / k!; lembre do sinal negativo no expoente de e e do fatorial em k.
- Média = variância = λ; assimetria = 1/√λ, sempre positiva.
- Moda: piso de λ se não for inteiro; duas modas (λ − 1 e λ) se for inteiro.
- Mudou o intervalo? Reescale λ pela razão entre os intervalos antes de calcular.
- Soma de Poisson independentes é Poisson com as taxas somadas; "pelo menos" e "mais de" se resolvem pelo complemento.

# SINTÉTICO

- **Quando é Poisson**: contagem de ocorrências independentes de evento raro em um intervalo, com taxa média constante e valores inteiros sem teto (chamadas por hora, falhas por semana).
- **Origem na binomial**: limite com n → ∞ e p → 0; serve de aproximação quando n é grande e p pequeno, com λ = n·p.
- **Fórmula**: P(X = k) = e^(−λ) · λ^k / k!, com k = 0, 1, 2, ...; atenção ao sinal negativo no expoente de e e ao fatorial no denominador.
- **Média e variância**: E(X) = Var(X) = λ, único parâmetro; média igual à variância indica Poisson.
- **Assimetria**: 1/√λ, positiva, diminuindo conforme λ cresce.
- **Moda**: piso de λ quando λ não é inteiro; quando é inteiro, há duas modas, λ − 1 e λ.
- **Mudança de intervalo**: λ_novo = λ_dado × (intervalo novo / intervalo dado); 6 por hora vira 2 em 20 minutos. Tempo médio entre ocorrências = intervalo / λ.
- **Casos clássicos**: P(0) = e^(−λ), P(1) = λ·e^(−λ); "no máximo k" soma de 0 a k; "mais de k" e "pelo menos" usam o complemento.
- **Soma**: X + Y independentes de Poisson resultam em Poisson com λx + λy; "soma menos uma parcela" é a soma das demais e continua Poisson.

# NOTAS

- Pág. 53: a expressão da binomial no exemplo da indústria vem escrita como P(X = 100) com C(400,5); é erro de digitação do material (deveria ser P(X = 5)). No resumo usei exemplo próprio, sem reproduzir o erro.
- Pág. 57: o material afirma que o coeficiente de curtose b2 da Poisson é igual a 1/√λ, igual à assimetria. Pelo consenso técnico, a assimetria é 1/√λ, mas a curtose em excesso é 1/λ (curtose "total" = 3 + 1/λ). Deixei a curtose fora do resumo por causa da divergência; revisão humana recomendada.
- Pág. 61: o material diz que também é possível "multiplicar os parâmetros por constantes" e continuar com Poisson. Em rigor, isso vale quando se toma uma fração das ocorrências (seleção aleatória, "thinning"), não para qualquer múltiplo cX. Descrevi apenas o caso da fração.
- Pág. 55: a variância é apresentada como n·p, com a aproximação q ≈ 1; coerente com Var = λ.
- Questões comentadas ocupam cerca de metade do trecho; o resumo contém os métodos que elas ensinam (mudança de intervalo, complemento, soma de Poisson). Nenhuma página vazia ou ilegível.
