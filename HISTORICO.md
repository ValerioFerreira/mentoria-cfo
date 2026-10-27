# Histórico do projeto e pendências de revisão

Registro único do que foi feito na construção do conteúdo (auditoria estrutural, bizus, questões autorais, auditoria de qualidade) e das **dúvidas do material** que exigem conferência humana. Substitui `PROGRESSO-AUDITORIA.txt`, `PROGRESSO-COLABORADOR*.txt`, `INSTRUCOES-COLABORADOR*.md` e `content/audit/qualidade/*` (todos recuperáveis pelo histórico do git). As regras vivas estão em `CLAUDE.md` e no fluxo de trabalho em `COLABORADORES.md`.

## 1. Linha do tempo

| Data | Marco |
|---|---|
| 2026-10-08 | **Auditoria estrutural** das 13 disciplinas (edital × PDFs × índice × segmentos), 25 complementos autorais (29 trechos `cNN`), mapa do edital fechado. Decisão: produção em duas etapas (bizu → questões) e duas frentes. |
| 2026-10-08/09 | **Etapa 1 (bizus)**: resumo + itens C/E + `pointers` dos 761 trechos, em duas frentes (jurídicas/línguas/biologia × exatas/informática). Tudo `DRAFT`. |
| 2026-10-09 | **Etapa 2 (questões autorais AOCP)** em quatro frentes de colaboradores (exatas; jurídicas + espanhol; parte A = biologia + inglês; parte B = português + penal militar + legislações PE). Todas fechadas e validadas. |
| 2026-10-10 | **Auditoria de qualidade** por amostragem (bizus/diretrizes e questões) e ampliação dos testes: interrompida pelo limite de uso da API. |
| 2026-10-11 | **Decisão:** a fonte única de questões passa a ser os cadernos do TecConcursos (`pipeline/questoes/`); as questões autorais e as do Estratégia saíram do banco e do repositório. Os bizus (resumo + C/E) continuam em `content/items/`. |
| 2026-10-12/13 | Resumos analíticos por colaboradores externos (`resumos-colaboradores/`), modelo comercial, Mercado Pago e parceiros (ver `CLAUDE.md`). |
| 2026-10-14 | **Auditoria do acervo de questões** (extração, imagens, classificação, correlação com os editais CBMPE/PMPE, banco). Produção só lida e copiada; nada aplicado. Relatório completo em `docs/questoes/auditoria/2026-10-14/RELATORIO.md` (fora do git). Resumo na seção 5. |

## 2. Auditoria estrutural (concluída)

Fluxo do material: `docs/` (PDFs) → `extract.py` → `segment.py` (classifica páginas T/C/L/K/S/F/B/X; teoria em trechos de 10–17 págs.) → `content/structure` + `content/segments` → `build_catalog.py` → `build_complements.py` → seed → planejador. Ids de trecho são **posicionais** (`<disc>/aNN/sNN`): toda resegmentação os muda; por isso bizus só se produzem depois de a estrutura da disciplina estar fechada.

Teoria em páginas / trechos, antes → depois da auditoria:
Português 802 → 801 / 58 → 60 · Inglês 313 → 278 / 21 → 23 · Espanhol 1279 → 466 / 103 → 36 · Informática 1129 → 1085 / 107 → 91 · Matemática 898 → 864 / 61 → 74 · Estatística 1020 → 916 / 71 → 75 · Física 501 → 494 / 37 → 39 · Química 1040 → 896 / 87 → 78 · Biologia 895 → 828 / 63 → 68 · Dir. Constitucional 957 → 930 / 82 → 87 · Dir. Administrativo 749 → 754 / 64 → 69 · Dir. Penal Militar 289 → 287 / 30 → 34 · Legislações PE 44 → 40 / 4. Cortes no meio de tópico: ~110 → 6; nenhum trecho acima de 17 págs.

Erros globais de classificação corrigidos: rótulos de questão ("1.(CESPE/…)", "QUESTÃO 11") reabriam a teoria; "<Tema> - Teoria" era lido como resumo; "Exercícios/Resolução" eram lidos como resumo; complemento de "que/se" removido (falsa lacuna).

Achados de maior impacto:
- Lei 8.112/1990 (regime jurídico único) **não** é ensinada pelo material-base (vacância, remoção, redistribuição, substituição, PAD).
- Legislações PE (maior peso da prova, 10 questões): o material cobre só arts. 1–26 e 50–59 dos 190 da Lei 11.817 e traz o Estatuto (Lei 6.783) em quadros-resumo.
- Óptica geométrica inteira ausente em Física; Inglês sem Present/Past Perfect Continuous e "had better".
- PDF com páginas duplicadas (Estatística a08 págs. 4–12 = a10 págs. 4–12; a07 37–42 = a09 16–21).
- Erros do material a avisar ao aluno: Inglês a06 p.39/42, a05 p.24; Física a09 p.20 (eclipse); Informática a12 p.122 (DELTREE) e 161–162 (WordPad no Windows 11 24H2).

Complementos (25 em `content/complements/*.md`, com PDF em `web/public/complementos/`): Dir. Administrativo (Lei 8.112), Dir. Constitucional (CE-PE, intertemporal), Dir. Penal Militar (súmulas), Física (óptica, tópicos), Matemática (geometria analítica, complementos), Legislações PE (Leis 15.187, 14.751, 11.817-penas, 6.783-lacunas, Decreto 50.014), ECA, Juventude, Maria da Penha, Inglês, Espanhol, Português (figuras, formação de palavras), Química aplicada, Biologia (qualidade de vida; biotecnologia/ambiente), Informática, Estatística. Lacunas registradas em `content/gaps.json`. Biologia ainda sem complemento de classificação/diversidade, origem das células e funções vitais (auditoria: parcial).

## 3. Produção de bizus e questões autorais (concluída)

- **Bizus (Etapa 1):** 761 trechos com resumo (6–14 tópicos só com **negrito**), itens C/E e `pointers` (≥ 4 pontos-chave com página). Tudo `DRAFT`; aprovação humana em `/admin/revisao`.
- **Questões autorais (Etapa 2):** exatas (Informática 1.229, Estatística 976, Matemática 944, Física 554, Química 1.016); jurídicas + espanhol (Espanhol 501; Dir. Constitucional e Dir. Administrativo na branch `questoes-juridicas`); parte A (Biologia 890 + Inglês 297 = 1.187); parte B (Português 753, Dir. Penal Militar 380, Legislações PE 103 = 1.236). Foram **descontinuadas em 2026-10-11** (ver linha do tempo); os arquivos de `content/items/` mantêm só os bizus.
- Método que funcionou: agente por lote de ~12 trechos (≈ 10 min), no máximo 3 agentes simultâneos (limite de uso do plano), leitura das páginas do trecho → JSON parcial → merge no arquivo da aula → `validate_content.py` → reparafrasear as frases copiadas (o material reproduz o texto da lei: trocar verbos/ordem e quebrar as listas legais) → commit pequeno por aula. Cada frente escrevia só nas pastas das suas disciplinas, o que evitou conflitos de merge.
- Pendências de conteúdo das exatas: Química a23/s02 (gasolina E30 desde ago/2025 × 25% no material), Física a17 (exemplos paramagnéticos duvidosos).

## 4. Auditoria de qualidade (parcial, 2026-10-10)

Amostragem com semente fixa, usando só o PDF como verdade (agentes S1–S3 para diretrizes/bizus; Q1–Q2 para questões AOCP). Interrompida pelo limite semanal de uso; cobriu 40 de 300 trechos e 200 de 10.332 questões.
- **Diretrizes/bizus (40 trechos):** nenhum ERRO de diretriz (só PEQUENO, quase sempre grafia de título); o **resumo** é a dimensão mais frágil (afirmação vinda de fora do intervalo ou detalhe omitido); ponteiros com 3 imprecisões de ±1 página; 363 itens C/E avaliados, **0 gabaritos errados** (3 ambíguos).
- **Questões (200):** 0 gabaritos errados, 0 críticas; 21,5% com algum achado (quase todos MENOR); a correta era a mais longa em 31% (esperado ≈ 20%); biologia concentrou achados (50%).
- **Testes:** Vitest passou de 11 para 27 arquivos (338 testes). Corrigidos `verifyPassword` (lançava exceção com registro truncado → agora falha fechado) e `isPlan` (aceitava chaves herdadas). Lacuna que segue em aberto: testes do pipeline Python (validador, `check_ranges.py`, funções puras de `segment`/`build_catalog`/`build_complements`) e das server actions.
- **Propostas de override de diretriz ainda pendentes** (aplicar só em `content/overrides/<disc>.json` → `segment.py --subject` → `build_catalog.py` → `build_complements.py` → seed, conferindo que os ids de trecho não mudam): (1) informática a12: `dropHeadings` p.62 e p.74 com capitular quebrada e `headings` "Painel de Controle" / "Configurações"; (2) inglês a04: título da p.24 "Futuro Simples e com o GOING TO"; (3) penal militar a04: `headings` p.9 "Aplicação da Pena" e p.19 "Concurso de agravantes e atenuantes"; (4) química a02, 1º trecho: `startPage` 3 → 4 (**muda página inicial; pode mudar ids**); (5) português a04 p.69 e a13 p.82 (baixa prioridade).
- Ferramentas dessa fase que continuam úteis: `pipeline/check_ranges.py` (alerta de ponteiro deslocado, título no meio, resumo fora do trecho) e `pipeline/validate_content.py`.

---

# Apêndice A — Pendências para decisão ou validação humana

Todo conteúdo entra como `DRAFT`; a aprovação (`APPROVED`) é humana, em `/admin/revisao`. Antes de aprovar, conferir:

## 5. Auditoria do acervo de questões (2026-10-14)

Ferramentas novas:
- `pipeline/questoes/auditoria.py`: validador independente PDF × extração × classificação × banco.
- `web/scripts/questoes-backup.ts`: backup verificável.
- `web/scripts/questoes-restore.ts`: reversão, testada em ida e volta no banco local.
- 12 agentes independentes:
  - 2 de validação visual do caderno de referência;
  - 4 de validação da classificação (amostra estratificada de 356 questões servidas);
  - 4 de correlação TEC → edital (601 categorias);
  - 2 de revisão de Atualidades (492 questões).

**Extração:**
- 38 cadernos, 1.830 páginas, 6.999 blocos e 5.883 questões únicas (100% AOCP): nenhuma perdida.
- Gabarito e número conferidos de forma independente.
- Corrigidos no extrator (versão `2026.10.14-1`):
  - fundo branco invisível transformava parágrafos em imagem (151 ocorrências);
  - sublinhado curto de letra destacada virava "•" no meio da palavra (19);
  - lacunas de preencher eram apagadas;
  - assertivas e itens ficavam colados (numeral em negrito, virada de página);
  - número no topo de página: 1 questão recuperada da quarentena.
- 2 questões continuam em quarentena por defeito do próprio PDF.

**Classificação:**
- Disciplina certa em ≈ 98,5%, mas trecho certo em ≈ 67%.
- O trecho ensina tudo o que a questão cobra em ≈ 56%; não ensina em ≈ 24% (≈ 800 questões, fora
  Atualidades).
- Atualidades: 311 de 492 em aula que não ensina o conteúdo (retrospectivas de 2026 recebendo fatos
  de 2006–2024).
- As 293 decisões `MANUAL` de aprovação/retirada em lote de rascunhos ficam travadas pelo
  importador e estão quase todas erradas na amostra.
- Corrigido: item do edital de outra disciplina (130 questões de Estatística sem assunto).
- Corrigido: questão retirada automaticamente nunca voltava.
- Corrigido: caderno do plano sem filtro AOCP.

**Editais:**
- "Fora do edital" estava valendo como "sem aula no catálogo CBMPE". ≈ 1.175 questões de Direito
  Administrativo do edital PMPE Oficial são descartadas: licitações, improbidade, LAI/LGPD,
  intervenção na propriedade, Lei 6.123/1968.
- A prova do Soldado CBMPE no sistema diverge da Tabela 10.1 do edital: falta Matemática (10) e
  Física (5); Legislações PE não consta.
- Os simulados PMPE mapeiam DGF/DH para `legislacoes-pe`.

**Trava nova:** gravação em massa na produção exige backup íntegro de menos de 24 h e
`--confirmo-producao`.

**Pendências** (decisão do dono; lista completa no § 10 do relatório):
1. prova do Soldado CBMPE;
2. taxonomia PMPE;
3. reabrir as 293 decisões `MANUAL`;
4. regras de Atualidades;
5. fonética (231 questões fora de qualquer edital);
6. genética clássica e fisiologia vegetal;
7. complementos ou `skip` para conjuntos/Venn, princípios fundamentais, zoologia/botânica e
   compactadores;
8. software antigo;
9. questões compartilhadas entre disciplinas;
10. casos pontuais de gabarito e figura ausente na fonte.

## A.1 Decisões e conferências pendentes (auditoria estrutural)

- Lei de referência do "regime jurídico único" do edital de Dir. Administrativo (assumida: Lei 8.112/1990).
- Decreto 50.014/2020 x ADI 6595 (STF declarou inconstitucional a Lei 13.967/2019 que motivou o decreto; o decreto
  segue publicado): complemento orienta a responder pela letra do decreto — validar.
- Lei 11.817: possíveis erros materiais nos arts. 37 e 58 (conferir no Diário Oficial).
- Alterações recentes do ECA em 2025-2026 não verificadas; Lei Maria da Penha conferida até a Lei 15.438/2026.
- Espanhol: promoção da a11 págs. 113-118 a teoria e a00 `partial` (confirmar).
- Todo conteúdo gerado entra como DRAFT; a aprovação (APPROVED) é humana, em /admin/revisao.

