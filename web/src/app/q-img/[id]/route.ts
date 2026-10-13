// Figuras e recortes (fórmulas, tabelas) das questões importadas dos cadernos. Ficam no banco
// (QuestionImage) para que questão nova apareça sem deploy; o id é o sha256 do PNG, então a
// resposta nunca muda e pode ficar em cache no navegador.
import type { NextRequest } from "next/server";
import { getCurrentUser } from "@/lib/auth/session";
import { db } from "@/lib/db";

export async function GET(_req: NextRequest, ctx: RouteContext<"/q-img/[id]">) {
  const { id } = await ctx.params;
  if (!/^[0-9a-f]{64}$/.test(id)) return new Response("Not found", { status: 404 });
  if (!(await getCurrentUser())) return new Response("Unauthorized", { status: 401 });
  const img = await db.questionImage.findUnique({ where: { id }, select: { data: true, mime: true } });
  if (!img) return new Response("Not found", { status: 404 });
  return new Response(new Uint8Array(img.data), {
    headers: {
      "Content-Type": img.mime,
      "Cache-Control": "private, max-age=31536000, immutable",
    },
  });
}
