##### informatica/a02/s04
Este trecho compara os principais algoritmos de criptografia e trata da autenticidade: os três fatores de autenticação (saber, ter, ser), senhas, PIN, biometria, tokens, aplicativos autenticadores e a autenticação forte, multifator e em dois fatores.

### Principais algoritmos de criptografia

| Algoritmo | Tipo | Chave | Observações |
| --- | --- | --- | --- |
| DES | Simétrico | 56 bits | Década de 1970; fraco pelos padrões atuais; legado |
| 3DES | Simétrico | 112 ou 168 bits | Aplica o DES três vezes; segurança moderada; lento; legado |
| AES | Simétrico | 128, 192 ou 256 bits | Substituiu o DES como padrão em 2001; forte e rápido; uso atual |
| IDEA | Simétrico | 128 bits | Década de 1990; alternativa ao DES; pouco usado hoje |
| RC4 | Simétrico | 40 a 2048 bits | Usado em redes sem fio e SSL/TLS; segurança moderada; legado |
| Blowfish | Simétrico | 32 a 448 bits | Rápido e considerado forte; classificado como legado |
| RSA | Assimétrico | 2048 a 4096 bits | Criptografia e assinaturas digitais; forte e lento; uso atual |
| Diffie-Hellman | Assimétrico (troca de chaves) | variável | Permite estabelecer chave em canal inseguro |

Leitura rápida: simétricos usam chave privada única; os algoritmos assimétricos usam chave pública. DES é o fraco; AES é o forte e atual; RSA é o assimétrico mais conhecido; Diffie-Hellman serve para **trocar chaves**, não para cifrar mensagens.

### Autenticidade e os três fatores

Autenticidade é a garantia de que a informação, transação ou comunicação vem de quem diz ter originado. Os métodos de autenticação verificam a identidade do usuário e se baseiam em três categorias:

| Fator | Exemplos |
| --- | --- |
| O que você **sabe** | senha, PIN, resposta a pergunta de segurança, código de acesso |
| O que você **tem** | token físico, dispositivo móvel, smartcard, certificado digital, aplicativo autenticador |
| O que você **é** | impressão digital, reconhecimento facial, retina, íris, voz, padrão de digitação |

#### O que você sabe

- É o método mais comum e também o **mais vulnerável**: senhas fracas, repetidas ou vazadas são exploradas por atacantes.
- **Força bruta** testa todas as combinações: uma senha de 5 dígitos numéricos tem só 100.000 combinações; 8 dígitos numéricos, 1 milhão; 8 caracteres variados (números, símbolos, maiúsculas e minúsculas) passam de 600 trilhões. Defesas: bloqueio temporário após várias tentativas e exigência de complexidade.
- Boas práticas: senhas longas (mínimo de 12 a 14 caracteres); misturar maiúsculas, minúsculas, números e símbolos; evitar palavras comuns, sequências óbvias ("123456", "senha", "admin") e dados pessoais; usar frases-senha (*passphrases*); não reutilizar senhas; usar gerenciador de senhas (Bitwarden, 1Password, LastPass); ativar autenticação em dois fatores; trocar senhas antigas em caso de suspeita de vazamento; testar a força da senha.
- **PIN** (*Personal Identification Number*): número pessoal, uma "senha curta" só de números; ideal para teclados numéricos e telas de toque (cartões, caixas eletrônicos, celulares). Combinações óbvias (1234, 0000, aniversários) o fragilizam; PINs mais longos são melhores. Costuma ter limite de tentativas e bloqueio temporário.
- **Perguntas de segurança**: respostas muitas vezes são fáceis de descobrir (redes sociais), genéricas ou sujeitas a variações de digitação; servem apenas como etapa adicional e **nunca como único método**.

#### O que você é (biometria)

- Biometria significa medir características biológicas: "bio" (vida) e "metria" (medida). Exemplos: impressão digital, rosto, voz, retina, íris, veias da mão e DNA.
- É considerada muito segura (características únicas, difíceis de copiar) e prática, e **assegura o princípio da autenticidade**. Pontos de atenção: privacidade e falsificação em sistemas mal projetados.

