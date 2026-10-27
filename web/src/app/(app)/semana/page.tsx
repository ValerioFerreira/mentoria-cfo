import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { ensurePlanCycle } from "@/lib/plan/cycle";
import { currentWeekIndex, getActivePlan } from "@/lib/data/study";

export default async function CurrentWeekRedirect() {
  const user = await requireUser();
  await ensurePlanCycle(user.id); // ciclo do edital terminou (ou a prova ganhou data): refaz o plano
  const plan = await getActivePlan(user.id);
  if (!plan) redirect("/plano");
  redirect(`/semana/${currentWeekIndex(plan.startDate, plan.weeks.length)}`);
}
