---
id: est-complementos-edital
subject: estatistica
title: Estatística: probabilidade geométrica, normas de apresentação de dados e amostragem
short: Prob. geométrica, normas e amostragem
subtitle: Itens 1 e 2 do edital de Estatística: normas para apresentação de dados (IBGE), amostra aleatória e probabilidade geométrica
weight: 0.07
order: 1
resolves: est-prob-geometrica,est-normas-amostragem
---

## O que este material cobre (e por quê)

Pessoal, o curso principal de Estatística é gigante, mas deixa três pontos do edital sem teoria própria. Este complemento fecha as três lacunas:

1. **Probabilidade geométrica** (item 2 do edital: "definição clássica, geométrica e axiomática"): o curso ensina a clássica e a axiomática, mas não a geométrica;
2. **Normas para apresentação de dados** (item 1): o curso mostra os elementos de uma tabela e os gráficos, mas não as **normas de apresentação tabular do IBGE**, que são cobradas quase em forma de "decoreba";
3. **Amostra aleatória** (item 1): o curso define amostra, mas não ensina os **tipos de amostragem** (simples, sistemática, estratificada e por conglomerados).

> **Dica de prova:** os itens 2 e 3 rendem questões "de lógica": a banca descreve uma situação (ex.: "sorteou-se um bairro e entrevistaram todos os moradores") e pede o nome da técnica. A probabilidade geométrica rende conta curta de **razão de áreas**.

## 1. Probabilidade geométrica

### 1.1 A ideia central

Na probabilidade **clássica**, o espaço amostral é **finito** e os resultados são **equiprováveis**: P(A) = casos favoráveis ÷ casos possíveis.

Mas e se o espaço amostral for **infinito e contínuo**? (Um instante entre 12h e 13h; um ponto num alvo circular; um ponto num segmento.) Não dá para contar casos. A saída é **medir**: a "chance" de um evento fica proporcional ao **tamanho** da região que ele ocupa.

> **Definição:** seja Ω uma região (segmento, figura plana ou sólido) com medida finita e positiva, e escolha-se um ponto **ao acaso** em Ω (isto é, com **distribuição uniforme**). A probabilidade de o ponto cair em uma região A contida em Ω é
>
> **P(A) = medida(A) ÷ medida(Ω)**
>
> - em **uma dimensão**, a medida é o **comprimento**;
> - em **duas dimensões**, a **área**;
> - em **três dimensões**, o **volume**.

A expressão "ao acaso" (ou "aleatoriamente") significa, nesse contexto, **uniforme**: regiões de **mesma medida** têm **mesma probabilidade**, estejam onde estiverem dentro de Ω.

| | Clássica | Geométrica |
|---|---|---|
| Espaço amostral | **Finito** | **Infinito** (contínuo) |
| Como "mede" o evento | **Conta** casos | **Mede** comprimento, área ou volume |
| Condição | Resultados equiprováveis | Pontos "igualmente prováveis" (distribuição **uniforme**) |
| Fórmula | n(A) ÷ n(Ω) | medida(A) ÷ medida(Ω) |

### 1.2 Propriedades (e uma pegadinha clássica)

A probabilidade geométrica cumpre os **axiomas de Kolmogorov**: P(A) ≥ 0, P(Ω) = 1 e P(A ∪ B) = P(A) + P(B) quando A e B são disjuntos. Por isso valem todas as regras que você já conhece (complementar, união etc.).

> **Pegadinha — probabilidade zero não é impossibilidade.** Um **ponto** (ou um segmento dentro de uma figura plana) tem comprimento/área **zero**, logo probabilidade **zero**. Mas isso **não** significa que o evento não possa ocorrer: o ponto sorteado é *algum* ponto. Em espaços contínuos, "P(A) = 0" **não** implica "A é impossível" (a recíproca, sim: impossível ⇒ P = 0). Do mesmo modo, P(A) = 1 não implica que A seja certo.

Consequência prática: em probabilidade geométrica, **incluir ou não as fronteiras não muda o resultado** (P(X ≤ 3) = P(X < 3)), porque a fronteira tem medida zero.

