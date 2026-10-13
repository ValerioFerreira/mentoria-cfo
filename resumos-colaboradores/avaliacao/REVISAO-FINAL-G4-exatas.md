# Revisão final G4 — Física, Matemática e Química

Escopo: `content/summaries/fisica`, `matematica`, `quimica` (65 arquivos). Nenhum comando git, seed, apply_synthetic ou gravação de importação foi executado.

## Resultado do validador
- Antes: 17 arquivos com ERRO (16 trechos de Física, 8 de Matemática, todos por "Para fixar" fora de 5–8 itens) + S0575 fora do content.
- Depois: **65 arquivos, 0 erros**. Dry-run de importação de S0575, S0651 e S0568: 3 válidos, 0 rejeitados.
- O validador atual calcula a cobertura por ranking: sempre há um "pior grupo". Os trechos listados abaixo como ainda REVISAR/REFAÇÃO têm lista de "faltam" dominada por ruído (palavras de enunciados, números de exercícios, símbolos).

## A) Para fixar (5 a 8 itens, tirados do próprio resumo)
Física: a00/s01, a00/s02, a02/s02, a03/s03, a04/s01, a04/s02, a06/s02, a07/s02, a08/s02, a09/s01, a13/s04 (13 itens), a14/s01, a14/s02, a17/s01, c01/s01, c02/s01.
Matemática: a01/s01, a06/s01, a13/s03, a17/s06, a17/s10, a17/s12 (parágrafo para lista); a13/s02 (15 itens) e a17/s04 (14 itens) consolidados. Também corrigido o erro de grafia "cosssec" em a17/s04.

## C) Entrega rejeitada
- **S0575 (fisica/a01/s01)**: o .md foi refeito em `resumos-colaboradores/entregas/resumos_EXT-L5_L5-01/S0575__EXT-L5.md` (Para fixar com 8; tabelas; resolução completa da questão dos relógios dessincronizados; sintético com 9 pontos). Passa no dry-run. **O orquestrador precisa rodar a importação real**, pois o trecho ainda aparece em `summary_queue --pending`.

## B) Conteúdo (acréscimos de cobráveis, correções, tabelas, sintético no formato "**Ponto**: explicação")
Reescritos/refeitos: **S0651 quimica/a08/s02** (de 446 palavras para ~1.100: 9 métodos que faltavam, quadro dos métodos, questões; .md atualizado), **S0568 quimica/c01/s01** (reestruturado com tabelas: monômeros, classes ONU, limites de dose 20/1 mSv, Portaria 888/2021; .md atualizado), fisica/a05/s01 (S0621: removido "impulso", pegadinha do cinto = 1ª lei, quatro condições do par ação-reação, inércia de repouso/movimento), fisica/a12/s01 (S0639: calor específico, não capacidade térmica; brisa terrestre; quadro dos processos; tabela vazia reconstruída).
Com seção acrescentada (e sintético reformatado quando necessário): 
- Física: a04/s01, a05/s03, a06/s02, a08/s01, a13/s04, a01/s02.
- Matemática: a01/s03, a05/s01, a05/s03, a06/s03, a08/s02, a11/s02, a17/s09, a17/s11.
- Química: a00/s01, a00/s03, a00/s04, a01/s03, a02/s01, a03/s01, a03/s02, a03/s03, a04/s02, a05/s02, a07/s01, a07/s02, a07/s03, a08/s01, a10/s02, a10/s04, a16/s02.

Erros de conteúdo encontrados e corrigidos nos resumos anteriores: TNG a07/s02 ("12 mol → 268,8 L" para 1 mol; correto 67,2 L); maré a17/s11 (a curva começa no mínimo, não no máximo); imaginário puro exige b = 0 (a08/s02); "Em ambos, verifique se Z coincide" em isóbaros/isótonos (a01/s03); capacidade térmica × calor específico.

