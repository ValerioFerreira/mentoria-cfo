import { ArrowLeft } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { redirect } from "next/navigation";
import { Alert, Card, LinkButton, PageHeader } from "@/components/ui";
import { requireUser } from "@/lib/auth/dal";
import { isScenario, loadScenario, overdueOf } from "@/lib/plan/reschedule-data";
import { addDaysISO, todayISO } from "@/lib/plan-time";
import { canUserAccessCoreFeatures } from "@/lib/system-settings";
import { RescheduleFlow } from "./reschedule-flow";

export const metadata: Metadata = { title: "Reprogramar atividades" };

export default async function ReschedulePage() {
  const user = await requireUser();
  if (!(await canUserAccessCoreFeatures(user.role, user.id))) redirect("/plano");
  const sc = await loadScenario(user.id);
  if (!isScenario(sc)) {
    return (
      <div className="mx-auto max-w-3xl space-y-5">
        <Back />
        <Alert tone="info">{sc.error}</Alert>
        <LinkButton href="/plano" variant="secondary">Ver o planejamento</LinkButton>
      </div>
    );
  }
  const overdue = overdueOf(sc);
  const lastDate = addDaysISO(sc.startIso, sc.lastContentOrd);
  return (
    <div className="mx-auto max-w-3xl space-y-6">
      <Back />
      <PageHeader
        eyebrow="Atividades atrasadas"
        title="Reprogramar"
        info="Escolha as atividades atrasadas e como quer encaixá-las. Antes de confirmar, você vê para onde cada uma vai, o que muda na carga de cada dia e quais atividades seguintes precisam andar junto (a revisão sempre vem depois da teoria, a fixação depois da revisão e o caderno de questões por último)."
      />
      {overdue.length === 0 ? (
        <Card className="space-y-3">
          <p className="font-display text-2xl font-bold uppercase tracking-wide">Nada atrasado</p>
          <p className="text-sm text-muted">Você está em dia com o plano.</p>
          <LinkButton href="/" variant="secondary">Voltar à Missão de hoje</LinkButton>
        </Card>
      ) : (
        <RescheduleFlow overdue={overdue} today={todayISO()} lastDate={lastDate} />
      )}
    </div>
  );
}

function Back() {
  return (
    <Link href="/" className="inline-flex items-center gap-1.5 text-sm font-semibold text-muted transition hover:text-text">
      <ArrowLeft className="h-4 w-4" aria-hidden />
      Missão de hoje
    </Link>
  );
}
