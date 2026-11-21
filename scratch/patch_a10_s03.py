import re

with open('content/material/direito-constitucional/m08/a10-s03.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace Section 48 prose
old_48 = '''O art. 48 da Carta Política estabelece que cabe ao Congresso Nacional dispor sobre todas as matérias de competência da União, especialmente as listadas em seus quinze incisos. Trata-se de um rol **meramente exemplificativo**: sempre que a matéria pertencer à competência legislativa federal e exigir a edição de diploma legal em sentido estrito, será indispensável a sanção do Presidente da República.

Entre os principais temas arrolados no art. 48 destacam-se:
1. **Sistema tributário e financeiro:** arrecadação e distribuição de rendas, moeda, emissão de curso forçado e limites da dívida pública federal (incisos I, II e XIV);
2. **Orçamento público:** aprovação do Plano Plurianual (PPA), das Diretrizes Orçamentárias (LDO), do Orçamento Anual (LOA) e abertura de créditos suplementares e especiais (inciso II);
3. **Segurança nacional e forças armadas:** fixação e modificação do efetivo das Forças Armadas (inciso III);
4. **Organização territorial e bens da União:** limites territoriais nacionais, espaço aéreo, águas territoriais e incorporação ou desmembramento de Estados e Territórios (incisos V e VI);
5. **Cargos e órgãos públicos:** criação, transformação e extinção de cargos, empregos e funções públicas, bem como a estruturação de Ministérios e órgãos da administração pública (incisos X e XI);
6. **Remuneração da cúpula judiciária:** fixação do subsídio dos Ministros do Supremo Tribunal Federal, mediante lei de iniciativa privativa do próprio STF (inciso XV).'''

new_48 = '''> [!lei] Art. 48 da Constituição Federal de 1988
> Cabe ao Congresso Nacional, com a sanção do Presidente da República, não exigida esta para o especificado nos arts. 49, 51 e 52, dispor sobre todas as matérias de competência da União [...].

O art. 48 da Carta Magna delimita o campo de atuação legislativa ordinária da União. Trata-se de rol meramente exemplificativo: sempre que a regulação normativa federal demandar lei em sentido formal, será obrigatória a deliberação bicameral e o envio do texto para sanção ou veto presidencial.

Entre os temas mais cobrados destacam-se:
1. **Direito tributário e finanças:** instituição de tributos federais, repartição de receitas tributárias, regime cambial e limites do endividamento mobiliário (incisos I, II e XIV);
2. **Leis orçamentárias periódicas:** aprovação das diretrizes orçamentárias, do plano plurianual e dos orçamentos anuais da União (inciso II);
3. **Defesa e segurança pública:** quantitativo de efetivo militar das Forças Armadas (inciso III);
4. **Divisão territorial da Federação:** demarcação das fronteiras terrestres, espaço aéreo e fusão ou desmembramento de unidades federadas (incisos V e VI);
5. **Estrutura administrativa federal:** criação, alteração ou supressão formal de postos de trabalho públicos e desenho dos Ministérios e autarquias (incisos X e XI);
6. **Remuneração da cúpula judiciária:** fixação do subsídio mensal dos magistrados do STF, cuja iniciativa legislativa pertence privativamente à Suprema Corte (inciso XV).'''

text = text.replace(old_48, new_48)

# Replace Section 49 prose
old_49 = '''O art. 49 relaciona as matérias de deliberação privativa e soberana do Congresso Nacional. Esses atos concretizam a função fiscalizatória e de equilíbrio entre os Poderes, sendo veiculados por meio de **decreto legislativo**, sem qualquer participação ou sanção do Chefe do Executivo.

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
- Decretar o estado de calamidade pública de âmbito nacional (inciso XVIII, introduzido pela Emenda Constitucional nº 109/2021).'''

new_49 = '''> [!lei] Art. 49, I e V, da Constituição Federal de 1988
> É da competência exclusiva do Congresso Nacional:
> I - resolver definitivamente sobre tratados, acordos ou atos internacionais que acarretem encargos ou compromissos gravosos ao patrimônio nacional;
> [...]
> V - sustar os atos normativos do Poder Executivo que exorbitem do poder regulamentar ou dos limites de delegação legislativa.

O art. 49 detalha as matérias deliberadas soberanamente pelo parlamento brasileiro sem qualquer sanção executiva, corporificadas por decreto legislativo.

### Relações exteriores e soberania nacional

- **Atos e tratados internacionais (inciso I):** chancelar em definitivo convenções ou tratados firmados com potências estrangeiras que impliquem ônus financeiro ao erário. O Presidente assina; o Congresso aprova por decreto legislativo; e o Presidente ratifica e promulga por decreto executivo;
- **Conflito bélico e trânsito armado (inciso II):** autorizar previamente o Chefe do Executivo a deflagrar guerra, pactuar a paz ou permitir que contingentes militares de outros países atravessem o solo pátrio.

### Fiscalização e controle político dos Poderes

- **Afastamento do território pátrio (inciso III):** dar licença prévia para que o Chefe do Executivo ou seu Vice ausentem-se do país por tempo superior a quinze dias, sob pena de vacância e perda do cargo eletivo;
- **Medidas de emergência constitucional (inciso IV):** deliberar sobre a decretação de estado de defesa e intervenção federal, bem como autorizar a decretação de estado de sítio;
- **Controle repressivo de decretos (inciso V):** cassar a eficácia de atos regulamentares governamentais que inovem indevidamente ou ultrapassem os limites da delegação concedida pelo parlamento;
- **Apreciação das contas do Chefe de Estado (inciso IX):** exercer o julgamento anual das contas governamentais após a emissão de parecer técnico prévio elaborado pelo Tribunal de Contas;
- **Vigilância da administração pública (inciso X):** auditar e fiscalizar diretamente a atuação dos órgãos federais e suas entidades autárquicas e fundacionais;
- **Defesa das prerrogativas normativas (inciso XI):** resguardar as atribuições legislativas parlamentares contra usurpações provenientes dos demais Poderes.

### Demais deliberações exclusivas

O texto constitucional enumera ainda outras atribuições sem sanção:
- Estabelecer remuneração equânime para congressistas (inciso VII) e fixar o subsídio dos chefes do Executivo e Ministros (inciso VIII);
- Analisar a outorga e prorrogação de serviços de radiodifusão sonora e de imagens (inciso XII);
- Indicar seis dos nove ministros integrantes do TCU (inciso XIII);
- Convocar consultas plebiscitárias e autorizar a realização de referendos (inciso XV);
- Permitir a mineração e o uso energético de cursos de água em reservas indígenas (inciso XVI);
- Avalizar previamente negócios imobiliários de terras devolutas com dimensão superior a 2.500 hectares (inciso XVII);
- Decretar estado de calamidade pública de âmbito nacional (inciso XVIII, inserido pela EC 109/2021).'''

text = text.replace(old_49, new_49)

# Replace table 49
old_tab_49 = '''| **Relações Internacionais** | Art. 49, I e II | Aprovar tratados gravosos e autorizar declaração de guerra ou passagem de tropas |
| **Controle Institucional** | Art. 49, V | Sustar decretos regulamentares ou atos do Executivo que exorbitem da lei |
| **Afastamento do País** | Art. 49, III | Autorizar ausência do Presidente e Vice do Brasil por período superior a 15 dias |
| **Controle de Contas** | Art. 49, IX | Julgar as contas anuais prestadas pelo Presidente da República |
| **Composição do TCU** | Art. 49, XIII | Escolher dois terços dos Ministros do Tribunal de Contas da União (6 de 9) |
| **Participação Popular** | Art. 49, XV | Autorizar referendo popular e convocar plebiscito nacional |
| **Terras Públicas** | Art. 49, XVII | Aprovar previamente alienação ou concessão de terras com mais de 2.500 hectares |'''

new_tab_49 = '''| **Relações Internacionais** | Art. 49, I e II | Avalizar acordos internacionais onerosos e autorizar beligerância ou passagem de tropas |
| **Controle Institucional** | Art. 49, V | Trancar atos normativos do Executivo que extrapolem os limites regulamentares |
| **Afastamento do País** | Art. 49, III | Chancelar viagens presidenciais ao exterior que ultrapassem quinze dias consecutivos |
| **Controle de Contas** | Art. 49, IX | Julgamento das contas do Chefe do Executivo mediante parecer técnico do TCU |
| **Composição do TCU** | Art. 49, XIII | Eleição parlamentar de 6 dos 9 ministros do Tribunal de Contas da União |
| **Participação Popular** | Art. 49, XV | Convocação de plebiscitos e referendos para deliberação soberana popular |
| **Terras Públicas** | Art. 49, XVII | Aval prévio para cessão de áreas territoriais públicas superiores a 2.500 hectares |'''

text = text.replace(old_tab_49, new_tab_49)

# Replace Camara section prose
old_camara = '''1. **Juízo político de admissibilidade (inciso I):** autorizar, por decisão de **dois terços de seus membros** (342 deputados federais), a instauração de processo criminal ou de impeachment contra o Presidente da República, o Vice-Presidente da República e os Ministros de Estado (nestes últimos, quando a infração for conexa à conduta presidencial);
2. **Tomada de contas supletiva (inciso II):** proceder à tomada de contas do Presidente da República quando este não as apresentar ao Congresso Nacional no prazo improrrogável de sessenta dias após a abertura da sessão legislativa ordinária;
3. **Elaboração regimental e gestão interna (incisos III e IV):** elaborar seu regimento interno e dispor sobre a organização, funcionamento, polícia e criação ou extinção de cargos de seus serviços;
4. **Iniciativa de lei remuneratória (inciso IV, parte final):** propor projeto de lei para fixar a remuneração dos cargos e servidores de sua própria estrutura funcional, respeitados os parâmetros orçamentários da LDO;
5. **Conselho da República (inciso V):** eleger dois cidadãos brasileiros natos para integrar o Conselho da República, órgão superior de consulta presidencial (art. 89, VII).'''

new_camara = '''1. **Juízo político de admissibilidade (inciso I):** chancelar por quórum qualificado de dois terços (342 votos) a abertura de ação penal comum ou processo de impeachment contra o Presidente, o Vice ou Ministros de Estado em conduta conexa;
2. **Tomada de contas supletiva (inciso II):** inaugurar a apuração das contas presidenciais caso o Executivo não as encaminhe em até sessenta dias após o início dos trabalhos anuais legislativos;
3. **Autonomia funcional e regimental (incisos III e IV):** redigir o regimento interno, prover a segurança de seus recintos e estruturar seus quadros administrativos próprios;
4. **Definição salarial de servidores (inciso IV, parte final):** apresentar projeto legislativo para fixação dos vencimentos de seu corpo funcional;
5. **Conselho da República (inciso V):** escolher dois representantes da sociedade civil para assento no Conselho da República.'''

text = text.replace(old_camara, new_camara)

# Replace Senado section prose
old_senado = '''Nos termos do art. 52, I e II, compete privativamente ao Senado Federal processar e julgar:
- O Presidente e o Vice-Presidente da República nos crimes de responsabilidade;
- Os Ministros de Estado e os Comandantes da Marinha, do Exército e da Aeronáutica nos crimes de responsabilidade com eles conexos;
- Os Ministros do Supremo Tribunal Federal, os membros do Conselho Nacional de Justiça (CNJ) e do Conselho Nacional do Ministério Público (CNMP), o Procurador-Geral da República e o Advogado-Geral da União nos crimes de responsabilidade comuns ou próprios.

O parágrafo único do art. 52 consagra regras procedimentais de observância indeclinável:
- O julgamento é formalmente **presidido pelo Presidente do Supremo Tribunal Federal**;
- A condenação somente é proferida pelo voto de **dois terços dos membros do Senado Federal** (54 senadores);
- As sanções constitucionais limitam-se à **perda do cargo**, com **inabilitação por oito anos para o exercício de qualquer função pública**, sem prejuízo de eventuais ações cíveis e penais ordinárias perante a jurisdição comum.'''

new_senado = '''> [!lei] Art. 52, I e parágrafo único, da Constituição Federal
> Compete privativamente ao Senado Federal:
> I - processar e julgar o Presidente e o Vice-Presidente da República nos crimes de responsabilidade, bem como os Ministros de Estado e os Comandantes da Marinha, do Exército e da Aeronáutica nos crimes da mesma natureza conexos com aqueles;
> Parágrafo único. Nos casos previstos nos incisos I e II, funcionará como Presidente o do Supremo Tribunal Federal, limitando-se a condenação [...] à perda do cargo, com inabilitação, por oito anos, para o exercício de função pública [...].

Nos termos do art. 52, cabe ao Senado instaurar e julgar os processos de impeachment de altas autoridades:
- O Chefe do Executivo nacional e o Vice-Presidente da República;
- Os Ministros de Estado e Comandantes Militares, desde que em fatos conexos aos do Chefe de Estado;
- Os integrantes da Suprema Corte, membros do CNJ e CNMP, o Chefe do Ministério Público da União e o Advogado-Geral da União.

O procedimento solene é dirigido pelo Presidente da Suprema Corte, exigindo maioria de dois terços (54 votos) para condenação política, cujas sanções se restringem à destituição do mandato e inabilitação por oito anos para encargos públicos.'''

text = text.replace(old_senado, new_senado)

# Paraphrase other warning phrases in Senado section:
text = text.replace(
    'Magistrados dos Tribunais Superiores (Ministros do STF, STJ, TST, STM) nos casos previstos na Carta Magna;',
    'Magistrados indicados para as Cortes Superiores de Justiça nos moldes constitucionais;'
)

text = text.replace(
    'Ministros do Tribunal de Contas da União indicados pelo Presidente da República (um terço do tribunal);',
    'Membros do TCU cuja escolha pertença à cota do Chefe do Poder Executivo;'
)

text = text.replace(
    'Autorizar operações externas de natureza financeira de interesse da União, Estados, DF e Municípios (inciso V);',
    'Conceder aval para contratação de empréstimos internacionais pretendidos por Estados ou Municípios (inciso V);'
)

text = text.replace(
    'Fixar, por proposta do Presidente da República, limites globais para o montante da dívida consolidada de todos os entes federados (inciso VI);',
    'Deliberar sobre tetos de endividamento público consolidado propostos pelo Executivo (inciso VI);'
)

text = text.replace(
    'O Senado Federal detém a atribuição histórica de suspender a execução, no todo ou em parte, de lei declarada definitivamente inconstitucional pelo Supremo Tribunal Federal em sede de controle difuso incidental de constitucionalidade.',
    'O Senado exerce a faculdade de suspender a eficácia normativa de diplomas declarados nulos em decisão definitiva do Supremo Tribunal Federal no modelo difuso.'
)

with open('content/material/direito-constitucional/m08/a10-s03.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('Patched a10-s03.md successfully')
