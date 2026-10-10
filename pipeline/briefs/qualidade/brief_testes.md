# Testes unitários do MentorIA (CFO-BM) — cobrir todo o código testável

Projeto: C:\Users\Administrador\Documents\Projetos\CFO-BM. Leia CLAUDE.md inteiro e `web/AGENTS.md`. Outros agentes editam `content/items` em paralelo: NÃO toque em `content/` (exceto o seu documento) e não use git (sem commit/stash/checkout/restore).

## Objetivo
Criar todos os testes unitários possíveis e úteis para o sistema, em duas frentes:
1. **Web** (`web/`, Vitest — `npm test` em `web/`): há testes em `web/src/lib/*.test.ts`, `planner/*.test.ts`, `quiz/logic.test.ts`. Mapeie TODO o código em `web/src` (lib, planejador, quiz, auth/sessão, metrics, directive, anamnesis, summaries, plan-time, pix, plans, contests, profile, data, schedule/days/review/select/blueprint/coverage/diagnostic etc.) e cubra o que for lógica pura ou isolável: casos normais, limites, entradas inválidas, datas (fuso de Recife, `todayISO`), arredondamentos, invariantes dos planos (use o planner real com o catálogo de `content/`). Para funções que dependem de banco/Next (server actions, `lib/data/*`), teste a lógica extraível ou use mocks simples (`vi.mock`) — sem banco real, sem rede. Não escreva testes frágeis (dependentes de horário real, aleatoriedade sem semente ou de textos de UI voláteis).
2. **Pipeline Python** (`pipeline/tests`, `pipeline/.venv/Scripts/python -m pytest pipeline/tests -q`, com `PYTHONIOENCODING=utf-8`): hoje há test_complements/content/extract/segment. Cubra o que falta: `validate_content.py` (esquema, gabarito, originalidade de 10 palavras, equilíbrio de tamanho), `check_ranges.py`, `segment`/`headings`/`build_catalog`/`build_complements` (funções puras), invariantes dos dados (`content/items`: toda questão com 5 alternativas e `answer` ∈ A–E, ids de trecho existentes no catálogo, `pageRef` dentro do trecho, sem trecho órfão, pesos de incidência somam ≤ 1…) — estes de "contrato dos dados" valem ouro, mas cuidado: o conteúdo muda em paralelo, então prefira invariantes estruturais a valores fixos. Use fixtures sintéticas pequenas quando o cache de páginas (pipeline/.cache) puder faltar (teste deve pular com `skip` se o cache não existir).

## Regras
- Padrão do código existente (nomes em inglês no código, descrições dos testes em português como nos testes atuais; olhe um arquivo de teste existente antes).
- Se um teste revelar um BUG real no código de produção: documente (arquivo, linha, entrada, saída esperada × obtida). Corrija só se a correção for pequena e inequívoca, e registre no documento; caso contrário deixe o teste marcado (`it.fails`/`xfail` com comentário) e documente.
- No fim, rode: `npm test`, `npm run typecheck`, `npm run lint` (em `web/`) e o pytest completo; corrija o que quebrar por causa dos seus testes. Meça cobertura se houver provider disponível (`npx vitest run --coverage` só se `@vitest/coverage-*` já estiver instalado — não instale pacotes novos).
- Não rode `prisma migrate`/`db seed`, nem `segment.py`/`build_*`.

## Documentação (crie cedo e atualize a cada bloco de testes): `content\audit\qualidade\testes-unitarios.md`
Conteúdo: (1) resumo executivo com números antes × depois (arquivos de teste, nº de testes, tempo, cobertura se medida); (2) inventário por módulo: o que existe, o que foi adicionado, o que ficou de fora e POR QUÊ (precisa de banco, UI, etc.); (3) bugs e riscos encontrados (com evidência e status); (4) como rodar; (5) lacunas e recomendações.

## Retorno final (≤ 300 palavras, pt-BR)
Números, bugs encontrados, estado final de testes/lint/typecheck e o caminho do documento.
