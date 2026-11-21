import re

content = """---
id: "biologia/a06/s04"
volume: "biologia/m05"
capitulo: 7
titulo: "O Esqueleto Apendicular Superior: Cintura Escapular e Membros Superiores"
fingerprint: {"startPage": 47, "endPage": 56, "startTopic": "O esqueleto apendicular"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-37"
edital: ["geral:2.5b"]
fontes: ["MOORE, K. L.; DALLEY, A. F.; AGUR, A. M. R. Anatomia Orientada para a Clínica. 8. ed. Rio de Janeiro: Guanabara Koogan, 2018.", "TORTORA, G. J.; DERRICKSON, B. Princípios de Anatomia e Fisiologia. 14. ed. Rio de Janeiro: Guanabara Koogan, 2016."]
notas: ""
---

O esqueleto apendicular compreende os ossos dos membros superiores e inferiores, juntamente com as cinturas esqueléticas que os ancoram ao eixo central axial. Nos membros superiores, a arquitetura óssea privilegia a amplitude de movimento e a destreza manual, características determinantes para a manipulação de ferramentas e equipamentos operacionais de salvamento.

> [!objetivos]
> - Compreender a organização estrutural da cintura escapular e sua conexão com o tórax.
> - Identificar os acidentes anatômicos do úmero, rádio e ulna.
> - Reconhecer os movimentos de pronação e supinação do antebraço.
> - Caracterizar a distribuição óssea do carpo, metacarpo e falanges da mão.

## A Cintura Escapular e a Mobilidade do Ombro

A cintura escapular (ou peitoral) une o membro superior ao esqueleto axial do tórax. Ela é composta por quatro ossos articulados em pares: duas **clavículas** anteriormente e duas **escápulas** dorsalmente.

A **clavícula** é um osso longo delgado e curvado em forma de "S" itálico, posicionado horizontalmente na raiz do pescoço. Ela atua como uma escora rígida que projeta o ombro lateralmente para longe do tronco, permitindo livre oscilação do braço. Sua extremidade esternal medial articula-se com o manúbrio do esterno por meio da **articulação esternoclavicular**. Esta articulação constitui o único ponto de contato sinovial direto entre a cintura escapular e o esqueleto axial. Sua extremidade acromial lateral articula-se com o acrômio da escápula.

A **escápula** é um osso plano triangular largo situado na face póstero-superior do tórax. Na sua face posterior sobressai uma crista óssea transversa saliente, a **espinha da escápula**, que se alarga lateralmente para formar o **acrômio**, ponto mais alto do ombro palpável sob a pele. Na margem superolateral localiza-se a **cavidade glenoide**, rasa depressão articular ovalada que recebe a cabeça esférica do úmero. Próximo à cavidade glenoide projeta-se o **processo coracoide**, projeção anterior semelhante a um bico de corvo para ancoragem ligamentar e muscular.

```mermaid Organização Funcional da Cintura Escapular
flowchart TD
    CE["Cintura Escapular"]
    
    CE --> CL["Clavícula (Osso em S)<br>Articulação esternoclavicular medial com o manúbrio"]
    CE --> ES["Escápula (Osso Plano Dorsal)<br>Espinha, acrômio, processo coracoide e cavidade glenoide"]
    
    ES --> AG["Articulação Glenoumeral<br>Grande mobilidade articular mantida pelo manguito rotador"]
```

> [!bizu] Compromisso Biomecânico: Mobilidade versus Estabilidade
> A articulação glenoumeral do ombro é a mais móvel de todo o corpo humano, executando circundução, flexão, extensão, abdução e rotação. Entretanto, essa extrema mobilidade cobra um preço em estabilidade mecânica: a cavidade glenoide é rasa e acomoda apenas um terço da cabeça umeral. Por essa razão, a luxação glenoumeral é a luxação articular traumática mais frequente em emergências, sendo a estabilidade dinâmica assegurada pelos tendões do manguito rotador muscular.

## Braço e Antebraço: Úmero, Rádio e Ulna

O esqueleto do braço é formado por um único osso longo, o **úmero**, que se articula proximalmente com a escápula e distalmente com o rádio e a ulna na articulação do cotovelo. Na sua extremidade proximal destacam-se a cabeça hemisférica lisa, o colo anatômico e o **colo cirúrgico**, estreitamento distal aos tubérculos que representa um ponto comum de fraturas traumáticas. Na face anterior proximal situam-se o **tubérculo maior** e o **tubérculo menor**, separados pelo sulco intertubercular. Na porção média da diáfise encontra-se a tuberosidade deltóidea para inserção muscular. Distalmente, o úmero expande-se nos epicôndilos medial e lateral, no capítulo lateral (que se articula com a cabeça do rádio) e na tróclea medial em forma de carretel (que se articula com a ulna).

```mermaid Ossos do Membro Superior
flowchart TD
    MS["Esqueleto do Membro Superior"]
    
    MS --> U["Úmero (Braço)<br>Cabeça, colo cirúrgico, tróclea e capítulo"]
    MS --> AB["Antebraço (Dois Ossos)<br>Rádio lateral e Ulna medial unidos por membrana"]
    MS --> MA["Mão (27 Ossos)<br>8 carpais, 5 metacarpais e 14 falanges"]
```

O antebraço abriga dois ossos paralelos interligados ao longo da diáfise pela flexível **membrana interóssea**:
- **Ulna:** osso medial do antebraço (do lado do dedo mínimo). Na sua extremidade proximal volumosa projeta-se o **olécrano**, saliência proeminente dorsal que forma a ponta óssea do cotovelo e bloqueia a hiperextensão articular ao se alojar na fossa do olécrano do úmero. Apresenta a incisura troclear e o processo coronoide. Distalmente termina na cabeça da ulna com um processo estiloide afilado.
- **Rádio:** osso lateral do antebraço (do lado do polegar). Possui uma cabeça proximal cilíndrica em formato de disco que gira contra o capítulo umeral e contra a incisura radial da ulna. Na posição anatômica, rádio e ulna repousam paralelos com a palma voltada para a frente (**supinação**). No movimento de **pronação**, a cabeça distal do rádio cruza diagonalmente sobre a ulna, girando a palma para trás.

## Esqueleto da Mão: Carpo, Metacarpo e Falanges

A mão humana contém vinte e sete ossos agrupados em três divisões esqueléticas integradas:

```mermaid Arquitetura Óssea da Mão
flowchart LR
    M["Ossos da Mão"]
    
    M --> C["Carpo (8 ossos)<br>Fileiras proximal e distal"]
    M --> MC["Metacarpo (5 ossos)<br>Numerados de I a V do polegar ao mínimo"]
    M --> F["Falanges (14 ossos)<br>Proximais, médias e distais"]
```

- **Carpo (Punho):** reúne oito pequenos ossos curtos distribuídos em duas fileiras transversais de quatro ossos cada:
  - Fileira Proximal (do polegar para o dedo mínimo): **Escafoide**, **Semilunar**, **Piramidal** e **Pisiforme** (pequeno osso sesamoide situado sobre a face anterior do piramidal). O escafoide e o semilunar articulam-se com a extremidade distal do rádio na articulação radiocárpica do punho.
  - Fileira Distal (do polegar para o dedo mínimo): **Trapézio**, **Trapezoide**, **Capitato** (o maior osso do carpo) e **Hamato** (dotado de um hâmulo em gancho saliente).
- **Metacarpo (Palma da Mão):** formado por cinco ossos longos denominados metacarpais, numerados de I a V a partir do polegar. Cada osso metacarpal possui base proximal articulada com o carpo, corpo longitudinal e cabeça distal arredondada. As cabeças dos metacarpais formam as saliências visíveis dos "nós dos dedos" com a mão fechada.
- **Falanges (Dedos):** somam catorze ossos longos miniaturas. Cada dedo de II a V (indicador, médio, anelar e mínimo) contém três falanges articuladas em série: falange **proximal**, falange **média** e falange **distal**. O **polegar (dedo I)** é uma exceção funcional: possui apenas duas falanges (proximal e distal), o que, aliado à mobilidade da articulação carpometacárpica do trapézio, viabiliza o movimento de oposição do polegar para pinça de precisão.

> [!atencao] Fratura do Escafoide e Necrose Avascular
> O osso escafoide é o osso do carpo mais frequentemente fraturado em quedas ao solo com a mão espalmada para a frente. Sua irrigação arterial arterial nutridora penetra predominantemente pela extremidade distal e viaja em sentido retrógrado em direção ao polo proximal. Fraturas na cintura do escafoide podem interromper esse fluxo capilar, provocando necrose avascular do polo proximal e artrose dolorosa se não houver diagnóstico radiográfico precoce e imobilização gessada adequada.

| Segmento | Ossos Constituintes | Detalhes Funcionais |
|---|---|---|
| **Cintura Escapular** | Clavícula e Escápula | Ancoragem do membro superior ao manúbrio |
| **Braço** | Úmero | Articulações glenoumeral e do cotovelo |
| **Antebraço** | Rádio e Ulna | Pronação e supinação com membrana interóssea |
| **Carpo** | 8 ossos em duas fileiras | Flexibilidade e circundução do punho |
| **Metacarpo e Dedos**| 5 metacarpais e 14 falanges | Preensão palmar e pinça de precisão digital |

## Mapa do capítulo

```mermaid Síntese Geral: Esqueleto Apendicular Superior
flowchart TD
    EAS["Membro Superior"]
    EAS --> CE["Cintura Escapular<br>Clavícula esternal e escápula com cavidade glenoide"]
    EAS --> BR["Braço e Antebraço<br>Úmero, rádio lateral rotatório e ulna com olécrano"]
    EAS --> MA["Punho e Mão<br>Oito carpais, cinco metacarpais e catorze falanges"]
    EAS --> OP["Oponência Digital<br>Mobilidade do polegar para preensão de precisão"]
```

### Para fixar

- A clavícula forma a única articulação sinovial direta entre a cintura escapular e o esqueleto axial no manúbrio.
- A escápula apresenta a cavidade glenoide rasa que se articula com a cabeça do úmero no ombro.
- O colo cirúrgico do úmero localiza-se abaixo dos tubérculos e representa frequente ponto de fraturas.
- O olécrano da ulna forma a ponta óssea posterior do cotovelo e se encaixa na fossa umeral.
- O rádio posiciona-se lateralmente no antebraço e cruza sobre a ulna durante a pronação da mão.
- O carpo possui oito ossos dispostos em fileira proximal (escafoide, semilunar, piramidal, pisiforme) e distal.
- O escafoide é o osso carpal mais fraturado em quedas, apresentando risco de necrose avascular.
- O polegar possui apenas duas falanges, enquanto os demais quatro dedos possuem três falanges cada.
"""

with open("content/material/biologia/m05/a06-s04.md", "w", encoding="utf-8") as f:
    f.write(content.strip() + "\n")
print("Wrote content/material/biologia/m05/a06-s04.md")
