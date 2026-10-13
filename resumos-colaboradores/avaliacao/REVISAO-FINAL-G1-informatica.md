# Revisão final G1 — Informática

Estado final (validador): 16 arquivos (`a00` a `a14` e `c01`) com **0 erros**. Antes: 66 erros de "Para fixar" (parágrafo corrido) + 1 trecho sem "Para fixar" (`a06/s12`).
Cobertura (summary_coverage.py): antes REFAÇÃO 2, REVISAR 12, ATENÇÃO 17; depois REFAÇÃO 0, REVISAR 10, ATENÇÃO 13. O veredito é relativo ao conjunto da disciplina: ao reescrever os piores, trechos antes ATENÇÃO subiram de categoria.

## A) "Para fixar"
Todos os 66 fechamentos viraram lista de 5 a 8 itens, tirados do próprio resumo (a00/s01-s05, a01/s02, a02/s01-s06, a03/s01-s07, a04/s01, a06/s01,s05,s08,s09, a07/s01-s04, a08/s01,s03,s04, a09/s01-s04, a10/s02, a11/s01, a12/s01-s15, a13/s01-s04, a14/s01-s10). Em `a06/s12` o fechamento foi criado. Fórmulas em LaTeX removidas (a02/s03, a07/s03, a07/s04, a14/s01, a14/s02, a14/s06), trocadas por texto simples. Nenhuma alteração de conteúdo além disso nesses trechos.

## B) Trechos reescritos por completo (leitura contra o texto-fonte)
Cobertura antes -> depois (nota):
- a14/s01 (S0220) REVISAR 0,28 -> OK 0,48. Faltava Von Neumann (5 componentes), tabela de bases e as conversões com exemplos; tirei barramentos, que o trecho não ensina.
- a12/s01 (S0250) REVISAR 0,31 -> OK 0,72. Faltavam novidades do Windows 11, kernel, drivers e edições Home x Pro.
- a03/s01 (S0243) REVISAR 0,34 -> OK 0,72. Acrescentados formas de infecção, prevenção, terminologia completa e vírus (3 partes, 4 fases, mito da imunidade).
- a12/s02 (S0214) REFAÇÃO 0,34 -> OK 0,58. Atalhos (.lnk), temas de contraste, personalização, barra de tarefas e widgets.
- a08/s01 (S0187) REVISAR 0,34 -> OK 0,59. Novidades do Word 2010, 2013 e 2016 (antes só 3 de cada).
- a12/s11 (S0241) REVISAR 0,36 -> OK 0,65. Oito modos de exibição, comandos (xcopy, tree, deltree), limites de caminho, limites da pesquisa.
- a02/s04 (S0213) REVISAR 0,36 -> OK 0,64. Tabela de algoritmos, OTP/TOTP/HOTP, tokens, 2FA x MFA x autenticação forte.
- a13/s01 (S0176) REFAÇÃO 0,37 -> OK 0,53. Escalabilidade x elasticidade, autosserviço x elasticidade, CPD, NIST (5/3/4).
- a14/s06 (S0190) REVISAR 0,38 -> OK 0,57. RISC x CISC, clock/overclock, palavra 32/64 bits, ciclo da UC em 4 etapas (o resumo anterior tinha 3).
- a03/s07 (S0216) REVISAR 0,39 -> OK 0,69. Hoax, MITM, defacement, SQL injection, furto de identidade e variações do golpe de antecipação.
- a13/s03 (S0237) REVISAR 0,40 -> OK 0,62. Cotas gratuitas, anos, recursos de cada serviço, Azure. Corrigido erro: o resumo anterior dizia "criptografia de ponta a ponta" no Google Drive (o trecho fala de criptografia em trânsito e armazenado).
- a14/s07 (S0246) REVISAR 0,40 -> OK 0,62. Primária x secundária x principal, SIMM x DIMM, DRAM/SDR/DDR com tabela, SRAM.
- a03/s05 (S0215) REVISAR 0,40 -> OK 0,54. Detalhes de força bruta, DoS, spoofing e termos vizinhos.
- a12/s09 (S0235) REVISAR 0,40 -> OK 0,63. Seções de Personalização, Aplicativos e Contas.
- Complementares: a12/s03 (S0226) 0,39 REFAÇÃO -> OK 0,50; a12/s08 (S0234) 0,40 REFAÇÃO -> OK 0,78 (corrigido: modos de energia são Equilibrado, Economia de energia e Desempenho máximo; o resumo anterior citava outros nomes); a14/s02 (S0205) 0,40 REFAÇÃO -> OK 0,60 (corrigido: ABNT e ABNT2 ambos têm Ç; a diferença é a tecla Alt Gr).

