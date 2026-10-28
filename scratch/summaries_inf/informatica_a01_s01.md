##### informatica/a01/s01
Este trecho distingue as três redes que organizam o acesso à informação: a Internet (pública e global), a Intranet (privada e interna) e a Extranet (ponte controlada para usuários externos). O peso maior está na Intranet, cuja comparação com a Internet rende pegadinhas recorrentes.

### Visão geral das três redes

| Rede | Quem acessa | Exemplo |
| --- | --- | --- |
| Internet | Qualquer pessoa com dispositivo e conexão | Navegar no site de uma loja virtual |
| Intranet | Somente membros autorizados da organização | Funcionário consultando estoque e folha de pagamento |
| Extranet | Usuários externos autorizados, como fornecedores | Área exclusiva para parceiros |

Intranet e extranet são **tipos de rede de computadores** e são **construídas sobre o modelo da internet**, isto é, com TCP/IP, HTTP e demais tecnologias dela, mas em contexto de rede privada. A extranet liga a rede interna da empresa a pessoas de fora, devidamente autorizadas; ela pode envolver a união de redes de organizações parceiras, enquanto a intranet fica restrita à própria organização.

### Internet

Internet é a **rede mundial de computadores**: um conjunto de segmentos de redes públicas espalhados pelo globo e interconectados, que trocam informações por meio de **protocolos comuns**. O nome vem de *inter* (entre) e *net* (rede): é uma **rede de redes**, formada por incontáveis redes locais (LANs) de casas, empresas, escolas.

- **Pública não é sinônimo de gratuita**: pública significa aberta a qualquer pessoa que cumpra requisitos mínimos, como contratar um provedor.
- **Classificação**: tecnicamente é uma **WAN** (rede de área ampla), pela abrangência geográfica, apesar de ser composta por LANs e MANs.
- **Backbones**: grandes canais de alta capacidade, geralmente de fibra óptica (inclusive submarinos), que ligam continentes e sustentam o tráfego. Funcionam como a espinha dorsal da rede.
- **Protocolos**: a Internet funciona porque todos os dispositivos "falam a mesma língua", a **arquitetura TCP/IP**, a principal família de protocolos tanto da Internet quanto das intranets. Outras famílias antigas (AppleTalk, NetBIOS, SPX/IPX, NetBEUI) são de redes específicas e não sustentam a Internet.
- **Acesso**: dá-se por um **provedor de Internet** (ISP), empresa que vende o acesso à infraestrutura, por fibra óptica ou outro meio. É a ideia do pedágio para entrar na estrada.
- **Controle**: descentralizado e distribuído; ninguém é dono único. A manutenção cabe a uma rede de provedores, empresas e governos.

Características resumidas da Internet:

| Aspecto | Descrição | Observação |
| --- | --- | --- |
| Acesso | Público, para qualquer pessoa com conexão | Controle descentralizado |
| Alcance | Global, em tempo real | Interliga milhões de dispositivos |
| Segurança | Menor controle; sujeita a ataques, vazamentos e interceptações | Exige firewalls, criptografia e outras camadas |

A Internet é também o conjunto de **serviços** que usam essa infraestrutura: Web (WWW, páginas HTML requisitadas sob demanda), correio eletrônico, grupos de discussão, mensagens instantâneas, **FTP** (transferência de arquivos: envio é *upload*, recebimento é *download*), bate-papo e redes sociais. Os **hiperlinks** permitem a leitura **não sequencial** de páginas, característica marcante da Web.

> ⚠️ Pegadinha: LAN (rede local, área pequena) não é a Internet. Intranet e extranet não são "tipos de Internet de outros países" nem se limitam a máquinas de usuários: incluem servidores e outros equipamentos de rede.

### Intranet

**Intranet** é a rede interna de uma organização, **fechada ao público em geral** e aberta só a quem for autorizado. Ela reaproveita as **mesmas tecnologias, padrões e serviços da Internet** para dividir informações e recursos e facilitar a comunicação entre os membros. Costuma ser uma LAN, mas o ponto central é o acesso restrito, não o tamanho. Pode pertencer a empresa, repartição pública, escola ou hospital.

> ⚖️ Ideia-chave: a intranet é a "internet da empresa, com chave na porta".

