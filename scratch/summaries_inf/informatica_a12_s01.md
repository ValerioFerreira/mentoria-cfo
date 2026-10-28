##### informatica/a12/s01
Este trecho conta por que existem sistemas operacionais, apresenta o Windows e reúne as novidades, os requisitos mínimos e as edições do Windows 11.

### Por que existe o sistema operacional

- Nos primeiros computadores, cada programa era entregue em cartões perfurados e a máquina rodava um programa por vez, com muita intervenção humana.
- Os primeiros sistemas operacionais automatizaram esse processo: vários programas passaram a ser executados em sequência, sem troca manual de cartões (**processamento em lote**).
- Com a variedade de periféricos (impressoras, mouses, scanners), surgiram os **drivers**: o sistema envia uma ordem genérica (imprimir) e o driver a traduz para a linguagem do dispositivo específico. Hoje o sistema costuma reconhecer e instalar o driver sozinho.
- O sistema operacional é o elo entre software e hardware e padroniza o funcionamento da máquina. Seu núcleo é o **kernel**, que gerencia memória, multitarefa (programas simultâneos) e entrada e saída de dados. Falha grave no kernel trava a máquina (a "tela azul").
- O **shell** é a interface entre o usuário e o sistema (interpreta comandos); o kernel é quem gerencia todos os recursos. Questão clássica: quem gerencia os recursos é o kernel, não o shell, a ROM nem o DOS (que é um sistema operacional).

### O Windows

O Windows, da Microsoft (criado por Bill Gates e equipe), recebe o nome das janelas ("windows") que aparecem a cada programa aberto: a interface visual virou padrão. Ele organiza os programas em execução e distribui memória e processamento, e já traz programas básicos (navegador, editor de texto simples, reprodutor de áudio e vídeo). Está em mais de 90% dos computadores pessoais. É multitarefa preemptivo (o próprio sistema controla o uso da CPU), multiusuário e de interface gráfica.

Linha do tempo citada: Windows 7 (outubro de 2009, menos de 3 anos após o Vista), Windows 8 (pouco mais de 3 anos depois), Windows 10 (julho de 2015) e Windows 11 (apresentado como lançamento de 2021; o texto cita outubro e também junho de 2021). O Windows 11 é construído sobre a mesma base do Windows 10, uma transição natural, e foi projetado para o trabalho híbrido (móvel e fixo).

### Novidades do Windows 11

Interface e organização:

- **Menu Iniciar centralizado** na barra de tarefas, com aplicativos fixados, documentos recentes e busca integrada.
- **Esquinas arredondadas e transparências** (efeito acrílico, animações suaves).
- **Widgets personalizáveis**: painel com previsão do tempo, notícias, calendário e tarefas.
- **Novo Explorador de Arquivos**: ícones renovados, nova barra de comandos e integração com a nuvem.
- **Novos temas e sons**, de tons suaves até modo escuro completo.
- **Snap Layouts**: passar o mouse no botão de maximizar mostra formatos prontos para organizar janelas (inclusive em monitores ultrawide).
- **Snap Groups**: o sistema lembra os conjuntos de janelas e restaura o grupo em uma ação.
- **Múltiplos desktops virtuais**, cada um com papel de parede próprio.
- **Suporte a várias telas**: lembra a posição das janelas ao reconectar monitores.
- **Nova Central de Configurações**, organizada em categorias, com busca melhor.

Produtividade e comunicação:

- **Microsoft Teams integrado**: reuniões, chamadas e chats a partir da barra de tarefas.
- **Modo Foco**: silencia notificações, com integração ao relógio e à lista de tarefas.
- **Copilot**: assistente de IA integrado, que responde perguntas, executa comandos e ajusta configurações.
- **Armazenamento Inteligente**: limpa automaticamente temporários, cache e lixeira.
- **Indicadores visuais de áudio e microfone**: mostram quando o microfone está ativo (privacidade).

Desempenho e compatibilidade:

- **Novo Gerenciador de Tarefas**: visual renovado, filtros, aba de eficiência energética, modo escuro.
- **Otimização para SSDs (NVMe) e inicialização rápida.**
- **Auto HDR e DirectStorage** (vindos do Xbox): cores melhores em jogos e carregamento mais rápido.
- **Melhor gestão de energia e bateria** em notebooks.
- **Compatibilidade com chips ARM.**
- **Suporte nativo a aplicativos Android**, por subsistema e loja integrada.

> ⚠️ Pegadinha: Snap Layouts organiza janelas pelo botão de maximizar; o menu Iniciar centralizado é o padrão do Windows 11 (pode ser movido para a esquerda).

### Requisitos mínimos

| Critério | Mínimo |
| --- | --- |
| Arquitetura | 64 bits (não há mais suporte a 32 bits) |
| Processador | 1 GHz |
| Memória RAM | 4 GB |
| Espaço livre em disco | 64 GB |

Em complemento, o Windows 11 também exige chip de segurança TPM 2.0 (citado como requisito de segurança) e inicialização UEFI com boot seguro.

### Edições

| Edição | Perfil e recursos |
| --- | --- |
| Home | Usuário doméstico; traz as funções básicas (widgets, Snap, Teams); modo S opcional; exige conta Microsoft e internet no primeiro uso; não hospeda área de trabalho remota |
| Pro | Profissionais e pequenas empresas; acrescenta BitLocker, Política de Grupo, Hyper-V, Área de Trabalho Remota (como host), até 2 TB de RAM e dois processadores |

Existem ainda Pro para Workstations, SE (educação), Enterprise e IoT Enterprise.

### Para fixar

- O sistema operacional liga software e hardware; o kernel é o núcleo que gerencia memória, CPU, dispositivos e processos.
- Driver traduz as ordens genéricas do sistema para cada dispositivo; processamento em lote foi o primeiro avanço dos sistemas operacionais.
- Windows: multitarefa preemptivo, multiusuário, interface gráfica de janelas.
- Windows 11: menu Iniciar centralizado, Snap Layouts e Snap Groups, widgets, Teams integrado, Copilot, Modo Foco e aplicativos Android.
- Requisitos mínimos: 64 bits, 1 GHz, 4 GB de RAM, 64 GB livres, além de TPM 2.0 e UEFI com boot seguro.
- Home: uso doméstico, conta Microsoft obrigatória e sem host de área de trabalho remota.
- Pro: BitLocker, Política de Grupo, Hyper-V, Área de Trabalho Remota, até 2 TB de RAM.

