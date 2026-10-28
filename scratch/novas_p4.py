NOVAS_P4 = """
@@ a12/s01 | D
No projeto estrutural dos sistemas operacionais modernos, a separação de camadas entre o usuário, as aplicações e os componentes físicos garante a estabilidade operacional da máquina. No que se refere às funções do núcleo (kernel) e da interface (shell) no Windows 11, assinale a opção correta.
A) O shell atua como o componente responsável por gerenciar diretamente a alocação física de memória RAM e os ciclos de processamento da CPU.
B) O kernel consiste unicamente em uma interface visual de janelas destinada a receber cliques do mouse e comandos digitados pelo usuário.
C) Os drivers de dispositivos operam como periféricos mecânicos externos, dispensando qualquer integração de software com o sistema operacional.
D) O kernel gerencia os recursos de hardware, processos e memória, enquanto o shell atua como a interface de interpretação de comandos do usuário.
E) A ocorrência de falhas graves de execução no shell bloqueia permanentemente o acesso ao disco rígido, exigindo a substituição física da placa-mãe.
// Comentário: No Windows 11, o kernel constitui o núcleo essencial do sistema operacional encarregado da gerência de baixo nível dos recursos de hardware (processamento, alocação de memória RAM e comunicação com periféricos via drivers), ao passo que o shell (como a interface gráfica do Explorer ou os interpretadores PowerShell e Prompt de Comando) atua como camada intermediária que recebe, interpreta e encaminha os comandos do usuário ao núcleo.

@@ a12/s01 | E
Para assegurar níveis elevados de desempenho, estabilidade e segurança criptográfica, a Microsoft estabeleceu parâmetros rígidos de hardware para a instalação do Windows 11. A respeito dos requisitos mínimos oficiais para a implantação desse sistema operacional, assinale a opção correta.
A) O sistema operacional mantém compatibilidade plena e nativa com processadores legados de arquitetura exclusiva de 32 bits.
B) A quantidade mínima exigida de memória RAM para a operação básica do sistema operacional é de 512 megabytes.
C) O espaço mínimo em disco rígido ou unidade de estado sólido exigido para instalação é de 16 gigabytes.
D) A inicialização do computador dispensa o suporte a firmware UEFI, admitindo o padrão de BIOS herdado da década de 1980 sem restrições.
E) O sistema exige processador compatível de 64 bits a 1 GHz ou superior, 4 GB de memória RAM, 64 GB de armazenamento e módulo TPM 2.0.
// Comentário: Os requisitos mínimos de hardware para instalação do Windows 11 englobam: processador compatível de 64 bits (não havendo mais suporte para arquiteturas de 32 bits) com frequência mínima de 1 GHz e 2 ou mais núcleos; 4 gigabytes de memória RAM; 64 gigabytes de espaço de armazenamento disponível; firmware do sistema compatível com UEFI e Inicialização Segura (Secure Boot); além do módulo de plataforma confiável TPM (Trusted Platform Module) versão 2.0.

@@ a12/s01 | E
O Windows 11 é comercializado em diferentes edições adaptadas a perfis específicos de uso corporativo e pessoal. Quanto às diferenças de recursos nativos entre as edições Windows 11 Home e Windows 11 Pro, assinale a opção correta.
A) A edição Home inclui suporte nativo a até dois processadores físicos na mesma placa-mãe e gerencia até 2 terabytes de memória RAM.
B) A edição Pro desativa por completo o acesso à loja de aplicativos da Microsoft e impede a navegação na Internet via protocolo HTTPS.
C) A ferramenta de criptografia de unidade BitLocker é disponibilizada como recurso padrão e exclusivo da edição Home do sistema operacional.
D) A edição Home permite configurar a máquina local como servidora para hospedar conexões de entrada da Área de Trabalho Remota.
E) A edição Pro oferece recursos corporativos avançados, como a criptografia de disco BitLocker, o Hyper-V e a edição de Políticas de Grupo.
// Comentário: A edição Windows 11 Pro é direcionada ao ambiente corporativo e profissional, trazendo funcionalidades que não integram a edição Home, tais como a criptografia de unidade BitLocker, o hipervisor Hyper-V para virtualização, o Editor de Política de Grupo Local (gpedit.msc) e a capacidade de atuar como computador host (servidor de entrada) para conexões da Área de Trabalho Remota (RDP). A edição Home atua apenas como cliente da Área de Trabalho Remota e possui limites de hardware inferiores.

@@ a12/s01 | C
Lançado com uma interface reformulada e foco no aumento da produtividade do trabalho híbrido, o Windows 11 introduziu diversos recursos nativos inexistentes em versões anteriores. Com base nas inovações introduzidas pelo Windows 11, assinale a opção correta.
A) A barra de tarefas tornou obrigatória a fixação rígida de todos os ícones e do menu Iniciar no canto superior direito da tela do computador.
B) O recurso Snap Layouts foi extinto para impedir que o usuário visualize simultaneamente duas ou mais janelas abertas no monitor.
C) O sistema introduziu o recurso Snap Layouts para organização rápida de janelas e o assistente de inteligência artificial Copilot integrado.
D) O sistema operacional abandonou o suporte à exibição de papéis de parede, permitindo unicamente telas em cor preta fosca uniforme.
E) A comunicação via Microsoft Teams foi bloqueada no sistema operacional, sendo restrita ao acesso por navegadores de terceiros.
// Comentário: Entre as principais inovações do Windows 11 destacam-se a nova interface com menu Iniciar centralizado, o recurso Snap Layouts (que permite organizar rapidamente janelas em arranjos predefinidos ao posicionar o cursor sobre o botão de maximizar ou pressionar Win + Z), a integração do assistente de inteligência artificial Copilot na barra de tarefas, o Modo Foco e a reformulação da Central de Configurações.

@@ a12/s02 | D
Na interface gráfica do Windows 11, a Área de Trabalho e os ícones de atalho facilitam a localização e o acionamento célere de arquivos e aplicativos. No que concerne aos atalhos e sua estrutura no sistema operacional, assinale a opção correta.
A) A exclusão de um atalho posicionado na Área de Trabalho acarreta a destruição definitiva e irreversível do arquivo ou aplicativo original.
B) Um atalho copia integralmente todo o código-fonte e o banco de dados do programa original, ocupando centenas de gigabytes em disco.
C) Os atalhos no Windows são identificados pela extensão obrigatória .exe e exibem uma imagem idêntica à de pastas compactadas em formato zip.
D) O atalho é um arquivo leve com extensão .lnk que armazena o caminho de referência para o item original, sem conter seus dados reais.
E) A cópia de um arquivo de atalho para um dispositivo removível transfere automaticamente o programa original instalado no sistema.
// Comentário: Um atalho no Windows é identificado pela extensão `.lnk` e visualmente por uma pequena seta sobreposta ao ícone. Trata-se de um arquivo muito leve que contém apenas a referência (caminho de destino) para o arquivo, pasta ou aplicativo original. Dessa forma, apagar o atalho não exclui o arquivo de destino, e apagar o item original corrompe o funcionamento do atalho.

@@ a12/s02 | E
A personalização visual do Windows 11 possibilita adaptar o ambiente de trabalho às preferências funcionais e necessidades ergonômicas de cada usuário. Acerca dos recursos de Personalização e Acessibilidade do Windows 11, assinale a opção correta.
A) A tela de fundo da Área de Trabalho aceita exclusivamente imagens estáticas em formato BMP gravadas em discos óticos regraváveis.
B) A alteração para o modo escuro do sistema operacional exige a formatação completa do disco rígido e nova instalação do Windows.
C) Os temas visuais oficiais da Microsoft impedem a alteração das cores de destaque das janelas e dos ponteiros do mouse.
D) A configuração de apresentação de slides na tela de fundo foi suprimida no Windows 11, admitindo apenas cores cinzas neutras.
E) O sistema oferece temas de contraste para facilitar a leitura por pessoas com sensibilidade à luz ou baixa visão, como Aquáticos e Deserto.
// Comentário: No Windows 11, as opções de Personalização permitem escolher como tela de fundo uma imagem individual, uma cor sólida ou uma apresentação de slides periódica. Para usuários com baixa visão ou sensibilidade à luz, o sistema disponibiliza na seção de Acessibilidade temas de contraste dedicados (como Aquáticos, Deserto, Entardecer e Céu Noturno), além de permitir alternar livremente entre modo claro, modo escuro e esquemas personalizados.

@@ a12/s02 | B
A Barra de Tarefas do Windows 11 desempenha papel central no gerenciamento de programas ativos e na organização do fluxo de trabalho diário. A respeito das características e atalhos da Barra de Tarefas e das Áreas de Trabalho Virtuais, assinale a opção correta.
A) O Windows 11 impede terminantemente que os ícones da barra de tarefas sejam alinhados à esquerda da tela pelo usuário.
B) A criação instantânea de uma nova Área de Trabalho Virtual pode ser executada por meio do atalho de teclado Windows + Ctrl + D.
C) A Barra de Tarefas foi convertida em um serviço exclusivo de gestão de tarefas acadêmicas, não exibindo mais janelas minimizadas.
D) A área de notificação da Barra de Tarefas foi suprimida no Windows 11, inviabilizando o ajuste rápido de conexões Wi-Fi e volume de som.
E) O botão Visão de Tarefas destina-se unicamente a formatar partições de inicialização do disco rígido sem confirmação do usuário.
// Comentário: O Windows 11 permite organizar o fluxo de trabalho em múltiplos desktops virtuais, cuja criação rápida é acionada pelo atalho `Windows + Ctrl + D` (e a alternância entre eles por `Windows + Ctrl + Seta para Esquerda/Direita`). Além disso, embora os ícones da Barra de Tarefas venham centralizados por padrão, o usuário pode configurar o alinhamento de volta à esquerda nas configurações de comportamento da Barra de Tarefas.

@@ a12/s02 | C
O painel de Widgets do Windows 11 foi concebido para entregar informações relevantes e dinâmicas de maneira ágil sem demandar a abertura constante de navegadores web. No que concerne aos Widgets do Windows 11, assinale a opção correta.
A) Os Widgets exigem que o computador opere sem conexão à Internet, operando unicamente com dados pré-instalados na placa de vídeo.
B) O acesso ao painel de Widgets do Windows 11 é viabilizado exclusivamente por comandos de depuração executados no Prompt de Comando.
C) O painel de Widgets pode ser aberto pelo atalho Windows + W e apresenta cartões dinâmicos como previsão do tempo, calendário e notícias.
D) A remoção de widgets da tela do computador desinstala permanentemente o pacote de drivers de rede sem fio da estação de trabalho.
E) O painel de Widgets permanece obrigatoriamente afixado no centro da Área de Trabalho, cobrindo todos os ícones de pastas do usuário.
// Comentário: No Windows 11, o painel de Widgets desliza na lateral da tela ao ser acionado pelo ícone na barra de tarefas ou pelo atalho de teclado `Windows + W`. Ele reúne blocos dinâmicos com dados em tempo real (como clima, trânsito, tarefas do Microsoft To Do, compromissos do calendário e cotações financeiras), acompanhados por um feed de notícias personalizável (Microsoft Start).

@@ a12/s02 | C
Durante a organização de pastas e documentos na Área de Trabalho do Windows 11, o usuário frequentemente manipula itens de dados e referências de acesso. Em relação ao gerenciamento de ícones, arquivos e atalhos na Área de Trabalho, assinale a opção correta.
A) A criação de um atalho para um documento sigiloso altera automaticamente suas permissões de segurança para acesso irrestrito na rede.
B) O comando Atualizar do menu de contexto da Área de Trabalho atua reiniciando o computador e apagando a memória cache da CPU.
C) Um item excluído da Área de Trabalho por meio da tecla Delete é direcionado para a Lixeira, podendo ser restaurado à sua posição original.
D) A alteração do ícone gráfico de um atalho modifica irreversivelmente o arquivo executável original hospedado na pasta de programas.
E) O tamanho de exibição dos ícones na Área de Trabalho é padronizado e imutável pelo usuário, não admitindo ícones médios ou grandes.
// Comentário: Quando um arquivo ou pasta armazenado na Área de Trabalho (unidade local) é excluído com a tecla `Delete` (ou clicando no botão Excluir da barra de comandos), ele é enviado para a Lixeira, permitindo sua recuperação para a pasta de origem por meio do comando "Restaurar". Por outro lado, a alteração visual do ícone associado a um atalho `.lnk` afeta somente as propriedades gráficas daquele atalho, sem modificar o arquivo executável ou documento original.

@@ a12/s04 | B
A interface do Explorador de Arquivos no Windows 11 passou por transformações arquiteturais para aprimorar a usabilidade e a navegação entre múltiplos diretórios. A respeito da navegação por abas no Explorador de Arquivos, assinale a opção correta.
A) A abertura de novas abas no Explorador de Arquivos foi suprimida no Windows 11, impondo a abertura de uma nova janela para cada diretório.
B) O usuário pode abrir uma nova aba de navegação na mesma janela por meio do atalho Ctrl + T e fechar a aba ativa pelo atalho Ctrl + W.
C) O fechamento de uma aba de navegação encerra compulsoriamente a conexão de rede local e desliga a fonte de energia da máquina.
D) As abas do Explorador de Arquivos são incompatíveis com o sistema de arquivos NTFS, funcionando exclusivamente em discos no formato FAT16.
E) A navegação por abas restringe o acesso de pastas a no máximo dois cliques por minuto por determinação dos protocolos de segurança.
// Comentário: Uma das principais inovações do Explorador de Arquivos no Windows 11 foi a introdução do suporte nativo a abas na mesma janela (semelhante aos navegadores web), permitindo navegar por diferentes pastas sem acumular múltiplas janelas na tela. O comando para abrir uma nova guia é `Ctrl + T` e para fechar a guia atual é `Ctrl + W`.

@@ a12/s04 | A
O gerenciamento ergonômico de janelas de programas no Windows 11 envolve o uso de botões de controle e comandos rápidos de teclado. Acerca dos botões de controle da barra de título e seus atalhos correspondentes, assinale a opção correta.
A) O comando Minimizar recolhe a janela ativa para a barra de tarefas, e o atalho Alt + F4 encerra o programa ou a janela em execução.
B) O comando Maximizar exclui permanentemente o arquivo ativo do disco rígido e desativa o suporte a placas de vídeo integradas.
C) O atalho Alt + Espaço bloqueia o sistema operacional e reinicia a placa-mãe em modo de segurança com rede ativada.
D) O botão Fechar atua salvando automaticamente cópias duplicadas do documento ativo em todos os servidores públicos da Internet.
E) A combinação de teclas Windows + Seta para Cima fecha a janela ativa e envia todos os dados da memória RAM para a Lixeira.
// Comentário: Na barra de título das janelas no Windows, os botões de controle realizam ações sobre a visualização da aplicação: "Minimizar" recolhe a janela para a Barra de Tarefas mantendo o programa em execução; "Maximizar" expande a janela para ocupar toda a tela (atalho `Windows + Seta para Cima`); "Restaurar" recupera as dimensões intermediárias anteriores; e "Fechar" encerra o aplicativo ou janela ativa (atalho `Alt + F4`).

@@ a12/s04 | A
A barra de comandos do Explorador de Arquivos do Windows 11 foi simplificada visualmente em relação à antiga Faixa de Opções (Ribbon) do Windows 10. No que se refere às ferramentas presentes na barra de comandos do Windows 11, assinale a opção correta.
A) A barra de comandos reúne botões de ação frequente, como Novo, Recortar, Copiar, Colar, Renomear, Compartilhar e Excluir.
B) O comando Novo atua exclusivamente formatando unidades físicas de disco rígido para limpeza de dados confidenciais do usuário.
C) O botão Excluir remove arquivos de forma direta e definitiva, sem qualquer possibilidade de retenção temporária na Lixeira.
D) A barra de comandos veda a classificação de arquivos por data ou tamanho, permitindo apenas a listagem por ordem decrescente de pixels.
E) O menu de reticências (···) destina-se unicamente a calibrar a saturação de cor dos monitores analógicos acoplados à máquina.
// Comentário: No Windows 11, a Faixa de Opções Ribbon do Explorador de Arquivos foi substituída por uma barra de comandos compacta e moderna, contendo ícones rápidos para operações rotineiras (Novo para criar pastas/arquivos, Recortar, Copiar, Colar, Renomear [F2], Compartilhar, Excluir [Delete], Classificar e Exibir), além do botão de reticências (···) que concede acesso a opções avançadas, como Propriedades e Selecionar Tudo.

@@ a12/s04 | E
A localização precisa de diretórios e arquivos no Explorador de Arquivos do Windows 11 apoia-se na barra de endereços e nas ferramentas de histórico de navegação. A respeito da navegação por pastas no Explorador de Arquivos, assinale a opção correta.
A) O botão Voltar sempre redireciona o usuário para a pasta raiz da unidade de disco, independentemente do histórico recente de visitas.
B) A barra de endereços exibe caminhos exclusivamente em código binário numérico, sendo impossível clicar nos nomes das pastas intermediárias.
C) O atalho de teclado padronizado para selecionar a barra de endereços e digitar um caminho direto de pasta corresponde a Ctrl + Z.
D) O botão Acima conduz o usuário à pasta acessada anteriormente no histórico de navegação, dispensando a relação hierárquica de pastas.
E) A barra de endereços exibe o caminho em formato de migalhas de pão (breadcrumbs), e o botão Acima sobe um nível na estrutura de diretórios.
// Comentário: A barra de endereços do Explorador de Arquivos adota o padrão de migalhas de pão (*breadcrumbs*), permitindo clicar em qualquer pasta intermediária da cadeia ou usar `Alt + D` / `Ctrl + L` para digitar caminhos diretamente. No que tange à navegação: o botão "Voltar" (atalho `Backspace` ou `Alt + Seta Esquerda`) retorna à última pasta efetivamente visitada no histórico; já o botão "Acima" (`Alt + Seta Acima`) sobe exatamente um nível hierárquico na árvore de diretórios em direção à pasta-mãe.

@@ a12/s05 | A
O Explorador de Arquivos do Windows 11 disponibiliza painéis modulares projetados para conferir visibilidade estrutural, prévia de conteúdos e metadados de arquivos. A respeito dos painéis do Explorador de Arquivos, assinale a opção correta.
A) O Painel de Navegação fica à esquerda com a árvore de pastas, enquanto os painéis de Visualização e Detalhes ocupam o lado direito.
B) Os painéis de Detalhes e de Visualização podem ser exibidos simultaneamente no mesmo lado da tela, dividindo a lateral direita ao meio.
C) O Painel de Visualização exibe a íntegra dos dados criptografados de arquivos compactados no formato .zip sem necessidade de descompactação.
D) O Painel de Navegação impede que o usuário fixe pastas personalizadas na seção de Acesso Rápido para consulta frequente.
E) O Painel de Detalhes mostra uma prévia interativa do conteúdo do documento, enquanto o Painel de Visualização mostra apenas metadados técnicos.
// Comentário: No Explorador de Arquivos, o Painel de Navegação situa-se na lateral esquerda, exibindo o Acesso Rápido, o OneDrive, Este Computador e as redes. Na lateral direita, o usuário pode habilitar (via menu Exibir > Mostrar) ou o "Painel de Visualização" (que mostra a prévia do conteúdo do arquivo selecionado sem abri-lo) ou o "Painel de Detalhes" (que exibe as propriedades e metadados do item, como tamanho, autor e datas). Como compartilham o mesmo espaço, Detalhes e Visualização são mutuamente exclusivos (não coexistem simultaneamente), e arquivos compactados (.zip) não exibem prévia no Painel de Visualização.

@@ a12/s05 | A
A transição ágil entre múltiplos aplicativos e tarefas concorrentes no Windows 11 é viabilizada por diferentes atalhos de teclado de alternância. Quanto aos atalhos de alternância de janelas no Windows 11, assinale a opção correta.
A) O atalho Alt + Tab exibe miniaturas das janelas abertas para alternância, enquanto Win + Tab abre a interface da Visão de Tarefas.
B) O atalho Alt + Esc abre a Central de Segurança do Windows Defender para execução de varredura completa contra códigos maliciosos.
C) A combinação de teclas Win + Tab fecha imediatamente todas as janelas ativas sem salvar as modificações feitas pelos usuários.
D) O atalho Ctrl + Alt + Tab desliga o monitor de vídeo do computador para preservar o consumo elétrico da placa gráfica.
E) A alternância de janelas pelo comando Alt + Tab é restrita a navegadores web, sendo vedada a exibição de programas de edição de texto.
// Comentário: No Windows 11, o comando `Alt + Tab` exibe uma grade com miniaturas visuais das janelas e tarefas em execução, permitindo ao usuário navegar entre elas e focar o aplicativo desejado ao soltar as teclas. O atalho `Win + Tab` abre a "Visão de Tarefas", exibindo as janelas abertas e as Áreas de Trabalho Virtuais. Por sua vez, `Alt + Esc` cicla diretamente entre as janelas na ordem em que foram abertas, sem exibir painel de miniaturas na tela, e `Ctrl + Alt + Tab` fixa a tela de miniaturas para seleção sem necessidade de manter teclas pressionadas.

@@ a12/s05 | E
O Windows 11 aprimorou substancialmente a gestão do espaço útil de telas por meio de arranjos geométricos automatizados conhecidos como recursos de Snap. No que diz respeito aos componentes Snap Layouts, Snap Assist e Snap Groups, assinale a opção correta.
A) O recurso Snap Layouts limita-se a dividir a tela em duas metades verticais idênticas, sendo incapaz de organizar três ou quatro janelas.
B) O Snap Groups consiste em um mecanismo que deleta janelas inativas após dez minutos de repouso operacional do sistema.
C) A utilização de Snap Layouts depende obrigatoriamente da instalação de placas controladoras de vídeo dedicadas ao processamento gráfico 3D.
D) O atalho de teclado que exibe o menu de opções do Snap Layouts na janela em foco corresponde à combinação de teclas Ctrl + Shift + Esc.
E) O Snap Layouts surge ao posicionar o mouse sobre o botão de maximizar (ou via Win + Z), e o Snap Groups lembra o arranjo das janelas.
// Comentário: O Windows 11 introduziu melhorias expressivas na organização de janelas: o "Snap Layouts" exibe modelos gráficos prontos para dividir a tela em duas, três ou quatro partes (acionado ao repousar o cursor do mouse sobre o botão de maximizar ou pressionando o atalho `Win + Z`); o "Snap Assist" sugere de forma inteligente quais outras janelas abertas devem preencher os espaços vagos restantes; e o "Snap Groups" memoriza o conjunto de janelas emparelhadas, permitindo restaurar todo o grupo com um único clique na barra de tarefas.

@@ a12/s05 | C
No Windows 11, o comportamento de comandos tradicionais de sistema pode ser parametrizado para integrar componentes do navegador web ao fluxo de trabalho nativo. Em relação às configurações de multitarefa e alternância de janelas no Windows 11, assinale a opção correta.
A) O sistema veda expressamente qualquer integração entre a alternância por Alt + Tab e as abas em execução no navegador Microsoft Edge.
B) A desativação do recurso Snap impede que o usuário mova ou arraste janelas pela tela do computador com o cursor do mouse.
C) O usuário pode configurar o sistema para que o atalho Alt + Tab mostre tanto janelas abertas quanto guias individuais do Microsoft Edge.
D) A Visão de Tarefas foi completamente descontinuada no Windows 11, impossibilitando a visualização geral de aplicativos abertos.
E) A fixação de janelas na lateral da tela por atalho de teclado exige o uso exclusivo da combinação Ctrl + Alt + Del seguida da tecla Enter.
// Comentário: Nas Configurações do Windows 11 (Sistema > Multitarefa), o usuário pode personalizar o comportamento do atalho `Alt + Tab` para escolher se ele deve exibir apenas janelas abertas ou também incluir as guias recentes do navegador Microsoft Edge (como mostrar as 3 ou 5 guias mais recentes, ou todas as guias abertas), facilitando a transição entre abas da web e aplicativos locais.

@@ a12/s08 | D
O gerenciamento de energia no Windows 11 disponibiliza diferentes modos de transição operacional para economizar eletricidade e preservar o estado dos programas em execução. Com relação aos estados de energia do Windows 11, assinale a opção correta.
A) O modo Suspender grava todos os dados do usuário no disco rígido e corta totalmente o fornecimento elétrico para a memória RAM.
B) O estado Hibernar mantém a memória RAM permanentemente energizada, consumindo a mesma carga elétrica de um computador em plena atividade.
C) O comando Desligar preserva todos os aplicativos abertos exatamente como estavam para restauração instantânea na próxima inicialização.
D) O modo Suspender mantém o estado na memória RAM com baixo consumo elétrico, enquanto o modo Hibernar salva o estado no disco e desliga o PC.
E) A hibernação é um recurso restrito a computadores do tipo servidor, sendo inexistente em computadores portáteis do tipo notebook.
// Comentário: No Windows 11: no estado "Suspender" (stand-by), o estado das aplicações e documentos abertos permanece armazenado na memória RAM em um estado de baixo consumo de energia, permitindo retomada quase instantânea das atividades; no estado "Hibernar", o conteúdo da memória RAM é salvo no arquivo de hibernação (hiberfil.sys) no disco rígido ou SSD e a máquina é totalmente desligada (consumo zero de energia), restaurando a sessão de trabalho ao ser ligada novamente.

@@ a12/s08 | D
O Windows 11 dispõe de um conjunto de ferramentas de recuperação desenvolvidas para reparar arquivos danificados, reverter falhas de atualização e restaurar o ambiente operacional. No que diz respeito às opções de Recuperação do Windows 11, assinale a opção correta.
A) A opção Retornar permite desfazer uma atualização de recursos do Windows a qualquer momento no prazo improrrogável de até cinco anos.
B) A opção Restaurar o PC apaga compulsoriamente todos os arquivos pessoais, sendo tecnicamente impossível optar por mantê-los.
C) O ambiente de Inicialização Avançada atua unicamente formatando o disco rígido em padrão Linux sem solicitar confirmação ao usuário.
D) A opção Restaurar o PC permite reinstalar o Windows mantendo ou removendo arquivos pessoais, e a opção Retornar reverte atualizações recentes.
E) A recuperação do sistema pelo Windows Update exige a digitação manual de comandos binários em placas de circuito integrado.
// Comentário: Nas opções de Recuperação do Windows 11 (Configurações > Sistema > Recuperação): a ferramenta "Restaurar o PC" reinstala o sistema operacional, dando ao usuário a opção de "Manter meus arquivos" ou "Remover tudo" (embora programas e configurações de sistema sejam removidos em ambos os casos); a opção "Retornar" permite reverter para a versão anterior do Windows após uma atualização de recursos (funcionalidade disponível habitualmente por um período de cerca de 10 dias após a instalação); e a "Inicialização Avançada" reinicia a máquina no Ambiente de Recuperação do Windows (WinRE).

@@ a12/s08 | B
O acesso à distância a estações de trabalho possibilita a realização de suporte técnico, administração remota de sistemas e execução de atividades corporativas descentralizadas. No que tange à Área de Trabalho Remota no Windows 11, assinale a opção correta.
A) A Área de Trabalho Remota do Windows opera exclusivamente por meio de frequências de rádio analógicas moduladas em amplitude (AM).
B) O protocolo utilizado é o RDP, e a capacidade de atuar como computador de destino (host) exige as edições Pro, Enterprise ou Education.
C) A edição Windows 11 Home pode ser acessada e controlada remotamente como máquina servidora sem necessidade de ferramentas de terceiros.
D) As conexões remotas pelo aplicativo Conexão de Área de Trabalho Remota dispensam qualquer autenticação de credenciais ou senhas.
E) O computador remoto acessado pelo protocolo RDP desliga-se de forma irreversível assim que o operador estabelece a conexão à distância.
// Comentário: A Área de Trabalho Remota do Windows utiliza o protocolo RDP (Remote Desktop Protocol). Para que um computador possa receber conexões de entrada (atuar como servidor ou host da Área de Trabalho Remota), é obrigatório que ele possua uma edição corporativa/profissional instalada (Windows 11 Pro, Enterprise ou Education). A edição Windows 11 Home pode apenas atuar como cliente (conectar-se a outras máquinas remotas), mas não aceita conexões de entrada nativas.

@@ a12/s08 | C
A Área de Transferência do Windows 11 foi aprimorada com recursos de armazenamento de múltiplos registros, sincronização na nuvem e painel visual de colagem. Com relação à Área de Transferência no Windows 11, assinale a opção correta.
A) A Área de Transferência do Windows é restrita a reter um único fragmento de texto por vez, descartando o histórico de comandos copiados.
B) O atalho de teclado padronizado para acessar o painel com o histórico da Área de Transferência corresponde à combinação Windows + H.
C) O atalho Windows + V abre o histórico da Área de Transferência, permitindo colar itens anteriores e fixar registros essenciais.
D) A execução do comando Limpar Dados apaga permanentemente todos os registros da Área de Transferência, incluindo os itens fixados pelo usuário.
E) A Área de Transferência armazena exclusivamente textos puros, sendo incompatível com a cópia de imagens e links hipertextuais.
// Comentário: No Windows 11, o histórico da Área de Transferência é acionado pelo atalho `Windows + V`. Esse painel armazena os múltiplos últimos itens copiados (textos, links e imagens). O usuário pode fixar itens importantes no painel, garantindo que eles não sejam descartados pelo limite de rotação nem excluídos ao acionar o botão "Limpar tudo". Além disso, é possível sincronizar os dados copiados entre diferentes dispositivos conectados à mesma conta Microsoft.

@@ a12/s08 | A
A gestão integrada de periféricos sem fio e opções de conectividade à rede no Windows 11 é centralizada no aplicativo de Configurações. Acerca das categorias Bluetooth e Dispositivos e Rede e Internet do Windows 11, assinale a opção correta.
A) A seção Bluetooth e Dispositivos centraliza o pareamento de mouses e fones sem fio, a gestão de impressoras e a reprodução automática.
B) A seção Rede e Internet proíbe expressamente a configuração de adaptadores de rede cabeada Ethernet com endereçamento IP estático.
C) O recurso de Hotspot móvel converte a placa-mãe do computador em uma antena de emissão televisiva de alta frequência analógica.
D) O recurso Modo Avião atua formatando os navegadores de Internet para impedir o acesso a portais de empresas de transporte aéreo.
E) A definição de servidores de VPN no Windows exige a substituição física da placa de rede local por placas de modem discado legado.
// Comentário: No aplicativo Configurações do Windows 11: a categoria "Bluetooth e Dispositivos" concentra o emparelhamento e gerenciamento de periféricos sem fio e com fio (fones, mouses, teclados, câmeras), configuração e filas de impressoras e scanners, além das preferências de Reprodução Automática; enquanto a categoria "Rede e Internet" gerencia conexões cabeadas (Ethernet), sem fio (Wi-Fi), VPN, Proxy, Modo Avião (que desativa comunicações sem fio) e Hotspot Móvel (compartilhamento da conexão do PC com outros dispositivos).
"""
