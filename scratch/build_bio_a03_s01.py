import re
import subprocess
import sys

content = """---
id: "biologia/a03/s01"
volume: "biologia/m03"
capitulo: 5
titulo: "Introdução à Biologia Molecular e Ácidos Nucleicos"
fingerprint: {"startPage": 4, "endPage": 15, "startTopic": "Introdução à Biologia Molecular"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-32"
edital: ["geral:1.3", "geral:1.6"]
fontes: ["Material didático institucional CBMPE — Biologia Geral e Molecular — consultado em 2026-10-31"]
notas: "Introdução à biologia molecular e ácidos nucleicos: composição de nucleotídeos (pentose, fosfato no carbono 5', base nitrogenada no carbono 1', ligação fosfodiéster na hidroxila 3'); bases púricas (adenina e guanina) e pirimídicas (citosina, timina e uracila); comparativo estrutural e bioquímico entre DNA e RNA; classes de RNA celular (RNAr catalítico estruturador do ribossomo no nucléolo, RNAm com códons e RNAt adaptador com anticódon e extremidade aceptor CCA); transcrição celular catalisada pela RNA polimerase no sentido 5' para 3', promotores de DNA, fita molde antisense versus fita codificadora sense; etapas de iniciação, alongamento e terminação transcricional; diferenças entre procariontes e eucariontes na organização da transcrição; processamento pós-transcricional eucarioto (5'-cap de 7-metilguanosina, cauda poli-A 3', splicing por snRNPs e splicing alternativo); estrutura em dupla hélice antiparalela do DNA (modelo de Watson, Crick e Franklin), pareamentos A=T e C-G, sulcos da hélice, formas B, A e Z; estabilidade físico-química, desnaturação térmica, temperatura de fusão (Tm) dependente de G+C, renaturação e topologia com atuação das topoisomerases tipo I e II."
---

A Biologia Molecular investiga a base química e física dos fenômenos vitais, concentrando-se nas macromoléculas portadoras e executoras da informação genética. O entendimento detalhado dos ácidos nucleicos revolucionou as ciências biológicas ao desvendar como as instruções hereditárias são armazenadas, transmitidas e convertidas em funções celulares específicas. Para as avaliações da carreira de oficial dos corpos de bombeiros e da segurança pública, o conhecimento sólido da composição dos nucleotídeos, da arquitetura da dupla hélice do DNA, dos tipos de RNA e das minúcias da transcrição gênica constitui alicerce indispensável para a resolução de itens analíticos e conceituais de alta complexidade.

> [!objetivos]
> - Identificar os componentes fundamentais dos nucleotídeos e as distinções bioquímicas entre DNA e RNA.
> - Caracterizar a estrutura, as peculiaridades e as funções celulares do RNAr, RNAm e RNAt.
> - Compreender a dinâmica da transcrição gênica e analisar as distinções operacionais entre procariontes e eucariontes.
> - Analisar o processamento do RNA mensageiro eucarioto e as características físico-químicas e topológicas da molécula de DNA.

## Estrutura Química dos Nucleotídeos

Os ácidos nucleicos foram identificados pioneiramente por Friedrich Miescher em 1869 a partir do núcleo de glóbulos brancos. Trata-se de macromoléculas de natureza polimérica constituídas pelo encadeamento ordenado de unidades estruturais menores denominadas nucleotídeos. Quando a estrutura apresenta apenas a pentose ligada covalentemente à base nitrogenada, desprovida de grupamento fosfato, recebe a designação de nucleosídeo. A incorporação de um a três grupos fosfato na posição 5' da pentose converte o composto em um nucleotídeo funcional mono, di ou trifosfatado.

Cada nucleotídeo é formado por três frações moleculares: uma pentose (monossacarídeo com cinco carbonos), uma base nitrogenada heterocíclica e um grupo fosfato. A base nitrogenada liga-se covalentemente ao carbono 1' da pentose por meio de uma ligação N-glicosídica. O grupo fosfato, por sua vez, esterifica-se ao carbono 5' do anel do açúcar. A hidroxila livre localizada no carbono 3' da pentose funciona como o sítio aceptor obrigatório para a adição do nucleotídeo subsequente. Na síntese polinucleotídica, a ligação fosfodiéster estabelece-se entre a hidroxila 3' do açúcar precedente e o fosfato 5' do nucleotídeo entrante, conferindo direcionalidade estrita 5' para 3' à fita em crescimento.

As bases nitrogenadas dividem-se bioquimicamente em duas famílias conformacionais conforme o número de anéis aromáticos presentes em seu arcabouço molecular: as purinas (ou bases púricas) e as pirimidinas (ou bases pirimídicas). As purinas possuem dois anéis condensados (anel pirimidínico fundido a anel imidazol) e englobam a adenina e a guanina. As pirimidinas possuem um anel aromático simples de seis membros e englobam a citosina, a timina e a uracila.

| Família Bioquímica | Anéis Aromáticos | Bases Nitrogenadas | Ocorrência Biológica |
| :--- | :--- | :--- | :--- |
| **Purinas (Bases Púricas)** | Dois anéis fundidos | Adenina (A) e Guanina (G) | Presentes no DNA e no RNA celular |
| **Pirimidinas (Bases Pirimídicas)** | Um anel hexagonal | Citosina (C), Timina (T) e Uracila (U) | Citosina em ambos; Timina no DNA; Uracila no RNA |

> [!atencao]
> As bancas examinadoras cobram frequentemente a identificação da polaridade 5' para 3' das fitas. A extremidade 5' é sempre caracterizada pelo grupo fosfato livre ou terminal, enquanto a extremidade 3' é marcada pela presença da hidroxila (OH) livre ligada ao carbono 3' da desoxirribose ou ribose.

## Comparativo Bioquímico entre DNA e RNA

As duas grandes classes de ácidos nucleicos desempenham papéis biológicos complementares na manutenção da vida celular, refletindo adaptações estruturais consolidadas ao longo da evolução. A principal diferença química entre o DNA e o RNA situa-se na estrutura da pentose. O DNA contém a 2'-desoxirribose, açúcar que carece de um átomo de oxigênio no carbono 2', apresentando apenas átomos de hidrogênio ligados a essa posição. O RNA, em contraste, contém a D-ribose, que mantém um grupamento hidroxila altamente reativo ligado ao carbono 2'.

A presença da hidroxila no carbono 2' da ribose torna o RNA substancialmente mais suscetível à hidrólise química em soluções alcalinas, justificando seu papel de intermediário dinâmico e efêmero na transmissão de sinais celulares. Por outro lado, a desoxirribose confere ao DNA uma estabilidade termodinâmica e conformacional superior, ideal para a preservação fidedigna do patrimônio genético através de sucessivas gerações celulares. Além disso, a timina do DNA corresponde estruturalmente à 5-metiluracila; esse grupo metila adicional facilita a identificação e o reparo de danos espontâneos por enzimas celulares especializadas.

| Parâmetro Estrutural | Ácido Desoxirribonucleico (DNA) | Ácido Ribonucleico (RNA) |
| :--- | :--- | :--- |
| **Pentose** | 2'-desoxirribose (sem oxigênio no carbono 2') | D-ribose (hidroxila reativa no carbono 2') |
| **Composição de Bases** | Adenina, Guanina, Citosina e Timina | Adenina, Guanina, Citosina e Uracila |
| **Conformação Espacial** | Dupla fita helicoidal antiparalela | Fita simples com dobramentos secundários locais |
| **Estabilidade Química** | Alta estabilidade contra hidrólise celular | Meia-vida reduzida, elevada susceptibilidade a nucleases |

## Classes de RNA e suas Funções Celulares

Ao contrário da molécula de DNA, que se organiza preferencialmente como uma dupla hélice longa e estável, o RNA celular é gerado como uma molécula de fita simples. No entanto, por meio de pareamentos intramoleculares de bases complementares, o RNA adota configurações secundárias e terciárias intrincadas, formando alças, grampos e domínios globulares que viabilizam suas múltiplas ações catalíticas e adaptadoras na síntese proteica.

No citoplasma e nas organelas atuam três classes universais de RNA:

1. **RNA ribossômico (RNAr):** Representa a fração molecular predominante, compondo mais de 80% do RNA total da célula. O RNAr associa-se a proteínas estruturais para constituir as duas subunidades do ribossomo. Nos eucariotos, a síntese e a montagem prévia das partículas ribonucleoproteicas ocorrem na região do nucléolo. O RNAr possui função catalítica direta (ribozima), sendo o catalisador biológico que efetiva a ligação peptídica entre aminoácidos adjacentes.
2. **RNA mensageiro (RNAm):** Corresponde à fita molde que transfere as instruções genéticas contidas no DNA nuclear para o maquinário tradutor ribossômico. Sua sequência linear é lida em trincas sucessivas de nucleotídeos denominadas códons.
3. **RNA transportador (RNAt):** Molécula adaptadora de pequenas dimensões (70 a 90 nucleotídeos) com conformação em folha de trevo dobrada tridimensionalmente em L. Na extremidade terminal 3' (sequência de consenso CCA), o RNAt acopla-se a um aminoácido ativado por meio da enzima aminoacil-RNAt sintetase. Na extremidade oposta, sua alça globular expõe o anticódon, trinca que pareia de modo antiparalelo com o códon correspondente do RNAm.

```mermaid Organização Estrutural das Três Classes de RNA
flowchart TD
    DNA["DNA Genômico"] -->|Transcrição| RNAr["RNAr (Ribossômico)"]
    DNA -->|Transcrição| RNAm["RNAm (Mensageiro)"]
    DNA -->|Transcrição| RNAt["RNAt (Transportador)"]

    RNAr --> Ribossomo["Estrutura o Ribossomo no Nucléolo e catalisa a ligação peptídica"]
    RNAm --> Matriz["Fornece a matriz de leitura dividida em Códons de trincas"]
    RNAt --> Adaptador["Carrega aminoácido específico no 3'-CCA e pareia pelo Anticódon"]

    Ribossomo --> Traducao["Síntese Polipeptídica no Citoplasma"]
    Matriz --> Traducao
    Adaptador --> Traducao
```

O pareamento entre bases nitrogenadas no RNA obedece ao princípio de complementaridade: a adenina emparelha-se com a uracila mediante duas pontes de hidrogênio (A=U), enquanto a guanina une-se à citosina mediante três pontes de hidrogênio (G-C). Em moléculas de RNAt ocorrem ainda bases modificadas enzimaticamente pós-transcrição, tais como a inosina e a pseudouridina, que viabilizam o pareamento oscilante (hipótese do balanço) com a terceira base dos códons.

> [!exemplo]
> Caso a matriz do RNA mensageiro apresente o códon 5'-AGC-3', o RNA transportador correspondente exibirá a trinca complementar e antiparalela no anticódon: 3'-UCG-5' (lida convencionalmente como 5'-GCU-3'). Esse reconhecimento termodinâmico exato orienta a correta incorporação da serina na extremidade C-terminal do peptídeo nascente.

## Mecanismo da Transcrição Gênica

A transcrição constitui a etapa primária da expressão dos genes, consistindo na polimerização enzimática de uma fita de RNA a partir de uma fita molde de DNA. Esse processo não exige a síntese de iniciadores (primers), diferenciando-se decisivamente da replicação do DNA. A enzima responsável pelo processo é a RNA polimerase dependente de DNA, que polimeriza a nova cadeia exclusivamente na direção 5' para 3', promovendo o ataque nucleofílico da hidroxila 3' nascente sobre o grupo fosfato alfa do ribonucleotídeo trifosfatado (rNTP) entrante.

Para sintetizar a nova molécula no sentido 5' para 3', a enzima lê obrigatoriamente a fita molde de DNA no sentido antiparalelo, ou seja, de 3' para 5'. A fita de DNA que serve de referência física direta é denominada fita molde, fita antisense ou fita negativa (-). Em contraposição, a fita complementar não transcrita da dupla hélice é chamada fita codificadora, fita sense ou fita positiva (+). A sequência da fita codificadora é idêntica à do RNA recém-transcrito, guardando apenas a diferença pontual da substituição de timinas por uracilas.

A maquinaria de transcrição opera por três etapas funcionais distintas:

1. **Iniciação:** A RNA polimerase reconhece e ancora-se em sequências específicas do DNA localizadas a montante do sítio de início da síntese, denominadas promotores. Ao ligar-se à região promotora, a enzima desfaz localmente as pontes de hidrogênio do DNA, desenrolando cerca de 14 pares de bases para estruturar a bolha de transcrição.
2. **Alongamento:** A polimerase transloca-se sobre a fita molde mantendo a bolha de transcrição aberta e adicionando ribonucleotídeos complementares à extremidade 3'-OH da cadeia em expansão. Atrás da enzima, o híbrido transitório DNA-RNA se desfaz e a dupla hélice de DNA recompõe-se espontaneamente.
3. **Terminação:** Ao alcançar sequências genéticas de finalização, o complexo ternário formado por enzima, DNA e transcrito dissocia-se. Em bactérias, a parada ocorre por colapso mecânico promovido por uma alça rica em GC (grampo hairpin) ou pela ação de desemparelhamento mediada pela proteína helicase Rho.

| Etapa da Transcrição | Dinâmica Bioquímica | Componentes Envolvidos |
| :--- | :--- | :--- |
| **Iniciação** | Reconhecimento do promotor e formação da bolha aberta | Promotor, polimerase de RNA, abertura de pontes de hidrogênio |
| **Alongamento** | Síntese catalítica contínua da fita de RNA no sentido 5' para 3' | Ribonucleotídeos ativados (ATP, GTP, CTP, UTP), fita molde lida 3' para 5' |
| **Terminação** | Desacoplamento do complexo e liberação do RNA recém-polimerizado | Sequências terminadoras de término, estrutura em grampo ou fator Rho |

> [!bizu]
> Guarde a assimetria do processo: a RNA polimerase caminha na fita de DNA de 3' para 5', mas constrói o RNA obrigatoriamente de 5' para 3'. O promotor determina não apenas o sítio inicial exato da transcrição, mas também qual das duas fitas do DNA será empregada como fita molde.

## Transcrição em Procariontes e Eucariontes

A arquitetura celular impõe diferenças substanciais no fluxo e na regulação da síntese do RNA entre organismos procariontes e eucariontes. Em bactérias e arqueas, a ausência de envoltório nuclear possibilita que os ribossomos tenham acesso físico imediato à molécula de RNA mensageiro à medida que ela emerge da RNA polimerase. Dessa forma, verifica-se o acoplamento simultâneo entre transcrição e tradução celular.

Nas células eucarióticas, por sua vez, a presença da carioteca impõe uma segregação físico-temporal estrita. A transcrição ocorre obrigatoriamente no interior do núcleo, e o transcrito imaturo necessita passar por um processamento químico extenso antes de ser transportado através dos complexos de poro nuclear até o citoplasma, onde residem os ribossomos tradutores. Essa compartimentação celular impede o acoplamento direto e viabiliza pontos suplementares de regulação da expressão fenotípica.

Quanto à diversidade enzimática, as células procarióticas utilizam uma única espécie de RNA polimerase central que interage com o fator sigma para identificar sequências promotoras específicas. Em contraste, os eucariotos possuem três variantes nucleares especializadas de RNA polimerase:

- **RNA Polimerase I:** Atua no nucléolo sintetizando o precursor dos grandes RNAs ribossômicos (RNAr 28S, 18S e 5,8S).
- **RNA Polimerase II:** Opera no nucleoplasma transcrevendo genes que originam os RNAs mensageiros e pequenos RNAs regulatórios.
- **RNA Polimerase III:** Sintetiza o RNA transportador, o RNAr 5S e pequenos RNAs nucleares estruturais.

Outra disparidade determinante repousa na quantidade de genes codificados por transcrito. O RNA mensageiro bacteriano é tipicamente policistrônico, carregando as instruções para a tradução de vários polipeptídeos independentes a partir de uma única transcrição contínua (operon). Nos eucariontes, o RNAm é quase exclusivamente monocistrônico, codificando apenas uma cadeia polipeptídica individual.

| Aspecto Diferencial | Procariontes | Eucariontes |
| :--- | :--- | :--- |
| **Compartimentação** | Ausente; transcrição acoplada à tradução no citoplasma | Presente; transcrição nuclear e tradução citoplasmática |
| **RNA Polimerases** | Apenas um tipo catalítico associado a fatores sigma | Três classes nucleares nucleolares e nucleoplásmicas (I, II e III) |
| **Natureza do Transcrito** | Fita comumente policistrônica (organização em operons) | Fita estritamente monocistrônica para cada polipeptídeo |
| **Processamento do RNA** | Ausente; tradução direta sem modificações terminais | Amplo; adição de 5'-cap, cauda poli-A e splicing de íntrons |

## Processamento Pós-Transcricional do Pré-RNAm

Nas células eucarióticas, o transcrito primário originado pela RNA polimerase II é denominado pré-RNA mensageiro (ou transcrito primário). Esse precursor imaturo não pode ser traduzido diretamente pelos ribossomos e passa por três eventos coordenados de modificação pós-transcricional no interior do núcleo: o capeamento 5', a poliadenilação 3' e o splicing.

O capeamento ocorre de maneira precoce, quando o transcrito nascente atinge cerca de vinte nucleotídeos de extensão. Uma 7-metilguanosina é adicionada à extremidade 5' da fita por meio de uma ligação atípica 5'-5' trifosfato. A estrutura resultante, denominada 5'-cap, desempenha papéis vitais: impede a degradação da extremidade 5' por exonucleases nucleares e citoplasmáticas, sinaliza o transporte ativo do transcrito através do envelope nuclear e serve de ponto de ancoragem para os fatores proteicos que orientam a ligação da subunidade menor do ribossomo durante o início da tradução.

A poliadenilação ocorre na extremidade oposta após a clivagem enzimática do transcrito primário provocada por um sinal de consenso no RNA (como AAUAAA). A enzima poli-A polimerase adiciona uma sequência contendo entre 100 e 250 resíduos consecutivos de adenina à ponta 3'-OH do RNA, gerando a chamada cauda poli-A. Essa cauda hidrofóbica protege o RNA contra a degradação celular por 3'-exonucleases e regula a estabilidade e a eficiência traducional do mensageiro no citoplasma.

O terceiro evento consiste no splicing, que promove a excisão precisa de regiões não codificadoras (denominadas íntrons) e a união consecutiva das regiões codificadoras remanescentes (denominadas éxons). O splicing é executado pelo spliceossomo, um maquinário nuclear composto por pequenos RNAs nucleares ricos em uracila conjugados a proteínas estruturais (as snRNPs). O complexo reconhece sítios conservados de clivagem nas fronteiras dos íntrons, catalisando duas reações de transesterificação consecutivas que liberam o íntron na conformação de laço e unem os éxons contíguos.

> [!esquema]
> A variabilidade fenotípica eucariótica é ampliada pelo mecanismo do **splicing alternativo**. Nesse processo, éxons selecionados podem ser incluídos ou excluídos do transcrito final em diferentes tecidos celulares. Dessa maneira, um único gene genômico pode dar origem a múltiplos RNAs mensageiros funcionais distintos e codificar diversas isoformas proteicas com propriedades biológicas variadas.

## Estrutura Tridimensional e Propriedades do DNA

O modelo tridimensional do DNA foi descrito em 1953 por James Watson e Francis Crick, integrando dados experimentais de difração de raios X colhidos por Rosalind Franklin e Maurice Wilkins com as análises quantitativas de Erwin Chargaff. O modelo consolidou o entendimento de que a molécula constitui uma dupla hélice formada por duas fitas polinucleotídicas enroladas em torno de um eixo comum.

As duas fitas do DNA são estritamente antiparalelas: enquanto uma fita segue a direção química 5' para 3', a fita pareada corre em orientação oposta, de 3' para 5'. A espinha dorsal hidrofílica composta por unidades alternadas de pentose e fosfato localiza-se na face externa do polímero, em contato direto com o ambiente aquoso intracelular. As bases nitrogenadas hidrofóbicas, com seus anéis aromáticos planos, projetam-se para o interior da hélice, posicionando-se quase perpendicularmente ao eixo central longitudinal.

O emparelhamento de bases no interior do cilindro molecular obedece a regras estereoquímicas estritas: a adenina forma invariavelmente duas pontes de hidrogênio com a timina (A=T), e a guanina forma três pontes de hidrogênio com a citosina (G-C). Essa geometria de pareamento corrobora a regra de Chargaff, segundo a qual, em qualquer amostra de DNA de fita dupla, a quantidade molar de purinas equivale à de pirimidinas. A estabilidade global da estrutura é garantida cumulativamente pelas pontes de hidrogênio transversais e pelas forças hidrofóbicas de empilhamento vertical que se estabelecem entre os anéis das bases adjacentes.

A geometria do enrolamento helicoidal do DNA gera dois sulcos longitudinais externos de profundidades desiguais: o sulco maior e o sulco menor. O sulco maior expõe bordas atômicas das bases nitrogenadas contendo potenciais doadores e aceitadores de pontes de hidrogênio, permitindo que fatores de transcrição e enzimas reconheçam sequências específicas de nucleotídeos sem desfazer a dupla hélice. Além da forma clássica B descrita por Watson e Crick, o DNA pode apresentar conformações alternativas em função da hidratação e da sequência primária de bases.

| Conformação Estrutural | Sentido do Giro | Pares de Base por Volta | Ocorrência e Características |
| :--- | :--- | :--- | :--- |
| **Forma B (Watson-Crick)** | Dextrogira (direita) | Cerca de 10,5 pares | Estrutura fisiológica preponderante em meio aquoso celular |
| **Forma A** | Dextrogira (direita) | Cerca de 11 pares | Duplexes híbridos DNA-RNA e amostras em desidratação |
| **Forma Z** | Levogira (esquerda) | Cerca de 12 pares | Sequências alternadas de purinas e pirimidinas; regulação gênica |

## Topologia, Desnaturação e Renaturação do DNA

O DNA pode ter sua dupla fita dissociada sem a quebra de ligações fosfodiéster covalentes por meio do processo de desnaturação (ou fusão térmica). Esse fenômeno ocorre mediante a elevação da temperatura do meio, alterações extremas de pH ou incubação com agentes caotrópicos que rompem as pontes de hidrogênio e as interações de empilhamento de bases. A separação das fitas é acompanhada pelo efeito hipercromômico, caracterizado pelo aumento acentuado da absorbância de luz ultravioleta no comprimento de onda de 260 nm, visto que as bases livres em fita simples absorvem mais radiação do que quando empilhadas no interior da dupla hélice.

O comportamento térmico do DNA é medido pela temperatura de fusão (Tm, melting temperature), definida operacionalmente como a temperatura na qual 50% das moléculas de dupla fita encontram-se desnaturadas em fitas simples. Como a ligação entre guanina e citosina envolve três pontes de hidrogênio e gera interações de empilhamento energeticamente mais fortes que a união entre adenina e timina (duas pontes), amostras de DNA com teor mais alto de pares G-C exibem valores proporcionalmente mais elevados de Tm. A desnaturação é um evento prontamente reversível: o resfriamento lento permite o reassociação exata das fitas complementares (renaturação ou anelamento), processo fundamental que embasa as técnicas de sondas de hibridação e reações de PCR.

No plano topológico celular, o DNA apresenta-se sob organização espacial linear nos cromossomos eucarióticos e circular covalentemente fechada em plasmídeos bacterianos e organelas citoplasmáticas. O desenrolamento da dupla fita durante a replicação e a transcrição induz tensões de torção que resultam em superenrolamentos (supercoiling). Essas tensões mecânicas são controladas pelas topoisomerases: as topoisomerases do tipo I cortam temporariamente apenas uma das fitas para desfazimento torsional sem consumo de ATP; as topoisomerases do tipo II (como a DNA girase) clivam simultaneamente as duas fitas da dupla hélice, permitindo a passagem de outro segmento de DNA com hidrólise concomitante de ATP.

## Mapa do capítulo

```mermaid Síntese de Biologia Molecular e Ácidos Nucleicos
flowchart TD
    A["Ácidos Nucleicos e Biologia Molecular"] --> B["Estrutura Química dos Nucleotídeos"]
    A --> C["Classes de RNA e Funções"]
    A --> D["Mecanismos da Transcrição"]
    A --> E["Processamento e Topologia do DNA"]

    B --> B1["Monômero: pentose + fosfato 5' + base nitrogenada 1'"]
    B --> B2["Purinas (A, G - 2 anéis) e Pirimidinas (C, T, U - 1 anel)"]
    B --> B3["DNA com desoxirribose e timina; RNA com ribose e uracila"]

    C --> C1["RNAr: estruturação ribossômica no nucléolo e ação de ribozima"]
    C --> C2["RNAm: transporte de matriz codificadora com trincas de códons"]
    C --> C3["RNAt: adaptador com extremidade 3'-CCA e alça do anticódon"]

    D --> D1["RNA polimerase sintetiza no sentido 5' para 3' lendo molde 3' para 5'"]
    D --> D2["Fases: iniciação com abertura da bolha, alongamento e terminação"]
    D --> D3["Procarionte: acoplamento e operon; Eucarionte: compartimentado"]

    E --> E1["Processamento do pré-RNAm: 5'-cap, cauda poli-A 3' e splicing"]
    E --> E2["DNA em dupla hélice antiparalela (A=T com 2 pontes, G-C com 3 pontes)"]
    E --> E3["Propriedades: Tm proporcional a G+C e topoisomerases tipo I e II"]
```

### Para fixar

- **Nucleotídeos:** Subunidades monoméricas formadas por pentose, fosfato ligado ao carbono 5' e base nitrogenada no carbono 1'.
- **Bases Nitrogenadas:** Purinas apresentam anel duplo fundido (A e G); pirimidinas apresentam anel simples hexagonal (C, T e U).
- **Distinção DNA e RNA:** DNA possui 2'-desoxirribose e timina; RNA apresenta D-ribose com hidroxila reativa em 2' e uracila.
- **Funções dos RNAs:** RNAr catalisa ligações peptídicas no ribossomo, RNAm transporta códons e RNAt atua como adaptador via anticódon.
- **Polaridade da Síntese:** A RNA polimerase sintetiza a fita no sentido 5' para 3', efetuando a leitura da fita molde de DNA de 3' para 5'.
- **Diferenças de Domínio:** Procariontes apresentam transcrição acoplada à tradução citoplasmática; eucariontes separam núcleo e citoplasma.
- **Maturação Eucariótica:** O pré-RNAm recebe capeamento 5', cauda de poliadenilação 3' e remoção de íntrons com união de éxons.
- **Splicing Alternativo:** Mecanismo nuclear que combina éxons de formas variáveis, gerando múltiplas proteínas a partir de um gene.
- **Dupla Hélice do DNA:** Fitas antiparalelas com interior hidrofóbico unidas por pareamentos de hidrogênio (A=T e G-C) e empilhamento de bases.
- **Desnaturação e Tm:** Ponto térmico de dissociação de 50% das fitas duplas, cujo valor eleva-se proporcionalmente ao conteúdo de pares G-C.
"""

path = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\content\material\biologia\m03\a03-s01.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("File written successfully.")
