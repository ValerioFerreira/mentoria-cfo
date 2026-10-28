##### informatica/a12/s10
Este trecho percorre categorias do aplicativo Configurações do Windows 11: Opções de entrada (Windows Hello), Backup do Windows, Hora e idioma, Jogos, Acessibilidade (com a Lupa), Privacidade e segurança e Windows Update.

### Opções de entrada (contas)

Concentra os métodos de login. As "maneiras de entrar" são:

| Método | Como funciona |
| --- | --- |
| Reconhecimento facial (Windows Hello) | Câmera compatível com infravermelho |
| Impressão digital (Windows Hello) | Leitor biométrico |
| **PIN** (Windows Hello) | Número secreto salvo apenas no aparelho, o que o torna mais seguro que uma senha trafegada pela rede |
| **Chave de segurança** | Chave física (USB ou NFC) baseada em padrões como FIDO2 |

O **Windows Hello** funciona como acesso **sem senha**, mais rápido e seguro. Características cobradas:

- **Segurança reforçada**: biometria é única de cada pessoa e mais difícil de roubar ou copiar que uma senha.
- **Privacidade**: os dados biométricos ficam **armazenados localmente** no aparelho; não são enviados à Microsoft nem guardados na nuvem.
- **Compatibilidade**: exige o hardware (câmera infravermelha ou leitor de digitais).
- Serve também para autenticar em aplicativos e serviços compatíveis, e a configuração é feita em "Opções de entrada".

Configurações adicionais: permitir **apenas** entrada pelo Windows Hello em contas Microsoft (reduz o login por senha tradicional), definir quando o Windows pede nova autenticação (por exemplo, ao sair da suspensão), **Bloqueio dinâmico** (pareia o PC com um celular por Bluetooth e bloqueia automaticamente quando o usuário se afasta), salvar e reabrir automaticamente os aplicativos após reiniciar e exibir ou ocultar dados da conta (nome e e-mail) na tela de entrada.

> ⚠️ Pegadinha: Windows Hello não é a Cortana (assistente digital), nem o Microsoft Defender (antivírus), nem o Edge (navegador). É o recurso de login por rosto, digital ou PIN.

### Backup do Windows

Cria cópias de segurança automáticas ligadas à **conta Microsoft**, para restaurar configurações, arquivos e preferências ao trocar de computador ou reinstalar o sistema. Opções:

- **Lembrar meus aplicativos**: registra os apps instalados (da Microsoft Store e informações de apps de desktop) para reinstalá-los em outro PC da mesma conta.
- **Lembrar minhas preferências**: guarda o idioma, as senhas das redes Wi-Fi e os ajustes regionais (data, teclado).
- **Sincronizar pastas com o OneDrive**: Documentos, Imagens e Área de Trabalho ficam na nuvem e podem ser restaurados em caso de perda.
- **Backup de senhas e contas**: guarda credenciais (Wi-Fi e senhas salvas no Edge) na nuvem.

Em questões sobre o backup nativo do Windows, vale a ideia do **Histórico de Arquivos**: permite recuperar **versões anteriores** de arquivos individuais e salvar em unidades externas ou locais de rede (não apenas em um deles).

### Hora e idioma

| Item | Função |
| --- | --- |
| Data e hora | Ajuste manual ou automático, fuso horário, sincronização com servidores de horário e horário de verão |
| Idioma e região | Idioma de exibição, idiomas preferenciais, idioma do sistema, formatos regionais (moeda, data, hora) |
| **Digitação** | Teclado virtual, sugestões de texto, correção automática e idioma do teclado |
| Fala | Idioma de fala, reconhecimento de voz, microfone e voz do sistema |

> ⚠️ Pegadinha: se o teclado está configurado para outra língua e dificulta acentos e cedilha, a configuração está em **Hora e idioma** (não em Sistema, Aplicativos ou Dispositivos).

### Jogos (atalho Win + G)

- **Xbox Game Bar**: sobreposição de jogos para atalhos, widgets de desempenho e áudio, gravação de clipes, capturas de tela e conversa com amigos.
- **Capturas**: onde e como os vídeos e capturas são salvos (qualidade, duração máxima, pasta).
- **Modo de Jogo**: reduz a atividade em segundo plano e prioriza recursos para o jogo, ganhando estabilidade e taxa de quadros.

### Acessibilidade (atalho Win + U)

