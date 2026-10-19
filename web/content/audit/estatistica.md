# Auditoria estrutural — Estatística (a00–a14)

Edital (Anexo II, 2º Tenente): 1. Conceitos (população, censo, amostra aleatória, normas de apresentação de dados) · 2. Probabilidade (clássica, geométrica, axiomática) · 3. Variáveis aleatórias discretas/contínuas, distribuições, f.d.p., f.d.a., função de probabilidade · 4. Descrição numérica e gráfica (centralidade, posição, dispersão, histograma, boxplot) · 5. Testes de hipóteses (t, F, ANOVA) · 6. Regressão linear (ajuste da reta e de outras funções lineares).

## Escopo auditado
- 15 aulas, 2.322 páginas de PDF: varredura `--heads` de todas as páginas de teoria, das bordas teoria/questões/lista e leitura das páginas suspeitas (aberturas, resumos, inícios de tópico, trechos sobre amostragem, normas de tabela, probabilidade geométrica, axiomas, f.d.a., regressão).
- Detecção automática de páginas repetidas entre aulas (sobreposição de 8-gramas entre páginas T).

## Números
| | Antes | Depois |
|---|---|---|
| Páginas de teoria | 1.020 | 956 |
| Trechos | 71 | 77 |
| Trechos > 17 págs. | 0 | 0 |
| Trechos que começam no meio de tópico | vários (a01, a02, a04, a07, a08, a09, a10, a13) | 1 (a08 s02, divisão da Binomial no início dos exercícios) |

Por aula (teoria antes → depois; trechos): a00 72→63 (5→5) · a01 72→67 (5) · a02 85→76 (6) · a03 35→37 (3) · a04 69→70 (5→6) · a05 77→75 (5) · a06 70→68 (5) · a07 82→75 (5→6) · a08 69→58 (5→6) · a09 47→45 (3→4) · a10 76→73 (5→7) · a11 109→106 (8) · a12 65→58 (4) · a13 40→36 (3) · a14 52→49 (4).

## Correções feitas (`content/overrides/estatistica.json`)
1. **Resumos tirados da teoria (SUMMARY)**: a00 68–75, a01 70–74, a02 79–87, a05 79–80, a06 72, a07 85, a08 71, a09 49, a10 77–78, a11 111–112, a12 61–67, a13 39–42, a14 53–54. Motivo: inflavam a teoria e geravam trechos de "resumo" (ex.: a02 s06, a12 s04 parcial).
2. **Aberturas tiradas da teoria (FRONT)**: a00 4 (aviso), a06 3, a08 3, a09 3, a10 3, a11 4, a14 3 (apresentação da professora).
3. **Teoria recuperada (THEORY)**: a03 3–4 (conceito de moda, uni/bi/amodal) e a04 3 (motivação das medidas de variabilidade), com subtítulo na página de início.
4. **Páginas duplicadas no PDF** (erro de montagem do material):
   - a08 4–12 = cópia de a10 4–12 (uniforme **contínua**; o cabeçalho diz "Distribuições Contínuas"). Retiradas da a08.
   - a07 37–42 = cópia de a09 16–21 (f.d.a. de variável contínua, com integrais ainda não ensinadas na a07). Retiradas da a07.
   - Marcadas como SUMMARY por não haver tipo "duplicado" (ver pedidos). Notas explicativas no catálogo das aulas a07 e a08.
