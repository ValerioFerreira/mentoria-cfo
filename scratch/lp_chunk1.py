# -*- coding: utf-8 -*-
"""Chunk 1: Q1 to Q20"""

def get_chunk1():
    q = []
    
    # 1. a02/s07 | A
    q.append({
        "seg": "a02/s07", "gab": "A",
        "stem": "Considerando as regras gramaticais relativas à colocação pronominal dos pronomes oblíquos átonos, assinale a opção correta.",
        "opts": [
            "O início de período mediante pronome oblíquo átono contraria frontalmente a norma culta padrão da língua portuguesa.",
            "A ocorrência de particípio passado admite livremente a aposição de pronome oblíquo átono em posição enclítica.",
            "Os verbos conjugados no futuro do presente autorizam a colocação enclítica do pronome oblíquo em qualquer contexto.",
            "A presença de conjunção coordenativa aditiva torna obrigatória a anteposição do pronome oblíquo ao verbo subordinado.",
            "A mesóclise é de emprego obrigatório mesmo quando houver palavra de sentido negativo antecedendo a forma verbal de futuro."
        ],
        "comment": "O início de período mediante pronome oblíquo átono é vedado pela norma culta, que exige ênclise nessa hipótese. O particípio nunca admite ênclise, os tempos de futuro repelem a ênclise, e a presença de termo negativo atrai o pronome, impondo a próclise mesmo diante de verbos no futuro."
    })

    # 2. a02/s07 | E
    q.append({
        "seg": "a02/s07", "gab": "E",
        "stem": "No que diz respeito à colocação pronominal em estruturas formadas por locuções verbais, assinale a opção correta.",
        "opts": [
            "Havendo palavra atrativa antes da locução com particípio, o pronome oblíquo deve ser colocado em ênclise ao verbo principal.",
            "Na locução formada por verbo auxiliar e particípio sem palavra atrativa, o pronome oblíquo pode ligar-se por ênclise ao particípio.",
            "Em locuções com verbo principal no infinitivo, o pronome oblíquo jamais pode ser posicionado após o verbo principal.",
            "A presença de palavra negativa antes de locução verbal anula qualquer possibilidade de colocação pronominal após o auxiliar.",
            "Na locução verbal cujo verbo principal é o infinitivo, admite-se a ênclise ao infinitivo mesmo havendo palavra atrativa antes do auxiliar."
        ],
        "comment": "Quando o verbo principal de uma locução verbal está no infinitivo ou gerúndio, a ênclise a essa forma nominal é sempre legítima, mesmo na presença de palavra atrativa antes do auxiliar. Ao contrário, formas no particípio jamais admitem ênclise, devendo o pronome apoiar-se no auxiliar."
    })

    # 3. a03/s01 | E
    q.append({
        "seg": "a03/s01", "gab": "E",
        "stem": "Quanto à classificação das preposições em essenciais e acidentais no sistema gramatical, assinale a opção correta.",
        "opts": [
            "As preposições acidentais pertencem originariamente à classe das preposições e nunca atuam como outras classes.",
            "Os vocábulos 'sob', 'sobre' e 'sem' configuram preposições acidentais que derivaram historicamente de adjetivos.",
            "As preposições essenciais perdem seu valor conectivo sempre que introduzem termos que funcionam como complementos.",
            "O termo 'conforme' classifica-se como preposição essencial de uso invariável em todos os contextos da oração.",
            "As palavras 'consoante', 'mediante' e 'segundo' atuam como preposições acidentais quando desempenham papel conectivo."
        ],
        "comment": "As preposições acidentais consistem em vocábulos originários de outras classes morfológicas (como adjetivos, advérbios ou conjunções) que passam a atuar eventualmente na função prepositiva, como consoante, segundo, mediante, durante e visto. Já vocábulos como sob, sobre e sem são essenciais."
    })

    # 4. a03/s01 | D
    q.append({
        "seg": "a03/s01", "gab": "D",
        "stem": "Acerca dos valores semânticos introduzidos pela preposição 'de' na estruturação oracional, assinale a opção correta.",
        "opts": [
            "Na frase 'O servidor morreu de exaustão', a preposição destacada introduz exclusivamente uma circunstância de modo.",
            "Na expressão 'mesa de carvalho maciço', a preposição em apreço estabelece inequívoca relação de causa originária.",
            "No enunciado 'Retornou de Brasília ontem', o termo preposicionado desempenha papel de adjunto com sentido de posse.",
            "Na estrutura 'Ele tremia de medo durante o depoimento', a preposição 'de' introduz valor semântico de causa do fato.",
            "Na construção 'Comprei o livro de poesias', a preposição em destaque exprime unicamente o instrumento da redação."
        ],
        "comment": "Na estrutura em que o indivíduo treme de medo ou morre de exaustão, a preposição 'de' estabelece a relação semântica de causa ou motivo gerador do estado. Nas demais construções, a preposição introduz noções materiais, procedência geográfica e conteúdo ou assunto."
    })

    # 5. a03/s01 | C
    q.append({
        "seg": "a03/s01", "gab": "C",
        "stem": "No que se refere às relações de sentido expressas pela preposição 'com' no padrão culto, assinale a opção correta.",
        "opts": [
            "Na frase 'O suspeito arrombou a porta com a gazua', a preposição em destaque denota circunstância de companhia.",
            "Na oração 'O delegado saiu com os agentes da equipe', o termo introduzido pela preposição possui sentido de instrumento.",
            "Na estrutura 'A testemunha falou com serenidade ao depor', a preposição 'com' introduz circunstância adverbial de modo.",
            "No trecho 'Com o temporal, os voos foram suspensos', a preposição utilizada exprime primariamente uma ideia de oposição.",
            "Na sentença 'Trabalhou com afinco durante o expediente', a expressão prepositiva estabelece noção de matéria física."
        ],
        "comment": "A locução prepositiva 'com serenidade' constrói adjunto adverbial de modo, assinalando a maneira como o ato de depor ocorreu. Por sua vez, o emprego de instrumento dá-se com ferramentas ou armas, a companhia envolve coautores ou acompanhantes, e temporais introduzem causa."
    })

    # 6. a03/s01 | D
    q.append({
        "seg": "a03/s01", "gab": "D",
        "stem": "Considerando os diferentes valores semânticos veiculados pelas preposições 'para' e 'por', assinale a opção correta.",
        "opts": [
            "A preposição 'para' atua exclusivamente na indicação de meio físico pelo qual se transmite uma ordem judicial.",
            "A preposição 'por' na oração 'Lutou por justiça social' veicula primordialmente uma noção espacial de limite terminal.",
            "Na estrutura 'Viajou para o litoral', o termo preposicionado introduz valor semântico de causa determinante da ação.",
            "No período 'Estudou com rigor para ser aprovado', a preposição 'para' introduz oração subordinada com sentido de finalidade.",
            "No enunciado 'O suspeito foi detido por populares', a preposição destacada indica direção espacial de afastamento."
        ],
        "comment": "A preposição 'para' antecedendo oração em forma nominal de infinitivo traduz a finalidade ou o objetivo visado pela conduta. Paralelamente, expressões como 'por populares' identificam o agente da passiva, e 'para o litoral' denota destino ou direção espacial."
    })

    # 7. a03/s01 | B
    q.append({
        "seg": "a03/s01", "gab": "B",
        "stem": "A respeito da distinção entre preposição gramatical e preposição nocional na análise sintática, assinale a opção correta.",
        "opts": [
            "A preposição gramatical introduz termos puramente acessórios e veicula ampla variedade de noções circunstanciais.",
            "A preposição gramatical é aquela exigida por regência verbal ou nominal, funcionando como mero conectivo sintático.",
            "A preposição nocional decorre obrigatoriamente da exigência sintática de um verbo transitivo direto ou indireto.",
            "As preposições que introduzem adjuntos adverbiais classificam-se como gramaticais por carência de conteúdo semântico.",
            "Toda preposição empregada no padrão culto atua indistintamente sem qualquer diferenciação funcional ou semântica."
        ],
        "comment": "A preposição gramatical atua como simples elo conectivo exigido pelas normas de regência de verbos ou nomes, desprovida de autonomia de significado. Já a preposição nocional preserva conteúdo semântico próprio ao introduzir termos adverbiais que veiculam circunstâncias concretas."
    })

    # 8. a03/s02 | C
    q.append({
        "seg": "a03/s02", "gab": "C",
        "stem": "Em relação ao emprego das conjunções coordenativas adversativas no encadeamento oracional, assinale a opção correta.",
        "opts": [
            "O conectivo 'porém' pode ser deslocado para o interior da oração sem que haja necessidade de isolamento por vírgulas.",
            "A conjunção 'mas' admite posicionamento intercalado ou no final da oração coordenada com plena correção gramatical.",
            "Os conectivos 'contudo', 'todavia' e 'entretanto' são sinônimos de 'mas' e podem ser empregados no início ou intercalados.",
            "A conjunção 'porquanto' classifica-se como adversativa e pode substituir 'porém' sem gerar qualquer alteração semântica.",
            "O nexo adversativo estabelece relação de justificativa necessária e harmônica com o teor expresso na oração anterior."
        ],
        "comment": "Conjunções coordenativas adversativas como contudo, todavia, porém e entretanto estabelecem oposição ou quebra de expectativa e podem figurar no início da oração ou intercaladas entre vírgulas. A conjunção 'mas' fixa-se no início da oração, e 'porquanto' tem sentido causal."
    })

    # 9. a03/s02 | E
    q.append({
        "seg": "a03/s02", "gab": "E",
        "stem": "No que concerne à distinção funcional entre a conjunção 'pois' explicativa e a conjunção 'pois' conclusiva, assinale a opção correta.",
        "opts": [
            "A conjunção 'pois' atua como conclusiva sempre que se posicionar no início da oração imediatamente antes do verbo.",
            "A forma 'pois' posposta ao verbo exerce valor exclusivamente causal e prescinde de vírgulas de isolamento no período.",
            "O vocábulo 'pois' no início da oração expressa dedução lógica que decorre naturalmente da proposição antecedente.",
            "As formas 'portanto' e 'pois' inicial são perfeitamente intercambiáveis sem provocar mudança na classificação oracional.",
            "A conjunção 'pois' adquire valor conclusivo quando colocada após o verbo da oração coordenada, devendo vir entre vírgulas."
        ],
        "comment": "A conjunção 'pois' possui valor estritamente conclusivo quando vem posposta ao verbo da oração coordenada, requerendo isolamento por vírgulas na estrutura sintática. Quando anteposta ao verbo, no início da oração, assume função explicativa ou causal."
    })

    # 10. a03/s02 | D
    q.append({
        "seg": "a03/s02", "gab": "D",
        "stem": "Acerca das conjunções coordenativas aditivas correlatas na estruturação do período, assinale a opção correta.",
        "opts": [
            "A estrutura 'não só... como também' estabelece oposição categórica entre as orações coordenadas articuladas.",
            "O emprego da conjunção 'nem' impõe que o período seja iniciado obrigatoriamente por uma proposição afirmativa enfática.",
            "A correlação 'não apenas... mas ainda' exprime relação sintática de exclusão mútua entre os termos por ela vinculados.",
            "As expressões correlativas aditivas acumulam informações e conferem destaque argumentativo ao segundo elemento coordenado.",
            "A conjunção aditiva simples 'e' repele qualquer associação com orações que contenham sujeitos gramaticais diferentes."
        ],
        "comment": "Locuções aditivas correlatas como 'não só... mas também' e 'não apenas... como ainda' operam a soma cumulativa de elementos sintáticos, conferindo maior peso retórico e discursivo à segunda informação agregada ao período, sem estabelecer oposição ou exclusão."
    })

    # 11. a03/s02 | B
    q.append({
        "seg": "a03/s02", "gab": "B",
        "stem": "Quanto ao emprego das conjunções coordenativas alternativas e aos sentidos que instauram no texto, assinale a opção correta.",
        "opts": [
            "As conjunções alternativas ligam unicamente ideias que se somam de maneira simultânea e perfeitamente idêntica no tempo.",
            "A conjunção 'ou' pode veicular valor semântico de exclusão recíproca ou expressar alternância de situações possíveis.",
            "O par correlativo 'ora... ora' introduz orações coordenadas conclusivas que decorrem logicamente de premissas certas.",
            "A repetição da partícula 'quer... quer' estabelece nexo de concessão irrestrita perante o fato enunciado na principal.",
            "As orações coordenadas alternativas prescindem do emprego de vírgula mesmo quando apresentarem elementos repetidos."
        ],
        "comment": "A conjunção alternativa 'ou' e suas variantes emparelhadas articulam ideias que oscilam entre a exclusão mútua (em que a realização de um termo impede a do outro) e a simples alternância ou equivalência funcional de fatos no enunciado."
    })

    # 12. a03/s03 | A
    q.append({
        "seg": "a03/s03", "gab": "A",
        "stem": "No que se refere às conjunções subordinativas adverbiais concessivas e à sua semântica oracional, assinale a opção correta.",
        "opts": [
            "O conectivo 'conquanto' introduz oração que apresenta fato que poderia obstar a ação principal, mas não a impede.",
            "A conjunção concessiva 'embora' exige que o verbo da oração subordinada se flexione compulsoriamente no modo indicativo.",
            "A locução conjuntiva 'visto que' classifica-se como concessiva e pode ser permutada livremente por 'ainda que'.",
            "A oração concessiva estabelece uma condição estrita e indispensável para que o evento da oração principal se realize.",
            "As locuções 'posto que' e 'se bem que' transmitem primariamente uma ideia de finalidade deliberada do agente."
        ],
        "comment": "A oração subordinada adverbial concessiva, introduzida por conectivos como conquanto, embora, ainda que e se bem que, estabelece uma ressalva ou obstáculo hipotético que é incapaz de frustrar a concretização da oração principal, regendo o verbo no modo subjuntivo."
    })

    # 13. a03/s03 | B
    q.append({
        "seg": "a03/s03", "gab": "B",
        "stem": "A respeito das conjunções subordinativas adverbiais conformativas na articulação textual, assinale a opção correta.",
        "opts": [
            "Os conectivos conformativos indicam que a oração principal decorre como consequência física da oração subordinada.",
            "As conjunções 'conforme', 'segundo' e 'consoante' exprimem acordo, conformidade ou regra adotada como referência.",
            "A conjunção 'como' jamais pode ser empregada com valor conformativo no padrão formal da língua portuguesa escrita.",
            "O conectivo 'caso' classifica-se legitimamente como conformativo quando associado a verbos no modo subjuntivo.",
            "A oração conformativa possui sentido equivalente ao da oração proporcional que registra variação concomitante."
        ],
        "comment": "Conjunções conformativas como conforme, segundo, consoante e como manifestam concordância, alinhamento ou fidelidade a um parâmetro normativo ou declaração prévia de terceiros, distinguindo-se das noções de causa, condição ou proporcionalidade."
    })

    # 14. a03/s03 | A
    q.append({
        "seg": "a03/s03", "gab": "A",
        "stem": "Considerando as regras gramaticais pertinentes às locuções conjuntivas proporcionais, assinale a opção correta.",
        "opts": [
            "A locução proporcional consagrada pela norma culta é 'à medida que', sendo considerada incorreta a forma 'à medida em que'.",
            "A expressão 'na medida em que' expressa rigorosamente proporção matemática e equivale semanticamente a 'à proporção que'.",
            "A locução 'ao passo que' é incapaz de expressar contraste ou proporção no encadeamento de dois fatos concomitantes.",
            "A forma híbrida 'à proporção em que' é plenamente admitida como padrão irrepreensível pela gramática normativa.",
            "As orações proporcionais estabelecem relação de causa determinante imediata sem qualquer paralelismo temporal."
        ],
        "comment": "No padrão culto, a locução proporcional legítima é 'à medida que', sendo considerada erro a fusão indevida 'à medida em que'. A locução 'na medida em que' possui valor causal (equivalente a já que, visto que), devendo ser preservada a distinção semântica entre os conectivos."
    })

    # 15. a03/s03 | A
    q.append({
        "seg": "a03/s03", "gab": "A",
        "stem": "Acerca da distinção semântica entre as orações subordinadas causais e as consecutivas, assinale a opção correta.",
        "opts": [
            "A oração causal exprime o motivo gerador anterior, ao passo que a consecutiva expressa o resultado ou efeito decorrente.",
            "A oração consecutiva apresenta a razão determinante que impulsiona o fato anunciado na oração subordinante.",
            "A locução 'de modo que' introduz prioritariamente oração subordinada causal com verbo conjugado no particípio.",
            "A oração causal é introduzida tipicamente por termos intensificadores antecedentes como 'tamanho', 'tão' e 'tanto'.",
            "As relações de causa e de consequência são absolutamente idênticas e intercambiáveis na estruturação do período."
        ],
        "comment": "A oração causal enuncia a razão, origem ou motivação cronologicamente prévia que provocou um dado fenômeno, enquanto a oração consecutiva manifesta o efeito, a consequência ou o resultado consequente, comumente precedida de termos intensivos na oração principal."
    })

    # 16. a05/s01 | E
    q.append({
        "seg": "a05/s01", "gab": "E",
        "stem": "No que se refere à indeterminação do sujeito por meio da partícula 'se', assinale a opção correta.",
        "opts": [
            "A indeterminação do sujeito ocorre exclusivamente quando o pronome 'se' estiver ligado a verbos transitivos diretos.",
            "O verbo transitivo direto acompanhado de 'se' fica indeterminado e flexiona-se compulsoriamente na terceira pessoa do plural.",
            "Na oração 'Trabalha-se com afinco nesta delegacia', a palavra 'se' atua como pronome apassivador de sujeito paciente.",
            "A presença de objeto direto na oração impede que o sujeito seja determinado pela desinência do verbo antecedente.",
            "O índice de indeterminação do sujeito atua com verbos transitivos indiretos, intransitivos e de ligação, mantendo o verbo no singular."
        ],
        "comment": "O pronome 'se' classifica-se como índice de indeterminação do sujeito quando vinculado a verbos transitivos indiretos, verbos intransitivos ou verbos de ligação, circunstância na qual o verbo permanece rigorosamente flexionado na terceira pessoa do singular."
    })

    # 17. a05/s01 | B
    q.append({
        "seg": "a05/s01", "gab": "B",
        "stem": "A respeito da identificação do núcleo do sujeito e de sua classificação sintática, assinale a opção correta.",
        "opts": [
            "O núcleo do sujeito de uma oração pode ser constituído por vocábulo obrigatoriamente regido por preposição explícita.",
            "Na oração 'A análise minuciosa dos vestígios revelou o autor', o núcleo do sujeito é o substantivo 'análise'.",
            "O sujeito de uma oração classifica-se como composto sempre que o seu único núcleo estiver modificado por vários adjuntos.",
            "Na estrutura 'Chegaram o perito e o escrivão', o sujeito classifica-se como simples em virtude da posição do verbo.",
            "Os termos determinantes como adjetivos e artigos integram o núcleo substancial do sujeito nas orações da língua."
        ],
        "comment": "O núcleo do sujeito é o vocábulo substantivo básico, desprovido de preposição, com o qual o verbo estabelece concordância. Em 'A análise minuciosa dos vestígios', o núcleo substantivo é unicamente 'análise', constituindo sujeito simples determinado."
    })

    # 18. a05/s01 | C
    q.append({
        "seg": "a05/s01", "gab": "C",
        "stem": "Quanto à distinção entre sujeito oculto (desinencial) e sujeito indeterminado na norma culta, assinale a opção correta.",
        "opts": [
            "O sujeito oculto ocorre quando não se pode identificar nem inferir o agente da oração por nenhum elemento linguístico.",
            "O verbo flexionado na terceira pessoa do plural sempre indetermina o sujeito, mesmo quando o referente já estiver expresso no texto.",
            "O sujeito é desinencial quando sua identificação é depreendida pela terminação verbal ou pelo contexto oracional precedente.",
            "Em 'Roubaram o veículo durante a madrugada', o sujeito classifica-se normativamente como desinencial da terceira pessoa.",
            "A oração com sujeito oculto carece de predicação e não permite qualquer tipo de concordância em número e pessoa."
        ],
        "comment": "O sujeito é desinencial, elíptico ou oculto quando não comparece explicitamente como palavra na oração, mas é perfeitamente identificável pela desinência número-pessoal do verbo ou pela retomada contextual do referente anterior."
    })

    # 19. a05/s01 | C
    q.append({
        "seg": "a05/s01", "gab": "C",
        "stem": "Considerando as regras sintáticas que disciplinam as orações sem sujeito na língua portuguesa, assinale a opção correta.",
        "opts": [
            "Os verbos que indicam fenômenos da natureza permanecem impessoais mesmo quando empregados em sentido figurado.",
            "O verbo 'fazer' na indicação de tempo transcorrido é pessoal e deve flexionar-se no plural para concordar com os dias.",
            "A oração sem sujeito estrutura-se com verbos impessoais que permanecem invariáveis na terceira pessoa do singular.",
            "Em 'Choveram denúncias contra a quadrilha', a oração é classificada como sem sujeito por envolver fenômeno meteorológico.",
            "O verbo 'haver' no sentido de existir admite flexão de plural se o objeto direto estiver no plural, tornando-se pessoal."
        ],
        "comment": "As orações sem sujeito constroem-se com verbos impessoais, os quais não possuem sujeito sintático e mantêm-se invariáveis na terceira pessoa do singular. Verbos meteorológicos figurados adquirem sujeito (como em 'choveram denúncias'), tornando-se regulares."
    })

    # 20. a05/s02 | A
    q.append({
        "seg": "a05/s02", "gab": "A",
        "stem": "No que se refere à ocorrência do objeto direto preposicionado na estrutura sintática, assinale a opção correta.",
        "opts": [
            "O emprego da preposição antes do objeto direto é obrigatório quando o complemento for representado por pronome oblíquo tônico.",
            "O objeto direto preposicionado transforma o verbo transitivo direto originário em verbo transitivo indireto puro.",
            "A anteposição de preposição ao objeto direto é terminantemente proibida nas hipóteses em que visar a evitar ambiguidade.",
            "O pronome relativo 'quem' atuando como objeto direto rejeita compulsoriamente a presença de qualquer preposição.",
            "A construção de objeto direto preposicionado decorre sempre de exigência expressa do padrão de regência do verbo."
        ],
        "comment": "O objeto direto preposicionado ocorre com verbos de regência direta por fatores estilísticos ou gramaticais específicos, sendo o emprego da preposição obrigatório quando o complemento é formado por pronome oblíquo tônico (como mim, ti, si, ele)."
    })

    return q