| Recurso | Para que serve |
| --- | --- |
| Tamanho do texto | Aumenta o texto sem mexer nos outros elementos |
| Efeitos visuais | Transparência, rolagem suave e animações |
| Ponteiro do mouse e toque | Cor, tamanho e espessura do ponteiro |
| Cursor de texto | Espessura e estilo do cursor de digitação |
| **Lupa** | Amplia a tela (baixa visão) |
| **Filtros de cor** | Auxiliam daltonismo (inversão, escala de cinza) |
| **Temas de contraste** | Alto contraste entre texto e fundo |
| **Narrador** | Leitura de tela com voz sintetizada, essencial para cegos |
| Áudio | Som mono, balanceamento de canais e alertas visuais |
| Dispositivos auditivos | Aparelhos auditivos e roteamento de áudio |
| Legendas | Estilo de legendas (fonte, cor, tamanho, fundo) |
| Fala | Comandos e digitação por voz |
| Teclado | Teclas de aderência, filtragem e alternância; teclado virtual |
| Mouse | Velocidade, aceleração e teclas do mouse |
| Controle com os olhos | Rastreamento ocular para mover o cursor |

#### Lupa

Amplia partes da tela (ou toda ela) de forma dinâmica, ajuda quem tem baixa visão e também quem quer ler textos pequenos em telas de alta resolução. Atalhos: **Win + +** liga (tecla Windows e sinal de mais) e **Win + Esc** desliga. Permite ajustar o nível de ampliação, inverter cores e ler em voz alta junto com o Narrador. Amplia texto, imagens, ícones e qualquer elemento, e não apenas texto digitado em editor. No menu Iniciar, fica na pasta **Facilidade de Acesso** (o nome do app é Lupa, e não "Ampliador").

### Privacidade e segurança

| Item | Função |
| --- | --- |
| **Segurança do Windows** | Antivírus, firewall, proteção contra ameaças, controle de aplicativos; mostra o estado da segurança |
| **Localizar meu dispositivo** | Rastreia o aparelho em caso de perda ou roubo; envia a localização à conta Microsoft (exige internet e localização) |
| Geral | ID de publicidade, conteúdo local e sugestões personalizadas |
| Controle por voz / fala | Reconhecimento de fala, ditado e comandos |
| Escrita à tinta e digitação | Coleta sobre escrita e digitação para melhorar sugestões e correções |
| Diagnóstico e comentários | Nível de dados de diagnóstico enviados à Microsoft e frequência de pedidos de feedback |
| Permissões de pesquisa e Pesquisa no Windows | Dados de busca na nuvem; indexação de arquivos locais para busca rápida |

**Permissões de aplicativos** (liga e desliga global ou por app): localização, câmera, microfone, notificações, informações da conta, contatos, calendário, histórico de chamadas, e-mail, tarefas, mensagens (SMS e MMS), ativação por voz (apps reagindo a palavras-chave, mantendo o microfone ativo) e chamadas telefônicas.

### Windows Update

| Opção | Função |
| --- | --- |
| Verificar se há atualizações | Consulta manual aos servidores da Microsoft por correções, melhorias, segurança e drivers |
| Obter as atualizações mais recentes | Recebe novidades assim que liberadas; pode estar indisponível em máquinas gerenciadas por empresa |
| **Pausar atualizações** | Suspende a instalação por algumas semanas; depois volta a aplicar |
| Histórico de atualização | Lista o que foi instalado e permite **desinstalar** atualizações problemáticas |
| Opções avançadas | Otimização de entrega, atualizações opcionais, **horas ativas** e reinício automático |
| Programa Windows Insider | Versões de teste antes do lançamento oficial |

O Windows Update é a ferramenta que mantém o sistema e outros softwares da Microsoft atualizados (segurança, correções e desempenho). Não confundir com o Microsoft Defender (antivírus), a Microsoft Store (loja de apps) ou o Windows Hello (login).

### Para fixar

- Windows Hello: rosto, digital e PIN sem senha tradicional; os dados biométricos ficam apenas no dispositivo; chave de segurança usa FIDO2 (USB ou NFC).
- Bloqueio dinâmico bloqueia o PC quando o celular pareado se afasta.
- Backup do Windows liga apps, preferências, pastas do OneDrive e senhas à conta Microsoft.
- Teclado e idioma ficam em Hora e idioma.
- Jogos: Win + G, Xbox Game Bar, Capturas e Modo de Jogo.
- Acessibilidade: Win + U; Lupa liga com Win + + e desliga com Win + Esc; Narrador lê a tela.
- Privacidade e segurança: Segurança do Windows, Localizar meu dispositivo e permissões por aplicativo.
- Windows Update permite verificar, pausar, ver histórico e desinstalar atualizações.

