# Prompts para os colaboradores externos (lotes 2, 3, 5 e 6)

## 1. O que enviar a cada colaborador (pacote)
Todos os arquivos estão no repositório, na pasta `resumos-colaboradores/` (raiz do projeto):

| Arquivo | Para quê |
| --- | --- |
| `resumos-colaboradores/INSTRUCOES.md` | Documento autossuficiente: método, estilo, formato exato do arquivo, originalidade, identificação do agente, entrega. **É a regra de execução.** |
| `resumos-colaboradores/INDICE-RESUMOS.xlsx` (ou `.csv`) | A lista de atividades: ID, matéria, aula, trecho, assuntos, PDF, páginas, alvo de palavras, **Lote**, **Sublote**, status. |
| `resumos-colaboradores/verificar_resumos.py` | Autoverificação (Python 3, sem dependências). |
| PDFs do material | Pasta `docs/` da raiz: **somente as pastas do lote** (ver cada prompt). Os PDFs de "Complemento" estão em `web/public/complementos/`. |

Os PDFs têm marca d'água e são material protegido: envie só o necessário ao lote e peça sigilo (não repassar o texto). Não envie `content/`, `pipeline/` nem o código.

## 2. Diretrizes de execução (valem para todos os lotes)
1. **Seguir o `INSTRUCOES.md` à risca.** Ele manda sobre formato, estilo, tabelas/figuras, originalidade (nenhuma sequência de 10 palavras igual ao material) e identificação.
2. **Agentes em paralelo.** Cada colaborador cria **3 agentes em paralelo** (A, B e C), cada um com 2 sublotes próprios e distintos (o lote tem 6 sublotes). Cada agente tem **identificador próprio** (ex.: `EXT-L2-A`), usado no nome dos arquivos, no cabeçalho e na pasta de entrega. Nenhum ID pode ser feito por dois agentes.
3. **Ordem de prioridade**: dentro do sublote, na ordem dos IDs; os sublotes de cada agente em ordem numérica. Não pular para as atividades mais fáceis.
4. **Ciclos curtos**: cada chamada de agente faz no máximo ~6 resumos consecutivos e recomeça de onde parou (evita estourar o contexto/limite de sessão). Antes de cada ciclo, o agente lista os IDs do seu sublote que ainda **não têm arquivo** e faz os próximos.
5. **Salvar cada resumo assim que concluído**: um arquivo `Sxxxx__AGENTE.md` por atividade, gravado e conferido (`verificar_resumos.py`) antes de passar ao próximo. Nunca acumular para salvar no fim.
6. **Entregar por sublote**: pasta `resumos_AGENTE_L2-01` com os arquivos + `RELATORIO_AGENTE.md`, compactada em `.zip`. Não esperar o lote inteiro.
7. **Não inventar**: dúvida sobre artigo, número ou data vai em `# NOTAS`, nunca no texto do resumo.
8. **Fase 1 apenas**: os lotes 1 a 6 só têm assuntos do edital do CFO CBMPE. Atualidades, Raciocínio Lógico e História de PE (Fase 2) serão passados depois, a quem terminar primeiro.

---

## Prompt — Lote 2 (Informática + Língua Inglesa)

Anexos para este colaborador: `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx`, `verificar_resumos.py`, as pastas de PDFs **06 - CBM-PE (Oficial) Informática**, **01 - CBM-PE (Oficial) Língua Inglesa** (de `docs/`) e os PDFs de complemento `ing-estruturas-complementares.pdf` (de `web/public/complementos/`).

