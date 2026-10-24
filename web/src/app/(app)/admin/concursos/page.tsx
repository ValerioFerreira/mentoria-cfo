import type { Metadata } from "next";
import Link from "next/link";
import { ActionForm } from "@/components/action-form";
import { Alert, Badge, Card, Field, PageHeader, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import { adminUpdateContestSetting } from "@/lib/commerce/admin-actions";
import { contestName, dayBR } from "@/lib/commerce/labels";
import { formatBRL } from "@/lib/commerce/money";
import { CATEGORY_LABEL, CATEGORY_PRICE_CENTS, LAUNCH_DISCOUNT_POINTS, PARTNER_COUPON_DISCOUNT_POINTS, quote } from "@/lib/commerce/pricing";
import { CONTESTS, CONTEST_SUBTITLES } from "@/lib/contests";
import { db } from "@/lib/db";

export const metadata: Metadata = { title: "Concursos" };

const CATEGORIES = Object.keys(CATEGORY_LABEL) as (keyof typeof CATEGORY_LABEL)[];

export default async function AdminConcursosPage() {
  await requireAdmin();
  const [settings, signed, waiting] = await Promise.all([
    db.contestSetting.findMany(),
    db.contract.groupBy({ by: ["contest"], where: { status: { not: "CANCELLED" } }, _count: { _all: true } }),
    // acesso liberado sem prazo: recebem o limite assim que a data da prova for cadastrada
    db.contract.groupBy({ by: ["contest"], where: { status: { not: "CANCELLED" }, accessGrantedAt: { not: null }, accessUntil: null, userId: { not: null } }, _count: { _all: true } }),
  ]);
  const byKey = new Map(settings.map((s) => [s.contest, s]));
  const signedBy = new Map(signed.map((r) => [r.contest, r._count._all]));
  const waitingBy = new Map(waiting.map((r) => [r.contest, r._count._all]));

  return (
    <div className="space-y-6">
      <Link href="/admin" className="text-sm font-semibold text-muted underline">← Administração</Link>
      <PageHeader
        eyebrow="Administração"
        title="Concursos"
        description="Dados de cada concurso do site: categoria, data oficial da prova, preço e desconto. Cadastrada a data, todo aluno que contratou o concurso passa a ter o acesso até o fim desse dia."
      />
      <Card tone="soft" className="space-y-1 text-sm">
        <p className="font-semibold">Como funciona o acesso</p>
        <p className="text-muted">
          Enquanto a prova não tem data (edital não publicado), quem contrata e paga fica com o acesso sem prazo. Ao salvar a data de um concurso, o limite (23:59 do dia da prova, em Recife) é aplicado a todos os alunos que contrataram esse concurso. Mudar a data depois também atualiza o limite deles.
        </p>
        <p className="text-muted">
          Regras comerciais padrão: preço original de Oficial e PCPE {formatBRL(CATEGORY_PRICE_CENTS.OFICIAL)}, Praça {formatBRL(CATEGORY_PRICE_CENTS.PRACA)}; lançamento {LAUNCH_DISCOUNT_POINTS}%; cupom de parceiro +{PARTNER_COUPON_DISCOUNT_POINTS} p.p. Sem categoria, o concurso não pode ser contratado.
        </p>
      </Card>
      <div className="grid gap-3 lg:grid-cols-2">
        {CONTESTS.map((info) => {
          const c = info.key;
          const s = byKey.get(c);
          const total = signedBy.get(c) ?? 0;
          const pending = waitingBy.get(c) ?? 0;
          return (
            <Card key={c} className="space-y-3">
              <div className="flex flex-wrap items-start justify-between gap-2">
                <div>
                  <h3 className="font-display text-lg font-bold uppercase">{contestName(c)}</h3>
                  <p className="text-xs text-muted">{CONTEST_SUBTITLES[c]}{info.category ? ` · ${info.category}` : ""}</p>
                </div>
                {!s?.category ? <Badge tone="warn">Sem categoria</Badge> : !s.examDate ? <Badge tone="warn">Data da prova pendente</Badge> : <Badge tone="ok">Completo</Badge>}
              </div>
              <dl className="grid grid-cols-3 gap-2 text-xs">
                <div className="rounded-lg bg-surface-2 px-3 py-2">
                  <dt className="text-muted">Data da prova</dt>
                  <dd className="font-semibold">{s?.examDate ? dayBR(s.examDate) : "A definir"}</dd>
                </div>
                <div className="rounded-lg bg-surface-2 px-3 py-2">
                  <dt className="text-muted">Contratações</dt>
                  <dd className="font-semibold tabular">{total}</dd>
                </div>
                <div className="rounded-lg bg-surface-2 px-3 py-2">
                  <dt className="text-muted">Acesso sem prazo</dt>
                  <dd className="font-semibold tabular">{pending}</dd>
                </div>
              </dl>
              <ActionForm action={adminUpdateContestSetting} submitLabel="Salvar" submitSize="sm" resetOnSuccess={false} className="grid gap-3 sm:grid-cols-2">
                <input type="hidden" name="contest" value={c} />
                <Field label="Categoria comercial">
                  <select name="category" defaultValue={s?.category ?? ""} className={inputCls}>
                    <option value="">— em revisão —</option>
                    {CATEGORIES.map((k) => (
                      <option key={k} value={k}>{CATEGORY_LABEL[k]}</option>
                    ))}
                  </select>
                </Field>
                <Field label="Data oficial da prova" hint="Ao salvar, o limite de acesso dos alunos deste concurso é definido.">
                  <input type="date" name="examDate" defaultValue={s?.examDate?.toISOString().slice(0, 10) ?? ""} className={inputCls} />
                </Field>
                <Field label="Preço do concurso (R$)" hint={`Vazio: padrão da categoria${s?.category ? ` (${formatBRL(CATEGORY_PRICE_CENTS[s.category])})` : ""}.`}>
                  <input name="price" inputMode="decimal" defaultValue={s?.priceCents ? (s.priceCents / 100).toFixed(2).replace(".", ",") : ""} placeholder={s?.category ? (CATEGORY_PRICE_CENTS[s.category] / 100).toFixed(2).replace(".", ",") : ""} className={inputCls} />
                </Field>
                <Field label="Desconto do site (%)" hint={`Vazio: desconto de lançamento padrão (${LAUNCH_DISCOUNT_POINTS}%). Use 0 para não dar desconto.`}>
                  <input name="siteDiscount" inputMode="numeric" defaultValue={s?.siteDiscountPoints ?? ""} placeholder={String(LAUNCH_DISCOUNT_POINTS)} className={inputCls} />
                </Field>
              </ActionForm>
              {s?.category && (() => {
                const q = quote(s.category, 0, s);
                const qc = quote(s.category, PARTNER_COUPON_DISCOUNT_POINTS, s);
                return (
                  <p className="rounded-lg bg-surface-2 px-3 py-2 text-xs text-muted">
                    Valor ao aluno: <strong className="text-text">{formatBRL(q.finalCents)}</strong>
                    {q.discountCents > 0 && <> (de {formatBRL(q.originalCents)}, {q.launchDiscountPoints}% de desconto)</>}
                    {" · "}com cupom de parceiro: <strong className="text-text">{formatBRL(qc.finalCents)}</strong>. Contratações já registradas não mudam de preço.
                  </p>
                );
              })()}
            </Card>
          );
        })}
      </div>
      <Alert tone="info">Nome, cargo, banca e conteúdo de cada concurso fazem parte do produto (planejador e editais); mudanças neles passam pelo desenvolvimento.</Alert>
    </div>
  );
}
