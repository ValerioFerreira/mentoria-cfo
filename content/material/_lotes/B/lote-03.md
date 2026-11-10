# Lote 03 — Frente B (produção contínua)

Início: 2026-10-30

| Tipo | Volume | Título | Autor |
|---|---|---|---|
| NOVO | lingua-portuguesa/m11 | Interpretação de textos, tipologia, gêneros e variação linguística | AGENTE-MATB-09 |
| NOVO | direito-administrativo/m13 | Agentes públicos III | AGENTE-MATB-10 |
| NOVO | direito-processual-penal-militar/m01 | Lei processual penal militar, polícia judiciária militar e IPM | AGENTE-MATB-11 |
| NOVO | direitos-humanos/m01 | Teoria geral e afirmação histórica dos direitos humanos | AGENTE-MATB-12 |

Seleção: `material_ficha.py --lote 4 --frente B`. A primeira execução reservou lingua-portuguesa/m11 e direito-administrativo/m13 e quebrou (`mkdir` sem `parents`) porque a pasta da disciplina direito-processual-penal-militar não existia; as pastas das 24 disciplinas da fila foram criadas (vazias) e a seleção foi repetida: os três primeiros apareceram como RETOMAR por estarem reservados e vazios, e na verdade são NOVOS.
Sessão sem subagentes: o coordenador escreve os volumes um de cada vez, na ordem acima.



## Validação (4 volumes)

### lingua-portuguesa/m11 — 0 erro(s), 9 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a11/s01 | ALTA (96) | 2845/3275 | 9/8 | 9/6 | 0.54 | 0 | 17.2 | 0 |
| a11/s02 | ALTA (93) | 2537/2816 | 7/5 | 11/5 | 0.61 | 0 | 17.1 | 0 |
| a11/s03 | ALTA (95) | 3340/3222 | 7/6 | 13/6 | 0.54 | 0 | 19.0 | 2 |
| a11/s04 | ALTA (95) | 1615/1788 | 5/4 | 7/3 | 0.62 | 0 | 17.8 | 0 |
| a11/s05 | ALTA (97) | 2887/3040 | 8/7 | 11/6 | 0.55 | 0 | 17.8 | 0 |
| a12/s01 | ALTA (73) | 2027/2377 | 7/5 | 8/4 | 0.63 | 0 | 17.7 | 0 |
| a12/s02 | MEDIA (59) | 1685/1941 | 5/2 | 7/4 | 0.58 | 0 | 16.7 | 2 |

Fixação: 20 questões · AOCP 19 · inéditas do banco 0 · inéditas novas 0
- AVISO a11-s01.md: cobertura da fonte 0.54 (esperado ≥ 0.6); faltam: 903, 003, neve, sacode, paulao, microfone, lidiane, desligou, desistira, chat, pedro, eventos
- AVISO a11-s03.md: cobertura da fonte 0.54 (esperado ≥ 0.6); faltam: alcamos, runico, citados, chamavam, atacam, vigor, denotativas, consumidores, temido, ombros, medieval, irlandes
- AVISO a11-s04.md: item do edital cfoa:2 pouco presente no texto: “Tipologia e gêneros textuais”
- AVISO a11-s05.md: seção 'Tipos de questão de interpretação' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a11-s05.md: cobertura da fonte 0.55 (esperado ≥ 0.6); faltam: sabios, tentasse, depreender, cego, olho, vivas, romanas, replica, quadrado, profissoes, maleabilidade, insinuada
- AVISO a11-s05.md: item do edital cfoa:2 pouco presente no texto: “Tipologia e gêneros textuais”
- AVISO a12-s02.md: cobertura da fonte 0.58 (esperado ≥ 0.6); faltam: contaram, junta, irritou, foramos, estigmatizacao, cumulo, botequim, tida, tiro, dinheiro, verifica, oral
- AVISO tec_3212839: questão com figura (confira se o comentário não depende de vê-la)
- AVISO tec_3099009: questão com figura (confira se o comentário não depende de vê-la)

### direito-administrativo/m13 — 0 erro(s), 3 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a09/s12 | MEDIA (38) | 2684/3130 | 9/4 | 11/6 | 0.67 | 0 | 21.3 | 0 |
| a09/s13 | BASE (30) | 2577/2875 | 6/2 | 11/5 | 0.64 | 37 | 19.9 | 0 |
| a09/s14 | MEDIA (38) | 3017/3455 | 7/4 | 10/6 | 0.65 | 0 | 20.3 | 0 |
| a09/s15 | BASE (30) | 2291/2622 | 6/6 | 8/5 | 0.64 | 0 | 21.1 | 0 |
| a09/s16 | MEDIA (36) | 2581/2962 | 6/3 | 8/5 | 0.71 | 0 | 22.6 | 0 |

