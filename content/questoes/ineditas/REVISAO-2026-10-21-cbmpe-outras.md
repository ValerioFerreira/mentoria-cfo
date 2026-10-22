# Revisão — inéditas de múltipla escolha CBMPE (agente `outras`, 21–22/10/2026)

Cinco disciplinas com poucos trechos faltando. Todas as questões foram gravadas com `pipeline/pcpe_tools/ineditas_append.py`
em `content/questoes/ineditas/mc/<disciplina>.txt` (5 alternativas, gabarito embaralhado e balanceado pela ferramenta). Resultado:
`lacunas_cbmpe.py --lista <disciplina>` vazio nas cinco disciplinas e `ineditas_mc_nativas.py --check` sem erro nas minhas disciplinas.

| Disciplina | Questões novas | Trechos atendidos |
| --- | ---: | --- |
| lingua-portuguesa | 51 | a00 (s02–s04), a02/s07, a03 (s01, s02), a04 (s04–s06), a05 (s02–s04), a06 (s01–s04), a07 (s01–s04), a08 (s01: 4, s02: 4, s03: 5), a09/s02, a12 (s01: 6, s02: 5), c01/s01 (6) |
| direito-administrativo | 39 | a00 (s01: 5, s02, s04, s05), a01 (s01–s04: 3 cada; s06, s07), a02/s05, a03/s02, a05 (s05, s11, s12), a06/s05, a07 (s03, s04), a08/s04, a09 (s03, s05, s06, s07, s09, s10, s12, s16) |
| direito-constitucional | 39 | a14/s02 (2), a17 (s01: 6, s02: 2, s03, s04, s06: 2), a18/s01 (7), c02/s01 (6), c04/s01 (7), c04/s02 (5) |
| informatica | 36 | a00 (s03, s05), a02 (s01–s06), a03 (s01–s07), a04 (s02–s04), a06 (s03, s11), a07 (s04: 3, s05: 2), a13 (s01–s04), a14 (s08: 5, s10: 2) |
| legislacoes-pe | 28 | a01/s01 (4), c01/s01 (7), c02/s01 (7), c03/s01 (3), c04/s01 (4), c05/s01 (3) |
| **Total** | **193** | |

## Conferência (revisão cruzada)

Cada questão foi relida após escrita (gabarito, vigência, números, coerência do comentário). Ajustes feitos nessa leitura: troca de
alternativas ambíguas (por exemplo "responder a pergunta", "preferência a", "como se é"), correção de classificação de figuras de
linguagem, alternativas que se repetiam ignorando maiúsculas (substituídas por regravação do bloco) e comprimento da correta.

Fontes oficiais conferidas por leitura do texto integral: Estatuto da Juventude (Planalto), Lei 14.751/2023 (Planalto), Decreto
50.014/2020, Lei 15.187/2013, Lei 11.817/2000 e Lei 6.783/1974 (ALEPE Legis / leisestaduais), CE-PE art. 100 (PDF da ALEPE). As demais
questões de Direito Administrativo e Constitucional seguem a CF/88, a Lei 9.784/1999, a Lei 8.987/1995, a Lei 12.016/2009, a Lei
9.868/1999, a Lei 13.848/2019, a Lei 8.112/1990 e as Súmulas Vinculantes 10 e 44, conhecidas e não consultadas de novo nesta rodada.

Cálculos de Informática (Calc/Excel) conferidos por dois caminhos: `MAIOR(...;2)+MÍNIMO(...)` = 18 + 7 = 25; `CONT.SES` = 3
(linhas 1, 3 e 6 de Recife; também 5 valores ≥ 10, dos quais 3 em Recife); `VP(0,08;5;1000)` = −3.992,71 (1.000 × 3,9927);
`SE` aninhado para 6,5 = "Recuperação".

## Pontos que dependem do dono (ou de nova conferência)

1. **CE-PE (direito-constitucional a18/s01, c04/s01, c04/s02).** O PDF da ALEPE disponível está desatualizado e mistura redações
   tachadas, então só o art. 100 foi confirmado no texto oficial. Os demais números (art. 19 §1º, quórum de emenda, veto de 15 dias úteis, CPI por 1/3,
   TCE com sete conselheiros, PGJ, Lei Orgânica por 2/3, estabilidade em 3 anos, 25% de ensino, intervenção municipal) vêm do resumo do curso
   e coincidem com o modelo federal. Vale uma conferência pontual dos arts. 19, 28–33, 75–99 contra o texto consolidado vigente (EC 68/2025, 70/2026, 71/2026).
2. **Quadro do Comandante-Geral.** A lei estadual do CBMPE (Lei 15.187/2013, art. 10 §1º) fala em oficial do **QOC**, e a Lei 14.751/2023
   (arts. 2º e 29) em oficial do **QOEM**. Há uma questão de cada lado, deixando claro qual lei foi citada no enunciado.
3. **Prisão disciplinar.** As questões de Lei 11.817/2000 (c04/s01) descrevem o texto da lei (detenção/prisão até 30 dias, art. 28 §4º) sem
   mencionar a Lei 13.967/2019 nem a ADI 6595; as do Decreto 50.014/2020 (c01/s01) seguem a letra do decreto (pena mantida, sem privação de liberdade).
   Se o dono preferir enunciados que avisem da decisão do STF, é preciso reescrever.
4. **Regência tradicional (Português).** Alguns itens seguem a norma tradicional e há gramáticos mais permissivos: "informar aos subordinados da
   mudança" e "comunicou ao delegado de que" (a08/s01), "implicar/obedecer a" e a preposição de "aspirar" (inalar x almejar).
5. **Header `item=` em 3 questões de Português** (a00/s02, a00/s03, a00/s04, itens 5.1 e 5.4): foram acrescentadas antes do aviso do orquestrador de
   que o item é opcional. Os códigos são os mesmos já usados nas demais questões desses trechos; se quiser, remova o `| item=...` desses três cabeçalhos.
6. **Ajuste manual de uma questão de Informática** (a07/s05, `DIREITA(PRI.MAIÚSCULA(A1);5)`): as alternativas "Silva/SILVA/silva" eram acusadas como
   repetidas pelo `--check` (que ignora maiúsculas). Foram substituídas por "Capit", "pitão", "ilva" e "Capitão", com o bloco gravado sob a trava do arquivo.

## Observação sobre `.txt` editados

Nenhuma questão antiga foi trocada. As duas intervenções diretas nos `.txt` foram sob a mesma trava usada pela ferramenta: inclusão de `item=` (item 5)
e substituição das alternativas da questão de PRI.MAIÚSCULA (item 6).