## A.2 Conteúdo escrito de memória nos complementos (verificar antes de aprovar)

    * Biologia: faixas do IDH, Vigitel 2023, Lei 9.433 art. 33 (consolidado), Leis 14.119/13.123/12.305, ADI 3.510,
      CRISPR 2023 foram escritos de memória/notícia — conferir.
    * Lei 8.112: estágio probatório = 36 meses (CF art. 41); o complemento cita o "Decreto 12.374/2025" — conferir o número;
      licença-paternidade/gestante vigentes não detalhadas; aposentadoria/pensão fora do complemento.
    * CE-PE: art. 171 §4º-B, art. 23 §5º, arts. 43 II x 61 I "a", art. 100 §13 (remissões estranhas) — conferir no Diário Oficial;
      a Aula 18 do Estratégia está desatualizada (art. 101 agora tem 6 incisos: EC 70 e 71/2026).
    * Penal Militar: vigência das súmulas do STJ não confirmada (STJ 172 pede cautela; STJ 47 desatualizada); art. 408 do CPM
      remete ao art. 233 revogado; ADI 7555 conferida só pela anotação do texto consolidado.
    * Física/Matemática: dados de tabela sem fonte primária (cosmologia, calor latente); nenhuma pendência de cálculo.
    * Material do Estratégia com erros a avisar ao aluno: Inglês (a06 p.39/42, a05 p.24), Física a09 p.20, Informática a12 p.122
      (DELTREE) e 161-162 (WordPad), Estatística a07/a08 (páginas duplicadas de outras aulas).

## A.3 Itens e complementos novos

  - Todos os itens são DRAFT; aprovar apenas em /admin/revisao.
  - Biologia: faixas do IDH, ADI 3.510, CRISPR 2023, Lei 9.433 — conferir. Atenção: o complemento lista 6 instrumentos da PNRH
    (incluindo "compensação a municípios", dispositivo que foi vetado na Lei 9.433); os itens NÃO cobram a contagem. Números
    datados (Vigitel, Mapa da Fome, linhas do Banco Mundial, STF 40 g) ficaram fora das questões de propósito.
  - Direito: EC 70/71 de 2026 (CE-PE art. 101) só aparecem no texto de bizu; Maria da Penha art. 16-A/12-D não foram usados
    em questões; Decreto 50.014 × ADI 6595; remissões estranhas do CE-PE (art. 171 §4º-B, art. 23 §5º, 43 II × 61 I "a").
  - Física/Química: tabelas (calor latente, rigidez dielétrica, composição do universo, Portaria GM/MS 888/2021) são valores usuais;
    cálculos foram conferidos em Python (08/10/2026).
  - Línguas: pontos que o complemento marca como "a conferir" foram evitados nas questões.

---

# Apêndice B — Dúvidas do material (pontos NÃO usados nos itens; conferir com humano)

Agrupadas por disciplina na ordem em que foram levantadas. Quem produzir novos bizus/questões deve **evitar** esses pontos.

## B.1 Bizus — frente jurídicas/línguas/biologia

- Pontos do material NAO usados por duvida (revisao humana): Estatuto PE a02 - regra de proventos com +30 anos e acrescimo de 20% no ultimo posto, reserva a pedido (35 anos / ingresso >= 2022) e idades-limite (67/63/70) - confirmar na redacao vigente da Lei 6.783/1974.
- 2026-10-08: direito-penal-militar COMPLETO no bizu (36/36 trechos, a00-a11). Duvidas do material p/ revisao humana (pontos NAO usados nos C/E):
  a00: Lei 13.491/2017 grafada 13.471; autoria da doutrina (Romeiro/Lobao) inconsistente; data impossivel HC 99.671; art. 18 CPM truncado; citacoes STF/STM sobre art. 9 II a nao usadas.
  a01: art. 42 lista incisos I,II,III,V (sem IV); teoria extremada x limitada contraditoria entre pags. 3 e 23; art. 41 ("as avessas") evitado.
  a04: concurso formal 1/6 a 1/2 (tabela do material diz 2/3); livramento condicional art. 89 (2/3 motim; 1/3 primario <21 ou >70) so no resumo - conferir com a lei.
  a05: "internacao minima 1 a 3 anos" nao confirmada no art. 112 CPM. a06: Ministerio x Ministro da Justica (art. 141). a07: reabilitacao (inciso V do art. 123 revogado) e faixa "menos de 1 ano = 3 anos" do art. 125 duvidosa.
  a08: Lei 7.170/83 desatualizada; incitamento so se consuma com concordancia (questionavel); veto ao art. 166; penas antigas (suspensao do posto) arts. 170/174/198/201 substituidas por detencao.
  a09: art. 218 I (autoridades) contradiz pag. 27; arts. 236/237 possivelmente alterados pela Lei 14.688/2023; roubo improprio "furto frustrado"; homicidio privilegiado "pode reduzir" (bizu usa leitura de direito do reu - conferir).
  a10: Lei 8.666 revogada pela 14.133; numeracao do par. 3 do art. 290; par. 4 confuso (so letra da lei). a11: art. 233 revogado citado no art. 408; "estado de sitio" = guerra discutivel.
- 2026-10-08: direito-constitucional a00-a05 com bizu (23 trechos). Duvidas do material (NAO usadas nos C/E):
  a00: EC 123/2022 "inconstitucional"; quorum 3/5 de emendas estaduais; regimentos/resolucoes CNJ-CNMP = lei ordinaria; tratados DH imunes a denuncia; CF/1937 "rigida".
  a01: 3 direitos fundamentais "absolutos" (corrente). a02: ADPF 635 (MP e forca letal), imprensa x individuo (p.24), aborto "por analogia" (p.14), Testemunhas de Jeova (menores), conceito de "dia" (p.31), aviso previo de reuniao contraditorio (p.43).
  a03: art. 5 XI x XIII (p.28); art. 5 XXXV x XXXVI (p.13); 25 jurados (Conselho de Sentenca tem 7); sancao perpetua art.137 Lei 8.112/ADI 2975 nao verificada; concretista geral x individual (Lei 13.300 adota individual); "sem liminar" em MI/HD; extradicao de quem renunciou a nacionalidade (EC 131/2023).
  a04: "PEC 72/2013" = EC 72; RE 788.889 = 778.889; "Ministerio do Trabalho e Previdencia" desatualizado; prazo licenca-paternidade; eficacia dos direitos sociais (so no resumo). a05: perda da nacionalidade - usada so a redacao da EC 131/2023.
- 2026-10-08: direito-constitucional a06-a10 com bizu. Duvidas do material (NAO usadas nos C/E):
  a06: idade minima "na data da posse" x data-limite do registro (Lei 9.504/Lei 14.211); perda x suspensao (classificacao doutrinaria). a07: "35 partidos" desatualizado.
  a08: LC 230/2026 (municipios), "EC/PEC 139/2026" (Tribunais de Contas) nao confirmadas; prazo de 15 dias na intervencao nao esta na CF; ADPF 982 so no resumo; art. 29-A (inativos), TRT-13 e taxa de antenas confusos.
  a09: EC 138/2025 e EC 135/2024 nao usadas; acumulo de militares estaduais (p.38 x p.69); typos "inciso XXVIII" (XVIII). a10: EC 136/2026 e "EC/PEC 139/2026"; Sumula 347 "superada"; CNJ; Daniel Silveira/LSN; typo art. 52 VI (V); conferir HC 232.627/2025 (foro) e ADPF 982.
- 2026-10-08: direito-constitucional a11-a13 com bizu. Duvidas (NAO usadas): a11 percentuais de emendas individuais/saude (EC 86 x EC 126/2022) omitidos; promulgacao de MP atribuida ao "Presidente do Senado" (e Mesa do Congresso); a12 "rainha", composicao dos Conselhos da Republica/Defesa em imagem; a13 EC 136/2025 (precatorios) usada com atribuicao - conferir; ADI 4357/7047/7064; STJ (quinto constitucional) debate; subteto 90,25% e IDC nao usados.
- Duvidas do material (NAO usadas nos C/E) - Administrativo: a02 DL 200/1967 so federal; ANPD como agencia (MP 1.317/2025) nao usada; a04 sem duvidas relevantes; a05 Lei 10.522/2000 (correto: 2002); a06 permissao como contrato x ato (usei a Lei 8.987); a07 "EC 139/2026" (Tribunais de Contas permanentes) USADA no bizu como no material - conferir texto/numeracao; a07 contradicao do material sobre ressarcimento imprescritivel (pag. 27) x Tema 899 (usei Tema 899); a09 Lei 15.142/2025 (cotas) e Lei 14.965/2024 (concursos) e EC 138/2025 (professor + qualquer cargo) usadas conforme o material - conferir vigencia; a09 limite "1,60 m/1,55 m" (Tema 1.424) idem.
- Duvidas do material (NAO usadas nos C/E; conferir com humano):
  Portugues - a00 sem; a02/s06-s07: lista visual de palavras atrativas e tabelas (e/como/pois, discurso direto->indireto) sao imagens, nao extraidas; a04/s04 p.55 "prover" x "ver" no perfeito contradiz o proprio texto; a05 "dói muito nas minhas costas" como oracao sem sujeito (discutivel); a06 virgula entre sujeito e verbo ("Quem compra, compra algo", ABL x Sacconi); a07 variantes ("Fomos nós quem convidou"), "nem" excludente (Ulisses Infante); a08 "entrei e saí de casa" e "visar" sem preposicao; a13 EUA/UNESCO x Unesco/Acnur (MRPR), Excelentissimo Senhor (MRPR x Decreto 9.758/2019), typos "decração", "25 km"/"Km".
  Ingles - a06 "a slap on the wrist" = punicao severa (errado: leve), "whom" glosado "cujo", "that" em non-defining, 5 tipos de condicionais; a05 Future Perfect Continuous "sempre com for"; a04 "hold" = abracar, tirinha "Where are you going?" como futuro; a05 p.18 gabarito com letras trocadas; a01 "data" plural; a03 9 modais + 3 semimodais (tabela lista 4); a00 falsos cognatos "magazine"/"alias".
  Espanhol - a06 "la cometa"=foguete, "violeta"=roxo, "botiquin"=boteco; a04 RAE nao registra "conjuncion explicativa", "segun/siempre que" em 2 classes; a09 "hay amado", tabela do imperativo (usted rotulado indicativo), typos "hubran"/"hubieramos"; a10 billon (escala curta x larga), trillon=10^18; a13 "biceps"="arvore", "el desordem", "a estante" heterogenericos, listas de heterosemanticos duvidosas.
  Biologia - a00 coronavirus "retrovirus", 38 ATP por glicose, anaerobica = fermentacao; a01 retina/epitelio olfativo "unipolares", juncoes comunicantes "em sinapses quimicas", selecao disruptiva "um extremo"; a02 "VNTP"/VNTR, STR com "baixa taxa de mutacao"; a03 Taq "isolada por Mullis"; a04 explosao cambriana, datas de mamiferos, ocupacao da America; a05 mamarias "apocrinas"; a06 coccix 3-5 x 4 vertebras, esterno x costelas, dens; a07 triceps "flexiona o cotovelo", intercostais; a08 arteriosclerose "tunica media", linfa "produzida pelo intestino", epitelio da laringe; a09 proenzimas (fibrinogenio), GnRH/LSH; a10 31 pares (12 dorsais, 5 lombares, 6 sacrais), -90 mV x -70 mV, "glandula perineal"; a12 numeros da morula/blastocisto, tabela de anexos; a13 Mata de Araucarias "2%"/FOM "13%", oxigenio dissolvido "indiretamente proporcionais"; a14 hotspots (criterio "1/3 da vegetacao" - real: perda >= 70%), "espécie chave = guarda-chuva"; a15 sorotipos de dengue desatualizados, malaria (72 h so P. malariae); a16 pulsacao de adolescentes, "dar agua" ao acidentado; a17 queimadura 1o grau "bolhas", 2o grau profundo "sem regeneracao", Heimlich "5 compressoes".

## B.2 Questões autorais — pontos evitados (frente de Valério)

- Ingles a01 s01: explicacao do exercicio de plural diz que em composto so a ultima palavra vai ao plural (falso p/ mother-in-law); "Eskimo" datado. a01 s02: gabarito do exercicio de artigos traz "AN economista" (typo). a02 s03: "friendly manner" tratado como adverbio (e adjetivo); lively/lovely como adverbios; regra de inversao com never/seldom/rarely incompleta. a02 s01: "not only...but also = as well as" impreciso. a02 s04: "overflow = inundacao"; "poetess" em desuso.
- Biologia a00-a01: coronavirus "retrovirus", 38 ATP por glicose, "anaerobica = fermentacao", voltagens do potencial de membrana inconsistentes, "transformacao bacteriana" como transferencia de plasmideos (seria conjugacao), cinetocoro/centromero imprecisos; a01: juncoes comunicantes "em sinapses quimicas" e neuronios "unipolares" na retina/epitelio olfativo. a00 s04: ">130 ATP" do acido palmitico nao usado. a00 s06: regra 2^n de gametas vem do exemplo do material (extrapola).
- Biologia a03-a05: a03 polimerases eucarioticas alfa/beta/gama (p21) e "TATA box" de procarioto (p9); a04 selecao balanceadora = estabilizadora (p11), placenta separando marsupiais de placentarios (p21), "purificadora"/"direcional" (s01 q10) e amniota monofiletico incluindo aves entre os repteis (s01 q12); a05 mastocitos como "celulas fagocitarias" (p37) e texto contraditorio sobre glandulas apocrinas (p28-29; s02 q11 segue o material).
- Portugues a00-a01: a00 p50-56 (virgula entre sujeito e verbo, "em pratica" como objeto indireto de "por", "assistir"=morar e "visar"=ter como objetivo); a01 p10 (tabela digrafo nasal x ditongo nasal repete "ontem"/"jejum"), p30/39 ("sub-humano"; "bem-feito/benfeito" com dupla grafia), p61 ("senao"/"se nao" apassivador, "grosseiro, senao verdadeiro").
- Portugues a02-a03: a02 p84 lista de palavras atrativas (imagem, nao usada); a02 s07 q6 (infinitivo livre mesmo com atrativo: gramaticos mais rigidos discordam); a03 p40-41 (tabelas de "e", "como", "pois" sao imagens), "tenho que estudar" como preposicao acidental (p26), "porque" = "para que" (p31), "e nem" redundante (p14), "atraves" (p8); a03 s01 q4 (eu/tu apos preposicao acidental, p4).
- Penal Militar a00-a04: a00 s03/s04 (veto dos par. 1 e 3 do art. 9 segue so o texto do material; arts. 17, 18 e 28; art. 11 confuso), a00 s02 (correntes STF/Neves x STM sobre "contra as instituicoes militares" atribuidas a eles); a01 s01 (exemplo de causa superveniente usa o resultado do material); a04 s02 (lista do paragrafo unico do art. 70 "c, l, m, o" contradiz o comentario do PDF, que cita a alinea "n"; seguiu-se a lei); a04 s03 (art. 78 e triplo do paragrafo unico do art. 80 sem conferencia); a04 s05 (Tema 1200 do STF segue a transcricao do material; arts. 100 e 101 "nao recepcionados" x mantidos).
- Portugues a04-a05: a04 p55 ("prover" x "ver" no perfeito), p78 ("tem gerado = gerou"; "se pudessemos, fariamos = se pudermos, faremos" contradiz p10), p33 ("nao ha imperativo na 1a pessoa" mas a tabela traz "nos"), p11/p15 (regra do auxiliar do tempo composto ignora "tinha/havia + participio"), p57 (typo "abativessem abatessem"); a05 p15-16 ("doi muito nas minhas costas" sem sujeito), p34 ("Jorge, malandro" predicativo), p20 (vir/ir/chegar), p32 (predicativo do objeto de objeto indireto). Revisao: a05 s01 q5 ("o" em "deixou-o sair" so como sujeito do infinitivo), a05 s04 q3 (contagem de oracoes com "e que"), a04 s01 q11 (perfeito no lugar do mais-que-perfeito), a05 s02 q12 e a04 s06 q12 seguem a classificacao do PDF.

