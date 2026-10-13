# Avaliação amostral — agentes EXT-L2 e EXT-L3

Data: 2026-10-12. Padrão de referência: `resumos-colaboradores/INSTRUCOES.md`. Método: cada resumo foi lido inteiro e conferido, ponto a ponto, contra o texto-fonte (`summary_source.py <trecho>`) e contra conhecimento técnico quando a fonte estava errada ou cortada (indicado em cada caso). Foram rodados também uma contagem de palavras, uma busca por expressões proibidas e uma comparação de sequências de 5 palavras com a fonte (apoio, não substitui a leitura). Escala: 1 a 5 (5 = excelente).

Limite da amostra: a amostra sorteada de EXT-L2 só tem Informática (nada de Língua Inglesa) e a de EXT-L3 só tem Língua Portuguesa (nada de Biologia). As conclusões valem para essas matérias; Inglês e Biologia não foram avaliados.

Resultado do `verificar_resumos.py` nas pastas: tudo passa (0 erros). Ele só confere presença de `### Para fixar`, não se é lista de 5 a 8 pontos; por isso os problemas abaixo de formato e conteúdo não aparecem nele.

---

## (a) Quadro por agente

### EXT-L3 (amostra: Língua Portuguesa, sublote L3-01)

| ID | Cobertura | Correção | Originalidade | Clareza/didática | Tamanho/formato | Ação |
| --- | --- | --- | --- | --- | --- | --- |
| S0033 | 3 | 3 | 4 | 3 | 4 | Correção pontual + complemento |
| S0041 | 3 | 3 | 4 | 3 | 4 | Correção pontual + complemento |
| S0048 | 3 | 4 | 4 | 3 | 4 | Correção pontual + complemento |
| S0057 | 3 | 3 | 4 | 2 | 2 | REFAÇÃO |
| S0062 | 2 | 3 | 4 | 2 | 2 | REFAÇÃO |
| **Média** | **2,8** | **3,2** | **4,0** | **2,6** | **3,2** | |

**Veredito EXT-L3: REPROVAR LOTE (L3-01), com devolução para complementação/refação.** Justificativa: cobertura (2,8) e clareza (2,6) abaixo de 3; 2 dos 5 resumos exigem refação completa (S0057 e S0062) e os outros 3 têm omissões de itens que a banca cobra e pelo menos um erro de fato cada. Originalidade é boa (4,0). Como os 20 resumos do sublote foram escritos com o mesmo método (700 a 900 palavras para trechos de 12 a 16 páginas, alvo de 1800 a 2000), é provável que o problema se repita nos outros 15. Recomendo devolver o sublote inteiro com uma lista de "assuntos obrigatórios" por ID, em vez de só corrigir os 5 amostrados. Biologia não foi amostrada: avaliar à parte.

### EXT-L2 (amostra: Informática, sublotes L2-01 e L2-02)

| ID | Cobertura | Correção | Originalidade | Clareza/didática | Tamanho/formato | Ação |
| --- | --- | --- | --- | --- | --- | --- |
| S0098 | 3 | 4 | 4 | 3 | 4 | Correção pontual + complemento |
| S0102 | 3 | 4 | 4 | 3 | 3 | Correção pontual + complemento |
| S0110 | 3 | 4 | 4 | 3 | 4 | Correção pontual + complemento |
| S0125 | 3 | 4 | 4 | 4 | 4 | Correção pontual + complemento |
| S0137 | 3 | 4 | 4 | 3 | 3 | Correção pontual + complemento |
| **Média** | **3,0** | **4,0** | **4,0** | **3,2** | **3,6** | |

**Veredito EXT-L2: APROVADO COM RESSALVAS.** Justificativa: nenhum erro grave de conceito nos 5 resumos e originalidade boa; o defeito é cobertura (3,0): em todos os 5 faltam itens cobráveis que estão na fonte (atalhos, tipos de gráfico, tabelas de comandos) e o trecho de maior incidência em prova (S0137, "ALTÍSSIMA") foi o que ficou mais enxuto. Nenhum precisa de refação; cada um precisa de um complemento localizado (lista em (b)). Condição para aprovar o restante: aplicar os complementos e conferir os atalhos listados em (d). Inglês não foi amostrado: avaliar à parte.

---

## (b) Por resumo

Legenda de ação: REFAÇÃO = reescrever; CORREÇÃO PONTUAL = editar/acrescentar itens, sem reescrever.

