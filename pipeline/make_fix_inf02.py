# -*- coding: utf-8 -*-
import json

raw = json.load(open('pipeline/.cache/material/questoes/informatica__m02.json', encoding='utf-8'))
qs_by_id = {q['id']: q for q in raw['questoes']}

selected_ids = [
    'mentoria_mcn_informatica_013_8efa19', 'mentoria_mcn_informatica_014_a0fbde', 'mentoria_mcn_informatica_015_9fdcc5',
    'mentoria_mcn_informatica_019_2145d9', 'mentoria_mcn_informatica_020_3c0863', 'mentoria_mcn_informatica_021_63a2b0',
    'mentoria_mcn_informatica_025_8861a4', 'mentoria_mcn_informatica_026_6f95b5', 'mentoria_mcn_informatica_027_fa1449',
    'tec_508384', 'mentoria_mcn_informatica_125_6f2d10', 'mentoria_mcn_informatica_126_442aae',
    'tec_389246', 'mentoria_mcn_informatica_130_b3a2c5', 'mentoria_mcn_informatica_131_eb8e81',
    'mentoria_mcn_informatica_031_b17519', 'mentoria_mcn_informatica_032_740a3d', 'mentoria_mcn_informatica_033_7619b4'
]

comentarios_data = {
    "mentoria_mcn_informatica_013_8efa19": {
        "comentario": "A segurança da informação visa resguardar os ativos corporativos contra acessos indevidos e destruição física. Os controles físicos abrangem barreiras arquitetônicas concretas como catracas e salas seguras. Já os controles lógicos apoiam-se em ferramentas de software, incluindo firewalls e senhas criptográficas. A correta identificação dessas categorias previne brechas em auditorias.",
        "alts": {
            "A": "Esta proposição define adequadamente os mecanismos físicos de proteção patrimonial corporativa.",
            "B": "Incorreta porque confunde barreiras materiais com procedimentos puramente gerenciais e diretrizes.",
            "C": "Incorreta porque os controles lógicos não se confundem com estruturas de alvenaria predial.",
            "D": "Incorreta pois desconsidera o papel do software na implementação dos controles lógicos.",
            "E": "Incorreta porque ignora a divisão clássica entre camadas de proteção lógica e material."
        }
    },
    "mentoria_mcn_informatica_014_a0fbde": {
        "comentario": "Vulnerabilidades e ameaças representam conceitos basilares na gestão de riscos operacionais. A vulnerabilidade expressa uma fragilidade interna inerente ao sistema computacional ou às rotinas administrativas. A ameaça consiste em um evento externo em potencial capaz de explorar a fraqueza para gerar danos. O impacto mede a gravidade do prejuízo efetivamente concretizado após o incidente.",
        "alts": {
            "A": "Incorreta pois inverte os conceitos fundamentais de ameaça externa e fragilidade intrínseca.",
            "B": "Incorreta porque define erroneamente o risco operacional como se fosse um controle de proteção.",
            "C": "Incorreta pois o impacto financeiro não se confunde com a probabilidade estatística.",
            "D": "Incorreta porque desconsidera a origem externa das ameaças aos ativos organizacionais.",
            "E": "Esta alternativa descreve perfeitamente a fragilidade interna como vulnerabilidade explorável."
        }
    },
    "mentoria_mcn_informatica_015_9fdcc5": {
        "comentario": "O termo ativo abrange qualquer elemento tangível ou intangível detentor de valor para a corporação. Inclui servidores físicos, bancos de dados, relatórios de investigação e a reputação pública do órgão. A taxonomia de riscos exige a identificação prévia dos ativos para mensurar as consequências institucionais decorrentes de sua perda de integridade ou confidencialidade.",
        "alts": {
            "A": "Esta assertiva conceitua com precisão o ativo como patrimônio informativo de valor relevante.",
            "B": "Incorreta porque restringe o ativo apenas aos componentes físicos de hardware de informática.",
            "C": "Incorreta pois exclui indevidamente os bancos de dados digitais do patrimônio organizacional.",
            "D": "Incorreta porque confunde a definição de ativo com as vulnerabilidades técnicas existentes.",
            "E": "Incorreta por classificar o pessoal operacional fora da abrangência dos ativos institucionais."
        }
    },
    "mentoria_mcn_informatica_019_2145d9": {
        "comentario": "A tríade CID reúne os pilares clássicos de confidencialidade, integridade e disponibilidade. A integridade garante a exatidão e completeza das informações, prevenindo modificações não autorizadas. A confidencialidade restringe o acesso somente aos usuários com permissão legal. A disponibilidade assegura o acesso tempestivo sempre que o serviço for demandado pelos operadores legítimos.",
        "alts": {
            "A": "Incorreta porque atribui à integridade a função de garantir o sigilo das mensagens corporativas.",
            "B": "Incorreta pois confunde disponibilidade com o conceito de confiabilidade operacional.",
            "C": "Esta opção conceitua acertadamente a integridade como salvaguarda da fidedignidade original.",
            "D": "Incorreta porque a confidencialidade não tem como objetivo prevenir falhas em discos de armazenamento.",
            "E": "Incorreta por misturar irretratabilidade jurídica com os pilares da tríade clássica CID."
        }
    },
    "mentoria_mcn_informatica_020_3c0863": {
        "comentario": "A quebra de confidencialidade ocorre quando pessoas não autorizadas obtêm visualização ou cópia de arquivos reservados. A integridade do documento pode permanecer rigorosamente intocada mesmo após a violação do sigilo. O ataque de interceptação passiva (como o sniffing de pacotes) viola a confidencialidade sem alterar nenhum bit do tráfego original transmitido pelo emissor.",
        "alts": {
            "A": "Esta alternativa acerta ao demonstrar a independência entre confidencialidade e integridade.",
            "B": "Incorreta pois sustenta falsamente que a quebra do sigilo implica modificação do texto.",
            "C": "Incorreta porque o ataque de interceptação atinge primariamente a confidencialidade da rede.",
            "D": "Incorreta por afirmar que a integridade só existe quando a mensagem é mantida em segredo.",
            "E": "Incorreta pois confunde o ataque de modificação com a escuta passiva não destrutiva."
        }
    },
    "mentoria_mcn_informatica_021_63a2b0": {
        "comentario": "O princípio da irretratabilidade ou não repúdio impede que o autor negue a prática de um ato eletrônico. A doutrina estabelece que a conjugação de autenticidade (identificação inequívoca do autor) e integridade (documento inalterado) viabiliza o não repúdio. As assinaturas digitais amparadas na infraestrutura ICP-Brasil fornecem a sustentação probatória indispensável perante os tribunais judiciais.",
        "alts": {
            "A": "Incorreta porque a autenticidade isolada não impede a contestação se o texto foi adulterado.",
            "B": "Esta opção sintetiza com perfeição a fórmula de autenticidade mais integridade gerando não repúdio.",
            "C": "Incorreta pois a disponibilidade não é requisito indispensável para provar a autoria de documento.",
            "D": "Incorreta porque o não repúdio é de natureza jurídica e transcende a simples criptografia simétrica.",
            "E": "Incorreta por afirmar que senhas simples de teclado garantem irretratabilidade perante o juízo."
        }
    },
    "mentoria_mcn_informatica_025_8861a4": {
        "comentario": "A ciência criptológica subdivide-se nos ramos teóricos da criptografia e da criptoanálise. Enquanto a criptografia desenvolve algoritmos para transformar mensagens legíveis em criptogramas ininteligíveis, a criptoanálise investiga vulnerabilidades e brechas matemáticas para decifrar conteúdos sem autorização prévia. O embate contínuo entre essas duas disciplinas complementares orienta os constantes avanços da engenharia de redes contemporânea.",
        "alts": {
            "A": "Incorreta porque inverte as atribuições teóricas da criptoanálise e da esteganografia.",
            "B": "Esta assertiva define com exatidão a criptografia e a criptoanálise como ramos da criptologia.",
            "C": "Incorreta pois afirma equivocadamente que a criptoanálise é uma modalidade de ataque malicioso ilegal.",
            "D": "Incorreta porque desconsidera o caráter científico e acadêmico dos estudos de decodificação.",
            "E": "Incorreta por limitar a criptologia exclusivamente às cifras simétricas de bloco."
        }
    },
    "mentoria_mcn_informatica_026_6f95b5": {
        "comentario": "A esteganografia tem por finalidade primária ocultar a existência da mensagem em um suporte hospedeiro inofensivo. Por outro lado, a criptografia torna a mensagem pública incompreensível, mas sua transmissão permanece visível aos observadores da rede. O analista pericial utiliza ferramentas estatísticas para detectar anomalias nos bits menos significativos de imagens suspeitas.",
        "alts": {
            "A": "Incorreta porque a criptografia não oculta o canal de tráfego, apenas cifra o conteúdo.",
            "B": "Incorreta pois a esteganografia altera arquivos multimídia sem torná-los ilegíveis aos usuários.",
            "C": "Incorreta porque as técnicas esteganográficas não dependem obrigatoriamente de chaves públicas.",
            "D": "Esta alternativa diferencia corretamente a dissimulação do canal da ininteligibilidade cifrada.",
            "E": "Incorreta por confundir funções de resumo hash com algoritmos de camuflagem de dados."
        }
    },
    "mentoria_mcn_informatica_027_fa1449": {
        "comentario": "O princípio de Kerckhoffs estabelece que a segurança de um sistema criptográfico repousa no sigilo da chave. O algoritmo de cifragem deve ser público, transparente e submetido ao escrutínio científico amplo. A premissa de manter o algoritmo secreto (segurança por obscurantismo) é rechaçada pelos padrões técnicos mundiais, pois oculta vulnerabilidades crassas.",
        "alts": {
            "A": "Incorreta pois contraria Kerckhoffs ao sugerir que algoritmos secretos são mais seguros.",
            "B": "Incorreta porque o tamanho da chave não dispensa o sigilo rigoroso de seu valor numérico.",
            "C": "Incorreta por afirmar que a segurança depende da complexidade do hardware proprietário.",
            "D": "Incorreta porque a criptografia moderna preconiza algoritmos de domínio e auditoria abertos.",
            "E": "Esta assertiva expressa com rigor o postulado de que a segurança repousa no sigilo da chave."
        }
    },
    "tec_508384": {
        "comentario": "A formulação de senhas robustas exige a combinação diversificada de caracteres e o cumprimento de tamanho mínimo. Sequências de teclado e padrões contíguos (como 'qwerty', '123456' ou 'asdfgh') são imediatamente exploradas por ataques de dicionário e de força bruta. O usuário deve priorizar senhas longas, caracteres alfanuméricos randômicos e símbolos especiais para evitar invasões.",
        "alts": {
            "A": "Incorreta porque a inserção de números aleatórios eleva significativamente a força da credencial.",
            "B": "Incorreta pois realizar substituições leet melhora a entropia perante listas de palavras comuns.",
            "C": "Incorreta porque a extensão de caracteres é o fator isolado mais determinante contra ataques.",
            "D": "Gabarito oficial: sequências de teclas no teclado facilitam ataques e jamais devem ser usadas.",
            "E": "Incorreta porque a mescla de maiúsculas, minúsculas e pontuação é expressamente recomendada."
        }
    },
    "mentoria_mcn_informatica_125_6f2d10": {
        "comentario": "O algoritmo AES (Advanced Encryption Standard) é o padrão mundial simétrico adotado em substituição ao antigo DES. Ele opera sobre blocos padronizados de 128 bits e suporta chaves de 128, 192 e 256 bits. O AES apresenta altíssimo desempenho computacional e resistência inquestionável contra ataques analíticos, consolidando-se em comunicações governamentais seguras.",
        "alts": {
            "A": "Incorreta porque o AES é uma cifra simétrica de blocos, e não um protocolo assimétrico de chaves.",
            "B": "Incorreta pois o tamanho de bloco do AES é estritamente fixado em 128 bits para todas as chaves.",
            "C": "Esta opção define corretamente o padrão AES como cifra simétrica de alto desempenho.",
            "D": "Incorreta porque o AES não utiliza chaves assimétricas de fatoração prima como o RSA.",
            "E": "Incorreta por classificar o AES como algoritmo obsoleto em vias de descontinuação."
        }
    },
    "mentoria_mcn_informatica_126_442aae": {
        "comentario": "A autenticação forte apoia-se na exigência simultânea de dois ou mais fatores de naturezas distintas. A doutrina classifica os métodos em: o que você sabe (conhecimento mental), o que você tem (posse material) e o que você é (inerência biométrica). A combinação de senha alfanumérica com leitura biométrica impede invasões decorrentes de vazamento prévio de credenciais.",
        "alts": {
            "A": "Incorreta porque utilizar duas senhas numéricas apenas duplica o mesmo fator de conhecimento.",
            "B": "Incorreta pois uma pergunta secreta continua pertencendo à categoria de conhecimento mental.",
            "C": "Esta proposição exemplifica com precisão a junção de conhecimento e inerência corporal.",
            "D": "Incorreta porque a biometria isolada não constitui autenticação em múltiplos fatores.",
            "E": "Incorreta por afirmar que tokens de hardware eliminam a utilidade do fator senha."
        }
    },
    "tec_389246": {
        "comentario": "No âmbito das redes corporativas e da internet, a identificação do usuário é processada pelo fornecimento de seu nome de login ou credencial. O login declara ao servidor quem pretende acessar o sistema. A autenticação subsequente valida essa declaração mediante conferência de senha ou token. O termo login consolidou-se como sinônimo operacional do ato de entrada.",
        "alts": {
            "A": "Incorreta porque a URL consiste no endereço padronizado de localização de recursos na rede web.",
            "B": "Gabarito oficial: o login representa o termo técnico adotado para identificação do operador.",
            "C": "Incorreta pois FAQ designa uma lista de perguntas frequentes e respostas de suporte técnico.",
            "D": "Incorreta porque pixel representa a menor unidade gráfica de composição de imagens digitais.",
            "E": "Incorreta pois spam refere-se a mensagens em massa indesejadas transmitidas pela rede."
        }
    },
    "mentoria_mcn_informatica_130_b3a2c5": {
        "comentario": "A assinatura digital é produzida pela cifragem do resumo hash da mensagem com a chave privada exclusiva do autor. O destinatário recebe o documento original acompanhado da assinatura e recalcula o hash, decifrando a assinatura com a chave pública do remetente. A perfeita equivalência entre os hashes atesta a autoria incontestável e a integridade integral do arquivo recebido.",
        "alts": {
            "A": "Incorreta pois a assinatura digital não cifra o texto claro com a chave pública do leitor.",
            "B": "Incorreta porque a função hash não executa a cifragem reversível dos dados do arquivo.",
            "C": "Esta assertiva descreve perfeitamente o processo de assinatura mediante cifragem do hash.",
            "D": "Incorreta por sustentar que a assinatura digital assegura sigilo e confidencialidade.",
            "E": "Incorreta porque a validação requer a chave pública do autor, e não sua chave secreta."
        }
    },
    "mentoria_mcn_informatica_131_eb8e81": {
        "comentario": "O algoritmo de hash SHA-256 produz um resumo matemático de tamanho fixo de 256 bits, independentemente da dimensão da entrada. Trata-se de uma função estritamente unidirecional e determinística, dotada de forte efeito avalanche. O SHA-256 é amplamente empregado na integridade de transações eletrônicas, no blockchain e na cadeia de custódia pericial de provas digitais.",
        "alts": {
            "A": "Incorreta porque o tamanho do resumo do SHA-256 não varia conforme a extensão do arquivo.",
            "B": "Incorreta pois o SHA-256 é unidirecional e não permite reconstruir o texto original de entrada.",
            "C": "Esta opção apresenta de forma irretocável as propriedades canônicas do padrão SHA-256.",
            "D": "Incorreta por afirmar que o SHA-256 apresenta vulnerabilidades práticas a colisões de dados.",
            "E": "Incorreta porque o algoritmo MD5 gera resumos de 128 bits e encontra-se descontinuado."
        }
    },
    "mentoria_mcn_informatica_031_b17519": {
        "comentario": "O certificado digital no padrão ITU-T X.509 funciona como uma carteira de identidade eletrônica, atestando publicamente a titularidade de uma chave pública. Ele contém os dados cadastrais do dono, o período de validade, o algoritmo adotado e a assinatura da Autoridade Certificadora. A chave privada do titular nunca é inserida no corpo do certificado.",
        "alts": {
            "A": "Incorreta porque o certificado digital não incorpora a chave privada do proprietário.",
            "B": "Incorreta pois o padrão X.509 não se restringe a criptografia simétrica de chaves secretas.",
            "C": "Esta alternativa define com perfeição a estrutura e os dados do certificado digital X.509.",
            "D": "Incorreta porque a assinatura digital da AC é elemento obrigatório de fé pública do documento.",
            "E": "Incorreta por afirmar que certificados digitais dispensam prazos de validade temporal."
        }
    },
    "mentoria_mcn_informatica_032_740a3d": {
        "comentario": "A ICP-Brasil foi estabelecida pela MP 2.200-2/2001 sob arquitetura hierárquica estrita. O vértice superior da cadeia é a Autoridade Certificadora Raiz (AC-Raiz), operada institucionalmente pelo Instituto Nacional de Tecnologia da Informação (ITI). A AC-Raiz não emite certificados para cidadãos comuns, emitindo apenas para as Autoridades Certificadoras subordinadas credenciadas.",
        "alts": {
            "A": "Incorreta porque o ITI opera exclusivamente a AC-Raiz no topo hierárquico da estrutura.",
            "B": "Incorreta pois a AC-Raiz não fornece atendimento presencial nem emite certificados a civis.",
            "C": "Incorreta porque a Autoridade de Registro não possui autoridade para emitir ACs de nível um.",
            "D": "Incorreta por afirmar que a cadeia de certificação brasileira adota uma malha descentralizada.",
            "E": "Esta opção caracteriza com fidelidade a competência e o papel institucional do ITI na AC-Raiz."
        }
    },
    "mentoria_mcn_informatica_033_7619b4": {
        "comentario": "Os certificados do tipo A1 e do tipo A3 diferenciam-se essencialmente pelo meio de armazenamento da chave privada e pelo prazo de validade. O certificado A1 guarda a chave em arquivo de software no computador, com validade de 1 ano. O certificado A3 armazena a chave em hardware seguro (token USB ou smartcard), com validade de até 5 anos.",
        "alts": {
            "A": "Incorreta porque o certificado A1 possui validade máxima de 1 ano e reside em software.",
            "B": "Incorreta pois o token criptográfico de hardware é característica típica do certificado A3.",
            "C": "Esta assertiva resume adequadamente as diferenças técnicas e temporais entre A1 e A3.",
            "D": "Incorreta porque a chave privada do tipo A3 é inexportável do chip criptográfico dedicado.",
            "E": "Incorreta por inverter os prazos regulamentares entre as duas modalidades de certificado."
        }
    }
}

