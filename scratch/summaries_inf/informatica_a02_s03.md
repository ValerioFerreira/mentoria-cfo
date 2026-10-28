##### informatica/a02/s03
A segurança da informação apoia-se em ramos matemáticos e tecnológicos complementares para blindar a confidencialidade e a integridade de mensagens corporativas: a criptologia, subdividida em criptografia e criptoanálise, a esteganografia e os paradigmas simétrico, assimétrico e híbrido de cifragem.

### Criptologia, Esteganografia e Criptoanálise

A Criptologia é a ciência abrangente que reúne o estudo de cifras e técnicas de decodificação analítica:

- **Criptografia versus Esteganografia**:
  - *Criptografia*: arte e técnica de converter uma mensagem clara inteligível em texto cifrado ininteligível. A existência da comunicação é manifesta e explícita, mas seu conteúdo semântico permanece protegido contra leitura desautorizada.
  - *Esteganografia*: técnica de camuflar e ocultar a própria existência da mensagem em outro invólucro ou portador multimídia aparentemente inofensivo (como fotos, arquivos de áudio, textos com espaçamentos invisíveis ou canais cobertos). O observador externo desconhece que há qualquer dado sensível sendo transmitido.
- **Criptoanálise**: estudo analítico e dedutivo de métodos para contornar, quebrar ou descriptografar textos cifrados sem conhecimento legítimo prévio das chaves originais. O confronto contínuo entre criptógrafos e criptoanalistas impulsiona a evolução dos algoritmos protetivos.

### Criptografia Simétrica (Chave Privada / Chave Secreta)

O paradigma simétrico apoia-se no compartilhamento de uma única chave secreta entre os polos comunicantes, utilizada tanto na fase de cifragem do texto original quanto na etapa reversa de decifragem:

- **Operações Fundamentais**: historicamente alicerça-se em substituição (mapeamento de caracteres claros por outros elementos) e transposição (permutação espacial ordenada das posições dos elementos originais sem perda de dados).
- **Vantagens Operacionais**: reduzido custo computacional, processamento matemático veloz e eficiência para cifrar volumes maciços de dados em tempo real.
- **Limitações e Gerenciamento**: enfrenta o gargalo da distribuição segura da chave secreta através de canais potencialmente inseguros. A escalabilidade é complexa em grandes redes, demandando n(n - 1) / 2 chaves distintas para interconectar n usuários de modo privativo.
- **Propriedades de Segurança**: preserva confidencialidade, integridade e autenticidade (se garantido o conhecimento restrito a apenas duas partes), mas não assegura o não-repúdio, pois ambos os participantes detêm a mesma chave idêntica.
- **Principais Algoritmos**: AES (*Advanced Encryption Standard*), DES, 3DES, RC4, Blowfish e IDEA.

### Criptografia Assimétrica (Chave Pública)

Desenvolvida para dirimir a vulnerabilidade de distribuição da chave simétrica, a criptografia de chave pública fundamenta-se em pares matematicamente correlacionados de chaves assimétricas:

- **Funcionamento do Par**:
  - *Chave Pública*: amplamente divulgada a qualquer interessado, inserida em repositórios abertos e utilizada rotineiramente para cifrar informações endereçadas ao dono do par.
  - *Chave Privada*: mantida em segredo absoluto e de posse exclusiva e personalíssima do seu titular, requerida para decifrar conteúdos previamente encriptados com a chave pública correspondente.
- **Propriedades e Não-Repúdio**:
  - Cifrar com a *chave pública do destinatário* garante **confidencialidade**, já que somente a chave privada dele poderá decodificar a carga.
  - Cifrar (ou assinar) com a *chave privada do remetente* garante **autenticidade** e **não-repúdio** (irretratabilidade), pois se a mensagem é decifrável pela chave pública dele, unicamente o detentor da respectiva chave privada poderia tê-la gerado.
- **Desempenho e Chaves**: demanda chaves substancialmente mais extensas e algoritmos mais lentos computacionalmente (a fonte fala em até cem vezes mais lentos que a cifragem simétrica, como ordem de grandeza). O gerenciamento de chaves é simplificado, necessitando de apenas 2n chaves para um ecossistema com n participantes.
- **Principais Algoritmos**: RSA, DSA, ECC/ECDSA, ElGamal e o protocolo de intercâmbio de chaves Diffie-Hellman.

### Criptografia Híbrida e Princípio de Kerckhoffs

Na prática da Internet contemporânea, as limitações individuais de desempenho e distribuição são equalizadas:

