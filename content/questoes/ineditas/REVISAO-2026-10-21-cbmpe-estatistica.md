# Revisão 2026-10-21 — inéditas CBMPE de múltipla escolha: Estatística (agente `estatistica`)

Arquivo gravado: `content/questoes/ineditas/mc/estatistica.txt` (+165 questões, de 183 para 348; letras A 69 · B 69 · C 70 · D 70 · E 70).
`lacunas_cbmpe.py --lista estatistica` não aponta mais nenhum trecho abaixo de 7; `ineditas_mc_nativas.py --check` termina com `erros 0`.

## Quantidade por aula (trechos)

| Aula | Trechos (questões novas) | Total |
| --- | --- | --- |
| a00 Apresentação de dados | s03 (1), s05 (1) | 2 |
| a01 Médias | s02 (1), s05 (1) | 2 |
| a04 Variabilidade | s02 (1), s04 (1) | 2 |
| a07 VA discretas | s01 (7), s02 (7), s03 (7), s05 (7), s06 (6) | 34 |
| a08 Distribuições discretas | s01 (3), s02 (6), s03 (6), s04 (5), s06 (4) | 24 |
| a09 VA contínuas | s01 (6), s02 (7), s03 (6), s04 (7) | 26 |
| a10 Distribuições contínuas | s01 (4), s02 (1), s03 (5), s04 (6), s05 (6), s06 (8), s07 (1) | 31 |
| a11 Testes de hipóteses | s01 (5), s05 (1) | 6 |
| a12 Regressão simples | s01 (4), s02 (6) | 10 |
| a13 Regressão múltipla | s01 (1), s02 (2), s03 (7) | 10 |
| a14 ANOVA | s01 (1), s02 (6), s03 (4), s04 (7) | 18 |
| **Total** | **38 trechos** | **165** |

(a10/s06 recebeu 8 em vez de 7, uma a mais que o mínimo.)

## Método de conferência

- Toda conta (médias, variâncias, binomial, geométrica, hipergeométrica, normal, TCL, Chebyshev, Markov, Cantelli, correlação, F da ANOVA, R² ajustado etc.) foi refeita por dois caminhos (fórmula direta e conferência por complemento, soma de quadrados ou raciocínio sequencial) e o caminho de conferência consta no comentário.
- Valores de tabela da normal padrão usados são fornecidos no enunciado (P(0<Z<1) = 0,3413; P(0<Z<2) = 0,4772; P(0<Z<1,96) = 0,475); nenhuma questão exige tabela externa.
- Convenções explicitadas nos enunciados: geométrica e binomial negativa contam **ensaios** (não fracassos) até o 1º/r-ésimo sucesso, inclusive o do sucesso; variância amostral com divisor n − 1 quando dito; desigualdade unilateral de Chebyshev (Cantelli) apresentada com a fórmula no enunciado.
- Comentários sem letras de alternativas (a posição da correta é embaralhada pela ferramenta).
- Nenhuma questão copia texto do material protegido nem de provas.

## Dúvidas para o dono

1. **Trechos sem assunto do edital**: a07/s02, s03, s05, s06; a09/s03, s04; a11/s05 e a14/s04 não constam do mapa `content/edital/estatistica.json` (nem do PCPE). Pelo aviso do coordenador, as questões ficam com `editalItemId` nulo; vale completar o mapa (sugestão: a07/s02-s06 e a09/s02-s04 junto aos itens 3.x de variáveis aleatórias; a11/s05 em 5.1; a14/s04 em 5.3) para que apareçam também na página Questões por assunto.
2. **Convenção da geométrica / binomial negativa**: bancas variam entre contar ensaios e contar fracassos. As inéditas fixam "número de ensaios" no enunciado, que é a convenção do resumo do curso; se o material-base usar outra, convém conferir.
3. **Desigualdade unilateral (a09/s04)**: usei a forma σ²/(σ² + t²) (Cantelli) escrita no enunciado, para não depender de qual das variantes o material adota.
4. **Aproximação binomial → normal (a10/s06)**: a questão de condições de uso é qualitativa ("n grande e p longe de 0 e 1"), sem fixar o critério numérico (np ≥ 5 ou ≥ 10), que varia entre fontes.
5. Em a10/s05 e a10/s06 há questões de média amostral/TCL que também servem a trechos de amostragem; podem ser realocadas se o dono preferir.
