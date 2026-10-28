"""Part 3: Questions 61 to 86 for informatica
Segments:
- informatica/a04/s03: Q61 to Q66
- informatica/a10/s01: Q67 to Q72
- informatica/a10/s02: Q73 to Q78
- informatica/a10/s04: Q79 to Q86
"""

QUESTOES_P3 = """
@@ a04/s03 | A
O policiamento de tráfego perimetral e a imposição de barreiras lógicas entre redes de diferentes níveis de confiança representam a essência técnica dos firewalls. Em relação à definição e às formas de implementação de um firewall corporativo, assinale a opção correta.
A) Um firewall pode ser implementado exclusivamente em software, em hardware dedicado ou em soluções híbridas combinadas de ambos.
B) Um firewall existe exclusivamente na forma de dispositivos físicos de hardware, sendo inviável sua execução em softwares de estações de trabalho.
C) Um firewall destina-se primordialmente a identificar e eliminar arquivos executáveis contaminados por vírus já residentes no disco rígido.
D) O firewall atua apenas sobre a rede elétrica dos servidores, protegendo centros de dados contra picos e descargas atmosféricas.
E) Um firewall substitui integralmente a necessidade de backups institucionais e de ferramentas de auditoria forense em ambientes corporativos.
// Comentário: A alternativa A está correta, pois o firewall pode ser implementado em software (aplicativos residentes no sistema operacional), em hardware dedicado (appliances corporativos) ou em modelos híbridos combinados. A alternativa B erra ao dizer que existe apenas em hardware. A alternativa C confunde firewall com antivírus. As alternativas D e E trazem assertivas absurdas sobre eletricidade e backups.

@@ a04/s03 | B
A política de segurança perimetral configurada em um firewall dita o comportamento padrão do dispositivo diante de conexões desconhecidas ou não catalogadas. A respeito do modo operacional restritivo (baseado em lista branca), assinale a opção correta.
A) O modo restritivo adota o princípio de que todo tráfego é permitido por padrão, bloqueando apenas as portas e IPs explicitamente proibidos.
B) O modo restritivo bloqueia todo tráfego por padrão, autorizando somente as comunicações expressamente permitidas na política de segurança.
C) O modo restritivo é considerado tecnicamente menos seguro que o modo permissivo, pois aumenta a exposição das portas lógicas do sistema.
D) O modo restritivo dispensa a criação de regras em listas de controle de acesso, operando por adivinhação estatística em redes locais.
E) O modo restritivo é incompatível com ambientes corporativos públicos, sendo restrito a roteadores domésticos sem fio de baixa capacidade.
// Comentário: A alternativa B está correta, pois a política restritiva (lista branca / default deny) bloqueia tudo aquilo que não foi expressamente autorizado, sendo a postura considerada mais segura em segurança da informação (análoga à estrita legalidade da administração pública). A alternativa A define o modo permissivo (lista negra). As alternativas C, D e E contêm afirmações sabidamente erradas.

@@ a04/s03 | C
Em estações de trabalho individuais e computadores corporativos portáteis, soluções defensivas locais atuam para blindar o dispositivo contra explorações externas. No que tange às funcionalidades de um firewall pessoal, assinale a opção correta.
A) O firewall pessoal atua convertendo automaticamente páginas da Web suspeitas em documentos de texto estruturado sem imagens.
B) O firewall pessoal é capaz de desinfectar arquivos corrompidos por ransomware e recuperar chaves privadas perdidas em mídias físicas.
C) O firewall pessoal monitora conexões de entrada e saída da máquina, bloqueando tentativas de invasão e comunicações de backdoors.
D) O firewall pessoal substitui a função dos navegadores de Internet, gerenciando o histórico de cookies e senhas bancárias em nuvem.
E) O firewall pessoal impede a emissão de ondas de rádio em redes móveis 5G, limitando o dispositivo a cabos coaxiais de alta tensão.
// Comentário: A alternativa C está correta, pois o firewall pessoal (como o Windows Defender Firewall) inspeciona o tráfego que entra e sai do host local, protegendo portas lógicas contra varreduras externas e impedindo que backdoors ou trojans enviem dados não autorizados para fora. As alternativas A, B, D e E atribuem papéis alheios ao firewall pessoal.

@@ a04/s03 | D
Os primeiros modelos de firewall surgiram integrados a roteadores de pacotes e baseavam suas decisões em campos básicos dos cabeçalhos dos protocolos de rede. Acerca do filtro de pacotes estático (stateless), assinale a opção correta.
A) O filtro de pacotes estático decifra mensagens de correio eletrônico na camada de aplicação para identificar tentativas sutis de phishing.
B) O filtro de pacotes estático mantém em memória uma tabela contínua de estados que rastreia todo o histórico de cada sessão TCP ativa.
C) O filtro de pacotes estático atua na camada de apresentação do modelo OSI, exigindo tokens criptográficos para validar cada pacote de voz.
D) O filtro de pacotes estático avalia cada pacote isoladamente nas camadas de rede e transporte (IP e portas), sem manter histórico de sessão.
E) O filtro de pacotes estático bloqueia obrigatoriamente qualquer conexão de saída iniciada por usuários internos em navegadores convencionais.
// Comentário: A alternativa D está correta, pois o filtro de pacotes estático (stateless) atua nas camadas 3 (rede) e 4 (transporte), inspecionando cada pacote de forma individual com base em endereços IP de origem/destino e portas lógicas, sem guardar histórico ou estado da conexão (stateful). A alternativa A descreve gateways de aplicação. A alternativa B descreve o filtro stateful (dinâmico). As alternativas C e E trazem concepções distorcidas.

@@ a04/s03 | E
Na arquitetura de redes de centros de processamento de dados, determinados servidores precisam ser acessíveis ao público da Internet, enquanto as bases corporativas internas devem permanecer resguardadas. A respeito do conceito e da finalidade da DMZ (Zona Desmilitarizada), assinale a opção correta.
A) A DMZ é uma área da rede física corporativa totalmente desprovida de regras de proteção e de qualquer firewall perimetral ativo.
B) A DMZ destina-se a abrigar exclusivamente os servidores centrais de banco de dados que contêm informações financeiras ultra-secretas.
C) A DMZ é um protocolo de comunicação sem fio utilizado em sensores biométricos de catracas perimetrais em prédios públicos.
D) A DMZ impede a conexão de internautas a sítios públicos da organização, forçando o atendimento por correspondência postal impressa.
E) A DMZ é uma sub-rede intermediária que isola servidores públicos (como Web e DNS), impedindo que invasões comprometam a rede interna.
// Comentário: A alternativa E está correta, pois a DMZ (Demilitarized Zone) é uma zona de rede intermediária entre a Internet e a rede local privada corporativa, onde são posicionados servidores de serviços públicos (Web, DNS, correio); caso um servidor da DMZ seja invadido, o invasor não ganha acesso direto à rede interna. As alternativas A e B erram sobre a localização e segurança da DMZ. As alternativas C e D são incoerentes com as redes de computadores.

@@ a04/s03 | A
As ferramentas de proteção perimetral e os programas antimalware desempenham papéis complementares, mas distintos, na infraestrutura de segurança cibernética. No que concerne aos limites técnicos de atuação de um firewall, assinale a opção correta.
A) O firewall não é capaz de detectar malwares embutidos no interior de arquivos transmitidos em conexões previamente autorizadas em suas regras.
B) O firewall garante proteção absoluta e infalível contra fraudes de engenharia social aplicadas verbalmente por telefone aos usuários.
C) O firewall tem como objetivo primário monitorar a integridade física de cabos de fibra óptica e emissores laser em redes metropolitanas.
D) O firewall impede de forma autônoma que senhas simples sejam digitadas em estações de trabalho desconectadas de qualquer rede física.
E) O firewall elimina completamente a necessidade de aplicação de patches de segurança e de atualizações nos softwares da rede local.
// Comentário: A alternativa A está correta, pois o firewall convencional valida portas lógicas e endereços IP; se uma conexão for permitida (como o download de um arquivo executável via HTTP na porta 80/443), o firewall tradicional deixará o tráfego passar sem inspecionar o conteúdo interno do arquivo, papel que cabe ao antivírus. As alternativas B, C, D e E extrapolam totalmente o escopo e as capacidades de um firewall.

@@ a10/s01 | B
O Microsoft PowerPoint consolidou-se como a ferramenta mais amplamente utilizada para a confecção e projeção de apresentações visuais no ambiente corporativo e governamental. Quanto ao histórico evolutivo e à origem do PowerPoint, assinale a opção correta.
A) O PowerPoint foi desenvolvido originalmente no início do século XXI pela Google para equipar exclusivamente telefones celulares inteligentes.
B) O PowerPoint foi concebido em 1987 pela empresa Forethought para computadores Macintosh, sendo adquirido logo em seguida pela Microsoft.
C) O PowerPoint foi criado originariamente como um módulo acessório de edição de áudio da IBM para computadores de grande porte (mainframes).
D) O PowerPoint surgiu como um software proprietário desenvolvido pelas Forças Armadas britânicas durante a Primeira Guerra Mundial.
E) O PowerPoint foi lançado inicialmente no ano de 2016 pela Microsoft como aplicativo de código aberto para sistemas operacionais Linux.
// Comentário: A alternativa B está correta, pois o PowerPoint foi criado em 1987 por Robert Gaskins e Dennis Austin na empresa Forethought para a plataforma Apple Macintosh; pouco tempo após o lançamento, a Microsoft adquiriu a Forethought e incorporou o programa à sua suíte de escritório Office. As alternativas A, C, D e E trazem dados históricos manifestamente incorretos.

@@ a10/s01 | C
O lançamento do Microsoft PowerPoint 2013 trouxe alterações significativas na identidade visual padrão dos documentos e na usabilidade da ferramenta em telas modernas. A respeito das inovações introduzidas na versão 2013 do PowerPoint, assinale a opção correta.
A) O PowerPoint 2013 eliminou o suporte a apresentações de slides, transformando o aplicativo em um editor exclusivo de fórmulas matemáticas.
B) O PowerPoint 2013 vedou o uso de arquivos de vídeo e áudio em apresentações, admitindo apenas a inserção de textos digitados no teclado.
C) O PowerPoint 2013 adotou a proporção panorâmica 16:9 como formato padrão de novos slides em substituição à proporção tradicional 4:3.
D) O PowerPoint 2013 retirou as guias inteligentes de alinhamento visual de objetos, forçando o uso de réguas manuais milimetradas.
E) O PowerPoint 2013 tornou obrigatória a aquisição de óculos especiais tridimensionais para a visualização de qualquer transição de tela.
// Comentário: A alternativa C está correta, pois a mudança estrutural marcante do PowerPoint 2013 foi a adoção da proporção widescreen 16:9 como padrão para novos slides (em substituição à clássica proporção 4:3), alinhando-se aos monitores de alta definição, além da introdução de guias inteligentes de alinhamento e do Modo do Apresentador aprimorado. As alternativas A, B, D e E são descrições incorretas.

@@ a10/s01 | D
Com o objetivo de otimizar a experiência do usuário e facilitar a localização rápida de comandos na interface Ribbon, o PowerPoint 2016 agregou novos recursos de busca e assistência. Acerca das ferramentas de usabilidade trazidas na versão 2016, assinale a opção correta.
A) A versão 2016 extinguiu a Faixa de Opções, exigindo a digitação de códigos hexadecimais para formatar fontes nos slides da apresentação.
B) A versão 2016 desativou o corretor ortográfico em língua portuguesa para reduzir o espaço ocupado pelo executável no disco rígido.
C) A versão 2016 impediu a exportação de apresentações para formatos estáticos como PDF ou arquivos de vídeo com alta resolução.
D) O recurso "Diga-me o que você deseja fazer" introduzido na versão 2016 permite buscar comandos e ações diretamente por digitação de texto.
E) O recurso de pesquisa inteligente foi suprimido no PowerPoint 2016 para restringir as fontes de informação aos manuais impressos em papel.
// Comentário: A alternativa D está correta, pois uma das principais novidades do PowerPoint 2016 foi a caixa de pesquisa textual "Diga-me o que você deseja fazer" (localizada acima da Faixa de Opções), que permite digitar o nome de um comando ou tarefa para acessá-lo ou executá-lo imediatamente. As alternativas A, B, C e E trazem assertivas falsas sobre a versão 2016.

@@ a10/s01 | E
O PowerPoint 2019 incorporou recursos visuais de impacto cinematográfico e ferramentas que flexibilizam a navegação durante a exposição de temas complexos. No que concerne às novidades do PowerPoint 2019, assinale a opção correta.
A) O PowerPoint 2019 eliminou o suporte a apresentações interativas, limitando a exibição de slides a uma sequência linear inalterável.
B) O PowerPoint 2019 vedou a importação de gráficos vetoriais no formato SVG, admitindo unicamente imagens bitmap em baixa resolução.
C) A versão 2019 extinguiu a ferramenta de marca-texto, tornando impossível destacar trechos textuais durante a edição de diapositivos.
D) O PowerPoint 2019 passou a exigir conexão ininterrupta com satélites militares para a troca de slides em ambientes corporativos fechados.
E) O PowerPoint 2019 introduziu a transição Transformar para animações contínuas e o recurso Zoom para navegação não linear entre slides.
// Comentário: A alternativa E está correta, pois o PowerPoint 2019 introduziu a popular transição "Transformar" (Morph), que cria animações suaves movimentando objetos comuns entre slides consecutivos, e o recurso "Zoom", que viabiliza sumários interativos e navegação dinâmica não linear. As alternativas A, B, C e D trazem assertivas incorretas ou absurdas.

@@ a10/s01 | A
A Microsoft reestruturou seu modelo comercial de distribuição de softwares de produtividade, substituindo a aquisição perpétua de caixas físicas fechadas por um ecossistema de serviços contínuos em nuvem. A respeito do Microsoft 365, assinale a opção correta.
A) O Microsoft 365 opera como serviço por assinatura contínua em nuvem (SaaS), recebendo atualizações mensais de segurança e recursos.
B) O Microsoft 365 é um pacote comercial estático que somente recebe melhorias funcionais a cada intervalo fechado de três anos civis.
C) O Microsoft 365 veda a instalação local de aplicativos como Word e PowerPoint em computadores de mesa, operando exclusivamente em navegadores.
D) O Microsoft 365 dispensa qualquer tipo de autenticação do usuário, permitindo acesso irrestrito a repositórios em nuvem de terceiros.
E) O Microsoft 365 deixou de oferecer suporte ao armazenamento de apresentações no OneDrive, forçando a gravação em disquetes magnéticos.
// Comentário: A alternativa A está correta, visto que o Microsoft 365 (antigo Office 365) adotou o modelo de Software como Serviço (SaaS) mediante assinatura periódica, integrando aplicações locais e web a serviços em nuvem (OneDrive, Teams) e recebendo atualizações mensais e contínuas de recursos. As alternativas B, C, D e E trazem afirmações falsas ou obsoletas.

@@ a10/s01 | B
A integração entre o aplicativo de apresentações e os serviços corporativos de nuvem possibilitou avanços significativos na produção colaborativa de materiais institucionais. Em relação ao recurso de coautoria em tempo real no PowerPoint para Microsoft 365, assinale a opção correta.
A) A coautoria em tempo real exige que todos os colaboradores operem fisicamente conectados ao mesmo teclado e monitor no escritório central.
B) A coautoria em tempo real permite que múltiplos usuários editem a mesma apresentação simultaneamente na nuvem, vendo as ações de cada um.
C) A coautoria em tempo real bloqueia o arquivo por setenta e duas horas sempre que um segundo usuário tenta visualizar os slides já prontos.
D) A coautoria em tempo real restringe-se a apresentações contendo no máximo três slides desprovidos de elementos visuais ou ilustrações.
E) A coautoria em tempo real elimina automaticamente qualquer versão anterior do documento, impossibilitando o histórico de alterações.
// Comentário: A alternativa B está correta, pois a coautoria em tempo real no Microsoft 365 permite que vários usuários abram e trabalhem simultaneamente sobre a mesma apresentação armazenada no OneDrive ou SharePoint, exibindo a presença, o cursor e as edições de cada participante em tempo real com preservação de versões anteriores. As alternativas A, C, D e E distorcem o funcionamento do recurso colaborativo.

@@ a10/s02 | C
A janela principal de trabalho do Microsoft PowerPoint apresenta elementos de interface organizados para agilizar o fluxo produtivo do usuário. No que se refere à Barra de Ferramentas de Acesso Rápido, assinale a opção correta.
A) A Barra de Ferramentas de Acesso Rápido possui botões fixos e imutáveis, sendo vedada qualquer adição ou remoção de comandos pelo usuário.
B) A Barra de Ferramentas de Acesso Rápido localiza-se obrigatoriamente no rodapé da janela, imediatamente abaixo da barra de rolagem vertical.
C) A Barra de Ferramentas de Acesso Rápido é totalmente personalizável e reúne atalhos frequentes, podendo ficar acima ou abaixo da Faixa de Opções.
D) A Barra de Ferramentas de Acesso Rápido impede a inclusão de atalhos convencionais de teclado, como os comandos de salvar e desfazer.
E) As personalizações efetuadas na barra de acesso rápido do PowerPoint são automaticamente replicadas para softwares de terceiros de edição gráfica.
// Comentário: A alternativa C está correta, pois a Barra de Ferramentas de Acesso Rápido do PowerPoint pode ser personalizada pelo usuário para incluir qualquer comando da Faixa de Opções (como Salvar, Desfazer, Iniciar Apresentação), podendo ser posicionada na parte superior esquerda ou logo abaixo da Faixa de Opções. A alternativa A erra porque ela é customizável. As alternativas B, D e E trazem afirmativas incorretas.

@@ a10/s02 | D
A Faixa de Opções (Ribbon) do Microsoft PowerPoint concentra a vasta maioria dos comandos e ferramentas do aplicativo organizados de forma hierárquica. Quanto às regras de personalização da Faixa de Opções, assinale a opção correta.
A) O usuário pode alterar individualmente o tamanho em pixels dos ícones da Faixa de Opções sem modificar as configurações de exibição do sistema.
B) As modificações e novos grupos criados na Faixa de Opções do PowerPoint alteram compulsoriamente a interface do Microsoft Word e do Excel.
C) Todas as guias da Faixa de Opções podem ser renomeadas, reorganizadas e livremente reposicionadas sem qualquer tipo de exceção técnica.
D) A Guia Arquivo, responsável pelo acionamento do Modo Backstage, não pode ser personalizada em posicionamento e ordem como as demais guias.
E) A Faixa de Opções não permite a criação de novas guias personalizadas nem a ocultação de guias nativas preexistentes no software.
// Comentário: A alternativa D está correta, pois a Guia Arquivo (que abre o Modo Backstage com opções de Salvar, Abrir, Imprimir e Exportar) constitui uma exceção crítica: ela não permite personalização de ordem, ocultação ou reorganização como as demais guias da Faixa de Opções. A alternativa A erra porque o tamanho dos ícones depende da escala do sistema operacional. A alternativa B erra porque a customização do PowerPoint é isolada dos outros aplicativos do Office. As alternativas C e E trazem regras falsas de customização.

@@ a10/s02 | E
Durante a elaboração de uma apresentação no Modo de Exibição Normal, a tela divide-se em painéis funcionais que auxiliam na estruturação lógica do conteúdo. A respeito do Painel de Slides (painel de miniaturas), assinale a opção correta.
A) O Painel de Slides localiza-se na margem direita da janela e exibe exclusivamente os cabeçalhos de impressoras conectadas na rede local.
B) O Painel de Slides impede a exclusão direta de diapositivos, exigindo a formatação completa do sistema de arquivos para apagar um slide.
C) O Painel de Slides veda a reordenação de itens por arrasto do mouse, forçando a criação de novos arquivos para alterar a sequência de telas.
D) O Painel de Slides tem sua visualização restrita à projeção em tela cheia no modo de apresentação com projetores multimídia digitais.
E) O Painel de Slides exibe miniaturas sequenciais dos slides à esquerda, permitindo reordenar itens, duplicar telas e gerenciar seções.
// Comentário: A alternativa E está correta, pois no Modo de Exibição Normal o Painel de Slides fica localizado na lateral esquerda, exibindo miniaturas numeradas de todos os slides e permitindo ao usuário reordená-los facilmente por arrasto com o mouse, duplicar, excluir ou organizar os slides em Seções. As alternativas A, B, C e D trazem afirmativas incorretas sobre sua localização e funcionalidades.

@@ a10/s02 | A
Ao trabalhar na criação de apresentações com grande quantidade de detalhes visuais e diagramas, o usuário pode necessitar maximizar a área útil da tela. No Microsoft PowerPoint, assinale a opção que indica o atalho de teclado empregado para recolher ou reexibir a Faixa de Opções:
A) Ctrl + F1
B) Alt + F4
C) Ctrl + P
D) Shift + Esc
E) Ctrl + Z
// Comentário: A alternativa A está correta, pois a combinação de teclas Ctrl + F1 alterna entre ocultar e reexibir a Faixa de Opções (Ribbon) nos aplicativos da suíte Microsoft Office (incluindo o PowerPoint), maximizando o espaço útil de edição. A alternativa B fecha a janela ativa. A alternativa C aciona a impressão. A alternativa D não tem essa função. A alternativa E desfaz a última ação realizada.

@@ a10/s02 | B
A exposição de temas em reuniões corporativas e palestras requer frequentemente que o orador consulte apontamentos privados que não devem ser visíveis aos espectadores. Acerca do Painel de Anotações no PowerPoint, assinale a opção correta.
A) O texto inserido no Painel de Anotações é projetado em letras gigantes sobre o centro da imagem durante a apresentação para o público geral.
B) As anotações digitadas sob o slide principal ficam visíveis exclusivamente na tela privada do orador no Modo de Exibição do Apresentador.
C) O Painel de Anotações não aceita a digitação de caracteres textuais, prestando-se apenas à inserção de arquivos de vídeo em formato AVI.
D) As anotações do orador são deletadas automaticamente do arquivo sempre que a apresentação é salva em formato padrão com extensão .pptx.
E) O Painel de Anotações substitui integralmente a área central de edição do slide, impedindo a inserção de imagens ou formas na apresentação.
// Comentário: A alternativa B está correta, pois o Painel de Anotações (posicionado logo abaixo da área do slide) destina-se a apoiar o orador durante sua apresentação; ao projetar em múltiplos monitores com o Modo do Apresentador, as anotações aparecem unicamente na tela do notebook do apresentador, mantendo o slide limpo para a plateia no projetor. As alternativas A, C, D e E distorcem o propósito e o funcionamento das anotações.

@@ a10/s02 | C
A área inferior da interface gráfica do PowerPoint fornece indicadores dinâmicos sobre o documento ativo e ferramentas de controle rápido de visualização. Em relação aos elementos que compõem a Barra de Status do PowerPoint, assinale a opção correta.
A) A Barra de Status exibe a cotação financeira internacional de títulos públicos e o extrato bancário corporativo do usuário ativo.
B) A Barra de Status veda a alternância entre os modos de exibição Normal, Classificação de Slides e Modo de Leitura na janela de edição.
C) A Barra de Status apresenta o indicador do slide ativo em relação ao total, atalhos de modos de exibição e o controle deslizante de zoom.
D) A Barra de Status é um recurso exclusivo de plataformas operacionais Unix, tendo sido eliminada nas versões para Microsoft Windows.
E) O controle deslizante de zoom presente na Barra de Status altera permanentemente as dimensões físicas dos monitores de vídeo do usuário.
// Comentário: A alternativa C está correta, pois a Barra de Status (localizada na base da janela do PowerPoint) contém na esquerda o número do slide ativo e total (ex.: Slide 1 de 15), idioma e acessibilidade, e na direita reúne atalhos para os Modos de Exibição (Normal, Classificação de Slides, Modo de Leitura e Apresentação) e a barra de Zoom. As alternativas A, B, D e E trazem assertivas manifestamente incorretas.

@@ a10/s04 | D
A criação de apresentações institucionais eficientes exige a representação gráfica de estruturas organizacionais, hierarquias de cargos e fluxos de processos de trabalho. No Microsoft PowerPoint, para inserir um organograma ou diagrama de processo estruturado, assinale a opção que indica o recurso correto a ser selecionado na guia Inserir:
A) WordArt, localizado no grupo Texto da referida guia.
B) Gravação de Tela, posicionado no grupo Mídia da aplicação.
C) Instantâneo, disponível no grupo Imagens da interface gráfica.
D) SmartArt, pertencente ao grupo Ilustrações da guia Inserir.
E) Caixa de Texto, situada no grupo Símbolos da Faixa de Opções.
// Comentário: A alternativa D está correta, pois o recurso SmartArt (localizado na guia Inserir, grupo Ilustrações) é a ferramenta projetada para criar elementos visuais de comunicação estruturada, como organogramas hierárquicos corporativos, listas gráficas, pirâmides e diagramas de fluxo de processos. As alternativas A, B, C e E citam outras ferramentas que não se prestam à elaboração de organogramas ou estão associadas a grupos incorretos.

@@ a10/s04 | E
Na edição de diapositivos no Microsoft PowerPoint, o posicionamento livre de trechos de texto em qualquer ponto da área útil do slide é uma tarefa cotidiana dos elaboradores. A respeito da localização do comando Caixa de Texto na Faixa de Opções, assinale a opção correta.
A) O comando Caixa de Texto localiza-se na guia Exibir, dentro do grupo Modos de Exibição Mestres da apresentação.
B) O comando Caixa de Texto está situado compulsoriamente na guia Design, dentro do grupo dedicado à seleção de Temas.
C) O comando Caixa de Texto pertence à guia Transições, integrando as opções avançadas de intervalo entre diapositivos.
D) O comando Caixa de Texto situa-se prioritariamente na guia Página Inicial, compondo o grupo de formatação de Parágrafo.
E) O comando Caixa de Texto localiza-se na guia Inserir, integrando o grupo Texto ao lado de Cabeçalho e Rodapé e WordArt.
// Comentário: A alternativa E está correta, pois na interface padrão do Microsoft PowerPoint o comando "Caixa de Texto" situa-se na guia Inserir, grupo Texto (ao lado de Cabeçalho e Rodapé, WordArt, Número do Slide e Data e Hora). Uma pegadinha muito comum de bancas examinadoras é sugerir que a Caixa de Texto pertença à guia Página Inicial ou Design, o que torna as alternativas A, B, C e D incorretas.

@@ a10/s04 | A
A preparação de uma apresentação pode exigir a adequação das dimensões dos slides ao equipamento de projeção ou a padrões impressos personalizados. No Microsoft PowerPoint, para personalizar as dimensões físicas dos slides, assinale a opção que apresenta o procedimento correto.
A) Guia Design > grupo Personalizar > comando Tamanho do Slide > Tamanho do Slide Personalizado.
B) Guia Inserir > grupo Ilustrações > comando Formas > Redimensionar Telas de Apresentação.
C) Guia Apresentação de Slides > grupo Configurar > comando Projeção em Múltiplos Monitores.
D) Guia Exibir > grupo Modos de Exibição de Apresentação > comando Classificação de Slides.
E) Guia Transições > grupo Intervalo > comando Duração de Slides em Tela Panorâmica.
// Comentário: A alternativa A está correta, pois o caminho oficial e padronizado para alterar a proporção (16:9 ou 4:3) ou ajustar medidas personalizadas de largura e altura em centímetros é: guia Design > grupo Personalizar > comando Tamanho do Slide > Tamanho do Slide Personalizado. As alternativas B, C, D e E apontam caminhos inexistentes ou alheios à definição das dimensões do slide.

@@ a10/s04 | B
A distinção conceitual e prática entre os recursos visuais disponíveis no Microsoft PowerPoint é frequentemente cobrada em concursos públicos. Acerca das diferenças entre Transição e Animação no PowerPoint, assinale a opção correta.
A) A transição aplica efeitos exclusivamente sobre palavras selecionadas, enquanto a animação atua na rotação de monitores de vídeo físicos.
B) A transição consiste no efeito visual ao passar de um slide para o outro, ao passo que a animação é o efeito em objetos dentro de um mesmo slide.
C) A transição e a animação são termos estritamente sinônimos no aplicativo, aplicando-se indistintamente a qualquer elemento gráfico da tela.
D) A animação pode ser aplicada unicamente ao plano de fundo geral dos slides, enquanto a transição aplica-se a imagens individuais vetoriais.
E) O efeito de transição é visível apenas no Modo de Exibição Normal, sendo suprimido quando a apresentação é projetada em tela cheia.
// Comentário: A alternativa B está correta, sintetizando a distinção fundamental do PowerPoint: "Transição" é o efeito visual exibido durante a passagem de um slide para o seguinte (no modo Apresentação de Slides), enquanto "Animação" é o efeito visual dinâmico aplicado a objetos específicos (textos, gráficos, imagens) situados dentro de um mesmo slide. As alternativas A, C, D e E trazem confusões conceituais recorrentes em provas.

@@ a10/s04 | C
Ao configurar os efeitos visuais de mudança de tela em uma apresentação com dezenas de diapositivos, o apresentador busca padronizar a experiência do público. Na guia Transições do Microsoft PowerPoint, assinale a opção que indica a finalidade do recurso "Aplicar a Todos":
A) Converter instantaneamente todos os slides da apresentação em arquivos de planilhas de cálculo financeiro vinculadas.
B) Aplicar a mesma imagem de plano de fundo e a mesma paleta de fontes a todas as apresentações salvas no computador do usuário.
C) Estender o efeito de transição, a temporização e as configurações de som do slide atual para todos os slides da apresentação.
D) Criar cópias automáticas idênticas de todos os parágrafos de texto no Painel de Anotações de todas as telas existentes.
E) Duplicar o número de diapositivos da apresentação e fechar o aplicativo sem salvar as modificações feitas pelo autor.
// Comentário: A alternativa C está correta, pois na guia Transições (grupo Intervalo), o botão "Aplicar a Todos" replica as configurações do slide ativo (tipo de efeito de transição, som, duração e método de avanço) para todos os outros slides da apresentação atual. A alternativa B descreve comandos de temas da guia Design. As alternativas A, D e E trazem ações descabidas.

@@ a10/s04 | D
O Microsoft PowerPoint oferece uma vasta biblioteca de efeitos visuais para dinamizar a entrada e a movimentação de elementos gráficos durante a fala do orador. No que tange às categorias formais de efeitos da guia Animações, assinale a opção correta.
A) Os efeitos de animação dividem-se formalmente em apenas duas classes: efeitos de compressão e efeitos de expansão de texto.
B) As animações classificam-se em efeitos de hardware de vídeo, efeitos de cabeamento de rede e efeitos de memória secundária.
C) Os efeitos de animação subdividem-se exclusivamente em efeitos monetários, efeitos contábeis e efeitos estatísticos descritivos.
D) As animações estruturam-se em quatro tipos formais: efeitos de Entrada, efeitos de Ênfase, efeitos de Saída e Caminhos de Animação.
E) A guia Animações disponibiliza apenas efeitos de Saída, sendo vedado animar o surgimento ou o deslocamento de objetos no slide.
// Comentário: A alternativa D está correta, pois os efeitos de animação de objetos no PowerPoint organizam-se formalmente em quatro categorias estruturadas: Entrada (como o objeto aparece na tela), Ênfase (destaque do objeto já presente, mudando cor ou tamanho), Saída (como o objeto sai ou desaparece do slide) e Caminhos de Animação (trajetórias pré-definidas ou personalizadas de deslocamento espacial). As alternativas A, B, C e E apresentam classificações inexistentes.

@@ a10/s04 | E
Na edição avançada de animações, replicar individualmente conjuntos complexos de temporização e efeitos sobre dezenas de objetos pode tornar-se uma tarefa repetitiva e sujeita a falhas. No Microsoft PowerPoint, para copiar rapidamente os efeitos de animação de um objeto para outro, assinale a opção que indica a ferramenta adequada:
A) Pincel de Formatação, acionado pelo atalho Ctrl + Shift + X na guia Design da Faixa de Opções.
B) Painel de Seleção, disponível exclusivamente no grupo Configurar da guia Apresentação de Slides.
C) Marcador de Slides, ativado por meio do atalho de teclado F5 durante a exibição em tela cheia.
D) Disparador de Ações, posicionado na guia Revisão no grupo dedicado a Comentários e Revisores.
E) Pincel de Animação, localizado no grupo Animação Avançada da guia Animações (atalho Alt + Shift + C).
// Comentário: A alternativa E está correta, pois o "Pincel de Animação" (atalho de teclado Alt + Shift + C), situado no grupo Animação Avançada da guia Animações, tem funcionamento análogo ao Pincel de Formatação, permitindo copiar todos os efeitos, disparadores e intervalos aplicados a um objeto e aplicá-los com um clique sobre outro objeto. A alternativa A erra porque o Pincel de Formatação copia a aparência visual (fonte, cor, borda), e não as animações. As alternativas B, C e D citam ferramentas alheias à cópia de animações.

@@ a10/s04 | A
A coordenação precisa dos momentos em que cada elemento gráfico deve surgir na tela durante a explanação exige o gerenciamento de uma linha do tempo detalhada. Acerca das funcionalidades do Painel de Animação no PowerPoint, assinale a opção correta.
A) O Painel de Animação exibe a lista sequencial de todos os efeitos do slide ativo, permitindo reordenar, ajustar intervalos e testar a reprodução.
B) O Painel de Animação bloqueia permanentemente a edição de slides, exigindo a reinicialização do sistema operacional para qualquer alteração.
C) O Painel de Animação atua convertendo automaticamente a apresentação de slides em um banco de dados relacional criptografado em nuvem.
D) O Painel de Animação limita-se a exibir a quantidade total de impressoras instaladas no sistema corporativo de centros de dados.
E) O Painel de Animação impede que dois objetos diferentes tenham efeitos configurados para serem reproduzidos de forma simultânea.
// Comentário: A alternativa A está correta, pois o Painel de Animação (ativado na guia Animações > grupo Animação Avançada) abre um painel lateral que mostra a lista cronológica completa de todas as animações aplicadas no slide atual, possibilitando reordená-las (mover antes ou depois), definir a forma de início (Ao Clicar, Com a Anterior ou Após a Anterior), regular duração/atraso e visualizar a execução. As alternativas B, C, D e E trazem assertivas falsas.
"""
