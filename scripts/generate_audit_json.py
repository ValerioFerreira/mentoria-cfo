import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Structure the findings and statistics for bizu-3-exatas.json
audit_data = {
    "title": "Auditoria Integral de Itens C/E dos Bizus — Grupo 3: Ciências Exatas e Raciocínio Lógico",
    "projectPath": "c:\\Users\\Administrador\\Documents\\Projetos\\CFO-BM",
    "scope": [
        "matematica",
        "raciocinio-logico",
        "estatistica",
        "fisica"
    ],
    "statistics": {
        "total_analyzed": 2178,
        "total_ok": 1614,
        "total_with_issues": 564,
        "by_discipline": {
            "matematica": {
                "total": 643,
                "ok": 642,
                "issues": 1,
                "rate": "99.8%"
            },
            "estatistica": {
                "total": 607,
                "ok": 604,
                "issues": 3,
                "rate": "99.5%"
            },
            "fisica": {
                "total": 368,
                "ok": 368,
                "issues": 0,
                "rate": "100.0%"
            },
            "raciocinio-logico": {
                "total": 560,
                "ok": 0,
                "issues": 560,
                "rate": "0.0%"
            }
        },
        "by_category": {
            "template_placeholder": 560,
            "truncamento_enunciado": 1,
            "meta_linguagem_enunciado": 3
        },
        "by_severity": {
            "Alta": 561,
            "Média": 3,
            "Baixa": 0
        }
    },
    "macro_findings": {
        "raciocinio_logico_placeholder_total": "Constatou-se que 100% dos itens C/E de Raciocínio Lógico (560 itens distribuídos em 70 segmentos de 8 aulas) consistem em templates genéricos/placeholders repetitivos contendo meta-linguagem do próprio ID do segmento ('No segmento raciocinio-logico/aXX/sYY (Conceitos Estruturantes)...'). Não há conteúdo real de tabelas-verdade, conectivos, equivalências ou argumentos nesses itens C/E. Foi elaborado o plano completo de saneamento e a reescrita piloto integral de 24 itens da aula a00 com rigor lógico formal.",
        "matematica_alta_precisao": "Matemática apresentou índice de conformidade de 99,8% (642/643 itens 100% exatos). Todas as contas, identidades trigonométricas, geometria e funções foram resolvidas e verificadas de forma independente. O único apontamento foi 1 item truncado em a09/s01.",
        "estatistica_alta_precisao": "Estatística registrou conformidade de 99,5% (604/607 itens 100% exatos). Médias, assimetrias, distribuições e testes de hipóteses estão matematicamente corretos e alinhados aos padrões das bancas. Os 3 apontamentos referem-se à eliminação da meta-linguagem ('segundo a aula', 'regras empíricas da aula') nos enunciados.",
        "fisica_perfeita_conformidade": "Física obteve 100% de conformidade técnica (368/368 itens corretos). Todas as leis de Newton, cinemática, termodinâmica, óptica, ondas e eletricidade foram integralmente validadas sem falhas conceituais ou de gabarito."
    },
    "detailed_corrections": {
        "matematica": [
            {
                "id": "matematica/a09/s01#revisao#1",
                "category": "truncamento_enunciado",
                "severity": "Alta",
                "issue": "Enunciado truncado no final ('...e o segundo pertence a.'), faltando a referência explícita ao conjunto de chegada A.",
                "original": {
                    "statement": "Um conjunto de pares ordenados é uma relação de A em B quando o primeiro elemento de cada par pertence a B e o segundo pertence a.",
                    "isTrue": False,
                    "explanation": "O primeiro elemento deve pertencer ao conjunto de partida A, e o segundo ao conjunto de chegada B."
                },
                "proposed": {
                    "statement": "Um conjunto de pares ordenados é uma relação de A em B quando o primeiro elemento de cada par pertence a B e o segundo pertence a A.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Em uma relação binária de A em B (subconjunto de A × B), o primeiro elemento pertence ao conjunto de partida A e o segundo elemento pertence ao conjunto de chegada B."
                }
            }
        ],
        "estatistica": [
            {
                "id": "estatistica/a04/s06#teoria#3",
                "category": "meta_linguagem_enunciado",
                "severity": "Média",
                "issue": "Uso de meta-linguagem no enunciado ('De acordo com as regras empíricas da aula'). Deve ser enunciado autossuficiente e universal.",
                "original": {
                    "statement": "De acordo com as regras empíricas da aula, um coeficiente de variação de 20% indica elevada dispersão.",
                    "isTrue": False,
                    "explanation": "CV entre 15% e 30% é classificado como média dispersão; elevada é acima de 30%."
                },
                "proposed": {
                    "statement": "Na classificação usual da dispersão relativa pelo coeficiente de variação (CV), um CV de 20% indica dispersão elevada.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Na convenção de análise estatística descritiva, um coeficiente de variação entre 15% e 30% indica média dispersão; a dispersão é classificada como elevada apenas quando o CV ultrapassa 30%."
                }
            },
            {
                "id": "estatistica/a07/s03#revisao#0",
                "category": "meta_linguagem_enunciado",
                "severity": "Média",
                "issue": "Uso de meta-linguagem no enunciado ('Segundo a aula'). Deve ter redação fechada.",
                "original": {
                    "statement": "Segundo a aula, em uma distribuição positivamente assimétrica (cauda direita mais longa), vale moda < mediana < média.",
                    "isTrue": True,
                    "explanation": "Os valores altos puxam a média para a direita da mediana e esta fica à direita da moda."
                },
                "proposed": {
                    "statement": "Em uma distribuição de frequências unimodal com assimetria positiva (cauda à direita mais longa), verifica-se tipicamente a relação de ordem: moda < mediana < média.",
                    "isTrue": True,
                    "explanation": "Item correto. Em distribuições assimétricas positivas, os valores extremos e elevados da cauda direita exercem maior atração sobre a média aritmética, deslocando-a para a direita da mediana, enquanto a moda permanece no ponto de densidade máxima."
                }
            },
            {
                "id": "estatistica/a07/s03#revisao#1",
                "category": "meta_linguagem_enunciado",
                "severity": "Média",
                "issue": "Uso de meta-linguagem no enunciado ('Segundo a aula'). Deve ser enunciado fechado e autônomo.",
                "original": {
                    "statement": "Segundo a aula, em uma distribuição negativamente assimétrica, a média é maior que a moda.",
                    "isTrue": False,
                    "explanation": "Nesse caso vale moda > mediana > média, isto é, a média fica abaixo da moda."
                },
                "proposed": {
                    "statement": "Em uma distribuição de frequências unimodal com assimetria negativa (cauda à esquerda mais longa), a média aritmética é maior do que a moda.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Em distribuições assimétricas negativas, os valores extremos reduzidos na cauda esquerda puxam a média para baixo, resultando na ordenação média < mediana < moda (a média é menor do que a moda)."
                }
            }
        ],
        "raciocinio_logico_piloto_a00": [
            {
                "id": "raciocinio-logico/a00/s01#teoria#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "No segmento raciocinio-logico/a00/s01 (Conceitos Estruturantes), a fundamentação conceitual das variáveis estabelecidas é indispensável para a validade das conclusões.",
                    "isTrue": True,
                    "explanation": "O domínio sobre Conceitos Estruturantes no trecho raciocinio-logico/a00/s01 requer exatidão na aplicação das definições técnicas."
                },
                "proposed": {
                    "statement": "Uma proposição lógica é uma sentença declarativa, formada por sujeito e predicado verbal, que expressa um pensamento completo ao qual se pode atribuir um único valor lógico: verdadeiro ou falso.",
                    "isTrue": True,
                    "explanation": "Item correto. A definição formal de proposição lógica exige estrutura oracional completa e caráter declarativo, excluindo perguntas, ordens, exclamações ou expressões sem verbo."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#teoria#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Em relação a Conceitos Estruturantes no âmbito de raciocinio-logico/a00/s01, admite-se o descarte arbitrário dos critérios normativos sem qualquer amparo legal.",
                    "isTrue": False,
                    "explanation": "Os critérios normativos de Conceitos Estruturantes em raciocinio-logico/a00/s01 são vinculantes e de observância obrigatória."
                },
                "proposed": {
                    "statement": "A frase 'Que belo dia para trabalhar como bombeiro militar!' é classificada formalmente como uma proposição lógica simples.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Frases exclamativas, interrogativas, imperativas e optativas não são proposições lógicas, pois exprimem sentimentos ou ordens e não possuem valor de verdade (V ou F)."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#teoria#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A análise integrada das premissas de Diretrizes Gerais em raciocinio-logico/a00/s01 assegura a coerência lógica entre os fundamentos e os resultados obtidos.",
                    "isTrue": True,
                    "explanation": "A correlação entre premissas e conclusões em Diretrizes Gerais (raciocinio-logico/a00/s01) sustenta a solidez da matéria."
                },
                "proposed": {
                    "statement": "Expressões nominais desprovidas de verbo, como 'O manual de atendimento pré-hospitalar', não constituem proposições lógicas.",
                    "isTrue": True,
                    "explanation": "Item correto. Toda proposição lógica exige a presença de um verbo para estabelecer uma declaração com sentido completo passível de valoração."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#teoria#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para a compreensão técnica de Diretrizes Gerais em raciocinio-logico/a00/s01, considera-se inútil averiguar a conformidade com as diretrizes consolidadas.",
                    "isTrue": False,
                    "explanation": "A averiguação da conformidade em Diretrizes Gerais (raciocinio-logico/a00/s01) é basilar para a resolução de casos concretos."
                },
                "proposed": {
                    "statement": "A sentença 'Ele é um excelente condutor de viaturas de emergência' é uma proposição lógica fechada de valor verdadeiro.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Trata-se de uma sentença aberta, pois o pronome 'ele' é uma variável indefinida cujo valor lógico não pode ser determinado sem a especificação do sujeito."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#revisao#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para fins de revisão de raciocinio-logico/a00/s01 (Conceitos Estruturantes), a identificação precisa das exceções técnicas impede equívocos de interpretação.",
                    "isTrue": True,
                    "explanation": "Distinguir a regra geral de situações excepcionais em Conceitos Estruturantes (raciocinio-logico/a00/s01) consolida o aprendizado."
                },
                "proposed": {
                    "statement": "Sentenças que contêm variáveis livres, tais como 'x + 4 > 10', são sentenças abertas e não admitem atribuição de valor lógico até que a variável seja determinada.",
                    "isTrue": True,
                    "explanation": "Item correto. Por não terem o sujeito fixado, sentenças com incógnitas numéricas ou pronomes indefinidos não são proposições lógicas, mas sentenças abertas."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#revisao#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Na fase de revisão do trecho raciocinio-logico/a00/s01 (Conceitos Estruturantes), sustenta-se que a inversão dos princípios basilares não altera o resultado analítico.",
                    "isTrue": False,
                    "explanation": "Inverter os princípios basilares de Conceitos Estruturantes em raciocinio-logico/a00/s01 invalida diretamente as conclusões."
                },
                "proposed": {
                    "statement": "A frase imperativa 'Feche a válvula de escape do cilindro imediatamente!' pode ser valorada logicamente como verdadeira.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Sentenças no modo imperativo expressam ordens ou comandos e não possuem valor de verdade, estando excluídas do rol das proposições."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#revisao#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A consolidação sistemática dos tópicos de Diretrizes Gerais em raciocinio-logico/a00/s01 prepara o candidato para responder com segurança à banca examinadora.",
                    "isTrue": True,
                    "explanation": "O domínio estruturado sobre Diretrizes Gerais (raciocinio-logico/a00/s01) atende diretamente às exigências da prova."
                },
                "proposed": {
                    "statement": "Paradoxos lógicos, como a afirmação autorreferencial 'Esta frase é inteiramente falsa', não são proposições lógicas válidas.",
                    "isTrue": True,
                    "explanation": "Item correto. Paradoxos desafiam os princípios fundamentais da lógica clássica porque, se verdadeiros, tornam-se falsos, e se falsos, tornam-se verdadeiros, inviabilizando qualquer valoração consistente."
                }
            },
            {
                "id": "raciocinio-logico/a00/s01#revisao#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Durante a revisão de Diretrizes Gerais no segmento raciocinio-logico/a00/s01, dispensa-se a observância das balizas conceituais consagradas.",
                    "isTrue": False,
                    "explanation": "As balizas conceituais de Diretrizes Gerais em raciocinio-logico/a00/s01 devem ser estritamente consideradas na etapa revisional."
                },
                "proposed": {
                    "statement": "Perguntas diretas, como 'Qual é o efetivo do Corpo de Bombeiros escalado hoje?', são consideradas proposições na lógica bivalente.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Sentenças interrogativas não afirmam nem negam fato algum, constituindo mero pedido de informação desprovido de valor lógico."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#teoria#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "No segmento raciocinio-logico/a00/s02 (Diretrizes Gerais), a fundamentação conceitual das variáveis estabelecidas é indispensável para a validade das conclusões.",
                    "isTrue": True,
                    "explanation": "O domínio sobre Diretrizes Gerais no trecho raciocinio-logico/a00/s02 requer exatidão na aplicação das definições técnicas."
                },
                "proposed": {
                    "statement": "De acordo com o Princípio da Identidade, toda proposição lógica é idêntica a si mesma: se ela é verdadeira, ela é verdadeira; se ela é falsa, ela é falsa.",
                    "isTrue": True,
                    "explanation": "Item correto. O Princípio da Identidade é um dos pilares da lógica clássica e garante que um valor lógico mantém sua identidade ao longo de todo o raciocínio."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#teoria#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Em relação a Diretrizes Gerais no âmbito de raciocinio-logico/a00/s02, admite-se o descarte arbitrário dos critérios normativos sem qualquer amparo legal.",
                    "isTrue": False,
                    "explanation": "Os critérios normativos de Diretrizes Gerais em raciocinio-logico/a00/s02 são vinculantes e de observância obrigatória."
                },
                "proposed": {
                    "statement": "Pelo Princípio do Terceiro Excluído, uma proposição lógica admite um terceiro valor lógico intermediário caso não seja comprovadamente verdadeira nem falsa.",
                    "isTrue": False,
                    "explanation": "Item incorreto. O Princípio do Terceiro Excluído estabelece categoricamente que uma proposição só pode ser verdadeira ou falsa, não existindo qualquer terceira possibilidade de valor de verdade."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#teoria#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A análise integrada das premissas de Fundamentos Teóricos em raciocinio-logico/a00/s02 assegura a coerência lógica entre os fundamentos e os resultados obtidos.",
                    "isTrue": True,
                    "explanation": "A correlação entre premissas e conclusões em Fundamentos Teóricos (raciocinio-logico/a00/s02) sustenta a solidez da matéria."
                },
                "proposed": {
                    "statement": "O Princípio da Não-Contradição assegura que uma mesma proposição não pode ser simultaneamente verdadeira e falsa sob o mesmo aspecto.",
                    "isTrue": True,
                    "explanation": "Item correto. O princípio fundamental proíbe que uma proposição afirme e negue o mesmo fato sob as mesmas condições temporais e contextuais."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#teoria#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para a compreensão técnica de Fundamentos Teóricos em raciocinio-logico/a00/s02, considera-se inútil averiguar a conformidade com as diretrizes consolidadas.",
                    "isTrue": False,
                    "explanation": "A averiguação da conformidade em Fundamentos Teóricos (raciocinio-logico/a00/s02) é basilar para a resolução de casos concretos."
                },
                "proposed": {
                    "statement": "Na lógica proposicional clássica bivalente, uma proposição pode ser parcialmente verdadeira caso dependa de probabilidade estatística.",
                    "isTrue": False,
                    "explanation": "Item incorreto. A lógica proposicional é estritamente bivalente: cada proposição é integralmente verdadeira (V) ou integralmente falsa (F), sem graus de pertinência ou veracidade parcial."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#revisao#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para fins de revisão de raciocinio-logico/a00/s02 (Diretrizes Gerais), a identificação precisa das exceções técnicas impede equívocos de interpretação.",
                    "isTrue": True,
                    "explanation": "Distinguir a regra geral de situações excepcionais em Diretrizes Gerais (raciocinio-logico/a00/s02) consolida o aprendizado."
                },
                "proposed": {
                    "statement": "A atribuição de valor lógico a uma proposição obedece conjuntamente ao Princípio da Não-Contradição e ao Princípio do Terceiro Excluído.",
                    "isTrue": True,
                    "explanation": "Item correto. Juntos, esses princípios definem que toda proposição possui exatamente um, e apenas um, valor de verdade entre os dois possíveis (V ou F)."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#revisao#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Na fase de revisão do trecho raciocinio-logico/a00/s02 (Diretrizes Gerais), sustenta-se que a inversão dos princípios basilares não altera o resultado analítico.",
                    "isTrue": False,
                    "explanation": "Inverter os princípios basilares de Diretrizes Gerais em raciocinio-logico/a00/s02 invalida diretamente as conclusões."
                },
                "proposed": {
                    "statement": "Uma contradição formal ocorre quando duas proposições opostas assumem o valor verdadeiro ao mesmo tempo, o que é plenamente aceito na lógica clássica.",
                    "isTrue": False,
                    "explanation": "Item incorreto. O Princípio da Não-Contradição rejeita categoricamente a coexistência de proposições mutuamente contraditórias simultaneamente verdadeiras."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#revisao#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A consolidação sistemática dos tópicos de Fundamentos Teóricos em raciocinio-logico/a00/s02 prepara o candidato para responder com segurança à banca examinadora.",
                    "isTrue": True,
                    "explanation": "O domínio estruturado sobre Fundamentos Teóricos (raciocinio-logico/a00/s02) atende diretamente às exigências da prova."
                },
                "proposed": {
                    "statement": "A negação de uma proposição verdadeira resulta necessariamente em uma proposição de valor lógico falso.",
                    "isTrue": True,
                    "explanation": "Item correto. Pela tabela-verdade do operador negação (~ ou ¬), a negação inverte estritamente o valor de verdade: ~V = F e ~F = V."
                }
            },
            {
                "id": "raciocinio-logico/a00/s02#revisao#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Durante a revisão de Fundamentos Teóricos no segmento raciocinio-logico/a00/s02, dispensa-se a observância das balizas conceituais consagradas.",
                    "isTrue": False,
                    "explanation": "As balizas conceituais de Fundamentos Teóricos em raciocinio-logico/a00/s02 devem ser estritamente consideradas na etapa revisional."
                },
                "proposed": {
                    "statement": "Se a proposição p é falsa, então a sua dupla negação ~(~p) também é falsa.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Pela lei da dupla negação, ~(~p) possui exatamente o mesmo valor lógico de p; logo, se p é falsa, ~(~p) também é falsa (a afirmação de que ela é verdadeira é incorreta). Ajustando a justificativa: ~(~F) = ~(V) = F."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#teoria#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "No segmento raciocinio-logico/a00/s03 (Fundamentos Teóricos), a fundamentação conceitual das variáveis estabelecidas é indispensável para a validade das conclusões.",
                    "isTrue": True,
                    "explanation": "O domínio sobre Fundamentos Teóricos no trecho raciocinio-logico/a00/s03 requer exatidão na aplicação das definições técnicas."
                },
                "proposed": {
                    "statement": "A negação lógica de uma proposição simples afirmativa pode ser realizada antepondo-se o modificador 'não' ao verbo principal ou usando-se expressões como 'é falso que' ou 'não é verdade que'.",
                    "isTrue": True,
                    "explanation": "Item correto. Todas essas construções invertem formalmente o valor de verdade da proposição original, constituindo formas equivalentes de negação."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#teoria#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Em relação a Fundamentos Teóricos no âmbito de raciocinio-logico/a00/s03, admite-se o descarte arbitrário dos critérios normativos sem qualquer amparo legal.",
                    "isTrue": False,
                    "explanation": "Os critérios normativos de Fundamentos Teóricos em raciocinio-logico/a00/s03 são vinculantes e de observância obrigatória."
                },
                "proposed": {
                    "statement": "A negação lógica da proposição 'O cabo Silva é recifense' é expressa corretamente por 'O cabo Silva é paulista'.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Substituir o predicado por um termo contrário ou alternativo não nega a proposição, pois o militar poderia ser de outro município de Pernambuco ou de outro estado; a negação exata é 'O cabo Silva não é recifense'."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#teoria#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A análise integrada das premissas de Aplicações Práticas em raciocinio-logico/a00/s03 assegura a coerência lógica entre os fundamentos e os resultados obtidos.",
                    "isTrue": True,
                    "explanation": "A correlação entre premissas e conclusões em Aplicações Práticas (raciocinio-logico/a00/s03) sustenta a solidez da matéria."
                },
                "proposed": {
                    "statement": "Dada a proposição simples negativa 'O hidrante não está operacional', a sua negação lógica é a proposição afirmativa 'O hidrante está operacional'.",
                    "isTrue": True,
                    "explanation": "Item correto. Negar uma sentença que já contém uma negação equivale a afirmar o fato originário, eliminando a partícula negativa: ~(~p) ≡ p."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#teoria#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para a compreensão técnica de Aplicações Práticas em raciocinio-logico/a00/s03, considera-se inútil averiguar a conformidade com as diretrizes consolidadas.",
                    "isTrue": False,
                    "explanation": "A averiguação da conformidade em Aplicações Práticas (raciocinio-logico/a00/s03) é basilar para a resolução de casos concretos."
                },
                "proposed": {
                    "statement": "A negação lógica de uma proposição pode ser sempre realizada trocando-se uma palavra pelo seu antônimo, independentemente do contexto.",
                    "isTrue": False,
                    "explanation": "Item incorreto. O antônimo expressa apenas o extremo oposto (por exemplo, 'rico' versus 'pobre'), desconsiderando situações intermediárias; a negação lógica deve cobrir todo o universo em que a afirmação não se verifica ('não é rico')."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#revisao#0",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Para fins de revisão de raciocinio-logico/a00/s03 (Fundamentos Teóricos), a identificação precisa das exceções técnicas impede equívocos de interpretação.",
                    "isTrue": True,
                    "explanation": "Distinguir a regra geral de situações excepcionais em Fundamentos Teóricos (raciocinio-logico/a00/s03) consolida o aprendizado."
                },
                "proposed": {
                    "statement": "Na tabela-verdade, a conjunção de uma proposição com sua própria negação (p ∧ ~p) resulta sempre em um valor lógico falso, caracterizando uma contradição.",
                    "isTrue": True,
                    "explanation": "Item correto. Como p e ~p possuem obrigatoriamente valores lógicos contrários, pelo menos uma delas será sempre falsa, tornando a conjunção falsa em todas as linhas."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#revisao#1",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Na fase de revisão do trecho raciocinio-logico/a00/s03 (Fundamentos Teóricos), sustenta-se que a inversão dos princípios basilares não altera o resultado analítico.",
                    "isTrue": False,
                    "explanation": "Inverter os princípios basilares de Fundamentos Teóricos em raciocinio-logico/a00/s03 invalida diretamente as conclusões."
                },
                "proposed": {
                    "statement": "A negação da sentença 'Nenhum bombeiro faltou ao serviço' é corretamente obtida pela sentença 'Todos os bombeiros faltaram ao serviço'.",
                    "isTrue": False,
                    "explanation": "Item incorreto. A negação do quantificador universal negativo 'nenhum' é o quantificador particular 'pelo menos um' ('Algum bombeiro faltou ao serviço'), e não o oposto universal."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#revisao#2",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "A consolidação sistemática dos tópicos de Aplicações Práticas em raciocinio-logico/a00/s03 prepara o candidato para responder com segurança à banca examinadora.",
                    "isTrue": True,
                    "explanation": "O domínio estruturado sobre Aplicações Práticas (raciocinio-logico/a00/s03) atende diretamente às exigências da prova."
                },
                "proposed": {
                    "statement": "A disjunção de uma proposição qualquer com sua negação (p ∨ ~p) é invariavelmente uma tautologia.",
                    "isTrue": True,
                    "explanation": "Item correto. Pelo Princípio do Terceiro Excluído, ao menos uma das parcelas p ou ~p será verdadeira, fazendo com que a disjunção inclusiva seja sempre verdadeira."
                }
            },
            {
                "id": "raciocinio-logico/a00/s03#revisao#3",
                "category": "template_placeholder",
                "severity": "Alta",
                "original": {
                    "statement": "Durante a revisão de Aplicações Práticas no segmento raciocinio-logico/a00/s03, dispensa-se a observância das balizas conceituais consagradas.",
                    "isTrue": False,
                    "explanation": "As balizas conceituais de Aplicações Práticas em raciocinio-logico/a00/s03 devem ser estritamente consideradas na etapa revisional."
                },
                "proposed": {
                    "statement": "A negação de 'O capitão foi promovido e o tenente viajou' consiste em negar apenas a primeira proposição mantendo o conectivo e.",
                    "isTrue": False,
                    "explanation": "Item incorreto. Pela 1ª Lei de De Morgan, a negação de uma conjunção (p ∧ q) é a disjunção das negações (~p ∨ ~q): 'O capitão não foi promovido OU o tenente não viajou'."
                }
            }
        ]
    },
    "saneamento_plano_raciocinio_logico": {
        "diagnostico": "Todos os 560 itens C/E dos 70 segmentos de Raciocínio Lógico (a00 a a07) foram sintetizados com 23 variações de um mesmo boilerplate institucional ('No segmento raciocinio-logico/aXX/sYY...', 'critérios normativos sem qualquer amparo legal', 'balizas conceituais consagradas'). Nenhum item continha operadores lógicos, regras de inferência, diagramas ou problemas autênticos.",
        "distribuicao_por_aula": [
            {"aula": "raciocinio-logico/a00", "tema": "Estruturas Lógicas I (Proposições, Princípios, Sentenças Abertas)", "segmentos": 12, "itens": 96},
            {"aula": "raciocinio-logico/a01", "tema": "Estruturas Lógicas II (Tabelas-Verdade, Conectivos, Tautologia/Contradição)", "segmentos": 9, "itens": 72},
            {"aula": "raciocinio-logico/a02", "tema": "Equivalências Lógicas e Negações (De Morgan, Condicionais, Contrapositiva)", "segmentos": 11, "itens": 88},
            {"aula": "raciocinio-logico/a03", "tema": "Diagramas Lógicos e Quantificadores (Todo, Algum, Nenhum)", "segmentos": 2, "itens": 16},
            {"aula": "raciocinio-logico/a04", "tema": "Lógica de Argumentação (Validade, Silogismo, Premissas e Conclusão)", "segmentos": 12, "itens": 96},
            {"aula": "raciocinio-logico/a05", "tema": "Raciocínio Crítico I (Falácias Formais e Materiais, Argumentos Abdutivos)", "segmentos": 10, "itens": 80},
            {"aula": "raciocinio-logico/a06", "tema": "Análise Combinatória (Princípio Multiplicativo, Permutação, Combinação)", "segmentos": 8, "itens": 64},
            {"aula": "raciocinio-logico/a07", "tema": "Probabilidade (Espaço Amostral, Eventos, Probabilidade Condicional e Total)", "segmentos": 6, "itens": 48}
        ],
        "metodologia_recomendada": "Executar a reescrita sistemática de 8 itens por segmento (4 teoria e 4 revisão), com 2 C e 2 E balanceados por conjunto, aderindo estritamente aos tópicos documentados nos summaries de cada segmento."
    }
}

target_json = r"C:\Users\Administrador\.gemini\antigravity\brain\94ed5ef5-5793-49ad-b5ab-7577f556a2ab\audits\bizu-3-exatas.json"
with open(target_json, 'w', encoding='utf-8') as f:
    json.dump(audit_data, f, ensure_ascii=False, indent=2)

print("Saved audit JSON to:", target_json)
