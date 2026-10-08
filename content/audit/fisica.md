# Auditoria estrutural — Física (fisica/a00–a17)

Escopo: 18 aulas do Estratégia (prof. Vinicius Silva), 1.410 págs. Varri todas as páginas (`--heads`) e li as suspeitas por inteiro (`--pages`). Conferi o edital (Anexo II, 2º Tenente) item a item, inclusive os itens menos comuns.

## Números
| | Antes | Depois |
|---|---|---|
| Págs. de teoria | 501 | 494 |
| Trechos de Teoria | 37 | 39 |
| Trechos > 17 págs. | 0 | 0 |
| Cortes no meio de tópico | vários (a03, a08, a11) | 0 |

Por aula, nas que mudaram: a00 39→31 págs., 3→2 trechos · a03 2→3 trechos · a11 3→4 trechos · a12 8 págs., 0→11 págs. comentadas · a13 60→61 págs., 4→5 trechos.

## Correções (`content/overrides/fisica.json`)
- **a00**: as págs. 5–13 (apresentação, metodologia, "A Física em concursos", estilo das questões, estrutura das aulas) passam a FRONT. Antes elas viravam um trecho de Teoria de 6 págs. sem conteúdo de Física. A pág. 87 passa a C (fim de comentário) e as 88–89 a S (quadro de fórmulas). Trechos: 14–27 vetores · 28–44 grandezas, notação científica, ordem de grandeza, análise dimensional, SI.
- **a03**: cortes em 14 e 21. O trecho antigo parava na pág. 16, no meio do lançamento horizontal. Agora: 3–13 queda livre e lançamentos verticais · 14–20 lançamento horizontal (7 págs., tema autônomo) · 21–32 lançamento oblíquo. Na pág. 13, o PDF repete o título "Lançamento vertical para cima" para a seção que trata do lançamento para baixo; corrigi o subtítulo.
- **a06**: as págs. 71–86 (lista sem comentário) passam a L, a 87 a K e a 88 a S. Antes tudo isso estava como C. As págs. 89–90 (questão avulsa sem comentário) passam a L.
- **a08**: corte na pág. 12, onde começa a estática do corpo extenso. O trecho 2 começava num falso subtítulo ("pista", pág. 16) no meio do torque. Agora: 3–11 ponto material e roldanas · 12–25 corpo extenso, torque, binário, tipos de equilíbrio, centro de gravidade.
- **a11**: cortes em 20, 34 e 43. O trecho 2 cortava "Leis físicas dos gases" no meio (36/37) e o trecho 3 juntava gases com termodinâmica. Agora: 5–19 termometria e calorimetria · 20–33 equilíbrio térmico, calorímetros e dilatação · 34–42 gases · 43–53 termodinâmica, máquinas térmicas e Carnot.
- **a12**: o 1º bloco "Questões Propostas" (11–21) tem resposta e comentário, então vira C. O 2º bloco (22–25) é a lista sem comentário. Antes a aula aparecia com 0 comentadas. A teoria (3–10, propagação do calor) continua num trecho único de 8 págs., porque o assunto é autônomo. Tentei incluir a pág. 2 (abertura do tema), mas o algoritmo ignora subtítulos em páginas de sumário; desfiz, e a perda é só um parágrafo retórico.
- **a13**: a pág. 47 (início do MHS) estava como resumo (S) e saía da teoria; passa a T. Com isso o MHS teria 18 págs., então há cortes em 47 e 56: 47–55 cinemática do MHS · 56–64 dinâmica, energia, pêndulo simples e massa-mola. Pus uma nota avisando que a aula não traz óptica geométrica.
- **a15**: removido o subtítulo meta "Conteúdo da aula" (pág. 3).
- **a16**: as págs. 102–104 (fórmulas) passam de K para S.
- **Subtítulos automáticos falsos**: removidos 131 em 16 aulas, com `dropHeadings`. São pedaços de fórmula ou de frase ("R = A + B", "Fsen", "540km", "q = −", "pista", "Patm", "g Vol", "igualando", "Bateria"…). Eles apareciam na lista de tópicos dos trechos e atraíam cortes. Mantive os automáticos numerados ("2.1 – …"), que são reais.

As outras aulas foram conferidas e mantidas: a01, a02, a04, a05, a07, a09, a10, a14, a15, a16, a17. Os cortes delas já caem em inícios de tópico e respeitam 6–17 págs. a10 fica com dois trechos curtos (9 e 10 págs.), porque juntar daria 19.

Os "FÓRMULAS MAIS UTILIZADAS NA AULA" marcados S estão corretos: são só quadros de fórmulas, sem teoria nova. O "Estilo das questões" (a00, pág. 11) é texto meta e agora fica em FRONT.