Fixação: 20 questões · AOCP 13 · inéditas do banco 7 · inéditas novas 0
- AVISO a09-s13.md: coincidência com a fonte (definição/norma? reescreva se puder): “as administrações tributárias da união dos estados do distrito federal e dos municípios” (13 palavras)
- AVISO a09-s13.md: coincidência com a fonte (definição/norma? reescreva se puder): “atividades essenciais ao funcionamento do estado exercidas por servidores de carreiras específicas” (12 palavras)
- AVISO a09-s13.md: coincidência com a fonte (definição/norma? reescreva se puder): “ix remuneração do trabalho noturno superior à do diurno xii salário família” (12 palavras)

### direito-processual-penal-militar/m01 — 0 erro(s), 13 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a00/s01 | ALTA (84) | 4425/4630 | 10/5 | 17/8 | 0.63 | 56 | 20.6 | 1 |
| a01/s01 | ALTA (84) | 2330/2458 | 5/3 | 7/5 | 0.6 | 0 | 19.2 | 0 |
| a02/s01 | MEDIA (62) | 2179/2373 | 7/3 | 8/4 | 0.6 | 22 | 19.3 | 0 |
| a02/s02 | ALTA (85) | 2232/2005 | 5/2 | 7/4 | 0.66 | 42 | 19.0 | 0 |

Fixação: 20 questões · AOCP 0 · inéditas do banco 20 · inéditas novas 0
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “o código de processo penal militar decreto lei 1 002 1969” (11 palavras)
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “se a infração atentar contra as instituições militares ou a segurança nacional” (12 palavras)
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “todos da ativa e do posto mais elevado da carreira” (10 palavras)
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “um juiz federal da justiça militar e um membro do ministério público militar” (13 palavras)
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “código de processo penal militar decreto lei 1 002 1969” (10 palavras)
- AVISO a01-s01.md: cobertura da fonte 0.60 (esperado ≥ 0.6); faltam: expedidos, alinho, neves, atender, gabinete, compreendidos, busquem, brigadas, ademais, 01, aeronautica, ilegal
- AVISO a02-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “segundo ou primeiro tenente se o indiciado for oficial e” (10 palavras)
- AVISO a02-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “apuração sumária de fato que configure crime militar e de sua autoria” (12 palavras)
- AVISO a02-s02.md: seção 'Como se colhem os depoimentos (art. 19)' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a02-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “ser prorrogado por mais vinte dias pelo comandante da região” (10 palavras)
- AVISO a02-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “nos casos de transgressão militar ou crime propriamente militar definidos em lei” (12 palavras)
- AVISO a02-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “a autoridade militar não pode mandar arquivar autos de inquérito” (10 palavras)
- AVISO a02-s02.md: coincidência com a fonte (definição/norma? reescreva se puder): “autoria já estiverem esclarecidos por documentos ou outras provas materiais” (10 palavras)

### direitos-humanos/m01 — 0 erro(s), 4 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a00/s01 | BASE (33) | 2102/2014 | 8/3 | 6/4 | 0.68 | 11 | 20.1 | 0 |
| a00/s02 | MEDIA (47) | 2868/3309 | 7/2 | 9/6 | 0.67 | 0 | 19.2 | 0 |
| a01/s01 | ALTA (92) | 2056/2159 | 5/3 | 5/4 | 0.67 | 0 | 22.2 | 0 |

Fixação: 20 questões · AOCP 6 · inéditas do banco 14 · inéditas novas 0
- AVISO a00-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “meios e instrumentos jurídicos para a defesa da dignidade das pessoas” (11 palavras)
- AVISO a01-s01.md: seção 'Limitação do poder político' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a01-s01.md: seção 'Direitos econômicos e sociais' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a01-s01.md: seção 'Primeira fase de internacionalização' com menos de 120 palavras: junte com outra ou desenvolva


## Notas dos autores

### lingua-portuguesa/m11 (AGENTE-MATB-09) — entregue em 30/10/2026
- 0 erros; 9 avisos, quase todos de cobertura da fonte (0,54 a 0,63): os termos que faltam são palavras isoladas e nomes próprios de enunciados de questões da fonte (neve, microfone, Lidiane, runas, Rubem Braga etc.).
- Os capítulos a11/s02 a a12/s02 foram escritos do zero com exemplos próprios. Nenhum trecho da fonte foi reproduzido; o validador acusou 0 palavras copiadas.
- O validador proíbe as palavras "professor", "pessoal,", "estratégia" e "a completar"; foram trocadas por "docente", "folha de servidores", "recurso" e "levar até".
- A tabela de operadores argumentativos (a11/s03) ganhou a linha "Escala (ênfase)" (até, inclusive, mesmo), porque a questão tec_3808120 trata do "até" como operador de escala.
- Fixação: 20 questões (19 AOCP e 1 SELECON). As questões com figura (tec_3212839 e tec_3099009) têm comentários que não dependem de ver a imagem. As com texto longo foram escolhidas só quando as alternativas permitem comentar sem o texto completo.