## B.3 Exatas e Informática (Informática, Estatística, Matemática, Física, Química)

PONTOS PARA REVISÃO HUMANA
1. Física a17 e Matemática a13-a14 foram primeiro escritos SEM o PDF; depois o Valério enviou
   os PDFs e as três aulas foram REESCRITAS lendo o material (validadas, com checagem de
   originalidade). Já não há aula escrita sem PDF.
2. Padrão de correção de originalidade: ao reescrever para passar nos 10-gramas, alguns
   resumos ficaram mais enxutos. Vale uma leitura rápida de Informática a09-a14, onde o
   material é muito tabular (menus, atalhos).
3. Atalhos do PowerPoint (a10) e do Writer (a09) seguem as tabelas do próprio material
   em português (PowerPoint PT-BR: Ctrl+O = Novo, Ctrl+A = Abrir, Ctrl+B = Salvar,
   Ctrl+N/I/S = negrito/itálico/sublinhado, Ctrl+L/U = localizar/substituir).

PROBLEMAS ENCONTRADOS NO MATERIAL (para o Valério avaliar)
- Informática a12 (Windows), pág. 10 e 11: o texto diz que o Windows 11 foi lançado em
  "outubro de 2021" e, duas páginas depois, em "junho de 2021". O bizu usa outubro de 2021
  (data de lançamento oficial; junho/2021 foi o anúncio).
- Informática a11 (Impress), págs. 19-23: as tabelas dos menus são imagens; o texto extraído não
  traz os comandos. As imagens foram lidas no PDF e o bizu foi corrigido (ex.: o menu
  "Apresentação de slides" só tem F5, Shift+F5, Cronometrar, apresentação personalizada e
  configurações; existe também o menu "Slide").
- Informática a10, pág. 57: a tabela da guia Revisão do PowerPoint cita "O Word vai verificar
  a ortografia" (erro de copiar/colar do material). Bizu escrito com "PowerPoint".
- Informática a12, pág. 186: no texto extraído faltavam os rótulos F1-F11; foram conferidos na imagem
  e incluídos no bizu (F1 ajuda, F2 renomeia, F3 pesquisa, F4 histórico de endereços, F5 atualiza,
  F6 foco, F10 menu, F11 tela cheia).
- Informática a14, pág. 120 ("Desafio de Configuração"): o gabarito está "de ponta-cabeça"
  no PDF e o texto extraído ficou truncado.

SEGMENTAÇÃO / ESTRUTURA (nenhum arquivo de estrutura foi alterado)
- Informática a10 s01: os "headings" detectados incluem frases longas em caixa alta
  (observações do professor) como se fossem tópicos; sugere-se `dropHeadings` em
  content/overrides/informatica.json.
- Informática a12 e a14: vários tópicos aparecem com a primeira letra truncada
  ("NTRODUÇÃO AO", "REA DE RABALHO", "ARDWARE") por causa de versalete no PDF; só cosmético.
- Informática a13 s01 tem 13 págs e a12 s13 / s15 têm 17 págs (teto): ok, mas s13/s15 ficaram
  no limite.

PROBLEMAS ADICIONAIS NO MATERIAL (reescrita de Matemática a13)
- Matemática a13, pág. 9: o número de Euler aparece como "aproximadamente 2,721"; o valor correto é
  ≈ 2,718 (o bizu usa 2,718).
- Matemática a14, pág. 22: o gabarito comentado fala em "progressões geométricas aritméticas" (erro
  de digitação; refere-se à PA).

ETAPA 2 — PROBLEMAS DO MATERIAL ENCONTRADOS (não geraram questão; o Valério corrige/avalia)
Informática
- a02 p36: senha de 8 dígitos numéricos = "1 milhão" (seria 100 milhões); p60 x p62 (AR emite ou não); p11 "risco" x ameaça.
- a01 p15-16: intranet remota x extranet depende da banca (ambíguo). a03 p27: "cavalo de Troia é vírus" varia por banca.
- a12: Windows 11 lançado em junho (p11) x outubro de 2021 (p10, p36); tabela p42 com Restaurar/Maximizar trocados;
  Win+Seta p42 x p186; barra de tarefas "movível" (p24, p29) é do Windows 10; F8 para Modo de Segurança e
  "Atualização e Segurança > Backup" (p176, p173) são do Windows 10; DELTREE (p122) não existe; histórico da
  área de transferência "25 itens" (p132) x 24 (p89-90, p133); "COM" provavelmente "CON" (p121).
- a13: Office 365 "5 PCs, R$30" desatualizado; CaaS tem 2 significados (p25); iCloud ambíguo (p37).
- a14: msinfo32 com Ctrl+R (p77, é Win+R); gabarito SSHD p116 (Letra C x explicação B); tempo de acesso de HD/SSD
  "em nanossegundos" (p118); memória primária RAM/ROM/cache (p84) x só RAM/ROM (p93); data/hora na ROM (p95, é CMOS);
  ISA "anos 90" (p56, é de 1981); AGP obsoleto (p60).
- a11 p11: cita "ocultar slides" no menu Apresentação de slides, mas a imagem não traz esse comando.
Estatística
- a00 p21 (total incoerente); a01 p33-34 (notas 7,0 x 6,0), p50 (comentário 7min14s x gabarito D 7min32s), p55 (média
  geométrica de taxas), p63 (média geométrica de 1 e -1); a02 p60 (P77 41,58 x 41,04); a03 p27 (média x moda);
  a05 p45 (D4 x D3). a07 págs. 37-42 (função de distribuição acumulada) são EXTRA e ficaram sem questões.
Matemática
- a01 p41, p43-44; a03 p19-20, p30-31, p62; a05 p24; a06 p6 (J=122 truncado; item do CFO DF falso); a07 p30 (gabarito C x
  valor da D); a08 p26; a09 p36-37 (mais de uma defensável); a10 p33, p46, p54; a11 p24-25, p46, p62; a13 p9 (e=2,721);
  a14 p19 (gabarito B x valor 600 = D) e p22; a15 p23, p25, p26, p44, p58, p69, p116, p119; a16 p42, p45 (esfera
  "inscrita" x circunscrita); a17 p53, p78.
Física
- a02 p19; a04 ("centrípeta constante"); a05 p36; a09 p7 (unidade/constante da 3ª lei); a10 ("E>P flutua"); a11 p13/15
  (capacidade térmica x calor específico); a13 (onda estacionária, difração do som, Vmax do MHS); a14 (corpo neutro);
  a16 (título não bate com o conteúdo); a17 p10 (plástico e madeira como paramagnéticos: duvidoso).
Química
- a00 (radônio "Rb"; fórmula do AAS), a01 (postulado 6), a02 (Mendeleyev 1871; "fosfato (SO4 2-)"; Mg paramagnético;
  limites 2n²), a03 (esquerda/direita; "5/2 de O2" para Cl2), a04 (Be no dueto; AgCl3/FeBr3; SO3), a06 (O +1 em
  fluoretos; "trinitroglicerina"; H2CO3; NO), a07 (nitroglicerina; NaCl 58,4), a08 ("solidificação fracionada"),
  a09 (nitrito de prata "insolúvel"), a22 (p56 sinal O/C=O; p63 Fehling Cu+; p65; p71 NaBH4; p102 biodiesel),
  a23 (p8 propano C3H6; p9 rocha geradora x reservatório; p10 butadieno; p17 HDS/HDN; p14 gasolina 25% de etanol:
  hoje E30 desde ago/2025, valor DESATUALIZADO também no bizu de a23/s02 — não alterado).
- Bizu de a23/s01 cita polos petroquímicos da p20, fora do trecho (p3-12).

ETAPA 2 — PONTOS PARA REVISÃO HUMANA (principais)
- Aulas com menos de 50% de cálculo (matéria conceitual): Física a12 (e em parte a03, a09, a13, a14), Química a05 e a08.
- Informática: em ~28-68% das questões a correta é a mais longa por margem pequena (passa na regra do validador).
- Alternativas/convenções: kilo = 1024 em bytes e 1000 em bits (convenção do material, não SI); 480 Mbps = 60 MB/s;
  espaços gratuitos de nuvem (15/2/5/5 GB) podem estar datados; PaaS x SO (a13 s02 Q6).
- Estatística: convenção de arredondamento de posições em quartis/decis/percentis; relação moda<mediana<média só em
  casos concretos; Cp de Mallows e R² ajustado (a14 s03) tratados de forma breve pelo PDF.
- Matemática: g²=R²+h² (cone, a16 s03), cos 120° = -1/2 dado no enunciado (a15 s04), "tan x >= 1" (a17 s10).
- Física: convenção de sinal no Doppler; fontes em oposição de fase; eta = 50% na potência máxima (derivado, não literal).
- Química: eletronegatividade N x Cl (a02); força do Mg(OH)2 (a05/a06); SF4 (a04); Grignard e estequiometria 3:1 da
  transesterificação (a22 s05, não explícitos no material).
- Informática: a02 s05 q13 (confidencial x restrito), a02 s06 q13 (A1 = 1 ano, A3 = 5 anos), a03 s06 q12 (whaling x
  spear phishing), a12 s13 q15 (chave HKEY_CURRENT_PROGRAMS inventada) e s11 q9 (AUX.docx), a12 s15 q10 (exFAT).
- Física a17: duas questões nível 3 (direção do campo, razão no solenoide).
- Intervenção no bizu fora do escopo: Química a09 s02 teoria[1] e [2] (paráfrase por originalidade).


## B.4 Dir. Constitucional, Dir. Administrativo e Língua Espanhola

Língua Espanhola a13 (relatório do agente):
- Evitados por serem discutíveis/regionais: cutis, cancelar = pagar, prohibido/ahijado como ditongo, latir, acudir,
  carro = carroça, bolso.
- Já apontados antes e evitados: 'bíceps' = 'árvore', 'el desordem', 'a estante', listas duvidosas.
- Revisão humana: billón = trilhão e mil millones = bilhão (s04, p. 46; coerente com a RAE, mas é a mesma escala numérica
  da a10); extrañar = sentir saudades (s04, p. 50; uso americano, com objeto pessoa); classes "total" e "conceitual" de
  sinonímia (s02) têm exemplos sobrepostos (marido/esposo): nunca foram oferecidas juntas como alternativas no mesmo item.
Dir. Constitucional / Dir. Administrativo: relatórios finais dos agentes ainda não recebidos (completar aqui).

6. PARA REVISÃO HUMANA
- Amostragem das questões antes de aprovar (APPROVED) em /admin/revisao, principalmente em lei seca e temas com alterações
  recentes (emendas constitucionais, leis novas).
- Espanhol: conferir os textos-base originais em espanhol e a correção segundo a RAE.


## B.5 Língua Portuguesa, Dir. Penal Militar e Legislações PE (parte B)

- LP6 (Português a03, a11): pontos do material NÃO usados em questões:
  a11 p.45 (poema com marcas emotivas = função poética) x p.41 (emotiva predomina em poemas líricos); a11 p.14 mantém o tempo
  verbal da fala no discurso indireto ("João disse que Pedro não desistirá"); pp. 40-41 (a03) e 12, 43, 48-49, 52 (a11) são imagens.
  a03/s02 usa a regra do material de que "mas" não vem intercalado entre vírgulas (p.20): a banca pode discordar.

PARA REVISÃO HUMANA
- Amostragem das questões antes de aprovar (APPROVED) em /admin/revisao, principalmente lei seca (CPM, Estatuto dos Militares de PE,
  Código Disciplinar) e temas com alterações recentes de lei.
- Língua Portuguesa: conferir os textos-base originais e a gramática normativa (dúvidas já mapeadas em B.1).


---

# Inclusão do PCPE (Outubro/2026)

## 0. Decisão do Dono do Produto (Out/2026)
**O único concurso da PCPE que será oferecido na plataforma é o de AGENTE DE POLÍCIA (`PCPE_AGENTE`).**
O cargo de Escrivão de Polícia (`PCPE_ESCRIVAO`) e a disciplina de Noções de Arquivologia estão **definitivamente fora do escopo**. Não haverá "Fase B" nem disciplina de Arquivologia. Todo o código, catálogo, enum, simulados e testes foram consolidados estritamente para `PCPE_AGENTE`.

