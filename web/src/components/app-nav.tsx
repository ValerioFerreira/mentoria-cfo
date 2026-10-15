"use client";

import { BadgePercent, CalendarDays, ChartNoAxesColumn, CreditCard, Crosshair, Ellipsis, Handshake, ListChecks, Map as MapIcon, NotebookPen, Send, ShieldCheck, Trophy, Users, Wallet, X, type LucideIcon } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { useEffect, useRef, useState, type KeyboardEvent, type ReactNode } from "react";
import { createPortal } from "react-dom";
import { Brand } from "@/components/brand";

const ICONS: Record<string, LucideIcon> = {
  today: Crosshair,
  week: CalendarDays,
  plan: MapIcon,
  quiz: ListChecks,
  simulado: Trophy,
  notes: NotebookPen,
  perf: ChartNoAxesColumn,
  billing: CreditCard,
  admin: ShieldCheck,
  users: Users,
  release: Send,
  finance: Wallet,
  partners: Handshake,
  partnership: BadgePercent,
};

export interface NavItem {
  href: string;
  label: string;
  icon: keyof typeof ICONS;
  /** rótulo curto da barra inferior (celular); sem ele usa `label` */
  short?: string;
}

function isActive(path: string, href: string) {
  if (href === "/") return path === "/" || path.startsWith("/atividade") || path.startsWith("/caderno");
  return path === href || path.startsWith(`${href}/`);
}

/** quantos itens ficam na barra inferior; o resto e a conta vão para o painel "Mais" */
const BAR_ITEMS = 4;
const FOCUSABLE = 'a[href], button:not([disabled]), [tabindex]:not([tabindex="-1"])';

/**
 * Painel "Mais" (celular e tablet em pé): itens que não cabem na barra e a conta (perfil e sair), que
 * só existiam no menu lateral. Abre por baixo, fecha com Esc, toque fora, botão ou ao trocar de página.
 */
function MoreSheet({ items, user, path, subtitle }: { items: NavItem[]; user: ReactNode; path: string; subtitle: string }) {
  // o painel fica preso à página em que foi aberto: navegar o fecha, sem efeito colateral
  const [openAt, setOpenAt] = useState<string | null>(null);
  const open = openAt === path;
  const trigger = useRef<HTMLButtonElement>(null);
  const dialog = useRef<HTMLDivElement>(null);
  const onAccount = path === "/perfil" || items.some((n) => isActive(path, n.href));

  function close() {
    setOpenAt(null);
    trigger.current?.focus();
  }

  useEffect(() => {
    if (!open) return;
    const prev = document.documentElement.style.overflow;
    document.documentElement.style.overflow = "hidden";
    dialog.current?.querySelector<HTMLElement>(FOCUSABLE)?.focus();
    return () => {
      document.documentElement.style.overflow = prev;
    };
  }, [open]);

  function onKeyDown(e: KeyboardEvent<HTMLDivElement>) {
    if (e.key === "Escape") {
      e.stopPropagation();
      close();
      return;
    }
    if (e.key !== "Tab") return;
    const nodes = dialog.current?.querySelectorAll<HTMLElement>(FOCUSABLE);
    if (!nodes?.length) return;
    const first = nodes[0];
    const last = nodes[nodes.length - 1];
    if (e.shiftKey && document.activeElement === first) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && document.activeElement === last) {
      e.preventDefault();
      first.focus();
    }
  }

  return (
    <>
      <button
        ref={trigger}
        type="button"
        onClick={() => setOpenAt(path)}
        aria-haspopup="dialog"
        aria-expanded={open}
        className={`relative flex min-h-14 cursor-pointer flex-col items-center justify-center gap-0.5 px-0.5 py-2 text-center text-[11px] font-semibold leading-tight transition ${onAccount ? "text-on-ink" : "text-on-ink-muted"}`}
      >
        <span className={`absolute top-0 h-0.5 rounded-b-full bg-primary transition-all duration-300 ${onAccount ? "w-8" : "w-0"}`} />
        <Ellipsis className={`h-5 w-5 ${onAccount ? "text-primary" : ""}`} aria-hidden />
        Mais
      </button>
      {/* portal: a barra tem backdrop-filter, que prende elementos `fixed` ao seu próprio quadro */}
      {open && createPortal(
        <div className="fixed inset-0 z-[55] lg:hidden" onKeyDown={onKeyDown}>
          <button type="button" tabIndex={-1} aria-label="Fechar o menu" onClick={close} className="absolute inset-0 cursor-default bg-black/55 backdrop-blur-[2px]" />
          <div
            ref={dialog}
            role="dialog"
            aria-modal="true"
            aria-label="Mais opções"
            className="pop absolute inset-x-0 bottom-0 mx-auto flex max-h-[88dvh] w-full max-w-xl origin-bottom flex-col overflow-y-auto overscroll-contain rounded-t-3xl border border-b-0 border-white/10 bg-ink p-4 pb-[max(1rem,env(safe-area-inset-bottom))] text-on-ink shadow-lift"
          >
            <div className="mb-2 flex items-center justify-between gap-3 px-1">
              <p className="eyebrow !text-on-ink-muted">{subtitle}</p>
              <button type="button" onClick={close} aria-label="Fechar o menu" className="-mr-1 flex h-11 w-11 cursor-pointer items-center justify-center rounded-xl text-on-ink-muted transition hover:bg-white/10 hover:text-on-ink">
                <X className="h-5 w-5" aria-hidden />
              </button>
            </div>
            {items.length > 0 && (
              <nav aria-label="Mais páginas" className="space-y-1">
                {items.map((n) => {
                  const Icon = ICONS[n.icon];
                  const on = isActive(path, n.href);
                  return (
                    <Link key={n.href} href={n.href} aria-current={on ? "page" : undefined} className={`flex min-h-12 items-center gap-3 rounded-xl px-3.5 py-2.5 text-[15px] font-semibold transition ${on ? "bg-white/10 text-on-ink" : "text-on-ink-muted hover:bg-white/5 hover:text-on-ink"}`}>
                      <Icon className={`h-5 w-5 shrink-0 ${on ? "text-primary" : ""}`} aria-hidden />
                      {n.label}
                    </Link>
                  );
                })}
              </nav>
            )}
            <div className="tape tape-rule my-4" aria-hidden />
            <div className="rounded-xl bg-white/5 p-2.5">{user}</div>
            <p className="mt-3 text-center text-[11px] leading-snug text-on-ink-muted">
              Desenvolvido por{" "}
              <a href="https://safercode.com.br" target="_blank" rel="noopener noreferrer" className="font-semibold text-on-ink underline-offset-2 hover:text-gold hover:underline">
                SaferCode Softwares
              </a>
            </p>
          </div>
        </div>,
        document.body,
      )}
    </>
  );
}

