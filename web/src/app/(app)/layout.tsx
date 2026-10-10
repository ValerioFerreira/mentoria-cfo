import Link from "next/link";
import { LogOut, User as UserIcon } from "lucide-react";
import { AppearanceMenu } from "@/components/appearance-menu";
import { AppNav, type NavItem } from "@/components/app-nav";
import { TimerWidget } from "@/components/timer-widget";
import { requireUser } from "@/lib/auth/dal";
import { getTheme } from "@/lib/theme";
import { getUserContestSubtitle } from "@/lib/user-contest";
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
  const contestSubtitle = await getUserContestSubtitle(user.email);
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
    <div className="flex items-center gap-2">
      <Link
        href="/perfil"
        className="group flex min-w-0 flex-1 items-center gap-2.5 rounded-lg p-1.5 transition hover:bg-white/10"
        title="Ver meu perfil e segurança"
      >
        <span
          className="flex h-9 w-9 shrink-0 items-center justify-center rounded-full bg-gradient-to-br from-primary to-gold font-display text-base font-bold uppercase text-on-primary shadow-sm"
          aria-hidden
        >
          {name.trim().charAt(0)}
        </span>
        <span className="min-w-0 flex-1 text-left">
          <span className="block truncate text-xs font-semibold leading-tight text-on-ink group-hover:text-gold transition">
            {user.name ?? "Aluno"}
          </span>
          <span className="block truncate text-[11px] text-on-ink-muted">
            {user.email}
          </span>
        </span>
      </Link>
      <form action={logout} className="shrink-0">
        <button
          type="submit"
          title="Sair da conta"
          className="flex h-8 w-8 cursor-pointer items-center justify-center rounded-lg text-on-ink-muted transition hover:bg-white/10 hover:text-red-400"
        >
          <LogOut className="h-4 w-4" aria-hidden />
          <span className="sr-only">Sair</span>
        </button>
      </form>
    </div>
  );

  return (
    <>
      <AppNav items={nav} user={who} appearance={<AppearanceMenu initial={theme} inverse />} subtitle={contestSubtitle} />
      <div className="flex flex-1 flex-col lg:pl-64">
        <div className="sticky top-0 z-20 pointer-events-none hidden justify-end px-10 pt-4 lg:flex">
          <div className="pointer-events-auto">
            <AppearanceMenu initial={theme} />
          </div>
        </div>
        <main className="mx-auto w-full max-w-6xl flex-1 px-4 py-6 pb-32 lg:px-10 lg:pb-24 lg:pt-4">{children}</main>
      </div>
      <TimerWidget />
    </>
  );
}
