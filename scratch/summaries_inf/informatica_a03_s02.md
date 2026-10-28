##### informatica/a03/s02
Este trecho percorre os tipos de vírus de computador, classificados pelo alvo que infectam (script, macro, boot, arquivo, multipartite, substituição), pela forma de se esconder (polimórfico, metamórfico, stealth), pelo momento de agir (time bomb) e pelo meio de propagação (e-mail). Lembre que o vírus é um malware dependente: precisa de um hospedeiro e da execução pelo usuário, ao contrário do worm, que se replica sozinho pela rede.

### Vírus de script
Script é um conjunto de instruções que diz ao computador o que fazer, como o JavaScript das páginas web, que as deixa dinâmicas. Documentos também carregam scripts: a macro do Excel é um script escrito em VBScript/VBA. O **vírus de script** é um código malicioso nessas linguagens, vindo de páginas web maliciosas, de anexos de e-mail ou do próprio corpo de mensagens em formato HTML. Conforme a configuração do navegador ou do leitor de e-mail, o script pode rodar automaticamente, sem clique do usuário. Por isso, nem anexos de remetente conhecido merecem confiança cega (o equipamento dele pode estar comprometido).

### Vírus de macro
Vírus de script especializado em linguagem de macro; contamina arquivos de aplicativos que usam essa linguagem, como Word, Excel, PowerPoint e Access (pacote Office). Tem incidência altíssima em prova. Características:
- infecta **documentos**, e não programas; como os documentos são muito compartilhados, ele se propaga com facilidade, em geral por anexos de e-mail;
- os controles de acesso tradicionais do sistema de arquivos pouco ajudam a contê-lo, pois ele vive em arquivos de dados do usuário;
- costuma alterar ou substituir comandos que o programa usa em ações comuns;
- só age quando o arquivo infectado é **aberto** (e a macro executada), momento em que passa a infectar outros arquivos;
- pode ser bloqueado desativando-se a execução de macros no Office; a assinatura digital com certificado também ajuda a evitá-lo.

> 💡 Exemplo: um usuário abre um .DOC recebido por e-mail e o computador passa a ter comportamento errático: a hipótese cobrada em prova é vírus de macro.

### Vírus de boot
Conhecido também como vírus de setor de inicialização, figura entre os mais antigos. Instala-se na área de partida do sistema (primeiro setor do disco/MBR, Master Boot Record) e é carregado na memória antes mesmo do sistema operacional, podendo impedir seu funcionamento correto. Também pode estar em dispositivos removíveis, como pendrives, e propagar-se por eles. Por isso, a **formatação rápida** de um pendrive infectado pode não eliminá-lo: ele pode permanecer na MBR, e o recomendado é evitar a opção de formatação rápida. (Incidência em prova baixíssima.)

### Vírus de arquivo (de programa ou parasitário)
É o vírus mais tradicional. Infecta **arquivos executáveis** (principalmente .exe; também .com, .dll e similares), sobrescrevendo o código original, o que causa danos quase sempre irreparáveis. Replica-se procurando outros executáveis e só contamina quem **executa** um arquivo já infectado. Incidência altíssima: entre os formatos de arquivo cobrados, o .EXE é o de maior risco; JPEG e MP3 oferecem risco baixo, e planilhas (.XLS) trazem o risco das macros.

### Vírus de substituição
Considerado uma forma de vírus de arquivo particularmente destrutiva: troca todo o conteúdo do executável por uma cópia de si mesmo, apagando o código legítimo, sem guardar cópia do original. Mesmo que o antivírus o remova, o arquivo só é recuperável a partir de um backup. A prevenção combina antivírus com proteção em tempo real, sistema atualizado, desconfiança de anexos e backups frequentes. (Incidência baixíssima.)

### Vírus multipartite
Infecta ao mesmo tempo mais de uma área, combinando o comportamento de vírus de arquivo e de vírus de boot (arquivos executáveis e setor de boot/MBR). A infecção começa na carga inicial do sistema, se o boot está contaminado, ou na execução de um arquivo infectado. É persistente: limpar só os arquivos não basta se o boot continua infectado, e vice-versa; a remoção pode exigir reparo do boot ou até reinstalação do sistema. Costuma usar técnicas de ocultação, como polimorfismo e stealth. A relação não é simétrica: todo multipartite tem um componente de boot, porém o vírus de boot comum ataca apenas a inicialização e, por isso, não é multipartite.

### Vírus polimórfico e metamórfico
O **polimórfico** (ou mutante) assume formas diferentes a cada infecção para driblar o antivírus: muda a assinatura (o padrão de bits que o identifica), mas mantém a função. Gera novas variantes alterando as rotinas de criptografia e descriptografia; por isso a detecção por simples comparação de assinatura é pouco eficaz, e o antivírus recorre a emulador ou à análise do padrão do corpo do vírus. O **metamórfico** é uma variação mais sofisticada: reescreve-se por completo a cada infecção, podendo mudar tamanho e comportamento. Regra de memória: o polimórfico muda a assinatura e preserva a funcionalidade; o metamórfico muda assinatura **e** funcionalidade.

### Vírus stealth (furtivo)
Foi projetado para não ser detectado: consegue, por exemplo, retirar-se temporariamente da memória para escapar do antivírus e intercepta chamadas do sistema para esconder sua presença (a analogia é com o avião furtivo, invisível ao radar). Não está ligado a arquivos Word ou Excel, que seria o caso do vírus de macro. (Incidência baixíssima.)

### Vírus time bomb (bomba-relógio)
Depois de infectar a máquina, fica latente, apenas se replicando, e executa a carga útil em um momento previsto pelo criador, como uma data. Costuma chegar como anexo de e-mail e depende de o usuário executar o arquivo. Exemplos: Sexta-feira 13 (age nas sextas-feiras 13), I Love You (12 de junho) e Chernobyl (25 de abril, segundo o material). Sua característica principal é a ativação em momento determinado, não a velocidade com que destrói o disco.

### Vírus de e-mail
Chega como anexo de mensagem cujo texto induz a clicar no arquivo. Ao agir, contamina arquivos e programas e remete cópias suas aos contatos armazenados na máquina. Medidas sensatas: desativar a execução automática de anexos no leitor de e-mail e conferir a extensão; não é necessário deixar de abrir todo anexo (basta passar o antivírus) nem excluir todas as mensagens com anexo.

### Para fixar
- Vírus precisa de hospedeiro e da execução pelo usuário; worm é autônomo.
- Script e macro: macro é um script em arquivos do Office; infecta documentos e se bloqueia desativando macros.
- Boot: MBR, carregado antes do sistema; a formatação rápida pode não removê-lo.
- Arquivo (programa): infecta executáveis (.exe) e sobrescreve o código; substituição é a forma destrutiva, sem recuperação sem backup.
- Multipartite: boot mais arquivo; todo multipartite inclui uma parte de boot, mas o contrário não vale.
- Polimórfico muda a assinatura e preserva a função; metamórfico reescreve tudo; stealth se esconde do antivírus.
- Time bomb age em momento definido; vírus de e-mail se espalha pelos contatos.