/**
 * Casca de navegação: trilho lateral (desktop) e barra inferior (celular).
 * `user` e `appearance` chegam prontos do servidor.
 */
export function AppNav({
  items,
  user,
  appearance,
  subtitle = "OFICIAL - CBMPE",
}: {
  items: NavItem[];
  user: ReactNode;
  appearance: ReactNode;
  subtitle?: string;
}) {
  const path = usePathname();
  return (
    <>
      {/* desktop */}
      <aside className="fixed inset-y-0 left-0 z-30 hidden w-64 flex-col bg-ink text-on-ink lg:flex" aria-label="Menu lateral">
        <div className="absolute inset-0 -z-10 overflow-hidden" aria-hidden>
          <div className="absolute -left-24 -top-24 h-72 w-72 rounded-full bg-primary/20 blur-3xl" />
          <div className="absolute -bottom-32 -right-20 h-72 w-72 rounded-full bg-teoria/10 blur-3xl" />
        </div>
        <div className="px-6 pb-5 pt-7">
          <Link href="/" aria-label="MentorIA — início">
            <Brand inverse subtitle={subtitle} />
          </Link>
        </div>
        <div className="tape tape-rule mx-6 mb-5" aria-hidden />
        <nav className="flex-1 space-y-1 px-3" aria-label="Principal">
          {items.map((n) => {
            const Icon = ICONS[n.icon];
            const on = isActive(path, n.href);
            return (
              <Link
                key={n.href}
                href={n.href}
                aria-current={on ? "page" : undefined}
                className={`group relative flex items-center gap-3 rounded-xl px-3.5 py-2.5 text-sm font-semibold transition duration-200 ${on ? "bg-white/10 text-on-ink" : "text-on-ink-muted hover:bg-white/5 hover:text-on-ink"}`}
              >
                <span className={`absolute left-0 top-1/2 h-5 w-1 -translate-y-1/2 rounded-r-full bg-primary transition-all duration-300 ${on ? "opacity-100" : "h-0 opacity-0"}`} />
                <Icon className={`h-[18px] w-[18px] transition-transform duration-200 group-hover:scale-110 ${on ? "text-primary" : ""}`} aria-hidden />
                {n.label}
              </Link>
            );
          })}
        </nav>
        <div className="p-4">
          <div className="rounded-xl bg-white/5 p-2.5">{user}</div>
          <p className="mt-2.5 text-center text-[11px] leading-snug text-on-ink-muted">
            Desenvolvido por{" "}
            <a href="https://safercode.com.br" target="_blank" rel="noopener noreferrer" className="font-semibold text-on-ink underline-offset-2 transition hover:text-gold hover:underline">
              SaferCode Softwares
            </a>
          </p>
        </div>
      </aside>

      {/* celular: barra superior + abas */}
      <header className="sticky top-0 z-30 flex items-center justify-between border-b border-white/10 bg-ink/95 px-4 py-2.5 text-on-ink backdrop-blur lg:hidden">
        <Link href="/" aria-label="MentorIA — início">
          <Brand inverse subtitle={subtitle} />
        </Link>
        {appearance}
      </header>
      <nav
        className="fixed inset-x-0 bottom-0 z-30 grid border-t border-white/10 bg-ink/95 pb-[env(safe-area-inset-bottom)] text-on-ink backdrop-blur lg:hidden"
        style={{ gridTemplateColumns: `repeat(${Math.min(items.length, BAR_ITEMS) + 1}, minmax(0, 1fr))` }}
        aria-label="Principal"
      >
        {items.slice(0, BAR_ITEMS).map((n) => {
          const Icon = ICONS[n.icon];
          const on = isActive(path, n.href);
          return (
            <Link key={n.href} href={n.href} aria-current={on ? "page" : undefined} className={`relative flex min-h-14 flex-col items-center justify-center gap-0.5 px-0.5 py-2 text-center text-[11px] font-semibold leading-tight transition ${on ? "text-on-ink" : "text-on-ink-muted"}`}>
              <span className={`absolute top-0 h-0.5 rounded-b-full bg-primary transition-all duration-300 ${on ? "w-8" : "w-0"}`} />
              <Icon className={`h-5 w-5 ${on ? "text-primary" : ""}`} aria-hidden />
              <span className="max-w-full truncate">{n.short ?? n.label}</span>
            </Link>
          );
        })}
        <MoreSheet items={items.slice(BAR_ITEMS)} user={user} path={path} subtitle={subtitle} />
      </nav>
    </>
  );
}