## 1. Análise do Edital Oficial (`docs/edital-pcpe.pdf`)
- **Norma**: Portaria Conjunta SAD/SDS nº 306, de 02/10/2026 (Polícia Civil de Pernambuco — PCPE).
- **Banca**: **Cebraspe** (Centro Brasileiro de Pesquisa em Avaliação e Seleção e de Promoção de Eventos).
- **Cargo incluído**: **Agente de Polícia** (`PCPE_AGENTE`) — 1.200 vagas (780 AC, 60 PCD, 300 PPP, 36 PI, 24 PQ). Remuneração inicial: R$ 5.667,92.
- **Fora do escopo**: Escrivão de Polícia (`PCPE_ESCRIVAO`) e Delegado de Polícia (`PCPE_DELEGADO`).
- **Data da Prova Objetiva e Discursiva (Anexo I)**: **07/03/2027** (`2027-03-07`, turno da tarde; duração de 4 horas).
- **Estrutura da Prova Objetiva (Itens 7.1 e 8)**:
  - **Formato (Item 8.2)**: **Múltipla escolha com 5 opções (`A` a `E`)**, uma única resposta correta por questão.
  - **Pontuação (Itens 8.11.1 e 8.11.2)**: **60 questões = 60,00 pontos** (`+1,00` ponto por questão certa; `0,00` por questão errada, em branco ou com marcação dupla — **sem penalidade negativa**).
  - **Critério de aprovação / corte (Item 8.11.4)**: Eliminado quem obtiver **menos de 30,00 pontos** no conjunto das provas objetivas (`P1 + P2`, 50% do total), sem nota mínima separada por bloco ou disciplina. Classificados para correção da Discursiva (Item 8.11.7): até 7.200 candidatos para Agente (4.680 AC).
  - **Distribuição dos blocos e disciplinas (`PCPE_AGENTE`)**:
    - **Bloco I — Noções de Direito (`P1`, 20 questões)**:
      1. *Legislação Estadual* (`legislacao-pcpe`): 4 questões.
      2. *Noções de Direito Constitucional* (`direito-constitucional`): 4 questões.
      3. *Noções de Direito Administrativo* (`direito-administrativo`): 4 questões.
      4. *Noções de Direito Penal* (`direito-penal`, Parte Geral e Especial): 3 questões.
      5. *Legislação Penal Extravagante* (`legislacao-penal-especial`): 2 questões.
      6. *Noções de Direito Processual Penal* (`direito-processual-penal`): 3 questões.
    - **Bloco II — Conhecimentos Específicos (`P2`, 40 questões)**:
      1. *Língua Portuguesa* (`lingua-portuguesa`): 10 questões.
      2. *Informática* (`informatica`): 10 questões.
      3. *Contabilidade Geral* (`contabilidade-geral`): 10 questões.
      4. *Raciocínio Lógico* (`raciocinio-logico`): 5 questões.
      5. *Estatística* (`estatistica`): 5 questões.
- **Prova Discursiva (`P3`)**: Decisão estratégica do Dono do Produto: A prova discursiva NÃO entra no sistema MentorIA. Nada será criado nem mantido para redação/discursiva. O escopo do sistema é 100% voltado para a prova objetiva (questões, simulados, bizus, resumos e teoria).

## 2. Decisões de Arquitetura e Preservação de IDs
1. **Preservação absoluta de IDs existentes (`<disc>/aNN/sNN`)**:
   - Nenhuma disciplina, aula ou trecho existente teve seu ID ou intervalo de páginas alterado (verificado contra baseline em `pipeline/.cache/pcpe-baseline/`).
   - Em `direito-administrativo`, as aulas novas entram como **`a20` a `a24`** e o complemento autoral da Lei Federal nº 9.784/1999 entra como **`c02`**, todas marcadas com `onlyContests: ["PCPE_AGENTE"]`. Os planos de `CBMPE_OFICIAL`, `CBMPE_SOLDADO`, `PMPE_OFICIAL` e `PMPE_SOLDADO` permanecem **100% idênticos** ao baseline de produção.
2. **Separação entre `direito-penal` e `legislacao-penal-especial`**:
   - *Noções de Direito Penal* (`direito-penal`, `a00`–`a10`: Parte Geral, Parte Especial e LCP) e *Legislação Penal Extravagante* (`legislacao-penal-especial`, `a11`–`a22` + `c01` ECA) estruturadas separadamente para evitar estrangular o limite diário por disciplina (`MAX_DAILY_SUBJECT_MIN = 120`).
3. **Complementos autorais para lacunas do edital**:
   - `legislacao-pcpe/c01` (`content/complements/leg-pcpe-ce-pe.md`): arts. 101 a 105-B da Constituição Estadual de PE (Polícia Civil e Segurança Pública), 100% neutro e autoral.
   - `direito-administrativo/c02` (`content/complements/da-lei-9784.md`): Lei Federal nº 9.784/1999 (Processo Administrativo Federal).
   - `legislacao-penal-especial/c01` (`content/complements/leg-penal-eca.md`): aspectos penais e procedimentais policiais do ECA (arts. 103–109, 171–178, 228–244-B e Súmula 500 do STJ).
4. **Cálculo de Importância e Exclusões Versionadas**:
   - Algoritmo de `pipeline/importance.py` recalculado de forma puramente funcional sobre `content/contests.json` e `catalog.json`.
   - Exclusões versionadas em `content/overrides/`:
     - `informatica`: `a07`, `a09`, `a11` (LibreOffice Writer, Calc, Impress excluídos para `PCPE_AGENTE` por exigir estritamente Microsoft 365).
     - `estatistica`: `a11`..`a14` (inferência estatística, testes de hipóteses, ANOVA e regressão múltipla excluídos para `PCPE_AGENTE` por exigir apenas descritiva, probabilidade e amostragem).
     - `direito-constitucional`: `a18` (art. 100 dos Militares de PE excluído para `PCPE_AGENTE`, que utiliza os arts. 101–105-B da Polícia Civil em `legislacao-pcpe/c01`).
   - Comprovada divergência zero (0 discrepâncias) nos 897 trechos de CBMPE e PMPE contra `main`.

## 3. Estado Atual dos Componentes
- **Banco de Dados Local**: Migração `20261016140000_pcpe_agente_settings` aplicada localmente (`category = 'PCPE'`, `examDate = '2027-03-07'`). `seedContestSettings` removido do seed de estrutura para respeitar as configurações manuais do administrador.
- **Next.js & Tipagem**: `typecheck` e `npm run build` aprovados com zero erros.
- **Motor de Planejamento**: 330 testes de planejador aprovados com 100% de sucesso.
- **Disponibilidade Comercial**: `available: false` mantido para `PCPE_AGENTE` até que as pendências de conteúdo autoral e questões sejam atendidas.

## 4. Pendências Identificadas para o Dono do Produto
1. **Cadernos de Questões Cebraspe (TecConcursos)**: Não existem cadernos baixados em `docs/questoes/` para as novas disciplinas da PCPE (Contabilidade Geral, Direito Penal, Processo Penal, Legislação PCPE e Leis Penais Especiais Cebraspe). O download deve ser realizado pelo Dono do Produto com sua conta e importado via `python pipeline/questoes/importar.py --remoto`.
2. **Bizus autorais (`content/items/`)**: Faltam 239 trechos nas disciplinas novas e em `direito-administrativo` `a20`..`a24`.
3. **Resumos analíticos (`content/summaries/`)**: Faltam 309 trechos (239 das matérias novas + 70 de raciocínio lógico em produção).

## 5. Rodada 3 de Correções (Outubro/2026) — Homologação Completa

Após a terceira rodada de revisão técnica e auditoria dos planos, foram implementadas e homologadas as seguintes correções:

### 5.1 Bloqueante 1: Prevenção de Diluição no Planejador (Isolamento por Concurso)
- **Problema:** O planejador calculava `totalInc` e `share` somando a incidência de todas as aulas selecionáveis do catálogo da disciplina, sem filtrar se pertenciam ao edital do concurso selecionado. Com isso, as aulas exclusivas de Direito Administrativo da PCPE (`a20` a `a24` + `c02`) diluíam o peso das aulas comuns no CBMPE e PMPE em cerca de 37%.
- **Solução:** 
  - Adicionado suporte aos campos `onlyContests` e `excludeContests` no tipo `CatalogAula` (`web/src/lib/planner/types.ts`).
  - Implementada a função pura `isAulaInEdital` em `web/src/lib/planner/select.ts`, garantindo que apenas aulas elegíveis para o concurso ativo entrem no somatório de incidência, ganho e share.
  - Exportado `inEditalAulas` em `Selection` e ajustado `web/src/lib/planner/coverage.ts` para que `totalInc`, `seenInc` e `notCovered` considerem estritamente as aulas do concurso.
- **Validação:** O script `web/scripts/compare-plans-main.ts` executou uma matriz de 48 cenários legados (CBMPE_OFICIAL, CBMPE_SOLDADO, PMPE_OFICIAL, PMPE_SOLDADO com 15h, 25h, 40h, níveis 0 e 2, com e sem Turbo) contra a branch `main`: **exatamente 0 divergências** de minutos, atividades ou cobertura.

### 5.2 Bloqueante 2: Escopo de Contabilidade Geral, Matemática em RL e Lacunas
- **Contabilidade Geral:** Auditoria detalhada dos itens 1 a 10 do edital. Aulas cobrindo normas societárias avançadas (`a09` CPC 01, `a10` CPC 04, `a12` CPC 25, `a14` Reservas de Capital, `a15` Reservas de Lucros, `a18` CPC 00 R2, `a19` CPC 26) marcadas com `edital: "partial"` e notas pedagógicas justificando o escopo.
- **Raciocínio Lógico & Matemática:** O edital Cebraspe (subitem 22.2.3.2) cobra 15 itens combinando matemática elementar e lógica sentencial. `matematica` foi adicionada a `CONTEST_SUBJECTS.PCPE_AGENTE`, com as aulas não pertinentes (`a06`, `a07`, `a12`, `a13`, `a16`, `a17` e complementos `c01`/`c02`) excluídas via `excludeContests: ["PCPE_AGENTE"]`.
- **Lacunas (`content/gaps.json`):**
  - `da-processo-adm`: mapeado explicitamente ao Item 10 do edital (Processo Administrativo Estadual Lei 11.781/2000 e Federal Lei 9.784/1999).
  - `leg-penal-eca`: detalhado como aspectos penais e procedimentais policiais (diferenciando de `dc-eca` do CBMPE).
  - `rl-matrizes-sistemas-lineares`: registrada lacuna média não resolvida para itens 5 e 15 do edital.
  - `est-tamanho-amostral`: registrada lacuna média não resolvida para o item 3.2 do edital.
  - `inf-deep-dark-web-discussao`: registrada como resolvida via resumo analítico de `informatica/a00`.

### 5.3 Bloqueante 3: Neutralidade Pedagógica Total
- Removidas menções a professores e equipes nos títulos das aulas através de higienização automatizada em `pipeline/build_catalog.py` (`clean_title`).
- Removidas menções a professores dos comentários e notas em `content/overrides/`.
- Adicionado teste automatizado de neutralidade em `pipeline/tests/test_content.py` (`test_titles_and_notes_are_neutral`), aprovado com sucesso.

### 5.4 Reestruturação da Prova Objetiva e Simulados (Cebraspe)
- Atualizado `EXAM_CONFIGS.PCPE_AGENTE` em `web/src/lib/simulado-rules.ts`:
  - **Bloco I (P1 — Noções de Direito, 20 questões):** Legislação PCPE (4), Direito Constitucional (4), Direito Administrativo (4), Direito Penal (3), Legislação Penal Especial (2), Direito Processual Penal (3).
  - **Bloco II (P2 — Conhecimentos Específicos, 40 questões):** Língua Portuguesa (10), Informática (10), Contabilidade Geral (10), Raciocínio Lógico (3), Matemática (3), Estatística (4).
  - **Critérios de Corte:** 60 questões no total, corte de 30 pontos (50%), `minPercentPerBlock: 0`, `noZeroInAnyArea: false`.
- Tornou-se opcional o campo `blocks.III` na interface `ContestExamConfig`, adaptando `simulados-view.tsx` e `resultado/[id]/page.tsx` para suporte dinâmico a 2 ou 3 blocos.

### 5.5 Resultados da Bateria de Verificação
- `npm run typecheck`: 0 erros.
- `npm test -- --project unit`: 462 testes unitários aprovados em 43 arquivos.
- `pipeline/test_plan_pcpe.ts`: 18 de 18 cenários aprovados com veredicto `LIBERAR` e 0 erros de integridade.
- `compare_importance_main.py`: 0 discrepâncias em 897 trechos legados.
- `compare-plans-main.ts`: 0 divergências em 48 cenários.
- `npm run build`: Build Next.js Turbopack com sucesso (código 0).

## 6. Rodada 4 de Correções (Outubro/2026) — Robustez e Consolidação Final

### 6.1 Robustez do Filtro por Concurso no Banco de Produção (Solução A)
- **Decisão:** Implementação da Solução (a), persistindo `onlyContests` e `excludeContests` no banco relacional.
- **Implementação:**
  - Adicionadas colunas `onlyContests TEXT[] @default([])` e `excludeContests TEXT[] @default([])` no modelo `Aula` de `web/prisma/schema.prisma`.
  - Criada e aplicada a migração `20261017130000_aula_contest_filters`.
  - Atualizados `web/prisma/seed-structure.ts` e `web/prisma/seed.ts` para persistirem os filtros durante o processo de seed idempotente.
  - Atualizado `web/src/lib/data/planner-data.ts` para carregar `onlyContests` e `excludeContests` em `CatalogAula` no runtime de produção.
- **Benefício:** Elimina a fragilidade da dependência do fallback exclusivo de importância (evita que eventuais aulas práticas sem trechos ou segmentos pontuais vazem para outros concursos).

### 6.2 Modo Dual no Comparador de Planos (`compare-plans-main.ts`)
- Implementado comparador com modo dual:
  1. `FIXTURES`: testa os planos com os campos nativos do catálogo.
  2. `COMO NO BANCO`: purga programaticamente `onlyContests` e `excludeContests` de `branchCat` antes de invocar o planejador para validar a robustez do fallback por importância.
