"""Part 2 of new questions for informatica: Q31 to Q59
Trechos:
- informatica/a03/s03: Q31 to Q32
- informatica/a03/s04: Q33 to Q37
- informatica/a03/s06: Q38 to Q42
- informatica/a03/s07: Q43 to Q47
- informatica/a04/s01: Q48 to Q49
- informatica/a04/s04: Q50 to Q53
- informatica/a05/s01: Q54 to Q59
"""

NOVAS_P2 = """
@@ a03/s03 | A
A proliferação de pragas virtuais em redes corporativas decorre frequentemente da atuação de códigos maliciosos capazes de se disseminar de modo automatizado. A respeito da distinção entre vírus e worms, assinale a opção correta.
A) O worm propaga-se de forma autônoma pela rede explorando vulnerabilidades em sistemas, dispensando a inserção em arquivos hospedeiros.
B) O vírus propaga-se autonomamente pelos enlaces de rede sem necessitar de qualquer ação ou clique executado pelo usuário da máquina.
C) O worm é incapaz de replicar a si mesmo, dependendo exclusivamente de comandos remotos digitados por operadores em sessões abertas.
D) O vírus e o worm são idênticos em seu mecanismo de propagação, infectando obrigatoriamente apenas arquivos executáveis com extensão .exe.
E) O worm requer a execução explícita de documentos de texto em formato estruturado para iniciar a contaminação de computadores vizinhos.
// Comentário: O worm destaca-se por sua capacidade de autorreplicação e propagação autônoma pelas redes de dados, explorando vulnerabilidades ativas em serviços e softwares sem depender de hospedeiro ou de cliques do usuário. Em contrapartida, o vírus clássico necessita parasitar um arquivo ou programa hospedeiro e requer a execução desse arquivo contaminado para entrar em atividade.

@@ a03/s03 | C
A persistência de invasores em ambientes corporativos comprometidos apoia-se em ferramentas que asseguram controle remoto e ocultação no sistema operacional. No que tange aos conceitos de Backdoor e Rootkit, assinale a opção correta.
A) O backdoor atua desfragmentando discos rígidos e desativando portas seriais para acelerar o tráfego de dados locais.
B) O rootkit é uma ferramenta inofensiva de auditoria contábil desenvolvida por fabricantes de hardware para verificar memórias RAM.
C) O rootkit tem como propósito assegurar a presença do invasor e ocultar atividades e códigos maliciosos nas camadas do sistema.
D) O backdoor impede a comunicação entre computadores locais, desativando permanentemente a placa de rede em estações de trabalho.
E) O rootkit atua exclusivamente convertendo arquivos de planilhas de cálculo em apresentações de slides protegidas por senhas.
// Comentário: O rootkit é um conjunto de códigos maliciosos projetado para manter o acesso privilegiado do invasor e ocultar de forma avançada a presença de outros malwares, processos, arquivos e chaves de registro contra ferramentas de monitoramento do sistema operacional. Já o backdoor consiste em uma porta dos fundos que possibilita o retorno e controle remoto do atacante contornando os mecanismos regulares de autenticação.

@@ a03/s04 | B
Softwares espiões utilizam técnicas especializadas de captura de dados para registrar informações confidenciais diretamente no momento de sua inserção na máquina. Acerca das diferenças entre Keyloggers e Screenloggers, assinale a opção correta.
A) O keylogger registra imagens gráficas da tela do computador, ao passo que o screenlogger grava unicamente comandos de voz.
B) O keylogger captura as teclas digitadas no teclado físico, enquanto o screenlogger grava imagens da área circundante aos cliques do mouse.
C) O screenlogger é um mecanismo de proteção que impede a interceptação de dados por navegadores de Internet em compras online.
D) O keylogger atua exclusivamente em conexões ópticas de alta velocidade, sendo ineficaz contra teclados físicos convencionais com fio.
E) Ambos os programas são softwares benignos homologados para restaurar arquivos excluídos acidentalmente por operadores de centros de dados.
// Comentário: O keylogger é um programa espião voltado a registrar e armazenar silenciosamente as teclas pressionadas no teclado físico pelo usuário (senhas, textos, dados pessoais). Para contornar teclados virtuais em tela criados por bancos, criminosos desenvolveram os screenloggers, que capturam imagens da tela na região imediatamente ao redor do cursor sempre que o mouse é clicado.

@@ a03/s04 | A
A navegação na Internet pode ser prejudicada pela exibição massiva e indesejada de anúncios publicitários que comprometem o desempenho do sistema operacional. Com relação aos Adwares e à sua relação com spywares, assinale a opção correta.
A) O adware é projetado para exibir anúncios publicitários, podendo incorporar rotinas de spyware para rastrear hábitos de navegação.
B) O adware atua exclusivamente destruindo a estrutura física do processador central por meio de comandos de overclock indevidos.
C) O adware elimina todos os arquivos executáveis do computador hospedeiro no exato momento em que uma janela pop-up é fechada.
D) O adware é uma categoria de antivírus de quarta geração baseada em aprendizado de máquina para conter infecções corporativas.
E) O adware impede que computadores acessem a World Wide Web, convertendo todas as portas lógicas de transporte em conexões seriais.
// Comentário: O adware é uma praga virtual projetada primordialmente para apresentar propagandas abusivas e anúncios não solicitados (banners, janelas pop-up). Frequentemente atua consorciado a rotinas de spyware, coletando silenciosamente dados de navegação, interesses de consumo e buscas do usuário para direcionar anúncios ou comercializar perfis com terceiros sem consentimento.

@@ a03/s04 | B
O monitoramento do fluxo de pacotes em um segmento de rede local permite a análise legítima de tráfego, mas também pode ser explorado por invasores. A respeito das ferramentas de Sniffer (farejador de rede), assinale a opção correta.
A) O sniffer atua compactando arquivos de texto em lote para reduzir o consumo de memória principal em servidores de bancos de dados.
B) O sniffer captura e inspeciona quadros e pacotes em trânsito no meio físico, operando com a placa de rede em modo promíscuo.
C) O sniffer é um tipo de vírus parasitário que sobrescreve o código de inicialização de roteadores ópticos de operadoras de telefonia.
D) O sniffer impede que estações de trabalho recebam dados via cabo de rede, limitando a comunicação institucional a conexões Bluetooth.
E) A utilização de sniffers é restrita a softwares maliciosos, não existindo qualquer aplicação de diagnóstico legítimo para administradores.
// Comentário: O sniffer (ou analisador de pacotes) é uma ferramenta que captura, decodifica e inspeciona os pacotes que trafegam pelo meio de transmissão da rede. Para capturar todo o tráfego que passa pelo segmento, e não apenas o endereçado à sua própria máquina, a placa de rede é configurada no chamado "modo promíscuo". Embora amplamente utilizado por administradores de redes para diagnóstico e segurança, pode ser explorado por criminosos para interceptar credenciais em trânsito sem criptografia.

@@ a03/s04 | A
A infecção de estações corporativas por softwares espiões frequentemente ocorre de forma dissimulada através de hábitos inadequados de operação de software. No que se refere às formas usuais de contaminação por Spywares, assinale a opção correta.
A) Os spywares costumam ser introduzidos como componentes ocultos em programas gratuitos duvidosos ou por meio de anexos maliciosos.
B) Os spywares contaminam computadores exclusivamente quando cabos de alimentação elétrica sofrem picos transitórios de tensão alternada.
C) A instalação de spywares é impedida de forma definitiva pela simples desconexão de caixas acústicas externas em computadores portáteis.
D) Os spywares são gerados espontaneamente pela memória volátil do sistema operacional em períodos de sobrecarga de processamento de texto.
E) A obtenção de spywares exige que o usuário digite comandos hexadecimais no terminal de controle de hardware em modo de depuração.
// Comentário: Os programas espiões (spywares) costumam ingressar nos computadores pegando carona na instalação de aplicativos gratuitos de fontes não confiáveis (freewares, instaladores com ofertas adicionais), através de cavalos de Troia (trojans bancários) embutidos em anexos de e-mail enganosos ou pela exploração de vulnerabilidades no navegador ao visitar sítios fraudulentos.

@@ a03/s04 | E
A manutenção da confidencialidade e da privacidade dos dados em estações corporativas demanda a implantação de defesas especializadas contra espiões. Acerca das medidas de proteção contra a atuação de Spywares, assinale a opção correta.
A) A proteção contra spywares restringe-se à limpeza física de poeira acumulada nas ventoinhas do gabinete dos servidores centrais.
B) A mitigação de spywares dispensa a utilização de ferramentas de segurança, dependendo exclusivamente da troca diária de monitores.
C) O uso de programas antispyware é desaconselhado pelas normas de segurança por aumentar a exposição de portas lógicas do sistema.
D) A instalação de softwares espiões é incentivada em redes públicas para acelerar o processamento de planilhas de cálculo contábil.
E) A prevenção envolve o uso de soluções antimalware com monitoramento em tempo real, sistemas atualizados e isolamento em quarentena.
// Comentário: A contenção de softwares espiões baseia-se na conjugação de práticas defensivas: instalação e atualização constante de soluções antimalware/antispyware com capacidade de monitoramento residente em memória, aplicação de correções no sistema operacional e nos navegadores, cautela no download de programas e arquivos externos e uso do recurso de quarentena para isolar arquivos suspeitos.

@@ a03/s06 | C
Golpes virtuais que empregam técnicas de engenharia social proliferam em diferentes canais de comunicação para capturar credenciais de vítimas. A respeito da distinção entre Phishing, Smishing e Vishing, assinale a opção correta.
A) O phishing restringe-se a mensagens de áudio analógicas transmitidas exclusivamente por cabos submarinos de telecomunicações.
B) O vishing opera exclusivamente por meio de mensagens de texto SMS que induzem a instalação de certificados digitais corrompidos.
C) O smishing utiliza mensagens de texto SMS fraudulentas, ao passo que o vishing conduz a persuasão por meio de chamadas de voz.
D) O phishing e o smishing são termos técnicos sinônimos que descrevem a quebra matemática de chaves assimétricas em roteadores.
E) O vishing caracteriza-se pela alteração visual de portais corporativos na Web sem qualquer interação verbal com o usuário.
// Comentário: Essas três modalidades representam vertentes de golpes de engenharia social: o phishing clássico emprega rotineiramente e-mails e páginas falsas; o smishing (SMS phishing) utiliza mensagens curtas de texto em telefones celulares com links ou solicitações maliciosas; e o vishing (voice phishing) aplica a persuasão mediante chamadas telefônicas de voz simulando falsas centrais de atendimento ou instituições financeiras.

@@ a03/s06 | D
A sofisticação dos ataques à integridade da resolução de nomes de domínio pode desviar internautas de rotas legítimas sem que falhas visíveis sejam notadas. Acerca do golpe denominado Pharming, assinale a opção correta.
A) O pharming consiste no envio massivo de e-mails contendo propostas comerciais legítimas de venda de suprimentos para escritórios.
B) O pharming atua destruindo fisicamente os comutadores ópticos de centros de dados mediante pulsos de micro-ondas de alta potência.
C) O pharming impede o carregamento de imagens no navegador, exibindo exclusivamente tabelas numéricas sem conexão com a rede.
D) O pharming corrompe a resolução de nomes (DNS ou arquivo hosts), redirecionando a navegação para sítios falsos mesmo com a URL correta.
E) O pharming é uma técnica de criptografia assimétrica de alta velocidade utilizada na emissão de carimbos do tempo certificados.
// Comentário: O pharming (ou envenenamento de DNS) consiste em adulterar o processo de tradução de nomes em endereços IP, seja modificando o arquivo local hosts no computador da vítima, seja envenenando o cache de servidores DNS. Como resultado, mesmo que o usuário digite o endereço eletrônico perfeitamente correto no navegador, ele é redirecionado silenciosamente para um sítio clonado mantido por criminosos para capturar credenciais.

@@ a03/s06 | B
A manipulação psicológica de pessoas por meio de canais de áudio tem sido intensamente utilizada em fraudes financeiras contra correntistas. No que tange às características de um ataque de Vishing, assinale a opção correta.
A) O vishing atua instalando programas de edição de vídeo em servidores de rede para capturar telas de conferências executivas.
B) O vishing baseia-se em chamadas telefônicas de voz nas quais criminosos induzem a vítima a transferir valores ou revelar senhas sigilosas.
C) O vishing é um ataque puramente lógico focado em inundar interfaces seriais de roteadores de borda com datagramas UDP sem dados.
D) O vishing limita-se ao envio de correspondências físicas impressas em papel timbrado contendo códigos de barras desativados.
E) O vishing realiza a quebra de senhas complexas mediante o teste exaustivo de combinações alfanuméricas em supercomputadores.
// Comentário: O vishing (voice phishing) apoia-se na comunicação verbal telefônica. Golpistas entram em contato com a vítima fazendo-se passar por funcionários de centrais de segurança de instituições financeiras ou operadoras de cartão de crédito, alegando supostas transações suspeitas e manipulando a vítima para que forneça senhas, confirme tokens ou realize transferências financeiras de emergência.

@@ a03/s06 | A
Determinados ataques de engenharia social escolhem alvos estratégicos com grande poder de comando na hierarquia das organizações. A respeito do golpe conhecido como Whaling (pesca de baleia), assinale a opção correta.
A) O whaling é um ataque direcionado a alvos de alto escalão, como presidentes de corporações, diretores e ocupantes de cargos executivos.
B) O whaling é um código malicioso desenvolvido para infectar exclusivamente comutadores de rede instalados em navios de pesquisa oceanográfica.
C) O whaling caracteriza-se pela distribuição aleatória e indiscriminada de mensagens publicitárias para milhões de caixas postais públicas.
D) O whaling atua desligando os sistemas de ar-condicionado de centros de dados para provocar superaquecimento nas placas de memória.
E) O whaling dispensa pesquisas prévias sobre a vítima, baseando-se no envio de arquivos compactados vazios sem qualquer texto.
// Comentário: O whaling (derivado metafórico da pesca de grandes baleias) é uma variante altamente sofisticada de spear phishing direcionada especificamente a indivíduos de alto escalão corporativo ou governamental (CEOs, diretores, magistrados e altos gestores públicos). Esses ataques utilizam linguagem formal e dados prévios minuciosos sobre a organização para obter transferências vultosas ou acesso a segredos institucionais.

@@ a03/s06 | B
A exploração da curiosidade e da ganância de colaboradores pode ser realizada mediante a oferta de recompensas materiais ou digitais aparentemente vantajosas. Em relação à técnica de engenharia social denominada Baiting (isca), assinale a opção correta.
A) O baiting consiste em interceptar o tráfego de pacotes na camada de rede para alterar campos do cabeçalho de roteamento dinâmico.
B) O baiting atrai a vítima oferecendo promessas tentadoras ou mídias físicas abandonadas contendo códigos maliciosos para induzir a execução.
C) O baiting é um recurso defensivo instalado em firewalls de borda para registrar endereços IP de criminosos que visitam portais públicos.
D) O baiting limita-se a monitorar o tempo de resposta de conexões de correio eletrônico em servidores centrais de centros de dados.
E) O baiting baseia-se na exclusão imediata de todos os certificados digitais do sistema operacional no momento da conexão à Internet.
// Comentário: O baiting (ataque por isca) explora a curiosidade ou o interesse pessoal da vítima. O atacante disponibiliza uma isca atraente, como um pendrive infectado deixado propositalmente em estacionamentos ou recepções corporativas (muitas vezes com rótulos chamativos como "Folha de Pagamento" ou "Bônus"), ou ofertas de downloads gratuitos na Web, induzindo a própria vítima a conectar a mídia e executar o malware.

@@ a03/s07 | E
A personalização profunda de mensagens fraudulentas com dados previamente coletados sobre a rotina da vítima potencializa a taxa de sucesso de invasões. No que concerne ao Spear Phishing, assinale a opção correta.
A) O spear phishing caracteriza-se pelo disparo aleatório e massivo de milhões de mensagens idênticas sem qualquer personalização de dados.
B) O spear phishing opera exclusivamente mediante a alteração dos registros de fuso horário na placa-mãe de computadores portáteis.
C) O spear phishing atua desativando os serviços de resolução de nomes em roteadores domésticos conectados à rede de telecomunicações.
D) O spear phishing é uma ferramenta de auditoria de conformidade tributária homologada para certificar a legalidade de contratos empresariais.
E) O spear phishing é um ataque direcionado a indivíduos ou departamentos específicos, empregando dados contextuais detalhados para obter credibilidade.
// Comentário: Diferentemente do phishing genérico disseminado em massa sem critério, o spear phishing é um ataque focado e customizado para uma pessoa, grupo ou departamento determinado. O atacante utiliza informações contextuais prévias (cargos, projetos em andamento, nomes de colegas e sistemas utilizados) para compor uma abordagem verossímil que induza o alvo a clicar em links ou abrir anexos nocivos.

@@ a03/s07 | D
A interceptação clandestina de fluxos de dados estabelecidos entre polos legítimos de comunicação permite a devassa e a adulteração indevida de dados. Acerca do ataque Man-in-the-Middle (MitM), assinale a opção correta.
A) O ataque MitM atua desinstalando permanentemente os drivers de impressoras departamentais em redes comutadas de alta velocidade.
B) O ataque MitM impede a emissão de comprovantes de pagamento em caixas registradoras conectadas a redes de alimentação ininterrupta.
C) O ataque MitM limita-se à exclusão física de bancos de dados relacionais por meio do envio de comandos de formatação ao disco rígido.
D) O invasor posiciona-se entre duas partes comunicantes, interceptando e podendo alterar os dados transmitidos sem que os polos percebam.
E) O ataque MitM caracteriza-se pela quebra incondicional e definitiva de todos os algoritmos de criptografia de chave pública conhecidos.
// Comentário: No ataque Man-in-the-Middle (homem no meio), o agente malicioso intercepta secretamente a comunicação entre duas entidades legítimas (por exemplo, entre o navegador do usuário e o servidor bancário), podendo ler em claro dados sensíveis (quebrando a confidencialidade) ou até modificar mensagens e transações em trânsito (violando a integridade), sem que nenhuma das partes desconfie da intromissão.

@@ a03/s07 | C
A integridade visual de sítios governamentais e empresariais pode ser violada por invasores com o propósito de transmitir manifestos ou expor fragilidades. Com relação ao ataque de Defacement (desfiguração ou pichação de páginas web), assinale a opção correta.
A) O defacement consiste na exclusão completa de todos os sistemas de arquivos operacionais de centros de processamento de dados.
B) O defacement é uma técnica de cifragem em lote aplicada por ransomware com exigência de resgate financeiro em criptomoedas.
C) O defacement consiste na alteração visual ou de conteúdo da página de um sítio na Web, frequentemente com motivação política ou de protesto.
D) O defacement atua impedindo fisicamente que servidores de correio eletrônico recebam mensagens através do protocolo SMTP.
E) O defacement opera no nível da camada física de enlaces de rede, rompendo conectores ópticos por meio de ondas de rádio polarizadas.
// Comentário: O defacement (desfiguração ou pichação de sítio web) ocorre quando invasores obtêm acesso indevido ao servidor web e modificam a página principal ou seções do portal, substituindo os conteúdos originais por mensagens provocativas, de cunho político, ativista (hacktivismo) ou de zombaria, evidenciando publicamente a invasão sem que necessariamente destruam os bancos de dados subjacentes.

@@ a03/s07 | A
A exploração de formulários eletrônicos que não realizam a higienização de parâmetros de entrada pode comprometer gravemente a segurança de dados corporativos. A respeito do ataque de Injeção de SQL (SQL Injection), assinale a opção correta.
A) O atacante insere comandos SQL maliciosos em campos de entrada de formulários para manipular consultas e acessar bases de dados internas.
B) A injeção de SQL atua infectando o setor de inicialização de discos rígidos em computadores portáteis desconectados da Internet.
C) A injeção de SQL consiste no envio massivo de pacotes de dados sem cabeçalho para saturar a largura de banda de enlaces de fibra óptica.
D) O ataque de SQL Injection elimina a necessidade de chaves assimétricas na validação de assinaturas em contratos digitais corporativos.
E) O SQL Injection afeta exclusivamente redes corporativas que utilizam bancos de dados estruturados em fitas perfuradas manuais.
// Comentário: O SQL Injection (SQLi) é uma vulnerabilidade clássica em aplicações web decorrente da falta de filtragem ou sanitização de dados submetidos por usuários em campos de formulários ou URLs. Ao introduzir fragmentos de código SQL, o invasor consegue alterar a lógica da consulta original executada pela aplicação, logando sem credenciais válidas, extraindo dados confidenciais ou excluindo tabelas inteiras no banco de dados.

@@ a03/s07 | B
A circulação de mensagens alarmistas e conteúdos fictícios em redes sociais e correios eletrônicos compromete a produtividade e dissemina desinformação. No que concerne aos Hoaxes (boatos na rede), assinale a opção correta.
A) O hoax é um código malicioso de primeira geração que atua reescrevendo instruções do BIOS em placas de circuito integrado.
B) O hoax consiste em um boato ou história alarmista falsa transmitida por mensagens com apelos emocionais para que o texto seja compartilhado em massa.
C) O hoax atua criptografando pastas de trabalho corporativas e cobrando taxas de recuperação financeira em contas internacionais.
D) O hoax é um protocolo padronizado internacionalmente para sincronizar relógios de rede em centros de processamento de dados.
E) O hoax atua convertendo automaticamente e-mails de texto claro em planilhas de cálculo financeiro auditadas por órgãos judiciais.
// Comentário: O hoax é um boato, história fabricada ou lenda urbana disseminada pela rede (via e-mail, redes sociais ou mensageiros instantâneos). Costuma conter alertas falsos sobre supostos novos vírus devastadores, pedidos de ajuda forjados ou promessas irreais de ganhos, instando o leitor a repassar a mensagem para todos os seus contatos, gerando pânico, desperdício de tempo e saturação inútil de canais corporativos.

@@ a04/s01 | D
Os primórdios do combate a códigos maliciosos apoiaram-se em softwares desenvolvidos para rastrear padrões específicos gravados em arquivos executáveis. Acerca das soluções antivírus de 1ª geração, assinale a opção correta.
A) A 1ª geração de antivírus baseava-se em inteligência artificial preditiva e monitoramento comportamental em tempo real em nuvem.
B) A 1ª geração de antivírus executava códigos suspeitos em ambientes virtuais de sandbox para isolar o sistema operacional.
C) A 1ª geração de antivírus realizava a desinfecção instantânea de pragas inéditas antes da compilação de seus binários pelos atacantes.
D) A 1ª geração de antivírus fundamentava-se na detecção por assinatura, comparando sequências de bytes dos arquivos com uma base catalogada.
E) A 1ª geração de antivírus dispensava a atualização de bases de dados, sendo imune ao surgimento de novas variantes de vírus no mercado.
// Comentário: As soluções antivírus de 1ª geração caracterizam-se pelo método reativo de detecção por assinaturas (dicionários de vírus). O programa faz a varredura dos arquivos em busca de sequências estáticas conhecidas de bytes (assinaturas binárias) correspondentes a vírus previamente catalogados em laboratório pelos analistas de segurança.

@@ a04/s01 | E
O paradigma de busca por padrões conhecidos exibe restrições técnicas estruturais perante a velocidade de surgimento de novas ameaças no ecossistema digital. Em relação às limitações da detecção baseada puramente em assinaturas, assinale a opção correta.
A) A detecção por assinatura apresenta como defeito central a ocorrência constante e indiscriminada de falsos positivos em programas novos.
B) A detecção por assinatura é a única técnica capaz de neutralizar ataques de dia zero (zero-day) no exato instante de sua concepção.
C) A detecção por assinatura dispensa o consumo de espaço de armazenamento, mantendo bases de dados com tamanho de apenas um único bit.
D) A detecção por assinatura atua decifrando senhas bancárias em texto claro nos servidores de correio eletrônico corporativo.
E) A detecção por assinatura é ineficaz contra malwares desconhecidos e vírus mutantes, exigindo catalogação prévia da praga na base de dados.
// Comentário: A grande limitação da detecção tradicional por assinaturas reside em sua incapacidade de bloquear malwares recém-criados para os quais ainda não existam vacinas ou assinaturas catalogadas (ameaças de dia zero / zero-day), bem como sua baixa efetividade contra vírus polimórficos e metamórficos que alteram sua assinatura a cada contaminação.

@@ a04/s04 | B
A evolução dos dispositivos de controle de tráfego perimetral permitiu que regras de segurança considerassem a dinâmica das conexões em andamento. No que diz respeito ao Firewall com inspeção de estado de sessão (Stateful), assinale a opção correta.
A) O firewall stateful inspeciona pacotes de forma totalmente isolada, descartando qualquer memória sobre conexões previamente abertas.
B) O firewall stateful monitora o estado das conexões e mantém uma tabela de estados, liberando pacotes legítimos que pertencem a sessões ativas.
C) O firewall stateful atua exclusivamente na camada física de transmissão, inspecionando a modulação óptica em cabos submarinos de dados.
D) O firewall stateful exige que todas as portas do sistema permaneçam permanentemente abertas para receber tráfego de qualquer origem.
E) O firewall stateful substitui a necessidade de servidores web corporativos, hospedando diretamente páginas de bancos de dados relacionais.
// Comentário: O firewall com inspeção de estados (stateful inspection) mantém na memória uma tabela dinâmica de estados que acompanha o ciclo de vida completo de cada sessão de comunicação (como as fases SYN, SYN-ACK, ACK do TCP). Isso permite que o firewall autorize automaticamente o tráfego de retorno pertencente a uma conexão legítima iniciada internamente, mantendo as portas fechadas para conexões não solicitadas vindas de fora.

@@ a04/s04 | E
Determinadas soluções de segurança perimetral operam na camada superior da arquitetura de redes para inspecionar comandos específicos de serviços corporativos. Acerca do Firewall do tipo Proxy de Aplicação, assinale a opção correta.
A) O proxy de aplicação atua na camada de enlace do modelo OSI, filtrando quadros com base exclusivamente no endereço físico MAC.
B) O proxy de aplicação veda a inspeção de conteúdos de páginas web, limitando-se a registrar a voltagem elétrica de cabos de par trançado.
C) O proxy de aplicação elimina os endereços IP dos servidores de rede, forçando o encaminhamento manual de mensagens por operadores.
D) O proxy de aplicação opera sem interromper o fluxo direto de pacotes IP, conectando os computadores externos diretamente aos servidores internos.
E) O proxy atua como intermediário na camada de aplicação, recebendo requisições, inspecionando conteúdos e estabelecendo novas conexões.
// Comentário: O firewall proxy de aplicação (ou gateway de aplicação) opera na camada 7 (aplicação). Ele atua como um intermediário mandatório: o cliente conecta-se ao proxy, que interrompe o fluxo de rede, examina profundamente os dados e comandos da aplicação (como comandos HTTP, requisições GET/POST e cabeçalhos) e, se a política autorizar, abre uma nova conexão própria com o servidor de destino, ocultando a rede interna.

@@ a04/s04 | E
A convergência de múltiplos mecanismos de segurança em uma única plataforma perimetral de alto desempenho caracteriza os firewalls contemporâneos. A respeito dos Firewalls de Próxima Geração (Next Generation Firewall - NGFW), assinale a opção correta.
A) O NGFW limita sua atuação a filtros simples de portas TCP e UDP, rejeitando módulos adicionais de prevenção contra intrusões de rede.
B) O NGFW foi projetado para operar exclusivamente em computadores portáteis domésticos desprovidos de conexão com a rede mundial.
C) O NGFW elimina os mecanismos de controle de aplicações em segundo plano, delegando a inspeção de dados ao usuário final da máquina.
D) O NGFW atua exclusivamente na camada física, controlando a temperatura de salas de servidores por meio de ventiladores automáticos.
E) O NGFW combina inspeção profunda de pacotes, identificação e controle de aplicações em tempo real e sistema integrado de prevenção de intrusão.
// Comentário: Os Firewalls de Próxima Geração (NGFW) integram em uma arquitetura única de hardware e software a inspeção profunda de pacotes (DPI), controle e visibilidade de aplicações específicas (mesmo trafegando em portas padrão como 80/443), sistemas de prevenção contra intrusão (IPS) integrados, suporte a inteligência contra ameaças em nuvem e inspeção de tráfego TLS/SSL criptografado.

@@ a04/s04 | D
A análise técnica comparativa entre diferentes gerações de firewalls evidencia ganhos substanciais de segurança com o avanço da tecnologia de filtragem. Quanto às vantagens do filtro stateful sobre o filtro estático stateless, assinale a opção correta.
A) O filtro stateful consome menos memória principal do que o stateless por não armazenar qualquer registro de conexões no circuito.
B) O filtro stateless impede de forma mais eficaz o tráfego de pacotes fraudulentos com endereçamento forjado em conexões de saída da rede.
C) O filtro stateful veda a utilização do protocolo TCP, restringindo o tráfego institucional a datagramas UDP não orientados à conexão.
D) O filtro stateful reduz a superfície de ataque ao dispensar portas abertas permanentemente para aceitar o tráfego de retorno legítimo.
E) O filtro stateless analisa comandos de protocolos da camada de aplicação com maior profundidade analítica do que as soluções stateful.
// Comentário: Em um filtro estático (stateless), para permitir que clientes internos naveguem na Web, o administrador precisava abrir permanentemente uma faixa ampla de portas altas de entrada para receber o retorno dos dados, abrindo brechas para invasões externas. O filtro com inspeção de estado (stateful) soluciona essa vulnerabilidade, pois rastreia a sessão e permite a entrada unicamente dos pacotes que correspondam a conexões abertas legitimamente pelo cliente interno, mantendo as portas trancadas para o restante.

@@ a05/s01 | B
A preservação da memória corporativa e a resiliência contra desastres dependem de políticas regulares de realização de cópias de segurança de dados. Com relação ao Backup Completo (ou Total), assinale a opção correta.
A) O backup completo copia exclusivamente os arquivos de sistema criados nas últimas vinte e quatro horas por administradores da rede.
B) O backup completo realiza a cópia integral de todos os arquivos selecionados e desmarca o atributo de arquivamento de cada arquivo copiado.
C) O backup completo dispensa o uso de mídias de armazenamento persistentes, mantendo os dados exclusivamente na memória volátil RAM.
D) O backup completo impede a realização subsequente de backups incrementais e diferenciais na rotina operacional do centro de dados.
E) O backup completo é o método mais rápido para a rotina diária de gravação, exigindo menos espaço em disco do que os backups incrementais.
// Comentário: O backup completo (ou total) faz a cópia de todos os arquivos selecionados na pasta ou unidade, independentemente de terem sido modificados recentemente ou não. Ele marca os arquivos como salvos, desmarcando o atributo de arquivamento (archive bit = 0), servindo como o ponto de partida indispensável para todas as rotinas posteriores de backups incrementais e diferenciais.

@@ a05/s01 | D
Em ambientes computacionais que manipulam grandes volumes de informação, a janela de tempo disponível para a rotina de cópias de segurança pode ser exígua. Acerca do Backup Incremental, assinale a opção correta.
A) O backup incremental copia todos os arquivos da unidade a cada execução diária, ignorando o atributo de arquivamento existente.
B) O backup incremental copia todos os arquivos modificados desde o último backup completo e mantém o atributo de arquivamento inalterado.
C) O backup incremental exige apenas duas mídias físicas para restaurar todo o ambiente, mesmo após meses de operações ininterruptas.
D) O backup incremental copia os arquivos criados ou modificados desde o último backup e desmarca o atributo de arquivamento dos itens copiados.
E) O backup incremental é a modalidade que demanda maior tempo de execução diária e maior espaço de armazenamento na mídia de destino.
// Comentário: O backup incremental copia unicamente os arquivos que foram criados ou alterados desde o último backup (seja este último completo ou incremental). Ao concluir a cópia de cada arquivo, ele desmarca o atributo de arquivamento (limpando a flag de arquivo pendente de backup). Por registrar apenas as alterações recentes, é o método mais rápido e que menos ocupa espaço na rotina diária.

@@ a05/s01 | D
A escolha da metodologia de salvaguarda adequada deve equilibrar o tempo gasto na gravação periódica e a complexidade do procedimento de restauração. No que tange ao Backup Diferencial, assinale a opção correta.
A) O backup diferencial copia apenas os arquivos do sistema operacional Windows, excluindo documentos e bancos de dados de usuários.
B) O backup diferencial desmarca o atributo de arquivamento de todos os arquivos copiados, esvaziando a fila de alterações da máquina.
C) O backup diferencial grava apenas os arquivos que não foram modificados ao longo dos últimos doze meses de operação institucional.
D) O backup diferencial copia os arquivos criados ou alterados desde o último backup completo e não altera o atributo de arquivamento.
E) O backup diferencial exige a restauração sequencial de todas as fitas diárias geradas ao longo da semana para recuperar os dados.
// Comentário: O backup diferencial copia todos os arquivos que foram criados ou modificados desde o último backup completo. Crucialmente, ele NÃO desmarca o atributo de arquivamento (a flag permanece ativa). Em decorrência disso, cada backup diferencial diário acumula todas as alterações ocorridas desde o completo, tornando o arquivo diferencial progressivamente maior ao longo da semana, mas facilitando a recuperação posterior.

@@ a05/s01 | A
Na hipótese de perda catastrófica do servidor de arquivos em uma corporação, a equipe de tecnologia deve executar a reconstrução dos sistemas de dados. A respeito da restauração de dados a partir de backups incrementais e diferenciais, assinale a opção correta.
A) Para restaurar com diferencial bastam o último completo e o último diferencial; com incremental exigem-se o completo e todos os incrementais.
B) A restauração de um backup diferencial exige obrigatoriamente a leitura de todas as mídias diárias gravadas nos últimos seis meses.
C) A restauração a partir de backups incrementais dispensa o backup completo original, utilizando apenas o último incremental gravado no disco.
D) O backup incremental proporciona o processo de restauração mais veloz e simples entre todas as metodologias de cópia de segurança existentes.
E) A restauração de dados danificados em servidores de rede impede o retorno de arquivos ao estado em que se encontravam antes do incidente.
// Comentário: Para restaurar dados utilizando a rotina diferencial, são necessários apenas dois conjuntos de dados: o último backup completo e o último backup diferencial realizado antes do sinistro. Já na rotina incremental, o procedimento de restauração exige o último backup completo seguido, obrigatoriamente, de todos os backups incrementais intermediários na ordem cronológica em que foram criados.

@@ a05/s01 | E
Determinadas operações administrativas demandam a realização de cópias de segurança pontuais sem interferir no cronograma rotineiro de backups institucionais. Em relação ao Backup de Cópia (Copy Backup), assinale a opção correta.
A) O backup de cópia destina-se exclusivamente a excluir arquivos temporários do sistema operacional para liberar espaço no disco rígido.
B) O backup de cópia altera compulsoriamente os atributos de arquivamento de todos os arquivos do servidor central de centro de dados.
C) O backup de cópia desorganiza a cadeia cronológica de restauração dos backups diferenciais por desmarcar as flags de sistema.
D) O backup de cópia é um recurso exclusivo de plataformas de fitas perfuradas legadas, tendo sido banido em sistemas corporativos modernos.
E) O backup de cópia copia os arquivos selecionados sem alterar o atributo de arquivamento, preservando a rotina regular dos demais backups.
// Comentário: O backup de cópia realiza a duplicação completa dos arquivos selecionados pelo usuário ou administrador, mas tem a propriedade crucial de NÃO desmarcar nem alterar o atributo de arquivamento (archive bit). Essa característica assegura que essa cópia avulsa não interfira nem corrompa a sequência temporal planejada de backups incrementais e diferenciais da instituição.

@@ a05/s01 | D
As melhores práticas internacionais de governança de segurança recomendam diretrizes estruturadas para garantir a resiliência contra desastres físicos e cibernéticos. Quanto à clássica estratégia de salvaguarda denominada Regra 3-2-1 de Backup, assinale a opção correta.
A) A regra preconiza manter apenas três arquivos de texto em duas pastas de trabalho compactadas em um único pendrive doméstico.
B) A regra determina a retenção de dados por três anos em dois centros de dados distintos pertencentes à mesma empresa de telefonia móvel.
C) A regra estabelece que backups devem ser realizados a cada três semanas utilizando dois operadores de computação e um supervisor.
D) A regra recomenda manter três cópias dos dados em dois tipos de mídias diferentes, guardando ao menos uma cópia em local externo ou nuvem.
E) A regra veda a utilização de repositórios em nuvem pública para o armazenamento de cópias de segurança de instituições governamentais.
// Comentário: A regra 3-2-1 estabelece um padrão de excelência para continuidade de negócios: manter ao menos 3 cópias dos dados institucionais (a cópia primária de produção mais duas cópias de segurança), distribuídas em pelo menos 2 tipos de mídias de armazenamento distintas (por exemplo, disco local/NAS e fitas ou nuvem), com pelo menos 1 das cópias armazenada fora das dependências físicas da organização (offsite ou nuvem protegida).
"""