5. **Falsos subtítulos removidos**: em todas as aulas, os subtítulos automáticos que começam por símbolo/fórmula (`^[^A-Za-zÀ-ÿ]`: "] × h", "P(A) =", "E(X) =", "SQT = SQM + SQR" etc.). Na a13, também ~90 linhas de exemplo/matriz e os rótulos de gráfico "Linear/Potência/Exponencial/Logarítmica/Polinomial". Eles barateavam cortes no meio de tópicos (ex.: a02 s02 começava em "] × h"; a13 s02 em "QMM = SQM").
6. **Cortes (início de tópico real)**:
   - a00 [19, 27, 42, 54]: conceitos/variáveis · séries e tabelas · elementos da distribuição de frequências · gráficos da distribuição · outros gráficos (antes: Séries cortada entre s01 e s02).
   - a01 [16, 33, 47, 59]: somatório · média aritmética · ponderada/agrupados · agrupados por classe/geométrica · harmônica/desigualdade.
   - a02 [17, 33, 44, 53, 67]: mediana (não agrupados) · mediana em classes · quartis · decis · percentis · box plot.
   - a04 [17, 27, 39, 50, 62]: amplitudes · desvios · desvio médio · variância · desvio-padrão · CV/variância relativa (antes três trechos começavam no meio de Desvio Médio, Variância e Propriedades do DP).
   - a07 [17, 27]: VA discreta · esperança · moda/mediana (antes s01 cortava "Medidas de Tendência Central").
   - a08 [33, 43, 53, 65]: uma distribuição por trecho; Bernoulli+Binomial (20 págs.) dividida no início dos exercícios da Binomial (pág. 23). Binomial Negativa fica com 6 págs. (autônoma).
   - a09 [16, 28, 42]: f.d.p. · f.d.a./mediana/moda · esperança/variância/covariância · desigualdades.
   - a10 [13, 25, 32, 42, 51]: uniforme · exponencial · exponencial (várias variáveis, relações) · normal/normal padrão · transformação · soma/TCL/aproximação · qui-quadrado/t/F.
   - a12 [19, 30]: Pearson · correlação parcial/propriedades · regressão (MQO, reta pela origem) · EMV + ANOVA da regressão.
   - a13 [13, 25]: modelo matricial · ANOVA da regressão múltipla · dummy/especificação/RESET/Box-Cox.
   - a03, a05, a06, a11, a14: divisão mantida (coerente).
7. **Edital das aulas**: a13 `partial` confirmado (nota atualizada: só ANOVA da regressão e formas funcionais servem ao item 6). a05 mantida `yes` com nota de relação cruzada com Matemática.

## Cobertura do edital
| Item | Status | Onde |
|---|---|---|
| 1.1 População | covered | a00 7–8 |
| 1.2 Censo | covered | a00 7 |
| 1.3 Amostra aleatória | **partial** | a00 7–8; a07 4 — sem tipos de amostragem |
| 1.4 Normas de apresentação de dados | **partial** | a00 19–23 (elementos da tabela, séries), 42–67 (gráficos) — sem normas IBGE/ABNT |
| 2.1 Probabilidade clássica | covered | a06 4–15 |
| 2.2 Probabilidade geométrica | **gap** | só análogo na uniforme contínua (a10 4–6) |
| 2.3 Probabilidade axiomática | covered | a06 38–42 |
| 3.1 VA discreta | covered | a07 4–16 |
| 3.2 VA contínua | covered | a07 5–8; a09 4–15 |
| 3.3 Distribuições discretas | covered | a08 13–70 (uniforme discreta sem teoria) |
| 3.4 Distribuições contínuas | covered | a10 4–76 |
| 3.5 Função densidade | covered | a09 4–15 |
| 3.6 Função distribuição | covered | a09 16–21; a10 5–6 |
| 3.7 Função de probabilidade | covered | a07 9–16 |
| 4.1 Centralidade | covered | a01; a02 3–32; a03 |
| 4.2 Posição | covered | a01 4–5; a02 33–66 |
| 4.3 Dispersão | covered | a04 3–72 |
| 4.4 Histograma | covered | a00 42–53 |
| 4.5 Boxplot | covered | a02 67–78 |
| 5.1 Teste t | covered | a11 36–55; a10 68–72 |
| 5.2 Teste F | covered | a11 70–75; a10 73–76; a14 16–20 |
| 5.3 ANOVA | covered | a14 4–41 |
| 6.1 Ajuste da reta | covered | a12 30–60 |
| 6.2 Outras funções lineares | **partial** | a13 30–31, 37–38 — sem linearização passo a passo |
| Matemática: contagem | elsewhere | a05 (Matemática não tem aula de combinatória) |
| Matemática: estatística/probabilidade | elsewhere | a00–a04, a06 |

