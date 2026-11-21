# Revisão de Balanço — Lote C (`legislacoes-pe` e `legislacao-pcpe`)

- **Data:** 2026-11-20
- **Agentes:** `agente-c` (etapa inicial: `a01/s01`, `a01/s02`, `a02/s01`, `a02/s02` de `legislacoes-pe`) e `agente-c-cont` (retomada: 56 questões de `legislacoes-pe` + 49 questões de `legislacao-pcpe` = **105 questões** adicionadas)
- **Validação estrutural:** `ineditas_mc_nativas.py --check` → **0 erros** (`legislacoes-pe`: 532 questões, distribuição A 106 / B 106 / C 106 / D 107 / E 107; `legislacao-pcpe`: 151 questões, distribuição A 30 / B 30 / C 30 / D 31 / E 30)
- **Balanço final (`lacunas_balanco.py --lista`):**
  - `legislacoes-pe`: **0 questões pendentes**
  - `legislacao-pcpe`: **0 questões pendentes**

## 1. Resumo por trecho — `legislacoes-pe` (retomada: +56 questões)

Os trechos `a01/s01`, `a01/s02`, `a02/s01` e `a02/s02` já se encontravam concluídos antes da retomada. Na etapa `agente-c-cont`, foram adicionadas:

| Trecho | Norma / Assunto | Qtd. adicionada | Rascunho |
| --- | --- | ---: | --- |
| `c06/s01` | Decreto Estadual nº 22.114/2000 (`ped22114`, arts. 1º a 19 — Código de Ética dos Militares de PE) | 10 | `legpe_c06_s01.txt` |
| `c07/s01` | LC Estadual nº 470/2021 (`pelc470`, arts. 1º a 82 — Lei de Promoção dos Militares de PE) | 10 | `legpe_c07_s01.txt` |
| `c08/s01` | Lei Federal nº 12.527/2011 (`l12527`, arts. 1º a 34 — Lei de Acesso à Informação) | 10 | `legpe_c08_s01.txt` |
| `c09/s01` | Lei Estadual nº 13.314/2007 e alterações (`pe13314`, arts. 1º a 6º-C — Assédio Moral e Sexual em PE) | 10 | `legpe_c09_s01.txt` |
| `c10/s01` | Portaria nº 395/2015 da Corregedoria Geral da SDS (arts. 1º a 33 — Sindicância ADM) | 8 | `legpe_c10_s01.txt` |
| `c11/s01` | Provimento Correicional nº 21/2021 da Corregedoria Geral da SDS (arts. 1º a 18 — Investigação Preliminar) | 8 | `legpe_c11_s01.txt` |
| **Subtotal** | | **56** | |

## 2. Resumo por trecho — `legislacao-pcpe` (+49 questões)

| Trecho | Norma / Assunto | Qtd. adicionada | Rascunho |
| --- | --- | ---: | --- |
| `a03/s01` | Lei Estadual nº 6.425/1972 (`pe6425` — Disposições Preliminares e LC nº 490/2022) | 2 | `pcpe_pe6425_bloco7.txt` |
| `a03/s02` | Lei Estadual nº 6.425/1972 (`pe6425` — Regime Jurídico, Gratificação de Função Policial e Cursos) | 2 | `pcpe_pe6425_bloco7.txt` |
| `a04/s01` | Lei Estadual nº 6.425/1972 (`pe6425` — Deveres, Detenção Disciplinar, Interrupção/Suspensão e Recusa) | 3 | `pcpe_pe6425_bloco7.txt` |
| `a04/s02` | Lei Estadual nº 6.425/1972 (`pe6425` — Suspensão Preventiva, Processo/Sindicância, CPD e Comissão Especial) | 3 | `pcpe_pe6425_bloco7.txt` |
| `a05/s01` | Lei Estadual nº 6.123/1968 (`pe6123` — Disposições Preliminares, Cargo Técnico/Científico, Posse e Exercício) | 3 | `pcpe_pe6123_a05.txt` |
| `a05/s02` | Lei Estadual nº 6.123/1968 (`pe6123` — Remoção, Estágio Probatório, Promoção, Reintegração, Aproveitamento, Reversão, Recondução/Readaptação e Vacância) | 8 | `pcpe_pe6123_a05.txt` |
| `a06/s01` | Lei Estadual nº 6.123/1968 (`pe6123` — Tempo de Serviço, Férias, Licenças, Vencimento, Concessões, Horário Especial PCD e Direito de Petição) | 10 | `pcpe_pe6123_a06.txt` |
| `a07/s01` | Lei Estadual nº 6.123/1968 (`pe6123` — Acumulação, Deveres, Proibições, Responsabilidade, Penalidades, Demissão "a bem do serviço público" e Cassação) | 9 | `pcpe_pe6123_a07_s01.txt` |
| `a07/s02` | Lei Estadual nº 6.123/1968 (`pe6123` — Competência, Prescrição, Suspensão/Prisão Preventiva, Sindicância, Inquérito, Recesso/Dias Úteis da LC nº 515/2022 e Revisão) | 9 | `pcpe_pe6123_a07_s02.txt` |
| **Subtotal** | | **49** | |

## 3. Verificações normativas de destaque

- Todas as normas disponíveis em `pipeline/leis.py` (`ped22114`, `pelc470`, `l12527`, `pe13314`, `pe6425` e `pe6123`) foram conferidas diretamente na redação vigente, contemplando alterações recentes:
  - **LC nº 490/2022** (limite de 2 vínculos na acumulação na Lei nº 6.425/1972, art. 4º).
  - **Leis nº 17.065/2020, nº 17.971/2022 e nº 18.379/2023** (assédio moral e sexual na Lei nº 13.314/2007).
  - **LCs nº 316/2015, nº 371/2017, nº 387/2018, nº 402/2019, nº 509/2022 e nº 515/2022** na Lei nº 6.123/1968 (conversão de exoneração em demissão, horário especial PCD, recondução por inconstitucionalidade de enquadramento, prazos em dias úteis e suspensão de prazos/audiências entre 20/12 e 20/01).
- Para `c10/s01` (Portaria nº 395/2015) e `c11/s01` (Provimento Correicional nº 21/2021), utilizou-se o material aprovado em `content/material/legislacoes-pe/m04/`.
- Todos os blocos foram testados com `ineditas_append.py --dry`, gravados exclusivamente via `ineditas_append.py` (sem edição manual de `content/questoes/ineditas/mc/*.txt`) e validados com `ineditas_mc_nativas.py --check` com **0 erros**.
