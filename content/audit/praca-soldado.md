# Concurso de praça (Soldado do CBMPE, código 201) × material do CFO (2º Tenente, código 401)

Fonte: edital de abertura (Diário Oficial, 29/09/2026), tabelas 10.1 e 10.2 e Anexo II. Prova objetiva de **28/02/2027** para os dois cargos.

## Estrutura da prova do Soldado (60 questões; mínimo de 30% por bloco, nenhuma área zerada, 30% no total)
| Bloco | Disciplina (questões) | No CFO? | Programa |
|---|---|---|---|
| I (30) | Língua Portuguesa (10) | sim | idêntico ao do CFO (18 itens) |
| I | Informática (5) | sim | idêntico |
| I | Matemática (10) | sim | idêntico (5 grupos) |
| I | **Raciocínio Lógico (5)** | **não** | estruturas lógicas, argumentação, diagramas, contagem e probabilidade |
| II (10) | Física (5) | sim | idêntico |
| II | Biologia (5) | sim | idêntico |
| III (20) | Direito Constitucional (10) | sim, **subconjunto** | princípios fundamentais; direitos e garantias; organização do Estado (inclui militares dos Estados); Poderes; funções essenciais; defesa do Estado; súmulas; ECA; Estatuto da Juventude; Maria da Penha |
| III | **Atualidades (5)** | **não** | mundo contemporâneo, América Latina/Mercosul, cotidiano brasileiro |
| III | **História de Pernambuco (5)** | **não** | 8 itens (colonização, holandeses, movimentos, república, cultura popular, aspectos afro-brasileiros) |

Redação: 40 pontos para o Soldado (mínimo 12) e 30 para o 2º Tenente (mínimo 9). Nenhum dos dois cargos tem Redação no MentorIA hoje.

Matérias do CFO que o Soldado **não** cobra: Língua Estrangeira, Estatística, Química, Direito Administrativo, Legislações PE e Direito Penal Militar.

## Conclusão
- 6 das 9 matérias já existem no material do CFO com o mesmo programa (45 das 60 questões = 75% dos pontos). Direito Constitucional é um subconjunto: o Soldado não cobra poder constituinte, controle de constitucionalidade, ordem social nem a Constituição de Pernambuco.
- **Faltam 3 matérias (15 questões = 25%)**: Raciocínio Lógico, Atualidades e História de Pernambuco. Como nenhuma área pode ser zerada, elas são obrigatórias para um plano de Soldado de verdade.
- Possível lacuna pequena: "Dos princípios fundamentais" (arts. 1º a 4º da CF) não aparece como assunto próprio no mapa do edital do CFO; conferir o material de Direito Constitucional a00/a01.
- Sobreposição parcial: contagem e probabilidade (Raciocínio Lógico, item 4) tocam Matemática 1.10 e 3.4.

## Procedimento para o site planejar o Soldado
1. **Concurso como dimensão do plano.** Hoje `Subject.block` e `Subject.examQuestions` valem para uma prova só. Criar `ContestSubject` (concurso, disciplina, bloco, nº de questões, ordem) e `Plan.contest`; semear a partir de `content/contests/cbmpe-soldado.json` (tabela 10.1) e do existente para o CFO. O enum `Contest` e a lista `CONTESTS` já existem (Soldado já aparece na escolha de concurso).
2. **Filtrar o programa.** `content/edital/<disciplina>.json` já liga cada assunto do edital aos trechos. Criar a lista de assuntos de cada disciplina que o Soldado cobra (em Direito Constitucional: só os itens 6, 7.x, 8, 9, 10, 13 a 16 do mapa do CFO, mais os arts. 1º a 4º) e fazer o planejador usar só os trechos ligados a esses assuntos. A tabela `EditalItem` (assuntos do edital) é a base disso.
3. **Três matérias novas.** Duas rotas: (a) adquirir os PDFs do curso para Raciocínio Lógico, Atualidades e História de Pernambuco e passar pelo pipeline (índice, extração, segmentação, auditoria, mapa do edital, bizus e questões); ou (b) escrever como complementos autorais (`content/complements/*.md`, como já foi feito em 25 pontos do CFO). Atualidades envelhece: exige revisão anual.
4. **Planejador e telas.** Parametrizar `loadPlannerData` por concurso (blocos, pesos, data da prova) e o assistente (`/onboarding?concurso=`), a projeção do Desempenho (blocos e mínimos do Soldado: bloco II só tem 10 questões) e a escolha do concurso na lista de espera.
5. **Conteúdo.** Reaproveitar bizus e questões das 6 matérias em comum; produzir bizus e questões das 3 novas; revisar o nível das questões (cargo de nível médio).
6. **Redação** (opcional, vale para os dois cargos): ainda fora do sistema.