### 1.3 Uma dimensão: o segmento

Escolhe-se um ponto ao acaso num segmento de comprimento L. A probabilidade de ele cair num trecho de comprimento ℓ é **ℓ ÷ L**.

> **Exemplo 1.** Um ponto é escolhido ao acaso no segmento [0, 10]. Qual a probabilidade de que ele esteja entre 3 e 7?
> Comprimento favorável = 7 − 3 = 4; total = 10. **P = 4/10 = 0,4**.

Isto é exatamente a **distribuição uniforme contínua** que você estudou: se X ~ U(a, b), então P(c ≤ X ≤ d) = (d − c) ÷ (b − a). **A probabilidade geométrica em uma dimensão é a uniforme contínua com outro nome.**

### 1.4 Duas dimensões: a razão de áreas

> **Exemplo 2 (alvo).** Um dardo é lançado ao acaso num alvo circular de raio 10 cm (supondo que sempre acerte o alvo). O círculo central tem raio 2 cm. Qual a probabilidade de acertar o círculo central? E o anel entre os raios 6 cm e 10 cm?
>
> - Área do alvo: π · 10² = 100π.
> - Círculo central: π · 2² = 4π → **P = 4π ÷ 100π = 0,04** (4%).
> - Anel: π · (10² − 6²) = 64π → **P = 64π ÷ 100π = 0,64** (64%).
>
> Note que o π **se cancela**: em figuras circulares concêntricas, basta comparar os **quadrados dos raios**.

> **Macete:** razão de áreas de figuras **semelhantes** = (razão de lados)². Dobrar o raio do alvo **quadruplica** a área, não dobra.

### 1.5 O problema do encontro (o mais clássico da prova)

> **Exemplo 3.** Duas pessoas combinam de se encontrar num local entre 12h e 13h. Cada uma chega **num instante aleatório** dessa hora, espera a outra no máximo **15 minutos** e vai embora. Qual a probabilidade de se encontrarem?

**Montagem:** seja x o instante de chegada da primeira e y o da segunda (em minutos, de 0 a 60). O espaço amostral é o **quadrado** [0, 60] × [0, 60], de área 60 × 60 = 3.600.

Elas se encontram quando **|x − y| ≤ 15**. A região **favorável** é uma faixa em torno da diagonal; o mais fácil é calcular a **região desfavorável** (|x − y| > 15), formada por **dois triângulos retângulos** de catetos 45:

- área de cada triângulo = 45 × 45 ÷ 2 = 1.012,5;
- dois triângulos = 2.025;
- área favorável = 3.600 − 2.025 = 1.575.

**P = 1.575 ÷ 3.600 = 0,4375 = 7/16.**

Atalho: P = 1 − ((60 − 15) ÷ 60)² = 1 − (3/4)² = 1 − 9/16 = **7/16**. Se esperassem apenas 10 minutos: P = 1 − (50/60)² = 11/36 ≈ **0,3056**.

> **Passo a passo para qualquer problema geométrico:** (1) defina as variáveis (x, y) e o **intervalo de cada uma**; (2) desenhe o espaço amostral (segmento, quadrado, cubo); (3) escreva a condição do evento como uma desigualdade e **desenhe a região**; (4) calcule **área (ou comprimento) favorável ÷ total**; (5) se a região favorável for complicada, use o **complementar**.

### 1.6 Mais três modelos para treinar

> **Exemplo 4.** Dois números x e y são escolhidos ao acaso em [0, 1]. Qual a probabilidade de x + y ≤ 1/2?
> A região é um triângulo retângulo de catetos 1/2: área = (1/2 × 1/2) ÷ 2 = 1/8. O quadrado tem área 1. **P = 1/8 = 0,125.**

> **Exemplo 5 (a vara quebrada).** Uma vara de comprimento L é quebrada em **dois pontos escolhidos ao acaso**. Qual a probabilidade de que os três pedaços formem um **triângulo**?
> Os três pedaços formam triângulo se **nenhum** deles for maior que L/2 (desigualdade triangular). Fazendo a mesma análise de regiões no quadrado dos dois pontos, a região favorável ocupa **1/4** do espaço amostral. **P = 1/4 = 0,25.**

