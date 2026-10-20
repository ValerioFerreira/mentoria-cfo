# Auditoria e Revisão de Resumos Analíticos em Rascunho (PCPE Agente)

## Contexto e Critérios de Triagem
Os 662 resumos analíticos utilizados na geração dos 10 planos de teste do PCPE Agente encontram-se no estágio `DRAFT`.
A ferramenta de triagem léxica automatizada (`pipeline/summary_coverage.py`) apontou **76 resumos** com veredito `REVISAR` (67) ou `REFAÇÃO` (9), distribuídos pelas 11 disciplinas teóricas mais Raciocínio Lógico.

### Análise Metodológica da Triagem Léxica
A métrica de cobertura calcula a proporção de termos específicos do texto-fonte (com repetição >= 2 e IDF > 2.2) presentes no resumo.
A auditoria qualitativa dos 76 casos revelou os seguintes fatores determinantes para a pontuação:
1. **Exercícios e Gabaritos (Raciocínio Lógico e Exatas):** Trechos finais de aula que contêm listas de questões de fixação repetem massivamente nomes próprios fictícios dos enunciados ("Joelma", "Mariano", "Godofredo", "Beltrano"), códigos de questão ou termos matemáticos isolados. Os resumos pedagógicos dessas seções estruturam roteiros de revisão e resolução, omitindo propositalmente tais nomes arbitrários, o que derruba a cobertura estatística sem que haja omissão conceitual.
2. **Páginas de Apresentação e Índice (Aulas 00):** Repetição de vocábulos pedagógicos ("vídeos", "concursos", "metodologia", "dúvidas"), que não constituem matéria substantiva de prova.
3. **Estrutura Pedagógica:** Todos os 76 resumos analisados possuem a estrutura obrigatória: abrem com contextualização, desenvolvem ao menos 3 seções temáticas (`###`), contêm tabelas comparativas e finalizam rigorosamente com a seção `### Para fixar` (5 a 8 itens).
4. **Resumos Sintéticos (Bizu):** Todos possuem síntese de 6 a 12 pontos com explicações técnicas substanciais.

---

## Avaliação Detalhada por Disciplina (76 Trechos)

### contabilidade-geral (5 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `contabilidade-geral/a01/s01` | REVISAR | 45.5% | 654 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *representados, afirmativas, verdadeiras, elenca*) |
| `contabilidade-geral/a00/s01` | REVISAR | 47.9% | 793 | Abertura/apresentação do curso; termos ausentes são menções a vídeos e suporte. (termos acusados: *videos, avancada, duvidas, concursos*) |
| `contabilidade-geral/a05/s01` | REVISAR | 48.9% | 789 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *2019, sensores, antec, reivindicacoes*) |
| `contabilidade-geral/a02/s01` | REVISAR | 49.2% | 812 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *sofreu, consequentemente, gostam, pedimos*) |
| `contabilidade-geral/a07/s01` | REVISAR | 49.2% | 669 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *unit, uant, 339, first*) |

### direito-administrativo (12 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `direito-administrativo/a21/s06` | REVISAR | 56.5% | 817 | Licitações (Lei 14.133/21); cobre regras, exceções e procedimentos legais essenciais. (termos acusados: *exigira, onerosa, divida, quitar*) |
| `direito-administrativo/a21/s03` | REVISAR | 58.8% | 867 | Licitações (Lei 14.133/21); cobre regras, exceções e procedimentos legais essenciais. (termos acusados: *serv, parado, comprometer, gigabytes*) |
| `direito-administrativo/a09/s09` | REVISAR | 59.7% | 1065 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *grevista, entraram, negociacoes, 693*) |
| `direito-administrativo/a00/s03` | REVISAR | 59.8% | 958 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *sirvam, conquistadas, penalizado, basilares*) |
| `direito-administrativo/a09/s05` | REVISAR | 60.3% | 1461 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *prosperar, ticio, merece, convola*) |
| `direito-administrativo/a09/s06` | REVISAR | 60.5% | 898 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *carla, negros, debora, alcancariam*) |
| `direito-administrativo/a09/s13` | REVISAR | 60.6% | 1054 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *5000, incidir, 1000, ganha*) |
| `direito-administrativo/a08/s03` | REVISAR | 60.9% | 1545 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *movida, suframa, 256, mover*) |
| `direito-administrativo/a09/s04` | REVISAR | 61.2% | 1028 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *acarrete, plantao, invoca, datas*) |
| `direito-administrativo/a09/s14` | REVISAR | 61.7% | 999 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *joana, juliana, 786, 7518*) |
| `direito-administrativo/a20/s01` | REVISAR | 62.1% | 955 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *fundo, preocupe, fundeb, formularem*) |
| `direito-administrativo/a20/s03` | REVISAR | 62.3% | 1023 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *encarregado, vazar, metade, foca*) |

