---
id: S0421
agente: CLAUDE-L4
materia: Estatística
aula: Aula 01 — Médias
trecho: estatistica/a01/s03
paginas_lidas: 33-46
---
# ANALÍTICO

Este trecho ensina a média aritmética quando os valores não têm o mesmo "peso": a **média ponderada** e a sua aplicação mais frequente em prova, a **média de dados agrupados** (tabelas de frequências). A ideia é uma só: multiplicar cada valor pelo seu peso (ou frequência), somar os produtos e dividir pela soma dos pesos.

### Média ponderada

Quando alguns valores têm mais importância que outros, não vale a média simples. A **média aritmética ponderada** atribui a cada valor x um peso p:

média = (x1·p1 + x2·p2 + ... + xn·pn) ÷ (p1 + p2 + ... + pn)

No numerador, cada valor é multiplicado pelo seu peso; no denominador, somam-se os pesos. Em símbolos: média = Σ(xi·pi) ÷ Σpi.

Passo a passo:
- multiplique cada valor pelo respectivo peso;
- some todos os produtos e guarde o resultado;
- divida pela soma dos pesos.

> 💡 **Exemplo:** num concurso com três provas de pesos 2, 3 e 5, um candidato tirou 6, 8 e 5. Média ponderada = (6·2 + 8·3 + 5·5) ÷ (2 + 3 + 5) = (12 + 24 + 25) ÷ 10 = 6,1. A média simples seria 6,33; a ponderada ficou menor porque a nota mais baixa tem o maior peso.

> ⚠️ **Pegadinha:** o peso pode vir como **porcentagem** ou **fração** do total (por exemplo, "1/4 das unidades vendidas era do tipo A"). Nesse caso os pesos somam 100% (ou 1), o denominador vale 1 e a média é só a soma dos produtos. Se o enunciado só informar duas frações, o peso da terceira categoria é o que falta para chegar a 100%.

> 💡 **Exemplo:** produtos vendidos a R$ 20 (30% das unidades) e a R$ 40 (70% das unidades). Preço médio = 20·0,30 + 40·0,70 = 6 + 28 = R$ 34 por unidade.

A média ponderada sempre fica entre o menor e o maior valor do conjunto e se aproxima dos valores de maior peso.

### Dados brutos e dados agrupados

- **Dados brutos (não agrupados)**: aparecem logo após a coleta, sem tratamento (uma lista de tempos de 10 pessoas, por exemplo).
- **Dados agrupados**: já passaram por alguma organização. Podem ser agrupados **por valor** (cada valor distinto aparece com sua frequência, em ordem crescente) ou **por classes** (intervalos preestabelecidos, como 0 ≤ x < 2, 2 ≤ x < 4, com a contagem de ocorrências em cada um).

A definição de média **não muda** para dados agrupados; só muda o jeito de calcular, porque a tabela já traz as repetições contadas.

### Média para dados agrupados por valor

A frequência de cada valor funciona como o **peso**. Fórmula:

média = Σ(Xi·fi) ÷ Σfi

Multiplique cada valor pela sua frequência, some a coluna dos produtos e divida pelo total de observações (soma das frequências).

> 💡 **Exemplo:** valores 2, 4 e 7 com frequências 3, 5 e 2. Produtos: 6, 20 e 14, soma 40. Total de observações: 3 + 5 + 2 = 10. Média = 40 ÷ 10 = 4,0.

Pontos práticos:
- A frequência é o número de **repetições**: "frequência 3 no valor 2" significa que o 2 apareceu três vezes. Por isso o denominador é o número total de dados.
- Valor com frequência zero não contribui (produto 0), mas também não altera o total.
- Se for usada **frequência relativa** (proporção ou porcentagem) como peso, a soma dos pesos é 1 (ou 100%) e a média é simplesmente Σ(Xi · fri). Foi assim que se obteve a média de pessoas por veículo numa questão: 1·0,50 + 2·0,20 + 3·0,15 + 4·0,10 + 5·0,05 = 2,0. Com 10 mil veículos, o total esperado de pessoas é 2 × 10.000 = 20 mil.
- Para dados agrupados em **classes**, o procedimento é o mesmo, usando como valor representativo de cada classe o seu ponto médio (soma dos limites ÷ 2).

### Propriedade: multiplicar todas as frequências não muda a média

Se uma segunda turma tem frequências todas iguais ao **dobro** das de uma primeira turma, a média das duas é a **mesma**: o numerador e o denominador dobram, e a razão não muda. Só mudaria se as proporções entre as frequências fossem alteradas. Afirmar que a média "dobra" é erro clássico.

### Questões típicas e como resolver