## Vereditos antes → depois (cobertura)
REFAÇÃO → OK: fisica a04/s01 (0,38→0,55). REFAÇÃO/REVISAR do CSV que saíram da lista do validador após o trabalho: fisica a08/s01, a06/s02, a13/s04, a05/s03; matematica a01/s03, a05/s01, a05/s03, a06/s03, a08/s02, a11/s02; quimica a00/s01, a00/s04, a01/s03, a02/s01, a03/s02, a03/s03, a05/s02, a07/s01–s03, a08/s02, a10/s02, a16/s02, a04/s02, a08/s01, a10/s04.
Ainda marcados (ruído; conteúdo conferido contra a fonte): fisica a02/s01, a06/s01, a11/s01, a13/s01; matematica a04/s01, a08/s03, a13/s01, a14/s03, a15/s02 (resumo completo: o texto-fonte é quase só exercícios com nomes e números), a17/s07, a17/s09, a17/s11; quimica a02/s03, a03/s01, a04/s01, a06/s01, a12/s02, a14/s01, a17/s02, a18/s03.

## Pendências
- Importação real de S0575; depois `apply_synthetic.py` e seed (por conta do orquestrador).
- Não revisados a fundo (só validados): fisica a01/s02 além do acréscimo, a02/s01, a06/s01, a11/s01, a13/s01; matemática a04/s01, a08/s03, a13/s01, a14/s03, a17/s07; química a06/s01, a12/s02, a14/s01, a17/s02, a18/s03 (a17/s02 tem fonte de ~1.000 linhas).
- Os .md em `entregas/` só foram atualizados para S0575, S0651 e S0568; nos demais o JSON em `content/summaries` é a versão corrigida (uma reimportação dos .md antigos a sobrescreveria).

## Dúvidas para revisão humana
1. **Fisica a01/s01**: a resolução da questão do posto policial estava truncada na fonte; o resumo completa a conta (Δt = 53 min 30 s, 156 km, ≈175 km/h acima de 110 km/h) e sugere resposta à pergunta final sobre medir a velocidade do suspeito (velocidade relativa) em a04/s01. Conferir no PDF.
2. **Matemática a05/s03**: o material diz que +10%, +11% e +12% dão 139,22 (+39,2%), mas 1,10·1,11·1,12 = 1,3675 (+36,75%). Exemplo omitido do resumo.
3. **Matemática a11/s02**: na questão do gráfico (a < 0, b > 0) o material marca alternativa com a > 0 e b < 0; o resumo não reproduz o gabarito.
4. **Química a02/s01**: o material usa ↑ = ms −1/2 (convenção inversa à usual); respostas de números quânticos do C e do O dependem disso.
5. **Química a10/s02**: densidade do H₂SO₄ 1,98 g/mL no material (usual 1,84, citado em outra aula); mufla "acima de 1.000 °C" × "perto de 2.000 °C".
6. **Química a10/s04**: o material calcula pH 11,98 e 11,77 (valores exatos 12,00 e 11,78) com log(0,06) no lugar de log(0,006); o resumo traz os valores corrigidos.
7. **Química a01/s03**: massa do cloro 35,45 u (tabela) × 35,49 u calculado com 75,4%/24,6%.
8. **Química a00/s01**: "radônio (Rb)" no material; correto Rn. **a03/s03**: rótulo "7 Cr³⁺" no material (correto 2 Cr³⁺). **a16/s02**: "sp2" no resumo final do carbono sp (correto sp).
9. **Química a04/s02**: material cita haletos "AgCl₃, AgBr₃, AgI₃, FeBr₃" como exceção covalente (fórmulas duvidosas).
10. **Física a12/s01**: o vácuo (e não só o ar aprisionado) é o principal isolante da garrafa térmica; incluído como conhecimento externo, entre parênteses. A tabela final do material estava vazia; o quadro comparativo foi reconstruído a partir do texto.
11. **Física a05/s03 / Química a07/s02**: valores de tabelas de coeficientes de atrito e densidades não extraídos; o resumo usa só os valores dos exemplos.
12. **S0568 (c01)**: limites de dose (20 mSv/ano, 1 mSv/ano) e Portaria 888/2021 vêm do próprio complemento autoral; conferir com a norma atual.
13. Física a04/s01: "aplicação policial" (medir a velocidade do suspeito pela velocidade relativa) é dedução do agente, pois o final do trecho estava cortado.
