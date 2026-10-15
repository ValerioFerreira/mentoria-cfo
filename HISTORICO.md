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
