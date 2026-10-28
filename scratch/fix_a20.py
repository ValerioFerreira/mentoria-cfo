import json
from pathlib import Path

# Load items and summaries from build_a20.py
import sys
sys.path.insert(0, '.')
import scratch.build_a20 as b20

items_a20 = b20.items_a20

# Let's inspect summaries_a20 and update the text
summaries_a20 = b20.summaries_a20

# Segment 1: expand analytic to ~630 words
summaries_a20["segments"][0]["analytic"] = """A Lei 9.605/1998 representou um marco dogmático pioneiro ao conferir efetividade ao mandamento do art. 225, § 3º, da Carta Constitucional brasileira, sistematizando a repressão criminal e as sanções administrativas voltadas a conter agressões ao equilíbrio ecológico. O diploma inovou ao introduzir a responsabilização penal da pessoa jurídica e estruturar um sistema autônomo de sanções alternativas orientadas à recomposição do patrimônio coletivo lesado em ilícitos contra a flora, a fauna e o meio ambiente urbano.

### Responsabilidade Penal Societária e Superação da Dupla Imputação
A tutela ambiental estruturou diretrizes próprias para responsabilizar criminalmente entidades corporativas:
- **Requisitos de Imputação Societária (art. 3º)**: a responsabilização penal do ente moral exige que o ilícito derive de deliberação de seus gestores estatutários ou colegiado diretivo superior, e que a atuação seja consumada em proveito direto ou econômico da entidade coletiva. A responsabilização do ente coletivo não exclui a responsabilidade penal individual das pessoas físicas coautoras ou partícipes do evento criminoso;
- **Superação Definitiva da Teoria da Dupla Imputação**: no passado doutrinário, sustentava-se que a corporação não poderia ser demandada sem a concomitante presença física de seus diretores no polo passivo da ação penal. Contudo, o Pleno do Supremo Tribunal Federal e o Superior Tribunal de Justiça consolidaram o entendimento de que **a pessoa jurídica pode ser denunciada, processada e condenada de forma autônoma**, prescindindo de acusação conjunta contra os sócios ou administradores pessoas naturais;
- **Desconsideração da Personalidade Jurídica (art. 4º)**: autoriza-se afastar o escudo corporativo sempre que sua estrutura societária configurar embaraço ou obstáculo material à satisfação indenizatória das ofensas infligidas ao ecossistema natural.

### Regime Sancionatório e Penas Especiais
O sistema ambiental diversificou os instrumentos coercitivos admitidos no processo penal:
- **Sanções Aplicáveis a Pessoas Jurídicas (arts. 21 a 24)**: vedada a imposição de penas privativas de liberdade carcerárias, cominam-se multas financeiras graduadas, sanções restritivas consubstanciadas na paralisação de linhas industriais, interdição temporária de estabelecimentos comerciais e impedimento de contratar com o Poder Público por lapso de 3 a 5 anos, além da prestação de serviços à comunidade (custeio de fundos ecológicos públicos, execução direta de obras de recuperação ambiental de sítios degradados e manutenção de áreas públicas);
- **Penas Substitutivas para Autores Individuais (art. 8º)**: prestação pecuniária destinada a vítimas ou entidades protetivas cadastradas, confisco de maquinários e embarcações clandestinas de pesca, recolhimento domiciliar monitorado e interdições temporárias de direitos inerentes a caça, pesca e comércio de madeira;
- **Liquidação Forçada por Fraude (art. 24)**: a pessoa jurídica constituída ou utilizada com o fim preponderante de permitir, ocultar ou facilitar a prática de crime ambiental terá decretada judicialmente sua dissolução compulsória e liquidação forçada de ativos.

### Dosimetria, Circunstâncias Atenuantes e Agravantes
A fixação da reprimenda judicial observa vetores legais expressos no diploma:
- **Atenuantes Próprias (art. 14)**: precária instrução formal do agente infrator; voluntário arrependimento materializado na pronta restauração do dano ecológico; comunicação prévia de risco às autoridades competentes; e colaboração estreita com os fiscais ambientais;
- **Agravantes Específicas (art. 15)**: reincidência delitiva ambiental; finalidade lucrativa desmedida; induzimento de subordinados ou empregados; prática no período noturno, domingos ou feriados; emprego de métodos cruéis contra espécimes da fauna; e perpetração em unidades de conservação ou períodos de defeso e estiagem prolongada.

### Para fixar
- A pessoa jurídica responde penalmente por delitos ambientais praticados em seu benefício por órgão diretivo.
- O STF e o STJ superaram a dupla imputação, admitindo persecução exclusiva contra a empresa.
- É proibida a cominação de penas carcerárias para pessoas jurídicas, recaindo penas de multa e restritivas.
- A desconsideração da personalidade é deferida sempre que obstar a reparação dos prejuízos ambientais.
- O baixo grau de escolaridade do agente figura expressamente como atenuante genérica da reprimenda.
- A prática de infração ambiental durante a noite ou feriados atrai agravamento sancionatório obrigatório."""