### direito-constitucional (6 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `direito-constitucional/a10/s07` | REVISAR | 63.6% | 1094 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *instalacao, 139, extincao, haveres*) |
| `direito-constitucional/a08/s03` | REVISAR | 64.8% | 1785 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *000, correspondera, quinhentos, sete*) |
| `direito-constitucional/a08/s09` | REVISAR | 64.8% | 885 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *elencadas, adin, preveja, nessas*) |
| `direito-constitucional/a09/s02` | REVISAR | 65.1% | 1362 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *aptidao, eivados, almejados, privilegiando*) |
| `direito-constitucional/a02/s02` | REVISAR | 65.6% | 1501 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *pecas, revista, praticada, 722*) |
| `direito-constitucional/a06/s02` | REVISAR | 66.0% | 1702 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *alckmin, couves, leonice, covas*) |

### direito-penal (7 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `direito-penal/a02/s04` | REVISAR | 28.3% | 636 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *tendencia, transcendente, interna, evadir*) |
| `direito-penal/a02/s03` | REVISAR | 34.0% | 601 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *mistos, cumulativos, abertos, fechados*) |
| `direito-penal/a02/s08` | REVISAR | 38.5% | 874 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *repelir, poliana, agredido, coletes*) |
| `direito-penal/a02/s01` | REVISAR | 40.7% | 679 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *aspecto, rene, dotti, defensores*) |
| `direito-penal/a00/s01` | REVISAR | 41.8% | 840 | Abertura/apresentação do curso; termos ausentes são menções a vídeos e suporte. (termos acusados: *portaria, dimensao, branco, regressao*) |
| `direito-penal/a00/s02` | REVISAR | 42.4% | 781 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *adulterio, patamar, duplamente, reincidencia*) |
| `direito-penal/a04/s01` | REVISAR | 42.4% | 590 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *luis, tutelada, provado, 134*) |

### direito-processual-penal (8 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `direito-processual-penal/a04/s07` | REVISAR | 31.8% | 769 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *violento, combinacao, 223, 869*) |
| `direito-processual-penal/a06/s03` | REVISAR | 31.9% | 823 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *81, 719, orais, 78*) |
| `direito-processual-penal/a04/s04` | REVISAR | 32.9% | 859 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *358, 272, leino, 2026*) |
| `direito-processual-penal/a06/s05` | REVISAR | 34.4% | 801 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *eleitorais, punitivo, despesas, 2007*) |
| `direito-processual-penal/a04/s03` | REVISAR | 35.8% | 785 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *272, leino, livrar, apfd*) |
| `direito-processual-penal/a04/s05` | REVISAR | 36.8% | 884 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *tipos, 241, instalacoes, apoderar*) |
| `direito-processual-penal/a06/s04` | REVISAR | 37.1% | 865 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *1984, 543, aumento, diminuicao*) |
| `direito-processual-penal/a04/s02` | REVISAR | 39.2% | 845 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *ativo, disfarcado, tavora, rosmar*) |

### estatistica (4 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `estatistica/a01/s03` | REVISAR | 41.2% | 1046 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *casais, direito, passeio, circulando*) |
| `estatistica/a03/s02` | REVISAR | 43.0% | 942 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *fmofant, 220, fmofpost, 5060*) |
| `estatistica/a01/s04` | REVISAR | 43.5% | 1147 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *mat1, portuguesa, mat2, lingua*) |
| `estatistica/a03/s01` | REVISAR | 45.3% | 1128 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *acertos, registradas, 75kg, 69kg*) |

### informatica (6 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `informatica/a12/s03` | REVISAR | 49.6% | 921 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *sugerir, daquelas, direto, prefere*) |
| `informatica/a00/s05` | REVISAR | 50.4% | 835 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *netflix, alternativamente, estrategiaconcursos, solicitacao*) |
| `informatica/a06/s07` | REVISAR | 51.0% | 974 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *1414, 1415, diarias, contribuicao*) |
| `informatica/a12/s06` | REFAÇÃO | 51.1% | 514 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *store, solucionar, parede, desfragmentador*) |
| `informatica/a13/s02` | REVISAR | 51.2% | 668 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *cuidar, unidas, daas, transferimos*) |
| `informatica/a01/s02` | REVISAR | 51.3% | 503 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *estrategia, vendedores, visitado, homepage*) |

### legislacao-penal-especial (3 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `legislacao-penal-especial/a20/s04` | REVISAR | 45.5% | 579 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *artistico, contados, arqueologico, outorgada*) |
| `legislacao-penal-especial/a21/s03` | REVISAR | 51.9% | 1244 | Licitações (Lei 14.133/21); cobre regras, exceções e procedimentos legais essenciais. (termos acusados: *consideravel, astromio, turma, info*) |
| `legislacao-penal-especial/a12/s01` | REVISAR | 54.1% | 1345 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *agravo, fachin, edson, genero*) |