> **Exemplo 6 (a agulha de Buffon).** Um piso é riscado com retas paralelas separadas por uma distância **d**. Joga-se ao acaso uma agulha de comprimento **L ≤ d**. A probabilidade de a agulha **tocar** alguma reta é
>
> **P = 2L ÷ (π · d)**
>
> Para L = d, P = 2/π ≈ **0,637**. É um caso famoso, porque permite **estimar π** repetindo o experimento muitas vezes. Para a prova, basta reconhecer que ele é um problema de **probabilidade geométrica** e que a fórmula envolve π.

### 1.7 Quando "ao acaso" é ambíguo (paradoxo de Bertrand)

A frase "escolha uma corda ao acaso num círculo" tem **mais de uma interpretação**: escolher dois pontos da circunferência, ou escolher o ponto médio da corda, ou escolher a direção e a distância ao centro. Cada método leva a uma **probabilidade diferente** (por exemplo, 1/3, 1/2 ou 1/4 para a corda ser maior que o lado do triângulo equilátero inscrito). Moral: **o espaço amostral e a distribuição uniforme precisam estar especificados**. Em prova, o enunciado sempre diz qual variável é uniforme.

### 1.8 Resumo rápido: probabilidade geométrica

- Espaço amostral **contínuo**; "ao acaso" = **uniforme**.
- **P(A) = medida(A) ÷ medida(Ω)** (comprimento, área ou volume).
- Em 1 dimensão = **uniforme contínua**; em 2 dimensões = **razão de áreas**.
- Pontos e linhas têm probabilidade **zero**, mas **podem ocorrer**; fronteiras não alteram o resultado.
- Encontro com espera t em um intervalo T: **P = 1 − ((T − t) ÷ T)²**.
- Obedece aos **axiomas** (Kolmogorov): então vale a regra do complementar.

## 2. Normas para apresentação de dados (IBGE)

O edital pede "normas para apresentação de dados". Na prática, a banca usa as **Normas de Apresentação Tabular do IBGE** (3ª edição, 1993), em conjunto com a ideia de que a tabela deve ser clara, completa e autoexplicativa.

### 2.1 Tabela × quadro

| | **Tabela** | **Quadro** |
|---|---|---|
| Conteúdo | **Dados numéricos** (tratamento estatístico) | Informação **textual** ou classificatória |
| Laterais | **Abertas** (sem traços verticais nas bordas) | **Fechado** (com bordas laterais) |
| Origem das normas | Normas de Apresentação Tabular (IBGE) | Convenção da ABNT para trabalhos |

### 2.2 Elementos de uma tabela

1. **Título:** colocado **acima** da tabela, deve responder, em geral na ordem, **O QUÊ** (o fenômeno), **ONDE** (local) e **QUANDO** (época). Exemplo: "População residente, por sexo, Recife (PE), 2022".
2. **Cabeçalho:** parte superior; especifica o **conteúdo de cada coluna**.
3. **Coluna indicadora:** a primeira coluna, que especifica o conteúdo das **linhas**.
4. **Corpo:** o conjunto de **linhas e colunas** com os dados.
5. **Casa (ou célula):** o cruzamento de uma linha com uma coluna. **Nenhuma casa pode ficar em branco**: cada uma recebe um **número ou um sinal convencional**.
6. **Fonte:** indica **quem forneceu** os dados (ou os elaborou). É **obrigatória** e vai no **rodapé**, precedida da palavra "Fonte".
7. **Notas:** esclarecimentos que valem para **toda a tabela** (notas gerais).
8. **Chamadas:** esclarecimentos de **células específicas** (notas específicas), indicadas por **números entre parênteses** ou sinais, numeradas de **cima para baixo e da esquerda para a direita**.

> **Unidade de medida:** deve aparecer no cabeçalho ou na coluna indicadora (ex.: "Produção (1.000 t)").

### 2.3 Regras de construção (o que mais cai)

