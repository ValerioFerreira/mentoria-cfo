---
id: S0453
agente: CLAUDE-L4
materia: Estatística
aula: Aula 06 — Probabilidade
trecho: estatistica/a06/s02
paginas_lidas: 16-28
---
# ANALÍTICO

Este trecho apresenta a probabilidade como frequência relativa (visão empírica) e mostra como combinar eventos: união, interseção, eventos exaustivos e mutuamente excludentes, regra da união de dois eventos e de três eventos. O fio condutor é nunca contar duas vezes o que está em mais de um evento.

### Probabilidade como frequência relativa (empírica)

Quando um experimento é repetido N vezes e um evento ocorre n vezes, a **frequência relativa** do evento é **f = n ÷ N**. Ela é observada, e não deduzida: depende da amostra.

- Com poucas repetições, f pode ficar longe da probabilidade teórica; com muitas repetições, **f se aproxima da probabilidade**. Isso é a ideia da lei dos grandes números.
- A probabilidade é o valor para o qual a frequência tende quando N cresce sem limite: **P = limite de n ÷ N, com N tendendo ao infinito**.
- Essa definição serve para eventos que **não são igualmente prováveis**, nos quais a definição clássica (casos favoráveis ÷ casos possíveis) não funciona. Exemplo típico: uma moeda viciada que dá coroa em 1 a cada 4 lançamentos tem P(coroa) = 1/4.

> 💡 **Exemplo próprio:** numa linha de produção, em 500 peças inspecionadas, 20 vieram com defeito. Estimativa da probabilidade de uma peça ser defeituosa: 20 ÷ 500 = 0,04 = 4%.

> ⚠️ **Pegadinha:** frequência relativa não é igual à probabilidade, só tende a ela. Quando o enunciado fornece uma contagem observada (por exemplo, 30 itens com defeito em cada 600), a probabilidade pedida é simplesmente essa razão observada (30 ÷ 600 = 5%).

### Escolha por combinação: revisão rápida

A probabilidade clássica é P(A) = n(A) ÷ n(U), com n(U) o total de resultados possíveis. Ao sortear um grupo sem ordem, use combinação nos dois termos.

> 💡 **Exemplo:** probabilidade de uma pessoa específica entrar numa equipe de 6 sorteada entre 12. Casos favoráveis: fixar a pessoa e escolher outras 5 entre as 11 restantes, C(11,5). Casos possíveis: C(12,6). A razão é 6 ÷ 12 = 1/2 = 50%. (Atalho: cada pessoa tem a mesma chance, e 6 das 12 vagas serão ocupadas.)

### Operações com eventos

Use o **diagrama de Venn**: o retângulo é o espaço amostral U e cada evento é uma região dentro dele.

| Conceito | Símbolo | Significado | Para ocorrer |
| --- | --- | --- | --- |
| União | A ∪ B | elementos de A, de B ou de ambos | A **ou** B (ou os dois) |
| Interseção | A ∩ B | elementos comuns a A e B | A **e** B ao mesmo tempo |
| Exaustivos | A ∪ B = U | juntos cobrem todo o espaço amostral | pelo menos um deles sempre ocorre |
| Mutuamente excludentes (disjuntos) | A ∩ B = vazio | não têm elementos em comum | nunca ocorrem juntos |

> 💡 **Exemplo (dado):** A = resultados menores que 4 = {1, 2, 3}; B = resultados maiores que 3 = {4, 5, 6}. A união é {1, 2, 3, 4, 5, 6} = U, então A e B são **exaustivos**; a interseção é vazia, então são **excludentes**. Já R = {1, 2, 3, 4} e S = {4, 5, 6} têm interseção {4}: são exaustivos, mas **não** excludentes.

### Probabilidade da união de dois eventos

Somar os elementos dos dois eventos conta duas vezes a interseção, que precisa ser descontada uma vez:

n(R ∪ S) = n(R) + n(S) − n(R ∩ S)

Dividindo por n(U), chega-se à **regra da união**:

**P(R ∪ S) = P(R) + P(S) − P(R ∩ S)**

- Se R e S são **mutuamente excludentes**, P(R ∩ S) = 0 e a regra se reduz a **P(R ∪ S) = P(R) + P(S)**.
- "R **ou** S" pede a união; "R **e** S" pede a interseção. Palavras como "pelo menos um" e "ao menos" também indicam união.

> 💡 **Exemplo (dado, com R = {1, 2, 3, 4} e S = {4, 5, 6}):** P(R) = 4/6, P(S) = 3/6, P(R ∩ S) = 1/6. P(R ∪ S) = 4/6 + 3/6 − 1/6 = 6/6 = 1.

> 💡 **Exemplo próprio (achar a interseção):** P(R) = 50%, P(S) = 35% e P(R ou S) = 60%. Da regra, 60% = 50% + 35% − P(R e S), logo P(R e S) = 85% − 60% = 25%.

> 💡 **Exemplo próprio (população):** numa sala há 40 homens e 60 mulheres; 30% dos homens e 50% das mulheres são fumantes. Probabilidade de sortear uma mulher ou um fumante: P(M) = 60/100, fumantes = 12 + 30 = 42, logo P(F) = 42/100, mulheres fumantes = 30, P(M ∩ F) = 30/100. P(M ∪ F) = 60/100 + 42/100 − 30/100 = 72/100 = 72%.