# Segment 2: fix all copied runs
summaries_a20["segments"][1]["analytic"] = """A seção dos crimes contra a fauna tutelou de maneira abrangente os animais silvestres nativos, espécimes em rota migratória e animais domésticos, cominando sanções aos atos de caça clandestina, cativeiro desautorizado, tráfico zoológico e práticas degradantes de crueldade e abusos corporais.

### Tipificação Básica da Fauna Silvestre e Perdão Judicial
- **Condutas Vedadas do Art. 29**: matar, perseguir, caçar, apanhar ou aprisionar animais da fauna silvestre nativos ou em rota migratória desprovido de autorização da autoridade, sancionado com detenção semestral a anual cumulada com penalidade pecuniária;
- **Equiparações Típicas (§ 1º)**: incorre nas mesmas sanções quem impede a procriação animal sem autorização; quem causa estragos a ninhos, tocas ou abrigos ecológicos da vida selvagem; ou quem comercializa, adquire, transporta ou guarda ovos ou crias sem comprovação de origem autorizada;
- **Faculdade do Perdão Judicial (§ 2º)**: na manutenção doméstica de animais nativos desprovida de intuito mercantil, pode o magistrado prescindir da imposição penal se o animal não integrar a lista oficial de espécies sob risco extintivo. Se o espécime estiver ameaçado, o perdão judicial é categoricamente vedado;
- **Majorantes na Fauna (§ 4º)**: a resposta sancionatória é exasperada pela metade quando cometida contra animais raros, em horários noturnos, em áreas de reserva ecológica ou mediante descumprimento dos limites da permissão concedida.

### Maus-Tratos a Animais e Inovação da Lei Sansão
- **Ofensas à Integridade Animal (art. 32)**: comete infração quem pratica atos degradantes, castigos imoderados ou mutilações contra seres da fauna urbana ou silvestre, punido com detenção de três meses até um ano e sanção pecuniária;
- **Qualificadora Específica para Cães e Gatos (Lei 14.064/2020 - § 1º-A)**: quando a agressão violenta for direcionada expressamente contra cão ou gato, a sanção corporal transmuda-se para **reclusão de dois a cinco anos**, multa e cominação obrigatória de proibição da guarda do animal vitimado. A alteração elevou a infração para patamar de gravidade incompatível com os institutos da Lei dos Juizados Especiais.

### Modalidades de Pesca Ilegal e Causas de Exclusão do Abate
- **Pesca Predatória (arts. 34 e 35)**: pescar em períodos nos quais a pesca seja proibida (defeso) ou em locais interditados atrai detenção de um a três anos. A modalidade é qualificada com reclusão de 1 a 5 anos se executada com dinamite, explosivos ou substâncias venenosas na água;
- **Causas Especiais de Justificação do Abate (Art. 37)**: não consubstancia crime o abate de animal quando realizado:
  1. Em estado de necessidade estrito, para suprir a carência alimentar grave do próprio agente ou de seus dependentes;
  2. Para proteger lavouras rurais de ataques predatórios, exigida permissão formal do Poder Público;
  3. Por ser nocivo o animal, com expressa classificação e declaração do poder competente.

### Para fixar
- A caça ou perseguição de espécimes da fauna silvestre sem licença constitui delito do art. 29.
- O perdão judicial é cabível na guarda doméstica de animais que não estejam ameaçados de extinção.
- Maus-tratos contra cães e gatos sujeitam o autor a reclusão de 2 a 5 anos e perda da guarda.
- A pesca predatória com explosivos ou substâncias tóxicas é delito punido com reclusão de um a cinco anos.
- O abate de animal para debelar a fome imediata do agente ou de seus dependentes afasta a ilicitude.
- Crimes contra a fauna cometidos em unidades de conservação ou à noite sofrem aumento de pena."""

