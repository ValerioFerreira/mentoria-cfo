##### informatica/a06/s08
No Microsoft Excel, a recuperação e o cruzamento automatizado de registros apoiam-se em funções clássicas de mapeamento tabular e em novas ferramentas matriciais dinâmicas que ampliam a flexibilidade de pesquisa.

### Funções Clássicas de Pesquisa: PROCV e PROCH

- **Função `=PROCV(valor_procurado; matriz_tabela; núm_índice_coluna; [procurar_intervalo])`**:
  - Executa busca vertical, inspecionando exclusivamente a primeira coluna mais à esquerda da matriz delimitada.
  - Ao localizar o registro, retorna a informação contida na mesma linha, na posição referenciada pelo número ordinal da coluna (1 para a primeira, 2 para a segunda, etc.).
  - *Restrições Operacionais Clássicas*:
    - Unidirecionalidade estrita: opera unicamente da esquerda para a direita, sendo incapaz de resgatar colunas posicionadas à esquerda do campo de pesquisa.
    - Fragilidade estrutural: a inserção ou exclusão de colunas intermediárias na planilha altera a contagem ordinal e corrompe o resultado das fórmulas existentes.
    - Padrão de correspondência: assume correspondência aproximada por padrão caso o quarto argumento seja omitido, exigindo `FALSO` (ou `0`) para impor busca exata.
- **Função `=PROCH(valor_procurado; matriz_tabela; núm_índice_linha; [procurar_intervalo])`**:
  - Opera a mesma sistemática lógica do PROCV, diferenciando-se por conduzir a varredura horizontalmente pela primeira linha superior da matriz, retornando o dado da linha indicada no índice.

### A Função PROCX e a Nova Geração de Consultas

- **Sintaxe e Parâmetros da `=PROCX(pesquisa_valor; pesquisa_matriz; matriz_retorno; [se_não_encontrado]; [modo_correspondência]; [modo_pesquisa])`**:
  - Concebida para unificar e substituir com superioridade tanto o PROCV quanto o PROCH nas versões modernas do Excel (Excel 2021 e Microsoft 365).
- **Vantagens Técnicas em Relação ao Modelo Tradicional**:
  - *Busca Bidirecional Completa*: localiza dados para a direita, para a esquerda, para cima ou para baixo com total independência espacial.
  - *Desacoplamento por Vetores*: recebe matrizes separadas de consulta (`pesquisa_matriz`) e retorno (`matriz_retorno`), tornando a fórmula imune a inserções ou exclusões de colunas na tabela.
  - *Correspondência Exata como Padrão*: adota busca exata de forma nativa sem exigir parâmetros adicionais de precisão.
  - *Tratamento de Exceções Integrado*: o argumento opcional `[se_não_encontrado]` permite definir uma mensagem amigável (como `"Não localizado"`), eliminando a necessidade de encadear a função auxiliar `SEERRO`.

### Seleção Pontual e Matrizes Dinâmicas: ESCOLHER e ÚNICO

- **Função `=ESCOLHER(núm_índice; valor1; [valor2]; ...)`**:
  - Recupera um elemento específico contido em uma lista de até 254 argumentos com base na posição ordinal indicada pelo parâmetro inicial.
  - Exemplo: na fórmula `=ESCOLHER(2; "Ouro"; "Prata"; "Bronze")`, a rotina avalia o índice 2 e retorna `"Prata"`.
- **Função `=ÚNICO(matriz; [por_coluna]; [exatamente_uma_vez])`**:
  - Mecanismo de matriz dinâmica que analisa um intervalo com valores repetidos e extrai automaticamente a lista condensada de elementos exclusivos e sem redundâncias.
  - Os resultados sofrem "derramamento" (*spill*) contínuo sobre as células adjacentes livres sem demandar atalhos clássicos de fórmulas matriciais.

### Detalhes que caem em prova

- **PROCV, passo a passo:** o valor procurado deve estar na primeira coluna do intervalo informado, e o número da coluna conta a partir da primeira coluna do intervalo, não da planilha. Exemplo: com tabela em B5:D10 (produto, código, preço), `=PROCV("Teclado"; B5:D10; 3; FALSO)` devolve o preço (terceira coluna do intervalo). Para procurar pelo código, o intervalo passa a ser C5:D10 e o preço fica na coluna 2: `=PROCV("C003"; C5:D10; 2; FALSO)`. O valor procurado pode ser uma referência de célula (por exemplo G5). A função devolve um único item.
- **Quarto argumento do PROCV/PROCH:** FALSO (ou 0) exige valor exato e dispensa ordenação; VERDADEIRO (ou 1, ou omitido) aceita valor aproximado e exige a primeira coluna ordenada. O aproximado não é o mais próximo, e sim o valor anterior na sequência ordenada: com 1, 3 e 5, buscar 2,99 devolve 1. Sem correspondência exata e com FALSO, o resultado é #N/D.
- **PROCH:** procura o valor na linha de cima e devolve o dado da mesma coluna, na linha indicada pelo índice. Por exemplo, `=PROCH(C9; A9:C13; 4; 1)` acha o valor de C9 na primeira linha da matriz e devolve o item da quarta linha da mesma coluna. O H é de horizontal.
- **PROCX:** a ordem é valor procurado, intervalo de busca, intervalo de retorno e, opcionalmente, a mensagem se não achar. O valor pode ser digitado ou vir de uma referência. Ele implementa o que o PROCV e o PROCH fazem.

| Modo de correspondência | Efeito |
| --- | --- |
| 0 | exata; se não achar, devolve #N/D (padrão) |
| -1 | exata; se não achar, devolve o próximo item menor |
| 1 | exata; se não achar, devolve o próximo item maior |
| 2 | curingas: `*` (qualquer quantidade de caracteres), `?` (um caractere) e `~` (para procurar o próprio curinga) |

| Modo de pesquisa | Efeito |
| --- | --- |
| 1 | do primeiro item para o último (padrão) |
| -1 | pesquisa reversa, do último para o primeiro |
| 2 | binária, com a matriz em ordem crescente |
| -2 | binária, com a matriz em ordem decrescente |

Na pesquisa binária, se a matriz não estiver na ordem indicada, os resultados são inválidos.

- **ESCOLHER:** o primeiro argumento é o índice e os demais são os valores (até 254). `=ESCOLHER(4; A1; A2; A3; A4; A5; A6)` devolve o conteúdo de A4. A função pode devolver uma referência: `=SOMA(A1:ESCOLHER(3; A2; A3; A4; A5))` equivale a `=SOMA(A1:A4)`, e com A1 a A4 valendo 5, 15, 25 e 35 o resultado é 80.
- **ÚNICO:** `=ÚNICO(A1:A7)` devolve só os valores distintos do intervalo, sem repetir, e o resultado se espalha pelas células abaixo.

### Para fixar

- PROCV busca na primeira coluna da tabela e retorna de uma coluna à direita; PROCH faz o mesmo na primeira linha.
- PROCV e PROCH quebram se colunas ou linhas forem movidas, pois usam índice numérico.
- PROCX busca em qualquer direção, com vetores separados de busca e de retorno.
- PROCX tem correspondência exata por padrão e trata o erro de forma nativa (argumento se_não_encontrado).
- ESCOLHER devolve o k-ésimo item de uma lista de valores.
- ÚNICO gera uma matriz dinâmica sem valores duplicados.

