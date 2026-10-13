import Link from "next/link";
import { Button, inputCls } from "@/components/ui";
import { CONTRACT_STATUS, PAYMENT_METHOD_LABEL, contestName } from "@/lib/commerce/labels";
import { FILTER_CONTESTS, FILTER_METHODS, FILTER_STATUSES } from "./filters";

/** Filtros por GET (ficam na URL): cliente, concurso, período, situação financeira e forma de pagamento. */
export function FilterBar({ action, raw, hidden, show = ["q", "concurso", "situacao", "forma", "periodo"] }: {
  action: string;
  raw: Record<string, string>;
  hidden?: Record<string, string>;
  show?: ("q" | "concurso" | "situacao" | "forma" | "periodo")[];
}) {
  const sel = `${inputCls} py-2`;
  const box = "min-w-[11rem] flex-1";
  return (
    <form method="get" action={action} className="flex flex-wrap items-end gap-2 rounded-2xl border border-border bg-surface-2 p-3">
      {hidden && Object.entries(hidden).map(([k, v]) => <input key={k} type="hidden" name={k} value={v} />)}
      {show.includes("q") && (
        <input name="q" defaultValue={raw.q} placeholder="E-mail ou nome do cliente" aria-label="Cliente" className={`${sel} min-w-[14rem] flex-[2]`} />
      )}
      {show.includes("concurso") && (
        <select name="concurso" defaultValue={raw.concurso ?? ""} aria-label="Concurso" className={`${sel} ${box} w-auto`}>
          <option value="">Todos os concursos</option>
          {FILTER_CONTESTS.map((c) => <option key={c} value={c}>{contestName(c)}</option>)}
        </select>
      )}
      {show.includes("situacao") && (
        <select name="situacao" defaultValue={raw.situacao ?? ""} aria-label="Situação financeira" className={`${sel} ${box} w-auto`}>
          <option value="">Todas as situações</option>
          {FILTER_STATUSES.map((s) => <option key={s} value={s}>{CONTRACT_STATUS[s].label}</option>)}
        </select>
      )}
      {show.includes("forma") && (
        <select name="forma" defaultValue={raw.forma ?? ""} aria-label="Forma de pagamento" className={`${sel} ${box} w-auto`}>
          <option value="">Todas as formas</option>
          {FILTER_METHODS.map((m) => <option key={m} value={m}>{PAYMENT_METHOD_LABEL[m]}</option>)}
        </select>
      )}
      {show.includes("periodo") && (
        <div className="flex min-w-[18rem] flex-[2] items-center gap-2">
          <input type="date" name="de" defaultValue={raw.de} aria-label="De" className={`${sel} min-w-0`} />
          <span className="text-xs text-muted">até</span>
          <input type="date" name="ate" defaultValue={raw.ate} aria-label="Até" className={`${sel} min-w-0`} />
        </div>
      )}
      <div className="flex shrink-0 items-center gap-3">
        <Button type="submit" size="sm">Filtrar</Button>
        <Link href={hidden ? `${action}?${new URLSearchParams(hidden)}` : action} className="self-center text-sm font-semibold text-muted underline">Limpar</Link>
      </div>
    </form>
  );
}
