# CFO-BM — MentorIA · Missão Oficial CBMPE

Site que monta o plano de estudos para o concurso de **2º Tenente do CBMPE (banca Instituto AOCP, prova 28/02/2027)** e aponta *onde* estudar no Estratégia (aula, página, tópico). Plano de produto aprovado: `C:\Users\Administrador\.claude\plans\vamos-criar-um-site-sparkling-mitten.md`.

## Estrutura
- `docs/` — PDFs do Estratégia, índice `.xlsx`, edital e (futuro) `docs/provas/`. **Protegido: marca d'água com nome/CPF do aluno. Nunca versionar, publicar ou copiar texto verbatim para `content/`.** (no `.gitignore`)
- `pipeline/` — Python (venv em `pipeline/.venv`): extração, validação do índice, segmentação, corpus/estilo AOCP, validador de conteúdo. Cache local em `pipeline/.cache/` (ignorado).
- `content/` — JSON versionado: `subjects.json` (edital), `catalog.json` (aulas), `structure/`, `segments/`, `gaps.json`, `overrides.json`, `style/aocp-profile.json`, **`items/<disciplina>/<aula>.json` (bizus e questões autorais)** e **`complements/*.md` (materiais complementares do MentorIA que preenchem lacunas do edital; viram PDF em `web/public/complementos/`)**.
- `content/overrides/<disciplina>.json` (correções da auditoria por aula: `pages` com tipos T/C/L/K/S/F/B/**EXTRA**, `headings`, `dropHeadings`, `cuts`, `edital`, `note`), `content/edital/<disciplina>.json` (mapa edital → material → trechos), `content/audit/<disciplina>.md` (relatório da auditoria), `pipeline/briefs/*.md` (briefings dos agentes: auditoria, conteúdo, complementos). **Estado e pendências da missão de auditoria: `PROGRESSO-AUDITORIA.txt` (raiz); divisão de trabalho com o colaborador e fluxo: `INSTRUCOES-COLABORADOR.md`; produção em 2 etapas (bizu → questões): `pipeline/briefs/bizu.md` e `content.md`.**
- `web/` — Next.js 16 + TypeScript + Tailwind + Prisma 7 (Postgres). Planejador em `web/src/lib/planner`; telas em `web/src/app/(app)`; auth própria (sessão em banco, cookie opaco) em `web/src/lib/auth`.

## Comandos
```bash
# Pipeline (raiz)
pipeline/.venv/Scripts/python pipeline/xlsx_index.py     # índice .xlsx -> cache
pipeline/.venv/Scripts/python pipeline/extract.py        # PDFs -> texto por página (cache; --only 08, --force)
pipeline/.venv/Scripts/python pipeline/headings.py       # subtítulos por fonte (cache)
pipeline/.venv/Scripts/python pipeline/index_validate.py # confere páginas do índice contra o texto
pipeline/.venv/Scripts/python pipeline/segment.py        # estrutura + segmentos -> content/
pipeline/.venv/Scripts/python pipeline/build_catalog.py  # content/catalog.json
pipeline/.venv/Scripts/python pipeline/edital_audit.py   # reanálise item a item do edital × material (relatório em pipeline/.cache/reports/)
pipeline/.venv/Scripts/python pipeline/build_complements.py  # RODAR DEPOIS de segment.py/build_catalog.py: md -> PDF + mescla aulas 'authored' no catálogo/estrutura/segmentos e marca lacunas resolvidas
pipeline/.venv/Scripts/python pipeline/corpus.py && pipeline/.venv/Scripts/python pipeline/style_stats.py  # corpus/estilo AOCP
pipeline/.venv/Scripts/python pipeline/validate_content.py  # valida content/items (esquema, gabarito, ORIGINALIDADE); --coverage mostra trechos sem bizu/questões
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN [--heads|--pages 10-14|--grep rx]  # mapa de páginas, tópicos e trechos de uma aula
pipeline/.venv/Scripts/python pipeline/segment.py --subject <disc>  # regenera só uma disciplina (lê content/overrides); depois build_catalog.py e build_complements.py
pipeline/.venv/Scripts/python pipeline/edital_map.py  # liga o mapa edital → material aos ids de trecho e resume a cobertura
# build_complements.py --only <id> --no-merge: só gera o PDF de um complemento (seguro com vários autores em paralelo)
pipeline/.venv/Scripts/python -m pytest pipeline/tests -q

# Web (em web/)
npx prisma dev -n cfo-bm -d        # sobe o Postgres de DESENVOLVIMENTO embutido (porta no web/.env)
npx prisma migrate deploy          # aplica migrações (usar `migrate diff` + deploy; o shadow DB do prisma dev falha)
npx prisma db seed                 # estrutura + bizus/questões (idempotente, upsert)
npx tsx scripts/invite.ts [--admin] [email]   # cria convite de cadastro
npx tsx scripts/plan-demo.ts 25 1 3           # inspeciona um plano (horas, nível, semanas a mostrar; mostra a divisão por dias)
npx tsx scripts/days-audit.ts 25              # estatísticas da divisão diária (minutos por dia, famílias coladas...)
npm run dev | build | lint | typecheck | test
```
Defina `PYTHONIOENCODING=utf-8` no Windows ao imprimir acentos.

## Convenções
- Idioma da UI e do conteúdo: **português (pt-BR)**.
- Questões AOCP: **5 alternativas (A–E), 1 correta**. Itens Certo/Errado só nos bizus. Campo `literal: true` só para citação de norma (lei/súmula/CF).
- Marcação em `content/items`: o `summary` do bizu só renderiza **negrito** (`BizuSummary` em `web/src/components/bizu.tsx`); itálico, crase e listas aparecem como texto cru. Enunciados, alternativas, C/E e explicações são texto puro. O validador avisa quando a alternativa correta é muito mais longa que as demais em >35% das questões: equilibre o tamanho das alternativas.
- Segmento de Teoria ≈ 1 h: **10–17 págs.** (teto 17), cortes no início de tópico. Revisão cobre até 3–4 Teorias; caderno = 25 questões / 60 min.
- **Tempo por atividade (em minutos, `web/src/lib/planner/blueprint.ts`)**: Teoria = 60 × carga/12 (clamp 30–75; o "load" do segmento já pondera a densidade); Revisão = 15 + 10 por Teoria revista (30–50); Fixação 60; Caderno 60. Tudo multiplicado pelo **ritmo do nível** (iniciante 1,0 · básico 0,9 · intermediário 0,75 · avançado 0,6) e, na Teoria/Revisão, por 0,65 nas aulas marcadas "já estudei". Aulas marcadas "domino" na anamnese saem do plano (contam como cobertas e voltam nas revisões finais). **Não voltar a tratar toda atividade como 1 h.**
- **Camadas por aula**: Essencial (toda a teoria + 1 revisão a cada 4 Teorias + prática enxuta) → Completo → Aprofundamento. O seletor é **amplitude primeiro**: todas as aulas entram no Essencial antes de qualquer aprofundamento. **Cobertura** = fração do edital vista (Essencial já conta); **prática** é outra métrica (fração da fixação+cadernos completos). O edital inteiro no Essencial cabe em ≈ 45 h/semana para nível intermediário e ≈ 36 h para avançado (`params.fullEditalHoursPerWeek`).
- **Divisão por dias (`planner/days.ts`)**: cada atividade tem `day` (0 = seg … 6 = dom, coluna `Activity.dayIndex`; planos antigos sem dia são espalhados por `effectiveDays`). Regras: sessões de ≤ ~2h30 por disciplina, no máx. 1 sessão/disciplina/dia (prática distribuída); Revisão nunca no dia da Teoria que revê (espaçamento); 3+ disciplinas/dia só com muita carga e sem famílias iguais coladas (jurídica, línguas, exatas, natureza — intercalação); Revisão da véspera abre o dia, exatas/teoria nova no começo, prática no fim; domingo leve (peso 0,45). Base: Cepeda et al. 2006 (espaçamento), Rohrer/Brunmair & Richter 2019 (intercalação), efeito do teste (Roediger & Karpicke).
- **Início dos estudos**: o assistente oferece "Começar imediatamente" (dia civil de **Recife**, calculado no servidor com `todayISO()`; o primeiro dia conta como hoje) ou uma data na agenda. A semana 1 começa na segunda (`Plan.startDate`); o dia real de início vai em `PlanInput.firstDay` (0 = seg … 6 = dom) e `plan.params.firstStudyDate`. Na semana 1 só há atividades a partir desse dia, com meta proporcional (`weekFraction`), e a capacidade total desconta os dias antes do início. Nunca usar `new Date().toISOString()` para "hoje" (UTC vira o dia às 21h em Recife).
- **Materiais complementares (lacunas do edital)**: Estratégia não cobre Decreto 50.014/2020, Lei 15.187/2013, Lei 14.751/2023, ECA, Estatuto da Juventude, Lei Maria da Penha, figuras de linguagem, formação de palavras, funções do "que"/"se" (aprofundamento), estruturas de Inglês (adverbiais, condicionais/relativas, padrões verbais, question tags) e Química aplicada (siderurgia, FDS, água). Eles são aulas `source = AUTHORED` numeradas 101+ (a interface mostra "Complemento 01…"), com PDF próprio (`Aula.materialPath`) aberto na página do trecho. Conteúdo **original/parafraseado** a partir do texto legal oficial; **não copiar o Estratégia**. Para editar, mexa no `.md` e rode `build_complements.py` + `npx prisma db seed`. A reanálise (`edital_audit.py`) confirmou que Biologia (biotecnologia) **não** tem lacuna e que "que/se" têm só uma lista curta na Aula 05, pág. 90.
- **Auditoria estrutural (2026-10-08)**: toda mudança de segmentação passa por `content/overrides/<disciplina>.json` (nunca editar `structure/` ou `segments/` à mão). Ids de trecho são posicionais (`<disc>/aNN/sNN`): resegmentar muda os ids, então **bizus/questões só se produzem depois de a estrutura da disciplina estar fechada** (e o seed desativa trechos/aulas órfãos). Páginas `EXTRA` (fora do edital, duplicadas ou opcionais) não viram atividade.
- Conteúdo autoral é **parafraseado/original**: `validate_content.py` rejeita sequências de 10 palavras iguais ao material. Novo conteúdo entra como `DRAFT`; só `APPROVED` chega aos alunos em produção (`SERVE_DRAFT_QUESTIONS=true` libera rascunhos em dev). Revisão em `/admin/revisao`.
- Marca: **MentorIA** (as letras "IA" ganham o gradiente `.brand-ia`), chama animada (`Flame` em `components/brand.tsx`, CSS puro; ícone da aba animado por `FaviconFlame` + `lib/flame-frames.ts`). `Brand` mostra só o nome; o subtítulo "Missão Oficial · CBMPE" só aparece no menu do app (prop `subtitle`), porque o sistema passou a atender mais de um concurso.
- **Páginas públicas (deploy inicial só de cadastro)**: quem não tem sessão vê `/login` como página inicial (o `proxy.ts` reescreve `/` para `/login`; layout em `app/(auth)/layout.tsx`, motivo visual do cartão-resposta: bolhas A–E e marcas de leitura na borda, classe `.omr-edge`). "Ainda não tem conta? Criar conta" leva a `/concursos` → `/lista-de-espera/<concurso>` (solicitação de cadastro + Pix). Sem data de prova nem contagem regressiva nessas páginas e sem menção a "acesso por convite" (`/cadastro?convite=` segue existindo, mas sem link na interface; é por ele que `scripts/waitlist.ts --convite` libera o acesso).
- **Lista de espera e planos**: a pessoa escolhe **Mensalidade R$ 35** ou **Acesso até a prova R$ 100** (oferta em destaque, pré-selecionada); valores em `web/src/lib/plans.ts`, que também define o valor fixo do QR Code (campo 54 do BR Code). O plano fica em `WaitlistEntry.plan` (nulo nos cadastros anteriores) e aparece em `npx tsx scripts/waitlist.ts`. `PIX_AMOUNT` não é mais usado. Textos do cartão de pagamento ("Falta pouco!"…) foram definidos pelo dono do produto: não reescrever.
- Menu: Missão de hoje (`/`), Meta semanal (`/semana`), Planejamento (`/plano`), Desempenho (`/desempenho`). Texto explicativo vai para `InfoTip` (balão "?") — evitar parágrafos de ajuda soltos nas telas.
- Cronômetro: balão flutuante arrastável (`components/timer-widget.tsx`), **só no navegador** (localStorage); o sistema não grava os tempos dele. O tempo de estudo é lançado pelo aluno em **horas + minutos** por atividade (`logManualTime`).
- Visual ("Quadro de Prontidão"): tokens e animações em `web/src/app/globals.css` (cores `ink/primary/gold`, tipos de atividade `teoria/revisao/fixacao/questoes`, classes `rise`, `page-in`, `card-hover`, `tape`); primitivos em `web/src/components/ui.tsx` (`Card tone`, `Button size/variant`, `Ring`, `Count`, `Progress`, `PageHeader`, `Stat`); fontes Barlow Condensed (`font-display`) + Public Sans. Não sobrescrever utilitários de cor/padding via `className` em `Card`/`Button` (sem twMerge): use as props `tone`/`size`. Aparência **Claro / Sépia / Dark** (botão "Aparência", canto superior direito) em cookie `theme` (lido no `app/layout.tsx`; sem cookie segue o sistema). Ícones: `lucide-react`. Animações respeitam `prefers-reduced-motion`.
- Next 16: ler `web/node_modules/next/dist/docs/` antes de mexer em rotas/auth (ver `web/AGENTS.md`). `cacheComponents` está desligado. `Date.now()` direto no render viola a regra de pureza do lint: usar helper fora do componente.
- Prisma 7: `prisma.config.ts` + adapter `@prisma/adapter-pg`; client em `@/generated/prisma/client`. **Pinar `prisma@7.10.0`** (o `latest` do npm é RC 8.x). `migrate reset` exige consentimento explícito do usuário (trava de segurança do Prisma).
- Nunca adivinhar/tentar senhas de bancos; credenciais só em `.env` (modelo em `web/.env.example`).
- Heredocs longos no Bash tool quebram com aspas: preferir a ferramenta Write para arquivos grandes.
