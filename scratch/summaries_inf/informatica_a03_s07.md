##### informatica/a03/s07
Este trecho trata de golpes e ataques de engenharia social e de aplicações: spear phishing, hoax, man in the middle, defacement, SQL injection, furto de identidade e fraude de antecipação de recursos.

### Spear phishing

Phishing comum envia mensagens genéricas a muita gente. O **spear phishing** é **direcionado e personalizado**: mira uma ou poucas vítimas específicas, com mensagens adaptadas à realidade delas, o que o torna muito mais convincente.

- O atacante pesquisa a vítima antes (redes sociais, sites corporativos, vazamentos) e imita colegas, parceiros ou sistemas da própria empresa.
- Objetivo: roubar credenciais, dados financeiros ou estratégicos, ou instalar malware (porta de entrada para ransomware e acesso persistente).
- Passa pelos filtros tradicionais, porque as mensagens não têm cara de spam em massa nem vírus conhecido.
- Defesa: conferir o remetente, desconfiar de urgência, não clicar em links desconhecidos, usar autenticação multifator e treinamentos regulares.
- Comparação: **whaling** é o ataque dirigido ao alto escalão (diretores e executivos); **smishing** usa SMS; **vishing** usa ligação telefônica.

### Hoax (boato)

Hoax é uma mensagem de conteúdo **alarmante ou falso**, em geral atribuída a instituição, empresa importante ou órgão do governo; correntes e pirâmides financeiras são exemplos. Lendo com atenção, costuma-se achar incoerências. Os danos possíveis:

- Conter código malicioso, espalhar desinformação ou apenas ocupar caixas de e-mail.
- Prejudicar a credibilidade de quem é citado na mensagem e de quem a repassa (parece endossar o conteúdo).
- Aumentar a carga dos servidores de e-mail e o consumo de banda.
- Pedir ações que, se feitas, causam danos sérios.

Espalha-se pela boa vontade e solidariedade de quem recebe e repassa sem checar. Prevenção: conferir a procedência, mesmo quando o remetente é conhecido.

> ⚠️ Pegadinha: hoax **não** é técnica para "pescar" senhas e dados financeiros (isso é phishing); é boato ou alerta falso, que alarma e induz a repassar a corrente.

### Man in the Middle (homem no meio)

Os dados trocados entre duas partes (você e seu banco) são **interceptados, registrados e possivelmente alterados** por um atacante, sem que as vítimas percebam. O atacante recebe a comunicação e a retransmite: pode repassá-la intacta, alterada ou bloquear partes. Cada lado acredita estar falando diretamente com o outro. Não confundir com DoS (derruba serviço por sobrecarga), pharming (redireciona via DNS) e spoofing (finge ser outro usuário ou sistema).

### Defacement (desfiguração ou pichação)

Alterar o **conteúdo de uma página web** (em geral a principal, para ganhar visibilidade; páginas internas também). O atacante é chamado *defacer*. Formas de realizar:

- Explorar vulnerabilidades da linguagem de programação ou dos pacotes usados na aplicação web.
- Invadir o servidor e alterar diretamente os arquivos do site.
- Explorar erros da aplicação ou vulnerabilidades do servidor de aplicação web.
- Furtar senhas da interface de administração remota.

### SQL Injection

Vulnerabilidade em que o invasor insere instruções SQL maliciosas em uma **entrada de dados** (campos de formulário ou parâmetros de URL) para manipular o banco de dados. Ocorre em sistemas que montam consultas SQL dinâmicas sem validar a entrada. Exemplo: digitar `OR 1=1` (sempre verdadeiro) em um campo faz a consulta devolver todos os registros. Consequência: acessar, modificar ou excluir dados, comprometendo integridade e segurança.

- Mitigação: **validação e sanitização das entradas** (a resposta clássica de prova), consultas parametrizadas ou preparadas, software atualizado, testes regulares e **princípio do menor privilégio** no acesso ao banco.
- Criptografia, autenticação e controle de acesso não impedem, por si, a injeção.

### Furto de identidade

Alguém se passa por outra pessoa, atribuindo-se falsa identidade para obter vantagens indevidas; alguns casos são crime de falsa identidade (contra a fé pública). Exemplos: abrir empresa ou conta bancária com seus documentos, criar perfil em seu nome, acessar seu e-mail e enviar mensagens em seu nome, falsificar o remetente. Quanto mais dados você expõe, mais fácil o furto; o golpista também usa códigos maliciosos, força bruta e interceptação de tráfego.

Indícios de que a identidade foi furtada: problemas com órgãos de proteção de crédito; retorno de e-mails que você não enviou; acessos à conta de e-mail ou rede social em horários ou locais estranhos; transações desconhecidas no extrato ou no cartão; ligações, cartas e e-mails sobre assuntos que você desconhece (conta bancária ou compra que não são suas). Prevenção: proteger dados e contas e ter cuidado ao usar e elaborar senhas.

### Fraude de antecipação de recursos (advance fee fraud)

O golpista induz a vítima a **fornecer dados confidenciais ou pagar adiantado**, prometendo um benefício futuro que não existe. Variações:

| Golpe | Como funciona |
| --- | --- |
| Golpe da Nigéria | Mensagem pede que a vítima atue como intermediária em uma transferência de fundos |
| Loteria internacional | Aviso de sorteio; para receber o prêmio, a vítima envia dados pessoais e bancários |
| Crédito fácil | Oferta de empréstimo com juros baixíssimos; exige depósito para cobrir despesas |
| Oferta de emprego | Proposta tentadora no celular; pede dados da conta bancária |
| Doação de animais | Animal caro "doado"; pede dinheiro para o transporte |
| Noiva russa | Contato afetivo pela rede social; pede ajuda financeira para viajar |

Sinais de alerta: valores astronômicos, pedido de sigilo e de resposta rápida, "urgente" e "confidencial" no assunto, erros de gramática e ortografia (tradução automática). Prevenção: perguntar por que você foi escolhido, desconfiar de pagamento antecipado, **não responder** (confirma que o endereço é válido) e lembrar que "quando a esmola é demais, o santo desconfia".

### Para fixar

- Spear phishing é direcionado e personalizado; whaling mira executivos; smishing é por SMS e vishing por telefone.
- Hoax é boato ou alerta falso que sobrecarrega a rede e prejudica reputações; não rouba senhas (isso é phishing).
- Man in the Middle intercepta, e pode alterar, a comunicação entre duas partes que não percebem.
- Defacement altera o conteúdo de páginas web, explorando falhas do servidor, da aplicação ou senhas de administração.
- SQL Injection insere comandos SQL em campos de entrada; a defesa principal é validar e sanitizar as entradas (e dar o menor privilégio).
- Furto de identidade: usar dados de outra pessoa para obter vantagem; indícios incluem transações e acessos desconhecidos.
- Fraude de antecipação de recursos: promessa de benefício em troca de pagamento ou dados prévios (golpe da Nigéria, loteria, noiva russa); não responder.

