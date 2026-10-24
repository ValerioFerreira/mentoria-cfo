# MentorIA · Missão Oficial CBMPE

Site que monta o plano de estudos para o concurso de 2º Tenente do CBMPE (banca Instituto AOCP, prova em 28/02/2027) e aponta *onde* estudar no material (aula, página, tópico). Atende também CBMPE Soldado, CBMPE 2º Tenente CFOA, PMPE (Oficial e Soldado) e PCPE Agente de Polícia sobre o mesmo catálogo.

## Documentação

| Documento | Para quê |
|---|---|
| [`CLAUDE.md`](CLAUDE.md) | Arquitetura, comandos, convenções e regras de negócio (lido pelos agentes; é a referência principal) |
| [`COLABORADORES.md`](COLABORADORES.md) | Como colaboradores e agentes produzem conteúdo (resumos, bizus, complementos), regras e preparação da máquina |
| [`HISTORICO.md`](HISTORICO.md) | O que foi feito na auditoria e na produção de conteúdo, e as dúvidas do material que pedem revisão humana |
| [`pipeline/questoes/EXTRACAO.md`](pipeline/questoes/EXTRACAO.md) | Importação das questões dos cadernos do TecConcursos (o importador copia este arquivo para `docs/questoes/`) |
| `pipeline/briefs/*.md`, `resumos-colaboradores/*.md` | Briefings entregues aos agentes (autossuficientes de propósito) |
| [`web/AGENTS.md`](web/AGENTS.md) | Aviso do Next.js 16 (gerado pelo `next dev`; não remover) |

## Estrutura

- `web/` — Next.js 16 + TypeScript + Tailwind + Prisma 7 (Postgres): planejador, telas, auth e painel administrativo. `web/content/` é um **espelho de `content/`** lido pelo build/seed na Vercel (atualizado por `pipeline/apply_synthetic.py`).
- `pipeline/` — Python: extração dos PDFs, segmentação, catálogo, validadores de conteúdo, importador de questões, perfis de aprovação. Testes em `pipeline/tests`.
- `content/` — JSON/Markdown versionados: edital (`subjects.json`), catálogo, estrutura e segmentos, bizus (`items/`), resumos (`summaries/`), complementos (`complements/`), mapas do edital e relatórios da auditoria (`audit/`).
- `docs/` — PDFs do material, índice e edital. **Protegido** (marca d'água com nome/CPF): fora do Git, nunca publicar nem copiar texto para `content/`.
- `scripts/` — backup/restauração de questões (`backup_questions.ts`, `verify_backup.ts`, `restore_backup.ts`) e `run_full_audit.py`.
- `backups/questoes/` — backups JSON das questões com manifesto de integridade.
- `tools/estrategia-downloader/` — baixador local dos PDFs do curso (ver abaixo).
- `images/` — identidade visual (logos, favicons) e imagens do carrossel da página pública.

## Começando

```bash
# Pipeline (Python 3.13)
python -m venv pipeline/.venv
pipeline/.venv/Scripts/python -m pip install -r pipeline/requirements.txt
pipeline/.venv/Scripts/python -m pytest pipeline/tests -q

# Web
cd web
cp .env.example .env                 # ajuste DATABASE_URL
npx prisma dev -n cfo-bm -d          # Postgres de desenvolvimento embutido (copie a URL para o .env)
npx prisma migrate deploy && npx prisma db seed
npx tsx scripts/invite.ts --admin    # convite do primeiro administrador
npm run dev                          # http://localhost:3000
```

Lista completa de comandos (pipeline, seed, planos, importador de questões) e as convenções: `CLAUDE.md`. Defina `PYTHONIOENCODING=utf-8` no Windows ao imprimir acentos.

## Ferramentas

**Baixador dos PDFs do curso** (`tools/estrategia-downloader/`). Automação local que baixa os PDFs originais das aulas disponíveis na sessão autenticada do usuário. Não pede senha ao CLI nem contorna controles de acesso: usa a URL assinada que a própria página da aula apresenta.

```powershell
python -m pip install -r tools/estrategia-downloader/requirements.txt
python -m playwright install chromium
python tools/estrategia-downloader/scraper.py --course "<URL do pacote>" --output .\downloads
```

Na primeira execução o Chromium abre visível: faça o login manualmente. O perfil fica em `browser-profile/`. Opções: `--headless`, `--resume`, `--max-retries`, `--delay`, `--timeout`, `--profile`. O progresso fica em `progress.json` e as falhas em `logs/errors.log`; uma nova execução valida os PDFs existentes e continua. `scrape_atualidades.py` é a variante para o módulo de Atualidades.

**Backup de questões** (`backups/questoes/`). Gerar: `npx --prefix web tsx ../scripts/backup_questions.ts` (exporta `Question`, `QuestionOption`, `QuizAnswer` e `QuizSession` para `backup_questions_<timestamp>.json` e grava o SHA-256 em `manifest.json`). Verificar integridade: `npx --prefix web tsx ../scripts/verify_backup.ts`. Restaurar: `npx --prefix web tsx ../scripts/restore_backup.ts [arquivo]` (sem argumento, usa o manifesto mais recente).

**Identidade visual** (`images/missao_mentoria_brand_assets/`). Conceito "Jornada até a Aprovação" (montanha, trilha, sol e bandeira vermelha). Prefira os SVG (`logo-horizontal`, `logo-stacked`, `logo-symbol`, `icon-symbol`, `favicon`; variantes `-dark-background` para fundo escuro). Os PNG têm fundo transparente, exceto os `favicon-*`, que têm fundo azul-marinho para contraste em tamanhos pequenos. As fontes dos SVG usam fallback `sans-serif`; converta os textos em curvas antes de publicar.