#### O que você tem

- Mesmo com a senha comprometida, o invasor precisaria do objeto ou dispositivo.
- **Smartcard**: cartão com chip que guarda certificados digitais, chaves criptográficas e dados; precisa de leitor e, em geral, de senha ou PIN (cartão = algo que tem; PIN = algo que sabe). Usado em login, assinatura digital, controle de acesso físico (crachás com chip) e redes corporativas; é muito difícil clonar.
- **Aplicativo autenticador** (Google, Microsoft Authenticator, Authy, LastPass Authenticator): gera códigos temporários **OTP** (*One-Time Password*) no próprio aparelho, sem precisar de internet ou sinal; a configuração se faz lendo um QR Code. Evita interceptação de SMS e clonagem de chip.
- Dois algoritmos geram o OTP: **TOTP** (*Time-Based*), código que muda com o tempo, em geral a cada 30 ou 60 segundos; e **HOTP** (*HMAC-Based*), código que muda com base em um **contador** de uso. Cada código vale uma única vez, o que impede reaproveitamento.
- **Token**: dispositivo físico ou digital que serve de chave temporária. **Token físico (hardware)**: chaveiro ou cartão com visor que gera códigos a cada 30 segundos, ou autentica por USB (YubiKey). **Token digital (software)**: aplicativo autenticador (inclusive o app do banco).
- Código enviado por **SMS ou e-mail** é menos seguro (pode ser interceptado se o celular ou e-mail forem invadidos); os métodos mais seguros são apps autenticadores e dispositivos dedicados.

### Autenticação forte, multifator e dois fatores

- **Autenticação forte**: exige dois ou mais fatores distintos de autenticação, reduzindo o risco mesmo se uma credencial (a senha) for comprometida. Exemplos: senha + código de aplicativo; biometria + smartcard. Protege contra phishing, força bruta, vazamento de senhas e engenharia social. Exigência de padrões como PCI DSS (setor financeiro), LGPD e GDPR.
- O que importa é a **natureza diferente** dos fatores, não só a quantidade: duas senhas são duas chaves parecidas e não dão a mesma segurança que senha + cartão.
- **MFA** (autenticação multifator): dois ou mais fatores. **2FA**: **exatamente dois** fatores distintos.
- Nota técnica: no rigor, a autenticação forte exige fatores de categorias diferentes, enquanto a MFA poderia juntar fatores iguais ou diferentes (toda forte é multifator, mas o inverso não vale). As bancas, porém, costumam tratar os termos como sinônimos.
- Exemplos de 2FA: senha + código enviado ao celular; caixa eletrônico (cartão, algo que se tem, mais senha ou digital).

> ⚠️ Pegadinha: afirmativas dizendo que a MFA usa "apenas senhas complexas", que é só para servidores corporativos ou que o usuário escolhe um fator ou outro estão erradas: a MFA combina dois ou mais fatores e está disponível a usuários comuns.

### Para fixar

- DES (56 bits) é fraco e legado; 3DES, IDEA, RC4 e Blowfish são simétricos legados; AES (128, 192 ou 256 bits) é o padrão atual desde 2001.
- RSA é assimétrico (2048 a 4096 bits); Diffie-Hellman serve para trocar chaves em canal inseguro.
- Três fatores: sabe (senha, PIN, pergunta), tem (token, smartcard, celular, certificado) e é (biometria).
- Senha é o fator mais comum e o mais vulnerável; força bruta é combatida com bloqueio de tentativas, senhas longas e complexas.
- OTP é código de uso único; TOTP varia com o tempo (30 ou 60 s) e HOTP com um contador; SMS e e-mail são menos seguros que aplicativos e tokens.
- Biometria garante autenticidade; perguntas de segurança nunca devem ser o único método.
- Autenticação forte combina fatores de naturezas diferentes; 2FA são exatamente dois fatores; MFA são dois ou mais (as bancas costumam tratar forte e multifator como sinônimos).

