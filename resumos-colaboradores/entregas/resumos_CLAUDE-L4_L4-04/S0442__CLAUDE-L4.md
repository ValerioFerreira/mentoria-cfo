---
id: S0442
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s02
paginas_lidas: 14-27
---
# ANALÍTICO

Este trecho aprofunda os testes de hipóteses em três frentes: os dois tipos de erro de decisão (e as probabilidades alfa e beta), a função potência (o poder do teste e o que o aumenta) e o cálculo dos erros quando a variável tem distribuição uniforme.

### Erros de decisão: tipo I e tipo II

Todo teste decide entre rejeitar ou não a hipótese nula (H0) e, como a decisão se baseia numa amostra, pode errar. A regra é sempre a mesma: resultado na **região crítica** leva à rejeição de H0; resultado na **região de não rejeição** leva à não rejeição. Mesmo seguindo a regra, existe risco.

| | H0 verdadeira | H0 falsa |
| --- | --- | --- |
| **Rejeita H0** | **Erro tipo I** (probabilidade α) | Decisão correta (poder = 1 − β) |
| **Não rejeita H0** | Decisão correta (confiança = 1 − α) | **Erro tipo II** (probabilidade β) |

- **Erro tipo I** = rejeitar H0 sendo ela verdadeira ("falso positivo"). Sua probabilidade é o **nível de significância α**, também chamado **tamanho do teste**.
- **Erro tipo II** = não rejeitar H0 sendo ela falsa ("falso negativo"). Sua probabilidade é **β**.
- **Nível de confiança** = 1 − α (não rejeitar H0 quando verdadeira). **Poder do teste** = 1 − β (rejeitar H0 quando falsa).

> ⚠️ **Pegadinha (evento × probabilidade):** o erro tipo I é o **evento** "rejeitar H0 sendo verdadeira"; α é a **probabilidade** desse evento. Alternativas que chamam "o erro" de "a probabilidade" (ou o contrário) podem ser distratores, e a questão de prova pode pedir uma ou outra.

> ⚠️ **Pegadinha (α + β ≠ 1):** os dois erros **não são complementares**. Eles são calculados em distribuições diferentes (α sob H0; β sob a distribuição verdadeira, diferente de H0), por isso a soma pode ser menor, igual ou até maior do que 1. O complementar de α é o nível de confiança; o complementar de β é o poder.

**Como visualizar.** Suponha H0: μ = 50, rejeitada se a média amostral for menor do que 48. Sob H0, a área à esquerda de 48 na curva centrada em 50 é α. Já β **não aparece** nessa curva: ele só existe quando se supõe um valor verdadeiro diferente de 50 (por exemplo, μ = 46, dado pelo enunciado ou pela hipótese alternativa). Nessa nova curva centrada em 46, β é a área do lado da **não rejeição** (média amostral maior ou igual a 48).

**Como α pode diminuir.** Além de ser fixado de antemão, α diminui se a amostra aumentar mantendo os mesmos limites da região de não rejeição, ou se a região de não rejeição for ampliada (mantida a amostra).

**Teste ótimo e razão de verossimilhanças.** O teste é ótimo quando uma combinação linear a·α + b·β (com a e b positivos) é a menor possível. Para construí-lo usa-se a razão de verossimilhanças RV = p0/p1, em que p é o produto das funções de probabilidade (ou de densidade) calculadas em cada valor da amostra, com p0 usando o parâmetro de H0 e p1 o parâmetro de H1. Regra: **RV menor que uma constante k rejeita H0; RV maior que k não rejeita; RV igual a k é inconclusivo**. Em resumo, rejeita-se H0 quando a razão é pequena (os dados são muito mais prováveis sob H1).

### Função potência

A **função potência**, π(μ1), mostra o poder do teste (1 − β) para cada valor verdadeiro do parâmetro. Três fatores aumentam o poder:

1. **Distância entre o parâmetro verdadeiro e o de H0**: quanto mais longe, maior o poder (β encolhe).
2. **Tamanho da amostra n**: maior n, maior poder.
3. **Nível de significância α**: maior α, maior poder (a região de rejeição cresce e a de não rejeição diminui).

O aumento de n ou de α reduz a região de não rejeição; logo β cai e 1 − β sobe. Quando um teste tem poder maior do que outro **para todos** os valores do parâmetro, diz-se que é **mais poderoso**. Exemplo: com n = 100 o poder é superior ao de n = 25 em qualquer ponto.

**Formato da função conforme o tipo de teste:**

| Teste | Hipótese alternativa | Função potência |
| --- | --- | --- |
| Unilateral à esquerda | μ < μ0 | estritamente **decrescente** (quanto menor o verdadeiro μ, maior o poder) |
| Unilateral à direita | μ > μ0 | estritamente **crescente** |
| Bilateral | μ ≠ μ0 | **decresce** à esquerda de μ0 e **cresce** à direita; **não é estritamente monótona** |

No ponto em que o parâmetro verdadeiro é o próprio valor de H0, a função vale α: é o seu **menor valor** (por exemplo, 5% para ambas as curvas de n diferentes, num teste de nível 5%).

> ⚠️ **Pegadinha:** "o poder do teste independe do nível de significância" é **falso**; "em testes bilaterais a função potência é estritamente monótona" também é falso.

**Teste uniformemente mais poderoso (UMP).** Para um nível α fixado, é o teste que maximiza o poder (minimiza β) contra as alternativas. Duas condições: (1) em todos os valores da alternativa, seu poder é maior ou igual ao de qualquer outro teste de mesmo nível; (2) a probabilidade máxima (supremo) de rejeitar H0 quando ela é verdadeira não passa de α. UMP só existe em situações especiais, como em distribuições da família exponencial.

### Testes para distribuições uniformes

