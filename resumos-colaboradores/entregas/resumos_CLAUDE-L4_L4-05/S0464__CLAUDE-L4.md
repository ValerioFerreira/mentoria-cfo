---
id: S0464
agente: CLAUDE-L4
materia: Estatística
aula: Aula 12 — Regressão Linear Simples
trecho: estatistica/a12/s02
paginas_lidas: 19-29
---
# ANALÍTICO

Este trecho amplia a ideia de correlação linear de Pearson em três frentes: a **correlação parcial** (relação entre duas variáveis retirando a influência de uma terceira), a **autocorrelação** (relação de uma variável com ela mesma em momentos ou posições diferentes) e as **propriedades do coeficiente de correlação** frente a transformações dos dados (soma de constante e multiplicação por constante).

### Correlação parcial

O coeficiente de Pearson entre X e Y pode estar "contaminado" por uma terceira variável Z que influencia as duas. A **correlação parcial** quantifica quão intensa é a associação linear entre X e Y, e em que sentido, **controlando (ajustando) o efeito de Z**, isto é, descontando o que Z provoca nas duas.

Notação: **rXY,Z** (X e Y, controlando Z). Se houver mais de uma variável controlada, elas são listadas depois da vírgula.

A fórmula, com a correlação de Pearson entre cada par:

**rXY,Z = ( rXY − rXZ × rYZ ) / √[ (1 − rXZ²) × (1 − rYZ²) ]**

Como interpretar: se a correlação parcial for bem diferente da correlação simples rXY, a variável Z estava influenciando a relação original. Se for igual ou muito próxima, Z pouco interfere.

> 💡 **Exemplo do trecho:** rXY = 0,6, rXZ = 0,5 e rYZ = 0,7. Numerador: 0,6 − 0,5 × 0,7 = 0,25. Denominador: √[(1 − 0,25) × (1 − 0,49)] = √(0,75 × 0,51) = √0,3825 ≈ 0,6185. Logo rXY,Z ≈ 0,404, menor que 0,6: parte da associação aparente vinha de Z.

> 💡 **Exemplo próprio:** rXY = 0,35, rXZ = 0,5 e rYZ = 0,7. O numerador é 0,35 − 0,5 × 0,7 = 0, então rXY,Z = 0: a associação entre X e Y era explicada inteiramente por Z. Já com rXY = 0,8, rXZ = 0,6 e rYZ = 0,5, o resultado é 0,5/√(0,64 × 0,75) = 0,5/0,693 ≈ 0,72, ainda forte depois do controle.

Situação típica: horas de estudo (X) e nota (Y), com o nível de estresse (Z) afetando ambas. A correlação parcial isola a relação "direta" entre estudo e desempenho.

> ⚠️ **Pegadinha:** se Z não se correlaciona com X nem com Y (rXZ = rYZ = 0), a fórmula devolve rXY: nada a ajustar. E o numerador usa o **produto** rXZ × rYZ, e não a soma; o denominador usa as correlações **ao quadrado** dentro da raiz.

### Autocorrelação

Em vez de relacionar duas variáveis diferentes, a **autocorrelação** relaciona os valores **de uma mesma variável em momentos ou posições diferentes** ("o valor de hoje se parece com o de ontem?").

| Autocorrelação | Interpretação |
| --- | --- |
| Positiva | valores da variável tendem a ser semelhantes em momentos ou posições diferentes |
| Negativa | valores tendem a variar em sentidos opostos |
| Próxima de zero | não há relação linear clara entre os valores em pontos diferentes |

Para que serve:
- Em **séries temporais** (dados ao longo do tempo), ajuda a identificar **tendências** e **sazonalidade**, e portanto a prever valores futuros a partir dos passados.
- Também se aplica a dados **espaciais** (posições no espaço).
- Em modelos de regressão, a autocorrelação dos **resíduos** (erros do modelo) é sinal de problema de especificação do modelo e **viola a suposição de independência dos erros**.
- É usada em áreas como economia, meteorologia e finanças.

> ⚠️ **Pegadinha:** autocorrelação alta nos resíduos de uma regressão é um problema (suposição violada), e não uma qualidade do modelo.

### Propriedades do coeficiente de correlação

O coeficiente de correlação linear é calculado com os desvios em relação às médias:

**r = Σ[(Xi − X̄)(Yi − Ȳ)] / √[ Σ(Xi − X̄)² × Σ(Yi − Ȳ)² ]**

Os valores de r ficam entre −1 e +1. Duas propriedades mostram como r reage a mudanças nos dados.

#### 1ª propriedade: soma ou subtração de constante

**Somar (ou subtrair) uma constante a uma variável não altera r.** Isso acontece porque a constante desloca a média na mesma medida, e os desvios continuam os mesmos. As constantes podem ser diferentes para X e Y.

> 💡 **Exemplo do trecho:** X = 1, 2, 3, 4, 5 e Y = 6, 7, 8, 9, 10 dão r = 10/√(10 × 10) = 1. Somando 3 a X e 5 a Y, os desvios não mudam e r continua 1.

Uso prático: simplificar contas, subtraindo valores grandes. Com X = 201, 202, 204, 205 e Y = 301, 302, 308, 309, subtrai-se 200 de X e 300 de Y, ficando com 1, 2, 4, 5 e 1, 2, 8, 9. Médias 3 e 5; soma dos produtos dos desvios = 22; Σ(dx²) = 10; Σ(dy²) = 50; r = 22/√500 ≈ 0,984, o mesmo valor dos dados originais.

