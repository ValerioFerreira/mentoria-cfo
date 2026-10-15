// Teste de responsividade em navegador real (Chrome/Edge do sistema, via playwright-core: não baixa navegador).
//
//   npm run test:responsive                       # servidor já rodando em http://localhost:3000
//   BASE_URL=http://localhost:3001 npm run test:responsive -- --shots
//   npm run test:responsive -- --only=360,1024    # só algumas larguras
//   npm run test:responsive -- --routes=/plano,/desempenho
//
// Entra com uma conta de TESTE do banco local (E2E_EMAIL/E2E_PASSWORD, ou DEV_TEST_EMAIL/DEV_TEST_PASSWORD do web/.env).
// Nunca aponte para produção. Por viewport e rota confere: sem rolagem horizontal indevida, nada fora da tela,
// texto que vaza do próprio quadro, imagens/fórmulas dentro do contêiner, markdown cru na tela e erros no console.
// Por viewport também exercita: menu "Mais" (perfil e sair no celular), diálogo "Concluir atividade", balão "Tempo".
// Sai com código 1 se houver falha. Capturas de tela (--shots) vão para web/test-results/responsive/.
import "dotenv/config";
import { chromium } from "playwright-core";
import fs from "node:fs";
import path from "node:path";

const BASE = (process.env.BASE_URL ?? "http://localhost:3000").replace(/\/$/, "");
const EMAIL = process.env.E2E_EMAIL ?? process.env.DEV_TEST_EMAIL;
const PASSWORD = process.env.E2E_PASSWORD ?? process.env.DEV_TEST_PASSWORD;
const arg = (name) => process.argv.find((a) => a.startsWith(`--${name}=`))?.split("=")[1];
const SHOTS = process.argv.includes("--shots");

if (!/^https?:\/\/(localhost|127\.0\.0\.1|\[::1\]|[\w-]+\.localhost)(:\d+)?$/.test(BASE)) {
  console.error(`BASE_URL precisa ser um servidor local de desenvolvimento (recebi ${BASE}).`);
  process.exit(2);
}
if (!EMAIL || !PASSWORD) {
  console.error("Defina E2E_EMAIL e E2E_PASSWORD (conta de teste do banco local) ou DEV_TEST_EMAIL/DEV_TEST_PASSWORD no web/.env.");
  process.exit(2);
}

/** [largura, altura, nome]. Os valores são pontos de teste, não breakpoints do layout. */
const VIEWPORTS = [
  [320, 700, "celular-320"],
  [360, 740, "celular-360"],
  [375, 812, "celular-375"],
  [390, 844, "celular-390"],
  [430, 932, "celular-430"],
  [667, 375, "celular-paisagem-667"],
  [768, 1024, "tablet-768"],
  [1024, 768, "tablet-paisagem-1024"],
  [1280, 800, "desktop-1280"],
  [1440, 900, "desktop-1440"],
  [1920, 1080, "desktop-1920"],
];
const only = arg("only")?.split(",").map(Number);
const viewports = only ? VIEWPORTS.filter(([w]) => only.includes(w)) : VIEWPORTS;

/** rotas fixas; as dinâmicas (atividade, caderno, prática) são descobertas pelos links da tela */
const STATIC_ROUTES = ["/", "/semana/1", "/plano", "/questoes", "/simulados", "/resumos", "/resumos/biologia", "/desempenho", "/pagamentos", "/perfil", "/onboarding", "/admin", "/admin/cadastros", "/admin/financeiro", "/admin/parceiros", "/admin/revisao", "/como-funciona"];
const ANON_ROUTES = ["/login", "/cadastro", "/recuperar-senha", "/concursos", "/lista-de-espera/cbmpe-oficial", "/como-funciona"];

const failures = [];
const warnings = [];
const fail = (vp, route, msg) => failures.push(`[${vp}] ${route}: ${msg}`);
const warn = (vp, route, msg) => warnings.push(`[${vp}] ${route}: ${msg}`);

