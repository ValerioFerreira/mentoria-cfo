# build_bio_m05_ch3.py
# Generates a05-s03.md for biologia/m05

content = '''---
id: "biologia/a05/s03"
volume: "biologia/m05"
capitulo: 3
titulo: "Pelos, Unhas e o Processo Biológico de Cicatrização"
fingerprint: {"startPage": 30, "endPage": 38, "startTopic": "Pelos e cabelos"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-37"
edital: ["geral:2.3", "geral:2.5a"]
fontes: ["JUNQUEIRA, L. C.; CARNEIRO, J. Histologia Básica: Texto e Atlas. 13. ed. Rio de Janeiro: Guanabara Koogan, 2017.", "GUYTON, A. C.; HALL, J. E. Tratado de Fisiologia Médica. 13. ed. Rio de Janeiro: Elsevier, 2017."]
notas: ""
---

Os pelos e as unhas constituem anexos queratinizados especializados derivados da diferenciação epitelial da epiderme. Paralelamente às suas funções táteis e de proteção mecânica, o tegumento ostenta uma notável capacidade regenerativa frente às agressões físicas, orquestrando um processo ordenado de cicatrização que restaura a barreira biológica lesada por traumas mecânicos ou queimaduras térmicas.

> [!objetivos]
> - Compreender a estrutura histológica do folículo piloso e as fases biológicas do ciclo de crescimento do pelo.
> - Identificar a arquitetura anatômica do aparelho ungueal e sua correlação com a avaliação clínica da perfusão tecidual.
> - Analisar as diferenças estruturais e pigmentares entre os diversos tipos de fios de cabelo.
> - Descrever minuciosamente as etapas coordenadas do processo de cicatrização e reparo tecidual cutâneo.

## Pelos e Cabelos: Anatomia e Fisiologia

Os pelos são estruturas filamentosas queratinizadas flexíveis que se projetam da superfície da pele, estando presentes em quase todo o corpo humano, exceto nas palmas das mãos, plantas dos pés e lábios. Eles desempenham funções de isolamento térmico, proteção contra atrito e dispersão de feromônios, além de funcionarem como sensíveis receptores mecânicos conectados a redes nervosas periféricas.

Cada pelo origina-se no interior de uma invaginação tubular da epiderme em direção à derme profunda, denominada **folículo piloso**. A porção dilatada terminal do folículo é o **bulbo piloso**, em cuja base se projeta a papila dérmica, uma estrutura conjuntiva vascularizada indispensável para o suprimento metabólico e a divisão celular. As células epiteliais que recobrem a papila formam a matriz do pelo, onde divisões mitóticas rápidas impulsionam o crescimento contínuo da haste.

```mermaid Estrutura Anatômica do Folículo Piloso
flowchart TD
    FP["Aparelho Folicular"]
    
    FP --> B["Bulbo Piloso<br>Matriz epitelial germinativa e papila dérmica vascular"]
    FP --> H["Haste do Pelo<br>Medula central, córtex queratinizado e cutícula protetora"]
    FP --> M["Músculo Eretor do Pelo<br>Músculo liso inervado pelo sistema simpático (arrepio)"]
    FP --> G["Glândula Sebácea Anexa<br>Ducto excretor que desemboca no colo folicular"]
```

O pelo propriamente dito é composto por três camadas concêntricas de células queratinizadas:
1. **Medula:** eixo central composto por células frouxas, pouco queratinizadas, presente apenas em pelos terminais grossos.
2. **Córtex:** camada intermediária predominante, formada por células alongadas densamente compactadas repletas de queratina dura. É no córtex que se concentram os grânulos de pigmento de melanina responsáveis pela cor do cabelo.
3. **Cutícula:** camada superficial mais externa, constituída por escamas anucleadas transparentes sobrepostas como telhas de um telhado, protegendo o córtex contra agentes químicos e desgaste físico.

Associado a cada folículo piloso encontra-se um feixe oblíquo de fibras musculares lisas denominado **músculo eretor do pelo**. Sob estímulo do sistema nervoso autônomo simpático (em resposta ao frio ou a emoções como o medo), esse músculo contrai-se, puxando o folículo para uma posição vertical e deprimindo a pele ao redor, fenômeno conhecido como piloereção (arrepio). Nos animais com pelagem densa, a piloereção aprisiona uma camada isolante de ar estagnado para conservar calor corpóreo.

```mermaid Fases do Ciclo Biológico do Folículo Piloso
flowchart LR
    A["1. Fase Anágena<br>(Crescimento Ativo / Mitoses)"] --> B["2. Fase Catágena<br>(Regressão / Apoptose Celular)"]
    B --> C["3. Fase Telógena<br>(Repouso Funcional e Queda)"]
    C --> A
```

O crescimento dos pelos não é contínuo, mas cíclico, alternando três fases sucessivas:
- **Fase Anágena:** período de proliferação celular ativa na matriz e crescimento longitudinal do fio, durando de dois a seis anos no couro cabeludo humano.
- **Fase Catágena:** fase de transição curta (cerca de duas a três semanas), na qual as mitoses cessam, a papila se desconecta e o bulbo sofre involução por morte celular programada.
- **Fase Telógena:** período de repouso metabólico de três a quatro meses. Ao término dessa fase, o pelo antigo desprende-se e cai, enquanto um novo ciclo anágeno se inicia a partir das células-tronco do folículo.

## Diferenças Estruturais dos Fios e Pigmentação

A variedade morfológica dos cabelos humanos reflete diferenças genéticas no formato transversal do folículo piloso e na síntese bioquímica de melanina no córtex:

```mermaid Tipologia e Formato da Haste Capilar
flowchart TD
    T["Formato do Fio de Cabelo"]
    
    T --> L["Cabelo Liso (Lisotríquio)<br>Folículo circular reto / haste cilíndrica"]
    T --> O["Cabelo Ondulado (Cinotríquio)<br>Folículo oval levemente curvado / haste elíptica"]
    T --> C["Cabelo Crespo (Ulótrio)<br>Folículo elíptico muito curvado / haste achatada em fita"]
```

A coloração dos pelos é determinada pela proporção relativa de dois pigmentos sintetizados pelos melanócitos foliculares:
- **Eumelanina:** pigmento insolúvel escuro que confere tonalidades castanhas e pretas aos fios, dotado de alta capacidade de absorção de luz.
- **Feomelanina:** pigmento rico em enxofre com tonalidade amarelada e avermelhada, predominante em indivíduos ruivos e louros naturais.
- **Cabelos Brancos (Canície):** decorrem da exaustão progressiva ou morte das células-tronco de melanócitos na matriz do bulbo piloso, associada ao acúmulo de pequenas bolhas de ar refratárias no interior da medula do fio.

## As Unhas

As unhas são placas compactas e translúcidas de queratina dura situadas na face dorsal das falanges distais dos dedos das mãos e dos pés. Elas atuam protegendo a extremidade sensível dos dígitos contra traumas mecânicos, aumentam a precisão na apreensão de pequenos objetos e auxiliam na discriminação tátil ao fornecerem um anteparo rígido de contrapressão para a polpa digital.

```mermaid Arquitetura Anatômica do Aparelho Ungueal
flowchart TD
    U["Aparelho Ungueal"]
    
    U --> L["Lâmina Ungueal<br>Placa visível de queratina dura anucleada"]
    U --> M["Matriz Ungueal<br>Região germinativa proliferativa sob a dobra proximal"]
    U --> B["Leito Ungueal<br>Tecido epitelial e derme muito vascularizada sob a lâmina"]
    U --> C["Eponíquio (Cutícula)<br>Borda córnea que veda e protege a matriz contra patógenos"]
    U --> Lu["Lúnula<br>Área esbranquiçada em crescente na base visível"]
```

A **lâmina ungueal** é a porção córnea visível da unha, composta por múltiplas camadas de escamas anucleadas achatadas fundidas entre si, ricas em enxofre e cálcio. A lâmina é continuamente produzida pela **matriz ungueal**, uma zona proliferativa profunda situada sob a dobra ungueal proximal. À medida que as células da matriz se dividem e se diferenciam, empurram a placa córnea para a frente, deslizando sobre o **leito ungueal**.

> [!atencao] Avaliação Clínica do Leito Ungueal no Atendimento Pré-Hospitalar
> O leito ungueal repousa sobre uma derme extraordinariamente rica em alças capilares e anastomoses arteriovenosas. Como a lâmina ungueal é transparente, a tonalidade rosada normal da unha reflete diretamente o fluxo de sangue oxigenado nos capilares dérmicos subjacentes. No socorro pré-hospitalar, o teste de enchimento capilar ungueal é realizado comprimindo-se a unha por alguns segundos até empalidecer; após a descompressão, o retorno à cor rosada normal deve ocorrer em **menos de dois segundos**. Um enchimento capilar lento indica choque circulatório, hipovolemia ou hipotermia grave.

As unhas das mãos crescem a uma velocidade média de três milímetros por mês, cerca de duas a três vezes mais rápido do que as unhas dos pés, cujo crescimento mensal é de apenas um milímetro. Fatores nutricionais, idade e aporte sanguíneo interferem diretamente nessa taxa metabólica de regeneração.

| Estrutura Ungueal | Localização Anatômica | Composição Histológica | Função Primária |
|---|---|---|---|
| **Lâmina Ungueal** | Superfície dorsal da falange distal | Queratina dura anucleada rica em cistina | Proteção física e anteparo mecânico |
| **Matriz Ungueal** | Porção proximal oculta sob a dobra | Epitélio germinativo proliferativo | Síntese e crescimento da placa ungueal |
| **Leito Ungueal** | Abaixo da lâmina córnea móvel | Epitélio delgado sobre derme vascular | Fixação mecânica e nutrição da unha |
| **Eponíquio (Cutícula)**| Borda da prega ungueal proximal | Projeção do estrato córneo epidérmico | Selamento hermético contra bactérias |

## O Processo de Cicatrização Cutânea

A ruptura da integridade tegumentar por traumas perfurocortantes, lacerações ou queimaduras desencadeia uma cascata biológica coordenada de reparo tecidual. Esse processo visa estancar a perda sanguínea, erradicar patógenos invasores e reconstituir a continuidade anatômica dos tecidos. A cicatrização divide-se classicamente em quatro etapas cronológicas integradas:

```mermaid Fases Coordenadas da Cicatrização Cutânea
flowchart TD
    H["1. Hemostasia (Minutos Iniciais)<br>Espasmo vascular, agregação de plaquetas e rede de fibrina"] --> I["2. Fase Inflamatória (1 a 4 Dias)<br>Infiltração de neutrófilos e macrófagos para fagocitose"]
    I --> P["3. Fase Proliferativa (4 a 14 Dias)<br>Angiogênese, proliferação de fibroblastos e colágeno tipo III"]
    P --> R["4. Fase de Remodelação (Semanas a Meses)<br>Substituição de colágeno III por colágeno I e contração tecidual"]
```

### 1. Fase de Hemostasia

Tem início imediatamente após a lesão tecidual com a exposição das fibras colágenas dérmicas ao sangue circulante. Ocorre vasoconstrição reflexa temporária para diminuir a perda volêmica. As plaquetas aderem ao colágeno subendotelial exposto, ativam-se e liberam fatores procoagulantes, originando o tampão hemostático primário. Concomitantemente, a cascata da coagulação converte fibrinogênio em uma rede de fibrina insolúvel que aprisiona hemácias e consolida o coágulo, formando a crosta que fecha temporariamente o leito da lesão.

### 2. Fase Inflamatória

Desenvolve-se do primeiro ao quarto dia após a agressão física. Sob o estímulo de mediadores químicos liberados pelo coágulo (como histamina, serotonina e citocinas), ocorre vasodilatação dos vasos vizinhos com aumento expressivo da permeabilidade capilar, provocando os sinais clássicos da inflamação: rubor, calor, edema e dor.

Os **neutrófilos** são os primeiros leucócitos a migrarem para a ferida por diapedese, destruindo bactérias invasoras por fagocitose e liberação de espécies reativas de oxigênio. Em seguida, os **macrófagos** assumem o protagonismo da reação: fagocitam restos celulares necrosados e secretam fatores de crescimento peptídicos (como VEGF, PDGF e TGF-beta), que atraem fibroblastos e estimulam a formação de novos vasos sanguíneos.

### 3. Fase Proliferativa

Ocorre aproximadamente entre o quarto e o décimo quarto dia, tendo como objetivo a reconstituição da derme e epiderme. Caracteriza-se por três fenômenos simultâneos:
- **Angiogênese:** brotamento de novos capilares sanguíneos a partir dos vasos pré-existentes, estimulados pelo fator VEGF em resposta à hipóxia local.
- **Fibroplasia e Tecido de Granulação:** migração e divisão ativa de fibroblastos na ferida. Essas células produzem ativamente nova matriz extracelular composta por proteoglicanos, ácido hialurônico e **fibras colágenas do tipo III** (colágeno jovem imaturo). A associação dos novos vasos sanguíneos permeáveis com o estroma rico em fibroblastos origina o **tecido de granulação**, de aspecto avermelhado brilhante, granuloso e facilmente sangrante.
- **Reepitelização:** queratinócitos da borda da ferida e dos restos de folículos pilosos vizinhos perdem seus desmossomos e migram sobre a matriz provisória até se encontrarem no centro da lesão, interrompendo a migração por inibição por contato.

### 4. Fase de Remodelação (Maturação)

Estende-se a partir da terceira semana, podendo durar meses ou anos. Nessa etapa, as células do tecido de granulação sofrem apoptose progressiva, diminuindo a densidade celular e o volume vascular da cicatriz, que passa de avermelhada para uma coloração esbranquiçada e plana.

O marco central da remodelação é a substituição do colágeno tipo III imaturo por **fibras espessas de colágeno tipo I**, organizadas em feixes paralelos que seguem as linhas de tensão mecânica da pele. Além disso, fibroblastos especializados adquirem características de células musculares lisas (miofibroblastos), promovendo a contração ativa da ferida e reduzindo a área total da cicatriz. Embora ganhe resistência ao longo dos meses, o tecido cicatricial maduro alcança no máximo cerca de oitenta por cento da força tênsil mecânica da pele íntegra original.

> [!bizu] Síntese Rápida das Etapas da Cicatrização
> - **Hemostasia:** agregação de plaquetas e rede de fibrina (cessa sangramento).
> - **Inflamatória:** neutrófilos e macrófagos limpam a ferida de bactérias e detritos.
> - **Proliferativa:** brotamento de vasos (angiogênese), fibroblastos com colágeno III e tecido de granulação avermelhado.
> - **Remodelação:** substituição do colágeno III pelo colágeno I maduro e contração pelos miofibroblastos.

## Mapa do capítulo

```mermaid Síntese Geral: Anexos e Cicatrização da Pele
flowchart TD
    A["Anexos e Cicatrização"]
    
    A --> P["Pelos e Folículos<br>Bulbo, haste com queratina e músculo eretor"]
    A --> U["Unhas<br>Lâmina de queratina dura, matriz e teste de perfusão"]
    A --> C["Fases da Cicatrização<br>Hemostasia, inflamação, proliferação e remodelação"]
    
    C --> C1["Proliferação: tecido de granulação e colágeno tipo III"]
    C --> C2["Remodelação: colágeno tipo I resistente e miofibroblastos"]
```

### Para fixar

1. **Folículo piloso**: estrutura epidérmica invaginada na derme contendo bulbo, papila vascularizada e matriz proliferativa responsável pelo crescimento do pelo.
2. **Camadas da haste do pelo**: medula central frouxa, córtex espesso com queratina dura e melanina, e cutícula externa com escamas transparentes protetoras.
3. **Músculo eretor do pelo**: músculo liso inervado pelo sistema simpático que traciona o folículo na piloereção térmica ou emocional.
4. **Ciclo folicular**: alternância periódica entre fases de crescimento ativo (anágena), involução por apoptose (catágena) e repouso com queda (telógena).
5. **Pigmentos capilares**: eumelanina escura e feomelanina avermelhada determinam o tom do fio; a perda funcional de melanócitos causa cabelos brancos.
6. **Lâmina ungueal**: placa visível de queratina dura produzida pela matriz ungueal proximal, repousando sobre um leito conjuntivo ricamente vascularizado.
7. **Perfusão capilar ungueal**: indicador clínico no qual o leito ungueal comprimido deve recobrar a cor rosada normal em menos de dois segundos no paciente hígido.
8. **Hemostasia e inflamação**: contenção inicial do sangramento por plaquetas e fibrina, seguida por recrutamento de neutrófilos e macrófagos fagocitários.
9. **Tecido de granulação**: tecido altamente vascularizado e avermelhado formado na fase proliferativa pela associação de angiogênese e deposição de colágeno tipo III.
10. **Remodelação cicatricial**: fase tardia caracterizada pela substituição do colágeno III por colágeno I resistente e ação contrátil de miofibroblastos.
'''

with open('content/material/biologia/m05/a05-s03.md', 'w', encoding='utf-8') as f:
    f.write(content.strip() + '\n')

print("a05-s03.md created successfully")
