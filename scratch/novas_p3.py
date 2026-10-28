"""Part 3 of new questions for informatica: Q60 to Q83
Trechos:
- informatica/a06/s08: Q60 to Q63
- informatica/a06/s11: Q64 to Q68
- informatica/a06/s12: Q69 to Q71 (com item=2.2)
- informatica/a08/s02: Q72 to Q73
- informatica/a10/s03: Q74 to Q79
- informatica/a10/s05: Q80 to Q83
"""

NOVAS_P3 = """
@@ a06/s08 | A
No aplicativo de planilhas eletrônicas Microsoft Excel 365, a busca e recuperação de valores entre matrizes foi aprimorada com funções modernas de consulta. Acerca das características operacionais da função PROCX, assinale a opção correta.
A) A função PROCX realiza buscas verticais e horizontais, adota correspondência exata por padrão e permite pesquisar à esquerda da coluna de pesquisa.
B) A função PROCX exige obrigatoriamente que a tabela de pesquisa esteja previamente classificada em ordem alfabética ascendente.
C) A função PROCX restringe sua busca exclusivamente a matrizes verticais, sendo incapaz de pesquisar dados dispostos em linhas horizontais.
D) A função PROCX impede o retorno de mensagens personalizadas na hipótese de o valor procurado não ser localizado na tabela.
E) A função PROCX foi descontinuada na versão Microsoft 365, sendo substituída integralmente pelo comando de busca manual do teclado.
// Comentário: A função PROCX (XLOOKUP) representa uma evolução substancial sobre o PROCV e o PROCH: opera tanto em colunas verticais quanto em linhas horizontais, adota por padrão a correspondência exata (dispensando o quarto argumento zero/falso do PROCV), pode pesquisar dados situados à esquerda da coluna de consulta e traz argumento nativo para tratar valores não encontrados sem demandar a função SEERRO.

@@ a06/s08 | C
Em planilhas corporativas organizadas horizontalmente, o resgate de parâmetros requer funções direcionadas à leitura de linhas de dados. Com relação à sintaxe e ao funcionamento da função PROCH no Microsoft Excel 365, assinale a opção correta.
A) A função PROCH realiza buscas estritamente verticais na primeira coluna à esquerda de uma matriz bidimensional de células.
B) A função PROCH destina-se a converter automaticamente números inteiros em valores monetários expressos em moeda estrangeira.
C) A função PROCH pesquisa um valor na linha superior de uma tabela e retorna o valor correspondente na mesma coluna em uma linha indicada.
D) A função PROCH exige que todos os dados da planilha sejam formatados obrigatoriamente em negrito e alinhados à margem direita.
E) A função PROCH atua excluindo de forma permanente as linhas intermediárias da planilha que contiverem células em branco.
// Comentário: A função PROCH (Pesquisa Horizontal) localiza um valor especificado na primeira linha superior de uma tabela ou matriz e retorna o valor contido na mesma coluna a partir de um índice de linha informado pelo usuário. Já a busca vertical na primeira coluna é desempenhada pela função PROCV.

@@ a06/s08 | E
A extração de elementos distintos em grandes bases de registros é frequentemente necessária para a elaboração de relatórios cadastrais e estatísticos. No Microsoft Excel 365, a respeito da função ÚNICO, assinale a opção correta.
A) A função ÚNICO atua excluindo fisicamente as linhas duplicadas da tabela de dados de origem sem manter qualquer registro original.
B) A função ÚNICO exige que o usuário digite fórmulas matriciais antigas com a combinação compulsória de teclas Ctrl + Shift + Enter.
C) A função ÚNICO opera exclusivamente sobre números inteiros pares, sendo incompatível com cadeias de caracteres textuais alfanuméricas.
D) A função ÚNICO restringe-se a somar os valores numéricos de células selecionadas que possuam preenchimento de cor amarelo claro.
E) A função ÚNICO é uma função de matriz dinâmica que extrai e retorna uma lista contendo apenas os valores exclusivos de um intervalo.
// Comentário: A função ÚNICO (UNIQUE) integra a categoria de matrizes dinâmicas do Microsoft 365. Ela recebe um intervalo ou matriz de dados e retorna automaticamente, em um bloco de despejo dinâmico, os valores exclusivos (sem duplicidade) ou aqueles que aparecem exatamente uma única vez, sem alterar os dados da fonte original.

@@ a06/s08 | B
O direcionamento programático de resultados em modelos matemáticos pode exigir a seleção de valores específicos com base em uma posição sequencial numérica. Acerca da função ESCOLHER no Microsoft Excel 365, assinale a opção correta.
A) A função ESCOLHER ordena alfabeticamente os valores de uma coluna e descarta registros que contiverem erros de sintaxe matemática.
B) A função ESCOLHER utiliza um número de índice inicial para selecionar e retornar um valor correspondente de uma lista de argumentos fornecida.
C) A função ESCOLHER restringe-se a calcular a média aritmética ponderada dos dez maiores números reais presentes na planilha ativa.
D) A função ESCOLHER atua como um comando de proteção de pasta de trabalho, impedindo que usuários editem fórmulas sem senha mestre.
E) A função ESCOLHER exige obrigatoriamente que todos os seus argumentos sejam referências circulares fechadas a células adjacentes.
// Comentário: A função ESCOLHER (CHOOSE) utiliza um argumento numérico inicial denominado número de índice (de 1 a 254) para selecionar e retornar um valor correspondente a partir da lista de argumentos subsequentes fornecidos na fórmula (por exemplo, `=ESCOLHER(2; "Bom"; "Regular"; "Excelente")` retorna "Regular").

@@ a06/s11 | B
A identificação da origem de valores e o rastreamento de dependências lógicas em modelos financeiros complexos constituem tarefas de controle de qualidade em planilhas. No Microsoft Excel 365, em relação aos recursos de Auditoria de Fórmulas, assinale a opção correta.
A) O comando Rastrear Precedentes apaga permanentemente as fórmulas das células vizinhas que contiverem números decimais fracionados.
B) As ferramentas Rastrear Precedentes e Rastrear Dependentes traçam setas gráficas indicando as células que alimentam ou dependem da fórmula ativa.
C) A ferramenta Avaliar Fórmula atua ocultando as linhas da planilha de dados para impedir a visualização dos resultados calculados.
D) Os recursos de auditoria de fórmulas são exclusivos de versões corporativas para servidores Linux, não integrando a suíte para Windows.
E) O rastreamento de dependentes veda a localização de erros do tipo divisão por zero, limitando-se à contagem de caracteres alfabéticos.
// Comentário: As ferramentas do grupo Auditoria de Fórmulas (guia Fórmulas do Excel) oferecem recursos visuais de inspeção: "Rastrear Precedentes" desenha setas gráficas apontando as células que fornecem dados para a fórmula selecionada; e "Rastrear Dependentes" exibe setas indicando quais outras células são afetadas pelo valor da célula ativa.

@@ a06/s11 | C
A imposição de restrições sobre o tipo e a faixa de valores admitidos em células evita a ocorrência de inconsistências em bancos de registros institucionais. No que tange ao recurso de Validação de Dados no Microsoft Excel 365, assinale a opção correta.
A) A validação de dados atua exclusivamente criptografando o arquivo da pasta de trabalho com algoritmos assimétricos de alta voltagem.
B) O recurso de validação impede que o usuário digite números inteiros em células formatadas nativamente no padrão de contabilidade.
C) A validação de dados permite restringir o tipo de entrada (como listas, números inteiros ou datas) e exibir mensagens de alerta personalizadas.
D) A validação de dados destina-se unicamente a traduzir textos de idiomas estrangeiros em tempo real durante a digitação de relatórios.
E) As regras de validação de dados são descartadas automaticamente pelo Excel sempre que a pasta de trabalho é salva no disco rígido.
// Comentário: O recurso Validação de Dados (guia Dados do Excel) permite definir critérios estritos para o que pode ser inserido em uma célula (como números inteiros em determinado intervalo, datas específicas, comprimento de texto ou itens selecionáveis a partir de uma lista suspensa), possibilitando ainda configurar mensagens de entrada explicativas e mensagens de erro de parada ou aviso em caso de entradas inválidas.

@@ a06/s11 | A
O cálculo do montante acumulado por uma aplicação financeira sujeita a depósitos regulares e a uma taxa constante apoia-se em funções financeiras padronizadas no Excel. A respeito da função VF (Valor Futuro) no Microsoft Excel 365, assinale a opção correta.
A) A função VF calcula o valor futuro de um investimento considerando pagamentos periódicos constantes e uma taxa de juros fixa ao período.
B) A função VF destina-se a converter parcelas mensais de financiamentos imobiliários em valores brutos de desconto comercial simples.
C) A função VF exige que a taxa de juros informada no primeiro argumento seja expressa obrigatoriamente sob a forma de números primos.
D) A função VF calcula exclusivamente a quantidade total de dias úteis decorridos entre a data inicial e o encerramento do contrato.
E) A função VF desconsidera pagamentos adicionais ao longo do tempo, limitando-se a duplicar o saldo inicial a cada semestre civil.
// Comentário: A função financeira VF (Valor Futuro) calcula o montante acumulado de um investimento com base em uma taxa de juros constante, em um número total de períodos (nper) e em pagamentos periódicos e iguais (pgto), podendo incluir um valor presente inicial (vp) e o tipo de vencimento das parcelas (postecipado ou antecipado).

@@ a06/s11 | A
A avaliação do valor monetário atual de uma sequência de recebimentos futuros prometidos em contratos comerciais é efetuada por meio de desconto financeiro no aplicativo de planilhas. Acerca da função VP (Valor Presente) no Microsoft Excel 365, assinale a opção correta.
A) A função VP retorna o valor presente e atual de uma série de pagamentos futuros com base em uma taxa de juros periódica constante.
B) A função VP tem como objetivo primário calcular a taxa percentual de depreciação física de maquinários pesados de uso industrial.
C) A função VP restringe sua aplicação a contas correntes bancárias encerradas por determinação judicial expressa em processos fiscais.
D) A função VP opera somando aritmeticamente o número de dependentes declarados pelos colaboradores em formulários de imposto de renda.
E) A função VP requer que todas as parcelas futuras possuam valores variáveis e aleatórios estipulados por cotações diárias de bolsas.
// Comentário: A função financeira VP (Valor Presente) traz a valor presente (desconta) o fluxo de pagamentos periódicos e constantes futuros ou um valor futuro único, considerando uma taxa de juros uniforme por período de capitalização (`=VP(taxa; nper; pgto; [vf]; [tipo])`).

@@ a06/s11 | B
A conferência do fluxo matemático de planilhas extensas pode demandar a visualização simultânea de todas as instruções embutidas em suas células. No Microsoft Excel 365, para exibir na tela as fórmulas contidas nas células em vez de seus resultados numéricos, assinale a opção que indica o procedimento correto:
A) Pressionar a combinação de teclas Alt + F4 na janela ativa da pasta de trabalho corporativa.
B) Acessar a guia Fórmulas > grupo Auditoria de Fórmulas e acionar o comando Mostrar Fórmulas (atalho Ctrl + `).
C) Selecionar a guia Inserir e acionar o botão Tabela Dinâmica no grupo Tabelas da interface.
D) Clicar na guia Exibir e marcar a opção Linhas de Grade enquanto o zoom estiver fixado em quatrocentos por cento.
E) Digitar a palavra fórmula na caixa de pesquisa do Windows e reiniciar a estação em modo de segurança.
// Comentário: O recurso "Mostrar Fórmulas" (disponível na guia Fórmulas > grupo Auditoria de Fórmulas ou acionado pelo atalho de teclado Ctrl + `) alterna a exibição de toda a planilha, mostrando as fórmulas exatas digitadas nas células em vez dos valores finais computados, facilitando a depuração e conferência em auditorias.

@@ a06/s12 | A | item=2.2
O cálculo periódico de prestações constantes para liquidação de financiamentos e empréstimos é executado por ferramentas matemáticas consolidadas na planilha eletrônica. No Microsoft Excel 365, com relação à função financeira PGTO, assinale a opção correta.
A) A função PGTO calcula o valor do pagamento periódico de um empréstimo com base em pagamentos e em uma taxa de juros constantes.
B) A função PGTO calcula a quantidade total de anos bissextos contidos no intervalo entre duas datas de nascimento informadas.
C) A função PGTO destina-se a excluir automaticamente débitos bancários prescritos sem necessidade de comprovação de quitação.
D) A função PGTO opera exclusivamente quando o pagamento é efetuado em moeda metálica em espécie nas agências bancárias credenciadas.
E) A função PGTO calcula a raiz quadrada do número total de colunas preenchidas na pasta de trabalho ativa do aplicativo.
// Comentário: A função financeira PGTO calcula a prestação constante periódica necessária para quitar um financiamento ou empréstimo a uma taxa de juros fixa ao longo de determinado número de períodos, com base em seu valor presente (`=PGTO(taxa; nper; vp; [vf]; [tipo])`).

@@ a06/s12 | D | item=2.2
Durante o processamento de cálculos no Microsoft Excel 365, incoerências lógicas em argumentos ou operações inválidas geram códigos padronizados de alerta. A respeito dos tipos de erros retornados em fórmulas do Excel, assinale a opção correta.
A) O erro #N/D surge quando uma fórmula divide um número real pelo valor nulo ou por uma célula desprovida de conteúdo preenchido.
B) O erro #DIV/0! indica que um valor procurado por funções de pesquisa não foi localizado de maneira exata na matriz de dados.
C) O erro #REF! manifesta-se unicamente quando o usuário digita nomes de funções em letras minúsculas sem utilizar acentos ortográficos.
D) O erro #VALOR! ocorre quando a fórmula encontra tipos incompatíveis de dados, como tentar executar operações aritméticas com texto.
E) O erro #NOME? indica que o disco rígido do computador não possui espaço físico livre para armazenar novos arquivos de planilha.
// Comentário: No Excel, o erro `#VALOR!` indica incoerência no tipo de dado esperado (por exemplo, somar um número com um texto não numérico); o erro `#DIV/0!` ocorre na divisão por zero ou célula em branco; o erro `#N/D` indica que o valor de pesquisa não foi encontrado (comum em PROCV e PROCX); o erro `#REF!` indica que a célula referenciada foi excluída ou movida; e o erro `#NOME?` decorre do uso de nome de função incorreto ou texto sem aspas.

@@ a06/s12 | A | item=2.2
A automação de tarefas repetitivas em planilhas eletrônicas pode ser estruturada por meio da gravação de sequências de comandos no aplicativo. No Microsoft Excel 365, acerca de Macros e da linguagem VBA (Visual Basic for Applications), assinale a opção correta.
A) Uma macro é uma rotina automatizada gravada em código VBA, exigindo que a pasta de trabalho seja salva no formato com extensão .xlsm.
B) As macros impedem a execução de comandos com referências relativas, admitindo unicamente o uso de coordenadas rígidas e absolutas.
C) A gravação de macros no Excel dispensa permissões de segurança, executando qualquer código de fontes externas sem restrições ou alertas.
D) O formato padrão de pastas de trabalho do Excel (.xlsx) armazena macros executáveis sem qualquer necessidade de conversão de extensão.
E) As macros em VBA funcionam exclusivamente quando o computador estiver operando desconectado de fontes de alimentação elétrica.
// Comentário: Uma macro no Excel automatiza sequências de ações gerando rotinas em linguagem VBA (Visual Basic for Applications). Por motivos de segurança contra malwares, pastas de trabalho convencionais (.xlsx) não podem conter macros ativas; para preservar o código executável das macros, o arquivo deve ser salvo obrigatoriamente no formato de Pasta de Trabalho Habilitada para Macro do Excel, com extensão `.xlsm`.

@@ a08/s02 | B
A interface visual do processador de textos Microsoft Word 365 estrutura comandos e ferramentas em componentes gráficos dispostos hierarquicamente. A respeito da Faixa de Opções (Ribbon) do Word 365, assinale a opção correta.
A) A Faixa de Opções organiza-se de maneira aleatória a cada abertura do aplicativo, sendo vedada a fixação de guias temáticas.
B) A Faixa de Opções decompõe-se estruturalmente em Guias, Grupos funcionais e Botões de comando, podendo ser recolhida pelo atalho Ctrl + F1.
C) A Faixa de Opções foi completamente suprimida na versão Microsoft 365, sendo substituída por menus em cascata idênticos aos do Word 97.
D) O atalho de teclado Ctrl + F1 atua deletando o primeiro parágrafo de texto selecionado no documento em edição no aplicativo.
E) A personalização da Faixa de Opções do Word altera de maneira compulsória a disposição dos botões na área de trabalho do Windows 11.
// Comentário: A Faixa de Opções (Ribbon) do Word organiza-se em três níveis hierárquicos: Guias (como Página Inicial, Inserir, Layout, Referências), subdivididas em Grupos temáticos (Fonte, Parágrafo, Estilos) contendo os Botões e comandos de ação. O atalho Ctrl + F1 permite alternar rapidamente entre recolher e reexibir a Faixa de Opções.

@@ a08/s02 | A
O acesso rápido a ferramentas frequentemente empregadas durante a redação de relatórios e documentos oficiais agiliza o trabalho do usuário. No Microsoft Word 365, acerca da Barra de Ferramentas de Acesso Rápido, assinale a opção correta.
A) A Barra de Ferramentas de Acesso Rápido é personalizável e reúne atalhos para ações frequentes, podendo situar-se acima ou abaixo da Faixa de Opções.
B) A Barra de Ferramentas de Acesso Rápido possui comandos imutáveis fixados em fábrica, sendo impossível adicionar novos botões de atalho.
C) A Barra de Ferramentas de Acesso Rápido localiza-se obrigatoriamente no rodapé do documento, imediatamente ao lado da contagem de palavras.
D) A inclusão de botões na Barra de Ferramentas de Acesso Rápido restringe-se a comandos de encerramento imediato do sistema operacional.
E) Os atalhos da Barra de Ferramentas de Acesso Rápido são desativados de forma compulsória sempre que o usuário ativa a numeração de páginas.
// Comentário: A Barra de Ferramentas de Acesso Rápido situa-se tradicionalmente na parte superior da janela (ou pode ser posicionada logo abaixo da Faixa de Opções) e disponibiliza acesso a comandos corriqueiros com um clique (como Salvar, Desfazer, Refazer e Impressão Rápida). O usuário pode personalizá-la livremente adicionando qualquer comando da Faixa de Opções.

@@ a10/s03 | E
No Microsoft PowerPoint 365, o gerenciamento de tarefas estruturadas relativas ao arquivo em sua totalidade ocorre em uma interface específica acessível na Faixa de Opções. Com relação à Guia Arquivo (Modo Backstage), assinale a opção correta.
A) O Modo Backstage destina-se unicamente a aplicar transições de tela com efeitos tridimensionais avançados entre slides consecutivos.
B) A Guia Arquivo pode ser livremente renomeada, ocultada e reposicionada pelo usuário na Faixa de Opções por meio do menu de opções.
C) O acionamento da Guia Arquivo acarreta a exclusão imediata de todos os comentários inseridos por revisores na apresentação ativa.
D) O Modo Backstage é incompatível com o salvamento de documentos na nuvem, operando exclusivamente com gravação em fitas magnéticas.
E) A Guia Arquivo abre o Modo Backstage, reunindo opções de gerenciamento geral como Salvar Como, Imprimir, Exportar e Informações.
// Comentário: Ao clicar na guia Arquivo no PowerPoint, o usuário acessa a exibição Backstage, dedicada às operações de gestão do documento em nível global: Salvar, Salvar Como, Abrir, Fechar, Informações (propriedades, proteção e inspeção de apresentação), Imprimir, Compartilhar e Exportar (para PDF, XPS ou vídeo). A guia Arquivo constitui exceção nas opções de personalização da Faixa de Opções, não podendo ser reposicionada ou desativada.

@@ a10/s03 | D
A organização e a inclusão de novas telas durante a montagem de uma apresentação no Microsoft PowerPoint 365 são efetuadas por comandos da guia principal. Na guia Página Inicial, no que se refere ao grupo Slides, assinale a opção correta.
A) O comando Novo Slide atua convertendo automaticamente arquivos de áudio em formato texto com reconhecimento óptico de caracteres.
B) O atalho de teclado utilizado pelo comando Novo Slide para incluir um diapositivo na apresentação corresponde à combinação Ctrl + N.
C) O botão Layout destina-se exclusivamente a alterar as dimensões físicas dos monitores de vídeo acoplados à estação de trabalho.
D) O comando Novo Slide insere um slide na apresentação (atalho Ctrl + M), e o comando Layout altera a disposição de seus espaços reservados.
E) O grupo Slides impede a redefinição de formatos de apresentação, exigindo o reinício do computador para reposicionar caixas de texto.
// Comentário: No grupo Slides da guia Página Inicial do PowerPoint, o comando "Novo Slide" (atalho `Ctrl + M`, lembrando que `Ctrl + N` abre uma nova apresentação em branco) insere um novo diapositivo, enquanto o comando "Layout" permite alterar a distribuição dos espaços reservados (título, conteúdo, duas colunas) do slide ativo. O grupo abriga ainda os botões "Redefinir" e "Seção".

@@ a10/s03 | D
A padronização tipográfica e a hierarquia visual dos textos em diapositivos demandam a utilização precisa de ferramentas de formatação. No PowerPoint 365, quanto aos grupos Fonte e Parágrafo da guia Página Inicial, assinale a opção correta.
A) O grupo Fonte permite alterar exclusivamente a cor do plano de fundo da apresentação inteira, sem atuar sobre letras digitadas.
B) O comando Limpar Toda a Formatação converte automaticamente o texto selecionado em uma imagem vetorial com extensão SVG.
C) O grupo Parágrafo é restrito a apresentações acadêmicas em língua estrangeira, sendo desativado em arquivos corporativos locais.
D) Os grupos Fonte e Parágrafo disponibilizam ajustes de tipografia, espaçamento entrelinhas, alinhamento, listas com marcadores e colunas.
E) O recurso de alinhamento justificado foi suprimido do PowerPoint 365, sendo obrigatório o alinhamento centralizado em todos os blocos.
// Comentário: Na guia Página Inicial do PowerPoint, o grupo Fonte concentra os comandos de tipografia (família de fontes, tamanho, negrito, itálico, sublinhado, sombra de texto, espaçamento entre caracteres e cor da fonte). O grupo Parágrafo, por sua vez, abriga controles de alinhamento horizontal e vertical, espaçamento entre linhas, divisão em colunas, direção do texto e listas com marcadores ou numeração.

@@ a10/s03 | E
A composição de telas explicativas frequentemente requer a inclusão rápida de elementos geométricos, setas de fluxo e realces gráficos na apresentação. No Microsoft PowerPoint 365, a respeito do grupo Desenho presente na guia Página Inicial, assinale a opção correta.
A) O grupo Desenho limita-se a calcular a velocidade de rotação do ventilador da placa de vídeo do computador do usuário.
B) As ferramentas do grupo Desenho operam unicamente quando o arquivo é salvo no formato de modelo do PowerPoint com extensão .potx.
C) O comando Organizar presente no grupo Desenho destina-se exclusivamente a reordenar a lista de contatos de correio eletrônico.
D) O grupo Desenho impede a alteração de cores de preenchimento de formas vetoriais, impondo a cor preta em todos os diagramas.
E) O grupo Desenho permite inserir formas geométricas, organizar a sobreposição de objetos e aplicar estilos rápidos de preenchimento e contorno.
// Comentário: Presente na guia Página Inicial para garantir agilidade na elaboração de slides sem necessidade de alternar para a guia Inserir, o grupo Desenho permite selecionar e desenhar formas geométricas (retângulos, círculos, setas, linhas), organizar a ordem de sobreposição visual (Avançar, Recuar, Trazer para a Frente), alinhar, agrupar objetos e aplicar Estilos Rápidos de preenchimento e contorno de forma.

@@ a10/s03 | E
Em apresentações institucionais extensas compostas por dezenas ou centenas de slides, a estruturação do material em blocos temáticos facilita o trabalho dos relatores. Acerca do recurso de Seções no PowerPoint 365, assinale a opção correta.
A) A criação de seções bloqueia a exibição de slides em tela cheia, impedindo que a apresentação seja projetada com equipamentos multimídia.
B) O recurso de seções é restrito a apresentações de diapositivo único, sendo vedado em arquivos com mais de duas telas cadastradas.
C) As seções impedem que múltiplos autores trabalhem na mesma apresentação em serviços de coautoria na nuvem do Microsoft 365.
D) O gerenciamento de seções exige a digitação de códigos matemáticos em janelas de depuração de programas do sistema operacional.
E) O recurso de seções permite agrupar e nomear conjuntos de slides, facilitando a organização, navegação e recolhimento de blocos temáticos.
// Comentário: O recurso Seções (adicionado pelo comando Seção no grupo Slides da guia Página Inicial ou clicando com o botão direito entre slides no painel de miniaturas) permite segmentar uma apresentação longa em partes lógicas nomeadas (por exemplo: Introdução, Metodologia, Resultados, Conclusão). Isso permite expandir e recolher blocos inteiros, aplicar ações em lote e organizar o fluxo de trabalho.

@@ a10/s03 | C
A localização rápida de palavras-chave e a substituição padronizada de termos técnicos ao longo de toda a apresentação são agilizadas por comandos específicos da interface. No PowerPoint 365, em relação ao grupo Edição na guia Página Inicial, assinale a opção correta.
A) O comando Localizar atua desinstalando aplicativos secundários do sistema operacional para liberar memória em apresentações pesadas.
B) O atalho de teclado padronizado no PowerPoint em português para acionar o comando Localizar corresponde à combinação Ctrl + F.
C) O grupo Edição reúne os comandos Localizar (Ctrl + L), Substituir (Ctrl + U) e Selecionar, incluindo o acesso ao Painel de Seleção.
D) O comando Substituir veda a substituição simultânea de todas as ocorrências de um termo, exigindo confirmações manuais individuais.
E) O Painel de Seleção destina-se unicamente a selecionar certificados digitais expirados armazenados no navegador de Internet.
// Comentário: No grupo Edição da guia Página Inicial do PowerPoint (versão em português do Brasil), encontram-se as ferramentas de busca e manipulação de texto e objetos: Localizar (atalho `Ctrl + L`), Substituir (atalho `Ctrl + U`) e o menu Selecionar, que inclui o Painel de Seleção (recurso essencial para visualizar, renomear, ocultar ou reordenar a sequência de sobreposição de elementos no slide).

@@ a10/s05 | D
A exibição de uma apresentação perante o público pode ser conduzida a partir do diapositivo inaugural ou de pontos intermediários da explanação. No Microsoft PowerPoint 365, na guia Apresentação de Slides, assinale a opção correta.
A) O comando Do Começo é acionado pelo atalho de teclado F1, enquanto a apresentação a partir do slide atual utiliza a combinação Alt + F4.
B) A execução de uma apresentação a partir do slide ativo é realizada obrigatoriamente pressionando-se a tecla Enter com o mouse desconectado.
C) A guia Apresentação de Slides veda a personalização de sequências de exibição, impondo a projeção linear e contínua de todos os slides.
D) O comando Do Começo inicia a projeção pelo primeiro slide (atalho F5), enquanto Do Slide Atual inicia pelo ativo (atalho Shift + F5).
E) A exibição em tela cheia de uma apresentação desativa permanentemente todas as animações e vídeos inseridos nos diapositivos.
// Comentário: Na guia Apresentação de Slides, os dois modos fundamentais de disparo são: "Do Começo" (que inicia a projeção em tela inteira a partir do primeiro slide, acionado pela tecla `F5`) e "Do Slide Atual" (que inicia a projeção a partir do slide selecionado na edição, acionado pelo atalho `Shift + F5`). A guia permite ainda configurar Apresentações Personalizadas para exibir apenas um subconjunto selecionado de diapositivos.

@@ a10/s05 | D
O controle prévio do tempo disponível para palestras e conferências requer a simulação precisa da duração gasta na explanação de cada tela. Com relação aos recursos de configuração da guia Apresentação de Slides no PowerPoint 365, assinale a opção correta.
A) O recurso Testar Intervalos impede que o apresentador avance os slides manualmente com o mouse durante a conferência de tempos.
B) A configuração de apresentação em quiosque (tela inteira) exige a presença obrigatória de dois operadores humanos ao lado da tela.
C) A gravação de intervalos em slides desativa os botões de controle de volume em equipamentos multimídia conectados por cabo HDMI.
D) O comando Testar Intervalos permite cronometrar o tempo de cada slide e gravar as temporizações para avanço automático na apresentação.
E) A reprodução de narrações e ponteiros laser durante a projeção é proibida pelas configurações padrão da suíte Microsoft Office.
// Comentário: O recurso "Testar Intervalos" (grupo Configurar da guia Apresentação de Slides) abre a apresentação com uma barra de cronômetro, registrando o tempo dedicado a cada diapositivo. Ao final, o PowerPoint oferece a opção de salvar essas temporizações para que a apresentação avance automaticamente nos tempos exatos cronometrados.

@@ a10/s05 | C
A revisão ortográfica rigorosa e a inserção de notas colaborativas constituem etapas essenciais antes do fechamento de materiais institucionais. No PowerPoint 365, a respeito dos recursos da guia Revisão, assinale a opção correta.
A) O comando Verificar Ortografia atua inserindo senhas de bloqueio de edição em documentos que contiverem erros gramaticais graves.
B) O atalho de teclado padronizado no PowerPoint para disparar a ferramenta de verificação ortográfica corresponde à combinação Ctrl + F7.
C) A guia Revisão reúne ferramentas de revisão textual, incluindo Verificar Ortografia (atalho F7), Dicionário de Sinônimos e Comentários.
D) A ferramenta de tradução da guia Revisão restringe-se a converter algarismos arábicos em números romanos sem traduzir vocábulos.
E) A inclusão de comentários na guia Revisão altera permanentemente o texto das caixas de diálogo dos slides projetados à plateia.
// Comentário: Na guia Revisão do PowerPoint, o usuário dispõe de recursos de checagem linguística e colaboração: "Verificar Ortografia" (acionado pela tecla `F7`), "Dicionário de Sinônimos", verificação de Acessibilidade, Tradução e o gerenciamento de Comentários (inserção, resposta, exclusão e exibição de anotações colaborativas que não aparecem na projeção final).

@@ a10/s05 | D
A padronização visual corporativa exige que elementos de cabeçalho, logotipos oficiais, paletas de cores e fontes sejam uniformizados em toda a apresentação. No Microsoft PowerPoint 365, na guia Exibir, assinale a opção que indica o recurso responsável por controlar essa estrutura global.
A) Modos de Exibição de Leitura, disponível no grupo Zoom da referida guia.
B) Painel de Tarefas de Desenho, situado no grupo Janela da interface gráfica.
C) Linhas de Grade e Guias, localizadas no grupo Mostrar do aplicativo.
D) Slide Mestre, situado no grupo Modos de Exibição Mestres da guia Exibir.
E) Painel de Notas do Orador, pertencente ao grupo Cores e Escala de Cinza.
// Comentário: O Slide Mestre (acessível na guia Exibir > grupo Modos de Exibição Mestres) é o slide principal de modelo que armazena informações sobre o tema, fontes, cores, efeitos, tamanhos e posições dos espaços reservados de toda a apresentação. Qualquer elemento inserido no Slide Mestre (como o brasão da instituição ou logotipo no topo) é automaticamente replicado em todos os slides e layouts a ele vinculados, garantindo uniformidade e facilidade de manutenção.
"""
