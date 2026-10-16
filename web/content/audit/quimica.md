# Auditoria estrutural — Química (a00–a23 + c01)

## Escopo e método
- 24 aulas do Estratégia (a00–a23, 3.068 págs. de PDF) e o complemento `c01` (`quim-aplicada-complementos`).
- Varredura página a página (primeira linha útil de todas as páginas, buscas por regex em toda a disciplina), conferência dos marcadores do índice e leitura das páginas suspeitas.
- Edital lido item a item (seção "Química", itens 1.1–1.9, 2.1–2.6, 3.1–3.5, 4.1/4.3/4.6, 5 e 6). Mapa em `content/edital/quimica.json`.

## Números
| | HEAD (commit) | Depois |
|---|---|---|
| Págs. de teoria (a00–a23) | 1.040 | 896 |
| Trechos de Teoria | 87 | 78 (máx. 17 págs.; 0 violações) |

Obs.: o estado intermediário entregue pelo orquestrador (a17 já corrigida) não foi medido; a diferença total vem de (1) a04 com 56 págs. de questões como teoria, (2) páginas de "Principais pontos do tópico" dentro da teoria em quase todas as aulas, (3) 4 trechos EXTRA (fora do edital).

## Correções feitas (`content/overrides/quimica.json`)
1. **a04** — págs. 70–125 reclassificadas como COMMENTED: eram questões comentadas de outras bancas (marcador do índice sem "AOCP" não reconhecido). Teoria real: 3–60 (resumo 54–60). Hipótese do coordenador confirmada.
2. **a17** — teoria 3–60, resumo 61–69 (SUMMARY), comentadas multibancas 76–97 (estavam como SUMMARY, agora COMMENTED), lista 98–101. Confirmada a correção do orquestrador e eliminado o resto do problema. Casos como o de a17: nenhum outro (a00, a01, a02, a03 etc. têm marcadores "Teoria" e "Instituto AOCP" reconhecidos).
3. **Páginas de resumo ("PRINCIPAIS PONTOS DO TÓPICO")** — em 20 aulas o resumo e as folhas de fórmulas ficavam dentro da faixa de teoria e inflavam trechos: marcados SUMMARY (a00 27–31, 73–76, 116; a01 30–32; a02 19, 71–72; a03 40–41; a04 54–60; a05 10, 41–42, 82–84; a06 14–20, 66–68, 119–121, 141–142; a07 36–41; a08 35–37; a09 30–31; a10 42–51; a11 28–33; a12 29–33; a13 33–37; a14 19–21, 123, 148; a15 41–45; a16 36–41; a18 46–52; a19 7–8, 71–77; a20 6, 38–40; a23 21–24). Resumo não vira atividade.
4. **EXTRA (fora do edital/opcional)** — a11 181–188 (titulometria), a12 125–131 (2ª/3ª leis da termodinâmica, Gibbs), a18 175–179 (sabões e detergentes), a20 3–6 (hidrofilia/hidrofobia de sabões).
5. **Falsos subtítulos** — `dropHeadings` com regex em todas as aulas removeu cabeçalhos que eram expressões numéricas ou fórmulas ("12,01g mol…", "[H][OH] 10", "log(2)", "ln 2", "V = C", "6,02"), rótulos de equação e legendas ("RADICAIS + PREFIXO…", "F O N Cl Br…"). Em a17 também foram removidos 7 subtítulos automáticos de uma tabela (págs. 11: Alcano, Alceno etc.), que forçavam cortes inúteis.
6. Notas de aula em a04, a11, a12, a17, a18, a20.

Resultado: trechos mais autônomos (sem corte em fórmula), ~10–16 págs. Mantidos curtos (autônomos): a00/s05 (4, classificação das reações), a05/s03 (5), a14/s03 (3, corrosão) e a19/s01 (4, isomeria plana). A aula a14 corrosão tem só 3 págs. de teoria — aceitável porque o assunto é curto e fecha o item 2.6.

## Cobertura do edital (resumo; detalhe no JSON)
- **covered**: quase tudo do bloco 1 (estrutura da matéria), 2 (transformação) e 3 (orgânica), além de petróleo/combustíveis (4.1).
- **partial**: critérios de pureza (conceito disperso em curvas de aquecimento e PF/PE), proteção radiológica, organometálicos (só Grignard), sulfurados (só sulfonação), solventes orgânicos (só polaridade).
- **complement (c01)**: polímeros (vinílicos, acrílicos, diênicos, propriedades), siderurgia, **química do fogo e da combustão**, produtos perigosos/incompatibilidade/FDS, água e tratamento; mais gás ideal e proteção radiológica (acrescentados).
- **gap sem complemento**: nenhum item relevante; sulfurados (tióis/tioéteres) fica como risco baixo.

