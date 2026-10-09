"use client";

import { CalendarDays, ChartNoAxesColumn, Crosshair, Map as MapIcon, ShieldCheck, type LucideIcon } from "lucide-react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import type { ReactNode } from "react";
import { Brand } from "@/components/brand";

const ICONS: Record<string, LucideIcon> = { today: Crosshair, week: CalendarDays, plan: MapIcon, perf: ChartNoAxesColumn, admin: ShieldCheck };

export interface NavItem {
  href: string;
  label: string;
  icon: keyof typeof ICONS;
}

function isActive(path: string, href: string) {
  if (href === "/") return path === "/" || path.startsWith("/atividade") || path.startsWith("/caderno");
  return path === href || path.startsWith(`${href}/`);
}

/**
 * Casca de navegação: trilho lateral (desktop) e barra inferior (celular).
 * `user` e `appearance` chegam prontos do servidor.
 */
export function AppNav({ items, user, appearance }: { items: NavItem[]; user: ReactNode; appearance: ReactNode }) {
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
            <Brand inverse subtitle="Missão Oficial · CBMPE" />
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
          <Brand inverse subtitle="Missão Oficial · CBMPE" />
        </Link>
        {appearance}
      </header>
      <nav
        className="fixed inset-x-0 bottom-0 z-30 grid border-t border-white/10 bg-ink/95 pb-[env(safe-area-inset-bottom)] text-on-ink backdrop-blur lg:hidden"
        style={{ gridTemplateColumns: `repeat(${items.length}, minmax(0, 1fr))` }}
        aria-label="Principal"
      >
        {items.map((n) => {
          const Icon = ICONS[n.icon];
          const on = isActive(path, n.href);
          return (
            <Link key={n.href} href={n.href} aria-current={on ? "page" : undefined} className={`relative flex flex-col items-center gap-0.5 px-1 py-2.5 text-center text-[10.5px] font-semibold leading-tight transition ${on ? "text-on-ink" : "text-on-ink-muted"}`}>
              <span className={`absolute top-0 h-0.5 rounded-b-full bg-primary transition-all duration-300 ${on ? "w-8" : "w-0"}`} />
              <Icon className={`h-5 w-5 ${on ? "text-primary" : ""}`} aria-hidden />
              {n.label}
            </Link>
          );
        })}
      </nav>
    </>
  );
}