- A tabela é **fechada em cima e embaixo** por **traços horizontais** (de preferência mais grossos).
- **Não** se fecham as laterais com traços verticais: a tabela é **aberta à direita e à esquerda**.
- O uso de traços verticais para **separar colunas** no corpo é **facultativo**.
- O **cabeçalho** é separado do corpo por traço horizontal fino.
- Se a tabela precisar de **mais de uma página**, **não** se fecha o traço inferior na primeira página e o cabeçalho é **repetido**, indicando-se "Continua" e, na última, "Conclusão".
- Os **números** devem ter o **mesmo número de casas decimais** dentro da mesma coluna, quando de mesma natureza, e alinhamento coerente.
- A **ordenação** das linhas deve seguir critério claro (cronológico, alfabético, de grandeza).

### 2.4 Sinais convencionais (decorar!)

| Sinal | Significado |
|---|---|
| **−** (traço) | Dado numérico **igual a zero não resultante de arredondamento** (isto é, o fenômeno **não ocorreu**) |
| **...** (três pontos) | Dado numérico **não disponível** (existe, mas não foi obtido) |
| **..** (dois pontos) | **Não se aplica** dado numérico |
| **?** | **Dúvida** quanto à exatidão do dado |
| **0**, **0,0**, **0,00** | Dado **igual a zero resultante de arredondamento** de um valor originalmente **positivo** |
| **−0**, **−0,0**, **−0,00** | Zero resultante do arredondamento de um valor originalmente **negativo** |
| **x** | Dado **omitido** para **evitar a individualização** da informação (sigilo estatístico) |

> **Pegadinhas de prova:**
> - **Traço** não é "dado desconhecido": traço é **zero verdadeiro**. Dado desconhecido é "**...**".
> - **"x"** serve para **proteger a identidade** (ex.: só existe uma empresa no setor, divulgar o dado revelaria o valor dela). Não é "valor ignorado".
> - **Zero** (0) significa que o valor é **menor que a metade da unidade** adotada, depois do arredondamento (o dado existe e é pequeno).
> - **Célula em branco** é **proibida**.
> - Tabelas **não** têm bordas laterais; quadros, sim.

### 2.5 Do dado à tabela: estratégia de prova

Se a questão mostra uma tabela "malfeita", procure o **erro**: falta título ou fonte? Tem traço vertical nas laterais? Célula vazia? Unidade ausente? Sinal convencional usado com sentido trocado? Quase sempre é um desses.

### 2.6 Resumo rápido: normas

- Normas do **IBGE (1993)**; tabela traz **dados numéricos**, quadro traz **texto**.
- Título: **o quê, onde, quando**. Fonte **obrigatória**. Notas (gerais) × chamadas (específicas).
- **Fechada em cima e embaixo; aberta nas laterais.** Colunas separadas por traço vertical: facultativo.
- Sinais: **−** zero real · **...** indisponível · **..** não se aplica · **?** dúvida · **0** zero por arredondamento · **x** sigilo.

## 3. Amostra aleatória: tipos de amostragem

### 3.1 Vocabulário de base

- **População:** conjunto de **todos** os elementos de interesse, com tamanho **N**.
- **Censo:** investigação de **todos** os elementos da população.
- **Amostra:** subconjunto da população, de tamanho **n**. É usada quando o censo é caro, demorado ou **destrutivo** (ex.: testar a resistência de lonas de salvamento).
- **Parâmetro:** medida que descreve a **população** (μ, σ, p), geralmente desconhecida. **Estimativa/estatística:** medida calculada na **amostra** (x̄, s, p̂).
- **Cadastro (ou quadro amostral):** a **lista** de onde a amostra é retirada (ex.: relação de efetivo do CBMPE).
- **Erro amostral:** a diferença inevitável entre a estatística e o parâmetro por observarmos só parte da população; **diminui** quando n aumenta e **só pode ser medido** em amostras **probabilísticas**. **Viés** (erro sistemático) vem de falha no plano (ex.: cadastro incompleto) e **não** diminui aumentando n.