## C) Entregas rejeitadas
`summary_queue.py --pending --subject informatica` retorna 0: os trechos rejeitados na importação (a01/s02, a03/s03-s04, a06/s05,s09,s12 etc., pelo "Para fixar") já estão no content e foram corrigidos em A. Os `.md` em `resumos-colaboradores/entregas/` desses IDs continuam com o fechamento antigo; não os alterei (o content é a versão válida). Se a importação for repetida a partir deles, os trechos serão rejeitados de novo.

## D) Pendências (não tratadas)
Ainda em REVISAR, sem erros de validação e com texto de 450 a 800 palavras sobre alvos maiores (a nota é relativa): a06/s01, a00/s01, a02/s05, a12/s10, a03/s06, a14/s04, a12/s07, a12/s05, a12/s12, a02/s02. Em ATENÇÃO: a02/s03, a02/s01, a00/s04, a06/s11, a14/s08, a03/s02, a06/s08, a12/s14, a04/s01, a03/s04. Muitos trechos pequenos (a06, a07, a08, a09, a12) estão abaixo de 45% do alvo, com avisos de tamanho; o conteúdo cobre o essencial, mas pode ser ampliado.

## Dúvidas para revisão humana
1. a12/s01: o material dá duas datas para o Windows 11 (outubro de 2021 na p. 10 e junho de 2021 na p. 11); o resumo cita "2021" com as duas menções. Também cita 2 TB de RAM e dois processadores no Pro (texto do material).
2. a14/s06: o material diz que "a IBM criou o primeiro microprocessador (Intel 4004)"; o resumo atribui o 4004 à Intel (sem citar IBM). A tabela de modelos Intel e clocks do material é antiga e foi só listada.
3. a12/s11: o material lista os nomes reservados como "COM, PRN, AUX, NUL" (provável erro de digitação de CON); o resumo usa CON, PRN, AUX, NUL, COM1-9, LPT1-9.
4. a02/s04: nota técnica do material diz que "autenticação forte" exige fatores de categorias diferentes e a "MFA" poderia aceitar a mesma categoria; as bancas tratam como sinônimos. O resumo traz os dois lados (a versão anterior afirmava que MFA exige categorias distintas). Conferir se isso conflita com a diretriz do edital AOCP.
5. a13/s03: no material, o plano pago do OneDrive aparece como 1 TB no texto e "a partir de 100 GB" na tabela; o resumo registra os dois. Valores de cotas e planos mudam com o tempo.
6. a13/s01: o exemplo de preço do Office 365 (cerca de R$ 30) está datado; o produto hoje se chama Microsoft 365.
7. a12/s03: o material diz que a Cortana foi descontinuada em 2020 e o Copilot lançado em 2023; o resumo evita a data da Cortana. Atalhos Win + Ctrl + D, Win + A, Win + N e Win + número (a12/s03) foram mantidos de resumos anteriores e não constam do trecho; são corretos no Windows 11, mas vale conferir.
8. a12/s08: "retornar à versão anterior em 10 dias" segue o material; o prazo real pode variar (padrão de 10 dias, extensível até 60 por comando).
9. a14/s07 e a14/s06: dados de DDR (tensão, frequências) vêm de tabela do material, não revisados contra especificação oficial.
10. Figuras não reconstruídas: diagramas de organização das memórias (a14/s07, reconstruído como tabela a partir do texto), logo e imagens de teclado (a14/s02), tabela de comparação do layout do Windows. Resumos de a00 a a11 e os trechos não listados acima foram revisados só quanto a estrutura, LaTeX e "Para fixar", não quanto à exatidão do conteúdo.
