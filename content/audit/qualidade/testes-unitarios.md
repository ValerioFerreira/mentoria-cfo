# Testes unitários do MentorIA — relatório (parcial, encerrado em 2026-10-10)

O agente de testes foi interrompido pelo limite semanal de uso da API (libera em 11/10, 16h, horário de Brasília). Este relatório foi fechado pelo orquestrador com o que ficou no disco e foi reexecutado.

## 1. Números

| Métrica | Antes | Depois |
|---|---|---|
| Web: arquivos de teste (Vitest) | 11 | **27** |
| Web: nº de testes | 115 | **338** (337 passam + 1 `expected fail` documentado) |
| Web: tempo de `npm test` | ~2,5 s | ~4 s |
| Pipeline: pytest | 45 (44 passam, 1 falha) | 45 (44 passam, 1 falha — ver §3) |
| Typecheck | ok | ok |
| Lint | — | só erros em `web/scripts/_sample-audit.ts` (corrigido com eslint-disable); demais são avisos antigos |
| Cobertura medida | n/d | n/d (`@vitest/coverage-*` não instalado; não instalamos pacotes novos) |

## 2. Arquivos de teste novos (todos em `web/src/lib`)
`activity-detail`, `auth/password`, `auth/rate-limit`, `contests`, `flame-frames`, `plans`, `ui-format`, `quiz/servable`, `planner/{blueprint, coverage, dates, days, invariants, review, schedule, select}` e o utilitário `planner/testkit.ts`. Ficaram de fora (precisam de banco/Next/UI): server actions, `lib/data/*`, componentes React, middleware `proxy.ts`. **Pipeline Python: nenhum teste novo foi escrito** (o agente caiu antes) — é a principal lacuna.

## 3. Bugs e riscos encontrados
1. **`verifyPassword` lançava exceção com registro truncado/corrompido** (`scrypt$16384$8$1`) em vez de falhar fechado. **Corrigido** em `web/src/lib/auth/password.ts` (retorna `false` se faltam salt/hash ou se o scrypt rejeita os parâmetros). O teste `password.test.ts` passou a ser verde.
2. `isPlan` aceitava chaves herdadas (`"constructor"`, `"toString"`): **corrigido** em `web/src/lib/plans.ts` (`Object.hasOwn`).
3. `pipeline/tests/test_content.py::test_authored_items_pass_validator` **falha** porque `content/items/direito-constitucional/a09.json` (commit antigo, sem alteração dos agentes) tem trechos com 10+ palavras iguais ao material (q1 alt. E; q3, q5, q6, q9 explicações; trecho s02 q3; s03 q1 e q2). Precisa ser reparafraseado — está na fila do HANDOFF.
4. 1 `expected fail` no Vitest documenta comportamento conhecido (ver comentário no próprio teste).

## 4. Como rodar
```bash
cd web && npm test && npm run typecheck && npm run lint
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python -m pytest pipeline/tests -q   # ~2 min (inclui o validador)
```

## 5. Lacunas / recomendações
- Escrever os testes do pipeline: `validate_content.py` (esquema, gabarito, originalidade de 10 palavras, equilíbrio de tamanho), `check_ranges.py` (com fixtures sintéticas), funções puras de `segment`/`build_catalog`/`build_complements`, e invariantes de dados (5 alternativas, `answer` ∈ A–E, ids de trecho no catálogo, `pageRef` dentro do trecho, pesos ≤ 1).
- Testes das server actions com `vi.mock` do Prisma (onboarding, listas de espera, perfil).
- Instalar `@vitest/coverage-v8` se o dono do produto aprovar, para medir cobertura.
