##### informatica/a04/s03
O controle de tráfego perimetral e a imposição de políticas corporativas de segurança da informação constituem a essência técnica dos firewalls. O trecho aborda os fundamentos conceituais do dispositivo, suas modalidades de operação (permissiva e restritiva), a estrutura de listas de controle de acesso (ACL), os tipos de firewalls existentes com ênfase no firewall pessoal, suas funções auxiliares de rede e o funcionamento básico da filtragem de pacotes estática (*stateless*).

### Conceitos Fundamentais e Natureza do Firewall

O firewall opera como uma barreira de controle posicionada entre redes com níveis de confiança distintos (como a rede local privada de uma organização e a Internet pública):

- **Definição e Formas de Implementação**: dispositivo concebido para regular, policiar, registrar e filtrar fluxos de tráfego de entrada e saída. Pode ser implementado estritamente em **hardware** (equipamentos dedicados com alto poder de processamento), em **software** (aplicativos residentes no sistema operacional) ou na forma híbrida de ambos.
- **Distinção Essencial em Relação ao Antivírus**:
  - *Firewall*: inspeciona cabeçalhos e fluxos de pacotes de dados de acordo com regras de acesso predefinidas, atuando de maneira preventiva para autorizar ou barrar conexões externas não permitidas.
  - *Antivírus*: analisa conteúdos de arquivos e processos utilizando assinaturas e heurística para localizar e desinfetar malwares já presentes na máquina.
- **Origem dos Ataques**: embora sua função primordial seja barrar incursões externas da Internet, um firewall bem posicionado internamente protege segmentos contra ameaças originadas dentro da própria rede local (como um computador departamental infectado tentando invadir servidores centrais).

### Modos Operacionais e Listas de Controle de Acesso (ACL)

A política de segurança de um firewall determina a lógica de tratamento das comunicações que trafegam pelo perímetro:

- **Modo Restritivo (Lista Branca / Whitelist)**:
  - Lógica: **tudo o que não for expressamente permitido é bloqueado por padrão**.
  - Comportamento: adota postura rígida análoga à da Administração Pública (onde só é lícito agir conforme autorização expressa). É a abordagem considerada tecnicamente mais segura, pois reduz drasticamente a superfície de ataque ao manter todas as portas fechadas exceto aquelas especificadas.
- **Modo Permissivo (Lista Negra / Blacklist)**:
  - Lógica: **tudo o que não for expressamente proibido é permitido por padrão**.
  - Comportamento: assemelha-se à esfera privada (onde tudo é lícito exceto o que a lei veda). Apresenta menor segurança, pois ameaças inéditas ou portas não catalogadas conseguem transpor o dispositivo.
- **Técnicas de Controle do Firewall**:
  - *Controle de Serviços*: define quais protocolos e aplicações de rede (como HTTP, DNS ou correio eletrônico) têm autorização para transitar nas portas lógicas.
  - *Controle de Direção*: estipula o sentido em que conexões podem ser iniciadas (por exemplo, autorizando conexões de dentro para fora, mas bloqueando novas conexões de fora para dentro).
  - *Controle de Usuário*: condiciona o tráfego à identidade e credenciais de autenticação do usuário solicitante.
  - *Controle de Comportamento*: regula a maneira como determinado serviço aceito é efetivamente consumido (por exemplo, bloqueando comportamentos anômalos em servidores web).

### Recursos e Funções Auxiliares dos Firewalls

Com a modernização das redes corporativas, equipamentos de firewall passaram a incorporar funções complementares:

| Função Auxiliar | Finalidade Operacional |
| --- | --- |
| **NAT (Network Address Translation)** | Traduz endereços IP privados internos em um IP público para saída à Internet. |
| **DMZ (Zona Desmilitarizada)** | Isola servidores de acesso público (Web, DNS, E-mail) da rede corporativa interna. |
| **VPN e Criptografia** | Cria túneis virtuais autenticados e criptografados para tráfego seguro remoto. |
| **Balanceamento de Carga** | Distribui requisições simultâneas entre múltiplos links ou servidores. |
| **Antispoofing e Filtro MAC** | Bloqueia pacotes com IP forjado e restringe conexões com base no endereço físico MAC. |

### Firewall Pessoal e Filtro de Pacotes

- **Firewall Pessoal**: software de proteção instalado em um computador individual (como o *Windows Defender Firewall*) voltado a proteger o host específico contra acessos indevidos e exploração remota de portas.
  - Registra tentativas de intrusão e impede comunicações não autorizadas disparadas por *backdoors* ou cavalos de Troia.
  - Contém preventivamente a propagação de *worms* pela rede ao isolar portas locais vulneráveis, embora não substitua o antivírus na remoção do código malicioso.
- **Filtro de Pacotes Estático (*Stateless*)**: modalidade primária de firewall que atua nas camadas de Rede (IP) e Transporte (TCP/UDP). Examina cada pacote isoladamente com base em endereços IP de origem/destino e números de portas lógicas (ex.: 80, 443, 53), sem guardar histórico das conexões ou do estado da sessão.

