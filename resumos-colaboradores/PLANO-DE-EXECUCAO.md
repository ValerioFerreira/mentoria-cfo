# Plano de execução dos resumos — divisão em 6 lotes

Gerado a partir de `INDICE-RESUMOS.xlsx` (colunas **Lote** e **Sublote (20)**). 850 atividades a fazer, 47 já feitas. Cada lote tem disciplinas inteiras (um agente fica com o mesmo vocabulário e as mesmas aulas do começo ao fim).

## Regras comuns a todos os agentes

1. **Fase 1 primeiro**: os lotes 1 a 6 só têm assuntos do edital do CFO CBMPE (714 atividades). **Fase 2** (Atualidades, Raciocínio Lógico, História de PE: 136 atividades, fora do edital do CFO CBMPE) só começa depois que todos os lotes da Fase 1 estiverem entregues; será dada a quem terminar primeiro.
2. Dentro do lote, **seguir a ordem dos IDs** (prioridade: comuns aos 4 concursos primeiro, depois por peso na prova).
3. **Salvar cada resumo assim que concluído** (um arquivo `Sxxxx__AGENTE.md` por atividade) e **entregar por sublote** (~20 resumos), nunca só no fim do lote.
4. Seguir `INSTRUCOES.md` à risca (formato, identificação do agente, relatório, autoverificação com `verificar_resumos.py`).
5. Retomada: se a sessão cair, o agente pula os IDs que já têm arquivo na pasta.

## Quadro resumo

| Lote | Quem | Disciplinas | Atividades | Palavras-alvo (teto) | Págs. do material | Sublotes | IDs (primeiro–último) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | **Claude (interno)** — agente `CLAUDE-L1` | Direito Constitucional + Direito Administrativo | 149 | 237.600 | 1.603 | 8 | S0023–S0561 |
| 2 | Colaborador externo | Informática + Língua Inglesa | 109 | 183.900 | 1.286 | 6 | S0087–S0357 |
| 3 | Colaborador externo | Biologia + Língua Portuguesa | 111 | 198.400 | 1.384 | 6 | S0028–S0563 |
| 4 | **Claude (interno)** — agente `CLAUDE-L4` | Estatística + Direito Penal Militar | 112 | 178.050 | 1.229 | 6 | S0254–S0565 |
| 5 | Colaborador externo | Matemática + Física | 117 | 200.050 | 1.410 | 6 | S0566–S0758 |
| 6 | Colaborador externo | Química + Língua Espanhola | 116 | 198.000 | 1.387 | 6 | S0255–S0761 |
| F2-A | A definir (Fase 2) | Atualidades | 63 | 105.150 | 735 | 4 | S0835–S0897 |
| F2-B | A definir (Fase 2) | Raciocínio Lógico + História de Pernambuco | 73 | 125.550 | 865 | 4 | S0762–S0834 |

Lotes 1 e 4 ficam com o Claude (2 agentes em paralelo); **lotes 2, 3, 5 e 6 são para os colaboradores externos**. O lote 1 concentra os assuntos de maior prioridade (começa em S0023) e o de Direito exige maior precisão, por isso ficou com o Claude.

## Lote 1 — Direito Constitucional + Direito Administrativo

**Executor:** Claude, agente `CLAUDE-L1` (pasta de entrega `resumos-colaboradores/entregas/resumos_CLAUDE-L1_<sublote>/`).

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L1-01 | 20 | S0023–S0100 | Direito Constitucional | 37250 |
| L1-02 | 20 | S0101–S0146 | Direito Constitucional | 33000 |
| L1-03 | 20 | S0148–S0180 | Direito Constitucional | 29850 |
| L1-04 | 20 | S0181–S0256 | Direito Administrativo, Direito Constitucional | 26150 |
| L1-05 | 20 | S0279–S0353 | Direito Administrativo | 36950 |
| L1-06 | 20 | S0354–S0425 | Direito Administrativo | 31050 |
| L1-07 | 20 | S0426–S0508 | Direito Administrativo | 31950 |
| L1-08 | 9 | S0520–S0561 | Direito Administrativo | 11400 |

