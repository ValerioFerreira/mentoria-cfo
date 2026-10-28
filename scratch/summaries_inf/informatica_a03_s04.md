##### informatica/a03/s04
Este trecho fecha a comparação entre os principais códigos maliciosos (vírus, worm, bot, trojan, spyware, backdoor e rootkit) e apresenta outros malwares cobrados em prova: ransomware, keylogger, screenlogger, adware, sniffer, bomba lógica, exploit e hijacker.

### Comparação entre os códigos maliciosos
A tabela comparativa clássica organiza cada praga por como é obtida (rede, e-mail, sites, compartilhamento de arquivos, mídias removíveis, redes sociais, mensagens instantâneas, inserida por invasor ou por outro código malicioso), como é instalada (execução de arquivo infectado, execução explícita, execução de outro código, exploração de vulnerabilidades), como se propaga e o que faz. Pontos que sustentam as questões:
- Só o **vírus** se propaga inserindo cópia de si em arquivos.
- **Worm** e **bot** enviam cópias de si automaticamente pela rede; o bot é o que envia spam e phishing.
- **Trojan, spyware, backdoor e rootkit não se propagam**.
- Rootkit e backdoor lidam com o retorno do invasor e com ocultação; o rootkit busca se manter escondido.

### Ransomware (incidência altíssima)
É o código malicioso que torna inacessíveis os dados do equipamento, em geral por criptografia, e exige um **resgate** (*ransom*) para devolver o acesso: uma extorsão virtual. Propaga-se, sobretudo, por anexos de e-mail ou links que induzem o usuário a clicar, e pela exploração de vulnerabilidades em sistemas sem atualização.
- **Locker**: impede o acesso ao equipamento infectado.
- **Crypto**: impede o acesso aos dados, por criptografia; tende a procurar também outros equipamentos ligados ao infectado, na rede ou localmente, para cifrá-los.

O pagamento costuma ser exigido em moeda digital (ex.: Bitcoin), para ser difícil de rastrear, e não garante a volta dos dados. Prevenção: sistema e programas atualizados, antivírus, cuidado com links e arquivos, e **backups regulares e atualizados**, a única garantia real de recuperar os dados.

> 💡 Exemplo: o WannaCry (maio de 2017) era um ransomware com comportamento de worm: explorou uma vulnerabilidade do Windows (EternalBlue), cifrou arquivos, pediu bitcoins e atingiu mais de 150 países. Houve também ataque de ransomware às bases do STJ.

### Keylogger (incidência média)
É um tipo de **spyware** que captura e armazena as teclas digitadas e as envia ao invasor, para obter senhas e dados de e-mail, redes sociais, mensageiros e bancos. Nasceu como ferramenta de suporte técnico e fiscalização, e vira malware quando é usado para coletar dados pessoais. Muitas vezes só é ativado depois de uma ação do usuário, como acessar um site de comércio eletrônico ou de internet banking. Os bancos reagiram com o **teclado virtual**, em que os caracteres são clicados com o mouse.

### Screenlogger (incidência média)
Também é um spyware, parecido com o keylogger: guarda a posição do cursor e a tela mostrada no momento do clique do mouse (ou a região em volta do clique). Foi criado principalmente para vencer o teclado virtual, pois a sequência de cliques e de imagens revela o que foi "digitado". Hoje é mais raro, porque teclados virtuais são menos usados e há outras formas de impedi-lo.

### Adware (incidência alta)
É um spyware projetado para exibir propagandas, normalmente por pop-ups e notificações dentro de outro programa, em geral o navegador. Pode ser legítimo, quando é a forma de patrocínio de programas ou serviços gratuitos. Torna-se malicioso quando direciona os anúncios conforme a navegação do usuário sem que ele saiba do monitoramento. Costuma ser instalado sem consentimento junto de outro software (atenção às telas de instalação), deixando o computador lento e a navegação incômoda. Não confundir: quem registra teclas é o keylogger, e quem mostra propaganda é o adware.

### Sniffer (incidência baixa)
É um analisador de pacotes capaz de monitorar, interceptar e registrar o tráfego de dados em segmentos de rede. Por padrão, cada computador só responde aos pacotes endereçados a ele; o sniffer "fareja" o que passa na rede.
- Uso legítimo (o mais comum): administradores detectam problemas, analisam desempenho e monitoram atividades maliciosas. Empresas podem usá-lo.
- Uso malicioso: o atacante captura senhas, números de cartão e conteúdo de arquivos que trafegam sem criptografia (nesse caso se diz que está em **modo promíscuo**). Informação criptografada só serve ao atacante se ele conseguir decodificá-la. Locais de wi-fi inseguro (cafeterias, hotéis, aeroportos) são típicos.
- Diferenças em relação ao spyware: o sniffer pode ser legítimo ou malicioso (o spyware é em regra malicioso) e pode ficar em **qualquer** computador da rede local, sem precisar estar na máquina monitorada, ao contrário do spyware.

### Bomba lógica (incidência baixa)
Software malicioso, normalmente instalado por usuário autorizado (como um administrador de rede), programado para causar dano quando ocorre um evento, por exemplo apagar arquivos críticos se determinado funcionário for demitido. O disparo pode ser **positivo** (fica inativa até um evento ocorrer) ou **negativo** (é ativada a não ser que um evento ocorra, como a senha diária que o programador deixa de digitar). Diferença para o vírus time bomb: a bomba lógica pode ser usada por outros tipos de malware, enquanto o time bomb é apenas um vírus. Não confunda com um ataque de negação de serviço (DoS), que sobrecarrega o sistema com requisições.

### Exploit (incidência baixíssima)
Software criado para explorar vulnerabilidades conhecidas de sistemas, permitindo invasões a atacantes sem conhecimento avançado; costuma causar instabilidade para reduzir temporariamente a segurança e então executar ordens (roubar informações, acessar áreas bloqueadas, propagar vírus). Pode explorar falhas **zero-day**: vulnerabilidade ainda desconhecida pelos administradores, cujo "dia zero" é o dia em que eles a descobrem e começam a mitigá-la.

### Hijacker (incidência média)
O *browser hijacker* ("sequestrador") modifica o registro do sistema e o funcionamento do navegador: troca a página inicial, abre páginas automaticamente, insere botões e redireciona páginas visitadas (também pode alterar a página de busca). Quem o cria costuma ser remunerado por cliques em páginas patrocinadas. Aparece em questões sobre software gratuito instalado junto com programas adicionais, pop-ups e página inicial alterada.

### Para fixar
- Só o vírus insere cópia em arquivos; worm e bot enviam cópias pela rede; trojan, spyware, backdoor e rootkit não se propagam.
- Ransomware: locker bloqueia o equipamento, crypto cifra os dados; pagamento não garante nada, backup sim.
- Keylogger registra teclas; screenlogger registra tela/cliques e visa teclados virtuais; ambos são spyware.
- Adware exibe propaganda e é malicioso quando monitora a navegação.
- Sniffer captura tráfego de rede (uso legítimo e malicioso), em qualquer máquina da rede; modo promíscuo no uso malicioso.
- Bomba lógica dispara por evento (positivo ou negativo) e serve a vários malwares; time bomb é só vírus.
- Exploit aproveita vulnerabilidade, inclusive zero-day; hijacker sequestra página inicial e busca do navegador.