```text
Você vai produzir resumos de estudo para um sistema de planejamento de concursos (CFO CBMPE). Receberá em anexo: (1) INSTRUCOES.md, o documento que manda em TUDO (método, estilo, formato exato dos arquivos, originalidade, identificação, entrega); (2) INDICE-RESUMOS.xlsx, a lista de atividades; (3) verificar_resumos.py, a autoverificação; (4) os PDFs do material das disciplinas do seu lote (06 - CBM-PE (Oficial) Informática e 01 - CBM-PE (Oficial) Língua Inglesa) e os PDFs de complemento (ing-estruturas-complementares.pdf). Você não tem acesso ao sistema nem ao código: trabalhe só com esses arquivos. Leia o INSTRUCOES.md INTEIRO antes de começar.

SUA TAREFA: executar o LOTE 2 do índice. Filtre a coluna Lote = 2 (109 atividades 'A fazer', 6 sublotes: L2-01, L2-02, L2-03, L2-04, L2-05, L2-06). Cada linha é uma atividade de Teoria: leia SOMENTE as páginas indicadas (Pág. inicial a Pág. final) do PDF indicado e escreva, com as suas palavras, o resumo analítico e o resumo sintético no formato do INSTRUCOES.md.

COMO ORGANIZAR O TRABALHO — AGENTES EM PARALELO (obrigatório): crie 3 agentes trabalhando ao mesmo tempo, cada um com sublotes próprios e distintos e com identificador próprio:
- Agente EXT-L2-A: sublotes L2-01 e L2-02 (40 atividades; IDs S0087–S0127, S0132–S0185). Arquivos: Sxxxx__EXT-L2-A.md.
- Agente EXT-L2-B: sublotes L2-03 e L2-04 (40 atividades; IDs S0186–S0216, S0217–S0240). Arquivos: Sxxxx__EXT-L2-B.md.
- Agente EXT-L2-C: sublotes L2-05 e L2-06 (29 atividades; IDs S0241–S0290, S0291–S0357). Arquivos: Sxxxx__EXT-L2-C.md.
ATENÇÃO: identifique as atividades de cada sublote pela coluna Sublote do índice, não pela faixa de IDs (a faixa tem buracos: os IDs intermediários pertencem a outros lotes e NÃO são seus).
Nenhuma atividade pode ser feita por dois agentes. (Se preferir outro número de agentes, divida os sublotes de forma disjunta, com um identificador por agente, mantendo cada sublote inteiro com um único agente.)

DIRETRIZES DE EXECUÇÃO:
1. Dentro de cada sublote, faça as atividades NA ORDEM DOS IDs (ordem de prioridade do produto) e os sublotes do agente em ordem numérica. Não pule para as mais fáceis. Pule linhas cujo status não seja 'A fazer'.
2. Trabalhe em ciclos curtos: no máximo ~6 resumos consecutivos por vez, listando antes quais IDs do seu sublote ainda não têm arquivo. Isso evita estourar o contexto; se a sessão cair, retome pulando os IDs que já têm arquivo.
3. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO: um arquivo Sxxxx__AGENTE.md por atividade, em UTF-8, no formato exato da seção 11 do INSTRUCOES.md (cabeçalho com id, agente, matéria, aula, trecho, páginas lidas; seções '# ANALÍTICO', '# SINTÉTICO', '# NOTAS'). Confira com: python verificar_resumos.py <pasta> --indice INDICE-RESUMOS.csv, e corrija os erros ANTES de passar ao próximo. Nunca acumule resumos para salvar no fim.
4. Leia o trecho INTEIRO antes de escrever; cubra todos os assuntos da coluna 'Atividade (assuntos do trecho)'; respeite o 'Alvo máx. (palavras)' (teto de ~20 min de leitura; não encha, o tamanho é o que o conteúdo pedir; mínimo 250 palavras). Figuras do material: descarte (salvo se forem a fonte da informação); tabelas: aproveite só o que acrescentar informação.
5. ORIGINALIDADE: o material é protegido. Escreva com as SUAS palavras; nenhuma sequência de 10 palavras iguais ao PDF. Não cite 'a aula', 'o PDF', 'o professor'. Não invente: o que não conseguir confirmar (artigo, número, data) fica FORA do resumo e vai em '# NOTAS'.
6. ENTREGA POR SUBLOTE (não espere o lote inteiro): ao terminar um sublote, monte a pasta resumos_AGENTE_SUBLOTE (ex.: resumos_EXT-L2-A_L2-01) só com os arquivos .md do sublote + RELATORIO_AGENTE.md (sublote recebido; IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico), rode a autoverificação e compacte em .zip. Não renomeie nem altere arquivos já entregues; não altere o índice.
7. Qualidade: antes de salvar, releia como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). A entrega será auditada por amostragem: 5 resumos sorteados por agente serão conferidos contra o PDF; resumos fora do padrão voltam para refação.

Ao final, devolva todos os .zip (um por sublote) e a lista do que ficou pendente, se algo ficou.
```

