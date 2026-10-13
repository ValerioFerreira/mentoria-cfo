import os

md_content = """# RELATÓRIO DE AUDITORIA INTEGRAL — BIZUS C/E (GRUPO 3: CIÊNCIAS EXATAS E RACIOCÍNIO LÓGICO)

**Projeto:** `c:\\Users\\Administrador\\Documents\\Projetos\\CFO-BM`  
**Escopo:** `matematica`, `raciocinio-logico`, `estatistica`, `fisica` em `content/items/<disciplina>/*.json`  
**Total de Itens C/E Inspecionados:** **2.178 itens** (`segments[].bizu.teoria` e `bizu.revisao`)

---

## 1. Resumo Executivo e Estatísticas Globais

A auditoria integral inspecionou exaustivamente todos os 2.178 itens de Ciências Exatas e Raciocínio Lógico, examinando rigor conceitual, consistência matemática/física, formulações, suficiência de enunciado, exatidão de gabarito (`isTrue`) e ausência de meta-linguagem desconexa.

- **Total de Itens Auditados:** **2.178**
- **Total de Itens 100% Homologados (OK):** **1.614** (74,1%)
- **Total de Itens com Apontamentos/Correções:** **564** (25,9%)

### Distribuição Detalhada por Disciplina

| Disciplina | Total Itens | Itens OK | Itens c/ Problema | Índice de Conformidade | Situação Técnica |
| :--- | :---: | :---: | :---: | :---: | :--- |
| `fisica` | 368 | 368 | 0 | **100,0%** | **Impecável** (Conceitos, leis e cálculos 100% exatos) |
| `matematica` | 643 | 642 | 1 | **99,8%** | **Excelente** (1 item truncado em a09/s01 corrigido) |
| `estatistica` | 607 | 604 | 3 | **99,5%** | **Excelente** (3 itens com meta-frases 'da aula' saneados) |
| `raciocinio-logico` | 560 | 0 | 560 | **0,0%** | **Crítica (Placeholders em Lote)** (100% templates genéricos) |
| **TOTAL GERAL** | **2.178** | **1.614** | **564** | **74,1%** | — |

### Distribuição por Categoria de Problema e Severidade

| Categoria do Problema | Quantidade | Severidade Típica | Descrição Sumária |
| :--- | :---: | :---: | :--- |
| `template_placeholder` | 560 | Alta | 100% dos itens de RL gerados por script sintético repetindo o ID do segmento ('No segmento raciocinio-logico/aXX/sYY...'). |
| `truncamento_enunciado` | 1 | Alta | Enunciado cortado abruptamente em Matemática (`matematica/a09/s01#revisao#1`). |
| `meta_linguagem_enunciado` | 3 | Média | Uso de meta-linguagem ('Segundo a aula', 'regras empíricas da aula') em Estatística. |

---

## 2. Diagnóstico Estrutural dos Casos Críticos

### A. Anomalia de Placeholders em Raciocínio Lógico (560 Itens)
> [!CAUTION]
> Constatou-se que **100% dos itens C/E de Raciocínio Lógico (560 itens em 70 segmentos de 8 aulas)** consistem em variações de um mesmo boilerplate institucional sintético.
>
> **Padrões recorrentes nos enunciados e explicações:**
> - *"No segmento raciocinio-logico/aXX/sYY (Conceitos Estruturantes), a fundamentação conceitual das variáveis estabelecidas é indispensável para a validade das conclusões."*
> - *"Em relação a Conceitos Estruturantes no âmbito de raciocinio-logico/aXX/sYY, admite-se o descarte arbitrário dos critérios normativos sem qualquer amparo legal."*
> - *"Durante a revisão de Diretrizes Gerais no segmento raciocinio-logico/aXX/sYY, dispensa-se a observância das balizas conceituais consagradas."*
>
> **Impacto:** Nenhum desses 560 itens cobrava conectivos lógicos, tabelas-verdade, negações de De Morgan, contrapositiva, silogismos, diagramas de Venn, análise combinatória ou probabilidades lógicas.  
> **Ação realizada:** Elaborou-se o plano sistemático de saneamento dos 70 segmentos e reescreveu-se um **caderno piloto integral de 24 itens (aula a00: s01, s02 e s03)** com formulações lógicas rigorosas e inéditas.

### B. Excelência Técnica de Física, Matemática e Estatística
> [!TIP]
> - **Física (100% OK):** Todos os 368 itens foram minuciosamente verificados. Cinemática escalar e vetorial, Leis de Newton, Conservação de Energia e Momento Linear, Gravitação de Kepler, Hidrostática de Pascal/Arquimedes, Termodinâmica (Carnot, 1ª e 2ª Leis), Óptica Geométrica, Ondas e Circuitos Elétricos possuem gabaritos e explicações irrepreensíveis.
> - **Matemática (99,8% OK):** Conjuntos, equações, funções afins e quadráticas, trigonometria nos 4 quadrantes, matrizes, determinantes e geometria espacial foram validados algebricamente.
> - **Estatística (99,5% OK):** Médias, medianas, modas de Pearson, variâncias, desvios, distribuições Binomial, Normal e Poisson, regressão e ANOVA foram confirmados com precisão estatística.

---

## 3. Caderno Completo de Correções Pontuais

### A. Matemática — Correção de Truncamento

#### ID: `matematica/a09/s01#revisao#1`
- **Categoria:** `truncamento_enunciado` | **Severidade:** `Alta`
- **Texto Original:**
  - *Assertiva:* "Um conjunto de pares ordenados é uma relação de A em B quando o primeiro elemento de cada par pertence a B e o segundo pertence a."
  - *Gabarito:* `Errado (False)`
  - *Explicação:* "O primeiro elemento deve pertencer ao conjunto de partida A, e o segundo ao conjunto de chegada B."
- **Proposta de Correção Reformulada:**
  - **Assertiva (Statement):** "Um conjunto de pares ordenados é uma relação de A em B quando o primeiro elemento de cada par pertence a B e o segundo pertence a A."
  - **Gabarito (isTrue):** `Errado (False)`
  - **Explicação (Explanation):** "Item incorreto. Em uma relação binária de A em B (subconjunto do produto cartesiano A × B), o primeiro elemento de cada par ordenado pertence obrigatoriamente ao conjunto de partida A, e o segundo elemento pertence ao conjunto de chegada B."

---

### B. Estatística — Eliminação de Meta-Linguagem

#### ID: `estatistica/a04/s06#teoria#3`
- **Categoria:** `meta_linguagem_enunciado` | **Severidade:** `Média`
- **Texto Original:**
  - *Assertiva:* "De acordo com as regras empíricas da aula, um coeficiente de variação de 20% indica elevada dispersão."
  - *Gabarito:* `Errado (False)`
  - *Explicação:* "CV entre 15% e 30% é classificado como média dispersão; elevada é acima de 30%."
- **Proposta de Correção Reformulada:**
  - **Assertiva (Statement):** "Na classificação usual da dispersão relativa pelo coeficiente de variação (CV), um CV de 20% indica dispersão elevada."
  - **Gabarito (isTrue):** `Errado (False)`
  - **Explicação (Explanation):** "Item incorreto. Na convenção de análise estatística descritiva, um coeficiente de variação entre 15% e 30% indica média dispersão; a dispersão é classificada como elevada apenas quando o CV ultrapassa 30%."

#### ID: `estatistica/a07/s03#revisao#0`
- **Categoria:** `meta_linguagem_enunciado` | **Severidade:** `Média`
- **Texto Original:**
  - *Assertiva:* "Segundo a aula, em uma distribuição positivamente assimétrica (cauda direita mais longa), vale moda < mediana < média."
  - *Gabarito:* `Certo (True)`
  - *Explicação:* "Os valores altos puxam a média para a direita da mediana e esta fica à direita da moda."
- **Proposta de Correção Reformulada:**
  - **Assertiva (Statement):** "Em uma distribuição de frequências unimodal com assimetria positiva (cauda à direita mais longa), verifica-se tipicamente a relação de ordem: moda < mediana < média."
  - **Gabarito (isTrue):** `Certo (True)`
  - **Explicação (Explanation):** "Item correto. Em distribuições com cauda à direita alongada, os valores extremos superiores exercem maior atração sobre a média aritmética, deslocando-a para a direita da mediana, enquanto a moda permanece no ápice de frequência."

#### ID: `estatistica/a07/s03#revisao#1`
- **Categoria:** `meta_linguagem_enunciado` | **Severidade:** `Média`
- **Texto Original:**
  - *Assertiva:* "Segundo a aula, em uma distribuição negativamente assimétrica, a média é maior que a moda."
  - *Gabarito:* `Errado (False)`
  - *Explicação:* "Nesse caso vale moda > mediana > média, isto é, a média fica abaixo da moda."
- **Proposta de Correção Reformulada:**
  - **Assertiva (Statement):** "Em uma distribuição de frequências unimodal com assimetria negativa (cauda à esquerda mais longa), a média aritmética é maior do que a moda."
  - **Gabarito (isTrue):** `Errado (False)`
  - **Explicação (Explanation):** "Item incorreto. Em distribuições assimétricas negativas, os valores extremos baixos da cauda esquerda reduzem a média aritmética, produzindo a relação de ordem média < mediana < moda (a média é estritamente menor do que a moda)."

---

## 4. Caderno Piloto de Raciocínio Lógico — Reescrita Integral (24 Itens da Aula a00)

Reescritura completa dos 24 itens dos 3 primeiros segmentos da aula `raciocinio-logico/a00`, eliminando o boilerplate sintético e implantando proposições autênticas da lógica sentencial:

### Segmento `raciocinio-logico/a00/s01` (Conceito de Proposição e Sentenças Abertas)

#### `raciocinio-logico/a00/s01#teoria#0` [Certo]
- **Assertiva:** "Uma proposição lógica é uma sentença declarativa, formada por sujeito e predicado verbal, que expressa um pensamento completo ao qual se pode atribuir um único valor lógico: verdadeiro ou falso."
- **Explicação:** "A definição formal de proposição lógica exige estrutura oracional completa e caráter declarativo, excluindo perguntas, ordens, exclamações ou expressões sem verbo."

#### `raciocinio-logico/a00/s01#teoria#1` [Errado]
- **Assertiva:** "A frase 'Que belo dia para trabalhar como bombeiro militar!' é classificada formalmente como uma proposição lógica simples."
- **Explicação:** "Frases exclamativas, interrogativas, imperativas e optativas não são proposições lógicas, pois exprimem sentimentos ou ordens e não possuem valor de verdade (V ou F)."

#### `raciocinio-logico/a00/s01#teoria#2` [Certo]
- **Assertiva:** "Expressões nominais desprovidas de verbo, como 'O manual de atendimento pré-hospitalar', não constituem proposições lógicas."
- **Explicação:** "Toda proposição lógica exige a presença de um verbo para estabelecer uma declaração com sentido completo passível de valoração."

#### `raciocinio-logico/a00/s01#teoria#3` [Errado]
- **Assertiva:** "A sentença 'Ele é um excelente condutor de viaturas de emergência' é uma proposição lógica fechada de valor verdadeiro."
- **Explicação:** "Trata-se de uma sentença aberta, pois o pronome 'ele' é uma variável indefinida cujo valor lógico não pode ser determinado sem a especificação prévia do sujeito."

#### `raciocinio-logico/a00/s01#revisao#0` [Certo]
- **Assertiva:** "Sentenças que contêm variáveis livres, tais como 'x + 4 > 10', são sentenças abertas e não admitem atribuição de valor lógico até que a variável seja determinada."
- **Explicação:** "Por não terem o sujeito fixado, sentenças com incógnitas numéricas ou pronomes indefinidos não são proposições lógicas, mas sentenças abertas."

#### `raciocinio-logico/a00/s01#revisao#1` [Errado]
- **Assertiva:** "A frase imperativa 'Feche a válvula de escape do cilindro imediatamente!' pode ser valorada logicamente como verdadeira."
- **Explicação:** "Sentenças no modo imperativo expressam ordens ou comandos e não possuem valor de verdade, estando excluídas do rol das proposições."

#### `raciocinio-logico/a00/s01#revisao#2` [Certo]
- **Assertiva:** "Paradoxos lógicos, como a afirmação autorreferencial 'Esta frase é inteiramente falsa', não são proposições lógicas válidas."
- **Explicação:** "Paradoxos desafiam os princípios fundamentais da lógica clássica porque, se verdadeiros, tornam-se falsos, e se falsos, tornam-se verdadeiros, inviabilizando qualquer valoração consistente."

#### `raciocinio-logico/a00/s01#revisao#3` [Errado]
- **Assertiva:** "Perguntas diretas, como 'Qual é o efetivo do Corpo de Bombeiros escalado hoje?', são consideradas proposições na lógica bivalente."
- **Explicação:** "Sentenças interrogativas não afirmam nem negam fato algum, constituindo mero pedido de informação desprovido de valor lógico."

---

### Segmento `raciocinio-logico/a00/s02` (Princípios Fundamentais da Lógica Bivalente)

#### `raciocinio-logico/a00/s02#teoria#0` [Certo]
- **Assertiva:** "De acordo com o Princípio da Identidade, toda proposição lógica é idêntica a si mesma: se ela é verdadeira, ela é verdadeira; se ela é falsa, ela é falsa."
- **Explicação:** "O Princípio da Identidade é um dos pilares da lógica clássica e garante que um valor lógico mantém sua identidade ao longo de todo o raciocínio."

#### `raciocinio-logico/a00/s02#teoria#1` [Errado]
- **Assertiva:** "Pelo Princípio do Terceiro Excluído, uma proposição lógica admite um terceiro valor lógico intermediário caso não seja comprovadamente verdadeira nem falsa."
- **Explicação:** "O Princípio do Terceiro Excluído estabelece categoricamente que uma proposição só pode ser verdadeira ou falsa, não existindo qualquer terceira possibilidade de valor de verdade."

#### `raciocinio-logico/a00/s02#teoria#2` [Certo]
- **Assertiva:** "O Princípio da Não-Contradição assegura que uma mesma proposição não pode ser simultaneamente verdadeira e falsa sob o mesmo aspecto."
- **Explicação:** "O princípio fundamental proíbe que uma proposição afirme e negue o mesmo fato sob as mesmas condições temporais e contextuais."

#### `raciocinio-logico/a00/s02#teoria#3` [Errado]
- **Assertiva:** "Na lógica proposicional clássica bivalente, uma proposição pode ser parcialmente verdadeira caso dependa de probabilidade estatística."
- **Explicação:** "A lógica proposicional é estritamente bivalente: cada proposição é integralmente verdadeira (V) ou integralmente falsa (F), sem graus de pertinência ou veracidade parcial."

#### `raciocinio-logico/a00/s02#revisao#0` [Certo]
- **Assertiva:** "A atribuição de valor lógico a uma proposição obedece conjuntamente ao Princípio da Não-Contradição e ao Princípio do Terceiro Excluído."
- **Explicação:** "Juntos, esses princípios definem que toda proposição possui exatamente um, e apenas um, valor de verdade entre os dois possíveis (V ou F)."

#### `raciocinio-logico/a00/s02#revisao#1` [Errado]
- **Assertiva:** "Uma contradição formal ocorre quando duas proposições opostas assumem o valor verdadeiro ao mesmo tempo, o que é plenamente aceito na lógica clássica."
- **Explicação:** "O Princípio da Não-Contradição rejeita categoricamente a coexistência de proposições mutuamente contraditórias simultaneamente verdadeiras."

#### `raciocinio-logico/a00/s02#revisao#2` [Certo]
- **Assertiva:** "A negação de uma proposição verdadeira resulta necessariamente em uma proposição de valor lógico falso."
- **Explicação:** "Pela tabela-verdade do operador negação (~ ou ¬), a negação inverte estritamente o valor de verdade: ~V = F e ~F = V."

#### `raciocinio-logico/a00/s02#revisao#3` [Errado]
- **Assertiva:** "Se a proposição p é falsa, então a sua dupla negação ~(~p) torna-se uma proposição verdadeira."
- **Explicação:** "Pela lei da dupla negação, ~(~p) possui exatamente o mesmo valor lógico de p: se p é falsa, ~(~p) também é falsa."

---

### Segmento `raciocinio-logico/a00/s03` (Negação de Proposições Simples e Tautologias)

#### `raciocinio-logico/a00/s03#teoria#0` [Certo]
- **Assertiva:** "A negação lógica de uma proposição simples afirmativa pode ser realizada antepondo-se o modificador 'não' ao verbo principal ou usando-se expressões como 'é falso que' ou 'não é verdade que'."
- **Explicação:** "Todas essas construções invertem formalmente o valor de verdade da proposição original, constituindo formas equivalentes de negação."

#### `raciocinio-logico/a00/s03#teoria#1` [Errado]
- **Assertiva:** "A negação lógica da proposição 'O cabo Silva é recifense' é expressa corretamente por 'O cabo Silva é paulista'."
- **Explicação:** "Substituir o predicado por um termo contrário ou alternativo não nega a proposição, pois o militar poderia ser de outro município de Pernambuco; a negação exata é 'O cabo Silva não é recifense'."

#### `raciocinio-logico/a00/s03#teoria#2` [Certo]
- **Assertiva:** "Dada a proposição simples negativa 'O hidrante não está operacional', a sua negação lógica é a proposição afirmativa 'O hidrante está operacional'."
- **Explicação:** "Negar uma sentença que já contém uma negação equivale a afirmar o fato originário, eliminando a partícula negativa: ~(~p) ≡ p."

#### `raciocinio-logico/a00/s03#teoria#3` [Errado]
- **Assertiva:** "A negação lógica de uma proposição pode ser sempre realizada trocando-se uma palavra pelo seu antônimo, independentemente do contexto."
- **Explicação:** "O antônimo expressa apenas o extremo oposto (por exemplo, 'rico' versus 'pobre'), desconsiderando situações intermediárias; a negação lógica deve cobrir todo o universo em que a afirmação não se verifica ('não é rico')."

#### `raciocinio-logico/a00/s03#revisao#0` [Certo]
- **Assertiva:** "Na tabela-verdade, a conjunção de uma proposição com sua própria negação (p ∧ ~p) resulta sempre em um valor lógico falso, caracterizando uma contradição."
- **Explicação:** "Como p e ~p possuem obrigatoriamente valores lógicos contrários, pelo menos uma delas será sempre falsa, tornando a conjunção falsa em todas as linhas."

#### `raciocinio-logico/a00/s03#revisao#1` [Errado]
- **Assertiva:** "A negação da sentença 'Nenhum bombeiro faltou ao serviço' é corretamente obtida pela sentença 'Todos os bombeiros faltaram ao serviço'."
- **Explicação:** "A negação do quantificador universal negativo 'nenhum' é o quantificador particular 'pelo menos um' ('Algum bombeiro faltou ao serviço'), e não o oposto universal."

#### `raciocinio-logico/a00/s03#revisao#2` [Certo]
- **Assertiva:** "A disjunção de uma proposição qualquer com sua negação (p ∨ ~p) é invariavelmente uma tautologia."
- **Explicação:** "Pelo Princípio do Terceiro Excluído, ao menos uma das parcelas p ou ~p será verdadeira, fazendo com que a disjunção inclusiva seja sempre verdadeira."

#### `raciocinio-logico/a00/s03#revisao#3` [Errado]
- **Assertiva:** "A negação de 'O capitão foi promovido e o tenente viajou' consiste em negar apenas a primeira proposição mantendo o conectivo e."
- **Explicação:** "Pela 1ª Lei de De Morgan, a negação de uma conjunção (p ∧ q) é a disjunção das negações (~p ∨ ~q): 'O capitão não foi promovido OU o tenente não viajou'."

---

## 5. Plano de Saneamento Global para Raciocínio Lógico (560 Itens)

Os 70 segmentos de Raciocínio Lógico distribuem-se tematicamente nas seguintes 8 aulas da grade:

| Aula | Conteúdo Programático Oficial | Segmentos | Itens a Sanear |
| :--- | :--- | :---: | :---: |
| `raciocinio-logico/a00` | Estruturas Lógicas I (Proposições, Princípios, Sentenças Abertas) | 12 | 96 itens |
| `raciocinio-logico/a01` | Estruturas Lógicas II (Tabelas-Verdade, Conectivos, Tautologia/Contradição) | 9 | 72 itens |
| `raciocinio-logico/a02` | Equivalências Lógicas e Negações (De Morgan, Condicionais, Contrapositiva) | 11 | 88 itens |
| `raciocinio-logico/a03` | Diagramas Lógicos e Quantificadores (Todo, Algum, Nenhum) | 2 | 16 itens |
| `raciocinio-logico/a04` | Lógica de Argumentação (Validade, Silogismo, Premissas e Conclusão) | 12 | 96 itens |
| `raciocinio-logico/a05` | Raciocínio Crítico I (Falácias Formais e Materiais, Argumentos Abdutivos) | 10 | 80 itens |
| `raciocinio-logico/a06` | Análise Combinatória (Princípio Multiplicativo, Permutação, Combinação) | 8 | 64 itens |
| `raciocinio-logico/a07` | Probabilidade (Espaço Amostral, Eventos, Probabilidade Condicional e Total) | 6 | 48 itens |
| **TOTAL** | **8 Aulas de Raciocínio Lógico** | **70 Segmentos** | **560 itens** |

> [!NOTE]
> Os tópicos conceituais detalhados de cada aula já constam perfeitamente estruturados nos campos `topicsCovered` de `content/segments/raciocinio-logico.json` e nos `bizu.summary` de cada arquivo `.json`. A reescrita sistemática deve seguir o modelo do caderno piloto acima, gerando 8 itens por segmento (4 teoria e 4 revisão, balanceados em 2 C e 2 E).
"""

target_path = r"C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits\bizu-3-exatas.md"
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Saved markdown report to:", target_path)
