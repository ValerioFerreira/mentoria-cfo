import { NextResponse, type NextRequest } from "next/server";

const PUBLIC = ["/login", "/cadastro", "/concursos", "/lista-de-espera", "/recuperar-senha", "/como-funciona"];

export default function proxy(req: NextRequest) {
  const { pathname } = req.nextUrl;
  const hasSession = Boolean(req.cookies.get("cfo_session")?.value);
  // quem ainda não entrou vê a página de login como página inicial
  if (!hasSession && pathname === "/") return NextResponse.rewrite(new URL("/login", req.nextUrl));
  const isPublic = PUBLIC.some((p) => pathname === p || pathname.startsWith(p + "/"));
  if (!hasSession && !isPublic) return NextResponse.redirect(new URL("/login", req.nextUrl));
  return NextResponse.next();
}

export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico|.*\.(?:png|svg|jpg|jpeg|webp|ico|pdf)$).*)"],
};
