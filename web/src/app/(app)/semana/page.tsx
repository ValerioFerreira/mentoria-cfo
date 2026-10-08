import { redirect } from "next/navigation";
import { requireUser } from "@/lib/auth/dal";
import { currentWeekIndex, getActivePlan } from "@/lib/data/study";

export default async function CurrentWeekRedirect() {
  const user = await requireUser();
  const plan = await getActivePlan(user.id);
  if (!plan) redirect("/onboarding");
  redirect(`/semana/${currentWeekIndex(plan.startDate, plan.weeks.length)}`);
}
