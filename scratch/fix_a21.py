import json
from pathlib import Path

# Load items and summaries from build_a21.py
import sys
sys.path.insert(0, '.')
import scratch.build_a21 as b21

items_a21 = b21.items_a21
summaries_a21 = b21.summaries_a21

# Fix items s03 teoria[0] and revisao[0]
items_a21["segments"][2]["bizu"]["teoria"][0]["statement"] = "O delito de possuir ou portar armamento classificado como de uso restrito comum permanece categorizado como infração hedionda após o Pacote Anticrime."
items_a21["segments"][2]["bizu"]["revisao"][0]["statement"] = "A guarda clandestina de armamento de calibre permitido no ambiente domiciliar sujeita o autor a pena privativa de liberdade sob a modalidade de reclusão inafiançável."
items_a21["segments"][2]["bizu"]["revisao"][0]["explanation"] = "O art. 12 comina pena detentiva de um a três anos e sanção pecuniária, admitindo arbitramento de fiança policial pelo delegado de polícia."

# Fix summaries s01: expand and eliminate coincidence
summaries_a21["segments"][0]["analytic"] = """A Lei 10.826/2003, denominada Estatuto do Desarmamento, estabeleceu a disciplina jurídica sobre o registro, controle da posse e restrição ao porte de armas de fogo e munições em âmbito nacional. O diploma estruturou uma rígida política de fiscalização armamentista, fruto dos debates que culminaram no histórico referendo popular de 2005 sobre a comercialização de armamentos, delineando esferas de atribuição administrativa entre órgãos civis e militares para restringir a circulação clandestina de armamentos no país.

### Sistema Nacional de Armas e Repartição de Atribuições com o SIGMA
O modelo de controle armamentista assenta-se em uma bifurcação orgânica de competências:
- **Atribuições do SINARM (arts. 1º e 2º)**: instituído no âmbito da Polícia Federal e vinculado ao Ministério da Justiça, congrega atribuições de identificação pericial e cadastro geral de armas de fogo produzidas, comercializadas, transferidas ou apreendidas em território brasileiro; cadastra as autorizações de porte e registro emitidas a cidadãos civis, policiais civis, guardas municipais e empresas de segurança privada;
- **Esfera de Atuação do SIGMA**: gerido pelo Comando do Exército sob a égide do Ministério da Defesa, detém competência privativa para autorizar e registrar armamentos bélicos dos quadros das Forças Armadas, das corporações militares estaduais e corpos de bombeiros, além de supervisionar as atividades de atiradores desportivos, colecionadores e caçadores cadastrados (CACs). O sistema cataloga armas portáteis, de repetição ou semiautomáticas, de alma raiada ou alma lisa, e calibres com especificações de cano longo ou curto.

### Requisitos Substanciais para Aquisição Civil de Arma de Fogo
A aquisição de armamento de uso permitido no comércio regular depende de comprovação de pressupostos cumulativos:
- **Idade Mínima de 25 Anos**: exigência de maturidade etária civil, ressalvados os integrantes de carreiras institucionais de segurança pública e corporações armadas;
- **Declaração de Efetiva Necessidade**: apresentação de motivos concretos que justifiquem a detenção da arma para proteção pessoal ou patrimonial;
- **Idoneidade Pessoal Comprovada**: juntada de certidões negativas de antecedentes criminais das Justiças Federal, Estadual, Militar e Eleitoral, além da demonstração cabal de ausência de inquérito policial ou ação penal condenatória em andamento;
- **Capacidade Técnica e Psicológica**: aprovação em testes de tiro prático e laudo conclusivo de aptidão mental emitido por psicólogo credenciado na Polícia Federal;
- **Comprovação de Ocupação Lícita e Domicílio Certo**: demonstração documental de trabalho regular e residência fixa.

### Distinção entre Registro Predial e Autorização de Porte
- **Certificado de Registro de Arma de Fogo (CRAF - art. 5º)**: autorização meramente predial, expedida pela Polícia Federal, que faculta ao titular manter o armamento exclusivamente no interior de sua moradia residencial ou dependências fechadas desta, ou ainda em seu local de trabalho, desde que figure como titular da empresa ou responsável legal pelo estabelecimento;
- **Porte de Arma de Fogo (art. 10)**: autorização excepcionalíssima e precária outorgada pelo Diretor-Geral da Polícia Federal, exigindo demonstração inequívoca de risco profissional ou ameaça concreta à integridade física do postulante.

### Para fixar
- O SINARM funciona no âmbito da Polícia Federal e controla armamentos de uso permitido civis.
- O SIGMA é administrado pelo Exército Brasileiro para gerir arsenais militares e de CACs.
- A aquisição de arma de fogo exige idade mínima de vinte e cinco anos e aptidão psicológica.
- O registro (CRAF) autoriza a guarda da arma exclusivamente em domicílio ou no local de trabalho do titular.
- O porte de arma constitui concessão precária e discricionária outorgada pela Polícia Federal.
- O furto ou extravio de arma particular deve ser comunicado à polícia em até vinte e quatro horas."""