- Tolerância de cobertura ajustada para `1e-6` (isolando resíduos de arredondamento de float de ~1.6e-8 sem mascarar regressões de planejamento).
- **Resultado:** 96 cenários executados (48 em fixtures + 48 como no banco) com **exatamente 0 divergências** em relação à `main`.

### 6.3 Generalização da Limpeza de Títulos (`clean_title`)
- Higienização de títulos em `pipeline/build_catalog.py` generalizada com expressões regulares para eliminar menções a professores (`- Prof./Professor(a) <Nome>`), equipes (`- Equipe <Nome>`) e mídias (`- Somente (em) PDF`, `(Somente em PDF)`).
- Preservadas intencionalmente as 3 exceções legadas herdadas da `main` (`biologia/a16`, `biologia/a17` e `direito-constitucional/a18`) para submissão à decisão do Dono do Produto.

### 6.4 Auditoria e Correção de Lacunas (`content/gaps.json`)
- `inf-deep-dark-web-discussao`: auditado e confirmado como **Falso Alarme**. O material-base `informatica/a00` já cobre integralmente os temas nas páginas 8 (grupos de discussão), 18–20 (teoria Deep/Dark Web/Tor), 60 (resumo) e 97, 103 (questões comentadas). Resumo analítico elaborado por Claude Sonnet 5.5 no commit `b40cb70`.
- `da-processo-adm`: ajustada a descrição da evidência para esclarecer que o item 10 do edital da PCPE traz a rubrica genérica "Processo administrativo" (sem números de leis). O curso-base supriu a Lei Estadual nº 11.781/2000 (`a23`) e o MentorIA complementou com a Lei Federal nº 9.784/1999 (`c02`), muito cobrada pelo Cebraspe.

### 6.5 Pesos de Disciplina Documentados como Estimativa de Projeto
- Documentado em `content/contests.json`, `web/content/contests.json` e `web/scripts/export-contests.ts` que o subitem 7.1.1 do edital PCPE fixa apenas `P1 = 20` (Noções de Direito) e `P2 = 40` (Conhecimentos Específicos).
- As quantidades individuais por matéria são estimativas técnicas de projeto do MentorIA:
  - Raciocínio Lógico (3) + Matemática (3) desmembrando o bloco RLM de 6 questões.
  - Estatística fixada em 4 questões (baseada em provas anteriores Cebraspe para carreiras policiais).

### 6.6 Rótulos de Perfis e Coluna Fixação no `pipeline/test_plan_pcpe.ts`
- Perfis atualizados para a nomenclatura oficial: `0: Iniciante`, `1: Básico`, `2: Intermediário`, `3: Domina`.
- Adicionada a coluna `Fixacao` na tabela de resultados da verificação.
- Execução de 24 cenários (4 perfis × 3 cargas × 2 turbos) aprovada com 100% de veredito `LIBERAR` e 0 erros de verificação independente.

### 6.7 Homologação e Verificação da Rodada 4
- `npm run typecheck`: 0 erros.
- `npm test -- --project unit`: 462 testes unitários aprovados (43 arquivos).
- `npm run lint`: 9 erros exatamente iguais à baseline da `main`.
- `pipeline/compare_importance_main.py`: 0 discrepâncias em 897 trechos legados.
- `web/scripts/compare-plans-main.ts`: 0 divergências em 96 cenários (modos fixtures e como no banco).
- `pipeline/test_plan_pcpe.ts`: 24 de 24 cenários aprovados com LIBERAR.
- `npm run build`: Build de produção Next.js Turbopack finalizado com sucesso (código 0).

## 7. Rodada 5 de Correções (Outubro/2026) — Alinhamento Fino do Edital e Priorização de Conteúdo

### 7.1 Importância Corrigida com Matemática no PCPE Agente
- **Problema:** `content/importance/segments.json` não havia sido recalculado após a ativação de `matematica` no PCPE Agente, mantendo os 76 trechos de Matemática com `appears: false` para o concurso.
- **Solução:**
  - Regenerada a importância via `pipeline/importance.py`, ativando 44 trechos de Matemática com `appears: true` no `PCPE_AGENTE`.
  - Criado teste invariante no pytest (`test_all_exam_subjects_have_appearing_segments` em `pipeline/tests/test_content.py`), garantindo que nenhuma disciplina com peso na prova fique sem trechos ativos no respectivo concurso.
  - Arquivo espelhado em `web/content/importance/segments.json`.

### 7.2 Alinhamento Cirúrgico das Disciplinas Comuns ao Edital do Agente
- **Mapeamento Próprio:** Criados 7 arquivos em `content/edital/pcpe/` (espelhados em `web/content/edital/pcpe/`), cobrindo item a item o subitem 22.2.3 do edital da PCPE sem alterar os mapas do CBMPE/PMPE:
  - `lingua-portuguesa.json`, `informatica.json`, `raciocinio-logico.json`, `matematica.json`, `estatistica.json`, `direito-constitucional.json`, `direito-administrativo.json`.
- **Inclusão da Aula 13 de Língua Portuguesa:** Incluída a aula `lingua-portuguesa/a13` (Manual de Redação da Presidência da República / Redação Oficial) com `onlyContests: ["PCPE_AGENTE"]`, dividida estritamente em 6 trechos de 14 a 17 páginas.
- **Exclusões de Conteúdos Fora do Edital:**
  - **Língua Portuguesa:** `a12` (variação linguística), `c01` (figuras de linguagem), `c02` (formação de palavras).
  - **Direito Constitucional:** `a16` (ordem social), `a17` (controle de constitucionalidade) e complementos autorais `c01` a `c05`.
  - **Informática:** `a14` (hardware e arquitetura), `c01` (prompt e periféricos).
  - **Estatística:** `a07` a `a10` (distribuições de probabilidade contínuas/discretas fora do escopo do Agente).
  - **Direito Administrativo:** `c01` (Lei 8.112/1990 pura), visto que o regime dos policiais civis de PE é regido pelo Estatuto Estadual (Lei 6.123/1968).
- **Ajustes de Lacunas (`content/gaps.json`):**
  - Adicionada lacuna `rl-operacoes-conjuntos` (subitem 1 do edital de RLM / Aula 08 não baixada do pacote 361849).
  - Refinada `rl-matrizes-sistemas-lineares` para `rl-matrizes-determinantes` (sistemas lineares já contemplados em `matematica/a08`).
- **Proporcionalidade dos Complementos:** Ajustado `pipeline/build_complements.py` para preservar a proporção exata `raw_base_sum * d.weight * block_weight`, eliminando qualquer distorção na base comum.

### 7.3 Arquitetura de Classificação Multiconcurso
- Desenvolvido e validado teste de arquitetura `pipeline/tests/test_multicontest_classifier.py` com 3 cenários de roteamento:
  1. Questão Cebraspe de Licitações (Lei 14.133/2021) classifica para `direito-administrativo/a20` ou `a21` na PCPE.
  2. Questão AOCP de Licitações no CBMPE nunca vaza para as aulas exclusivas da PCPE.
  3. Questão do ECA classifica em Direito Constitucional no CBMPE e em Legislação Penal Especial na PCPE.

### 7.4 Diretriz do Dono do Produto: Foco Exclusivo em Atividades, Bizus e Resumos
- O download de cadernos de questões Cebraspe do TecConcursos foi postergado pelo Dono do Produto para execução posterior.
- O foco integral do projeto passa a ser a catalogação de todas as atividades do edital, a garantia de que os planejamentos possam ser montados e a produção massiva dos Bizus (`content/items/`) e Resumos Analíticos (`content/summaries/`) dos 657 trechos ativos da PCPE.

### 7.5 Conclusão da Produção Massiva: 100% dos 657 Trechos com Bizus e Resumos Analíticos
- **Mobilização de Agentes Especialistas em Paralelo:** 7 subagentes executaram a geração e validação rigorosa de conteúdo pedagógico a partir dos PDFs do material-base:
  1. `legislacao-pcpe`: 12 trechos (96 itens C/E, 9.121 palavras).
  2. `legislacao-penal-especial`: 29 trechos (232 itens C/E, 26.525 palavras).
  3. `direito-processual-penal`: 38 trechos (304 itens C/E, 29.806 palavras).
  4. `contabilidade-geral`: 44 trechos (352 itens C/E, 24.944 palavras).
  5. `direito-administrativo` (aulas exclusivas `a20`..`a24`, `c02`): 47 trechos (376 itens C/E, 39.357 palavras).
  6. `raciocinio-logico` (`a00`..`a07`) + `lingua-portuguesa` (`a13`): 76 trechos (40.461 palavras).
  7. `direito-penal`: 69 trechos (552 itens C/E, 44.791 palavras).
- **Inventário 100% Concluído (`docs/inventario_pcpe.json`):**
  - Total de trechos ativos no `PCPE_AGENTE`: **657 trechos**.
  - Bizus (`content/items/`): **657 / 657 (100.0%)** — 0 pendências.
  - Resumos Analíticos (`content/summaries/`): **657 / 657 (100.0%)** — 0 pendências.
  - Todas as 12 disciplinas com 100% de cobertura.
- **Validação Estrita:** 100% dos arquivos validados via `pipeline/validate_content.py` e `pipeline/validate_summaries.py` com zero erros de esquema, integridade de fingerprints e conformidade de originalidade.
- **Banco de Dados Local Sincronizado (`prisma/seed-structure.ts`):** 1.142 bizus, 9.913 itens C/E e 1.076 resumos analíticos carregados com sucesso no banco de dados relacional local (`npx prisma dev`).
- **Homologação Completa:**
  - `npx tsc --noEmit`: 0 erros.
  - `npx vitest run --project unit`: 462 de 462 testes aprovados.
  - `npx tsx pipeline/test_plan_pcpe.ts`: 24 de 24 cenários com 100% `LIBERAR` e 0 erros.
  - `npx tsx web/scripts/compare-plans-main.ts`: 96 de 96 cenários com 0 divergências em relação à `main`.
  - `npm run build`: Build de produção Turbopack do Next.js finalizado com código 0.





## 8. Rodada 6 (19/10/2026) — Auditoria de qualidade, complementos e mapa do edital do Agente

### 8.1 Auditoria de qualidade dos resumos e bizus
- Triagem automática (`pipeline/pcpe_triage.py`, `pipeline/pcpe_tools/audit_pcpe.py`, `val_pcpe.py`) mais leitura por amostragem encontrou conteúdo gerado a partir do **título do tópico** (e não do texto-fonte) em várias disciplinas: itens C/E preenchedores ("Em relação a Aplicações Práticas…"), ponteiros genéricos ("Conceitos Estruturantes (Foco 1)…"), resumos que não correspondiam às páginas do trecho e sequências copiadas do material.
- Foram **refeitos, lendo o texto-fonte trecho a trecho**: Contabilidade Geral (a00–a19), Direito Processual Penal (a00–a03), Direito Penal (a04–a10), Legislação Penal Especial (a11–a21 e ECA penal), Legislação da PCPE (a01, a03–a07; a02 e c01 conferidos), Direito Administrativo (a20–a24; o complemento c02 foi conferido e mantido), Língua Portuguesa a13 e **Raciocínio Lógico inteiro** (a00–a07, 70 trechos). Cada trecho tem resumo analítico, sintético (Bizu), 8 itens C/E e ponteiros de página reais. Estado final: `validate_content.py`, `validate_summaries.py` e `pipeline/pcpe_tools/runs.py` sem erros nas 12 disciplinas do PCPE.
- Rascunhos versionados em `pipeline/pcpe_tools/drafts/` (uma refação por trecho); método e ferramentas em `PCPE-PROGRESSO.md`.

### 8.2 Dúvidas do material-base (para revisão humana; nenhuma altera o gabarito)
- **Raciocínio Lógico:** (1) a01/s07–s08, questão da UFRGS: a coluna da tabela 3 de (p ∨ ~q) → (p ∧ ~q) vem impressa como F, F, F, F; o cálculo correto é F, V, V, F. (2) a02/s03, questão da AGENERSA: a negação aparece como "~c ∨ s" e deveria ser "~c ∧ s". (3) a04/s09 (Consulplan/Prodabel): a afirmação III é chamada de "condicional falsa", mas é uma conjunção verdadeira. (4) a04/s03, questão da PF: a premissa 3 é chamada de "f" quando é "d" (o número de linhas, 8, não muda). (5) a06/s05: o desarranjo de 3 elementos é escrito como "D4 = 3! × …" (deveria ser D3). (6) a06/s06: no texto da combinação completa, "5 − 1 + 3" é dado como 8 (o correto é 7). (7) a04/s05: "inocente" e "culpado" são tratados como negações exatas, o que não vale em geral.
- **Legislação Penal Especial:** (a) o Tema 506/RE 635.659 foi tratado só para a maconha (40 g / 6 plantas), e a aula chama o art. 28 de sanção administrativa; (b) em a18/s04 o tráfico privilegiado aparece como "1/6 a 1/3", mas a lei diz 1/6 a 2/3; (c) Lei 9.605, art. 60: a aula traz duas penas diferentes (6 meses a 2 anos, com aumento por EIA × 1 a 6 meses); adotou-se o texto mais recente.
- **Direito Penal a06 (s05–s06):** a fonte não mostra se a Lei 15.280/2025 alterou as penas dos arts. 227–230 e 232-A; mantiveram-se as da aula.
- **Direito Administrativo a22/s14:** o Tema 1.118 do STF aparece grafado "118" na fonte.

### 8.3 Complementos novos do Agente (`onlyContests: PCPE_AGENTE`)
Lacunas do edital sem aula no material-base, resolvidas com texto autoral (aulas `c`, PDF em `web/public/complementos/`, com resumo, sintético, 8 itens C/E e importância): `rl-operacoes-conjuntos` (item 14 de RL → `raciocinio-logico/c01`), `rl-matrizes-determinantes` (item 15, problemas matriciais → `raciocinio-logico/c02`), `est-tamanho-amostral` e `est-assimetria-curtose` (itens 1 e 3.2 de Estatística → `estatistica/c02`), `mat-divisao-proporcional` (item 3.1 → `matematica/c03`) e `dc-principios-fundamentais` (arts. 1º a 4º da CF → `direito-constitucional/c06`). Todas registradas em `content/gaps.json`.