### Detalhes que caem em prova

- **Definição mais cobrada:** dispositivo (software, hardware ou a combinação) que regula o tráfego entre redes distintas, barrando acessos prejudiciais ou sem autorização que passem de uma rede a outra. Não é correto dizer que existe apenas como software ou apenas como hardware, nem que sua função é impedir o tráfego de vírus. Duas em cada três questões cobram só a definição.
- **Exemplos de implementação:** Windows Firewall (Windows), IPTables/Netfilter (Linux) e firewall do macOS; o roteador doméstico já traz um. Empresas usam equipamentos mais robustos e caros. Os primeiros firewalls foram implementados em roteadores.
- **O que faz:** controla, analisa, registra, policia, monitora, regula e filtra a entrada e a saída de dados conforme a política de segurança (conjunto de regras que permite ou proíbe o acesso aos ativos). Tudo que não viola as regras continua fluindo normalmente.
- **Firewall de borda × interno:** o de borda fica entre a rede interna e a Internet. Um firewall interno pode proteger, por exemplo, o banco de dados da folha de pagamento mesmo depois de o usuário ter entrado na intranet. **Atenção:** as bancas não têm entendimento único; algumas questões (como uma da Polícia Federal de 2014) consideram que firewalls não protegem contra ataques internos, enquanto outras (como a da FUB de 2016) aceitam que impedem acesso indevido dentro da rede e vindo da Internet. Leia o enunciado para ver se trata só do firewall de borda.
- **Firewall não é antivírus:** o firewall analisa pacotes segundo uma política e age de forma preventiva; o antivírus identifica e elimina de forma reativa o malware já presente. Recomenda-se usar os dois.
- **Modo restritivo × permissivo:** o restritivo bloqueia o que não foi expressamente permitido (lista branca, como o servidor público, que só faz o que a lei autoriza); o permissivo libera o que não foi expressamente proibido (lista negra, como o particular). A lista branca é mais segura; o conjunto de regras da organização é a ACL (lista de controle de acesso). Em geral, o firewall trabalha em modo restritivo.
- **Técnicas:** controle de serviço (quais serviços de Internet podem ser acessados, filtrando por IP e porta TCP, podendo usar proxy), de direção (sentido em que as solicitações podem ser iniciadas), de usuário (acesso conforme quem pede; para usuários externos, exige autenticação segura) e de comportamento (como os serviços são usados, por exemplo filtrando spam ou liberando só parte de um servidor web). Cuidado: dizer que o controle de comportamento define quais serviços podem ser acessados é troca com o controle de serviço.
- **Funções auxiliares:** NAT, DMZ, balanceamento de carga, antispoofing, autenticação de usuário, VPN/criptografia, alta disponibilidade, filtros de URL, spam e e-mail, bloqueio de alguns ataques de negação de serviço e bloqueio por endereço MAC (camada de enlace). Não são o foco do firewall, e quanto mais funções, maior a complexidade da administração.
- **Firewall pessoal:** protege um computador contra acessos não autorizados vindos da Internet; o antimalware não impede que alguém explore vulnerabilidades pela rede nem o uso de backdoor, daí a necessidade dele. Bem configurado, registra tentativas de acesso e bloqueia o envio a terceiros de dados coletados por invasores, bloqueia invasões e permite identificar a origem, filtra o conteúdo das conexões e barra a comunicação entre invasor e código malicioso instalado, e impede a propagação de código já instalado. Verifique a procedência, mantenha-o ativo e configure o registro com o máximo de informações. Filtrar spam, listar programas desatualizados e alertar sobre páginas falsas não são funções do firewall pessoal. Programas e portas usados pelo usuário às vezes precisam ser liberados. O Windows Defender Firewall unificou antimalware e firewall no Windows 10.
- **Filtro de pacotes e portas:** o computador tem 65.536 portas, cada uma associada a um serviço (SMTP 587, DNS 53, HTTP 80, HTTPS 443); o firewall funciona como um muro com portas, e o filtro de pacotes decide por IP e porta.

### Para fixar

- Um firewall pode ser implementado exclusivamente em software, em hardware ou de forma híbrida.
- O modo restritivo adota lista branca: bloqueia tudo por padrão e autoriza apenas o que está expresso.
- O modo permissivo adota lista negra: aceita tudo por padrão e barra somente o que está listado.
- O firewall atua preventivamente controlando conexões, enquanto o antivírus detecta e destrói malwares.
- Um firewall pessoal protege o dispositivo individual, bloqueando tentativas de invasão e comunicações de backdoors.
- O firewall impede a propagação de worms pela rede, mas não é capaz de exterminar o malware já instalado.
- O filtro de pacotes simples é estático (*stateless*): analisa pacotes individualmente sem rastrear o estado da sessão.
- Serviços adicionais como NAT, DMZ e VPN são funções auxiliares frequentemente agregadas a firewalls modernos.