## Cobertura do edital (resumo; detalhe em `content/edital/fisica.json`)
| Bloco | Coberto | Parcial | Lacuna |
|---|---|---|---|
| 1. Conhecimentos básicos (7) | 7 | – | – |
| 2. Movimento, equilíbrio, leis (19) | 15 | 2.16 diagramas de forças; 2.18 aspectos históricos da hidrostática | 2.2 relação histórica força × movimento; 2.6 referenciais inerciais e não inerciais |
| 3. Energia, trabalho, potência (5) | 5 | – | – |
| 4. Mecânica e universo (6) | 4 | 4.6 origem do universo (só geo/heliocentrismo) | 4.5 marés e variações climáticas |
| 5. Elétricos e magnéticos (19) | 15 | 5.7 blindagem; 5.14 CC × CA; 5.16 símbolos e representação de circuitos | 5.15 medidores elétricos |
| 6. Ondas e óptica (11) | 5 | 6.2 reflexão e refração; 6.11 índice e leis da refração | 6.1 feixes/frentes de onda; 6.3 lentes e espelhos; 6.4 formação de imagens; 6.5 instrumentos ópticos |
| 7. Calor e termodinâmica (13) | 12 | 7.13 fenômenos climáticos e ciclo da água | – |

Itens menos comuns, já conferidos e cobertos: centro de massa e ponto material (a07 21–23; a01 6–8), forças internas e externas (a07 9–12), poder das pontas (a14 23, um parágrafo), superfícies equipotenciais (a14 20–22), campo magnético terrestre (a17 11–12), máquinas térmicas (a11 49–52), Carnot (a11 52–53, curto), capacitores (a16 22–30).

## Auditoria inversa (classificação)
- **Indexada no lugar errado**: a00 5–13 (meta como teoria), a00 87–89, a06 71–90, a12 11–21, a13 47, a16 102–104. Todas corrigidas.
- **Superfragmentada / corte ruim**: a03 (horizontal partido), a08 (torque partido), a11 (gases partidos). Corrigidas.
- **Conteúdo complementar**: MHS (a13 47–64, cabe em "Oscilações"); geradores, receptores e associações (a16 10–21). Mantidos.
- **Necessita revisão humana**: a03 pág. 13, título trocado no PDF (corrigido no override). a09 pág. 20, o comentário da questão 2 explica eclipses como fenômeno eletromagnético (na verdade descreve auroras), um erro conceitual do material. Os subtítulos automáticos falsos foram removidos.
- Nenhuma aula fora do edital e nenhuma aula só de questões.

## Lacunas e complementos
`content/gaps.json` não registra nenhuma lacuna de Física, e não existe complemento de Física. A auditoria confirma lacunas reais, em ordem de peso provável na prova AOCP:
1. **Óptica geométrica**: princípios da óptica, feixes, reflexão (leis, espelhos planos e esféricos), refração da luz (Snell-Descartes, reflexão total), lentes, formação de imagens, instrumentos ópticos simples (olho, lupa, câmara escura, microscópio, luneta). É um bloco inteiro do item 6 sem nenhuma aula. **Lacuna principal.**
2. **Medidores elétricos e símbolos de circuitos**: amperímetro e voltímetro (ideal, ligação), galvanômetro, quadro de símbolos. Na CA, valor eficaz e rede de 60 Hz.
3. **Referenciais inerciais e não inerciais** e **relação histórica entre força e movimento** (Aristóteles, Galileu, Newton).
4. **Marés, estações e variações climáticas**; **origem e evolução do universo** (Big Bang, expansão).
5. **Ciclo da água e fenômenos climáticos**: evaporação × ebulição, condensação, orvalho, umidade, nuvens e chuva, calor latente no clima. Também a **blindagem eletrostática** (gaiola de Faraday).

Não criei complementos (o briefing reserva essa decisão ao orquestrador).

## Pendências
- Decidir e redigir os complementos acima. Sugestão: um "Óptica geométrica" (grande, ≈ 3 trechos) e um "Física — tópicos do edital" (medidores e símbolos, CA, referenciais, história força × movimento, marés e clima, origem do universo, ciclo da água, blindagem).
- `gaps.json` deveria registrar essas lacunas (arquivo global, não editei).
- A Aula 05 tem no título "referenciais inerciais e não inerciais", mas não ensina o tema. O catálogo usa esse título, e isso pode levar o aluno a achar que o item está coberto.
- MHS (a13, 18 págs.) fica no plano como conteúdo de "Oscilações". Se o orquestrador quiser priorizar o enxuto, é candidato a nota "partial".
- `segment.py` ignora subtítulos em páginas ≤ `tocMax`. Em a12 isso impede que a abertura do tema na pág. 2 inicie o trecho. O impacto é mínimo.
