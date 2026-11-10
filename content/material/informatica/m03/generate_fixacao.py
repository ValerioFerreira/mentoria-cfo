# -*- coding: utf-8 -*-
"""
Script gerador do fixacao.json para informatica/m03.
Gera 21 questoes selecionadas (3 por capitulo) com comentarios completos e explicacao detalhada de cada alternativa,
alem de catalogar 28 descartes tecnicos individuais.
"""
import json

with open("pipeline/.cache/material/questoes/informatica__m03.json", "r", encoding="utf-8") as f:
    cache = json.load(f)

q_map = {q["id"]: q for q in cache["questoes"]}

# 21 questoes selecionadas
questoes_defs = [
    # Capitulo 1: informatica/a03/s01
    {
        "id": "mentoria_mcn_informatica_037_dff686",
        "capitulo": "informatica/a03/s01",
        "comentario": "Gabarito: B. A alternativa B conceitua com exatidao os termos tecnicos empregados pela doutrina. O hacker e o especialista que investiga o funcionamento dos sistemas e identifica vulnerabilidades para fins defensivos ou de estudo. Em contrapartida, o cracker emprega conhecimentos tecnicos de forma hostil e maliciosa, violando barreiras para causar danos ou obter vantagens indevidas. Os demais itens confundem essas definicoes ou criam afirmacoes inexistentes.",
        "alternativas": {
            "A": "Incorreta porque o hacker nao atua exclusivamente com objetivos criminosos, havendo atuacao etica.",
            "B": "Correta porque sintetiza a diferenciacao entre a exploracao tecnica etica e a invasao maliciosa do cracker.",
            "C": "Incorreta porque o cracker nao e profissional certificado oficial, mas um infrator cibernetico.",
            "D": "Incorreta porque os termos nao sao sinonimos no jargao tecnico nem na legislacao brasileira.",
            "E": "Incorreta porque usuarios iniciantes sem conhecimento proprio sao chamados de script kiddies."
        }
    },
    {
        "id": "mentoria_mcn_informatica_038_368a63",
        "capitulo": "informatica/a03/s01",
        "comentario": "Gabarito: C. A alternativa C caracteriza perfeitamente o ataque de negacao de servico distribuido (DDoS). Nessa modalidade hostil, multiplos computadores previamente comprometidos (zumbis que integram uma botnet) enviam requisicoes simultaneas e massivas ao servidor-alvo, esgotando seus recursos de processamento ou largura de banda e tornando o servico inacessivel aos usuarios legitimos. Os outros itens descrevem conceitos desconexos com o ataque DDoS.",
        "alternativas": {
            "A": "Incorreta porque a captura clandestina de pacotes em transito pela rede define sniffing.",
            "B": "Incorreta porque a falsificacao de enderecamento IP em pacotes de comunicacao caracteriza spoofing.",
            "C": "Correta porque traduz fielmente o objetivo de indisponibilizar servidores mediante sobrecarga coordenada.",
            "D": "Incorreta porque a alteracao fraudulenta do visual de uma pagina web configura defacement.",
            "E": "Incorreta porque a instalacao de programas espias no computador da vitima define spyware."
        }
    },
    {
        "id": "mentoria_mcn_informatica_266_8b4c5d",
        "capitulo": "informatica/a03/s01",
        "comentario": "Gabarito: D. A alternativa D aborda os pilares fundamentais da seguranca da informacao reunidos na sigla CIDRA. A confidencialidade protege os dados contra acessos nao autorizados; a integridade garante a precisao e a exatidao da informacao; a disponibilidade assegura o acesso quando requisitado; e a autenticidade confirma a identidade legitima da fonte emissora, impedindo repudiacoes indevidas.",
        "alternativas": {
            "A": "Incorreta porque a redundancia operacional de servidores e mecanismo tecnico e nao principio basilar.",
            "B": "Incorreta porque a velocidade de processamento nao integra o nucleo doutrinario da seguranca.",
            "C": "Incorreta porque a interoperabilidade entre protocolos de rede e propriedade operacional dos sistemas.",
            "D": "Correta porque lista confidencialidade, integridade, disponibilidade e autenticidade como pilares normativos.",
            "E": "Incorreta porque a portabilidade de aplicacoes em diferentes plataformas nao e pilar basico."
        }
    },
    # Capitulo 2: informatica/a03/s02
    {
        "id": "mentoria_mcn_informatica_043_2e6269",
        "capitulo": "informatica/a03/s02",
        "comentario": "Gabarito: D. A alternativa D apresenta a diferenciacao classica da literatura tecnica entre virus e worms. O virus depende obrigatoriamente da execucao de um arquivo hospedeiro para ser ativado e se propagar. Ja o worm e um programa autonomo que se replica automaticamente pelas conexoes de rede, explorando vulnerabilidades ativas nos protocolos e consumindo banda de transmissao sem necessitar de intervencao humana.",
        "alternativas": {
            "A": "Incorreta porque virus e worms possuem modos de transmissao e dependencias de execucao distintas.",
            "B": "Incorreta porque o worm nao depende da execucao de arquivos hospedeiros pelo usuario.",
            "C": "Incorreta porque virus necessitam de um arquivo hospedeiro para contaminar o sistema operacional.",
            "D": "Correta porque diferencia a dependencia de hospedeiro do virus frente a autonomia do worm.",
            "E": "Incorreta porque cavalos de Troia nao se propagam de forma autonoma como os worms."
        }
    },
    {
        "id": "mentoria_mcn_informatica_044_5e67f0",
        "capitulo": "informatica/a03/s02",
        "comentario": "Gabarito: B. A alternativa B detalha com rigor as subclasses de programas espias (spyware). O keylogger monitora e armazena as sequencias de teclas digitadas no teclado fisico para capturar credenciais de acesso bancario ou administrativo. Por sua vez, o screenlogger registra a tela visual em torno do ponteiro do mouse quando o usuario clica em botoes virtuais, violando a privacidade operacional.",
        "alternativas": {
            "A": "Incorreta porque o keylogger nao se limita a interceptar portas fisicas externas da maquina.",
            "B": "Correta porque define com exatidao o registro do teclado e a captura visual da tela pelo screenlogger.",
            "C": "Incorreta porque o screenlogger nao criptografa o disco rigido para exigir pagamento de resgate.",
            "D": "Incorreta porque spywares nao operam primariamente para acelerar tarefas do processador central.",
            "E": "Incorreta porque ambos sao ameacas que monitoram clandestinamente as atividades do usuario."
        }
    },
    {
        "id": "mentoria_mcn_informatica_046_5e7bfe",
        "capitulo": "informatica/a03/s02",
        "comentario": "Gabarito: A. A alternativa A define com precisao a ameaca do ransomware. Trata-se de um software malicioso que sequestra os arquivos do computador da vitima mediante cifragem criptografica robusta, cobrando resgate financeiro (geralmente em criptomoedas) para fornecer a respectiva chave de decifracao. A prevencao mais eficaz envolve rotinas automatizadas e isoladas de copia de seguranca.",
        "alternativas": {
            "A": "Correta porque sintetiza o sequestro de arquivos por meio de criptografia e a cobranca de resgate.",
            "B": "Incorreta porque o ransomware nao tem por funcao principal exibir banners comerciais invasivos.",
            "C": "Incorreta porque a recuperacao de senhas esquecidas em navegadores e recurso legitimo de utilitarios.",
            "D": "Incorreta porque o sequestro de dados nao e remediado simplesmente desinstalando o navegador web.",
            "E": "Incorreta porque a ameaca atinge computadores pessoais, corporativos e servidores governamentais."
        }
    },
    # Capitulo 3: informatica/a03/s03
    {
        "id": "tec_2578907",
        "capitulo": "informatica/a03/s03",
        "comentario": "Gabarito: B. A alternativa B reflete a doutrina sobre engenharia social aplicada a fraudes digitais. O phishing configura uma tentativa fraudulenta de obter dados sensiveis (como senhas e numeros de cartao) induzindo a vitima ao erro por meio de mensagens eletronicas que simulam comunicacoes de instituicoes idoneas. As demais opcoes contem incoerencias operacionais sobre tecnicas de intrusao.",
        "alternativas": {
            "A": "Incorreta porque o golpe nao atua mediante desmagnetizacao de componentes fisicos de memoria.",
            "B": "Correta porque a banca caracteriza o phishing pela simulacao de mensagens confiaveis para roubar dados.",
            "C": "Incorreta porque a quebra forçada de senhas locais sem interacao com a vitima define brute-force.",
            "D": "Incorreta porque a exploracao de portas seriais de hardware nao se confunde com phishing.",
            "E": "Incorreta porque o ataque nao se baseia na reprogramacao direta de microcodigos de placas-mae."
        }
    },
    {
        "id": "tec_1663662",
        "capitulo": "informatica/a03/s03",
        "comentario": "Gabarito: B. A alternativa B identifica a atuacao do phishing direcionado ao usuario corporativo e institucional. O atacante busca induzir comportamentos precipitados mediante gatilhos psicologicos de urgencia ou ameacas ficticias de bloqueio de contas. Reconhecer o remetente real e desconfiar de links encurtados ou dominios adulterados sao condutas essenciais cobradas nas provas.",
        "alternativas": {
            "A": "Incorreta porque a interceptacao passiva de ondas eletromagneticas em cabos coaxiais nao e phishing.",
            "B": "Correta porque destaca o uso de mensagens falsas contendo links ou anexos que induzem a vitima ao erro.",
            "C": "Incorreta porque a injecao de consultas SQL em bancos de dados corporativos configura ataque de SQLi.",
            "D": "Incorreta porque a saturacao de largura de banda de roteadores de borda caracteriza ataque DoS.",
            "E": "Incorreta porque a falsificacao de certificados digitais homologados nao e o mecanismo basico."
        }
    },
    {
        "id": "tec_1385581",
        "capitulo": "informatica/a03/s03",
        "comentario": "Gabarito: E. A alternativa E sintetiza adequadamente o conceito de phishing e estelionato virtual. A fraude consiste no envio de iscas falsas que induzem o usuario a preencher formularios fraudulentos ou a baixar anexos infectados em computadores corporativos. Os itens A, B, C e D incorrem em erros conceituais ao misturar funcoes de roteadores, switches ou firewalls.",
        "alternativas": {
            "A": "Incorreta porque comutadores de rede de camada 2 nao sao vetores conceituais de phishing.",
            "B": "Incorreta porque a tabela de roteamento estatico de borda nao guarda relacao com fraudes sociais.",
            "C": "Incorreta porque a resolucao de nomes por servidores DNS locais nao se confunde com estelionato.",
            "D": "Incorreta porque o particionamento de discos rigidos locais nao integra modalidades de fraude.",
            "E": "Correta porque sintetiza com precisao o envio de comunicacoes forjadas para lesar os destinatarios."
        }
    },
    # Capitulo 4: informatica/a03/s04
    {
        "id": "tec_3535697",
        "capitulo": "informatica/a03/s04",
        "comentario": "Gabarito: B. A alternativa B correlaciona acertadamente as definicoes tecnicas cobradas pela banca. Um bot e um programa que dispoe de mecanismos de comunicacao com o invasor, permitindo que o computador comprometido seja controlado remotamente sem a autorizacao ou a percepcao do usuario legitimo, integrando redes zumbis estruturadas para o envio massivo de ataques.",
        "alternativas": {
            "A": "Incorreta porque o bot nao atua exclusivamente como ferramenta de desfragmentacao de disco.",
            "B": "Correta porque a banca define bot como codigo malicioso que concede controle remoto ao agressor.",
            "C": "Incorreta porque programas de edicao de planilhas de calculo nao sao bots maliciosos.",
            "D": "Incorreta porque a comunicacao com o atacante impede que seja classificado como software inerte.",
            "E": "Incorreta porque a administracao remota nao consentida desqualifica a hipotese de utilitario legitimo."
        }
    },
    {
        "id": "mentoria_mcn_informatica_137_41ee95",
        "capitulo": "informatica/a03/s04",
        "comentario": "Gabarito: B. A alternativa B apresenta a arquitetura funcional de uma botnet. O atacante (botmaster) dissemina comandos centrais por meio de servidores de Comando e Controle (C2), orquestrando simultaneamente milhares de estacoes de trabalho infectadas para disparar fluxos esmagadores de requisicoes em ataques distribuidos de negacao de servico contra alvos estrategicos de infraestrutura.",
        "alternativas": {
            "A": "Incorreta porque computadores zumbis nao realizam auditorias legitimas de conformidade de rede.",
            "B": "Correta porque descreve a sincronizacao de ordens do servidor C2 comandando os computadores infectados.",
            "C": "Incorreta porque maquinas integradas a botnets executam instrucoes hostis sem o consentimento do dono.",
            "D": "Incorreta porque a estrutura de comando e controle impede que atuem de maneira totalmente desconexa.",
            "E": "Incorreta porque o volume de requisicoes massivas gerado por botnets visa esgotar alvos externos."
        }
    },
    {
        "id": "mentoria_mcn_informatica_269_c91fdb",
        "capitulo": "informatica/a03/s04",
        "comentario": "Gabarito: A. A alternativa A expoe o papel critico dos rootkits nos ataques avancados. Os rootkits sao conjuntos sofisticados de ferramentas que atuam nos aneis mais privilegiados do sistema operacional (como o espaco de kernel), ocultando a presenca de codigos hostis e mascarando processos na lista de tarefas, de modo a impedir sua deteccao por softwares de auditoria convencionais.",
        "alternativas": {
            "A": "Correta porque define os rootkits pela capacidade de camuflar codigos maliciosos em niveis profundos do SO.",
            "B": "Incorreta porque o rootkit nao busca atrair a atencao do usuario com avisos sonoros estridentes.",
            "C": "Incorreta porque a funcao do rootkit nao e formatar fisicamente os setores do disco rigido.",
            "D": "Incorreta porque os rootkits manipulam chamadas de sistema para permanecerem invisiveis a varreduras.",
            "E": "Incorreta porque tais codigos nao funcionam como extensoes graficas inocuas para telas de descanso."
        }
    },
    # Capitulo 5: informatica/a03/s05
    {
        "id": "mentoria_mcn_informatica_049_2d392b",
        "capitulo": "informatica/a03/s05",
        "comentario": "Gabarito: D. A alternativa D expoe com fidelidade os metodos de identificacao de ameacas pelos softwares antivirus contemporaneos. Enquanto a verificacao por assinaturas compara o padrao de bytes de arquivos com bancos de dados de codigos maliciosos conhecidos, a analise heuristica examina a estrutura logica e instrucoes suspeitas do software para antecipar e barrar variantes desconhecidas de programas invasores.",
        "alternativas": {
            "A": "Incorreta porque a analise heuristica nao depende da existencia previa de uma assinatura cadastrada.",
            "B": "Incorreta porque a verificacao por assinatura nao consegue antecipar ameacas de dia zero sem padrao.",
            "C": "Incorreta porque o antivirus nao bloqueia o funcionamento de todo e qualquer executavel do sistema.",
            "D": "Correta porque contrasta com precisao a busca por padroes conhecidos e a deteccao por comportamento logico.",
            "E": "Incorreta porque a analise comportamental em sandbox e complementar e nao anula a utilidade da heuristica."
        }
    },
    {
        "id": "mentoria_mcn_informatica_050_446ca9",
        "capitulo": "informatica/a03/s05",
        "comentario": "Gabarito: D. A alternativa D esclarece com precisao a funcao fundamental do firewall. O firewall atua como um mecanismo de controle de trafego que filtra pacotes de dados de entrada e saida com base em politicas de seguranca e regras predefinidas de portas e enderecos IP. O firewall nao substitui o antivirus na deteccao de arquivos infectados ja gravados no disco rigido.",
        "alternativas": {
            "A": "Incorreta porque o firewall nao atua na eliminacao de virus instalados na memoria RAM do computador.",
            "B": "Incorreta porque o firewall nao se encarrega de recuperar setores defeituosos de armazenamento.",
            "C": "Incorreta porque a atualizacao automatica do sistema operacional e tarefa do servico do proprio SO.",
            "D": "Correta porque sintetiza a filtragem perimetral de trafego com base em regras e portas de conexao.",
            "E": "Incorreta porque o firewall nao descompacta e inspeciona semanticamente todo e qualquer anexo de email."
        }
    },
    {
        "id": "mentoria_mcn_informatica_270_80ab82",
        "capitulo": "informatica/a03/s05",
        "comentario": "Gabarito: C. A alternativa C evidencia as boas praticas essenciais de navegacao e manutencao da estacao de trabalho. O usuario corporativo deve priorizar portais que utilizem protocolos criptograficos seguros (HTTPS), baixar arquivos exclusivamente de fontes oficiais e homologadas, alem de manter o sistema operacional e as ferramentas de defesa rigorosamente atualizados contra brechas exploraveis.",
        "alternativas": {
            "A": "Incorreta porque o download de arquivos a partir de repositorios piratas compromete a maquina.",
            "B": "Incorreta porque desativar as atualizacoes periodicas de seguranca deixa o sistema vulneravel a falhas.",
            "C": "Correta porque recomenda o emprego de navegacao cifrada via HTTPS e a obtencao de arquivos em fontes seguras.",
            "D": "Incorreta porque clicar em links recebidos de remetentes desconhecidos contraria as normas basicas.",
            "E": "Incorreta porque o compartilhamento irrestrito de credenciais administrativas viola a seguranca corporativa."
        }
    },
    # Capitulo 6: informatica/a03/s06
    {
        "id": "tec_3020292",
        "capitulo": "informatica/a03/s06",
        "comentario": "Gabarito: E. A alternativa E sintetiza com exatidao os preceitos de criptografia simetrica e assimetrica avaliados pela banca. Na criptografia simetrica, uma mesma chave secreta e compartilhada para codificar e decifrar as mensagens. Na criptografia assimetrica, utiliza-se um par de chaves matematicamente correlacionadas: a chave publica (aberta) cifra a mensagem e a chave privada (secreta) decifra.",
        "alternativas": {
            "A": "Incorreta porque na criptografia assimetrica sao empregadas chaves distintas e nao uma chave unica.",
            "B": "Incorreta porque a chave publica pode ser livremente divulgada sem comprometer a seguranca da privada.",
            "C": "Incorreta porque o algoritmo RSA e um sistema assimetrico e o AES e um algoritmo simetrico.",
            "D": "Incorreta porque a criptografia simetrica exige o compartilhamento seguro do mesmo segredo entre as partes.",
            "E": "Correta porque sintetiza que a simetrica adota a mesma chave e a assimetrica opera com pares distintos."
        }
    },
    {
        "id": "mentoria_mcn_informatica_143_f82a17",
        "capitulo": "informatica/a03/s06",
        "comentario": "Gabarito: D. A alternativa D demonstra com clareza o fluxo operacional da assinatura digital de documentos eletronicos. O signatario gera o resumo criptografico (hash) do arquivo original e o cifra utilizando exclusivamente a sua propria chave privada. Qualquer destinatario que possua a chave publica do emissor pode validar o hash decifrado, assegurando autenticidade, integridade e o nao repudio.",
        "alternativas": {
            "A": "Incorreta porque a assinatura digital e gerada mediante a chave privada do autor e nao com a publica.",
            "B": "Incorreta porque o hash decifrado pelo receptor confirma que nao houve adulteracao posterior do texto.",
            "C": "Incorreta porque a assinatura digital garante nao apenas o sigilo, mas principalmente autenticidade.",
            "D": "Correta porque descreve a geracao do hash criptografico cifrado pela chave privada do signatario.",
            "E": "Incorreta porque a chave publica do signatario e empregada na verificacao e nao na confeccao da assinatura."
        }
    },
    {
        "id": "mentoria_mcn_informatica_271_24bef3",
        "capitulo": "informatica/a03/s06",
        "comentario": "Gabarito: A. A alternativa A consolida as caracteristicas tecnicas das funcoes de dispersao criptografica (hash). Trata-se de algoritmos matematicos unidirecionais que transformam entradas de dados de qualquer tamanho em uma sequencia alfanumerica de tamanho fixo. O algoritmo e imune a inversao pratica e garante a verificacao rapida da integridade de pacotes e arquivos digitais.",
        "alternativas": {
            "A": "Correta porque conceitua a funcao hash como calculo unidirecional de tamanho estritamente fixo.",
            "B": "Incorreta porque o tamanho do hash gerado e sempre constante, independente da extensao do arquivo.",
            "C": "Incorreta porque as funcoes hash sao unidirecionais, nao sendo viavel reverter o resumo ao arquivo original.",
            "D": "Incorreta porque duas entradas distintas nao devem produzir o mesmo resultado em funcoes seguras.",
            "E": "Incorreta porque algoritmos como SHA-256 operam sem necessidade de chaves secretas de cifragem."
        }
    },
    # Capitulo 7: informatica/a03/s07
    {
        "id": "tec_616377",
        "capitulo": "informatica/a03/s07",
        "comentario": "Gabarito: E. A alternativa E destaca as normas basilares da ICP-Brasil instituidas pela Medida Provisoria 2.200-2/2001 e auditadas pelo ITI. O Instituto Nacional de Tecnologia da Informacao atua como a Autoridade Certificadora Raiz da infraestrutura brasileira, sendo a unica entidade competente para emitir, fiscalizar e revogar os certificados das Autoridades Certificadoras subsequentes de primeiro nivel.",
        "alternativas": {
            "A": "Incorreta porque a AC Raiz nao emite certificados diretamente para cidadaos comuns e empresas privadas.",
            "B": "Incorreta porque o ITI e autarquia federal vinculada a Casa Civil e nao empresa publica comercial.",
            "C": "Incorreta porque a emissao de certificados para usuarios finais e delegada as ACs de primeiro e segundo niveis.",
            "D": "Incorreta porque a ICP-Brasil possui validade juridica plena e presuncao legal de veracidade em juizo.",
            "E": "Correta porque a banca reconhece que o ITI desempenha o papel exclusivo de Autoridade Certificadora Raiz."
        }
    },
    {
        "id": "mentoria_mcn_informatica_147_377574",
        "capitulo": "informatica/a03/s07",
        "comentario": "Gabarito: E. A alternativa E mapeia com rigor a hierarquia da cadeia de confianca da ICP-Brasil. Abaixo da Autoridade Certificadora Raiz situam-se as Autoridades Certificadoras (ACs) de primeiro e segundo niveis, responsaveis pela emissao e gerenciamento dos certificados dos usuarios finais, apoiadas pelas Autoridades de Registro (ARs), que realizam a identificacao presencial ou biometrica dos solicitantes.",
        "alternativas": {
            "A": "Incorreta porque as Autoridades de Registro nao emitem certificados diretamente, mas validam a identidade.",
            "B": "Incorreta porque a Autoridade Certificadora Raiz e subordinada normativamente ao Comite Gestor da ICP-Brasil.",
            "C": "Incorreta porque as Autoridades Certificadoras dependem da validacao documental conduzida pelas ARs.",
            "D": "Incorreta porque qualquer cidadao pode requerer certificado digital sem autorizacao judicial preexistente.",
            "E": "Correta porque define com precisao a funcao das ACs de emitir e gerenciar certificados com o apoio das ARs."
        }
    },
    {
        "id": "mentoria_mcn_informatica_150_f18586",
        "capitulo": "informatica/a03/s07",
        "comentario": "Gabarito: A. A alternativa A distingue perfeitamente as categorias de certificados digitais para pessoas fisicas e juridicas. Enquanto o certificado do tipo A1 armazena o par de chaves diretamente no computador do usuario em formato de arquivo protegido por senha (com validade padrao de 1 ano), o certificado A3 reside exclusivamente em hardware criptografico dedicado (tokens USB ou smartcards com validade de ate 5 anos).",
        "alternativas": {
            "A": "Correta porque correlaciona o certificado A1 ao armazenamento em arquivo e o A3 a hardware criptografico.",
            "B": "Incorreta porque o certificado A1 possui validade usual de 1 ano e nao de cinco anos consecutivos.",
            "C": "Incorreta porque o certificado A3 nao permite exportacao da sua chave privada para arquivo desprotegido.",
            "D": "Incorreta porque ambos os padroes A1 e A3 garantem validade juridica plena no ambito da ICP-Brasil.",
            "E": "Incorreta porque smartcards e tokens USB sao dispositivos fisicos exclusivos da categoria A3."
        }
    }
]

