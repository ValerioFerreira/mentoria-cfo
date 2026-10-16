# Auditoria estrutural — Matemática (a00–a17)

Escopo: 18 aulas do Estratégia (2.316 págs.). Todas as páginas foram varridas pelo primeiro título de cada uma (`--heads`). As páginas suspeitas foram lidas por inteiro: abertura, mapas, resumos, fronteiras de seção e as ocorrências de cada termo do edital. Edital: Anexo II, Matemática, itens 1 a 5.

**Números:** teoria **898 → 864 págs.**; trechos **61 → 74**; cortes no meio de tópico **10 → 0**; nenhum trecho passa de 17 págs. (maior = 17).

## Correções feitas (`content/overrides/matematica.json`)

### Páginas reclassificadas
| Aula | Págs. | De → para | Motivo |
|---|---|---|---|
| a00 | 3–4 | T → FRONT | Aviso e apresentação do curso, sem conteúdo |
| a02 | 4–5 | T → SUMMARY | Mapa-resumo da aula (formulário) |
| a03 | 3–4, 38–39 | T → SUMMARY | Mapas de Frações e de Razão e Proporção |
| a05 | 35–36 | T → SUMMARY | "Resumo da aula" |
| a06 | 50–52 | T → SUMMARY | "Resumo da aula" |
| a07 | 51–52 | T → SUMMARY | "Resumo da aula" |
| a09 | 18 | T → SUMMARY | Quadro-resumo de par ordenado, produto cartesiano e relação |
| a11 | 65–69 | T → EXTRA | **Duplicata**: repete as págs. 10–14 da a10 (domínio e imagem da função afim) |
| a12 | 3–4 | T → SUMMARY | Mapa da função exponencial |
| a17 | 3–7, 74, 93–94, 125–127 | T → SUMMARY | Formulários de abertura das seções de Trigonometria, Equações, Inequações e Funções (a pág. 94 está em branco) |

### Subtítulos
- **a05**: acrescentados subtítulos reais que faltavam no índice: Cálculo da porcentagem (pág. 5), Fração ordinária em taxa (pág. 14), Variação percentual (pág. 24) e Variação acumulada (pág. 34).
- **a14**: o índice punha "Progressão Aritmética" na pág. 13, mas a seção começa na pág. 10. O subtítulo foi movido.
- Em a00, a01, a03, a08, a09, a12, a13, a14 e a15 foram removidos **cerca de 90 falsos subtítulos automáticos**: fórmulas como "Δ > 0", "𝜋 rad 180°" e "𝑎𝑏 = ℎ𝑐", linhas de tabela (nomes de polígonos na a15, "maior que" na a08) e cabeçalhos de quadro. Para isso foi usada uma regex que pega títulos sem nenhuma palavra de 4 letras ou mais, mais algumas entradas por página.

### Nova divisão em trechos (cortes em inícios de tópico)
| Aula | Teoria (págs.) | Trechos | Trechos depois |
|---|---|---|---|
| a00 | 19 → 17 | 2 → 2 | 5–12, 13–21 |
| a01 | 48 → 48 | 3 → 4 | 3–9, 10–20, 21–33, 34–50 |
| a02 | 22 → 20 | 2 → 2 | 6–14, 15–25 |
| a03 | 63 → 59 | 4 → 5 | 5–14, 15–27, 28–37, 40–50, 51–65 |
| a04 | 7 → 7 | 1 → 1 | 3–9 |
| a05 | 34 → 32 | 2 → 3 | 3–15, 16–23, 24–34 |
| a06 | 50 → 47 | 3 → 4 | 3–8, 9–21, 22–36, 37–49 |
| a07 | 50 → 48 | 3 → 4 | 3–14, 15–23, 24–34, 35–50 |
| a08 | 51 → 51 | 3 → 5 | 3–12, 13–23, 24–31, 32–44, 45–53 |
| a09 | 48 → 47 | 3 → 3 | 3–17, 19–33, 34–50 |
| a10 | 53 → 53 | 4 → 4 | 3–14, 15–31, 32–44, 45–55 |
| a11 | 67 → 62 | 4 → 5 | 3–11, 12–27, 28–37, 38–48, 49–64 |
| a12 | 21 → 19 | 2 → 2 | 5–13, 14–23 |
| a13 | 42 → 42 | 3 → 4 | 4–14, 15–26, 27–33, 34–45 |
| a14 | 34 → 34 | 2 → 3 | 3–9, 10–20, 21–36 |
| a15 | 85 → 85 | 6 → 7 | 3–14, 15–26, 27–37, 38–51, 52–62, 63–76, 77–87 |
| a16 | 54 → 54 | 4 → 4 | sem mudança |
| a17 | 150 → 139 | 10 → 12 | 8–17, 18–29, 30–43, 44–59, 60–73, 75–81, 82–92, 95–104, 105–115, 116–124, 128–143, 144–152 |

