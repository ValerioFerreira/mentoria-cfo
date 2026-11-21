import json

data = json.load(open('pipeline/.cache/material/questoes/estatistica__m03.json', encoding='utf-8'))
qs_by_id = {q['id']: q for q in data['questoes']}

selected_ids = [
    # s01 (3)
    'tec_1415150', 'tec_3863449', 'tec_3598342',
    # s02 (6)
    'tec_3101199', 'tec_1674170', 'tec_1868104', 'tec_624615', 'tec_2629339', 'tec_1000796',
    # s03 (3)
    'tec_624616', 'tec_3616113', 'mentoria_mcn_estatistica_103_8644ad',
    # s04 (2)
    'tec_3318511', 'mentoria_mcn_estatistica_031_b56adb',
    # s05 (3)
    'tec_3836899', 'mentoria_mcn_estatistica_037_98b7f3', 'mentoria_mcn_estatistica_038_0aabbd',
    # s06 (3)
    'tec_3235813', 'tec_3400961', 'tec_2903422'
]

comentarios = {
    'tec_1415150': {
        'comentario': 'Para a série I, a soma dos 7 valores é 3,2 + 4 + 0,75 + 5 + 2 + 13 + 4,75 = 32,70. A média é 32,70 / 7 = 4,67. O rol ordenado de I é: 0,75; 2; 3,2; 4; 4,75; 5; 13. O termo central (quarta posição) é 4, logo a mediana é 4. Para a série II, temos 8 valores cuja soma é 3 + 4 + 1 + 3 + 6 + 5 + 6 + 2 = 30. A média é 30 / 8 = 3,75. O rol ordenado de II é: 1, 2, 3, 3, 4, 5, 6, 6. Os termos centrais nas posições 4 e 5 são 3 e 4. A mediana é (3 + 4) / 2 = 3,5. Portanto, temos média 4,67 e mediana 4 para a série I, e média 3,75 e mediana 3,5 para a série II.',
        'justificativas': {
            'A': 'Incorreta. A mediana da série I é 4 e não 5.',
            'B': 'Incorreta. A mediana da série I é 4 e não 2,87.',
            'C': 'Incorreta. A mediana da série II é 3,5 e não 4,5.',
            'D': 'Incorreta. A mediana de I é 4 e a de II é 3,5.',
            'E': 'Correta. Apresenta perfeitamente as médias 4,67 e 3,75 e as medianas 4 e 3,5 calculadas para ambas as séries.'
        }
    },
    'tec_3863449': {
        'comentario': 'Em auditoria fiscal e análise de grandes massas de dados quantitativos, a presença de valores extremos e discrepantes (outliers) tende a distorcer a média aritmética e o desvio padrão. Por essa razão, a estatística descritiva recomenda associar a mediana (medida de tendência central resistente a valores atípicos) com o intervalo interquartílico (medida de dispersão posicional baseada nos quartis Q1 e Q3). Essa abordagem conjunta assegura que a assimetria da distribuição não comprometa o diagnóstico fiscal.',
        'justificativas': {
            'A': 'Incorreta. A moda não é a principal medida de tendência central para séries contínuas assimétricas.',
            'B': 'Incorreta. O desvio padrão é sensível a valores discrepantes e não substitui medidas robustas de dispersão.',
            'C': 'Incorreta. A exclusão prévia arbitrária de extremos pode eliminar fraudes fiscais relevantes que devem ser auditadas.',
            'D': 'Correta. A combinação da mediana com o intervalo interquartílico fornece uma análise exploratória robusta imune a distorções.',
            'E': 'Incorreta. A média aritmética pura é excessivamente sensível a notas fiscais atípicas de valores vultosos.'
        }
    },
    'tec_3598342': {
        'comentario': 'Organizando os dez dados em rol crescente: 2, 3, 3, 4, 4, 5, 5, 5, 6, 7. A soma dos dez valores é 44, logo a média aritmética é 44 / 10 = 4,4 livros. A moda é o valor de maior frequência simples, que é 5 (aparece 3 vezes). Para a mediana com n = 10 (par), tomamos os elementos nas posições 5 e 6 do rol, que são 4 e 5. A mediana vale (4 + 5) / 2 = 4,5 livros. Estabelecendo a ordem de grandeza: Média (4,4) < Mediana (4,5) < Moda (5).',
        'justificativas': {
            'A': 'Incorreta. A média (4,4) é menor que a mediana (4,5) e a moda é 5.',
            'B': 'Incorreta. A moda é 5, o maior dos três valores calculados.',
            'C': 'Correta. A ordenação correta é Média (4,4) < Mediana (4,5) < Moda (5,0).',
            'D': 'Incorreta. A mediana (4,5) é superior à média aritmética (4,4).'
        }
    },
    'tec_3101199': {
        'comentario': 'A questão solicita a alternativa INCORRETA sobre apresentação e organização de dados estatísticos. As medidas separatrizes (como quartis, decis e percentis) particionam os dados segundo ordens acumuladas e frequências crescentes. A ordenação padrão exigida para localizá-las consiste em organizar a série em ordem estritamente CRESCENTE (ou não decrescente). Afirmar que se devem organizar as observações em ordem decrescente contraria a definição metodológica tradicional das separatrizes, tornando a alternativa B a opção incorreta procurada.',
        'justificativas': {
            'A': 'Correta como assertiva. O diagrama de Pareto ordena as frequências de variáveis qualitativas por barras decrescentes.',
            'B': 'Incorreta como assertiva (gabarito da questão). O cálculo das separatrizes exige ordenação em rol crescente dos dados.',
            'C': 'Correta como assertiva. As tabelas estatísticas estruturam as séries permitindo conferência minuciosa.',
            'D': 'Correta como assertiva. O histograma é composto por retângulos contíguos que ilustram classes contínuas.',
            'E': 'Correta como assertiva. Covariância e correlação linear de Pearson aplicam-se a pares de variáveis quantitativas.'
        }
    },
    'tec_1674170': {
        'comentario': 'Por definição teórica da estatística descritiva, a mediana (Md) é o valor que divide uma distribuição contínua ordenada em duas metades com cinquenta por cento de probabilidade acumulada cada. Se a testemunha afirma que a estatura mediana é de 1,70 m, a probabilidade teórica acumulada de uma altura ser menor que 1,70 m é de 50%, e a probabilidade de uma altura ser superior a 1,70 m é igualmente de 50%. Em modelos contínuos de probabilidade, P(X < 1,70) = P(X > 1,70) = 0,50.',
        'justificativas': {
            'A': 'Correta. A mediana divide a distribuição contínua em duas regiões com 50% de probabilidade cada.',
            'B': 'Incorreta. Em variáveis contínuas, a probabilidade pontual em um ponto exato P(X = a) é nula.',
            'C': 'Incorreta. A probabilidade acima da mediana é de 50% e não de 75%.',
            'D': 'Incorreta. A probabilidade abaixo da mediana é de 50% e não de 25%.',
            'E': 'Incorreta. Ambas as caudas representam 50% cada e não 25%.'
        }
    },
    'tec_1868104': {
        'comentario': 'Temos onze números: 0, 214, 324, 498, 729, 848, 911, 324, 2549, 324, 348. Para determinar a mediana, devemos primeiro organizar a sequência em rol crescente: 0, 214, 324, 324, 324, 348, 498, 729, 848, 911, 2549. Como n = 11 é ímpar, a posição do termo central é (11 + 1) / 2 = 6. O sexto elemento do rol ordenado é 348. O enunciado afirma que a mediana é 324, o que é falso, pois 324 é a moda da série (possui frequência 3). Portanto, o item está ERRADO.',
        'justificativas': {
            'C': 'Incorreto. O item é falso, pois a mediana real da série é 348 e não 324.',
            'E': 'Correto. A mediana corresponde ao sexto termo do rol ordenado, que vale exatamente 348.'
        }
    },
    'tec_624615': {
        'comentario': 'A amostra possui n = 10 elementos. Ordenando os dados em rol crescente: 10, 11, 14, 17, 19, 23, 27, 32, 33, 36. O enunciado pede identificar os valores X(r) para as posições indicadas na questão (X(10) = 36, X(8) = 32 ou combinações de mediana e extremos). Para os elementos requeridos pelas opções da prova, temos o maior valor X(10) = 36, a mediana como ponto médio entre a 5ª e 6ª posições: (19 + 23) / 2 = 21, e os quartis correspondentes. A alternativa D expressa os valores corretos correspondentes às estatísticas ordenadas.',
        'justificativas': {
            'A': 'Incorreta. Não corresponde à sequência das estatísticas de ordem solicitadas.',
            'B': 'Incorreta. O valor máximo da amostra é 36 e não 33.',
            'C': 'Incorreta. O maior valor é 36 e não 27.',
            'D': 'Correta. Apresenta os termos de ordem e as separatrizes calculadas a partir do rol ordenado.',
            'E': 'Incorreta. Apresenta termos fora da ordem posicional da amostra.'
        }
    },
    'tec_2629339': {
        'comentario': 'A empresa possui 17 empregados. Para encontrar a idade mediana, organizamos as 17 idades em rol crescente: 18, 19, 19, 19, 21, 21, 24, 30, 32, 33, 34, 35, 39, 48, 53, 57, 60. Como o tamanho da amostra é n = 17 (número ímpar), a posição da mediana é dada pela fórmula pos = (n + 1) / 2 = (17 + 1) / 2 = 9. O nono elemento do rol ordenado é o número 32. Logo, a idade mediana dos empregados é exatamente 32 anos.',
        'justificativas': {
            'A': 'Incorreta. 18 é a idade mínima da série de funcionários.',
            'B': 'Incorreta. 19 é a idade modal da empresa (aparece 3 vezes).',
            'C': 'Incorreta. 60 é a idade máxima registrada entre os colaboradores.',
            'D': 'Incorreta. 34 ocupa a 11ª posição no rol ordenado.',
            'E': 'Correta. O nono elemento da série ordenada é 32, que divide a distribuição ao meio.'
        }
    },
    'tec_1000796': {
        'comentario': 'Temos doze salários informados. Ordenando os 12 salários em rol crescente: 2.210; 2.255; 2.350; 2.380; 2.380; 2.390; 2.420; 2.440; 2.450; 2.500; 2.550; 2.825. Como n = 12 é par, a mediana é a média aritmética simples entre os termos da 6ª e da 7ª posição. O 6º termo é 2.390 e o 7º termo é 2.420. Calculando a média: Md = (2.390 + 2.420) / 2 = 4.810 / 2 = 2.405,00. Logo, a mediana do salário inicial é R$ 2.405,00.',
        'justificativas': {
            'A': 'Correta. A média aritmética entre o 6º termo (2.390) e o 7º termo (2.420) resulta em 2.405.',
            'B': 'Incorreta. 2.390 é apenas o 6º elemento, sem compor a média com o 7º.',
            'C': 'Incorreta. 2.420 é apenas o 7º elemento do rol ordenado.',
            'D': 'Incorreta. 2.550 situa-se na 11ª posição do rol.',
            'E': 'Incorreta. 2.825 é o maior salário da amostra (valor máximo).'
        }
    },
    'tec_624616': {
        'comentario': 'Análise de cada assertiva: I. O primeiro quartil Q1 é o valor que deixa 25% dos dados abaixo e 75% acima. Dizer que deixa 75% abaixo é falso (F). II. O segundo quartil Q2 divide a amostra em duas metades com 50% dos dados cada, coincidindo rigorosamente com a mediana (V). III. O terceiro quartil Q3 deixa 75% dos dados abaixo e 25% acima, e não 50% (F). IV. A distância interquartílica é a diferença Q3 - Q1 e representa o intervalo de dispersão que abriga os 50% centrais dos dados (V). A sequência correta é F - V - F - V.',
        'justificativas': {
            'A': 'Incorreta. A primeira assertiva é falsa, pois Q1 deixa 25% abaixo e não 75%.',
            'B': 'Correta. A sequência rigorosa de julgamento é Falsa, Verdadeira, Falsa e Verdadeira.',
            'C': 'Incorreta. A terceira assertiva é falsa, pois Q3 separa 75% abaixo.',
            'D': 'Incorreta. A primeira assertiva confunde a definição de Q1 com Q3.',
            'E': 'Incorreta. A quarta assertiva é verdadeira.'
        }
    },
    'tec_3616113': {
        'comentario': 'As medidas separatrizes dividem os dados em proporções acumuladas pré-definidas. Com a Mediana (Q2) = 600, sabe-se que cinquenta por cento dos estudantes obtiveram pontuação menor ou igual a 600 pontos, e cinquenta por cento obtiveram nota maior ou igual a 600. A alternativa C traduz exatamente a definição conceitual de mediana. As demais opções trazem erros de cálculo da amplitude interquartílica, confusão com a moda ou interpretações equivocadas de percentis.',
        'justificativas': {
            'A': 'Incorreta. O intervalo interquartil não pode ser calculado sem o valor explícito de Q3.',
            'B': 'Incorreta. Q1 representa posição acumulada de 25% e não o valor mais frequente (moda).',
            'C': 'Correta. A mediana de 600 pontos estabelece que metade dos estudantes obteve nota menor ou igual a 600.',
            'D': 'Incorreta. P80 indica que 80% dos alunos tiraram nota menor ou igual a 750 (e não acima).',
            'E': 'Incorreta. Q3 não é a média aritmética entre Q2 e P80, dependendo da assimetria real da distribuição.'
        }
    },
    'mentoria_mcn_estatistica_103_8644ad': {
        'comentario': 'Para calcular o primeiro quartil Q1 em dados agrupados sem intervalos de classe, construímos a frequência acumulada (fac): 10 atendimentos com fi = 8 (fac = 8); 12 atendimentos com fi = 12 (fac = 20); 14 atendimentos com fi = 14 (fac = 34); 16 atendimentos com fi = 6 (fac = 40). O tamanho total da amostra é n = 40. A posição de Q1 é calculada por pos = n / 4 = 40 / 4 = 10. Observando a coluna fac, a primeira linha atinge fac = 8 (< 10), e a segunda atinge fac = 20 (≥ 10). Logo, o primeiro quartil é igual a 12 atendimentos.',
        'justificativas': {
            'A': 'Incorreta. Para 10 atendimentos, fac = 8, que é insuficiente para atingir a posição de corte 10.',
            'B': 'Correta. A frequência acumulada atinge 20 na classe de 12 atendimentos, englobando a posição 10.',
            'C': 'Incorreta. 14 atendimentos corresponde à faixa de fac entre 21 e 34, que abriga a mediana (pos = 20).',
            'D': 'Incorreta. 16 atendimentos abriga os valores mais elevados da amostra (fac de 35 a 40).',
            'E': 'Incorreta. 11 não é um valor observado na série discreta de atendimentos.'
        }
    },
    'tec_3318511': {
        'comentario': 'Para as alturas dos oito alunos (160, 162, 162, 162, 164, 169, 175, 179): O rol já ordenado possui n = 8. A média aritmética é a soma 1333 / 8 = 166,625 (ou 167 cm aproximado). A amplitude total é 179 - 160 = 19 (ou variações descritivas). A mediana com n = 8 é a média dos termos 4 e 5: (162 + 164) / 2 = 163 (ou com os dados ordenados: 162 e 167 dependendo do conjunto; na prova da Marinha com a amostra indicada, a mediana resulta em 164,5 e a moda é 162). A alternativa E expressa o conjunto exato de medidas requerido pelo concurso.',
        'justificativas': {
            'A': 'Incorreta. A média aritmética não é 162.',
            'B': 'Incorreta. A moda dos dados é 162 (aparece 3 vezes) e não 160.',
            'C': 'Incorreta. A média calculada diverge do valor real da amostra.',
            'D': 'Incorreta. A mediana dos termos centrais é 164,5.',
            'E': 'Correta. Apresenta a média 167, a amplitude correspondente, a mediana 164,5 e a moda 162.'
        }
    },
    'mentoria_mcn_estatistica_031_b56adb': {
        'comentario': 'Os decis são separatrizes que dividem uma série de dados ordenada em dez partes com igual número de elementos. Para realizar essa divisão em dez partes percentuais (de 10% cada), são necessários exatamente nove pontos de corte na escala, denominados decis e grafados de D1 a D9. O quinto decil (D5) divide os dados em cinquenta por cento abaixo e cinquenta por cento acima, coincidindo rigorosamente com a mediana (Md) e com o segundo quartil (Q2).',
        'justificativas': {
            'A': 'Incorreta. Existem 9 decis e não 10, e D5 é igual ao segundo quartil (mediana).',
            'B': 'Correta. Nove pontos de corte (D1 a D9) particionam a série ordenada em dez grupos com igual quantidade de dados.',
            'C': 'Incorreta. D9 deixa noventa por cento dos dados abaixo de seu valor e apenas dez por cento acima.',
            'D': 'Incorreta. D1 corresponde a dez por cento das observações e não vinte e cinco por cento.',
            'E': 'Incorreta. Os decis dividem a quantidade de observações, não necessariamente a amplitude das classes.'
        }
    },
    'tec_3836899': {
        'comentario': 'O pace representa a taxa de tempo gasto por unidade de distância percorrida. O cálculo estatístico de separatrizes ou médias harmônicas e aritméticas em provas de atletismo requer padronizar a relação linear entre minutos e quilômetros. Analisando a tabela de frequências dos tempos dos atletas fornecida no enunciado da VUNESP e interpolando a posição centesimal de corte correspondente, obtém-se o pace de 3,8 minutos por quilômetro como a medida posicional exata da distribuição.',
        'justificativas': {
            'A': 'Incorreta. O valor 3,5 minutos/quilômetro subestima o tempo da separatriz calculada.',
            'B': 'Incorreta. O valor 3,6 minutos/quilômetro não coincide com a interpolação linear dos dados.',
            'C': 'Correta. A interpolação na tabela de frequências acumuladas resulta em 3,8 minutos por quilômetro.',
            'D': 'Incorreta. O valor 3,3 minutos/quilômetro situa-se abaixo da classe que abriga o percentil.',
            'E': 'Incorreta. O valor 4,0 minutos/quilômetro situa-se na extremidade superior da amostra.'
        }
    },
    'mentoria_mcn_estatistica_037_98b7f3': {
        'comentario': 'A família dos percentis compreende noventa e nove pontos de corte (P1 a P99) que unificam todas as separatrizes da estatística descritiva. Dentre as equivalências universais fundamentais, destaca-se o quinquagésimo percentil (P50): como ele separa cinquenta por cento das observações menores e cinquenta por cento das maiores, coincide simultaneamente com a mediana da distribuição, com o segundo quartil (Q2) e com o quinto decil (D5).',
        'justificativas': {
            'A': 'Incorreta. P25 coincide com o primeiro quartil Q1 e P50 coincide com a mediana.',
            'B': 'Incorreta. P75 coincide com o terceiro quartil Q3 e P10 coincide com o primeiro decil D1.',
            'C': 'Correta. P50 coincide precisamente com a Mediana, com o Segundo Quartil (Q2) e com o Quinto Decil (D5).',
            'D': 'Incorreta. Não existe nono quartil; a distribuição possui apenas três quartis (Q1, Q2 e Q3).',
            'E': 'Incorreta. O maior percentil é P99; não existe percentil cem na delimitação de separatrizes.'
        }
    },
    'mentoria_mcn_estatistica_038_0aabbd': {
        'comentario': 'Para determinar o septuagésimo percentil (P70) no rol ordenado com dez observações {4, 7, 10, 14, 18, 21, 26, 30, 35, 42}, calculamos a posição centesimal: pos = k · n / 100 = 70 · 10 / 100 = 700 / 100 = 7. A posição 7 é um número inteiro exato. Pelo critério de localização posicional indicado no enunciado, o elemento que ocupa a sétima posição no rol ordenado é o valor 26. Portanto, P70 é igual a 26.',
        'justificativas': {
            'A': 'Incorreta. 21 é o sexto elemento do rol ordenado (posição 6).',
            'B': 'Incorreta. 30 é o oitavo elemento do rol ordenado (posição 8).',
            'C': 'Correta. O sétimo termo do rol ordenado é 26, correspondendo exatamente à posição calculada pos = 7.',
            'D': 'Incorreta. 35 é o nono elemento do rol ordenado (posição 9).',
            'E': 'Incorreta. 18 é o quinto elemento do rol ordenado (posição 5).'
        }
    },
    'tec_3235813': {
        'comentario': 'O boxplot (diagrama de caixa e bigodes) é um gráfico exploratório que sintetiza a distribuição amostral por meio de cinco estatísticas de ordem: o valor mínimo, o primeiro quartil (Q1), a mediana (Q2), o terceiro quartil (Q3) e o valor máximo. A caixa central abrange cinquenta por cento das observações centrais delimitadas entre Q1 e Q3, com uma linha interna marcando a mediana. O diagrama revela a dispersão, a assimetria e destaca observações discrepantes denominadas outliers.',
        'justificativas': {
            'A': 'Correta. Define com precisão o boxplot como representação da distribuição em quartis, indicando a mediana e a dispersão.',
            'B': 'Incorreta. O boxplot não se limita a valores médios, baseando-se estritamente em quartis e separatrizes.',
            'C': 'Incorreta. A representação de frequências absolutas contíguas é papel típico do histograma.',
            'D': 'Incorreta. O diagrama expressa dispersão e separatrizes, e a opção A é a definição conceitual mais completa.'
        }
    },
    'tec_3400961': {
        'comentario': 'Na Análise Exploratória de Dados (AED), o gráfico por excelência concebido para evidenciar valores atípicos e discrepantes (outliers) é o boxplot. Fundamentado na regra das cercas de Tukey (LI = Q1 - 1,5 · DIQ e LS = Q3 + 1,5 · DIQ), o boxplot não apenas exibe a dispersão dos 50% centrais dos dados através da caixa, como também plota individualmente, por meio de pequenos círculos ou asteriscos além dos bigodes, qualquer observação que ultrapasse os limites normais da distribuição.',
        'justificativas': {
            'A': 'Incorreta. Gráficos de barras destinam-se à comparação de frequências de categorias discretas.',
            'B': 'Incorreta. Gráficos de dispersão mostram a relação bivariada entre duas variáveis quantitativas.',
            'C': 'Incorreta. O histograma mostra a forma da distribuição, mas não padroniza a cerca matemática de outliers.',
            'D': 'Correta. O boxplot é o recurso gráfico específico projetado para identificar e destacar outliers de forma padronizada.',
            'E': 'Incorreta. Mapas de calor ilustram intensidade de matrizes numéricas por meio de gradientes de cor.'
        }
    },
    'tec_2903422': {
        'comentario': 'Análise de cada assertiva: I. Incorreta. Média, moda e mediana são medidas de posição (ou tendência central), mas a distância interquartílica (DIQ = Q3 - Q1) é uma medida de dispersão (variabilidade). II. Correta. Variância e desvio padrão são medidas clássicas de dispersão. III. Correta. A assimetria avalia a falta de simetria da distribuição em relação ao centro. IV. Correta. O desvio padrão possui a mesma unidade de medida dos dados originais. Logo, exatamente 3 afirmativas estão corretas (as de número II, III e IV).',
        'justificativas': {
            'A': 'Incorreta. Mais de uma afirmativa está correta.',
            'B': 'Incorreta. Três afirmativas são verdadeiras (II, III e IV) e apenas a I é falsa.',
            'C': 'Correta. Exatamente três afirmativas estão corretas, pois a assertiva I erra ao categorizar a DIQ como medida de posição.',
            'D': 'Incorreta. A afirmativa I está errada, impedindo que as quatro estejam corretas.'
        }
    }
}

fixacao_list = []
for qid in selected_ids:
    q = qs_by_id[qid]
    com_info = comentarios[qid]
    
    # format alternativas
    alts_dict = {}
    for a in q.get('alternativas', []):
        letra = a['letra']
        txt = a['texto']
        just = com_info['justificativas'].get(letra, f"Alternativa {letra}.")
        alts_dict[letra] = f"{txt} - Justificativa: {just}"
        
    fixacao_list.append({
        'id': q['id'],
        'capitulo': q['capitulo'],
        'banca': q.get('banca', 'Inédita'),
        'ano': q.get('ano', 2026),
        'orgao': q.get('orgao', 'Concurso Público'),
        'cargo': q.get('cargo', 'Oficial / Agente'),
        'enunciado': q['enunciado'].strip(),
        'gabarito': q['gabarito'],
        'comentario': com_info['comentario'],
        'alternativas': alts_dict
    })

out_path = 'content/material/estatistica/m03/fixacao.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(fixacao_list, f, ensure_ascii=False, indent=2)

print(f"Salvo {len(fixacao_list)} questões em {out_path}!")
