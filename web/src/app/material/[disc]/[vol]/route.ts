// PDF de um volume do material próprio MentorIA (material-pdf/<disciplina>/mNN.pdf, gerado por pipeline/build_material.py).
// Lê do Cloudflare R2 (ou do disco, sem R2 configurado: lib/material-storage.ts), carimba nome e CPF do aluno na faixa do
// rodapé de cada página e entrega por streaming (a resposta comum da Vercel é limitada a 4,5 MB). Sem CPF no perfil o aluno é levado a informá-lo. O "#page=X" do link é tratado
// pelo leitor de PDF.
import type { NextRequest } from "next/server";
import { getCurrentUser } from "@/lib/auth/session";
import { hasBillingAccess } from "@/lib/billing/access";
import { formatCpf } from "@/lib/cpf";
import { db } from "@/lib/db";
import { hasVolume } from "@/lib/material";
import { readMaterialPdf, streamBytes } from "@/lib/material-storage";
import { stampPdf } from "@/lib/material-stamp";

export const runtime = "nodejs";
export const maxDuration = 60;

export async function GET(req: NextRequest, ctx: { params: Promise<{ disc: string; vol: string }> }) {
  const { disc, vol } = await ctx.params;
  if (!/^[a-z-]+$/.test(disc) || !/^m\d{2}$/.test(vol) || !hasVolume(`${disc}/${vol}`)) return new Response("Not found", { status: 404 });
  const user = await getCurrentUser();
  if (!user) return new Response("Unauthorized", { status: 401 });
  if (!user.isPartner && user.accessExpiresAt && user.accessExpiresAt < new Date() && !(await hasBillingAccess(user.id))) {
    return new Response("Forbidden", { status: 403 });
  }
  const owner = await db.user.findUnique({ where: { id: user.id }, select: { id: true, name: true, email: true, cpf: true, role: true } });
  if (!owner) return new Response("Unauthorized", { status: 401 });
  // administrador sem CPF cadastrado recebe o carimbo com o e-mail; aluno precisa informar o CPF no perfil
  if (!owner.cpf && owner.role === "USER" && !user.isPartner) return Response.redirect(new URL("/perfil?cpf=necessario", req.url), 302);
  let pdf: Uint8Array | null;
  try {
    pdf = await readMaterialPdf(disc, vol);
  } catch (err) {
    console.error("[material] falha ao ler o PDF do armazenamento", err instanceof Error ? err.message : "erro desconhecido");
    return new Response("Não foi possível abrir o PDF agora.", { status: 502 });
  }
  if (!pdf) return new Response("Not found", { status: 404 });
  let stamped: Uint8Array;
  try {
    stamped = await stampPdf(pdf, { id: owner.id, name: owner.name ?? owner.email, idLabel: owner.cpf ? `CPF ${formatCpf(owner.cpf)}` : owner.email.toUpperCase() });
  } catch (err) {
    console.error("[material] falha ao carimbar o PDF", err instanceof Error ? err.message : "erro desconhecido");
    return new Response("Não foi possível preparar o PDF agora.", { status: 500 });
  }
  // streaming: os PDFs passam de 4,5 MB, o limite da resposta comum da Vercel
  return new Response(streamBytes(stamped), {
    headers: {
      "Content-Type": "application/pdf",
      "Content-Length": String(stamped.length),
      "Content-Disposition": `inline; filename="mentoria-${disc}-${vol}.pdf"`,
      "Cache-Control": "private, no-store",
    },
  });
}
