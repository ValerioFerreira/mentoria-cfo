# Prompts para os colaboradores (2 colaboradores × 2 agentes em paralelo = lotes 2, 3, 5 e 6)

Os colaboradores têm **acesso ao projeto**: não há pacote de arquivos a enviar. Cada colaborador recebe **um prompt** e, a partir dele, cria **2 agentes em paralelo**, cada um responsável por **um lote** (todos os sublotes dele, do primeiro ao último).

| Colaborador | Agente (identificador) | Lote | Disciplinas | Atividades | Sublotes |
| --- | --- | --- | --- | --- | --- |
| **1** | `EXT-L2` | 2 | Informática + Língua Inglesa | 109 | L2-01 a L2-06 |
| **1** | `EXT-L3` | 3 | Biologia + Língua Portuguesa | 111 | L3-01 a L3-06 |
| **2** | `EXT-L5` | 5 | Matemática + Física | 117 | L5-01 a L5-06 |
| **2** | `EXT-L6` | 6 | Química + Língua Espanhola | 116 | L6-01 a L6-06 |

(Os lotes 1 e 4 — Direito Constitucional/Administrativo e Estatística/Direito Penal Militar — ficam com os agentes internos `CLAUDE-L1` e `CLAUDE-L4`. Atualidades, Raciocínio Lógico e História de PE são a Fase 2 e serão passados depois, a quem terminar primeiro.)

## Onde estão os arquivos (raiz do projeto: `C:\Users\Administrador\Documents\Projetos\CFO-BM`)

| O quê | Caminho |
| --- | --- |
| Regra de execução (método, estilo, formato do arquivo, originalidade) | `resumos-colaboradores/INSTRUCOES.md` |
| Índice de atividades (ID, trecho, assuntos, páginas, alvo, Lote, Sublote, status) | `resumos-colaboradores/INDICE-RESUMOS.xlsx` e `.csv` (e `indice.json`) |
| Plano de execução (lotes e sublotes) | `resumos-colaboradores/PLANO-DE-EXECUCAO.md` |
| Lista das próximas atividades pendentes do lote | `python pipeline/next_summaries.py --lot N --agent EXT-LN --n 6` |
| Texto-fonte de um trecho (protegido) | `python pipeline/summary_source.py <trecho>` (PDFs originais em `docs/`, só para consulta de figuras) |
| Autoverificação de formato/tamanho | `python resumos-colaboradores/verificar_resumos.py <pasta> --indice resumos-colaboradores/INDICE-RESUMOS.csv` |
| Validação de originalidade (sem gravar) | `python pipeline/import_agent_summaries.py <pasta> --dry-run` |
| **Onde gravar os resumos** | `resumos-colaboradores/entregas/resumos_<AGENTE>_<SUBLOTE>/Sxxxx__<AGENTE>.md` |

Python do projeto: `pipeline/.venv/Scripts/python` (defina `PYTHONIOENCODING=utf-8` no Windows).

