import "server-only";
import { cookies } from "next/headers";
import type { Theme } from "@/components/appearance-menu";

/** Tema salvo no cookie (null = segue o sistema). */
export async function getTheme(): Promise<Theme | null> {
  const v = (await cookies()).get("theme")?.value;
  return v === "light" || v === "sepia" || v === "dark" ? v : null;
}
