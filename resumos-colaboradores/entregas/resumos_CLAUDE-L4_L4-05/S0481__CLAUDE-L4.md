---
id: S0481
agente: CLAUDE-L4
materia: Estatística
aula: Aula 13 — Regressão Linear Múltipla
trecho: estatistica/a13/s02
paginas_lidas: 13-24
---
# ANALÍTICO

Este trecho trata da interpretação do modelo de regressão com várias variáveis explicativas e do seu teste global por análise de variância. Cobre a decomposição das somas de quadrados, o R² e o R² ajustado, os graus de liberdade, a estatística F, a tabela ANOVA e os estimadores da variância dos erros.

### Interpretação do modelo

No modelo com duas variáveis explicativas, a reta estimada é Ŷ = a + b1·X1 + b2·X2.

- **a** (intercepto) é o valor estimado de Y quando X1 = 0 e X2 = 0.
- **b1 e b2** são **efeitos parciais**: b1 mede quanto Ŷ varia por unidade de X1 **mantendo X2 constante**, e b2 faz o mesmo para X2.

Em termos de variações: ΔŶ = b1·ΔX1 + b2·ΔX2. Se X2 fica fixo (ΔX2 = 0), então ΔŶ = b1·ΔX1. Uma variável explicativa **sem relação** com Y tem coeficiente igual a zero.

> 💡 **Exemplo:** na regressão do salário estimado (R$ mil) sobre anos de estudo (X1) e anos de experiência (X2), com b1 = 0,8, aumentar um ano de estudo, com a experiência igual, eleva o salário estimado em 0,8 mil.

### Teste global do modelo (ANOVA)

Para saber se **pelo menos uma** variável explicativa se relaciona com Y, usa-se a análise de variância, com as hipóteses:

- **H0**: β1 = β2 = ... = βk = 0 (nenhuma variável explica Y linearmente);
- **Ha**: pelo menos um βi é diferente de zero.

Se H0 não for rejeitada, não há relação linear entre Y e nenhuma das variáveis independentes.

### Soma dos quadrados e R²

A decomposição vale também na regressão múltipla:

**SQT = SQM + SQR**

| Sigla | Significado | Fórmula |
| --- | --- | --- |
| SQT | soma dos quadrados total | Σ(Yi − Ȳ)² |
| SQM | soma dos quadrados do modelo (explicada pela regressão) | Σ(Ŷi − Ȳ)² |
| SQR | soma dos quadrados dos resíduos (erros) | Σ(εi)², com εi = Yi − Ŷi |

Outros autores chamam SQM de "SQR" (regressão) e SQR de "SQE" (erros), então confira as siglas na prova antes de aplicar as fórmulas. O **coeficiente de determinação** é a fração da variação total explicada pelo modelo:

**R² = SQM/SQT = 1 − SQR/SQT**

Como R² tende a **aumentar** sempre que se acrescenta uma variável (mesmo irrelevante), e o excesso de variáveis consome graus de liberdade, usa-se o **R² ajustado**, que penaliza o número de parâmetros:

**R² ajustado = 1 − (SQR/(n − p)) / (SQT/(n − 1)) = 1 − (1 − R²)·(n − 1)/(n − p)**

O R² ajustado é sempre menor ou igual ao R² (quando p > 1) e pode cair se a variável nova pouco contribui.

### Graus de liberdade

Seja **n** o número de observações e **p** o número de **parâmetros estimados, incluindo o intercepto** (p = nº de variáveis explicativas + 1):

| Fonte | Graus de liberdade |
| --- | --- |
| Modelo | p − 1 |
| Resíduos | n − p |
| Total | n − 1 |

E vale gl total = gl resíduos + gl modelo. Alguns autores escrevem o denominador dos resíduos como n − k − 1, com k = nº de variáveis explicativas: é o mesmo valor, pois p = k + 1.

### Quadrados médios e estatística F

Cada quadrado médio é uma soma de quadrados dividida pelos seus graus de liberdade:

- **QMM** = SQM/(p − 1);
- **QMR** = SQR/(n − p);
- **QMT** = SQT/(n − 1).

A estatística do teste global é a razão **F* = QMM/QMR**. Sob H0, F* segue a distribuição **F de Snedecor** com **p − 1** graus de liberdade no numerador e **n − p** no denominador. Quanto maior F*, mais evidência contra H0:

- F* > F crítico: **rejeita-se** H0 (há relação linear significativa);
- F* < F crítico: **não se rejeita** H0.

O F crítico vem da tabela, para o nível de significância dado, com (p − 1; n − p) graus de liberdade.

### Estimadores da variância dos erros

A variância dos erros verdadeiros, σ² = Var(εi), é desconhecida; só se observam os **resíduos** ei = yi − ŷi.

- **EQM** (erro quadrático médio) = SQR/n: média dos quadrados dos resíduos. Mede o ajuste, mas **subestima** σ², sendo estimador **viciado**.
- **σ̂² = SQR/(n − p)** = QMR: corrige o viés pelos graus de liberdade e é o estimador **não viciado** de σ².
- O EQM (SQR/n) é também o **estimador de máxima verossimilhança** (EMV) de σ² quando os erros são normais N(0; σ²); como é viciado, é não viciado só **assintoticamente** (n → infinito).