### direito-administrativo/m13 (AGENTE-MATB-10) — entregue em 30/10/2026
- 0 erros; 3 avisos de coincidência de 10 a 13 palavras com a fonte, em definição de norma (art. 37, XXII, e art. 7º, IX e XII).
- Pontos que o revisor deve conferir, por terem sido escritos de memória e a lei não estar no cache: (a) ADI 2.135 — o texto afirma que o STF validou, em 2024, a redação da EC 19/1998 e encerrou a obrigatoriedade do regime jurídico único, com modulação; (b) ADI 6.327 e o tema 1.072 (licença da mãe não gestante em união homoafetiva); (c) a prorrogação das licenças pelo Programa Empresa Cidadã e a omissão legislativa quanto à licença-paternidade; (d) os valores de pensão por morte da EC 103/2019 (50% mais 10% por dependente); (e) a redação do art. 37, XII, da CF.
- O capítulo a09/s16 usa as teses de 2025 listadas na fonte (Temas 1.164, 1.189, 1.388, 1.424 e 1.427, ADPF 1.095 e 1.132, ADI 3.228, STJ Tema 1.233), reescritas com palavras próprias.
- `check_citations.py` atribuiu a "Código Penal" citações de artigos da CF que vinham entre parênteses; as citações foram reescritas com "da Constituição" ao lado. A referência a "arts. 312 a 326" do CP também foi trocada por "artigos 312 a 326 desse Código".
- Fixação: 20 questões (13 AOCP e 7 inéditas MentorIA no capítulo s16, que não tem questão real). Foram evitadas as questões de aposentadoria compulsória aos 70 anos (desatualizadas pela LC 152/2015).

### direito-processual-penal-militar/m01 (AGENTE-MATB-11) — entregue em 30/10/2026
- 0 erros; 13 avisos, em geral de coincidência de 10 a 13 palavras em texto de artigo do CPPM (citação necessária) e de cobertura da fonte.
- Os artigos 1º a 28 e 243 a 253 do CPPM foram lidos do cache local de leis (`leis.py art cppm N`); o texto dos capítulos os resume com palavras próprias, com `[!lei]` apenas para os arts. 3º, 6º, 8º, a, 9º e 18.
- Pontos para o revisor conferir: (a) a Súmula 172, não usada aqui, e as Súmulas 53 e 78 do STJ, citadas de memória; (b) o HC 127.900 do STF (interrogatório ao final, também no processo penal militar); (c) a composição do STM e dos Conselhos de Justiça da JMU (art. 123 da CF e Lei 13.774/2018); (d) a observação de que o art. 17 (incomunicabilidade) é questionado pela doutrina quanto à recepção pela CF/88; (e) o prazo da detenção do art. 18 só é compatível com a CF no crime propriamente militar (art. 5º, LXI).
- Fixação: 20 questões, todas inéditas MentorIA já existentes no banco (não há questão real para o assunto). Duplicatas do banco (028, 031 e 066) foram evitadas, escolhendo a versão sem erro de enunciado.

### direitos-humanos/m01 (AGENTE-MATB-12) — entregue em 30/10/2026
- 0 erros; 4 avisos de seção curta (menos de 120 palavras) no capítulo a01/s01, onde cada marco histórico foi tratado em seção própria por clareza.
- O capítulo a00/s01 recebeu seções de características e de dimensões dos direitos humanos, porque seis das oito questões do banco para esse capítulo as cobram e a fonte as trata em outro lugar.
- Pontos para o revisor conferir: (a) a atribuição do conceito de período axial a Karl Jaspers; (b) as Cortes de Leão (1188), cujo conteúdo foi descrito de modo geral; (c) a fórmula de Radbruch e o caso Lüth (1958), citados de memória; (d) a data e a descrição do Habeas Corpus Act de 1679.
- Fixação: 20 questões (6 reais AOCP e 14 inéditas MentorIA, pois o banco não tem questão real da AOCP sobre fundamentos e história).

### Ferramentas e custo
- Sessão sem subagentes: os volumes foram escritos pelo próprio coordenador, um capítulo por vez, com validação a cada capítulo. O lote foi concluído em duas sessões (a primeira terminou depois de `lingua-portuguesa/m11/a11-s01`). Término: 2026-10-30.
- `validate_material.py --relatorio` sobrescreve o arquivo de saída; por isso o cabeçalho e as notas ficam guardados à parte e são montados no fim.
- Scripts auxiliares (fora do repositório): geração dos `fixacao.json` com conferência automática do gabarito, do capítulo e das letras contra o banco.