Uma uniforme em (a, b) tem densidade constante k no intervalo e zero fora. Como a área total é 1, (b − a)·k = 1, portanto **k = 1/(b − a)**. Os limites a e b são os únicos parâmetros, e o teste consiste em rejeitar H0 (sobre a e b) conforme o valor observado caia ou não em determinada faixa.

A probabilidade num intervalo (m, o) dentro de (a, b) é a área de um retângulo: **P(m < X < o) = (o − m)/(b − a)**.

- **α** usa o intervalo de H0: probabilidade da região de rejeição.
- **β** usa o intervalo verdadeiro (ou o de H1): probabilidade da região de **não** rejeição.

> 💡 **Exemplo 1 (α e β):** H0: X é uniforme em (0, 10), rejeitada se X > 7. Então α = P(7 < X < 10) = 3/10 = 30%. Se o verdadeiro intervalo for (0, 14), β = P(X ≤ 7) = 7/14 = 50%, e o poder é 1 − 0,5 = 50%.

> 💡 **Exemplo 2 (a faixa verdadeira pode ser outra):** H0: uniforme em (2, 8), rejeitada se X < 3. α = (3 − 2)/(8 − 2) = 1/6. Se o verdadeiro intervalo for (4, 10), nenhum valor observado fica abaixo de 3, então a rejeição nunca ocorre: β = 1 e o poder é zero.

> 💡 **Exemplo 3 (padrão de prova):** X uniforme em (0, θ), com H0: θ = 20 contra H1: θ > 20, rejeitando H0 se a única observação passar de 15. Para o verdadeiro θ = 24, β = P(X ≤ 15 | θ = 24) = 15/24 = 5/8. O erro é calculado com o intervalo (0, 24) e sobre a região de **não** rejeição (X ≤ 15). O mesmo teste teria α = P(15 < X < 20) = 5/20 = 1/4 sob H0.

Passos práticos: (1) identifique a região de rejeição; (2) para α, calcule a área dessa região usando (a, b) de H0; (3) para β, calcule a área da região de não rejeição usando o intervalo verdadeiro; (4) limite a região ao intervalo da distribuição, porque fora dele a densidade é zero.

### Para fixar
- Erro tipo I = rejeitar H0 verdadeira (falso positivo), probabilidade α (nível de significância ou tamanho). Erro tipo II = não rejeitar H0 falsa (falso negativo), probabilidade β.
- 1 − α é a confiança; 1 − β é o poder. α + β não precisa valer 1.
- β só se calcula com um valor verdadeiro do parâmetro diferente do de H0 (dado pelo enunciado ou pela hipótese alternativa).
- Poder cresce com a distância ao valor de H0, com o tamanho da amostra e com α.
- Função potência: decrescente no teste à esquerda, crescente no teste à direita, decresce e depois cresce no bilateral (não monótona); no valor de H0 vale α.
- Teste ótimo: rejeita H0 quando p0/p1 < k; UMP maximiza o poder para um α dado e só existe em casos especiais.
- Uniforme (a, b): densidade 1/(b − a); P(m < X < o) = (o − m)/(b − a); α com o intervalo de H0, β com o intervalo verdadeiro na região de não rejeição.

# SINTÉTICO

- **Erro tipo I**: rejeitar H0 sendo verdadeira (falso positivo); sua probabilidade é o nível de significância α, também chamado tamanho do teste.
- **Erro tipo II**: não rejeitar H0 sendo falsa (falso negativo), com probabilidade β; só se calcula supondo um valor verdadeiro do parâmetro diferente do de H0.
- **Complementares**: 1 − α é o nível de confiança e 1 − β é o poder. Os dois erros não são complementares entre si: α + β pode ser menor, igual ou maior que 1.
- **Evento × probabilidade**: o erro é o evento (rejeitar ou não rejeitar na situação errada); α e β são as probabilidades desses eventos.
- **Função potência**: π(μ1) é o poder em função do parâmetro verdadeiro; no valor de H0 vale α, seu mínimo.
- **O que aumenta o poder**: maior distância entre o parâmetro verdadeiro e o de H0, maior amostra e maior α (a região de não rejeição encolhe e β cai).
- **Forma da função**: estritamente decrescente no teste à esquerda, estritamente crescente no teste à direita e não monótona (decresce, depois cresce) no bilateral.
- **Teste ótimo e UMP**: o ótimo rejeita H0 quando a razão de verossimilhanças p0/p1 é menor do que k; o UMP maximiza o poder para um α fixado e só existe em casos especiais, como a família exponencial.
- **Uniforme**: densidade 1/(b − a) em (a, b); P(m < X < o) = (o − m)/(b − a). α usa o intervalo de H0 sobre a região de rejeição; β usa o intervalo verdadeiro sobre a região de não rejeição.

# NOTAS

- Gráficos das páginas 15, 19, 20, 21, 22 e 25 não foram extraídos; o conteúdo deles é descrito no texto e foi reconstruído em palavras. A figura da página 22 (duas curvas de poder, n = 25 e n = 100, teste bilateral em μ = 60) foi resumida só pela conclusão.
- Página 16: o material afirma que os erros "não são complementares: α + β = 1" em destaque; leia-se "α + β não é necessariamente 1", como o texto explica logo depois (a soma pode até exceder 1).
- Página 23 (questão da DPE-RJ, item II): a justificativa do gabarito menciona "valores compatíveis com H0" ao definir teste uniformemente mais poderoso, mas a definição correta refere-se aos valores da hipótese alternativa; o resumo segue a definição das páginas 22 (poder maximizado contra H1, com nível α).
- Página 22: o supremo (sup) aparece como "menor limite superior"; usei apenas o sentido de "valor máximo" da probabilidade de rejeitar H0 quando verdadeira.
