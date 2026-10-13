---
id: S0454
agente: CLAUDE-L4
materia: Estatística
aula: Aula 06 — Probabilidade
trecho: estatistica/a06/s05
paginas_lidas: 59-71
---
# ANALÍTICO

Este trecho cobre a independência de três ou mais eventos (e o que se pode ou não concluir dela), o teorema da probabilidade total (probabilidade de um efeito a partir das causas) e o teorema de Bayes (caminho inverso: dado o efeito, qual a probabilidade da causa).

### Independência de três eventos

Dois eventos são independentes quando P(A ∩ B) = P(A) · P(B). Para **três** eventos A, B e C serem independentes (também dito **mutuamente independentes**), é preciso que valham **todas** estas igualdades:

- P(A ∩ B) = P(A) · P(B)
- P(A ∩ C) = P(A) · P(C)
- P(B ∩ C) = P(B) · P(C)
- P(A ∩ B ∩ C) = P(C) · P(A) · P(B)

Ou seja, independência de dois em dois **e** a regra do produto para os três juntos. Para n eventos independentes: P(A1 ∩ A2 ∩ ... ∩ An) = P(A1) · P(A2) · ... · P(An).

> 💡 **Exemplo próprio:** 5 questões com 3 alternativas, chute aleatório. Probabilidade de acertar todas: (1/3)⁵ = 1/243.

#### O que a independência não permite concluir (pegadinhas de prova)

| Informação dada | Conclusão possível? |
| --- | --- |
| Os eventos são independentes | Sim: P(interseção) = produto das probabilidades |
| P(A ∩ B ∩ C) = P(C) · P(A) · P(B) | **Não**: a igualdade tripla sozinha não garante independência |
| A, B e C independentes dois a dois | **Não** garante independência dos três juntos |
| A independente de B e B independente de C | **Nada** se pode afirmar sobre A e C |

> 💡 **Exemplo próprio (dois a dois, mas não os três):** duas moedas equilibradas. A = cara na 1ª; B = cara na 2ª; C = as duas moedas dão o mesmo resultado. Cada par é independente (todas as interseções de pares valem 1/4 = 1/2 · 1/2), mas P(A ∩ B ∩ C) = 1/4, e não 1/8. Logo os três não são independentes.

> 💡 **Exemplo próprio (A e B independentes, B e C independentes, A e C dependentes):** o 1º e o 2º lançamentos são de moedas equilibradas; o 3º lançamento usa moeda viciada se o 1º deu cara e equilibrada caso contrário. O 3º depende do 1º, mas não do 2º.

Também é importante saber que **os complementares preservam a independência**: se A e B são independentes, então B e o complementar de A também são (e A e o complementar de B; e os dois complementares). Isso aparece em questões do tipo "B é independente do complementar de C".

> ⚠️ **Pegadinha:** independência não é o mesmo que ser mutuamente excludente. Eventos excludentes (interseção vazia) com probabilidades não nulas são **dependentes**: se um ocorre, o outro não pode ocorrer.

#### Uso prático: "nenhum" e "pelo menos um"

Para eventos independentes, a probabilidade de **nenhum** ocorrer é o produto dos complementares, e a de **pelo menos um** é o complemento disso.

> 💡 **Exemplo próprio:** três tentativas independentes, cada uma com 20% de sucesso. Nenhum sucesso: 0,8 · 0,8 · 0,8 = 0,512. Pelo menos um sucesso: 1 − 0,512 = 0,488.

### Teorema da probabilidade total

Serve para achar a probabilidade de um evento E quando se conhece sua probabilidade **dentro de cada grupo** (causa) e o peso de cada grupo. Os grupos H1, H2, ..., Hn devem **dividir o espaço amostral** (não se sobrepõem e juntos cobrem tudo; por exemplo, "fabricante A, B ou C", ou "A e não A"). Então E "se espalha" pelos grupos:

P(E) = P(E ∩ H1) + P(E ∩ H2) + ... + P(E ∩ Hn)

Pelo teorema da multiplicação, cada interseção é P(E | Hk) · P(Hk), o que dá a forma usual:

**P(E) = P(E | H1) · P(H1) + P(E | H2) · P(H2) + ... + P(E | Hn) · P(Hn)**

É uma **média ponderada** das probabilidades condicionais, com pesos iguais às participações dos grupos (que somam 1).

> 💡 **Exemplo próprio:** três máquinas produzem 50%, 30% e 20% das peças, com defeito em 2%, 3% e 5% das peças de cada uma. P(defeito) = 0,5 · 0,02 + 0,3 · 0,03 + 0,2 · 0,05 = 0,010 + 0,009 + 0,010 = 0,029 = 2,9%.

Dicas de resolução:

- Identifique o que é o **grupo** (aquilo que o enunciado diz "dentro de") e o que é o **efeito** E.
- Se o enunciado dá só a participação de um grupo e o outro é o complemento, calcule: P(2º grupo) = 1 − P(1º grupo). Se dois grupos têm "mesma proporção", cada um pesa 1/2.
- Se a pergunta é o complemento do evento (por exemplo, "não queimar"), calcule P(E) e depois 1 − P(E).
- Quando o enunciado encadeia percentuais (por exemplo, "20% dos processos são analisados no mês e, desses, 10% são indeferidos"), a condicional pedida é um produto encadeado: a fração deferida no mês é 20% · 90% = 18% dos processos daquele grupo.

### Teorema de Bayes

Usa-se quando se conhece P(E | Hk) (efeito dado a causa) e se quer P(Hk | E) (causa dado o efeito, isto é, "sabendo que o efeito ocorreu, qual a chance de ter vindo do grupo k"). Parte-se da definição de condicional:

P(Hk | E) = P(Hk ∩ E) ÷ P(E)

O numerador sai do teorema da multiplicação, P(E | Hk) · P(Hk); o denominador é a probabilidade total de E. Logo:

**P(Hk | E) = P(E | Hk) · P(Hk) ÷ [ P(E | H1) · P(H1) + ... + P(E | Hn) · P(Hn) ]**

Ou seja: a parte do evento E que vem do grupo k, dividida pelo evento E inteiro.

> 💡 **Exemplo próprio (continuação das máquinas):** uma peça sorteada é defeituosa. Chance de ter vindo da primeira máquina: 0,010 ÷ 0,029 = 10/29 ≈ 34,5%. Para a segunda: 0,009 ÷ 0,029 ≈ 31,0%; para a terceira: 0,010 ÷ 0,029 ≈ 34,5%. As três chances (posteriores) somam 100%.

> 💡 **Exemplo próprio (teste diagnóstico):** 2% das pessoas têm certa doença; o teste dá positivo em 90% dos doentes e em 10% dos sadios. P(positivo) = 0,02 · 0,9 + 0,98 · 0,1 = 0,018 + 0,098 = 0,116. P(doente | positivo) = 0,018 ÷ 0,116 ≈ 15,5%. Mesmo com teste "bom", a chance de doença é baixa quando a doença é rara.

> ⚠️ **Pegadinha:** P(A | B) e P(B | A) são coisas diferentes. A questão de Bayes costuma dar a probabilidade na direção "causa → efeito" e perguntar a direção contrária. Muitos erros vêm de responder com o dado do enunciado (P(E | Hk)) em vez de aplicar a fórmula.

Como reconhecer: o enunciado informa os grupos e seus pesos, informa a proporção do efeito em cada grupo e diz que **o efeito já ocorreu** ("sabendo que foi inadimplente...", "constatou-se que a ação é do tipo...", "recebeu análise favorável"); a pergunta é sobre a **origem** do efeito.

### Quadro-resumo

| Conceito | Fórmula |
| --- | --- |
| Condicional | P(B dado A) = P(A ∩ B) ÷ P(A) |
| Multiplicação | P(A ∩ B) = P(B dado A) · P(A) |
| Probabilidade total | P(E) = soma de P(E dado Hk) · P(Hk) |
| Bayes | P(Hk dado E) = P(E dado Hk) · P(Hk) ÷ P(E) |
| Independência (2 eventos) | P(A ∩ B) = P(A) · P(B) |
| Independência (3 eventos) | os três pares e o produto triplo |

### Para fixar
- Três eventos são independentes só se valerem as três igualdades de pares e a do produto triplo; o produto triplo sozinho ou os pares sozinhos não bastam.
- Se A independe de B e B independe de C, nada se conclui sobre a relação entre A e C.
- Complementares preservam a independência; eventos excludentes de probabilidade não nula são dependentes.
- "Nenhum" = produto dos complementares; "pelo menos um" = 1 menos esse produto.
- Probabilidade total: média ponderada das probabilidades condicionais pelos pesos dos grupos, que devem dividir o espaço amostral.
- Bayes inverte a condicional: P(causa | efeito) = parte do efeito vinda da causa ÷ probabilidade total do efeito.
- O denominador de Bayes é a probabilidade total do efeito; as probabilidades de todas as causas, dado o efeito, somam 1.
- Atenção ao sentido da condicional: não confundir P(A | B) com P(B | A).

# SINTÉTICO

- **Independência de 3 eventos**: exige os três pares (A e B, A e C, B e C) e o produto triplo; todos juntos.
- **Recíprocas falsas**: produto triplo igual ao produto das probabilidades, ou independência dois a dois, não provam independência dos três.
- **Transitividade falsa**: ligar A a B e B a C por independência não significa que A e C sejam independentes.
- **Complementares**: se dois eventos são independentes, também o são os seus complementares e as combinações entre evento e complementar.
- **Nenhum e pelo menos um**: com eventos independentes, nenhum = produto dos complementares; pelo menos um = 1 menos esse produto.
- **Probabilidade total**: P(E) = soma de P(E | grupo) · P(grupo); os grupos devem dividir o espaço amostral.
- **Complemento do grupo**: se um grupo é dado, o outro vale 1 menos ele; em "mesma proporção" cada um tem metade.
- **Bayes**: P(grupo | E) = P(E | grupo) · P(grupo) ÷ P(E); o denominador é a probabilidade total.
- **Reconhecer Bayes**: o efeito já ocorreu e a pergunta é a origem; as causas somam 100% após o condicionamento.

# NOTAS

- Página 59: o trecho começa no fim de uma questão de eventos independentes (probabilidade de pelo menos um); resumi só o método (complementar do "nenhum"), sem usar os números dela.
- Página 64 do material: na questão do auditor aparece "P(C|A) 0,4" sem o sinal de igual (erro de digitação); os valores usados na resolução estão corretos.
- Página 66: a questão sobre processos usa o encadeamento "analisados no mês × deferidos entre os analisados"; usei a ideia de produto encadeado em texto, sem reproduzir a questão.
- Figuras (diagramas de Venn do teorema da probabilidade total) não foram extraídas; descrevi a ideia em texto.
- Os exemplos das moedas (A, B, C dois a dois independentes mas não os três; e C como "mesmo resultado") e o do teste diagnóstico são próprios; conferi os valores: pares 1/4 cada e produto triplo 1/4, versus 1/8 esperado; 0,018 ÷ 0,116 ≈ 15,5%.
