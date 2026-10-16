---
id: fis-optica-geometrica
subject: fisica
title: Óptica geométrica
short: Óptica geométrica
subtitle: Feixes e frentes de onda, reflexão, espelhos, refração, lentes, formação de imagens e instrumentos ópticos (item 6 do edital de Física)
weight: 0.12
order: 1
resolves: fis-optica
---

## O que este material cobre e como estudar

Pessoal, o edital de Física pede o bloco de **óptica geométrica** inteiro: feixes e frentes de onda, reflexão e refração da luz, espelhos, lentes, formação de imagens, índice de refração e leis da refração e instrumentos ópticos simples. O curso principal só trata de reflexão e refração **do som**, então este complemento fecha a lacuna.

A ordem é a mesma de uma boa aula de óptica:

1. Princípios da óptica, feixes de luz, frentes de onda, sombra e penumbra, câmara escura;
2. Reflexão da luz e espelhos planos;
3. Espelhos esféricos (côncavo e convexo);
4. Refração da luz: índice de refração, lei de Snell, ângulo limite e reflexão total, dioptro plano, lâminas e prismas;
5. Lentes esféricas delgadas;
6. Instrumentos ópticos e o olho humano.

> **Como a AOCP cobra óptica:** a maior parte das questões é **conceitual** ("a imagem é real ou virtual? direita ou invertida? maior ou menor?") ou pede **uma conta curta** com a equação de Gauss, a lei de Snell ou o ângulo limite. Quase nunca exige construção geométrica elaborada. Domine as **tabelas de imagem** e a **convenção de sinais**, que valem mais que qualquer macete.

### Convenção de sinais (a de Gauss), que vamos usar o tempo todo

| Grandeza | Símbolo | Positivo (+) | Negativo (−) |
|---|---|---|---|
| Posição do objeto | p | objeto **real** (o normal) | objeto virtual (raros casos) |
| Posição da imagem | p' | imagem **real** (do lado de onde a luz sai) | imagem **virtual** |
| Distância focal | f | espelho **côncavo**; lente **convergente** | espelho **convexo**; lente **divergente** |
| Altura do objeto | o | acima do eixo | abaixo do eixo |
| Altura da imagem | i | imagem **direita** (mesmo sentido do objeto) | imagem **invertida** |

Equações que valem para espelhos esféricos **e** lentes delgadas:

- **Equação de Gauss:** 1/f = 1/p + 1/p'
- **Aumento linear transversal:** A = i/o = − p'/p

> **Leitura dos sinais:** p' > 0 → imagem real; p' < 0 → imagem virtual. A > 0 → imagem direita; A < 0 → imagem invertida. |A| > 1 → ampliada; |A| < 1 → reduzida.

## 1. Princípios da óptica e feixes de luz

### 1.1 Luz, fontes e meios

A **óptica geométrica** descreve a luz por **raios** (linhas orientadas que indicam a direção e o sentido de propagação) e não leva em conta sua natureza ondulatória. Ela funciona bem quando os objetos e aberturas são muito maiores que o comprimento de onda da luz (da ordem de 400 a 700 nm).

- **Fonte primária (luminosa):** emite luz própria. Ex.: Sol, lâmpada acesa, chama.
- **Fonte secundária (iluminada):** só reenvia a luz que recebe. Ex.: Lua, uma parede, este papel.
- **Fonte puntiforme (pontual):** de dimensões desprezíveis. **Fonte extensa:** de dimensões consideráveis em relação às distâncias do problema.

| Meio | Comportamento da luz | Exemplo |
|---|---|---|
| **Transparente** | passa quase toda, e dá para enxergar nitidamente através dele | ar, vidro liso, água limpa |
| **Translúcido** | passa, mas espalhada: enxerga-se luz, não a imagem nítida | vidro fosco, papel vegetal |
| **Opaco** | não deixa passar a luz (absorve ou reflete) | madeira, metal, parede |

A velocidade da luz **no vácuo** é **c ≈ 3,0 × 10⁸ m/s**, o limite máximo de velocidade do universo; em qualquer meio material ela é menor.

### 1.2 Os três princípios da óptica geométrica

1. **Propagação retilínea:** em um meio **homogêneo e transparente**, a luz se propaga em linha reta.
2. **Independência dos raios luminosos:** quando raios de luz se cruzam, cada um segue como se os outros não existissem (por isso duas lanternas cruzadas não se atrapalham).
3. **Reversibilidade dos raios:** se a luz percorre um caminho num sentido, pode percorrer o mesmo caminho no sentido oposto. Se você vê os olhos de alguém num espelho, essa pessoa também vê os seus.

### 1.3 Feixes de luz

Um **feixe** é um conjunto de raios. Classifica-se pela forma como os raios se comportam:

| Feixe | Como são os raios | Origem típica |
|---|---|---|
| **Paralelo (cilíndrico)** | mantêm distância constante entre si | fonte **muito distante** (Sol, estrelas), laser |
| **Divergente (cônico)** | se afastam uns dos outros, partindo de um ponto | fonte puntiforme próxima, lâmpada pequena |
| **Convergente** | se aproximam e se encontram em um ponto | luz que sai de uma lente convergente ou espelho côncavo |

O ponto de onde os raios divergem (ou para onde convergem) é o **foco** do feixe. Se os raios **realmente** passam por ele, o ponto é **real**; se são só os **prolongamentos** dos raios que passam por ele, o ponto é **virtual**. Essa distinção é a base de toda a discussão de imagens: **imagem real é formada por raios que de fato se cruzam; imagem virtual, pelos prolongamentos.**

