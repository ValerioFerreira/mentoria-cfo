---
id: est-tamanho-amostral
subject: estatistica
title: Tamanho da amostra, assimetria e curtose
short: Tamanho amostral, assimetria e curtose
subtitle: Itens 1 e 3.2 do edital de Estatística: dimensionamento de amostras (média e proporção), alocação em estratos e medidas de assimetria e curtose
weight: 0.08
order: 2
resolves: est-tamanho-amostral,est-assimetria-curtose
onlyContests: "PCPE_AGENTE"
---

## O que este material cobre e como estudar

Pessoal, este material fecha dois pontos do edital de Estatística da Polícia Civil:

1. **Tamanho amostral** (item 3.2): quantas unidades é preciso pesquisar para estimar uma média ou uma proporção com certa **precisão** e **confiança**; e como repartir a amostra entre **estratos**;
2. **Assimetria e curtose** (item 1, medidas descritivas): o formato da distribuição, e como a banca costuma cobrar isso, de forma conceitual (interpretar o sinal de um coeficiente, comparar média, mediana e moda).

> **Dica de prova:** as questões de tamanho amostral costumam entregar o valor de z e pedir só a conta de n (arredondando **sempre para cima**). Já as de assimetria e curtose são, quase sempre, de **interpretação**: sinal do coeficiente, posição da média em relação à mediana e à moda, e nomes (platicúrtica, mesocúrtica, leptocúrtica).

## 1. Ideias básicas

- **População**: o conjunto completo que se quer estudar (tamanho **N**). **Amostra**: um subconjunto da população (tamanho **n**).
- **Parâmetro** é a medida da população (média μ, proporção p, desvio padrão σ); **estimativa** (ou estatística) é a medida calculada na amostra (x̄, p̂, s).
- **Erro amostral máximo (E), ou margem de erro**: a distância máxima tolerada entre a estimativa e o parâmetro. Exemplo: "estimar a proporção com erro de no máximo 3 pontos percentuais" significa E = 0,03.
- **Nível de confiança (1 − α)**: a probabilidade de o intervalo construído conter o parâmetro. Para cada nível há um valor crítico **z** da distribuição normal padrão:

| Confiança | z |
|---|---|
| 90% | 1,645 |
| 95% | 1,96 |
| 99% | 2,576 |

(Em provas, o valor de z costuma ser fornecido ou descrito como "percentil da normal".)

## 2. Tamanho da amostra para estimar uma média

A margem de erro de uma média com desvio padrão σ conhecido é E = z · σ/√n. Isolando n:

**n = (z · σ / E)²**

- Quanto **maior** a variabilidade (σ) e a confiança (z), **maior** o n necessário.
- Quanto **menor** o erro tolerado (E), **maior** o n.
- Arredonda-se **sempre para cima** (o inteiro imediatamente maior), porque uma amostra menor não garantiria a precisão.

> **Exemplo 1.** σ = 15, erro máximo E = 3 e confiança de 95% (z = 1,96): n = (1,96 · 15/3)² = 9,8² = 96,04 ⟹ **n = 97**.

### População finita

Se a amostra for uma fração apreciável da população (por exemplo, mais de 5% de N), corrige-se o resultado. Sendo **n₀** o valor da fórmula anterior:

**n = n₀ / [1 + (n₀ − 1)/N]** (equivale a n = N · n₀ / (N + n₀ − 1))

> **Exemplo 2.** Mesmos dados do exemplo 1, mas com população de N = 500: n = 96,04 / (1 + 95,04/500) ≈ 96,04/1,190 ≈ 80,7 ⟹ **n = 81**. A correção reduz a amostra necessária; quanto menor a população, maior a redução. Para N muito grande, n ≈ n₀.

## 3. Tamanho da amostra para estimar uma proporção

A margem de erro de uma proporção é E = z · √[p(1 − p)/n]. Isolando n:

**n₀ = z² · p · (1 − p) / E²**

- Se há uma **estimativa prévia** de p, use-a.
- Se **não há informação** sobre p, use **p = 0,5**, o pior caso (o que maximiza p(1 − p) = 0,25) e que garante a precisão para qualquer valor de p. Então **n₀ = z² / (4E²)**.

> **Exemplo 3.** Pesquisa sobre aprovação, sem estimativa prévia, confiança de 95% e erro de 3 pontos percentuais (E = 0,03): n₀ = 1,96² · 0,25 / 0,03² = 3,8416 · 0,25 / 0,0009 = 1.067,1 ⟹ **n = 1.068**.