## Auditoria inversa (resumo)
- **Indexada no lugar errado**: 13 resumos e 7 aberturas como teoria; 2 blocos duplicados (a07 37–42, a08 4–12).
- **Subindexada**: a03 3–4, a04 3 (teoria marcada como abertura).
- **Superfragmentada**: fórmulas como subtítulos em quase todas as aulas; a13 com ~90 falsos subtítulos.
- **Conteúdo complementar** (mantido, base para itens do edital): covariância/correlação (a07 61–78), TCL e qui-quadrado como distribuição (a10 51–67), intervalos de confiança e teste t dos coeficientes (a14 42–52).
- **Possível fora do escopo** (mantido, em trechos próprios fáceis de pular): partições/Kaplansky (a05 65–78), desigualdade de Chebyshev (a09 42–48), testes para uniforme/proporções/binomial e não paramétricos (a11 25–27, 56–65, 81–110), correlação parcial/autocorrelação/EMV (a12 19–20, 46–47), regressão múltipla/dummy/RESET (a13).
- **Já corretamente indexada**: propriedade da mediana repetida em a02 30–32 e a04 22–24 (repetição intencional).
- **Necessita revisão humana**: a08 sem a seção de uniforme discreta (PDF trocado).

## Lacunas e complementos
- `content/gaps.json` não tem lacunas de Estatística e não há complemento da disciplina.
- **Probabilidade geométrica**: lacuna real (item explícito do edital). Recomendo complemento curto (3–4 págs.: razão entre comprimentos, áreas e volumes; exemplos de ponto ao acaso em segmento, quadrado e círculo; encontro de duas pessoas).
- **Normas para apresentação de dados**: parcial. Complemento curto recomendado com as normas de apresentação tabular do IBGE (elementos obrigatórios, sinais convencionais "–", "...", "x", "0", tabela aberta, notas e chamadas, arredondamento).
- **Outras funções lineares**: parcial. Complemento curto opcional sobre linearização (log em exponencial/potência, recíproca) e ajuste pela reta de MQO.
- **Amostra aleatória**: parcial. Os tipos de amostragem podem entrar no mesmo complemento das normas.
- Nenhum complemento foi criado (decisão do orquestrador).

## Pendências
1. Duplicatas marcadas como SUMMARY: semanticamente incorreto, mas é o único tipo que tira as páginas da teoria. As questões da a08 sobre uniforme discreta (C 72–74, L 117–118) continuam na Fixação, sem teoria correspondente.
2. a08 s02 (págs. 23–32) começa no meio da Binomial (Bernoulli + Binomial = 20 págs., acima do teto). O corte foi posto no início dos exercícios.
3. Três trechos curtos de assunto autônomo: a08 s06 (6 págs., Binomial Negativa), a09 s04 (7, Chebyshev), a10 s03 (7, exponencial com várias variáveis e relações).
4. a11 tem ~45 págs. de testes não pedidos (qui-quadrado, não paramétricos, proporções); sem tipo de página "opcional", continuam contando como teoria do Essencial.
5. Verificar se o Estratégia publicou versão corrigida das Aulas 07 e 08.

## Pedidos ao orquestrador
1. Criar um tipo de página para **duplicado** (e talvez **opcional/fora do edital**) no `segment.py`/planejador, em vez de usar SUMMARY; permitiria tirar do Essencial a11 81–110, a05 65–78, a09 42–48, a13 25–38.
2. Decidir os complementos: probabilidade geométrica (prioridade alta), normas IBGE + tipos de amostragem (média), linearização de funções (baixa).
3. Registrar no mapa de Matemática que "princípios de contagem" e "estatística e probabilidade" são atendidos por estatistica/a05 e a00–a04, a06.
4. Rodar `build_catalog.py` (e o seed) para levar as notas das aulas a05, a07, a08 e a13 e os novos trechos ao catálogo.
