##### informatica/a03/s05
Este trecho trata de ataques e golpes clássicos da segurança da informação: engenharia social, força bruta, negação de serviço (DoS e DDoS), IP spoofing e e-mail spoofing, além de termos vizinhos que aparecem como alternativas nas questões.

### Engenharia social

Técnica pela qual uma pessoa **persuade outra, por má-fé, a executar ações** ou revelar informações sigilosas, explorando **confiança, ingenuidade, ganância, vaidade ou boa-fé**. Ataca o fator humano e não o computacional (o hacker Kevin Mitnick resumia: a melhor técnica para descobrir uma senha é perguntar). Costuma usar telefone, e-mail ou salas de bate-papo; o **phishing** é exemplo comum.

- Exemplo clássico: um falso "suporte técnico do provedor" liga, diz que há lentidão na conexão, confirma dados e pede a senha; outro: alguém se passa por esposa de um diretor e pede troca de login e senha à secretária.
- Defesa: duvidar de abordagens desse tipo, **confirmar a identidade de quem pede dados** (ligando para o número oficial) e nunca revelar senhas ou números de cartão por telefone.
- Outros termos que aparecem como alternativas erradas: dumpster diving (vasculhar o lixo), varredura de vulnerabilidades (scan) e ataque físico (roubo de equipamentos).

### Força bruta (brute force)

Adivinhar, por **tentativa e erro**, nome de usuário e senha para executar processos e acessar sites, computadores e serviços **com os mesmos privilégios** do usuário. Qualquer equipamento ou serviço acessível pela Internet com usuário e senha pode ser alvo. Em geral usa ferramentas automáticas; as tentativas se baseiam em:

- dicionários de vários idiomas e listas de palavras comuns (personagens, times);
- substituições óbvias de caracteres (a por @, o por 0);
- sequências numéricas e de teclado ("123456", "qwert", "1qaz2wsx");
- informações pessoais (nomes, datas, números de documentos).

Mesmo sem descobrir a senha, a vítima pode ficar sem acesso, pois muitos sistemas **bloqueiam a conta** após várias tentativas falhas. Dependendo de como é feito, o ataque pode virar **negação de serviço**, pela sobrecarga de tentativas. Defesa: senhas longas e complexas, bloqueio de tentativas, CAPTCHA e autenticação multifator.

### Negação de serviço (DoS) e DDoS

- **DoS** (*Denial of Service*): técnica para **retirar de operação** um serviço, computador ou rede conectada à Internet. O objetivo **não é invadir nem coletar informações**, e sim **exaurir recursos e causar indisponibilidade** (atinge a disponibilidade). Terminado o ataque, o alvo volta ao normal, sem vazamento nem comprometimento do sistema.
- **DDoS** (*Distributed*): o ataque é coordenado e **distribuído**, usando um conjunto de equipamentos; costuma empregar computadores infectados (por exemplo, por worms) que formam **botnets** (zumbis) sem o dono saber.
- Formas: enviar enorme quantidade de requisições a um serviço (consumindo processamento, conexões simultâneas, memória, disco); gerar grande tráfego para ocupar toda a banda de uma rede; explorar vulnerabilidades em programas para deixar um serviço inacessível.
- Variantes citadas: **SYN flooding** (muitos pedidos TCP incompletos) e Ping of Death (pacotes ICMP malformados).

### Spoofing (falsificação)

- **IP spoofing**: técnica de invasão comum quando a autenticação de uma rede se baseia em **endereços IP**. O atacante **forja o endereço IP de origem** dos pacotes e se passa por usuário autorizado, ganhando acesso indevido ou escondendo a própria identidade.
- **E-mail spoofing**: **alterar campos do cabeçalho do e-mail** (como o remetente) para parecer enviado de outra origem. É possível por características do protocolo **SMTP**, que permitem falsificar o cabeçalho. Usado para propagar códigos maliciosos, enviar spam e aplicar golpes de phishing (e-mail "de um conhecido", "do banco" ou "do administrador do serviço").
- Indícios de que seu endereço foi usado: respostas a e-mails que você não enviou, e-mails aparentemente enviados por você mesmo e mensagens de devolução de e-mails que você nunca mandou (usuário desconhecido, caixa lotada).
- Existem ainda ARP spoofing, MAC spoofing e DNS spoofing (resposta DNS falsa que redireciona o tráfego).

### Termos que confundem

| Termo | O que é |
| --- | --- |
| Sniffing | Interceptação e captura de dados em trânsito na rede (não é força bruta nem spoofing) |
| Defacement | Alteração visual de páginas de sites |
| Spam | E-mail não solicitado, em massa |
| Honeypot | Técnica **defensiva** que simula sistema vulnerável para atrair e monitorar atacantes |

> ⚠️ Pegadinha: DoS não rouba nem altera dados; força bruta não é interceptação de tráfego; e-mail spoofing não é spam (spam é o e-mail em massa; spoofing é a falsificação do remetente).

### Para fixar

- Engenharia social: persuasão que explora confiança e ingenuidade; defesa é confirmar a identidade de quem pede dados.
- Força bruta: tentativa e erro de usuário e senha (dicionários, sequências, dados pessoais); gera bloqueio de conta e pode virar DoS.
- DoS tira um serviço do ar por sobrecarga, sem invadir nem roubar dados; atinge a disponibilidade.
- DDoS é DoS coordenado e distribuído, em geral por botnets de computadores zumbis.
- IP spoofing forja o IP de origem dos pacotes; usa-se quando a autenticação se baseia em IP.
- E-mail spoofing altera o cabeçalho (remetente) do e-mail, possível pelas características do SMTP.
- Sniffing intercepta tráfego; defacement altera páginas; honeypot é defesa, não ataque.