### Achado importante: química do fogo
O Estratégia **não ensina** os "aspectos químicos do fogo e da combustão" como tema. Existe só: combustível × comburente (a00 p19), combustão completa/incompleta de hidrocarbonetos (a17 46–47) e a combustão como oxirredução (a22 64). Em `gaps.json` não havia lacuna para esse item e o complemento original (c01) também não o cobria (só "ponto de fulgor", LII/LSI e densidade de vapor, na Parte 2). **Acrescentei a Parte 4 do c01**: triângulo/tetraedro do fogo, métodos de extinção, combustão completa × incompleta, queima de sólidos/líquidos/gases, gases de incêndio (CO, HCN, HCl, SO₂), transmissão de calor, flashover/backdraft/BLEVE, classes A–D e K e agentes extintores.

## Complemento c01 — avaliação e alterações
Revisei fórmulas, equações balanceadas, constantes e normas.
- Siderurgia: reações do alto-forno e do conversor corretas; faixas de carbono (gusa 3,5–4,5%; aço < 2%) corretas.
- FDS: 16 seções na ordem da NBR 14725/GHS corretas; pictogramas, Hommel (NFPA 704) e classes ONU corretos. Ponto de fulgor ≤ 60 °C para inflamável é a convenção usual (NBR/NR-20); mantido.
- Água: etapas na ordem correta; reações de coagulação balanceadas; padrões da Portaria GM/MS 888/2021 (cloro residual mín. 0,2 mg/L, E. coli ausente em 100 mL, flúor máx. 1,5 mg/L, pH 6–9) corretos. Nenhum erro encontrado nas partes originais.
- **Acrescentado** (texto original, sem cópia do Estratégia): Parte 4 (fogo), Parte 5 (polímeros: adição × condensação, vinílicos, acrílicos PAN/PMMA, diênicos e vulcanização, termoplásticos × termofixos × elastômeros), Parte 6 (proteção radiológica: blindagem, tempo/distância/blindagem, ALARA, Bq/Gy/Sv, determinísticos × estocásticos, irradiação × contaminação), Parte 7 (gás ideal: Boyle, Charles, Gay-Lussac, Clapeyron, Avogadro, Dalton). Atualizei título, subtítulo, "Como a banca cobra", resumo e fontes; `weight` subiu de 0,07 para 0,10 (o complemento passou de 232 para 420 linhas, ≈ 5.000 palavras). O build vai gerar mais de um trecho de Teoria (≤ 17 págs. cada).
- O PDF, por ter 7 partes, ficou longo; se o orquestrador preferir, pode separar em dois complementos (ex.: "fogo e produtos perigosos" e "polímeros/gases/radiação").

## Pendências e incertezas
1. **Questões embutidas na teoria** (necessita revisão humana): o professor intercala exercícios comentados à teoria sem marcador do índice (15–35% das págs. T por aula). O pipeline trabalha por página; esses exercícios ficam nos trechos de Teoria. Não corrigível sem granularidade menor.
2. **Tempo de Teoria** pode ainda estar acima do real em aulas muito exercitadas (a02, a04, a08); o tempo no plano é calculado pelo "load" do trecho.
3. Itens `partial`: sulfurados (tióis/tioéteres) e solventes orgânicos não têm seção própria; baixa frequência esperada.
4. `gaps.json` está desatualizado quanto a: fogo, polímeros, gás ideal e proteção radiológica (agora resolvidos pelo c01 ampliado). Pedido para marcar/ajustar.
5. a19 págs. 62–77 (análise conformacional) é aprofundamento além do edital literal (isomeria plana e espacial), mantida como teoria; decidir se vira EXTRA.
6. Nas aulas com títulos "(não localizado)" no índice (ex.: "<Tema> - Teoria") o tópico inicial não é verificado no PDF, mas as páginas e os marcadores foram conferidos manualmente.

## Pedidos ao orquestrador
- Rodar `build_complements.py` e o seed para refletir o c01 ampliado (título/peso novos).
- Atualizar `gaps.json` (itens: química do fogo, polímeros, gás ideal, proteção radiológica) para "resolvidos pelo complemento".
- Considerar, se couber, um item de banco de questões autorais para classes de incêndio/extintores e blindagem radiológica.
