##### informatica/a02/s01
A salvaguarda de ativos corporativos articula a preservação das propriedades nucleares da informação mediante a aplicação coordenada de defesas materiais, lógicas e gerenciais estruturadas para neutralizar ameaças.

### O Escopo Institucional da Segurança da Informação

- **Definição Normativa**:
  - Disciplina orientada a resguardar o patrimônio informativo de uma organização, garantindo a sua disponibilidade contínua, a veracidade integral dos dados (integridade) e o sigilo rigoroso perante terceiros (confidencialidade), em consonância com as normas da família ISO/IEC 27000.
  - Abrange tanto os registros codificados eletronicamente em bancos de dados quanto documentos físicos em papel, canais de voz e o conhecimento intelectual de colaboradores.

### Arquitetura de Controles e Mecanismos de Proteção

- **Controles Físicos**:
  - Obstáculos materiais tangíveis projetados para restringir a aproximação humana e proteger a infraestrutura contra sinistros ambientais.
  - Englobam portas com fechaduras biométricas, torniquetes, vigilância patrimonial presencial, sistemas de circuito fechado de televisão (CFTV), alarmes de intrusão perimetral, detectores térmicos de fumaça e geradores de energia autônomos.
- **Controles Lógicos (Tecnológicos)**:
  - Barreiras digitais implementadas por software e firmware para blindar o ambiente computacional.
  - Compreendem sistemas operacionais protegidos por senhas complexas, firewalls de borda para filtragem de pacotes, cifras criptográficas assimétricas e simétricas, antivírus com varredura contínua, listas de controle de acesso (ACLs) e sensores de prevenção de intrusão (IPS).
- **Controles Administrativos (Organizacionais)**:
  - Diretrizes institucionais formalizadas que disciplinam a conduta dos usuários e estruturam a governança da entidade.
  - Abrangem a formulação da Política de Segurança da Informação (PSI), termos de sigilo e não divulgação (NDA), programas periódicos de capacitação e treinamentos contra engenharia social.
- **Enquadramento Funcional**:
  - *Preventivos*: antecipam-se ao problema para impedir o acontecimento da falha.
  - *Detectivos*: alertam instantaneamente sobre violações em curso.
  - *Corretivos*: restauram as operações normais e reparam arquivos após a ocorrência do dano.

### Taxonomia de Riscos e Ciclo de Incidentes

- **Cadeia de Elementos de Segurança**:
  - *Ativo*: qualquer bem material, digital ou humano que possua valor intrínseco para a instituição e justifique investimento defensivo.
  - *Vulnerabilidade*: fraqueza existente que diminui a resistência do ativo a agressões.
  - *Ameaça*: agente ou evento probabilístico capaz de tirar proveito de uma vulnerabilidade.
  - *Incidente de Segurança*: confirmação de um evento inesperado ou malicioso que rompe os postulados de proteção e gera prejuízo operacional ou financeiro.

### Detalhes que caem em prova

- **Definições aceitas:** proteção de informações e sistemas contra acesso, uso, divulgação, interrupção, modificação ou destruição não autorizados; ou conjunto de estratégias para prevenir, detectar, documentar e combater ameaças.
- **Decreto nº 9.637 (PNSI):** institui a Política Nacional de Segurança da Informação na Administração Pública Federal e busca assegurar disponibilidade, integridade, confidencialidade e **autenticidade** em nível nacional. A segurança da informação, nesse decreto, abrange segurança cibernética, defesa cibernética, segurança física e proteção de dados organizacionais, e as ações para garantir aqueles quatro atributos.
- **Tríade CID:** confidencialidade (a informação não é revelada a quem não está autorizado), integridade (exatidão e completeza) e disponibilidade (acessível e utilizável quando uma entidade autorizada precisa). Não há hierarquia entre os três; desrespeitar um ou mais deles configura incidente.
- **Tipos de controle:** a classificação tradicional tem dois grandes tipos, **físicos** (barreiras que limitam o acesso direto à informação ou à infraestrutura: portas, trancas, vigilantes, geradores, câmeras, alarmes, catracas, cadeados, salas-cofre, crachás) e **lógicos ou técnicos** (limitam o acesso por monitoramento e controle de acesso: senhas, firewalls, ACLs, criptografia, IDS, IPS). Controles processuais/administrativos (por exemplo, trocar a senha periodicamente) não aparecem em bibliografias clássicas, mas já foram cobrados.
- **Regra-chave:** o tipo do controle depende do **recurso protegido**, não do método de autenticação. Biometria para entrar numa sala é controle físico; biometria para acessar um sistema é controle lógico. Há quem classifique a biometria de formas diferentes, por isso observe o que está sendo protegido.
- **Pegadinhas já cobradas:** dizer que controles físicos são soluções implantadas no sistema operacional está errado (isso é controle lógico); dizer que os controles lógicos são só software também é incompleto, pois podem usar hardware ou software e os físicos são barreiras físicas.

| Termo | Definição |
| --- | --- |
| Ativo | qualquer coisa de valor para a instituição: informação, pessoas, serviços, software, hardware, documentos |
| Agente | fonte de um evento que pode afetar adversamente um ativo (funcionário, meio ambiente, hacker) |
| Vulnerabilidade | fragilidade de ou associada a um ativo, que ameaças podem explorar |
| Ameaça | agente externo que, aproveitando vulnerabilidades, pode quebrar a CID e causar perda ou desastre |
| Ataque | exploração de uma vulnerabilidade por uma ameaça para obter, alterar, destruir, remover, implantar ou revelar informação sem autorização |
| Evento | ocorrência identificada em sistema, serviço ou rede que indica possível violação da política ou falha de controle |
| Incidente | fato decorrente de um ataque bem-sucedido, com consequências negativas |
| Impacto | abrangência dos danos de um incidente sobre processos de negócio |
| Risco | probabilidade de um evento causar dano a ativos |

- **Ameaça × risco:** ameaça é um dano potencial (pode haver dano ou não); risco avalia a probabilidade de o incidente ocorrer e o impacto associado, normalmente a chance de uma ameaça se concretizar explorando uma vulnerabilidade.
- **Exemplo do carro:** o carro novo é o ativo; estacioná-lo longe é uma decisão diante de um evento; os assaltantes são os agentes; a falta de alarme é a vulnerabilidade; a chance de furto é o risco; o assaltante que anuncia o crime é a ameaça; o roubo em si é o ataque; perder o carro de vez é o impacto.
- **Ameaça é fator externo** que pode gerar incidente explorando vulnerabilidades (afirmação considerada certa em prova).

### Para fixar

- Pilares da segurança da informação (ISO 27001): confidencialidade, integridade e disponibilidade.
- Controles físicos: portas, catracas, extintores, CFTV.
- Controles lógicos: senhas, antivírus, firewall, criptografia.
- Controles administrativos: políticas de segurança e treinamentos.
- Quanto à função, os controles podem ser preventivos, detectivos ou corretivos.
- Ativo é o bem a proteger; vulnerabilidade é a brecha; ameaça é o perigo potencial; incidente é a concretização do dano.