Motivos principais:
- **a00**: a teoria (5–21) virava um trecho único de 17 págs., com carga 15,5. Foi dividida em "tipos de conjunto" (5–12) e "complexos + operações" (13–21).
- **a01**: o corte antigo caía dentro de "Divisão", que começa no meio da pág. 16. Agora são quatro trechos: soma/subtração, multiplicação/divisão, potenciação/radiciação e problemas/expressões.
- **a02**: o corte saía no meio de "Unidades de área e volume". Agora o 2º trecho começa na pág. 15.
- **a03**: Dízima ficava junto com Razão. Agora Frações tem 3 trechos (MMC e operações; problemas; modelagem e dízima) e Razão e Proporção tem 2 (razão/proporção; escala, velocidade e vazão).
- **a05, a06, a07, a13, a14**: os cortes estavam na pág. 19/20 por limite de páginas, no meio de tópico. Agora seguem as seções de nível 1 do PDF (por exemplo, a07: capitalização composta | taxa nominal/efetiva | taxas equivalentes | convenção e tabela).
- **a08**: um trecho juntava discriminante, Girard e inequações de 1º grau, e outro juntava inequações de 1º e 2º grau. Agora são 5 trechos: 1º grau + sistemas; Bhaskara/discriminante; Girard/biquadradas; inequações de 1º grau; inequações de 2º grau.
- **a10**: "Coeficientes" (15–31) ficava partido. Agora é um trecho inteiro.
- **a11**: havia 3 cortes no meio de tópico. Agora: definição/gráfico | coeficientes | raízes | forma fatorada e soma/produto | vértice (inclui as aplicações de máximo e mínimo).
- **a15**: cada trecho é um bloco do PDF: noções e ângulos | circunferência | triângulos (classificação, congruência, semelhança) | Tales, áreas, Pitágoras e relações métricas | pontos notáveis | quadriláteros e polígonos | inscrição.
- **a17**: depois que os formulários saíram, equações e inequações de seno/cosseno/tangente ficaram em trechos próprios e não se misturam mais com funções. Funções trigonométricas foram divididas em básicas/gráficos e frequência/máximos/inversas.

Trechos curtos (carga < 5, que o planejador eleva para 30 min): a13 27–33 (definição e domínio da função logarítmica) e a17 75–81 (equação sen = sen). São assuntos autônomos, por isso foram mantidos.

## Cobertura do edital (detalhe em `content/edital/matematica.json`)
| Item | Assunto | Status | Onde |
|---|---|---|---|
| 1.1 | Operações em conjuntos numéricos | covered | a00 5–21; a01 3–33; a03 5–37 |
| 1.2 | Desigualdades | covered | a08 32–53 |
| 1.3 | Divisibilidade | **partial** | a03 5–8 (primos, múltiplos, MMC); a01 16–20 (divisão). Sem critérios de divisibilidade nem MDC |
| 1.4 | Fatoração | covered | a03 6–7; a01 44–50 |
| 1.5 | Razões e proporções | covered | a03 40–65 |
| 1.6 | Porcentagem | covered | a05 3–34 |
| 1.7 | Juros | covered | a06 3–49; a07 3–50 |
| 1.8 | Dependência entre grandezas | covered | a04 3–9; a03 53–65 (sem divisão proporcional) |
| 1.9 | Sequências e progressões | covered | a14 3–36 |
| 1.10 | Princípios de contagem | elsewhere | estatistica/a05 4–80 |
| 2.1 | Figuras planas e espaciais | covered | a15; a16 3–42 |
| 2.2 | Grandezas, unidades e escalas | covered | a02 6–25; escala a03 51–52 |
| 2.3 | Comprimentos, áreas e volumes | covered | a15; a16 12–56 |
| 2.4 | Ângulos | covered | a15 5–14; a17 8–10 |
| 2.5 | Posições de retas | **partial** | a15 3–5, 9–11 (só no plano: paralelas, concorrentes, coincidentes) |
| 2.6 | Simetrias de figuras | **gap** | — |
| 2.7 | Congruência e semelhança | covered | a15 31–37 |
| 2.8 | Teorema de Tales | covered | a15 38–39 |
| 2.9 | Relações métricas nos triângulos | covered | a15 42–51; a17 44–48 |
| 2.10 | Circunferências | covered | a15 15–26, 77–87 |
| 2.11 | Trigonometria do ângulo agudo | covered | a17 8–20; a15 42–43 |
| 3.1 | Representação de dados | elsewhere | estatistica/a00 4–75 |
| 3.2 | Média, moda e mediana | elsewhere | estatistica/a01, a02, a03 |
| 3.3 | Desvios e variância | elsewhere | estatistica/a04 4–72 |
| 3.4 | Probabilidade | elsewhere | estatistica/a06 3–72 |
| 4.1 | Gráficos e funções | covered | a09 3–50 |
| 4.2–4.3 | Funções de 1º e 2º grau | covered | a10 3–55; a11 3–64 |
| 4.4 | Funções polinomiais | **partial** | só graus 1 e 2 (a10, a11) |
| 4.5 | Funções racionais | **partial** (muito raso) | a08 40–44, 49–53 (inequação-quociente); a09 27–30 (domínio) |
| 4.6 | Funções exponenciais | covered | a12 5–23 (sem seção de equações exponenciais) |
| 4.7 | Funções logarítmicas | covered | a13 4–45 |
| 4.8 | Equações e inequações | covered | a08 3–53; a17 75–124 |
| 4.9 | Relações no ciclo trigonométrico | covered | a17 21–73 |
| 4.10 | Funções trigonométricas | covered | a17 128–152 |
| 5.1 | Plano cartesiano | covered (raso) | a09 3–5 |
| 5.2 | Retas (analítica) | **partial** | a10 15–44 (reta só como gráfico da função afim) |
| 5.3 | Circunferências (analítica) | **gap** | — |
| 5.4 | Paralelismo e perpendicularidade (analítica) | **gap** | — |
| 5.5 | Sistemas de equações | covered | a08 7–12 |