> ⚠️ **Pegadinha:** o divisor é n − p, e não n − 1 nem n. O QMR é a estimativa não viciada de σ²; o EMV tem n no denominador.

### Tabela ANOVA e exemplo resolvido

As questões costumam trazer a tabela incompleta e pedir um campo faltante. A estrutura é sempre:

| Fonte | gl | Soma dos quadrados | Quadrado médio | F |
| --- | --- | --- | --- | --- |
| Modelo | p − 1 | SQM | SQM/(p − 1) | QMM/QMR |
| Resíduos | n − p | SQR | SQR/(n − p) | |
| Total | n − 1 | SQT | SQT/(n − 1) | |

> 💡 **Exemplo (próprio):** n = 12 observações e 3 variáveis explicativas (p = 4), com SQT = 200 e SQR = 40. Então SQM = 160; gl: modelo 3, resíduos 8, total 11. R² = 160/200 = 0,80. R² ajustado = 1 − (40/8)/(200/11) = 1 − 5/18,18 ≈ 0,725. QMM = 160/3 ≈ 53,3; QMR = 40/8 = 5 (que é σ̂²); F* = 53,3/5 ≈ 10,7. Se esse valor supera o F crítico de (3; 8) graus de liberdade, rejeita-se H0.

> 💡 **Exemplo simples:** com SQM = 60.000 e SQR = 15.000, SQT = 75.000 e R² = 60.000/75.000 = 0,80.

Num exemplo com n = 5 e p = 3 (SQT = 10, SQM = 9,5, SQR = 0,5), os quadrados médios são 4,25, 0,25 e 2,5; o F* é 17, menor que o F crítico (2; 2) = 19,00, e portanto **não se rejeita** H0, mesmo com R² = 0,95. Isso mostra o efeito de poucos graus de liberdade nos resíduos (amostra pequena).

### Para fixar
- Coeficientes são efeitos parciais: variação de Y por unidade da variável, com as demais constantes; o intercepto é Y estimado com todas as variáveis iguais a zero.
- Teste global: H0 é β1 = ... = βk = 0; contra Ha, em que pelo menos um é diferente de zero.
- SQT = SQM + SQR; R² = SQM/SQT = 1 − SQR/SQT.
- gl: modelo p − 1, resíduos n − p, total n − 1 (p inclui o intercepto).
- QMM = SQM/(p − 1); QMR = SQR/(n − p); F* = QMM/QMR, com F de Snedecor (p − 1; n − p).
- Rejeita-se H0 se F* for maior que o F crítico; senão, não se rejeita.
- R² ajustado = 1 − (1 − R²)(n − 1)/(n − p) penaliza variáveis demais.
- σ̂² = SQR/(n − p) é não viciado; SQR/n (EQM e EMV) subestima σ².

# SINTÉTICO

- **Efeitos parciais**: cada coeficiente mede a variação de Y por unidade da variável, mantidas as demais constantes; o intercepto é o valor de Y com todas iguais a zero.
- **Teste global**: H0 diz que todos os βi são zero; aceitá-la significa ausência de relação linear com qualquer variável explicativa.
- **Decomposição**: SQT = SQM + SQR, com R² = SQM/SQT = 1 − SQR/SQT.
- **Graus de liberdade**: modelo p − 1, resíduos n − p, total n − 1, sendo p o número de parâmetros com o intercepto.
- **Quadrados médios**: cada soma de quadrados dividida pelo seu gl; QMM = SQM/(p − 1) e QMR = SQR/(n − p).
- **Estatística F**: F* = QMM/QMR, com F de Snedecor de p − 1 e n − p graus; F* maior que o crítico rejeita H0.
- **R² ajustado**: 1 − (1 − R²)(n − 1)/(n − p); corrige o aumento automático do R² quando se acrescentam variáveis.
- **Variância dos erros**: SQR/(n − p) é o estimador não viciado; SQR/n (EQM, também EMV sob normalidade) é viciado e subestima, só assintoticamente não viciado.
- **Tabela ANOVA**: nas questões, preencha o campo faltante com as relações entre gl, soma de quadrados, quadrado médio e F.

# NOTAS

- Pág. 23: a tabela ANOVA do exemplo traz F = 14, mas o cálculo anterior (págs. 22) dá F* = 4,25/0,25 = 17. Segui 17, pois é o resultado das fórmulas.
- Pág. 16: a frase sobre o comportamento do R² perdeu o verbo no texto extraído ("o R² conforme são adicionadas variáveis..."); entendi como "aumenta", que é o resultado padrão.
- Pág. 17: o texto alterna "QME" e "QMR" para o quadrado médio dos resíduos; usei QMR.
- Acrescentado fora do trecho: a observação de que o R² ajustado é menor ou igual ao R², e o exemplo próprio com n = 12 (valores calculados por mim). Não incluí o valor numérico do F crítico (3; 8), por não constar do trecho.
- Páginas 14 e 23 contêm matrizes e tabelas que a extração reproduz parcialmente; reconstruí pelas fórmulas e pelos números dos cálculos do próprio texto.
