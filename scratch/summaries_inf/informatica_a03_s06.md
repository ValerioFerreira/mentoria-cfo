##### informatica/a03/s06
Este trecho reúne os golpes baseados em engenharia social: phishing scam, smishing, pharming, vishing, baiting e whaling. Para cada um, interessa saber o canal usado, o mecanismo do golpe, o que o diferencia dos demais e como se prevenir.

### Visão geral

| Golpe | Canal ou alvo | Ideia central |
| --- | --- | --- |
| Phishing | E-mail e mensagens eletrônicas | Isca em massa que imita instituição conhecida para obter dados |
| Smishing | SMS (celular) | Phishing por mensagem de texto |
| Pharming | DNS | Redireciona o usuário a site falso, mesmo digitando o endereço certo |
| Vishing | Telefone (voz) | Golpista por ligação, muitas vezes com número falsificado |
| Baiting | Pendrive ou links tentadores | Isca que aproveita a curiosidade ou a ganância |
| Whaling | Executivos e altos cargos | Phishing sob medida contra a "baleia" da empresa |

Observação: engenharia social explora o comportamento humano (confiança, urgência, curiosidade), não uma falha técnica. Man-in-the-Middle, DDoS e força bruta são ataques técnicos, e não engenharia social.

### Phishing scam

Fraude em que o golpista tenta enganar o usuário para obter dados pessoais e financeiros, combinando **técnicas computacionais com engenharia social**. Ocorre por mensagens eletrônicas que:

- fingem ser comunicação oficial de banco, empresa ou site conhecido, ou despertam curiosidade, caridade ou promessa de vantagem;
- ameaçam com consequências (inclusão em cadastro de inadimplentes, cancelamento de conta, cartão ou cadastro) se o procedimento não for feito;
- induzem a fornecer dados em páginas falsas, a instalar malware ou a responder formulários.

Variações de abordagem: páginas falsas de comércio eletrônico ou internet banking; páginas falsas de redes sociais e companhias aéreas (capturam login e senha); mensagens com formulário embutido; links que baixam código malicioso; falso pedido de recadastramento por suposto suporte da empresa ou escola.

#### Como se prevenir

- Desconfie de instituições com as quais você não tem relação que pedem dados, atualização ou clique em link. Sem conta no banco, não há por que recadastrar nada.
- Desconfie de mensagens com pressão e ameaça. Não confie só no remetente: a conta pode ter sido invadida ou o e-mail forjado.
- Digite o endereço no navegador em vez de clicar; passe o mouse sobre o link para ver o destino real, pois golpistas disfarçam o endereço.
- Use antimalware, firewall pessoal e filtros antiphishing.
- Confira se a página usa **conexão segura** (HTTPS) e se o **certificado** corresponde ao site verdadeiro: uma página falsa pode ter conexão segura, mas com certificado e endereço diferentes.
- Consulte o site oficial da instituição, que costuma publicar alertas sobre e-mails falsos. Sinais de fraude: erro de português no título e remetente com domínio estranho.

> ⚠️ Pegadinha: phishing não é malware nem vírus. É uma **técnica de fraude**. Worm, keylogger, ransomware e backdoor são códigos maliciosos, não golpes de engano por mensagem.

### Smishing

Junção de **SMS + phishing**: o golpe chega por mensagem de texto no celular, para roubar dados ou instalar malware. O SMS imita banco, operadora, loja ou órgão público, com tom alarmante ou tentador ("conta bloqueada", "cobrança pendente", "você ganhou um prêmio") e traz um **link clicável** ou **número para ligar**. O link leva a site falso que pede CPF, cartão, senhas ou códigos, ou dispara o download de malware; em outros casos a vítima é induzida a responder o SMS com dados. Funciona pela falsa urgência e pela sensação de que o celular é um ambiente seguro.

Prevenção: não clicar em links suspeitos de SMS, não informar dados por mensagem, acessar sites digitando o endereço, desconfiar de urgência e prêmios, ativar filtro de spam e confirmar pelos canais oficiais.

> ⚠️ Pegadinha: smishing não é um vírus específico para Android ou iOS; é um **método de engenharia social** que pode levar à instalação de malware.

### Pharming

