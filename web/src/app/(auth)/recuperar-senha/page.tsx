import type { Metadata } from "next";
import { redirect } from "next/navigation";
import { getCurrentUser } from "@/lib/auth/session";
import { ForgotPasswordForm } from "./forgot-password-form";

export const metadata: Metadata = { title: "Recuperar Senha" };

export default async function ForgotPasswordPage() {
  if (await getCurrentUser()) redirect("/");
  return <ForgotPasswordForm />;
}