#### O ponto mais cobrado: mesmas tecnologias

A intranet utiliza os **mesmos protocolos** (pilha TCP/IP, HTTP, HTTPS, FTP) e os **mesmos serviços** da Internet: navegação em páginas, transferência e compartilhamento de arquivos, compartilhamento de impressoras, streaming de vídeo, formulários eletrônicos e chat interno. Tudo o que foi desenvolvido para a Internet pode ser usado em intranets de qualquer porte.

Por isso são **erradas** afirmações como "Internet e intranet operam com protocolos diferentes" ou "a intranet não utiliza as mesmas tecnologias da Internet". A intranet também **não se define** apenas por usar endereços IP numa rede local: isso não basta para classificá-la.

#### A diferença é o acesso

| Critério | Internet | Intranet |
| --- | --- | --- |
| Acesso | Público, qualquer pessoa | Restrito a pessoas autorizadas |
| Controle | Descentralizado | Centralizado na organização |
| Segurança | Menor controle, mais exposta | Alta: autenticação, firewalls e permissões |

É possível acessar a intranet de fora por **VPN** ou autenticação remota, mas ainda assim é preciso se identificar (usuário e senha autorizados). Também a **propriedade** difere: a intranet pertence a uma organização; a Internet não é de uma só entidade, e sim um conglomerado de redes mantidas por provedores, governos, empresas e instituições acadêmicas.

#### Relação com a Internet

Para existir, a intranet **dispensa a Internet**: pode ficar totalmente isolada, apenas entre os computadores da rede local. É comum, porém, que esteja ligada à Internet, sobretudo com trabalho em locais diferentes, e essa ligação deve ser protegida. Em consequência, serviços da intranet podem, sim, ser alcançados por quem está fora da rede, desde que autenticados. Já a Internet e a intranet não têm relação **obrigatória** entre si. Por estar mais próxima dos recursos e usada por um grupo menor, a intranet costuma ter velocidade maior e menos congestionamento, mas isso é tendência, não regra.

#### Usos e vantagens

- compartilhar manuais, modelos e formulários, aumentando o tempo produtivo;
- reduzir distâncias com reuniões virtuais, acesso remoto, listas de discussão e colaboração em documentos;
- transferir conhecimento pela reutilização de documentos que deram certo;
- dar a gestores acesso rápido a relatórios para decidir no tempo certo;
- proteger contra acesso não autorizado com **firewall**, hardware e/ou software que reforça a segurança entre a rede interna e as externas.

Exemplos do cotidiano: o RH divulga vagas internas, um analista abre chamado técnico para a TI, um gestor publica relatório mensal. Frequentemente há registro do que foi acessado ou modificado, e a gestão dos dados é interna, com acesso hierarquizado e controle de versões.

#### Questões típicas

As bancas costumam perguntar qual solução uma empresa deve montar para que seus colaboradores usem recursos distribuídos sem que estranhos tenham o mesmo privilégio: a resposta é a **intranet**, e não Ethernet (tecnologia de LAN), WAN (rede de grande área), VLAN (sub-rede lógica que agrupa dispositivos) ou WLAN (LAN sem fio). Outra forma comum descreve um "conglomerado de redes locais interconectadas pelo mundo", que é a Internet, e não a LAN, a intranet ou a extranet. Dizer que a intranet pode ser ligada à Internet está correto, assim como afirmar que seus serviços podem ser alcançados por quem não está fisicamente na rede, desde que autorizado.

### Para fixar

- Internet é rede pública e global, rede de redes, classificada como WAN, sustentada por backbones e acessada por um provedor.
- Pública quer dizer aberta a qualquer um, não gratuita.
- TCP/IP é a principal família de protocolos da Internet e das intranets.
- Intranet é rede privada e restrita que usa as mesmas tecnologias da Internet; afirmar que usa protocolos diferentes é erro.
- A diferença entre Internet e intranet é o acesso (e a propriedade), não a tecnologia.
- A intranet pode existir sem conexão com a Internet, mas pode ser ligada a ela e acessada de fora por VPN com autenticação.
- A extranet estende a rede interna a usuários externos autorizados, como parceiros e fornecedores.
- Firewall reforça a segurança entre a rede interna e a Internet.

