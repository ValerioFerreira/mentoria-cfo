##### informatica/a00/s01
Este trecho conta como a Internet nasceu, quais serviços ela oferece, o que é uma rede de computadores e como as redes são classificadas pelo alcance geográfico (PAN, LAN, MAN e WAN).

### Contexto histórico da Internet

A Internet surgiu como um sistema de redes interconectadas, criado com fins militares nos Estados Unidos durante a Guerra Fria. O objetivo era manter a comunicação segura mesmo diante de uma guerra nuclear. Nos anos 1950 foi criada a **ARPA** (Advanced Research Projects Agency), para manter o país na vanguarda tecnológica militar, em especial depois que a União Soviética lançou o satélite Sputnik.

A **ARPANET**, precursora da Internet, nasceu nos anos 1960 ligando universidades. Seu grande diferencial foi usar **comutação por pacotes**, em vez da **comutação por circuito** típica da telefonia:

| Característica | Comutação por circuito | Comutação por pacotes |
| --- | --- | --- |
| Como funciona | Reserva uma linha dedicada para cada comunicação | A informação é dividida em blocos (pacotes) que viajam de forma independente |
| Uso dos recursos | Canal fica ocupado mesmo sem tráfego | Aproveitamento melhor, pois nada fica reservado ocioso |
| Robustez | Falha na linha derruba a comunicação | Mais resistente a falhas, pois cada pacote pode escolher outra rota |

Cada pacote pode seguir um caminho diferente e chegar fora de ordem; o destino os remonta na sequência correta. Pense em um relatório grande enviado em vários envelopes pelos Correios.

Com o crescimento da rede, surgiram dois problemas. O primeiro foi manter a lista de endereços dos computadores: em 1973 optou-se por um registro central na Universidade de Stanford. O segundo foi a incompatibilidade entre redes que usavam formatos de pacote diferentes. A solução foi adotar um conjunto comum de protocolos, o **TCP/IP**, que padroniza o envio e o recebimento de dados entre redes e dispositivos distintos. A interconexão de redes por meio do TCP/IP evoluiu até a Internet atual.

> ⚠️ Pegadinha: a Internet não é sinônimo de Web. A Web é apenas um dos serviços que funcionam sobre a Internet.

### Principais serviços da Internet

| Serviço | O que é | Protocolos típicos |
| --- | --- | --- |
| World Wide Web (WWW) | Visualização de páginas organizadas em sites, em hipermídia, acessadas por navegador; é o serviço mais usado | HTTP e HTTPS |
| Correio eletrônico | Composição, envio e recebimento de mensagens, de modo assíncrono; é anterior à própria Internet | POP3, IMAP e SMTP |
| Acesso remoto | Conectar-se a computadores distantes, com autenticação e criptografia quando necessário | SSH, RDP e VNC |
| Transferência de arquivos | Disponibilizar arquivos por download e upload | FTP e P2P |

Outras aplicações cobradas:

- **Wiki**: plataforma colaborativa em que vários usuários criam, editam e organizam o conteúdo em conjunto (exemplo: Wikipedia).
- **Ferramentas de busca**: pesquisam por palavras-chave, usando algoritmos que indexam e classificam páginas (Google, Bing, Yahoo).
- **Redes sociais**: conectam usuários que compartilham textos, imagens, vídeos e links, com curtidas, comentários e mensagens.
- **Grupos de discussão**: espaços (fóruns, listas de e-mail ou plataformas sociais) para debater temas de interesse comum.
- **Computação em nuvem**: guarda e processa dados e roda aplicativos por meio da Internet, sem depender de servidores locais; os recursos são oferecidos sob demanda, permitem escalar operações e reduzem custos de infraestrutura física.
- **Portais web**: centralizam em um único local notícias, e-mail, fóruns, comércio eletrônico e outros serviços, como porta de entrada para a navegação.

A Internet segue a arquitetura **cliente/servidor**: o **cliente** faz solicitações (por exemplo, abrir um site) e o **servidor** as processa e fornece os recursos (páginas, arquivos). Isso permite centralizar e gerenciar dados, com escalabilidade e compartilhamento de recursos.

### Conceito de rede e seus objetivos

Em definição formal, rede é o conjunto de terminais, equipamentos e meios de transmissão e comutação que, ligados entre si, viabilizam serviços. De forma simples: um conjunto de dispositivos, chamados **nós**, conectados por **links** de comunicação. Um nó pode ser computador, impressora, notebook, smartphone, tablet ou relógio inteligente, desde que esteja ligado a outros nós.

