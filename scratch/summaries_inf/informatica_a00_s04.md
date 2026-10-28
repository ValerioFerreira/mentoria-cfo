##### informatica/a00/s04
Os protocolos da camada de aplicação do modelo TCP/IP disponibilizam serviços essenciais para a experiência do usuário final, abrangendo o intercâmbio de mensagens eletrônicas, a configuração automática de parâmetros de rede e a tradução mnemônica de localizadores de recursos.

### Serviços de Correio Eletrônico: SMTP, POP3, IMAP e Acesso Web

- **Protocolo SMTP (*Simple Mail Transfer Protocol*)**:
  - Responsável exclusivamente pelo envio (*push*) e roteamento de correspondências eletrônicas.
  - Opera tanto na transmissão da máquina cliente para o servidor de correio de saída quanto no repasse subsequente entre servidores intermediários na Internet.
- **Protocolo POP3 (*Post Office Protocol*, versão 3)**:
  - Destinado à recuperação e download de e-mails da caixa postal do servidor para o terminal do usuário.
  - No modelo clássico, transfere os arquivos para a máquina local e exclui as cópias originais hospedadas no servidor, inviabilizando sincronização homogênea entre múltiplos terminais.
- **Protocolo IMAP (*Internet Message Access Protocol*)**:
  - Desenvolvido para acesso interativo e sincronizado em tempo real.
  - As mensagens, pastas e marcações de status permanecem preservadas na nuvem do servidor, permitindo que alterações efetuadas em um celular reflitam imediatamente no computador de mesa.
- **Ambiente Webmail**:
  - Modalidade na qual o gerenciamento de e-mails ocorre dentro de navegadores web utilizando os protocolos HTTP e HTTPS, dispensando clientes dedicados de correio eletrônico.

### Infraestrutura de Conexão: DHCP e DNS

- **Protocolo DHCP (*Dynamic Host Configuration Protocol*)**:
  - Automatiza a distribuição de parâmetros de conectividade TCP/IP em redes locais com base em concessões dinâmicas (*leases*).
  - Atribui dinamicamente aos computadores clientes: endereço IP utilizável, máscara de sub-rede correspondente, endereço do gateway padrão e apontadores para os servidores de nomes (DNS).
  - Utiliza o protocolo de transporte UDP (portas 67 para servidores e 68 para clientes).
- **Protocolo DNS (*Domain Name System*)**:
  - Base de dados distribuída e hierárquica que traduz endereços alfanuméricos inteligíveis para seres humanos (como `www.exemplo.com.br`) em endereços numéricos IP operados pelos roteadores.
  - Permite a navegação mnemônica, operando preferencialmente sob a porta 53 via pacotes UDP para consultas rápidas.

### Anatomia Estrutural dos Localizadores de Recursos (URL)

- **Composição da URL (*Uniform Resource Locator*)**:
  - *Esquema/Protocolo*: define a regra de comunicação a ser aplicada (ex.: `http://`, `https://`, `ftp://`).
  - *Domínio/Host*: identifica a máquina ou serviço na rede mediante nome de domínio ou endereço IP.
  - *Porta*: canal de comunicação lógica de transporte (frequentemente omitida quando padrão, como 80 para HTTP e 443 para HTTPS).
  - *Caminho e Recurso*: hierarquia de pastas lógicas e nome do arquivo específico no servidor (ex.: `/noticias/artigo.html`).
  - *Parâmetros de Consulta (Query String)*: argumentos variáveis iniciados pelo delimitador `?` e concatenados por `&`.
  - *Âncora/Fragmento*: marcador precedido por `#` que desloca a visualização para um ponto específico da página.

### Detalhes que caem em prova

| Termo | Significado |
| --- | --- |
| Cliente de e-mail | aplicativo instalado na máquina (Thunderbird, Outlook) |
| Servidor de e-mail | máquina que recebe as mensagens e as repassa ao servidor de destino |
| Provedor de e-mail | empresa que hospeda o serviço (Gmail, Yahoo, UOL) |
| Webmail | aplicação hospedada em servidor remoto, usada no navegador |

- **Comparação POP3 × IMAP:** POP3 (porta 110) lê as mensagens offline, não cria pastas no servidor, não permite ver só o cabeçalho antes de baixar nem baixar parcialmente, e as mudanças feitas em um aparelho não aparecem nos outros. IMAP (porta 143) trabalha online por padrão, permite pastas e várias caixas postais, pré-visualizar o cabeçalho, pesquisar no servidor, baixar parte da mensagem e manter todos os dispositivos sincronizados. A versão segura (IMAPS) usa a porta 993.
- **Modos do POP3:** no modo padrão (baixar e apagar) a cópia do servidor é removida; em outro modo as mensagens são baixadas e uma cópia fica no servidor, com risco de esgotar o limite de espaço.
- **Webmail não usa IMAP:** o navegador fala com o servidor web por HTTP/HTTPS, tanto para enviar quanto para ler; é comum associar erroneamente webmail a IMAP. O webmail exige só um navegador, guarda as mensagens na nuvem do provedor e deixa segurança e atualização por conta do provedor.
- **Fluxo de uma mensagem:** o e-mail é assíncrono (o destinatário lê quando quiser). Dentro do mesmo provedor, o servidor apenas coloca a mensagem na caixa postal do destinatário. Entre provedores diferentes, o servidor de saída olha a parte depois da @ (domínio) para encontrar o servidor de entrada, envia por SMTP, e este usa a parte antes da @ para achar a caixa postal. O destinatário recupera depois por POP3 ou IMAP. O SMTP moderno tem autenticação para reduzir spam.
- **DHCP:** aloca endereços de modo dinâmico, automático ou estático, e recolhe de volta o IP quando a conexão termina, para reutilizá-lo. IP dinâmico muda a cada nova conexão; IP estático é fixo e comum em servidores. O endereço IP é lógico e pode mudar; o MAC é físico e permanente.
- **DNS:** funciona como agenda de contatos da Internet; usa consulta e resposta, hierarquia de servidores, guarda respostas recentes em cache para reduzir tempo e tráfego e tem extensões de segurança. Traduz nome para IP e também o inverso. Digitar o IP no navegador abre o mesmo site que o nome, pois o computador só entende endereços IP.
- **Sintaxe da URL:** protocolo://IP-ou-domínio:porta/caminho/recurso. O caminho é a estrutura de diretórios no servidor; recurso é o arquivo ou item procurado.

### Para fixar

- SMTP envia e-mail; POP3 baixa as mensagens e, tradicionalmente, esvazia a caixa no servidor.
- IMAP mantém as mensagens no servidor e sincroniza vários dispositivos; Webmail funciona por HTTP/HTTPS no navegador.
- DHCP entrega automaticamente ao host endereço IP, máscara, gateway e DNS.
- DNS converte nomes amigáveis em endereços IP (porta 53, em regra UDP).
- Estrutura da URL: protocolo, domínio, porta opcional, caminho do recurso, parâmetros de busca após `?` e âncora após `#`.

