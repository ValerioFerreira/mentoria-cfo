# Lote 10 — Frente B (produção contínua, onda 2)

Início: 2026-10-31 · Término: 2026-10-31

| Tipo | Volume | Título | Capítulos | Autor | Situação |
|---|---|---|---|---|---|
| NOVO | biologia/m04 | Evolução e biotecnologia | 4 | AGENTE-MATB-31 | concluído 31/10 |
| NOVO | direito-constitucional/m09 | Processo legislativo e Poder Executivo | 8 | AGENTE-MATB-32 | concluído 31/10 |
| NOVO | estatistica/m02 | Médias e moda | 8 | AGENTE-MATB-33 | concluído 31/10 |
| NOVO | fisica/m02 | Queda livre, lançamentos e movimento circular | 5 | AGENTE-MATB-34 | concluído 31/10 |

Seleção: `material_ficha.py --lote 4 --onda 2 --frente B` (uma única execução, depois do "Sim, onda 2" do usuário, porque a onda 1 estava esgotada para a frente B). Os quatro volumes foram reservados com `.frente` = B. A seleção devolveu quatro volumes NOVOS; nenhum devolvido.
Sessão sem subagentes: o coordenador escreveu os quatro volumes, um de cada vez. Todos ficaram em PRONTO_PARA_REVISAO. Os capítulos `c02` de biologia/m04 foram adaptados do complemento autoral `content/complements/bio-biotec-ambiente.md`, que é material do projeto.

## Validação (4 volumes)

### biologia/m04 — 0 erro(s), 1 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a04/s01 | BASE (14) | 1798/1739 | 6/2 | 5/3 | 0.75 | 0 | 16.1 | 0 |
| a04/s02 | BASE (14) | 1687/1894 | 7/4 | 5/4 | 0.7 | 0 | 17.4 | 0 |
| c02/s01 | ALTA (97) | 5751/5241 | 17/8 | 15/11 | — | 0 | 21.4 | 0 |
| c02/s02 | ALTA (82) | 1456/1498 | 4/2 | 6/3 | — | 0 | 19.7 | 0 |

Fixação: 12 questões · AOCP 12 · inéditas do banco 0 · inéditas novas 0
- AVISO a04-s01.md: tópico da fonte pouco presente no texto: “Introdução”

### direito-constitucional/m09 — 0 erro(s), 0 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a11/s01 | MEDIA (63) | 3665/4232 | 10/2 | 12/8 | 0.7 | 0 | 17.3 | 0 |
| a11/s02 | MEDIA (44) | 2833/3273 | 9/3 | 10/6 | 0.7 | 0 | 15.3 | 0 |
| a11/s03 | MEDIA (44) | 2811/3157 | 6/4 | 8/6 | 0.68 | 0 | 16.6 | 0 |
| a11/s04 | MEDIA (35) | 2369/2775 | 7/2 | 7/5 | 0.74 | 0 | 21.2 | 0 |
| a11/s05 | MEDIA (60) | 3086/3535 | 9/3 | 8/6 | 0.74 | 0 | 17.8 | 0 |
| a12/s01 | ALTA (70) | 2678/3111 | 8/4 | 9/6 | 0.68 | 0 | 17.6 | 0 |
| a12/s02 | MEDIA (52) | 2117/2372 | 6/2 | 6/4 | 0.72 | 0 | 18.7 | 0 |
| a12/s03 | ALTA (79) | 3323/3819 | 9/6 | 8/7 | 0.64 | 0 | 16.5 | 0 |

Fixação: 20 questões · AOCP 20 · inéditas do banco 0 · inéditas novas 0

