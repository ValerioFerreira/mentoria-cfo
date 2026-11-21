import re

content = """---
id: "estatistica/a00/s02"
volume: "estatistica/m01"
capitulo: 2
titulo: "Séries Estatísticas e Apresentação Tabular"
fingerprint: {"startPage": 19, "endPage": 26, "startTopic": "Séries Estatísticas"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-33"
edital: ["geral:1.4", "geral:MAT-3", "geral:3.1", "pcpe:1"]
fontes: ["Material didático institucional CBMPE/PMPE/PCPE — Estatística Geral — consultado em 2026-10-31"]
notas: "Séries estatísticas e normas de apresentação tabular: anatomia e regras de construção de tabelas segundo as normas do IBGE (título, cabeçalho, coluna indicadora, corpo, linhas e fonte no rodapé, sem fechamento lateral); os três elementos fundamentais (tempo, espaço e espécie); classificação das séries homogêneas simples (temporal ou cronológica, geográfica ou territorial, e específica ou categórica); séries mistas ou compostas em tabelas de dupla entrada (específico-temporal e geográfico-temporal); e transição para distribuição de frequências, diferenciando distribuição pontual para variáveis discretas de distribuição por intervalos de classe fechados à esquerda."
---

A apresentação organizada e fidedigna dos dados estatísticos constitui um requisito basilar para a análise técnica e a comunicação transparente na administração pública e na segurança pericial. Tabelas e séries numéricas mal concebidas geram distorções interpretativas e induzem a erros na alocação de recursos operacionais. O conhecimento minucioso das normas de apresentação tabular e o domínio da taxonomia das séries estatísticas e da distribuição de frequências capacitam o estudante a resolver questões de concurso com exatidão e segurança conceitual.

> [!objetivos]
> - Compreender a estrutura formal e as normas técnicas de elaboração de tabelas estatísticas.
> - Dominar os três elementos referenciais: tempo, espaço e espécie em uma série estatística.
> - Classificar as séries simples em temporais, geográficas e específicas.
> - Analisar a estrutura de séries mistas e tabelas de dupla entrada.
> - Compreender a transição entre dados brutos, rol e distribuições de frequências pontuais e intervalares.

## Estrutura Formal e Normas de Apresentação Tabular

Uma **tabela estatística** é uma representação compacta de dados ordenados em linhas e colunas, planejada para expor um resumo metódico de observações numéricas. A construção de tabelas no Brasil é regulamentada formalmente pelas **Normas de Apresentação Tabular da Fundação Instituto Brasileiro de Geografia e Estatística (IBGE)**, que estabelecem parâmetros rigorosos para garantir legibilidade, precisão e comparabilidade científica entre diferentes estudos.

Segundo as normas técnicas vigentes, uma tabela completa compõe-se dos seguintes elementos constitutivos:

1. **Título:** Posicionado na parte superior da tabela, deve responder com clareza a três indagações fundamentais: o que o dado representa (o fato ou fenômeno), onde foi registrado (o local ou espaço geográfico) e quando foi apurado (a época ou período temporal).
2. **Cabeçalho:** Parte superior interna que especifica a natureza do conteúdo contido em cada coluna da tabela.
3. **Coluna Indicadora:** Primeira coluna vertical à esquerda, destinada a identificar o conteúdo descrito em cada linha horizontal correspondente.
4. **Corpo:** Conjunto central de linhas e colunas no qual estão inseridos os dados numéricos da variável pesquisada.
5. **Célula (ou Casa):** Espaço individual resultante da interseção de uma linha com uma coluna, onde se aloja um dado numérico singular.
6. **Rodapé:** Região inferior externa que abriga a **Fonte** (indicação obrigatória da instituição que produziu os dados primários), acompanhada eventualmente por **Notas** (esclarecimentos de metodologia) e **Chamadas** numéricas.

| Componente Estrutural | Posição Técnica | Função Informativa |
| :--- | :--- | :--- |
| **Título** | Topo exterior | Responde: o que, onde e quando foi investigado |
| **Cabeçalho** | Topo interior | Nomeia e descreve as colunas verticais |
| **Coluna Indicadora** | Extremo esquerdo | Nomeia e descreve o conteúdo das linhas |
| **Corpo** | Núcleo da tabela | Malha de dados numéricos distribuídos em células |
| **Fonte** | Rodapé inferior | Identifica a procedência e a autoria dos dados |

> [!atencao]
> As normas do IBGE vedam rigorosamente o fechamento das laterais da tabela com linhas verticais. A tabela deve permanecer aberta dos lados esquerdo e direito. Utilizam-se traços horizontais apenas para delimitar o topo da tabela, separar o cabeçalho do corpo e fechar a base inferior antes do rodapé.

## Os Três Elementos e a Classificação das Séries Simples

Uma **série estatística** define-se como toda sucessão ordenada de dados numéricos que guardam relação direta com uma mesma variável sob análise. Toda série estatística apoia-se invariavelmente em três elementos referenciais determinantes:

- O **Tempo** (época, período cronológico ou momento da ocorrência);
- O **Espaço** (localidade geográfica, município, estado ou região física);
- A **Espécie** (o fato pesquisado, o evento ou a categoria em investigação).

A classificação técnica das séries estatísticas simples decorre diretamente de qual desses três fatores varia, enquanto os outros dois permanecem estritamente constantes ao longo das linhas da tabela:

1. **Série Temporal (ou Cronológica, Histórica, Evolutiva):** O elemento variável é o **tempo** (anos, meses, dias), enquanto a espécie e o espaço geográfico permanecem fixos. Permite analisar a evolução temporal e as oscilações históricas do fenômeno investigado.
2. **Série Geográfica (ou Territorial, Espacial, de Localização):** O elemento variável é o **espaço** (bairros, cidades, estados ou países), mantendo-se inalterados o tempo e o fato pesquisado. Serve para mapear a distribuição territorial de eventos.
3. **Série Específica (ou Categórica):** O elemento variável é o **fato ou categoria** (causas de ocorrência, tipo de veículo, gênero, faixa etária), enquanto a época e a localidade física são mantidas rigorosamente constantes.

| Categoria da Série | Denominações Sinônimas | Elemento que Varia | Elementos Fixados |
| :--- | :--- | :--- | :--- |
| **Temporal** | Cronológica, histórica, evolutiva | Tempo (anos, meses) | Espaço e Espécie |
| **Geográfica** | Territorial, espacial, local | Espaço (cidades, regiões) | Tempo e Espécie |
| **Específica** | Categórica, qualitativa | Espécie (categorias, fatos) | Tempo e Espaço |

```mermaid Taxonomia das Séries Estatísticas Simples
flowchart TD
    Serie["Série Estatística Simples"] --> Temp["Série Temporal: o Tempo varia (anos, meses)"]
    Serie --> Geog["Série Geográfica: o Espaço varia (regiões, municípios)"]
    Serie --> Espec["Série Específica: a Espécie varia (categorias, tipos de eventos)"]

    Temp --> ExTemp["Exemplo: Atendimentos de socorro no Recife de 2018 a 2023"]
    Geog --> ExGeog["Exemplo: Atendimentos de socorro em 2023 por Região de PE"]
    Espec --> ExEspec["Exemplo: Atendimentos no Recife em 2023 por tipo de sinistro"]
```

> [!bizu]
> Para classificar com rapidez uma série estatística simples em prova de concurso, inspecione a coluna indicadora da tabela:
> - Se a coluna indicadora traz anos, meses ou datas: a série é **temporal**.
> - Se a coluna indicadora traz nomes de bairros, cidades ou estados: a série é **geográfica**.
> - Se a coluna indicadora traz categorias funcionais ou tipos de ocorrência: a série é **específica**.

## Séries Mistas e Tabelas de Dupla Entrada

Em estudos técnicos avançados da gestão pública e do policiamento preventivo, comumente surge a necessidade metodológica de analisar simultaneamente o comportamento de duas ou mais variáveis correlacionadas em um mesmo documento tabular. Quando dois ou mais elementos referenciais (tempo, espaço ou espécie) variam concomitantemente, origina-se uma **série mista (ou composta)**.

A apresentação visual de uma série mista requer a utilização de uma **tabela de dupla entrada** (ou tabela de contingência). Nessa configuração, as categorias de uma das variáveis variáveis são dispostas horizontalmente nas linhas da coluna indicadora, enquanto as categorias da segunda variável distribuem-se verticalmente no cabeçalho das colunas superiores. A denominação formal da série mista resulta da combinação dos elementos que variam conjuntamente:

- **Série Específico-Temporal:** Apresenta a variação concomitante de categorias específicas ao longo de sucessivos períodos temporais, mantendo-se constante o local geográfico (por exemplo, ocorrências de acidentes, incêndios e salvamentos registrados ano a ano na cidade de Caruaru).
- **Série Geográfico-Temporal:** Registra simultaneamente diferentes localidades territoriais distribuídas ao longo de diversos anos ou meses, mantendo-se fixada a espécie da ocorrência pesquisada (por exemplo, o número anual de resgates aquáticos realizados nos municípios litorâneos de Pernambuco de 2019 a 2024).
- **Série Geográfico-Específica:** Combina a variação de múltiplas regiões espaciais com diferentes categorias de eventos para um mesmo período fixo de tempo.

| Ocorrência em Caruaru | Ano de 2022 | Ano de 2023 | Ano de 2024 | Total Trienal |
| :--- | :--- | :--- | :--- | :--- |
| **Incêndio em Edificação** | 142 | 165 | 158 | 465 |
| **Salvamento Terrestre** | 210 | 235 | 240 | 685 |
| **Resgate Pré-Hospitalar** | 480 | 512 | 530 | 1.522 |
| **Total Anual** | 832 | 912 | 928 | 2.672 |

> [!exemplo]
> A tabela acima exemplifica uma **série mista específico-temporal**: a coluna indicadora varia a espécie da ocorrência (incêndio, salvamento, resgate) e o cabeçalho varia o tempo cronológico (2022, 2023, 2024), permanecendo constante o espaço territorial delimitado no município de Caruaru.

## Da Tabela Primitiva à Distribuição de Frequências

Ao concluir o processo de coleta em campo, o analista dispõe de uma relação desorganizada de observações numéricas denominada tabela primitiva ou dados brutos. A partir desse material amorfo, a estruturação de uma síntese compreensível segue etapas técnicas indispensáveis:

Primeiramente, constrói-se o **rol**, ordenando-se os dados em ordem crescente de magnitude. A partir dos extremos do rol calcula-se a **Amplitude Total (AT)**, definida pela diferença aritmética entre a observação de valor máximo (X_max) e a observação de valor mínimo (X_min) da amostra:

AT = X_max - X_min

Em seguida, apura-se a **frequência absoluta simples (fi)** de cada valor, que expressa a contagem de vezes que uma dada observação se repete no conjunto amostral. Quando a variável apresenta poucos valores distintos, estrutura-se uma **distribuição de frequências pontual (ou discreta)**, na qual cada valor numérico individual figura em uma linha acompanhado de sua respectiva frequência absoluta, sem perda de nenhum dado original.

Todavia, quando a variável sob análise é contínua ou assume dezenas de valores inteiros distintos, a tabela pontual torna-se excessivamente extensa e ineficiente. Impõe-se, então, o agrupamento dos dados em intervalos numéricos denominados classes, forjando a **distribuição de frequências por intervalos de classe**. Nesse formato, a individualidade dos valores pontuais é sacrificada em benefício de uma visão global clara da distribuição de massa dos dados.

A notação matemática padrão para a delimitação de classes na estatística descritiva é o intervalo **fechado à esquerda e aberto à direita**, convencionalmente representado pelo símbolo "|--":

a |-- b (lê-se: intervalo fechado em a e aberto em b, ou a <= x < b)

Nessa convenção uniforme, o valor exatamente igual ao limite inferior (a) pertence à classe, enquanto um dado cujo valor coincida numericamente com o limite superior (b) é excluído dessa classe e contabilizado compulsoriamente no intervalo de classe imediatamente seguinte, afastando qualquer risco de duplicidade de contagem.

| Notação Algébrica | Notação Simbólica | Significado Estatístico | Inclusão dos Limites |
| :--- | :--- | :--- | :--- |
| **a <= x < b** | a |-- b | Fechado à esquerda, aberto à direita | Inclui o valor a; exclui o valor b |
| **a < x <= b** | a --| b | Aberto à esquerda, fechado à direita | Exclui o valor a; inclui o valor b |
| **a <= x <= b** | a |--| b | Totalmente fechado em ambos os lados | Inclui simultaneamente a e b |
| **a < x < b** | a -- b | Totalmente aberto em ambos os lados | Exclui simultaneamente a e b |

> [!resolvido]
> **Questão Conceitual de Concurso:** Em uma tabela de distribuição de frequências de tempos de atendimento com intervalos de classe delimitados na forma 10 |-- 20 e 20 |-- 30 minutos, em qual classe deve ser computada uma ocorrência cujo tempo exato foi de 20 minutos?
> **Resolução:** A convenção padrão fechada à esquerda e aberta à direita (a |-- b) determina que o limite inferior é inclusivo e o limite superior é exclusivo. Portanto, o valor 20 minutos não entra na classe 10 |-- 20, sendo alocado obrigatoriamente na classe seguinte 20 |-- 30 minutos.

## Mapa do capítulo

```mermaid Síntese de Séries Estatísticas e Apresentação Tabular
flowchart TD
    A["Apresentação Tabular e Séries"] --> B["Normas de Construção Tabular"]
    A --> C["Classificação das Séries Simples"]
    A --> D["Séries Mistas de Dupla Entrada"]
    A --> E["Distribuição de Frequências"]

    B --> B1["Título: o que, onde e quando investigado"]
    B --> B2["Cabeçalho, coluna indicadora, corpo e fonte no rodapé"]
    B --> B3["Normas IBGE: proibição de traços laterais de fechamento"]

    C --> C1["Série Temporal: tempo varia (espécie e espaço fixos)"]
    C --> C2["Série Geográfica: espaço varia (tempo e espécie fixos)"]
    C --> C3["Série Específica: espécie varia (tempo e espaço fixos)"]

    D --> D1["Variação simultânea de dois elementos de referência"]
    D --> D2["Tabelas de dupla entrada: específico-temporal e geográfico-temporal"]

    E --> E1["Rol e Amplitude Total: AT = X_max - X_min"]
    E --> E2["Distribuição pontual versus por intervalos de classe (a |-- b)"]
```

### Para fixar

- **Componentes da Tabela:** Título explicativo, cabeçalho descritivo, coluna indicadora à esquerda, corpo de dados e fonte no rodapé.
- **Normas do IBGE:** As bordas laterais externas da tabela devem permanecer abertas, sem traços verticais de fechamento.
- **Três Elementos Referenciais:** Tempo (época), Espaço (localização geográfica) e Espécie (o fato ou categoria investigada).
- **Série Temporal:** O tempo varia ao longo das linhas, enquanto o local e o fato permanecem rigorosamente constantes.
- **Série Geográfica:** O espaço territorial varia entre as linhas, mantendo-se constantes a época e a espécie sob análise.
- **Série Específica:** As categorias ou espécies variam nas linhas, conservando-se fixos o período temporal e o espaço geográfico.
- **Séries Mistas:** Apresentam variação simultânea de dois elementos, estruturando-se em tabelas matriciais de dupla entrada.
- **Amplitude Total:** Medida calculada pela subtração direta entre o valor máximo e o valor mínimo do rol estatístico.
- **Distribuição Pontual:** Lista cada valor observado individualmente acompanhado de sua contagem de frequência absoluta simples.
- **Intervalo de Classe Padrão:** Adota a convenção fechada à esquerda e aberta à direita (a |-- b), incluindo o limite inferior e excluindo o superior.
"""

path = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\content\material\estatistica\m01\a00-s02.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("File written successfully.")
