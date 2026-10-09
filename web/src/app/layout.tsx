import type { Metadata, Viewport } from "next";
import { Barlow_Condensed, Public_Sans } from "next/font/google";
import { cookies } from "next/headers";
import { FaviconFlame } from "@/components/favicon-flame";
import "./globals.css";

const display = Barlow_Condensed({ subsets: ["latin"], weight: ["500", "600", "700", "800"], variable: "--font-barlow", display: "swap" });
const sans = Public_Sans({ subsets: ["latin"], variable: "--font-public", display: "swap" });

export const metadata: Metadata = {
  title: { default: "MentorIA", template: "%s · MentorIA" },
  description: "Plano de estudos exclusivo e individualizado para concursos: direcionamento detalhado, resumos e questões com a pegada da banca.",
};

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#edf0f4" },
    { media: "(prefers-color-scheme: dark)", color: "#080f1a" },
  ],
};

export default async function RootLayout({ children }: LayoutProps<"/">) {
  // o tema escolhido vem de um cookie: o servidor já entrega o <html> certo, sem script e sem piscar
  const saved = (await cookies()).get("theme")?.value;
  const theme = saved === "light" || saved === "sepia" || saved === "dark" ? saved : undefined;
  return (
    <html lang="pt-BR" data-theme={theme} className={`${display.variable} ${sans.variable} h-full`} suppressHydrationWarning>
      <body className="min-h-full flex flex-col">
        <FaviconFlame />
        {children}
      </body>
    </html>
  );
}