/** roda dentro da página: devolve o que estourou */
function measure() {
  const vw = document.documentElement.clientWidth;
  const out = { vw, scrollW: document.documentElement.scrollWidth, offenders: [], textOvf: [], rawMd: [], badImg: [] };
  const clipped = (el) => {
    for (let p = el.parentElement; p && p !== document.body; p = p.parentElement) if (getComputedStyle(p).overflowX !== "visible") return true;
    return false;
  };
  const desc = (el) => `${el.tagName.toLowerCase()}.${(el.getAttribute("class") || "").split(/\s+/).slice(0, 4).join(".")} «${(el.innerText || el.getAttribute("aria-label") || "").trim().replace(/\s+/g, " ").slice(0, 30)}»`;
  const bad = new Set();
  for (const el of document.body.querySelectorAll("*")) {
    const cs = getComputedStyle(el);
    if (cs.display === "none" || cs.visibility === "hidden") continue;
    const r = el.getBoundingClientRect();
    if (r.width === 0 && r.height === 0) continue;
    if (el.closest("svg, nextjs-portal, [data-nextjs-toast]")) continue;
    if ((r.right > vw + 1 || r.left < -1) && cs.position !== "fixed" && !clipped(el)) bad.add(el);
    // o balão (?) amplia a área de toque com um pseudo-elemento: isso aparece como estouro de poucos px e não é defeito
    const tipSlack = (el.matches('button[aria-label="Mais informações"]') || el.querySelector('button[aria-label="Mais informações"]')) && el.scrollWidth - el.clientWidth <= 14;
    if (!tipSlack && cs.overflowX === "visible" && cs.display !== "inline" && el.scrollWidth > el.clientWidth + 1 && el.clientWidth > 0 && !el.closest("table") && [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim())) {
      out.textOvf.push(`${desc(el)} ${el.scrollWidth}>${el.clientWidth}`);
    }
    if (el.tagName === "IMG" && r.width > 0 && (el.naturalWidth === 0 || r.right > vw + 1) && el.complete) out.badImg.push(desc(el));
  }
  out.offenders = [...bad].filter((el) => !bad.has(el.parentElement)).slice(0, 6).map((el) => `${desc(el)} [${Math.round(el.getBoundingClientRect().left)}..${Math.round(el.getBoundingClientRect().right)}]`);
  out.textOvf = out.textOvf.slice(0, 6);
  // markdown de imagem/fórmula que não foi interpretado
  const body = document.body.innerText;
  const m = body.match(/!\[[^\]]*\]\(\/q-img\/[0-9a-f]+\)/g);
  if (m) out.rawMd = m.slice(0, 3);
  return out;
}

async function login(page) {
  await page.goto(`${BASE}/login`, { waitUntil: "domcontentloaded" });
  await page.fill('input[type="email"]', EMAIL);
  await page.fill('input[type="password"]', PASSWORD);
  await Promise.all([page.waitForURL((u) => !u.pathname.startsWith("/login"), { timeout: 60_000 }), page.keyboard.press("Enter")]);
}

async function discoverRoutes(page) {
  const found = new Set();
  for (const from of ["/", "/semana/1", "/desempenho"]) {
    await page.goto(`${BASE}${from}`, { waitUntil: "load", timeout: 90_000 }).catch(() => {});
    const hrefs = await page.$$eval("a[href]", (as) => as.map((a) => a.getAttribute("href")));
    for (const prefix of ["/atividade/", "/caderno/", "/questoes/pratica/", "/simulados/resultado/"]) {
      const h = hrefs.find((x) => x?.startsWith(prefix));
      if (h) found.add(h);
    }
  }
  return [...found];
}