### S0033 (EXT-L3, Língua Portuguesa, a05/s06, "que", "se", "como") — 3 / 3 / 4 / 3 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Na seção do QUE, as conjunções ficam incompletas: faltam a alternativa ("Que chova, que faça sol"), a aditiva ("fala que fala"), a concessiva ("pouco que seja") e a temporal ("Agora que eu ia viajar"), todas listadas na fonte (págs. 69 e 70). O resumo só traz causal/explicativa, consecutiva, comparativa, final e adversativa.
- Faltam o SE conjunção causal (equivale a "já que"; fonte pág. 77) e a distinção "expletivo com rir/sorrir" que a fonte diz ser muito cobrada.
- A maior lacuna: os critérios para separar SE apassivador, reflexivo e parte integrante do verbo (págs. 78 e 79: sentido passivo exige agente externo; verbo pronominal costuma ser VTI ou intransitivo; reflexivo exige sujeito que pratica a ação em si mesmo; "só há dúvida passiva × reflexiva se o sujeito pode agir sobre si; ambiguidade contextual"). O resumo só traz a "pegadinha" PA × PIS, que a fonte não destaca; os critérios que a fonte dedica quase 2 páginas ficaram de fora.
- Falta a observação, cobrada em questão (PRF 2019, pág. 74 a 75), de que o sujeito do verbo da oração adjetiva é o próprio pronome relativo ("os processos... que nos cercam": o sujeito de "cercam" é o "que", não "os processos"). O método dos 3 passos está lá, mas sem essa armadilha.
- Faltam "como" interjeição e o verbo "como"; e a função de adjunto adverbial de modo/oração substantiva justaposta.

Correção:
- "Vêem-se falhas" (pegadinha, linha 57 do arquivo): com o Acordo Ortográfico de 2009 a forma é "veem-se" (sem circunflexo). Erro de grafia numa matéria de Língua Portuguesa.
- "Fiz sinal que entrassem" é dado como exemplo de conjunção final. Pela análise do próprio resumo ("substituível por ISTO") seria integrante, oração objetiva direta; a fonte usa como exemplo de final "Estudo para que meu filho tenha uma vida melhor" e "Faço votos que sejas feliz". Exemplo duvidoso, trocar.
- Tabela do SE: o PIS é descrito como "VTI / VI / VL + SE + complemento preposicionado"; o verbo de ligação não tem complemento preposicionado (a fonte exemplifica com "Sempre se está sujeito a erros", mas o complemento ali é predicativo). Impreciso.
- Partícula expletiva "associada a verbos intransitivos de sentimento/movimento": generalização que não está na fonte (a fonte dá "Vão-se minhas economias", "Passaram-se anos").
- "Que belo dia!" como advérbio de intensidade: discutível (a fonte classifica "Que ideia mais descabida!" como pronome indefinido exclamativo e "Que chato!" como advérbio). Registrar para revisão.
- Erro de digitação no COMO comparativo: "Confronte termos" (imperativo, em vez de "confronta").

Originalidade: parafraseado, exemplos trocados (nenhuma sequência de 6 palavras além de termos técnicos). Mas a estrutura segue a fonte página a página.

Clareza: predomina a lista de classificações com vocabulário rebuscado ("amplo espectro", "mesmíssima função", "destituída de carga sintática", "extirpada"). Explica pouco o porquê de cada caso; a tabela do SE é boa.

Formato: 892 palavras (alvo 2000, piso 400), 5 seções, Para fixar em bullets (7), sintético com 10 pontos e 163 palavras; mas o ponto do sintético sobre "funções sintáticas do QUE relativo" cita só "sujeito, objeto direto, objeto indireto, complemento nominal, adjunto" (faltam predicativo e agente da passiva, e "adjunto" sem qualificar).

### S0041 (EXT-L3, Língua Portuguesa, a08/s03, crase) — 3 / 3 / 4 / 3 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Falta o macete do teste do sujeito (colocar o substantivo como sujeito e ver se aceita artigo; fonte pág. 27), que a fonte apresenta como principal modo de identificar a crase.
- Falta o paralelismo em enumerações: se há crase no 1º item ("à rigidez, à inadequação e à grande quantidade"), a banca exige nos demais; e a variante com a preposição só no 1º (págs. 32 a 34, 4 questões: MP-CE, IPHAN, ABIN, IFF). É uma regra de alta incidência e está ausente.
- Falta a crase com o pronome relativo "a qual/as quais" (à qual, às quais) × "a que" (sem crase) (págs. 17, 28). Aparece só "à que" como demonstrativo.
- Faltam as locuções de meio/instrumento "à mão, à caneta, à vista, à prestação" (crase facultativa/controversa; preferência pela crase) e "a distância" (sem crase, salvo distância especificada) (pág. 30).
- Falta a crase facultativa antes de pronomes indefinidos/demonstrativos femininos que aceitem artigo: às outras, demais, várias, mesmas, próprias, pouca(s) (págs. 31 e 35).
- Faltam: "até" com sentido de inclusão não vira "até a" ("Até a bruxa..."), a distinção "dispensável × específica" no substantivo genérico (a fonte diz para ver com muita ressalva), e "bife a cavalo / frango a passarinho" (sem crase).