### 8.4 Mapa edital → material do Agente refeito
Os sete arquivos `content/edital/pcpe/*.json` entregues antes tinham `where` inventado (aulas, páginas e tópicos inexistentes). Foram regenerados por `pipeline/pcpe_tools/build_edital_pcpe.py` a partir dos itens do edital oficial e dos trechos reais (códigos = numeração do edital; Raciocínio Lógico e Matemática dividem o bloco "Raciocínio Lógico"): RL 12 itens, Matemática 11, Estatística 5, Direito Constitucional 14, Direito Administrativo 20, Língua Portuguesa 21 e Informática 12. Itens tratados em outra disciplina (segurança pública na CE-PE; disposições constitucionais do agente público) ficam `elsewhere`. Sistemas lineares (Matemática 5) está `partial`: a escrita matricial e a regra de Cramer estão no complemento de matrizes.

## 9. Questões do PCPE (19/10/2026)

- **Cadernos novos importados (local):** 11 PDFs do TecConcursos baixados em 19/10 (Contabilidade Geral, Direito Penal, Legislação Estadual de PE e ECA; 2.000 questões: Cebraspe 846, FGV 918, FCC 236). `content/questoes/mapa-assuntos.json` ganhou as matérias *Direito Penal* → `direito-penal`, *Contabilidade Geral* → `contabilidade-geral`, *Direito Administrativo Estadual e do DF*, *Direito Constitucional Estadual e Distrital* e *Segurança Pública e Legislação Policial* → `legislacao-pcpe` (LC 150/2009 e "outros normativos" descartados). A importação rodou só no banco local (a produção não foi tocada). O acervo total passou a 7.971 questões aprovadas.
- **Banca do PCPE:** `contestBancas('PCPE_AGENTE')` aceita Cebraspe (inclusive a grafia `CEBRASPE (CESPE)`), AOCP e as inéditas MentorIA, provisoriamente, até haver cadernos Cebraspe suficientes.
- **Assuntos do edital sem questão no sistema:** antes das inéditas, 37 dos 140 assuntos do Agente (cinco disciplinas inteiras: Contabilidade, Direito Processual Penal, Legislação Penal Especial, Legislação do PCPE e Direito Penal) não tinham nenhuma; depois, só os dois "tratados em outra disciplina" (CE-PE em Direito Constitucional e disposições constitucionais do agente público em Direito Administrativo, ambos com questões na disciplina de origem).
- **Questões inéditas MentorIA:** 485 questões certo/errado (239 C, 246 E) no padrão Cebraspe aprendido nas 610 questões C/E do acervo (frase de abertura "julgue o item…", uma assertiva por questão, mediana de 46 palavras, pegadinhas de número, prazo e palavra absoluta), com comentário. Cobrem 51 assuntos, 8 ou mais por assunto. Marcadas em `Question.banca = "Inédita MentorIA"` e `batch = mentoria-inedita-2026-10-19`. Fonte versionada em `content/questoes/ineditas/*.txt`; gravação por `web/scripts/questoes-ineditas.ts`. **Revisão humana recomendada:** foram escritas a partir dos resumos do curso e da legislação; conferir principalmente números e prazos das leis recentes.
- **Para trocar pelas reais:** baixar os cadernos de `PCPE-CADERNOS-TEC.md`, importar e rodar `questoes-ineditas.ts --aposentar`.


### 9.1 ECA no PCPE (20/10/2026)
- Os assuntos de ECA com conteúdo penal e processual (ato infracional, direitos individuais, garantias processuais, medidas socioeducativas e remissão; 63 questões) passaram do complemento de ECA do CBMPE (`direito-constitucional/c01`) para o complemento de ECA penal do PCPE (`legislacao-penal-especial/c01`), por `content/questoes/mapa-assuntos.json` + `importar.py --reclassificar`. Os demais assuntos de ECA (guarda, adoção, conselho tutelar, saúde, educação, procedimentos) continuam no CBMPE. As 8 inéditas do item 12 foram aposentadas (`questoes-ineditas.ts --aposentar`).
- Testes de integração de preço ajustados ao desconto de lançamento de 25% (Oficial/PCPE R$ 90, Praça R$ 60; com cupom de parceiro, R$ 72 e R$ 48).
- A frente de classificação por agentes (extrator 2026.10.16-1, overrides, scripts de pacotes e prioridades) foi commitada.

### 9.2 Prova de múltipla escolha, simulado e teste ponta a ponta (20/10/2026)
- **Correção:** o edital do PCPE (item 8.2) define a prova objetiva como **múltipla escolha com cinco alternativas**, 60 questões (P1 Noções de Direito: 20; P2 Conhecimentos Específicos: 40), 1 ponto cada, mínimo de 30 pontos. A afirmação anterior de que a prova seria certo/errado estava errada; o `EXAM_CONFIGS` do PCPE (`simulado-rules.ts`) já seguia o edital. O módulo de simulados continua desligado por `SIMULADOS_ENABLED = false` (decisão do dono).
- **Inéditas em múltipla escolha:** `pipeline/questoes/ineditas_mc.py` compõe 50 questões de 5 alternativas (1 certa + 4 erradas, ou 4 certas + 1 "incorreta") a partir das assertivas certo/errado do mesmo assunto; ficam na produção e no banco local. Com elas, todas as disciplinas da prova do PCPE têm questões de múltipla escolha suficientes para montar um simulado (Direito Processual Penal: 16; Legislação Penal Especial: 14). Conversão completa das inéditas para múltipla escolha segue pendente.
- **Teste ponta a ponta (conta PCPE de teste, banco local):** o assistente de plano mostrava a "Língua Estrangeira" e os "Blocos I a III" do CBMPE, e a data da prova padrão era 28/02/2027. Corrigido: blocos P1 e P2 do edital, sem língua estrangeira, data 07/03/2027 (`ContestSetting.examDate`). O Banco de Questões mostrava ids crus (`direito-penal`), blocos do CBMPE e assuntos do edital do CBMPE; agora usa os nomes, os blocos da prova e os **assuntos do edital do PCPE** (as questões de aulas que o edital do PCPE trata entram nos assuntos próprios dele: `lib/quiz/topic-map.ts`). O treino por assunto e o caderno personalizado usam o mesmo mapeamento.
- **Seed:** `seed-structure.ts` passou a atualizar título, ordem e aulas dos assuntos do edital já semeados e a aposentar assuntos próprios (`/p`) que saíram do mapa (apaga se ninguém usa; senão, inativa). Antes, `createMany` ignorava mudanças e o banco local mantinha títulos do mapa antigo.
- **Achado:** alguns trechos de Direito Penal têm zero questões (o caderno da atividade fica vazio); `pipeline/questoes/lacunas.py` lista os trechos com menos de 5 questões.


## 10. Finalização do PCPE (21/10/2026)

### 10.1 Inéditas na produção
- 409 inéditas de múltipla escolha novas gravadas na produção (2.013 atualizadas), com backup íntegro antes (`backups/questoes-remoto-20261021-031903`). Total: 2.999 inéditas. A regra de completar caderno curto com trechos já estudados da mesma disciplina está na `main` (e4cf70d). A conferência visual de um caderno curto no app exige sessão de aluno e não foi feita; a regra tem testes em `logic.test.ts`.

### 10.2 Os 76 resumos em rascunho
- Relatório por trecho em `content/audit/pcpe-resumos.md` (tipo a/b/c, ação, cobertura, dúvidas). Todos seguem `DRAFT`. Foram corrigidos erros do resumo anterior: audiência de custódia agora por videoconferência (Lei 15.358/2026), transação penal não é direito subjetivo, rito sumaríssimo com até 5 testemunhas, lei de recorrência de Matemática (a perda de expoente na extração do PDF trocava 2^n por 2n), Manual de Redação (regras inexistentes no Manual), Lei 9.605 (arts. 49, 60 e 67), EC 139/2026 e LC 219/2025.
- **Atenção à nota de cobertura**: nos guias de método de Raciocínio Lógico ela cai de propósito (não repetem nomes dos enunciados).
- **Pendência técnica**: a extração dos PDFs pode ter perdido expoentes e índices em outras disciplinas exatas. Vale conferir as fórmulas de Estatística, Matemática e Contabilidade na revisão humana.
- Dúvidas do material registradas em `notes` de cada aula (ex.: Lei 15.371/2026 licença-paternidade; Lei 15.142/2025 e o "mais de duas vagas" do STF; conflito entre o Manual de Redação e o Decreto 9.758/2019).

### 10.3 Questões reais do TecConcursos (cadernos de 20 e 21/10)
- 20 cadernos ("Caderno Falta adm 1–10" e "Caderno Falta Matemática, Consti, Penal, Racio e Adm 1–10"): 3.859 questões, 0 anuladas, 0 quarentena. **Só 309 são Cebraspe**; o resto é FGV, Quadrix, Fundatec, VUNESP, Consulplan, AOCP e outras. O caderno das atividades do PCPE usa só Cebraspe e AOCP; as demais bancas servem ao treino livre.
- `mapa-assuntos.json`: `Direito Processual Penal` passou a mapear para `direito-processual-penal` (517 questões: 397 aprovadas, 120 rascunho). Não importadas: Engenharia Elétrica (399) e Direito Digital (48), sem mapa nem aula; licitações (Lei 14.133) e improbidade seguem `skip`.
- Importação no banco local (11.920 questões) e, com autorização do dono, na **produção** em 21/10/2026: 3.702 criadas, 16 atualizadas, 141 iguais, 934 figuras, nenhum trecho ausente (backup íntegro `backups/questoes-remoto-20261021-185538`). 18 questões com defeito de extração foram para rascunho e 29 inéditas foram aposentadas (N = 8, Cebraspe/AOCP por trecho). Contagem após: 10.825 aprovadas e 1.095 em rascunho do TEC, 2.928 inéditas ativas.
- Auditoria (`auditoria.py`, backup de 21/10): nos 20 cadernos, 24 questões com defeito real de extração (perda de texto, enunciado vazio, alternativa duplicada, referência visual sem figura) listadas em `docs/questoes/auditoria/2026-10-21/problemas-novos.csv`; `web/scripts/questoes-marcar-rascunho.ts` as manda para `DRAFT` (14 estavam aprovadas; feito no local). As 113+76 ocorrências de "texto virou imagem/recorte" são só de legibilidade.
- `questoes-ineditas.ts --aposentar` passou a contar só as reais **Cebraspe/AOCP por trecho** (as demais bancas não entram no caderno do plano) e ganhou `--simular`. Com N = 8, 29 inéditas passam do limite (6 trechos); simulação de cadernos: 0 curtos em 8.348.

### 10.4 Verificações
- typecheck e 576 testes (vitest) passando; eslint limpo nos scripts alterados; `compare-plans-main.ts`: 0 divergências em 96 cenários (com a `main` atualizada); `pcpe-plan-test.ts`: 10 de 10 planos LIBERAR; `audit_planos.py`: 0 cadernos que não abrem (a coluna "menores que o pedido" desse script ignora a regra de completar do app).
- `pytest`: 5 falhas que não vêm desta rodada (`test_complements` ×2, `test_content` ×3, entre elas as inéditas de atualidades com C/E repetido, já conhecida).
- `validate_summaries.py`: havia 35 arquivos com "impressão digital diferente" (só o nome do tópico inicial mudou depois da resegmentação, as páginas batem); corrigidos.
- `verify-plans.ts --remoto --apply`: 1 plano real em análise (PCPE, 38 h/semana), LIBERAR, ativado com autorização do dono. Os 35 resumos com impressão digital desatualizada (agora 36 arquivos) tiveram só o `startTopic` atualizado (commit 7751004): `validate_summaries.py` sem erros. Push na `main`: 6f6bf00.

## 11. Cadernos completos no CBMPE Oficial (21–22/10/2026)

- **Levantamento** (produção, só leitura, `web/scripts/cadernos-auditoria.ts`): PCPE sem caderno curto; CBMPE Oficial com 405 de 2.038 cadernos abaixo de 25 nos 14 planos reais (Informática 13 e Biologia 18 reproduzidos). Causa: caderno só aceitava AOCP e o CBMPE não recebia inéditas.
- **Regra nova** (`web/src/lib/quiz/banca.ts`, `pool.ts`, `logic.ts`): AOCP do caderno → AOCP de trechos já estudados → reforço (múltipla escolha de outras bancas e inéditas MentorIA, dos trechos do caderno e dos já estudados). Vale para `CBMPE_OFICIAL` e planos antigos sem concurso (`REFORCO_CONTESTS`); os demais concursos ficam como estavam. Só com a regra, 405 → 180 cadernos curtos.
- **1.771 inéditas novas de múltipla escolha** (401 trechos abaixo de 7; Química 419, Espanhol 232, Direito Penal Militar 196, Matemática 176, Estatística 165, Física 151, Biologia 135, Inglês 104, Português 51, Direito Administrativo 39, Direito Constitucional 39, Informática 36, Legislações PE 28), em `content/questoes/ineditas/mc/`. Briefing `pipeline/briefs/ineditas-cbmpe.md`; acompanhamento `pipeline/questoes/lacunas_cbmpe.py`; relatórios de revisão `content/questoes/ineditas/REVISAO-2026-10-21-cbmpe-*.md` (dúvidas do material para o dono). Com elas, 405 → **57** cadernos curtos (simulação).
- **O que sobra**: o primeiro caderno da disciplina em aulas de 2 ou 3 trechos (sem trecho anterior para completar). Fechar 100% exige ~975 questões a mais (88 aulas) ou uma regra de último recurso (completar com trechos ainda não estudados). `ineditas_mc_nativas.py --check` passou a tratar "trecho sem assunto do edital" como aviso (a questão fica com `editalItemId` nulo e só aparece no caderno do plano).
- Pendente de aprovação do dono antes da produção: gravar o lote (`ineditas_mc_nativas.py --json` + `questoes-ineditas.ts --retirar-ausentes --remoto`, com backup) e publicar a regra nova.

