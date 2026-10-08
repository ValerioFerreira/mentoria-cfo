import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { SignupForm } from "./signup-form";

export const metadata: Metadata = { title: "Criar conta" };

export default async function SignupPage({ searchParams }: PageProps<"/cadastro">) {
  if (await getCurrentUser()) redirect("/");
  const sp = await searchParams;
  const invite = typeof sp.convite === "string" ? sp.convite : undefined;
  return <SignupForm invite={invite} />;
}
