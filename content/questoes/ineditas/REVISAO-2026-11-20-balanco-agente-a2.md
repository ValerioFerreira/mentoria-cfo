# Balanço de Questões Inéditas — Direito Processual Penal Militar (Parte 2 / `agente-a2`)

- **Data:** 2026-11-20
- **Matéria:** `direito-processual-penal-militar`
- **Escopo (Parte 2):** `a08/s02`, `a08/s03`, `a08/s04`, `a10/s01`, `a10/s02`, `a12/s01` e `c01/s01`
- **Arquivo oficial:** `content/questoes/ineditas/mc/direito-processual-penal-militar.txt`

## Resumo por Trecho (Parte 2)

| Trecho | Assunto Principal | Adicionadas na retomada (`agente-a2-cont`) | Total Final no Trecho |
| :--- | :--- | ---: | ---: |
| `a08/s02` | Prisão preventiva e medidas cautelares no CPPM | (já concluído) | 37 |
| `a08/s03` | Prisão em flagrante no CPPM | (já concluído) | 42 |
| `a08/s04` | Busca e apreensão e restituição de coisas | (já concluído) | 42 |
| `a10/s01` | Qualificação, interrogatório, confissão, ofendido e perícias (arts. 294–346) | +28 | 41 |
| `a10/s02` | Testemunhas, acareação, reconhecimento, documentos e indícios (arts. 347–383) | +30 | 42 |
| `a12/s01` | Instrução provisória e processos especiais de deserção (arts. 451–457, Lei 8.236/1991) | +16 | 41 |
| `c01/s01` | Prerrogativas de posto/função, comparecimento espontâneo, menagem e liberdade provisória (arts. 234, 242, 253, 262–271) | +16 | 41 |
| **Subtotal retomada** | **4 trechos pendentes concluídos** | **+90** | — |

## Validação Final

- **Ferramenta de gravação:** `pipeline/pcpe_tools/ineditas_append.py` (com `--dry` prévio aprovado em todos os 4 rascunhos).
- **Checagem final:** `pipeline/questoes/ineditas_mc_nativas.py --check content/questoes/ineditas/mc/direito-processual-penal-militar.txt`
  - **Resultado:** `TOTAL 610 · erros 0`
  - **Distribuição de gabaritos:** `A 122 · B 122 · C 122 · D 122 · E 122` (equilíbrio exato de 20% por alternativa).
- **Qualidade pedagógica:** Cobertura integral da legislação seca do CPPM (incluindo redação vigente da Lei nº 8.236/1991 na deserção e diálogo constitucional sobre direito ao silêncio, momento do interrogatório no HC 127.900/STF e presunção de inocência na liberdade provisória), casos concretos contextualizados ao Corpo de Bombeiros Militar, proporção de questões com comando `INCORRETA` acima de 20%, ausência de citações de letras nos comentários e ausência de duplicidade com os itens pré-existentes.