### 11.1 Atualização (22/10/2026)
- **Publicado:** as 4.193 inéditas de múltipla escolha (1.771 novas + 2.422 já existentes) estão na produção (backup `backups/questoes-remoto-20261022-163224`) e a regra de reforço do caderno está na `main` (64fcc33).
- **Segunda leva (ainda NÃO gravada na produção):** 983 inéditas para que a soma dos até 4 primeiros trechos de cada aula chegue a 25 (88 aulas; Física 212, Espanhol 142, Direito Penal Militar 125, Química 118, Legislações PE 102, Direito Constitucional 88, Biologia 60, Português 52, Inglês 46, Informática 21, Matemática 8, Estatística 4). Briefing `pipeline/briefs/ineditas-cbmpe2.md`, acompanhamento `pipeline/questoes/lacunas_cbmpe_aula.py`, revisões `content/questoes/ineditas/REVISAO-2026-10-22-cbmpe2-*.md`. Simulação nos 14 planos reais: **0 cadernos abaixo de 25** (de 405 no início).
- **Limites da garantia:** vale para aulas estudadas desde o primeiro trecho. Um plano que começa a disciplina no meio de uma aula (por exemplo, Turbo com 15 questões) pode ainda faltar 1 ou 2 questões; o levantamento (`web/scripts/cadernos-auditoria.ts`) deve ser rodado a cada plano novo.

### 11.2 Cadernos do TEC de 22/10/2026 (importados em 23/10)
- 11 PDFs ("Caderno Falta adm 11–15", "Caderno Falta Matemática, Consti, Penal, Racio e Adm 11–15" e "Caderno CONT GERAL, DIR PENAL, LEG PEN ESP 11"): 1.999 ocorrências, **só 16 questões novas** (as do caderno de Contabilidade/Penal/Legislação Penal Especial); o resto repete questões já importadas. 0 anuladas, 0 quarentena.
- Local e produção (backup `backups/questoes-remoto-20261023-032947`, `--confirmo-producao`): 16 criadas, 5 a 56 atualizadas, 6 figuras novas, nenhum trecho ausente. Auditoria: 1 defeito novo de extração (alternativa duplicada, tec 3202040), enviado para rascunho; os outros 16 já estavam tratados.
- **Aposentadoria de inéditas não aplicada.** A gravação do lote de 22/10 (`--retirar-ausentes`) reativou as 29 inéditas aposentadas em 21/10, e a contagem de reais Cebraspe/AOCP por trecho (N = 8) hoje listaria 65. Mas o CBMPE Oficial usa inéditas como reforço e não aproveita Cebraspe certo/errado: aposentá-las pode reabrir cadernos curtos do CBMPE. `questoes-ineditas.ts --aposentar` agora exige `--sei-do-cbmpe` (e `--simular` lista sem gravar). Levantamento em produção depois da importação: CBMPE 0 cadernos abaixo de 25 em 2.098; PCPE 0 em 137.

## 12. Pacotes combo CBMPE e PMPE (23/10/2026)

- **O que é.** `CBMPE_COMBO` e `PMPE_COMBO`: um plano único para o 2º Tenente e o Soldado da mesma corporação. O aluno escolhe qual concurso é a prioridade; se o tempo não fechar o edital, o prioritário é mais atendido (peso 2:1) e o outro continua no plano, inclusive nas disciplinas que só ele cobra (piso por disciplina do motor).
- **Decisões do dono.** Preço original R$ 160 (R$ 120 no lançamento, R$ 96 com cupom de parceiro); prioridade com peso fixo, sem escolher intensidade; Soldado CBMPE como está (C13 à parte); sem migração do individual para o combo.
- **Sobreposição de conteúdo** (trechos com `appears`): CBMPE — comuns 321 (Português, Informática, Biologia, Direito Constitucional, Legislações PE), só Oficial 440, só Soldado 136 (Raciocínio Lógico, Atualidades, História PE). PMPE — comuns 320, só Oficial 244, só Soldado 3 (História PE).
- **Resultado do motor** (`web/scripts/combo-demo.ts`, nível 0, sem Turbo; cobertura 2º Tenente · Soldado): CBMPE 15 h — prioridade Oficial 40% · 50%, prioridade Soldado 35% · 56%; PMPE 15 h — 53% · 63% contra 49% · 67%. Todos os planos testados (15/25/40 h, com e sem Turbo) passam em `verifyPlan`.
- **Verificado:** snapshot dos 60 planos individuais idêntico antes e depois (`scripts/plan-snapshot.ts`); migrações aplicadas no banco de desenvolvimento; assistente, `/plano` e Desempenho conferidos no navegador com um usuário local.
- **Pendências.** Revisar o texto de venda dos combos nas páginas públicas (hoje o cartão diz "2º Tenente + Soldado · Combo"); aplicar as migrações e o seed na produção; decidir quando o combo PMPE deixa de ser "o Oficial mais História PE" (depende de estruturar o edital da PMPE).

## 13. Inclusão do CFOA (24/10/2026)

- **O que é:** Concurso interno para 2º Tenente CFOA do CBMPE (Quadro de Oficiais da Administração), 100 questões objetivas (50 Bloco I - Direito, 50 Bloco II - Conhecimentos Gerais), 9 disciplinas, sem língua estrangeira nem matérias de ciências da natureza/exatas além de Raciocínio Lógico.
- **Decisões do dono:**
  - Base no edital de 2023 (código próprio, edital próprio via `content/edital/cfoa/` com prefixo `f`).
  - Data da prova: ainda não divulgada (prevista para 2024/2025; no sistema, campo de data fica vazio até sair o edital; no onboarding, o assistente sugere hoje em Recife + 365 dias com InfoTip explicativo).
  - Preço: categoria `OFICIAL` (R$ 120 / R$ 90 lançamento / R$ 72 parceiro).
  - Banca da prova: qualquer banca com prioridade AOCP. Ordem do caderno: AOCP primeiro, seguido pelo reforço de outras bancas e inéditas MentorIA (`REFORCO_CONTESTS`).
  - Treino livre: aluno do CFOA vê as inéditas normalmente (`hideInedita("CBMPE_CFOA") = {}`).
  - Inéditas provisórias: redigir inéditas de múltipla escolha (padrão AOCP, 5 alternativas) para garantir cadernos completos em todas as 365 atividades (meta de >= 7 por trecho e >= 25 na soma dos 4 primeiros trechos de cada aula).
- **Correções do commit anterior (6c13e84 revertido):**
  - Isolamento de aulas exclusivas (`onlyContests: CBMPE_CFOA`): `direito-administrativo` (a00, a01, a03, a05, a07, a08, c01) e `lingua-portuguesa` (a13) para não poluir os outros concursos.
  - Correção na soma de fatias exclusivas em `build_catalog.py` e `build_complements.py` para calcular fatias por concurso, garantindo 0 divergência nos 5 concursos existentes.
- **Aulas e trechos por disciplina (365 trechos no total):**
  - `administracao` (NOVA): 8 aulas, 24 trechos.
  - `direito-administrativo`: 27 aulas, 119 trechos (inclui 7 aulas exclusivas: a00, a01, a03, a05, a07, a08, c01).
  - `direito-constitucional`: 15 aulas, 94 trechos.
  - `direito-penal-militar`: 15 aulas, 41 trechos (inclui novas: a20, a21, c02).
  - `direito-processual-penal-militar` (NOVA): 9 aulas, 15 trechos.
  - `direitos-humanos` (NOVA): 7 aulas, 13 trechos.
  - `legislacoes-pe`: 13 aulas, 13 trechos (inclui novos complementos c06 a c09).
  - `lingua-portuguesa`: 14 aulas, 62 trechos (inclui a13 Manual de Redação).
  - `raciocinio-logico`: 8 aulas, 70 trechos.
- **Complementos novos criados:**
  - `direito-processual-penal-militar/c01`: Organização Judiciária Militar Estadual em Pernambuco (LC 284/2014 e 353/2017).
  - `direito-penal-militar/c02`: Crimes em Licitações e Contratos Administrativos (arts. 337-E a 337-P do Código Penal).
  - `direitos-humanos/c01`: Convenção Interamericana contra o Racismo e toda Forma de Discriminação (Decreto 10.932/2022).
  - `direitos-humanos/c02`: Convenção sobre os Direitos das Pessoas com Deficiência (Decreto 6.949/2009).
  - `legislacoes-pe/c06`: Código de Ética Profissional dos Militares de Pernambuco (Decreto Estadual nº 22.114/2000).
  - `legislacoes-pe/c07`: Lei de Promoção dos Militares de Pernambuco (LC Estadual nº 470/2021).
  - `legislacoes-pe/c08`: Lei de Acesso à Informação (Lei Federal nº 12.527/2011).
  - `legislacoes-pe/c09`: Vedação ao Assédio Moral e Sexual no Serviço Público de Pernambuco (Lei Estadual nº 13.314/2007).
  - `administracao/c01`: Gestão Estratégica e BSC na Segurança Pública (PDD, BSC, OKR).
- **Bizus e Resumos Analíticos:**
  - 100% de cobertura nos 365 trechos do CFOA.
  - Validação `validate_content.py`: 0 erros.
  - Validação `validate_summaries.py`: 0 erros (58.302 palavras de resumo analítico adicionadas).
- **Questões Inéditas de Múltipla Escolha (1.333 novas questões):**
  - Mapeadas por trecho com comentários didáticos e 5 alternativas balanceadas (~20% por letra A-E).
  - `administracao`: 233 questões em 8 aulas.
  - `direito-processual-penal-militar`: 228 questões em 9 aulas.
  - `direitos-humanos`: 175 questões em 7 aulas.
  - `direito-constitucional`: 25 questões em 1 aula (a18).
  - `direito-administrativo`: 192 questões em 7 aulas.
  - `direito-penal-militar`: 158 questões em 5 aulas.
  - `legislacoes-pe`: 184 questões em 9 aulas.
  - `lingua-portuguesa`: 91 questões em 7 aulas.
  - `raciocinio-logico`: 47 questões em 5 aulas.
  - `ineditas_mc_nativas.py --check`: 6.509 questões totais, 0 erros.
  - `lacunas_cfoa.py --check`: 0 trechos < 7, 0 aulas < 25, 0 questões faltantes.
  - Gravadas no banco de dados local com lote `mentoria-inedita-2026-10-24-cfoa`. Relatório em `content/questoes/ineditas/REVISAO-2026-10-24-cfoa.md`.
- **Verificações e Testes:**
  - `compare-plans-main.ts`: 0 divergências nos 96 cenários de teste entre main e branch.
  - `plan-snapshot.ts`: 0 diferenças para os 5 concursos existentes contra `scratch/plan-snapshot-main.json`.
  - `compare_importance_main.py`: 0 discrepâncias nos trechos dos concursos existentes.
  - 12 planos de teste do CFOA (10/20/40h × iniciante/avançado × Turbo off/on): 100% LIBERAR em `verifyPlan`, sem erros, sem atividades de disciplinas proibidas e sem aulas excluídas.
  - `buildSpareReview` aprimorado com teto semanal para evitar `SEMANA_EXCESSO` em horizontes longos (52 semanas) mantendo rigorosamente `sum <= weeklyMinutes * 1.05`.
  - `vitest`: todos os testes unitários passando.


## 14. Questões do TecConcursos (rodada de 23/10), publicação do CFOA e revisão por amostra (24/10/2026)

