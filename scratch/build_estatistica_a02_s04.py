import re

content = """---
id: "estatistica/a02/s04"
volume: "estatistica/m03"
capitulo: 4
titulo: "Decis: Definição, Algoritmos e Interpolação Linear"
fingerprint: {"startPage": 44, "endPage": 52, "startTopic": "Decil para dados não-agrupados"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-38"
edital: ["geral:4.2", "geral:3.2", "pcpe:1"]
fontes: ["BUSSAB, W. O.; MORETTIN, P. A. Estatística Básica. 9. ed. São Paulo: Saraiva, 2017.", "TRIOLA, M. F. Introdução à Estatística. 12. ed. Rio de Janeiro: LTC, 2017."]
notas: ""
---

Os decis representam a partição decimal da distribuição de dados estatísticos. Ao repartir um rol ordenado em dez faixas com igual quantidade de observações, os decis oferecem um detalhamento posicional intermediário entre a amplitude dos quartis e a minuciosidade dos percentis. Seu cálculo adapta a estrutura conceitual da mediana, substituindo a divisão por dois pela razão decimal por dez.

> [!objetivos]
> - Compreender a definição dos nove decis e suas equivalências com as demais separatrizes.
> - Calcular decis em séries brutas não agrupadas a partir do rol ordenado.
> - Localizar decis em tabelas de frequências simples sem intervalos de classe.
> - Aplicar a fórmula de interpolação linear para obtenção de decis em classes contínuas.

## O Conceito de Decil e a Partição Decimal

Os decis são medidas separatrizes que dividem uma série previamente disposta em rol em dez partes com quantidades rigorosamente iguais de observações. Cada fração delimitada por dois decis consecutivos engloba exatamente dez por cento do total de dados da amostra.

Para repartir uma distribuição em dez partes iguais, são necessários **nove pontos de corte**, designados pelos símbolos D1, D2, D3, D4, D5, D6, D7, D8 e D9. O índice k varia de 1 a 9, indicando a ordem do decil:
- **D1 (Primeiro decil):** deixa dez por cento dos elementos abaixo de si e noventa por cento acima.
- **D2 (Segundo decil):** deixa vinte por cento dos elementos abaixo e oitenta por cento acima.
- **D5 (Quinto decil):** deixa cinquenta por cento dos dados abaixo e cinquenta por cento acima, coincidindo perfeitamente com a mediana e com o segundo quartil: D5 = Md = Q2 = P50.
- **D9 (Nono decil):** deixa noventa por cento dos elementos abaixo de si e apenas os dez por cento maiores acima.

```mermaid Estrutura da Partição por Decis
flowchart TD
    D["Divisão Decimal por Decis (D1 a D9)"]
    D --> D1["D1: Separa os 10% menores (P10)"]
    D --> D2["D2: Separa os 20% menores (P20)"]
    D --> D5["D5: Separa os 50% centrais = Mediana = Q2 = P50"]
    D --> D8["D8: Separa os 80% menores (P80)"]
    D --> D9["D9: Separa os 90% menores (P90)"]
```

O método de cálculo dos decis reproduz fielmente as regras já estudadas para a mediana e os quartis. Substitui-se o fator de posição n / 2 ou k · n / 4 pelo termo posicional decimal:
pos = k · n / 10.

| Decil | Percentual Acumulado Abaixo | Percentual Acumulado Acima | Equivalência Direta |
|---|---|---|---|
| **D1** | 10% | 90% | P10 |
| **D2** | 20% | 80% | P20 |
| **D5** | 50% | 50% | Md, Q2, P50 |
| **D8** | 80% | 20% | P80 |
| **D9** | 90% | 10% | P90 |

## Decis para Dados Não Agrupados e sem Classes

O cálculo de decis em dados não agrupados exige a organização prévia do rol crescente. Para calcular o decil Dk, avalia-se a posição dada por:
pos = k · n / 10.

Se o produto k · n / 10 for um número inteiro, o decil Dk é obtido pela média aritmética simples entre o termo que ocupa essa posição e o termo imediatamente seguinte no rol, ou pelo valor na posição mais próxima adotada pela convenção da banca. Se a posição for fracionária, adota-se o termo correspondente à posição inteira imediatamente superior no rol ordenado.

> [!resolvido] Exemplo em Rol com Dez Observações
> Considere as notas de dez candidatos em um teste operacional:
> Rol: 42, 48, 55, 60, 64, 70, 75, 82, 88, 95.
> Temos n = 10 observações.
> 1. Para D3 (terceiro decil):
> pos = 3 · 10 / 10 = 3.
> O terceiro termo é x(3) = 55 e o quarto é x(4) = 60.
> Fazendo a média entre os termos centrais da faixa:
> D3 = (55 + 60) / 2 = 57,5 pontos.
> 2. Para D8 (oitavo decil):
> pos = 8 · 10 / 10 = 8.
> O oitavo termo é x(8) = 82 e o nono é x(9) = 88.
> D8 = (82 + 88) / 2 = 85 pontos.

Em tabelas pontuais de dados agrupados sem intervalos de classe (valores isolados com frequências fi), a localização do decil utiliza a coluna de frequências acumuladas (Fi ou fac).
Calcula-se o ponto de corte k · n / 10 e identifica-se a primeira linha onde Fi atinge ou supera esse corte. Se Fi coincidir exatamente com k · n / 10, o decil Dk é a média aritmética simples entre o valor xi dessa linha e o valor xi+1 da linha seguinte:
Dk = (xi + xi+1) / 2.

> [!exemplo] Filhos de 170 Professores
> Uma amostra reúne dados sobre o número de dependentes de 170 docentes:
> 
> | Dependentes (xi) | fi | fac |
> |---|---|---|
> | 0 | 40 | 40 |
> | 1 | 65 | 105 |
> | 2 | 45 | 150 |
> | 3 | 20 | 170 |
> | **Total** | **n = 170** | — |
> 
> Para achar o quarto decil D4:
> corte = 4 · 170 / 10 = 68.
> Na primeira linha, fac = 40 < 68. Na segunda linha, fac = 105 ≥ 68.
> Logo, o quarto decil é D4 = 1 dependente.

## Decis para Dados Agrupados em Classes

Quando os dados são contínuos e organizados em intervalos de classe, o decil Dk é estimado por interpolação linear, pressupondo densidade uniforme de dados no interior da classe do decil.

A fórmula geral para o decil Dk em classes é:
Dk = linf + [((k · n / 10) - facant) / fi] · h.

Onde:
- **k:** ordem do decil desejado (k varia de 1 a 9).
- **linf:** limite inferior da classe que contém o decil.
- **k · n / 10:** posição acumulada de corte decimal.
- **facant:** frequência acumulada da classe imediatamente anterior.
- **fi:** frequência simples da própria classe do decil.
- **h:** amplitude da classe do decil (h = lsup - linf).

```mermaid Roteiro do Decil em Classes Contínuas
flowchart TD
    A["Tabela em Classes"] --> B["Calcular Posição: pos = k · n / 10"]
    B --> C["Identificar a Classe do Decil (fac >= k·n/10)"]
    C --> D["Aplicar Dk = linf + [ (k·n/10 - facant) / fi ] · h"]
    D --> E["Conferir se Dk está dentro da classe identificada"]
```

> [!resolvido] Estaturas de 54 Alunos
> Uma pesquisa mediu as estaturas em centímetros de 54 alunos, distribuídas em classes com amplitude h = 8 cm:
> 
> | Classes de Estatura (cm) | fi | fac |
> |---|---|---|
> | 120 a 128 | 6 | 6 |
> | 128 a 136 | 12 | 18 |
> | 136 a 144 | 20 | 38 |
> | 144 a 152 | 10 | 48 |
> | 152 a 160 | 6 | 54 |
> | **Total** | **n = 54** | — |
> 
> 1. **Cálculo de D1 (primeiro decil):**
> Posição: 1 · 54 / 10 = 5,4.
> A primeira classe (120 a 128 cm) tem fac = 6 ≥ 5,4.
> Parâmetros: linf = 120, facant = 0, fi = 6, h = 8.
> D1 = 120 + [((5,4 - 0) / 6)] · 8 = 120 + [(5,4 / 6)] · 8 = 120 + 0,9 · 8 = 120 + 7,2 = 127,2 cm.
> O valor 127,2 cm situa-se perfeitamente dentro do intervalo de 120 a 128 cm.
> 
> 2. **Cálculo de D7 (sétimo decil):**
> Posição: 7 · 54 / 10 = 37,8.
> A terceira classe (136 a 144 cm) tem fac = 38 ≥ 37,8.
> Parâmetros: linf = 136, facant = 18, fi = 20, h = 8.
> D7 = 136 + [((37,8 - 18) / 20)] · 8 = 136 + [(19,8 / 20)] · 8 = 136 + 0,99 · 8 = 136 + 7,92 = 143,92 cm.

> [!atencao] Notação e Rigor nos Cálculos
> Fique atento para não confundir a letra D de decil com o termo quartil em enunciados de provas. Além disso, verifique com cuidado as operações de multiplicação e divisão com decimais para não incorrer em erros de arredondamento.

## Mapa do capítulo

```mermaid Síntese Geral: Cálculo de Decis
flowchart TD
    D["Os Nove Decis (D1 a D9)"]
    D --> P["Partição Decimal<br>Dez partes iguais de 10% com nove pontos de corte"]
    D --> EQ["Equivalência Central<br>D5 = Mediana = Q2 = P50 (50% dos dados)"]
    D --> BR["Dados Brutos e sem Classes<br>Uso da posição k·n/10 no rol e na coluna de fac"]
    D --> CL["Dados em Classes<br>Dk = linf + [ (k·n/10 - facant) / fi ] · h"]
```

### Para fixar

- Os decis dividem a série ordenada em dez partes com igual número de elementos (dez por cento cada).
- Existem nove decis (D1 a D9), sendo D5 rigorosamente igual à mediana e ao segundo quartil.
- Em dados brutos ordenados em rol, calcula-se a posição de ordem através da relação k · n / 10.
- Em tabelas pontuais sem classes, se fac for exatamente igual a k · n / 10, faz-se a média com o valor seguinte.
- Em tabelas com classes, aplica-se interpolação linear com o corte k · n / 10 no numerador.
- O resultado numérico de cada decil deve obrigatoriamente estar contido nos limites da classe identificada.
"""

with open("content/material/estatistica/m03/a02-s04.md", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")
print("Wrote content/material/estatistica/m03/a02-s04.md")