Correção:
- "Diante da maioria dos pronomes: ... pronomes indefinidos repelem artigo": contradiz a fonte, que diz que a ideia "não pode haver crase com pronomes indefinidos" não é totalmente verdade (pág. 34 e 35) e dá "às outras/demais/várias". É exatamente o que a questão MP-PI (2018) cobra ("à outra" é obrigatória). Leva o aluno a errar.
- Exemplo do possessivo: "Referiu-se à minha escala, não à sua" é apresentado como caso de crase obrigatória por possessivo substantivo, mas "à minha escala" é possessivo adjetivo (crase facultativa); só "não à sua" é obrigatório. Confuso (a fonte: "Referi-me à/a minha mãe, não à sua").
- Pegadinha final ("a suas ordens... terminantemente proibida... só existirá se houver plural formal"): não está na fonte, e a redação é confusa. A conclusão (não existe "à suas") é correta, mas o enunciado "plural formal" não esclarece; na prática o artigo antes de possessivo plural é facultativo e "a suas ordens" e "às suas ordens" são ambas corretas.
- "Nomes históricos ou figuras públicas que rejeitam artigo não admitem crase": não está na fonte (regra geral correta, mas sem exemplo).
- Sintético: "partícula demonstrativa 'à que'" é uma formulação inadequada para o aluno.

Originalidade: boa; exemplos próprios.

Clareza: 3. Os 8 casos de crase proibida numerados são úteis, mas explicações como "A coexistência de dois artigos com o mesmo nome é inviável" (para "uma") são pouco claras.

Formato: 833 palavras, 4 seções, 7 bullets em Para fixar, sintético com 10 pontos (166 palavras).

### S0048 (EXT-L3, Língua Portuguesa, a05/s02, objetos, CN × AA, predicativo) — 3 / 4 / 4 / 3 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- OD preposicionado: dos ~10 casos da fonte (págs. 20 e 21) faltam: infinitivo com ensinar/aprender ("aprendi a nadar"), reciprocidade ("uns aos outros"), "ambos", construções enfáticas e paralelas. O resumo traz 5 hipóteses.
- Falta o critério central da distinção CN × AA: o complemento nominal é exigido pelo nome, o adjunto não; e o teste "o termo preposicionado pode ser trocado por um adjetivo equivalente (mulher de branco / feminina) → adjunto" (págs. 24 a 26). A tabela do resumo tem 5 critérios, mas nenhum desses dois, e a fonte diz que o teste do adjetivo vem antes do agente/paciente.
- Falta a armadilha da questão TRT-MT (pág. 23): no OD preposicionado a preposição é exigência do complemento, não do verbo (impor é VTD; dispor é VTI).
- Falta o OI pleonástico ("Aos amigos, dou-lhes tudo") e o OD pleonástico de oração; a observação sobre vir/ir/chegar + lugar (intransitivo + adjunto adverbial × VTI).
- Predicativo do sujeito: faltam as "formas" (adjetivo, substantivo, numeral, locução com preposição, oração, pronome "o") e verbos andar/virar (o resumo troca por "parecer", que não está na fonte; correto na prática).

Correção: sem erro de fato encontrado. Ressalvas: "Objetos Pleonásticos" descreve só o OD; "exaltação mística" é rótulo próprio para o caso "reforço de sentimento" da fonte; o item "Raro quando associado a nomes abstratos" (preposição diferente de "de") é aproximação sem apoio claro na fonte.

Originalidade: boa; "Cumpriu o dever / Cumpriu com o dever" e "Amar a Deus / Judas traiu a Cristo" coincidem com a fonte (exemplos curtos).

Clareza: a tabela CN × AA é útil. O resto é definição em vocabulário técnico (ex.: sintético "Núcleo qualificativo do predicado nominal articulado por verbo conectivo de estado").

Formato: 754 palavras, 5 seções, 7 bullets, sintético com 10 pontos e 142 palavras (vários pontos são definições, não regra+exceção).

### S0057 (EXT-L3, Língua Portuguesa, a08/s01, regência verbal) — 3 / 3 / 4 / 2 / 2 — REFAÇÃO

Cobertura:
- Faltam três verbos que a fonte traz como "principais regências": responder (VTD × VTI/VTDI), atender (VTD/VTI; só pronomes o/a/os/as; "atender a/às súplicas") e chegar (intransitivo × VTI "a") (págs. 12 a 14). Duas questões de prova da fonte são sobre eles.
- O "lhe" como objeto indireto: o resumo diz que VTI com "a" "combinam-se classicamente com lhe", mas omite a lista de VTI que NÃO aceitam "lhe" (assistir no sentido de ver, aspirar no sentido de almejar, proceder, presidir, recorrer, aludir, anuir; pág. 10) e os exemplos errados ("Quero lhe ver"). Para assistir (caber) e para o "lhe" como OI vale a regra geral; o resumo não distingue.
- Faltam: verbos com regências diferentes não dividem o mesmo complemento ("Entrei e saí de casa"); a regência do relativo com crase (à qual × a que; págs. 6 e 7); ordem das regras -lo/-no (exceções "qui-lo", "perdemo-nos" não aparecem).
- Faltam exemplos em quase todos os verbos (agradar, aspirar, implicar, preferir sem sequer uma frase-modelo): contra a regra "explique, não liste".

