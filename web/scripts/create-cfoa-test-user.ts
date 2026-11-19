// Cria (ou refaz) um usuário de teste LOCAL com plano ATIVO do CFOA e SEM CPF: cfoa@teste.com / senha "teste".
// Serve para ver o pop-up dos PDFs no 1º login, abrir PDFs (com o pedido de CPF e nome), os Termos e os cadernos com questões comentadas.
//   npx tsx --conditions=react-server scripts/create-cfoa-test-user.ts [--horas 21] [--atrasadas]
// --atrasadas: só refaz o plano, começando ontem (as atividades de ontem ficam vencidas, para testar /reprogramar); a conta não muda.
// Recusa qualquer banco que não seja localhost.
import "dotenv/config";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";
import { hashPassword } from "../src/lib/auth/password";
import { CONTEST_SUBJECTS } from "../src/lib/contests";
import { dayOfWeekIndex, addDaysISO, todayISO } from "../src/lib/plan-time";
import { generatePlan } from "../src/lib/planner";
import { loadCatalog, loadExamQuestions, loadImportance, loadSegments } from "../src/lib/planner/fixtures";
import type { Level } from "../src/lib/planner/types";
import { localDatabase } from "../src/lib/test-user";

const EMAIL = "cfoa@teste.com";
const PASSWORD = "teste";
const args = process.argv.slice(2);
const atrasadas = args.includes("--atrasadas");

async function main() {
  if (!localDatabase()) throw new Error("DATABASE_URL não aponta para localhost: o usuário de teste só existe no banco local.");
  const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
  await db.$executeRawUnsafe("SET search_path TO public");
  let user;
  if (atrasadas) {
    // só refaz o plano: a conta (CPF, nome, aviso visto) fica como está
    user = await db.user.findUnique({ where: { email: EMAIL } });
    if (!user) throw new Error("Usuário de teste não existe: rode o script sem --atrasadas primeiro.");
  } else {
    const passwordHash = await hashPassword(PASSWORD);
    const data = { passwordHash, name: "Carlos Alberto de Souza", role: "USER" as const, mustChangePassword: false, accessExpiresAt: null, cpf: null, seenNotices: [] as string[] };
    user = await db.user.upsert({ where: { email: EMAIL }, create: { email: EMAIL, username: "cfoateste", ...data }, update: data });
    await db.materialOpen.deleteMany({ where: { userId: user.id } });
    // o concurso do aluno vem da inscrição (ou do cookie): a inscrição aponta para o CFOA
    await db.waitlistEntry.upsert({
      where: { contest_email: { contest: "CBMPE_CFOA", email: EMAIL } },
      create: { contest: "CBMPE_CFOA", name: data.name, email: EMAIL, username: "cfoateste", plan: "UNTIL_EXAM", status: "APPROVED", approvedAt: new Date() },
      update: {},
    });
  }
  await db.plan.updateMany({ where: { userId: user.id, status: { in: ["ACTIVE", "PENDING_ANALYSIS"] } }, data: { status: "ARCHIVED" } });

  // com --atrasadas o plano "começou ontem": as atividades de ontem ficam pendentes e vencidas (para testar Reprogramar)
  const today = todayISO();
  const first = atrasadas ? addDaysISO(today, -1) : today;
  const startIso = addDaysISO(first, -dayOfWeekIndex(first)); // segunda-feira da semana do 1º dia
  const hours = Number(args.includes("--horas") ? args[args.indexOf("--horas") + 1] : 21);
  const subjects = CONTEST_SUBJECTS.CBMPE_CFOA.filter((id) => id !== "lingua-espanhola");
  const input = {
    catalog: loadCatalog(),
    segments: loadSegments(),
    startDate: startIso,
    firstDay: dayOfWeekIndex(first),
    examDate: "2027-03-28",
    hoursPerWeek: hours,
    subjects: subjects.map((id) => ({ id, level: 1 as Level })),
    importance: loadImportance("CBMPE_CFOA"),
    examQuestions: loadExamQuestions("CBMPE_CFOA"),
    contest: "CBMPE_CFOA" as const,
  };
  const result = generatePlan(input);
  const { savePlan } = await import("../src/lib/plan/persist");
  const planId = await savePlan({ userId: user.id, input, result, diagnostics: {}, foreignLanguage: "EN", hoursBand: "MODERADO", status: "ACTIVE", dbClient: db as never });
  const acts = await db.activity.count({ where: { planId } });
  console.log(`Usuário de teste do CFOA pronto: ${EMAIL} / ${PASSWORD} (sem CPF). Plano ${planId}: ${acts} atividades.`);
  await db.$disconnect();
}
main().catch((e) => {
  console.error(String(e instanceof Error ? e.message : e));
  process.exit(1);
});
