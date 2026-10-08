# MentorIA — Missão Oficial CBMPE (web)

App Next.js do mentor de estudos. Veja `../CLAUDE.md` para estrutura, comandos e convenções.

Desenvolvimento rápido:

```bash
cp .env.example .env            # ajuste DATABASE_URL
npx prisma dev -n cfo-bm -d     # Postgres de desenvolvimento embutido (copie a URL para o .env)
npx prisma migrate deploy && npx prisma db seed
npx tsx scripts/invite.ts --admin   # gera o convite do primeiro administrador
npm run dev                     # http://localhost:3000
```

## Início dos estudos

No último passo do assistente (`/onboarding`) o aluno escolhe **"Começar imediatamente"** ou uma **data na agenda**.
- "Imediatamente" usa o dia civil de **Recife** (`todayISO()` em `src/lib/plan-time.ts`, fuso `America/Recife`), calculado no servidor — nunca `new Date().toISOString()`, que vira o dia às 21h locais.
- A semana 1 sempre começa numa segunda-feira (`Plan.startDate`); o dia em que o aluno de fato começa fica em `Plan.params.firstStudyDate` e `PlanInput.firstDay` (0 = segunda … 6 = domingo). Na semana 1 só entram os dias a partir dele (meta proporcional aos pesos dos dias, `weekFraction` em `planner/days.ts`).
- Antes do primeiro dia de estudo, a "Missão de hoje" mostra "O plano começa em …" (`planPosition(..., firstStudyIso)`).
- Datas passadas são rejeitadas no servidor (`resolveStart` em `onboarding/actions.ts`).