As primeiras redes surgiram em organizações para trocar informações com mais rapidez e confiança do que o transporte manual de cartões perfurados ou fitas magnéticas. O segundo benefício foi **compartilhar recursos físicos**, como uma impressora para todo o departamento ou dispositivos de armazenamento, na época caríssimos. O objetivo central, portanto, é o **compartilhamento de recursos** (equipamentos, programas e, principalmente, dados), além de servir como meio de comunicação por texto, áudio ou vídeo.

### Classificação por abrangência geográfica

As redes são classificadas quanto ao tamanho, ou área geográfica coberta, em PAN, LAN, MAN e WAN.

| Tipo | Descrição | Distância |
| --- | --- | --- |
| PAN (Personal Area Network) | Dispositivos pessoais (celular, tablet, notebook) | Poucos centímetros a poucos metros |
| LAN (Local Area Network) | Lares, escritórios, prédios, campus | Algumas centenas de metros a alguns quilômetros |
| MAN (Metropolitan Area Network) | Ligação entre matriz e filiais na mesma cidade | Em torno de dezenas de quilômetros |
| WAN (Wide Area Network) | Entre cidades, países ou continentes | Algumas dezenas a milhares de quilômetros |

#### PAN

Cobre uma área pequena, em torno de poucos metros. Também chamada de **WPAN** quando sem fio, pois seu principal meio é o **Bluetooth** (também usa Wi-Fi e USB). Exemplos: caixa de som ou fone sem fio ligado ao celular. Em geral tem alta velocidade, é mais segura pela proximidade física e simples de diagnosticar. Atenção: a PAN nem sempre aparece nas questões como classificação padrão.

#### LAN

Conecta dispositivos de uma área restrita (casa, escritório, prédio, campus, lan house). Oferece velocidade alta, baixa ocorrência de erros e pode ser **cabeada ou sem fio**, nas topologias barramento, anel ou **estrela (a mais comum)**. Usa tipicamente **Ethernet e Wi-Fi**, aceita medidas como firewall e tem complexidade moderada. Pegadinha clássica: dizer que a LAN usa apenas Wi-Fi ou que cobre um país inteiro está errado.

#### MAN

É maior que a LAN e menor que a WAN; normalmente resulta da interligação de várias LANs de uma cidade, como as filiais de uma rede de lanchonetes na mesma metrópole. Usa em geral Ethernet e fibra óptica, tem velocidade variável conforme a infraestrutura, maior risco de segurança pela extensão e problemas mais difíceis de isolar.

#### WAN

Rede de grande área, entre cidades, países ou continentes, para conectar redes geograficamente distantes (exemplo: pesquisas na Antártida enviando dados ao Brasil). **A Internet é o exemplo clássico de WAN.** Usa tecnologias como Frame Relay, MPLS e a própria Internet, tem velocidade geralmente menor pelas longas distâncias, complexidade alta e exige segurança rigorosa. Aparece em provas como a rede que cobre áreas dispersas, interliga várias sub-redes e usa inúmeras linhas de transmissão. Em termos de **escalabilidade**, a WAN precisa crescer muito mais do que a LAN.

> 💡 Redes sem fio: cada classificação tem correspondente sem fio (WPAN, WLAN, WMAN e WWAN), mas as provas nem sempre são rigorosas e tratam Wi-Fi local como LAN.

### Para fixar

- A Internet nasceu da ARPANET, rede de comutação por pacotes, e foi unificada pelo conjunto de protocolos TCP/IP.
- Na comutação por pacotes os dados são divididos, seguem rotas independentes e são remontados no destino; na comutação por circuito há linha dedicada.
- Web, e-mail, acesso remoto e transferência de arquivos são serviços com protocolos próprios (HTTP/HTTPS, POP3/IMAP/SMTP, SSH/RDP/VNC, FTP).
- A arquitetura é cliente/servidor: o cliente solicita, o servidor processa e responde.
- O objetivo principal de uma rede é compartilhar recursos e permitir comunicação.
- PAN (metros, Bluetooth), LAN (centenas de metros a quilômetros, estrela), MAN (dezenas de quilômetros, cidade), WAN (cidades a continentes).
- A Internet é uma WAN; LAN pode ser com ou sem fio.

