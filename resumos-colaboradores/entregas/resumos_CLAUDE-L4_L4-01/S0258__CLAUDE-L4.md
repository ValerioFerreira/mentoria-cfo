---
id: S0258
agente: CLAUDE-L4
materia: Estatística
aula: Complemento 01 — Estatística: probabilidade geométrica, normas de apresentação de dados e amostragem
trecho: estatistica/c01/s01
paginas_lidas: 1-8
---
# ANALÍTICO

Este complemento cobre três pontos que costumam faltar na preparação: a probabilidade geométrica, as normas de apresentação tabular do IBGE e os tipos de amostragem. As questões sobre os dois últimos pedem identificar uma regra ou nomear a técnica descrita; a primeira rende contas curtas de razão entre áreas.

### Probabilidade geométrica
Na definição clássica o espaço amostral é finito e equiprovável: P(A) = casos favoráveis ÷ casos possíveis. Quando o espaço é contínuo (um instante dentro de uma hora, um ponto num alvo), não há o que contar; mede-se. Escolhendo um ponto "ao acaso" (distribuição **uniforme**) numa região Ω, a probabilidade de cair na parte A é:

**P(A) = medida(A) ÷ medida(Ω)**

A medida é o comprimento em uma dimensão, a área em duas e o volume em três. Vale todo o cálculo dos axiomas (P ≥ 0, P(Ω) = 1, aditividade para disjuntos), inclusive o complementar.

> ⚠️ **Pegadinha:** um ponto ou uma linha tem medida zero e, portanto, probabilidade zero, mas pode ocorrer. Em espaço contínuo, P = 0 não significa evento impossível (o contrário vale: impossível implica P = 0). Pelo mesmo motivo, incluir ou excluir a fronteira não muda a probabilidade: P(X ≤ 3) = P(X < 3).

- **Uma dimensão**: coincide com a uniforme contínua. Se X ~ U(a, b), então P(c ≤ X ≤ d) = (d − c) ÷ (b − a).
- **Duas dimensões**: razão de áreas. Figuras semelhantes têm áreas na razão do quadrado dos lados; dobrar o raio quadruplica a área.

> 💡 **Exemplo (alvo):** num alvo circular de raio 10 cm, o disco central tem raio 2 cm. A área do alvo é 100π e a do centro, 4π, logo P = 4%. O π some na divisão; basta comparar quadrados de raios.

**Problema do encontro.** Duas pessoas chegam em instantes aleatórios dentro de um intervalo T e cada uma espera t minutos. Com x e y como chegadas, o espaço é um quadrado de lado T e há encontro quando |x − y| ≤ t. A região desfavorável são dois triângulos de catetos T − t, e então:

**P(encontro) = 1 − ((T − t) ÷ T)²**

> 💡 **Exemplo:** T = 60 min e espera de 20 min: P = 1 − (40/60)² = 1 − 4/9 = 5/9.

Roteiro geral: defina as variáveis e seus intervalos; desenhe o espaço; escreva o evento como desigualdade e desenhe a região; divida a área favorável pela total, usando o complementar se for mais fácil. Outros modelos clássicos: dois números em [0, 1] com soma menor ou igual a 1/2 (triângulo de área 1/8, P = 1/8); vara quebrada em dois pontos formando triângulo (P = 1/4); agulha de Buffon, em que uma agulha de tamanho L, menor ou igual à distância d entre retas paralelas, toca uma reta com P = 2L ÷ (π·d). O paradoxo de Bertrand lembra que "ao acaso" precisa vir com a variável uniforme definida.

### Normas de apresentação de dados (IBGE)
A **tabela** traz dados numéricos e tem laterais abertas; o **quadro** traz informação textual e é fechado nas laterais.

**Elementos da tabela**
- **Título**, acima, responde o quê, onde e quando.
- **Cabeçalho** (conteúdo das colunas) e **coluna indicadora** (conteúdo das linhas).
- **Corpo**: o conjunto de linhas e colunas; cada cruzamento é uma **casa**, que nunca fica em branco.
- **Fonte**, obrigatória, no rodapé.
- **Notas** são esclarecimentos gerais; **chamadas** referem-se a células específicas, numeradas entre parênteses.
- A unidade de medida aparece no cabeçalho ou na coluna indicadora.

**Construção**: traços horizontais fecham a tabela em cima e embaixo; os verticais nas laterais não existem, e entre colunas são facultativos. Tabela que passa de uma página não fecha o rodapé e repete o cabeçalho, com "Continua" e "Conclusão". Colunas de mesma natureza têm o mesmo número de casas decimais.

**Sinais convencionais**
| Sinal | Significado |
| --- | --- |
| − (traço) | Zero absoluto: o fenômeno não ocorreu |
| ... | Dado não disponível |
| .. | Não se aplica |
| ? | Dúvida quanto à exatidão |
| 0, 0,0 | Zero por arredondamento de valor positivo pequeno |
| x | Omitido por sigilo, para não identificar o informante |

> ⚠️ **Pegadinha:** traço não é dado desconhecido (esse é "..."), e "x" não quer dizer valor ignorado, e sim protegido. Nas questões, procure o defeito: falta de título ou fonte, laterais fechadas, célula vazia, sinal com sentido trocado.