# Segment 3: fix coincidences
summaries_a20["segments"][2]["analytic"] = """Os crimes contra a flora constituem o núcleo mais extenso da tutela penal ecológica na Lei 9.605/1998, conferindo blindagem punitiva rigorosa às áreas de preservação permanente (APP), florestas de domínio público, unidades de conservação e à circulação mercantil de produtos de origem florestal.

### Preservação Permanente e Incêndios Florestais
- **Destruição de Área de Preservação Permanente (art. 38)**: lesar ou suprimir vegetação de preservação permanente, ainda que em fase regenerativa inicial, com pena de detenção de 1 a 3 anos e multa. Se decorrer de negligência, atenua-se a reprimenda pela metade;
- **Corte Ilegal de Vegetação em APP (art. 39)**: cortar árvores em floresta de preservação permanente sem a devida autorização formal da autoridade competente;
- **Crime de Incêndio em Mata ou Floresta (art. 41)**: provocar incêndio em mata ou floresta, cominando severa pena de reclusão de 2 a 4 anos e multa. O preceito admite expressamente modalidade culposa no parágrafo único (detenção de seis meses a um ano), sancionando quem ateia queimadas descuidadas que se alastram incontrolavelmente;
- **Manejo e Soltura de Balões (art. 42)**: manufaturar, comercializar, transportar ou lançar artefatos aéreos incendiários com potencial de atear fogo em biomas florestais ou perímetros citadinos. Trata-se de ilícito formal e de perigo abstrato consumado com o manuseio desautorizado.

### Extração Mineral e Comércio Clandestino de Madeira
- **Mineração Clandestina em Vegetação Nativa (art. 44)**: retirar areia, calcário, saibro ou recursos minerais de reservas públicas ou APPs sem chancela estatal prévia (detenção de 6 meses a um ano e multa);
- **Transporte e Comércio Florestal sem Licença (art. 46)**: receber ou adquirir, para fins industriais, comerciais, energéticos ou para consumo, madeira, lenha, carvão vegetal ou outros derivados florestais, sem exigir a exibição de licença válida outorgada pelo vendedor e sem portar a guia de controle ambiental correspondente durante o percurso rodoviário ou hidroviário.

### Plantas Ornamentais e Controle de Motosserras
- **Vandalismo contra Espécimes Paisagísticos (art. 49)**: vilipendiar, arrancar ou estragar mudas e arborização estética de praças municipais ou jardins particulares, prevendo sanção de detenção e causa de diminuição se praticado culposamente;
- **Comercialização e Posse de Motosserras (art. 51)**: comercializar motosserra ou utilizá-la em floresta ou vegetação sem registro ou licença do órgão competente, viabilizando o monitoramento preventivo do desmatamento.

### Para fixar
- Destruir ou danificar floresta de preservação permanente configura crime doloso ou culposo do art. 38.
- Provocar incêndio em mata ou floresta é punido com reclusão de 2 a 4 anos, admitindo forma culposa.
- Fabricar, transportar ou soltar balões é delito formal de perigo abstrato que prescinde de incêndio.
- A extração clandestina de areia ou minerais em floresta pública ou APP configura crime do art. 44.
- Adquirir madeira ou carvão para indústria sem licença e guia ambiental válida é infração penal do art. 46.
- Destruir plantas ornamentais de vias e praças públicas consubstancia crime ambiental autônomo.
- O porte ou uso de motosserra em ambiente florestal exige registro compulsório expedido pelo órgão competente."""