### estatistica/m02 — 0 erro(s), 26 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a01/s01 | MEDIA (62) | 1790/2050 | 6/5 | 5/4 | 0.61 | 0 | 15.3 | 0 |
| a01/s02 | ALTA (74) | 2009/2139 | 5/5 | 7/4 | 0.56 | 10 | 15.6 | 0 |
| a01/s03 | MEDIA (66) | 1886/2046 | 6/5 | 8/4 | 0.54 | 0 | 18.4 | 0 |
| a01/s04 | MEDIA (57) | 1834/1914 | 4/4 | 7/4 | 0.51 | 0 | 17.2 | 0 |
| a01/s05 | MEDIA (53) | 1762/1701 | 4/4 | 8/3 | 0.65 | 0 | 17.5 | 0 |
| a03/s01 | ALTA (71) | 1658/1694 | 5/4 | 7/3 | 0.52 | 11 | 15.5 | 0 |
| a03/s02 | ALTA (85) | 1823/1754 | 6/4 | 6/3 | 0.54 | 0 | 18.7 | 0 |
| a03/s03 | ALTA (77) | 1648/1449 | 5/3 | 6/3 | 0.55 | 0 | 18.2 | 0 |

Fixação: 20 questões · AOCP 3 · inéditas do banco 7 · inéditas novas 0
- AVISO a01-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “a soma dos desvios em relação à média é sempre” (10 palavras)
- AVISO a01-s02.md: cobertura da fonte 0.56 (esperado ≥ 0.6); faltam: paraguaios, 57300, xquim, xmat, 70400, 17600, 27300, 19000, 11000, tomar, quociente, satisfaz
- AVISO a01-s02.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”
- AVISO a01-s03.md: seção 'Que média usar' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a01-s03.md: cobertura da fonte 0.54 (esperado ≥ 0.6); faltam: 060, tributaria, tributario, municipio, fabs, conseguiram, ascendente, lingua, brutos, administrativo, venda, transportadas
- AVISO a01-s03.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a01-s03.md: item do edital geral:3.2 pouco presente no texto: “Medidas de tendência central (médias, moda e mediana)”
- AVISO a01-s03.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”
- AVISO a01-s04.md: cobertura da fonte 0.51 (esperado ≥ 0.6); faltam: 8000, 075, 235, primo, lembram, somaremos, monteiro, 1700, matematica, voces, divisor, repare
- AVISO a01-s04.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a01-s04.md: item do edital geral:3.2 pouco presente no texto: “Medidas de tendência central (médias, moda e mediana)”
- AVISO a01-s04.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”
- AVISO a01-s05.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a01-s05.md: item do edital geral:3.2 pouco presente no texto: “Medidas de tendência central (médias, moda e mediana)”
- AVISO a01-s05.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”
- AVISO a03-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “moda para dados agrupados sem intervalos de classe quando os dados” (11 palavras)
- AVISO a03-s01.md: cobertura da fonte 0.52 (esperado ≥ 0.6); faltam: 75kg, 69kg, 60kg, 55kg, drogas, lsup, aprenderemos, 380, possuir, 48, linf, evidencia
- AVISO a03-s01.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a03-s02.md: seção 'Uma tabela para estudar os dois métodos' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s02.md: cobertura da fonte 0.54 (esperado ≥ 0.6); faltam: 220, 5060, 3040, 2030, 4050, 1020, 880, 1640, 80, 200, medios, salarios
- AVISO a03-s02.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a03-s02.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”
- AVISO a03-s03.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s03.md: cobertura da fonte 0.55 (esperado ≥ 0.6); faltam: dfmodfant, 74, adjacentes, 1020, 5560, 3555, 2035, etaria, linf, dfmodfpost, 6070, reparem
- AVISO a03-s03.md: item do edital geral:MAT-3 pouco presente no texto: “Matemática 3 — estatística e probabilidade (representação de dados, média/moda/mediana, de”
- AVISO a03-s03.md: item do edital pcpe:1 pouco presente no texto: “Estatística descritiva e análise exploratória de dados: gráficos, diagramas, tabelas, medi”

### fisica/m02 — 0 erro(s), 14 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a03/s01 | ALTA (70) | 1583/1514 | 5/3 | 6/3 | 0.55 | 0 | 20.2 | 0 |
| a03/s02 | MEDIA (39) | 1141/900 | 3/2 | 5/2 | 0.71 | 0 | 20.8 | 0 |
| a03/s03 | ALTA (76) | 1185/1202 | 4/3 | 4/3 | 0.61 | 0 | 18.6 | 0 |
| a04/s01 | ALTA (85) | 1889/2081 | 6/5 | 7/4 | 0.61 | 0 | 18.2 | 0 |
| a04/s02 | ALTA (85) | 1672/1810 | 4/4 | 8/4 | 0.59 | 0 | 17.9 | 0 |

Fixação: 15 questões · AOCP 8 · inéditas do banco 7 · inéditas novas 0
- AVISO a03-s01.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s01.md: cobertura da fonte 0.55 (esperado ≥ 0.6); faltam: tijolo, cinematica, ultimo, algumas, matematico, primeiro, 03, causas, horaria, estudo, presentes, vistas
- AVISO a03-s01.md: item do edital geral:2.4 pouco presente no texto: “Casos especiais de movimentos e suas regularidades”
- AVISO a03-s02.md: 1141 palavras: acima da faixa (1080); confira se não há repetição
- AVISO a03-s02.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s02.md: item do edital geral:2.4 pouco presente no texto: “Casos especiais de movimentos e suas regularidades”
- AVISO a03-s03.md: seção 'Uma ideia antiga e a ideia moderna' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s03.md: seção 'Decomposição da velocidade' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s03.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a03-s03.md: item do edital geral:2.4 pouco presente no texto: “Casos especiais de movimentos e suas regularidades”
- AVISO a04-s01.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a04-s02.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a04-s02.md: cobertura da fonte 0.59 (esperado ≥ 0.6); faltam: rapidez, 98, fabrica, dentadas, espacos, diametro, espaco, desgastado, acoplada, descobrir, 100km, perseguido
- AVISO a04-s02.md: item do edital geral:2.4 pouco presente no texto: “Casos especiais de movimentos e suas regularidades”

### Notas dos autores

### biologia/m04 (AGENTE-MATB-31)
- 0 erros; 1 aviso (tópico "Introdução" da fonte, que é uma saudação sem conteúdo). Os capítulos 3 e 4 (`c02-s01` e `c02-s02`) vêm do complemento autoral do projeto, adaptados ao formato (abertura, objetivos, seções sem numeração, mapa e "Para fixar", quadros com tipos corretos).
- Pontos para o revisor conferir: (1) o Planalto bloqueou a consulta automática em 31/10 ("Acesso Negado") e a Câmara retornou 404, então os artigos da Lei 11.105/2005 (arts. 5º, 6º, 11, 24 a 26 e 40), da Lei 9.433/1997 (arts. 1º, 5º, 12, 15 e 33), do Código Florestal (arts. 4º, 12, 15 e 29), do SNUC (arts. 8º e 14) e da Lei 11.445/2007 com a Lei 14.026/2020 (art. 11-B, metas de 2033) foram mantidos como no complemento, que foi verificado em 08/10/2026; (2) o valor das multas da Lei de Biossegurança está no regulamento (Decreto 5.591/2005), e o texto o diz assim; (3) as datas geológicas e as de fósseis humanos do capítulo 2 são arredondadas e em alguns pontos diferem da fonte-base (origem dos mamíferos, primeiras formas de vida, chegada à América); (4) o capítulo 1 foi escrito do conhecimento didático padrão e do resumo próprio, sem fonte externa aberta.
- Fixação: 12 questões AOCP do banco (3 por capítulo). Descartadas as de taxonomia, deriva genética, reuso de água e estação de tratamento, que o volume não desenvolve; a tec_3554827 (especiação) está classificada no capítulo 1 no banco, mas o conteúdo está no capítulo 2.

### direito-constitucional/m09 (AGENTE-MATB-32)
- 0 erros; 0 avisos. Artigos conferidos com `pipeline/leis.py art cf N` (arts. 14, 50 a 52, 56 a 69, 77 a 91, 102, 165 e 166) e `check_citations.py` sem citação inexistente. A redação atual dos arts. 82 (mandato de 4 anos, posse em 5 de janeiro, EC 111/2021) e 166 (emendas individuais de 2% da RCL, 1,55% para deputados e 0,45% para senadores, EC 126/2022) foi conferida no cache; as provas ainda citam os 1,2% da EC 86/2015, e o texto traz os dois.
- Pontos para o revisor conferir: (1) decisões do STF citadas de memória, sem consulta ao tribunal: Tema 917 (iniciativa e despesa), ADPF 402 (réu em ação penal e linha sucessória), ADI 939 (anterioridade como cláusula pétrea), ADI 3.367 (PEC paralela), ADPF 132 e ADI 4.277 (mutação), SV 46 (crimes de responsabilidade) e a Súmula 5, descrita como superada; (2) prazos do ADCT, art. 35, § 2º, para PPA, LDO e LOA; (3) a Resolução 1/2002-CN (promulgação da lei de conversão de MP aprovada sem alteração pelo Presidente da Mesa do Congresso); (4) a exigência de autorização da Câmara para processar Ministros de Estado (art. 51, I) foi descrita segundo a leitura que a restringe aos crimes conexos com os do Presidente; (5) a admissão de MP estadual pelo STF (ADI 425).
- Fixação: 20 questões do banco (19 AOCP). Descartada a tec_3526863, porque a alternativa A trata como pacífica a MP municipal, que é controvertida.

### estatistica/m02 (AGENTE-MATB-33)
- 0 erros; 26 avisos (cobertura de termos entre 0,51 e 0,65, porque os exemplos específicos da fonte foram substituídos por exemplos próprios; seções curtas; itens do edital pouco presentes em palavras exatas). Todos os cálculos de exemplos e resolvidos foram refeitos em Python.
- Pontos para o revisor conferir: (1) a mediana só aparece na fórmula de Pearson, com interpolação; (2) o volume usa a notação "⊢" para classes (limite inferior incluído e superior excluído), porque a barra vertical quebra as tabelas do formato; (3) a Fixação tem poucas questões AOCP (3 em 20), pois o banco só tem 7 AOCP nesses assuntos; as demais são de outras bancas ou inéditas MentorIA já existentes.
- Fixação: 20 questões (3 AOCP, 10 de outras bancas, 7 inéditas do banco).

### fisica/m02 (AGENTE-MATB-34)
- 0 erros; 14 avisos (seções curtas; capítulo 2 com 1141 palavras para meta de 900; cobertura entre 0,55 e 0,71). g = 10 m/s² e π = 3,14 nos exemplos.
- Pontos para o revisor conferir: (1) a tec_1387526 usa g = 9,8 m/s² e é ambígua quanto ao nível de retorno; o comentário adota 1 m acima do lançamento, que reproduz o gabarito (2,99 s); (2) a tec_1407970 trata de encontros em movimento circular em sentidos opostos, que o capítulo só toca de leve; (3) a tec_717692 (Aristóteles) foi acomodada com um parágrafo no capítulo 2.
- Fixação: 15 questões (8 AOCP, 7 inéditas do banco).

### Ferramentas e custo
- Sessão sem subagentes; capítulos escritos um a um, com validação a cada capítulo e correções em seguida.
- Scripts auxiliares (fora do repositório, no scratchpad): `mk_bio_c02.py` e `mk_bio_c3.py` (conversão do complemento autoral em capítulos), `fix_bio04.py`, `fix_dc09.py`, `fix_est02.py` e `fix_fis02.py` (geram os `fixacao.json`).
- Ferramentas com problema: o `firecrawl_scrape` do Planalto retornou "Acesso Negado" e o da Câmara, 404; `leis.py art cf N` aceita um artigo por chamada; o cache da Constituição traz o texto revogado junto do vigente, e foi preciso separar a redação atual.
- O validador mede a cobertura por tokens exatos da fonte (inclusive números e abreviaturas como "fmo" e "fant"); subir a cobertura exigiu reintroduzir termos de domínio.
- Nenhum arquivo `.frente` foi apagado ou editado; nenhum volume reservado por A ou C foi tocado; nada foi commitado nem gravado no banco.
- Este foi o oitavo lote de frente B da sessão (lotes 03 a 10); o lote 10 foi autorizado pelo usuário com "Sim, onda 2".
