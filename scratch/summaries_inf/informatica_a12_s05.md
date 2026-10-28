##### informatica/a12/s05
Este trecho trata dos três painéis do Explorador de Arquivos do Windows 11 (Navegação, Visualização e Detalhes) e de dois recursos de gerenciamento de janelas: a alternância de janelas (Alt + Tab e atalhos relacionados) e o Snap (Layouts, Groups e Assist).

### Painel de Navegação

É a coluna **à esquerda** do Explorador de Arquivos, com a estrutura hierárquica do sistema de arquivos: atalhos para pastas, unidades de disco, bibliotecas, locais de rede e serviços de nuvem. Setas ao lado dos nomes expandem ou recolhem pastas com subpastas, e o painel mostra onde você está dentro da árvore de pastas. Ele é personalizável: com o botão direito do mouse sobre um item aparecem opções como Renomear, Remover do Acesso rápido e **Fixar no Acesso rápido**.

| Item do painel | O que é |
| --- | --- |
| Acesso rápido | Atalhos para pastas fixadas manualmente e para as usadas com frequência; o usuário inclui ou retira itens |
| OneDrive | Armazenamento em nuvem da Microsoft integrado ao sistema; sincroniza e faz backup de arquivos entre dispositivos |
| Este Computador | Pastas pessoais (Documentos, Imagens, Downloads) e as unidades locais (disco C:, pendrives, discos externos) |
| Área de Trabalho | Pasta cujo conteúdo aparece na tela principal; guarda ícones, atalhos e arquivos colocados ali |
| Downloads | Destino padrão do que é baixado por navegadores e aplicativos |
| Documentos | Local padrão de textos, planilhas e apresentações; muito usada por Word e Excel |
| Imagens | Fotos, capturas de tela e imagens; integrada a aplicativos como Fotos e Paint |
| Músicas | Áudios, gravações e playlists |
| Vídeos | Vídeos pessoais, filmes e exportações de editores |

> ⚠️ Pegadinhas: no Windows, para tornar uma pasta mais acessível, a opção do menu de contexto é **Fixar no Acesso rápido**, e não "Adicionar" ou "Marcar". O OneDrive aparece no painel de navegação; Chrome, Word, Edge e Windows Defender não são itens do painel.

### Painel de Visualização

Área opcional **à direita** da janela que mostra uma **prévia do conteúdo** do arquivo, sem abri-lo no aplicativo padrão. Ativação: aba **Exibir** na Faixa de Opções, grupo **Mostrar**, opção **Painel de Visualização**. Ao selecionar um arquivo, o conteúdo aparece no painel: miniatura da imagem, primeiras linhas de um .docx ou .txt, primeiras páginas de um PDF.

- Funciona com .jpg, .png, .txt, .docx, .pdf, .mp4 e outros formatos, mas depende do mecanismo chamado **preview handler**; para alguns formatos é preciso ter instalado o programa correspondente (Office, leitor de PDF).
- **Arquivos .zip (compactados) não têm o conteúdo exibido** no painel: é necessário abri-los com um programa de compactação. Essa é a exceção cobrada em prova.

### Painel de Detalhes

Também fica à direita e é ativado em **Exibir > Mostrar > Painel de Detalhes**. Mostra os **metadados** do item selecionado, e não o conteúdo: nome, tipo, tamanho, datas de criação e modificação, autor e propriedades específicas. Em pastas, pode indicar a quantidade de itens e a data da última modificação. O conteúdo muda conforme o tipo de arquivo:

- música: álbum, artista, gênero e duração;
- foto: dimensões, resolução, câmera usada e configurações como ISO e exposição;
- documentos: título, tags e comentários, que em alguns casos podem ser **editados direto no painel**, se as permissões permitirem.

| Painel | Posição | Mostra |
| --- | --- | --- |
| Navegação | Esquerda | Árvore de pastas, unidades e locais |
| Visualização | Direita | Prévia do **conteúdo** do arquivo |
| Detalhes | Direita | **Propriedades** (metadados) do arquivo ou pasta |

