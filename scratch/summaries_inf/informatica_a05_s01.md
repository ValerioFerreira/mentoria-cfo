##### informatica/a05/s01
Backup é a cópia de segurança que permite recuperar dados após perda por falha, desastre, furto ou exclusão acidental. O núcleo cobrado em prova são os **tipos de backup** e o comportamento de cada um diante do **atributo de arquivamento**. Este resumo cobre os conceitos, o atributo, os cinco tipos (completo, incremental, diferencial, de cópia e diário) e as práticas recomendadas.

### Conceitos básicos

Backup (também grafado "becape") é o serviço que garante poder recuperar informações de forma confiável e no tempo necessário. Ele protege principalmente a **integridade** dos dados; já a garantia plena de **disponibilidade** é tema controverso, e uma afirmação de que o backup, sozinho, garante a disponibilidade tende a ser considerada errada.

- **On-site**: a cópia fica na própria instituição. **Off-site**: a cópia fica em local geograficamente distante. O ideal é o off-site, porque um desastre no local principal não atinge a cópia.
- A **mídia** precisa ser segura e adequada: pendrive, fita magnética, cartão de memória, HD externo ou nuvem. A escolha considera volume de dados, tempo de leitura e gravação, tempo de restauração e custo.
- **Memória RAM não serve para backup**, pois é volátil: uma queda de energia apaga tudo.
- Em ambiente doméstico, um pendrive basta; em empresa, ele não é o mais indicado. Hoje o meio mais recomendado costuma ser a **nuvem**, por causa da infraestrutura física protegida, da redundância em locais distantes e da possibilidade de **criptografar** o backup.
- **Fita** é boa para grandes volumes guardados por muito tempo e com baixo custo, mas a gravação é sequencial e a recuperação é lenta (a unidade precisa percorrer a fita). **Disco** grava de forma aleatória e recupera mais rápido, sendo melhor para arquivos individuais.

### O atributo de arquivamento

Todo arquivo tem atributos, entre eles **R** (somente leitura), **H** (oculto), **S** (sistema) e **A** (arquivamento). Só o **A** interessa aqui. Ele é um único bit, também chamado de **Bit Archive** ou **Flag Archive**, que indica que o arquivo **ainda não passou por backup**.

- Sempre que um arquivo é criado ou salvo/modificado, o atributo A é **marcado** (Bit Archive = 1).
- Quando um backup que "limpa" o atributo copia o arquivo, o A é **desmarcado** (Bit Archive = 0), indicando que o arquivo foi arquivado.
- Na linguagem de prova: **marcado = 1 = arquivo precisa de backup**; **desmarcado = 0 = já sofreu backup**.

O software de backup decide o que copiar combinando o **tipo de backup** com o **estado do atributo A**. Copiar manualmente funciona, mas não é o recomendado.

### Visão geral dos tipos

| Tipo | O que copia | Desmarca o atributo A? |
| --- | --- | --- |
| Completo (normal, total, full) | Todos os arquivos selecionados | Sim |
| Incremental | Criados ou modificados desde o último completo ou incremental | Sim |
| Diferencial | Criados ou modificados desde o último completo (ou incremental) | **Não** |
| De cópia | Todos os arquivos selecionados | **Não** |
| Diário | Arquivos modificados no dia da execução | **Não** |

### Backup completo

Também chamado de **normal, total ou full**, copia **todos os dados selecionados**, estejam ou não alterados, e **desmarca** o atributo A. É a base de qualquer rotina.

- **Vantagens**: operação simples (não analisa nada, apenas copia), maior chance de recuperar dados íntegros e **restauração rápida**, pois basta o último backup completo.
- **Desvantagens**: execução demorada e muito espaço de armazenamento.
- Por isso costuma ser feito periodicamente (a cada 10 ou 15 dias, ou aos domingos para não prejudicar o desempenho das máquinas) e combinado com incrementais ou diferenciais.

> 💡 Exemplo: numa pasta com três arquivos recém-criados, todos com o atributo A, um backup completo copia os três para um único arquivo de backup e desmarca o A de todos.

Com relação à complexidade, o completo é o tipo **mais simples** e o mais fácil de restaurar.

### Backup incremental

Copia somente o que foi **criado ou modificado desde o último backup completo ou incremental** e **desmarca** o atributo A. Nasceu para corrigir a deficiência do completo, que recopia tudo a cada vez. O primeiro passo da rotina é sempre um backup completo.

- **Vantagens**: é o mais **rápido de executar** e o que **menos espaço** ocupa.
- **Desvantagem**: a **restauração é mais lenta e trabalhosa**. É preciso restaurar o último completo e, em seguida, **todos** os incrementais em ordem até o momento da falha.

> 💡 Exemplo: completo no domingo e incrementais de segunda a sexta. Se o disco queimar no sábado, será preciso restaurar o completo mais os cinco incrementais.

