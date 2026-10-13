---
id: S0463
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s03
paginas_lidas: 28-40
---
# ANALÍTICO

Este trecho ensina a executar o **teste de hipóteses para a média de uma população**, em dois cenários: variância populacional conhecida (teste Z, distribuição normal) e variância desconhecida (teste T, distribuição t de Student). Também mostra como calcular o **poder do teste** e como julgar a rejeição em diferentes níveis de significância.

### Ideia geral e vocabulário

Parte-se da hipótese nula (H0: μ = valor dado) como premissa. Define-se a região de não rejeição (RNR) e a região crítica (RC), em que H0 é rejeitada. Os limites dependem de duas escolhas: o **nível de significância α** (ou de confiança 1 − α) e o **tipo de teste**: bilateral (H1: μ ≠ μ0), unilateral à esquerda (H1: μ < μ0) ou unilateral à direita (H1: μ > μ0). Decide-se com base na **média amostral** observada, ou, de forma equivalente, na sua **estatística do teste** (escore padronizado).

### Teste para a média com variância conhecida (teste Z)

Se a população é normal com variância σ² conhecida, a média amostral também é normal. Se a população não é normal, mas a amostra é grande, o Teorema Central do Limite autoriza a aproximação. Como a normal é usada, o teste se chama **teste Z**.

Sob H0, a média amostral tem média μ (a da hipótese nula) e desvio padrão dado pelo **erro padrão**:

**σ(x̄) = σ / √n**

A estatística do teste padroniza a média observada:

**z = (x̄ − μ) / (σ / √n)**

#### Valor crítico zC

É o ponto da normal padrão que separa RNR de RC. Como achar na tabela depende do tipo de tabela:

- **Bilateral**: α/2 em cada cauda, com valores críticos simétricos, −zC e +zC. A probabilidade acumulada até +zC é 1 − α/2. Para 90% de confiança (α = 10%), cada cauda tem 5%: a probabilidade entre 0 e zC é 45% e zC ≈ 1,64 (mais exato, 1,645). Para 99% de confiança, a acumulada é 0,995 e zC = 2,58.
- **Unilateral**: toda a área α fica em um só lado; a acumulada até zC (direita) é 1 − α. Se a tabela dá a área entre 0 e z, procure 0,5 − α.

Valores usuais para decorar:

| Teste | α = 10% | α = 5% | α = 1% |
| --- | --- | --- | --- |
| Bilateral (±zC) | 1,645 | 1,96 | 2,58 |
| Unilateral | 1,28 | 1,645 | 2,33 |

#### Duas formas equivalentes de decidir

1. **Pelos limites da média amostral**: L = μ ± zC × σ/√n (o sinal + dá o limite superior e o − o inferior). Rejeita-se H0 se x̄ cair fora (ou além, nos unilaterais).
2. **Pela estatística**: calcule z e compare com zC. No bilateral, rejeita-se se |z| > zC. No unilateral à esquerda, rejeita-se se z < −zC; no unilateral à direita, se z > zC.

> 💡 **Exemplo do trecho:** μ0 = 2, σ = 1, n = 16, bilateral a 10% (zC = 1,64). Erro padrão = 1/4. Limites: 2 ± 1,64 × 0,25 = 2 ± 0,41, ou seja, 1,59 e 2,41. Se a amostra der x̄ = 1,55, rejeita-se H0, pois 1,55 < 1,59. Pela estatística: z = (1,55 − 2)/0,25 = −1,8, e |−1,8| > 1,64: mesma conclusão.

#### Qual tipo de teste escolher

O tipo vem da hipótese alternativa. Se um desvio para qualquer lado é problema (uma máquina que embale a mais prejudica o dono, a menos lesa o cliente), o teste é **bilateral**. Se o interesse é só em "maior que" ou só em "menor que", é unilateral.

> 💡 **Exemplo do trecho:** máquina de empacotar 300 g, amostra de 1.500 pacotes, confiança de 99%: teste bilateral, α/2 = 0,5% em cada cauda, acumulada 99,5% e zC = ±2,58.

> 💡 **Exemplo com incógnita no desvio padrão:** lâmpadas com μ0 = 2.000 h, amostra de 100, x̄ = 2.050 e estatística z = 2,5. Como z = (x̄ − μ)·√n/σ, σ = 50 × 10/2,5 = 200 h.

> ⚠️ **Pegadinha:** confira se a tabela fornece a área entre 0 e z, a área acumulada ou a área da cauda. Um 99% bilateral exige acumulada de 0,995 (não 0,99). Confusões entre α e α/2 são o erro mais comum.