Como Visualização e Detalhes ocupam o mesmo lugar, **não aparecem ao mesmo tempo**: escolhe-se um ou outro. Para organizar fotos por data, usa-se o Explorador de Arquivos com exibição em detalhes (a pasta se chama Painel de **Controle**, não "Painel de Comando"; e "Gerenciador de Arquivos" não é o nome correto).

### Alternância de janelas

| Atalho | Efeito |
| --- | --- |
| **Alt + Tab** | Mostra miniaturas das janelas abertas; mantendo Alt e tocando Tab, você percorre as janelas, e ao soltar Alt a escolhida vem para a frente |
| **Win + Tab** | Abre a **Visão de Tarefas**: janelas abertas, áreas de trabalho virtuais e histórico recente |
| **Ctrl + Alt + Tab** | Igual ao Alt + Tab, mas o painel de miniaturas **fica fixo** na tela, sem precisar segurar as teclas; navega-se por setas ou mouse |
| **Alt + Esc** | Alterna diretamente entre as janelas, **sem exibir caixa de diálogo** |

No Windows 11 as miniaturas ficaram maiores e com cantos arredondados (Fluent Design), e o Alt + Tab pode listar **cada aba do Microsoft Edge** separadamente. Isso é configurável em Configurações > Sistema > Multitarefa, onde se escolhe se o Alt + Tab mostra só as janelas ou também as abas do navegador.

> ⚠️ Pegadinha: outros atalhos frequentes que aparecem como alternativas erradas: Alt + F4 fecha a janela atual, Win + L bloqueia o computador, Win + D mostra ou oculta a Área de Trabalho, Ctrl + Shift + Esc abre o Gerenciador de Tarefas, Ctrl + Shift + N cria nova pasta e Win + seta para cima maximiza a janela.

### Snap

Recurso para encaixar janelas em posições predefinidas da tela, aproveitando melhor o espaço (útil em monitores grandes, ultrawide e múltiplos monitores). Já existia em versões anteriores, mas o Windows 11 o ampliou com a interface dos layouts.

| Componente | O que faz |
| --- | --- |
| **Snap Layouts** | Menu visual que aparece ao passar o mouse sobre o botão **maximizar** (ou ao pressionar **Win + Z**), com modelos de divisão em duas, três ou quatro áreas, colunas ou grade |
| **Snap Assist** | Assistente que surge depois de encaixar uma janela (por layout ou arrastando para a lateral) e sugere outras janelas abertas para ocupar os espaços restantes |
| **Snap Groups** | Gravação automática do arranjo criado; o grupo pode ser restaurado de uma vez, clicando nele na barra de tarefas |

Atalhos do Snap: **Win + seta para a esquerda ou direita** encaixa a janela na lateral; as setas para cima e para baixo também funcionam (maximizar, restaurar, minimizar); **Win + Z** abre o menu de layouts.

### Para fixar

- Painel de Navegação fica à esquerda (Acesso rápido, OneDrive, Este Computador); fixar pasta é "Fixar no Acesso rápido".
- Painel de Visualização mostra o conteúdo; Painel de Detalhes mostra os metadados; ambos ficam à direita e não coexistem; ativam-se em Exibir > Mostrar.
- Arquivo .zip não tem prévia no Painel de Visualização.
- Alt + Tab alterna janelas; Win + Tab abre a Visão de Tarefas; Ctrl + Alt + Tab mantém o painel fixo; Alt + Esc alterna sem caixa de diálogo.
- No Windows 11 o Alt + Tab pode incluir abas do Edge (Configurações > Sistema > Multitarefa).
- Snap Layouts aparece no botão maximizar ou com Win + Z; Snap Assist sugere janelas para ocupar o espaço; Snap Groups lembra o arranjo.