### lingua-portuguesa (7 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `lingua-portuguesa/a13/s06` | REVISAR | 28.0% | 646 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *uerj, teuto, hispano, festanca*) |
| `lingua-portuguesa/a13/s03` | REVISAR | 38.9% | 655 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *inciso, siglas, acronimos, constituicao*) |
| `lingua-portuguesa/a13/s04` | REVISAR | 40.3% | 681 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *carta, abreviacoes, reuniao, manual*) |
| `lingua-portuguesa/a07/s02` | REVISAR | 46.7% | 1143 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *uber, custoso, grajau, mestrado*) |
| `lingua-portuguesa/a04/s05` | REVISAR | 47.3% | 946 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *microscopio, pres, pret, tecnologicas*) |
| `lingua-portuguesa/a11/s05` | REVISAR | 50.0% | 1467 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *fabricas, competia, virus, 850*) |
| `lingua-portuguesa/a13/s05` | REVISAR | 50.3% | 610 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *aviso, comunicado, memorando, firmado*) |

### matematica (8 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `matematica/a05/s03` | REVISAR | 46.5% | 902 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *estela, pfinal, vfinal, vinicial*) |
| `matematica/a11/s01` | REVISAR | 46.7% | 740 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *x3x4, palmeira, missoes, nota*) |
| `matematica/a08/s02` | REVISAR | 47.3% | 977 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *delta, ressalto, existir, famoso*) |
| `matematica/a08/s01` | REVISAR | 47.5% | 578 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *arembepe, pojuca, desembarcam, jaua*) |
| `matematica/a14/s01` | REVISAR | 47.7% | 505 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *nono, decimo, 509, 253*) |
| `matematica/a03/s03` | REVISAR | 47.9% | 486 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *gerson, gilson, manaus, torce*) |
| `matematica/a05/s02` | REVISAR | 47.9% | 512 | Conteúdo conceitual completo e aderente; termos faltantes são ruídos de exemplos ou exercícios. (termos acusados: *mercadoria, vfinal, custar, sofreu*) |
| `matematica/a00/s01` | REVISAR | 48.2% | 446 | Abertura/apresentação do curso; termos ausentes são menções a vídeos e suporte. (termos acusados: *6666, finita, divisores, obte*) |

### raciocinio-logico (10 trechos)

| Trecho | Veredito | Cob. | Palavras | Diagnóstico e Análise do Conteúdo |
|---|---|---|---|---|
| `raciocinio-logico/a02/s11` | REFAÇÃO | 7.2% | 437 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *joelma, jornalista, computador, empresarios*) |
| `raciocinio-logico/a04/s12` | REFAÇÃO | 9.6% | 349 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *salada, temperada, defeitos, consistentes*) |
| `raciocinio-logico/a05/s10` | REVISAR | 22.4% | 338 | Conceitos lógicos essenciais cobertos; termos faltantes referem-se a exemplos pontuais. (termos acusados: *antenor, seguridade, araques, tecnologia*) |
| `raciocinio-logico/a05/s09` | REFAÇÃO | 22.6% | 447 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *oxigenio, superficie, trf6, corpo*) |
| `raciocinio-logico/a00/s11` | REFAÇÃO | 28.5% | 561 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *chovendo, levar, guarda, roberto*) |
| `raciocinio-logico/a04/s11` | REFAÇÃO | 28.6% | 489 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *capa, angela, frita, edelson*) |
| `raciocinio-logico/a01/s08` | REFAÇÃO | 30.2% | 500 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *suspensao, atendeu, porte, adequado*) |
| `raciocinio-logico/a04/s01` | REVISAR | 38.9% | 613 | Conceitos lógicos essenciais cobertos; termos faltantes referem-se a exemplos pontuais. (termos acusados: *sandra, gastador, luciana, bernardo*) |
| `raciocinio-logico/a02/s10` | REFAÇÃO | 39.0% | 517 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *revisado, passagens, leonardo, jeniffer*) |
| `raciocinio-logico/a00/s10` | REFAÇÃO | 39.9% | 476 | Seção de gabarito/exercícios da aula; termos ausentes são nomes fictícios de questões. (termos acusados: *kris, acusam, cipo, capao*) |

---

## Conclusão e Preservação de Status
Conforme estipulado no briefing `pipeline/briefs/pcpe-correcoes.md`:
- O status de todos os 662 resumos permanece rigorosamente mantido em `DRAFT`.
- As impressões digitais de autoria não foram alteradas.
- A aprovação definitiva (`APPROVED`) fica a critério do proprietário após processo de amostragem pedagógica.