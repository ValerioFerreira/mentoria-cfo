import Link from "next/link";
import { LogOut, User as UserIcon } from "lucide-react";
import { AppearanceMenu } from "@/components/appearance-menu";
import { AppNav, type NavItem } from "@/components/app-nav";
import { TimerWidget } from "@/components/timer-widget";
import { requireUser } from "@/lib/auth/dal";
import { getTheme } from "@/lib/theme";
import { logout } from "../(auth)/actions";

const NAV: NavItem[] = [
  { href: "/", label: "Missão de hoje", icon: "today" },
  { href: "/semana", label: "Meta semanal", icon: "week" },
  { href: "/plano", label: "Planejamento", icon: "plan" },
  { href: "/resumos", label: "Meus resumos", icon: "notes" },
  { href: "/desempenho", label: "Desempenho", icon: "perf" },
];

export default async function AppLayout({ children }: LayoutProps<"/">) {
  const user = await requireUser();
  const theme = await getTheme();
  if (user.role !== "ADMIN" && process.env.APP_ENABLED !== "true") {
    return (
      <main className="mx-auto flex min-h-screen max-w-xl flex-1 flex-col items-center justify-center gap-4 px-6 text-center">
        <h1 className="font-display text-3xl font-bold">Cadastro confirmado!</h1>
        <p className="text-on-surface-muted">
          Sua conta está criada. Avisaremos assim que o plano de estudos for liberado.
        </p>
        <form action={logout}>
          <button type="submit" className="cursor-pointer text-sm underline">
            Sair
          </button>
        </form>
      </main>
    );
  }

  const nav: NavItem[] =
    user.role === "ADMIN"
      ? [
          ...NAV,
          { href: "/admin/cadastros", label: "Cadastros", icon: "users" },
          { href: "/admin/revisao", label: "Revisão", icon: "admin" },
        ]
      : NAV;
  const name = user.name ?? user.email;

  const who = (
    <div className="space-y-2">
      <Link
        href="/perfil"
        className="flex items-center gap-2.5 rounded-lg p-1 transition hover:bg-white/5"
        title="Ver meu perfil e segurança"
      >
        <span className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-gold font-display text-lg font-bold uppercase text-on-primary" aria-hidden>
          {name.trim().charAt(0)}
        </span>
        <span className="min-w-0 flex-1 text-left">
          <span className="block truncate text-[13px] font-semibold leading-tight text-on-ink">{user.name ?? "Aluno"}</span>
          <span className="block text-[11px] text-on-ink-muted hover:text-gold transition">Meu perfil →</span>
        </span>
      </Link>
      <form action={logout} className="flex justify-end px-1">
        <button type="submit" className="flex cursor-pointer items-center gap-1 text-xs text-on-ink-muted transition hover:text-on-ink">
          <LogOut className="h-3 w-3" aria-hidden />
          Sair
        </button>
      </form>
    </div>
  );

  return (
    <>
      <AppNav items={nav} user={who} appearance={<AppearanceMenu initial={theme} inverse />} />
      <div className="flex flex-1 flex-col lg:pl-64">
        <div className="sticky top-0 z-20 hidden justify-end px-10 pt-4 lg:flex">
          <AppearanceMenu initial={theme} />
        </div>
        <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-6 pb-32 lg:px-10 lg:pb-24 lg:pt-4">{children}</main>
      </div>
      <TimerWidget />
    </>
  );
}
