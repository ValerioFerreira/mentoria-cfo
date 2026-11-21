# Balanço — Lote B / Parte 1 (`agente-b1` + `agente-b1-cont`)

- **Disciplina:** Atualidades (`atualidades`)
- **Escopo:** `a00/s04` a `a11/s04` (27 trechos, 163 questões totais na Parte 1; 78 questões gravadas nesta retomada de `a09/s01` a `a11/s04`)
- **Arquivo-alvo:** `content/questoes/ineditas/mc/atualidades.txt`
- **Validação final (`ineditas_mc_nativas.py --check`):** `atualidades: 335 questões · A 67 B 67 C 67 D 67 E 67` — **0 erros**.

## Quadro de Cobertura da Parte 1 (`a00/s04` a `a11/s04`)

| Aula / Trecho | Questões no arquivo | Etapa |
|---|---:|---|
| `a00/s04` | 6 | Concluído anteriormente |
| `a01/s01` | 6 | Concluído anteriormente |
| `a01/s02` | 4 | Concluído anteriormente |
| `a02/s01` | 5 | Concluído anteriormente |
| `a02/s02` | 4 | Concluído anteriormente |
| `a02/s03` | 3 | Concluído anteriormente |
| `a02/s04` | 2 | Concluído anteriormente |
| `a03/s03` | 6 | Concluído anteriormente |
| `a03/s04` | 2 | Concluído anteriormente |
| `a04/s01` | 5 | Concluído anteriormente |
| `a05/s02` | 2 | Concluído anteriormente |
| `a05/s03` | 1 | Concluído anteriormente |
| `a07/s01` | 8 | Concluído anteriormente |
| `a07/s02` | 8 | Concluído anteriormente |
| `a07/s03` | 8 | Concluído anteriormente |
| `a07/s04` | 8 | Concluído anteriormente |
| `a07/s05` | 7 | Concluído anteriormente |
| `a09/s01` | 8 | Corrigido e gravado (`a09_p1.txt`) |
| `a09/s02` | 8 | Corrigido e gravado (`a09_p1.txt`) |
| `a09/s03` | 8 | Redigido e gravado (`a09_p2.txt`) |
| `a09/s04` | 8 | Redigido e gravado (`a09_p2.txt`) |
| `a09/s05` | 7 | Redigido e gravado (`a09_p2.txt`) |
| `a09/s06` | 8 | Redigido e gravado (`a09_p2.txt`) |
| `a11/s01` | 8 | Redigido e gravado (`a11_p1.txt`) |
| `a11/s02` | 7 | Redigido e gravado (`a11_p1.txt`) |
| `a11/s03` | 8 | Redigido e gravado (`a11_p1.txt`) |
| `a11/s04` | 8 | Redigido e gravado (`a11_p1.txt`) |
| **Total Parte 1** | **163** | **100% concluído (78 novas nesta etapa)** |

## Resumo das Ações Executadas na Retomada (`agente-b1-cont`)

1. **`a09_p1.txt` (`a09/s01` e `a09/s02` — 16 questões):** Equilibrados os tamanhos das 9 alternativas corretas sinalizadas no `--dry`, ajustado o texto para manter foco estritamente em conteúdo estável, validado com `--dry` (0 problemas) e gravado via `ineditas_append.py`.
2. **`a09_p2.txt` (`a09/s03` a `a09/s06` — 31 questões):** Redigidas com conteúdo estável sobre Ciência e Tecnologia (IA, AI Act, Marco Civil, LGPD, hidrogênio verde, Programa Artemis/ISS, CRISPR-Cas9, ransomware), Sociedade/Cultura/Economia Brasileira (Censo 2022, Reforma Tributária EC 132/2023, Pix, patrimônio cultural/IPHAN/UNESCO, commodities e indústria, Banco Central/Selic, saneamento básico, povos indígenas), Política Brasileira (sistemas eleitorais, cláusula de desempenho e federações, Medidas Provisórias, federalismo, orçamento/emendas, Justiça Eleitoral/urna, STF) e Segurança Pública (art. 144 CF/88, SUSP, crime organizado, crimes cibernéticos, Lei Maria da Penha, Defesa Civil/PNPDEC, LEP, policiamento comunitário). Validado com `--dry` e gravado via `ineditas_append.py`.
3. **`a11_p1.txt` (`a11/s01` a `a11/s04` — 31 questões):** Redigidas com conteúdo estável sobre Copa do Mundo (histórico, organização conjunta EUA-México-Canadá, formato de 48 seleções, México como sede tripla, logística continental, economia de megaeventos, confederações da FIFA, Copa Feminina), Tecnologia e Geopolítica no Esporte (VAR, GLT e impedimento semiautomático, telemetria/ciência de dados, *sportswashing*, governança da FIFA/FIFAgate, boicotes históricos, COI/Carta Olímpica), Diplomacia Esportiva e Geografia/História de Países (Brasil nas Copas, diplomacia do pingue-pongue/*soft power*, Curaçao, Haiti, Marrocos, Irã, Copas no Brasil 1950/2014, elegibilidade e diásporas) e Fatos Internacionais/Conflitos (guerra na Ucrânia, OTAN, Conselho de Segurança da ONU, TPI, Acordo de Paris, BRICS, estreitos estratégicos e Direito Internacional dos Refugiados). Validado com `--dry` e gravado via `ineditas_append.py`.
4. **Validação integral:** `pipeline/questoes/ineditas_mc_nativas.py --check content/questoes/ineditas/mc/atualidades.txt` aprovado com **335 questões**, distribuição perfeitamente equilibrada (**A 67 / B 67 / C 67 / D 67 / E 67**) e **0 erros**.
