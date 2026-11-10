import { ClipboardCheck, Flag, Handshake, Ticket, Users, Wallet, type LucideIcon } from "lucide-react";
import type { Metadata } from "next";
import Link from "next/link";
import { Card, PageHeader } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { CONTESTS } from "@/lib/contests";
import { db } from "@/lib/db";

export const metadata: Metadata = { title: "Administração" };

export default async function AdminHomePage() {
  await requireAdmin();
  const [pendingSignups, draftQuestions, openReports, activePartners, openContracts, activeCoupons, datedContests] = await Promise.all([
    db.waitlistEntry.count({ where: { status: "PENDING" } }),
    db.question.count({ where: { status: "DRAFT" } }),
    db.questionReport.count({ where: { status: "OPEN" } }),
    db.partner.count({ where: { active: true } }),
    db.contract.count({ where: { status: { in: ["OPEN", "PARTIAL"] } } }),
    db.coupon.count({ where: { active: true } }),
    db.contestSetting.count({ where: { examDate: { not: null } } }),
  ]);
  const pendingDates = Math.max(0, CONTESTS.length - datedContests);

  const cards: { href: string; title: string; text: string; icon: LucideIcon; stat: string }[] = [
    {
      href: "/admin/cadastros",
      title: "Cadastros",
      text: "Solicitações de cadastro, aprovação, acesso e dados dos alunos.",
      icon: Users,
      stat: `${pendingSignups} ${pendingSignups === 1 ? "solicitação pendente" : "solicitações pendentes"}`,
    },
    {
      href: "/admin/financeiro",
      title: "Financeiro",
      text: "Contratações, pagamentos, clientes, saldos, Mercado Pago e histórico.",
      icon: Wallet,
      stat: `${openContracts} ${openContracts === 1 ? "contratação com saldo" : "contratações com saldo"}`,
    },
    {
      href: "/admin/concursos",
      title: "Concursos",
      text: "Categoria, preço, desconto e data oficial da prova de cada concurso. A data define o limite de acesso dos alunos.",
      icon: Flag,
      stat: `${pendingDates} ${pendingDates === 1 ? "concurso sem data de prova" : "concursos sem data de prova"}`,
    },
    {
      href: "/admin/parceiros",
      title: "Parceiros",
      text: "Cadastro, cupons, comissões, repasses e indicadores da parceria.",
      icon: Handshake,
      stat: `${activePartners} ${activePartners === 1 ? "parceiro ativo" : "parceiros ativos"}`,
    },
    {
      href: "/admin/cupons",
      title: "Cupons",
      text: "Cupons de desconto do site: criar, editar, ativar, inativar e excluir.",
      icon: Ticket,
      stat: `${activeCoupons} ${activeCoupons === 1 ? "cupom ativo" : "cupons ativos"}`,
    },
    {
      href: "/admin/revisao",
      title: "Revisão de questões",
      text: "Aprovação, correção e classificação das questões, por matéria, assunto e banca.",
      icon: ClipboardCheck,
      stat: `${draftQuestions} rascunhos · ${openReports} ${openReports === 1 ? "denúncia" : "denúncias"}`,
    },
  ];

  return (
    <div className="space-y-6">
      <PageHeader eyebrow="Painel" title="Administração" description="Tudo o que a gestão da plataforma precisa, em um só lugar." />
      <div className="grid gap-4 sm:grid-cols-2">
        {cards.map((c) => (
          <Link key={c.href} href={c.href} className="group block focus-visible:outline-none">
            <Card className="card-hover flex h-full flex-col gap-3 p-5 group-focus-visible:ring-2 group-focus-visible:ring-primary">
              <span className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary-soft text-primary">
                <c.icon className="h-5 w-5" aria-hidden />
              </span>
              <h2 className="font-display text-2xl font-bold uppercase tracking-wide">{c.title}</h2>
              <p className="flex-1 text-sm text-muted">{c.text}</p>
              <p className="text-sm font-semibold text-primary">{c.stat}</p>
            </Card>
          </Link>
        ))}
      </div>
    </div>
  );
}