> **Amostra aleatória** (probabilística) é aquela em que **cada elemento da população tem probabilidade conhecida e positiva de ser escolhido**, definida antes do sorteio. Em amostra **não aleatória**, o pesquisador escolhe por critério próprio e **não** se calcula erro amostral.

### 3.2 Amostragem aleatória simples (AAS)

Todos os elementos têm a **mesma chance**, e todas as amostras de tamanho n são **igualmente prováveis**: é o "sorteio de papeizinhos" (ou números aleatórios). Pode ser:

- **Com reposição:** o elemento volta à população após o sorteio (pode repetir). Há **Nⁿ** amostras ordenadas possíveis;
- **Sem reposição:** não repete. Há **C(N, n)** amostras não ordenadas possíveis.

> **Exemplo.** Da população de N = 10 militares, sorteiam-se n = 3 **sem reposição**. Número de amostras possíveis: C(10, 3) = **120**. Com reposição e considerando a ordem do sorteio: 10³ = **1.000**.

**Quando usar:** população **homogênea** e **cadastro completo**.

### 3.3 Amostragem sistemática

Ordena-se a população, calcula-se o **intervalo de amostragem k = N ÷ n**, sorteia-se um **ponto de partida** entre 1 e k e, a partir dele, tomam-se os elementos de **k em k**.

> **Exemplo.** N = 1.000, n = 50 → k = 1.000 ÷ 50 = **20**. Se o ponto de partida sorteado for 7, a amostra será 7, 27, 47, 67, …, 987 (50 elementos).

- **Vantagem:** simples e rápida; espalha bem a amostra pela lista.
- **Risco:** se a lista tiver **periodicidade** coincidente com k (ex.: sorteio a cada 7 dias, sempre dia de plantão), a amostra fica **enviesada**.
- Só é considerada aleatória se o **ponto de partida** for sorteado.

### 3.4 Amostragem estratificada

Divide-se a população em **estratos** (grupos **homogêneos dentro** e **diferentes entre si**, em relação à característica estudada) e **sorteia-se uma amostra em cada estrato**. A amostra final reúne os sorteios.

Há três formas de repartir n entre os estratos:

| Alocação | Quantos de cada estrato | Quando usar |
|---|---|---|
| **Uniforme** (igual) | O **mesmo n** em cada estrato | Estratos de tamanho parecido ou quando se quer comparar estratos |
| **Proporcional** | nₕ = n · Nₕ ÷ N | O mais comum: a amostra "espelha" a população |
| **Ótima (de Neyman)** | nₕ ∝ Nₕ · σₕ | Quando estratos variam muito em **variabilidade**: sorteia-se mais nos mais heterogêneos |

> **Exemplo (proporcional).** Efetivo de N = 1.000, sendo 600 praças e 400 oficiais; amostra n = 100. Praças: 100 × 600/1.000 = **60**. Oficiais: 100 × 400/1.000 = **40**.
>
> **Exemplo (Neyman).** Dois estratos de 500 elementos cada, com desvios-padrão σ₁ = 10 e σ₂ = 30; n = 200. Proporção do primeiro: (500 × 10) ÷ (500 × 10 + 500 × 30) = 5.000 ÷ 20.000 = 25%. Logo n₁ = **50** e n₂ = **150**.

**Vantagem:** garante **representação de todos os grupos** e costuma **reduzir o erro** (ganha precisão) quando os estratos são bem escolhidos.

### 3.5 Amostragem por conglomerados (clusters)

A população é dividida em **conglomerados** (grupos naturais, como quarteirões, escolas, quartéis, municípios). Sorteiam-se **conglomerados inteiros** e, nos sorteados, observam-se **todos** os elementos (**um estágio**) ou **uma subamostra** deles (**dois estágios**).

> **Exemplo.** Para pesquisar a satisfação dos moradores de uma cidade, sorteiam-se 8 quarteirões e entrevistam-se **todos** os moradores deles. Isto é **conglomerados em um estágio**. Se, nos 8 quarteirões, se sorteasse uma parte dos moradores, seriam dois estágios.

**Vantagem:** barato e prático quando não há lista completa de indivíduos. **Desvantagem:** costuma ser **menos preciso** que a AAS de mesmo tamanho.

