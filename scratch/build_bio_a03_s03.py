import re

content = """---
id: "biologia/a03/s03"
volume: "biologia/m03"
capitulo: 7
titulo: "Código Genético, Tradução e Eletroforese"
fingerprint: {"startPage": 29, "endPage": 41, "startTopic": "Código genético e o processo de tradução – do RNAm à Proteína"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-32"
edital: ["geral:1.6", "geral:1.12"]
fontes: ["Material didático institucional CBMPE — Biologia Geral e Molecular — consultado em 2026-10-31"]
notas: "Código genético, tradução proteica, mutações e biologia molecular laboratorial: estrutura gênica eucariótica com íntrons, éxons, sítios reguladores e splicing alternativo; código genético em trincas de códons, universalidade e degeneração ou redundância; códon de iniciação AUG (metionina/N-formilmetionina) e códons de parada de tradução UAA, UAG e UGA; ribossomos celulares com subunidades e sítios funcionais A, P e E; etapas da tradução (iniciação com Shine-Dalgarno ou 5'-cap, elongação com catálise por peptidil transferase do RNAr e terminação por fatores de liberação RF/eRF); mutações pontuais por transição e transversão, lesões químicas espontâneas (desaminação, despurinação e dímeros de pirimidina por radiação UV); consequências funcionais: mutações silenciosas, missense (exemplo da anemia falciforme), nonsense e por deslocamento do quadro de leitura (frameshift); métodos forenses e laboratoriais de extração de DNA (fenol-clorofórmio com proteinase K e DTT, Chelex 100, papel FTA e colunas de sílica); e princípios da eletroforese em gel de agarose, poliacrilamida e eletroforese capilar (migração de ácidos nucleicos aniônicos em direção ao polo positivo/ânodo, marcadores de tamanho molecular e revelação por brometo de etídio sob luz ultravioleta)."
---

A síntese proteica é o processo celular central que traduz as sequências de nucleotídeos dos ácidos nucleicos na linguagem funcional dos aminoácidos. A correspondência entre o RNA mensageiro e a estrutura tridimensional das proteínas é regida pelo código genético, uma das mais expressivas evidências da origem biológica comum dos seres vivos. Simultaneamente, o conhecimento das mutações moleculares e o domínio de técnicas laboratoriais como a extração de ácidos nucleicos e a eletroforese consolidam as bases da biotecnologia moderna e da perícia forense, temas cobrados com alto rigor em exames técnicos e militares.

> [!objetivos]
> - Compreender a organização modular dos genes e o impacto do splicing alternativo na diversidade proteica.
> - Analisar as propriedades do código genético e correlacionar códons de iniciação e terminação.
> - Descrever minuciosamente as fases da tradução ribossômica e a dinâmica dos sítios catalíticos A, P e E.
> - Classificar os tipos de mutações gênicas e avaliar seus efeitos sobre a sequência de aminoácidos polipeptídica.
> - Dominar os métodos de extração de DNA e os princípios operacionais da eletroforese laboratorial e forense.

## Estrutura Modular dos Genes e Splicing

Nos organismos eucarióticos, a arquitetura dos genes não é contínua, apresentando uma alternância entre segmentos codificadores e sequências intercalares não codificadoras. Os segmentos que contêm as instruções que serão mantidas no RNA mensageiro maduro e traduzidas em polipeptídeos denominam-se **éxons** (do termo inglês expressed sequences). Em contraposição, as sequências intervenientes que são transcritas no núcleo, mas posteriormente removidas durante o processamento do transcrito primário, são chamadas de **íntrons** (do termo intervenient sequences).

Além dos éxons e íntrons, a unidade gênica compreende regiões regulatórias cruciais situadas nas extremidades da matriz de leitura aberta (ORF, Open Reading Frame). A montante do primeiro éxon localiza-se a região promotora, responsável pelo acoplamento da RNA polimerase e dos fatores de transcrição basais. Na extremidade oposta, sequências de terminação sinalizam o ponto no qual o complexo enzimático deve cessar a polimerização e desacoplar o transcrito primário.

A existência de íntrons viabiliza o mecanismo de **splicing alternativo**. Nesse processo nuclear, os éxons de um mesmo transcrito primário podem ser reunidos em combinações variadas. Como resultado, um único gene nuclear é capaz de codificar múltiplas variantes de RNA mensageiro maduro e produzir diversas isoformas proteicas com propriedades biológicas, afinidades enzimáticas e localizações teciduais distintas. Esse mecanismo explica por que o genoma humano, contendo cerca de vinte mil genes codificadores de proteínas, sintetiza mais de cem mil polipeptídeos diferentes.

| Componente Gênico | Natureza Estrutural | Papel Funcional na Expressão |
| :--- | :--- | :--- |
| **Promotor** | Sequência regulatória a montante (5') | Sítio de ligação de fatores de transcrição e da polimerase |
| **Éxons** | Sequências codificadoras conservadas | Preservadas no RNAm maduro para compor a matriz traduzida |
| **Íntrons** | Sequências intercalares não codificadoras | Removidas no núcleo pela ação do complexo spliceossomo |
| **Sítio Terminador** | Sequência regulatória a jusante (3') | Sinaliza a parada da transcrição e a clivagem do pré-RNAm |

## O Código Genético: Propriedades e Mecânica

O código genético é o dicionário biológico universal que estabelece as regras de correspondência entre as trincas de nucleotídeos presentes no RNA mensageiro, denominadas **códons**, e os vinte aminoácidos fundamentais que constituem as proteínas celulares. Como o RNA contém quatro bases nitrogenadas distintas (A, U, C e G), o arranjo em trincas gera exatamente 64 combinações possíveis de códons (quatro elevado à terceira potência), quantidade mais do que suficiente para codificar os vinte aminoácidos padrão.

O código genético é dotado de propriedades universais determinantes:

1. **Organização em Trincas:** A leitura da matriz do RNA mensageiro é realizada estritamente de três em três nucleotídeos, sem espaços vazios e sem sobreposição de bases adjacentes entre códons consecutivos.
2. **Degeneração ou Redundância:** Quase todos os aminoácidos são codificados por mais de um códon sinônimo. Por exemplo, a leucina e a arginina possuem seis códons diferentes cada uma. As únicas exceções são a metionina (codificada exclusivamente por AUG) e o triptofano (codificado apenas por UGG). Contudo, o código jamais é ambíguo: cada códon individual codifica um único aminoácido específico.
3. **Universalidade Quase Absoluta:** O significado de cada trinca de nucleotídeos é idêntico em praticamente todos os seres vivos da biosfera, desde as bactérias mais simples até os mamíferos superiores. Essa universalidade representa uma das evidências moleculares mais robustas da ancestralidade evolutiva comum e fundamenta a moderna engenharia genética de transgenia.

```mermaid Organização Lógica do Código Genético
flowchart TD
    DNA["DNA Genômico"] -->|Transcrição 5' para 3'| RNAm["RNA Mensageiro com Códons de Trincas"]
    RNAm -->|Leitura Ribossômica| CodonInic["AUG: Códon de Iniciação (Metionina)"]
    RNAm -->|Elongação Contínua| CodonsDeg["61 Códons Codificadores (Código Degenerado)"]
    RNAm -->|Terminação Estrita| CodonsParada["UAA, UAG e UGA: Códons de Parada (Fatores de Liberação)"]

    CodonInic --> Proteina["Polipeptídeo Funcional"]
    CodonsDeg --> Proteina
    CodonsParada --> Proteina
```

Entre os 64 códons existentes, 61 especificam aminoácidos. A síntese proteica é iniciada universalmente pelo códon **AUG**, que codifica o aminoácido metionina em eucariontes e a N-formilmetionina em bactérias. Os três códons restantes não codificam nenhum aminoácido: **UAA**, **UAG** e **UGA**. Essas trincas atuam como **códons de parada** (stop codons ou códons de terminação), sinalizando o término obrigatório da polimerização da cadeia polipeptídica.

> [!bizu]
> Mnemônico infalível para memorizar os três códons de parada no RNA mensageiro:
> - **UAA:** Você É Alto (*U Are Away*)
> - **UAG:** Você É Grande (*U Are Gone*)
> - **UGA:** Você É Gigante (*U Go Away*)
> Nenhum deles carrega aminoácido; sua função exclusiva é sinalizar a terminação traducional.

## Mecanismo da Tradução Ribossômica

A tradução celular ocorre no interior dos **ribossomos**, complexos ribonucleoproteicos presentes no citoplasma livre e aderidos às membranas do retículo endoplasmático rugoso (ergastoplasma). Cada ribossomo é estruturado por duas subunidades independentes: a subunidade menor, encarregada de acomodar o RNA mensageiro e inspecionar a fidelidade do pareamento códon-anticódon; e a subunidade maior, responsável por catalisar a formação da ligação peptídica.

No ribossomo completamente montado formam-se três sítios funcionais de ligação para moléculas de RNA transportador:

- **Sítio A (Aminoacil):** Sítio de entrada onde se acomoda o aminoacil-RNAt recém-chegado, carregando o próximo aminoácido a ser incorporado.
- **Sítio P (Peptidil):** Sítio intermediário que retém o peptidil-RNAt acoplado à cadeia polipeptídica em crescimento.
- **Sítio E (Exit ou Saída):** Sítio transitório que acomoda o RNAt desacilado (descarregado de aminoácido) antes de sua expulsão do ribossomo.

```mermaid Dinâmica dos Sítios Ribossômicos durante a Elongação
flowchart LR
    subgraph Ribossomo Completo
        E["Sítio E (Exit): saída do RNAt descarregado"]
        P["Sítio P (Peptidil): retém a cadeia polipeptídica nascente"]
        A["Sítio A (Aminoacil): entrada do novo aminoacil-RNAt"]
    end
    Entrada["Aminoacil-RNAt"] --> A
    A -->|Ligação Peptídica e Translocação| P
    P -->|Translocação com GTP| E
    E --> Liberacao["RNAt livre retorna ao citosol"]
```

A síntese polipeptídica desdobra-se em três etapas coordenadas:

1. **Iniciação:** A subunidade menor liga-se ao RNA mensageiro. Em procariontes, o alinhamento ocorre pela ligação do RNAr 16S à sequência de **Shine-Dalgarno** (rica em purinas) situada a montante do AUG, recrutando o RNAt iniciador carregado com N-formilmetionina. Nos eucariotos, o complexo de pré-iniciação reconhece a estrutura do **5'-cap** e desliza ao longo da fita (mecanismo de escaneamento) até identificar o primeiro códon AUG no contexto de uma sequência conservada de Kozak. Em seguida, a subunidade maior acopla-se, posicionando o RNAt iniciador diretamente no sítio P.
2. **Elongação:** Um aminoacil-RNAt com o anticódon complementar pareia com o códon exposto no sítio A com hidrólise de GTP. A enzima **peptidil transferase** (uma ribozima intrínseca do RNAr da subunidade maior) catalisa a formação da ligação peptídica, transferindo o peptídeo do sítio P para o aminoácido do sítio A. Em seguida, o ribossomo transloca-se exatamente três nucleotídeos na direção 5' para 3': o RNAt descarregado move-se para o sítio E e é ejetado, enquanto o RNAt portador da cadeia peptídica passa do sítio A para o sítio P, liberando o sítio A para o ciclo seguinte.
3. **Terminação:** Ao surgir um códon de parada (UAA, UAG ou UGA) no sítio A, proteínas citoplasmáticas denominadas **fatores de liberação** (RF em procariontes e eRF em eucariontes) ocupam o sítio A. Esses fatores catalisam a clivagem hidrolítica da ligação éster entre o polipeptídeo e o último RNAt no sítio P, liberando a proteína recém-formada e provocando a dissociação espontânea das subunidades ribossômicas.

| Etapa da Tradução | Eventos Bioquímicos Fundamentais | Fatores e Consumo Energético |
| :--- | :--- | :--- |
| **Iniciação** | Reconhecimento do RNAm (Shine-Dalgarno ou 5'-cap) e encaixe no AUG | Fatores IF ou eIF, hidrólise de GTP |
| **Elongação** | Entrada do aminoacil no sítio A, peptidil transferase e translocação | Fatores EF ou eEF, gasto de 2 GTP por ligação |
| **Terminação** | Reconhecimento do códon de parada e liberação do polipeptídeo | Fatores de liberação RF ou eRF com GTP |

> [!atencao]
> A ligação peptídica é catalisada pelo próprio RNA ribossômico (RNAr da subunidade maior), atuando como uma ribozima verdadeira. Além disso, múltiplos ribossomos podem ler simultaneamente a mesma molécula de RNA mensageiro em fila indiana, formando um complexo macromolecular denominado polirribossomo ou polissomo, otimizando a velocidade da produção celular.

## Mutações Gênicas e suas Repercussões Traducionais

As mutações consistem em modificações hereditárias ou permanentes na sequência de nucleotídeos do DNA que escapam aos sistemas de revisão e reparo celulares. Podem ocorrer espontaneamente por desvios tautoméricos ou ser provocadas por agentes mutagênicos (agentes genotóxicos) ambientais: agentes físicos (como radiação ultravioleta que gera dímeros de timina, e radiações ionizantes como raios X) ou agentes químicos (como análogos de bases e agentes intercalantes).

Quanto à substituição de uma única base nitrogenada por outra (mutação pontual), distinguem-se duas categorias de trocas:

- **Transição:** Substituição de uma base por outra da mesma família química, isto é, uma purina é trocada por outra purina (A por G ou G por A), ou uma pirimidina é trocada por outra pirimidina (C por T ou T por C).
- **Transversão:** Substituição de uma base por outra de família química distinta, envolvendo a troca de uma purina por uma pirimidina ou de uma pirimidina por uma purina (por exemplo, A trocada por C ou T trocada por G).

No que tange aos reflexos funcionais sobre a sequência de aminoácidos durante a tradução, as mutações pontuais classificam-se em:

1. **Mutação Silenciosa ou Sinônima:** A alteração do nucleotídeo gera um novo códon que, em razão da degeneração do código genético, codifica exatamente o mesmo aminoácido. A estrutura primária da proteína permanece inalterada e a mutação é fenotipicamente neutra.
2. **Mutação de Sentido Trocado (Missense ou Não Sinônima):** A alteração do nucleotídeo resulta em um códon que especifica um aminoácido diferente na cadeia polipeptídica. O impacto varia conforme a relevância biológica do resíduo modificado. O exemplo clássico é a **anemia falciforme**, causada pela troca pontual de adenina por timina no sexto códon do gene da beta-globina, substituindo o ácido glutâmico polar por uma valina hidrofóbica e provocando a polimerização da hemoglobina sob baixa oxigenação.
3. **Mutação Sem Sentido (Nonsense):** A modificação nucleotídica converte um códon que codificava um aminoácido em um dos três códons de parada precoces (UAA, UAG ou UGA). A síntese proteica é interrompida prematuramente, gerando um polipeptídeo truncado, geralmente desprovido de atividade biológica funcional.
4. **Mutação por Mudança da Matriz de Leitura (Frameshift):** Decorre da inserção ou deleção de um número de nucleotídeos que não seja múltiplo de três. Esse evento desalinha o enquadramento de leitura a partir daquele ponto em diante, alterando radicalmente todos os códons subsequentes e frequentemente criando um stop codon prematuro.

| Tipo de Mutação | Mecanismo Molecular | Consequência na Proteína |
| :--- | :--- | :--- |
| **Silenciosa** | Troca por códon sinônimo | Nenhuma; polipeptídeo tem sequência e função normais |
| **Missense** | Troca por códon de outro aminoácido | Substituição de resíduo; pode alterar função (ex: falciforme) |
| **Nonsense** | Criação precoce de códon de parada | Proteína truncada encurtada com perda de função |
| **Frameshift** | Inserção ou deleção não múltipla de três | Deslocamento da leitura alterando todos os resíduos posteriores |

> [!exemplo]
> Na anemia falciforme, a mutação na beta-globina transforma o códon 5'-GAG-3' (ácido glutâmico) em 5'-GUG-3' (valina). A presença do resíduo hidrofóbico exposto na superfície da molécula desencadeia a agregação das hemoglobinas desoxigenadas, deformando os eritrócitos na clássica conformação em foice (drepanócitos) que causa oclusão vascular e crises dolorosas agudas.

## Métodos de Extração e Purificação de DNA

As técnicas de biologia molecular dependem da obtenção de amostras purificadas e íntegras de DNA a partir de tecidos biológicos como sangue, saliva, raízes capilares, fragmentos ósseos e dentes (fundamentais na identificação médico-legal de cadáveres carbonizados ou em adiantado estado de putrefação). Qualquer protocolo de extração de ácidos nucleicos cumpre três etapas fundamentais: lise celular e tecidual, digestão de proteínas nucleares e purificação com separação dos interferentes biológicos.

Os principais procedimentos laboratoriais e forenses englobam:

- **Extração Orgânica (Fenol-Clorofórmio):** Método clássico considerado padrão ouro para amostras difíceis. Utiliza detergentes tensoativos como o SDS para dissolver as bicamadas lipídicas, EDTA para quelar íons divalentes e inativar nucleases, e DTT (ditiotreitol) para quebrar pontes dissulfeto resistentes (indispensável para romper a parede proteica de espermatozoides e separá-los de células epiteliais femininas em exames periciais de crimes sexuais). Emprega a enzima **proteinase K** para degradar histonas. Em seguida, a adição de fenol-clorofórmio-álcool isoamílico precipita as proteínas na interfase orgânica, mantendo o DNA na fase aquosa superior, o qual é finalmente precipitado com isopropanol ou etanol absoluto.
- **Extração por Resina Quelante (Chelex 100):** Emprega microesferas de poliestireno com grupos quelantes que sequestram com alta avidez cátions metálicos bivalentes (como Mg2+), inibindo permanentemente as enzimas nucleases endógenas. A amostra é aquecida a 100 °C, rompendo as membranas e desnaturando as fitas de DNA. Após centrifugação rápida, o sobrenadante límpido contendo DNA em fita simples é utilizado diretamente em reações de PCR, constituindo um método ágil, econômico e com risco mínimo de contaminação cruzada.
- **Papel FTA:** Matriz celulósica impregnada com substâncias químicas estabilizantes que provocam a lise das células depositadas, desnaturam proteínas e inativam patógenos virais e bacterianos. O DNA fica fisicamente imobilizado na trama das fibras do papel, podendo ser armazenado de forma estável em temperatura ambiente por anos. Para a análise, pequenos fragmentos do papel são recortados, lavados para remoção de inibidores e inseridos diretamente no tubo de amplificação.
- **Fase Sólida em Colunas de Sílica:** Método moderno e altamente automatizado. O DNA liberado liga-se seletivamente a uma membrana de sílica na presença de sais caotrópicos em pH ácido. Após etapas sequenciais de lavagem para eliminar contaminantes e inibidores celulares, o DNA purificado é eluído em solução tampão com pH alcalino ou água deionizada pura, oferecendo alto grau de pureza para testes de sequenciamento genético.

## Eletroforese: Princípios, Matrizes e Aplicações

A eletroforese é uma técnica laboratorial clássica que promove a separação física de macromoléculas biológicas (ácidos nucleicos e proteínas) em virtude de suas diferenças de tamanho molecular, conformação geométrica e carga elétrica líquida, impulsionadas pela aplicação de um campo elétrico uniforme em um suporte poroso imerso em solução tampão condutora.

No caso dos ácidos nucleicos, os grupos fosfato presentes na espinha dorsal das fitas encontram-se completamente ionizados em pH neutro ou alcalino, conferindo ao DNA e ao RNA uma **carga elétrica líquida uniformemente negativa**. Por essa razão, quando uma cuba eletroforética é conectada a uma fonte de corrente contínua, os fragmentos de ácidos nucleicos migram obrigatoriamente do polo negativo (cátodo) em direção ao **polo positivo (ânodo)**. Como a densidade de carga por nucleotídeo é praticamente constante, a matriz de suporte funciona como uma peneira molecular mecânica: os fragmentos menores de DNA atravessam os poros da malha com facilidade e migram mais rapidamente, enquanto os fragmentos maiores encontram maior resistência por atrito estérico e deslocam-se mais lentamente, ficando retidos mais próximos aos poços de aplicação.

```mermaid Dinâmica da Migração na Eletroforese em Gel
flowchart LR
    PoloNeg["Cátodo (-): Poços de Aplicação"] --> Gel["Matriz Porosa (Agarose ou Poliacrilamida)"]
    Gel --> FragGrandes["Fragmentos Maiores: Retidos Próximos aos Poços"]
    FragGrandes --> FragMedios["Fragmentos Médios: Migração Intermediária"]
    FragMedios --> FragPequenos["Fragmentos Menores: Alta Mobilidade Eletroforética"]
    FragPequenos --> PoloPos["Ânodo (+): Polo Positivo Atrator"]
```

Conforme a resolução espacial desejada, duas matrizes poliméricas são usualmente empregadas:

- **Gel de Agarose:** Polímero natural de polissacarídeo purificado de algas marinhas. Utilizado rotineiramente em concentrações entre 0,7% e 2% para a análise e controle de qualidade de produtos de digestão enzimática e fragmentos de PCR de tamanho médio (entre 100 e 20.000 pares de bases).
- **Gel de Poliacrilamida:** Matriz sintética formada pela polimerização de monômeros de acrilamida cruzados por bisacrilamida. Apresenta poros microscópicos muito menores e altamente uniformes, permitindo resolução discriminatória de altíssima precisão, capaz de separar fragmentos curtos de ácidos nucleicos que apresentem diferença de apenas um único nucleotídeo.

Para estimar a massa molecular e a extensão exata dos fragmentos separados, aplica-se concomitantemente em uma das canaletas do gel um padrão de referência denominado **ladder** (marcador de peso molecular), composto por fragmentos de DNA com comprimentos pré-determinados. Para a visualização dos fragmentos após a corrida, utiliza-se agentes intercalantes fluorescentes como o **brometo de etídio** ou corantes mais modernos (GelRed e SYBR Safe), que se intercalam entre as bases nitrogenadas e emitem fluorescência visível alaranjada quando submetidos à radiação de luz ultravioleta (UV) em um transiluminador.

Na genética forense moderna para exames de identificação criminal e paternidade, a metodologia foi refinada com a **eletroforese capilar**. O procedimento ocorre no interior de tubos capilares ultrafinos preenchidos com polímero fluido, nos quais fragmentos de marcadores microssatélites (STRs, Short Tandem Repeats) marcados com fluoróforos distintos são tracionados em alta voltagem e detectados automaticamente por um sensor a laser, gerando gráficos de picos conhecidos como eletroferogramas.

> [!resolvido]
> **Questão Conceitual:** Em uma cuba eletroforética contendo gel de agarose submetida a campo elétrico, um fragmento de DNA amplificado por PCR de 350 pares de bases migrará mais ou menos rapidamente do que um fragmento genômico de 1.200 pares de bases?
> **Resolução:** Como o DNA possui carga elétrica líquida negativa uniforme em virtude de seus grupos fosfato, a mobilidade no gel é governada pelo tamanho molecular. O fragmento de 350 pares de bases migrará substancialmente mais rápido em direção ao polo positivo (ânodo) do que o fragmento de 1.200 pares de bases, pois atravessa os poros microscópicos da agarose com menor resistência mecânica por atrito.

## Mapa do capítulo

```mermaid Síntese de Tradução, Mutações e Eletroforese
flowchart TD
    A["Expressão Proteica e Biologia Molecular Laboratorial"] --> B["Código Genético e Propriedades"]
    A --> C["Dinâmica da Tradução Ribossômica"]
    A --> D["Mutações Gênicas e Tipos"]
    A --> E["Extração e Eletroforese de DNA"]

    B --> B1["Leitura em trincas de códons no RNAm (5' para 3')"]
    B --> B2["Universalidade evolutiva e degeneração/redundância"]
    B --> B3["Iniciação AUG e parada UAA, UAG e UGA"]

    C --> C1["Ribossomo com sítios A (aminoacil), P (peptidil) e E (saída)"]
    C --> C2["Iniciação: Shine-Dalgarno bacteriano ou 5'-cap eucarioto"]
    C --> C3["Elongação com peptidil transferase do RNAr e translocação"]

    D --> D1["Transição (mesma família) versus transversão (famílias opostas)"]
    D --> D2["Silenciosa, missense (anemia falciforme) e nonsense"]
    D --> D3["Frameshift por inserções ou deleções não múltiplas de 3"]

    E --> E1["Extração: fenol-clorofórmio, Chelex 100, papel FTA e sílica"]
    E --> E2["DNA negativo migra para o polo positivo (ânodo)"]
    E --> E3["Matrizes: agarose e poliacrilamida; revelação por intercalantes"]
```

### Para fixar

- **Íntrons e Éxons:** Éxons contêm sequências codificadoras mantidas no RNAm; íntrons são excisados no núcleo pelo spliceossomo.
- **Splicing Alternativo:** Combinação diferencial de éxons que permite a um único gene gerar múltiplas variantes polipeptídicas.
- **Propriedades do Código:** Organizado em trincas, degenerado (múltiplos códons por aminoácido) e praticamente universal.
- **Códons Reguladores:** AUG inicia a tradução codificando metionina; UAA, UAG e UGA atuam como sinais estritos de parada.
- **Sítios do Ribossomo:** Sítio A recebe o aminoacil-RNAt, sítio P ancora o peptídeo e sítio E descarrega o RNAt livre.
- **Peptidil Transferase:** Atividade enzimática catalítica do RNAr da subunidade maior que forja a ligação peptídica.
- **Mutações Pontuais:** Transições trocam bases da mesma família; transversões substituem purinas por pirimidinas ou vice-versa.
- **Impactos Funcionais:** Missense altera o aminoácido (anemia falciforme); nonsense gera parada precoce; frameshift altera o enquadramento.
- **Métodos de Extração:** Fenol-clorofórmio clássico com proteinase K e DTT; Chelex quelante de íons; papel FTA para guarda ambiente.
- **Migração Eletroforética:** DNA com carga negativa migra para o ânodo positivo, separando-se pelo atrito nos poros da matriz.
"""

path = r"c:\Users\Administrador\Documents\Projetos\CFO-BM\content\material\biologia\m03\a03-s03.md"
with open(path, "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")

print("File written successfully.")
