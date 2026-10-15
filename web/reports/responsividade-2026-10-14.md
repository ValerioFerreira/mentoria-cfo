# Auditoria de responsividade — 2026-10-14 (branch `responsive`)

Método: inventário das rotas (`src/app`, 38 páginas + 2 rotas de API), varredura automática por iframe em larguras controladas
(320, 360, 390, 768, 1024, 1280), inspeção visual no navegador do app (360 px) e, depois, teste em navegador real
(`npm run test:responsive`, `scripts/responsive-audit.mjs`, Chrome do sistema via `playwright-core`).
Banco de desenvolvimento local, conta de teste. Nada foi feito em produção.

## Cobertura

| Situação | Itens |
|---|---|
| **Testado em navegador real** (11 viewports: 320, 360, 375, 390, 430, 667×375 paisagem, 768, 1024×768, 1280, 1440, 1920) | `/`, `/semana/1`, `/plano`, `/questoes`, `/simulados`, `/resumos`, `/resumos/biologia`, `/desempenho`, `/pagamentos`, `/perfil`, `/onboarding` (1º passo), `/admin`, `/admin/cadastros`, `/admin/financeiro`, `/admin/parceiros`, `/admin/revisao`, `/como-funciona`, uma `/atividade/[id]`; públicas: `/login`, `/cadastro`, `/recuperar-senha`, `/concursos`, `/lista-de-espera/cbmpe-oficial`, `/como-funciona` |
| **Interações testadas** (por viewport) | painel "Mais" (celular/tablet em pé: perfil, sair, Esc), diálogo "Concluir atividade", balão "Tempo" |
| **Inspecionado visualmente** (360 px, manual) | login, cadastro, concursos, lista de espera, runner de questões, modal "Montar caderno", painel "Mais" |
| **Verificação manual pendente** | `/simulados/[id]` e `/simulados/resultado/[id]` (funcionalidade "em breve", sem dados), `/pagamentos/contratacao/[id]`, `/pagamentos/pix/[id]`, `/admin/financeiro/[id]`, `/admin/parceiros/[id]`, `/parceria`, `/trocar-senha`, passos 2+ do assistente `/onboarding`, `/caderno/[id]` em andamento com figuras, temas Sépia/Dark, teclado virtual e zoom 200% em aparelho real |

## Problemas encontrados

**P0 (corrigidos)**
1. Abaixo de 1024 px não havia como abrir **Perfil** nem **Sair** (só existiam no menu lateral). → painel "Mais" na barra inferior (`app-nav.tsx`).
2. O diálogo **"Concluir atividade"**, aberto de um cartão, ficava preso e cortado dentro dele (cartão com `overflow-hidden` e transformação) — ação central da Missão de hoje/Meta semanal. → portal para `document.body`.
3. O modal **"Montar caderno personalizado"** abria com o fundo deslocado (3.652 px de altura, fora da tela) pelo mesmo motivo. → portal.

**P1 (corrigidos)**
4. Barra inferior com 8 rótulos sobrepostos/cortados em 320–430 px → 4 itens + "Mais", rótulos curtos, alvo ≥ 56 px.
5. Balão "Tempo" dos cartões cortado pelo cartão → portal com posição acompanhando o botão.
6. Revisão de caderno (prática) e resultado do simulado mostravam enunciado/alternativas/explicação como texto cru (`![Figura](/q-img/…)`, `<sub>`) e estouravam 257–297 px → `RichContent`.
7. Itens Certo/Errado dos Bizus (até 20 marcas de 24 px) estouravam 298–360 px.
8. Desempenho em 360 px: seções "Assuntos para reforçar"/"Últimos cadernos" 83 px além da tela (grade sem `grid-cols-1`).
9. Meta semanal em 1024–1279 px: 7 colunas de ~58 px; Plano e Desempenho em 1024: cartões espremidos com texto vazando. → 7 colunas e grades lado a lado só a partir de `xl` (1280).
10. Barra do simulado em andamento ficava sob o cabeçalho fixo no celular (cronômetro escondido).
11. Lightbox de imagens também preso ao cartão → portal, Esc, botão de 44 px.

**P2 (corrigidos)**: `min-w` fixos que estouravam em 320 px (filtros do Financeiro, assistente, caderno, perfil); login/recuperar senha 3–19 px além da tela em 320 px; CTA de "Como funciona" em 320 px e paisagem; botão de rótulo longo no Perfil; legenda do Plano; modais sem rolagem em celular deitado (classe `.modal-scroll`); alvos de toque (balão "?" ampliado em telas de toque, "Aparência", fechar do modal); fórmulas inline sem `max-width`; imagens ampliáveis sem teclado/indício em toque; Esc nos diálogos.

## Pendências (não corrigidas)
- Gráficos de barras do Desempenho: valores só em `title` (hover); em toque não há leitura por barra (P2, exige novo padrão).
- Muitos controles densos ainda têm 28–34 px de altura em telas de toque (filtros do banco de questões, botões `sm`, "Limpar"): maiores que 24 px (WCAG 2.2 AA), abaixo de 44 px (P3).
- Rótulos de 10–11 px em selos e eyebrows (P3).
- Dropdown de bancas em `/questoes` não foi exercitado em toque (P2, verificar).
- Contraste dos temas Sépia/Dark não reauditado.

## Testes
- `npm run test:responsive` (novo; exige servidor local e conta de teste): 275 verificações (11 viewports × 25 rotas) + interações → **OK**.
- `vitest --project unit`: 43 arquivos, 457 testes → OK. `tsc --noEmit` → OK. `eslint` nos arquivos alterados: 0 erros (avisos antigos de imports não usados).
- Build de produção (`npm run build` com `VERCEL=1 VERCEL_ENV=preview`, que não toca no banco) → OK.

## Observações do ambiente
- O Postgres de dev (PGlite) cai com várias consultas em paralelo (ex.: `/desempenho`); a auditoria usou um pré-carregamento fora do repositório que limita o pool a 1 conexão. Nenhum código do projeto foi alterado por isso.
- Dependência nova: `playwright-core@1.63.0` (devDependency, sem download de navegador).