Correção:
- "Verbos que admitem predicativo do objeto (chamar, tachar, considerar, julgar): ... facultando a presença da preposição 'de'": a fonte estende a facultatividade a chamar/tachar; "considerar de" e "julgar de" não são regência aceita. Generalização incorreta.
- "Implicar ... rejeitando a preposição 'em', comum no uso coloquial": a fonte não faz essa afirmação (só lista os sentidos). É posição normativa tradicional e defensável, mas é opinião não confirmada; levar para revisão humana.
- "Preferir ... repelindo ... 'do que', 'mais que' ou 'antes que'": "antes que" é invenção do resumo; a fonte condena "prefiro mais ... do que" e "prefiro antes ... a". Falta dizer que o paralelismo de artigo é exigido ("prefiro o axé ao rock").
- "Assistir" no sentido de socorrer: a fonte diz "preferencialmente VTD; aceita também 'a'", o resumo só traz o VTD.

Originalidade: ok, mas pouca elaboração própria (poucos exemplos).

Clareza: ruim. Vocabulário que não ajuda um aluno de concurso ("alomórficas", "acusativos", "dativo", "ao revés", "predicador", "nós fundamentais").

Formato:
- 670 palavras para 12 páginas (alvo 1800).
- `### Para fixar` é um único parágrafo, não 5 a 8 pontos (INSTRUCOES seção 5).
- Sintético tem 8 pontos e os dois primeiros são tautologias ("Regência verbal: disciplina o nexo de dependência e regência sintática entre verbos e seus objetos") e "Pronomes relativos e regência", violando "Proibido: pontos sem explicação"; o sintético não cobre os pronomes oblíquos, chamar/transobjetivos, assistir (caber) nem o lhe.

### S0062 (EXT-L3, Língua Portuguesa, a07/s02, concordância) — 2 / 3 / 4 / 2 / 2 — REFAÇÃO

Cobertura:
- Omissão grave: o HAVER impessoal e a regra do verbo auxiliar "contaminado" nas locuções ("Deve haver 15 anos", "Devem existir soluções"; págs. 17, 25 a 29), mais "fazer" temporal impessoal ("Faz cinco anos", "Vai fazer", "Vão fazer" errado), os sentidos de haver pessoal (haver de, haver-se) e o contraste "ter" existencial (informal). Cerca de metade das questões comentadas na fonte gira em torno disso (TJ-PA, EMAP, CAGE-RS, EBSERH, Pref. Monte Alegre, Pref. Maracanã, UFPE, UNESP, DPE-AM e a questão de "fazer" da Pref. São Roque). O resumo enuncia a regra das locuções ("a flexão incide unicamente sobre o verbo auxiliar") sem a exceção, ou seja, a regra incompleta induz ao erro nas provas.
- Primeiro assunto do índice ("expressões com pronome que, núcleo do sujeito no singular e núcleo do adjunto no plural": "Não sou um daqueles que pensam/pensa", "O efeito das catástrofes que se verificaram/verificou") não aparece com o exemplo e, sobretudo, sem a condição "desde que o sentido permita" (a fonte dá o contraexemplo "atos de terceiro que sejam considerados crime"). O que o resumo escreve em "Pronome 'que'" sobre "nós somos aqueles que" está obscuro.
- "Concordância com predicativos": o resumo descreve outra regra ("perante o verbo de ligação 'ser'... a atração pode pender para o termo plural ou para a pessoa gramatical de maior primazia"), que não é a do trecho. A regra do trecho é: "Fui eu o último que consegui / que conseguiu" (concorda com o sujeito ou com o predicativo). Texto sem apoio na fonte e sem o exemplo.
- Faltam: "tratar-se de" (indeterminado) × "tratam-se doenças" (VTD passivo), "só não vale misturar: Foi eu que fiz", sujeito oracional com "se" apassivador ("Espera-se que a economia melhore"), o erro de "parecem não pisarem" (dupla flexão), "onde" × "em que", percentuais e fração (Dois terços... compareceram), exemplos de passiva com erro de concordância.

Correção:
- Índice de indeterminação: "ocorre diante de verbos transitivos indiretos, intransitivos ou de ligação seguidos de preposição obrigatória". Intransitivos e de ligação não pedem preposição obrigatória ("Vive-se bem aqui", "Está-se bem aqui"). Erro de definição.
- "Ambas as redações encontram amparo na norma culta" (parecer): a fonte aceita "parecia entenderem" como forma "formal e rara"; o resumo não avisa que a forma com dupla flexão ("parecem não pisarem") é errada.

Originalidade: ok.

Clareza: ruim; o texto é abstrato (ex.: "a atração pode pender para o termo plural ou para a pessoa gramatical de maior primazia"), com poucos exemplos e nenhuma tabela.

Formato: 698 palavras para 13 páginas (alvo 1950); Para fixar é um parágrafo com 3 itens em vez de 5 a 8 bullets; sintético com 8 pontos sem haver/fazer.

