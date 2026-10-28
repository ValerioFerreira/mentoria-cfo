##### informatica/a02/s06
A infraestrutura de confiança digital na Internet alicerça-se nos Certificados Digitais, documentos eletrônicos autenticados que vinculam indissoluvelmente uma entidade à sua respectiva chave pública, estruturados sob a hierarquia regulatória da ICP-Brasil.

### Conceito e Estrutura do Certificado Digital

Um Certificado Digital atua como uma carteira de identidade virtual expedida por uma entidade terceira de confiança, atestando publicamente que determinada chave pública pertence a um indivíduo, corporação ou servidor web específico:

- **Conteúdo Estrutural Padronizado (Padrão ITU-T X.509)**:
  - Dados do titular (nome civil, razão social, CPF, CNPJ, e-mail).
  - Chave pública do titular do certificado.
  - Período de vigência temporal (data de emissão e data de expiração).
  - Identificação e assinatura digital da Autoridade Certificadora (AC) emissora.
  - Número de série único e versão do padrão criptográfico.
- **Lista de Certificados Revogados (LCR) e Validação OCSP**:
  - Quando um certificado perde sua confiabilidade antes do prazo regulamentar (por suspeita de comprometimento da chave privada, alteração cadastral ou demissão de operador), a AC emissora inclui o número de série em um documento público assinado periodicamente denominado **Lista de Certificados Revogados (LCR)**.
  - Consultas em tempo real sobre a validade do certificado podem ser realizadas através do protocolo OCSP (*Online Certificate Status Protocol*), sem necessidade de download integral da LCR.

### Infraestrutura de Chaves Públicas Brasileira (ICP-Brasil)

Criada pela Medida Provisória nº 2.200-2/2001, a ICP-Brasil organiza-se sob uma cadeia hierárquica estrita de confiança baseada em três entidades centrais:

1. **Autoridade Certificadora Raiz (AC-Raiz)**:
   - Primeira autoridade no vértice superior da cadeia hierárquica nacional, operada institucionalmente pelo **Instituto Nacional de Tecnologia da Informação (ITI)**.
   - Compete à AC-Raiz executar as diretrizes do Comitê Gestor da ICP-Brasil, fiscalizar as entidades credenciadas e emitir, distribuir, revogar e gerenciar exclusivamente os certificados digitais das Autoridades Certificadoras subsequentes (ela não emite certificados diretamente para usuários finais comuns). Possui certificado autoassinado.
2. **Autoridade Certificadora (AC)**:
   - Entidade pública ou privada credenciada subordinada à AC-Raiz responsável por emitir, distribuir, renovar e revogar os certificados digitais de pessoas físicas, jurídicas e equipamentos finais.
   - Mantém as listas de certificados revogados (LCR) e assegura que a chave pública pertence legítima e comprovadamente ao titular registrado.
3. **Autoridade de Registro (AR)**:
   - Atua como o braço operacional de interface física ou presencial entre o cidadão/empresa e a Autoridade Certificadora.
   - É encarregada do recebimento documental, verificação biométrica e validação presencial ou remota assistida dos solicitantes, encaminhando os pedidos de emissão ou revogação à AC vinculada. A AR não assina nem gera certificados por conta própria.

### Categorias e Tipos de Certificados: A1 versus A3

No ecossistema da ICP-Brasil, os certificados dividem-se em séries funcionais: categoria A (assinatura e autenticação), categoria S (sigilo e criptografia) e categoria T (carimbo do tempo):

- **Certificado Tipo A1**:
  - A chave privada é gerada e armazenada diretamente em formato de software (arquivo de extensão `.pfx` ou `.p12`) no disco rígido do computador ou navegador da vítima.
  - Possui prazo de validade estrito de até **1 ano**.
  - Permite fácil portabilidade e instalação em múltiplas máquinas por cópia do arquivo protegido por senha simples, porém apresenta menor robustez contra cópias indevidas de arquivos.
- **Certificado Tipo A3**:
  - A chave privada é gerada e retida inviolavelmente em dispositivo físico criptográfico dedicado de hardware (*smart card* com leitora ou *token* criptográfico USB) ou em módulo de segurança em nuvem (HSM).
  - Possui validade de **1 a 5 anos** (comumente 3 anos).
  - O hardware criptográfico impede a extração ou cópia da chave privada para o disco do computador; o processamento da assinatura digital ocorre internamente no chip do token, bloqueando o acesso após tentativas consecutivas errôneas de digitação da senha PIN/PUK.

### Para fixar

- Certificado digital (padrão X.509): atesta a posse da chave pública, com assinatura da AC.
- Revogação antes do prazo: Lista de Certificados Revogados (LCR) ou consulta OCSP.
- ICP-Brasil: o ITI opera a AC-Raiz, no topo da hierarquia.
- As ACs emitem certificados aos usuários; as ARs fazem a identificação presencial.
- A1: gerado em software (arquivo .pfx), validade de 1 ano.
- A3: guardado em hardware inexportável (token USB ou cartão inteligente), validade de até 3 ou 5 anos.

