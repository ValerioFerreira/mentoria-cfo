# Relatório de Auditoria Estrutural — Legislação Estadual (PCPE)

**Data**: 16/10/2026  
**Auditor**: Agente MentorIA  
**Aulas auditadas**: `legislacao-pcpe/a01` a `a07` + complemento `legislacao-pcpe/c01`  
**Total de páginas auditadas**: 284 págs. (material-base) + 3 págs. (complemento)  
**Total de trechos de teoria gerados**: 12 trechos (11 base + 1 complemento)  

---

## 1. Visão Geral e Estrutura das Aulas

A disciplina cobre a legislação institucional e estatutária exigida no edital da Polícia Civil de Pernambuco (Portaria Conjunta SAD/SDS nº 306/2026), composta por cinco blocos normativos principais:
1. **Constituição do Estado de Pernambuco** (artigos 101 a 105-B) — suprida pelo complemento autoral `c01`.
2. **Lei nº 6.425/1972** (Estatuto do Policial Civil de Pernambuco) — Aulas `a03` e `a04` (Prof. Giulian Salvador).
3. **Lei nº 6.123/1968** (Estatuto dos Servidores Públicos do Estado de Pernambuco) — Aulas `a05`, `a06` e `a07` (Prof. Felipe Leal).
4. **Lei Complementar nº 137/2008** (Cargos e Remuneração da PCPE) — Aula `a01`.
5. **Lei Complementar nº 317/2015** (Estrutura Remuneratória e Progressão) — Aula `a02`.

---

## 2. Diagnóstico e Correções Estruturais (`content/overrides/legislacao-pcpe.json`)

### Aulas `a03`, `a04` e `a05` (In-line questions e correção de falso gabarito)
- **Problema encontrado**: Os professores utilizam questões de fixação intercaladas no corpo da teoria. Quando apareceu a linha `Gabarito: B.` ou `Gabarito: C.` no meio do texto (ex.: pág. 10 na `a03`, pág. 12 na `a04` e pág. 16 na `a05`), o classificador heurístico identificou a aula inteira subsequente como seção de gabarito (`K`), cortando a teoria precocemente e perdendo de 10 a 15 páginas essenciais em cada aula.
- **Solução adotada**:
  - `a03`: classificada com teoria de 2 a 20 (19 págs.), cortada pedagogicamente na pág. 10 (*Da Nomeação, Posse e Exercício*), gerando os segmentos `s01` (8 págs.) e `s02` (11 págs.). Páginas 21-37 comentadas (`C`), 38-46 lista (`L`), 47 gabarito (`K`), 48-75 resumo (`S`).
  - `a04`: classificada com teoria de 2 a 26 (25 págs.), cortada pedagogicamente na pág. 13 (*Das Penas Disciplinares e Processo*), gerando os segmentos `s01` (11 págs.) e `s02` (14 págs.). Páginas 27-44 comentadas (`C`), 45-53 lista (`L`), 54 gabarito (`K`), 55-63 resumo (`S`).
  - `a05`: classificada com teoria de 3 a 21 (19 págs.), cortada pedagogicamente na pág. 12 (*Remoção, Redistribuição e Vacância*), gerando os segmentos `s01` (9 págs.) e `s02` (10 págs.). Páginas 22-36 comentadas (`C`), 37-42 lista (`L`), 43-44 gabarito (`K`).

### Aula `a07`
- **Divisão pedagógica**: Teoria de 3 a 19 (17 págs.), dividida em pág. 11 (*Penalidades Disciplinares e Processo*) para separar o bloco de deveres/proibições/responsabilidades (`s01`, 8 págs.) do bloco sancionatório e processual (`s02`, 9 págs.).

---

## 3. Cobertura do Edital

| Item do Edital | Dispositivo Legal | Onde é estudado | Status |
|---|---|---|---|
| **1. Constituição Estadual** | Arts. 101 a 105-B da CE-PE | `legislacao-pcpe/c01` (págs. 1–3) | Coberto por Complemento |
| **2. Estatuto Policial Civil** | Lei nº 6.425/1972 | `legislacao-pcpe/a03` (págs. 2–20) e `a04` (págs. 2–26) | Coberto |
| **3. Estatuto Servidor PE** | Lei nº 6.123/1968 | `legislacao-pcpe/a05` (3–21), `a06` (3–15), `a07` (3–19) | Coberto |
| **4. LC 137/2008** | LC Estadual nº 137/2008 | `legislacao-pcpe/a01` (págs. 2–14) | Coberto |
| **5. LC 317/2015** | LC Estadual nº 317/2015 | `legislacao-pcpe/a02` (págs. 2–4) | Coberto |

**Resultado**: 100% dos itens do edital cobertos (4 cobertos diretamente pelo material-base e 1 suprido por complemento autoral atualizado com as ECs 70/2026 e 71/2026). Zero pendências de conteúdo.
