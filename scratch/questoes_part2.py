"""Part 2: Questions 31 to 60 for informatica
Segments:
- informatica/a02/s06: Q31 to Q36
- informatica/a03/s01: Q37 to Q42
- informatica/a03/s02: Q43 to Q48
- informatica/a03/s05: Q49 to Q54
- informatica/a04/s02: Q55 to Q60
"""

QUESTOES_P2 = """
@@ a02/s06 | A
A utilização de certificados digitais permite atestar com segurança a identidade de pessoas, empresas e servidores em transações eletrônicas na Internet. Em relação à estrutura padrão de um certificado digital segundo o padrão ITU-T X.509, assinale a opção correta.
A) O certificado digital atesta a titularidade de uma chave pública, trazendo os dados do titular e a assinatura digital da autoridade certificadora emissora.
B) O certificado digital armazena em seu corpo a chave privada do titular em formato legível para facilitar a conferência de senhas de acesso.
C) O certificado digital dispensa a menção a períodos de validade temporal, possuindo vigência perpétua a partir de sua emissão inicial.
D) O certificado digital é emitido sem número de série ou controle de versão, operando unicamente com o registro do endereço MAC do computador.
E) O certificado digital pode ser emitido de forma autônoma pelo próprio usuário final, com pleno reconhecimento automático na cadeia da ICP-Brasil.
// Comentário: A alternativa A está correta, pois em conformidade com o padrão internacional X.509, o certificado digital vincula a chave pública do titular à sua identidade formal, trazendo prazo de validade, número de série e a assinatura da Autoridade Certificadora (AC). A alternativa B erra gravemente, pois a chave privada jamais é inserida no certificado público. A alternativa C erra porque todo certificado possui vigência temporal definida. A alternativa D erra ao dispensar número de série e versão. A alternativa E erra, pois certificados da ICP-Brasil exigem emissão por AC credenciada.

@@ a02/s06 | B
A Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil), instituída pela Medida Provisória nº 2.200-2/2001, organiza-se segundo uma cadeia hierárquica de confiança rigorosamente auditada. Acerca das atribuições da Autoridade Certificadora Raiz (AC-Raiz), assinale a opção correta.
A) A AC-Raiz é operada diretamente por empresas privadas de telecomunicação que comercializam certificados para o público geral.
B) A AC-Raiz, operada pelo Instituto Nacional de Tecnologia da Informação (ITI), ocupa o topo da hierarquia e emite certificados apenas para outras ACs.
C) A AC-Raiz é encarregada de realizar a conferência presencial de documentos de identificação de todos os cidadãos solicitantes de certificados.
D) A AC-Raiz possui vigência operacional subordinada a autoridades de registro locais, dependendo de sua validação para operar no país.
E) A AC-Raiz emite certificados diretamente para usuários finais e computadores domésticos, dispensando autoridades certificadoras intermediárias.
// Comentário: A alternativa B está correta, pois a AC-Raiz da ICP-Brasil é executada institucionalmente pelo ITI (Instituto Nacional de Tecnologia da Informação), ocupando o vértice da cadeia hierárquica e emitindo certificados exclusivamente para as Autoridades Certificadoras subordinadas credenciadas (ela não atende diretamente o usuário comum). A alternativa A erra a natureza pública e gestora do ITI. A alternativa C descreve atribuições da Autoridade de Registro (AR). As alternativas D e E contradizem a hierarquia da ICP-Brasil.

@@ a02/s06 | C
O processo de emissão de um certificado digital na ICP-Brasil requer etapas formais de verificação cadastral e presencial do solicitante. No que se refere às competências de uma Autoridade de Registro (AR), assinale a opção correta.
A) A Autoridade de Registro tem competência legal para assinar e emitir certificados digitais com sua própria chave privada de autoridade.
B) A Autoridade de Registro opera como o órgão regulador supremo da ICP-Brasil, fiscalizando as diretrizes normativas do comitê gestor.
C) A Autoridade de Registro atua na identificação presencial ou remota do titular, validação documental e encaminhamento do pedido à AC vinculada.
D) A Autoridade de Registro substitui a autoridade certificadora na publicação e gerenciamento das Listas de Certificados Revogados (LCR).
E) A Autoridade de Registro tem suas funções limitadas à fiscalização tributária de notas fiscais eletrônicas emitidas por empresas comerciais.
// Comentário: A alternativa C está correta, pois a AR atua como o braço operacional presencial ou de contato com o solicitante, validando documentos físicos e dados biométricos antes de encaminhar a solicitação para que a Autoridade Certificadora (AC) efetivamente assine e gere o certificado. A alternativa A erra porque a AR não emite nem assina certificados. A alternativa B descreve o Comitê Gestor / ITI. A alternativa D erra porque a AC mantém as LCRs. A alternativa E distorce as competências da AR.

@@ a02/s06 | D
Os certificados digitais emitidos sob as regras da ICP-Brasil são enquadrados em diferentes tipos de acordo com o nível de segurança e a forma de guarda da chave privada. A respeito das distinções entre os certificados do tipo A1 e do tipo A3, assinale a opção correta.
A) O certificado do tipo A1 armazena a chave privada em smart card inviolável, apresentando prazo de validade máximo de até cinco anos.
B) O certificado do tipo A3 tem sua chave privada gerada e armazenada em arquivo de software no disco rígido com validade máxima de doze meses.
C) O certificado do tipo A1 permite a extração física de chips criptográficos dedicados para instalação em múltiplos computadores portáteis.
D) O certificado do tipo A1 armazena a chave em arquivo de software com validade de um ano, enquanto o A3 utiliza hardware criptográfico seguro.
E) Os certificados A1 e A3 são idênticos em infraestrutura física, diferenciando-se apenas pelo preço de comercialização no mercado.
// Comentário: A alternativa D está correta, pois o certificado A1 armazena a chave privada em software (arquivo com extensão .pfx ou .p12 no computador) com validade de até 1 ano, enquanto o tipo A3 armazena a chave em dispositivo físico dedicado inexportável (token USB ou smart card criptográfico) com validade comumente de até 3 ou 5 anos. As alternativas A e B invertem as características do A1 e do A3. As alternativas C e E ignoram a diferença estrutural entre software e hardware criptográfico.

@@ a02/s06 | E
Na eventualidade de perda, roubo da mídia criptográfica ou suspeita de comprometimento da chave privada, um certificado digital deve perder imediatamente sua eficácia antes do término de sua vigência temporal. Acerca dos mecanismos de revogação de certificados, assinale a opção correta.
A) A perda da mídia criptográfica não autoriza a revogação antecipada do certificado, sendo obrigatório aguardar a expiração do prazo regular.
B) A revogação de um certificado digital exige ordem judicial expressa transitada em julgado, sendo vedada a solicitação direta pelo titular.
C) A Lista de Certificados Revogados (LCR) é um documento sigiloso ao qual apenas peritos da polícia judiciária possuem permissão de acesso.
D) O protocolo OCSP exige o download completo e periódico de todas as listas de revogação emitidas no país para cada consulta pontual.
E) A revogação é publicada na Lista de Certificados Revogados da AC ou verificada em tempo real por meio de consultas pelo protocolo OCSP.
// Comentário: A alternativa E está correta, pois a perda de confiabilidade de um certificado acarreta sua inclusão na Lista de Certificados Revogados (LCR) mantida e assinada pela AC emissora, ou sua checagem instantânea online via Online Certificate Status Protocol (OCSP). As alternativas A e B erram, pois o titular pode e deve solicitar a revogação imediata em caso de perda ou suspeita. A alternativa C erra ao classificar a LCR como sigilosa (ela é pública). A alternativa D inverte as vantagens do OCSP (que evita o download da lista completa).

@@ a02/s06 | A
A ICP-Brasil estabelece séries padronizadas de certificados digitais para atender a diferentes finalidades no ambiente de segurança cibernética. Em relação às categorias funcionais de certificados reconhecidas na cadeia brasileira, assinale a opção correta.
A) Os certificados da categoria A destinam-se à assinatura e autenticação digital, enquanto os da categoria S voltam-se ao sigilo e à criptografia.
B) Os certificados da categoria A são voltados exclusivamente ao carimbo do tempo, sendo vedada sua utilização em assinaturas de contratos digitais.
C) Os certificados da categoria T destinam-se ao sigilo de mensagens confidenciais trocadas entre servidores de bancos de dados relacionais.
D) Os certificados da categoria S são empregados unicamente para a emissão de notas fiscais eletrônicas com validade jurídica de pessoa física.
E) Os certificados da categoria T operam substituindo a autoridade certificadora raiz na fiscalização técnica de prestadores de serviços.
// Comentário: A alternativa A está correta, pois na ICP-Brasil a série A (A1, A3, A4) destina-se à autenticação e assinatura digital, a série S (S1, S2, S3, S4) volta-se ao sigilo (criptografia de conteúdos) e a série T (T3, T4) é dedicada ao carimbo do tempo (Time Stamping). As alternativas B, C, D e E misturam e desvirtuam essas categorias funcionais.

@@ a03/s01 | B
A literatura técnica de segurança da informação e a comunidade de segurança computacional utilizam terminologia precisa para qualificar diferentes atores e comportamentos no ambiente digital. Acerca da distinção entre Hacker e Cracker, assinale a opção correta.
A) Hacker é o indivíduo que invade sistemas exclusivamente com propósitos criminosos, visando causar danos patrimoniais e lucros ilícitos.
B) Hacker estuda o funcionamento de sistemas para descobrir falhas e aprimorar a segurança, enquanto o cracker atua com má-fé para obter vantagens indevidas.
C) Cracker é o profissional certificado por órgãos oficiais de perícia policial que atua exclusivamente na defesa perimetral de redes públicas.
D) Hacker e Cracker são termos rigorosamente sinônimos na legislação brasileira, designando qualquer pessoa com conhecimentos em programação.
E) Cracker é o usuário iniciante que utiliza ferramentas prontas desenvolvidas por terceiros sem possuir conhecimento técnico especializado.
// Comentário: A alternativa B está correta, pois tecnicamente o hacker é um especialista que explora e compreende a fundo sistemas para aprender, testar e relatar vulnerabilidades, enquanto o cracker invade sistemas com motivação ilícita, para causar danos, roubar dados ou quebrar travas de software (pirataria). A alternativa A inverte a definição de hacker. A alternativa C erra sobre o cracker. A alternativa D trata os termos como sinônimos. A alternativa E define o script kiddie.

@@ a03/s01 | C
Os vírus de computador estruturam-se tecnicamente em módulos funcionais que coordenam a infecção de arquivos e a execução de suas rotinas no sistema operacional. No que diz respeito aos componentes estruturais de um vírus, assinale a opção correta.
A) A carga útil é o componente encarregado exclusivamente de monitorar a data e hora do relógio da placa-mãe para autorizar a infecção.
B) O mecanismo de infecção corresponde ao módulo que determina o momento exato em que danos aos arquivos do usuário serão executados.
C) O mecanismo de ativação, comumente chamado de bomba lógica, avalia a ocorrência de condições ou eventos para disparar a carga útil.
D) O vetor de infecção constitui a rotina responsável por formatar o disco rígido e apagar os registros de inicialização do computador.
E) A carga útil é um elemento dispensável em vírus destrutivos, sendo substituída integralmente pelo cabeçalho de rede do protocolo IP.
// Comentário: A alternativa C está correta, pois a estrutura de um vírus compõe-se de: mecanismo de infecção (como ele se propaga e anexa a outros programas), mecanismo de ativação ou bomba lógica (condição ou evento, como data ou limite, que dispara o efeito) e a carga útil (ação efetiva, destrutiva ou notória, que ele executa). As alternativas A e B invertem as atribuições. As alternativas D e E distorcem o papel do vetor e da carga útil.

@@ a03/s01 | D
O universo de softwares maliciosos compreende diversas classes de pragas virtuais que se diferenciam pelo modo como se propagam e interagem com o sistema operacional hospedeiro. Em relação às características fundamentais do vírus de computador, assinale a opção correta.
A) O vírus propaga-se de forma completamente autônoma pelas redes de dados, dispensando qualquer ação ou clique de usuários para sua ativação.
B) O vírus é incapaz de replicar seu próprio código, dependendo exclusivamente de comandos remotos digitados por um invasor conectado via Telnet.
C) O vírus prescinde de hospedeiro, executando-se diretamente na memória volátil como um serviço independente do sistema de arquivos.
D) O vírus insere cópias de seu código em programas ou arquivos hospedeiros, dependendo da execução do arquivo contaminado para entrar em atividade.
E) O vírus é um software benigno desenvolvido por fabricantes de antivírus com o intuito de corrigir falhas de segurança em sistemas legados.
// Comentário: A alternativa D está correta, pois o vírus tradicional caracteriza-se essencialmente por anexar seu código a um arquivo ou programa hospedeiro e depender da execução desse arquivo contaminado pelo usuário (não é autônomo, diferentemente do worm). A alternativa A define o comportamento do worm. As alternativas B e C negam a autorreplicação e a dependência de hospedeiro. A alternativa E é manifestamente falsa.

@@ a03/s01 | E
A infecção e a atuação de um vírus em um computador seguem uma sequência cronológica de etapas até que seus objetivos sejam alcançados. Acerca das fases do ciclo de vida de um vírus, assinale a opção correta.
A) A fase de propagação ocorre exclusivamente após a desinstalação completa do sistema operacional pelo usuário da máquina.
B) A fase de ativação é caracterizada pela completa inatividade do vírus, impedindo qualquer gravação de dados em disco ou memória.
C) A fase de dormência é obrigatória para todos os tipos de vírus existentes, não havendo pragas que atuem imediatamente após a infecção.
D) A fase de ação consiste no envio de relatórios técnicos de conformidade para as autoridades governamentais de segurança cibernética.
E) A fase de propagação instala cópias do vírus em novos arquivos ou áreas de disco, podendo gerar variantes modificadas para evitar detecção.
// Comentário: A alternativa E está correta, pois no ciclo de vida típico (dormência, propagação, ativação e ação), a propagação é a fase na qual o vírus faz cópias de si mesmo em outros arquivos executáveis ou discos, podendo recorrer ao polimorfismo para enganar antivírus. A alternativa A erra sobre o momento da propagação. A alternativa B descreve a fase de dormência. A alternativa C erra porque nem todo vírus possui fase de dormência. A alternativa D confunde a ação do vírus com auditoria de segurança.

@@ a03/s01 | A
A crença na imunidade de determinados sistemas operacionais perante códigos maliciosos tem sido objeto recorrente de debates na segurança da informação. A respeito da suscetibilidade de sistemas operacionais a vírus e malwares, assinale a opção correta.
A) Nenhum sistema operacional é completamente imune a pragas virtuais, embora plataformas Unix e macOS possuam modelos rigorosos de permissão.
B) O sistema operacional Linux é invulnerável a qualquer código malicioso em virtude do fato de possuir código-fonte aberto e auditável.
C) O sistema operacional macOS é arquitetonicamente blindado contra infecções virtuais, dispensando a aplicação de atualizações periódicas.
D) A maior prevalência histórica de vírus para o Windows decorre da ausência total de mecanismos de segurança no núcleo do sistema operacional.
E) Os vírus para computadores conseguem executar com facilidade qualquer binário em qualquer sistema operacional, independentemente da arquitetura.
// Comentário: A alternativa A está correta, pois é um consenso técnico que nenhum sistema operacional é totalmente invulnerável ou imune a malwares; a maior incidência no Windows deve-se à sua imensa base instalada corporativa e doméstica, e não a imunidade mágica do Linux ou macOS. As alternativas B e C propagam mitos de imunidade absoluta. A alternativa D é falsa, pois o Windows possui robustos mecanismos de segurança em seu kernel. A alternativa E desconsidera a especificidade de código de máquina e chamadas de sistema entre diferentes sistemas operacionais.

@@ a03/s01 | B
As políticas corporativas de segurança da informação devem contemplar não apenas defesas perimetrais contra ataques externos, mas também ameaças internas à infraestrutura. Quanto ao conceito de Insider no contexto das ameaças cibernéticas, assinale a opção correta.
A) O insider é um atacante estrangeiro que opera remotamente sem qualquer vínculo anterior ou permissão de acesso à instituição-alvo.
B) O insider é um colaborador ou agente interno que se aproveita de seus acessos e privilégios legítimos para violar normas ou vazar dados.
C) O insider representa um tipo específico de vírus de setor de inicialização que infecta comutadores ópticos de alta velocidade.
D) O insider atua exclusivamente mediante o envio massivo de e-mails de propaganda não solicitada para bases públicas da Internet.
E) O insider é um robô de inteligência artificial autônomo programado para monitorar vulnerabilidades em roteadores de borda.
// Comentário: A alternativa B está correta, pois o termo insider (ameaça interna) designa o colaborador, prestador de serviço ou funcionário que, detendo privilégios e credenciais legítimas dentro da rede institucional, comete fraudes, subtrai dados confidenciais ou sabota sistemas. As alternativas A, C, D e E trazem definições incorretas ou absurdas para o termo.

@@ a03/s02 | C
Ambientes corporativos que utilizam intensivamente pacotes de automação de escritório frequentemente lidam com arquivos de texto e planilhas contendo rotinas automatizadas. Com relação às características dos vírus de macro, assinale a opção correta.
A) Os vírus de macro infectam exclusivamente setores de inicialização física (MBR) de discos rígidos em servidores de centros de dados.
B) Os vírus de macro são autônomos e se propagam automaticamente por difusão na camada física sem necessitar de arquivos hospedeiros.
C) Os vírus de macro contaminam arquivos de aplicativos que utilizam linguagem de automação, como o Microsoft Office, agindo ao abrir o documento.
D) Os vírus de macro afetam unicamente arquivos executáveis com extensão .exe, alterando os binários do compilador do sistema operacional.
E) Os vírus de macro não podem ser prevenidos pela desativação de recursos de macros ou pela exigência de certificados de confiança nos editores.
// Comentário: A alternativa C está correta, pois os vírus de macro infectam arquivos de dados de aplicativos de produtividade (Word, Excel, PowerPoint) que executam rotinas em linguagens de script/macro (como VBA); a infecção propaga-se ao abrir o documento se as macros forem habilitadas. As alternativas A e D confundem vírus de macro com vírus de boot ou de arquivo. A alternativa B erra ao descrever o comportamento de worms. A alternativa E erra porque desabilitar macros é a principal medida de proteção contra esses códigos.

@@ a03/s02 | D
Determinados códigos maliciosos atuam na fase inicial de carregamento do computador para assumir o controle do sistema antes da ativação dos mecanismos de proteção do sistema operacional. A respeito do vírus de boot, assinale a opção correta.
A) O vírus de boot infecta exclusivamente scripts em páginas web HTML, operando apenas enquanto o navegador de Internet estiver aberto.
B) O vírus de boot atua apagando planilhas de cálculo financeiro no momento em que macros são salvas em formato de texto estruturado.
C) O vírus de boot aloja-se nas portas lógicas do firewall de borda, impedindo que requisições HTTP alcancem os servidores de aplicação.
D) O vírus de boot instala-se na área de partida do disco (como o registro mestre de inicialização) e carrega-se na memória antes do sistema operacional.
E) A formatação rápida de um disco removível contaminado garante de forma infalível e definitiva a eliminação de qualquer vírus de boot residual.
// Comentário: A alternativa D está correta, pois o vírus de boot (setor de inicialização) aloja-se no Master Boot Record (MBR) ou primeiro setor do disco/pendrive, carregando-se na memória RAM antes do sistema operacional. As alternativas A, B e C descrevem outros alvos. A alternativa E erra, pois a formatação rápida pode não reescrever o setor de boot/MBR, deixando o vírus latente na mídia.

@@ a03/s02 | E
Algumas pragas virtuais sofisticadas combinam diferentes vetores de ataque para ampliar sua persistência no sistema computacional e dificultar a ação de desinfecção. Acerca do vírus multipartite, assinale a opção correta.
A) O vírus multipartite limita sua infecção exclusivamente a arquivos de áudio gravados em taxas de compressão sem perda de qualidade.
B) O vírus multipartite atua unicamente durante o tráfego de pacotes UDP na rede, não permanecendo armazenado em qualquer mídia persistente.
C) O vírus multipartite é uma modalidade inofensiva de código que apenas exibe mensagens humorísticas no monitor sem replicar código.
D) A remoção de um vírus multipartite é trivial, bastando fechar as janelas ativas do navegador sem necessidade de checagem do setor de boot.
E) O vírus multipartite infecta simultaneamente arquivos executáveis e o setor de inicialização, exigindo tratamento em ambas as áreas para desinfecção.
// Comentário: A alternativa E está correta, pois o vírus multipartite reúne as características de vírus de arquivo e de vírus de boot, contaminando tanto programas executáveis (.exe) quanto o setor de inicialização (MBR); se apenas um dos focos for limpo, o sistema será reinfectado a partir do outro. As alternativas A, B, C e D trazem concepções manifestamente equivocadas.

@@ a03/s02 | A
As técnicas de evasão desenvolvidas por criadores de malwares visam burlar a detecção realizada por soluções antivírus baseadas em padrões estáticos de assinaturas binárias. Com relação às diferenças entre vírus polimórficos e metamórficos, assinale a opção correta.
A) O vírus polimórfico altera sua assinatura a cada replicação mantendo sua função, enquanto o metamórfico reescreve todo o seu código estrutural.
B) O vírus metamórfico preserva sua assinatura binária perfeitamente inalterada ao longo de todas as gerações de contaminação em disco.
C) O vírus polimórfico e o vírus metamórfico são termos sinônimos que descrevem malwares que atacam exclusivamente arquivos em formato PDF.
D) O vírus polimórfico perde completamente sua capacidade de execução após sofrer a primeira mutação de suas rotinas de criptografia.
E) O vírus metamórfico opera sem utilizar instruções de máquina, dependendo de emuladores manuais instalados pelos usuários do sistema.
// Comentário: A alternativa A está correta: o vírus polimórfico altera seu padrão de bits (assinatura) a cada infecção alterando as chaves e rotinas de criptografia/descriptografia, mas mantém a funcionalidade original; já o vírus metamórfico é ainda mais avançado, reescrevendo completamente sua estrutura lógica e corpo a cada replicação. A alternativa B inverte o conceito do metamórfico. A alternativa C erra ao tratá-los como sinônimos. As alternativas D e E contêm afirmações incorretas sobre sua operação.

@@ a03/s02 | B
Mecanismos avançados de ocultação permitem que determinados códigos maliciosos permaneçam ocultos aos olhos do usuário e de ferramentas de inspeção do sistema operacional. No que tange às características do vírus stealth (furtivo), assinale a opção correta.
A) O vírus stealth atua exibindo janelas pop-up publicitárias de grande formato na área de trabalho para demonstrar sua presença ao usuário.
B) O vírus stealth utiliza técnicas para ocultar sua presença, como interceptar chamadas ao sistema operacional e mascarar alterações de tamanho em arquivos.
C) O vírus stealth limita sua infecção ao código-fonte de sistemas operacionais livres, sendo incapaz de ser executado em plataformas proprietárias.
D) O vírus stealth converte automaticamente todas as senhas armazenadas no navegador em texto cifrado com chaves públicas de quarenta bits.
E) O vírus stealth é detectado com facilidade por simples comandos de listagem de diretório devido ao aumento perceptível no volume de dados.
// Comentário: A alternativa B está correta, pois o vírus furtivo (stealth) intercepta requisições de leitura de arquivos e chamadas de sistema (API) para mascarar sua presença; ao ser requisitado o tamanho do arquivo infectado, ele retorna o valor original do arquivo antes da contaminação, enganando o usuário e antivírus simplistas. As alternativas A e E negam a natureza furtiva do malware. As alternativas C e D são distorções conceituais.

@@ a03/s02 | C
Certos programas maliciosos mantêm suas rotinas lesivas em estado de latência no computador infectado, aguardando condições temporais específicas para liberar sua ação. Acerca do vírus do tipo time bomb (bomba-relógio), assinale a opção correta.
A) O vírus time bomb explode fisicamente a placa-mãe do computador por meio de superaquecimento programado dos capacitores elétricos.
B) O vírus time bomb caracteriza-se por deletar arquivos instantaneamente no exato segundo em que o usuário faz o download do arquivo.
C) O vírus time bomb permanece dormente após a infecção e dispara sua carga maliciosa em uma data ou horário pré-determinado pelo criador.
D) O vírus time bomb afeta unicamente dispositivos periféricos de impressão, impedindo a emissão de comprovantes de pagamento bancário.
E) O vírus time bomb propaga-se exclusivamente por meio de frequências sonoras emitidas pelos alto-falantes de computadores portáteis.
// Comentário: A alternativa C está correta, pois a bomba-relógio (time bomb) é o malware dotado de mecanismo de ativação programado para detonar sua carga útil somente quando uma data, horário ou contagem de eventos específicos for atingida (ex.: vírus Sexta-feira 13, Chernobyl). As alternativas A, B, D e E trazem assertivas absurdas ou incorretas.

@@ a03/s05 | D
Ataques cibernéticos contra serviços governamentais frequentemente não buscam a invasão de bases nem a violação de sigilo, mas a paralisia do atendimento aos cidadãos. Com relação aos ataques de Negação de Serviço (DoS e DDoS), assinale a opção correta.
A) O ataque DoS visa subtrair senhas bancárias por meio da instalação clandestina de um keylogger residente na memória principal.
B) O ataque DDoS é executado a partir de um único computador pessoal sem conexão com a Internet, visando saturar portas seriais locais.
C) O ataque DoS altera permanentemente a estrutura dos bancos de dados relacionais da organização-alvo, tornando os dados irrecuperáveis.
D) O ataque DoS/DDoS visa exaurir recursos computacionais ou banda de rede para provocar indisponibilidade dos serviços, sem foco em roubo de dados.
E) O ataque DoS garante que a confidencialidade e a disponibilidade dos sistemas permaneçam intocadas durante toda a ocorrência do incidente.
// Comentário: A alternativa D está correta, pois os ataques de negação de serviço (DoS/DDoS) têm por objetivo saturar recursos de hardware, conexões ou largura de banda do servidor-alvo, provocando a indisponibilidade do serviço para os usuários legítimos; finalizado o ataque, os dados permanecem intactos, pois a intenção não é invadir nem furtar arquivos. As alternativas A, B, C e E distorcem completamente a natureza e as consequências de ataques DoS.

@@ a03/s05 | E
A tentativa de obtenção de credenciais de acesso legítimas para invasão de contas corporativas é realizada por meio de ferramentas automatizadas especializadas. Acerca do ataque de Força Bruta (brute force) e de suas formas de mitigação, assinale a opção correta.
A) O ataque de força bruta consiste em interceptar o tráfego de pacotes na camada de enlace para decifrar chaves WPA2 em redes Wi-Fi públicas.
B) O ataque de força bruta dispensa o uso de dicionários ou palavras comuns, baseando-se unicamente na indução psicológica do operador de TI.
C) A implementação de senhas de quatro dígitos com datas de nascimento constitui a forma mais eficiente de conter ataques de força bruta.
D) O ataque de força bruta não acarreta riscos à disponibilidade de contas corporativas, já que as tentativas são imperceptíveis aos servidores.
E) A força bruta baseia-se na tentativa exaustiva de combinações de senhas, sendo mitigada por senhas complexas, bloqueio por erros e MFA.
// Comentário: A alternativa E está correta, pois a força bruta (brute force) envolve testar sistematicamente combinações alfanuméricas, dicionários e padrões previsíveis até adivinhar as credenciais; suas defesas essenciais incluem políticas de senhas longas e complexas, bloqueio temporário de contas após sucessivas falhas, CAPTCHA e autenticação multifator (MFA). A alternativa A confunde força bruta com sniffing. A alternativa B confunde com engenharia social. A alternativa C indica senhas extremamente vulneráveis. A alternativa D erra porque sucessivas falhas costumam bloquear a conta, gerando negação de serviço.

@@ a03/s05 | A
Mensagens fraudulentas de correio eletrônico frequentemente aparentam ter sido emitidas por instituições bancárias ou órgãos policiais respeitados. No que tange à técnica de E-mail Spoofing, assinale a opção correta.
A) O e-mail spoofing adultera campos do cabeçalho da mensagem para forjar o endereço do remetente, explorando fragilidades originárias do protocolo SMTP.
B) O e-mail spoofing consiste no sequestro de arquivos corporativos com exigência de pagamento de resgate financeiro em criptomoedas.
C) O e-mail spoofing exige que o atacante tenha invadido previamente o computador físico do destinatário para enviar os comunicados.
D) O e-mail spoofing é evitado de forma integral e definitiva pela simples desativação de caixas postais secundárias de servidores de correio.
E) O e-mail spoofing e o spam são conceitos idênticos, designando a transmissão de arquivos compactados com senha para múltiplos contatos.
// Comentário: A alternativa A está correta, pois o e-mail spoofing falsifica os campos de cabeçalho da mensagem eletrônica (como o campo "From:"), fazendo com que o e-mail aparente vir de remetente legítimo; isso é possível pelas características históricas do protocolo SMTP, que não exigia validação nativa de remetente. A alternativa B descreve ransomware. A alternativa C é incorreta, pois o e-mail parte de servidores controlados pelo atacante. A alternativa D é ineficaz. A alternativa E confunde spoofing (falsificação) com spam (envio massivo).

@@ a03/s05 | B
Em redes computacionais nas quais o controle de acesso e permissões entre estações fundamenta-se na verificação de endereçamento lógico, vulnerabilidades específicas podem ser exploradas por invasores. Com relação ao IP Spoofing, assinale a opção correta.
A) O IP spoofing consiste em danificar fisicamente o cabo de rede Ethernet para impedir o encaminhamento de quadros pelo comutador de núcleo.
B) O IP spoofing forja o endereço IP de origem nos pacotes de rede para contornar filtros baseados em IP e disfarçar a verdadeira identidade do emissor.
C) O IP spoofing converte endereços IPv4 em endereços IPv6 de forma automática nos servidores DNS para otimizar o tempo de latência.
D) O IP spoofing impede que computadores utilizem endereçamento dinâmico via DHCP, obrigando a configuração estática de rotas de borda.
E) O IP spoofing afeta exclusivamente redes domésticas que utilizam roteadores desprovidos de portas USB integradas ao circuito principal.
// Comentário: A alternativa B está correta, pois no IP spoofing o invasor mascara ou altera o endereço IP de origem no cabeçalho do pacote, fingindo que a requisição partiu de um host confiável da rede; é comum quando regras de autenticação ou permissões de firewall baseiam-se ingenuamente apenas no IP de origem. As alternativas A, C, D e E trazem descrições fantasiosas ou desconexas.

@@ a03/s05 | C
Incidentes cibernéticos graves frequentemente têm como porta de entrada a indução psicológica de colaboradores desavisados em vez de falhas complexas de software. Acerca da Engenharia Social na segurança corporativa, assinale a opção correta.
A) A engenharia social baseia-se exclusivamente na quebra matemática de chaves simétricas de 256 bits mediante supercomputadores quânticos.
B) A engenharia social atua instalando chips espiões nas placas de rede durante o processo de fabricação industrial dos servidores de borda.
C) A engenharia social explora a confiança, ingenuidade ou boa-fé das pessoas para induzi-las a executar ações ou revelar dados confidenciais.
D) A engenharia social atinge unicamente usuários desprovidos de contas ativas no sistema de correio eletrônico corporativo da instituição.
E) Os treinamentos de capacitação e conscientização de usuários mostram-se ineficazes contra ataques estruturados de engenharia social.
// Comentário: A alternativa C está correta, pois a engenharia social manipula psicologicamente pessoas para obter informações sigilosas (senhas, documentos) ou fazer com que tomem ações lesivas (clicar em links maliciosos, autorizar acessos), explorando sentimentos como ingenuidade, autoridade, medo ou prestatividade (ex.: phishing). As alternativas A e B citam técnicas puramente computacionais/materiais. A alternativa D é sem sentido. A alternativa E erra ao descartar o treinamento e a cultura de segurança, que são as principais defesas contra a engenharia social.

@@ a03/s05 | D
Para aprimorar a detecção precoce de ameaças e mapear as táticas de grupos maliciosos, administradores de segurança utilizam armadilhas tecnológicas no perímetro de rede. Quanto ao conceito e à finalidade de um Honeypot, assinale a opção correta.
A) O honeypot é um vírus destrutivo utilizado por corporações para contra-atacar computadores de invasores externos na Internet pública.
B) O honeypot é uma técnica de falsificação de páginas web que redireciona clientes bancários para servidores clonados da quadrilha criminosa.
C) O honeypot opera interceptando silenciosamente senhas em texto claro em redes locais desprovidas de isolamento de portas comutadas.
D) O honeypot é um recurso de defesa que simula um sistema deliberadamente vulnerável para atrair invasores, registrar e analisar suas ações.
E) O honeypot substitui integralmente a necessidade de firewalls corporativos e antivírus residentes nos servidores centrais de produção.
// Comentário: A alternativa D está correta, pois o honeypot (pote de mel) é uma ferramenta estritamente defensiva concebida para parecer um sistema real vulnerável; seu papel é atrair atacantes para longe dos ativos reais, retardá-los e coletar informações forenses sobre suas técnicas de ataque. As alternativas A, B e C confundem honeypot com malware, pharming/phishing ou sniffing. A alternativa E erra ao sugerir que o honeypot dispense os demais controles essenciais.

@@ a04/s02 | E
A evolução dos programas antivírus levou ao desenvolvimento de técnicas capazes de identificar pragas virtuais antes que seus padrões binários fossem catalogados formalmente em bases de assinaturas. A respeito da análise heurística adotada pelos antivírus de 2ª geração, assinale a opção correta.
A) A heurística analisa exclusivamente as assinaturas binárias exatas já previamente conhecidas e homologadas no laboratório do fabricante.
B) A heurística garante que nenhum programa inofensivo seja classificado por engano como malicioso, eliminando a taxa de falsos positivos.
C) A heurística é incapaz de detectar variantes de vírus polimórficos que alteram a sua sequência de bits externa a cada nova infecção.
D) A análise heurística exige a execução simultânea de todas as rotinas em ambientes de produção sem qualquer isolamento computacional.
E) A heurística avalia instruções e estruturas suspeitas para identificar malwares inéditos, apresentando como desafio a emissão de falsos positivos.
// Comentário: A alternativa E está correta, pois a análise heurística (2ª geração) inspeciona o código em busca de estruturas, comportamentos e instruções típicas de malware, permitindo identificar ameaças inéditas (zero-day) e vírus polimórficos; seu principal efeito colateral é a ocorrência eventual de falsos positivos (classificar código legítimo e incomum como ameaça). A alternativa A define a 1ª geração (assinaturas). A alternativa B erra ao dizer que elimina falsos positivos. A alternativa C erra porque a heurística combate justamente polimórficos. A alternativa D desconsidera a heurística estática e as sandboxes.

@@ a04/s02 | A
As ferramentas de segurança de 3ª geração trouxeram um aprofundamento na proteção computacional ao direcionar o foco de inspeção para os acontecimentos em tempo de execução no sistema operacional. No que tange à interceptação de atividades, assinale a opção correta.
A) A 3ª geração monitora chamadas de sistema em tempo real, bloqueando ações suspeitas como alterações no Registro e criação de processos ocultos.
B) A interceptação de atividades baseia-se na exclusão cega de todos os arquivos executáveis que forem abertos simultaneamente pelo usuário.
C) A 3ª geração de antivírus dispensa o consumo de processamento e memória, atuando sem qualquer integração com o kernel do sistema operacional.
D) O monitoramento comportamental atua exclusivamente quando o computador encontra-se desconectado da fonte de alimentação elétrica.
E) A interceptação de atividades limita-se a analisar os endereços de correio eletrônico presentes na pasta de mensagens enviadas do usuário.
// Comentário: A alternativa A está correta, pois a 3ª geração de antivírus foca no monitoramento comportamental ativo em tempo de execução (interceptação de chamadas de sistema), barrando em tempo real tentativas de injeção em processos legítimos, gravações maliciosas no Registro do Windows e abertura de conexões anômalas para servidores C2. As alternativas B, C, D e E trazem afirmações sem qualquer respaldo técnico.

@@ a04/s02 | B
A sofisticação crescente de ataques corporativos impulsionou o surgimento de plataformas de antivírus de nova geração (NGAV) consorciadas a sistemas de detecção e resposta de endpoints. Acerca dos antivírus de 4ª geração e soluções NGAV, assinale a opção correta.
A) O modelo NGAV desativa os recursos de nuvem e inteligência artificial para operar segundo padrões herdados da computação legada.
B) As soluções NGAV combinam aprendizado de máquina e proteção multicamadas em nuvem para neutralizar malwares sem arquivos e ransomwares.
C) A 4ª geração restringe-se a comparar assinaturas binárias locais, sendo incapaz de inspecionar processos residentes diretamente na memória.
D) As plataformas modernas de endpoint detection and response (EDR) vedam o isolamento preventivo de computadores comprometidos na rede.
E) Os antivírus de 4ª geração dependem da digitação manual de comandos pelo usuário no prompt para autorizar a abertura de cada aplicativo.
// Comentário: A alternativa B está correta, pois as soluções de 4ª geração e os NGAV (Next-Generation Antivirus) incorporam modelos de inteligência artificial, análise em nuvem e detecção em profundidade para combater ameaças avançadas, como ataques fileless (sem arquivos no disco) e ransomwares sofisticados. As alternativas A e C retrocedem à 1ª geração. As alternativas D e E contradizem os princípios de automação e resposta rápida do modelo EDR/NGAV.

@@ a04/s02 | C
O correio eletrônico institucional representa um dos principais vetores de transmissão de ameaças, fraudes e conteúdos indesejados nas corporações. Quanto às características operacionais dos filtros antispam, assinale a opção correta.
A) O filtro antispam atua aplicando criptografia assimétrica de ponta a ponta sobre todas as mensagens que ingressam no servidor institucional.
B) O filtro antispam tem a função exclusiva de gerenciar as chaves privadas dos certificados digitais corporativos de todos os colaboradores.
C) O filtro antispam realiza a triagem de mensagens não solicitadas com base em regras de reputação, listas e algoritmos bayesianos.
D) O filtro antispam elimina a necessidade de políticas de senhas fortes, garantindo a imunidade dos bancos de dados relacionais internos.
E) As mensagens classificadas como spam pelo filtro são obrigatoriamente convertidas em formatos de imagem vetorial no gateway de borda.
// Comentário: A alternativa C está correta, visto que os filtros antispam realizam a triagem automatizada de comunicações massivas e maliciosas avaliando o conteúdo textual com algoritmos bayesianos, reputação de IPs, listas negras/brancas e cabeçalhos. A alternativa A e a alternativa B incorrem na clássica pegadinha: filtros antispam não aplicam criptografia nem gerenciam chaves de segurança. As alternativas D e E são descrições manifestamente falsas.

@@ a04/s02 | D
O furto silencioso de hábitos de navegação, credenciais de acesso bancário e documentos institucionais é coordenado por classes especializadas de malwares invasivos. Em relação ao papel dos softwares antispyware, assinale a opção correta.
A) O antispyware destina-se a acelerar o tempo de inicialização do sistema operacional por meio da exclusão de logs de segurança do kernel.
B) O antispyware substitui os protocolos de roteamento dinâmico em redes corporativas comutadas para evitar congestionamentos de dados.
C) O antispyware é desenvolvido unicamente para combater vírus de macro que infectam apresentações de slides em formato digital.
D) O antispyware combate programas espiões em segundo plano, como keyloggers e adwares invasivos, isolando itens suspeitos em quarentena.
E) O antispyware atua exclusivamente quando o usuário autoriza formalmente a gravação de suas senhas em servidores públicos remotos.
// Comentário: A alternativa D está correta, pois o antispyware é uma ferramenta especializada em rastrear, bloquear e remover spywares (keyloggers, screenloggers, adwares intrusivos) projetados para espionar e violar a privacidade do usuário em segundo plano, disponibilizando área de quarentena para isolar arquivos sob suspeita. As alternativas A, B, C e E apresentam funções equivocadas ou desconexas.

@@ a04/s02 | E
A análise dinâmica em ambientes controlados permite que pesquisadores e sistemas de proteção avaliem códigos suspeitos antes que provoquem danos aos sistemas reais. No que tange ao conceito e à operação de Sandbox em soluções antivírus, assinale a opção correta.
A) A sandbox é uma técnica que expõe diretamente a máquina física de produção para avaliar a velocidade com que os dados são corrompidos.
B) A sandbox atua desativando permanentemente a memória volátil do computador hospedeiro para impedir a execução de qualquer processo.
C) A sandbox é um módulo de hardware conectado à placa-mãe que destrói fisicamente o disco rígido em caso de tentativa de invasão.
D) A sandbox realiza a assinatura digital de contratos corporativos utilizando algoritmos quânticos padronizados internacionalmente.
E) A sandbox é um ambiente virtual isolado onde o código suspeito é executado para que seu comportamento seja monitorado com segurança.
// Comentário: A alternativa E está correta, pois uma sandbox (caixa de areia) consiste em um ambiente virtual restrito e rigorosamente isolado do restante do sistema operacional, permitindo executar programas suspeitos para observar suas ações (como tentativas de criar chaves no registro ou abrir conexões clandestinas) sem colocar em risco a máquina real. As alternativas A, B, C e D trazem concepções distorcidas ou fantasiosas do recurso.
"""
