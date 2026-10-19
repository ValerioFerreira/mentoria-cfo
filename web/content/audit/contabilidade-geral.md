# Relatório de Auditoria Estrutural — Contabilidade Geral (PCPE)

**Data**: 16/10/2026  
**Auditor**: Agente MentorIA  
**Aulas auditadas**: `contabilidade-geral/a00` a `a19` (pasta `docs/43`, Profs. Luciano Rosa e Júlio Cardozo)  
**Total de páginas auditadas**: 1.189 págs. (material-base)  
**Total de trechos de teoria gerados**: 44 segmentos (594 páginas úteis de teoria, média de 13,5 págs/seg, 0 violações de teto, 0 cortes no meio de tópico)  

---

## 1. Visão Geral e Estrutura das Aulas

A disciplina atende com rigor e profundidade a todos os tópicos de **Contabilidade Geral** exigidos para o cargo de **Agente de Polícia Civil de Pernambuco** (Portaria Conjunta SAD/SDS nº 306/2026, banca Cebraspe, itens 1 a 11):
1. **Aula `a00`**: Conceitos, objetivos, finalidades e funções da contabilidade; usuários e elementos básicos.
2. **Aula `a01`**: Patrimônio, componentes patrimoniais, situações líquidas e atos/fatos administrativos (permutativos, modificativos e mistos).
3. **Aula `a02`**: Teoria das contas, débitos, créditos, saldos, contas patrimoniais e de resultado.
4. **Aula `a03`**: Plano de contas, partidas dobradas, fórmulas de lançamento e retificação de lançamentos contábeis.
5. **Aula `a04`**: Livros de escrituração contábil (Diário, Razão, Caixa) e Balancete de Verificação.
6. **Aula `a05`**: Regime de competência e regime de caixa; operações contábeis básicas e apuração do resultado.
7. **Aula `a06`**: Balanço Patrimonial: conceito, objetivo, estrutura segundo a Lei 6.404/1976 e CPC 26; Ativo Circulante e Não Circulante.
8. **Aula `a07`**: Avaliação de estoques (PEPS, custo médio) e contabilização de operações com mercadorias e tributos.
9. **Aula `a08`**: CPC 27 — Ativo Imobilizado: custo inicial, depreciação, amortização e baixa de bens.
10. **Aula `a09`**: CPC 01 (R1) — Redução ao Valor Recuperável de Ativos (*Impairment Test*).
11. **Aula `a10`**: CPC 04 (R1) — Ativo Intangível: reconhecimento, pesquisa/desenvolvimento e amortização.
12. **Aula `a11`**: Passivo Exigível (Circulante e Não Circulante), Ajuste a Valor Presente e folha de pagamento/encargos sociais.
13. **Aula `a12`**: CPC 25 — Provisões, Passivos Contingentes e Ativos Contingentes.
14. **Aula `a13`**: Operações financeiras diversas: juros, descontos, duplicatas descontadas, variação cambial e debêntures.
15. **Aula `a14`**: Patrimônio Líquido: Capital Social, Reservas de Capital e Ajuste de Avaliação Patrimonial.
16. **Aula `a15`**: Reservas de Lucros, destinação do resultado, dividendos obrigatórios e prejuízos acumulados.
17. **Aula `a16`**: Demonstração do Resultado do Exercício (DRE): estrutura, receita bruta, deduções e lucro líquido.
18. **Aula `a17`**: Princípios Fundamentais de Contabilidade.
19. **Aula `a18`**: CPC 00 (R2) — Estrutura Conceitual para Relatório Financeiro: características qualitativas e mensuração.
20. **Aula `a19`**: CPC 26 (R1) — Apresentação das Demonstrações Contábeis e notas explicativas.

---

## 2. Diagnóstico e Correções Estruturais (`content/overrides/contabilidade-geral.json`)

### Mapeamento das Aulas e Delimitação Teoria × Prática
- Todos os 20 PDFs foram mapeados isolando com exatidão a teoria pura dos blocos de questões comentadas, listas de exercícios de fixação e gabaritos finais.
- Com esse isolamento, nenhuma página de questões sem comentário ou de resposta é incluída na carga de estudo teórico.

### Particionamento Pedagógico das Aulas Densas
- Foram inseridos cortes pedagógicos respeitando os tópicos conceituais nas aulas com mais de 17 páginas:
  - `a00` (corte p. 19), `a01` (corte p. 16), `a02` (corte p. 16), `a03` (cortes p. 19 e 31).
  - `a05` (cortes p. 14, 30 e 45), dividindo a aula de 59 páginas em 4 trechos equilibrados.
  - `a06` (cortes p. 15 e 30), `a07` (corte p. 12), `a08` (cortes p. 19 e 36).
  - `a10` (corte p. 12), `a11` (corte p. 17), `a13` (corte p. 19), `a14` (corte p. 14), `a15` (cortes p. 16 e 28).
  - `a17` (corte p. 12), `a18` (corte p. 12) e `a19` (cortes p. 18, 33 e 46).
- **Resultado da segmentação**: 0 trechos violando o teto de 17 páginas e 0 cortes no meio de tópico.

---

## 3. Cobertura do Edital

| Item do Edital | Descrição | Onde é estudado | Status |
|---|---|---|---|
| **1** | Conceitos, objetivos e finalidades | `contabilidade-geral/a00` | Coberto (100%) |
| **2** | Patrimônio e situação líquida | `contabilidade-geral/a01` (s01) | Coberto (100%) |
| **3** | Atos e fatos administrativos | `contabilidade-geral/a01` (s02) | Coberto (100%) |
| **4** | Contas, débitos, créditos e saldos | `contabilidade-geral/a02` | Coberto (100%) |
| **5** | Plano de contas | `contabilidade-geral/a03` (s01) | Coberto (100%) |
| **6** | Escrituração, livros, métodos e regimes | `contabilidade-geral/a03` (s02, s03), `a04`, `a05` (s01) | Coberto (100%) |
| **7** | Contabilização de operações diversas | `contabilidade-geral/a05`, `a07`, `a11` (s02), `a13` | Coberto (100%) |
| **8** | Balancete de verificação | `contabilidade-geral/a04` | Coberto (100%) |
| **9** | Balanço patrimonial | `contabilidade-geral/a06`, `a11` (s01), `a14`, `a15` | Coberto (100%) |
| **10** | Demonstração do resultado do exercício (DRE) | `contabilidade-geral/a16` | Coberto (100%) |
| **11** | Normas Brasileiras de Contabilidade e CPCs | `contabilidade-geral/a08`, `a09`, `a10`, `a12`, `a17`, `a18`, `a19` | Coberto (100%) |

**Resultado**: 100% dos itens de Contabilidade Geral do edital PCPE plenamente cobertos.