async function checkPage(page, vpName, route, vp) {
  const errors = [];
  const onErr = (m) => m.type() === "error" && !/favicon|Failed to load resource: the server responded with a status of (401|404)/.test(m.text()) && errors.push(m.text().slice(0, 160));
  const onPageErr = (e) => errors.push(String(e).slice(0, 160));
  page.on("console", onErr);
  page.on("pageerror", onPageErr);
  const res = await page.goto(`${BASE}${route}`, { waitUntil: "load", timeout: 90_000 }).catch((e) => ({ error: e }));
  if (!res || res.error) fail(vpName, route, `não carregou (${res?.error?.message?.slice(0, 80) ?? "sem resposta"})`);
  else if (res.status() >= 500) fail(vpName, route, `HTTP ${res.status()}`);
  await page.waitForTimeout(900); // animações de entrada
  const m = await page.evaluate(measure);
  if (m.scrollW > m.vw + 1) fail(vpName, route, `rolagem horizontal: página ${m.scrollW}px em viewport de ${m.vw}px · ${m.offenders.join(" | ") || "(sem elemento isolado)"}`);
  else if (m.offenders.length) fail(vpName, route, `elemento fora da tela: ${m.offenders.join(" | ")}`);
  if (m.rawMd.length) fail(vpName, route, `markdown de imagem/fórmula aparecendo como texto: ${m.rawMd[0]}`);
  if (m.badImg.length) fail(vpName, route, `imagem quebrada ou maior que a tela: ${m.badImg.join(" | ")}`);
  if (m.textOvf.length) warn(vpName, route, `texto vazando do quadro: ${m.textOvf.join(" | ")}`);
  if (errors.length) fail(vpName, route, `erro no console: ${errors[0]}`);
  page.off("console", onErr);
  page.off("pageerror", onPageErr);
  if (SHOTS) {
    const dir = path.join("test-results", "responsive", vpName);
    fs.mkdirSync(dir, { recursive: true });
    await page.screenshot({ path: path.join(dir, `${route.replace(/[^\w]+/g, "_") || "home"}.png`), fullPage: true }).catch(() => {});
  }
}

/** diálogo ou balão aberto tem que caber na tela (ou rolar, se for mais alto que ela) */
async function insideViewport(page, selector) {
  return page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (!el) return { found: false };
    const r = el.getBoundingClientRect();
    const vw = document.documentElement.clientWidth;
    const vh = window.innerHeight;
    const scrollable = ["auto", "scroll"].includes(getComputedStyle(el).overflowY) || ["auto", "scroll"].includes(getComputedStyle(el.parentElement).overflowY);
    return { found: true, ok: r.left >= -0.5 && r.right <= vw + 0.5 && (scrollable || (r.top >= -0.5 && r.bottom <= vh + 0.5)), rect: [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)], vw, vh };
  }, selector);
}

