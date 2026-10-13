# Achados: questões no padrão AOCP (parcial, encerrado em 2026-10-10)

Os 2 agentes de análise (Q1: jurídicas + línguas; Q2: exatas, natureza e Informática) foram interrompidos pelo limite semanal de uso da API. Eles trabalhavam em rodadas de 25 questões sorteadas (semente base + nº da rodada), verificando gabarito (no PDF ou recalculando), padrão AOCP, distratores, explicação e fidelidade ao material, e corrigindo no ato. Registro completo em `_parcial-questoes-aocp-Q1.md` e `_parcial-questoes-aocp-Q2.md`.

## Cobertura realizada

| Agente | Rodadas | Questões auditadas | Pool da fatia |
|---|---|---|---|
| Q1 | 2 | 50 | 4.674 |
| Q2 | 6 | 150 | 5.658 |
| **Total** | 8 | **200** (≈ 1,9% das 10.332) | 10.332 |

## Métricas

| | Q1 (50) | Q2 (150) | Geral (200) |
|---|---|---|---|
| Sem achado | 34 (68%) | 123 (82%) | 157 (78,5%) |
| Com achado | 16 (32%) | 27 (18%) | 43 (21,5%) |
| CRÍTICO (gabarito errado / 2 corretas / falso) | 0 | 0 | **0** |
| MAIOR | 3 | 2 | 5 |
| MENOR | 13 | 25 | 38 |
| Gabarito errado | 0/50 | 0/150 | **0/200** |
| Correta é a alternativa mais longa | 22/50 (44%) | 40/150 (27%) | 62/200 (31%; esperado ≈ 20%) |
| Explicação problemática | 4 (8%) | 3 (2%) | 7 (3,5%) |

Taxa de achado por disciplina (amostra): biologia 50% (17/34), direito-administrativo 50% (4/8), direito-constitucional 40% (4/10), espanhol 50% (1/2), estatística 22%, informática 13%, física 7%, química 3%, matemática 0%, penal-militar 0%.

## Leitura dos números (amostra pequena)
- **Nenhum gabarito errado em 200**: o banco é confiável no essencial; os problemas são de qualidade.
- **Viés de tamanho**: em Q1 a correta é a mais longa em 44% (o dobro do esperado). Vale um passe automático no banco todo (`validate_content.py` já avisa >35% por arquivo) e reequilíbrio das alternativas nas aulas jurídicas.
- **Distratores fracos** são a categoria nº 1 de achado em Q1 (7 de 16); **biologia** concentra achados em Q2 (17 de 27), principalmente de estilo e fidelidade.
- **Negações sem destaque em MAIÚSCULAS**: ocorreram (1 de 2 em Q1, 1 de 4 em Q2) e um caso com “NÃO” corrompido (“NíO”) — vale uma busca global por caracteres corrompidos em enunciados.
- Todas as correções foram aplicadas direto em `content/items` (ver `git diff`); `validate_content.py` seguia limpo nos arquivos corrigidos (a única falha atual é `direito-constitucional/a09`, anterior ao trabalho dos agentes).

## Pendências
- 99% do banco de questões não foi amostrado; extrapolar a taxa de 21,5% com achados (principalmente MENOR) dá ≈ 2.200 questões com algum ajuste, mas ≈ 0,0% crítico.
- Direito-constitucional/a09 precisa de reparafraseio (ver `testes-unitarios.md` §3).