#### Decidir em diferentes níveis de significância

Quanto **menor** o α, **maior** o valor crítico e **mais difícil rejeitar**. Se H0 é rejeitada a certo nível, também é rejeitada em qualquer nível maior; se não é rejeitada, também não será em níveis menores. Para saber a faixa de α em que se rejeita, compare |z| com os valores críticos de cada nível.

> 💡 **Exemplo do trecho:** H0: μ = 500, H1: μ < 500, σ = 20, n = 4, x̄ = 485. Erro padrão = 10 e z = −1,5. A tabela mostra z crítico de 1,64 (α = 5%) e 1,48 (α = 7%). Como 1,5 < 1,64, não rejeita a 5%; como 1,5 > 1,48, rejeita a 7%. A conclusão correta: rejeita-se com 7%, mas não com 5%.

### Poder do teste

O **poder do teste** é 1 − β, a probabilidade de **rejeitar H0 quando ela é falsa** (β é a probabilidade do erro tipo II). Para calculá-lo:

1. Calcule o limite da RC sob H0: L = μ0 ± zC × σ/√n.
2. Suponha que o verdadeiro valor da média seja μ1 (o da hipótese alternativa) e padronize o limite L com μ1: z = (L − μ1)/(σ/√n).
3. O poder é a probabilidade de a média amostral cair na RC sob μ1.

> 💡 **Exemplo do trecho:** H0: μ = 600, H1: μ > 600, σ = 20, n = 100 (erro padrão 2), α = 2,5% (zC ≈ 2). Limite L = 600 + 2 × 2 = 604. Com μ verdadeiro = 608: z = (604 − 608)/2 = −2, e o poder = P(Z > −2) = 1 − 0,0228 ≈ 97,7%.

> 💡 **Exemplo próprio:** H0: μ = 50, H1: μ > 50, σ = 10, n = 25 (erro padrão 2), α = 5% (zC = 1,645). L = 50 + 3,29 = 53,29. Se μ = 55: z = (53,29 − 55)/2 ≈ −0,86 e o poder = P(Z > −0,86) ≈ 80%.

Quanto mais distante o verdadeiro valor de μ de H0, maior o poder.

### Teste para a média com variância desconhecida (teste T)

Na prática σ² raramente é conhecida; usa-se a **variância amostral**, que é um estimador não tendencioso (sem viés) da variância populacional:

**s² = Σ(xi − x̄)² / (n − 1)**, ou, de forma alternativa, **s² = [ Σx²/n − x̄² ] × n/(n − 1)**.

O segundo formato parte da variância populacional (média dos quadrados menos o quadrado da média), multiplicada por n/(n − 1) para passar do divisor n ao n − 1.

Esse estimador vale para população infinita ou amostra com reposição. Para população finita de tamanho N e amostragem sem reposição, entra o fator de correção (N − n)/(N − 1).

A variância estimada da média amostral e seu desvio padrão (erro padrão estimado) são:

**s²(x̄) = s²/n** e **s(x̄) = s/√n**

Quando a população é normal (ou a amostra permite essa aproximação) e σ é desconhecido, a estatística segue a **distribuição t de Student**: simétrica como a normal, mas com pico mais baixo e extremos mais volumosos, o que reflete a maior incerteza de estimar σ. Por isso o teste se chama **teste T**.

**t = (x̄ − μ) / (s/√n)**

Compara-se t com o valor crítico tC da tabela t, escolhido pelo nível de significância, pelo tipo de teste e por **n − 1 graus de liberdade**. Os limites críticos da média são L = μ ± tC × s/√n.

> 💡 **Exemplo do trecho:** confiança de 90%, bilateral, n = 5 (4 graus de liberdade): a acumulada até tC é 5% + 90% = 95%, e a tabela dá tC = 2,13. Com s² = 0,0125, a variância da média é 0,0125/5 = 0,0025 e o erro padrão é 0,05. Se μ0 = 1: limites 1 ± 2,13 × 0,05 = 1 ± 0,1065, isto é, 0,8935 e 1,1065.

> 💡 **Exemplo próprio:** H0: μ = 100, n = 16, x̄ = 104, s = 8. Erro padrão = 8/4 = 2 e t = 4/2 = 2, com 15 graus de liberdade. No bilateral a 5%, tC ≈ 2,13; como 2 < 2,13, não se rejeita H0.

