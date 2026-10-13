---
id: S0317
agente: CLAUDE-L4
materia: Estatística
aula: Aula 03 — Moda
trecho: estatistica/a03/s02
paginas_lidas: 13-27
---
# ANALÍTICO

Quando os dados vêm agrupados em classes, a moda não aparece diretamente: é preciso estimá-la. O trecho ensina dois métodos de aproximação: a **moda de Pearson**, que usa a média e a mediana, e a **moda de Czuber**, que usa as frequências da classe modal e das vizinhas.

### Moda de Pearson

Karl Pearson notou que, em distribuições **moderadamente assimétricas**, as três medidas de tendência central guardam uma relação aproximada:

**Mo = 3 · Md − 2 · x̄**

em que Md é a mediana e x̄ é a média. Em outras palavras, a distância entre a média e a moda é cerca de três vezes a distância entre a média e a mediana. Consequência prática: se a média é maior que a mediana (assimetria à direita), a moda fica abaixo da mediana, e vice-versa.

O trabalho do exercício está em obter média e mediana de dados agrupados. O roteiro é:

1. Monte uma tabela com ponto médio da classe (PM), frequência (f), frequência acumulada (fac) e o produto PM · f.
2. **Média**: x̄ = Σ(PM · f) / Σf.
3. **Mediana por interpolação linear**: localize a posição Σf / 2; a classe mediana é a primeira cuja fac alcança ou supera essa posição. Então
   Md = linf + [ (Σf / 2 − fac anterior) / f da classe ] · h,
   com linf = limite inferior da classe mediana e h = amplitude da classe.
4. Aplique Mo = 3 · Md − 2 · x̄.

> 💡 **Exemplo:** 40 observações nas classes 0 a 10 (f = 4), 10 a 20 (10), 20 a 30 (16), 30 a 40 (8) e 40 a 50 (2). Pontos médios 5, 15, 25, 35, 45. Soma de PM · f = 20 + 150 + 400 + 280 + 90 = 940, então x̄ = 940 / 40 = 23,5. A posição da mediana é 20; as frequências acumuladas são 4, 14, 30, 38, 40, logo a classe mediana é a de 20 a 30. Md = 20 + [(20 − 14) / 16] · 10 = 23,75. Então Mo = 3 · 23,75 − 2 · 23,5 = 71,25 − 47 = 24,25.

### Moda de Czuber

Czuber partiu do histograma e considerou três colunas: a da **classe modal** (a de maior frequência simples) e as das classes vizinhas. A moda é o limite inferior da classe modal somado a uma fração x da amplitude. Pela semelhança de triângulos, essa fração é proporcional às diferenças de frequência:

**Mo = linf + [ Δ1 / (Δ1 + Δ2) ] · h**

com:
- linf: limite inferior da classe modal;
- h: amplitude da classe modal;
- Δ1 = f da classe modal − f da classe anterior;
- Δ2 = f da classe modal − f da classe posterior.

A mesma expressão aparece de outras formas, todas equivalentes:

| Forma | Fórmula |
| --- | --- |
| Com diferenças | Mo = li + [ (fMo − fant) / ((fMo − fant) + (fMo − fpost)) ] · h |
| Com denominador simplificado | Mo = li + h · (fMo − fant) / [ 2 · fMo − (fant + fpost) ] |

A ideia (hipótese de Czuber) é que a moda divide a classe modal em partes proporcionais a essas diferenças: quanto mais a vizinha anterior é menor que a classe modal, mais a moda é "puxada" para cima, e vice-versa. Note que a fórmula leva em conta a frequência da própria classe modal, e não só a das vizinhas.

### Casos particulares

- Se a classe modal é a **primeira**, use fant = 0; se é a **última**, use fpost = 0.
- Se fant = fpost, então Δ1 = Δ2 e a moda cai exatamente no **ponto médio** da classe modal (linf + h / 2).
- Lembre-se de identificar corretamente as classes: a modal é a de maior frequência **simples**, não a de maior acumulada.

