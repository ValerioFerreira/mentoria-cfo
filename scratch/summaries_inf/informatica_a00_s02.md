##### informatica/a00/s02
A compreensão da infraestrutura digital global exige diferenciar a infraestrutura de rede da Internet de suas aplicações de topo, compreender as gerações evolutivas da World Wide Web, delimitar as camadas de visibilidade de dados na rede e analisar as arquiteturas de acesso do usuário final.

### Distinção entre Internet e Web e Evolução das Gerações Web

Internet e Web constituem conceitos técnicos distintos que operam em camadas funcionais complementares:

- **Internet versus Web**: a Internet é a infraestrutura física e lógica mundial de telecomunicações que interliga redes de computadores sob a pilha TCP/IP. A *World Wide Web* (WWW), idealizada em 1989 por Tim Berners-Lee com as especificações do protocolo HTTP e da linguagem HTML, é apenas uma entre as diversas aplicações que trafegam sobre a infraestrutura da Internet (ao lado de serviços de e-mail, VoIP e transferência de arquivos).
- **Gerações da Web**:
  - *Web 1.0 (Web Estática ou Informativa)*: caracterizada pelo consumo passivo de hipertexto unidirecional. Produtores e jornalistas publicavam páginas estáticas em HTML e a grande massa de internautas apenas realizava leitura, sem interação colaborativa.
  - *Web 2.0 (Web Social ou Participativa)*: transição para plataformas dinâmicas e colaborativas alavancadas por tecnologias como AJAX, APIs e feeds RSS. O usuário converteu-se em produtor e distribuidor ativo de conteúdo em blogs, wikis e redes sociais.
  - *Web 3.0 (Web Semântica ou Inteligente)*: incorporação de inteligência artificial, processamento de linguagem natural e aprendizado de máquina para contextualizar os dados, gerando experiências hiperpersonalizadas e integração com assistentes virtuais e objetos conectados. Também se associa a blockchain e descentralização, dando ao usuário mais controle sobre os próprios dados e permitindo interagir com aplicações sem intermediários. Comparação: interatividade baixa (1.0), alta (2.0) e muito alta (3.0); tecnologias típicas HTML, AJAX/APIs/RSS e IA/aprendizado de máquina. As gerações não se excluem, elas se sobrepõem.

### Camadas da Web: Surface Web, Deep Web e Dark Web

O ecossistema de dados na teia mundial distribui-se em diferentes níveis de visibilidade e indexação:

- **Surface Web (Web de Superfície)**: representa a camada pública indexada por robôs de busca convencionais (Google, Bing). Engloba websites estáticos, portais noticiosos e páginas abertas acessíveis sem barreiras de autenticação direta.
- **Deep Web (Web Profunda)**: engloba a grande massa de páginas e repositórios não indexáveis por mecanismos de busca públicos gerais. Compreende intranet corporativa, extranets, prontuários médicos, caixas postais de e-mail, portais de internet banking, plataformas de cursos sob login e bancos de dados acadêmicos protegidos por senha ou muros de consulta dinâmica.
- **Dark Web (Web Escura)**: subconjunto especializado da Deep Web que opera sobre redes sobrepostas (*overlay networks*) e arquiteturas descentralizadas com tráfego fortemente cifrado, como o Tor (*The Onion Router*). Demanda navegadores específicos e configurações pontuais, proporcionando anonimato tanto para os emissores quanto para os servidores hospedeiros.

### Internet das Coisas (IoT)

A Internet das Coisas (*Internet of Things* - IoT) refere-se à interconexão digital de objetos físicos do cotidiano — lâmpadas, eletrodomésticos, termostatos, sensores industriais e veículos — dotados de sensores, atuadores e conectividade de rede, que coletam e trocam dados em tempo real.

- **Conectividade e Protocolo IPv6**: o avanço da IoT decorre criticamente da expansão do protocolo IPv6, cujo espaço de endereçamento de 128 bits supriu o esgotamento do IPv4, permitindo alocar endereços IP exclusivos a bilhões de novos dispositivos autônomos.
- **Ecossistema Operacional**: os dados captados pelos sensores são frequentemente canalizados para instâncias de computação em nuvem (*cloud computing*) ou nós de borda (*edge computing*), viabilizando monitoramento remoto contínuo, automação residencial e telemetria preditiva.

### Tecnologias de Conexão e Hierarquia de Provedores (ISPs)

A transmissão global apoia-se em troncos de altíssima velocidade (*backbones* terrestres e submarinos de fibra óptica) e distribui-se através de Provedores de Serviços de Internet (ISPs):

- **Hierarquia de ISPs**:
  - *Tier 1 (Nível 1)*: grandes operadoras globais proprietárias de infraestruturas continentais e transoceânicas. Trocam tráfego entre si sem ônus tarifário (*peering*) e compõem a espinha dorsal da Internet.
  - *Tier 2 (Nível 2)*: operadoras de abrangência nacional ou regional que adquirem trânsito de redes Tier 1 e podem revender conectividade para provedores de menor escala.
  - *Tier 3 (Nível 3 / Provedores Locais)*: provedores de acesso final que compram banda de camadas superiores para atender diretamente aos domicílios e empresas clientes.

