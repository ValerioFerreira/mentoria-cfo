---
id: S0360
agente: CLAUDE-L4
materia: Estatística
aula: Aula 03 — Moda
trecho: estatistica/a03/s03
paginas_lidas: 28-39
---
# ANALÍTICO

Este trecho completa o estudo da moda para dados agrupados em classes: o método de King, o ajuste necessário quando as classes têm larguras diferentes (uso da densidade de frequência) e as duas propriedades da moda diante de operações com constantes. Usaremos a notação: **l_inf** (limite inferior da classe modal), **h** (amplitude da classe modal), **f_ant** e **f_post** (frequências das classes vizinhas, anterior e posterior, à modal) e **f_mo** (frequência da classe modal).

### Moda de King

King é um método **gráfico-aproximado**: usa só os dois retângulos vizinhos da classe modal no histograma. A ideia é que a moda "puxa" para o lado da vizinha mais frequente: ela divide o intervalo da classe modal em partes **inversamente proporcionais** às frequências das classes adjacentes. Por semelhança de triângulos, se x é a distância da moda ao limite inferior, vale x / (h − x) = f_post / f_ant. Resolvendo:

**x = [ f_post / (f_ant + f_post) ] · h**  e, portanto,  **Mo (King) = l_inf + [ f_post / (f_ant + f_post) ] · h**

Passos: (1) achar a classe modal (a de maior frequência, desde que as classes tenham a mesma amplitude); (2) identificar l_inf, h, f_ant e f_post; (3) aplicar a fórmula. O resultado sempre cai **dentro da classe modal**.

> 💡 **Exemplo:** idades em classes de amplitude 10 com frequências 0⊢10: 8; 10⊢20: 14; 20⊢30: 22; 30⊢40: 18; 40⊢50: 6. A classe modal é 20⊢30 (22). Então l_inf = 20, h = 10, f_ant = 14, f_post = 18 e Mo = 20 + [18 / (14 + 18)] · 10 = 20 + 5,625 = 25,625.

> ⚠️ **Pegadinha:** a fórmula de King usa **só as vizinhas**; na de Czuber entra também a frequência da própria classe modal. Em King, o numerador é a frequência da classe **posterior** (confundi-la com a anterior inverte o resultado). Czuber: Mo = l_inf + [ (f_mo − f_ant) / ((f_mo − f_ant) + (f_mo − f_post)) ] · h. Com os dados do exemplo, Czuber dá 20 + [8 / (8 + 4)] · 10 ≈ 26,67, diferente de King.

Em questões de concurso, a banca costuma dar a tabela e pedir "a moda pelo método de King": basta aplicar a fórmula com cuidado ao ler as frequências das vizinhas.

### Classes com amplitudes diferentes

King e Czuber, na forma básica, **exigem classes de mesma amplitude**. Quando as larguras variam, a classe de maior frequência absoluta pode não ser a mais "concentrada": uma classe larga com muitos casos pode ter menos concentração que uma classe estreita com quase tantos. Por isso se compara a **densidade de frequência**:

**d = f / h** (frequência da classe dividida pela sua amplitude)

- A **classe modal** é a de **maior densidade**, não a de maior frequência.
- Em histogramas com larguras desiguais, a altura do retângulo deve ser a densidade, para que a **área** seja proporcional à frequência.
- Nas fórmulas de Czuber e King, substituem-se as frequências pelas densidades dos três retângulos (modal, anterior, posterior), mantendo l_inf e h da classe modal.

> 💡 **Exemplo:** classes 0⊢4 (f = 12), 4⊢10 (f = 30), 10⊢12 (f = 14), 12⊢20 (f = 8). Densidades: 12/4 = 3; 30/6 = 5; 14/2 = 7; 8/8 = 1. A maior frequência está em 4⊢10, mas a **modal é 10⊢12** (d = 7). Com d_ant = 5 e d_post = 1: King = 10 + [1 / (5 + 1)] · 2 ≈ 10,33; Czuber = 10 + [(7 − 5) / ((7 − 5) + (7 − 1))] · 2 = 10 + (2/8) · 2 = 10,5.