### 1.4 Frentes de onda

Uma **frente de onda** é a superfície que une todos os pontos do meio que são atingidos pela onda **no mesmo instante** (pontos em fase). Ela é **perpendicular aos raios** de luz.

- Fonte **puntiforme**, meio homogêneo: frentes de onda **esféricas**, e os raios saem radialmente (feixe divergente).
- Fonte **muito distante**: frentes de onda praticamente **planas**, e os raios são paralelos (feixe paralelo).
- Feixe **convergente**: frentes esféricas "fechando" em direção ao ponto de convergência.

> **Macete:** raio é sempre **perpendicular** à frente de onda. Se o enunciado traz frentes de onda planas, os raios são paralelos; se esféricas, os raios são radiais.

### 1.5 Sombra, penumbra e câmara escura

Como a luz anda em linha reta, um objeto opaco colocado entre a fonte e um anteparo projeta **sombra**.

- **Fonte puntiforme:** só há **sombra** (região escura, sem luz).
- **Fonte extensa:** aparecem **sombra** (nenhum ponto da fonte ilumina) e **penumbra** (alguns pontos da fonte iluminam, outros não).

Por **semelhança de triângulos**, a altura da sombra de um objeto vertical iluminado por uma fonte puntiforme depende das distâncias. Para o Sol, cujos raios chegam paralelos, vale: **H/sombra de H = h/sombra de h** (a razão altura/sombra é a mesma para todos os objetos no mesmo instante).

> **Exemplo 1.** Uma vara de 1,5 m projeta sombra de 2,0 m. No mesmo instante, um prédio projeta sombra de 40 m. Qual a altura do prédio?
> Altura/sombra = 1,5/2,0 = 0,75. Prédio: 0,75 × 40 = **30 m**.

A **câmara escura de orifício** é uma caixa fechada com um furo pequeno numa face. A luz que entra forma, na face oposta, uma imagem **real, invertida** do objeto. Semelhança de triângulos dá:

- **o / i = p / p'**, em que o = altura do objeto, i = altura da imagem, p = distância do objeto ao orifício, p' = profundidade da câmara.

> **Exemplo 2.** Um objeto de 2,0 m está a 10 m do orifício de uma câmara escura de 20 cm de profundidade. Qual o tamanho da imagem?
> i = o · p'/p = 2,0 × 0,20 / 10 = **0,04 m = 4 cm** (invertida).

Se o orifício for aumentado, a imagem fica mais **brilhante**, porém menos **nítida**.

## 2. Reflexão da luz e espelho plano

### 2.1 Leis da reflexão

Reflexão é o retorno da luz ao meio de origem ao incidir numa superfície. Os ângulos são sempre medidos em relação à **normal** (reta perpendicular à superfície no ponto de incidência), e **não** em relação à superfície.

1. **1ª lei:** o raio incidente, o raio refletido e a normal estão **no mesmo plano**.
2. **2ª lei:** o ângulo de reflexão é **igual** ao ângulo de incidência (**r = i**).

Tipos de reflexão:

- **Especular (regular):** superfície lisa, raios paralelos continuam paralelos; formam-se imagens (espelhos).
- **Difusa:** superfície rugosa, raios saem em todas as direções; é por ela que enxergamos os objetos que não têm luz própria. Cada raio individual ainda obedece às leis da reflexão.

### 2.2 Espelho plano: formação de imagem

Num espelho plano, a imagem de um objeto real tem as seguintes características:

- é **virtual** (formada pelos prolongamentos dos raios, atrás do espelho);
- é **direita** e do **mesmo tamanho** do objeto (A = +1);
- é **simétrica** ao objeto em relação ao plano do espelho: **p' = − p** (mesma distância, porém do outro lado);
- é **enantiomorfa**: imagem e objeto não se sobrepõem (como a mão direita e a esquerda). Por isso a mão direita da imagem "aparece" como mão esquerda, e as letras ficam invertidas lateralmente (não de cima para baixo).

> **Pegadinha clássica:** o espelho inverte **esquerda-direita**? Na verdade ele inverte **frente-trás** (a imagem "olha" para você). A impressão de inversão lateral vem de nós girarmos para nos comparar com a imagem. Em prova, use a palavra **enantiomorfa** ou "não sobreponível".

