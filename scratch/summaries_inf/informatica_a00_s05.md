##### informatica/a00/s05
A localização e a transferência de objetos na Internet apoiam-se em identificadores universais de recursos, protocolos de aplicação orientados à navegação web, mecanismos dedicados para cópia de arquivos e sistemas de voz digitalizados sobre pacotes IP.

### Sintaxe Completa da URL e Estrutura de Domínios

O Localizador Padrão de Recursos (*Uniform Resource Locator* - URL) constitui o endereço formal de um objeto em rede. Uma URL completa decompõe-se nos seguintes segmentos hierárquicos:

- **Protocolo ou Esquema**: método de comunicação exigido para acessar o conteúdo (como `http://`, `https://` ou `ftp://`).
- **Autenticação de Usuário (Opcional)**: credenciais no formato `usuario:senha@`, raramente expostas de modo direto na web moderna por razões de confidencialidade.
- **Host ou Domínio**: endereço lógico do servidor (nome amigável como `www.exemplo.com.br` ou endereço IP direto).
- **Porta de Comunicação (Opcional)**: ponto de conexão TCP/UDP de destino (porta 80 para HTTP padrão, porta 443 para HTTPS), frequentemente implícita.
- **Caminho de Diretórios (*Path*)**: sequência de pastas e subpastas no sistema de arquivos do servidor que conduz ao arquivo ou recurso requisitado.
- **Parâmetros de Consulta (*Query String*)**: iniciados pelo caractere `?` e concatenados por `&`, enviando pares chave-valor para processamento dinâmico em scripts do servidor.
- **Fragmento ou Âncora**: introduzido pelo símbolo cerquilha `#`, identifica um marcador interno específico no documento. O fragmento é processado exclusivamente pelo navegador no cliente e nunca é transmitido na requisição HTTP ao servidor.

No Brasil, os registros sob o domínio `.br` (coordenados pelo Registro.br) obedecem a regras estritas de composição: tamanho de 2 a 26 caracteres (sem incluir a categoria), formado por caracteres alfanuméricos, não podendo conter apenas números nem iniciar ou terminar por hífen.

### Protocolos Web: HTTP e HTTPS

Operando na camada de aplicação sob o modelo cliente/servidor:

- **Protocolo HTTP (*HyperText Transfer Protocol*)**:
  - Transporta dados multimídia e páginas de hipertexto de forma textual e desprovida de criptografia padrão (porta padrão TCP 80).
  - É um protocolo sem estado (*stateless*), no qual cada requisição é tratada de forma autônoma sem retenção nativa de contexto anterior da conexão.
  - Respostas do servidor retornam códigos de status numéricos padronizados divididos em classes: informativos (1xx), sucesso (2xx, ex.: 200 OK), redirecionamentos (3xx), erros do cliente (4xx, ex.: 404 Not Found) e falhas internas do servidor (5xx, ex.: 500 Internal Server Error).

- **Protocolo HTTPS (*HTTP Secure*)**:
  - Implementação do HTTP envelopado por uma camada criptográfica SSL/TLS (*Transport Layer Security*), operando habitualmente na porta TCP 443.
  - Provê três pilares fundamentais de segurança: confidencialidade (cifragem simétrica e assimétrica dos pacotes em trânsito), integridade (garantia de que a carga não foi alterada) e autenticação mútua através de certificados digitais validados por Autoridades Certificadoras (AC).

### Protocolo de Transferência de Arquivos (FTP)

O FTP (*File Transfer Protocol*) atua na camada de aplicação com a missão precípua de efetuar download (obtenção) e upload (envio) de arquivos entre sistemas computacionais:

- **Arquitetura de Duas Conexões**:
  - *Canal de Controle (Porta TCP 21)*: estabelece a autenticação, navega em diretórios remotos e transmite comandos de controle. Permanece ativo durante toda a sessão.
  - *Canal de Dados (Porta TCP 20 no modo ativo)*: canal aberto sob demanda exclusivamente para efetivar o fluxo binário de transferência de arquivos ou listagem volumosa de diretórios.
- **Distinção Prática de Transferência**: embora o FTP seja projetado especificamente para manipulação de arquivos, diversas outras aplicações e protocolos também executam transferência de arquivos acessoriamente (como HTTP para downloads em páginas da web e SMTP com extensões MIME para anexos de mensagens eletrônicas).

### Serviço de Voz sobre IP (VoIP)

A tecnologia VoIP (*Voice over Internet Protocol*) viabiliza o tráfego de voz falada e transmissões multimídia convertendo o sinal analógico de áudio em dados digitais fracionados em pacotes IP.

- **Comutação por Pacotes versus Circuitos**: ao contrário da rede telefônica convencional comutada (PSTN), que aloca canais físicos dedicados e cobra tarifas proporcionais a distâncias geográficas, o VoIP trafega sobre a infraestrutura compartilhada da Internet via comutação de pacotes, reduzindo drasticamente custos corporativos.
- **Protocolos de Transporte e Sinalização**:
  - Os blocos amostrais de voz em tempo real são encapsulados preferencialmente no protocolo de transporte UDP, uma vez que a agilidade e a baixa latência superam a necessidade de integridade estrita; pequenos atrasos ou perdas residuais de milissegundos não justificam retransmissões onerosas típicas do TCP.
  - Todavia, a inicialização, o controle de sessão e a terminação das chamadas adotam protocolos de sinalização estruturados (como SIP e H.323), garantindo que a comunicação seja coordenada de forma orientada à conexão.
- **Equipamentos e Desvantagens**: ligações podem ser integradas por telefones IP dedicados ou via adaptadores ATA (*Analog Telephone Adapter*). Sujeita-se a jitter, variações de latência e dependência da qualidade da banda larga e do fornecimento elétrico contínuo.

### Para fixar

- A URL organiza protocolo, domínio, porta, caminho, parâmetros de consulta (`?`) e fragmento (`#`).
- O fragmento (`#`) é tratado localmente pelo navegador e não é enviado ao servidor.
- HTTP (porta 80) é aberto e *stateless*; HTTPS (porta 443) acrescenta criptografia SSL/TLS e certificados digitais.
- FTP usa duas portas: 21 para controle e 20 para dados.
- VoIP digitaliza a voz e a transporta em pacotes (em geral UDP).
- SIP e H.323 são protocolos de sinalização usados em VoIP.