# Fix summaries s02: eliminate coincidences
summaries_a21["segments"][1]["analytic"] = """O Estatuto do Desarmamento estabeleceu prerrogativas institucionais para o exercício do porte funcional de armas de fogo, conferindo autorização legal direta a corporações policiais e carreiras estatais encarregadas da preservação da ordem pública e da soberania nacional, além de disciplinar o porte de subsistência e a entrega espontânea de armamentos.

### Rol de Agentes com Porte de Arma Funcional
O art. 6º da Lei 10.826/2003 elenca taxativamente as categorias profissionais detentoras de porte por prerrogativa funcional do cargo:
- **Integrantes das Forças Armadas**: membros da Marinha, Exército e Aeronáutica;
- **Órgãos de Segurança Pública Constitucionais (art. 144 da CF)**: integrantes da Polícia Federal, Polícia Rodoviária Federal, Polícia Ferroviária Federal, Polícias Civis, Polícias Militares, Corpos de Bombeiros Militares e Polícias Penais distrital, estaduais e federal, possuindo porte funcional com validade nacional mesmo fora do serviço;
- **Guardas Municipais e Pacificação pelo STF**: o legislador originário tentou graduar o porte das guardas conforme a densidade populacional do município. Contudo, o Pleno do Supremo Tribunal Federal (julgamento conjunto das ADIs 5948, 5538 e ADPF 524) **declarou inconstitucionais todas as travas demográficas**, reconhecendo que **todos os integrantes das Guardas Municipais do país possuem legitimidade funcional para portar armas institucionais nas atividades operacionais e nos períodos de folga**;
- **Outras Categorias Autorizadas**: agentes da Agência Brasileira de Inteligência (ABIN), agentes do Gabinete de Segurança Institucional (GSI), auditores-fiscais e analistas da Receita Federal e da Auditoria Fiscal do Trabalho.

### Porte de Subsistência e Trânsito de Desportistas
- **Porte de Subsistência Rural (art. 6º, § 5º)**: outorga especial concedida a moradores rurais maiores de 25 anos que demonstrem a imprescindibilidade do artefato bélico para garantir a subsistência alimentar familiar, restrito a uma espingarda de alma lisa de calibre permitido;
- **Caçadores, Atiradores e Colecionadores (CACs)**: o deslocamento de armamento de tiro desportivo e coleção submete-se à estrita expedição de guia de tráfego pelo Comando do Exército, devendo a arma ser transportada desmuniciada em estojo ou embalagem de resguardo.

### Política de Desarmamento e Entrega Espontânea de Armas
Os arts. 31 e 32 consagraram uma política permanente de anistia indenizada. Qualquer cidadão que possua arma irregular, com registro vencido ou sem origem documentada, pode entregá-la espontaneamente nos postos credenciados da Polícia Federal. A legislação assegura sigilo absoluto ao entregador, indenização financeira fixada em tabela ministerial e atipicidade penal absoluta do transporte do artefato, desde que acobertado por prévia guia de trânsito retirada via internet.

### Para fixar
- Policiais civis, militares, federais e penais possuem porte de arma funcional em serviço e folga.
- O STF julgou inconstitucional o critério populacional, garantindo porte a todas as guardas municipais.
- Integrantes da Receita Federal e do Trabalho possuem porte funcional para missões fiscalizatórias.
- O porte de subsistência é reservado a residentes rurais que dependem da caça para alimentar a família.
- Atiradores desportivos e CACs devem transportar armas desmuniciadas sob guia de tráfego do Exército.
- A entrega voluntária de arma de fogo perante a autoridade afasta o crime e confere indenização estatal."""

