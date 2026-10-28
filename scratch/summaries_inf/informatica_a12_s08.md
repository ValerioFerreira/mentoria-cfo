##### informatica/a12/s08
Este trecho percorre seções das Configurações do Windows 11: Energia (suspender, hibernar, desligar), Recuperação, Área de Trabalho Remota, Área de Transferência, Bluetooth e Dispositivos, Rede e Internet e Personalização.

### Energia

Concentra o consumo de energia, útil em notebooks. Opções:

- **Recomendações de energia**: sugere até 5 ajustes (escurecer a tela, suspensão mais rápida, otimizar atividade em segundo plano).
- **Modo de energia**: perfis **Equilibrado** (bom desempenho com consumo moderado), **Economia de energia** e **Desempenho máximo**; em notebooks afeta a duração da bateria, a ventilação e a velocidade de resposta.
- **Tempo limite de tela, suspensão e hibernação**: quanto tempo de ociosidade até apagar a tela, suspender (modo stand-by) ou hibernar.
- **Economia de energia**: limita atividades em segundo plano e reduz o brilho; liga em um nível de bateria definido ou manualmente.
- **Controles de botão de energia e suspensão**: o que o botão liga/desliga e o fechamento da tampa fazem (suspender, hibernar, desligar ou nada).

| Opção | O que faz |
| --- | --- |
| **Suspender** | Salva o estado **na memória RAM** e deixa o PC em baixo consumo (ainda usa um pouco de energia); retoma rápido; para pausas curtas |
| **Hibernar** | Salva o estado **no disco rígido** e desliga totalmente; consumo zero; restaura exatamente como estava; para longas ausências |
| **Desligar** | Fecha programas e desliga; ao religar, o Windows inicia do zero |
| **Reiniciar** | Fecha programas e reinicia o sistema (após atualizações, instalações, problemas momentâneos) |
| **Sair** | Encerra a sessão do usuário e volta à tela de login, com o computador ligado |

> ⚠️ Pegadinha: o recurso que mantém o computador ligado com baixo consumo e monitor desligado é **Suspender** (não existe "Repousar"); **Hibernar existe em notebooks**, mesmo que venha desativado por padrão.

### Recuperação

- **Corrigir problemas sem redefinir o computador**: solução automática de erros comuns, sem apagar arquivos nem reinstalar.
- **Corrigir problemas usando o Windows Update**: baixa de novo componentes essenciais e substitui arquivos danificados; depende de conexão.
- **Restaurar o PC**: **reinstala o Windows**, podendo manter ou remover os arquivos pessoais (mas os aplicativos e as configurações são removidos de qualquer forma).
- **Retornar** (voltar a versão anterior do Windows): desfaz uma atualização de recurso (por exemplo, 22H2 para 23H2); fica disponível só por pouco tempo, normalmente **10 dias**, e depende de os arquivos da instalação antiga terem sido mantidos (não são 90 dias).
- **Inicialização Avançada**: reinicia em um ambiente especial de recuperação (WinRE) com restauração do sistema, prompt de comando, reparo de inicialização, reversão por **imagem de backup** (cópia completa do sistema) e instalação limpa por USB ou DVD. Não baixa imagem do site da Microsoft.
- Gerenciamento de disco serve para partições e volumes; Limpeza de disco remove temporários e instalações antigas (Windows.old), sem excluir o sistema atual.

### Área de Trabalho Remota

- Permite acessar e controlar outro computador à distância, como se estivesse na frente dele, por meio do protocolo **RDP** (*Remote Desktop Protocol*); serve para suporte técnico, trabalho remoto e administração de servidores. O computador de destino precisa estar ligado, configurado e com o recurso ativado.
- Você usa o aplicativo **Conexão de Área de Trabalho Remota** a partir de outro dispositivo e, após autenticar, enxerga e opera a tela remota.
- **Usuários da Área de Trabalho Remota**: por padrão só contas administrativas se conectam; é possível adicionar usuários específicos.
- **Edições**: **receber** conexões (ser acessado) só é possível nas edições Professional, Enterprise e Education; a edição **Home** não pode ser acessada remotamente, mas pode se conectar a outros PCs.

### Área de Transferência