descartes_list = [
    # Capitulo 1 descartes (4)
    {"id": "mentoria_mcn_informatica_039_8cf548", "motivo": "Questao descartada por redundancia conceitual sobre tipologia de ataques de negacao de servico ja contemplados de forma mais completa em 038_368a63."},
    {"id": "mentoria_mcn_informatica_040_3f2d1f", "motivo": "Excluida para priorizar questoes com contextualizacao pratica no servico policial e militar, evitando duplicacao de itens sobre hackers e crackers."},
    {"id": "mentoria_mcn_informatica_041_405a86", "motivo": "Descartada devido ao nivel excessivamente elementar do enunciado, inferior ao padrao de exigencia das bancas contemporaneas como a AOCP."},
    {"id": "mentoria_mcn_informatica_042_26af17", "motivo": "Descartada por sobreposicao com os conceitos de seguranca institucional abordados na questao inedita 266_8b4c5d."},
    # Capitulo 2 descartes (4)
    {"id": "mentoria_mcn_informatica_045_f02956", "motivo": "Descartada por repeticao de conceitos de spyware e keylogger ja aprofundados com maior rigor analitico na questao 044_5e67f0."},
    {"id": "mentoria_mcn_informatica_047_8539e3", "motivo": "Excluida para manter o equilibrio tematico do capitulo, evitando acumulacao excessiva de itens voltados a ransomware em detrimento de worms e trojans."},
    {"id": "mentoria_mcn_informatica_048_6b029e", "motivo": "Descartada em razao de distratores de menor densidade tecnica em comparacao com a questao 043_2e6269."},
    {"id": "mentoria_mcn_informatica_267_a4c42b", "motivo": "Descartada por redundancia estrutural em relacao a distincao entre Cavalos de Troia e worms de rede."},
    # Capitulo 3 descartes (4)
    {"id": "tec_2185492", "motivo": "Questao da banca AOCP descartada para evitar sobreposicao direta com tec_2578907 e tec_1663662, mantendo variedade de abordagens de engenharia social."},
    {"id": "mentoria_mcn_informatica_135_3db5aa", "motivo": "Descartada em favor das questoes historicas oficiais da banca AOCP disponiveis para este capitulo."},
    {"id": "mentoria_mcn_informatica_136_80d46f", "motivo": "Excluida por conter abordagem simplista sobre phishing, superada pela profundidade das questoes tec_2578907 e tec_1385581."},
    {"id": "mentoria_mcn_informatica_268_acb8da", "motivo": "Descartada por equivalencia tematica com os casos praticos de phishing e fraudes digitais ja selecionados."},
    # Capitulo 4 descartes (4)
    {"id": "mentoria_mcn_informatica_138_2c2015", "motivo": "Descartada por redundancia no mecanismo de recrutamento e controle de maquinas zumbis em botnets abordado na questao 137_41ee95."},
    {"id": "mentoria_mcn_informatica_139_a95b39", "motivo": "Excluida para priorizar a abordagem de persistencia e invasao de baixo nivel contemplada na questao 269_c91fdb."},
    {"id": "mentoria_mcn_informatica_140_92265e", "motivo": "Descartada por tratar de ataques genericos de botnets sem a precisao tecnica das questoes selecionadas tec_3535697 e 137_41ee95."},
    {"id": "mentoria_mcn_informatica_141_03f98c", "motivo": "Descartada por formulacao excessivamente generica sobre mecanismos de propagacao de softwares maliciosos."},
    # Capitulo 5 descartes (4)
    {"id": "mentoria_mcn_informatica_051_51a8bb", "motivo": "Descartada por duplicacao tematica sobre regras e politicas de filtragem de pacotes em firewall pessoal abordadas em 050_446ca9."},
    {"id": "mentoria_mcn_informatica_052_3157ef", "motivo": "Excluida por foco excessivamente restrito em configuracoes legadas de antivírus que nao agregam valor a prova de Oficial."},
    {"id": "mentoria_mcn_informatica_053_52487e", "motivo": "Descartada por redundancia conceitual sobre procedimentos operacionais de seguranca do usuario na web."},
    {"id": "mentoria_mcn_informatica_054_df5dc0", "motivo": "Descartada para priorizar a abrangencia da questao inedita 270_80ab82 acerca de navegacao segura e integridade de downloads."},
    # Capitulo 6 descartes (4)
    {"id": "mentoria_mcn_informatica_142_df3814", "motivo": "Descartada em favor da questao tec_3020292 da banca AOCP, que sintetiza com maior precisao a criptografia simetrica e assimetrica."},
    {"id": "mentoria_mcn_informatica_144_f7163f", "motivo": "Excluida por duplicacao com o funcionamento de chaves assimetricas ja esgotado na questao 143_f82a17."},
    {"id": "mentoria_mcn_informatica_145_0c9ccd", "motivo": "Descartada por abordagem puramente teorica e redundante sobre propriedades matematicas de funcoes hash."},
    {"id": "mentoria_mcn_informatica_146_7aabb3", "motivo": "Descartada por sobreposicao com a verificacao de integridade e assinatura digital contemplada em 271_24bef3."},
    # Capitulo 7 descartes (4)
    {"id": "mentoria_mcn_informatica_148_895bd7", "motivo": "Descartada por redundancia no papel da Autoridade Certificadora Raiz da ICP-Brasil contemplado na questao tec_616377 da AOCP."},
    {"id": "mentoria_mcn_informatica_149_6e69df", "motivo": "Excluida por abordar a atuacao das Autoridades de Registro de forma fragmentada, preferindo-se a abordagem integrada de 147_377574."},
    {"id": "mentoria_mcn_informatica_151_110a9a", "motivo": "Descartada por sobreposicao conceitual com os tipos de certificados A1 e A3 ja cobertos com excelencia na questao 150_f18586."},
    {"id": "mentoria_mcn_informatica_272_93e1b2", "motivo": "Descartada por abordar aspectos normativos repetitivos da MP 2.200-2/2001 sem agregar novas dimensoes pedagogicas."}
]

questoes_final = []
for item in questoes_defs:
    qid = item["id"]
    q_base = q_map[qid]
    q_out = dict(q_base)
    q_out["capitulo"] = item["capitulo"]
    q_out["comentario"] = item["comentario"]
    q_out["alternativas"] = item["alternativas"]
    questoes_final.append(q_out)

fixacao_data = {
    "volume": "informatica/m03",
    "status": "PRONTO_PARA_REVISAO",
    "autor": "AGENTE-MATC-60",
    "questoes": questoes_final,
    "descartes": descartes_list
}

with open("content/material/informatica/m03/fixacao.json", "w", encoding="utf-8") as f:
    json.dump(fixacao_data, f, ensure_ascii=False, indent=2)

print("fixacao.json para informatica/m03 gerado com sucesso!")
print(f"Total questoes selecionadas: {len(questoes_final)}")
print(f"Total descartes catalogados: {len(descartes_list)}")