# Fix summaries s03: eliminate coincidence in omissao de cautela
summaries_a21["segments"][2]["analytic"] = """O capítulo incriminador da Lei 10.826/2003 tutela a incolumidade pública contra a circulação, comércio e guarda desautorizada de armas, acessórios e munições, escalonando as sanções criminais de acordo com o potencial lesivo do artefato e a gravidade social da conduta, com reflexos diretos na Lei de Crimes Hediondos.

### Posse Irregular e Porte Ilegal de Armas de Calibre Permitido
- **Posse Irregular em Domicílio (art. 12)**: manter sob guarda arma, acessório ou munição de calibre permitido no interior da residência ou dependência desta, ou no local de trabalho do responsável legal, sem autorização ou com registro vencido. Trata-se de infração de perigo abstrato punida com **detenção de um a três anos e multa**, permitindo fiança diretamente na delegacia;
- **Porte Ilegal de Uso Permitido (art. 14)**: portar, transportar, ter em depósito ou circular com arma, acessório ou munição permitida fora dos limites residenciais ou funcionais sem autorização. Delito formal punido com **reclusão de dois a quatro anos e multa**, cuja fiança sujeita-se à esfera judicial;
- **Omissão de Cautela (art. 13)**: negligenciar os cuidados indispensáveis de guarda e segurança, possibilitando que menor de dezoito anos ou pessoa com déficit mental se apodere indevidamente do armamento (pena de detenção e multa).

### Disparo em Via Pública e Subsidiariedade Expressa
O art. 15 incrimina disparar arma de fogo ou detonar projétil em áreas habitadas, imediações comunitárias ou em direção a vias públicas urbanas, cominando pena de **reclusão de 2 a 4 anos e multa**. O tipo expressamente encerra cláusula de subsidiariedade expressa (*desde que a conduta não tenha por finalidade a prática de outro crime*), sendo absorvido se configurar crime-meio para homicídio, lesão corporal, roubo ou ameaça.

### Armas de Uso Restrito, Raspadas e Hediondez de Uso Proibido
- **Uso Restrito Comum (art. 16, caput)**: possuir ou portar arma de uso restrito atrai **reclusão de três a seis anos e multa**. A Lei 13.964/2019 (Pacote Anticrime) **retirou a natureza hedionda do porte de arma de uso restrito comum**;
- **Armas com Numeração Raspada (art. 16, § 1º, I)**: raspar, suprimir ou adulterar sinal de identificação ou numeração de série equipara a conduta às penas do art. 16, independentemente de a arma ser de calibre originalmente permitido;
- **Arma de Fogo de Uso Proibido (art. 16, § 2º)**: portar ou possuir arma, acessório ou munição de uso proibido (como armas dissimuladas ou bélicas) atrai severa pena de **reclusão de 4 a 12 anos**. Essa conduta específica é **expressamente catalogada como crime hediondo** na Lei 8.072/1990.

### Comércio Clandestino, Tráfico Internacional e Majorantes
- **Comércio Ilegal de Arma de Fogo (art. 17)**: comercializar clandestinamente armas, acessórios ou munições em atividade industrial ou comercial ilícita, com pena de **reclusão de 6 a 12 anos e multa**, qualificado como **crime hediondo**;
- **Tráfico Internacional de Arma de Fogo (art. 18)**: importar ou exportar armamento, acessórios ou munição transpondo fronteiras sem autorização, punido com **reclusão de 8 a 16 anos e multa**, igualmente dotado de **natureza hedionda**;
- **Causas Especiais de Exasperação de Pena (arts. 19 e 20)**: aumento de metade nas penas se a infração for praticada por integrante de forças policiais, guardas armadas ou empresas de segurança privada, ou se o agente for reincidente específico em crimes da lei.

### Para fixar
- A posse irregular do art. 12 ocorre no interior da residência ou trabalho, punida com detenção.
- O porte ilegal do art. 14 perfaz-se fora do ambiente domiciliar, punido com reclusão de 2 a 4 anos.
- O disparo de arma de fogo é delito expressamente subsidiário punido com reclusão de 2 a 4 anos.
- A arma com numeração de série raspada equipara-se à arma de uso restrito em qualquer hipótese.
- O porte ou posse de arma de fogo de uso proibido é crime hediondo na Lei 8.072/1990.
- O comércio ilegal e o tráfico internacional de armas são crimes hediondos punidos com penas gravosas.
- As penas sofrem aumento da metade se cometidas por servidores da segurança pública ou reincidentes específicos."""

Path("content/items/legislacao-penal-especial/a21.json").write_text(json.dumps(items_a21, ensure_ascii=False, indent=2), encoding="utf-8")
Path("content/summaries/legislacao-penal-especial/a21.json").write_text(json.dumps(summaries_a21, ensure_ascii=False, indent=2), encoding="utf-8")
print("Saved fixed a21 successfully.")
