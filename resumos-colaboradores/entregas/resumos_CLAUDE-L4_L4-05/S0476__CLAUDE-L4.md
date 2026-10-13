---
id: S0476
agente: CLAUDE-L4
materia: Estatística
aula: Aula 14 — Análise de Variância (ANOVA):
trecho: estatistica/a14/s04
paginas_lidas: 42-52
---
# ANALÍTICO

Este trecho mostra como medir a incerteza dos coeficientes de uma regressão linear: construir intervalos de confiança (para o coeficiente angular, para o intercepto e para uma predição individual) e testar se cada coeficiente é estatisticamente diferente de zero (teste t de significância individual).

### Por que há incerteza nos coeficientes

Os coeficientes da reta são estimados com uma amostra. Outra amostra daria outros números. Quanto mais as estimativas oscilam de amostra para amostra, menos precisas elas são. A oscilação é maior nas regiões afastadas da média de X, e é por isso que previsões para valores de X distantes da média são mais incertas.

Para quantificar isso, constrói-se um **intervalo de confiança** (IC). Como os erros são supostos normais e a variância verdadeira é desconhecida (estimada pelos dados), usa-se a distribuição **t de Student**, e não a normal.

### Graus de liberdade e erro padrão

- **Graus de liberdade dos erros (GLE)** = GLT − GLM, em que GLT = n − 1 (total) e GLM = k (modelo, com k variáveis explicativas). Logo **GLE = n − k − 1**.
- Na regressão **simples** (k = 1): **GLE = n − 2**.
- **Erro padrão do coeficiente angular** (regressão simples): sβ² = QME / Σ(Xi − X̄)², e sβ é a raiz quadrada. QME é o quadrado médio dos erros (SQE / GLE).

