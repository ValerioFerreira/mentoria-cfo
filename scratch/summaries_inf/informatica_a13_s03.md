##### informatica/a13/s03
Este trecho cobre o armazenamento em nuvem (vantagens e riscos), compara Google Drive, Dropbox, OneDrive e iCloud (cotas gratuitas, integração, recursos de segurança) e apresenta o Microsoft Azure como plataforma de nuvem.

### Armazenamento em nuvem

Guardar arquivos fora do dispositivo, em servidores na internet operados por provedores especializados (Google Drive, Dropbox, OneDrive, iCloud). Controla-se o acesso por usuário e senha, e o serviço pode ser gratuito.

- **Acessibilidade**: o arquivo não fica preso a um computador; dá para começar no trabalho, seguir no celular e terminar no notebook, sem pendrive ou envio por e-mail, e colaborar em tempo real.
- **Escalabilidade**: planos gratuitos com alguns GB e planos pagos maiores (inclusive para empresas), sem comprar discos novos.
- **Segurança**: cópias em vários servidores do mundo (**redundância**, protege contra falha de um datacenter), criptografia, autenticação em duas etapas e controle de acesso.
- **Desvantagens**: depende de internet estável; preocupação com privacidade e conformidade com leis de proteção de dados (**LGPD** no Brasil, GDPR na Europa); convém checar se o provedor cumpre essas normas.
- Uso pessoal (iCloud, por exemplo) ou corporativo, com ofertas como **Amazon S3**, **Azure Blob Storage** e **Google Cloud Storage**, integradas a backup, recuperação de desastres, análise de dados e IA.

### Google Drive

- Lançado em 2012 pelo Google; integra-se a Gmail, Google Docs, Google Fotos e Android. Acesso por navegador e por aplicativos (Windows, macOS, Android e iOS), inclusive em tablets.
- **15 GB gratuitos, compartilhados entre Drive, Gmail e Google Fotos**. Mais espaço pelo **Google One** (a partir de 100 GB); empresas usam o **Google Workspace** (painel de administração e, conforme o plano, armazenamento ilimitado).
- Compartilhamento com permissão de visualizar, comentar ou editar; coedição em tempo real; histórico de versões; recuperação de arquivos excluídos; criação e edição de Documentos, Planilhas, Apresentações e Formulários direto no navegador.
- Segurança: criptografia em trânsito e armazenado, autenticação em dois fatores e controles de acesso detalhados.

### Dropbox

- Lançado em 2007; marcado pela **sincronização simples e eficiente**: o arquivo salvo na pasta do Dropbox aparece em todos os dispositivos conectados à mesma conta.
- **2 GB gratuitos**; planos Plus e Family; **Dropbox Business** para equipes (integração com Zoom, Slack e Office).
- **Dropbox Paper**: documentos colaborativos com texto, imagens, listas e multimídia. Links com senha, prazo de validade e permissões ajustáveis. Criptografia em trânsito e armazenado, autenticação em dois fatores e histórico de versões (recupera arquivos excluídos).

### OneDrive

- Antigo SkyDrive; é o serviço da **Microsoft**, integrado ao Windows e ao Microsoft 365 (antigo Office 365). Vem **pré-instalado** nas versões recentes do Windows (aparece como pasta comum, que sincroniza automaticamente) e acessa-se por computador, celular, tablet ou navegador.
- **5 GB gratuitos**; com assinatura Microsoft 365 o espaço sobe (o texto cita 1 TB); **OneDrive for Business** para empresas.
- Recursos: **Cofre Pessoal** (área protegida com verificação extra), criptografia em trânsito e armazenado, autenticação em dois fatores, recuperação de versões e arquivos, compartilhamento com permissões e edição simultânea de Word, Excel e PowerPoint online.

### iCloud

- Serviço da **Apple**, desde 2011; integra iPhone, iPad, Mac e Apple Watch (fotos, arquivos, contatos, calendários e notas sincronizados; arquivos do Pages, Numbers e Keynote salvos na nuvem). Acesso por navegador (iCloud.com) e versão para Windows.
- **5 GB gratuitos** (não é espaço ilimitado); planos **iCloud+** de 50 GB, 200 GB ou 2 TB, compartilháveis com a família, com ocultação de e-mail, Private Relay e suporte a vídeo seguro de câmeras residenciais.
- Criptografia de ponta a ponta em vários serviços (Keychain de senhas, Fotos, Mensagens e backups, principalmente com a proteção avançada de dados).

| Serviço | Dona | Espaço grátis | Ligações nativas | Pagos a partir de | Indicado para |
| --- | --- | --- | --- | --- | --- |
| Drive | Google | 15 GB, divididos com Gmail e Fotos | Docs, Gmail, Android | 100 GB (Google One) | Quem vive no mundo Google; coedição |
| Dropbox | Dropbox, Inc. | 2 GB | Paper e Office | 2 TB | Sincronização e envio simples |
| OneDrive | Microsoft | 5 GB | Windows e Microsoft 365 | 100 GB (Microsoft 365) | Usuários de Windows e Office |
| iCloud | Apple | 5 GB | iOS, macOS, iPadOS | 50 GB (iCloud+) | Usuários de aparelhos Apple |

Colaboração em tempo real: completa nos apps do Google, por arquivos compartilhados e comentários no Dropbox, com Word, Excel e PowerPoint online no OneDrive e limitada aos apps da Apple (Pages, Numbers) no iCloud.

> ⚠️ Pegadinha: o Google Drive funciona em tablets; o iCloud não é gratuito sem limite de espaço; o OneDrive é o serviço de nuvem que já vem no Windows; VirtualBox, Wamp, VLC e VNC não são serviços de nuvem.

### Microsoft Azure

- Plataforma de computação em nuvem da Microsoft (lançada em 2010), uma das gigantes ao lado de **AWS** e **Google Cloud**. Oferece armazenar dados, rodar **máquinas virtuais** (Windows Server ou Linux, como CentOS, Suse e Ubuntu), bancos de dados, IA, redes e mais.
- Integra-se ao ecossistema Microsoft (Windows Server, Active Directory, SQL Server, Microsoft 365) e é aberta a Linux, Java, Python, PHP e .NET.
- **Cobrança por uso**; pode ser nuvem pública, privada ou híbrida. Serviços comuns: VMs, Blob Storage (objetos), Azure SQL Database, Azure DevOps e Kubernetes Service. Entrega serviços de IaaS e PaaS.
- Segurança e conformidade: criptografia, autenticação multifator, identidades pelo Azure Active Directory, normas ISO, GDPR e LGPD; soluções de backup e recuperação de desastres. Em dados e IA, Synapse Analytics e Power BI.

### Para fixar

- Armazenamento em nuvem: acesso de qualquer dispositivo, coedição, redundância e escalabilidade; depende de internet e exige atenção à LGPD.
- Google Drive (2012): 15 GB compartilhados com Gmail e Fotos; planos via Google One; Workspace para empresas.
- Dropbox (2007): 2 GB gratuitos, sincronização rápida e Paper; links com senha e validade.
- OneDrive: da Microsoft, pré-instalado no Windows, 5 GB gratuitos, Cofre Pessoal e coedição com Office online.
- iCloud (2011): ecossistema Apple, 5 GB gratuitos (não é ilimitado), planos iCloud+ de 50 GB a 2 TB.
- Todos usam criptografia e autenticação em dois fatores.
- Azure (2010), AWS e Google Cloud são plataformas empresariais (IaaS e PaaS), com cobrança por uso.