> 💡 **Exemplo:** classes de amplitude 10, a partir do zero, com frequências 5, 12, 16, 8 e 3 (da primeira à última). A classe modal é a terceira (20 a 30), com f = 16, anterior 12 e posterior 8. Δ1 = 4 e Δ2 = 8, então Mo = 20 + [4 / 12] · 10 = 23,33. Se, noutro caso, as frequências forem 12, 8 e 3 em classes de amplitude 5, a modal é a primeira: Δ1 = 12 − 0 = 12, Δ2 = 12 − 8 = 4 e Mo = 0 + [12 / 16] · 5 = 3,75.

### Como a banca cobra

- Fornece a tabela de frequências e pede a moda por Pearson ou Czuber, às vezes indicando a fórmula no próprio enunciado.
- Dá a tabela com **frequências relativas acumuladas** e um valor desconhecido k. O caminho: tire a frequência simples de cada classe por diferença entre acumuladas consecutivas, escreva a média em função de k e iguale ao valor dado para achar k; depois calcule a mediana e a moda.
- Dá o histograma, e é preciso ler as alturas (frequências) das classes e aplicar Czuber.
- Em certos enunciados, as frequências aparecem em função de uma incógnita (por exemplo 2k, 8k) e o total também; a soma das frequências fornece o valor de k, e o resultado final pode ficar expresso em múltiplos de k.

> ⚠️ **Pegadinha:** as classes podem ser fechadas à esquerda ou à direita; isso não altera as fórmulas, mas exige cuidado para usar o limite inferior correto da classe. Em Pearson, use a mediana por interpolação (e não a posição "aproximada") para chegar ao valor esperado pela banca.

### Para fixar
- Pearson: Mo = 3 · Md − 2 · x̄, válida para distribuições moderadamente assimétricas.
- Média agrupada: soma de (ponto médio · f) dividida por Σf; mediana: interpolação linear na classe de posição Σf / 2.
- Czuber: Mo = linf + [Δ1 / (Δ1 + Δ2)] · h, com Δ1 e Δ2 as diferenças entre a frequência modal e a das classes vizinhas.
- Classe modal é a de maior frequência simples.
- Classe modal na ponta: use zero para a vizinha que não existe.
- Vizinhas iguais: a moda é o ponto médio da classe modal.
- Pearson é cobrado com menos frequência que Czuber; ambas pedem cálculo cuidadoso de média e mediana.

# SINTÉTICO

- **Pearson**: Mo = 3 · Md − 2 · x̄; relação empírica para distribuições moderadamente assimétricas, que exige calcular antes a média e a mediana.
- **Média agrupada**: x̄ = Σ(PM · f) / Σf, com PM o ponto médio de cada classe.
- **Mediana agrupada**: Md = linf + [(Σf / 2 − fac anterior) / f da classe] · h, aplicada à primeira classe cuja acumulada alcança Σf / 2.
- **Czuber**: Mo = linf + [Δ1 / (Δ1 + Δ2)] · h, em que Δ1 e Δ2 são as diferenças entre a frequência da classe modal e as das classes anterior e posterior.
- **Formas equivalentes de Czuber**: Mo = li + h · (fMo − fant) / [2 · fMo − (fant + fpost)]; é a mesma conta, só reescrita.
- **Classe modal**: a de maior frequência simples; nas extremidades, a vizinha ausente conta como frequência zero.
- **Vizinhas iguais**: se fant = fpost, a moda cai no ponto médio da classe modal.
- **Estratégia na prova**: com frequências relativas acumuladas e incógnita k, obtenha as frequências simples por diferença, use a média dada para achar k e só então calcule mediana e moda.

# NOTAS

O material contém um lapso no comentário de uma questão sobre Czuber (a classe com vizinhas iguais): diz "a média é 5" onde deveria dizer "a moda é 5"; o resumo usa o termo correto. Na resolução da primeira questão de Pearson, os valores 35,56 do exemplo-base saem de arredondamentos intermediários; usei exemplos próprios para evitar discrepâncias. Os histogramas e tabelas das questões de concurso vieram como texto embaralhado e não foram usados além do método de resolução.