descartes_motivos = {
    # s01
    "mentoria_mcn_informatica_016_6a986f": "Descarte por redundância didática: a questão aborda controles lógicos e administrativos já suficientemente cobertos com excelência pela questão 013.",
    "mentoria_mcn_informatica_017_9bee80": "Descarte por saturação temática: foca em taxonomia básica de riscos, cujo conteúdo teórico já foi contemplado na questão 014.",
    "mentoria_mcn_informatica_018_a40fb4": "Descarte por duplicidade de conceitos: explora definições de vulnerabilidades e ameaças em formato muito similar ao item 014.",
    "mentoria_mcn_informatica_260_9d6d58": "Descarte por excedente de cota: o capítulo s01 já conta com 3 questões selecionadas com equilíbrio doutrinário entre controles e riscos.",
    # s02
    "mentoria_mcn_informatica_022_8f203c": "Descarte por sobreposição de conteúdo: aborda a tríade CID com foco em disponibilidade, tema já explorado e fixado no item 019.",
    "mentoria_mcn_informatica_023_deda8b": "Descarte por redundância: trata da independência entre confidencialidade e integridade, aspecto coberto com mais rigor pelo item 020.",
    "mentoria_mcn_informatica_024_b27c3a": "Descarte por saturação: examina o não repúdio e autenticidade sob formulação quase idêntica à questão 021.",
    "mentoria_mcn_informatica_261_03f576": "Descarte por limite quantitativo: excedente da cota de 3 questões por capítulo do volume regular.",
    # s03
    "mentoria_mcn_informatica_028_d14cae": "Descarte por redundância conceitual: aborda esteganografia e criptografia, tema já plenamente coberto pela questão 026.",
    "mentoria_mcn_informatica_029_c4fc24": "Descarte por sobreposição de tópicos: explora a distinção entre cifras de substituição e transposição, coberta na teoria.",
    "mentoria_mcn_informatica_030_46638b": "Descarte por foco repetitivo: trata do princípio de Kerckhoffs, já fixado de maneira abrangente no item 027.",
    "mentoria_mcn_informatica_262_849fe9": "Descarte por cota: questão complementar descartada para manter exatamente 3 itens selecionados no capítulo 3.",
    # s04
    "mentoria_mcn_informatica_127_7b3490": "Descarte por redundância temática: examina ataques de força bruta a senhas, assunto já avaliado pela questão oficial AOCP tec_508384.",
    "mentoria_mcn_informatica_128_9e6d66": "Descarte por duplicidade: foca em fatores de autenticação de posse, cuja base conceitual foi contemplada no item 126.",
    "mentoria_mcn_informatica_129_bf8339": "Descarte por sobreposição: aborda tokens e OTP em nível excessivamente específico para a prova geral.",
    "mentoria_mcn_informatica_263_12ee52": "Descarte por limite de cota: excedente do capítulo 4, priorizando a questão histórica da AOCP e itens nucleares.",
    # s05
    "mentoria_mcn_informatica_132_e315aa": "Descarte por redundância: examina propriedades do hash SHA-256 sob a mesma perspectiva do item 131.",
    "mentoria_mcn_informatica_133_021ed4": "Descarte por sobreposição: trata de integridade na perícia digital, tema suficientemente consolidado no texto principal.",
    "mentoria_mcn_informatica_134_e3f43a": "Descarte por repetição doutrinária: aborda a tríade de controle de acesso, já examinada pela questão tec_389246.",
    "mentoria_mcn_informatica_264_aa19bd": "Descarte por cota: item excedente do segmento s05, garantindo a representatividade da questão AOCP.",
    # s06
    "mentoria_mcn_informatica_034_d75535": "Descarte por redundância: explora o papel das Autoridades Certificadoras na ICP-Brasil, tema já abordado no item 032.",
    "mentoria_mcn_informatica_035_a80d82": "Descarte por sobreposição técnica: trata das listas de certificados revogados (LCR) e protocolo OCSP de forma pontual.",
    "mentoria_mcn_informatica_036_7cce7c": "Descarte por duplicidade: foca nas diferenças entre certificados A1 e A3, tema examinado com profundidade no item 033.",
    "mentoria_mcn_informatica_265_552fdf": "Descarte por limite de cota: questão complementar descartada para preservar o total de 18 questões do volume."
}

# Montar a lista final de questões
final_questoes = []
for qid in selected_ids:
    q_banco = qs_by_id[qid]
    c_info = comentarios_data[qid]
    
    final_questoes.append({
        "id": qid,
        "capitulo": q_banco["capitulo"],
        "gabarito": q_banco["gabarito"],
        "comentario": c_info["comentario"],
        "alternativas": c_info["alts"]
    })

final_descartes = [{"id": qid, "motivo": motivo} for qid, motivo in descartes_motivos.items()]

fixacao = {
    "volume": "informatica/m02",
    "status": "PRONTO_PARA_REVISAO",
    "total": len(final_questoes),
    "questoes": final_questoes,
    "descartes": final_descartes
}

with open("content/material/informatica/m02/fixacao.json", "w", encoding="utf-8") as f:
    json.dump(fixacao, f, ensure_ascii=False, indent=2)

print("fixacao.json criado com sucesso!")
print(f"Total questoes: {len(final_questoes)}, Total descartes: {len(final_descartes)}")
