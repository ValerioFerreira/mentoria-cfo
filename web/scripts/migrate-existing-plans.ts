import "dotenv/config";
import { db } from "../src/lib/db";

async function main() {
  console.log("=== MIGRANDO PLANOS EXISTENTES NO BANCO DE DADOS ===");

  const plans = await db.plan.findMany({
    select: { id: true, status: true },
  });

  for (const plan of plans) {
    console.log(`\nProcessando plano: ${plan.id} (${plan.status})`);

    // 1. Ajustar plannedMinutes para o intervalo [50, 80], com alvo de 60m
    const allActs = await db.activity.findMany({
      where: { planId: plan.id },
      select: { id: true, plannedMinutes: true, weekId: true, dayIndex: true, subjectId: true, sortOrder: true },
    });

    let updatedMinutesCount = 0;
    for (const act of allActs) {
      let newMin = act.plannedMinutes;
      if (newMin < 50) {
        newMin = 60;
      } else if (newMin > 80) {
        newMin = 80;
      }
      if (newMin !== act.plannedMinutes) {
        await db.activity.update({
          where: { id: act.id },
          data: { plannedMinutes: newMin },
        });
        act.plannedMinutes = newMin;
        updatedMinutesCount++;
      }
    }
    console.log(`  Atividades com minutos atualizados: ${updatedMinutesCount}`);

    // 2. Para cada semana, garantir que nenhuma disciplina ultrapasse 120 min/dia
    const weeks = await db.week.findMany({
      where: { planId: plan.id },
      select: { id: true, index: true },
      orderBy: { index: "asc" },
    });

    for (const week of weeks) {
      const weekActs = await db.activity.findMany({
        where: { weekId: week.id },
        select: { id: true, plannedMinutes: true, dayIndex: true, subjectId: true, sortOrder: true },
        orderBy: { sortOrder: "asc" },
      });

      if (weekActs.length === 0) continue;

      const uniqueSubjects = [...new Set(weekActs.map((a) => a.subjectId))];
      for (const subId of uniqueSubjects) {
        const subActs = weekActs.filter((a) => a.subjectId === subId);

        // Se algum dia tiver mais de 2 atividades, redistribui para dias com < 2
        for (let pass = 0; pass < 20; pass++) {
          let moved = false;
          for (let d = 0; d < 7; d++) {
            const actsOnD = subActs.filter((a) => (a.dayIndex ?? 0) === d);
            if (actsOnD.length > 2) {
              for (let td = 0; td < 7; td++) {
                if (td === d) continue;
                const actsOnTd = subActs.filter((a) => (a.dayIndex ?? 0) === td);
                if (actsOnTd.length < 2) {
                  const toMove = actsOnD[actsOnD.length - 1];
                  toMove.dayIndex = td;
                  moved = true;
                  break;
                }
              }
            }
          }
          if (!moved) break;
        }

        // Se algum dia tiver 2 atividades somando > 120, tenta mover uma para outro dia livre
        for (let d = 0; d < 7; d++) {
          const actsOnD = subActs.filter((a) => (a.dayIndex ?? 0) === d);
          const totalM = actsOnD.reduce((n, a) => n + a.plannedMinutes, 0);
          if (totalM > 120 && actsOnD.length === 2) {
            for (let td = 0; td < 7; td++) {
              if (td === d) continue;
              const actsOnTd = subActs.filter((a) => (a.dayIndex ?? 0) === td);
              if (actsOnTd.length === 0) {
                actsOnD[1].dayIndex = td;
                break;
              }
            }
          }
        }

        // Calibra minutos em dias com 2 atividades para exatamente <= 120 min
        for (let d = 0; d < 7; d++) {
          const actsOnD = subActs.filter((a) => (a.dayIndex ?? 0) === d);
          const totalM = actsOnD.reduce((n, a) => n + a.plannedMinutes, 0);
          if (totalM > 120) {
            if (actsOnD.length === 1) {
              actsOnD[0].plannedMinutes = Math.min(80, 120);
            } else if (actsOnD.length === 2) {
              actsOnD[0].plannedMinutes = 60;
              actsOnD[1].plannedMinutes = 60;
            } else {
              actsOnD[0].plannedMinutes = 60;
              actsOnD[1].plannedMinutes = 60;
              for (let i = 2; i < actsOnD.length; i++) {
                actsOnD[i].plannedMinutes = 60;
                let bestTd = 0;
                let minTdMinutes = Number.POSITIVE_INFINITY;
                for (let td = 0; td < 7; td++) {
                  if (td === d) continue;
                  const m = subActs.filter((a) => (a.dayIndex ?? 0) === td).reduce((n, a) => n + a.plannedMinutes, 0);
                  if (m < minTdMinutes) {
                    minTdMinutes = m;
                    bestTd = td;
                  }
                }
                actsOnD[i].dayIndex = bestTd;
              }
            }
          }
        }

        // Salvar alterações no banco
        for (const act of subActs) {
          await db.activity.update({
            where: { id: act.id },
            data: {
              dayIndex: act.dayIndex,
              plannedMinutes: act.plannedMinutes,
            },
          });
        }
      }

      // Atualizar week.targetMinutes
      const totalWeekMin = weekActs.reduce((n, a) => n + a.plannedMinutes, 0);
      await db.week.update({
        where: { id: week.id },
        data: { targetMinutes: totalWeekMin },
      });
    }
  }

  console.log("\n=== MIGRAÇÃO CONCLUÍDA COM SUCESSO! ===");
}

main().catch(console.error).finally(() => db.$disconnect());