### 3.6 A confusão mais cobrada: estratos × conglomerados

| | **Estratos** | **Conglomerados** |
|---|---|---|
| Como são os grupos | **Homogêneos por dentro**, **diferentes entre si** | **Heterogêneos por dentro** (cada um é um "mini-retrato" da população), **parecidos entre si** |
| O que se sorteia | **Elementos dentro de todos** os estratos | **Alguns conglomerados** (e, neles, todos ou parte dos elementos) |
| Objetivo | **Precisão** e representação dos grupos | **Economia** e praticidade |

> **Macete:** *estrato* = "**TODOS** os grupos participam, sorteio **dentro** deles". *Conglomerado* = "**ALGUNS** grupos são sorteados, e dentro deles toma-se **tudo**".

### 3.7 Amostragem não probabilística (não aleatória)

Nestas técnicas a escolha **não** é sorteada, então **não é possível** calcular o erro amostral nem generalizar com segurança:

- **Por conveniência:** os elementos mais fáceis de alcançar (ex.: quem passa na frente do quartel).
- **Intencional (por julgamento):** o pesquisador escolhe quem considera mais representativo.
- **Por cotas:** reserva-se número de entrevistados por perfil (sexo, idade), mas a escolha dentro da cota é do entrevistador. Parece estratificada, mas **não sorteia**.
- **Bola de neve:** um participante indica o seguinte (útil em populações de difícil acesso).
- **Voluntária (autosseleção):** responde quem quer (ex.: enquete de internet). Gera **viés** de autosseleção.

### 3.8 Bônus: quantas pessoas pesquisar?

Para estimar uma **proporção** com confiança de 95% (z = 1,96) e erro máximo E, no pior caso (p = 0,5):

**n₀ = z² · p · (1 − p) ÷ E²**

> **Exemplo.** E = 5 pontos percentuais (0,05): n₀ = 1,96² × 0,5 × 0,5 ÷ 0,05² = 0,9604 ÷ 0,0025 = 384,16 → **385 pessoas** (arredonda-se **sempre para cima**).
> Se a população for pequena (N = 2.000), corrige-se: n = n₀ ÷ (1 + (n₀ − 1) ÷ N) = 384,16 ÷ (1 + 383,16 ÷ 2.000) ≈ 322,4 → **323**.

Para estimar uma **média**: n = (z · σ ÷ E)². Ex.: σ = 12, E = 3, z = 1,96 → n = (1,96 × 12 ÷ 3)² = 7,84² ≈ 61,5 → **62**.

### 3.9 Resumo rápido: amostragem

- **Aleatória** = chance conhecida e positiva para todos; só nela se mede o **erro amostral**.
- **AAS:** sorteio simples (com ou sem reposição). **Sistemática:** de k em k, k = N ÷ n, partida sorteada.
- **Estratificada:** sorteia **em todos** os estratos (homogêneos por dentro): proporcional, uniforme ou ótima.
- **Conglomerados:** sorteia **alguns** grupos (heterogêneos por dentro) e observa tudo ou parte deles.
- **Não probabilística:** conveniência, intencional, cotas, bola de neve, voluntária. **Sem** erro amostral calculável.
- **Aumentar n** reduz o erro amostral, mas **não corrige viés**.

## Fontes

Consulta realizada em 08/10/2026.

- IBGE, *Normas de apresentação tabular*, 3ª ed., Rio de Janeiro: Centro de Documentação e Disseminação de Informações, 1993 (sinais convencionais, elementos e regras de construção da tabela), conferidas com resumos didáticos publicados por instituições de ensino que reproduzem as normas.
- Resultados de probabilidade geométrica (encontro, vara quebrada, agulha de Buffon) conferidos por cálculo exato e por simulação de Monte Carlo (2 milhões de sorteios por caso).
- Conceitos de amostragem: tratamento didático padrão de livros de Estatística e Métodos de Amostragem (população, amostra, AAS, sistemática, estratificada com alocação proporcional e de Neyman, conglomerados, métodos não probabilísticos).
- Todos os exemplos e números foram elaborados para este material.
