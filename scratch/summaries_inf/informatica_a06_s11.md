##### informatica/a06/s11
A gestão corporativa de planilhas exige ferramentas para diagnosticar dependências lógicas, sintetizar matrizes dispersas, blindar a integridade da digitação e modelar fluxos de capital no tempo. O trecho aborda a auditoria de fórmulas, os mecanismos de consolidação de dados entre abas ou arquivos, os controles e alertas de validação de dados e as funções financeiras fundamentais de valor futuro (VF) e valor presente (VP).

### Auditoria de Fórmulas: Precedentes e Dependentes

O grupo Auditoria de Fórmulas (localizado na guia Fórmulas) disponibiliza inspeção gráfica vetorial para verificar a integridade dos cálculos:

- **Rastrear Precedentes**: ao selecionar uma célula que abriga uma fórmula e acionar o comando, o Excel traça setas azuis com um pequeno círculo nas células que **fornecem dados** para alimentar o cálculo corrente.
- **Rastrear Dependentes**: desenha setas a partir da célula ativa apontando para todas as fórmulas da planilha que **utilizam o seu valor**.
- **Remover Setas**: limpa instantaneamente todas as representações vetoriais sobrepostas na tela.
- **Janela de Inspeção e Avaliar Fórmula**: permite monitorar valores críticos continuamente ou inspecionar o cálculo subexpressão por subexpressão para identificar a causa exata de inconsistências lógicas.

### Consolidação de Dados

A ferramenta **Consolidar** (guia Dados > grupo Ferramentas de Dados) sintetiza dados espalhados em múltiplas planilhas ou pastas de trabalho distintas em uma única tabela resumo:

- **Operações Disponíveis**: além de acumular valores pela função Soma (mais comum), admite consolidações por Média, Contagem, Máximo, Mínimo e Desvio-Padrão.
- **Modos de Agrupamento**:
  - *Por Posição*: quando todas as planilhas de origem possuem idêntica disposição de células (ex.: célula `B2` sempre contém o faturamento do mês 1).
  - *Por Categoria (Rótulos)*: consolida com base nos nomes das linhas e colunas, permitindo que os itens estejam em ordens diferentes nas planilhas de origem.
- **Opção "Criar vínculos com dados de origem"**:
  > ⚠️ **Pegadinha crítica:** se essa caixa de seleção permanecer desmarcada, o Excel efetua uma consolidação estática; qualquer modificação futura nos dados das planilhas de origem **não será refletida** na matriz consolidada. Quando marcada, o software constrói vínculos dinâmicos automáticos organizados em estrutura de tópicos.

### Validação de Dados: Restrições e Mensagens

A **Validação de Dados** blinda a planilha contra entradas errôneas ou fora do padrão corporativo:

- **Critérios de Validação**: restringe a digitação a Números Inteiros, Decimais, Lista suspensa, Datas, Horas, Comprimento de Texto ou Fórmulas Lógicas Personalizadas.
- **Mensagem de Entrada**: exibe um balão informativo flutuante quando o operador seleciona a célula, orientando sobre o formato esperado antes da digitação.
- **Alerta de Erro**: janela disparada quando o dado digitado viola a regra. Possui três níveis de severidade com comportamentos distintos:
  1. **Parar (Stop)**: nível mais restritivo; **impede terminantemente** a aceitação do dado incorreto, obrigando o usuário a corrigir ou cancelar.
  2. **Aviso (Warning)**: adverte sobre a inconformidade, mas faculta ao usuário prosseguir clicando em "Sim".
  3. **Informações (Information)**: apenas notifica sobre o desvio e aceita o dado digitado mediante um clique em "OK".

### Matemática Financeira no Excel: Funções VF e VP

O Excel modela o valor do dinheiro no tempo por meio de parâmetros padronizados: taxa periódica, número de períodos (*nper*), aporte periódico (*pgto*), valor presente (*vp*) e tipo de vencimento (*0* para postecipado/fim do período; *1* para antecipado/início do período). No fluxo de caixa do software, desembolsos e aplicações financeiras assumem sinal negativo (`-`), enquanto recebimentos assumem sinal positivo (`+`).

#### Função Valor Futuro: `=VF(taxa; nper; pgto; [vp]; [tipo])`
Calcula o montante capitalizado acumulado ao término de uma série de aportes constantes:
- Exemplo prático de aplicação: `=VF(0,5%; 60; -500; 0; 0)`
  - Taxa mensal constante de `0,5%` (ou `0,005`).
  - Duração de `60` meses (5 anos).
  - Aporte mensal de `R$ 500,00` negativos (saída de caixa do investidor).
  - Capital inicial zero (`vp = 0`).
  - Depósitos realizados no término de cada mês (`tipo = 0`).
  - O resultado aponta o saldo final acumulado da aplicação.

#### Função Valor Presente: `=VP(taxa; nper; pgto; [vf]; [tipo])`
Determina a quantia equivalente hoje de um fluxo futuro de recebimentos descontado a uma taxa de juros:
- Exemplo prático de avaliação: `=VP(0,08; 5; 1000)`
  - Taxa anual de desconto de `8%` (`0,08`).
  - Prazo de `5` anos (*nper*).
  - Retorno anual de `R$ 1.000,00` recebidos ao final de cada exercício financeiro.
  - O Excel retorna o montante inicial que justificaria o fluxo (aproximadamente `-R$ 3.992,71`).

