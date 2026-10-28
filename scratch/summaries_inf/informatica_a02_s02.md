##### informatica/a02/s02
Este trecho detalha os princípios da segurança da informação: a tríade clássica CID (confidencialidade, integridade e disponibilidade), os princípios adicionais (autenticidade e irretratabilidade), o modelo ampliado de Parker, a rastreabilidade e a relação entre cada tipo de ataque e o princípio violado.

### Confidencialidade

É a capacidade de proteger a informação contra acesso não autorizado: só vê quem tem permissão, seja pessoa, sistema, dispositivo ou processo. Analogia: uma carta em envelope lacrado; se o carteiro rompe o lacre e lê, a confidencialidade foi violada.

- Vale em **todo o ciclo de vida**: na criação, na transmissão (rede), no armazenamento e no descarte. Apagar também deve ser seguro, para que ninguém recupere o dado depois.
- A **criptografia** é o mecanismo típico que assegura confidencialidade (e não, por si só, autenticidade, irretratabilidade ou disponibilidade).

> ⚠️ Pegadinha: confidencialidade não é **confiabilidade**. Confiabilidade é a resistência do sistema a falhas e seu funcionamento correto ao longo do tempo, e não é um dos requisitos clássicos.

### Integridade

É garantir que a informação está correta, fidedigna e **não foi alterada sem autorização**, da origem ao destino, mantendo as características originais definidas pelo proprietário. Cobre a exatidão e a completeza. Indica que os dados guardados correspondem às inserções, alterações e processamentos autorizados, e que o que o emissor enviou é o que o destinatário recebeu, sem alteração, gravação ou exclusão, acidental ou proposital.

Na analogia da carta: ela chegou lacrada, original e sem manipulação. É por isso que o comércio eletrônico orienta recusar produtos com embalagem violada.

**Confidencialidade e integridade são independentes**: quebrar uma não implica quebrar a outra. Se o carteiro olha a carta contra a luz e a entrega intacta, violou a confidencialidade, mas manteve a integridade.

### Disponibilidade

É assegurar que quem tem permissão consiga **acessar e usar a informação no momento em que precisar**. Não basta existir; precisa estar acessível na hora certa (dados num servidor fora do ar não servem).

- Exemplo clássico: um ataque que derruba o acesso ao internet banking (negação de serviço, DoS) afeta a disponibilidade.
- Meios de garantia: backups atualizados, redundância de servidores, fontes de energia ininterrupta (nobreak), firewalls e proteção contra ataques, monitoramento constante.

> ⚠️ Pegadinha: confidencialidade garante acesso **somente** a autorizados; disponibilidade garante acesso aos autorizados **sempre que necessário** (dois requisitos).

### Princípios adicionais

A tríade **CID** é a base de qualquer estratégia de proteção, mas alguns autores incluem **autenticidade** e **irretratabilidade (não repúdio)**, valorizados em assinaturas digitais, certificados e transações online. Donn B. Parker propôs o **Hexagrama Parkeriano**, com seis atributos: os quatro anteriores (confidencialidade, integridade, disponibilidade, autenticidade) mais:

| Atributo | Significado | Exemplo |
| --- | --- | --- |
| Posse ou controle | Quem de fato detém a informação, seja qual for o seu criador | Celular roubado: o dado segue intacto, mas o dono perde o controle |
| Utilidade | A informação precisa ser útil a quem a usa | Dado correto e protegido, porém em formato ilegível, perde a utilidade |

#### Autenticidade

Garante que o emissor da mensagem é **quem alega ser**, ou seja, assegura a identidade de quem envia ou requisita acesso. A assinatura em papel, conferida pelo cartório, é uma forma frágil (pode ser imitada); as contas verificadas das redes sociais evitam que alguém se passe por figuras públicas. Senhas são técnica de verificação de autenticidade. Em segurança, o verbo "garantir" é usado assumindo que não houve incidente e que existe autenticação forte.

A autenticação se divide em dois tipos:

- **Autenticação de origem dos dados**: dispensa conexão (**sem conexão**) e confirma a origem dos dados recebidos.
- **Autenticação de entidade par**: exige conexão (**com conexão**) e assegura a identidade das entidades conectadas.

#### Irretratabilidade

Também chamada de **irrefutabilidade** ou **não repúdio**: o autor não pode negar depois que enviou a mensagem ou que participou do processo; nenhuma das partes pode negar o envio ou o recebimento de uma transação. A tecnologia (criptografia, assinatura digital) ajuda, mas o conceito é essencialmente **jurídico**: sempre é possível alegar celular roubado, estagiário ou erro do sistema, e a autenticação forte reduz muito essa defesa.

Autenticidade e irretratabilidade **são distintos**. Uma carta assinada prova a autoria (autenticidade), mas alguém pode ter alterado o texto mantendo a assinatura. Somando a integridade, a negação deixa de ser possível:

**AUTENTICIDADE + INTEGRIDADE = IRRETRATABILIDADE**

#### Rastreabilidade (auditoria)

Não é princípio clássico, mas é mecanismo importante: capacidade de registrar e reconstruir as ações sobre dados e recursos (quem fez o quê, quando, onde e como), por meio de **logs de auditoria** com acessos, alterações, exclusões, falhas e operações administrativas. Serve para investigação, conformidade legal, detecção de fraudes e análise de incidentes. Para os logs serem confiáveis:

- **Integridade** e **imutabilidade** (trilha append-only: só se acrescenta, nunca se altera ou remove), reforçadas por assinatura digital.
- **Sincronização de horário** (por exemplo, NTP confiável) para ordenar os eventos.
- **Armazenamento separado** das tabelas de negócio, com acesso restrito (inclusive em sistemas de auditoria ou SIEM), para que quem tem privilégio operacional não apague rastros.
- **Retenção segura**: arquivar sob controle em vez de simplesmente apagar logs antigos, preservando a cadeia de evidências.

### Ataques e o princípio violado

Partindo do fluxo normal (fonte envia, destinatário recebe), há quatro cenários de ataque:

| Ataque | O que acontece | Princípio violado |
| --- | --- | --- |
| Interrupção | A informação é cortada no caminho e não chega | Disponibilidade |
| Interceptação | A informação chega, mas um não autorizado leu o conteúdo | Confidencialidade |
| Modificação | Um terceiro recebe, altera e reenvia ao destinatário | Integridade |
| Fabricação | Um terceiro envia fingindo ser a fonte | Autenticidade |

### Para fixar

- CID: confidencialidade (só autorizados acessam), integridade (sem alteração não autorizada) e disponibilidade (acessível quando necessário).
- Criptografia protege a confidencialidade; confiabilidade não é o mesmo que confidencialidade.
- Confidencialidade e integridade são independentes: violar uma não viola necessariamente a outra.
- Autenticidade confirma quem é o emissor; irretratabilidade impede a negação de autoria; autenticidade + integridade = irretratabilidade.
- Hexagrama Parkeriano acrescenta posse ou controle e utilidade.
- Rastreabilidade usa logs imutáveis, com horário sincronizado, armazenados separadamente.
- Interrupção ataca a disponibilidade, interceptação a confidencialidade, modificação a integridade e fabricação a autenticidade.