- **Meios de Acesso Domiciliar e Empresarial**:
  - *Dial-Up*: conexão discada analógica legada (até 56 Kbps) que monopolizava a linha telefônica.
  - *ADSL*: linha digital de assinante assimétrica sobre par trançado de cobre, permitindo tráfego simultâneo de voz e dados com taxa de download superior ao upload.
  - *HFC (Hybrid Fiber-Coaxial)*: combinação de anéis de fibra óptica da operadora com cabos coaxiais na distribuição de ponta (típico de redes de TV a cabo).
  - *FTTH (Fiber to the Home)*: cabeamento de fibra óptica estendido até o interior da residência do assinante, ofertando taxas simétricas, altíssima largura de banda e latência reduzida.
  - *PLC, Rádio, Satélite e Celular*: tecnologias complementares empregando a fiação elétrica (PLC), enlaces de micro-ondas, satélites de órbita baixa ou geoestacionários, e redes móveis celulares (3G, 4G, 5G).

### Componentes da Web e detalhes cobrados

| Componente | Função |
| --- | --- |
| Hipertexto | documentos ligados por hiperlinks |
| URL | endereço único de cada recurso |
| Navegador | aplicativo que exibe e permite interagir com os documentos (Chrome, Firefox, Edge, Safari) |
| Protocolos | HTTP e HTTPS levam os dados entre navegador e servidor |
| Servidor web | máquina que hospeda os recursos e responde às requisições |
| Página web | documento escrito em linguagem de marcação (HTML), com texto, imagens e links |
| Motor de busca | indexa e classifica páginas por palavras-chave |

- **Analogia:** a Internet é a malha de estradas; a Web são as lojas e os destinos ao longo delas.
- **Surface × Deep:** a fonte estima que a Surface Web seja só cerca de 4% do total e a Deep Web, os 96% restantes (estimativa genérica, não uma medida exata). A Intranet é um exemplo de Deep Web, mas não é totalmente segura: a comunicação deixa rastros.
- **Dark Web × Darknet:** a darknet é a infraestrutura de rede anônima; a Dark Web são os sites e conteúdos hospedados dentro dela.
- **Tor:** nasceu como projeto militar dos EUA para comunicação segura. Os pedidos passam por uma sequência de servidores proxy voluntários e várias camadas de criptografia (daí "cebola"), o que impede identificar a origem. O navegador Tor também abre a Surface Web; nesse caso, não se identifica quem acessa, mas se pode identificar o serviço acessado. Páginas que só existem dentro da rede Tor são totalmente anônimas.
- **IoT, quatro componentes:** dispositivos, tecnologias de comunicação (Wi-Fi 802.11, Bluetooth 802.15, Zigbee, LoRa, 3G/4G/5G), sensores e atuadores (os sensores captam o ambiente; os atuadores executam ações, como ligar ou desligar) e nuvem. A IoT costuma usar redes de longa distância e baixo consumo (LPWAN), ao contrário do Bluetooth, que é de curto alcance e baixo consumo (rede pessoal). Riscos: acesso não autorizado, uso indevido de dados pessoais e dispositivos usados em botnets.
- **Backbone:** formado por satélites, ondas de rádio e cabos de fibra óptica terrestres e submarinos; a fonte diz que responde por cerca de 80% da comunicação global. ISPs vendem acesso a provedores menores e a usuários finais.
- **Satélite:** atende áreas remotas, mas com maior latência e menor velocidade que as soluções terrestres. **Rádio:** usa torres, boa para áreas rurais, e depende da distância e do clima. **ADSL:** velocidade típica de até 24 Mbps.
- **Modem × roteador:** o modem converte os sinais do computador para o meio usado (telefone, cabo coaxial, fibra, rádio); em redes modernas o roteador muitas vezes já traz o modem integrado. Todo computador precisa de placa de rede (NIC), Ethernet ou Wi-Fi.

### Para fixar

- Internet é a infraestrutura física e lógica mundial de interconexão; Web é a aplicação de hipertexto que roda sobre ela (HTTP e HTML).
- Deep Web: conteúdo restrito por credenciais ou não indexado por buscadores públicos (bancos de dados, intranets).
- Dark Web: parte da Deep Web que exige roteamento cifrado, como o Tor.
- IoT: objetos físicos conectados à rede, apoiados no endereçamento IPv6.
- No acesso residencial, a hierarquia vai dos provedores Tier 1 (backbones globais) aos Tier 2 e Tier 3.
- Tecnologias de acesso citadas: FTTH (fibra até a casa), HFC (cabo coaxial/fibra) e ADSL (linha telefônica).
- Backbone (fibra, satélite, rádio) sustenta o acesso; modem converte o sinal e o roteador pode integrá-lo.