> 💡 **Exemplo do trecho (qual teste usar):** gasto médio de 16 municípios com distribuição normal de parâmetros desconhecidos, x̄ = 1.000.000, s = 500.000, H0: μ = 750.000. Variância desconhecida: **teste T**, t = 250.000/(500.000/4) = 2, com 15 graus de liberdade. (Teste F serve para comparar variâncias, não para a média.)

> ⚠️ **Pegadinha:** o enunciado indica qual teste. Variância populacional informada (ou "desvio padrão da população") leva ao Z; só o desvio padrão da amostra leva ao T. E, no T, os graus de liberdade são n − 1.

### Para fixar
- Teste Z (σ conhecido): z = (x̄ − μ0)/(σ/√n); teste T (σ desconhecido): t = (x̄ − μ0)/(s/√n), com n − 1 graus de liberdade.
- Limites críticos: L = μ0 ± zC × σ/√n (ou ± tC × s/√n); no bilateral, α/2 em cada cauda.
- Valores usuais de zC bilateral: 1,645 (90%), 1,96 (95%), 2,58 (99%); unilateral a 5%: 1,645 e a 1%: 2,33.
- Rejeita-se H0 quando a estatística cai na região crítica: |z| > zC (bilateral), ou do lado indicado em H1 (unilateral).
- Menor α exige valor crítico maior; rejeitar a um nível implica rejeitar a níveis maiores.
- Poder = 1 − β: acha-se o limite da RC sob H0 e padroniza-se com a média verdadeira; quanto mais longe de H0, maior o poder.
- A variância amostral usa n − 1 e é estimador sem viés; a distribuição t tem pico mais baixo e extremos mais volumosos que a normal.

# SINTÉTICO

- **Hipóteses e regiões**: H0 é a premissa (μ = μ0); H1 define se o teste é bilateral ou unilateral; a região crítica depende de α e do tipo de teste.
- **Teste Z**: σ conhecido (população normal ou amostra grande, pelo Teorema Central do Limite); z = (x̄ − μ0)/(σ/√n).
- **Valores críticos**: bilateral a 5% é ±1,96, a 1% é ±2,58; a 10% é ±1,645; unilateral a 5% é 1,645, a 1% é 2,33. Atenção ao tipo de tabela (acumulada = 1 − α/2 no bilateral).
- **Regra de decisão**: rejeita-se H0 se |z| > zC (bilateral) ou se z passa do crítico no lado de H1; equivale a x̄ cair fora de μ0 ± zC·σ/√n.
- **Menor α**: valor crítico maior, rejeição mais difícil; se rejeita a um nível, rejeita a níveis maiores (z = −1,5 rejeita a 7%, não a 5%).
- **Tipo do teste**: bilateral quando desvios dos dois lados importam (máquina que embala a mais ou a menos).
- **Poder (1 − β)**: probabilidade de rejeitar H0 falsa; calcula-se padronizando o limite crítico com a média verdadeira (exemplo: 97,7%).
- **Variância desconhecida**: usa-se s² com n − 1 como estimador sem viés; erro padrão estimado s/√n.
- **Teste T**: t = (x̄ − μ0)/(s/√n), com n − 1 graus de liberdade; distribuição de pico baixo e extremos volumosos.
- **Escolha do teste**: σ informado leva ao Z; só s leva ao T (16 municípios, s = 500.000: t = 2).

# NOTAS

Páginas 28-40 legíveis; fórmulas recompostas pelo contexto, tabelas de z e t aparecem fragmentadas na extração e foram usadas apenas nos valores citados no texto. Divergências e dúvidas: (1) no exemplo do teste T o material calcula limites 1,165 e 0,8935 (1 + 0,1065 deveria dar 1,1065); o valor correto do limite superior é 1,1065 e foi usado no resumo. (2) O material arredonda zC de 90% bilateral para 1,64 e usa 1,96 ≈ 2 no cálculo do poder; segui os arredondamentos do material nos exemplos dele, mas mencionei os valores exatos (1,645 e 1,96). (3) O fator de correção (N − n)/(N − 1) para população finita sem reposição é descrito na fonte como aplicado à fórmula da variância amostral; a teoria de amostragem o associa à variância da média amostral; não detalhei mais para evitar erro. (4) A última questão da fonte (página 40, sobre o menor x̄ que não rejeita H0 com n = 9, s = 6) tem o comentário fora do intervalo de páginas e a tabela t não foi extraída; não foi incluída. (5) Os valores unilaterais 1,28 (10%) e 2,33 (1%) são valores usuais da normal padrão e não aparecem explicitamente no texto, exceto 2,33 numa alternativa de questão.