---

## Prompt — Lote 3 (Biologia + Língua Portuguesa)

Anexos para este colaborador: `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx`, `verificar_resumos.py`, as pastas de PDFs **07 - CBM-PE (Oficial) Biologia**, **03 - CBM-PE (Oficial) Língua Portuguesa** (de `docs/`) e os PDFs de complemento `bio-biotec-ambiente.pdf`, `bio-qualidade-vida.pdf` (de `web/public/complementos/`).

```text
Você vai produzir resumos de estudo para um sistema de planejamento de concursos (CFO CBMPE). Receberá em anexo: (1) INSTRUCOES.md, o documento que manda em TUDO (método, estilo, formato exato dos arquivos, originalidade, identificação, entrega); (2) INDICE-RESUMOS.xlsx, a lista de atividades; (3) verificar_resumos.py, a autoverificação; (4) os PDFs do material das disciplinas do seu lote (07 - CBM-PE (Oficial) Biologia e 03 - CBM-PE (Oficial) Língua Portuguesa) e os PDFs de complemento (bio-biotec-ambiente.pdf, bio-qualidade-vida.pdf). Você não tem acesso ao sistema nem ao código: trabalhe só com esses arquivos. Leia o INSTRUCOES.md INTEIRO antes de começar.

SUA TAREFA: executar o LOTE 3 do índice. Filtre a coluna Lote = 3 (111 atividades 'A fazer', 6 sublotes: L3-01, L3-02, L3-03, L3-04, L3-05, L3-06). Cada linha é uma atividade de Teoria: leia SOMENTE as páginas indicadas (Pág. inicial a Pág. final) do PDF indicado e escreva, com as suas palavras, o resumo analítico e o resumo sintético no formato do INSTRUCOES.md.

COMO ORGANIZAR O TRABALHO — AGENTES EM PARALELO (obrigatório): crie 3 agentes trabalhando ao mesmo tempo, cada um com sublotes próprios e distintos e com identificador próprio:
- Agente EXT-L3-A: sublotes L3-01 e L3-02 (40 atividades; IDs S0028–S0062, S0063–S0249). Arquivos: Sxxxx__EXT-L3-A.md.
- Agente EXT-L3-B: sublotes L3-03 e L3-04 (40 atividades; IDs S0253–S0420, S0428–S0510). Arquivos: Sxxxx__EXT-L3-B.md.
- Agente EXT-L3-C: sublotes L3-05 e L3-06 (31 atividades; IDs S0512–S0546, S0547–S0563). Arquivos: Sxxxx__EXT-L3-C.md.
ATENÇÃO: identifique as atividades de cada sublote pela coluna Sublote do índice, não pela faixa de IDs (a faixa tem buracos: os IDs intermediários pertencem a outros lotes e NÃO são seus).
Nenhuma atividade pode ser feita por dois agentes. (Se preferir outro número de agentes, divida os sublotes de forma disjunta, com um identificador por agente, mantendo cada sublote inteiro com um único agente.)

DIRETRIZES DE EXECUÇÃO:
1. Dentro de cada sublote, faça as atividades NA ORDEM DOS IDs (ordem de prioridade do produto) e os sublotes do agente em ordem numérica. Não pule para as mais fáceis. Pule linhas cujo status não seja 'A fazer'.
2. Trabalhe em ciclos curtos: no máximo ~6 resumos consecutivos por vez, listando antes quais IDs do seu sublote ainda não têm arquivo. Isso evita estourar o contexto; se a sessão cair, retome pulando os IDs que já têm arquivo.
3. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO: um arquivo Sxxxx__AGENTE.md por atividade, em UTF-8, no formato exato da seção 11 do INSTRUCOES.md (cabeçalho com id, agente, matéria, aula, trecho, páginas lidas; seções '# ANALÍTICO', '# SINTÉTICO', '# NOTAS'). Confira com: python verificar_resumos.py <pasta> --indice INDICE-RESUMOS.csv, e corrija os erros ANTES de passar ao próximo. Nunca acumule resumos para salvar no fim.
4. Leia o trecho INTEIRO antes de escrever; cubra todos os assuntos da coluna 'Atividade (assuntos do trecho)'; respeite o 'Alvo máx. (palavras)' (teto de ~20 min de leitura; não encha, o tamanho é o que o conteúdo pedir; mínimo 250 palavras). Figuras do material: descarte (salvo se forem a fonte da informação); tabelas: aproveite só o que acrescentar informação.
5. ORIGINALIDADE: o material é protegido. Escreva com as SUAS palavras; nenhuma sequência de 10 palavras iguais ao PDF. Não cite 'a aula', 'o PDF', 'o professor'. Não invente: o que não conseguir confirmar (artigo, número, data) fica FORA do resumo e vai em '# NOTAS'.
6. ENTREGA POR SUBLOTE (não espere o lote inteiro): ao terminar um sublote, monte a pasta resumos_AGENTE_SUBLOTE (ex.: resumos_EXT-L3-A_L3-01) só com os arquivos .md do sublote + RELATORIO_AGENTE.md (sublote recebido; IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico), rode a autoverificação e compacte em .zip. Não renomeie nem altere arquivos já entregues; não altere o índice.
7. Qualidade: antes de salvar, releia como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). A entrega será auditada por amostragem: 5 resumos sorteados por agente serão conferidos contra o PDF; resumos fora do padrão voltam para refação.

Ao final, devolva todos os .zip (um por sublote) e a lista do que ficou pendente, se algo ficou.
```