Tipo de phishing que **redireciona a navegação** para site falso por alteração no **DNS** (sistema que converte nomes de domínio em endereços IP). O usuário digita o endereço correto e é levado ao falso sem perceber (por exemplo, o .com.br vira outro domínio parecido). O método mais comum é o **envenenamento de cache de DNS**, que corrompe a tabela de associações entre nomes e IPs.

Há uma variante chamada **DNS spoofing (DNS poisoning)**, que envenena o próprio servidor DNS do provedor e atinge muitos usuários em larga escala.

Formas de redirecionamento:

- comprometimento do servidor DNS do provedor;
- código malicioso que altera o comportamento do DNS do computador;
- invasor com acesso às configurações de DNS do computador ou do modem de banda larga.

Prevenção: desconfiar de redirecionamentos inesperados ou de abertura/instalação de programas, desconfiar de sites de compras e bancos sem conexão segura e conferir se o certificado é do site verdadeiro.

> 💡 Pharming é o golpe que **corrompe o DNS e leva o endereço de um site a servidor diferente do original**. Em questão sobre a base técnica do pharming, a resposta é envenenamento de cache DNS (e não DDoS, troca de cabeçalhos IP ou de portas TCP).

### Vishing

Junção de **voice + phishing**: golpe por **telefone**. O criminoso se passa por funcionário de banco, suporte técnico, operadora ou agente de segurança, usa tom de urgência (movimentação estranha, compra suspeita) e pede senhas, códigos recebidos por SMS ou até transferências para "verificação". Pode usar **spoofing** para falsificar o número e parecer instituição oficial, e muitas vezes já conhece nome, CPF ou banco da vítima, o que reforça a credibilidade.

Prevenção: nunca informar senhas, códigos ou dados bancários por telefone; desconfiar de pedidos urgentes (inclusive em nome de parentes); desligar e ligar de volta para o número oficial do site ou do cartão; divulgar o alerta a outras pessoas.

### Baiting

Do inglês **bait (isca)**: o atacante deixa uma armadilha e espera que a vítima aja por conta própria, explorando **curiosidade, distração e ganância**, sem depender de falha técnica.

- **Físico**: pendrive abandonado em recepção, elevador ou estacionamento, com etiqueta atraente ("folha de pagamento", "confidencial"); ao ser conectado, instala malware automaticamente.
- **Virtual**: links "bons demais" (músicas, filmes, cursos ou programas grátis) que levam a site falso que instala vírus ou pede senhas e dados bancários.

Prevenção: desconfiar de brindes e promessas, nunca conectar dispositivo desconhecido, desativar a execução automática de mídias removíveis e manter antivírus e sistema atualizados.

### Whaling

De **whale (baleia)**: phishing **direcionado e personalizado** contra diretores, executivos e gestores de alto escalão, que têm poder de decisão e acesso a informações valiosas. Os criminosos pesquisam cargo, rotina, contatos e até o jeito de escrever da vítima, e montam mensagem que parece vir de fornecedor, parceiro ou outro executivo. Exemplo típico, chamado de **fraude do CEO**: e-mail falso do presidente exigindo transferência urgente ou documentos sigilosos. Explora hierarquia e urgência, e um único sucesso pode causar grande perda financeira e de reputação.

Prevenção: autenticação multifator (MFA) para acessos sensíveis e aprovação de transações, treinamento de conscientização (principalmente de líderes), confirmação de pedidos fora do padrão por outro canal (ligação ou vídeo) e cultura de segurança em toda a empresa.

> ⚠️ Pegadinha: phishing é em massa e genérico; whaling é uma forma de **spear phishing** (alvo específico) dirigida a pessoas de alto escalão.

### Para fixar

- Phishing: fraude de engano por mensagem eletrônica, que combina técnica e engenharia social; confira link, HTTPS e certificado.
- Smishing = SMS + phishing; não é vírus, é método de golpe, com link ou telefone para retorno.
- Pharming corrompe o DNS (envenenamento de cache) e redireciona o usuário a site falso mesmo com o endereço certo.
- Vishing = voz + phishing, por telefone, com possível falsificação de número (spoofing).
- Baiting usa isca (pendrive deixado, download grátis) e explora curiosidade e ganância.
- Whaling mira executivos (fraude do CEO) e é a versão mais direcionada do phishing.
- Man-in-the-Middle, DDoS e força bruta são ataques técnicos, não engenharia social.