1. **Frequência desconhecida.** Use o total para achar a incógnita. Exemplo: 20 pessoas, 5 com 18 anos, 9 com 20 anos e as demais com 25 anos. As demais são 20 − 14 = 6. Média = (5·18 + 9·20 + 6·25) ÷ 20 = (90 + 180 + 150) ÷ 20 = 21 anos. Quando a relação entre frequências for dada (uma é o dobro da outra), chame de x e de 2x, resolva a soma e depois calcule a média.
2. **Tabela com frequências absolutas, relativas e porcentagens misturadas.** Complete-a por regra de três, usando que a frequência relativa total é 1, a porcentagem total é 100% e a frequência absoluta total é o total de observações (por exemplo, com 100 caixas, frequência relativa 0,2 corresponde a frequência absoluta 100·0,2 = 20). Depois aplique a fórmula.
3. **Diferença percentual em relação à média.** Primeiro calcule a média, depois a diferença e só então divida pela média, pois a base de comparação é a média (se o enunciado disser "em relação à média"). Exemplo: 5 funcionários ganham R$ 1.000 e 15 ganham R$ 2.000. Média = (5.000 + 30.000) ÷ 20 = R$ 1.750; a diferença do primeiro grupo é 750, ou seja, 750 ÷ 1.750 ≈ 42,9% da média.
4. **Nota final com pesos diferentes e exigência de nota mínima.** Calcule a média ponderada e compare com o mínimo exigido; a média alta numa disciplina de peso pequeno pode não salvar o candidato.

> ⚠️ **Pegadinha:** não confunda o **total de linhas** da tabela com o total de observações. O denominador é a **soma das frequências** (ou dos pesos), não a quantidade de valores distintos.

### Para fixar
- Média ponderada = Σ(valor · peso) ÷ Σ pesos.
- Se os pesos forem porcentagens que somam 100%, basta somar os produtos.
- Dados agrupados por valor: média = Σ(Xi · fi) ÷ Σ fi; a frequência é o peso.
- O denominador é o número total de observações (soma das frequências).
- Em classes, usa-se o ponto médio de cada intervalo como valor representativo.
- Multiplicar todas as frequências pelo mesmo número não altera a média.
- A média ponderada fica entre o menor e o maior valor e pende para os de maior peso.
- Em questões com incógnita, descubra primeiro a frequência que falta pelo total.

# SINTÉTICO

- **Média ponderada**: Σ(valor · peso) ÷ Σ pesos; valores mais importantes pesam mais, e o resultado fica entre o mínimo e o máximo e pende para os de maior peso.
- **Passo a passo**: multiplique cada valor pelo seu peso, some os produtos e divida pela soma dos pesos.
- **Pesos em porcentagem ou fração**: se somam 100% (ou 1), o denominador vale 1 e a média é só a soma dos produtos; a parcela que falta para 100% é o peso da última categoria.
- **Dados brutos × agrupados**: brutos estão como foram coletados; agrupados foram organizados por valor (com frequências) ou por classes (intervalos).
- **Média por valor**: Σ(Xi · fi) ÷ Σ fi; a frequência faz o papel de peso e o denominador é o total de observações.
- **Frequência relativa como peso**: a soma dos pesos é 1, então a média é Σ(Xi · frequência relativa); por exemplo, 1·0,5 + 2·0,2 + 3·0,3 = 1,8.
- **Dobrar as frequências**: se todas as frequências são multiplicadas pelo mesmo número, a média não muda, pois numerador e denominador crescem na mesma proporção.
- **Frequência desconhecida**: ache-a pelo total (soma das frequências); se há relação (dobro, triplo), use x e 2x e resolva antes de calcular a média.
- **Tabelas incompletas**: complete-as por regra de três (frequência relativa total = 1; porcentagem total = 100%; absoluta total = N) e só então calcule.
- **Diferença percentual**: calcule a média, depois a diferença e divida pela média quando a comparação for com ela.

# NOTAS

- Na primeira questão com tabela de notas por disciplina, as notas de Direito Tributário, Legislação Tributária, Contabilidade e Auditoria aparecem diferentes entre a primeira tabela do material (7, 7, 8, 8) e a usada no cálculo (6, 6, 7, 7). O resultado do cálculo (98/17 ≈ 5,76) é coerente com a segunda tabela. Optei por não reproduzir esses dados e usei exemplos próprios.
- Na resolução da questão da turma B, o material escreve "12 × 1" e soma 600 ao final, mas o termo correto da idade 12 é 12 × 2 (frequência dobrada), o que fecha em 600/60 = 10. O resumo usa apenas a propriedade (média não muda).
- A última questão (PRF 2012) termina sem gabarito na última página do trecho; a conta de 2,0 pessoas por veículo foi refeita e é consistente.
- O trecho anuncia a média para dados agrupados em classes (intervalos), mas as páginas lidas desenvolvem só o agrupamento por valor. Incluí uma linha com o uso do ponto médio por ser o procedimento padrão; recomenda-se conferir se o trecho seguinte traz o detalhamento.