> **Exemplo 4.** Com 99% de confiança (z = 2,576) e E = 0,05, sem informação prévia: n₀ = 2,576² · 0,25 / 0,05² = 663,6 ⟹ **n = 664**.

> **Exemplo 5.** Estimativa prévia p = 0,2, confiança de 95% e E = 0,04: n₀ = 1,96² · 0,2 · 0,8 / 0,04² = 3,8416 · 0,16 / 0,0016 = 384,16 ⟹ **n = 385**.

Com **população finita** (N conhecido), aplica-se a mesma correção do item anterior. Para o exemplo 3 com N = 2.000: n = 1.067,11 / (1 + 1.066,11/2.000) ≈ 696,1 ⟹ **n = 697**.

### Como o tamanho reage às mudanças (julgamentos rápidos)

- n é proporcional a **σ²** (ou a p(1 − p)) e a **z²**; é **inversamente proporcional a E²**.
- **Reduzir o erro pela metade quadruplica n** (E/2 ⟹ n × 4). Exemplo: no exemplo 1, com E = 1,5 em vez de 3, n passa de 96,04 para 384,16.
- **Passar de 95% para 99%** de confiança aumenta n (z sobe de 1,96 para 2,576): n cresce na razão (2,576/1,96)² ≈ 1,73.
- O tamanho **não** depende diretamente da população, desde que ela seja grande em relação à amostra. Dobrar N **não** dobra n.
- O tamanho da amostra **não garante** representatividade se a seleção não for aleatória: a fórmula pressupõe amostragem aleatória.

## 4. Amostragem estratificada: como repartir a amostra

Na amostragem **estratificada**, a população é dividida em **estratos** (grupos homogêneos, como faixas de idade ou bairros) e sorteia-se em cada um. Dado o tamanho total **n**, a divisão entre os estratos pode ser:

- **Uniforme:** n/H unidades em cada um dos H estratos;
- **Proporcional:** cada estrato recebe uma fração proporcional ao seu tamanho: **nₕ = n · Nₕ/N**;
- **Ótima (de Neyman):** proporcional ao tamanho **e ao desvio padrão** do estrato: **nₕ = n · Nₕσₕ / Σ(Nₖσₖ)**. Estratos maiores e mais variáveis recebem mais unidades.

> **Exemplo 6.** População com dois estratos: N₁ = 400 (σ₁ = 5) e N₂ = 600 (σ₂ = 10); amostra total n = 100.
> **Proporcional:** n₁ = 100 · 400/1.000 = **40** e n₂ = 100 · 600/1.000 = **60**.
> **Neyman:** Σ Nσ = 400·5 + 600·10 = 8.000; n₁ = 100 · 2.000/8.000 = **25** e n₂ = 100 · 6.000/8.000 = **75**. O estrato 2, maior e mais variável, ganha mais unidades.

**Amostragem sistemática:** com população ordenada de tamanho N e amostra desejada n, o **intervalo de seleção** é **k = N/n**. Sorteia-se o ponto de partida entre 1 e k e toma-se uma unidade a cada k. Exemplo: N = 1.200 e n = 48 ⟹ k = **25**.

## 5. Assimetria

A **assimetria** descreve se a distribuição é **simétrica** ou se tem uma "cauda" mais longa de um dos lados.

| Tipo | Forma | Posição das medidas |
|---|---|---|
| **Simétrica** | cauda igual nos dois lados | média = mediana = moda |
| **Assimétrica positiva** (à direita) | cauda longa à direita | **moda < mediana < média** |
| **Assimétrica negativa** (à esquerda) | cauda longa à esquerda | **média < mediana < moda** |

A média é a medida mais "puxada" pelos valores extremos; por isso, na assimetria positiva ela fica maior que a mediana, e na negativa, menor.

### Coeficientes de assimetria

- **1º coeficiente de Pearson:** AS₁ = (x̄ − moda)/s.
- **2º coeficiente de Pearson:** AS₂ = 3 · (x̄ − mediana)/s.
- **Coeficiente de Bowley (quartílico):** AS = (Q₃ + Q₁ − 2 · Q₂)/(Q₃ − Q₁), com Q₂ a mediana; varia de −1 a +1.
- **Pelo momento centrado de 3ª ordem:** m₃/s³, com m₃ = Σ(x − x̄)³/n.

**Interpretação (vale para todos):** valor **positivo** ⟹ assimetria positiva; **negativo** ⟹ assimetria negativa; **zero** ⟹ simétrica. Quanto maior o módulo, mais acentuada a assimetria.