## Lote 2 — Informática + Língua Inglesa

**Executor:** colaborador externo. Mensagem sugerida para enviar junto com `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx` e a pasta de PDFs:

> Siga o documento INSTRUCOES.md. Escolha um identificador próprio (ex.: `EXT-L2`) e use-o em tudo. Execute o **Lote 2** do INDICE-RESUMOS (filtre a coluna *Lote* = 2; 109 atividades), um sublote por vez, na ordem dos IDs, a partir do sublote **L2-01**. Salve cada resumo ao concluir e devolva uma pasta por sublote.

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L2-01 | 20 | S0087–S0127 | Informática | 37200 |
| L2-02 | 20 | S0132–S0185 | Informática | 36600 |
| L2-03 | 20 | S0186–S0216 | Informática | 33400 |
| L2-04 | 20 | S0217–S0240 | Informática | 30450 |
| L2-05 | 20 | S0241–S0290 | Informática, Língua Inglesa | 33050 |
| L2-06 | 9 | S0291–S0357 | Língua Inglesa | 13200 |

## Lote 3 — Biologia + Língua Portuguesa

**Executor:** colaborador externo. Mensagem sugerida para enviar junto com `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx` e a pasta de PDFs:

> Siga o documento INSTRUCOES.md. Escolha um identificador próprio (ex.: `EXT-L3`) e use-o em tudo. Execute o **Lote 3** do INDICE-RESUMOS (filtre a coluna *Lote* = 3; 111 atividades), um sublote por vez, na ordem dos IDs, a partir do sublote **L3-01**. Salve cada resumo ao concluir e devolva uma pasta por sublote.

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L3-01 | 20 | S0028–S0062 | Língua Portuguesa | 38650 |
| L3-02 | 20 | S0063–S0249 | Língua Portuguesa | 35550 |
| L3-03 | 20 | S0253–S0420 | Biologia | 35600 |
| L3-04 | 20 | S0428–S0510 | Biologia | 35900 |
| L3-05 | 20 | S0512–S0546 | Biologia | 35150 |
| L3-06 | 11 | S0547–S0563 | Biologia | 17550 |

## Lote 4 — Estatística + Direito Penal Militar

**Executor:** Claude, agente `CLAUDE-L4` (pasta de entrega `resumos-colaboradores/entregas/resumos_CLAUDE-L4_<sublote>/`).

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L4-01 | 20 | S0254–S0316 | Direito Penal Militar, Estatística | 30300 |
| L4-02 | 20 | S0317–S0393 | Direito Penal Militar, Estatística | 28850 |
| L4-03 | 20 | S0394–S0433 | Direito Penal Militar, Estatística | 34400 |
| L4-04 | 20 | S0434–S0463 | Estatística | 38100 |
| L4-05 | 20 | S0464–S0513 | Estatística | 32100 |
| L4-06 | 12 | S0514–S0565 | Direito Penal Militar, Estatística | 14300 |

## Lote 5 — Matemática + Física

**Executor:** colaborador externo. Mensagem sugerida para enviar junto com `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx` e a pasta de PDFs:

> Siga o documento INSTRUCOES.md. Escolha um identificador próprio (ex.: `EXT-L5`) e use-o em tudo. Execute o **Lote 5** do INDICE-RESUMOS (filtre a coluna *Lote* = 5; 117 atividades), um sublote por vez, na ordem dos IDs, a partir do sublote **L5-01**. Salve cada resumo ao concluir e devolva uma pasta por sublote.

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L5-01 | 20 | S0566–S0591 | Física, Matemática | 38600 |
| L5-02 | 20 | S0592–S0619 | Física, Matemática | 36000 |
| L5-03 | 20 | S0620–S0656 | Física, Matemática | 35750 |
| L5-04 | 20 | S0658–S0687 | Física, Matemática | 34400 |
| L5-05 | 20 | S0689–S0717 | Matemática | 31900 |
| L5-06 | 17 | S0718–S0758 | Matemática | 23400 |