## Diretrizes de execução (valem para os dois agentes de cada colaborador)
1. **Seguir o `INSTRUCOES.md` à risca.** A única diferença: como os agentes têm acesso ao projeto, a **entrega não é `.zip`**: os arquivos ficam na pasta `entregas/` indicada acima (a seção 12 do documento vale só para quem não tem acesso).
2. **Dois agentes em paralelo, um por lote**, cada um com identificador próprio (`EXT-L2`, `EXT-L3`…), usado no nome dos arquivos, no cabeçalho (`agente:`) e na pasta. Os lotes são disjuntos: nenhum agente toca em atividade de outro lote.
3. **Ordem de prioridade**: o comando `next_summaries.py` já devolve as pendentes na ordem dos IDs. Não pular para as mais fáceis.
4. **Ciclos curtos**: cada ciclo faz as **6 próximas** pendentes (`--n 6`), depois recomeça com um novo ciclo até o lote acabar. Evita estourar o contexto; se a sessão cair, o comando pula automaticamente o que já tem arquivo.
5. **Salvar cada resumo assim que concluído** (um arquivo por atividade) e conferi-lo com a autoverificação e com o `--dry-run` **antes** de passar ao próximo. Nunca acumular para salvar no fim.
6. **Originalidade**: o texto-fonte é protegido (marca d'água). Escrever com as próprias palavras; nenhuma sequência de 10 palavras igual ao material (atenção a artigos de lei, ementas, definições e exemplos citados).
7. **Não inventar**: o que não puder ser confirmado (artigo, número, data) fica fora do texto e vai em `# NOTAS`. Figuras sem texto extraído: reconstruir só se tiver certeza e registrar em `# NOTAS`.
8. **Escopo do que cada agente pode mexer**: só criar os `.md` dentro de `resumos-colaboradores/entregas/resumos_<AGENTE>_*`. **Não** editar nenhum outro arquivo do projeto, **não** fazer commit/push, **não** rodar o import de verdade (sem `--dry-run`), `apply_synthetic.py` nem seed: quem importa e faz a análise amostral (5 resumos sorteados por agente, conferidos contra o PDF) é o responsável pelo projeto.
9. Ao fim de cada sublote, criar `RELATORIO_<AGENTE>_<SUBLOTE>.md` na pasta do sublote (IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico).

---

## PROMPT — COLABORADOR 1 (lotes 2 e 3)

```text
Você é responsável por produzir resumos de estudo do projeto CFO-BM (raiz: C:\Users\Administrador\Documents\Projetos\CFO-BM; você tem acesso a ele). Crie DOIS agentes trabalhando em paralelo, um para cada lote abaixo, cada um com o seu identificador. Os lotes são disjuntos.

- Agente EXT-L2: LOTE 2 (Informática + Língua Inglesa; 109 atividades; sublotes L2-01 a L2-06).
- Agente EXT-L3: LOTE 3 (Biologia + Língua Portuguesa; 111 atividades; sublotes L3-01 a L3-06).

Passe a cada agente o prompt "PROMPT DO AGENTE" abaixo, trocando N pelo número do lote e AGENTE pelo identificador (EXT-L2 ou EXT-L3).

PROMPT DO AGENTE:
Você é o agente de resumos AGENTE do projeto CFO-BM (raiz: C:\Users\Administrador\Documents\Projetos\CFO-BM). Sua tarefa: escrever todos os resumos pendentes do LOTE N, em ciclos de 6, seguindo à risca o documento resumos-colaboradores/INSTRUCOES.md (leia-o INTEIRO antes de começar: método, estilo, formato exato do arquivo, originalidade, tabelas/figuras, identificação do agente). Exceção ao INSTRUCOES.md: a entrega NÃO é .zip; os arquivos ficam em resumos-colaboradores/entregas/ (abaixo). Defina PYTHONIOENCODING=utf-8 e use o Python do projeto (pipeline/.venv/Scripts/python).

CADA CICLO:
1. Liste as próximas pendentes: pipeline/.venv/Scripts/python pipeline/next_summaries.py --lot N --agent AGENTE --n 6 (mostra ID, trecho, páginas, alvo de palavras, assuntos e o caminho exato onde gravar). Faça SOMENTE essas, NA ORDEM (é a ordem de prioridade). Se não houver pendentes, o lote acabou: pare e reporte.
2. Para cada atividade, leia o texto-fonte COMPLETO do trecho: pipeline/.venv/Scripts/python pipeline/summary_source.py <trecho> (use --max-chars 60000 se preciso). O texto é protegido (marca d'água): entenda e escreva com as SUAS palavras; nenhuma sequência de 10 palavras igual ao material (atenção a artigos de lei, ementas, definições e exemplos). Todos os assuntos da coluna "assuntos" devem aparecer. Trechos cNN são complementos autorais do MentorIA: resuma, não copie. Se uma figura/tabela vier sem texto, consulte o PDF em docs/ e reconstrua só se tiver certeza (registre em NOTAS).
3. Escreva # ANALÍTICO (até o alvo de palavras; mínimo 250; tamanho conforme o conteúdo), # SINTÉTICO (6–12 pontos, 110–320 palavras) e # NOTAS no formato da seção 11 do INSTRUCOES.md, com o cabeçalho completo (id, agente: AGENTE, materia, aula, trecho, paginas_lidas...). Use a ferramenta de escrever arquivos (não heredoc no shell). Respeite o alvo desde a primeira versão.
4. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO, no caminho que next_summaries.py indicou: resumos-colaboradores/entregas/resumos_AGENTE_<SUBLOTE>/Sxxxx__AGENTE.md. Em seguida confira: pipeline/.venv/Scripts/python resumos-colaboradores/verificar_resumos.py <pasta> --indice resumos-colaboradores/INDICE-RESUMOS.csv (o aviso de falta de RELATORIO pode ser ignorado até o fim do sublote) e pipeline/.venv/Scripts/python pipeline/import_agent_summaries.py <pasta> --dry-run (valida originalidade e impressão digital SEM gravar). Corrija todos os erros do arquivo antes de passar ao próximo. Nunca deixe resumos prontos só na memória para salvar no fim.
5. Releia cada um como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). Dúvida sobre artigo, número ou data: fora do texto, em # NOTAS.
6. Ao concluir o último resumo de um sublote, crie RELATORIO_AGENTE_<SUBLOTE>.md na pasta dele (IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico). Depois volte ao passo 1 (novo ciclo) até acabarem as pendentes do lote.

REGRAS: só crie arquivos .md em resumos-colaboradores/entregas/resumos_AGENTE_*. NÃO edite nenhum outro arquivo do projeto, NÃO faça commit/push, NÃO rode o import de verdade (sem --dry-run), apply_synthetic.py nem seed. Atividades de outros lotes não são suas. Cada resumo será auditado por amostragem (5 sorteados por agente, conferidos contra o PDF); resumos fora do padrão voltam para refação.
Ao final (ou se parar por limite de sessão), responda de forma CURTA: sublotes concluídos, IDs entregues, IDs não feitos (com motivo) e problemas do material. Não cole o conteúdo dos resumos.
```

---

## PROMPT — COLABORADOR 2 (lotes 5 e 6)

```text
Você é responsável por produzir resumos de estudo do projeto CFO-BM (raiz: C:\Users\Administrador\Documents\Projetos\CFO-BM; você tem acesso a ele). Crie DOIS agentes trabalhando em paralelo, um para cada lote abaixo, cada um com o seu identificador. Os lotes são disjuntos.

- Agente EXT-L5: LOTE 5 (Matemática + Física; 117 atividades; sublotes L5-01 a L5-06).
- Agente EXT-L6: LOTE 6 (Química + Língua Espanhola; 116 atividades; sublotes L6-01 a L6-06).

Passe a cada agente o prompt "PROMPT DO AGENTE" abaixo, trocando N pelo número do lote e AGENTE pelo identificador (EXT-L5 ou EXT-L6).

PROMPT DO AGENTE:
Você é o agente de resumos AGENTE do projeto CFO-BM (raiz: C:\Users\Administrador\Documents\Projetos\CFO-BM). Sua tarefa: escrever todos os resumos pendentes do LOTE N, em ciclos de 6, seguindo à risca o documento resumos-colaboradores/INSTRUCOES.md (leia-o INTEIRO antes de começar: método, estilo, formato exato do arquivo, originalidade, tabelas/figuras, identificação do agente). Exceção ao INSTRUCOES.md: a entrega NÃO é .zip; os arquivos ficam em resumos-colaboradores/entregas/ (abaixo). Defina PYTHONIOENCODING=utf-8 e use o Python do projeto (pipeline/.venv/Scripts/python).

CADA CICLO:
1. Liste as próximas pendentes: pipeline/.venv/Scripts/python pipeline/next_summaries.py --lot N --agent AGENTE --n 6 (mostra ID, trecho, páginas, alvo de palavras, assuntos e o caminho exato onde gravar). Faça SOMENTE essas, NA ORDEM (é a ordem de prioridade). Se não houver pendentes, o lote acabou: pare e reporte.
2. Para cada atividade, leia o texto-fonte COMPLETO do trecho: pipeline/.venv/Scripts/python pipeline/summary_source.py <trecho> (use --max-chars 60000 se preciso). O texto é protegido (marca d'água): entenda e escreva com as SUAS palavras; nenhuma sequência de 10 palavras igual ao material (atenção a artigos de lei, ementas, definições e exemplos). Todos os assuntos da coluna "assuntos" devem aparecer. Trechos cNN são complementos autorais do MentorIA: resuma, não copie. Se uma figura/tabela vier sem texto, consulte o PDF em docs/ e reconstrua só se tiver certeza (registre em NOTAS). Fórmulas em texto simples, sem LaTeX; resolva um exemplo curto quando o trecho ensina um método de cálculo.
3. Escreva # ANALÍTICO (até o alvo de palavras; mínimo 250; tamanho conforme o conteúdo), # SINTÉTICO (6–12 pontos, 110–320 palavras) e # NOTAS no formato da seção 11 do INSTRUCOES.md, com o cabeçalho completo (id, agente: AGENTE, materia, aula, trecho, paginas_lidas...). Use a ferramenta de escrever arquivos (não heredoc no shell). Respeite o alvo desde a primeira versão.
4. SALVE CADA RESUMO ASSIM QUE CONCLUÍ-LO, no caminho que next_summaries.py indicou: resumos-colaboradores/entregas/resumos_AGENTE_<SUBLOTE>/Sxxxx__AGENTE.md. Em seguida confira: pipeline/.venv/Scripts/python resumos-colaboradores/verificar_resumos.py <pasta> --indice resumos-colaboradores/INDICE-RESUMOS.csv (o aviso de falta de RELATORIO pode ser ignorado até o fim do sublote) e pipeline/.venv/Scripts/python pipeline/import_agent_summaries.py <pasta> --dry-run (valida originalidade e impressão digital SEM gravar). Corrija todos os erros do arquivo antes de passar ao próximo. Nunca deixe resumos prontos só na memória para salvar no fim.
5. Releia cada um como aluno (dá para resolver questões só com isto?) e como banca (ficou algum ponto cobrável de fora? algum erro?). Dúvida sobre artigo, número, fórmula ou data: fora do texto, em # NOTAS.
6. Ao concluir o último resumo de um sublote, crie RELATORIO_AGENTE_<SUBLOTE>.md na pasta dele (IDs entregues; IDs não feitos e motivo; problemas do material por ID; mín./média/máx. de palavras do analítico). Depois volte ao passo 1 (novo ciclo) até acabarem as pendentes do lote.

REGRAS: só crie arquivos .md em resumos-colaboradores/entregas/resumos_AGENTE_*. NÃO edite nenhum outro arquivo do projeto, NÃO faça commit/push, NÃO rode o import de verdade (sem --dry-run), apply_synthetic.py nem seed. Atividades de outros lotes não são suas. Cada resumo será auditado por amostragem (5 sorteados por agente, conferidos contra o PDF); resumos fora do padrão voltam para refação.
Ao final (ou se parar por limite de sessão), responda de forma CURTA: sublotes concluídos, IDs entregues, IDs não feitos (com motivo) e problemas do material. Não cole o conteúdo dos resumos.
```

---

## Depois da devolução (responsável pelo projeto)
1. `pipeline/.venv/Scripts/python pipeline/import_agent_summaries.py resumos-colaboradores/entregas/resumos_<AGENTE>_<SUBLOTE>` (real; rejeitados em `resumos-colaboradores/rejeitados/`).
2. Ler `resumos-colaboradores/amostras/<AGENTE>.md` (5 resumos sorteados por agente) e conferir contra o PDF.
3. `pipeline/apply_synthetic.py` e `npx prisma db seed`.
