import json

questoes = [
    # 1. biologia/a05/s01 - tec_1407221
    {
        "id": "tec_1407221",
        "capitulo": "biologia/a05/s01",
        "comentario": "Gabarito: Letra E.\n\nA alternativa E está correta porque a pele é dividida didaticamente em epiderme superficial epitelial, derme conjuntiva vascularizada e a hipoderme (tela subcutânea) de sustentação rica em adipócitos.\nA alternativa A está incorreta: a hipoderme é a camada mais profunda, enquanto a epiderme é a mais superficial.\nA alternativa B está incorreta: a pele desempenha múltiplas funções essenciais, como termorregulação, excreção sudorípara, percepção sensorial tátil e síntese de precursores da vitamina D.\nA alternativa C está incorreta: o tegumento é indispensável à homeostase corporal e barreira imunológica primária.\nA alternativa D está incorreta: apenas a lâmina superficial córnea é formada por queratinócitos mortos anucleados; os estratos subjacentes da epiderme e toda a derme são altamente celulares e metabolicamente vivos."
    },
    # 2. biologia/a05/s01 - tec_1407305
    {
        "id": "tec_1407305",
        "capitulo": "biologia/a05/s01",
        "comentario": "Gabarito: Letra D.\n\nAnálise minuciosa de cada assertiva:\nItem I: Correto. A pele desempenha proteção contra dessecação e patógenos, controle térmico por vasodilatação e suor, recepção sensorial somatossensorial e conversão metabólica.\nItem II: Correto. Pelos, unhas, glândulas sebáceas e glândulas sudoríparas representam os anexos queratinizados e glandulares clássicos derivados da diferenciação epitelial.\nItem III: Correto. O organismo regula a perda calórica pela evaporação aquosa do suor e pela contração do músculo eretor do pelo que eriça a pelagem corporal.\nItem IV: Correto. As lâminas ungueais são compactações densas e translúcidas de queratina dura anucleada com elevado teor de enxofre.\nItem V: Incorreto. A coloração cutânea oferece sinais clínicos valiosos: palidez indica má perfusão periférica, cianose traduz hipóxia arterial e icterícia sinaliza hiperbilirrubinemia hepática."
    },
    # 3. biologia/a05/s02 - tec_2703167
    {
        "id": "tec_2703167",
        "capitulo": "biologia/a05/s02",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A apresenta a sequência anatômica estratigráfica exata da parede abdominal, da superfície externa em direção às vísceras profundas: epiderme avascular superficial, derme vascular com colágeno, tela subcutânea (hipoderme adiposa), fáscia muscular de revestimento profundo, planos musculares esqueléticos da parede abdominal, peritônio parietal seroso e, finalmente, as vísceras e órgãos abdominais cavitários.\nAs alternativas B, C, D e E estão erradas porque invertem a ordem lógica dos estratos teciduais, posicionando incorretamente a fáscia profunda antes da hipoderme ou inserindo a lâmina peritoneal antes dos planos musculares da parede do abdome."
    },
    # 4. biologia/a05/s02 - tec_2119446
    {
        "id": "tec_2119446",
        "capitulo": "biologia/a05/s02",
        "comentario": "Gabarito: Letra B.\n\nA alternativa B está correta porque a camada lesada descrita no enunciado corresponde precisamente à hipoderme (também denominada tela subcutânea ou panículo adiposo). Este estrato profundo é composto por lóbulos de adipócitos uniloculares ricos em triglicerídeos que funcionam como reserva energética, isolamento térmico, proteção mecânica contra choques e secreção de citocinas endócrinas como a leptina.\nAs alternativas A, C e D (ectoderme, endoderme e mesoderme) são folhetos embrionários primordiais germinativos, não camadas tegumentares anatômicas.\nA alternativa E está errada porque a derme não é a camada mais profunda e é formada primariamente por tecido conjuntivo fibroso e vascular, e não por massa lobular predominante de adipócitos."
    },
    # 5. biologia/a05/s03 - tec_1718940
    {
        "id": "tec_1718940",
        "capitulo": "biologia/a05/s03",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A é a correta: o sistema tegumentar reveste externamente todo o corpo humano, constituindo uma barreira de proteção física, química e biológica que isola o meio interno do ambiente externo.\nA alternativa B está incorreta: a eliminação de resíduos metabólicos hidrossolúveis é atribuição do sistema urinário/renal, e não do sistema entérico (que rege a motilidade e secreção digestória gastrointestinal).\nA alternativa C está incorreta: a respiração e expansão mecânica pulmonar são coordenadas por centros nervosos motores do tronco encefálico e musculatura esquelética (diafragma e intercostais), não por hormônios endócrinos pulmonares.\nA alternativa D está incorreta: o sistema reprodutor masculino produz espermatozoides nos testículos e o feminino produz ovócitos nos ovários, sem uma estrutura central única compartilhada.\nA alternativa E está incorreta: a distribuição de oxigênio e nutrientes impulsionada pelo coração corresponde ao sistema circulatório/cardiovascular."
    },
    # 6. biologia/a05/s03 - mentoria_mcn_biologia_023_5a08b8
    {
        "id": "mentoria_mcn_biologia_023_5a08b8",
        "capitulo": "biologia/a05/s03",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A está correta porque retrata com fidelidade a cronologia biológica do reparo tecidual cutâneo: após a fase de hemostasia primária e coagulação por fibrina nos primeiros minutos, segue-se a fase inflamatória (1 a 4 dias) com migração leucocitária de neutrófilos e macrófagos fagocitários; logo após instala-se a fase proliferativa (4 a 14 dias), caracterizada por angiogênese, síntese de colágeno jovem do tipo III por fibroblastos e formação do tecido de granulação avermelhado; por fim, na fase de maturação e remodelação (semanas a meses), o colágeno tipo III é substituído pelo colágeno tipo I com retração das bordas pelos miofibroblastos.\nAs alternativas B, C e D erram ao inverter as etapas temporais ou negar a síntese ativa de matriz pelos fibroblastos no tecido de granulação."
    },
    # 7. biologia/a06/s01 - tec_1429638
    {
        "id": "tec_1429638",
        "capitulo": "biologia/a06/s01",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A é a correta pois conceitua de forma precisa a cartilagem hialina: trata-se de um tecido avascular homogêneo dotado de fibrilas delicadas de colágeno do tipo II, sendo a variedade cartilaginosa mais amplamente distribuída no organismo humano, constituindo as cartilagens articulares móveis, os anéis traqueais e o molde esquelético fetal embrionário.\nA alternativa B está errada: o tecido ósseo é altamente vascularizado por canais de Havers e Volkmann e apresenta intensa inervação sensitiva perióstica.\nA alternativa C está errada: os osteoclastos promovem a reabsorção enzimática ácida e mineral, enquanto os osteoblastos sintetizam o osteoide e promovem a deposição óssea.\nA alternativa D está errada: o canal medular diafisário de adultos abriga medula amarela lipídica; a hematopoiese no adulto ocorre nas trabéculas do osso esponjoso nas epífises, pelve, costelas e vértebras.\nA alternativa E está errada: o crescimento longitudinal depende exclusivamente da proliferação condrocítica nos discos epifisários das metáfises."
    },
    # 8. biologia/a06/s01 - tec_1407316
    {
        "id": "tec_1407316",
        "capitulo": "biologia/a06/s01",
        "comentario": "Gabarito: Letra E.\n\nAnálise individual das proposições da questão:\nItem I: Incorreto. O tecido ósseo compacto apresenta espessa densidade cortical mineralizada, enquanto o tecido esponjoso (trabecular) possui rede arejada de trabéculas intercomunicantes contendo medula óssea.\nItem II: Incorreto. No indivíduo adulto a medula óssea amarela é constituída principalmente por gordura (adipócitos uniloculares de reserva), ao passo que a hematopoiese celular ocorre na medula óssea vermelha ativa.\nItem III: Correto. A cartilagem hialina é a variedade mais comum no corpo, existindo também a fibrocartilagem (discos e meniscos) e a cartilagem elástica (orelha e epiglote).\nItem IV: Correto. Na anatomia de um osso longo identificam-se a epífise distal e proximal, a haste central diafisária e as metáfises intermediárias.\nItem V: Incorreto. A diáfise tubular dos ossos longos é formada essencialmente por córtex espesso de tecido ósseo compacto; o osso esponjoso predomina no interior das epífises dilatadas."
    },
    # 9. biologia/a06/s02 - tec_2703168
    {
        "id": "tec_2703168",
        "capitulo": "biologia/a06/s02",
        "comentario": "Gabarito: Letra C.\n\nA alternativa C está correta: a estrutura fibrocartilaginosa interposta entre os corpos vertebrais adjacentes é o disco intervertebral. Cada disco é composto por um anel fibroso periférico resistente e um núcleo pulposo central elástico e gelatinoso rico em água, atuando como amortecedor de impacto axial contra atritos mecânicos e conferindo mobilidade à coluna.\nA alternativa A está incorreta: o disco epifisário situa-se na metáfise de ossos longos promovendo crescimento em comprimento na juventude.\nA alternativa B está incorreta: inexiste estrutura anatômica denominada disco romboide na coluna vertebral.\nA alternativa D está incorreta: os meniscos são estruturas fibrocartilaginosas em crescente localizadas especificamente no platô articular da articulação femorotibial do joelho.\nA alternativa E está incorreta: embora a cartilagem articular das facetas zigoapofisárias seja hialina, o coxim principal de absorção de peso entre os corpos vertebrais é fibrocartilaginoso."
    },
    # 10. biologia/a06/s02 - tec_870374
    {
        "id": "tec_870374",
        "capitulo": "biologia/a06/s02",
        "comentario": "Gabarito: Letra D.\n\nA alternativa D está correta: o forame magno é uma ampla abertura oval localizada na porção basilar do osso occipital. Por esse orifício o bulbo do tronco encefálico estabelece continuidade física com a medula espinhal, acompanhado pelas artérias vertebrais, ramos espinhais do nervo acessório e pelas meninges protetoras.\nA alternativa A está incorreta: o osso frontal compõe a fronte e o teto da órbita, sem relação com a transição medular da base craniana.\nA alternativa B está incorreta: o osso temporal abriga os aparelhos auditivo e vestibular, o meato acústico interno e o canal carotídeo.\nA alternativa C está incorreta: a maxila compõe o esqueleto facial superior e a arcada dentária superior.\nA alternativa E está incorreta: o zigomático forma a saliência da bochecha (maçã do rosto) e o arco zigomático lateral facial."
    },
    # 11. biologia/a06/s03 - tec_739961
    {
        "id": "tec_739961",
        "capitulo": "biologia/a06/s03",
        "comentario": "Gabarito: Letra C.\n\nA alternativa C expressa a contagem anatômica padrão das vértebras da coluna vertebral humana: sete vértebras cervicais (C1 a C7) no pescoço; doze vértebras torácicas (T1 a T12) articuladas com as costelas; cinco vértebras lombares robustas (L1 a L5) na porção inferior do tronco; cinco vértebras sacrais fundidas que compõem o osso sacro triangular; e quatro vértebras coccígeas fusionadas que formam o cóccix terminal vestigial.\nAs alternativas A e D erram ao listar oito vértebras cervicais (existem oito pares de nervos cervicais, mas apenas sete vértebras ósseas cervicais).\nAs alternativas B e E erram ao indicar apenas uma vértebra sacral ou coccígea em vez de considerar a fusão das cinco sacrais e quatro coccígeas embrionárias."
    },
    # 12. biologia/a06/s03 - tec_870402
    {
        "id": "tec_870402",
        "capitulo": "biologia/a06/s03",
        "comentario": "Gabarito: Letra D.\n\nA alternativa D está correta: o ângulo do esterno (também consagrado na semiologia como ângulo de Louis) é uma crista óssea transversa facilmente palpável na parede torácica anterior, formada pela sincondrose manubrioesternal. Esse marco corresponde com precisão ao ponto de inserção da segunda cartilagem costal no esterno; a partir dele, médicos e socorristas contam para baixo os espaços intercostais e as costelas subjacentes.\nA alternativa A está incorreta: a incisura jugular fica na borda superior do manúbrio na base do pescoço, acima da primeira costela.\nA alternativa B está incorreta: o processo xifoide marca o bordo inferior do esterno na altura da vértebra T9/T10.\nA alternativa C está incorreta: a articulação esternoclavicular é lateral à incisura jugular e fixa a clavícula, não servindo para contagem seriada de costelas.\nA alternativa E está incorreta: o ângulo subcostal demarca a margem inferior do gradil costal abaixo da décima costela."
    },
    # 13. biologia/a06/s04 - tec_1666202
    {
        "id": "tec_1666202",
        "capitulo": "biologia/a06/s04",
        "comentario": "Gabarito: Letra E.\n\nA alternativa E está correta: na nomenclatura anatômica internacional, o termo \"braço\" refere-se estritamente ao segmento anatômico situado entre o ombro e o cotovelo, cujo único arcabouço ósseo é o úmero.\nA alternativa A está incorreta: a ulna localiza-se no antebraço em posição medial paralela ao rádio.\nA alternativa B está incorreta: o escafoide é um dos oito ossos que compõem o carpo na articulação do punho.\nA alternativa C está incorreta: o fêmur é o osso longo que constitui a coxa no membro inferior.\nA alternativa D está incorreta: o rádio compõe a porção lateral do antebraço articulando-se com o carpo no punho."
    },
    # 14. biologia/a06/s04 - tec_529939
    {
        "id": "tec_529939",
        "capitulo": "biologia/a06/s04",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A é a única que elenca a totalidade dos ossos da cintura peitoral e do membro superior: a cintura escapular é formada pelas clavículas e escápulas; o braço pelo úmero; o antebraço pelo rádio e pela ulna; o punho pelos oito ossos do carpo; a palma pelos cinco metacarpais; e os dígitos pelas catorze falanges articulares.\nA alternativa B está errada pois omitiu o úmero.\nA alternativa C está errada pois omitiu o rádio e usou incorretamente a grafia no singular (\"osso do carpo\").\nA alternativa D está errada pois esqueceu a ulna e os metacarpais da palma.\nA alternativa E está errada porque descreveu apenas os ossos do membro superior livre, esquecendo completamente a clavícula e a escápula que compõem a cintura escapular."
    },
    # 15. biologia/a06/s05 - tec_1666223
    {
        "id": "tec_1666223",
        "capitulo": "biologia/a06/s05",
        "comentario": "Gabarito: Letra E.\n\nA alternativa E está correta: o fêmur, osso par que constitui o esqueleto da coxa humana, é comprovadamente o osso mais longo, volumoso, pesado e resistente de todo o corpo humano, suportando forças mecânicas axiais de várias vezes o peso corporal durante corridas e saltos.\nAs alternativas A, B, C e D (úmero, rádio, fíbula e tíbia) representam ossos longos do esqueleto apendicular, porém todos possuem dimensões de comprimento e massa consideravelmente inferiores às medidas métricas do fêmur em indivíduos adultos normais."
    },
    # 16. biologia/a06/s05 - tec_529941
    {
        "id": "tec_529941",
        "capitulo": "biologia/a06/s05",
        "comentario": "Gabarito: Letra A.\n\nA alternativa A descreve com exatidão a morfologia e as relações articulares do fêmur: sendo um osso longo típico, apresenta uma epífise proximal (com cabeça hemisférica, colo e trocanteres), uma haste cilíndrica central diafisária e uma epífise distal bicondilar. Sua cabeça proximal articula-se com a cavidade cotiloide do acetábulo no osso do quadril, enquanto seus côndilos distais articulam-se com os platôs da tíbia no joelho.\nA alternativa B está errada: o fêmur não é osso laminar, possui apenas uma diáfise e duas epífises e não toca os ossos do tarso no pé.\nAs alternativas C e E estão erradas: o fêmur não é classificado como osso irregular, mas sim como osso longo clássico.\nA alternativa D está errada: afirma falsamente que o fêmur tem \"duas diáfises\" e que se articula diretamente com a fíbula (a fíbula não participa da articulação do joelho com o fêmur, apenas com a tíbia lateralmente)."
    }
]

fixacao_data = {
    "volume": "biologia/m05",
    "status": "PRONTO_PARA_REVISAO",
    "questoes": questoes,
    "ineditas": []
}

with open("content/material/biologia/m05/fixacao.json", "w", encoding="utf-8") as f:
    json.dump(fixacao_data, f, indent=1, ensure_ascii=False)

print("Saved content/material/biologia/m05/fixacao.json with 16 questions.")