---

## Prompt — Lote 5 (Matemática + Física)

Anexos para este colaborador: `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx`, `verificar_resumos.py`, as pastas de PDFs **10 - CBM-PE (Oficial) Matemática**, **12 - CBM-PE (Oficial) Física** (de `docs/`) e os PDFs de complemento `fis-optica-geometrica.pdf`, `fis-topicos-edital.pdf`, `mat-complementos-edital.pdf`, `mat-geometria-analitica.pdf` (de `web/public/complementos/`).

```text
Você vai produzir resumos de estudo para um sistema de planejamento de concursos (CFO CBMPE). Receberá em anexo: (1) INSTRUCOES.md, o documento que manda em TUDO (método, estilo, formato exato dos arquivos, originalidade, identificação, entrega); (2) INDICE-RESUMOS.xlsx, a lista de atividades; (3) verificar_resumos.py, a autoverificação; (4) os PDFs do material das disciplinas do seu lote (10 - CBM-PE (Oficial) Matemática e 12 - CBM-PE (Oficial) Física) e os PDFs de complemento (fis-optica-geometrica.pdf, fis-topicos-edital.pdf, mat-complementos-edital.pdf, mat-geometria-analitica.pdf). Você não tem acesso ao sistema nem ao código: trabalhe só com esses arquivos. Leia o INSTRUCOES.md INTEIRO antes de começar.

SUA TAREFA: executar o LOTE 5 do índice. Filtre a coluna Lote = 5 (117 atividades 'A fazer', 6 sublotes: L5-01, L5-02, L5-03, L5-04, L5-05, L5-06). Cada linha é uma atividade de Teoria: leia SOMENTE as páginas indicadas (Pág. inicial a Pág. final) do PDF indicado e escreva, com as suas palavras, o resumo analítico e o resumo sintético no formato do INSTRUCOES.md.

COMO ORGANIZAR O TRABALHO — AGENTES EM PARALELO (obrigatório): crie 3 agentes trabalhando ao mesmo tempo, cada um com sublotes próprios e distintos e com identificador próprio:
- Agente EXT-L5-A: sublotes L5-01 e L5-02 (40 atividades; IDs S0566–S0591, S0592–S0619). Arquivos: Sxxxx__EXT-L5-A.md.
- Agente EXT-L5-B: sublotes L5-03 e L5-04 (40 atividades; IDs S0620–S0656, S0658–S0687). Arquivos: Sxxxx__EXT-L5-B.md.
- Agente EXT-L5-C: sublotes L5-05 e L5-06 (37 atividades; IDs S0689–S0717, S0718–S0758). Arquivos: Sxxxx__EXT-L5-C.md.
ATENÇÃO: identifique as atividades de cada sublote pela coluna Sublote do índice, não pela faixa de IDs (a faixa tem buracos: os IDs intermediários pertencem a outros lotes e NÃO são seus).
Nenhuma atividade pode ser feita por dois agentes. (Se preferir outro número de agentes, divida os sublotes de forma disjunta, com um identificador por agente, mantendo cada sublote inteiro com um único agente.)

DIRETRIZES DE EXECUÇÃO:
1. Dentro de cada sublote, faça as atividades NA ORDEM DOS IDs (ordem de prioridade do produto) e os sublotes do agente em ordem numérica. Não pule para as mais fáceis. Pule linhas cujo status não seja 'A fazer'.
2. Trabalhe em ciclos curtos: no máximo ~6 resumos consecutivos por vez, listando antes quais IDs do seu sublote ainda não têm arquivo. Isso evita estourar o contexto; se a sessão cair, retome pulando os IDs que já têm arquivo.
3. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO: um arquivo Sxxxx__AGENTE.md por atividade, em UTF-8, no formato exato da seção 11 do INSTRUCOES.md (cabeçalho com id, agente, matéria, aula, trecho, páginas lidas; seções '# ANALÍTICO', '# SINTÉTICO', '# NOTAS'). Confira com: python verificar_resumos.py <pasta> --indice INDICE-RESUMOS.csv, e corrija os erros ANTES de passar ao próximo. Nunca acumule resumos para salvar no fim.
4. Leia o trecho INTEIRO antes de escrever; cubra todos os assuntos da coluna 'Atividade (assuntos do trecho)'; respeite o 'Alvo máx. (palavras)' (teto de ~20 min de leitura; não encha, o tamanho é o que o conteúdo pedir; mínimo 250 palavras). Figuras do material: descarte (salvo se forem a fonte da informação); tabelas: aproveite só o que acrescentar informação.
5. ORIGINALIDADE: o material é protegido. Escreva com as SUAS palavras; nenhuma sequência de 10 palavras iguais ao PDF. Não cite 'a aula', 'o PDF', 'o professor'. Não invente: o que não conseguir confirmar (artigo, número, data) fica FORA do resumo e vai em '# NOTAS'.
6. ENTREGA POR SUBLOTE (não espere o lote inteiro): ao terminar um sublote, monte a pasta resumos_AGENTE_SUBLOTE (ex.: resumos_EXT-L5-A_L5-01) só com os arquivos .md do sublote + RELATORIO_AGENTE.md (sublote recebido; IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico), rode a autoverificação e compacte em .zip. Não renomeie nem altere arquivos já entregues; não altere o índice.
7. Qualidade: antes de salvar, releia como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). A entrega será auditada por amostragem: 5 resumos sorteados por agente serão conferidos contra o PDF; resumos fora do padrão voltam para refação.

Ao final, devolva todos os .zip (um por sublote) e a lista do que ficou pendente, se algo ficou.
```