### União de três eventos

Para três eventos R, S e T, as somas simples contam as interseções duas a duas em duplicidade e a interseção tripla além do devido. A correção (**inclusão e exclusão**) é:

**P(R ∪ S ∪ T) = P(R) + P(S) + P(T) − P(R ∩ S) − P(R ∩ T) − P(S ∩ T) + P(R ∩ S ∩ T)**

Em palavras: somam-se os três eventos, subtraem-se as três interseções duas a duas e **soma-se de volta** a interseção dos três (ela foi retirada demais ao descontar os pares). O mesmo vale com contagens, trocando P por n.

#### Método do diagrama de Venn (alternativa à fórmula)

Preencha as regiões **de dentro para fora**:

1. Comece pela região central (interseção dos três).
2. Cada região "só de dois" = interseção dos dois menos a interseção tripla.
3. Cada região "só de um" = o evento menos as regiões "só de dois" que o tocam e menos a central.
4. A união é a soma de todas as regiões; o que sobra do total é "nenhum dos eventos".

> 💡 **Exemplo próprio:** numa pesquisa com 100 pessoas, 45 leem o jornal R, 40 leem S e 30 leem T; 15 leem R e S, 10 leem R e T, 12 leem S e T, e 5 leem os três. União pela fórmula: 45 + 40 + 30 − 15 − 10 − 12 + 5 = 83. Pelo diagrama: região central 5; só R e S = 10; só R e T = 5; só S e T = 7; só R = 45 − 10 − 5 − 5 = 25; só S = 40 − 10 − 7 − 5 = 18; só T = 30 − 5 − 7 − 5 = 13; soma = 83. Portanto, 17 pessoas não leem nenhum.

#### Usos típicos

- **Achar uma probabilidade desconhecida:** se a união é conhecida (por exemplo, 1, quando todos consomem ao menos uma opção), isole o termo que falta na fórmula. Exemplo: se P(R ∪ S ∪ T) = 100% e a soma "P(R) + P(S) + P(T) − pares" dá 97%, então P(R ∩ S ∩ T) = 100% − 97% = 3%.
- **Consumir "uma e somente uma":** monte o Venn e some só as regiões "só de um".
- **Total conhecido, interseção tripla desconhecida:** use a fórmula para achá-la e depois preencha o diagrama.

### Para fixar
- Frequência relativa f = n ÷ N; com muitas repetições, ela se aproxima da probabilidade, que é o limite de n ÷ N.
- A definição empírica vale também para eventos não equiprováveis (moeda viciada, peças com defeito).
- União = "ou" (inclui "ambos"); interseção = "e"; exaustivos: união igual a U; excludentes: interseção vazia.
- P(R ∪ S) = P(R) + P(S) − P(R ∩ S); se excludentes, soma-se apenas P(R) + P(S).
- Eventos excludentes têm P(R ∩ S) = 0.
- Para três eventos: soma dos três − interseções dois a dois + interseção tripla.
- No diagrama de Venn, preencha do centro (interseção tripla) para fora, subtraindo o que já foi contado.
- "Uma e somente uma" soma apenas as regiões exclusivas de cada evento.

# SINTÉTICO

- **Frequência relativa**: f = n ÷ N é o que se observa; quanto maior N, mais próxima da probabilidade, que é o limite de n ÷ N.
- **Definição empírica**: serve quando os resultados não são equiprováveis (moeda viciada, taxa de defeitos), onde a definição clássica não se aplica.
- **União e interseção**: união é "ou" (um, outro ou ambos); interseção é "e" (os dois ao mesmo tempo).
- **Exaustivos × excludentes**: exaustivos cobrem todo o espaço amostral (união igual a U); excludentes não têm elementos em comum (interseção vazia).
- **Regra da união**: P(R ∪ S) = P(R) + P(S) − P(R ∩ S), descontando uma vez a interseção que foi somada duas vezes.
- **Caso excludente**: com interseção vazia, P(R ∪ S) = P(R) + P(S).
- **Três eventos**: soma os três, tira as interseções dois a dois e soma de volta a tripla.
- **Venn por regiões**: preencha do centro para fora; "só de dois" = par menos tripla; "só de um" = evento menos todas as interseções.
- **Incógnita na união**: se todos pertencem a pelo menos um evento (união igual a 1), isole a interseção tripla na fórmula.

# NOTAS

- Página 24 do material: a probabilidade da interseção é escrita como "P(M ∪ S) = n(M ∩ S) ÷ n(U)"; o correto é P(M ∩ S). Usei a forma correta.
- Página 27: as três diferenças "x", "y" e "z" aparecem todas rotuladas como "x =" (erro de digitação); os valores numéricos estão corretos e o resumo usa o método, não as letras.
- Página 28: a questão sobre sabonetes termina sem a resolução completa (o texto acaba no enunciado do diagrama); usei apenas o passo inicial de achar a interseção tripla pela fórmula da união.
- Figuras (diagramas de Venn) não foram extraídas; descrevi o método em texto.
- A menção à lei dos grandes números é a denominação usual do fenômeno descrito no trecho (frequência tendendo à probabilidade).
