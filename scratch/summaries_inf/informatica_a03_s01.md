##### informatica/a03/s01
Este trecho define malware, mostra como ele infecta e como prevenir, reúne a terminologia do mundo hacker e detalha o vírus (partes, fases e o mito de que Linux e macOS são imunes).

### O que é malware e por que existe

Malware (*malicious software*, também chamado de software malicioso ou praga virtual) é qualquer programa ou código criado para invadir, estragar, espionar ou conseguir acesso indevido a sistemas, aparelhos ou redes. Pode se disfarçar de software legítimo ou agir em silêncio, comprometendo segurança, privacidade e desempenho. Uma vez instalado, acessa dados, espiona atividades e executa ações em nome do usuário, dentro das permissões que ele tem.

- **Motivos** mais comuns: ganhar dinheiro, roubar informações confidenciais (senhas, dados bancários), buscar notoriedade ou vandalismo.
- Também servem de ponte para outros crimes: golpes, ataques a outros sistemas e disseminação de spam.
- **Principais categorias**: vírus, worm, bot, trojan, spyware, backdoor e rootkit (e também ransomware).

### Infecção e prevenção

A principal porta de entrada hoje é a **Internet**. Formas comuns de infecção:

- Exploração de vulnerabilidades dos programas instalados ou autoexecução de mídias removíveis infectadas (pen drives).
- Acesso a páginas maliciosas com navegador vulnerável, ou ação direta de um atacante que, após invadir o computador, coloca arquivos maliciosos.
- Execução de arquivos já infectados, vindos de anexos de e-mail, mídias removíveis, páginas web, redes sociais ou outros computadores.

Procedimentos de segurança (base: cartilha do CERT.br):

- Manter programas na versão mais recente e com todas as atualizações aplicadas.
- Usar apenas software original (sem pirataria) e ter cuidado com aplicativos de terceiros.
- Usar mecanismos de proteção (antivírus, firewall) e as configurações de segurança disponíveis.
- Ter cuidado ao manipular arquivos, ao enviar o computador para manutenção e ao usá-lo em locais públicos.
- Proteger os dados com backup, manter data e hora corretas e criar um disco de recuperação do sistema.

> ⚠️ Pegadinha: achar que o computador não interessa a um atacante é erro. Muitos ataques buscam quantidade de máquinas, sem escolher a vítima.

### Terminologia

| Termo | Significado |
| --- | --- |
| Hacker | Usuário experiente, ótimo programador, que invade sistemas para provar habilidade, aprender, descobrir técnicas e mostrar vulnerabilidades, sem causar dano |
| Cracker | Invade para roubar informações, violar a integridade de sistemas e outras atividades maliciosas; também quem quebra proteções de software (pirataria) |
| Script kiddie (newbie) | Hacker iniciante que usa ferramentas prontas da internet para atacar |
| Insider | Ameaça interna: funcionário descontente, corrompido, subornado ou enganado |
| Phreaking | Especialista em telefonia: ligações gratuitas, clonagem e escutas em telefones fixos e celulares |
| Warez | Software pirata distribuído ilegalmente pela internet |
| Spam | E-mail não solicitado, enviado em massa, em geral com fim comercial |

Conceitos de risco: **vulnerabilidade** é a falha ou fragilidade; **ameaça** é o agente ou evento com potencial de explorá-la; **ataque** é a exploração efetiva; **risco** é a probabilidade de a ameaça se concretizar combinada ao impacto. Quebrar a proteção de uma versão de demonstração para usá-la sem limite é ação de cracker, não de hacker, worm ou trojan.

### Vírus

Vírus é um programa (ou trecho de código) que se espalha infectando arquivos e programas existentes. Anexa-se a um hospedeiro e, quando o arquivo hospedeiro é executado, ativa-se, replica-se e tenta contaminar outros programas. Dois pontos centrais:

- Precisa ter **autorreplicação** (faz cópias de si).
- **Não é autônomo**: depende de o usuário executar o arquivo infectado. Em um anexo de e-mail, basta abrir ou executar o arquivo contaminado, sem executar "o vírus" explicitamente.
- Faz duas tarefas: replicar-se (discreta ou agressivamente, inclusive por redes) e executar a carga maliciosa (de mensagem na tela até lentidão, reinício, apagamento de arquivos ou perda total de dados). Nem todo vírus é destrutivo.
- Surgiram na década de 1980, com efeitos simples.

**Três partes de um vírus:**

| Parte | Função |
| --- | --- |
| Mecanismo de infecção (vetor de infecção) | Como o vírus se propaga e se reproduz |
| Mecanismo de ativação (bomba lógica) | Condição ou evento que decide o momento em que a carga útil dispara |
| Carga útil | O que o vírus faz além de se espalhar (dano ou ação apenas notável) |

> ⚠️ Pegadinha clássica: é o mecanismo de **ativação**, e não o de infecção, que determina quando a carga útil dispara.

**Quatro fases de execução:**

1. **Dormência**: o vírus fica ocioso até ser ativado por algum evento (data, presença de outro arquivo, limite de disco). Nem todo vírus tem essa fase.
2. **Propagação**: instala cópias de si em outros programas ou áreas do disco; a cópia pode ser diferente da original (o vírus muda de forma para fugir da detecção).
3. **Ativação**: o vírus é acionado para cumprir sua função, também por eventos de sistema (inclusive o número de cópias feitas).
4. **Ação**: a função é executada, inofensiva (mensagem) ou danosa (destruir programas e dados).

### Vírus e sistemas operacionais

Vírus que infectam executáveis são escritos para um sistema operacional (às vezes para um hardware) específico, porque exploram suas falhas: um malware feito para Windows, em geral, não roda em Linux ou macOS. Mesmo assim **nenhum sistema é 100% imune**; é mito que Linux e macOS não pegam vírus. Há mais vírus para Windows porque ele roda na maioria dos computadores (maior alcance e impacto) e domina ambientes corporativos e domésticos; o Linux predomina em servidores, datacenters e sistemas embarcados. As falhas do Windows não se limitam ao kernel.

### Para fixar

- Malware é o termo geral para software malicioso; a principal porta de entrada é a Internet (anexos, pen drives, páginas, redes sociais).
- Prevenção: atualizar sistema e programas, software original, antivírus e firewall, backup, cuidado com arquivos e locais públicos.
- Hacker explora para aprender e mostrar falhas; cracker invade e quebra proteções para dano e pirataria; script kiddie usa ferramentas prontas; insider é ameaça interna.
- Phreaking é fraude em telefonia; warez é software pirata; spam é e-mail em massa não solicitado.
- Vulnerabilidade é a falha; ameaça é o agente com potencial; ataque é a exploração efetiva.
- Vírus se replica, mas depende de hospedeiro e da execução do arquivo infectado; composto de mecanismo de infecção, mecanismo de ativação (bomba lógica) e carga útil.
- Fases do vírus: dormência, propagação, ativação e ação; nenhum sistema operacional é imune a vírus.

