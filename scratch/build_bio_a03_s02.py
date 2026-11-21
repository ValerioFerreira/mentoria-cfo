import re

content = """---
id: "biologia/a03/s02"
volume: "biologia/m03"
capitulo: 6
titulo: "Replicação do DNA, Estrutura Cromossômica e Anomalias"
fingerprint: {"startPage": 16, "endPage": 28, "startTopic": "A replicação do DNA"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-32"
edital: ["geral:1.6"]
fontes: ["Material didático institucional CBMPE — Biologia Geral e Molecular — consultado em 2026-10-31"]
notas: "Replicação do DNA, organização cromossômica e mutações: modelo semiconservativo demonstrado por Meselson e Stahl; forquilha de replicação e enzimas (helicase, proteínas SSB, topoisomerases/girases, primase com síntese de primers de RNA, DNA polimerase no sentido 5' para 3' com adição na ponta 3'-OH); síntese semidescontínua: fita líder contínua versus fita atrasada descontínua formada por fragmentos de Okazaki unidos pela DNA ligase; fidelidade de cópia, atividade exonucleolítica revisora 3' para 5' e sistemas de reparo celular (reparo por excisão de nucleotídeos e xeroderma pigmentoso por dímeros de timina induzidos por radiação UV); empacotamento da cromatina (eucromatina versus heterocromatina, octâmero de histonas no nucleossomo e histona H1); morfologia cromossômica (centrômero, cinetócoro, telômeros, braços p e q) e classificação (metacêntrico, submetacêntrico, acrocêntrico e telocêntrico); cariótipo humano em metáfase (46 cromossomos, 44 autossomos e 2 sexuais); anomalias cromossômicas numéricas (aneuploidias por não disjunção meiótica: Síndrome de Down trissomia do 21, Turner 45,X, Klinefelter 47,XXY) e estruturais (deleções como Cri-du-chat, duplicações, inversões e translocações); e conceito contemporâneo de gene e fluxo do dogma central da biologia molecular."
---

A duplicação fidedigna do genoma e a correta segregação dos cromossomos constituem pilares indispensáveis para a continuidade da vida e para a estabilidade celular. O processo de replicação do DNA coordena uma sofisticada bateria de enzimas especializadas que copiam bilhões de nucleotídeos com precisão extrema, minimizando a ocorrência de mutações deletérias. Paralelamente, o estudo da organização física da cromatina, da morfologia dos cromossomos e das anomalias numéricas e estruturais fundamenta a compreensão de patologias genéticas de alto impacto biomédico e pericial, assunto recorrente em provas de concurso.

> [!objetivos]
> - Compreender o modelo semiconservativo e a dinâmica enzimática da forquilha de replicação do DNA.
> - Diferenciar a síntese da fita líder da síntese descontínua da fita atrasada em fragmentos de Okazaki.
> - Analisar os mecanismos de fidelidade replicativa, a atividade exonucleolítica 3' para 5' e as vias de reparo do DNA.
> - Caracterizar a arquitetura cromossômica, os níveis de condensação da cromatina e o cariótipo humano normal.
> - Identificar as principais anomalias cromossômicas numéricas e estruturais, correlacionando-as com suas síndromes clínicas.

## O Modelo Semiconservativo e a Forquilha de Replicação

A elucidação da dupla hélice por Watson e Crick sugeriu de imediato um modelo mecânico para a replicação do material genético: as duas fitas da molécula parental separam-se, servindo cada uma como molde direto para a montagem de uma nova cadeia complementar. Esse modelo semiconservativo foi comprovado experimentalmente em 1958 por Matthew Meselson e Franklin Stahl, utilizando marcação isotópica com nitrogênio pesado (N-15) e leve (N-14) em bactérias submetidas à centrifugação em gradiente de densidade. O resultado demonstrou que cada molécula-filha preserva exatamente uma fita original intacta e uma fita recém-sintetizada.

O evento de replicação inicia-se em sequências genômicas específicas denominadas origens de replicação (ori). Em procariontes, que possuem um cromossomo circular único, existe uma origem exclusiva (oriC de aproximadamente 245 pares de bases), a partir da qual duas forquilhas de replicação progridem bidirecionalmente até se encontrarem na região de término. Nos eucariotos, em virtude da enorme extensão linear do genoma associado a proteínas histonas, a replicação opera simultaneamente a partir de milhares de origens distribuídas ao longo de cada cromossomo, agilizando a duplicação total durante a fase S da intérfase.

A abertura da dupla fita no sítio de origem requer a ação de enzimas e proteínas acessórias integradas na forquilha de replicação:

1. **DNA Helicase:** Enzima que se desloca ao longo do DNA rompendo as pontes de hidrogênio entre as bases nitrogenadas com gasto de energia proveniente da hidrólise de ATP, promovendo a separação física das fitas.
2. **Proteínas SSB (Single-Stranded Binding Proteins):** Proteínas de ligação à fita simples que recobrem o DNA desnaturado, impedindo que as fitas complementares se reassociem espontaneamente ou sofram clivagem por nucleases citoplasmáticas.
3. **Topoisomerases (Girase bacteriana):** À medida que a helicase avança, o desenrolamento mecânico acumula superenrolamentos positivos e tensão de torção à frente da forquilha. As topoisomerases aliviam essa tensão realizando quebras transitórias em uma ou ambas as fitas do DNA e religando-as em seguida.

```mermaid Dinâmica das Enzimas na Forquilha de Replicação
flowchart LR
    DNA["Dupla Hélice Parental"] --> Topo["Topoisomerase: alívio do estresse torsional"]
    Topo --> Heli["Helicase: abertura de pontes de H com ATP"]
    Heli --> SSB["Proteínas SSB: estabilização da fita simples"]
    SSB --> Prima["Primase: síntese de primers de RNA"]
    Prima --> Pol["DNA Polimerase: síntese no sentido 5' para 3'"]
    Pol --> Liga["DNA Ligase: selamento fosfodiéster"]
```

## Síntese Semidescontínua e Enzimas Polimerases

Todas as DNA polimerases celulares conhecidas compartilham duas restrições bioquímicas rígidas: não conseguem iniciar uma cadeia polinucleotídica do zero, necessitando de uma ponta 3'-OH pré-existente (iniciador ou primer), e catalisam a polimerização exclusivamente no sentido 5' para 3'. O ataque nucleofílico ocorre a partir da hidroxila livre do carbono 3' da pentose sobre o grupo fosfato alfa do desoxirribonucleotídeo trifosfatado (dNTP) entrante, liberando pirofosfato inorgânico.

Para viabilizar o início da síntese, a enzima RNA primase sintetiza um pequeno oligonucleotídeo iniciador de RNA (primer), de cerca de 10 a 15 nucleotídeos, que fornece a extremidade 3'-OH livre necessária para o ancoramento da DNA polimerase III (a principal enzima de síntese replicativa bacteriana).

Como as duas fitas da dupla hélice parental são antiparalelas e a forquilha de replicação progride em sentido único, a síntese do DNA ocorre por uma modalidade denominada semidescontínua:

- **Fita Líder (leading strand):** Sua fita molde orienta-se no sentido 3' para 5' na direção do avanço da forquilha. A síntese do DNA procede de forma contínua no sentido 5' para 3', demandando apenas um primer inicial de RNA na origem.
- **Fita Atrasada ou Retardada (lagging strand):** Sua fita molde expõe-se no sentido 5' para 3' em relação ao avanço da forquilha. A síntese é descontínua e orienta-se no sentido oposto à movimentação da forquilha, ocorrendo pela produção seriada de múltiplos segmentos curtos denominados fragmentos de Okazaki. Cada fragmento necessita de um primer de RNA individual sintetizado pela primase.

Posteriormente, a DNA polimerase I bacteriana remove os primers de RNA por sua atividade exonucleolítica 5' para 3' e preenche as lacunas com desoxirribonucleotídeos (processo denominado nick translation). Em seguida, a enzima DNA ligase sela as descontinuidades remanescentes na cadeia, forjando a ligação fosfodiéster covalente final entre a hidroxila 3' de um fragmento e o fosfato 5' do fragmento adjacente com consumo de ATP ou NAD+.

| Enzima Replicativa | Função Bioquímica Principal | Atividade Exonucleolítica |
| :--- | :--- | :--- |
| **DNA Helicase** | Rompe pontes de hidrogênio e separa a dupla hélice | Não possui atividade nuclease |
| **RNA Primase** | Sintetiza primers curtos de RNA com hidroxila 3'-OH | Não possui atividade revisora |
| **DNA Polimerase III** | Principal polimerase de elongação replicativa em bactérias | Exonuclease 3' para 5' (revisão de cópia) |
| **DNA Polimerase I** | Degradação de primers e preenchimento de lacunas | Exonuclease 5' para 3' e 3' para 5' |
| **DNA Ligase** | Catalisa a formação da ligação fosfodiéster entre fragmentos | Não possui atividade catalítica de síntese |

> [!atencao]
> Tenha em mente a distinção fundamental de direção: a DNA polimerase desloca-se lendo a fita molde no sentido 3' para 5', mas adiciona nucleotídeos na cadeia nova estritamente no sentido 5' para 3'. Jamais assinale alternativas que indiquem síntese no sentido 3' para 5'.

## Mecanismos de Reparo e Fidelidade da Replicação

A sobrevivência celular exige que a replicação do genoma atinja índices ínfimos de erro. Durante a incorporação primária pelas polimerases, a taxa de pareamento errôneo é de cerca de um erro para cada 10.000 ou 100.000 pares de bases adicionados, decorrente em grande parte da transição transitória de formas tautoméricas anômalas das bases nitrogenadas (como formas imino e enol).

Para corrigir esses equívocos antes da conclusão da síntese, as principais DNA polimerases replicativas são dotadas de atividade de revisão intrínseca (proofreading), mediada por um domínio com função de exonuclease 3' para 5'. Quando um nucleotídeo incorreto é incorporado, a extremidade 3' desemparelhada sofre instabilidade física que trava o centro ativo de síntese. A enzima retrocede um passo, seu sítio exonucleolítico cliva o nucleotídeo distorcido e o centro catalítico retoma a síntese correta, reduzindo a taxa residual de erros para apenas um em cada 10 milhões de pares de bases.

Após a forquilha de replicação passar, sistemas adicionais de reparo de DNA entram em atividade no nucleoplasma para manter a integridade genômica frente a danos endógenos e agressões ambientais:

- **Reparo de Malpareamento (Mismatch Repair - MMR):** Reconhece distorções estruturais na hélice causadas por nucleotídeos errôneos que escaparam à revisão da polimerase. Em bactérias, o sistema distingue a fita original da fita recém-sintetizada pelo padrão temporário de metilação em resíduos de adenina, degradando apenas o segmento da fita nova incorreta.
- **Reparo por Excisão de Bases (BER):** Atua na correção de bases danificadas por oxidação, alquilação ou desaminação espontânea. A enzima DNA glicosilase cliva a base alterada gerando um sítio apurínico ou apirimidínico (sítio AP), que é em seguida reconhecido por endonucleases AP, preenchido por polimerase e selado por ligase.
- **Reparo por Excisão de Nucleotídeos (NER):** Remove lesões volumosas que desestruturam a dupla hélice, com destaque para os dímeros de pirimidina (ligações anômalas entre timinas adjacentes) induzidos por exposição à radiação ultravioleta (UV). Um complexo enzimático promove incisões de dupla fita ladeando a lesão, remove um oligonucleotídeo contendo o defeito e permite que a polimerase e a ligase reconstituam a integridade local.

```mermaid Vias Principais de Reparo do DNA
flowchart TD
    Dano["Lesão ou Erro na Molécula de DNA"] --> Proof["Revisão Imediata pela Polimerase: exonuclease 3' para 5'"]
    Dano --> MMR["Mismatch Repair: correção de malpareamento pós-síntese"]
    Dano --> BER["Reparo por Excisão de Bases: remoção de base alterada por glicosilase"]
    Dano --> NER["Reparo por Excisão de Nucleotídeos: excisão de dímeros de pirimidina induzidos por UV"]

    Proof --> Integridade["Manutenção da Integridade Genômica"]
    MMR --> Integridade
    BER --> Integridade
    NER --> Integridade
```

> [!bizu]
> O **xeroderma pigmentoso** é o exemplo patológico clássico mais frequente em concursos sobre reparo de DNA. Trata-se de uma síndrome genética autossômica recessiva originada por mutações inativadoras nos genes do reparo por excisão de nucleotídeos (NER). Incapazes de remover dímeros de timina induzidos por radiação UV solar, os pacientes apresentam sensibilidade solar extrema e incidência precocíssima de neoplasias cutâneas graves.

## Estrutura e Condensação Cromossômica

Nos organismos eucarióticos, a extensão física total do DNA nuclear de uma única célula somática humana supera dois metros de comprimento. Para acomodar esse volume no interior de um núcleo que mede apenas alguns micrômetros de diâmetro, o DNA associa-se a proteínas estruturais formando um complexo macromolecular denominado cromatina.

A unidade estrutural fundamental de empacotamento da cromatina é o **nucleossomo**, visualizado ao microscópio eletrônico sob a clássica morfologia de contas em um colar. Cada nucleossomo é composto por um cerne proteico octamérico formado por dois pares de cada uma das histonas centrais (H2A, H2B, H3 e H4). Em torno desse núcleo octamérico enrolam-se aproximadamente 146 a 147 pares de bases de DNA de dupla fita, executando quase duas voltas completas. As histonas são proteínas de caráter marcadamente básico, enriquecidas nos aminoácidos lisina e arginina, cujas cargas líquidas positivas interagem fortemente com as cargas negativas dos grupos fosfato da espinha dorsal do DNA.

Entre nucleossomos adjacentes localiza-se o DNA de ligação (linker DNA), associado à histona H1. A interação da histona H1 promove a aproximação dos nucleossomos, condensando o filamento de 10 nm na fibra de 30 nm (solenoide), a qual subsequently se organiza em alças presas a uma matriz nuclear não histônica (scaffold proteico) até atingir o grau máximo de condensação visível no cromossomo metafásico.

Conforme o grau de empacotamento físico e a atividade transcricional, a cromatina classifica-se em dois compartimentos funcionais:

- **Eucromatina:** Fração menos condensada da cromatina, dispersa pelo nucleoplasma durante a intérfase. Apresenta fita de DNA acessível aos fatores de transcrição basais e às RNA polimerases, abrigando a maioria dos genes metabolicamente ativos da célula.
- **Heterocromatina:** Fração densamente empacotada e condensada ao longo de todo o ciclo celular, caracterizada por inatividade transcricional. Subdivide-se em **heterocromatina constitutiva**, permanentemente condensada em todas as células (como nas regiões centroméricas e teloméricas ricas em DNA repetitivo), e **heterocromatina facultativa**, que pode se condensar ou descondensar em momentos específicos do desenvolvimento ou em tipos celulares distintos (como o corpúsculo de Barr, que representa a inativação aleatória de um dos cromossomos X nas células somáticas femininas).

| Nível de Organização | Componentes Principais | Diâmetro Estrutural | Estado Funcional |
| :--- | :--- | :--- | :--- |
| **Dupla Hélice de DNA** | Desoxirribonucleotídeos pareados | Cerca de 2 nm | Molécula nua não empacotada |
| **Nucleossomos ("Contas")** | Octâmero de histonas (H2A, H2B, H3, H4) e DNA | Cerca de 10 a 11 nm | Eucromatina ativa e acessível |
| **Fibra Cromatínica** | Nucleossomos compactados pela histona H1 | Cerca de 30 nm | Grau intermediário de empacotamento |
| **Cromossomo Metafásico** | Alças condensadas sobre esqueleto não histônico | Cerca de 1.400 nm | Condensação máxima para segregação meiótica/mitótica |

## Morfologia dos Cromossomos e Cariótipo Humano

Durante a metáfase da divisão celular, a condensação cromossômica alcança seu ponto culminante, tornando os cromossomos individualizados e facilmente visíveis à microscopia óptica. A morfologia externa de um cromossomo metafásico duplicado compõe-se de duas cromátides-irmãs rigorosamente idênticas, unidas na região do centrômero.

O centrômero ou constrição primária abriga o cinetócoro, uma estrutura proteica especializada em forma de disco que ancora os microtúbulos do fuso mitótico encarregados de tracionar as cromátides para os polos celulares opostos durante a anáfase. As extremidades terminais dos cromossomos são denominadas telômeros, segmentos de sequências repetitivas ricas em guanina (TTAGGG em humanos) que protegem a molécula linear contra a degradação e fusões anômalas, compensando o encurtamento gerado pela perda de primers durante a replicação terminal da fita atrasada através da enzima telomerase.

A posição relativa do centrômero divide o cromossomo em dois braços: o braço curto (designado pela letra p, do francês petit) e o braço longo (designado pela letra q). Conforme o índice centromérico e a razão de comprimento entre os braços, os cromossomos classificam-se em quatro tipos fundamentais:

1. **Metacêntrico:** O centrômero ocupa posição exatamente central ou mediana, delimitando braços p e q de comprimentos virtuais idênticos.
2. **Submetacêntrico:** O centrômero posiciona-se ligeiramente deslocado do centro, estabelecendo um braço curto p nitidamente menor que o braço longo q.
3. **Acrocêntrico:** O centrômero situa-se muito próximo a uma das extremidades, gerando um braço curto extremamente diminuto (que frequentemente ostenta constrições secundárias e satélites contendo genes para RNAr) e um braço longo proeminente.
4. **Telocêntrico:** O centrômero situa-se estritamente na extremidade terminal do cromossomo, inexistindo braço curto. Este tipo não ocorre no cariótipo humano normal, existindo em outras espécies de mamíferos como camundongos.

O cariótipo consiste no conjunto cromossômico característico de uma espécie ou indivíduo, analisado quanto ao número, tamanho e morfologia dos cromossomos. Em seres humanos, as células somáticas normais são diploides (2n), contendo 46 cromossomos distribuídos em 23 pares: 22 pares de cromossomos autossômicos (iguais em ambos os sexos, numerados de 1 a 22 por ordem decrescente de tamanho) e um par de cromossomos sexuais ou heterossomos (XX no sexo feminino e XY no sexo masculino). Os gametas maduros (espermatozoides e óvulos) são haploides (n), apresentando 23 cromossomos (22 autossomos e 1 sexual).

> [!exemplo]
> Para a montagem laboratorial do cariótipo humano, leucócitos sanguíneos são cultivados e estimulados à mitose. Adiciona-se a droga colchicina, que inibe a polimerização da tubulina e desfaz o fuso mitótico, bloqueando as células na metáfase. Após choque hipotônico e coloração por bandas (como o bandeamento G), os cromossomos são fotografados e pareados segundo o tamanho e o padrão de bandas.

## Anomalias Cromossômicas Numéricas e Estruturais

Alterações no cariótipo podem decorrer de erros ocorridos durante a gametogênese ou nas divisões mitóticas iniciais do embrião. Essas aberrações cromossômicas dividem-se em numéricas e estruturais.

As anomalias numéricas originam-se predominantemente pela **não disjunção meiótica**, fenômeno no qual um par de cromossomos homólogos falha em se separar durante a anáfase I, ou cromátides-irmãs não se separam durante a anáfase II. Como consequência, formam-se gametas que carregam um cromossomo a mais (n + 1) ou a menos (n - 1), gerando aneuploidias após a fecundação:

- **Síndrome de Down (Trissomia do 21):** Caracterizada pela presença de três cópias do cromossomo 21, totalizando cariótipo 47,XX,+21 ou 47,XY,+21. Clinicamente cursa com hipotonia muscular, prega palmar única transversal, fendas palpebrais oblíquas, cardiopatias congênitas e déficit intelectual variável. A incidência eleva-se progressivamente com o avanço da idade materna.
- **Síndrome de Turner (Monossomia do X):** Única monossomia viável em humanos, afetando indivíduos do sexo feminino portadores de cariótipo 45,X. Apresentam baixa estatura marcante, pescoço alado, tórax largo com mamilos amplamente espaçados, disgenesia gonadal (ovários em fita), amenorreia primária e esterilidade.
- **Síndrome de Klinefelter (Cariótipo 47,XXY):** Afeta indivíduos com fenótipo masculino que herdam um cromossomo X supranumerário. Caracteriza-se por estatura elevada, hipogonadismo, testículos diminutos, ginecomastia na puberdade, azoospermia e infertilidade.

As anomalias estruturais decorrem de quebras cromossômicas seguidas de religamento incorreto ou de permutações anômalas entre cromossomos não homólogos:

- **Deleção:** Perda de um segmento cromossômico, como na **Síndrome de Cri-du-chat** (miado do gato), decorrente da deleção parcial do braço curto do cromossomo 5 (cariótipo 5p-).
- **Duplicação:** Presença de segmento cromossômico repetido em duplicidade.
- **Inversão:** Um segmento cromossômico sofre duas quebras, roda 180 graus e se reintegra invertido. É dita paracêntrica quando não engloba o centrômero e pericêntrica quando inclui a região centromérica.
- **Translocação:** Troca de fragmentos entre cromossomos não homólogos. Destaca-se a **translocação Robertsoniana**, que ocorre pela fusão dos braços longos de dois cromossomos acrocêntricos (como 14 e 21), com perda dos braços curtos diminutos. Portadores equilibrados de translocação Robertsoniana possuem 45 cromossomos e fenótipo normal, mas têm risco aumentado de gerar filhos com síndrome de Down por translocação.

| Alteração Cromossômica | Classificação Genética | Cariótipo Típico | Manifestações Clínicas Notáveis |
| :--- | :--- | :--- | :--- |
| **Síndrome de Down** | Aneuploidia (trissomia autossômica) | 47,XX,+21 ou 47,XY,+21 | Hipotonia, fenda palpebral oblíqua, cardiopatia congênita |
| **Síndrome de Turner** | Aneuploidia (monossomia sexual) | 45,X | Sexo feminino, baixa estatura, pescoço alado, ovários em fita |
| **Síndrome de Klinefelter** | Aneuploidia (trissomia sexual) | 47,XXY | Sexo masculino, hipogonadismo, ginecomastia, azoospermia |
| **Síndrome de Cri-du-chat** | Anomalia estrutural (deleção) | 46,XX,del(5p) ou 46,XY | Choro agudo característico, microcefalia, retardo grave |
| **Translocação Robertsoniana** | Anomalia estrutural (fusão cêntrica) | 45 cromossomos (portador sadio) | Envolve acrocêntricos; pode gerar trissomia não disjuncional |

## O Conceito de Gene e o Dogma Central

O conceito de gene evoluiu consideravelmente desde a formulação das unidades particuladas da hereditariedade propostas por Gregor Mendel. Ao longo do século XX, prevaleceu temporariamente a hipótese de George Beadle e Edward Tatum sintetizada no axioma "um gene, uma enzima", posteriormente ampliada para "um gene, um polipeptídeo".

Na biologia molecular contemporânea, o conceito de gene define-se como uma sequência contínua ou descontínua de nucleotídeos de DNA que contém as informações necessárias para direcionar a síntese de um produto biológico funcional, o qual pode ser uma cadeia polipeptídica ou uma molécula de RNA não codificante dotada de papel regulador ou catalítico (tais como RNAr, RNAt, microRNAs e lncRNAs). A região cromossômica física ocupada por um gene específico é designada loco gênico (locus), e as versões alternativas de sequências que podem existir em um mesmo loco na população constituem os alelos.

O fluxo de informações biológicas no interior das células é formalizado pelo **Dogma Central da Biologia Molecular**, postulado originalmente por Francis Crick:

1. **Replicação:** O DNA direciona a cópia fidedigna de si próprio, assegurando a transmissão hereditária.
2. **Transcrição:** A informação codificada na fita molde do DNA é transcrita para uma molécula de RNA mensageiro.
3. **Tradução:** O maquinário ribossômico decodifica as trincas de códons do RNA mensageiro para polimerizar uma sequência linear de aminoácidos em uma proteína funcional.

A formulação original do dogma foi atualizada pela descoberta de fluxos de informação excepcionais. Em retrovírus (como o vírus do HIV), o RNA genômico viral é retrotranscrito em DNA complementar de fita dupla mediante a enzima viral **transcriptase reversa** (DNA polimerase dependente de RNA). Em outros vírus de RNA, a replicação do genoma opera diretamente de RNA para RNA através de RNA polimerases dependentes de RNA. Destaca-se ainda o fenômeno da **pleiotropia**, no qual um único gene mutado desencadeia simultaneamente múltiplos efeitos fenotípicos não correlacionados em órgãos distintos, como ocorre na fenilcetonúria e na anemia falciforme.

> [!resolvido]
> **Questão Conceitual:** Uma célula somática humana feminina em metáfase mitótica normal apresenta qual quantitativo total de moléculas de DNA de dupla fita e cromátides?
> **Resolução:** A célula diploide humana possui 46 cromossomos. Na fase S da intérfase, cada cromossomo duplica seu material genético. Assim, na metáfase mitótica, a célula exibe 46 cromossomos duplicados, compostos por 92 cromátides-irmãs, correspondendo exatamente a 92 moléculas individuais de DNA de fita dupla.

## Mapa do capítulo

```mermaid Síntese de Replicação do DNA e Citogenética
flowchart TD
    A["Replicação do DNA e Citogenética"] --> B["Forquilha Replicativa e Enzimas"]
    A --> C["Sistemas de Fidelidade e Reparo"]
    A --> D["Organização da Cromatina"]
    A --> E["Anomalias Cromossômicas"]

    B --> B1["Replicação semiconservativa no sentido 5' para 3'"]
    B --> B2["Fita líder contínua e fita atrasada em fragmentos de Okazaki"]
    B --> B3["Helicase, SSB, primase, DNA polimerases e ligase"]

    C --> C1["Proofreading por exonuclease 3' para 5' da polimerase"]
    C --> C2["Reparo NER com falha no xeroderma pigmentoso"]
    C --> C3["Reparo BER de bases e mismatch repair de pareamento"]

    D --> D1["Nucleossomo: octâmero de histonas H2A, H2B, H3, H4 com DNA"]
    D --> D2["Eucromatina ativa e heterocromatina condensada"]
    D --> D3["Cromossomos: metacêntrico, submetacêntrico, acrocêntrico"]

    E --> E1["Aneuploidias: Síndrome de Down (47,XX/XY,+21)"]
    E --> E2["Aneuploidias sexuais: Turner (45,X) e Klinefelter (47,XXY)"]
    E --> E3["Estruturais: deleção (Cri-du-chat 5p-) e translocações"]
```

### Para fixar

- **Modelo Semiconservativo:** Cada nova dupla hélice conserva uma fita parental intacta emparelhada com uma fita recém-sintetizada.
- **Direcionalidade da Síntese:** As DNA polimerases polimerizam exclusivamente de 5' para 3', promovendo ataque na ponta 3'-OH livre.
- **Fita Líder e Fita Atrasada:** A fita líder sintetiza-se de forma contínua; a fita retardada é descontínua em fragmentos de Okazaki.
- **Atividade de Revisão:** A exonuclease 3' para 5' da DNA polimerase corrige bases trocadas, elevando a fidelidade da cópia.
- **Xeroderma Pigmentoso:** Erro congênito no reparo por excisão de nucleotídeos (NER) que impede a remoção de dímeros de timina por UV.
- **Nucleossomos:** Unidades de cromatina formadas por octâmeros de histonas básicas circundados por cerca de 147 pares de bases de DNA.
- **Morfologia Cromossômica:** Classificação pela posição do centrômero em metacêntrico, submetacêntrico, acrocêntrico e telocêntrico.
- **Cariótipo Humano:** Células somáticas apresentam 46 cromossomos (44 autossomos e 2 sexuais); gametas apresentam 23 cromossomos.
- **Síndromes Numéricas:** Down (trissomia do 21), Turner (monossomia 45,X) e Klinefelter (trissomia sexual 47,XXY).
- **Dogma Central:** O fluxo clássico da informação genética transita de DNA para RNAm e deste para Proteína, admitindo transcrição reversa.
"""

path = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\content\material\biologia\m03\a03-s02.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("File written successfully.")
