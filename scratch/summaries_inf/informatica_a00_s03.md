##### informatica/a00/s03
A infraestrutura de comunicação de redes modernas assenta-se em modelos conceituais estratificados e arquiteturas de protocolos que viabilizam o tráfego global de dados. O trecho aborda os conceitos essenciais de protocolos de rede, o Modelo de Referência OSI de 7 camadas, a arquitetura prática TCP/IP, o protocolo IP nas versões IPv4 e IPv6 e os dois principais protocolos da camada de transporte: o TCP (orientado à conexão e confiável) e o UDP (não orientado à conexão e veloz).

### Fundamentos de Protocolos e o Modelo de Referência OSI/ISO

Protocolos de comunicação são conjuntos formais de normas, formatos e procedimentos que regulam a transmissão, sequenciamento e correção de erros entre dispositivos computacionais em rede:

- **Conceito Estrutural**: para lidar com a complexidade da comunicação digital, os sistemas adotam arquitetura modular em camadas, onde cada nível presta serviços à camada imediatamente superior por meio de interfaces padronizadas.
- **O Modelo OSI (Open Systems Interconnection)**: modelo de referência teórico de 7 camadas formulado pela ISO para finalidade didática e padronização conceitual (não sendo uma pilha de software implementada na prática).

As sete camadas do modelo teórico (ordenadas da base ao topo):
1. **Física**: especificações elétricas, mecânicas e transmissão binária de bits no meio físico (cabos de cobre, fibra óptica, conectores).
2. **Enlace**: organiza os dados em **quadros (frames)**, realiza detecção básica de erros e controle de acesso ao meio físico (endereçamento físico MAC, protocolos Ethernet e Wi-Fi).
3. **Rede**: responsável pelo roteamento, entrega de **pacotes** e endereçamento lógico entre múltiplas redes distintas (protocolos IP, ICMP).
4. **Transporte**: gerencia a comunicação fim a fim entre processos de aplicação, fragmentando os dados em **segmentos** com controle de fluxo e erros (TCP, UDP).
5. **Sessão**: gerencia o estabelecimento, manutenção e sincronização de conexões entre aplicações.
6. **Apresentação**: encarrega-se da formatação, conversão de conjuntos de caracteres, compressão e criptografia dos dados.
7. **Aplicação**: interface direta com os programas e serviços utilizados pelo usuário final (HTTP, DNS, SMTP).

### Arquitetura Prática TCP/IP e o Protocolo IP

Diferente do Modelo OSI conceitual, a **Arquitetura TCP/IP** foi desenvolvida pragmaticamente e constitui o padrão de fato da Internet mundial. Conforme a RFC 1122, estrutura-se em 4 camadas principais:
- *Aplicação*: unifica as funções de aplicação, apresentação e sessão do OSI.
- *Transporte*: comunicação host a host (TCP e UDP).
- *Internet (Rede)*: endereçamento lógico e roteamento de datagramas (IP, ICMP).
- *Acesso à Rede (Enlace/Física)*: interfaceamento com o meio físico de transmissão.

#### O Protocolo IP (Internet Protocol)
Opera na camada de rede/Internet provendo endereçamento lógico e roteamento:
- **Características**: protocolo **não confiável**, **sem conexão** e de **melhor esforço** (*best-effort*). Ele não assegura que pacotes chegarão na ordem, nem retransmite dados perdidos por conta própria.
- **Versões de Endereçamento**:
  - **IPv4**: utiliza endereços de **32 bits**, estruturados em 4 blocos decimais de 8 bits (octetos) separados por pontos (ex.: `192.168.0.1`), permitindo cerca de 4,3 bilhões de endereços teóricos (`2³²`).
  - **IPv6**: desenvolvido para sanar o esgotamento do IPv4. Utiliza **128 bits**, representados em 8 grupos de 4 dígitos hexadecimais separados por dois-pontos (ex.: `2001:0db8:85a3::8a2e:0370:7334`), disponibilizando aproximadamente `3,4 × 10³⁸` endereços (`2¹²⁸`). Admite supressão de zeros à esquerda e compressão consecutiva de zeros com `::` (aplicada estritamente uma única vez por endereço).

### Protocolos da Camada de Transporte: TCP e UDP

A camada de transporte estabelece a comunicação entre **processos** específicos em execução nos computadores, utilizando **portas lógicas** (que variam de 0 a 65535, totalizando 65536 portas possíveis por endereço IP):