Leitura: se os valores de X forem mais dispersos (soma dos desvios ao quadrado maior), o coeficiente é estimado com mais precisão. Na regressão múltipla, os erros padrão saem da diagonal da matriz (X'X)⁻¹ multiplicada pela variância do erro; para a prova, o foco é a regressão simples.

### Intervalos de confiança (bilaterais)

Estrutura comum: **estimativa ± t(GLE) × erro padrão**, com t tomado na tabela para o nível de confiança pedido (a área em cada cauda é α/2).

| Alvo | Estimativa | Erro padrão |
| --- | --- | --- |
| Coeficiente angular β | β̂ | sβ = raiz de QME / Σ(Xi − X̄)² |
| Intercepto α | α̂ | sα = raiz de QME × [1/n + X̄² / Σ(Xi − X̄)²] |
| Predição individual Y0 em X0 | Ŷ0 = α̂ + β̂·X0 | sY = raiz de QME × [1 + 1/n + (X0 − X̄)² / Σ(Xi − X̄)²] |

> 💡 **Exemplo:** n = 12, β̂ = 2,4, QME = 6 e Σ(Xi − X̄)² = 150. Então sβ² = 6/150 = 0,04 e sβ = 0,2. Com GLE = 10 e 95% de confiança, t = 2,228. IC = 2,4 ± 2,228 × 0,2 = 2,4 ± 0,45, ou seja, de 1,95 a 2,85.

> 💡 **Exemplo do intercepto:** com α̂ = 5, X̄ = 10 e os mesmos dados, sα² = 6 × (1/12 + 100/150) = 6 × 0,75 = 4,5, logo sα ≈ 2,12.

> 💡 **Exemplo da predição:** em X0 = 14, Ŷ0 = 5 + 2,4 × 14 = 38,6. sY² = 6 × (1 + 1/12 + 16/150) = 7,14 e sY ≈ 2,67. O IC fica em 38,6 ± 2,228 × 2,67.

Pontos que a banca explora:

- na predição aparece o termo **"1 +"** dentro dos colchetes, que representa o erro individual de uma nova observação; por isso a faixa da predição individual é bem mais larga do que a de uma estimativa média;
- o termo **(X0 − X̄)²** faz o intervalo **crescer conforme X0 se afasta da média**; a predição mais precisa ocorre em X0 = X̄;
- o intervalo de confiança do **intercepto** depende de X̄²: quanto mais longe de zero está a média de X, maior o erro padrão do intercepto;
- se o intervalo do coeficiente angular **contém o zero**, não há evidência de efeito linear ao nível correspondente;
- em **amostras grandes**, a t de Student se aproxima da normal padrão e pode-se usar a tabela normal (por exemplo, 1,96 para 95%).

> ⚠️ **Pegadinha:** o número de graus de liberdade correto é n − 2 na regressão simples. Usar n − 1 ou n é erro de tabela.

### Teste de significância individual (teste t)

Testa se cada coeficiente é diferente de um valor de referência. Como as estimativas seguem t de Student, o teste se chama **teste t**.

**Estatística:** t = (β̂ − β0) / sβ, em que β0 é o valor da hipótese nula. No caso comum, **H0: β = 0** (nenhuma relação linear), e então t = β̂ / sβ. Como o erro padrão é positivo, **t tem sempre o mesmo sinal da estimativa**.

> 💡 **Exemplo:** com β̂ = 2,4 e sβ = 0,2, t = 12. Para o intercepto, 5 / 2,12 ≈ 2,36.

**Decisão:**

- teste **bilateral** (H1: β ≠ 0), o padrão: rejeita-se H0 se t estiver acima do crítico superior ou abaixo do crítico inferior, ou seja, se |t| for grande;
- testes **unilaterais** (H1: β > valor ou β < valor), quando a questão pedir;
- regra do **p-valor**: rejeita-se H0 quando **p < α** (nível de significância); não se rejeita caso contrário;
- o p-valor vem da t de Student com GLE graus de liberdade; em tabela, costuma-se localizar o |t| entre duas colunas e dar o p-valor como faixa;
- o p-valor do teste **unilateral é a metade do bilateral** (para estatística no lado compatível com H1).

> 💡 **Exemplo de faixa:** com 3 graus de liberdade e |t| = 0,8, a tabela bilateral mostra t = 0,765 para p = 0,5 e t = 0,978 para p = 0,4. Logo 0,4 < p < 0,5 (bilateral), e o unilateral fica entre 0,2 e 0,25. Como p é muito maior que qualquer α usual, não se rejeita H0: o coeficiente não é significativo.

### Teste t × teste F

O **teste F** avalia a significância **global** da regressão; o **teste t** avalia cada coeficiente separadamente (útil sobretudo na regressão múltipla, que tem vários coeficientes). Na regressão **simples**, os dois levam à mesma conclusão: **F = t²** sob H0: β = 0. Se F = 144, |t| = 12, e o sinal de t é o do coeficiente estimado. Com F = 0,64, |t| = 0,8.

### Como a banca cobra o cálculo

Em questões numéricas, o caminho padrão é:

1. descobrir n e GLE = n − 2;
2. obter QME = SQE / GLE (ou SQE = SQT − SQM, em que SQM = β̂² × Σ(Xi − X̄)²);
3. obter Σ(Xi − X̄)² = variância amostral de X × (n − 1), quando a questão dá a variância;
4. calcular o erro padrão pedido e o t crítico da tabela (para 95% bilateral, a cauda superior é 0,025);
5. montar a estimativa ± t × erro padrão ou a razão t = β̂ / sβ.

> 💡 **Exemplo:** n = 20, SQE = 9, variância de X = 28, X̄ = 22, α̂ = 5, β̂ = 1,5. Predição em X0 = 18: 5 + 1,5 × 18 = 32. QME = 9/18 = 0,5; Σ = 28 × 19 = 532; sY² = 0,5 × (1 + 1/20 + 16/532) ≈ 0,54. Com t18 = 2,10 (cauda de 0,025), o IC é 32 ± 2,10 × raiz de 0,54.

### Para fixar
- IC bilateral = estimativa ± t(GLE) × erro padrão; usa-se t de Student porque a variância é estimada.
- GLE = n − k − 1; na regressão simples, n − 2.
- sβ² = QME / Σ(Xi − X̄)²; sα² tem o termo extra 1/n + X̄²/Σ(...); a predição tem o "1 +" e o termo (X0 − X̄)².
- A predição é mais incerta quanto mais X0 se afasta de X̄.
- Teste t de significância: H0: β = 0 e t = β̂ / sβ, com o sinal do coeficiente; rejeita-se H0 se p < α (ou |t| passa do crítico).
- Teste unilateral: p-valor é a metade do bilateral.
- Na regressão simples, F = t²; o teste F é global, o teste t é individual.
- Em amostras grandes, a t de Student é aproximada pela normal.

# SINTÉTICO

- **Intervalo de confiança**: estimativa ± t(GLE) × erro padrão; usa-se t de Student porque a variância dos erros é estimada.
- **Graus de liberdade**: GLE = n − k − 1; na regressão simples, n − 2.
- **Erro do coeficiente angular**: sβ² = QME / Σ(Xi − X̄)²; mais dispersão em X dá estimativa mais precisa.
- **Erro do intercepto**: sα² = QME × [1/n + X̄² / Σ(Xi − X̄)²]; cresce quando a média de X é grande em módulo.
- **Predição individual**: sY² = QME × [1 + 1/n + (X0 − X̄)² / Σ(Xi − X̄)²]; o "1 +" a deixa mais larga e ela piora longe de X̄.
- **Intervalo com zero**: se o IC do coeficiente inclui o zero, não há evidência de efeito linear.
- **Teste t**: H0: β = 0, t = β̂ / sβ, com o mesmo sinal da estimativa; rejeita-se H0 se p < α.
- **Unilateral × bilateral**: o p-valor unilateral é a metade do bilateral; o bilateral é o padrão.
- **Relação com F**: na regressão simples, F = t²; o teste F é global e o teste t é individual por coeficiente.
- **Amostra grande**: a t de Student se aproxima da normal, e vale a tabela normal padrão.

# NOTAS

- O material chama o coeficiente angular (inclinação) de "coeficiente linear" em vários pontos (págs. 43, 48); usei "coeficiente angular", que é o termo habitual, e "intercepto" para o termo constante.
- Pág. 45: o material chama de "intervalo de confiança para uma predição individual" a faixa com o termo "1 +"; tecnicamente é um intervalo de predição. Mantive o nome do material e destaquei o "1 +" como diferença.
- Acrescentado fora do trecho: apenas a ideia de que o IC do coeficiente contendo o zero equivale a não rejeitar H0: β = 0 no teste bilateral de mesmo nível, e a observação sobre o intercepto depender de X̄².
- Pág. 52: na questão do IBGE, o material conclui t ≈ 3,2 (item Errado), com a variância do estimador igual a 1/18; conferido.
- A figura das retas simuladas (pág. 42) e as tabelas t de Student parciais (págs. 44, 46, 49) não foram extraídas; as informações necessárias constam do texto (valores t3 = 2,353 e t18 = 2,101 usados nas questões). Cerca de um terço do trecho é questão comentada; resumi os métodos.