- Ao copiar, o conteúdo vai para a área de transferência. **Histórico** (**Win + V**): guarda vários itens (texto, imagens, links) e permite fixar itens.
- **Sincronização entre dispositivos** com a mesma conta Microsoft (precisa de internet), de modo **automático** (tudo o que é copiado) ou **manual** (só o que o usuário escolher).
- **Limpar dados**: apaga tudo, **exceto os itens fixados**; fixar impede que o item seja removido ao limpar ou quando novos itens chegam, mas não cria tecla de atalho nem impede novos itens.
- Capacidade: o histórico guarda até 25 itens, com **24** efetivamente utilizáveis (resposta clássica de prova); armazena vários tipos de conteúdo e funciona com programas de qualquer fabricante.

### Bluetooth e Dispositivos

| Seção | Função |
| --- | --- |
| Bluetooth | Ativar, ver pareados e adicionar fones, teclados, mouses e caixas de som sem fio |
| Dispositivos | Mouses, teclados, monitores, adaptadores de áudio, canetas e outros periféricos |
| Impressoras e scanners | Adicionar, remover, configurar, definir impressora padrão e gerir filas |
| Dispositivos móveis | Conectar smartphone: trocar arquivos, mensagens e espelhar tela |
| Câmeras | Brilho, contraste, resolução e câmera padrão |
| Mouse | Velocidade do ponteiro, rolagem, trocar botões (destro ou canhoto) |
| Caneta e Windows Ink | Botões, modo de escrita, atalhos e lateralidade da caneta |
| Reprodução automática | O que fazer ao conectar pendrive, HD externo, CD ou cartão SD |
| USB | Notificações e suspensão seletiva para economizar bateria |

### Rede e Internet

| Seção | Função |
| --- | --- |
| Ethernet | Conexão cabeada: IP estático ou dinâmico, DNS preferencial e alternativo, rede limitada |
| VPN | Adicionar e conectar a servidores VPN (PPTP, L2TP/IPsec) com privacidade e criptografia |
| Hotspot móvel | Compartilha a conexão do PC por Wi-Fi, como roteador portátil |
| Modo avião | Desativa Wi-Fi, Bluetooth e conexões móveis |
| Proxy | Servidor proxy, de forma automática ou manual (controle de acesso, políticas) |
| Conexão discada | Recurso legado de modem telefônico (número, usuário e senha) |
| Configuração avançada de rede | Adaptadores, redefinição de rede, ponte e diagnóstico |

### Personalização

Tela de fundo (fotos, cores sólidas, slides e posição: cobrir a tela, ajustar, centralizar); Cores (cor de destaque, transparência, modo claro ou escuro); Temas (plano de fundo, cores, sons e cursor; baixados da Microsoft Store); Iluminação dinâmica (teclados RGB e periféricos); Tela de bloqueio; Entrada de texto (layout do teclado, idioma, escrita por voz, emojis, teclado virtual); Iniciar; Barra de tarefas; Fontes; Uso do dispositivo (jogos, trabalho, escola, criatividade, para o Windows sugerir dicas). A alteração das cores padrão é em **Personalização, Cores** (não em Sistema, Vídeo nem Facilidade de acesso).

### Para fixar

- Suspender guarda o estado na RAM; hibernar, no disco e desliga totalmente; desligar inicia do zero; reiniciar fecha tudo; sair encerra só a sessão.
- Modos de energia: Equilibrado, Economia de energia e Desempenho máximo; hibernar existe em notebooks.
- Restaurar o PC reinstala o Windows (mantendo ou removendo arquivos); retornar à versão anterior só vale por cerca de 10 dias; Inicialização Avançada abre o WinRE.
- Área de Trabalho Remota usa RDP; só edições Pro, Enterprise e Education aceitam conexão de entrada; Home só se conecta a outros.
- Área de Transferência (Win + V): histórico de até 25 itens (24 utilizáveis), itens fixados sobrevivem à limpeza, sincroniza por conta Microsoft.
- Bluetooth e Dispositivos reúne impressoras, mouse, caneta, câmeras e reprodução automática; Rede e Internet reúne Ethernet, VPN, hotspot, modo avião e proxy.
- Cores padrão do Windows: Personalização, Cores.

