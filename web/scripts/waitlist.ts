// Lista de espera. Uso:
//   npx tsx scripts/waitlist.ts                     lista todos (mais antigos primeiro)
//   npx tsx scripts/waitlist.ts --pago <email>      marca o Pix como conferido
//   npx tsx scripts/waitlist.ts --convite <email>   marca como pago (se ainda não estiver) e gera o convite restrito ao e-mail
//   npx tsx scripts/waitlist.ts --remover <email>   remove da lista
// O link do convite usa SITE_URL (padrão http://localhost:3000).
import "dotenv/config";
import { randomBytes } from "node:crypto";
import { PrismaPg } from "@prisma/adapter-pg";
import { PrismaClient } from "../src/generated/prisma/client";

const args = process.argv.slice(2);
const flag = (n: string) => {
  const i = args.indexOf(n);
  return i >= 0 ? args[i + 1]?.toLowerCase() : undefined;
};
const db = new PrismaClient({ adapter: new PrismaPg({ connectionString: process.env.DATABASE_URL }) });
const LABEL = { CBMPE_SOLDADO: "CBMPE Soldado", CBMPE_OFICIAL: "CBMPE 2º Tenente", PCPE_AGENTE: "PCPE Agente" } as const;
const PLAN = { MONTHLY: "R$ 35/mês", UNTIL_EXAM: "R$ 100 até a prova" } as const;

async function main() {
  const paid = flag("--pago");
  const invite = flag("--convite");
  const remove = flag("--remover");

  if (paid || invite) {
    const email = (paid ?? invite)!;
    const entries = await db.waitlistEntry.findMany({ where: { email } });
    if (!entries.length) return console.log(`Ninguém na lista com o e-mail ${email}.`);
    await db.waitlistEntry.updateMany({ where: { email, paidAt: null }, data: { paidAt: new Date() } });
    console.log(`Pix conferido para ${email}.`);
    if (invite) {
      const code = randomBytes(6).toString("base64url");
      await db.invite.create({ data: { code, email } });
      const base = (process.env.SITE_URL ?? "http://localhost:3000").replace(/\/$/, "");
      console.log(`Convite: ${code}\nLink: ${base}/cadastro?convite=${code}`);
    }
    return;
  }
  if (remove) {
    const r = await db.waitlistEntry.deleteMany({ where: { email: remove } });
    return console.log(`${r.count} registro(s) removido(s).`);
  }

  const all = await db.waitlistEntry.findMany({ orderBy: { createdAt: "asc" } });
  if (!all.length) return console.log("Lista de espera vazia.");
  for (const e of all) {
    const when = e.createdAt.toLocaleString("pt-BR", { timeZone: "America/Recife" });
    console.log(`${e.paidAt ? "[PAGO]    " : "[aguarda] "}${when}  ${LABEL[e.contest].padEnd(16)} ${(e.plan ? PLAN[e.plan] : "—").padEnd(19)} ${e.email.padEnd(34)} @${e.username.padEnd(20)} ${e.name}`);
  }
  console.log(`\n${all.length} na lista · ${all.filter((e) => e.paidAt).length} com Pix conferido`);
}
main().finally(() => db.$disconnect());
