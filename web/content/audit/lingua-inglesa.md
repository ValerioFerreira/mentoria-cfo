# Auditoria — Língua Inglesa (a00–a06 + c01)

## Escopo auditado
- 7 aulas do Estratégia (996 págs.), varridas página a página com `--heads`; trechos suspeitos lidos com `--pages`. Complemento autoral `c01` (`content/complements/ing-estruturas-complementares.md`) revisto por inteiro.
- Edital (Anexo II, 2º Ten.): itens 1, 2 e 3 (3 desdobrado em 15 subitens; tempos verbais em 12, modais em 2).

## Números
| | Antes | Depois |
|---|---|---|
| Págs. de Teoria (T) | 313 | 278 |
| Trechos de Teoria | 21 | 23 (7–17 págs.; 0 acima de 17; 0 cortes no meio de tópico) |
| Págs. comentadas (C) | 517 | 515 (−108 de listas duplicadas em a00 e +20 de resoluções embutidas em a02/a03) |

## Correções (`content/overrides/lingua-inglesa.json`)
**Resoluções de prova dentro da teoria → C** (blocos ≥ 5 págs. só de questões comentadas, que inflavam a Teoria):
- a03 11-18 ("Como esse assunto pode ser cobrado em uma prova?" — phrasal verbs) e a03 36-42 ("Como os verbos modais podem ser cobrados em provas?").
- a02 33-37 (questões de advérbios logo após 2.7 Adjuncts).
- Mantidos como T, por decisão: blocos curtos (1–4 págs.) de exercícios resolvidos inseridos no meio do tópico (a00 14-16/22-23/26-31, a01 vários, a04, a05 17-18/22-23/35-36/39-41, a06 9-12/30-33). São exemplos resolvidos da própria explicação; tirá-los fragmentaria a teoria (ex.: a00 deixaria um trecho de 2 págs.).
- As seções principais "Questões Comentadas e Textos Traduzidos" já estavam todas como C.

**Listas de questões sem comentário** (repetem as questões já comentadas): a00 125-145 estava como C (dobrava a Fixação e a incidência da aula) → L, gabarito 146 → K. Em a01, a03, a04, a05 e a06 as listas estavam inteiras como K → L + K só na página do gabarito (a02 148 → K).

**Glossário de Termos Policiais** (a06 129-142) virava um trecho de Teoria de 15 págs.: é glossário de consulta de termos policiais (fora do perfil bombeiro) → S; pág. 143 em branco → B.

**Divisão pedagógica (`cuts`)**, sempre em início de tópico:
- a01 [20, 33, 46, 58]: Frases+Substantivos (3-19) · Genitivo+Artigos (20-32) · Pronomes pessoais→interrogativos (33-45) · Relativos+Indefinidos (46-57) · Preposições (58-70). Antes Pronomes era cortado no meio (36/37) e Indefinidos também (53/54).
- a02 [10, 24]: Conjunções (3-9, 7 p., assunto autônomo e base das adverbiais) · Adjetivos (10-23) · Advérbios (24-32) · Afixos+Funções comunicativas (38-48). Antes os adjetivos ficavam em dois trechos e os graus junto com advérbios.
- a04 [12, 24]: um trecho por tempo (Presente 3-11, Passado 12-23, Futuro 24-32). Antes misturava presente e metade do passado.
- a05 [12, 25, 37]: Contínuos (3-11) · Perfeitos (12-24) · Voz passiva (25-36) · Imperativo+Subjuntivo (37-43). Antes a voz passiva era partida em dois trechos.
- a03 ficou com Verbos frasais (3-10) e Auxiliares+Modais (19-35, 17 p.) após a retirada das resoluções.

**Falsos subtítulos removidos** (rótulos de mapa mental/figura): a02 p. 22 (MAPA MENTAL, Superlativo, Comparativo, Superioridade, Adjetivo); a03 p. 4; a05 p. 16-17; a06 p. 21.

**Edital da aula a06: partial → yes.** A aula traz question tags, infinitivo × gerúndio, condicionais, relativas, quantificadores e conectivos (itens do edital) além de idioms (vocabulário, item 2). O "partial" cortava pela metade a incidência de uma aula com itens centrais. A brevidade desses tópicos é compensada pelo c01.