Caso particular que aparece em prova: se a densidade da classe anterior é **igual** à da posterior, a moda fica no **ponto médio** da classe modal (tanto em Czuber quanto em King, já que as forças dos vizinhos se equilibram). Ex.: uma classe modal 25 ⊢ 27,5 com vizinhas de mesma densidade tem moda (25 + 27,5)/2 = 26,25. Se os dados fornecem só a frequência relativa e todas as classes têm a mesma, a classe **mais estreita** é a de maior densidade, logo é a modal.

### Propriedades da moda

A moda se comporta como a média e a mediana diante de transformações lineares:

| Operação em todos os valores | Efeito na moda |
| --- | --- |
| Somar (ou subtrair) uma constante c | A moda também soma (ou subtrai) c |
| Multiplicar (ou dividir) por uma constante c | A moda também é multiplicada (ou dividida) por c |

> 💡 **Exemplo:** em {3, 8, 8, 8, 10} a moda é 8. Somando 5 a cada elemento, a lista vira {8, 13, 13, 13, 15} e a moda é 13. Multiplicando a lista original por 5, vem {15, 40, 40, 40, 50} e a moda é 40.

Isso vale também para as modas aproximadas (King, Czuber), porque deslocar ou esticar a escala desloca ou estica as classes. Para uma transformação y = a·x + b com a > 0, a moda de y é a·Mo(x) + b.

### Para fixar
- King: Mo = l_inf + [ f_post / (f_ant + f_post) ] · h; só usa as frequências das classes vizinhas.
- Czuber usa também a frequência da classe modal: Δ1 = f_mo − f_ant e Δ2 = f_mo − f_post.
- Os métodos exigem classes de mesma amplitude; sem isso, trabalhe com a **densidade** d = f / h.
- Classe modal com amplitudes variáveis = maior densidade (nem sempre a maior frequência).
- Vizinhas com mesma densidade: moda no ponto médio da classe modal.
- Somar/subtrair constante altera a moda na mesma medida; multiplicar/dividir altera a moda na mesma proporção.
- Sempre confira se o resultado ficou dentro da classe modal.

# SINTÉTICO

- **Moda de King**: Mo = l_inf + [ f_post / (f_ant + f_post) ] · h; usa apenas as frequências das classes vizinhas à modal e posiciona a moda em direção à vizinha mais frequente.
- **Passo a passo**: achar a classe de maior frequência, anotar l_inf, h, f_ant e f_post e substituir; o resultado fica sempre dentro da classe modal (ex.: classe modal 20⊢30 com vizinhas 14 e 18 e h = 10 dá 25,625).
- **King × Czuber**: Czuber considera também a frequência da própria classe modal, com Δ1 = f_mo − f_ant e Δ2 = f_mo − f_post; as respostas costumam diferir.
- **Larguras desiguais**: a classe modal é identificada pela densidade d = f / h, não pela maior frequência absoluta; um retângulo largo pode ter muitos casos e pouca concentração.
- **Cálculo com densidades**: substituir as frequências pelas densidades dos três retângulos nas fórmulas de Czuber e King, mantendo l_inf e h da classe modal.
- **Vizinhas iguais**: se as densidades anterior e posterior são iguais, a moda é o ponto médio da classe modal.
- **Propriedade da soma**: somar ou subtrair c de todos os valores soma ou subtrai c da moda.
- **Propriedade do produto**: multiplicar ou dividir todos os valores por c multiplica ou divide a moda por c.

# NOTAS

- Págs. 28-29: a dedução de King depende de uma figura (triângulos semelhantes) que não foi extraída; reconstruí a lógica em texto a partir das frases e da fórmula final do material.
- Pág. 30: o texto define f_post com a letra "post" e "pos" em fórmulas diferentes (mesma grandeza); padronizei como f_post.
- Pág. 37: a fórmula de Czuber aparece com "df_ant" misturado a "f_ant" em um termo; tratei como erro de digitação e usei densidades nos dois termos, como a conta resolvida confirma.
- Pág. 36 a 37: o exemplo de prova (CESPE/PF 2004) usa quartis para deduzir classes; foi usado apenas o raciocínio do ponto médio quando as densidades das vizinhas são iguais.
- Os exemplos numéricos do resumo (idades de 0 a 50 e classes de larguras 4, 6, 2 e 8) são próprios.
