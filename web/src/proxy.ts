import { NextResponse, type NextRequest } from "next/server";

// Checagem otimista (só presença do cookie). A validação de verdade acontece no DAL (requireUser).
const PUBLIC = ["/login", "/cadastro", "/concursos", "/lista-de-espera"];

export default function proxy(req: NextRequest) {
  const { pathname } = req.nextUrl;
  const hasSession = Boolean(req.cookies.get("cfo_session")?.value);
  // quem ainda não entrou vê a escolha do concurso na página inicial
  if (!hasSession && pathname === "/") return NextResponse.rewrite(new URL("/concursos", req.nextUrl));
  const isPublic = PUBLIC.some((p) => pathname === p || pathname.startsWith(p + "/"));
  if (!hasSession && !isPublic) return NextResponse.redirect(new URL("/login", req.nextUrl));
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\.(?:png|svg|jpg|jpeg|webp|ico|pdf)$).*)"],
};
