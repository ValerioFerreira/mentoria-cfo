# Auditoria estrutural — Biologia (a00–a17)

Método: varredura de todas as páginas de cada aula (`inspect_aula.py --heads`), leitura de páginas suspeitas, busca por termos do edital em toda a disciplina e medição de sobreposição textual (8-gramas) entre as 18 aulas. Nada foi copiado dos PDFs. Não há complemento autoral nem lacuna aberta de Biologia em `content/complements`/`gaps.json` (a única entrada, `bio-biotecnologia`, está resolvida como falso alarme).

## Números
- Aulas: 18 · Páginas de teoria: 895 → 828 (−67: a02 −21 EXTRA, a13 −43 líquido (139 → 96: sem resumo, exercícios e gabarito; págs. 6-8 passam a teoria), a14 −2 EXTRA, a05 −2 exercícios; a16 +1) · Trechos: 63 → 68. Maior trecho: 17 págs. (nenhum acima do teto).

## Correções feitas (`content/overrides/biologia.json`)
| Aula | Correção | Motivo |
|---|---|---|
| a00 | corte na pág. 57 | Mitose começava no fim do trecho de "tipos de células" (págs. 55-68). Agora: organelas 40-56 / mitose 57-68. |
| a01 | cortes 19 e 35 | Trechos antigos misturavam glândulas (epitelial) com conjuntivo e ossos com músculo/nervoso. Agora: epitelial 3-18 / conjuntivo+cartilagem+osso 19-34 / muscular+nervoso 35-44. |
| a02 | págs. 4-24 → EXTRA | Repetem a Aula 03 (sobreposição de 60 a 99% por página). Ficam mutações, Mendel, heredogramas, probabilidade, identificação por DNA, populações e OGM. |
| a05 | págs. 17-18 → C | "Exercícios de fixação" + resolução no meio da teoria. |
| a06 | cortes 17 e 47 | Antigos trechos cortavam no meio de "ossos da cabeça". Agora: ossos/cartilagens 4-16, axial 17-30, coluna 31-46, apendicular 47-56, pelve/membros inferiores 57-70. |
| a07 | cortes 23 e 36 | Separar articulações (3-22), fisiologia muscular (23-35) e anatomia muscular (36-51); antes o trecho 2 misturava joelho/quadril com músculos. |
| a08 | cortes 22 e 32 | Antes 18-34 juntava ABO/coagulação, coração e vasos. Agora sangue / coração / vasos e circulação. |
| a09 | corte 33 | Intestino grosso estava junto com urinário e reprodutor. Agora digestório 3-32 (2 trechos) e urinário+reprodutor 33-44. |
| a10 | corte 22 | Medula, cérebro e SNP/potencial de ação viram 3 trechos autônomos (3-12, 13-21, 22-34). |
| a11 | corte 13; pág. 36 → S | Endócrino e imune estavam num trecho de 17 págs.; "7. Resumo" estava como questões. |
| a13 | páginas 1-5 F, 6-101 T, 102-108 S, 109-119 C, 120-140 L, 141-146 K, 147 B; 36 subtítulos; cortes 29, 48, 63 | O pipeline não leu o índice (sumário detectado até a pág. 8; real 2-4) e tratou tudo (inclusive 38 págs. de questões e o resumo) como teoria, com tópico errado ("3.3.4 Amonificação") em 6 de 10 trechos. Agora 8 trechos coerentes; a aula ganha Fixação (C 11 págs. + L 21). |
| a14 | págs. 55-56 → EXTRA; remove subtítulo "Estatística paramétrica…" | Estatística de dados ecológicos não está no edital de Biologia. |
| a15 | corte 30 | Protozooses (20-29) separadas de verminoses (30-41/42-50). |
| a16 | pág. 31 → T | Era B, mas contém a conduta no trauma torácico. |
| a17 | pág. 21 → C; corte 13 | Pág. 21 contém comentários de questões; teoria (carga ≈ 17) dividida em hemorragia/vias aéreas/PCR (4-12) e queimaduras (13-20). |
Aulas sem alteração: a03, a04, a12.

## Cobertura do edital (resumo; detalhe em `content/edital/biologia.json`)
- **Cobertos**: citologia, divisão celular, metabolismo, síntese proteica, tecidos animais, DNA recombinante, forense/identificação, evolução, embriologia, todos os sistemas humanos, ecologia geral (populações, interações, ciclos, biomas), problemas ambientais, conservação/SNUC/Código Florestal, primeiros socorros, IST (AIDS/sífilis), parasitoses.
- **Parciais**: bioquímica das estruturas celulares (sem capítulo de biomoléculas), diferenciação celular, origem das células, células-tronco (1 parágrafo), clonagem (só molecular), terapia gênica (1 parágrafo), classificação/diversidade, funções vitais e adaptação, biogeografia, microplásticos, tecnologias ambientais, saneamento básico, legislação de biodiversidade, doenças da população brasileira, desenvolvimento sustentável.
- **Lacunas reais (sem material)**: tecidos vegetais; ética em biotecnologia; biotecnologia e sustentabilidade; serviços ecossistêmicos; legislação da água (Lei 9.433); pobreza/desenvolvimento humano; indicadores sociais e IDH; Saúde Única; drogas; obesidade; saúde mental.
- **Biotecnologia (confirmação da reanálise)**: NÃO é lacuna em técnicas, OGM, fármacos (insulina, vacinas) e DNA forense (a02 págs. 55-64, a02 73-74, a03 38-53). Mas os subitens **ética, sustentabilidade, clonagem de organismos, terapia gênica e células-tronco** têm tratamento zero ou de uma frase; vale um complemento curto único.

## Auditoria inversa (achados)
Ver `inverse` no JSON. Principais: a02 duplicada (EXTRA), a13 inteira mal classificada, a11/a16/a17 marcadores de fim errados, a05 exercícios no meio da teoria, a14 estatística fora do edital.

## Lacunas e complementos
Não há complementos de Biologia. Recomendo ao orquestrador decidir sobre (em ordem de peso provável na prova): (1) Qualidade de vida/saúde: IDH e indicadores, Saúde Única, drogas, obesidade, saúde mental — 5 itens do bloco 4, sem nenhuma página; (2) Biotecnologia: ética, clonagem e células-tronco, terapia gênica, biotecnologia e sustentabilidade; (3) Ambiente: serviços ecossistêmicos, saneamento básico, legislação da água e da biodiversidade, microplásticos; (4) Identidade dos seres vivos: classificação (reinos/grupos) e tecidos vegetais. Nenhum complemento foi criado por mim.

## Pendências
- Aula 13: o pipeline calcula `tocMax = 8` (real 4). Títulos nas págs. 6-8 são ignorados e o trecho s01 (págs. 6-15) fica sem tópico inicial ("startTopic": null). Correção de código fica a cargo do orquestrador (usar o último sumário contíguo).
- a02 EXTRA: a Aula 03 traz a mesma matéria, mas só depois de Mendel na ordem numérica; o planejador pode apontar a02 → a03 para "síntese proteica". Validar se o aluno prefere essa ordem.
- a06: profundidade anatômica (vértebras, ossos do pé) acima do que costuma cair em 5 questões — decisão humana se mantém "Essencial" completo.
- a05 pág. 23 e exercícios inline em a00 (págs. 12, 24, 54, 81) mantidos como T (misturam questão e texto).
- Conferência de textos: afirmações "sem material" vêm de buscas por termos + leitura de páginas candidatas; recomendável uma checagem humana rápida antes de encomendar complementos.