## Cobertura do edital (resumo; detalhe em `content/edital/lingua-inglesa.json`)
| Item | Status | Onde |
|---|---|---|
| 1 Interpretação de gêneros textuais | partial | a00 17-33, a02 45-48 + prática em todas as aulas; não há seção sobre gêneros |
| 2 Vocabulário | covered | a00 9-16 (cognatos), a06 3-12 (idioms), a02 38-44 (afixos) |
| Substantivos (plural, contáveis) | covered | a01 8-24; a06 22-27 |
| Adjetivos / comparativo e superlativo | covered | a02 10-23 |
| Advérbios | covered | a02 24-32 |
| Preposições | covered | a01 58-70 |
| Artigos a/an/the | covered | a01 25-32 |
| Pronomes personal/object/demonstrative/possessive/reflexive | covered | a01 33-44 |
| Phrasal verbs | covered | a03 3-10 |
| Present simple · past simple · future simple | covered | a04 3-11 · 12-23 · 24-32 |
| Present/past/future continuous | covered | a05 3-8 |
| Present perfect · past perfect · future perfect | covered | a05 12-18 · 19-20 · 20-23 |
| **Present perfect continuous** | **complement** | não existe no Estratégia → c01 §6.1 (novo) |
| **Past perfect continuous** | **complement** | não existe no Estratégia → c01 §6.2 (novo) |
| Future perfect continuous | partial | a05 p. 24 (só afirmativa) + c01 §6.3 (novo) |
| Modais can…need | covered | a03 24-35 (+ quadro de formas em c01 §7.2) |
| **Had better** | **complement** | nenhuma ocorrência no material → c01 §7.1 (novo) |
| Voz ativa e passiva | covered | a05 25-36 |
| Orações adverbiais (7 tipos) | complement | a02 4-5 (tabela curta) + a06 28-33; c01 §1 |
| Condicionais zero/1/2/3/mista | complement | a06 40-42 (2 págs.); c01 §2 |
| Relativas defining/non-defining | complement | a01 46-51, a06 42-43; c01 §3 |
| Padrões verbais to-inf / bare / gerund | complement | a06 38-39, a05 33-35 (causativas); c01 §4 |
| Question tags | complement | a06 34-35; c01 §5 |

## Complemento c01 — avaliação e alterações
A lacuna `ing-estruturas` está confirmada nos PDFs (adverbiais só como tabela de conjunções; condicionais e relativas com ~1 pág. cada; padrões verbais e tags com 2 págs.). O c01 já cobria bem as 5 estruturas, com profundidade adequada à AOCP (conectivo certo, tempo verbal em cada oração, pegadinhas). Mas faltavam três itens que o edital cita nominalmente e o Estratégia não ensina. **Alterações feitas (texto original):**
1. **Novo §6, tempos perfeitos contínuos:** present perfect continuous e past perfect continuous (usos e as 3 formas, simple × continuous, verbos de estado, "há/faz... que"); future perfect continuous com negativa e interrogativa (o a05 só dá a afirmativa e diz que o tempo vem "sempre" com *for*, o que é exagero); quadro dos 12 tempos do edital nas 3 formas.
2. **Novo §7, *had better*** (formas, ✘ *had better to*, *'d better* × *'d rather*, *should* × *had better*) e quadro de formas negativas e interrogativas dos 10 modais do edital (*mustn't* × *don't have to*).
3. **Correções e reforços:** *once* = "assim que" (estava "uma vez que", que soa causal); conectivos de lugar sem *somewhere* (não é conjunção); *whose* também para coisas; *which* retomando a oração inteira; alerta *whom* ≠ "cujo"; verbos de percepção + -ing (ação em andamento); *allow/advise/permit/recommend* com e sem objeto; tags de *this/that/these/those*; Pegadinha 12 reescrita (com *have* principal o padrão atual é *don't you?*; *haven't you?* é britânico tradicional).
4. Front matter `subtitle`, a introdução, a seção "como aparece em prova" e o resumo foram atualizados. O texto passou de ~3.350 para ~5.200 palavras: o PDF deve crescer de 8 para ~12-13 págs. e talvez virar 2 trechos.

## Pendências / validação humana
- **Conflitos edital × PDF (erros do Estratégia que o aluno lê):** a06 p. 42 admite *that* em relativa non-defining e traduz *whom* como "cujo"; a06 p. 39 lista *advise* entre verbos só com gerúndio; a05 p. 24 diz que o future perfect continuous vem "sempre" com *for*. O c01 dá a regra correta. Pode valer um bizu/aviso na atividade.
- **Gêneros textuais (item 1):** sem seção teórica. Fica `partial` (aprendido na prática). Decidir se vale uma seção curta no c01 (tipos de texto mais usados pela AOCP e como identificá-los).
- **Exercícios curtos embutidos na teoria** ficaram T (decisão de critério: ≥ 5 págs. contínuas de resolução → C). Se o orquestrador quiser um critério mais estrito, os candidatos são a00 26-31 (6 págs., mas é o próprio exemplo de leitura não verbal) e a06 9-12.
- **a06 Discurso direto/indireto e Numerais** (13-21): não estão explícitos no edital. Mantidos (curtos, ligados a tempos e vocabulário).
- O peso `weight: 0.15` do c01 não foi alterado. Com o conteúdo ~55% maior, talvez convenha revê-lo.

## Pedidos ao orquestrador
1. Rodar `build_catalog.py` e depois `build_complements.py` (o c01 mudou; regenerar o PDF `web/public/complementos/ing-estruturas-complementares.pdf`, a contagem de páginas e os trechos do c01) e o `npx prisma db seed`.
2. Os `"where"` do c01 no mapa do edital estão sem páginas (o PDF ainda não foi regenerado). Calcular depois do build, pelas seções §1–§7.
3. Avaliar se o `weight` do c01 deve subir (conteúdo maior, cobre 3 itens nominais a mais do edital).