---

## Prompt — Lote 6 (Química + Língua Espanhola)

Anexos para este colaborador: `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx`, `verificar_resumos.py`, as pastas de PDFs **09 - CBM-PE (Oficial) Química**, **05 - CBM-PE (Oficial) Língua Espanhola** (de `docs/`) e os PDFs de complemento `esp-grau-verbos-heterograficos.pdf`, `quim-aplicada-complementos.pdf` (de `web/public/complementos/`).

```text
Você vai produzir resumos de estudo para um sistema de planejamento de concursos (CFO CBMPE). Receberá em anexo: (1) INSTRUCOES.md, o documento que manda em TUDO (método, estilo, formato exato dos arquivos, originalidade, identificação, entrega); (2) INDICE-RESUMOS.xlsx, a lista de atividades; (3) verificar_resumos.py, a autoverificação; (4) os PDFs do material das disciplinas do seu lote (09 - CBM-PE (Oficial) Química e 05 - CBM-PE (Oficial) Língua Espanhola) e os PDFs de complemento (esp-grau-verbos-heterograficos.pdf, quim-aplicada-complementos.pdf). Você não tem acesso ao sistema nem ao código: trabalhe só com esses arquivos. Leia o INSTRUCOES.md INTEIRO antes de começar.

SUA TAREFA: executar o LOTE 6 do índice. Filtre a coluna Lote = 6 (116 atividades 'A fazer', 6 sublotes: L6-01, L6-02, L6-03, L6-04, L6-05, L6-06). Cada linha é uma atividade de Teoria: leia SOMENTE as páginas indicadas (Pág. inicial a Pág. final) do PDF indicado e escreva, com as suas palavras, o resumo analítico e o resumo sintético no formato do INSTRUCOES.md.

COMO ORGANIZAR O TRABALHO — AGENTES EM PARALELO (obrigatório): crie 3 agentes trabalhando ao mesmo tempo, cada um com sublotes próprios e distintos e com identificador próprio:
- Agente EXT-L6-A: sublotes L6-01 e L6-02 (40 atividades; IDs S0255–S0337, S0338–S0581). Arquivos: Sxxxx__EXT-L6-A.md.
- Agente EXT-L6-B: sublotes L6-03 e L6-04 (40 atividades; IDs S0587–S0636, S0640–S0688). Arquivos: Sxxxx__EXT-L6-B.md.
- Agente EXT-L6-C: sublotes L6-05 e L6-06 (36 atividades; IDs S0690–S0734, S0737–S0761). Arquivos: Sxxxx__EXT-L6-C.md.
ATENÇÃO: identifique as atividades de cada sublote pela coluna Sublote do índice, não pela faixa de IDs (a faixa tem buracos: os IDs intermediários pertencem a outros lotes e NÃO são seus).
Nenhuma atividade pode ser feita por dois agentes. (Se preferir outro número de agentes, divida os sublotes de forma disjunta, com um identificador por agente, mantendo cada sublote inteiro com um único agente.)

DIRETRIZES DE EXECUÇÃO:
1. Dentro de cada sublote, faça as atividades NA ORDEM DOS IDs (ordem de prioridade do produto) e os sublotes do agente em ordem numérica. Não pule para as mais fáceis. Pule linhas cujo status não seja 'A fazer'.
2. Trabalhe em ciclos curtos: no máximo ~6 resumos consecutivos por vez, listando antes quais IDs do seu sublote ainda não têm arquivo. Isso evita estourar o contexto; se a sessão cair, retome pulando os IDs que já têm arquivo.
3. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO: um arquivo Sxxxx__AGENTE.md por atividade, em UTF-8, no formato exato da seção 11 do INSTRUCOES.md (cabeçalho com id, agente, matéria, aula, trecho, páginas lidas; seções '# ANALÍTICO', '# SINTÉTICO', '# NOTAS'). Confira com: python verificar_resumos.py <pasta> --indice INDICE-RESUMOS.csv, e corrija os erros ANTES de passar ao próximo. Nunca acumule resumos para salvar no fim.
4. Leia o trecho INTEIRO antes de escrever; cubra todos os assuntos da coluna 'Atividade (assuntos do trecho)'; respeite o 'Alvo máx. (palavras)' (teto de ~20 min de leitura; não encha, o tamanho é o que o conteúdo pedir; mínimo 250 palavras). Figuras do material: descarte (salvo se forem a fonte da informação); tabelas: aproveite só o que acrescentar informação.
5. ORIGINALIDADE: o material é protegido. Escreva com as SUAS palavras; nenhuma sequência de 10 palavras iguais ao PDF. Não cite 'a aula', 'o PDF', 'o professor'. Não invente: o que não conseguir confirmar (artigo, número, data) fica FORA do resumo e vai em '# NOTAS'.
6. ENTREGA POR SUBLOTE (não espere o lote inteiro): ao terminar um sublote, monte a pasta resumos_AGENTE_SUBLOTE (ex.: resumos_EXT-L6-A_L6-01) só com os arquivos .md do sublote + RELATORIO_AGENTE.md (sublote recebido; IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico), rode a autoverificação e compacte em .zip. Não renomeie nem altere arquivos já entregues; não altere o índice.
7. Qualidade: antes de salvar, releia como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). A entrega será auditada por amostragem: 5 resumos sorteados por agente serão conferidos contra o PDF; resumos fora do padrão voltam para refação.

Ao final, devolva todos os .zip (um por sublote) e a lista do que ficou pendente, se algo ficou.
```
