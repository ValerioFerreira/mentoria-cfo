# Achados: diretrizes, resumos de bizu, ponteiros e itens C/E × PDF (parcial, encerrado em 2026-10-10)

Os 3 agentes de amostragem (S1, S2, S3) foram interrompidos pelo limite semanal de uso da API. Cada um fazia 10 rodadas de 10 trechos (100 trechos por agente, sorteio com semente fixa, só o PDF como verdade). O registro completo de cada achado (evidência, página, correção) está nos arquivos parciais desta pasta; aqui fica a consolidação.

## Cobertura realizada

| Agente | Disciplinas | Semente | Trechos auditados | Meta |
|---|---|---|---|---|
| S1 | direito-constitucional, informática, legislações-PE, penal-militar, inglês | 71001 | 10 (o agente chegou ao n=13 sem registrar) | 100 |
| S2 | biologia, química, física, direito-administrativo | 72002 | 20 | 100 |
| S3 | estatística, matemática, português, espanhol | 73003 | 10 | 100 |
| **Total** | | | **40 registrados** | 300 |

## Métricas das rodadas registradas (40 trechos)

| Dimensão | S1 (10) PEQ/ERRO | S2 (20) PEQ/ERRO | S3 (10) PEQ/ERRO |
|---|---|---|---|
| Diretriz | 3 / 0 | 1 / 0 | 2 / 0 |
| Resumo | 5 / 0 | 8 / 0 | 4 / 1 |
| Ponteiros | 1 / 0 | 1 / 0 | 1 / 0 |
| C/E | 1 / 0 | 2 / 0 | 0 / 1 |

Itens C/E avaliados: 363 (90 + 182 + 91), **0 gabaritos errados**; 3 itens ambíguos ou não sustentados pelo trecho.
Achados: S1 10 (7 corrigidos, 3 propostos), S2 10 (8 corrigidos, 1 proposto), S3 ver arquivo (≈ 6, dos quais A-01 e A-05 de diretriz propostos).

## Leitura dos números (amostra pequena, ainda indicativa)
- **Diretriz**: nenhum ERRO; só PEQUENO (≈ 5–30%), quase sempre grafia do título ou sufixo do tópico, não localização. Confirma a melhora após o texto "se começar no meio da página… leia também a parte antes do título".
- **Resumo** é a dimensão mais frágil (40–50% com algum PEQUENO; 1 ERRO em português): afirmação que vem de fora do intervalo ou detalhe omitido do trecho.
- **Ponteiros**: 3 imprecisões em 40 trechos (≈ 7,5%), todas de ±1 página.
- **C/E**: gabarito sempre correto; o problema é item que mistura matéria de fora do trecho.

## Correções aplicadas (já no working tree, não commitadas)
~67 arquivos de `content/items/` alterados (138 linhas), entre rodadas dos agentes de amostragem e de questões, mais as edições do ciclo anterior (Matemática, Estatística, Constitucional). `legislacoes-pe/a01` s02 foi reparafraseado pelo orquestrador porque a correção do agente enumerava os incisos quase literalmente (o validador acusou 10 palavras iguais).

## Propostas de override de diretriz (PENDENTES — ninguém aplicou)
Não editar `structure/`/`segments/` à mão. Aplicar em `content/overrides/<disc>.json`, rodar `segment.py --subject <disc>` → `build_catalog.py` → `build_complements.py` → `prisma db seed`, e **conferir se os ids de trecho não mudaram** (mudança de página inicial pode deslocar ids e invalidar `content/items`).
1. informática, aula a12: `dropHeadings` p.62 “AINEL DE ONTROLE” e p.74 “ONFIGURAÇÕES”; `headings` “Painel de Controle” (p.62) e “Configurações” (p.74), nível 1 (títulos com capitular quebrada).
2. língua-inglesa, aula a04: troca do título da p.24 por “Futuro Simples e com o GOING TO” (grafia).
3. direito-penal-militar, aula a04: `headings` p.9 “Aplicação da Pena” e p.19 “Concurso de agravantes e atenuantes” (+ `dropHeadings` dos antigos).
4. química, aula a02, 1º trecho: `startPage` 3 → 4 e título “Distribuição eletrônica de Linus Pauling” (sem sufixo “- Teoria”). **Cuidado: muda página inicial.**
5. língua-portuguesa: a04 p.69 “Noções iniciais” e a13 p.82 “Uso de formas abreviadas” (efeito prático nulo, baixa prioridade).
Texto exato de cada proposta: arquivos `_parcial-diretrizes-bizus-S1.md` (A-xx com status “proposto”), `S2` (linha ~102) e `S3` (A-01, A-05).

## Arquivos de origem
`_parcial-diretrizes-bizus-S1.md`, `_parcial-diretrizes-bizus-S2.md`, `_parcial-diretrizes-bizus-S3.md` (tabelas por rodada, registro de achados, padrões).