### Detalhes que caem em prova

- **Precedente × dependente:** se D10 contém `=B5*2`, B5 é precedente de D10 e D10 é dependente de B5. No desenho, a linha termina com uma bola na célula precedente e uma seta na dependente. Várias setas saindo de uma célula para outras indicam Rastrear Dependentes; setas vindas de várias células para uma só indicam Rastrear Precedentes. Se B8 = B7/25 e E8 = B7/B8, então B8 depende de B7 e E8 depende de B7 e de B8. O recurso valida visualmente as relações; as outras opções do grupo são Mostrar Fórmulas e Janela de Inspeção.
- **Formas de consolidar dados:** funções (SOMA, MÉDIA, CONT.SE, MÁXIMO, MÍNIMO, PROCV etc.), tabelas dinâmicas, Power Query e a ferramenta Consolidar. A consolidação funciona com planilhas do mesmo arquivo ou de arquivos diferentes.
- **Passo a passo da ferramenta Consolidar:** abrir o arquivo mestre; Dados > Ferramentas de Dados > Consolidar; escolher a função (soma, média, contagem etc.); em Referência, selecionar o intervalo de cada origem e clicar em Adicionar; se os rótulos estiverem na linha superior e na coluna esquerda, marcar essas duas opções; marcar, se desejado, Criar vínculos com dados de origem; confirmar. Sem os vínculos, mudar os dados de origem não altera a planilha consolidada.
- **Power Query:** Dados > Obter Dados; escolher a fonte (pasta de trabalho, CSV, página da web, banco de dados); no Editor de Consultas, limpar e transformar (filtrar, remover duplicatas, mudar tipos, criar colunas); combinar consultas; Fechar e Carregar; para atualizar depois, usar Atualizar sobre a tabela.
- **Validação de dados, passo a passo:** selecionar as células; Dados > Validação de Dados; escolher o tipo (número inteiro, lista, data, personalizado etc.) e os parâmetros; na guia Mensagem de Entrada, o texto aparece ao selecionar a célula; na guia Alerta de Erro, escolher o estilo (Parar, Aviso, Informações) e a mensagem. Tipos de validação: por regras (por exemplo, inteiros positivos), por lista suspensa (valores permitidos) e por fórmula (por exemplo, valores que somem 100). Benefícios: menos erros, consistência, limite de valores, orientação ao usuário e apoio a análises confiáveis.
- **VF, argumentos:** taxa (por período) e nper (número de períodos) são obrigatórios; pgto é o pagamento constante de cada período; vp é opcional e, se omitido, vale 0; tipo é opcional e, se omitido, vale 0. Se pgto for omitido, vp passa a ser obrigatório. Taxa e nper devem estar na mesma unidade: taxa anual de 6% com 5 anos, ou taxa mensal de 0,5% com 60 meses. Depósitos feitos saem do bolso e entram como negativos; valores recebidos, como positivos. O resultado de `=VF(0,5%; 60; -500; 0; 0)` é cerca de R$ 34.885.
- **VF em questão:** com taxa anual em B2, número de meses em B3, depósito em B4 e pagamento no início do mês, a fórmula é `=VF(B2/12; B3; B4;; 1)` (taxa mensal, vp omitido, tipo 1).
- **VP, argumentos:** taxa, nper e pgto; vf (opcional, 0 se omitido) e tipo (0 ou 1). Se pgto for omitido, vf é obrigatório. Exemplo: `=VP(0,08; 5; 1000)` dá cerca de -R$ 3.992,71; o sinal negativo indica que é preciso desembolsar esse valor hoje para receber os R$ 1.000 anuais.
- **TAXA:** `=TAXA(nper; pgto; vp; [vf]; [tipo]; [estimativa])` devolve a taxa de juros por período; a estimativa, se omitida, é 10% (em geral converge entre 0 e 1). A lista de funções financeiras do assunto inclui VF, VP, TAXA, NPER e PGTO.

### Para fixar

- Rastrear Precedentes localiza células que originaram o cálculo; Rastrear Dependentes identifica fórmulas dependentes.
- A ferramenta Consolidar agrega intervalos de diferentes planilhas por soma, média ou contagem.
- Para manter a matriz consolidada atualizada após alterações na origem, é obrigatório marcar "Criar vínculos com dados de origem".
- O estilo "Parar" da Validação de Dados é o único que bloqueia compulsoriamente a inserção de dados inválidos.
- No fluxo de caixa das funções financeiras, saídas de recursos são representadas por números negativos.
- Em `VF` e `VP`, o argumento tipo `0` indica pagamentos postecipados (no final do período) e `1` indica antecipados.
- A fórmula `=VF(0,5%; 60; -500; 0; 0)` projeta o montante financeiro futuro de 60 depósitos mensais de R$ 500.
- A função `=VP(0,08; 5; 1000)` desconta os pagamentos futuros para determinar o valor presente da operação.

