---
id: S0538
agente: CLAUDE-L4
materia: Estatística
aula: Aula 11 — Testes de Hipóteses
trecho: estatistica/a11/s01
paginas_lidas: 5-13
---
# ANALÍTICO

Um teste de hipóteses decide, com base em uma amostra, se uma afirmação sobre um parâmetro populacional merece ser rejeitada. O trecho apresenta as hipóteses nula e alternativa, a região crítica e a de não rejeição, o nível de significância, a decisão pelo intervalo de confiança, os testes bilateral e unilaterais, a classificação das hipóteses em simples e compostas e como deduzir H0 e H1 a partir de um enunciado.

### Ideia geral do teste

Alguém afirma algo sobre um parâmetro (por exemplo, "a média da população é 2"). Extrai-se uma amostra, calcula-se a estatística correspondente (a média amostral) e decide-se se o resultado é compatível com a afirmação. Se o valor observado fica perto do afirmado, não há razão para discordar; se fica muito longe, discorda-se. O estudo do tema é justamente definir **qual é o limite** entre "perto" e "longe".

> 💡 **Exemplo próprio:** uma padaria afirma que seus pães pesam 50 g, em média. Uma amostra de pães com média de 49,8 g sugere que a afirmação é plausível; uma com média de 38 g, não.

### Hipótese nula e hipótese alternativa

- **Hipótese nula (H0)**: a suposição que se testa, aquela que se considera verdadeira até que a amostra a contrarie (por exemplo, μ = 2). Também chamada hipótese de nulidade.
- **Hipótese alternativa (H1 ou HA)**: a suposição de que H0 é **falsa** (por exemplo, μ ≠ 2).

As duas são **mutuamente excludentes**: se uma é verdadeira, a outra é falsa. Todo teste começa com H0 tida como verdadeira.

### Região de não rejeição, região crítica e nível de significância

Supondo H0 verdadeira, constrói-se um intervalo de confiança de nível 1 − α em torno do parâmetro de H0 (os detalhes dependem da situação). Esse intervalo divide os resultados possíveis da estatística em duas regiões:

| Região | Onde fica | Probabilidade (com H0 verdadeira) | Decisão |
| --- | --- | --- | --- |
| **Não rejeição (RNR)** | dentro do intervalo | 1 − α | não rejeitar H0 |
| **Crítica (RC)** | fora do intervalo | α | rejeitar H0 |

A probabilidade **α** é o **nível de significância**: a chance de rejeitar H0 quando ela é verdadeira. Valores comuns são 5% e 1%.

**Regra de decisão (teste bilateral):** rejeita-se H0 se X̄ < LINF ou X̄ > LSUP; não se rejeita se LINF ≤ X̄ ≤ LSUP, sendo LINF e LSUP os limites inferior e superior do intervalo.

> 💡 **Exemplo próprio:** H0: μ = 50, e o intervalo de 95% em torno de 50 é (48; 52). Uma média amostral de 51 cai na RNR (não rejeita); uma de 47 cai na RC (rejeita).

### "Não rejeitar" não é "aceitar"

A **rejeição é a decisão forte**: se H0 fosse mesmo verdadeira, cair na região crítica teria probabilidade de apenas α (pequena). Rejeitar, portanto, gera **evidência estatística** contra H0, e se diz que o teste é **significante**.

Já a não rejeição não prova que H0 é verdadeira: o resultado pode ter sido apenas insuficiente para contrariá-la. Por isso se diz "não rejeitamos H0", e o teste é **não significante**, sem evidência estatística. É possível que μ seja de fato o valor de H0 e a amostra tenha dado um valor distante, mas isso é improvável.

> ⚠️ **Pegadinha:** "o teste gera evidência estatística tanto na rejeição quanto na aceitação" é falso. Só a rejeição de H0 gera evidência.

### Decidir pelo intervalo de confiança da amostra

Há um caminho equivalente: construir o intervalo de confiança **a partir da estatística da amostra** e verificar se o parâmetro de H0 está dentro dele.

- Se o intervalo **contém** o valor de H0: **não rejeita** H0.
- Se **não contém**: **rejeita** H0.

> 💡 **Exemplo próprio:** H0: μ = 50. Amostra com média 49,5 e intervalo (48,7; 50,3): contém 50, não se rejeita. Outra amostra com média 45 e intervalo (44,2; 45,8): não contém 50, rejeita-se.

Em questão com vários intervalos de confiança, a região em que se pode rejeitar a hipótese de, digamos, 50% é aquela cujo intervalo **não inclui 50**, ainda que o intervalo fique apenas encostado fora do valor.

### Teste bilateral e testes unilaterais

O formato da região crítica depende de H1. Seja θ o parâmetro e θ0 o valor de H0:

| Teste | H0 | H1 | Região crítica | Rejeita H0 se |
| --- | --- | --- | --- | --- |
| **Bilateral** (bicaudal, não direcional) | θ = θ0 | θ ≠ θ0 | dividida nos dois extremos (α/2 em cada) | X̄ < LINF ou X̄ > LSUP |
| **Unilateral à esquerda** (direcional) | θ = θ0 (ou θ ≥ θ0) | θ < θ0 | só à esquerda (α) | X̄ < LINF |
| **Unilateral à direita** (direcional) | θ = θ0 (ou θ ≤ θ0) | θ > θ0 | só à direita (α) | X̄ > LSUP |