Um arquivo alterado em vários dias pode aparecer em vários incrementais, e todos serão usados na restauração. Depois de um incremental, o software espera encontrar o A desmarcado nos arquivos copiados; uma questão que afirme que, logo após o incremental, o bit está ajustado como "já copiado" está correta.

> ⚠️ Pegadinha: muitas questões dizem que o incremental copia o que mudou "desde o último backup de qualquer tipo". Isso só vale em rotinas com apenas completo e incremental. Com diferencial no meio, a afirmação cai, porque o diferencial não desmarca o A e o incremental seguinte voltaria a copiar os mesmos arquivos.

### Backup diferencial

Também conhecido como **incremental cumulativo**. Copia o que foi criado ou modificado desde o último backup **completo** (e, na definição mais genérica, também incremental), mas **não desmarca** o atributo A.

Como o A permanece marcado, cada novo diferencial **recopia tudo o que os diferenciais anteriores já tinham copiado** e acrescenta as novidades. Ele cresce a cada dia.

- **Desvantagens**: mais espaço e mais tempo de execução que o incremental.
- **Vantagem**: restauração **mais rápida** que a do incremental, pois bastam o **último completo e o último diferencial**; os diferenciais anteriores podem ser descartados.

Síntese: **o incremental é mais rápido para criar e mais lento para restaurar; o diferencial é mais lento para criar e mais rápido para restaurar.**

#### Comparando dia a dia

Imagine uma base que ganha um item novo por dia. Num completo, o conteúdo vai crescendo inteiro. No incremental, cada dia leva apenas o item novo (D, depois E, depois F). No diferencial, cada dia leva a soma desde o completo (D, depois DE, depois DEF). Se a falha vier no fim, o incremental exige completo mais todos os pedaços; o diferencial exige o completo mais o último pedaço.

#### A pegadinha das definições

Incremental e diferencial têm a mesma frase de definição, e o que os diferencia é **o tratamento do atributo A depois da cópia**: o incremental desmarca, o diferencial não. Ainda mais: dizer que o diferencial copia o que mudou "desde o último backup completo" só é exato quando a rotina tem apenas completos e diferenciais. Se houver um incremental no meio (completo na segunda, incremental na terça, diferencial na quarta), o diferencial de quarta copia o que mudou desde o incremental de terça.

Muitas questões usam a forma restrita ("desde o último completo"). Por isso, quando a pergunta pede uma definição simples e direta, aceite-a; quando for sofisticada e a alternativa trouxer "completo ou incremental", essa é a forma mais abrangente. Em alternativas que invertem os conceitos (diferencial marca arquivos, incremental precisa só do completo), desconfie: estão trocados.

### Backup de cópia

Copia todos os arquivos selecionados, mas **não altera** o atributo A. Usa-se em situações **emergenciais** ou antes de uma mudança crucial no sistema, porque **não interfere** na rotina de backups da organização (nem em completos nem em incrementais). É raro em prova.

### Backup diário

Entre os itens escolhidos para backup, leva apenas aqueles cuja alteração aconteceu **na data em que a rotina roda**; o único critério é a **data**. Também **não altera** o atributo A. É raro em prova; guarde a ideia de que olha para a data de hoje e não para o bit.

### Práticas recomendadas

A lista é longa, mas as ideias que mais aparecem são:

- definir a **periodicidade** conforme a criticidade dos dados e a taxa de alteração (backup de e-mails semestral é inadequado);
- manter **várias cópias**, em **mídias diferentes** e em **locais diferentes**, com **pelo menos uma cópia fora do local principal**, em lugar seguro (cofre ou nuvem);
- **agendar** os backups para evitar falha humana e **monitorar** o sucesso e a integridade deles;
- **testar a restauração** regularmente e simular desastres; não é dispensável testar;
- **documentar** os procedimentos de restauração e conscientizar os usuários;
- usar **criptografia** nos backups e guardá-los em local seguro;
- verificar o espaço disponível e configurar alertas quando estiver no limite;
- fazer backup de **todos os dados relevantes**, não só dos mais recentes, e dar prioridade a dados e configurações críticas; refazer o backup completo do sistema operacional e dos aplicativos com frequência não é necessário.

### Para fixar

- O atributo de arquivamento é um bit: marcado (1) significa que o arquivo ainda não passou por backup; desmarcado (0), que já passou.
- Completo copia tudo, desmarca o A, é o mais simples e o de restauração mais rápida, mas o de execução mais lenta.
- Incremental copia o novo desde o último completo ou incremental, desmarca o A, é o mais rápido para criar e o mais lento para restaurar.
- Diferencial copia o acumulado desde o último completo, não desmarca o A, restaura com o último completo e o último diferencial.
- Cópia e diário não alteram o A; o diário usa a data de modificação do dia.
- RAM é volátil e não serve para backup; ao menos uma cópia deve ficar off-site; nuvem e criptografia são boas práticas.
- Testar a restauração periodicamente é essencial.