### S0098 (EXT-L2, Informática, a08/s06, Word: Layout, Referências, Correspondências) — 3 / 4 / 4 / 3 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Faltam os atalhos das quebras: Quebra de Página (`CTRL + ENTER`), Quebra de Coluna (`CTRL + SHIFT + ENTER`), Quebra Automática de Texto (`SHIFT + ENTER`) (fonte pág. 69), e a explicação "quebra de página mantém a formatação; quebra de seção permite formatação nova".
- Falta a equivalência sumário = índice analítico × índice = índice remissivo (fonte pág. 76; é a armadilha da questão CEBRASPE/PF 2018).
- Faltam Índice de Ilustrações, Atualizar Tabela e Referência Cruzada (grupo Legendas), Gerenciar Fontes Bibliográficas, Realçar Campos de Mesclagem, Atualizar Etiquetas, Primeiro/Anterior/Próximo/Último Registro e Localizar Destinatário.
- Ignora os sinais de incidência da fonte (Layout: média; Referências: baixa; Correspondências: baixíssima), que servem para priorizar o estudo.

Correção:
- Os estilos de citação são "ABNT, APA e Chicago"; a fonte diz APA, Chicago e MLA. Troca não sinalizada em NOTAS; verificar na versão do Word de referência.
- "Quebra de Ajuste de Texto": o nome da fonte (e do Word em português) é "Quebra Automática de Texto".
- "Tamanho: A4, Carta, Ofício, A5": a fonte cita Letter, A3, A4, A5, Ledger (Ofício não está na fonte).
- "medianiz" aparece sem fonte (existe nas margens personalizadas do Word, informação correta).

Originalidade: ok; a "arquitetura tripartite" da mala direta é paráfrase fiel dos três arquivos da fonte.

Clareza: texto denso ("calibração dimensional", "controla milimetricamente"). Não usa tabelas para os atalhos.

Formato: 880 palavras (alvo 2000), 4 seções, 8 bullets no Para fixar, sintético com 10 pontos. A página 77 do PDF está em branco e não foi anotada em NOTAS (INSTRUCOES seção 6).

### S0102 (EXT-L2, Informática, a10/s05, PowerPoint: Apresentação, Revisão, Exibir, Conceitos avançados) — 3 / 4 / 4 / 3 / 3 — CORREÇÃO PONTUAL + complemento

Cobertura:
- A introdução promete "organização de janelas", mas o corpo não a traz. Faltam do grupo Janela: Nova Janela, Organizar Todas, Em Cascata, Mover Divisão, Alternar Janelas; do grupo Zoom: Zoom e Ajustar à Janela; do grupo Macros: `ALT + F8`; do grupo Mostrar: Anotações (painel de notas).
- A nota "Controlar Alterações não existe no PowerPoint (diferente do Word)" (pág. 59) é cobrável e não aparece. Falta também Pesquisa Inteligente (Ideias) e Anotações à Tinta.
- Atalhos que a fonte lista como incidência ALTA: faltam `CTRL + X`, `CTRL + C`, `CTRL + V`, `CTRL + SHIFT + F`, `CTRL + SHIFT + P`, `CTRL + SHIFT + >` e `<`, `END` (último slide) e `F1`.
- O resumo gasta o mesmo espaço em Revisão (incidência baixíssima) e deixa de fora partes de Exibir (alta).
- Faltam "Usar Intervalos" e "Mostrar Controles de Mídia".

Correção:
- "Gravar Apresentação: registra narrações em voz, marcações de ponteiro laser e temporização": a fonte lista "Executar Narrações" (reproduzir narrações e gestos de ponteiro laser), não gravar. A descrição foi trocada.
- "Ctrl + O cria uma nova apresentação vazia": correto no Office em português (onde Ctrl+O é "Novo" e Ctrl+A é "Abrir"), mas não está na fonte e pode confundir quem usa a regra do inglês. Marcar para revisão.
- Teclas numéricas + Enter para saltar ao slide e a barra de espaço para avançar: corretas, mas fora da fonte.

Originalidade: ok.

Clareza: ok em lista, com termos desnecessariamente abstratos ("condução, revisão e padronização estrutural", "auditoria ortográfica").

Formato: 881 palavras (alvo 1800). Sem anotar a página 60 em branco no PDF (NOTAS "nenhuma"). Sem tabela para os atalhos.

### S0110 (EXT-L2, Informática, a07/s05, Calc: funções lógicas/texto/data, Detetive, atalhos) — 3 / 4 / 4 / 3 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Faltam exemplos de fórmulas. A fonte traz `=SE(F2>6;"Aprovado";"Reprovado")` (incidência ALTÍSSIMA), `=ESQUERDA(B2;3)`, `=E(1=1;2=2;3=3)`. O resumo só tem a sintaxe.
- Faltam os atalhos da lista da fonte que a banca cobra: `F4` (alterna referências relativas/absolutas), `SHIFT + F5` (rastrear dependentes) e `SHIFT + F7` (rastrear precedentes), `CTRL + F1`, `F9`, `F11`, `F12`/`CTRL + F12` (agrupar/desagrupar), `CTRL + SHIFT + 2` e `6`, `CTRL + F7` (sinônimos), `F5` (Navegador), `HOME/END`, `CTRL + PAGE UP/DOWN`.
- DIA.DA.SEMANA: faltam os exemplos da fonte (`=DIA.DA.SEMANA(A1)` com 14/02/2008 resulta 5; `=DIA.DA.SEMANA(3)` resulta 3; `=DIA.DA.SEMANA(14)` resulta 7): o argumento inteiro é lido como número de dias desde a data inicial. O resumo só diz "tipo 1".
- Falta explicar a diferença precedente × dependente com exemplo (`D10 = B5*2`: B5 é precedente, D10 dependente).