Unilateral também é chamado unicaudal ou monocaudal. A hipótese alternativa é **direcional** nos unilaterais (afirma maior ou menor) e **não direcional** nos bilaterais (afirma apenas "diferente").

A escolha vem do problema. Se um lote só deve ser recusado quando o conteúdo for **menor** que o prometido (não há problema em vir mais), o teste é unilateral à esquerda. Se uma peça só causa problema quando for **maior** que um limite (menor encaixa), o teste é unilateral à direita.

Sobre os limites da região crítica: no teste à esquerda, a RC tem limite **superior** (coincide com o limite inferior da RNR); no teste à direita, tem limite **inferior**; no bilateral, nenhuma das duas caudas tem limite do lado de fora, então não se diz que a RC é limitada em ambos os sentidos.

### Hipóteses simples e compostas

- **Simples**: especifica o valor do parâmetro, com **igualdade** (μ = 2).
- **Composta**: traz informação sobre a distribuição sem fixar o valor, sem igualdade (μ > 2, μ ≠ 2, μ ≤ 2).

Normalmente H0 é simples e H1 composta, mas não é obrigatório: nos unilaterais, H0 pode ser composta (μ ≥ 2 ou μ ≤ 2). H1 pode ser simples quando só há dois valores possíveis (H0: μ = 2 contra H1: μ = 1,5, ambas simples).

### Como deduzir H0 e H1 de um enunciado

Quando o texto não diz quais são as hipóteses, **a afirmação que se quer comprovar entra como H1**. Só se concorda com ela se o teste for significante (se rejeitar H0). H0 é o contrário, incluindo a igualdade.

| Objetivo do enunciado | H0 | H1 |
| --- | --- | --- |
| Demonstrar que a renda média é **menor** que 1.000 | μ ≥ 1.000 | μ < 1.000 |
| Demonstrar que a média **superou** um valor | μ ≤ valor | μ > valor |
| Verificar se a média **mudou** | μ = valor | μ ≠ valor |

> ⚠️ **Pegadinha:** o raciocínio do enunciado pode inverter o óbvio. Na questão em que a prioridade é nunca negar o benefício a quem precisa (mesmo concedendo a quem pode pagar), só se nega o serviço em caso excepcional, de renda **comprovadamente acima** da linha de corte. Assim a renda acima da referência é H1 (só se aceita se o teste for significante) e H0 é "renda menor ou igual". O erro mais grave a evitar define o que fica como H0.

### Para fixar
- H0 é a suposição testada; H1 a nega; são mutuamente excludentes.
- RNR tem probabilidade 1 − α; RC tem α (nível de significância).
- Rejeitar H0 gera evidência estatística; não rejeitar não é aceitar.
- Pelo intervalo da amostra: rejeita H0 se o valor de H0 estiver fora do intervalo.
- Bilateral: H1 com ≠ e α/2 em cada cauda; unilaterais: H1 com < ou > e α em uma cauda (direcionais).
- Simples: com igualdade; composta: sem igualdade; H0 pode ser composta nos unilaterais.
- O que se quer provar vai em H1; H0 inclui a igualdade.

# SINTÉTICO

- **H0 e H1**: H0 é a suposição inicial tida como verdadeira; H1 afirma que H0 é falsa, e as duas são mutuamente excludentes.
- **Regiões**: a região de não rejeição tem probabilidade 1 − α e a crítica tem α; o α é o nível de significância (chance de rejeitar H0 sendo verdadeira).
- **Decisão**: rejeita-se H0 quando a estatística cai na região crítica (fora de LINF e LSUP no bilateral).
- **Rejeição × aceitação**: rejeitar é a decisão forte e gera evidência estatística; não rejeitar não prova H0 e o teste é dito não significante.
- **Pelo intervalo de confiança da amostra**: rejeita-se H0 se o intervalo construído da amostra não contém o valor de H0.
- **Bilateral**: H1 usa ≠ (não direcional) e a região crítica se divide em α/2 nas duas caudas.
- **Unilateral**: H1 usa < (teste à esquerda) ou > (à direita), é direcional e concentra α em uma única cauda.
- **Simples × composta**: simples fixa o parâmetro com igualdade; composta não (>, <, ≠); em unilaterais, H0 pode ser μ ≥ ou μ ≤ valor.
- **Dedução das hipóteses**: o que se deseja comprovar vai em H1, e H0 é o contrário com a igualdade.

# NOTAS

nenhuma. Tabelas de exemplo e curvas com regiões sombreadas foram descartadas por apenas ilustrarem. Os exemplos numéricos são próprios. As páginas 11-13 trazem questões comentadas (CESPE e FGV); seus ensinamentos (H0/H1 mutuamente excludentes, evidência só na rejeição, hipótese direcional nos unilaterais, limites da região crítica, dedução de H1 a partir do objetivo) foram incorporados ao texto.
