# Auditoria — Legislações pertinentes aos militares de PE (`legislacoes-pe`)

Disciplina de maior peso na prova (10 questões). Auditoria feita em 10/2026 contra o edital (Anexo II, 2º Tenente) e contra o texto oficial das normas: Alepe Legis (Lei 11.817/2000 texto anotado; Lei 6.783/1974 texto atualizado; Decreto 50.014/2020; Lei 15.187/2013; Lei 16.277/2017) e Planalto (Lei 14.751/2023, com partes vetadas e promulgadas).

## Aulas e páginas auditadas

| Aula | Páginas | Mapa final | Teoria antes → depois | Trechos |
|---|---|---|---|---|
| a01 — Lei 11.817/2000 | 1–66 (todas, `--heads`; teoria 3–23 e lei seca 56–65 lidas por inteiro) | F1-4 T5-22 B23 C24-40 L41-49 K50 S51-66 | 20 → 18 | s01 5–11 (7 p.) · s02 12–22 (11 p.) |
| a02 — Lei 6.783/1974 | 1–60 (todas, `--heads`; teoria 3–26 lida por inteiro) | F1-4 T5-26 B27 C28-41 L42-49 K50 S51-60 | 24 → 22 | s01 5–14 (10 p.) · s02 15–26 (12 p.) |
| c01–c03 (complementos) | `.md` lidos por inteiro e conferidos com o texto legal | — | — | — |

Total: teoria 44 → 40 págs.; trechos 4 → 4; nenhum trecho acima de 17 págs.

## Correções feitas (`content/overrides/legislacoes-pe.json`)

1. **a01 e a02, págs. 3–4 → FRONT.** São só a apresentação do professor e as redes sociais; inflavam a carga do primeiro trecho.
2. **a01, corte na pág. 12.** O corte automático caía na pág. 15 e separava o conceito de transgressão (12–14) de consumação/tentativa (15). Agora: s01 = princípios, regime e competência; s02 = transgressões (conceito, julgamento, classificação) e recursos/comissões. O s01 fica com 7 págs.; o assunto é curto e fechado em si.
3. **a02, falso subtítulo removido** ("Política e Sistema Nacional de Proteção e Defesa Civil", pág. 5 — título de outra aula colado no PDF) e **subtítulo real adicionado** ("Da Hierarquia e da Disciplina", pág. 5).
4. **a02, corte na pág. 15** ("Dos Direitos"). O corte automático caía na pág. 17 (Licenças) e deixava o início de "Direitos" no trecho de obrigações. Agora: s01 = hierarquia, cargo e obrigações; s02 = direitos, licenças, prerrogativas, situações especiais, desligamento e tempo de serviço.
5. **a01 e a02 marcadas `edital: partial`**, com nota explicando o que falta (aparece no catálogo).

## Cobertura do edital

| Item | Status | Onde | Observação |
|---|---|---|---|
| 1.1 Código: regime disciplinar (arts. 1–12) | covered | a01 5–13 | quadro de competência omite o inciso V do art. 10 |
| 1.2 Código: transgressões (arts. 13–26) | covered | a01 12–19 | listas de justificação/atenuantes/agravantes em imagem (págs. 17–18) |
| 1.3 Código: penas e medidas administrativas (arts. 27–49) | **partial** | c01 (parcial); a01 6–7 (só em questão) | Estratégia não ensina; faltam arts. 29–37, 39–49 |
| 1.4 Código: recursos e comissões recursais (arts. 50–59) | covered | a01 19–22 | completo |
| 1.5 Código: cancelamento de penas e recompensas (arts. 60–71) | **gap** | — | ausente |
| 1.6 Código: transgressões em espécie (arts. 75–188) | **gap** | — | ausente (114 tipos) |
| 2 Decreto 50.014/2020 | complement | c01 | correto |
| 3.1 Estatuto: hierarquia e disciplina | covered | a02 5–9 | |
| 3.2 Estatuto: cargo e função | covered | a02 9–11 | |
| 3.3 Estatuto: obrigações e deveres | **partial** | a02 11–15 | faltam deveres, compromisso, comando, violação (arts. 30–48) |
| 3.4 Estatuto: direitos, prerrogativas e proteção social | **partial** | a02 15–21 | Sistema de Proteção Social (arts. 74-A a 74-AD) ausente; remuneração/promoção/férias quase ausentes |
| 3.5 Estatuto: situações especiais | partial | a02 21–23 | só quadro-resumo |
| 3.6 Estatuto: desligamento/exclusão | partial | a02 23–24 | capítulo extenso condensado em um quadro (dados conferem com o texto atual) |
| 3.7 Estatuto: tempo de serviço | covered | a02 25–26 | |
| 4.1–4.4 Lei 15.187/2013 | complement | c02 | correto; completado |
| 5 Lei 14.751/2023 (inteira) | complement | c03 | correto; completado |