Correção:
- Data inicial: o resumo diz 30/12/1899 "(ou 31/12/1899 dependendo...)"; a fonte diz 31/12/1899. A fonte tem um erro interno: com 31/12/1899 como dia zero, o dia 3 seria 02/01/1900 e o resultado "3" só fecha com o ponto de partida de 30/12/1899 (o padrão real do LibreOffice). Ou seja, o resumo está tecnicamente correto e a fonte confusa. Mas o resumo não registra a divergência em NOTAS. Revisão humana.
- "Eliminar Rastros": em LibreOffice Calc o comando é "Remover todos os rastros" (Ferramentas > Detetive). Nome provavelmente trocado.
- `ESQUERDA(texto; [k])`: ok (k é opcional no Calc).

Originalidade: ok.

Clareza: lista de funções organizada e uma tabela de atalhos; faltam exemplos. Linguagem pouco natural ("sintaxe tripartite", "higienização de dados cadastrais", "cauda final do texto à direita").

Formato: 869 palavras (alvo 2000), 6 seções, 8 bullets, sintético 10 pontos. Página 60 do PDF praticamente em branco, não anotada.

### S0125 (EXT-L2, Informática, a06/s10, Excel: gráficos, formatação condicional, classificação/filtros e tabelas dinâmicas) — 3 / 4 / 4 / 4 / 4 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Tipos de gráfico: a introdução diz "taxonomia completa", mas faltam Ações/Velas (preço de abertura, fechamento, máximo e mínimo), Superfície, Radar, Combinação, Gantt, Pareto e Contorno (fonte págs. 138 a 141); a banca pergunta "qual gráfico representa...". Faltam também "criar o gráfico: Inserir > Gráficos", atualização automática e gráfico dinâmico.
- Formatação condicional: falta o passo a passo (Página Inicial > Estilos > Formatação condicional > Nova regra) e o uso por datas; a aplicação em gráficos aparece na fonte e o resumo omite (aqui talvez bem, pois a fonte parece forçada, mas deveria estar em NOTAS).
- Tabelas dinâmicas: faltam Tabela Dinâmica Recomendada, o caminho Inserir > Tabela Dinâmica, a preparação dos dados (sem linhas/colunas vazias, não misturar tipos), agrupamento de datas/números, subtotais e totais gerais, filtros e ordenação dentro da dinâmica, e a comparação com PROCV/PROCH.

Correção:
- Sintético: "Gestão de Regras ... remove regras sobrepostas": o gerenciador permite remover regras manualmente; não remove sozinho as sobrepostas.
- "Valores... CONTAGEM para campos de texto" e `Ctrl + Shift + L` (filtro): corretos mas não estão na fonte. "Interromper se Verdadeiro": correto, não está na fonte.
- Resto correto.

Originalidade: ok.

Clareza: melhor do grupo; categorização dos gráficos em dois blocos ajuda.

Formato: 753 palavras (alvo 2000), 4 seções, 8 bullets, sintético 10 pontos. Páginas 138 e 139 do PDF só têm nomes de gráficos (figuras) e não foram anotadas em NOTAS.

### S0137 (EXT-L2, Informática, a08/s04, Word: Guia Página Inicial) — 3 / 4 / 4 / 3 / 3 — CORREÇÃO PONTUAL + complemento

Cobertura:
- Falta a tabela de marcas de formatação da fonte (pág. 48): espaço inquebrável (`CTRL + SHIFT + ESPAÇO`), quebra de parágrafo (Enter), quebra de linha (`SHIFT + ENTER`), tabulação, hífen opcional (`CTRL + -`), quebra de página (`CTRL + ENTER`), caractere de tabela (sem atalho), quebra de seção, texto oculto. O resumo só cita "Mostrar Tudo".
- Colar Especial: faltam a lista de outros formatos (planilha, texto, bitmap, imagem, HTML) e o detalhe do vínculo (Colar Link: o `CTRL + V` comum não cria vínculo; RTF e imagem eliminam a atualização; Inserir > Objeto > Criar Novo não liga ao arquivo original; pág. 43). É tema cobrado (CEBRASPE/CNPq).
- "24 itens" da Área de Transferência só aparece no Para fixar; o corpo do resumo não traz essa informação nem a pergunta ao fechar o aplicativo.
- Faltam: grupo Selecionar (do Editando); modificar um estilo atualiza todos os textos marcados com ele; opções "pelo menos / exatamente / múltiplos" do espaçamento; "Justificar: exceto a última linha"; os demais curingas da fonte (`<`, `>`, `[ ]`, `{n}`, `@`).
- Trecho de incidência ALTÍSSIMA com 705 palavras, o menor da amostra L2.