- **Criptografia Híbrida**: combina a velocidade do método simétrico com a segurança de intercâmbio do método assimétrico. Em protocolos como TLS/SSL e HTTPS, utiliza-se a criptografia assimétrica pontualmente para negociar e trocar uma chave simétrica temporária e descartável (denominada **chave de sessão**). Estabelecido o canal, todo o fluxo volumoso de dados da sessão passa a ser cifrado exclusivamente pelo algoritmo simétrico de alto desempenho.
- **Princípio de Kerckhoffs**: postulado clássico segundo o qual o que protege o sistema é a chave (seu sigilo e seu tamanho em bits), e não o segredo dos detalhes do algoritmo, que pode e deve ser público. Três fatores influenciam a segurança: a força computacional do algoritmo (um algoritmo simples demais é fraco), o sigilo da chave e o comprimento da chave. Os detalhes de implementação são irrelevantes para a segurança. Algoritmos criptográficos robustos devem ser integralmente públicos e amplamente testados pela comunidade científica contra ataques diversos.

### Detalhes que caem em prova

- **Criptologia = criptografia + criptoanálise.** A ocultação da informação pode ser feita por esteganografia ou por criptografia; a quebra dos segredos é feita pela criptoanálise. A criptografia tem dois grupos: **códigos** (palavras, símbolos ou frases que substituem elementos do texto claro) e **cifras** (algoritmos de cifragem e decifragem), que usam transposição e substituição sem perder informação.
- **Esteganografia:** ocultar uma mensagem dentro de outra (imagens, sons, vídeos, textos), por exemplo alterando poucos bits de uma imagem de forma imperceptível. Não é algoritmo criptográfico simétrico, não é análise de desempenho, não tem relação com hash e não é a técnica de decifrar sem conhecer o algoritmo (isso é criptoanálise). Também não se confunde com codificar binários em texto ASCII (Base64).
- **Hash** não é criptografia: é função unidirecional que gera um resumo fixo e não permite recuperar a mensagem. **Assinatura digital** assina com a chave privada e confere com a pública (autenticidade e integridade), não para cifrar o conteúdo.
- **Cifra de César:** substitui cada letra por outra três posições adiante no alfabeto (A vira D); a chave é 3. Serve para ilustrar substituição e chave simétrica. A máquina Enigma, de rotores, foi usada pelos nazistas na Segunda Guerra, e a máquina Bombe, de Alan Turing, ajudou a decifrar suas mensagens.
- **Sinônimos da simétrica:** chave secreta, chave única, chave compartilhada, chave privada ou convencional. A criptografia por si só garante a confidencialidade; os algoritmos simétricos podem dar também integridade (comparando com o texto em claro enviado junto) e autenticidade (se só duas partes conhecem a chave), mas não o não-repúdio, porque qualquer uma das partes pode negar o envio. Quanto mais partes compartilham a chave, maior o risco de comprometimento.
- **Assimétrica:** o par de chaves é exclusivo; o que uma cifra, só a outra decifra. Cifrar com a pública do destinatário dá confidencialidade; cifrar com a privada do emissor não dá confidencialidade (qualquer um tem a pública), mas dá autenticidade e, junto com a integridade, não-repúdio. Sempre que há não-repúdio há autenticidade, mas o contrário não vale. Simétrica: confidencialidade, integridade e autenticidade; assimétrica: todas essas mais o não-repúdio.
- **Comparação:** a simétrica tem menor custo computacional e chaves menores para o mesmo nível de segurança; a assimétrica usa chaves maiores, mas simplifica o gerenciamento (2n chaves contra n(n−1)/2). Exemplo: com 10 pessoas, são 45 chaves simétricas ou 20 chaves assimétricas.
- **Segurança computacional:** os sistemas atuais são considerados computacionalmente seguros (quebrá-los leva mais tempo que a vida útil da informação ou custa mais que o valor dela), e não incondicionalmente seguros. Afirmar que são incondicionalmente seguros está errado.
- **SSL/TLS:** usa chave de sessão; a troca da chave é assimétrica e o tráfego principal é simétrico. A cifra de chave de sessão é a resposta de provas sobre o SSL.
- **Kerckhoffs em prova:** o criptoanalista deve ser considerado conhecedor dos métodos genéricos de cifragem; algoritmos devem ser públicos e chaves secretas; resistir a um ataque só com texto cifrado não prova que a cifra é segura.

### Para fixar

- Esteganografia oculta a existência da mensagem; criptografia torna a mensagem ilegível, mas visível.
- Simétrica: chave única compartilhada, rápida (AES, DES); para n pessoas exige n(n - 1)/2 chaves e não dá não repúdio.
- Assimétrica: par de chaves pública/privada (RSA, ECC); exige 2n chaves e viabiliza o não repúdio.
- Criptografia híbrida (ex.: TLS): a assimétrica negocia uma chave simétrica de sessão, temporária, que cifra os dados.
- Princípio de Kerckhoffs: o algoritmo pode ser público; a segurança repousa apenas no sigilo da chave.