Mapa detalhado em `content/edital/legislacoes-pe.json`.

## Auditoria inversa (material → estrutura)

- **a01 3–4, a02 3–4** — apresentação classificada como teoria → *indexada no lugar errado* (corrigido).
- **a02 pág. 5** — título "Política e Sistema Nacional de Proteção e Defesa Civil" → *indexada no lugar errado* (falso título, corrigido).
- **a01 corte 15 / a02 corte 17** → *superfragmentada* (cortes no meio de assunto; corrigidos com `cuts`).
- **a01 56–65 "Dispositivos mais cobrados"** (S) → *já corretamente indexada*: lei seca só das partes já ensinadas; não traz os arts. 27–49 nem a Parte Especial.
- **a01 17–18** (quadros-imagem de justificação/atenuantes/agravantes) → *necessita revisão humana*: o texto do quadro não é extraído; confirmar visualmente que está completo.
- **a02 pág. 16** — frase truncada no PDF sobre o prazo para recorrer → *necessita revisão humana* (o quadro da pág. 17 traz os prazos certos: 15 e 120 dias corridos).
- **Questões dentro da teoria** (a01 e a02) → *já corretamente indexada*: fazem parte do método da aula; boa parte das páginas T são questões comentadas, o que deixa a teoria efetiva ainda menor.
- Questões comentadas (C), listas (L), gabarito (K) e resumos (S): faixas conferidas, sem teoria perdida.

## Complementos: avaliação e mudanças

**c01 — Decreto 50.014/2020** (`leg-pe-decreto-50014.md`). Conferido artigo por artigo (10 artigos; DOE 23/12/2020; Alepe sem registro de alteração): **sem erros**. A norma tem 4 págs. porque o decreto é curto — cobertura integral. Acrescentado: (a) aviso de que o **STF declarou inconstitucional a Lei 13.967/2019 (ADI 6595, maio/2022)** e de que a Lei 14.751 ressalva as prisões disciplinares — o decreto continua publicado e é o que o edital pede; (b) quadro com o **rol de penas do art. 28** da Lei 11.817 (repreensão, detenção, prisão, licenciamento, exclusão), limite de 30 dias e advertência verbal — necessário para entender o decreto e hoje ausente do Estratégia.

**c02 — Lei 15.187/2013** (`leg-pe-lei-15187.md`). Conferido com o texto original (sem atualização registrada): **sem erros**; já apontava o erro material do art. 33 (COEsp no lugar de COM). Acrescentado: incisos XI–XV do art. 97 e a pegadinha relatório **mensal** (art. 97) × **anual** (art. 95); nota sobre a **Lei 16.277/2017** (cria DEIP, CAC, GBFN, 8º–12º GB e novos CAT sem alterar a redação da Lei 15.187) e o **Decreto 47.743/2019**. Não detalha as divisões internas de cada órgão (baixa probabilidade de cobrança).

