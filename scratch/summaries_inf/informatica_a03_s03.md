##### informatica/a03/s03
O ecossistema contemporâneo de ameaças à segurança da informação engloba códigos maliciosos especializados em auto-replicação autônoma por redes, controle remoto distribuído de computadores zumbis, camuflagem por engenharia social, espionagem comportamental, abertura de portas furtivas e ocultação profunda no sistema operacional.

### Worm e Botnets

Diferenciando-se dos vírus biológicos digitais clássicos que dependem da infecção e execução de um arquivo hospedeiro:

- **Worm (Verme)**:
  - Consiste em um programa completo, independente e autossuficiente capaz de se propagar diretamente de computador para computador através de redes de dados.
  - Não embute seu código no interior de outros programas hospedeiros. A propagação ocorre de modo automatizado mediante a exploração de vulnerabilidades e falhas de segurança (*exploits*) em softwares e serviços ativos nas máquinas de destino, ou pelo envio em massa de mensagens contendo anexos ou links nocivos.
  - Em virtude do tráfego massivo gerado pela proliferação descontrolada de cópias de si mesmo, os worms provocam frequente congestionamento de banda em enlaces de rede e sobrecarga severa no desempenho dos processadores.

- **Bot e Botnet (Redes de Zumbis)**:
  - *Bot*: código malicioso dotado de rotinas de comunicação bidirecional com o atacante remoto (*botmaster*), transformando o computador infectado em um elemento zumbi subordinado a comandos externos.
  - *Botnet*: malha consolidada de milhares de computadores zumbis distribuídos geograficamente sob coordenação central. São empregadas para desferir ataques massivos de negação de serviço distribuída (DDoS), disparo coordenado de correio eletrônico indesejado (spam), disseminação em larga escala de novos malwares e mineração ilegal de criptoativos.

### Cavalo de Troia (Trojan Horse) e Spyware

- **Trojan Horse**:
  - Código malicioso que chega disfarçado como um presente digital aparentemente legítimo, inofensivo ou útil (como protetores de tela, cartões virtuais, utilitários de limpeza ou jogos), demandando habitualmente a execução manual voluntária induzida por técnicas de engenharia social.
  - Não possui mecanismos nativos de auto-replicação autônoma para outros computadores. Ao ser executado, libera sua carga danosa (*payload*), assumindo diversas especializações funcionais: *Trojan Downloader* (baixa malwares externos pela web), *Trojan Dropper* (extrai executáveis maliciosos embutidos em seu próprio corpo binário), *Trojan Backdoor*, *Trojan DoS*, *Trojan Destrutivo* e *Trojan Clicker*.

- **Spyware (Software Espião)**:
  - Destina-se a violar a privacidade monitorando e coletando hábitos comportamentais de navegação, credenciais de acesso e dados corporativos sensíveis da vítima, retransmitindo-os a terceiros externos sem autorização.
  - Pode assumir viés legítimo (softwares de auditoria instalados com o consentimento do titular em estações corporativas) ou viés puramente ilícito.
  - Subtipos mais cobrados: *Keylogger* (captura toques físicos no teclado para furtar senhas), *Screenlogger* (registra capturas de imagem da tela do monitor ao redor do ponteiro do mouse) e *Adware* (projeta anúncios publicitários invasivos e altera configurações padrão de busca).

### Backdoor e Rootkit: Acesso e Ocultação em Nível de Sistema

- **Backdoor (Porta dos Fundos)**:
  - Mecanismo que assegura o retorno furtivo e permanente do invasor a uma máquina previamente comprometida, contornando procedimentos habituais de autenticação através da abertura de portas TCP/UDP e ativação de serviços remotos camuflados.
  - Pode ser introduzido intencionalmente por invasores após a quebra do perímetro de segurança, por infecção secundária via trojans ou decorrer de falhas propositais deixadas por programadores durante o desenvolvimento de sistemas.

- **Rootkit**:
  - Coleção sofisticada de ferramentas, rotinas e scripts desenvolvida especificamente para mascarar e assegurar a permanência invisível do invasor ou de outras pragas digitais no sistema hospedeiro.
  - Opera habitualmente em níveis privilegiados do sistema operacional (modo núcleo / *kernel mode*), interceptando chamadas de sistema da API.
  - Não se destina primordialmente a danificar dados do usuário, mas a adulterar os relatórios e consultas que o sistema operacional fornece: oculta do Gerenciador de Tarefas os processos ativos do invasor, mascara chaves de inicialização no Registro do sistema, oculta arquivos em listagens de diretórios e forja a visualização de portas abertas em comandos de auditoria.

### Para fixar

- Worm é independente, se propaga explorando falhas de rede e consome banda sem precisar de hospedeiro.
- Bot transforma a máquina em zumbi sob comando externo; um conjunto deles forma uma botnet (DDoS, spam).
- Cavalo de Troia aparenta utilidade para enganar o usuário e não se auto-replica.
- Spyware espia a atividade em silêncio (keyloggers, screenloggers, adwares).
- Backdoor cria uma rota de retorno que contorna a autenticação.
- Rootkit age no núcleo do sistema para ocultar processos, arquivos e chaves do invasor.