Correção:
- Pincel de Formatação: o resumo informa `CTRL + SHIFT + C` / `CTRL + SHIFT + V`; a fonte diz `CTRL + ALT + C` / `CTRL + ALT + V`. O Word de fato usa Ctrl+Shift+C/V, então o resumo está correto na prática, mas a divergência com o material do aluno não foi registrada em NOTAS. Revisão humana.
- "Alinhar à direita (comum para assinaturas e datas)": a fonte diz "pequenas seções, como cabeçalho ou rodapé". Exemplo trocado, sem erro.

Originalidade: ok.

Clareza: bons atalhos, sem tabela (INSTRUCOES recomendam tabelas para atalhos).

Formato: `### Para fixar` é um parágrafo único (5 frases), não 5 a 8 pontos; sintético com 9 pontos, 162 palavras.

---

## (c) Padrões recorrentes por agente

### EXT-L3 (Língua Portuguesa)
- Encurta demais e escolhe errado o que cortar: 620 a 900 palavras para trechos de 12 a 16 páginas (alvo 1800 a 2000, 35% a 45%). Os cortes caem em exceções, armadilhas e itens que a fonte marca como "cai muito" (haver impessoal em S0062; paralelismo de crase em S0041; critérios PA/reflexivo/PIV em S0033; responder/atender/chegar em S0057).
- Escreve em registro erudito e abstrato ("predicador", "alomórficas", "esmiúça", "ao revés", "extirpada"), que reduz a clareza para um aluno de concurso. Poucos exemplos e quase nenhuma tabela; o que há de exemplo costuma ser frase-modelo curta.
- Generaliza regras sem a ressalva da fonte (pronomes indefinidos "repelem artigo" em S0041; "considerar/julgar" com "de" em S0057; "intransitivos/de ligação seguidos de preposição" em S0062). Risco de ensinar errado, que é pior que omitir.
- `### Para fixar` em parágrafo (S0057 e S0062) em vez de 5 a 8 pontos, e sintético com pontos tautológicos (S0057) ou só com definições (S0048).
- Erro de grafia numa matéria de Português (S0033: "vêem-se") e um erro de digitação ("Confronte termos").
- NOTAS sempre "nenhuma"; o relatório do sublote diz "nenhuma inconsistência". As divergências e generalizações acima não foram sinalizadas.

### EXT-L2 (Informática)
- Cobertura sistematicamente incompleta de itens de tabela da fonte: tipos de gráfico, atalhos, comandos de grupos menores, tabela de marcas de formatação, exemplos de fórmulas. O agente cobre bem os blocos principais de cada grupo e deixa de fora as listas completas, que é onde a banca de Informática cobra "nome exato" e "atalho exato".
- Não aproveita os rótulos de "incidência em prova" da fonte para priorizar: espaço quase igual para Revisão (baixíssima) e Exibir (alta) em S0102; S0137 (ALTÍSSIMA) é o mais curto.
- Troca de nomes oficiais por rótulos próprios ou de outras versões, sem avisar: "Quebra de Ajuste de Texto", "Gravar Apresentação" (por "Executar Narrações"), "Eliminar Rastros", "ABNT" no lugar de "MLA", "Ofício" fora da lista. Em Informática, o nome do botão é o conteúdo cobrado.
- Substituição silenciosa de atalhos e datas da fonte por valores da prática (pincel de formatação, data inicial do Calc). Provavelmente corretos, mas deveriam estar em NOTAS.
- Páginas em branco ou só com figuras (S0098 p. 77; S0102 p. 60; S0110 p. 60; S0125 págs. 138 e 139) não foram anotadas em NOTAS ("nenhuma" em todos).
- Linguagem de adjetivação inflada ("calibração dimensional", "higienização", "controla milimetricamente"), mas as listas e tabelas funcionam bem.
- Pontos fortes: sem erro conceitual grave nos 5; blocos "Pegadinha" bem escolhidos (Detetive não protege células; filtro não exclui linhas); o texto é mais didático e organizado que o de EXT-L3.
- `### Para fixar` em parágrafo em S0137.

### Originalidade (ambos)
Sem cópia: nenhuma sequência literal maior que 8 palavras (e as maiores são nomes de comandos ou termos técnicos, ex.: "manter formatação original / mesclar formatação / manter somente texto"). Há semelhança estrutural esperada (ordem dos grupos em Informática). Em LP, vários exemplos foram trocados mas os pares permanecem ("Cumpriu o dever / Cumpriu com o dever"; "Amar a Deus"; "Judas traiu a Cristo", curtos). Nenhum resumo contém expressão proibida ("nesta aula", "no PDF", "segundo o professor" etc.).

---

## (d) REVISÃO HUMANA

NOTAS dos 10 resumos: todas "nenhuma". Não há item de NOTAS a transcrever; o que segue são pontos duvidosos achados pela avaliação, que o agente devia ter registrado.