## Lacunas reais (não há complemento de Matemática em `content/complements/` nem em `gaps.json`)
1. **Geometria analítica (item 5 quase inteiro)**: distância entre pontos, ponto médio, equações da reta (reduzida, geral, ponto-inclinação), interseção de retas, condições de paralelismo e de perpendicularidade, distância de ponto a reta, equação da circunferência e posições relativas. É a lacuna de **maior peso**, porque o edital dedica a ela um item próprio.
2. **Simetrias de figuras planas ou espaciais (2.6)**: ausente (eixos de simetria, simetria central, reflexão, rotação e translação de figuras).
3. **Funções polinomiais de grau ≥ 3 e funções racionais (4.4–4.5)**: ausentes ou muito rasas.
4. **Divisibilidade (1.3)**: faltam os critérios de divisibilidade e o MDC.
5. Menores: posições de retas no espaço (reversas, perpendiculares) (2.5); equações exponenciais como tópico (4.6/4.8); divisão proporcional (1.8).

Itens que **não** são lacuna: contagem, estatística descritiva e probabilidade estão na disciplina Estatística (aulas a00–a06). Escala está em a03 51–52. Tales, relações métricas e sistemas estão cobertos.

## Pendências e incertezas
- **a11 págs. 65–69**: erro editorial do PDF (cópia de a10 10–14). Elas saíram da teoria, mas a aula fica sem uma seção de domínio e imagem da quadrática. O conteúdo aparece em parte no vértice (47–64). Vale verificar se existe uma versão corrigida do PDF.
- **a02 pág. 21** (mapa de Unidades de Tempo, 1 pág.) ficou como teoria. Se fosse SUMMARY, sobraria um trecho isolado de 4 págs. (22–25).
- **a17 inequações trigonométricas (95–124, 3 trechos)** e transformação em produto (71–73) são aprofundamento. Os trechos não têm marcação de camada, então eles entram no Essencial. Ver os pedidos abaixo.
- **a07 35–50** (convenção linear, tabela financeira) vai além do edital, mas foi mantido.
- **a00 pág. 13** (complexos) está fora da lista do edital. É só 1 pág. e foi mantida.
- As referências a Estatística usam as páginas de teoria da estrutura atual de `estatistica`, que está sendo auditada em paralelo. Se aquela auditoria mudar as faixas, o mapa precisa ser refeito.
- Muitos trechos têm questões resolvidas no meio da teoria (estilo "Comentários / Gabarito"). Isso é normal no material e foi mantido como teoria.

## Pedidos ao orquestrador
1. Decidir quais complementos autorais criar, por prioridade: (a) **"Geometria analítica plana"** (itens 5.1–5.4, alta prioridade); (b) "Simetrias de figuras" (2.6); (c) "Polinômios e funções racionais" (4.4–4.5); (d) "Divisibilidade: critérios e MDC" (1.3). Depois, registrar em `gaps.json`.
2. Se o planejador aceitar prioridade por trecho, marcar como aprofundamento os trechos a17 s08–s10 (inequações trigonométricas) e a07 s04 (convenção e tabela financeira).
3. Fazer o planejador ou catálogo ligar os itens 1.10 e 3.x de Matemática às aulas de Estatística, para que contem na cobertura de Matemática.
4. Cosmético: o título da a01 no catálogo vem truncado do nome do arquivo ("...Expressões Numéricas; Ex").