- **Rodada de cadernos de 23/10:** 17.172 questões únicas (20.655 no total). `importar.py --so-extrair` + 33 agentes sobre os rascunhos (pacotes de `pacotes_rascunhos.py`, resultados em `docs/questoes/classificacao-agentes/2026-10-24/`, aplicados por `aplicar_agentes.py`): rascunhos de 1.430 para 168; 881 decisões em trecho, 381 `skip`, 162 de baixa confiança (continuam rascunho), 6 já decididas (preservadas). Resultado local: **13.197 aprovadas, 168 rascunhos, 3.473 fora do edital, 330 anuladas, 4 em quarentena**. Commit `9fc8793` (mapa de assuntos por banca, decisões, editais do CFOA que usam `title` em vez de `item`). **Nada gravado em banco** (nem local nem Neon) além do que está dito.
- **Mapa por banca (`outras_bancas` em `mapa-assuntos.json`):** AOCP segue o destino do CBMPE/PMPE; as demais bancas vão para a disciplina do PCPE (14 entradas, ex.: Maria da Penha, ECA). "Legislação Penal e Processual Penal Especial" e "Direitos Humanos" ganharam disciplinas próprias.
- **Lacunas abertas (trechos com < 5 questões / sem nenhuma):** Administração 37/37, Direito Processual Penal Militar 24/24, Direito Penal Militar 34/16, Atualidades 48/38, Contabilidade 31/26, Língua Espanhola 35/25, Química 68/34, Direito Administrativo 75/54, Estatística 39/15, Física 25/9, Informática 39/13, Matemática 37/15, Raciocínio Lógico 31/17, Língua Portuguesa 23/13, demais menores. A rodada de 23/10 não cobriu as disciplinas novas do CFOA (use `CFOA-CADERNOS-TEC.md`).
- **Achados dos agentes (decisões do dono pendentes):** Lei 9.099/1995 com 80 questões em `skip` (conteúdo ensinado em `direito-processual-penal/a06`: proposta de remapear); Estatuto da Pessoa Idosa (35), Lei Anticorrupção 12.846 (10) e Lei 13.019 (7) sem trecho; concurso de pessoas/de crimes e dosimetria sem trecho em Direito Penal; 14 questões de conjuntos (matemática) cujo trecho é de raciocínio lógico; 1 questão de licitações em `a22/s03` (licitações estão fora do edital); Engenharia Elétrica (399), LGPD (109) e LINDB (21) sem mapa.
- **CFOA em produção (main `a33ed64`):** migrações aplicadas pelo build da Vercel; backup íntegro antes; **6.509 inéditas gravadas no Neon** (1.333 novas do CFOA, 5.176 atualizadas). Planos do CFOA continuam retidos (`CONTESTS_HELD_FOR_REVIEW`).
- **Acesso sem prazo até a data da prova (decisão do dono, 24/10):** sem `ContestSetting.examDate`, a contratação paga libera o acesso **sem prazo** (`accessUntil = null`, `User.accessExpiresAt = null`); ao salvar a data em **Administração › Concursos**, `applyExamDateToContracts` define o limite (fim do dia da prova, Recife) de todos os contratantes (respeitando outras contratações do mesmo aluno) e acompanha mudanças de data. O estorno total encerra o acesso mesmo sem prazo. Substitui a regra anterior (sem data, o acesso aguardava liberação manual).
- **Página `/admin/concursos`:** um cartão por concurso (data da prova, contratações, contratações sem prazo; edita categoria, data, preço e desconto); a aba "Concursos e preços" saiu do Financeiro (redireciona). Nome, cargo e banca continuam no código.
- **`/concursos` (público):** contêineres por órgão (CBMPE, PMPE, PCPE), com CFOA no CBMPE, tom discreto por órgão e brasão cortado no card.
- **Revisão por amostra do conteúdo do CFOA** (`pipeline/briefs/revisao-amostral-cfoa.md`, relatório em `content/questoes/ineditas/REVISAO-2026-10-24-cfoa-amostral.md`): 325 inéditas auditadas; taxa de erro de fato 0% (Administração, Direitos Humanos, Constitucional, Português, Raciocínio), 3,4–3,6% (DPPM, Legislações PE, Dir. Administrativo) e **8,3% em Direito Penal Militar (revisar as 110 restantes)**; 7 questões corrigidas, 2 reescritas, 2 complementos ajustados; resumos e bizus amostrados sem erro. Os erros eram sobretudo **capitulação** (artigo/inciso/pena errados). Correções ainda **não regravadas na produção** (exigem autorização). Dúvida: o texto de CPM art. 191 II e Lei 13.869 art. 12 não pôde ser lido na fonte oficial.
- **Passagem para outro agente:** `pipeline/briefs/cfoa-conclusao.md` (revisão integral de DPM, regravação das inéditas, extração e inserção dos 11 cadernos novos de 24/10, itens menores).
- **Conclusão (25/10/2026), Etapa A:** revisão integral das 158 inéditas de Direito Penal Militar do CFOA contra o texto oficial (63 ajustadas, ~38 com erro de fato, taxa real ~24% contra 8,3% da amostra) e varredura automatizada de capitulação em Processual Penal Militar (31 corrigidas), Legislações PE (24, conferidas na ALEPE) e Direito Administrativo (nada a corrigir). Confirmados CPM art. 191, II, e Lei 13.869 art. 12, p.u., III/IV. PDFs dos complementos `leg-lei-12527-lai` e `leg-pe-lei-6783-lacunas` regenerados. Commit `8c7da0c`; relatório na seção 9 de `REVISAO-2026-10-24-cfoa-amostral.md`. **Inéditas corrigidas não regravadas** (local nem Neon): aguardam autorização.
- **Conclusão (25/10/2026), Etapa B — cadernos de 24/10:** 11 cadernos, 2.000 questões, 0 quarentena/anomalia; acervo 18.752 únicas. 493 rascunhos novos (os 168 já vistos em 24/10 foram excluídos dos pacotes) classificados por 10 agentes (`docs/questoes/classificacao-agentes/2026-10-25/`): 232 em trecho, 174 `skip`, 87 de baixa confiança (continuam rascunho). Classificação: **14.382 aprovadas, 255 rascunhos, 3.753 fora do edital, 358 anuladas, 4 em quarentena**. Banco **local**: 2.916 criadas, 21 atualizadas (só os cadernos novos; as decisões sobre questões antigas, inclusive as de 23/10, pedem `--reclassificar`, não rodado). Antes, o `search_path` do PGlite estava preso em `vitest_online` e foi restaurado para `public`. Achados: ~120 questões de Raciocínio Lógico de **sequências** e **associação/ordenação** sem trecho nem item de edital (lacuna de conteúdo); mais 9 do Estatuto da Pessoa Idosa. Lacunas (< 5 / nenhuma): Química 60/17, Português 14/10, Raciocínio 30/16; Administração 38/38, DPPM 25/25 e DPM 35/17 seguem sem cadernos do TEC. **Nada gravado no Neon.**
- **Produção (26/10/2026, com autorização do dono):** (1) inéditas corrigidas regravadas no Neon com `--retirar-ausentes` após backup íntegro (`backups/questoes-remoto-20261026-024837`): 87 criadas, 6.422 atualizadas, **87 aposentadas** (exatamente as de texto editado); também gravadas no banco local. (2) Cadernos de 25/10 (12 cadernos, ~2.000 questões, 1 quarentena; 1.087 de Direito Administrativo e 57 de Direito Penal Militar novas; 111 de Matemática Financeira sem mapa e ~300 de técnicas laboratoriais de Biologia fora do edital) e 213 rascunhos novos classificados por 5 agentes (`docs/questoes/classificacao-agentes/2026-10-26/`: 155 trecho, 51 `skip`, 7 baixa). (3) `importar.py --reclassificar` no local e depois `--so-remoto --reclassificar --confirmo-producao` (backup `backups/questoes-remoto-20261026-050620`): remoto 3.928 criadas, 327 atualizadas, 215 aposentadas, 300 figuras. Produção: **15.532 TEC aprovadas** (967 com decisão MANUAL preservada), 117 rascunhos, 7.034 inéditas aprovadas. Antes da importação local o `search_path` do PGlite estava em `vitest_online` (restaurado para `public`).
- **Auditoria de planos do CFOA:** `web/scripts/cfoa-plan-test.ts` gera 10 planos do CFOA a partir de `content/` (prova hipotética 28/03/2027) e roda o verificador: todos LIBERAR; cobertura máxima do edital 86% (parte do edital sem material). Relatórios de auditoria item a item em `pipeline/.cache/auditoria-cfoa/`.
- **`/concursos`:** brasão inteiro (sem recorte) dentro do card, com fade leve nas laterais.
- **Correções da auditoria de planos do CFOA (26/10/2026):**
  - **Pesos do concurso no planejador:** véspera, revisão geral e cobertura usavam os pesos do CBMPE Oficial em todo concurso individual; agora usam `input.examQuestions` e o total da prova (`PlanInput.examTotalQuestions`, vindo de `EXAM_CONFIGS` por `contest-data.ts`/`plan-input.ts`). CBMPE Oficial idêntico (`plan-snapshot.ts`, total 70 = constante antiga); teste novo em `planner.test.ts`. A cobertura máxima de 86% do CFOA era efeito dos pesos errados: com os certos, chega a 99–100%.
  - **Divisão por dias (`days.ts`):** termo de urgência (fila que, a ~1 atividade/dia, não cabe nos dias restantes ganha prioridade; `URGENCY_*`). Sem ele, a fila mais longa sobrava sozinha no fim e o combo PMPE 40 h falhava no verificador depois da resegmentação de RL. **Turbo:** se o plano normal já fecha o edital, vale o normal. 2 de 12 cenários do CBMPE Oficial mudaram; 522 testes passando.
  - **Raciocínio Lógico (auditoria estrutural):** `content/overrides/raciocinio-logico.json` (questões comentadas/listas fora da teoria, capa/índice como abertura, págs. 38–45 da a01 como teoria, títulos e tópicos de abertura). 70 → 35 trechos (o maior tem 17 págs.). Resumos analíticos, sintéticos e bizus dos 35 trechos reescritos (lote `rl-resegment-2026-10-26`); 395 inéditas MC e 43 C/E reetiquetadas pelos redatores (9 novas); todo trecho com ≥ 7.
  - **Resumos e bizus de Penal Militar (40 trechos) e Processual Penal Militar (15) revisados contra a lei:** ~155 correções de fato (penas desatualizadas, artigos e parágrafos trocados, prazos inventados, teses sem fonte); 57 inéditas de DPPM corrigidas (22 com a alternativa do gabarito falsa) e 6 de DPM; complemento `dppm-cfoa-lacunas.md` reescrito (PDF regenerado, 4 págs.). Relatórios em `pipeline/.cache/auditoria-cfoa/revisao-resumos-*.md` (fora do git).
  - **Espelho `web/content` (o seed do build lê dele):** não tinha os bizus de Administração, Direitos Humanos, DPPM, DPM a20/a21, DA c03/c04 e Legislações PE c06–c09 — a produção tinha **0 bizus** nessas três disciplinas. Copiados. Restam divergências antigas fora do CFOA (atualidades, biologia, línguas, história-pe, 2 de Legislações PE), para decisão.
- **Fechamento do CFOA (26/10/2026, noite):**
  - **Ciclo do edital (concurso sem data de prova):** `PlanInput.cycle` / `generateCyclePlan` (`planner/index.ts`): o plano vai até o menor prazo em que o edital inteiro cabe no ciclo de estudo (sem Turbo) e termina com a revisão da "véspera" do fim do ciclo; `params.cycle` guarda o nº do ciclo. O assistente não pede data quando o concurso não a tem (`resolveExam` em `onboarding/actions.ts`); `ensurePlanCycle` (`lib/plan/cycle.ts`, chamado em Missão de hoje, Semana e Planejamento) refaz o plano como ciclo seguinte quando o anterior termina; ao salvar a data em Administração › Concursos, `replanCyclePlans` refaz os planos em ciclo até a prova a partir daquele dia. A liberação continua manual (CFOA em `CONTESTS_HELD_FOR_REVIEW`); recomeço de ciclo de plano já liberado nasce liberado. Os 10 cenários de `scripts/cfoa-plan-test.ts --ciclo` cobrem 100% do edital (13 a 70 semanas), verificador LIBERAR.
  - **Importância do CFOA pelo edital:** `importance.py` (`EDITAL_MAPS`): cada item do edital do CFOA recebe a mesma fatia das questões da disciplina, repartida pelas páginas dos trechos que o cobrem; só aparecem os trechos do mapa. Saem DA a08, DC a13 (exceto s08), DC a09/s01–s05, LP a00 (nivelamento) etc.; DPM volta a pesar nas aulas centrais (a00/a01/a08/a10) e os complementos curtos deixam de valer uma aula inteira. Mapa do RL refeito para os ids novos; LP a06/a07/a11 e DC a03 (MS e MI) ampliados para a aula inteira.
  - **Títulos e tópicos:** `clean_title` normaliza "Lei no 14.133:2021" → "Lei nº 14.133/2021", tira ". Não há" e "24 e julho"; `segment.py` tira caracteres invisíveis e letras matemáticas dos tópicos; `build_complements.py` recupera o espaço perdido na quebra de linha dos títulos ("deJustificação"); overrides de título (LegPE a01/a02, Matemática a03, Química a19, Espanhol a13) e de tópico (DC a13/s08 "Justiça Eleitoral, Justiça Militar e Tribunais dos Estados"; DA a09/s04). Complementos de LegPE sem "Aula 01/02 do curso base". Ids e páginas dos trechos conferidos: inalterados.
  - **Revisões de conteúdo:** LPE 13 trechos restantes revisados contra o texto vigente (CNH categoria B = 3.500 kg, D/E com no máximo uma gravíssima, toxicológico na 1ª habilitação A/B; art. 12-C da Maria da Penha; § 4º da Lei 12.850 com o ECA); Direitos Humanos a05/s02–s03 reescritos com acentuação; +10 trechos de LP auditados (4 com erro pontual, corrigidos; pela regra do briefing, LP pede revisão integral). Súmula 172 do STJ registrada como superada pela Lei 13.491/2017 (DPM c01).
  - **Questões fora de todo edital:** as ~15 inéditas de RL apontadas (entimema, premissas dependentes, princípio da explosão, verdades e mentiras) tratam de lógica de argumentação/estruturas lógicas, que estão nos editais: não foram retiradas.
  - **Pendências:** Legislações PE itens 9 (Portaria Normativa SDS 395/2015, sindicância) e 10 (Provimento Correicional 21/2021, investigação preliminar) sem material; Administração e DPPM sem cadernos do TEC (matérias ausentes de `mapa-assuntos.json`); licitações seguem `skip` no mapa, mas estão no edital do CFOA (DA 10.x e DPM 6.1).
- **Fechamento do CFOA (27/10/2026, madrugada):**
  - **Produção:** backup íntegro `backups/questoes-remoto-20261027-023243`; `importar.py --so-remoto --reclassificar --confirmo-producao` (739 questões atualizadas para os trechos novos de Raciocínio Lógico, 0 criadas/aposentadas); inéditas regravadas no Neon com `--retirar-ausentes` (lotes de múltipla escolha e certo/errado).
  - **Itens 9 e 10 de Legislações PE:** complementos `legislacoes-pe/c10` (Portaria nº 395/2015 da Corregedoria Geral da SDS, sindicância administrativo-disciplinar militar; texto conferido na reprodução integral dos 33 artigos — o edital data a norma de 03/02/2015, mas o ato localizado foi assinado em 01/07/2015) e `legislacoes-pe/c11` (Provimento Correicional nº 21/2021, BG SDS nº 196 de 15/10/2021, texto oficial em `pipeline/.cache/leis-oficiais/sds-prov21/`), com resumos, bizus e 16 inéditas (`lote-legpe-novas.json`). Edital do CFOA sem lacunas de material.
  - **Resumos:** a correção dos tópicos mudou o `startTopic` de 28 trechos; as impressões digitais foram atualizadas (o seed não descarta resumos por impressão digital).
  - **Questões reais:** assuntos de licitações da Lei 14.133 (instrução, modalidades, divulgação do edital, fases) e Desapropriação saíram de `skip` no `mapa-assuntos.json` e vão para DA a20/a21/c04, aulas só do CFOA e do PCPE.