> **Exemplo 7.** x̄ = 52, moda = 48, mediana = 50, s = 8, Q₁ = 44 e Q₃ = 60: AS₁ = (52 − 48)/8 = **0,5**; AS₂ = 3 · (52 − 50)/8 = **0,75**; Bowley = (60 + 44 − 2 · 50)/(60 − 44) = 4/16 = **0,25**. Todos positivos: distribuição assimétrica positiva (cauda à direita).

## 6. Curtose

A **curtose** mede o "achatamento" da distribuição (o peso das caudas e a altura do pico) em relação à **curva normal**.

| Tipo | Forma | Interpretação |
|---|---|---|
| **Mesocúrtica** | como a normal | curtose de referência |
| **Leptocúrtica** | mais **afunilada** (pico alto, caudas pesadas) | mais concentrada em torno do centro |
| **Platicúrtica** | mais **achatada** (pico baixo) | mais dispersa |

### Coeficientes de curtose

- **Coeficiente percentílico de curtose:** **K = (Q₃ − Q₁) / [2 · (P₉₀ − P₁₀)]**. Referência da normal: **K = 0,263**. **K = 0,263** ⟹ mesocúrtica; **K < 0,263** ⟹ leptocúrtica; **K > 0,263** ⟹ platicúrtica.
- **Pelo momento centrado de 4ª ordem:** **m₄/s⁴**, com m₄ = Σ(x − x̄)⁴/n. Para a normal vale **3**: acima de 3 ⟹ leptocúrtica; abaixo de 3 ⟹ platicúrtica. Muitos autores usam a **curtose em excesso**: m₄/s⁴ − 3 (0 para a normal; positiva ⟹ leptocúrtica; negativa ⟹ platicúrtica).

> **Exemplo 8.** Q₁ = 44, Q₃ = 60, P₁₀ = 34 e P₉₀ = 70: K = (60 − 44)/[2 · (70 − 34)] = 16/72 ≈ **0,222**, menor que 0,263 ⟹ distribuição **leptocúrtica**.

> **Pegadinha:** o nome "platicúrtica" lembra "prato" (achatada); "leptocúrtica" lembra "leptos = fino", ou seja, mais afunilada. Assimetria e curtose são **características diferentes**: uma distribuição pode ser simétrica e leptocúrtica, por exemplo.

## 7. Exemplos para julgar (estilo certo ou errado)

1. **Para estimar uma média com erro máximo de 2, σ = 10 e confiança de 90% (z = 1,645), a amostra mínima é 68.** *Certo:* (1,645 · 10/2)² = 67,65 ⟹ 68.
2. **Reduzir pela metade a margem de erro tolerada reduz à metade o tamanho da amostra.** *Errado:* quadruplica.
3. **Sem informação prévia sobre a proporção, o tamanho de amostra mais conservador usa p = 0,5.** *Certo.*
4. **O tamanho amostral para estimar uma média independe do desvio padrão populacional.** *Errado:* é proporcional ao quadrado de σ.
5. **Em uma distribuição assimétrica positiva, a média é menor que a mediana.** *Errado:* na assimetria positiva, média > mediana > moda.
6. **Uma distribuição com curtose maior que a da normal é denominada leptocúrtica.** *Certo.*
7. **Na alocação proporcional, um estrato com 30% da população recebe 30% da amostra.** *Certo.*
8. **Na amostragem sistemática com N = 1.200 e n = 48, a amostra é formada tomando-se uma unidade a cada 25.** *Certo.*

## 8. Resumo para revisão

- Média: n = (zσ/E)². Proporção: n = z²p(1 − p)/E² (sem informação, p = 0,5). Sempre arredonde para cima.
- Metade do erro ⟹ n × 4. Mais confiança ⟹ mais n. População finita reduz n.
- Estratificada: proporcional (nₕ = nNₕ/N) e Neyman (inclui σₕ). Sistemática: k = N/n.
- Assimetria positiva: moda < mediana < média; negativa: média < mediana < moda.
- Curtose: K = 0,263 (mesocúrtica); menor, leptocúrtica; maior, platicúrtica. Normal: m₄/s⁴ = 3.

## Fontes

Conteúdo elaborado a partir de conhecimento didático padrão de Estatística (inferência, planejamento amostral e medidas descritivas, conforme manuais clássicos de Estatística Básica e Amostragem) e do edital do concurso de Agente de Polícia da PCPE (Cebraspe, itens 1 e 3.2 de Estatística). Os valores numéricos dos exemplos foram conferidos por cálculo direto. Consulta e revisão em 19/10/2026.
