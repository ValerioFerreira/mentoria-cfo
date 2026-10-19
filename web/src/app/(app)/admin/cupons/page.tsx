import type { Metadata } from "next";
import Link from "next/link";
import { ActionForm } from "@/components/action-form";
import { Badge, Card, Field, InfoTip, PageHeader, SectionTitle, inputCls } from "@/components/ui";
import { requireAdmin } from "@/lib/auth/dal";
import {
  adminCreateSiteCoupon,
  adminDeleteSiteCoupon,
  adminSetSiteCouponActive,
  adminUpdateSiteCoupon,
} from "@/lib/commerce/admin-actions";
import { listSiteCoupons } from "@/lib/commerce/coupons";
import { dateBR } from "@/lib/commerce/labels";
import { formatBRL } from "@/lib/commerce/money";
import { MAX_DISCOUNT_POINTS, quote } from "@/lib/commerce/pricing";

export const metadata: Metadata = { title: "Cupons" };

const th = "px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-muted";
const td = "px-3 py-2 align-top";

export default async function CouponsPage() {
  await requireAdmin();
  const coupons = await listSiteCoupons();
  const active = coupons.filter((c) => c.active).length;

  return (
    <div className="space-y-6">
      <Link href="/admin" className="text-sm font-semibold text-muted underline">← Administração</Link>
      <PageHeader
        eyebrow="Administração"
        title="Cupons"
        description={`${active} ${active === 1 ? "cupom ativo" : "cupons ativos"} de ${coupons.length}.`}
        info={
          <>
            <p>
              O desconto de cada cupom é um percentual do <strong>valor original</strong> e se <strong>soma</strong> aos demais (desconto de lançamento e cupom de parceiro), nunca em cascata.
            </p>
            <p className="mt-2">
              Exemplo: valor original R$ 100 com cupons de 25% e 10% = R$ 35 de desconto, valor final R$ 65 (e não 10% sobre os R$ 75). O total de desconto nunca passa de 100%: o preço mínimo é R$ 0.
            </p>
            <p className="mt-2">O cliente pode informar vários cupons na inscrição; o servidor confere cada código e calcula o preço.</p>
          </>
        }
      />

      <SectionTitle id="lista">Cupons cadastrados</SectionTitle>
      <Card className="overflow-x-auto p-0">
        <table className="w-full min-w-[820px] text-sm">
          <thead className="border-b border-border">
            <tr>
              <th className={th}>Código</th>
              <th className={th}>Desconto</th>
              <th className={th}>
                <span className="inline-flex items-center gap-1">
                  Exemplo (Oficial)
                  <InfoTip align="start">Preço do concurso Oficial no valor padrão, com o desconto de lançamento e só este cupom. Cada concurso pode ter preço e desconto próprios (Financeiro › Concursos).</InfoTip>
                </span>
              </th>
              <th className={th}>Usos</th>
              <th className={th}>Situação</th>
              <th className={th}>Ações</th>
            </tr>
          </thead>
          <tbody>
            {coupons.length === 0 && (
              <tr><td className={td} colSpan={6}><span className="text-muted">Nenhum cupom cadastrado.</span></td></tr>
            )}
            {coupons.map((c) => {
              const example = quote("OFICIAL", 0, undefined, [c.discountPoints]);
              return (
                <tr key={c.id} className="border-b border-border/60 align-top last:border-0 hover:bg-surface-2/60">
                  <td className={`${td} font-mono font-semibold`}>
                    {c.code}
                    <span className="block font-sans text-xs font-normal text-muted">criado em {dateBR(c.createdAt)}</span>
                  </td>
                  <td className={`${td} tabular whitespace-nowrap font-semibold`}>{c.discountPoints}%</td>
                  <td className={`${td} tabular whitespace-nowrap text-xs`}>
                    {formatBRL(example.finalCents)}
                    <span className="block text-muted">de {formatBRL(example.originalCents)}</span>
                  </td>
                  <td className={`${td} tabular whitespace-nowrap`}>{c.uses}</td>
                  <td className={td}>
                    {c.active ? <Badge tone="ok">Ativo</Badge> : <Badge tone="neutral">Inativo</Badge>}
                    {c.deactivatedAt && !c.active && <span className="mt-1 block text-xs text-muted">desde {dateBR(c.deactivatedAt)}</span>}
                  </td>
                  <td className={td}>
                    <div>
                      <div className="flex flex-wrap items-start gap-2">
                      <ActionForm
                        action={adminSetSiteCouponActive}
                        submitLabel={c.active ? "Inativar" : "Ativar"}
                        submitSize="sm"
                        submitVariant={c.active ? "secondary" : "primary"}
                        confirmText={c.active ? `Inativar o cupom ${c.code}? Ele deixa de valer para novas contratações; o histórico é mantido.` : undefined}
                        resetOnSuccess={false}
                      >
                        <input type="hidden" name="couponId" value={c.id} />
                        <input type="hidden" name="active" value={c.active ? "false" : "true"} />
                      </ActionForm>
                      <ActionForm
                        action={adminDeleteSiteCoupon}
                        submitLabel="Excluir"
                        submitSize="sm"
                        submitVariant="danger"
                        confirmText={`Excluir o cupom ${c.code}? Esta ação não pode ser desfeita.`}
                        resetOnSuccess={false}
                      >
                        <input type="hidden" name="couponId" value={c.id} />
                      </ActionForm>
                      </div>
                      <details className="group mt-2">
                        <summary className="cursor-pointer list-none rounded-xl border border-border px-3 py-1.5 text-xs font-semibold hover:bg-surface-2 group-open:bg-surface-2">Editar</summary>
                        <div className="mt-2 w-72 rounded-xl border border-border bg-surface p-3 shadow-lift">
                          <ActionForm action={adminUpdateSiteCoupon} submitLabel="Salvar" submitSize="sm" resetOnSuccess={false}>
                            <input type="hidden" name="couponId" value={c.id} />
                            {c.uses === 0 ? (
                              <Field label="Código"><input name="code" defaultValue={c.code} required minLength={4} maxLength={20} pattern="[A-Za-z0-9]{4,20}" autoComplete="off" className={`${inputCls} uppercase`} /></Field>
                            ) : (
                              <p className="text-xs text-muted">Código fixo: o cupom já foi usado em contratações.</p>
                            )}
                            <Field label="Desconto (%)" hint="Vale só para novas contratações.">
                              <input name="discountPoints" type="number" inputMode="numeric" min={1} max={MAX_DISCOUNT_POINTS} step={1} defaultValue={c.discountPoints} required className={inputCls} />
                            </Field>
                          </ActionForm>
                        </div>
                      </details>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </Card>

      <Card className="space-y-3">
        <h2 className="flex items-center gap-2 font-display text-lg font-bold uppercase">
          Novo cupom
          <InfoTip align="start">
            O código tem de 4 a 20 letras ou números (sem espaços ou acentos) e é único entre os cupons do site e os de parceiros. Cupom já usado numa contratação não pode ser excluído, apenas inativado.
          </InfoTip>
        </h2>
        <ActionForm action={adminCreateSiteCoupon} submitLabel="Criar cupom" className="grid gap-3 sm:grid-cols-2">
          <Field label="Código">
            <input name="code" required minLength={4} maxLength={20} pattern="[A-Za-z0-9]{4,20}" autoComplete="off" className={`${inputCls} uppercase`} />
          </Field>
          <Field label="Desconto (%)" hint={`Número inteiro de 1 a ${MAX_DISCOUNT_POINTS}, sobre o valor original.`}>
            <input name="discountPoints" type="number" inputMode="numeric" min={1} max={MAX_DISCOUNT_POINTS} step={1} required className={inputCls} />
          </Field>
        </ActionForm>
      </Card>
    </div>
  );
}