| ID | Ponto a revisar | Motivo |
| --- | --- | --- |
| S0033 | "Vêem-se falhas" na pegadinha | Grafia pós-Acordo Ortográfico: "veem-se". Corrigir. |
| S0033 | "Fiz sinal que entrassem" como conjunção final | Provavelmente integrante (OD oracional); trocar o exemplo. |
| S0033 | "Que belo dia!" como advérbio de intensidade | A fonte classifica "Que ideia mais descabida!" como pronome indefinido e "Que chato!" como advérbio; classificação do exemplo é discutível. |
| S0033 | Expletivo "associado a verbos de sentimento/movimento" | Generalização sem apoio na fonte. |
| S0041 | "Pronomes indefinidos repelem artigo" | Contradiz a fonte (às outras/demais/várias); item cobrado em prova (MP-PI). Corrigir. |
| S0041 | "Referiu-se à minha escala, não à sua" | Mistura possessivo adjetivo (facultativo) e substantivo (obrigatório). |
| S0041 | Pegadinha "a suas ordens... plural formal" | Não está na fonte; redação confusa. Decidir se mantém e reescrever. |
| S0041 | "Nomes históricos/figuras públicas... não admitem crase" | Não consta na fonte. |
| S0048 | "Raro quando associado a nomes abstratos" (AA com preposição diferente de "de") | Aproximação sem apoio claro na fonte. |
| S0057 | "Considerar, julgar" com "de" facultativo | Provável erro de generalização. |
| S0057 | "Implicar" rejeita "em" (acarretar) | Posição normativa não confirmada pela fonte; verificar a norma adotada. |
| S0057 | "Preferir... antes que" | Termo inventado; a fonte condena "prefiro antes... a". |
| S0057 | "Lhe" com VTI "a" sem a lista de exceções | Regra incompleta (assistir, aspirar, proceder, presidir, recorrer, aludir, anuir). |
| S0062 | Regra "concordância com predicativos" | Texto do resumo não corresponde ao que o trecho ensina; reescrever com "Fui eu o último que consegui/conseguiu". |
| S0062 | Índice de indeterminação "intransitivos/de ligação seguidos de preposição obrigatória" | Definição incorreta. |
| S0062 | "Ambas as redações" de "parecer + infinitivo" | Falta avisar que "parecem não pisarem" (dupla flexão) é errado. |
| S0098 | Estilos de citação "ABNT, APA e Chicago" | Fonte: APA, Chicago, MLA. Confirmar qual está certo na versão do Word. |
| S0098 | "Quebra de Ajuste de Texto" e tamanho "Ofício" | Nomes diferentes da fonte (Quebra Automática de Texto; Letter, A3, A4, A5, Ledger). |
| S0098 / S0102 / S0110 / S0125 | Páginas em branco ou só com figuras sem registro em NOTAS (S0098 p. 77; S0102 p. 60; S0110 p. 60; S0125 págs. 138 e 139) | INSTRUCOES seção 6: registrar página vazia em NOTAS. |
| S0102 | `Ctrl + O` cria nova apresentação | Correto no Office em português, mas fora da fonte; confirmar. |
| S0102 | "Gravar Apresentação" (narração, laser, temporização) | A fonte diz "Executar Narrações" (reproduzir). Corrigir o nome e a ação. |
| S0102 | Fonte: tecla "E" oculta o slide (pág. 65) | Dúvida sobre a fonte, não do resumo (que omitiu). Em PowerPoint, "E" apaga anotações; verificar antes de qualquer resumo futuro trazer esse atalho. |
| S0110 | Data inicial do Calc 30/12/1899 × 31/12/1899 | Fonte inconsistente (explica 31/12/1899, mas resultados só fecham com 30/12/1899); decidir o texto oficial. |
| S0110 | "Eliminar Rastros" | Nome oficial no Calc: "Remover todos os rastros". |
| S0125 | "Taxonomia completa" dos gráficos e ausência de Ações, Radar, Superfície, Combinação, Gantt, Pareto, Contorno | Afirmação falsa e conteúdo faltando. |
| S0125 | Formatação condicional em gráficos (fonte pág. 144) | Fonte afirma que se aplica a gráficos; recurso não existe como tal no Excel. Avaliar se deve entrar com ressalva. |
| S0125 | `Ctrl + Shift + L`, "CONTAGEM para campos de texto", "Interromper se Verdadeiro" | Corretos mas fora da fonte; confirmar. |
| S0137 | Pincel de Formatação `CTRL + SHIFT + C/V` × fonte `CTRL + ALT + C/V` | Resumo está certo no Word real, fonte divergente; registrar em NOTAS e decidir qual o aluno verá. |
| S0137 | Falta a tabela de marcas de formatação e o detalhe do vínculo no Colar Especial | Cobráveis; complementar. |

Itens de processo para o dono do produto:
- O relatório do agente EXT-L3 afirma "nenhuma inconsistência impeditiva" e o do EXT-L2 relata um problema só (S0117); a avaliação mostra problemas que o próprio agente deveria ter registrado (páginas vazias, divergência de atalhos).
- O `verificar_resumos.py` não detecta `### Para fixar` em parágrafo único (S0057, S0062, S0137). Sugestão: exigir 5 a 8 linhas iniciadas por `- ` na seção.
- Sugestão de instrução adicional para o próximo sublote: "para cada trecho, listar no relatório os itens de tabela/lista da fonte (comandos, atalhos, verbos, casos) e marcar quais entraram"; e "priorizar pelos rótulos de incidência em prova do material".
