import type { ReactNode } from "react";
import Link from "next/link";
import { AppearanceMenu } from "@/components/appearance-menu";
import { Brand } from "@/components/brand";
import { getTheme } from "@/lib/theme";

/** Casca das páginas públicas (escolha do concurso e lista de espera). */
export default async function PublicLayout({ children }: { children: ReactNode }) {
  const theme = await getTheme();
  return (
    <div className="flex min-h-screen flex-col">
      <header className="mx-auto flex w-full max-w-6xl items-center justify-between gap-4 px-5 py-5 sm:px-8">
        <Link href="/" aria-label="MentorIA — início">
          <Brand />
        </Link>
        <div className="flex items-center gap-3">
          <Link href="/login" className="rounded-lg px-3 py-1.5 text-sm font-semibold text-muted transition hover:bg-surface-3/70 hover:text-text">
            Já tenho acesso
          </Link>
          <AppearanceMenu initial={theme} />
        </div>
      </header>
      <main className="mx-auto w-full max-w-6xl flex-1 px-5 pb-16 sm:px-8">{children}</main>
    </div>
  );
}