# Segment 4: fix coincidences
summaries_a20["segments"][3]["analytic"] = """O diploma ambiental conclui seu sistema incriminador tutelando a incolumidade sanitária coletiva contra a poluição perigosa, resguardando o ordenamento urbanístico e o patrimônio cultural urbano, e sancionando condutas violadoras da probidade da administração ambiental desempenhada pelos órgãos do Sisnama.

### Crime de Poluição e Riscos à Incolumidade Coletiva
- **Degradação Tóxica Potencial (art. 54)**: gerar contaminação atmosférica, hídrica ou do solo em patamares graves com aptidão para lesionar a incolumidade sanitária da população ou provocar mortandade na fauna local. Trata-se de crime formal e de perigo comum abstrato ou concreto conforme o grau verificado;
- **Formas Qualificadas e Modalidade Culposa**: o delito admite a modalidade culposa no § 1º (detenção de seis meses a um ano). As penas privativas de liberdade são exasperadas para reclusão de 1 a 5 anos se a poluição tornar uma área imprópria para ocupação humana, causar poluição hídrica que interrompa o abastecimento público de água potável, ou decorrer de lançamento clandestino de efluentes e resíduos industriais perigosos;
- **Resíduos Perigosos (art. 56)**: fabricar, guardar, estocar ou dispensar produtos químicos nocivos à saúde sem observância aos padrões de controle ambiental previstos na regulação legal ou infralegal.

### Ordenamento Urbano, Pichação e Descriminalização do Grafite
- **Pichação de Fachadas e Monumentos (art. 65)**: conspurcar edificações urbanas ou muros com inscrições sem autorização, sujeitando o autor a pena de detenção de 3 meses a um ano e multa. Se o ato for perpetrado contra monumento tombado em virtude de seu valor artístico, arqueológico ou histórico, a pena eleva-se para detenção de seis meses a um ano e multa qualificada;
- **Descriminalização Expressa do Grafite (§ 2º)**: o estatuto expressamente retirou a tipicidade criminal de manifestações visuais de grafite destinadas a embelezar o espaço urbano, exigindo autorização formal do proprietário e harmonia com posturas municipais vigentes.

### Crimes contra a Administração Ambiental
- **Falsidade em Licenciamento (art. 66)**: funcionário público que faz afirmação falsa ou enganosa, omite a verdade, sonega informações ou dados técnico-científicos em procedimentos de autorização, licença ou concessão ambiental;
- **Outorga Administrativa Ilícita (art. 67)**: responsabiliza com detenção o funcionário que concede ato autorizativo ou parecer ambiental vulnerando preceitos legais e regulamentos vigentes;
- **Obstrução à Fiscalização (art. 69)**: criar embaraços ou dificultar a ação fiscalizadora exercida pelos agentes públicos ambientais competentes;
- **Perícia e Laudo Falso (art. 69-A)**: apresentar parecer técnico, estudo ecológico ou relatório em processo de licenciamento com dados fraudulentos, inexatos ou omissões relevantes, punido severamente com reclusão de 3 a 6 anos e sanção pecuniária.

### Para fixar
- O crime de poluição do art. 54 é punido nas modalidades dolosa e culposa.
- A poluição hídrica que interrompe o abastecimento urbano de água constitui forma qualificada.
- Manusear ou estocar substâncias tóxicas violando regulamentos técnicos é delito do art. 56.
- Pichar patrimônio urbano tombado atrai causa qualificadora específica na Lei de Crimes Ambientais.
- O grafite com viés artístico e prévio consentimento do titular não consubstancia crime.
- A concessão de licença ambiental em desconformidade com a lei por servidor público é crime autônomo.
- Apresentar estudo ambiental falso ou omisso em licenciamento atrai reclusão de 3 a 6 anos."""

Path("content/items/legislacao-penal-especial/a20.json").write_text(json.dumps(items_a20, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a20.json").write_text(json.dumps(summaries_a20, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved fixed a20 successfully.")