## Lote 6 — Química + Língua Espanhola

**Executor:** colaborador externo. Mensagem sugerida para enviar junto com `INSTRUCOES.md`, `INDICE-RESUMOS.xlsx` e a pasta de PDFs:

> Siga o documento INSTRUCOES.md. Escolha um identificador próprio (ex.: `EXT-L6`) e use-o em tudo. Execute o **Lote 6** do INDICE-RESUMOS (filtre a coluna *Lote* = 6; 116 atividades), um sublote por vez, na ordem dos IDs, a partir do sublote **L6-01**. Salve cada resumo ao concluir e devolva uma pasta por sublote.

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| L6-01 | 20 | S0255–S0337 | Língua Espanhola | 38450 |
| L6-02 | 20 | S0338–S0581 | Língua Espanhola, Química | 34350 |
| L6-03 | 20 | S0587–S0636 | Química | 38150 |
| L6-04 | 20 | S0640–S0688 | Química | 36250 |
| L6-05 | 20 | S0690–S0734 | Química | 33650 |
| L6-06 | 16 | S0737–S0761 | Química | 17150 |

## Lote F2-A — Atualidades

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| F2-A-01 | 20 | S0835–S0854 | Atualidades | 40000 |
| F2-A-02 | 20 | S0855–S0874 | Atualidades | 34100 |
| F2-A-03 | 20 | S0875–S0894 | Atualidades | 28050 |
| F2-A-04 | 3 | S0895–S0897 | Atualidades | 3000 |

## Lote F2-B — Raciocínio Lógico + História de Pernambuco

| Sublote | Atividades | IDs | Disciplinas / aulas | Palavras-alvo |
| --- | --- | --- | --- | --- |
| F2-B-01 | 20 | S0762–S0781 | Raciocínio Lógico | 39300 |
| F2-B-02 | 20 | S0782–S0801 | Raciocínio Lógico | 39150 |
| F2-B-03 | 20 | S0802–S0821 | Raciocínio Lógico | 30150 |
| F2-B-04 | 13 | S0822–S0834 | História de Pernambuco, Raciocínio Lógico | 16950 |

## Como o Claude executa os lotes 1 e 4 (2 agentes em paralelo)
- Dois fluxos independentes, um por lote, em disciplinas diferentes (nenhum arquivo em comum).
- Cada chamada de agente faz **6 resumos consecutivos** (≈ 6 × 10 mil tokens de leitura do material), na ordem dos IDs do lote, e já devolve para um novo ciclo. Isso evita estourar o contexto e limita a perda se uma sessão cair.
- Cada resumo é gravado em arquivo **assim que concluído**: `resumos-colaboradores/entregas/resumos_<AGENTE>_<sublote>/Sxxxx__<AGENTE>.md`, e conferido com `verificar_resumos.py` antes de passar ao próximo. Nada fica na memória para ser salvo no fim.
- Texto-fonte: `pipeline/summary_source.py <trecho>` (protegido; só leitura, nunca copiar).
- Depois de cada ciclo o orquestrador roda `pipeline/import_agent_summaries.py` (grava em `content/summaries`, rejeita o que falhar, atualiza a amostra de 5 por agente). Retomada: o fluxo pula IDs que já têm arquivo.
- Estimativa: lote 1 = 149 atividades (≈ 25 ciclos); lote 4 = 112 (≈ 19 ciclos).

## Depois da devolução
1. Reunir as pastas devolvidas e rodar `pipeline/.venv/Scripts/python pipeline/import_agent_summaries.py <pasta-mãe>`.
2. Ler `resumos-colaboradores/amostras/<AGENTE>.md` (5 resumos sorteados por agente) e avaliar contra o PDF; agente reprovado tem os resumos devolvidos para refação (`rejeitados/` lista os que falharam na validação automática).
3. `pipeline/apply_synthetic.py` e `npx prisma db seed`.