| Critério | Protocolo TCP (Transmission Control Protocol) | Protocolo UDP (User Datagram Protocol) |
| --- | --- | --- |
| **Conexão** | Orientado à conexão (*three-way handshake*) | Não orientado à conexão (*connectionless*) |
| **Confiabilidade** | Confiável (confirma recebimento e retransmite) | Não confiável (sem confirmação de entrega) |
| **Ordenação** | Garante entrega na ordem sequencial correta | Não reordena pacotes que cheguem fora de ordem |
| **Controle de Fluxo** | Possui controle de fluxo e congestionamento | Não implementa controle de fluxo |
| **Sobrecarga (Overhead)** | Maior sobrecarga e latência | Mínima sobrecarga, alta velocidade |
| **Uso Recomendado** | Web (HTTP/HTTPS), arquivos (FTP), e-mail (SMTP) | Voz sobre IP (VoIP), streaming ao vivo, jogos online |

O **UDP** destaca-se pela agilidade: ao abrir mão de confirmações e retransmissões desnecessárias para aplicações em tempo real, garante baixa latência indispensável onde eventuais perdas mínimas de pacotes são preferíveis a atrasos na transmissão contínua.

### Detalhes que caem em prova

| Camada OSI | Exemplos de protocolos |
| --- | --- |
| 7 Aplicação | HTTP, SMTP, FTP, SSH, Telnet, SNMP, POP3, IMAP, DNS |
| 6 Apresentação | tradução/formato dos dados (XDR e outros) |
| 5 Sessão | abre, usa e fecha sessões (NetBIOS) |
| 4 Transporte | TCP, UDP |
| 3 Rede | IP, ICMP, ARP, RARP, NAT |
| 2 Enlace | Ethernet, Token Ring, Bluetooth, Wi-Fi |
| 1 Física | USB, DSL |

- **Mnemônico (base ao topo):** Física, Enlace, Rede, Transporte, Sessão, Apresentação, Aplicação (F-E-R-T-S-A-A).
- **OSI não é arquitetura em uso:** ele é referência didática e não define exatamente quais protocolos entram em cada camada; por isso nem todo protocolo se encaixa com precisão. O TCP/IP é anterior ao OSI e é o que a Internet usa.
- **TCP/IP:** as quatro camadas seguem a RFC 1122 (aplicação, transporte, internet e acesso à rede); alguns autores adotam cinco camadas (física, enlace, rede, transporte e aplicação), unindo apenas as três de cima do OSI. Um servidor costuma ser chamado pelo protocolo que oferece (servidor HTTP, SMTP, DNS, FTP).
- **IPv4:** endereço de 32 bits em 4 octetos, cada um de 0 a 255 (por exemplo, 10101010.01010101.11100111.10111101 em binário vale 170.85.231.189). Nasceu em 1983 e entrou em escassez; o comando `ipconfig` mostra o IP da máquina, geralmente privado.
- **IPv6:** 8 grupos de 16 bits (4 dígitos hexadecimais) separados por dois-pontos; não tem classes nem broadcast e não conversa diretamente com IPv4. Também trouxe suporte a tempo real e a criptografia/autenticação.
- **Abreviação no IPv6:** só se omitem zeros à esquerda de cada grupo (0074 vira 74; 0000 vira 0; 3210 não muda). Sequências consecutivas de grupos zerados viram `::` apenas uma vez por endereço. Exemplo: 2001:0C00:0000:0000:5400:0000:0000:0009 pode virar 2001:C00::5400:0:0:9 ou 2001:C00:0:0:5400::9, mas 2001:C00::5400::9 é inválido.
- **Portas:** a porta de destino serve para entregar o segmento ao processo certo e a de origem permite a resposta. A porta padrão do HTTP é 80 (definida pela IANA). Protocolo + IP + porta formam um socket.
- **TCP:** além do descrito, permite comunicação bidirecional, usa soma de verificação para detectar erros e divide os dados em segmentos. **UDP:** entrega sem conexão e sem controle de fluxo ou congestionamento; faz só verificação limitada de erros, sem corrigi-los; acrescenta ao IP apenas a comunicação entre processos, não entre hosts; é usado em áudio, vídeo e tempo real, onde perdas pequenas são toleráveis.

### Para fixar

- O Modelo OSI divide as redes conceitualmente em 7 camadas teóricas.
- A pilha prática da Internet é o modelo TCP/IP, estruturado em 4 camadas essenciais.
- O protocolo IP é não confiável, sem conexão e atua na modalidade de melhor esforço (*best-effort*).
- O IPv4 adota endereçamento de 32 bits em notação decimal pontuada; o IPv6 adota 128 bits em notação hexadecimal.
- As portas lógicas de transporte numeram-se de 0 a 65535, identificando o processo de destino na máquina.
- O TCP é orientado à conexão, confiável, ordena pacotes e retransmite segmentos perdidos.
- O UDP não estabelece conexão prévia, não garante entrega, mas proporciona alta velocidade com baixo overhead.
- A compressão de sequências consecutivas de blocos zerados no IPv6 (`::`) só pode ser utilizada uma única vez no endereço.

