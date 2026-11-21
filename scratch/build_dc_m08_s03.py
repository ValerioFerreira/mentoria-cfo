# Script to generate a10-s03.md for DC m08
import re

content = """---
id: "direito-constitucional/a10/s03"
volume: "direito-constitucional/m08"
capitulo: 3
titulo: "Atribuições do Congresso Nacional, Câmara e Senado"
fingerprint: {"startPage": 21, "endPage": 31, "startTopic": "Atribuições do Congresso Nacional (art. 48 - art. 50, CF/88)"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-31"
edital: ["geral:8.1", "pcpe:7"]
fontes: ["Constituição Federal de 1988 (arts. 48 a 52) — https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm — consultado em 2026-10-31"]
notas: "Estudo sistemático das atribuições do Poder Legislativo federal na CF/88: matérias com sanção presidencial (art. 48, mediante lei); competências exclusivas do Congresso Nacional (art. 49, mediante decreto legislativo); convocação e pedidos de informações a Ministros e autoridades (art. 50); competências privativas da Câmara dos Deputados (art. 51, juízo de admissibilidade no impeachment e tomada de contas); competências privativas do Senado Federal (art. 52, julgamento de crimes de responsabilidade, sabatina de autoridades, limites da dívida pública e suspensão de lei inconstitucional)."
---

A repartição das atribuições constitucionais entre os órgãos do Poder Legislativo federal reflete a complexidade do arranjo federativo e o sistema de freios e contrapesos da Constituição Federal de 1988. O constituinte originário estruturou as competências parlamentares em blocos específicos, distinguindo matérias que reclamam a colaboração harmônica entre o Legislativo e o Executivo mediante sanção presidencial daquelas reservadas com exclusividade ao Congresso Nacional, à Câmara dos Deputados ou ao Senado Federal.

> [!objetivos]
> - Diferenciar os instrumentos normativos cabíveis para cada espécie de competência parlamentar federal.
> - Compreender o rol exemplificativo de matérias que dependem de lei com sanção do Presidente da República.
> - Analisar as competências exclusivas do Congresso Nacional veiculadas por meio de decreto legislativo.
> - Identificar as atribuições privativas da Câmara dos Deputados e o juízo de admissibilidade de autoridades.
> - Dominar as competências privativas do Senado Federal, com foco no julgamento de autoridades e sabatinas.

## Visão panorâmica dos instrumentos normativos

A compreensão das competências do Poder Legislativo federal exige a prévia correlação entre o órgão titular da atribuição, a espécie normativa formalmente exigida e a necessidade ou dispensa de sanção ou veto do Chefe do Poder Executivo:

```mermaid Repartição de Atribuições e Atos Normativos no Legislativo
flowchart TD
    A["Atribuições Legislativas Federais"] --> B["Congresso Nacional com Sanção (art. 48)"]
    A --> C["Congresso Nacional Exclusivo (art. 49)"]
    A --> D["Câmara dos Deputados Privativa (art. 51)"]
    A --> E["Senado Federal Privativo (art. 52)"]
    B --> B1["Espécie Normativa: LEI ordinária ou complementar"]
    B --> B2["Sujeita a sanção ou veto do Presidente da República"]
    C --> C1["Espécie Normativa: DECRETO LEGISLATIVO"]
    C --> C2["Promulgado pelo Presidente do Senado (sem sanção)"]
    D --> D1["Espécie Normativa: RESOLUÇÃO da Câmara"]
    D --> D2["Matérias internas e juízo político de admissibilidade"]
    E --> E1["Espécie Normativa: RESOLUÇÃO do Senado"]
    E --> E2["Julgamento político, sabatinas e finanças federativas"]
```

Embora o texto constitucional utilize o vocábulo "privativas" para as competências da Câmara (art. 51) e do Senado (art. 52), a doutrina constitucional majoritária esclarece que tais atribuições são, em rigor técnico, **exclusivas e indelegáveis**. Elas não admitem delegação legislativa a outro órgão nem submetem-se a interferência do Poder Executivo.

| Dispositivo Constitucional | Órgão Titular | Instrumento Normativo Adequado | Sanção / Veto Presidencial? |
|---|---|---|---|
| **Artigo 48** | Congresso Nacional | **Lei** (ordinária ou complementar) | **Sim**, submete-se a sanção ou veto |
| **Artigo 49** | Congresso Nacional | **Decreto Legislativo** | **Não**, promulgado pelo Presidente do Senado |
| **Artigo 51** | Câmara dos Deputados | **Resolução** da Câmara | **Não**, promulgado pela Mesa da Câmara |
| **Artigo 52** | Senado Federal | **Resolução** do Senado | **Não**, promulgado pela Mesa do Senado |

## Matérias sujeitas a lei com sanção presidencial (art. 48)

O art. 48 da Carta Política estabelece que cabe ao Congresso Nacional dispor sobre todas as matérias de competência da União, especialmente as listadas em seus quinze incisos. Trata-se de um rol **meramente exemplificativo**: sempre que a matéria pertencer à competência legislativa federal e exigir a edição de diploma legal em sentido estrito, será indispensável a sanção do Presidente da República.

Entre os principais temas arrolados no art. 48 destacam-se:
1. **Sistema tributário e financeiro:** arrecadação e distribuição de rendas, moeda, emissão de curso forçado e limites da dívida pública federal (incisos I, II e XIV);
2. **Orçamento público:** aprovação do Plano Plurianual (PPA), das Diretrizes Orçamentárias (LDO), do Orçamento Anual (LOA) e abertura de créditos suplementares e especiais (inciso II);
3. **Segurança nacional e forças armadas:** fixação e modificação do efetivo das Forças Armadas (inciso III);
4. **Organização territorial e bens da União:** limites territoriais nacionais, espaço aéreo, águas territoriais e incorporação ou desmembramento de Estados e Territórios (incisos V e VI);
5. **Cargos e órgãos públicos:** criação, transformação e extinção de cargos, empregos e funções públicas, bem como a estruturação de Ministérios e órgãos da administração pública (incisos X e XI);
6. **Remuneração da cúpula judiciária:** fixação do subsídio dos Ministros do Supremo Tribunal Federal, mediante lei de iniciativa privativa do próprio STF (inciso XV).

> [!pegadinha]
> Distinção clássica: a criação e a extinção de cargos, empregos e funções públicas exigem lei em sentido formal aprovada pelo Congresso e sancionada pelo Presidente (art. 48, X). Todavia, nos termos do art. 84, VI, "b", da Constituição, o Presidente da República pode dispor mediante **decreto autônomo** sobre a **extinção de cargos ou funções públicas quando vagos**, dispensando inteiramente a edição de lei parlamentar.

## Competência exclusiva do Congresso Nacional (art. 49)

O art. 49 relaciona as matérias de deliberação privativa e soberana do Congresso Nacional. Esses atos concretizam a função fiscalizatória e de equilíbrio entre os Poderes, sendo veiculados por meio de **decreto legislativo**, sem qualquer participação ou sanção do Chefe do Executivo.

### Relações internacionais e defesa da soberania

- **Tratados internacionais (inciso I):** resolver definitivamente sobre tratados, acordos ou atos internacionais que acarretem encargos ou compromissos gravosos ao patrimônio nacional. A celebração e assinatura do tratado constituem ato privativo do Presidente da República; a aprovação política cabe ao Congresso por decreto legislativo; e a ratificação internacional definitiva, com promulgação interna por decreto executivo, retorna ao Presidente;
- **Guerra, paz e forças estrangeiras (inciso II):** autorizar o Presidente da República a declarar guerra, celebrar a paz e permitir que forças militares estrangeiras transitem pelo território nacional ou nele permaneçam temporariamente, ressalvados casos previstos em lei complementar.

### Controle político do Poder Executivo

- **Ausência do Presidente e Vice do país (inciso III):** autorizar o afastamento do Presidente e do Vice-Presidente da República do território nacional quando a ausência exceder a **quinze dias**, sob pena de perda do mandato eletivo (art. 83 da CF/88);
- **Estado de sítio, defesa e intervenção (inciso IV):** aprovar o estado de defesa e a intervenção federal decretados pelo Presidente, autorizar previamente a decretação do estado de sítio ou suspender qualquer dessas medidas excepcionais;
- **Sustação de atos normativos exorbitantes (inciso V):** sustar atos normativos do Poder Executivo que exorbitem do poder regulamentar ou dos limites da delegação legislativa. É a expressão mais nítida do controle de constitucionalidade e legalidade repressivo exercido pelo Legislativo;
- **Julgamento das contas do Presidente (inciso IX):** julgar anualmente as contas prestadas pelo Presidente da República e apreciar os relatórios sobre a execução dos planos de governo, com o auxílio técnico prévio do TCU;
- **Fiscalização e controle direto (inciso X):** fiscalizar e controlar diretamente os atos do Poder Executivo, abrangidos os órgãos da administração direta e entidades da administração indireta;
- **Defesa das prerrogativas parlamentares (inciso XI):** zelar pela preservação de sua competência legislativa em face da usurpação normativa dos demais Poderes.

### Demais deliberações exclusivas

O art. 49 contempla ainda competências fundamentais:
- Fixar subsídio idêntico para deputados federais e senadores (inciso VII), e fixar a remuneração do Presidente, do Vice e dos Ministros de Estado (inciso VIII);
- Apreciar atos de concessão e renovação de concessão de emissoras de rádio e televisão (inciso XII);
- Escolher **dois terços dos ministros do Tribunal de Contas da União** (inciso XIII);
- Autorizar referendo popular e convocar plebiscito (inciso XV);
- Autorizar a exploração e o aproveitamento de recursos hídricos e a lavra mineral em terras indígenas (inciso XVI);
- Conferir aprovação prévia para a alienação ou concessão de terras públicas com área superior a **dois mil e quinhentos hectares** (inciso XVII);
- Decretar o estado de calamidade pública de âmbito nacional (inciso XVIII, introduzido pela Emenda Constitucional nº 109/2021).

| Área de Incidência | Dispositivo do Artigo 49 | Atribuição Exclusiva do Congresso Nacional |
|---|---|---|
| **Relações Internacionais** | Art. 49, I e II | Aprovar tratados gravosos e autorizar declaração de guerra ou passagem de tropas |
| **Controle Institucional** | Art. 49, V | Sustar decretos regulamentares ou atos do Executivo que exorbitem da lei |
| **Afastamento do País** | Art. 49, III | Autorizar ausência do Presidente e Vice do Brasil por período superior a 15 dias |
| **Controle de Contas** | Art. 49, IX | Julgar as contas anuais prestadas pelo Presidente da República |
| **Composição do TCU** | Art. 49, XIII | Escolher dois terços dos Ministros do Tribunal de Contas da União (6 de 9) |
| **Participação Popular** | Art. 49, XV | Autorizar referendo popular e convocar plebiscito nacional |
| **Terras Públicas** | Art. 49, XVII | Aprovar previamente alienação ou concessão de terras com mais de 2.500 hectares |

## Convocação de autoridades e pedidos de informação (art. 50)

O art. 50 disciplina os mecanismos diretos de fiscalização exercidos pela Câmara dos Deputados, pelo Senado Federal e por suas respectivas comissões parlamentares:

> [!lei] Art. 50, caput e § 2º, da Constituição Federal de 1988
> A Câmara dos Deputados e o Senado Federal, ou qualquer de suas Comissões, poderão convocar Ministro de Estado ou quaisquer titulares de órgãos diretamente subordinados à Presidência da República para prestarem, pessoalmente, informações sobre assunto previamente determinado, importando crime de responsabilidade a ausência sem justificação adequada.
> [...]
> § 2º As Mesas da Câmara dos Deputados e do Senado Federal poderão encaminhar pedidos escritos de informações a Ministros de Estado ou a qualquer das pessoas referidas no caput deste artigo, importando em crime de responsabilidade a recusa, ou o não atendimento, no prazo de trinta dias, bem como a prestação de informações falsas.

A Emenda Constitucional nº 132/2023 inseriu expressamente o Presidente do Comitê Gestor do Imposto sobre Bens e Serviços (IBS) no rol de autoridades sujeitas à convocação e pedidos formais de informação parlamentar.

> [!atencao]
> Impossibilidade de convocar o Chefe do Executivo: a prerrogativa parlamentar de convocação restringe-se a Ministros de Estado e titulares de órgãos subordinados à Presidência. Nem o Plenário nem as comissões da Câmara ou do Senado possuem competência para convocar o próprio Presidente da República ou Governadores para depor obrigatoriamente perante o Legislativo, sob pena de violação à independência e harmonia dos Poderes da República.

## Atribuições privativas da Câmara dos Deputados (art. 51)

A Câmara dos Deputados atua com protagonismo no juízo inicial de responsabilização de altas autoridades do Poder Executivo, competindo-lhe privativamente nos termos do art. 51:

1. **Juízo político de admissibilidade (inciso I):** autorizar, por decisão de **dois terços de seus membros** (342 deputados federais), a instauração de processo criminal ou de impeachment contra o Presidente da República, o Vice-Presidente da República e os Ministros de Estado (nestes últimos, quando a infração for conexa à conduta presidencial);
2. **Tomada de contas supletiva (inciso II):** proceder à tomada de contas do Presidente da República quando este não as apresentar ao Congresso Nacional no prazo improrrogável de sessenta dias após a abertura da sessão legislativa ordinária;
3. **Elaboração regimental e gestão interna (incisos III e IV):** elaborar seu regimento interno e dispor sobre a organização, funcionamento, polícia e criação ou extinção de cargos de seus serviços;
4. **Iniciativa de lei remuneratória (inciso IV, parte final):** propor projeto de lei para fixar a remuneração dos cargos e servidores de sua própria estrutura funcional, respeitados os parâmetros orçamentários da LDO;
5. **Conselho da República (inciso V):** eleger dois cidadãos brasileiros natos para integrar o Conselho da República, órgão superior de consulta presidencial (art. 89, VII).

```mermaid Fluxo do Juízo de Admissibilidade e Impeachment Presidencial
flowchart TD
    A["Denúncia por Crime de Responsabilidade"] --> B["Câmara dos Deputados (art. 51, I)"]
    B --> B1["Juízo de Admissibilidade Político"]
    B1 --> B2{"Aprovação por 2/3 dos Deputados (342 votos)?"}
    B2 -- Não --> B3["Arquivamento Sumário da Denúncia"]
    B2 -- Sim --> C["Encaminhamento ao Senado Federal"]
    C --> C1["Senado Instaura e Julga o Processo (art. 52, I)"]
    C1 --> C2["Sessão presidida pelo Presidente do STF"]
    C2 --> C3{"Condenação por 2/3 dos Senadores (54 votos)?"}
    C3 -- Sim --> D["Perda do Mandato + Inabilitação por 8 anos"]
    C3 -- Não --> E["Absolvição do Denunciado"]
```

## Atribuições privativas do Senado Federal (art. 52)

O Senado Federal ostenta atribuições exclusivas de envergadura superior, destacando-se o julgamento político de autoridades, a sabatina de dirigentes públicos e a fixação de parâmetros financeiros e tributários para toda a Federação brasileira.

### Julgamento por crimes de responsabilidade

Nos termos do art. 52, I e II, compete privativamente ao Senado Federal processar e julgar:
- O Presidente e o Vice-Presidente da República nos crimes de responsabilidade;
- Os Ministros de Estado e os Comandantes da Marinha, do Exército e da Aeronáutica nos crimes de responsabilidade com eles conexos;
- Os Ministros do Supremo Tribunal Federal, os membros do Conselho Nacional de Justiça (CNJ) e do Conselho Nacional do Ministério Público (CNMP), o Procurador-Geral da República e o Advogado-Geral da União nos crimes de responsabilidade comuns ou próprios.

O parágrafo único do art. 52 consagra regras procedimentais de observância indeclinável:
- O julgamento é formalmente **presidido pelo Presidente do Supremo Tribunal Federal**;
- A condenação somente é proferida pelo voto de **dois terços dos membros do Senado Federal** (54 senadores);
- As sanções constitucionais limitam-se à **perda do cargo**, com **inabilitação por oito anos para o exercício de qualquer função pública**, sem prejuízo de eventuais ações cíveis e penais ordinárias perante a jurisdição comum.

### Sabatina e aprovação prévia de autoridades

O Senado Federal exerce relevante controle institucional ao aprovar previamente, mediante **arguição pública** e **voto secreto**, os titulares dos seguintes cargos estatais (art. 52, III e IV):
- Magistrados dos Tribunais Superiores (Ministros do STF, STJ, TST, STM) nos casos previstos na Carta Magna;
- Ministros do Tribunal de Contas da União indicados pelo Presidente da República (um terço do tribunal);
- Governadores de Territórios Federais;
- Presidente e Diretores do Banco Central do Brasil;
- Procurador-Geral da República;
- Chefes de missão diplomática permanente (cuja arguição ocorre em **sessão secreta** perante comissão temática, nos termos do inciso IV).

### Regulação financeira e limites da dívida pública

Em seu papel de equilíbrio federativo, cabe privativamente ao Senado:
- Autorizar operações externas de natureza financeira de interesse da União, Estados, DF e Municípios (inciso V);
- Fixar, por proposta do Presidente da República, limites globais para o montante da dívida consolidada de todos os entes federados (inciso VI);
- Estabelecer limites globais e condições para operações de crédito externo e interno e para a concessão de garantia da União (incisos VII e VIII);
- Determinar limites globais para a dívida mobiliária dos Estados, DF e Municípios (inciso IX);
- Avaliar periodicamente a eficácia do Sistema Tributário Nacional (inciso XV).

### Suspensão de lei inconstitucional (art. 52, X)

O Senado Federal detém a atribuição histórica de suspender a execução, no todo ou em parte, de lei declarada definitivamente inconstitucional pelo Supremo Tribunal Federal em sede de controle difuso incidental de constitucionalidade.

> [!jurisprudencia] STF: O Papel do Senado no Controle Difuso e a Teoria da Mutação Constitucional
> A interpretação tradicional do art. 52, X, assentava que a decisão do STF em controle difuso produzia efeitos apenas entre as partes (*inter partes*), dependendo de resolução do Senado Federal para expandir a eficácia contra todos (*erga omnes*).
> Todavia, a jurisprudência mais recente do Supremo Tribunal Federal (notadamente na ADI 3406 e ADI 3470) desenvolveu a tese da **mutação constitucional**: a declaração de inconstitucionalidade proferida pelo Plenário do STF, mesmo no modelo difuso, já ostenta eficácia expansiva e vinculante imediata, cabendo ao Senado Federal atuar precipuamente dando publicidade à decisão da Suprema Corte.

| Categoria Temática | Dispositivo Constitucional | Atribuição Privativa do Senado Federal |
|---|---|---|
| **Julgamento de Autoridades** | Art. 52, I e II | Processar e julgar Presidente, Ministros do STF, PGR e AGU |
| **Sabatina Pública** | Art. 52, III | Arguição e voto secreto para aprovar Ministros de Tribunais e PGR |
| **Sabatina Diplomática** | Art. 52, IV | Arguição em sessão secreta para aprovar chefes de embaixadas |
| **Operações Externas** | Art. 52, V | Autorizar empréstimos internacionais de Estados e Municípios |
| **Dívida Consolidada** | Art. 52, VI | Fixar limites globais de endividamento para toda a Federação |
| **Controle de Leis** | Art. 52, X | Suspender a execução de lei declarada inconstitucional pelo STF |

> [!bizu]
> Regra prática de memorização:
> - Juízo de admissibilidade para processar o Presidente -> Exclusivo da Câmara dos Deputados por 2/3 (art. 51, I).
> - Julgamento definitivo do Presidente em crime de responsabilidade -> Exclusivo do Senado Federal por 2/3 (art. 52, I).
> - Julgamento do Presidente em crime comum -> Competência privativa do Supremo Tribunal Federal (art. 102, I, "b"), sempre após autorização prévia da Câmara.

## Mapa do capítulo

A tabela consolida a distribuição constitucional de competências legislativas no plano federal:

| Esfera Deliberativa | Dispositivo na CF/88 | Forma do Ato | Dependência de Sanção | Exemplos Marcantes |
|---|---|---|---|---|
| **Congresso com Sanção** | Art. 48 | Lei ordinária ou complementar | **Sim** (Presidente sanciona ou veta) | Matéria tributária, orçamentos (PPA/LOA) e criação de cargos |
| **Congresso Exclusivo** | Art. 49 | Decreto Legislativo | **Não** (Promulgado pelo Presidente do Senado) | Tratados internacionais, sustação de decretos e contas do Executivo |
| **Câmara Privativa** | Art. 51 | Resolução da Câmara | **Não** (Promulgado pela Mesa da Câmara) | Admissibilidade de impeachment (2/3) e tomada de contas |
| **Senado Privativo** | Art. 52 | Resolução do Senado | **Não** (Promulgado pela Mesa do Senado) | Julgamento de impeachment, sabatinas e limites da dívida pública |

### Para fixar

- O art. 48 elenca matérias que dependem de lei aprovada pelo Congresso com sanção ou veto do Presidente da República (tributos, orçamento e criação de cargos públicos).
- O art. 49 prevê competências exclusivas do Congresso Nacional veiculadas por decreto legislativo, dispensando sanção executiva (tratados, sustação de atos e 2/3 do TCU).
- O art. 50 autoriza a convocação pessoal de Ministros de Estado para prestar informações em audiência, tipificando crime de responsabilidade a ausência injustificada.
- Compete privativamente à Câmara dos Deputados (art. 51, I) autorizar por dois terços a instauração de processo por crime comum ou de responsabilidade contra o Presidente da República.
- O Senado Federal julga privativamente o Presidente da República nos crimes de responsabilidade (art. 52, I), sessão presidida pelo Presidente do STF e com sanção restrita à perda do cargo e inabilitação por 8 anos.
- Compete ao Senado sabatinar por voto secreto magistrados de Tribunais Superiores e o Procurador-Geral da República, bem como fixar os limites globais da dívida consolidada nacional.
- O art. 52, X, confere ao Senado a prerrogativa de suspender a execução de lei declarada definitivamente inconstitucional pelo Supremo Tribunal Federal.
"""

with open("content/material/direito-constitucional/m08/a10-s03.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved content/material/direito-constitucional/m08/a10-s03.md")
