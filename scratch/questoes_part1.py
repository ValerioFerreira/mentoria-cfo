"""Part 1: Questions 1 to 30 for informatica
Segments:
- informatica/a00/s01: Q1 to Q6
- informatica/a01/s02: Q7 to Q12
- informatica/a02/s01: Q13 to Q18
- informatica/a02/s02: Q19 to Q24
- informatica/a02/s03: Q25 to Q30
"""

QUESTOES_P1 = """
@@ a00/s01 | A
A ARPANET, precursora histórica da Internet desenvolvida no final da década de 1960, introduziu uma mudança paradigmática na forma como os dados trafegavam pelas redes de comunicação. Com relação à arquitetura de comutação adotada na Internet e às suas características fundamentais, assinale a opção correta.
A) A comutação por pacotes divide a informação em blocos autônomos que percorrem rotas dinâmicas e independentes na rede.
B) A comutação por circuitos estabelece uma linha física dedicada que permanece reservada e exclusiva durante todo o tráfego de dados.
C) A comutação por pacotes exige que todos os fragmentos da mensagem transitem obrigatoriamente pela mesma rota física pré-estabelecida.
D) A comutação por circuitos apresenta maior tolerância a falhas físicas do que a comutação por pacotes em caso de ruptura de enlace.
E) A comutação por pacotes mantém o canal de transmissão permanentemente ocupado mesmo durante os períodos em que não há tráfego de dados.
// Comentário: A alternativa A está correta porque a Internet adota comutação por pacotes, na qual as informações são fragmentadas em unidades independentes (pacotes) capazes de utilizar caminhos dinâmicos até o destino. A alternativa B erra ao descrever o modelo telefônico de circuitos como base da Internet. A alternativa C é incorreta porque os pacotes podem seguir rotas distintas. A alternativa D é falsa, pois circuitos caem quando a linha falha, enquanto pacotes desviam da falha. A alternativa E erra ao atribuir o desperdício de canal ocioso à comutação por pacotes.

@@ a00/s01 | B
As redes de computadores podem ser classificadas quanto à sua abrangência geográfica em diferentes categorias, como PAN, LAN, MAN e WAN. A respeito das características de uma Rede Local (Local Area Network - LAN), assinale a opção correta.
A) As redes LAN cobrem distâncias intercontinentais e dependem exclusivamente de linhas de transmissão alugadas de operadoras públicas de telecomunicação.
B) As redes LAN limitam-se a uma área geográfica restrita, como um prédio ou campus, podendo utilizar meios de transmissão cabeados ou sem fio.
C) As redes LAN prescindem inteiramente do protocolo TCP/IP, operando unicamente por meio de conexões diretas ponto a ponto sem roteamento.
D) As redes LAN caracterizam-se por apresentar taxas de transmissão sensivelmente mais baixas e taxas de erro mais altas do que as redes WAN.
E) As redes LAN suportam exclusivamente enlaces físicos com cabeamento de par trançado, sendo incompatíveis com tecnologias de transmissão sem fio.
// Comentário: A alternativa B está correta, pois a LAN (Local Area Network) abrange áreas geograficamente limitadas (como escritórios, residências ou campi corporativos) e suporta tecnologias cabeadas (Ethernet) e sem fio (WLAN). A alternativa A define uma WAN. A alternativa C erra porque LANs utilizam amplamente a pilha TCP/IP. A alternativa D inverte os conceitos, pois LANs possuem alta velocidade e baixas taxas de erro. A alternativa E erra ao afirmar que LANs não aceitam conexões sem fio.

@@ a00/s01 | C
Embora sejam frequentemente tratados de forma indistinta na linguagem cotidiana, os conceitos de Internet e World Wide Web (WWW) possuem definições técnicas e papéis estruturais distintos na computação. Acerca da relação entre a Internet e seus serviços, assinale a opção correta.
A) A Internet e a World Wide Web são termos sinônimos que descrevem a mesma aplicação de navegação criada no início da década de 1990.
B) A World Wide Web constitui a infraestrutura física de cabeamento submarino e roteadores que viabiliza a transmissão global de dados brutos.
C) A World Wide Web é um dos serviços suportados pela Internet, baseado em páginas de hipertexto acessadas por meio do protocolo HTTP ou HTTPS.
D) A Internet foi desenvolvida exclusivamente para hospedar websites na Web, sendo incompatível com outros serviços como o correio eletrônico.
E) A World Wide Web antecedeu historicamente a Internet, tendo fornecido a base física para a subsequente criação da rede militar ARPANET.
// Comentário: A alternativa C está correta, visto que a Web (WWW) é apenas uma das diversas aplicações que operam sobre a infraestrutura da Internet, baseando-se em hipertexto e protocolos como HTTP e HTTPS. A alternativa A erra ao tratar os termos como sinônimos. A alternativa B descreve a infraestrutura física da Internet, e não a Web. A alternativa D é incorreta porque outros serviços (como e-mail e FTP) operam na Internet e muitos até antecederam a Web. A alternativa E inverte a cronologia histórica.

@@ a00/s01 | D
Para interligar estações de trabalho e centros de dados situados em diferentes municípios, estados ou países, as organizações utilizam infraestruturas de telecomunicações de grande escala. Quanto às características operacionais das redes de longa distância (Wide Area Network - WAN), assinale a opção correta.
A) As redes WAN operam com enlaces de curtíssimo alcance físico, não ultrapassando a distância perimetral de cinquenta metros entre seus nós.
B) As redes WAN dispensam a presença de roteadores e gateways, realizando toda a comunicação por difusão direta em enlaces de camada física.
C) As redes WAN são restritas a ambientes residenciais, não comportando tráfego interurbano ou enlaces via satélite e fibras ópticas submarinas.
D) As redes WAN cobrem extensas áreas geográficas, conectando cidades e continentes, sendo a própria Internet o exemplo clássico dessa arquitetura.
E) As redes WAN caracterizam-se por dispensar mecanismos de controle de segurança, já que sua infraestrutura física é inteiramente privada.
// Comentário: A alternativa D está correta, pois a WAN (Wide Area Network) é caracterizada pela cobertura de amplas extensões territoriais (cidades, países e continentes), tendo a Internet como seu maior exemplo. A alternativa A confunde WAN com PAN. A alternativa B erra ao desconsiderar roteadores e gateways, indispensáveis para interconectar sub-redes em WANs. A alternativa C erra ao restringir a WAN a ambientes residenciais. A alternativa E é falsa, pois enlaces de longa distância exigem rigorosos mecanismos de proteção.

@@ a00/s01 | E
Dispositivos móveis, como smartphones, fones de ouvido sem fio e relógios inteligentes, costumam comunicar-se diretamente em distâncias curtas sem demandar infraestrutura de roteamento complexa. Acerca das Redes de Área Pessoal (Personal Area Network - PAN), assinale a opção correta.
A) A rede PAN é projetada para conectar matrizes corporativas e filiais industriais distribuídas em múltiplos polos de uma região metropolitana.
B) A rede PAN é implementada exclusivamente por meio de cabos de fibra óptica monomodo conectados a comutadores de núcleo de alta densidade.
C) A rede PAN abrange distâncias de centenas de quilômetros, operando com protocolos complexos de comutação por rótulos multiprotocolo.
D) A rede PAN impede a comunicação direta ponto a ponto entre aparelhos pessoais, exigindo intermediação por satélites geoestacionários.
E) A rede PAN atende ao espaço pessoal de um indivíduo em distâncias de poucos metros, tendo na tecnologia Bluetooth sua principal implementação sem fio.
// Comentário: A alternativa E está correta, visto que a PAN (Personal Area Network) conecta equipamentos no espaço pessoal do usuário em raios curtos de poucos metros, sendo o padrão Bluetooth (WPAN) seu expoente mais comum. A alternativa A define uma MAN. As alternativas B e C descrevem características incompatíveis com redes pessoais de curta distância. A alternativa D erra ao exigir enlaces via satélite para comunicação pessoal.

@@ a00/s01 | A
A maior parte das aplicações convencionais da Internet, como a navegação em portais institucionais e o envio de mensagens, opera segundo modelos estruturados de comunicação em rede. Em relação à arquitetura cliente/servidor, assinale a opção correta.
A) O modelo cliente/servidor baseia-se na separação entre as entidades que solicitam recursos e os nós dedicados a prestar e gerenciar esses serviços.
B) O modelo cliente/servidor veda a conexão simultânea de múltiplos clientes ao mesmo nó prestador de serviços na infraestrutura corporativa.
C) O modelo cliente/servidor exige que os clientes armazenem previamente cópias idênticas e completas de todas as bases de dados corporativas.
D) O modelo cliente/servidor opera de forma simétrica, impedindo que haja servidores dedicados a funções especializadas na rede institucional.
E) O modelo cliente/servidor inviabiliza o compartilhamento de recursos computacionais centralizados, obrigando a redundância local de arquivos.
// Comentário: A alternativa A está correta, pois a arquitetura cliente/servidor fundamenta-se na distinção entre clientes (que requisitam dados ou processamento) e servidores (que processam as solicitações e fornecem os recursos de forma centralizada). A alternativa B erra porque servidores atendem múltiplos clientes simultaneamente. A alternativa C é incorreta, pois a centralização dos dados no servidor evita cópias completas nos clientes. As alternativas D e E contradizem os princípios básicos da arquitetura cliente/servidor.

@@ a01/s02 | B
A interconexão entre as redes internas corporativas e o ecossistema externo demanda soluções arquiteturais que combinem acessibilidade e restrição de privilégios. Com relação ao conceito e às características de uma Extranet, assinale a opção correta.
A) A extranet é uma rede completamente pública e aberta que dispensa mecanismos de identificação e autorização para qualquer internauta.
B) A extranet representa uma extensão controlada da intranet corporativa, permitindo acesso externo restrito a parceiros, clientes ou fornecedores autorizados.
C) A extranet opera isolada da Internet em meio físico estritamente exclusivo, sem trafegar dados por provedores públicos de telecomunicações.
D) A extranet concede aos usuários externos os mesmos privilégios irrestritos de configuração administrativa atribuídos aos servidores centrais.
E) A extranet impede a comunicação entre sistemas heterogêneos de diferentes organizações, restringindo-se ao tráfego de páginas institucionais estáticas.
// Comentário: A alternativa B está correta, pois a extranet consubstancia uma extensão segura e delimitada da intranet corporativa sobre a Internet, concedendo acesso controlado a entidades externas homologadas (fornecedores, clientes e parceiros). A alternativa A confunde extranet com portal web público. A alternativa C erra porque a extranet utiliza a infraestrutura pública da Internet. As alternativas D e E erram sobre os níveis de privilégio e a integração de sistemas na extranet.

@@ a01/s02 | C
Em um cenário corporativo moderno, diferentes perfis de usuários acessam recursos institucionais a partir de múltiplos ambientes físicos e lógicos. A respeito da distinção entre Intranet, Extranet e Portal Web Público, assinale a opção correta.
A) O acesso de qualquer cidadão a um sítio público governamental com formulário aberto de notícias configura uma conexão típica de intranet.
B) O colaborador em trabalho presencial conectado à rede local corporativa realiza acesso por extranet devido à natureza física do tráfego.
C) O parceiro comercial homologado que acessa o sistema de faturamento corporativo mediante credenciais autorizadas opera no ambiente de extranet.
D) A existência de uma tela de login em um portal comercial aberto na Internet transforma automaticamente a navegação do internauta em intranet.
E) Os conceitos de intranet e extranet são idênticos em privilégios, dispensando a delimitação de perímetros e regras de controle de acesso.
// Comentário: A alternativa C está correta, uma vez que o acesso de parceiros homologados a módulos específicos de negócio constitui o núcleo da definição de extranet. A alternativa A erra, pois sítio aberto é portal web público. A alternativa B erra, pois funcionário na rede física interna acessa a intranet local. A alternativa D é uma clássica pegadinha: telas de login em portais públicos não configuram intranet. A alternativa E ignora a distinção fundamental de escopo e perfis de acesso.

@@ a01/s02 | D
Para viabilizar a comunicação segura entre matriz e filiais distribuídas por diferentes regiões geográficas, as corporações comumente utilizam Redes Privadas Virtuais (VPN). Acerca da arquitetura de VPN Site-to-Site, assinale a opção correta.
A) A VPN Site-to-Site conecta dispositivos móveis individuais isolados a um concentrador central, exigindo discagem manual a cada transmissão.
B) A VPN Site-to-Site prescinde de mecanismos de criptografia, dependendo unicamente da confiança mútua entre os provedores de acesso à Internet.
C) A VPN Site-to-Site inviabiliza a comunicação entre sub-redes corporativas completas, limitando-se ao espelhamento de um único computador de borda.
D) A VPN Site-to-Site interliga redes locais completas de modo transparente aos usuários finais por meio de concentradores ou roteadores de borda.
E) A VPN Site-to-Site requer a instalação de softwares clientes de conexão privativa em cada estação de trabalho individual de todas as filiais.
// Comentário: A alternativa D está correta, já que a VPN Site-to-Site conecta redes inteiras (como matriz e filiais) por meio de gateways/roteadores de borda de forma transparente para os computadores internos. A alternativa A descreve o modelo Client-to-Site (acesso remoto). A alternativa B erra porque VPNs empregam criptografia e tunelamento. As alternativas C e E erram ao exigir clientes individuais em cada máquina final para uma topologia Site-to-Site.

@@ a01/s02 | E
Servidores públicos em regime de teletrabalho frequentemente necessitam acessar repositórios internos e bancos de dados da instituição a partir de seus computadores portáteis residenciais. No que se refere à topologia de VPN Client-to-Site, assinale a opção correta.
A) A conexão Client-to-Site prescinde de autenticação de credenciais do usuário, confiando no endereço IP doméstico atribuído pelo provedor.
B) A conexão Client-to-Site estabelece um túnel permanente entre dois comutadores físicos centrais sem suporte a estações de trabalho isoladas.
C) A conexão Client-to-Site transmite os dados corporativos em texto claro pela Internet pública, sem aplicar camadas adicionais de encapsulamento.
D) A conexão Client-to-Site veda o acesso a pastas compartilhadas e correios eletrônicos da intranet, limitando-se à navegação em sítios abertos.
E) A conexão Client-to-Site interliga um dispositivo terminal remoto à rede corporativa central mediante software cliente autenticado e canal seguro.
// Comentário: A alternativa E está correta, pois a modalidade Client-to-Site (ou de acesso remoto) conecta com segurança um equipamento individual à rede da instituição por meio de um aplicativo cliente e canal criptografado. A alternativa A erra porque a autenticação forte do usuário é indispensável. A alternativa B descreve a topologia Site-to-Site. A alternativa C é falsa, pois a VPN cifra e encapsula o tráfego. A alternativa D é incorreta, pois o objetivo do túnel é justamente acessar os recursos internos da rede.

@@ a01/s02 | A
As Redes Privadas Virtuais utilizam uma combinação coordenada de técnicas para garantir que o tráfego confidencial transite por redes públicas desprotegidas. Em relação aos papéis desempenhados pelo tunelamento e pela criptografia em uma VPN, assinale a opção correta.
A) O tunelamento encapsula os pacotes corporativos em envelopes de transporte, enquanto a criptografia assegura o sigilo contra leitura indevida.
B) O tunelamento é responsável exclusivo pela garantia da confidencialidade, ao passo que a criptografia atua apenas no roteamento físico dos pacotes.
C) O tunelamento elimina a necessidade de cabeçalhos de rede, enquanto a criptografia converte os dados em sinal óptico nos comutadores de borda.
D) A criptografia dispensa o uso de chaves computacionais em túneis VPN, limitando-se a reorganizar a sequência dos bits transmitidos no enlace.
E) O tunelamento e a criptografia operam de forma idêntica, sendo termos sinônimos que descrevem a compressão sem perdas de arquivos transmitidos.
// Comentário: A alternativa A está correta, pois o tunelamento encapsula o pacote original dentro de um novo invólucro de dados para transitar por redes intermediárias, enquanto a criptografia protege o conteúdo garantindo a sua confidencialidade. A alternativa B inverte as atribuições técnicas. A alternativa C erra sobre cabeçalhos e conversão óptica. A alternativa D erra ao dispensar chaves criptográficas. A alternativa E erra ao tratar os dois conceitos como sinônimos.

@@ a01/s02 | B
A implantação de canais de comunicação corporativa do tipo Extranet visa otimizar processos operacionais que envolvem agentes externos integrados à rotina de uma organização. Quanto às aplicações típicas de uma Extranet corporativa, assinale a opção correta.
A) A extranet destina-se primordialmente ao envio indiscriminado de campanhas publicitárias de marketing direto para o público em geral.
B) A extranet viabiliza a integração da cadeia de suprimentos e o intercâmbio eletrônico de dados B2B entre parceiros comerciais homologados.
C) A extranet tem como propósito central substituir os servidores de correio eletrônico e hospedar jogos corporativos interativos para terceiros.
D) A extranet restringe-se a hospedar o catálogo institucional estático de produtos da corporação com acesso livre de navegadores convencionais.
E) A extranet opera exclusivamente na camada de enlace físico, sendo incapaz de suportar módulos transacionais de faturamento ou controle de estoque.
// Comentário: A alternativa B está correta, pois as principais finalidades da extranet englobam a gestão da cadeia de suprimentos (supply chain), transações Business-to-Business (B2B) e compartilhamento de processos logísticos com parceiros homologados. A alternativa A confunde extranet com spam comercial. A alternativa C erra ao desvirtuar a finalidade do recurso. A alternativa D descreve um site institucional aberto. A alternativa E erra ao negar o suporte a aplicações transacionais corporativas.

@@ a02/s01 | C
Uma organização implementa diferentes categorias de barreiras defensivas para proteger suas instalações físicas e seus ativos lógicos contra acessos não autorizados. No que tange à distinção entre controles físicos e lógicos em segurança da informação, assinale a opção correta.
A) A utilização de fechaduras com leitor biométrico para ingresso físico em uma sala de servidores constitui um exemplo de controle puramente lógico.
B) A adoção de senhas complexas e de barreiras de firewall de borda para proteger o acesso a sistemas computacionais configura um controle físico.
C) Os controles físicos representam barreiras tangíveis que limitam a aproximação humana aos ativos, enquanto os controles lógicos operam no meio digital.
D) Os controles lógicos dispensam o processamento computacional, consistindo exclusivamente em vigilância patrimonial humana e portas blindadas.
E) As catracas eletrônicas e os sistemas de circuito fechado de televisão (CFTV) são classificados tecnicamente como controles de natureza lógica.
// Comentário: A alternativa C está correta, pois controles físicos são barreiras materiais tangíveis (portas, catracas, salas-cofre, CFTV) e controles lógicos são soluções tecnológicas/digitais (senhas, firewalls, criptografia, ACLs). A alternativa A erra, pois a biometria usada para entrada física em sala é controle físico. A alternativa B inverte o conceito, pois senhas e firewalls são controles lógicos. As alternativas D e E confundem as atribuições de cada tipo de controle.

@@ a02/s01 | D
A gestão de segurança da informação baseia-se na compreensão das relações de dependência e causalidade entre ativos, vulnerabilidades, ameaças e incidentes. Com relação a esses conceitos fundamentais, assinale a opção correta.
A) A vulnerabilidade representa a concretização efetiva de um dano patrimonial resultante da atuação destrutiva de um código malicioso.
B) A ameaça é uma fragilidade interna de um ativo computacional que decorre da ausência de atualizações periódicas no sistema operacional.
C) O ativo compreende exclusivamente os equipamentos de hardware instalados nos centros de processamento de dados da organização.
D) A vulnerabilidade é uma fraqueza que reduz a resistência de um ativo, a qual pode ser explorada por uma ameaça para desencadear um incidente.
E) O incidente de segurança caracteriza-se como a probabilidade matemática teórica de que uma falha de sistema venha a ser detectada no futuro.
// Comentário: A alternativa D está correta, definindo perfeitamente a vulnerabilidade como uma falha ou fraqueza existente que pode ser explorada por um agente de ameaça para gerar um incidente. A alternativa A confunde vulnerabilidade com impacto ou incidente consumado. A alternativa B confunde ameaça com vulnerabilidade. A alternativa C erra ao restringir ativos ao hardware (inclui dados, processos, pessoas e documentos). A alternativa E define risco ou probabilidade, não incidente.

@@ a02/s01 | E
Além dos dispositivos de infraestrutura física e das ferramentas de software de proteção, as organizações dependem de normas comportamentais e procedimentos operacionais formais. A respeito dos controles administrativos ou organizacionais, assinale a opção correta.
A) Os controles administrativos limitam-se ao fornecimento de baterias auxiliares e nobreaks contra interrupções na rede de energia elétrica.
B) Os controles administrativos são compostos exclusivamente por placas de rede e cabos blindados de transmissão instalados nos roteadores.
C) Os controles administrativos correspondem aos algoritmos matemáticos empregados na cifragem de discos rígidos em computadores portáteis.
D) Os controles administrativos restringem-se ao uso de câmeras com sensores de movimento instaladas no perímetro externo dos edifícios.
E) Os controles administrativos compreendem políticas de segurança da informação, termos de sigilo e programas de conscientização corporativa.
// Comentário: A alternativa E está correta, pois controles administrativos ou organizacionais abrangem diretrizes formais, normas internas, Políticas de Segurança da Informação (PSI), termos de confidencialidade (NDA) e programas de capacitação e conscientização contra engenharia social. As alternativas A, B, C e D descrevem controles físicos ou lógicos.

@@ a02/s01 | A
Os mecanismos de salvaguarda de dados podem ser classificados de acordo com a função temporal que desempenham no ciclo de vida de um incidente de segurança. Quanto aos controles preventivos, detectivos e corretivos, assinale a opção correta.
A) Os controles preventivos atuam de forma proativa para impedir que vulnerabilidades sejam exploradas e que incidentes venham a se consumar.
B) Os controles detectivos têm como objetivo exclusivo reparar os arquivos corrompidos e restaurar backups após a concretização de um desastre.
C) Os controles corretivos operam emitindo avisos imediatos em tempo real no momento exato em que uma violação perimetral está em andamento.
D) Os controles preventivos são acionados apenas após a constatação de prejuízos materiais para avaliar a magnitude do impacto patrimonial.
E) Os controles detectivos impedem fisicamente a ocorrência de qualquer tentativa de invasão, dispensando a geração de registros de auditoria.
// Comentário: A alternativa A está correta, pois os controles preventivos agem para evitar que o incidente ocorra (ex.: políticas de senhas fortes, firewalls e treinamento). A alternativa B descreve controles corretivos. A alternativa C descreve controles detectivos. As alternativas D e E invertem a atuação e as propriedades dos mecanismos preventivos e detectivos.

@@ a02/s01 | B
A análise e o tratamento de riscos constituem etapas estruturantes para a alocação eficiente de investimentos em segurança da informação em uma instituição. Acerca do conceito de risco em segurança da informação, assinale a opção correta.
A) O risco equivale numericamente ao custo monetário bruto de substituição de todos os equipamentos de tecnologia presentes na organização.
B) O risco reflete a probabilidade de uma ameaça concretizar-se mediante a exploração de uma vulnerabilidade, associada ao impacto correspondente.
C) O risco existe apenas nas situações em que um incidente já foi consumado com destruição completa das bases de dados corporativas.
D) O risco é um elemento estático que não se altera com a implementação de controles adicionais de segurança ou com a atualização de softwares.
E) O risco depende unicamente da quantidade de computadores conectados à rede, sendo indiferente à natureza e à criticidade das informações manipuladas.
// Comentário: A alternativa B está correta, pois em conformidade com as normas ISO/IEC 27005, o risco computacional resulta da combinação entre a probabilidade de uma ameaça explorar determinada vulnerabilidade de um ativo e o impacto negativo gerado sobre a instituição. A alternativa A confunde risco com valor contábil dos ativos. A alternativa C erra porque o risco é potencial e antecede o incidente. As alternativas D e E ignoram a dinâmica de mitigação e o valor intrínseco dos ativos protegidos.

@@ a02/s01 | C
As normas internacionais da família ISO/IEC 27000 e o Decreto federal nº 9.637/2018 (Política Nacional de Segurança da Informação) balizam as práticas de governança de segurança. No que se refere ao escopo institucional da segurança da informação, assinale a opção correta.
A) A segurança da informação restringe sua atuação aos ativos codificados digitalmente em sistemas de bancos de dados relacionais corporativos.
B) A segurança da informação desconsidera comunicações verbais e o conhecimento tácito dos colaboradores, focando apenas no hardware de rede.
C) A segurança da informação protege o patrimônio informativo em seus múltiplos suportes, incluindo registros digitais, documentos impressos e pessoas.
D) A segurança da informação subordina a integridade e a disponibilidade dos dados à confidencialidade, estabelecendo esta como único pilar válido.
E) A segurança da informação exime a administração pública de adotar medidas defensivas contra ameaças originadas em seu ambiente interno.
// Comentário: A alternativa C está correta, pois a disciplina de segurança da informação abrange a proteção dos dados em qualquer formato ou meio: eletrônico, físico (papel), comunicações orais e recursos humanos. As alternativas A e B erram ao restringir o escopo ao meio digital ou hardware. A alternativa D erra ao estabelecer hierarquia entre os pilares fundamentais. A alternativa E contraria expressamente a PNSI e as boas práticas de gestão de segurança pública.

@@ a02/s02 | D
A preservação das propriedades intrínsecas da informação constitui o objetivo primário das práticas de segurança em ambientes corporativos e públicos. Com relação ao princípio da integridade, assinale a opção correta.
A) A integridade assegura que a informação seja mantida em segredo absoluto, tornando-a inacessível até mesmo para os usuários autorizados do sistema.
B) A integridade é violada no momento em que um usuário não autorizado simplesmente visualiza o conteúdo de uma mensagem sem realizar qualquer alteração.
C) A integridade e a confidencialidade são princípios interdependentes, de modo que a violação da confidencialidade acarreta necessariamente a perda da integridade.
D) A integridade garante que a informação não foi modificada, corrompida ou excluída de maneira desautorizada ao longo de todo o seu ciclo de vida.
E) A integridade limita-se a monitorar o tempo de resposta das consultas efetuadas aos bancos de dados nos servidores centrais de produção.
// Comentário: A alternativa D está correta, pois a integridade garante a exatidão, originalidade e completeza da informação, assegurando que ela permaneça sem alterações ou exclusões desautorizadas desde a origem. A alternativa A descreve confidencialidade extrema. A alternativa B descreve violação de confidencialidade (a integridade foi mantida se o texto não mudou). A alternativa C é uma pegadinha clássica: integridade e confidencialidade são independentes. A alternativa E confunde integridade com métricas de desempenho.

@@ a02/s02 | E
A continuidade das operações institucionais requer que os recursos tecnológicos permaneçam operacionais e aptos a atender às demandas de serviços. No que tange ao princípio da disponibilidade, assinale a opção correta.
A) A disponibilidade visa garantir que apenas administradores com privilégios máximos consigam visualizar os dados cadastrais da instituição.
B) A disponibilidade impede a realização de cópias de segurança em locais remotos para evitar que a informação se disperse na infraestrutura de rede.
C) A disponibilidade estabelece que as bases de dados devem ser desativadas periodicamente para impedir a ocorrência de acessos concomitantes.
D) A disponibilidade concentra-se exclusivamente em atestar a autenticidade jurídica da identidade digital dos remetentes de mensagens eletrônicas.
E) A disponibilidade assegura que os dados e sistemas estejam acessíveis e utilizáveis sempre que demandados por entidades devidamente autorizadas.
// Comentário: A alternativa E está correta, pois a disponibilidade garante o acesso oportuno e confiável aos dados e serviços sempre que requisitados por usuários, processos ou sistemas autorizados. A alternativa A descreve confidencialidade. A alternativa B contraria as práticas de backup, que sustentam a disponibilidade. A alternativa C prejudica diretamente a disponibilidade. A alternativa D refere-se à autenticidade ou irretratabilidade.

@@ a02/s02 | A
Em transações eletrônicas e processos administrativos digitais, a segurança jurídica depende da garantia de que as partes não possam recusar a autoria de seus atos. Acerca dos princípios de autenticidade e irretratabilidade (não repúdio), assinale a opção correta.
A) A irretratabilidade impede que o emissor negue ter enviado a mensagem, decorrendo da presença conjunta de autenticidade e integridade.
B) A autenticidade e a irretratabilidade são conceitos perfeitamente sinônimos, referindo-se unicamente ao tempo de vigência de certificados de rede.
C) A autenticidade assegura a confidencialidade do conteúdo transmitido, impedindo que qualquer entidade intercepte os pacotes no enlace.
D) A irretratabilidade é uma propriedade física alcançada exclusivamente pela redundância de fontes de alimentação e geradores elétricos.
E) A autenticidade de origem prescinde da identificação do emissor, validando apenas o endereço MAC dos comutadores intermediários da rede.
// Comentário: A alternativa A está correta, pois a irretratabilidade (não repúdio) impede a negação da autoria ou do envio de uma comunicação, sendo obtida tecnicamente pela soma de autenticidade (prova de quem enviou) e integridade (prova de que a mensagem não foi alterada): Autenticidade + Integridade = Irretratabilidade. A alternativa B erra ao tratá-las como sinônimos. A alternativa C confunde autenticidade com confidencialidade. A alternativa D confunde irretratabilidade com disponibilidade. A alternativa E erra ao afirmar que a autenticidade dispensa a identificação do autor.

@@ a02/s02 | B
A investigação de incidentes cibernéticos em uma corporação exige a capacidade de reconstruir cronologicamente todos os eventos e acessos ocorridos nos sistemas. Em relação à rastreabilidade e à gestão de trilhas de auditoria (logs), assinale a opção correta.
A) Os registros de auditoria devem ser salvos nas mesmas tabelas de usuários operacionais, permitindo que operadores comuns editem entradas antigas.
B) A confiabilidade dos logs de auditoria requer armazenamento em regime de somente anexação, sincronização por NTP e controle rigoroso de acesso.
C) A rastreabilidade é assegurada pela exclusão rotineira de registros com mais de vinte e quatro horas para evitar sobrecarga de armazenamento.
D) A sincronização temporal dos servidores é dispensável para a análise pericial de trilhas de auditoria em ambientes corporativos distribuídos.
E) Os arquivos de log constituem evidências descartáveis em processos forenses, sendo vedada sua apresentação em procedimentos administrativos.
// Comentário: A alternativa B está correta, visto que os logs de auditoria devem manter integridade e imutabilidade (política append-only), isolamento de armazenamento em relação a tabelas comuns, sincronização temporal rigorosa (Network Time Protocol - NTP) e controle restrito de acesso. A alternativa A facilita a adulteração de provas. A alternativa C prejudica a retenção e a memória dos fatos. As alternativas D e E erram sobre a importância forense e temporal dos registros.

@@ a02/s02 | C
As violações de segurança da informação podem ser classificadas conforme o tipo de interferência praticada pelo invasor sobre o fluxo regular de comunicação. No que concerne aos tipos de ataques e aos princípios correspondentes violados, assinale a opção correta.
A) Um ataque de interceptação passiva que apenas realiza a leitura de pacotes em trânsito compromete primordialmente a integridade dos dados.
B) Um ataque de interrupção que derruba um servidor de correio eletrônico corporativo compromete diretamente a confidencialidade do sistema.
C) Um ataque de modificação no qual o atacante altera o valor de uma transferência bancária em trânsito viola diretamente a integridade.
D) Um ataque de fabricação em que o invasor forja a transmissão de ordens fraudulentas atinge exclusivamente o princípio da disponibilidade.
E) Um ataque de negação de serviço atua preservando a disponibilidade enquanto promove a violação contínua da confidencialidade corporativa.
// Comentário: A alternativa C está correta, pois a adulteração não autorizada de dados em trânsito ou repouso configura ataque de modificação e fere a integridade. A alternativa A erra porque a leitura sem alteração fere a confidencialidade. A alternativa B erra porque derrubar serviços fere a disponibilidade. A alternativa D erra porque fabricar dados fingindo ser outra pessoa compromete a autenticidade. A alternativa E inverte os efeitos do ataque de negação de serviço (DoS).

@@ a02/s02 | D
Modelos conceituais avançados de segurança da informação, como o Hexagrama Parkeriano formulado por Donn B. Parker, expandem os atributos da tríade clássica para avaliar novos aspectos de proteção. Quanto aos atributos propostos por Parker, assinale a opção correta.
A) O modelo de Parker rejeita os princípios clássicos de confidencialidade e integridade, substituindo-os por métricas puramente contábeis.
B) A utilidade refere-se à retenção do controle físico de um dispositivo móvel, independentemente de os dados nele contidos estarem legíveis.
C) A posse ou controle determina a velocidade em megabits por segundo com que um determinado link de dados opera em momentos de pico.
D) O atributo de posse ou controle diz respeito a quem detém a custódia do dado, ao passo que a utilidade avalia se a informação serve ao seu propósito.
E) A perda de posse de uma mídia criptografada acarreta obrigatoriamente a destruição física irreversível de todos os dados do proprietário.
// Comentário: A alternativa D está correta, pois no Hexagrama Parkeriano o atributo de posse/controle verifica quem efetivamente detém o meio físico ou acesso ao ativo (ex.: celular corporativo furtado), e a utilidade avalia se a informação pode ser efetivamente aproveitada pelo titular (dados intactos mas em formato ilegível perdem a utilidade). As alternativas A, B e C distorcem os conceitos. A alternativa E é falsa, pois dados criptografados numa mídia perdida mantêm sua integridade e confidencialidade caso a chave não seja comprometida.

@@ a02/s03 | E
A preservação da privacidade e a salvaguarda de conteúdos sensíveis apoiam-se em diferentes ramos teóricos e práticos da criptologia. A respeito da distinção conceitual entre Criptografia e Esteganografia, assinale a opção correta.
A) A esteganografia atua na cifragem matemática do conteúdo, tornando explícita aos olhos de qualquer observador a existência da cifra.
B) A criptografia baseia-se exclusivamente na inserção de dados em pixels de imagens digitais, dispensando o emprego de chaves lógicas.
C) A esteganografia e a criptografia são técnicas mutuamente exclusivas que não podem ser aplicadas de maneira combinada sobre uma mensagem.
D) A criptografia oculta o próprio canal de transmissão, enquanto a esteganografia altera a chave privada do usuário a cada byte enviado.
E) A esteganografia camufla a própria existência da mensagem em outro meio portador, ao passo que a criptografia torna o conteúdo ininteligível.
// Comentário: A alternativa E está correta, pois a esteganografia oculta a existência do tráfego ou da mensagem dentro de outro arquivo ou veículo aparentemente inofensivo (fotos, áudio, espaços), enquanto a criptografia torna o texto claro ininteligível (cifrado), deixando explícito que há uma mensagem protegida sendo transmitida. A alternativa A inverte a definição. As alternativas B, C e D erram sobre os mecanismos e a possibilidade de combinar as duas técnicas.

@@ a02/s03 | A
A criptografia simétrica fundamenta-se na utilização de um elemento de segredo compartilhado entre os polos de uma comunicação privativa. No que diz respeito às características operacionais da criptografia simétrica, assinale a opção correta.
A) A criptografia simétrica utiliza uma única chave secreta compartilhada para cifrar e decifrar os dados, destacando-se pela velocidade de processamento.
B) A criptografia simétrica emprega pares distintos de chaves públicas e privadas, sendo inadequada para a transmissão de grandes volumes de dados.
C) A criptografia simétrica viabiliza por si só o não repúdio pleno, já que apenas uma das partes possui acesso legítimo à chave compartilhada.
D) Os algoritmos RSA e ECC são exemplos clássicos de cifras simétricas padronizadas internacionalmente para a cifragem de discos magnéticos.
E) A criptografia simétrica elimina a necessidade de canais prévios de distribuição de chaves, permitindo a divulgação irrestrita de seu segredo.
// Comentário: A alternativa A está correta, pois a criptografia simétrica (de chave secreta) utiliza a mesma chave para cifrar e decifrar mensagens, caracterizando-se por seu baixo custo computacional e rapidez ao processar grandes volumes de dados (ex.: AES). A alternativa B descreve a criptografia assimétrica. A alternativa C é incorreta, pois ambas as partes conhecem a mesma chave, inviabilizando o não repúdio intrínseco. A alternativa D cita algoritmos assimétricos. A alternativa E ignora o clássico problema da distribuição segura de chaves simétricas.

@@ a02/s03 | B
Em uma corporação composta por múltiplos departamentos, a equipe de infraestrutura avalia a complexidade de gerenciamento de chaves para viabilizar comunicações privativas entre os colaboradores. A respeito da escalabilidade e distribuição de chaves na criptografia simétrica, assinale a opção correta.
A) O número de chaves secretas necessárias para conectar privativamente n usuários por criptografia simétrica é expresso pela fórmula 2n.
B) Para conectar n usuários aos pares de maneira estritamente privativa, o ecossistema puramente simétrico demanda um total de n(n - 1) / 2 chaves.
C) O gerenciamento de chaves simétricas é mais escalável que o assimétrico, exigindo menos chaves à medida que a quantidade de nós se expande.
D) A troca de chaves simétricas por canais abertos e não seguros é uma prática recomendada pelas normas internacionais de segurança da informação.
E) A adição de novos membros a uma rede simétrica dispensa a geração de chaves adicionais para o estabelecimento de novas comunicações seguras.
// Comentário: A alternativa B está correta, pois a fórmula matemática de combinações simples para conectar n participantes aos pares com chaves simétricas exclusivas é C(n, 2) = n(n - 1) / 2. A alternativa A cita a fórmula do modelo assimétrico (que exige 2n chaves, uma pública e uma privada por usuário). A alternativa C erra porque o modelo simétrico é de difícil escalabilidade em redes grandes. As alternativas D e E violam preceitos criptográficos essenciais.

@@ a02/s03 | C
A criptografia assimétrica baseia-se em fundamentos matemáticos que envolvem o emprego de um par de chaves complementares associadas a cada entidade participante. Acerca da utilização das chaves no paradigma de chave pública, assinale a opção correta.
A) Para garantir a confidencialidade no envio de uma mensagem, o emissor deve cifrar o conteúdo utilizando a sua própria chave privada.
B) Para assinar digitalmente um documento com garantia de autenticidade, o remetente deve cifrar o resumo criptográfico com a chave pública do receptor.
C) Para assegurar a confidencialidade na comunicação, o remetente deve cifrar o texto claro utilizando a chave pública do destinatário.
D) A chave privada de um usuário deve ser publicada em repositórios abertos de acesso irrestrito para viabilizar a validação de assinaturas por terceiros.
E) O que é cifrado com a chave pública de um usuário só pode ser decifrado utilizando-se essa mesma chave pública nos sistemas de destino.
// Comentário: A alternativa C está correta, pois para alcançar a confidencialidade no modelo assimétrico, cifra-se a mensagem com a chave pública do destinatário; dessa forma, unicamente o portador da chave privada correspondente será capaz de decifrá-la. A alternativa A erra, pois cifrar com a chave privada do emissor gera assinatura/autenticidade, não confidencialidade (todos têm a chave pública). A alternativa B erra, pois assinatura é feita com a chave privada do remetente. As alternativas D e E distorcem o segredo da chave privada e a complementaridade matemática do par assimétrico.

@@ a02/s03 | D
Os protocolos de segurança da camada de transporte na Internet, como TLS e HTTPS, equilibram desempenho computacional e segurança ao estabelecer canais criptografados. No que tange à arquitetura de criptografia híbrida, assinale a opção correta.
A) A criptografia híbrida rejeita a criptografia simétrica em virtude de suas falhas estruturais, operando exclusivamente com cifras de chave pública.
B) A criptografia híbrida utiliza algoritmos simétricos apenas para assinar digitalmente certificados e algoritmos assimétricos para transmissão de dados.
C) A criptografia híbrida exige o envio manual e físico de cartões magnéticos contendo a chave de sessão antes de cada conexão web efetuada.
D) A criptografia híbrida emprega o método assimétrico para trocar com segurança uma chave de sessão simétrica, que passa a cifrar todo o tráfego.
E) A chave de sessão gerada na criptografia híbrida é permanente e reutilizada indefinidamente ao longo de todos os acessos subsequentes do usuário.
// Comentário: A alternativa D está correta, pois a criptografia híbrida aproveita a segurança de distribuição da criptografia assimétrica para autenticar e acordar uma chave simétrica temporária (chave de sessão) e, em seguida, utiliza essa chave com um algoritmo simétrico veloz (ex.: AES) para cifrar a comunicação volumosa. As alternativas A, B e C distorcem o modelo. A alternativa E erra, pois a chave de sessão é efêmera/descartável.

@@ a02/s03 | E
A robustez de um sistema criptográfico é avaliada segundo princípios científicos consolidados que orientam o projeto e a auditoria de algoritmos seguros. Em relação ao Princípio de Kerckhoffs, assinale a opção correta.
A) A segurança de uma cifra depende intrinsecamente de manter o funcionamento de seu algoritmo em segredo perante a comunidade técnica.
B) O algoritmo criptográfico deve ser mantido em segredo absoluto, enquanto a chave privada do sistema pode ser divulgada publicamente.
C) A comprovação de que uma cifra resiste a ataques de texto cifrado simples atesta de forma incondicional a sua inviolabilidade perpétua.
D) A complexidade das instruções do programa executável constitui o único elemento determinante para a resistência de uma cifra matemática.
E) A segurança de um sistema criptográfico deve repousar exclusivamente no segredo da chave, e não na ocultação dos detalhes do algoritmo.
// Comentário: A alternativa E está correta, pois o clássico Princípio de Kerckhoffs estabelece que a segurança de um criptossistema não deve decorrer do segredo do algoritmo (que deve ser público e testado por especialistas), mas unicamente do sigilo da chave criptográfica. As alternativas A e B pregam a falaciosa "segurança por obscuridade". A alternativa C é falsa, pois testes simples não garantem segurança incondicional. A alternativa D erra ao focar em detalhes de programação em vez do tamanho e sigilo da chave.
"""
