##### informatica/a01/s02
O modelo de interconexão corporativa contemporâneo expande as fronteiras da rede local para integrar parceiros e filiais através de arquiteturas de Extranet e canais seguros estruturados sobre Redes Privadas Virtuais (VPN).

### Conceito e Delimitação da Extranet

A extranet consubstancia uma extensão controlada da intranet institucional que se projeta sobre a infraestrutura pública da Internet, permitindo que entidades externas previamente autorizadas — tais como fornecedores, clientes corporativos, prestadores de serviços e parceiros comerciais — acessem módulos, bases e serviços específicos da corporação.

- **Diferenciação Prática de Acesso**:
  - *Intranet Local*: colaborador operando fisicamente nas dependências da organização e conectado aos comutadores e servidores internos.
  - *Intranet Remota*: funcionário executando trabalho a distância que se conecta de modo seguro aos repositórios internos da empresa via canal criptografado.
  - *Extranet*: parceiro externo de negócios, fornecedor ou cliente homologado que acessa recursos delimitados e autorizados da organização a partir de ambiente externo.
  - *Portal Web Público*: usuário convencional que acessa um website aberto na Internet; a mera exigência de credenciais de login em portal público corporativo não caracteriza acesso à intranet nem à extranet.

- **Finalidades e Aplicações Corporativas**:
  - Fortalecimento da comunicação ao longo da cadeia de suprimentos (*supply chain*).
  - Viabilização de transações eletrônicas *Business-to-Business* (B2B).
  - Execução coordenada de projetos colaborativos interorganizacionais.
  - Disponibilização de consultas de estoque, faturamento e logística para distribuidores homologados.

### Redes Privadas Virtuais (VPN) e Tecnologias de Conexão

Para assegurar que o tráfego corporativo trafegue sobre a Internet sem interceptação ou devassa indevida, a extranet comumente adota túneis protegidos por VPN (*Virtual Private Network*).

#### Mecanismos de Tunelamento e Criptografia
O tunelamento consiste em encapsular um pacote de dados original (frequentemente cifrado) no interior de outro invólucro de dados para viabilizar seu transporte por redes públicas intermediárias. No ponto de destino, ocorre o desencapsulamento para recuperação do conteúdo original. A cifragem isolada apenas garante a confidencialidade do conteúdo contra leitura indevida, enquanto o tunelamento fornece a rota estruturada de transporte dos pacotes corporativos. Os protocolos de tunelamento podem operar na camada de enlace ou na camada de rede (como IPSec e L2TP).

#### Modelos de Topologia VPN

- **VPN Site-to-Site (Gateway a Gateway ou Roteador a Roteador)**:
  - Destina-se a interligar duas redes locais completas geograficamente separadas, como a sede matriz e filiais regionais.
  - O canal seguro é mantido permanentemente entre dispositivos concentradores (*gateways* de borda ou roteadores), tornando o processo transparente aos computadores de ponta em cada segmento.

- **VPN Client-to-Site (Acesso Remoto)**:
  - Estabelece uma conexão protegida individual entre um único dispositivo terminal e a rede corporativa remota.
  - Exige a instalação ou configuração de cliente de software no dispositivo do usuário, que autentica credenciais e direciona o tráfego de trabalho ao concentrador central.

### Para fixar

- Extranet: acesso externo restrito concedido a parceiros, fornecedores e clientes autorizados.
- Intranet: rede privada restrita ao quadro interno da organização.
- Internet: rede pública e universal.
- VPN Site-to-Site: conecta redes inteiras, por meio de gateways de borda.
- VPN Client-to-Site: conecta um equipamento isolado à rede corporativa central.
- A VPN funciona com tunelamento e criptografia, protegendo o tráfego que cruza a Internet.

