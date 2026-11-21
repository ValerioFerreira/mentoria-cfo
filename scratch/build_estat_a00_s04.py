import re

content = """---
id: "estatistica/a00/s04"
volume: "estatistica/m01"
capitulo: 4
titulo: "Representação Gráfica das Distribuições de Frequências"
fingerprint: {"startPage": 42, "endPage": 53, "startTopic": "Representação Gráfica das Distribuições de Frequências"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-33"
edital: ["geral:1.4", "geral:4.4", "geral:MAT-3", "geral:3.1", "pcpe:1"]
fontes: ["Material didático institucional CBMPE/PMPE/PCPE — Estatística Geral — consultado em 2026-10-31"]
notas: "Representação gráfica de distribuições de frequências: gráfico de hastes para dados pontuais não agrupados; histograma com retângulos contíguos apoiados nos limites de classe; histograma de densidade de frequência para intervalos de larguras desiguais; polígono de frequências ligando pontos médios e fechando nos eixos com classes fictícias nulas; curva de frequências obtida por polimento pela média ponderada; taxonomia de curvas simétricas e assimétricas; e ogiva de frequências acumuladas crescentes e decrescentes projetando a mediana na interseção."
---

A representação gráfica de uma distribuição de frequências traduz tabelas numéricas complexas em imagens visuais de apreensão imediata. Nos relatórios periciais de criminalística e nos boletins de ocorrência de bombeiros, os diagramas estatísticos permitem aos gestores e analistas identificar padrões de concentração, tendências evolutivas e assimetrias territoriais. Compreender a distinção metodológica entre gráficos de hastes, histogramas, polígonos de frequências, curvas suavizadas e ogivas acumuladas é indispensável para resolver questões de concurso com exatidão matemática.

> [!objetivos]
> - Diferenciar a representação por gráfico de hastes da representação contínua por histograma.
> - Compreender a construção geométrica do histograma e o papel da densidade de frequência.
> - Analisar a obtenção do polígono de frequências e a transição para a curva de frequências polida.
> - Interpretar a ogiva de frequências acumuladas e correlacionar sua interseção com a mediana.

## Gráfico de Hastes para Dados Não Agrupados

O **gráfico de hastes** (também denominado gráfico de bastões) é o modelo visual adequado para representar séries estatísticas compostas por dados pontuais não agrupados em classes. Essa configuração aplica-se tipicamente a variáveis quantitativas discretas que assumem um número limitado de valores inteiros na amostra (como a quantidade de viaturas danificadas por equipe ou o número de ocorrências registradas por turno de serviço).

Na construção do diagrama de hastes, os valores observados da variável são alocados no eixo horizontal das abscissas. Sobre cada valor numérico individual ergue-se um segmento de reta vertical (uma haste) perpendicular ao eixo. A altura física de cada haste é rigorosamente igual à frequência absoluta (ou relativa) daquela observação.

Uma vantagem metodológica primordial do gráfico de hastes reside na **ausência de perda de informação**. Como cada ponto amostral é mantido em sua identidade singular e com sua frequência exata, é perfeitamente viável reconstruir a tabela original completa a partir do gráfico e vice-versa, o que não ocorre em diagramas de dados agrupados.

```mermaid Estrutura Visual do Gráfico de Hastes
flowchart TD
    EixoX["Eixo Horizontal: Valores Discretos da Variável (0, 1, 2, 3)"] --> Hastes["Hastes Verticais Individuais Perpendiculares"]
    Hastes --> Altura["Altura da Haste = Frequência Absoluta ou Relativa"]
    Altura --> Reversibilidade["Preservação Total da Informação: Reversibilidade Completa"]
```

> [!exemplo]
> Em uma inspeção militar registra-se o número de faltas disciplinares de 50 servidores: 0 faltas (30 servidores), 1 falta (12 servidores), 2 faltas (6 servidores) e 3 faltas (2 servidores). O gráfico de hastes exibirá quatro bastões isolados posicionados sobre os pontos 0, 1, 2 e 3, com alturas respectivas 30, 12, 6 e 2, permitindo leitura direta sem agregação.

## O Histograma e a Densidade de Frequência

O **histograma** constitui o gráfico padrão por excelência para representar distribuições de frequências com dados agrupados em intervalos de classe. Trata-se de um diagrama bidimensional formado por uma sucessão de retângulos contíguos (barras justapostas sem qualquer intervalo ou espaçamento vazio entre si), erguidos a partir do eixo horizontal.

A geometria do histograma obedece a regras de construção rigorosas:

1. A base de cada retângulo assenta-se diretamente sobre o eixo horizontal, coincidindo com os limites da respectiva classe (do limite inferior l_inf ao limite superior l_sup), de modo que a largura da base é igual à amplitude do intervalo h.
2. O ponto médio da base do retângulo coincide exatamente com o ponto médio PM da classe correspondente.
3. Quando todos os intervalos possuem a mesma amplitude h constante, a **altura** de cada retângulo é proporcional à frequência absoluta f_i (ou relativa F_i) da classe.
4. A **área total** englobada por todos os retângulos do histograma é diretamente proporcional ao tamanho total da amostra n (ou igual a 1,0 quando se utilizam frequências relativas unitárias).

```mermaid Comparativo Estrutural: Histograma versus Gráfico de Colunas
flowchart LR
    A["Gráficos de Barras Verticais"] --> B["Histograma"]
    A --> C["Gráfico de Colunas"]

    B --> B1["Retângulos contíguos sem espaçamento"]
    B --> B2["Variáveis contínuas agrupadas em classes"]
    B --> B3["A área do retângulo representa a frequência"]

    C --> C1["Colunas separadas por espaços vazios"]
    C --> C2["Variáveis qualitativas ou discretas puras"]
    C --> C3["Apenas a altura representa a frequência"]
```

> [!pegadinha]
> A distinção entre histograma e gráfico de colunas é uma das armadilhas prediletas das bancas de concurso. No histograma, os retângulos são colados (contíguos) porque representam classes de uma variável contínua. No gráfico de colunas clássico, as barras são obrigatoriamente separadas por espaços vazios uniformes, pois representam categorias qualitativas nominais ou dados discretos isolados.

Quando a distribuição apresenta classes com larguras desiguais, a utilização direta da frequência na altura dos retângulos distorceria a percepção visual do leitor. Para manter a proporcionalidade das áreas, a altura deve ser dada pela **densidade de frequência (d_i = f_i / h)**. Dessa forma, a área de cada retângulo expressa com fidelidade a frequência real: Área = Base * Altura = h * (f_i / h) = f_i. A linha contínua que contorna o topo dos retângulos do histograma é denominada poligonal característica.

| Elemento do Histograma | Significado Geométrico | Relação Matemática |
| :--- | :--- | :--- |
| **Base do Retângulo** | Limites do intervalo de classe | Comprimento igual à amplitude h |
| **Centro da Base** | Ponto médio da classe | Posição x_i = (l_inf + l_sup) / 2 |
| **Altura (Classes Iguais)** | Proporcional à contagem de dados | Altura h_ret = f_i (ou F_i) |
| **Altura (Classes Desiguais)** | Densidade de frequência | Altura h_ret = d_i = f_i / h |
| **Área do Retângulo** | Volume proporcional da classe | Área = h * d_i = f_i |

## Polígono de Frequências e Curva Suavizada

O **polígono de frequências** é um gráfico em linha concebido para evidenciar o perfil e o desenho morfológico de uma distribuição agrupada por classes. Ele é construído marcando-se um ponto cartesiano sobre o topo de cada retângulo do histograma, cuja abscissa é o ponto médio da classe (PM) e cuja ordenada é a sua respectiva frequência f_i. Em seguida, unem-se esses pontos sucessivos por meio de segmentos de reta.

Para que a figura geométrica resultante se configure como um polígono fechado, acrescentam-se compulsoriamente duas classes fictícias nos extremos da distribuição: uma classe imaginária anterior à primeira e uma classe imaginária posterior à última, ambas dotadas de frequência rigorosamente igual a zero. Ao ligar as extremidades da linha aos pontos médios dessas classes nulas no eixo horizontal, o polígono fecha-se no eixo. A área total delimitada sob o polígono de frequências é aritmeticamente equivalente à área total dos retângulos do histograma.

Quando o tamanho da amostra n cresce indefinidamente e a amplitude das classes torna-se infinitesimalmente estreita, os vértices angulosos do polígono atenuam-se naturalmente. O analista pode antecipar essa tendência por meio da **curva de frequências**, obtida pelo processo de **polimento**. O polimento suaviza a linha empírica mediante o cálculo de médias ponderadas entre três classes contíguas com peso dois atribuído à classe central:

f_c = (f_anterior + 2 * f_classe + f_posterior) / 4

As curvas de frequências classificam-se quanto à sua simetria e forma em:

- **Curva Simétrica (em Sino):** Valores distribuem-se com perfeita simetria em torno do centro, apresentando caudas laterais idênticas. Média, mediana e moda coincidem no mesmo ponto.
- **Curva Assimétrica à Direita (Assimetria Positiva):** Apresenta concentração de observações nos valores inferiores e cauda alongada à direita. A média é maior que a mediana, que é maior que a moda.
- **Curva Assimétrica à Esquerda (Assimetria Negativa):** Concentra a massa de dados nos valores elevados e alonga sua cauda à esquerda. A média é menor que a mediana, que é menor que a moda.
- **Curvas em J, J Invertido e em U:** Apresentam máximos pronunciados em um ou nos dois extremos da distribuição.

| Morfologia da Curva | Disposição das Caudas | Relação entre Medidas |
| :--- | :--- | :--- |
| **Simétrica (Sino)** | Caudas equilibradas em ambos os lados | Média = Mediana = Moda |
| **Assimétrica Positiva** | Cauda alongada para a direita | Moda < Mediana < Média |
| **Assimétrica Negativa** | Cauda alongada para a esquerda | Média < Mediana < Moda |
| **Forma em U** | Concentrações nos dois extremos | Mínimo na região central |

> [!bizu]
> Grave a regra para assimetria de curvas: o nome da assimetria acompanha sempre o lado da **cauda longa** e não o lado da aglomeração. Se a cauda se estica para a direita, a assimetria é à direita (positiva).

## A Ogiva de Galton (Polígono de Frequências Acumuladas)

A **ogiva** (ou ogiva de Galton) é o gráfico em linha especificamente projetado para representar frequências acumuladas, desempenhando papel crucial na localização gráfica de separatrizes e percentis. Diferentemente do polígono de frequências simples, a ogiva adota convenções geométricas distintas no plano cartesiano:

No eixo horizontal das abscissas não se utilizam os pontos médios, mas sim os **limites exatos das classes**. A ogiva divide-se em duas vertentes:

1. **Ogiva Crescente:** Plota as frequências acumuladas crescentes (f_ac ou F_ac%). O traçado inicia-se no limite inferior da primeira classe com frequência acumulada igual a zero. A partir desse ponto basal, a linha sobe monotonicamente ligando o limite superior de cada classe à sua respectiva frequência acumulada, até atingir o total amostral n (ou 100%) no limite superior da última classe.
2. **Ogiva Decrescente:** Plota as frequências acumuladas decrescentes (f_ad ou F_ad%). O traçado parte do limite inferior da primeira classe com o valor máximo n (ou 100%) e desce monotonicamente até alcançar o valor zero no limite superior da classe derradeira.

Uma propriedade analítica de extraordinária relevância em provas de concurso é o **ponto de interseção entre a ogiva crescente e a ogiva decrescente**. Quando ambas as curvas são traçadas no mesmo sistema de eixos coordenados, o ponto exato no qual elas se cruzam corresponde à frequência acumulada de n/2 (ou 50%). Projetando-se esse ponto de cruzamento perpendicularmente sobre o eixo horizontal, obtém-se diretamente a **Mediana (Md)** da distribuição de frequências.

```mermaid Ogiva de Galton e Interseção na Mediana
flowchart TD
    OgivaCresc["Ogiva Crescente: Sobe de 0 até n (limites superiores)"] --> Cruzamento["Ponto de Interseção: f_ac = f_ad = n/2 (50%)"]
    OgivaDecresc["Ogiva Decrescente: Desce de n até 0 (limites inferiores)"] --> Cruzamento
    Cruzamento --> Projecao["Projeção Perpendicular no Eixo Horizontal"]
    Projecao --> Mediana["Determinação Exata da Mediana da Distribuição"]
```

> [!resolvido]
> **Questão Conceitual de Concurso:** Em um ensaio de aptidão física com 120 candidatos, foram construídas a ogiva de frequências acumuladas crescente e a decrescente para os tempos de corrida. O cruzamento das duas linhas ocorreu em um ponto com ordenada igual a 60 candidatos e abscissa igual a 12 minutos. O que representa o valor 12 minutos?
> **Resolução:** O ponto de cruzamento das ogivas crescente e decrescente indica exatamente a marca dos 50% dos dados (ordenada n/2 = 120/2 = 60). A abscissa correspondente a essa interseção projeta no eixo horizontal o valor da **Mediana**. Logo, 12 minutos é a mediana dos tempos de corrida, significando que metade dos candidatos concluiu a prova em até 12 minutos e a outra metade demandou tempo igual ou superior a 12 minutos.

## Mapa do capítulo

```mermaid Síntese de Representação Gráfica de Frequências
flowchart TD
    A["Representação Gráfica de Frequências"] --> B["Gráfico de Hastes"]
    A --> C["Histograma e Densidade"]
    A --> D["Polígono e Curva de Frequências"]
    A --> E["Ogiva de Galton"]

    B --> B1["Adequado para dados discretos não agrupados"]
    B --> B2["Uma haste por valor com preservação total de informação"]

    C --> C1["Retângulos contíguos apoiados nos limites de classe"]
    C --> C2["Classes desiguais: altura dada pela densidade di = fi / h"]

    D --> D1["Polígono: linha unindo pontos médios (fecha com classes nulas)"]
    D --> D2["Curva polida: fc = (f_ant + 2*f + f_post) / 4"]
    D --> D3["Formas: simétrica em sino, assimétrica positiva e negativa"]

    E --> E1["Representa frequências acumuladas sobre limites de classe"]
    E --> E2["Interseção da crescente com a decrescente projeta a Mediana"]
```

### Para fixar

- **Gráfico de Hastes:** Empregado em dados discretos não agrupados; cada haste reflete a frequência sem perda de informação.
- **Histograma:** Formado por retângulos contíguos sem espaçamento; a base representa a classe e a área reflete a frequência.
- **Distinção Essencial:** Gráfico de colunas possui barras separadas; o histograma apresenta barras coladas de dados contínuos.
- **Classes Desiguais:** Exigem que a altura do retângulo seja calculada pela densidade de frequência di = fi / h.
- **Polígono de Frequências:** Linha que une os pontos médios superiores dos retângulos, fechando no eixo em classes fictícias nulas.
- **Curva de Frequências:** Linha suavizada por polimento ponderado que revela a tendência contínua da população subjacente.
- **Assimetria das Curvas:** A assimetria positiva estica a cauda para a direita; a assimetria negativa estica a cauda para a esquerda.
- **Ogiva Crescente:** Linha de frequências acumuladas crescentes que parte do zero na base e alcança 100% no topo.
- **Eixo da Ogiva:** Utiliza os limites dos intervalos de classe na linha horizontal, diferenciando-se dos pontos médios do polígono.
- **Interseção das Ogivas:** O cruzamento das ogivas crescente e decrescente ocorre em 50% e projeta a mediana da distribuição.
"""

path = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\content\material\estatistica\m01\a00-s04.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("File written successfully.")