**Consequências quantitativas** (todas decorrem de p' = − p):

- **Distância entre objeto e imagem** = 2d, sendo d a distância do objeto ao espelho.
- Se o objeto se **afasta** do espelho com velocidade v, a imagem se afasta com velocidade v em sentido oposto; a velocidade da imagem **em relação ao objeto** é **2v**.
- Se o **espelho** se desloca d (objeto parado), a imagem se desloca **2d**.
- Se o espelho **gira** um ângulo α (mantendo fixo o raio incidente), o raio refletido gira **2α**.

> **Exemplo 3.** Uma pessoa anda a 1,5 m/s em direção a um espelho plano fixo. Com que velocidade ela se aproxima da própria imagem?
> A imagem se aproxima do espelho também a 1,5 m/s, em sentido contrário. Velocidade relativa: 1,5 + 1,5 = **3,0 m/s**.

> **Exemplo 4.** Um raio incide em um espelho plano. O espelho gira 15° em torno de um eixo no ponto de incidência. De quanto gira o raio refletido?
> Gira o **dobro**: 2 × 15° = **30°**.

**Espelho mínimo para ver o corpo inteiro.** Para ver o corpo inteiro, o espelho precisa ter **metade da altura da pessoa**, e a borda inferior deve estar a **metade da altura dos olhos** em relação ao chão. A distância da pessoa ao espelho **não** altera esse tamanho mínimo.

> **Exemplo 5.** Uma pessoa de 1,80 m tem os olhos a 1,70 m do solo. Altura mínima do espelho e posição da borda inferior?
> Altura mínima: 1,80/2 = **0,90 m**. Borda inferior: 1,70/2 = **0,85 m** do chão (a borda superior fica a 1,75 m, ponto médio entre o olho e o topo da cabeça).

**Campo visual:** é a região do espaço que um observador consegue ver pelo espelho. Aproximar-se do espelho **aumenta** o campo visual; é por isso que retrovisores são vistos com mais amplitude quando o motorista chega perto.

### 2.3 Associação de dois espelhos planos

Dois espelhos planos formando um ângulo **θ** entre si, com um objeto entre eles, produzem várias imagens. Se 360°/θ é um número **inteiro**:

- **N = 360°/θ − 1** imagens.

| θ | 360°/θ | Imagens formadas |
|---|---|---|
| 120° | 3 | 2 |
| 90° | 4 | 3 |
| 72° | 5 | 4 |
| 60° | 6 | 5 |
| 45° | 8 | 7 |

Em casos extremos: espelhos **paralelos** (θ = 0°) formam **infinitas** imagens (como nos corredores de espelhos de elevadores); com θ = 180° (um espelho só), há uma imagem. A fórmula acima vale quando 360°/θ é inteiro; quando não é, a contagem depende da posição do objeto e a questão normalmente informa.

### 2.4 Espelhos planos no cotidiano

Periscópio (dois espelhos a 45°), caleidoscópio (espelhos em ângulo), retrovisores e espelhos de maquiagem (estes últimos esféricos). A reflexão em ambulâncias com a palavra "AMBULÂNCIA" escrita "ao contrário" é uma aplicação direta da enantiomorfia: o motorista à frente lê corretamente pelo retrovisor.

## 3. Espelhos esféricos

### 3.1 Elementos

Um **espelho esférico** é uma calota esférica com uma das faces refletora. Se a face refletora é a **interna**, o espelho é **côncavo**; se é a **externa**, é **convexo**.

| Elemento | O que é |
|---|---|
| **C** (centro de curvatura) | centro da esfera da qual a calota faz parte |
| **R** (raio de curvatura) | raio da esfera |
| **V** (vértice) | centro da calota, ponto do espelho que fica no eixo |
| **Eixo principal** | reta que passa por C e V |
| **F** (foco principal) | ponto onde convergem (ou de onde parecem divergir) os raios paralelos ao eixo |
| **f** (distância focal) | distância de F ao vértice |

**Relação fundamental:** o foco fica no **ponto médio** entre C e V (válido para espelhos de **pequena abertura**, condições de Gauss):

- **f = R / 2**

Em módulo; com a convenção de sinais, f > 0 no côncavo (**foco real**) e f < 0 no convexo (**foco virtual**).

> **Macete dos sinais:** côncavo = "convergente" = **f positivo**. Convexo = "divergente" = **f negativo**.

### 3.2 Raios notáveis

Para construir a imagem de um ponto, bastam dois destes quatro raios:

1. Raio que **incide paralelo ao eixo** → o refletido **passa pelo foco** (côncavo) ou tem **prolongamento passando pelo foco** (convexo).
2. Raio que **incide passando pelo foco** (ou com prolongamento por ele) → o refletido sai **paralelo ao eixo**.
3. Raio que **incide passando pelo centro C** → volta sobre si mesmo (incidência normal).
4. Raio que **incide no vértice V** → sai simétrico em relação ao eixo (r = i).

### 3.3 Espelho côncavo: imagem conforme a posição do objeto

Considere o objeto **real** sobre o eixo, a uma distância p do vértice. Lembre-se: **F = f e C = 2f**.

| Posição do objeto | Imagem | Natureza | Orientação | Tamanho |
|---|---|---|---|---|
| **p > 2f** (além de C) | entre F e C | real | invertida | menor |
| **p = 2f** (sobre C) | sobre C | real | invertida | igual |
| **f < p < 2f** (entre C e F) | além de C | real | invertida | **maior** |
| **p = f** (sobre F) | no infinito (raios saem paralelos) | **imprópria** | – | – |
| **p < f** (entre F e V) | atrás do espelho | **virtual** | **direita** | **maior** |

> **Macete:** no côncavo, a imagem é **real e invertida** para qualquer objeto **além do foco**, e **virtual, direita e maior** para objeto **entre o foco e o vértice** (o efeito "espelho de barbear" ou de maquiagem).

### 3.4 Espelho convexo: imagem única

Para qualquer posição do objeto real, a imagem é **virtual, direita e menor**, situada entre o foco e o vértice, atrás do espelho. Por isso o convexo oferece **campo visual amplo**: é usado em retrovisores externos de carros, espelhos de segurança em lojas e em esquinas de garagens. A contrapartida é a distância aparente maior (por isso o aviso "objetos no espelho estão mais próximos do que parecem").

### 3.5 Exemplos numéricos

> **Exemplo 6 (côncavo, imagem real).** Um espelho côncavo tem raio de curvatura 40 cm. Um objeto de 5 cm de altura é colocado a 30 cm do vértice. Determine posição, natureza e altura da imagem.
> f = R/2 = **+20 cm**. 1/p' = 1/f − 1/p = 1/20 − 1/30 = 1/60 → **p' = +60 cm** (imagem **real**, na frente do espelho).
> A = − p'/p = − 60/30 = **−2** → imagem **invertida e ampliada** (2×). Altura: i = A·o = −2 × 5 = **−10 cm** (10 cm, invertida).

> **Exemplo 7 (côncavo, imagem virtual).** Mesmo espelho (f = +20 cm), objeto a 10 cm do vértice.
> 1/p' = 1/20 − 1/10 = −1/20 → **p' = −20 cm** (**virtual**, 20 cm atrás do espelho). A = −(−20)/10 = **+2** → **direita e ampliada**.

> **Exemplo 8 (convexo).** Espelho convexo de distância focal 15 cm (f = −15 cm). Objeto a 30 cm do vértice.
> 1/p' = 1/f − 1/p = −1/15 − 1/30 = −3/30 → **p' = −10 cm** (virtual). A = −(−10)/30 = **+1/3** → **direita e reduzida** (um terço do tamanho).

> **Exemplo 9 (descobrir o espelho pelo aumento).** Um espelho forma uma imagem direita e 3 vezes maior que o objeto, que está a 12 cm do vértice. Que espelho é esse e qual sua distância focal?
> Imagem direita e maior só ocorre no côncavo com p < f. A = +3 = −p'/p → p' = −3p = −36 cm. 1/f = 1/p + 1/p' = 1/12 − 1/36 = 2/36 → **f = +18 cm** (côncavo, e de fato p = 12 < f = 18).

> **Exemplo 10 (relação com C).** Um objeto é colocado sobre o centro de curvatura de um espelho côncavo de raio 30 cm. Onde está a imagem?
> p = R = 30 cm; f = 15 cm. 1/p' = 1/15 − 1/30 = 1/30 → p' = 30 cm, A = −1. A imagem está **sobre o próprio C**, real, invertida e do mesmo tamanho.

> **Cuidado com a pegadinha do foco impróprio:** quando o objeto está exatamente em F, não há imagem a distância finita (os raios refletidos saem paralelos). Na equação, 1/p' = 0.

## 4. Refração da luz

### 4.1 Índice de refração

**Refração** é a passagem da luz de um meio para outro, com **mudança de velocidade**. O **índice de refração absoluto** de um meio é

- **n = c / v**

onde c é a velocidade da luz no vácuo e v a velocidade no meio. Como v ≤ c, sempre **n ≥ 1**, e n é **adimensional**. Quanto maior n, mais **refringente** é o meio e menor a velocidade da luz nele.

| Meio | n (aproximado) |
|---|---|
| Vácuo | 1,00 |
| Ar | ≈ 1,00 (1,0003) |
| Água | 1,33 |
| Vidro comum | 1,5 |
| Diamante | 2,42 |

> **Exemplo 11.** Qual a velocidade da luz num vidro de n = 1,5?
> v = c/n = 3,0 × 10⁸ / 1,5 = **2,0 × 10⁸ m/s**.

Na passagem de um meio para outro, o que muda e o que não muda:

| Grandeza | Na refração |
|---|---|
| **Frequência (f)** | **não muda** (é determinada pela fonte) |
| **Velocidade (v)** | muda (v = c/n) |
| **Comprimento de onda (λ)** | muda (λ = v/f), diminui ao entrar num meio mais refringente |
| **Direção de propagação** | muda, se a incidência for oblíqua |

O **índice de refração relativo** do meio 2 em relação ao meio 1 é n₂,₁ = n₂ / n₁ = v₁ / v₂.

### 4.2 Lei de Snell-Descartes

1. **1ª lei:** raio incidente, raio refratado e normal estão **no mesmo plano**.
2. **2ª lei (Snell):**

   **n₁ · sen θ₁ = n₂ · sen θ₂**

   onde θ₁ e θ₂ são os ângulos que os raios formam com a **normal**.

Interpretação rápida:

- Passando de meio **menos** refringente para **mais** refringente (n₂ > n₁): o raio **se aproxima da normal** (θ₂ < θ₁).
- Passando de meio **mais** para **menos** refringente (n₂ < n₁): o raio **se afasta da normal** (θ₂ > θ₁).
- **Incidência normal** (θ₁ = 0°): não há desvio, o raio continua na mesma direção (mas a velocidade e o λ mudam).

> **Macete de memória:** "mais lento, mais perto da normal". Onde a luz anda mais devagar (n maior), o raio fica mais próximo da normal.

> **Exemplo 12.** Um raio de luz incide do ar (n = 1,0) em vidro (n = 1,5) com ângulo de 60° em relação à normal. Qual o ângulo de refração?
> sen θ₂ = (1,0 × sen 60°)/1,5 = 0,866/1,5 = 0,577 → θ₂ ≈ **35,3°** (menor que 60°, aproximou-se da normal, como previsto).

A refração é sempre acompanhada de uma **reflexão parcial**: parte da luz volta ao meio de origem.

### 4.3 Ângulo limite e reflexão total

Quando a luz vai de um meio **mais refringente** para um **menos refringente** (n₁ > n₂), o raio se afasta da normal. Aumentando θ₁, chega-se a um valor em que θ₂ = 90° (o raio refratado "rasa" a superfície). Esse valor de θ₁ é o **ângulo limite L**:

- **sen L = n_menor / n_maior**   (por exemplo, sen L = n_ar / n_meio)

Para incidência com ângulo **maior que L**, não há raio refratado: toda a luz é refletida. É a **reflexão total** (interna).

**Condições para a reflexão total (as duas ao mesmo tempo):**
1. a luz deve **ir do meio mais refringente para o menos refringente**;
2. o ângulo de incidência deve ser **maior que o ângulo limite** (θ₁ > L).

> **Pegadinha:** não existe reflexão total quando a luz passa do ar para a água ou para o vidro; só no sentido contrário. E em θ₁ = L exatamente, o raio refratado é rasante, e ainda não se fala em reflexão total.

| Interface | Ângulo limite |
|---|---|
| Vidro (1,5) → ar | sen L = 1/1,5 → **L ≈ 41,8°** |
| Água (1,33) → ar | sen L = 1/1,33 → **L ≈ 48,8°** |
| Diamante (2,42) → ar | sen L = 1/2,42 → **L ≈ 24,4°** |

O diamante tem ângulo limite muito pequeno: grande parte da luz que entra sofre reflexão total várias vezes dentro da pedra, e é isso que lhe dá brilho.

**Aplicações da reflexão total:**
- **Fibra óptica:** o núcleo (n maior) é envolto pela casca (n menor); a luz "viaja" por reflexões totais sucessivas, quase sem perda. Usada em telecomunicações e endoscopia. Exemplo: núcleo n = 1,5 e casca n = 1,4 → sen L = 1,4/1,5 → L ≈ 69°. Só ficam guiados os raios que incidem na interface com ângulo maior que 69°.
- **Prismas de reflexão total** (binóculos, periscópios): prisma de vidro com ângulos de 45°-45°-90°; como L ≈ 41,8° < 45°, a luz que incide a 45° na hipotenusa sofre reflexão total.
- **Miragem:** o ar quente próximo ao asfalto tem n menor, e raios que vêm do céu sofrem refração progressiva e reflexão total, dando a ilusão de "poça d'água".
- **Brilho de bolhas, gotas e do "espelho" que se vê ao olhar para cima, debaixo d'água.**

### 4.4 Dioptro plano

**Dioptro plano** é um sistema formado por dois meios transparentes separados por uma superfície plana (por exemplo, a superfície da água). Para o observador que olha **quase perpendicularmente**, vale (condições de Gauss):

- **p' / p = n_observador / n_objeto**

onde p = distância real do objeto à superfície, p' = distância aparente da imagem à superfície, n_observador = índice do meio onde está o observador e n_objeto = índice do meio onde está o objeto.

> **Exemplo 13.** Um peixe está a 40 cm de profundidade, visto por um observador no ar, olhando quase na vertical. (n_água = 4/3.) A que profundidade o observador o vê?
> p' = p · n_obs/n_obj = 40 × (1)/(4/3) = **30 cm**. O peixe parece **mais perto da superfície** do que realmente está. (Por isso piscinas parecem mais rasas do que são.)

Regra geral: quem olha de um meio **menos refringente** para um objeto num meio **mais refringente** vê o objeto **mais próximo** da superfície (p' < p). Inverta e tem o oposto: o peixe, olhando para um pássaro no ar, vê o pássaro mais **longe** que ele realmente está.

### 4.5 Lâmina de faces paralelas

Uma lâmina de vidro (espessura **e**, índice n, no ar) desloca lateralmente o raio, mas **não altera sua direção**: o raio emergente é **paralelo** ao incidente. O desvio lateral é

- **d = e · sen(i − r) / cos r**

onde i é o ângulo de incidência e r o de refração na primeira face.

> **Exemplo 14.** Uma lâmina de vidro (n = 1,5) tem 6,0 cm de espessura. Um raio incide a 60°. Qual o deslocamento lateral?
> sen r = sen 60°/1,5 → r = 35,26°. d = 6,0 × sen(60° − 35,26°)/cos 35,26° = 6,0 × 0,4184/0,8165 ≈ **3,1 cm**.

Para incidência normal (i = 0), d = 0. O deslocamento cresce com a espessura e com o ângulo de incidência.

### 4.6 Prisma óptico

O **prisma** é um meio transparente limitado por duas faces planas que formam um ângulo **A** (ângulo de abertura). A luz sofre duas refrações e **o raio se desvia em direção à base** do prisma (se n_prisma > n_meio).

- **Desvio total:** **δ = i + i' − A**, sendo i o ângulo de incidência na 1ª face e i' o de emergência na 2ª.
- O desvio é **mínimo** (δ_min) quando o raio atravessa o prisma **simetricamente** (i = i'). Nesse caso: **n = sen[(A + δ_min)/2] / sen(A/2)**.
- **Prisma de pequeno ângulo A** (≲ 10°) com incidência quase normal: **δ ≈ (n − 1)·A**.

> **Exemplo 15.** Prisma de vidro (n = 1,5) com A = 60° no ar, em desvio mínimo. Qual o desvio mínimo?
> sen[(60° + δ)/2] = 1,5 × sen 30° = 0,75 → (60° + δ)/2 = 48,59° → δ_min = 97,18° − 60° = **≈ 37,2°**.

> **Exemplo 16.** Um prisma de pequeno ângulo A = 8° e n = 1,5. Desvio: δ ≈ (1,5 − 1) × 8° = **4°**.

**Dispersão da luz branca.** O índice de refração depende da cor (do comprimento de onda): é **maior para o violeta** e **menor para o vermelho**. Por isso, ao atravessar um prisma, a luz branca se decompõe nas cores do arco-íris, e o **violeta é o mais desviado, o vermelho o menos desviado**. O arco-íris resulta de refração, reflexão interna e dispersão nas gotas de chuva.

> **Macete:** no vácuo todas as cores têm a mesma velocidade c; **num meio material, o violeta é o mais lento** (maior n) e o vermelho o mais rápido. A frequência não muda na refração; o que muda com a cor é a frequência de origem.

## 5. Lentes esféricas delgadas

### 5.1 Tipos e comportamento

**Lente** é um meio transparente limitado por duas superfícies, ao menos uma esférica. Seis formatos básicos: de **bordas finas** (biconvexa, plano-convexa, côncavo-convexa ou menisco convergente) e de **bordas grossas** (bicôncava, plano-côncava, convexo-côncava ou menisco divergente).

O comportamento depende da **comparação entre o índice da lente (n_L) e o do meio (n_m)**:

| Situação | Bordas finas | Bordas grossas |
|---|---|---|
| n_L > n_m (ex.: vidro no ar) | **convergente** | **divergente** |
| n_L < n_m (ex.: bolha de ar na água) | divergente | convergente |

> **Pegadinha preferida das bancas:** "lente de bordas finas é convergente" só vale se a lente for **mais refringente** que o meio. Uma bolha de ar (lente biconvexa de ar) dentro da água é **divergente**.

- **Lente convergente:** raios paralelos ao eixo convergem para o **foco imagem F'** (**real**, f > 0).
- **Lente divergente:** raios paralelos ao eixo divergem, como se partissem do foco virtual (f < 0).

Uma lente tem **dois focos** simétricos (objeto e imagem), um de cada lado, cada um a uma distância |f| do centro óptico O. Para a lente **delgada**, trabalha-se com o centro óptico O como referência.

### 5.2 Raios notáveis

1. Raio **paralelo ao eixo** → refratado passa pelo **foco imagem** F' (convergente) ou tem **prolongamento passando por F'** (divergente).
2. Raio que passa pelo **foco objeto** F (ou com prolongamento por F) → refratado sai **paralelo ao eixo**.
3. Raio que passa pelo **centro óptico O** → **não sofre desvio**.

Os mesmos três raios servem para qualquer lente delgada.

### 5.3 Lente convergente: imagens

Fazendo A = 2f o ponto "anti-principal" (2 vezes a distância focal):

| Posição do objeto | Imagem | Natureza | Orientação | Tamanho |
|---|---|---|---|---|
| **p > 2f** | entre f e 2f | real | invertida | menor |
| **p = 2f** | em 2f, do outro lado | real | invertida | igual |
| **f < p < 2f** | além de 2f | real | invertida | **maior** |
| **p = f** | no infinito | imprópria | – | – |
| **p < f** | mesmo lado do objeto | **virtual** | **direita** | **maior** |

> **Macete:** a lente convergente se comporta como o espelho côncavo (as regras de "real invertida" e "virtual direita ampliada" são as mesmas). A diferença é de lado: **imagem real fica do lado oposto ao objeto** na lente, e do **mesmo lado** no espelho.

Aplicações: lupa (objeto entre F e O), projetor (objeto entre F e 2F), câmera fotográfica e olho (objeto além de 2F).

### 5.4 Lente divergente: imagem única

Para qualquer objeto real, a imagem é **virtual, direita e menor**, do mesmo lado do objeto, entre o foco e o centro óptico. É a lente usada para corrigir a **miopia** e nos "olhos mágicos" de portas.

### 5.5 Exemplos numéricos

> **Exemplo 17 (convergente, imagem real).** Lente convergente de f = 10 cm. Objeto de 4 cm a 30 cm da lente.
> 1/p' = 1/10 − 1/30 = 2/30 → **p' = +15 cm** (real, do outro lado). A = −15/30 = **−0,5** → invertida e reduzida; i = −2 cm.

> **Exemplo 18 (convergente como lupa).** Mesma lente, objeto a 5 cm.
> 1/p' = 1/10 − 1/5 = −1/10 → **p' = −10 cm** (virtual, do mesmo lado do objeto). A = −(−10)/5 = **+2** → direita e ampliada 2×.

> **Exemplo 19 (divergente).** Lente divergente de f = −20 cm. Objeto a 20 cm.
> 1/p' = −1/20 − 1/20 = −1/10 → **p' = −10 cm** (virtual). A = 10/20 = **+0,5** → direita e reduzida.

> **Exemplo 20 (imagem real do mesmo tamanho).** Como obter, com uma lente convergente de f = 12 cm, uma imagem real do mesmo tamanho do objeto? Coloque o objeto em p = 2f = **24 cm**; a imagem surge a p' = 24 cm, com A = −1.

### 5.6 Vergência (convergência) de uma lente

A **vergência** (ou "grau" da lente) é o inverso da distância focal **em metros**:

- **V = 1 / f**   (unidade: **dioptria, di**, 1 di = 1 m⁻¹)

Lente convergente: V > 0; divergente: V < 0. Para lentes **justapostas** (coladas), as vergências **somam**: V = V₁ + V₂ (e portanto 1/f = 1/f₁ + 1/f₂).

> **Exemplo 21.** Lente convergente de f = 25 cm: V = 1/0,25 = **+4 di**. Lente divergente de f = −50 cm: V = **−2 di**. Justapondo as duas: V = +4 − 2 = **+2 di** (convergente, f = 50 cm).

> **Macete dos óculos:** "grau" é a vergência em dioptrias. Um "−2,0" é lente divergente com f = −50 cm. Oftalmologistas falam em "graus" para dioptrias.

### 5.7 Equação dos fabricantes de lentes (Halley)

Para uma lente delgada de índice n_L imersa em meio de índice n_m:

- **1/f = (n_L / n_m − 1) · (1/R₁ + 1/R₂)**

Convenção para os raios das faces: **R > 0** para face **convexa**, **R < 0** para face **côncava**, e **1/R = 0** para face **plana** (R → ∞). Resultado com f > 0 é lente convergente; f < 0, divergente.

> **Exemplo 22.** Lente biconvexa de vidro (n = 1,5) com R₁ = R₂ = 20 cm, no ar.
> 1/f = (1,5 − 1)(1/20 + 1/20) = 0,5 × 0,1 = 0,05 → **f = 20 cm** (convergente).

> **Exemplo 23 (mesma lente imersa em água).** n_m = 1,33: n_L/n_m = 1,128; 1/f = 0,128 × 0,1 = 0,0128 → **f ≈ 78 cm**. A lente fica **muito menos convergente** quando mergulhada na água (por isso não enxergamos bem debaixo d'água sem máscara: o olho, imerso, perde grande parte do poder de convergência da córnea).

> **Exemplo 24 (menisco).** Menisco de vidro (n = 1,5) com face convexa R₁ = 10 cm e face côncava R₂ = −20 cm, no ar.
> 1/f = 0,5 × (1/10 − 1/20) = 0,5 × 0,05 = 0,025 → f = **+40 cm**: menisco convergente (bordas finas).

> **Exemplo 25 (plano-convexa).** R₁ = 15 cm, face plana, n = 1,5: 1/f = 0,5 × 1/15 → **f = 30 cm**.

### 5.8 Resumo para a prova (espelhos × lentes)

| | Espelho côncavo | Espelho convexo | Lente convergente | Lente divergente |
|---|---|---|---|---|
| Sinal de f | + | − | + | − |
| Foco | real | virtual | real | virtual |
| Imagem de objeto real | real/invertida ou virtual/direita | sempre virtual, direita, menor | real/invertida ou virtual/direita | sempre virtual, direita, menor |
| Lado da imagem real | mesmo lado do objeto | – | lado oposto ao objeto | – |
| Uso típico | maquiagem, faróis, telescópios | retrovisor, segurança | lupa, câmera, projetor, hipermetropia | miopia, olho mágico |

## 6. Instrumentos ópticos simples e o olho humano

### 6.1 Câmera escura e câmara fotográfica

A **câmara fotográfica** moderna substitui o orifício por uma **lente convergente** e o anteparo por filme ou **sensor**. A imagem formada é **real, invertida e menor** (objeto além de 2f), e a nitidez é ajustada **variando a distância lente-sensor** (foco). O **diafragma** controla a quantidade de luz que entra; o **obturador**, o tempo de exposição.

### 6.2 Lupa (microscópio simples)

A **lupa** é uma lente convergente usada com o objeto entre o **foco e o centro óptico** (p < f): a imagem é **virtual, direita e ampliada**.

Para especificar a ampliação, usa-se a **distância mínima de visão distinta**, D ≈ **25 cm** (ponto próximo do olho normal).

- **Imagem formada no infinito** (olho relaxado): **A = D / f**.
- **Imagem formada no ponto próximo** (25 cm da lente): **A = 1 + D / f** (ampliação máxima).

> **Exemplo 26.** Lupa de f = 5 cm. Com a imagem no ponto próximo, A = 1 + 25/5 = **6**; com a imagem no infinito, A = 25/5 = **5**.
> Verificação para A = 6: p' = −25 cm; 1/5 = 1/p − 1/25 → p = 25/6 ≈ 4,17 cm; A = 25/4,17 = 6.

Quanto **menor** a distância focal, **maior** o aumento.

### 6.3 Microscópio composto

Formado por duas lentes convergentes: a **objetiva** (de pequena distância focal, perto do objeto) e a **ocular** (que funciona como lupa). O objeto fica um pouco além do foco da objetiva, que dá uma **imagem real, invertida e ampliada**; essa imagem fica **entre a ocular e seu foco**, e a ocular fornece a **imagem final virtual, ampliada** (invertida em relação ao objeto).

- **Ampliação total: A = A_objetiva × A_ocular** (em módulo).

> **Exemplo 27.** Objetiva com f = 1,0 cm e objeto a 1,1 cm: 1/p' = 1/1 − 1/1,1 = 0,0909 → p' = 11 cm, |A_obj| = 11/1,1 = **10**. Ocular de f = 5 cm com imagem final no infinito: A_oc = 25/5 = **5**. Total: 10 × 5 = **50×**.

### 6.4 Luneta e telescópio

Instrumentos para observar objetos **distantes**, que parecem pequenos pelo pequeno ângulo de visão. A **luneta astronômica** (refratora) tem objetiva e ocular convergentes.

- A objetiva (grande distância focal f_ob) forma uma **imagem real, invertida e reduzida** do objeto distante no seu foco.
- Esta imagem fica no foco da ocular (f_oc), que a amplia (imagem final virtual no infinito).
- **Aumento angular: G = f_ob / f_oc.**
- **Comprimento da luneta** (imagem final no infinito): **L = f_ob + f_oc.**

> **Exemplo 28.** f_ob = 100 cm e f_oc = 5 cm: G = 100/5 = **20×**; L = 105 cm.

Tipos: **luneta terrestre** (com lentes que endireitam a imagem), **luneta de Galileu** (ocular divergente, imagem direita) e **telescópio refletor** (de Newton), em que a objetiva é um **espelho côncavo**, o que evita defeitos das lentes e permite grandes diâmetros. O poder de captar luz depende do diâmetro da objetiva.

### 6.5 Projetor

Uma lente convergente com o objeto (slide, filme) **entre F e 2F** produz imagem **real, invertida e ampliada** sobre a tela; por isso o slide é colocado de cabeça para baixo.

### 6.6 O olho humano

| Estrutura | Função |
|---|---|
| **Córnea** | superfície externa transparente; é onde ocorre a **maior parte** da convergência do olho |
| **Pupila / íris** | a pupila é a abertura; a íris (colorida) regula seu diâmetro, controlando a luz que entra |
| **Cristalino** | lente convergente **de foco variável**; muda de curvatura (acomodação) para focalizar |
| **Retina** | tela onde se forma a imagem **real, invertida e menor**; tem **cones** (visão em cores, luz intensa) e **bastonetes** (luz fraca, sem cores) |
| **Nervo óptico** | leva a informação ao cérebro, que "desinverte" a imagem |

O olho normal (emétrope) forma na retina a imagem de objetos distantes com o músculo ciliar **relaxado** (cristalino menos curvo). Para objetos próximos, o músculo ciliar **contrai** e o cristalino fica mais curvo (mais convergente): é a **acomodação visual**.

- **Ponto remoto:** maior distância de visão nítida. No olho normal, o **infinito**.
- **Ponto próximo:** menor distância de visão nítida. No olho normal, **≈ 25 cm**.

### 6.7 Defeitos da visão e correção

| Defeito | O que ocorre | Imagem se forma... | Correção |
|---|---|---|---|
| **Miopia** | globo ocular "longo" ou cristalino convergente demais; ponto remoto **finito** | **antes** da retina | lente **divergente** |
| **Hipermetropia** | globo "curto" ou cristalino fraco; ponto próximo **distante** | **depois** da retina | lente **convergente** |
| **Presbiopia** ("vista cansada") | cristalino perde elasticidade com a idade; ponto próximo se afasta | – | lente **convergente** (para perto); lentes bifocais |
| **Astigmatismo** | córnea com curvatura irregular (não esférica) | foco diferente em eixos diferentes | lente **cilíndrica** |

**Cálculo da correção da miopia.** A lente deve fornecer, para objetos no infinito, uma imagem **virtual no ponto remoto** do míope. Assim p = ∞, p' = −(ponto remoto), e f = −d_PR.

> **Exemplo 29.** Um míope só enxerga com nitidez até 50 cm. Que lente corrige? (lente colada ao olho)
> 1/f = 1/∞ + 1/(−0,50) → f = **−0,50 m**, V = **−2,0 di** (divergente).

**Cálculo da correção da hipermetropia.** A lente deve dar, para um objeto à distância de leitura (25 cm), uma imagem virtual no **ponto próximo** do hipermétrope.

> **Exemplo 30.** O ponto próximo de um hipermétrope é 50 cm. Que lente permite ler a 25 cm?
> p = 25 cm, p' = −50 cm: 1/f = 1/25 − 1/50 = 1/50 → f = **+50 cm**, V = **+2,0 di** (convergente).

> **Macete:** míope **não vê de longe**, usa lente **divergente (grau negativo)**. Hipermetrope e presbíope **não veem de perto**, usam **convergente (grau positivo)**. A lente corretora forma, no ponto que o olho consegue ver, uma **imagem virtual** do objeto que ele quer ver.

### 6.8 Comparando câmera e olho

| Câmera | Olho |
|---|---|
| lente (objetiva) | córnea + cristalino |
| diafragma | íris / pupila |
| sensor ou filme | retina |
| foco: mover a lente | foco: variar a curvatura do cristalino |
| imagem real, invertida, menor | imagem real, invertida, menor |

## 7. Pegadinhas e revisão relâmpago

1. **Ângulo de incidência e reflexão** sempre se medem em relação à **normal**, nunca à superfície.
2. Espelho plano: imagem **virtual, direita, igual e enantiomorfa**; distância do objeto ao espelho = distância da imagem ao espelho.
3. Rotação do espelho de α → raio refletido gira **2α**. Imagens em dois espelhos planos: **360°/θ − 1**.
4. **f = R/2**; côncavo f > 0, convexo f < 0. Convexo: imagem **sempre** virtual, direita e menor.
5. Côncavo: objeto **além de F** → imagem real e invertida; **entre F e V** → virtual, direita, maior.
6. **Equação de Gauss:** 1/f = 1/p + 1/p'; **A = −p'/p**. Substitua os sinais **com cuidado**: erro de sinal é a causa nº 1 de erros em prova.
7. Na refração: **frequência constante**; mudam v e λ. n = c/v ≥ 1.
8. **Snell:** n₁ sen θ₁ = n₂ sen θ₂. Meio mais refringente → raio mais próximo da normal.
9. **Reflexão total:** só do meio **mais** para o **menos** refringente **e** com θ > L; **sen L = n_menor/n_maior**.
10. **Dioptro plano:** p'/p = n_obs/n_obj; peixe visto de cima parece mais raso.
11. Lente de **bordas finas** é convergente **se n_lente > n_meio**; invertendo, é divergente.
12. **Vergência V = 1/f** em dioptrias (f em metros); justapostas somam. Miopia → V < 0; hipermetropia → V > 0.
13. Lupa: **A = 1 + 25/f** (imagem a 25 cm). Luneta: **G = f_ob/f_oc**. Microscópio: **A = A_ob · A_oc**.
14. Imagem **real** = raios que se cruzam de fato (pode ser projetada na tela); **virtual** = prolongamentos (não projetável).

## Fontes

Conteúdo didático padrão de Física do ensino médio e vestibular (óptica geométrica), elaborado pelo MentorIA com texto, tabelas e exemplos próprios. As convenções de sinais seguem a de Gauss, usada nos livros-texto de ensino médio. Índices de refração e demais constantes são valores usuais de tabela. Todos os exemplos numéricos foram conferidos por cálculo (Python) em 08/10/2026.