**c03 — Lei 14.751/2023** (`leg-pe-lei-14751.md`). Conferido com o Planalto: **sem erros de conteúdo**, mas havia uma afirmação desatualizada — dizia que a privação de liberdade disciplinar "foi afastada pela Lei 13.967/2019", sem mencionar a ADI 6595; corrigida. Cobria a lei inteira em visão geral; completado com os dispositivos que faltavam (lista no `content/edital/legislacoes-pe.json`, item 5), as partes **vetadas e promulgadas** (arts. 15 § 2º, 18 XII, 22 § 2º, 28 § 3º, 29 § 6º, 40, 41), os vetos totais (arts. 20 e 21) e um quadro de **choques com o Estatuto de PE** (estabilidade 3 × 10 anos; candidatura 10 × 5 anos). Retirada a frase de marketing "mais importante e mais cobrada".

**Novos complementos (rascunhos, não publicados).** Como o Estratégia não cobre três blocos do Código e partes do Estatuto que o edital nomeia, deixei dois rascunhos prontos (frontmatter no padrão, texto original/parafraseado, artigos citados) em `content/audit/`, **fora** de `content/complements/` para não entrarem no build sem decisão do orquestrador:

- `content/audit/legislacoes-pe-rascunho-lei-11817-penas.md` — penas, medidas administrativas, aplicação/cumprimento, modificação, comportamento, cancelamento, recompensas e guia da Parte Especial (graves/médias/leves, faixas e exemplos).
- `content/audit/legislacoes-pe-rascunho-lei-6783-lacunas.md` — deveres, compromisso, comando e subordinação, violação das obrigações (crimes, transgressões, Conselhos), remuneração, promoção/quota compulsória, férias e Sistema de Proteção Social (LC 460/2021).

## Pendências

1. **Decidir os dois complementos novos** (orquestrador): mover para `content/complements/`, criar as lacunas `leg-lei-11817-penas` e `leg-lei-6783-lacunas` em `gaps.json`, rodar `build_complements.py` e o seed. Até lá, os itens 1.3, 1.5, 1.6, 3.3 e 3.4 ficam sem material adequado.
2. **Parte Especial (114 tipos)**: mesmo com o complemento, o aluno precisa ler a lei seca dos arts. 75–188. Sugiro uma atividade de "leitura de lei seca" no planejador (ver pedidos).
3. **ADI 6595 × Decreto 50.014**: conflito real entre o decreto (vigente no Alepe) e a decisão do STF sobre a lei federal que o motivou. O complemento manda responder pela letra do decreto; validar com quem acompanha a banca.
4. **Antinomias Estatuto PE × Lei 14.751**: estabilidade (10 × 3 anos) e candidatura (5 × 10 anos). Não há alteração do Estatuto registrada; a banca pode cobrar qualquer das redações.
5. **Lei 11.817**: o art. 58 vigente remete a "art. 20" (provável erro por "art. 10"); o art. 37 remete à Parte Especial para limites por autoridade que ela não traz. Conferir no DOE.
6. **Imagens não extraídas** (a01 págs. 7 e 17–18; a01 pág. 19 classificação): conferir visualmente.
7. **Estatuto — situações especiais e desligamento** (arts. 75–118) estão só resumidos no Estratégia e não entraram no rascunho; avaliar se vale um terceiro bloco do complemento ou só leitura de lei seca.
8. Alepe Legis e Planalto consultados em 10/2026; o texto do Estatuto usado é o "atualizado" (com LC 460/2021); conferir se houve alteração posterior antes da prova.

## Pedidos ao orquestrador

- Avaliar e, se aprovado, publicar os dois rascunhos de complemento (itens 1 da lista de pendências); criar as lacunas correspondentes em `content/gaps.json` (hoje só existem as três dos complementos atuais).
- Considerar no planejador um tipo de atividade "Leitura de lei seca" (ou Fixação com o PDF da lei) para normas cobradas literalmente — aqui, Lei 11.817 arts. 75–188 e Lei 6.783 arts. 75–118.
- Rodar `build_complements.py` + seed para publicar as edições dos três `.md` (c01, c02, c03) — os PDFs em `web/public/complementos/` estão desatualizados em relação aos `.md`.
- Dado o peso (10 questões) e o pouco material, avaliar subir o `weight` dos complementos da disciplina no planejamento.
