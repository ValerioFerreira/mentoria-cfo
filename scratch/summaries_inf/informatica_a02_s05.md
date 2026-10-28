##### informatica/a02/s05
Este trecho mostra como a assinatura digital combina hash e criptografia assimétrica, compara os principais algoritmos de hash (MD5, SHA-1, SHA-256), explica o uso do hash na perícia digital, separa identificação, autenticação e autorização e apresenta a classificação de dados em níveis.

### Assinatura digital: o que garante

Assinar por meio digital é mais rápido e seguro do que o papel (que pode ser falsificado ou perdido) e tem o **mesmo valor legal** de uma assinatura de próprio punho. Lembrete de criptografia assimétrica: cifrar com a **chave pública do destinatário** dá confidencialidade; cifrar com a **chave privada do autor** dá autenticidade. A assinatura digital vai além e garante três propriedades:

- **Autenticidade**: confirma quem assinou.
- **Integridade**: prova que o documento não foi alterado depois de assinado.
- **Irretratabilidade (não repúdio)**: o signatário não pode negar a assinatura.

Para isso funcionar é preciso entender o **algoritmo de hash**.

### Algoritmo de hash (função de resumo)

Também conhecido como função de resumo ou função módulo, transforma uma entrada de **qualquer tamanho** (uma palavra ou um vídeo inteiro) em uma saída de **tamanho fixo**, que funciona como uma "impressão digital" do conteúdo. A analogia é o resto da divisão: 10 ÷ 3 deixa resto 1 e 942.386 ÷ 3 deixa resto 2; a entrada muda de tamanho, a saída continua sendo um dígito.

Propriedades que precisam ser memorizadas:

| Propriedade | Significado |
| --- | --- |
| Tamanho fixo | Entrada qualquer, saída sempre do mesmo tamanho |
| Unidirecional (one-way) | Gera-se o hash a partir do dado, mas não se recupera o dado a partir do hash |
| Determinístico | A mesma entrada sempre produz o mesmo hash |
| Efeito avalanche | Mudar um caractere ou bit altera o hash por completo (base da integridade) |
| Resistência a colisões | Deve ser praticamente impossível achar duas entradas com o mesmo hash |

**Colisão** é quando entradas diferentes geram a mesma saída (no exemplo do resto, 10 ÷ 3 e 13 ÷ 3 dão ambos resto 1). Por ser altamente suscetível a colisões, a função resto serve só de analogia, não de algoritmo real. Para reduzir colisões, aumenta-se o tamanho da saída: hashes criptográficos modernos exigem no mínimo 128 bits (2^128 combinações).

Exemplos cotidianos: o **dígito verificador** do boleto e os dois últimos dígitos do **CPF** são calculados sobre os demais números; se alguém digitar errado, o dígito não confere. E, sabendo só o dígito, não se descobre os números originais.

> 💡 Senhas: bons sistemas guardam apenas o **hash da senha**. No login, geram o hash da senha digitada e comparam com o armazenado; se coincidirem, o acesso é liberado. Assim, o vazamento do banco não expõe as senhas em texto puro.

### Como a assinatura digital é feita e verificada

1. Maria escreve a mensagem em texto claro e gera o **hash** dela.
2. Maria **criptografa o hash com a sua chave privada**: isso é a assinatura digital.
3. Maria envia a mensagem original (em claro) e o hash criptografado.
4. João calcula um novo hash da mensagem recebida e **descriptografa a assinatura com a chave pública de Maria**.
5. Se os dois hashes forem iguais: a mensagem não foi alterada (integridade), foi assinada pela chave privada de Maria (autenticidade) e, por isso, ela não pode negar o envio (irretratabilidade).

> ⚠️ Pegadinhas: (1) a assinatura digital **não garante confidencialidade**, pois a mensagem segue legível por qualquer pessoa; (2) o hash **não criptografa** o documento, ele só resume; o que se criptografa com a chave privada é o hash; (3) só a chave pública de Maria consegue abrir o que foi cifrado com a chave privada dela, e é daí que vem a prova de autoria.

### Algoritmos de hash

| Algoritmo | Saída | Situação |
| --- | --- | --- |
| MD5 (1991) | 128 bits (16 bytes) | Foram achadas colisões; não recomendado para certificação, autenticação e senhas. Ainda aparece em sistemas legados e checagem rápida de arquivos |
| SHA-1 (NSA, 1995) | 160 bits (20 bytes) | Em 2017 o Google gerou a primeira colisão real; considerado obsoleto, desencorajado por NIST, Microsoft, Google e Mozilla |
| SHA-256 (família SHA-2, NSA) | 256 bits (32 bytes) | Seguro; nenhuma colisão prática conhecida; também há SHA-512 (512 bits) e SHA-3 |