async function interactions(page, vpName, vp) {
  // 1. celular e tablet em pé: a barra inferior leva ao painel "Mais" com perfil e sair
  if (vp.width < 1024) {
    await page.goto(`${BASE}/`, { waitUntil: "load", timeout: 90_000 }).catch(() => {});
    const more = page.getByRole("button", { name: "Mais", exact: true });
    if (!(await more.count())) fail(vpName, "/", 'faltou o botão "Mais" da barra inferior');
    else {
      await more.click();
      const dlg = page.getByRole("dialog", { name: "Mais opções" });
      if (!(await dlg.isVisible())) fail(vpName, "/", 'o painel "Mais" não abriu');
      else {
        if (!(await dlg.getByRole("link", { name: /perfil|@/i }).count())) fail(vpName, "/", 'painel "Mais" sem o link do perfil');
        if (!(await dlg.getByRole("button", { name: "Sair" }).count())) fail(vpName, "/", 'painel "Mais" sem o botão Sair');
        const box = await dlg.boundingBox();
        if (!box || box.x < -0.5 || box.x + box.width > vp.width + 0.5) fail(vpName, "/", 'painel "Mais" fora da tela');
        await page.keyboard.press("Escape");
        if (await dlg.isVisible()) fail(vpName, "/", 'Esc não fechou o painel "Mais"');
      }
    }
    // rótulos da barra inferior não se sobrepõem
    const nav = await page.evaluate(() => {
      const links = [...document.querySelectorAll('nav[aria-label="Principal"].fixed a, nav[aria-label="Principal"].fixed button')];
      return links.map((a) => ({ t: a.textContent.trim(), over: a.scrollWidth > a.clientWidth + 1, h: Math.round(a.getBoundingClientRect().height) }));
    });
    for (const n of nav) {
      if (n.over) fail(vpName, "/", `rótulo da barra inferior vaza: ${n.t}`);
      if (n.h && n.h < 44) fail(vpName, "/", `alvo de toque da barra inferior com ${n.h}px: ${n.t}`);
    }
  }
  // 2. concluir atividade (diálogo) e lançar tempo (balão) a partir de um cartão
  await page.goto(`${BASE}/semana/1`, { waitUntil: "load", timeout: 90_000 }).catch(() => {});
  await page.waitForTimeout(700);
  const complete = page.locator('button[aria-label="Concluir atividade"]:visible').first();
  if (await complete.count()) {
    await complete.scrollIntoViewIfNeeded();
    await complete.click();
    const r = await insideViewport(page, '[role="dialog"][aria-labelledby="complete-modal-title"]');
    if (!r.found) fail(vpName, "/semana/1", 'o diálogo "Concluir atividade" não abriu');
    else if (!r.ok) fail(vpName, "/semana/1", `diálogo "Concluir atividade" fora da tela: ${JSON.stringify(r.rect)} em ${r.vw}x${r.vh}`);
    await page.keyboard.press("Escape");
    if (await page.locator('[aria-labelledby="complete-modal-title"]').count()) fail(vpName, "/semana/1", 'Esc não fechou o diálogo "Concluir atividade"');
  } else warn(vpName, "/semana/1", "sem atividade pendente para testar o diálogo de conclusão");
  const quick = page.locator('button[aria-label="Lançar tempo estudado"]:visible').first();
  if (await quick.count()) {
    await quick.scrollIntoViewIfNeeded();
    await quick.click();
    await page.waitForTimeout(250);
    const r = await insideViewport(page, '[role="dialog"][aria-label="Lançar tempo gasto"]');
    if (!r.found) fail(vpName, "/semana/1", 'o balão "Tempo" não abriu');
    else if (!r.ok) fail(vpName, "/semana/1", `balão "Tempo" fora da tela ou cortado: ${JSON.stringify(r.rect)} em ${r.vw}x${r.vh}`);
    await page.keyboard.press("Escape");
  }
}

const browser = await chromium
  .launch({ channel: "chrome", headless: true })
  .catch(() => chromium.launch({ channel: "msedge", headless: true }));
const t0 = Date.now();
let routes = [];
let checks = 0;
const only_routes = arg("routes")?.split(",");

// páginas públicas, sem sessão
for (const [w, h, name] of viewports) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, hasTouch: w < 1024, isMobile: w < 768 });
  const page = await ctx.newPage();
  for (const r of ANON_ROUTES) {
    if (only_routes && !only_routes.includes(r)) continue;
    await checkPage(page, name, r, { width: w, height: h });
    checks++;
  }
  await ctx.close();
}

// páginas do app, com sessão
for (const [w, h, name] of viewports) {
  const ctx = await browser.newContext({ viewport: { width: w, height: h }, hasTouch: w < 1024, isMobile: w < 768 });
  const page = await ctx.newPage();
  await login(page);
  if (!routes.length) routes = [...STATIC_ROUTES, ...(await discoverRoutes(page))];
  for (const r of routes) {
    if (only_routes && !only_routes.includes(r)) continue;
    await checkPage(page, name, r, { width: w, height: h });
    checks++;
  }
  if (!only_routes) await interactions(page, name, { width: w, height: h });
  await ctx.close();
}
await browser.close();

console.log(`\n${checks} páginas × viewports verificadas em ${Math.round((Date.now() - t0) / 1000)} s (${viewports.length} viewports, ${routes.length} rotas com sessão + ${ANON_ROUTES.length} públicas).`);
if (warnings.length) console.log(`\nAvisos (${warnings.length}):\n${warnings.map((w) => `  · ${w}`).join("\n")}`);
if (failures.length) {
  console.log(`\nFALHAS (${failures.length}):\n${failures.map((f) => `  ✗ ${f}`).join("\n")}`);
  process.exit(1);
}
console.log("\nOK: nenhuma falha de responsividade.");
