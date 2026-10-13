import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  const adminUsers = await db.user.findMany({
    where: { role: "ADMIN" },
    select: { id: true, email: true },
  });

  console.log(`Encontrados ${adminUsers.length} administradores no sistema.`);

  for (const admin of adminUsers) {
    const updated = await db.plan.updateMany({
      where: { userId: admin.id, status: "PENDING_ANALYSIS" },
      data: { status: "ACTIVE" },
    });
    console.log(`Admin ${admin.email}: ${updated.count} plano(s) liberado(s) para ACTIVE.`);
  }
}

main().catch(console.error).finally(() => db.$disconnect());