Usos do SHA-256: blockchain do Bitcoin (validar transações e minerar blocos), certificados digitais e SSL/TLS, assinaturas digitais e armazenamento de senhas (combinado com técnicas como **salting** e **stretching**). Como é mais robusto, exige mais processamento, o que pesa em dispositivos limitados (smartwatches, sistemas embarcados), mas o custo compensa.

#### Hash na perícia digital

A **cadeia de custódia** é a sequência documentada de controle e proteção de tudo que é coletado em uma investigação, para provar que a evidência permaneceu intacta e quem a manuseou. O hash é o instrumento que garante isso:

- O perito calcula o hash do dispositivo original (HD, celular, pendrive), faz a **imagem forense** (cópia bit a bit) e calcula o hash da cópia. Hashes idênticos provam que a cópia é perfeita.
- Nas etapas seguintes (transferência, análise, apresentação no tribunal) o hash é conferido de novo; se coincidir, ninguém alterou a prova.

### Controle de acesso

Conjunto de práticas e tecnologias para que **só usuários autorizados** acessem sistemas, redes e informações, apoiado em três etapas em sequência:

| Aspecto | Identificação | Autenticação | Autorização |
| --- | --- | --- | --- |
| Pergunta | Quem está tentando entrar? | Prove que é essa pessoa | O que essa pessoa pode fazer? |
| Exemplos | Login, matrícula, e-mail, CPF | Senha, biometria, token, SMS, smartcard | Ler, editar ou excluir dados, mudar configurações |
| Momento | Primeira etapa | Segunda, logo após a identificação | Depois da autenticação bem-sucedida |
| Segurança | Baixa: apenas declara quem é | Média: exige prova | Alta: limita as ações mesmo após autenticar |

- Identificação é apenas a declaração de identidade; o sistema ainda não sabe se é verdade.
- Autenticação pode usar um fator ou vários: senha + impressão digital é **autenticação multifator (MFA)**.
- Autorização é definida por políticas, cargos, grupos ou regras (por exemplo, usuário que só lê relatórios versus usuário que edita e exclui). Em questões, "determinar as ações que a entidade pode executar" é a autorização.

### Classificação de dados

Consiste em reconhecer, categorizar e rotular a informação conforme **sensibilidade, criticidade e impacto** para a organização, para aplicar controles proporcionais ao risco (sem expor dados sensíveis nem exagerar nos controles de dados de pouco valor). Considera confidencialidade, integridade e disponibilidade e apoia políticas internas, treinamentos, conformidade (LGPD, ISO/IEC 27001) e resposta a incidentes.

| Nível | Descrição | Exemplos | Controles típicos |
| --- | --- | --- | --- |
| Público | Divulgação livre, sem prejuízo | Conteúdo de site, comunicados oficiais | Integridade básica, controle de versão, backups simples |
| Interno | Uso da organização; vazamento causa impacto moderado | Organogramas, manuais, relatórios não estratégicos | Controle de acesso interno, autenticação, política de uso aceitável |
| Confidencial | Divulgação indevida gera prejuízo financeiro, legal ou de imagem | Dados pessoais, contratos, relatórios financeiros | Acesso restrito, criptografia, logs, monitoramento |
| Restrito | Altamente crítico; acesso indevido causa dano grave ou irreversível | Segredos industriais, chaves criptográficas, dados estratégicos | Mínimo privilégio, criptografia forte, segregação de ambientes, auditoria contínua |

### Para fixar

- Assinatura digital = hash da mensagem cifrado com a chave privada do remetente; garante autenticidade, integridade e irretratabilidade, mas não confidencialidade.
- A verificação usa a chave pública do remetente e compara os hashes recalculado e recebido.
- Hash: entrada qualquer, saída fixa, unidirecional, determinístico; mudança mínima altera tudo.
- Colisão: entradas diferentes com o mesmo hash; saídas maiores reduzem o risco.
- MD5 (128 bits) e SHA-1 (160 bits) estão quebrados; SHA-256 (256 bits, família SHA-2) é o atual.
- Na perícia, o hash prova que a evidência e a imagem forense não foram alteradas (cadeia de custódia).
- Identificação (quem sou), autenticação (prova) e autorização (permissões), nessa ordem.
- Níveis de classificação: público, interno, confidencial e restrito.