#### 2ª propriedade: multiplicação ou divisão por constante

Ao multiplicar (ou dividir) uma variável por uma constante, o **valor absoluto de r não muda**; o que pode mudar é o **sinal**:

| Constantes aplicadas a X e a Y | Efeito sobre r |
| --- | --- |
| Mesmo sinal (ambas positivas ou ambas negativas) | r não muda (valor e sinal) |
| Sinais contrários | r troca de sinal, com o mesmo valor absoluto |

> 💡 **Exemplo do trecho:** com os dados X = 1 a 5 e Y = 6 a 10, r = 1. Multiplicando ambos por 2, ou ambos por −2, continua 1. Multiplicando X por 2 e Y por −2, r passa a −1.

Uso prático: dividir os dados por um fator comum para facilitar a conta. Com X = 200, 350, 400, 450 e Y = 300, 350, 450, 500, dividindo tudo por 50 obtêm-se X = 4, 7, 8, 9 e Y = 6, 7, 9, 10. Médias 7 e 9; soma dos produtos dos desvios = 11; Σ(dx²) = 14; Σ(dy²) = 10; r = 11/√140 ≈ 0,93.

Regra geral: multiplicar só uma das variáveis por uma constante positiva não muda r; por uma negativa, inverte o sinal. Em geral, o sinal de r é multiplicado pelo sinal do produto das duas constantes.

> 💡 **Exemplo próprio:** X = 1, 2, 3 e Y = 2, 4, 3. Médias 2 e 3; produtos dos desvios somam 1; Σ(dx²) = 2 e Σ(dy²) = 2; r = 1/√4 = 0,5. Somando 100 a X e multiplicando Y por −3: r = −0,5 (a soma é irrelevante; o fator negativo inverte o sinal).

> ⚠️ **Pegadinha:** somar constante nunca muda r; multiplicar por constante só pode mudar o sinal. Já a covariância e as variâncias mudam com a multiplicação (a covariância é multiplicada pelo produto das constantes), mas r, que é uma razão, fica preservado em valor absoluto.

### Para fixar
- Correlação parcial rXY,Z = (rXY − rXZ·rYZ)/√[(1 − rXZ²)(1 − rYZ²)]: relação entre X e Y retirando o efeito de Z.
- Se rXY,Z difere muito de rXY, a terceira variável influenciava a relação; se rXZ = rYZ = 0, nada muda.
- Autocorrelação mede a relação de uma variável consigo mesma em momentos ou posições diferentes; positiva = valores semelhantes, negativa = valores opostos, próxima de zero = sem relação linear.
- Usa-se em séries temporais (tendência, sazonalidade, previsão); autocorrelação nos resíduos de uma regressão viola a independência dos erros.
- Somar ou subtrair constante de X e/ou Y não altera o coeficiente de correlação.
- Multiplicar por constantes de mesmo sinal preserva r; por constantes de sinais contrários inverte o sinal de r, mantendo o valor absoluto.
- Essas propriedades permitem simplificar contas (subtrair valores grandes, dividir por fator comum) sem alterar r.

# SINTÉTICO

- **Correlação parcial**: associação linear entre X e Y depois de descontado o efeito de uma terceira variável Z; notação rXY,Z, com mais variáveis controladas após a vírgula.
- **Fórmula**: rXY,Z = (rXY − rXZ·rYZ)/√[(1 − rXZ²)(1 − rYZ²)]; com 0,6, 0,5 e 0,7 o resultado é cerca de 0,404.
- **Interpretação**: se a parcial for bem diferente de rXY, Z influenciava a relação; se rXZ e rYZ forem nulos, a parcial é igual a rXY.
- **Autocorrelação**: relaciona os valores de uma mesma variável em momentos ou posições distintos; positiva indica semelhança, negativa indica oposição e perto de zero indica ausência de relação linear.
- **Utilidade**: detecta tendência e sazonalidade em séries temporais, ajuda a prever valores e, nos resíduos de uma regressão, sinaliza violação da independência dos erros.
- **Soma de constante**: somar ou subtrair constante em X e/ou Y não altera r, porque os desvios em relação às médias continuam iguais.
- **Multiplicação por constante**: o valor absoluto de r se mantém; sinais iguais preservam o sinal de r e sinais contrários o invertem (de 1 para −1).
- **Aplicação nas contas**: subtrair valores grandes ou dividir por um fator comum simplifica o cálculo de r (por exemplo, subtrair 200 e 300, ou dividir tudo por 50).

# NOTAS

Páginas 19-29 legíveis; fórmulas recompostas pelo contexto, e todos os cálculos numéricos dos exemplos foram refeitos e conferidos (0,404; 0,984; 0,93). O texto não traz a fórmula formal da autocorrelação (defasagem); o resumo mantém apenas a definição e a interpretação do texto. A afirmação de que r varia entre −1 e +1 e a regra geral do sinal do produto das constantes não estão escritas literalmente no trecho (as tabelas dão apenas casos particulares), mas são consequências diretas da definição. Os cabeçalhos de algumas tabelas auxiliares do material estão desalinhados (por exemplo, colunas rotuladas Xi onde deveria constar o valor transformado), sem prejuízo dos resultados. Apenas exemplos numéricos de tabelas; nenhuma questão comentada no trecho.