### Amostragem
**Vocabulário.** População (N) é o conjunto de interesse; censo investiga todos; amostra (n) é a parte observada. Parâmetro descreve a população (μ, σ, p); estatística descreve a amostra (x̄, s, p̂). O cadastro é a lista de onde se sorteia. O **erro amostral** é inevitável, diminui com n maior e só é mensurável em amostras probabilísticas; o **viés** vem de falha no plano e não some aumentando n. Amostra **aleatória** é aquela em que cada elemento tem chance conhecida e positiva de ser escolhido.

| Técnica | Como funciona | Observação |
| --- | --- | --- |
| Aleatória simples | Sorteio direto; mesma chance para todos | Com reposição há Nⁿ amostras ordenadas; sem reposição, C(N, n) |
| Sistemática | k = N ÷ n; sorteia-se a partida e tomam-se os elementos de k em k | Risco se a lista tiver ciclo igual a k |
| Estratificada | Divide em estratos homogêneos por dentro e sorteia em todos | Alocação uniforme, proporcional ou ótima |
| Conglomerados | Sorteia grupos inteiros, heterogêneos por dentro, e observa todos ou parte | Barata, porém menos precisa |

> 💡 **Exemplo (sistemática):** N = 600 e n = 30 dão k = 20; se a partida sorteada é 5, a amostra é 5, 25, 45, ... , 585.

> 💡 **Exemplo (proporcional):** efetivo de 800 com 560 praças e 240 oficiais, n = 80. Praças: 80 × 560/800 = 56; oficiais: 24. Na alocação **ótima de Neyman** o tamanho em cada estrato é proporcional a Nₕ·σₕ, ou seja, amostra-se mais onde há mais variabilidade.

**Estratos × conglomerados.** Em estratos, todos os grupos participam e o sorteio ocorre dentro deles, buscando precisão. Em conglomerados, apenas alguns grupos são sorteados e, neles, observa-se tudo (um estágio) ou parte (dois estágios), buscando economia.

**Não probabilísticas**: conveniência, intencional, por cotas (a escolha dentro da cota é do entrevistador), bola de neve e voluntária. Nenhuma permite calcular erro amostral.

**Tamanho da amostra.** Para proporção, com confiança de 95% (z = 1,96) e pior caso p = 0,5: n = z²·p·(1 − p) ÷ E², arredondando sempre para cima. Com E = 0,04, n = 3,8416 × 0,25 ÷ 0,0016 = 600,25, logo 601. Para média: n = (z·σ ÷ E)².

### Para fixar
- Probabilidade geométrica = medida favorável ÷ medida total, com distribuição uniforme.
- Probabilidade zero não é impossibilidade em espaço contínuo; fronteiras não importam.
- Encontro: P = 1 − ((T − t) ÷ T)².
- Tabela: título (quê, onde, quando), fonte obrigatória, laterais abertas, nenhuma casa vazia.
- Traço é zero absoluto; "..." é indisponível; "x" é sigilo.
- Estratificada sorteia em todos os grupos; conglomerados sorteia alguns grupos.
- Aumentar n reduz erro amostral, mas não corrige viés.
- Amostragem por cotas e por conveniência não são probabilísticas.

# SINTÉTICO

- **Probabilidade geométrica**: com espaço contínuo e distribuição uniforme, P(A) = medida(A) ÷ medida(Ω), usando comprimento, área ou volume.
- **Probabilidade zero**: um ponto ou linha tem P = 0 e ainda pode ocorrer; incluir ou excluir fronteiras não altera o resultado.
- **Encontro**: duas pessoas, intervalo T e espera t; P = 1 − ((T − t)/T)². Com T = 60 e t = 15, P = 7/16.
- **Modelos clássicos**: vara quebrada formando triângulo, P = 1/4; agulha de Buffon, P = 2L/(π·d).
- **Tabela × quadro**: tabela tem dados numéricos e laterais abertas; quadro é textual e fechado.
- **Elementos da tabela**: título (quê, onde, quando), cabeçalho, coluna indicadora, corpo, fonte obrigatória, notas gerais e chamadas específicas; casa nunca em branco.
- **Sinais do IBGE**: traço é zero absoluto, "..." indisponível, ".." não se aplica, "?" dúvida, "0" zero por arredondamento, "x" sigilo.
- **Aleatória simples e sistemática**: simples sorteia direto; sistemática usa k = N/n com partida sorteada e erra se a lista tiver ciclo.
- **Estratificada**: sorteia dentro de todos os estratos homogêneos; a alocação pode ser uniforme, proporcional ou ótima (Neyman, proporcional a Nₕ·σₕ).
- **Conglomerados**: sorteia grupos heterogêneos inteiros; é econômica e menos precisa.
- **Não probabilísticas**: conveniência, intencional, cotas, bola de neve e voluntária não permitem calcular erro amostral.
- **Tamanho da amostra**: proporção n = z²·p·(1 − p)/E², arredondando para cima.

# NOTAS

nenhuma
