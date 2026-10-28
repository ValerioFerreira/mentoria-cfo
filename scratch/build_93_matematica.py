# -*- coding: utf-8 -*-
"""Gerador e validador das 93 novas questões de Matemática para MentorIA / CFO-BM."""
import re
import sys
from pathlib import Path
from collections import Counter

# Lista com as 93 questões
# Cada item: (seg, gab, stem, [optA, optB, optC, optD, optE], comentario)
questions = [
    # --- a00/s01 (4 qs) ---
    (
        "a00/s01", "C",
        "Acerca da classificação dos números nos conjuntos numéricos fundamentais, assinale a opção correta.",
        [
            "Todo número com representação decimal infinita pertence necessariamente ao conjunto dos números irracionais.",
            "O número zero pertence ao conjunto dos números inteiros, mas não pertence ao conjunto dos números racionais.",
            "A dízima periódica 0,777... é um número racional porque pode ser expressa como a razão 7/9 entre dois inteiros.",
            "A raiz quadrada de qualquer número natural resulta sempre em um número racional.",
            "O número pi (π) é um número racional com representação decimal exata.",
        ],
        "A dízima periódica simples 0,777... possui período 7 e fração geratriz 7/9. Como pode ser escrita como a razão entre dois números inteiros com denominador não nulo, classifica-se como número racional. Em contrapartida, números com expansão decimal infinita e não periódica, como pi e raízes de inteiros que não são quadrados perfeitos, integram os irracionais, enquanto o zero é inteiro e racional (0/1)."
    ),
    (
        "a00/s01", "B",
        "A respeito das operações envolvendo números racionais e irracionais no conjunto dos números reais, assinale a opção correta.",
        [
            "A soma de dois números irracionais quaisquer resulta obrigatoriamente em um número irracional.",
            "A soma entre um número racional qualquer e um número irracional resulta sempre em um número irracional.",
            "O produto de dois números irracionais quaisquer nunca pode resultar em um número racional.",
            "O conjunto dos números irracionais é fechado para a operação de multiplicação.",
            "O quociente entre dois números irracionais resulta invariavelmente em um número irracional.",
        ],
        "A soma de um número racional com um número irracional é invariavelmente um número irracional, pois se a soma resultasse racional, a subtração entre dois racionais exigiria que o número original fosse racional, o que gera contradição lógica. Já as operações entre dois irracionais não possuem fechamento, pois a soma de opostos como raiz de dois e menos raiz de dois resulta em zero (racional), e o produto de raiz de dois por raiz de dois resulta em dois (racional)."
    ),
    (
        "a00/s01", "A",
        "Ao converter a dízima periódica simples 0,454545... em uma fração irredutível da forma a/b, obtêm-se dois inteiros positivos a e b. Em relação a essa fração geratriz, assinale a opção correta.",
        [
            "A soma do numerador a com o denominador b da fração irredutível é igual a 16.",
            "A fração irredutível que gera a referida dízima periódica é igual a 45/100.",
            "O denominador b da fração irredutível corresponde ao número primo 13.",
            "A soma do numerador a com o denominador b da fração irredutível é igual a 20.",
            "O numerador a da fração irredutível obtida é um número par maior do que 8.",
        ],
        "Para obter a fração geratriz de 0,454545..., define-se x = 0,454545... e multiplica-se por 100: 100x = 45,454545... Subtraindo as duas equações: 100x − x = 45 ⇒ 99x = 45 ⇒ x = 45/99. Simplificando por 9 numerador e denominador, obtém-se a fração irredutível 5/11. A soma pedida é a + b = 5 + 11 = 16. A razão 45/100 corresponde ao decimal exato 0,45, que difere da dízima infinita periódica."
    ),
    (
        "a00/s01", "C",
        "No que se refere às relações de inclusão e às operações entre os conjuntos numéricos N, Z, Q, I e R, assinale a opção correta.",
        [
            "A interseção entre o conjunto dos números racionais Q e o conjunto dos números irracionais I é não vazia.",
            "O conjunto dos números reais R é formado pela diferença entre os números inteiros Z e os naturais N.",
            "O conjunto dos números racionais Q e o conjunto dos números irracionais I são disjuntos e sua união é o conjunto dos números reais R.",
            "Todo número pertencente ao conjunto dos inteiros Z é também um número irracional.",
            "O conjunto dos números naturais N não está contido no conjunto dos números inteiros Z.",
        ],
        "Os números reais R são formados pela união disjunta dos racionais Q e dos irracionais I, ou seja, a união de ambos resulta em R e a interseção entre eles é o conjunto vazio. Além disso, todo número natural é também inteiro, e todo inteiro é racional, não existindo elementos que pertençam simultaneamente a Q e a I."
    ),

    # --- a00/s02 (5 qs) ---
    (
        "a00/s02", "A",
        "Considerando a unidade imaginária i tal que i² = −1, assinale a opção que indica o valor da potência i³⁷.",
        [
            "i",
            "−1",
            "1",
            "−i",
            "0",
        ],
        "As potências da unidade imaginária i repetem-se em ciclos de quatro expoentes inteiros positivos: i⁰ = 1, i¹ = i, i² = −1 e i³ = −i. Dividindo 37 por 4, encontra-se quociente 9 e resto 1 (37 = 4 × 9 + 1). Portanto, i³⁷ = i¹ = i. Valores como −1, 1 ou −i decorrem de divisões com restos 2, 0 ou 3, respectivamente."
    ),
    (
        "a00/s02", "A",
        "Seja o número complexo z = 4 − 3i, em que i é a unidade imaginária. A respeito da parte real, da parte imaginária e do conjugado de z, assinale a opção correta.",
        [
            "A parte real de z é 4, sua parte imaginária é −3 e seu conjugado é dado por 4 + 3i.",
            "A parte real de z é −3, sua parte imaginária é 4 e seu conjugado é dado por −4 − 3i.",
            "O conjugado de z é igual a −4 + 3i e sua parte imaginária corresponde a −3i.",
            "A parte real de z é 4 e seu conjugado é dado pelo número complexo −4 − 3i.",
            "A parte imaginária de z é 3 e o seu conjugado coincide com o próprio número z.",
        ],
        "Na representação z = a + bi, o número real a é a parte real e o número real b é a parte imaginária. Para z = 4 − 3i, a parte real é 4 e a parte imaginária é −3. O conjugado de z inverte unicamente o sinal da parte imaginária, resultando em 4 + 3i. Confusões usuais ocorrem ao anexar a letra i à parte imaginária ou trocar o sinal da parte real."
    ),
    (
        "a00/s02", "B",
        "Um perito em telecomunicações analisou a impedância de um circuito representada pelo número complexo z = 6 + 8i, em ohms. Assinale a opção que indica o módulo |z| desse número complexo.",
        [
            "14",
            "10",
            "48",
            "100",
            "2",
        ],
        "O módulo de um número complexo z = a + bi é a distância euclidiana da origem ao afixo no plano complexo: |z| = raiz quadrada de (a² + b²). Substituindo: |z| = raiz quadrada de (6² + 8²) = raiz quadrada de (36 + 64) = raiz quadrada de 100 = 10. O valor 14 advém da soma aritmética direta de 6 com 8, enquanto 100 corresponde ao módulo elevado ao quadrado."
    ),
    (
        "a00/s02", "A",
        "Considere os números complexos z₁ = 2 + 3i e z₂ = 1 − 2i. A respeito do produto z₁ · z₂, assinale a opção correta.",
        [
            "O produto z₁ · z₂ é igual a 8 − i.",
            "O produto z₁ · z₂ é igual a 2 − 6i.",
            "O produto z₁ · z₂ é igual a −4 − i.",
            "O produto z₁ · z₂ é igual a 8 + 7i.",
            "O produto z₁ · z₂ é igual a −4 + 5i.",
        ],
        "Multiplicando os números complexos pela propriedade distributiva: (2 + 3i)(1 − 2i) = 2 − 4i + 3i − 6i². Como i² = −1, temos 2 − i − 6(−1) = 2 − i + 6 = 8 − i. O valor 2 − 6i decorre da multiplicação direta e incorreta de termos semelhantes sem aplicação da propriedade distributiva completa."
    ),
    (
        "a00/s02", "E",
        "Ao efetuar a divisão do número complexo z₁ = 5 + 5i pelo número complexo z₂ = 1 + 2i, obtém-se um novo número complexo. Assinale a opção que apresenta o resultado correto dessa divisão.",
        [
            "5 + 2,5i",
            "1 + 3i",
            "4 − i",
            "2 + 4i",
            "3 − i",
        ],
        "Para realizar a divisão, multiplicam-se o numerador e o denominador pelo conjugado do denominador (1 − 2i): numerador (5 + 5i)(1 − 2i) = 5 − 10i + 5i − 10i² = 5 − 5i + 10 = 15 − 5i; denominador (1 + 2i)(1 − 2i) = 1² + 2² = 5. Dividindo cada termo por 5 obtém-se 15/5 − (5/5)i = 3 − i. Divisões isoladas de partes reais e imaginárias desrespeitam a álgebra dos complexos."
    ),

    # --- a01/s02 (5 qs) ---
    (
        "a01/s02", "E",
        "Em uma divisão euclidiana de números inteiros positivos, o divisor é igual a 14, o quociente é igual a 25 e o resto é o maior possível. Assinale a opção que indica o valor do dividendo dessa operação.",
        [
            "350",
            "364",
            "377",
            "359",
            "363",
        ],
        "Na divisão de números inteiros, o resto deve satisfazer 0 ≤ resto < divisor. Se o divisor é 14, o maior resto possível é 13. Pela relação fundamental da divisão, Dividendo = (divisor × quociente) + resto. Logo: D = (14 × 25) + 13 = 350 + 13 = 363. O valor 350 desconsidera a presença do resto, enquanto 364 atribui erroneamente resto igual ao divisor."
    ),
    (
        "a01/s02", "A",
        "A respeito das propriedades estruturais da multiplicação no conjunto dos números reais, assinale a opção correta.",
        [
            "O número 1 é o elemento neutro da multiplicação e o número 0 atua como elemento nulo.",
            "A propriedade distributiva da multiplicação é válida apenas em relação à adição, não se aplicando à subtração.",
            "A multiplicação de números reais não atende à propriedade associativa quando há mais de três fatores.",
            "O elemento neutro da multiplicação é o número 0, pois a multiplicação por zero preserva o valor original.",
            "A inversão da ordem dos fatores altera o produto final em multiplicações com números decimais.",
        ],
        "O número 1 é o elemento neutro da multiplicação porque qualquer número multiplicado por 1 permanece inalterado (a × 1 = a). O zero é o elemento nulo, pois anula qualquer multiplicação (a × 0 = 0). A multiplicação é sempre comutativa e associativa no conjunto dos reais, e a distributiva aplica-se tanto à adição quanto à subtração."
    ),
    (
        "a01/s02", "A",
        "Um técnico em criminalística mediu a largura e o comprimento de uma mancha retangular no piso, encontrando 1,25 metro e 0,84 metro. Assinale a opção que indica a área dessa mancha em metros quadrados.",
        [
            "1,05 m²",
            "10,5 m²",
            "0,105 m²",
            "1,20 m²",
            "0,95 m²",
        ],
        "A área do retângulo é dada pelo produto do comprimento pela largura: 1,25 × 0,84. Multiplicando os números como inteiros: 125 × 84 = 10.500. Como há duas casas decimais no primeiro fator e duas no segundo, o produto deve conter quatro casas decimais: 1,0500 m² = 1,05 m². Resultados como 10,5 ou 0,105 derivam de contagem equivocada de casas decimais."
    ),
    (
        "a01/s02", "C",
        "Uma corporação militar precisa transportar 218 novos soldados para um curso de formação utilizando ônibus com capacidade para 45 passageiros sentados cada um. Assinale a opção que indica o número mínimo de ônibus necessários para transportar todos os soldados sentados.",
        [
            "4 ônibus.",
            "6 ônibus.",
            "5 ônibus.",
            "7 ônibus.",
            "3 ônibus.",
        ],
        "Dividindo 218 por 45 passageiros: 218 = 45 × 4 + 38. Quatro ônibus acomodam 180 soldados, restando 38 pessoas sem assento. Para que todos viajem sentados, é necessário adicionar mais um ônibus para transportar os 38 soldados restantes, totalizando 4 + 1 = 5 veículos. Quatro ônibus seriam insuficientes para acomodar todo o contingente."
    ),
    (
        "a01/s02", "E",
        "Um batalhão adquiriu um fardo contendo 24 lanternas táticas pelo valor total de R$ 1.860,00. Assinale a opção que indica o preço unitário de cada lanterna.",
        [
            "R$ 72,50",
            "R$ 82,00",
            "R$ 75,00",
            "R$ 78,50",
            "R$ 77,50",
        ],
        "O preço unitário é obtido pela divisão do montante total pela quantidade adquirida: 1.860 ÷ 24. Efetuando a divisão: 1.860 ÷ 24 = 77 com resto 12. Acrescentando a vírgula e zero decimal: 120 ÷ 24 = 5. O quociente exato é R$ 77,50 por lanterna. Valores diferentes resultam de erros na divisão decimal."
    ),

    # --- a01/s04 (4 qs) ---
    (
        "a01/s04", "B",
        "Ao realizar uma apuração pericial, calculou-se o valor numérico da expressão E = 50 − 2 · [18 − (3² + 5)]. Assinale a opção que indica o valor correto de E.",
        [
            "36",
            "42",
            "48",
            "24",
            "56",
        ],
        "Obedecendo à ordem de precedência: primeiro calcula-se a potência e os parênteses: 3² + 5 = 9 + 5 = 14. Em seguida, os colchetes: 18 − 14 = 4. Posteriormente, a multiplicação antes da subtração: 2 · 4 = 8. Por fim, subtrai-se: 50 − 8 = 42. Subtrair 50 − 2 antes de multiplicar violaria a ordem das operações aritméticas."
    ),
    (
        "a01/s04", "B",
        "Em relação aos produtos notáveis no conjunto dos números reais, assinale a opção correta.",
        [
            "A expressão (x − 3)² desenvolve-se algebricamente como x² − 9.",
            "A expressão (2x + 5)² desenvolve-se algebricamente como 4x² + 20x + 25.",
            "A expressão (x + y)² é numericamente equivalente a x² + y² para quaisquer valores de x e y.",
            "O desenvolvimento de (3x − 1)² resulta em 9x² − 3x + 1.",
            "A expressão (a − b)² é sempre igual a −(a + b)².",
        ],
        "O quadrado da soma de dois termos segue a identidade algébrica (a + b)² = a² + 2ab + b². Desenvolvendo (2x + 5)²: (2x)² + 2 · (2x) · 5 + 5² = 4x² + 20x + 25. Omitir o termo intermediário duas vezes o primeiro pelo segundo conduz a erros comuns como supor que o expoente se distribui na adição."
    ),
    (
        "a01/s04", "C",
        "Ao simplificar a expressão numérica P = (105)² − (95)², um analista utilizou a fatoração pelo produto da soma pela diferença de dois termos. Assinale a opção que indica o valor correto de P.",
        [
            "1.000",
            "1.500",
            "2.000",
            "2.500",
            "400",
        ],
        "A diferença entre dois quadrados pode ser fatorada como o produto da soma pela diferença: a² − b² = (a + b)(a − b). Fazendo a = 105 e b = 95: (105 + 95) · (105 − 95) = 200 · 10 = 2.000. Essa fatoração fornece o resultado sem a necessidade de calcular as potências elevadas 11.025 e 9.025."
    ),
    (
        "a01/s04", "D",
        "A respeito do desenvolvimento algébrico do cubo da soma e do cubo da diferença de dois termos reais, assinale a opção correta.",
        [
            "A expressão (x + 2)³ desenvolve-se algebricamente como x³ + 8.",
            "A expressão (x − 1)³ desenvolve-se algebricamente como x³ − 3x² − 3x − 1.",
            "O desenvolvimento de (a + b)³ contém exatamente três termos algébricos.",
            "O desenvolvimento de (x + 1)³ é dado pelo polinômio x³ + 3x² + 3x + 1.",
            "A expressão (x − y)³ é idêntica a x³ − y³ para quaisquer números reais x e y.",
        ],
        "O cubo da soma obedece à fórmula (a + b)³ = a³ + 3a²b + 3ab² + b³. Para (x + 1)³: x³ + 3·x²·1 + 3·x·1² + 1³ = x³ + 3x² + 3x + 1, resultando em um polinômio com quatro termos. Omitir os termos centrais do binômio desconsidera as regras de potenciação de polinômios."
    ),

    # --- a02/s01 (3 qs) ---
    (
        "a02/s01", "B",
        "Uma cerca de segurança de uma penitenciária possui comprimento total de 3,45 quilômetros. Assinale a opção que apresenta essa medida convertida para metros.",
        [
            "345 metros.",
            "3.450 metros.",
            "34.500 metros.",
            "34,5 metros.",
            "0,345 metro.",
        ],
        "No sistema métrico decimal, 1 quilômetro equivale a 1.000 metros (1 km = 1.000 m). Para converter quilômetros em metros, multiplica-se a extensão por 1.000, deslocando a vírgula três ordens para a direita: 3,45 × 1.000 = 3.450 metros. Valores como 345 ou 34.500 decorrem de potências incorretas de base dez."
    ),
    (
        "a02/s01", "C",
        "Durante uma operação policial, foram apreendidas 2,8 toneladas de uma substância ilícita. Assinale a opção que indica essa mesma massa expressa em quilogramas.",
        [
            "280 kg",
            "28.000 kg",
            "2.800 kg",
            "28 kg",
            "280.000 kg",
        ],
        "A tonelada é uma unidade de massa equivalente a exatamente 1.000 quilogramas (1 t = 1.000 kg). Para converter toneladas para quilogramas, multiplica-se o valor por mil: 2,8 × 1.000 = 2.800 kg. Resultados como 280 kg ou 28.000 kg provêm de conversões com fatores 100 ou 10.000."
    ),
    (
        "a02/s01", "E",
        "A distância percorrida por um feixe de luz em determinado experimento foi registrada como 450.000.000 de metros. Assinale a opção que expressa corretamente essa medida em notação científica.",
        [
            "45 × 10⁷ m",
            "4,5 × 10⁶ m",
            "0,45 × 10⁹ m",
            "4,5 × 10⁷ m",
            "4,5 × 10⁸ m",
        ],
        "A notação científica requer a forma N × 10ⁿ com 1 ≤ N < 10. No número 450.000.000, desloca-se a vírgula 8 posições à esquerda até atingir 4,5, gerando o expoente 8: 4,5 × 10⁸ m. Formatos como 45 × 10⁷ ou 0,45 × 10⁹ não satisfazem o intervalo padrão para o coeficiente N."
    ),

    # --- a02/s02 (1 q) ---
    (
        "a02/s02", "C",
        "Uma caixa-d'água de formato cúbico possui capacidade interna para armazenar 8.000 litros de água. Assinale a opção que indica o volume interno dessa caixa em metros cúbicos.",
        [
            "80 m³",
            "0,8 m³",
            "8 m³",
            "800 m³",
            "0,08 m³",
        ],
        "A relação de equivalência entre volume e capacidade do sistema métrico define que 1 metro cúbico equivale a 1.000 litros (1 m³ = 1.000 L). Dividindo a capacidade em litros por 1.000: 8.000 ÷ 1.000 = 8 m³. Valores como 80 m³ ou 0,8 m³ correspondem a divisões por fatores 100 ou 10.000."
    ),

    # --- a03/s03 (1 q) ---
    (
        "a03/s03", "A",
        "Ao converter a dízima periódica composta 0,1666... em sua fração geratriz irredutível, obtém-se uma razão entre dois números inteiros. Assinale a opção que indica essa fração.",
        [
            "1/6",
            "1/5",
            "2/15",
            "1/3",
            "5/33",
        ],
        "A dízima periódica composta 0,1666... possui anteperíodo 1 e período 6. Pelo método algébrico: x = 0,1666..., logo 10x = 1,666... e 100x = 16,666... Subtraindo: 100x − 10x = 15 ⇒ 90x = 15 ⇒ x = 15/90. Dividindo numerador e denominador por 15, obtém-se a fração irredutível 1/6. Frações como 1/5 equivalem a 0,2 e 1/3 equivale a 0,333..."
    ),

    # --- a03/s04 (4 qs) ---
    (
        "a03/s04", "B",
        "Em um concurso público para a polícia civil, inscreveram-se 1.200 candidatos para concorrer a 40 vagas disponíveis. Assinale a opção que indica a razão candidato por vaga desse certame.",
        [
            "25 candidatos por vaga.",
            "30 candidatos por vaga.",
            "40 candidatos por vaga.",
            "35 candidatos por vaga.",
            "20 candidatos por vaga.",
        ],
        "A razão entre o número de candidatos inscritos e o total de vagas ofertadas é dada pela divisão do antecedente pelo consequente: 1.200 ÷ 40 = 30 candidatos por vaga. As demais alternativas apresentam valores que não correspondem à divisão exata dos dados fornecidos."
    ),
    (
        "a03/s04", "D",
        "Na proporção x / 15 = 8 / 20, o valor da incógnita x satisfaz à propriedade fundamental das proporções. Assinale a opção que indica o valor correto de x.",
        [
            "10",
            "8",
            "4",
            "6",
            "12",
        ],
        "Pela propriedade fundamental das proporções, o produto dos extremos é igual ao produto dos meios: 20 · x = 15 · 8 ⇒ 20x = 120 ⇒ x = 120 ÷ 20 = 6. De forma alternativa, simplificando 8/20 para 2/5, tem-se x = 15 · (2/5) = 6. Valores divergentes violam a igualdade entre as razões."
    ),
    (
        "a03/s04", "D",
        "Dois policiais atenderam juntos 72 ocorrências em um plantão. Sabendo que a razão entre o número de ocorrências atendidas pelo primeiro policial e pelo segundo policial é de 5 para 3, assinale a opção que indica quantas ocorrências foram atendidas pelo primeiro policial.",
        [
            "40 ocorrências.",
            "36 ocorrências.",
            "48 ocorrências.",
            "45 ocorrências.",
            "27 ocorrências.",
        ],
        "A soma das partes proporcionais é 5 + 3 = 8 partes. Cada parte unitária equivale a k = 72 ÷ 8 = 9 ocorrências. O primeiro policial foi responsável por 5 partes: 5 × 9 = 45 ocorrências (enquanto o segundo atendeu 3 × 9 = 27 ocorrências). Quantidades como 40 ou 48 não preservam a razão 5/3."
    ),
    (
        "a03/s04", "E",
        "Em uma delegacia, a razão entre o número de agentes homens e mulheres é de 7 para 4. Se nessa delegacia há 18 homens a mais do que mulheres, assinale a opção que indica o número total de agentes policiais da unidade.",
        [
            "54 agentes.",
            "60 agentes.",
            "72 agentes.",
            "48 agentes.",
            "66 agentes.",
        ],
        "Representando a quantidade de homens por 7k e de mulheres por 4k, a diferença informada é 7k − 4k = 3k. Como há 18 homens a mais: 3k = 18 ⇒ k = 6. O efetivo total da delegacia é a soma dos grupos: 7k + 4k = 11k = 11 × 6 = 66 agentes (sendo 42 homens e 24 mulheres). Totais diferentes não satisfazem a diferença de 18 indivíduos."
    ),

    # --- a03/s05 (4 qs) ---
    (
        "a03/s05", "B",
        "Em um mapa elaborado na escala 1 : 250.000, a distância em linha reta entre dois postos de fiscalização é de 8 centímetros. Assinale a opção que indica a distância real entre esses dois postos em quilômetros.",
        [
            "25 km",
            "20 km",
            "16 km",
            "32 km",
            "2 km",
        ],
        "Na escala 1 : 250.000, 1 cm no mapa corresponde a 250.000 cm reais. Multiplicando: 8 × 250.000 cm = 2.000.000 cm. Como 1 km = 100.000 cm, converte-se dividindo por 100.000: 2.000.000 ÷ 100.000 = 20 km. Respostas como 25 km ou 2 km provêm de fatores de conversão métrica equivocados."
    ),
    (
        "a03/s05", "B",
        "Uma viatura da polícia rodoviária percorreu um trecho de 180 quilômetros de rodovia em exatamente 2 horas e 30 minutos. Assinale a opção que indica a velocidade média dessa viatura ao longo do percurso.",
        [
            "80 km/h",
            "72 km/h",
            "65 km/h",
            "90 km/h",
            "60 km/h",
        ],
        "A velocidade média é a razão entre a distância percorrida e o tempo gasto: Vm = Δs / Δt. Duas horas e trinta minutos correspondem a 2,5 horas (pois 30 minutos equivalem a meia hora). Calculando: 180 ÷ 2,5 = 72 km/h. Tomar erroneamente 2h30min como 2,3 horas geraria um cálculo distorcido."
    ),
    (
        "a03/s05", "A",
        "Uma motobomba de combate a incêndio possui vazão constante de 150 litros por minuto. Assinale a opção que indica o tempo necessário para essa bomba encher completamente um tanque com capacidade de 9.000 litros.",
        [
            "60 minutos.",
            "45 minutos.",
            "75 minutos.",
            "90 minutos.",
            "50 minutos.",
        ],
        "A vazão é a razão Q = Volume ÷ tempo, donde tempo = Volume ÷ Vazão. Substituindo os valores da operação: tempo = 9.000 ÷ 150 = 60 minutos (equivalente a 1 hora de bombeamento). Tempos diferentes não correspondem à taxa contínua de 150 litros por minuto."
    ),
    (
        "a03/s05", "D",
        "Um reservatório pode ser completamente abastecido pela bomba Alfa em 3 horas ou pela bomba Beta em 6 horas. Se ambas as bombas forem ligadas simultaneamente, assinale a opção que indica em quanto tempo o reservatório estará cheio.",
        [
            "4,5 horas.",
            "1,5 hora.",
            "3 horas.",
            "2 horas.",
            "2,5 horas.",
        ],
        "Trabalhando simultaneamente, somam-se as taxas horárias: a bomba Alfa enche 1/3 do reservatório por hora e a Beta enche 1/6. Soma: 1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2 do tanque por hora. O tempo para completar o volume total é o inverso dessa taxa: 1 ÷ (1/2) = 2 horas. A média simples (3 + 6) / 2 = 4,5 horas ignora a natureza inversa da vazão."
    ),

    # --- a04/s01 (1 q) ---
    (
        "a04/s01", "C",
        "Em uma gráfica da polícia, 8 impressoras de mesmo rendimento imprimem 12.000 cartilhas trabalhando 6 horas por dia durante 5 dias. Para imprimir 16.000 cartilhas idênticas em 4 dias, operando as mesmas 8 impressoras, assinale a opção que indica quantas horas por dia as impressoras deverão trabalhar.",
        [
            "8 horas por dia.",
            "7 horas por dia.",
            "10 horas por dia.",
            "9 horas por dia.",
            "12 horas por dia.",
        ],
        "Fixando o número de impressoras, a carga horária diária é diretamente proporcional à produção de cartilhas e inversamente proporcional ao total de dias: x / 6 = (16.000 / 12.000) × (5 / 4) = (4/3) × (5/4) = 5/3 ⇒ x = 6 × (5/3) = 10 horas diárias. Jornadas de 8 ou 12 horas desconsideram as proporções diretas e inversas do processo."
    ),

    # --- a05/s01 (2 qs) ---
    (
        "a05/s01", "D",
        "Em uma operação de trânsito foram fiscalizados 650 veículos. Constatou-se que 18% desses veículos apresentavam alguma irregularidade documental. Assinale a opção que indica o número de veículos irregulares identificados.",
        [
            "108 veículos.",
            "125 veículos.",
            "130 veículos.",
            "117 veículos.",
            "98 veículos.",
        ],
        "Para calcular 18% de 650, multiplica-se a taxa decimal pela quantidade total de veículos: 0,18 × 650 = 117 veículos. De forma decomposta: 10% de 650 é 65, e 8% é 52; 65 + 52 = 117. Contagens divergentes decorrem de erros na multiplicação de decimais."
    ),
    (
        "a05/s01", "B",
        "Ao analisar a taxa de resolução de inquéritos, um delegado observou que 7 em cada 20 procedimentos instaurados foram concluídos no prazo regulamentar. Assinale a opção que expressa essa proporção na forma percentual.",
        [
            "30%",
            "35%",
            "28%",
            "40%",
            "32%",
        ],
        "A fração 7/20 pode ser convertida diretamente multiplicando numerador e denominador por 5 para que a base se torne cem: (7 × 5) / (20 × 5) = 35/100 = 35%. Alternativamente, divide-se 7 por 20 obtendo 0,35, que equivale a 35%. Valores como 28% ou 30% provêm de estimativas inexatas."
    ),

    # --- a05/s02 (5 qs) ---
    (
        "a05/s02", "C",
        "Um equipamento tático que custava R$ 2.400,00 sofreu um reajuste de preço com aumento de 15%. Assinale a opção que indica o novo preço desse equipamento após o aumento.",
        [
            "R$ 2.640,00",
            "R$ 2.700,00",
            "R$ 2.760,00",
            "R$ 2.800,00",
            "R$ 2.850,00",
        ],
        "O fator de aumento correspondente a 15% é (1 + 0,15) = 1,15. Multiplicando pelo preço inicial: 2.400 × 1,15 = R$ 2.760,00. Calculando o acréscimo isoladamente: 15% de 2.400 = 360 reais; somando ao valor original: 2.400 + 360 = 2.760 reais. Preços como R$ 2.700,00 aplicam taxas incorretas."
    ),
    (
        "a05/s02", "B",
        "Uma compra de coletes balísticos no valor de R$ 18.000,00 foi paga à vista com a concessão de um desconto de 12%. Assinale a opção que indica o valor efetivamente pago pela corporação após o desconto.",
        [
            "R$ 16.200,00",
            "R$ 15.840,00",
            "R$ 15.600,00",
            "R$ 16.000,00",
            "R$ 14.840,00",
        ],
        "O fator de desconto para 12% é (1 − 0,12) = 0,88. Multiplicando: 18.000 × 0,88 = R$ 15.840,00. Pelo cálculo da redução: 12% de 18.000 = 2.160 reais; subtraindo: 18.000 − 2.160 = 15.840 reais. Montantes como R$ 16.200,00 aplicam taxa de 10% em vez dos 12% estabelecidos."
    ),
    (
        "a05/s02", "D",
        "Após um reajuste salarial de 8%, a remuneração de um perito criminal passou a ser de R$ 8.640,00. Assinale a opção que indica o valor da remuneração desse perito antes do reajuste.",
        [
            "R$ 7.948,80",
            "R$ 8.200,00",
            "R$ 7.800,00",
            "R$ 8.000,00",
            "R$ 8.100,00",
        ],
        "O valor final é obtido por Salário_inicial × 1,08 = 8.640. Para reencontrar o salário inicial, divide-se o montante pelo fator de aumento: 8.640 ÷ 1,08 = R$ 8.000,00. Subtrair 8% do valor final de 8.640 resultaria erroneamente em 7.948,80, pois a porcentagem incidiu originalmente sobre a base menor anterior."
    ),
    (
        "a05/s02", "D",
        "Com a aplicação de um desconto de 20% para pagamento à vista, uma arma de treinamento foi adquirida por R$ 1.440,00. Assinale a opção que indica o preço original dessa arma sem o desconto.",
        [
            "R$ 1.728,00",
            "R$ 1.600,00",
            "R$ 1.750,00",
            "R$ 1.800,00",
            "R$ 1.900,00",
        ],
        "Sendo o desconto de 20%, o valor pago representa 80% do preço inicial (fator 0,80): Preço_inicial × 0,80 = 1.440 ⇒ Preço_inicial = 1.440 ÷ 0,80 = R$ 1.800,00. Somar 20% a 1.440 daria erroneamente 1.728, desconsiderando que a base de cálculo do abatimento foi o preço bruto original."
    ),
    (
        "a05/s02", "C",
        "Em relação aos conceitos de aumentos e descontos percentuais e seus respectivos fatores de multiplicação, assinale a opção correta.",
        [
            "Aplicar um desconto de 25% equivale a multiplicar o valor original pelo fator 0,85.",
            "Para conceder um aumento de 30%, deve-se multiplicar o valor original pelo fator 0,30.",
            "Um acréscimo de 18% sobre determinado valor corresponde a multiplicá-lo pelo fator 1,18.",
            "Retirar um desconto de 10% sobre um preço que já havia sido reduzido em 10% restabelece o preço original.",
            "O fator multiplicativo correspondente a um desconto de 5% é dado pelo número decimal 0,50.",
        ],
        "Um aumento percentual de taxa i é representado pelo fator multiplicativo (1 + i). Para uma taxa de 18% (0,18), o fator é 1 + 0,18 = 1,18. Desconto de 25% usa fator 0,75; aumento de 30% usa 1,30; desconto de 5% usa fator 0,95; e aumentos e reduções sucessivos não se anulam pela mesma taxa nominal."
    ),

    # --- a05/s03 (5 qs) ---
    (
        "a05/s03", "D",
        "O número de homicídios registrados em determinada região caiu de 250 casos em 2024 para 190 casos em 2025. Assinale a opção que indica a variação percentual do número de homicídios no período analisado.",
        [
            "Redução de 20%",
            "Redução de 30%",
            "Redução de 25%",
            "Redução de 24%",
            "Redução de 18%",
        ],
        "A taxa de variação percentual é a diferença entre o valor final e o inicial dividida pelo valor inicial: (190 − 250) ÷ 250 = −60 ÷ 250 = −0,24, o que corresponde a uma redução de 24%. Dividir 60 pela base errada de 190 geraria 31,5%, violando a definição de variação sobre a base temporal inicial."
    ),
    (
        "a05/s03", "D",
        "A verba de custeio de uma delegacia teve dois aumentos sucessivos: o primeiro de 10% e o segundo de 20%. Assinale a opção que indica o aumento percentual acumulado sobre a verba inicial.",
        [
            "30%",
            "28%",
            "35%",
            "32%",
            "22%",
        ],
        "Em aumentos sucessivos, multiplicam-se os respectivos fatores de acréscimo: (1 + 0,10) × (1 + 0,20) = 1,10 × 1,20 = 1,32. Subtraindo a unidade base obtém-se 1,32 − 1 = 0,32, correspondendo a um aumento acumulado de 32%. A soma direta das taxas (10% + 20% = 30%) ignora a incidência do segundo aumento sobre o valor já corrigido."
    ),
    (
        "a05/s03", "E",
        "Uma loja de uniformes operacionais concedeu dois descontos sucessivos sobre o preço de uma jaqueta tática: o primeiro de 10% e o segundo de 20%. Assinale a opção que indica o desconto percentual acumulado correspondente.",
        [
            "30%",
            "25%",
            "32%",
            "26%",
            "28%",
        ],
        "Os descontos sucessivos são compostos pela multiplicação dos fatores de desconto: (1 − 0,10) × (1 − 0,20) = 0,90 × 0,80 = 0,72. O desconto real acumulado é a diferença em relação a 1: 1 − 0,72 = 0,28 = 28%. A soma aritmética 10% + 20% = 30% desconsidera que o segundo abatimento incide sobre a base menor já reduzida."
    ),
    (
        "a05/s03", "E",
        "O preço de determinado suprimento pericial sofreu um aumento de 20% em janeiro e, em fevereiro, sofreu uma redução de 20%. Em relação ao preço original do produto antes de janeiro, assinale a opção correta.",
        [
            "O preço final permaneceu inalterado.",
            "Houve um aumento final de 4%.",
            "Houve uma redução final de 2%.",
            "Houve uma redução final de 5%.",
            "Houve uma redução final de 4%.",
        ],
        "Aplicando os fatores sucessivos de aumento e desconto: (1 + 0,20) × (1 − 0,20) = 1,20 × 0,80 = 0,96. Comparando com o valor inicial 1: 0,96 − 1 = −0,04, o que representa uma redução final líquida de 4%. Supor que acréscimo e decréscimo de mesma taxa se anulam é um equívoco conceitual clássico em matemática financeira."
    ),
    (
        "a05/s03", "A",
        "Durante três meses consecutivos, a inflação sobre os insumos laboratoriais da polícia técnica foi de 2% no primeiro mês, 3% no segundo mês e 5% no terceiro mês. A respeito da taxa de inflação acumulada nesse trimestre, assinale a opção correta.",
        [
            "A taxa acumulada no trimestre foi superior a 10%.",
            "A taxa acumulada no trimestre foi exatamente igual a 10%.",
            "A taxa acumulada no trimestre foi inferior a 10%.",
            "A taxa acumulada é obtida pela média aritmética simples das taxas mensais.",
            "A taxa acumulada resultou em exatamente 10,00%.",
        ],
        "O fator acumulado trimestral é o produto dos fatores mensais: (1 + 0,02)(1 + 0,03)(1 + 0,05) = 1,02 × 1,03 × 1,05 = 1,0506 × 1,05 = 1,10313. A taxa acumulada real é 10,313%, sendo estritamente superior a 10%. A soma linear 2% + 3% + 5% = 10% subestima a inflação acumulada por desconsiderar o efeito cumulativo das variações sucessivas."
    ),

    # --- a08/s02 (5 qs) ---
    (
        "a08/s02", "E",
        "Considere a equação quadrática 2x² − 6x + 5 = 0. A respeito do discriminante delta dessa equação e da existência de raízes reais, assinale a opção correta.",
        [
            "O discriminante é igual a 4 e a equação possui duas raízes reais distintas.",
            "O discriminante é igual a zero e a equação possui uma única raiz real dupla.",
            "O discriminante é igual a −4 e a equação possui duas raízes reais distintas.",
            "O discriminante é igual a 16 e a equação possui duas raízes reais positivas.",
            "O discriminante é igual a −4 e a equação não possui raízes reais.",
        ],
        "Para a equação ax² + bx + c = 0 com a = 2, b = −6 e c = 5, o discriminante delta é dado por delta = b² − 4ac = (−6)² − 4·2·5 = 36 − 40 = −4. Como o discriminante é estritamente negativo (delta < 0), a equação não admite raízes no conjunto dos números reais. Valores positivos para delta decorrem de erros nos sinais da multiplicação."
    ),
    (
        "a08/s02", "C",
        "Ao resolver a equação do segundo grau x² − 8x + 15 = 0 utilizando a fórmula de Bhaskara, um estudante calculou suas raízes reais. Assinale a opção que indica essas raízes.",
        [
            "−3 e −5",
            "2 e 6",
            "3 e 5",
            "1 e 15",
            "−1 e 15",
        ],
        "Na equação x² − 8x + 15 = 0: a = 1, b = −8 e c = 15. Discriminante: delta = (−8)² − 4·1·15 = 64 − 60 = 4. Aplicando Bhaskara: x = [−(−8) ± raiz(4)] / (2·1) = (8 ± 2) / 2. As raízes reais são x₁ = (8 + 2)/2 = 5 e x₂ = (8 − 2)/2 = 3. Raízes negativas como −3 e −5 resultam de equívocos no sinal de menos da fórmula."
    ),
    (
        "a08/s02", "D",
        "Dada a equação quadrática incompleta 3x² − 12x = 0, assinale a opção que indica o conjunto solução dessa equação no conjunto dos números reais.",
        [
            "{0, −4}",
            "{3, 12}",
            "{2, 4}",
            "{0, 4}",
            "{−2, 2}",
        ],
        "Com c = 0, a equação pode ser resolvida fatorando o termo comum x: 3x(x − 4) = 0. Para que o produto seja nulo, 3x = 0 ⇒ x = 0, ou x − 4 = 0 ⇒ x = 4. O conjunto solução é portanto {0, 4}. O valor −4 decorre de erro na transposição do termo negativo para o outro membro da equação."
    ),
    (
        "a08/s02", "E",
        "Considere a equação do segundo grau 4x² − 64 = 0. A respeito das raízes dessa equação no conjunto dos números reais, assinale a opção correta.",
        [
            "A equação possui uma única raiz real igual a 4.",
            "A equação possui raízes reais iguais a −16 e 16.",
            "A equação não possui raízes no conjunto dos números reais.",
            "A equação possui raízes reais iguais a 0 e 16.",
            "As raízes da equação são reais e simétricas, sendo iguais a −4 e 4.",
        ],
        "Na equação incompleta com b = 0: 4x² = 64 ⇒ x² = 64/4 = 16. Extraindo a raiz quadrada: x = ±raiz(16) = ±4. As duas raízes reais são números simétricos opostos: −4 e 4. Considerar apenas a raiz positiva 4 ignora a solução negativa igualmente válida que satisfaz à igualdade quadrática."
    ),
    (
        "a08/s02", "A",
        "Para que a equação quadrática x² − 6x + k = 0 admita uma única raiz real (raiz dupla), o valor da constante real k deve satisfazer a determinada condição. Assinale a opção que indica o valor correto de k.",
        [
            "9",
            "−9",
            "36",
            "6",
            "3",
        ],
        "Uma equação do segundo grau possui uma única raiz real dupla se, e somente se, seu discriminante for igual a zero: delta = 0. Calculando: delta = b² − 4ac = (−6)² − 4·1·k = 36 − 4k. Impondo a condição: 36 − 4k = 0 ⇒ 4k = 36 ⇒ k = 9. Valores como −9 ou 36 resultam de erros na resolução da equação do primeiro grau em k."
    ),

    # --- a08/s04 (5 qs) ---
    (
        "a08/s04", "C",
        "Seja a inequação do primeiro grau 5x − 15 > 0 definida no conjunto dos números reais. Assinale a opção que indica o conjunto solução dessa inequação.",
        [
            "x < 3",
            "x ≥ 3",
            "x > 3",
            "x > −3",
            "x < −3",
        ],
        "Para resolver 5x − 15 > 0, isola-se a incógnita x: 5x > 15 ⇒ x > 15/5 ⇒ x > 3. Sendo a desigualdade estrita (>), o número 3 não faz parte da solução, correspondendo ao intervalo aberto de 3 ao infinito. Inverter o sinal da desigualdade sem multiplicar por número negativo é um erro conceitual."
    ),
    (
        "a08/s04", "D",
        "Ao resolver a inequação −3x + 12 ≤ 0 no conjunto dos números reais, deve-se aplicar as regras operatórias de desigualdades. Assinale a opção que indica a solução correta.",
        [
            "x ≤ 4",
            "x ≤ −4",
            "x < 4",
            "x ≥ 4",
            "x > −4",
        ],
        "Isolando o termo com a incógnita: −3x ≤ −12. Ao multiplicar ou dividir ambos os membros por um número negativo (−3), é obrigatório inverter o sentido da desigualdade: x ≥ (−12) / (−3) ⇒ x ≥ 4. Não inverter a desigualdade ao dividir por valor negativo gera a solução incorreta x ≤ 4."
    ),
    (
        "a08/s04", "D",
        "Considere a inequação linear (2x − 1) / 3 < (x + 4) / 2 no conjunto dos números reais. Assinale a opção que indica o conjunto de valores de x que satisfaz a essa desigualdade.",
        [
            "x > 14",
            "x < 10",
            "x > 10",
            "x < 14",
            "x ≤ 14",
        ],
        "Multiplicando ambos os membros pelo mínimo múltiplo comum dos denominadores (que é 6, positivo): 2·(2x − 1) < 3·(x + 4) ⇒ 4x − 2 < 3x + 12. Subtraindo 3x e somando 2: 4x − 3x < 12 + 2 ⇒ x < 14. Inversões na distribuição dos coeficientes geram soluções incorretas como x < 10."
    ),
    (
        "a08/s04", "B",
        "Um número real x satisfaz simultaneamente às seguintes condições: 2x + 4 ≥ 10 e 3x − 1 < 20. Assinale a opção que expressa o intervalo de variação de x.",
        [
            "3 < x ≤ 7",
            "3 ≤ x < 7",
            "x ≥ 3",
            "x < 7",
            "2 ≤ x < 7",
        ],
        "Resolvendo a primeira inequação: 2x + 4 ≥ 10 ⇒ 2x ≥ 6 ⇒ x ≥ 3. Resolvendo a segunda inequação: 3x − 1 < 20 ⇒ 3x < 21 ⇒ x < 7. A interseção das duas soluções simultâneas é o intervalo semiaberto 3 ≤ x < 7. Trocar os sinais de inclusão (≥ por > ou < por ≤) descaracteriza a solução exata."
    ),
    (
        "a08/s04", "B",
        "A respeito da inequação 4x − 7 > 21 definida para x pertencente aos números inteiros, assinale a opção que indica o menor valor inteiro possível para x.",
        [
            "7",
            "8",
            "9",
            "6",
            "10",
        ],
        "Resolvendo a inequação: 4x > 21 + 7 ⇒ 4x > 28 ⇒ x > 7. Como a desigualdade é estrita (x deve ser estritamente maior do que 7) e x é um número inteiro, o menor inteiro que satisfaz a condição é 8. O valor 7 não satisfaz a desigualdade porque tornaria o membro esquerdo igual a 21 e não maior."
    ),

    # --- a09/s01 (4 qs) ---
    (
        "a09/s01", "A",
        "Sejam os conjuntos A = {1, 2, 3} e B = {4, 5, 6, 7}. Assinale a opção que indica o número total de elementos (pares ordenados) pertencentes ao produto cartesiano A × B.",
        [
            "12",
            "7",
            "10",
            "16",
            "9",
        ],
        "O número de pares ordenados do produto cartesiano entre dois conjuntos finitos é o produto entre a quantidade de elementos de cada um: n(A × B) = n(A) · n(B). Como o primeiro conjunto possui 3 elementos e o segundo possui 4 elementos, temos 3 × 4 = 12 pares ordenados. Somar os elementos (3 + 4 = 7) desconsidera a definição combinatória de produto cartesiano."
    ),
    (
        "a09/s01", "A",
        "Em relação aos conceitos fundamentais da teoria das funções entre dois conjuntos não vazios A e B, assinale a opção correta.",
        [
            "Uma relação f de A em B é função se todo elemento de A possui um único correspondente em B.",
            "Para que uma relação seja função, cada elemento do contradomínio B deve receber pelo menos uma flecha.",
            "O domínio de uma função coincide obrigatoriamente com o conjunto imagem da função.",
            "Um elemento do domínio pode possuir dois ou mais elementos correspondentes no contradomínio.",
            "Todo gráfico no plano cartesiano representa necessariamente uma função de x em y.",
        ],
        "Pela definição matemática formal, uma relação binária entre dois conjuntos é classificada como função se, e somente se, para cada elemento x do domínio existir um único elemento y no contradomínio tal que f(x) = y. Nem todos os elementos do contradomínio precisam ser atingidos (função não sobrejetora), e nenhum elemento do domínio pode ter correspondência múltipla."
    ),
    (
        "a09/s01", "B",
        "Considere a função real f(x) = 5 / √(x − 4). Assinale a opção que indica o domínio dessa função no conjunto dos números reais.",
        [
            "x ≥ 4",
            "x > 4",
            "x < 4",
            "x ≠ 4",
            "todo x real",
        ],
        "No conjunto dos números reais, uma raiz de índice par no denominador impõe duas condições simultâneas: o radicando deve ser não negativo e o denominador não pode ser zero. Assim: x − 4 > 0 ⇒ x > 4. O valor x = 4 deve ser excluído porque anularia o denominador, inviabilizando a divisão."
    ),
    (
        "a09/s01", "C",
        "Seja a função f: A → R definida por f(x) = 2x + 3 com domínio A = {−1, 0, 2}. Assinale a opção que indica o conjunto imagem dessa função.",
        [
            "{−1, 0, 2}",
            "{1, 5, 7}",
            "{1, 3, 7}",
            "{3, 5, 7}",
            "{−2, 0, 4}",
        ],
        "O conjunto imagem é formado pelos valores calculados f(x) para cada elemento do domínio A: f(−1) = 2(−1) + 3 = 1; f(0) = 2(0) + 3 = 3; f(2) = 2(2) + 3 = 7. O conjunto imagem é {1, 3, 7}. Conjuntos como {1, 5, 7} provêm de substituições incorretas de x na função afim."
    ),

    # --- a10/s02 (1 q) ---
    (
        "a10/s02", "E",
        "A reta representativa de uma função afim passa pelos pontos A(2, 5) e B(6, 17) no plano cartesiano. Assinale a opção que indica o coeficiente angular dessa reta.",
        [
            "4",
            "2",
            "5",
            "6",
            "3",
        ],
        "O coeficiente angular a é a taxa de variação da função afim, calculada por a = (y₂ − y₁) / (x₂ − x₁). Substituindo os pontos dados: a = (17 − 5) / (6 − 2) = 12 / 4 = 3. Inverter a razão calculando a variação de x sobre y geraria 4/12 = 1/3, e subtrair diretamente coordenadas sem dividir geraria valores desprovidos de sentido geométrico."
    ),

    # --- a11/s03 (4 qs) ---
    (
        "a11/s03", "C",
        "Uma função quadrática é dada por f(x) = x² − 5x + 6. A respeito dos pontos em que o gráfico dessa função cruza o eixo das abscissas (eixo x), assinale a opção correta.",
        [
            "O gráfico cruza o eixo x nos pontos (−2, 0) e (−3, 0).",
            "O gráfico cruza o eixo x no ponto (0, 6).",
            "O gráfico cruza o eixo x nos pontos (2, 0) e (3, 0).",
            "O gráfico cruza o eixo x nos pontos (1, 0) e (6, 0).",
            "O gráfico não cruza o eixo x porque seu discriminante é nulo.",
        ],
        "O gráfico corta o eixo das abscissas nas raízes reais da equação f(x) = 0: x² − 5x + 6 = 0 ⇒ (x − 2)(x − 3) = 0 ⇒ x = 2 e x = 3. Os pontos geométricos correspondentes são (2, 0) e (3, 0). O ponto (0, 6) representa a interseção com o eixo vertical y, não com o eixo horizontal x."
    ),
    (
        "a11/s03", "A",
        "Considere a função quadrática f(x) = x² − 6x + 9. A respeito da quantidade de raízes reais e da representação gráfica dessa função, assinale a opção correta.",
        [
            "A função possui uma única raiz real dupla e seu gráfico tangencia o eixo x no ponto (3, 0).",
            "A função possui duas raízes reais distintas e corta o eixo x em dois pontos diferentes.",
            "A função não possui raízes reais e sua parábola não toca o eixo x.",
            "O gráfico corta o eixo das ordenadas na origem do plano cartesiano.",
            "A parábola possui concavidade voltada para baixo com ponto de máximo em x = 3.",
        ],
        "O discriminante dessa função é delta = (−6)² − 4·1·9 = 36 − 36 = 0. Quando delta = 0, a função admite uma única raiz real dupla (x = 3), e a parábola tangencia o eixo x exatamente no ponto (3, 0), que é o vértice da curva. Para cortar em dois pontos distintos delta deveria ser positivo."
    ),
    (
        "a11/s03", "E",
        "Seja a função do segundo grau f(x) = x² + 2x + 5. A respeito das raízes e do posicionamento de sua parábola em relação ao eixo horizontal x, assinale a opção correta.",
        [
            "A parábola intercepta o eixo x nos pontos (1, 0) e (−5, 0).",
            "A parábola é tangente ao eixo horizontal na sua raiz x = −1.",
            "A função possui duas raízes reais distintas de sinais contrários.",
            "A função possui discriminante positivo igual a 16.",
            "A parábola não intercepta o eixo x porque a função não possui raízes reais.",
        ],
        "Calculando o discriminante da função: delta = 2² − 4·1·5 = 4 − 20 = −16. Sendo delta < 0 e a = 1 > 0, a parábola não intercepta o eixo x em nenhum ponto, permanecendo inteiramente posicionada acima do eixo horizontal no plano cartesiano. Raízes reais só existiriam com discriminante maior ou igual a zero."
    ),
    (
        "a11/s03", "E",
        "Considere a função quadrática f(x) = −x² + 4. A respeito das interseções do gráfico dessa função com os eixos cartesianos x e y, assinale a opção correta.",
        [
            "O gráfico intercepta o eixo x em (4, 0) e o eixo y em (0, −2).",
            "O gráfico intercepta o eixo x na origem e o eixo y em (0, 4).",
            "O gráfico possui apenas uma raiz real no ponto (2, 0).",
            "O gráfico não intercepta o eixo vertical y.",
            "O gráfico intercepta o eixo x nos pontos (−2, 0) e (2, 0), e o eixo y no ponto (0, 4).",
        ],
        "As raízes ocorrem quando f(x) = 0: −x² + 4 = 0 ⇒ x² = 4 ⇒ x = ±2, gerando os pontos (−2, 0) e (2, 0) sobre o eixo x. A interseção com o eixo vertical ocorre quando x = 0: f(0) = 4, definindo o ponto (0, 4). Inverter os pontos ou admitir apenas a raiz positiva desconsidera a simetria da parábola."
    ),

    # --- a15/s01 (4 qs) ---
    (
        "a15/s01", "A",
        "Dois ângulos são complementares e a medida de um deles é o dobro da medida do outro. Assinale a opção que indica a medida do maior desses dois ângulos.",
        [
            "60°",
            "45°",
            "75°",
            "30°",
            "50°",
        ],
        "Dois ângulos são complementares quando a soma de suas medidas é 90 graus: x + 2x = 90° ⇒ 3x = 90° ⇒ x = 30°. O maior dos ângulos mede 2x = 2 × 30° = 60°. O valor 30° corresponde ao menor ângulo, e 45° ocorreria apenas se os ângulos fossem congruentes entre si."
    ),
    (
        "a15/s01", "C",
        "Duas retas concorrentes determinam dois ângulos opostos pelo vértice cujas medidas em graus são dadas por 4x − 10° e 2x + 30°. Assinale a opção que indica a medida comum desses ângulos.",
        [
            "50°",
            "60°",
            "70°",
            "80°",
            "40°",
        ],
        "Ângulos opostos pelo vértice são geometricamente congruentes: 4x − 10 = 2x + 30 ⇒ 4x − 2x = 30 + 10 ⇒ 2x = 40 ⇒ x = 20. Substituindo na expressão: 4(20) − 10 = 80 − 10 = 70° (ou 2·20 + 30 = 70°). O valor 20° é apenas o parâmetro da incógnita x, e não a medida angular do problema."
    ),
    (
        "a15/s01", "E",
        "Ao somar os ângulos A = 25° 40' e B = 34° 35', um desenhista técnico obteve uma medida angular expressa na forma padrão. Assinale a opção que indica o resultado dessa soma.",
        [
            "59° 75'",
            "60° 05'",
            "61° 15'",
            "59° 15'",
            "60° 15'",
        ],
        "Somando separadamente graus e minutos: 25° + 34° = 59° e 40' + 35' = 75'. Como cada grau contém 60 minutos (60' = 1°), decompõe-se 75' em 60' + 15' = 1° 15'. Somando o grau transportado: 59° + 1° = 60°, restando 15 minutos: 60° 15'. Manter 75 minutos viola a representação sexagesimal padrão."
    ),
    (
        "a15/s01", "D",
        "A respeito da classificação e nomenclatura dos ângulos segundo suas medidas geométricas, assinale a opção correta.",
        [
            "Um ângulo de 90 graus é classificado geometricamente como raso.",
            "Todo ângulo cuja medida é estritamente maior que 90 graus é classificado como raso.",
            "Um ângulo cuja medida é estritamente menor que 90 graus é classificado como obtuso.",
            "Um ângulo cuja medida é estritamente maior que 0 grau e menor que 90 graus é classificado como agudo.",
            "Dois ângulos cuja soma é igual a 180 graus são denominados complementares.",
        ],
        "Por definição geométrica, um ângulo agudo possui abertura estritamente compreendida entre 0° e 90°. O ângulo de 90° é chamado reto, o de 180° é o raso, e ângulos com medidas entre 90° e 180° são obtusos. Além disso, ângulos cuja soma é 180° denominam-se suplementares e não complementares."
    ),

    # --- a15/s02 (3 qs) ---
    (
        "a15/s02", "A",
        "Uma pista circular de treinamento possui raio medindo 50 metros. Adotando pi igual a 3,14, assinale a opção que indica a distância percorrida por um policial ao completar 4 voltas inteiras nessa pista.",
        [
            "1.256 metros.",
            "628 metros.",
            "1.570 metros.",
            "942 metros.",
            "1.884 metros.",
        ],
        "O comprimento de uma volta circular é dado por C = 2·pi·R. Substituindo os valores: C = 2 × 3,14 × 50 = 314 metros. Para 4 voltas completas percorridas, multiplica-se a extensão por 4: 4 × 314 = 1.256 metros. O valor 628 metros corresponderia a apenas 2 voltas no percurso."
    ),
    (
        "a15/s02", "B",
        "O heliponto de um grupamento aéreo tem o formato de um círculo com diâmetro de 20 metros. Considerando pi igual a 3,14, assinale a opção que indica a área total dessa superfície de pouso.",
        [
            "628 m²",
            "314 m²",
            "1.256 m²",
            "157 m²",
            "78,5 m²",
        ],
        "Sendo o diâmetro D = 20 metros, o raio mede a metade: R = 10 metros. A área do círculo é dada pela fórmula A = pi·R². Substituindo os dados: A = 3,14 × 10² = 3,14 × 100 = 314 m². Utilizar diretamente o diâmetro 20 na fórmula da área resultaria erroneamente em 1.256 m² (quatro vezes a área real)."
    ),
    (
        "a15/s02", "A",
        "Em um terreno circular de raio igual a 6 metros, reservou-se um setor circular correspondente a um ângulo central de 60 graus. Considerando pi igual a 3,14, assinale a opção que indica a área desse setor circular.",
        [
            "18,84 m²",
            "37,68 m²",
            "12,56 m²",
            "24,84 m²",
            "9,42 m²",
        ],
        "A área total do círculo é A = pi·R² = 3,14 × 6² = 3,14 × 36 = 113,04 m². Um setor circular de ângulo central 60° corresponde à fração proporcional 60° / 360° = 1/6 da área total. Logo: A_setor = 113,04 ÷ 6 = 18,84 m² (ou 6·pi = 6 × 3,14 = 18,84 m²). O dobro desse valor corresponderia a um ângulo de 120°."
    ),

    # --- a15/s03 (4 qs) ---
    (
        "a15/s03", "B",
        "Em um triângulo, as medidas de dois de seus ângulos internos são 45° e 70°. Assinale a opção que indica a medida do terceiro ângulo interno desse triângulo.",
        [
            "55°",
            "65°",
            "75°",
            "60°",
            "70°",
        ],
        "A soma das medidas dos três ângulos internos de qualquer triângulo no plano euclidiano é igual a 180 graus. Somando os ângulos conhecidos: 45° + 70° = 115°. O terceiro ângulo interno é obtido subtraindo esse valor de 180°: 180° − 115° = 65°. Medidas como 55° ou 75° não totalizam a soma angular obrigatória de 180 graus."
    ),
    (
        "a15/s03", "C",
        "Em um triângulo qualquer, a medida de um ângulo externo é igual a 125° e um dos ângulos internos não adjacentes a ele mede 55°. Assinale a opção que indica a medida do outro ângulo interno não adjacente.",
        [
            "60°",
            "65°",
            "70°",
            "75°",
            "80°",
        ],
        "Pelo teorema do ângulo externo, a medida de qualquer ângulo externo de um triângulo é igual à soma das medidas dos dois ângulos internos a ele não adjacentes: Angulo_externo = Â₁ + Â₂. Substituindo os valores: 125° = 55° + Â₂ ⇒ Â₂ = 125° − 55° = 70°. Outros valores não satisfazem o teorema angular."
    ),
    (
        "a15/s03", "B",
        "A respeito da condição geométrica de existência de um triângulo cujos lados medem a, b e c, assinale a opção que indica um conjunto de medidas capaz de formar um triângulo.",
        [
            "3 cm, 4 cm e 8 cm",
            "5 cm, 7 cm e 10 cm",
            "2 cm, 3 cm e 6 cm",
            "4 cm, 6 cm e 10 cm",
            "1 cm, 2 cm e 4 cm",
        ],
        "Pela desigualdade triangular, cada lado de um triângulo deve ser estritamente menor do que a soma dos outros dois lados. Para 5, 7 e 10: 10 < 5 + 7 = 12 (válido). Já nos demais trios a condição falha: 3 + 4 = 7 < 8; 2 + 3 = 5 < 6; 4 + 6 = 10 (segmentos colineares degenerados sem formar triângulo); e 1 + 2 = 3 < 4."
    ),
    (
        "a15/s03", "E",
        "A respeito dos critérios clássicos de congruência de triângulos na geometria plana Euclidiana, assinale a opção correta.",
        [
            "A igualdade dos três ângulos internos (AAA) é critério suficiente para garantir a congruência de dois triângulos.",
            "Dois triângulos que possuem a mesma área são necessariamente congruentes.",
            "O critério Lado-Lado-Lado (LLL) garante apenas a semelhança, não garantindo a congruência de triângulos.",
            "A congruência de triângulos exige que todos os ângulos sejam retos ou obtusos.",
            "Pelo critério Lado-Ângulo-Lado (LAL), dois triângulos são congruentes se tiverem dois lados e o ângulo entre eles respectivamente congruentes.",
        ],
        "O critério LAL (Lado-Ângulo-Lado) estabelece que dois triângulos são congruentes quando possuem dois lados correspondentes congruentes e o ângulo formado por esses lados também congruente. Ter os três ângulos congruentes (AAA) garante apenas semelhança (e não congruência), e ter a mesma área não implica congruência de formas."
    ),

    # --- a15/s04 (5 qs) ---
    (
        "a15/s04", "C",
        "Três retas paralelas r, s e t são cortadas por duas retas transversais u e v. A transversal u é dividida pelas paralelas em segmentos que medem 6 cm e 9 cm, enquanto a transversal v é dividida em segmentos medindo 8 cm e x cm. Assinale a opção que indica o valor de x em centímetros.",
        [
            "10 cm",
            "15 cm",
            "12 cm",
            "14 cm",
            "11 cm",
        ],
        "Pelo Teorema de Tales, um feixe de retas paralelas determina sobre retas transversais segmentos proporcionais: 6 / 9 = 8 / x. Multiplicando em cruz: 6 · x = 9 · 8 ⇒ 6x = 72 ⇒ x = 72 ÷ 6 = 12 cm. De forma simplificada, 6/9 = 2/3, logo x = 8 · (3/2) = 12 cm. Valores divergentes não mantêm a proporcionalidade das transversais."
    ),
    (
        "a15/s04", "E",
        "Uma escada de 10 metros de comprimento está apoiada em uma parede vertical. Se a base da escada está afastada 6 metros da parede, assinale a opção que indica a altura alcançada pelo topo da escada na parede.",
        [
            "7 metros.",
            "9 metros.",
            "7,5 metros.",
            "8,5 metros.",
            "8 metros.",
        ],
        "A situação forma um triângulo retângulo onde a escada é a hipotenusa (a = 10) e a distância ao solo é um cateto (b = 6). Pelo Teorema de Pitágoras: a² = b² + h² ⇒ 10² = 6² + h² ⇒ 100 = 36 + h² ⇒ h² = 64 ⇒ h = 8 metros. O resultado corresponde à proporção do triângulo pitagórico 3-4-5 multiplicado por dois."
    ),
    (
        "a15/s04", "A",
        "Em um triângulo retângulo, a altura relativa à hipotenusa divide-a em dois segmentos de projeção que medem 4 cm e 9 cm. Assinale a opção que indica a medida dessa altura em centímetros.",
        [
            "6 cm",
            "6,5 cm",
            "5 cm",
            "7 cm",
            "8 cm",
        ],
        "Pelas relações métricas no triângulo retângulo, o quadrado da altura relativa à hipotenusa é igual ao produto das projeções dos catetos sobre a hipotenusa: h² = m · n. Substituindo os valores: h² = 4 × 9 = 36 ⇒ h = raiz quadrada de 36 = 6 cm. A média aritmética simples (4 + 9)/2 = 6,5 cm não traduz a média geométrica dessa relação métrica."
    ),
    (
        "a15/s04", "D",
        "Um cabo de aço de fixação de uma torre de transmissão tem 20 metros de comprimento e forma um ângulo de 30° com o solo horizontal plano. Sabendo que o seno de 30° é igual a 1/2, assinale a opção que indica a altura do ponto de fixação do cabo na torre.",
        [
            "15 metros.",
            "12 metros.",
            "8 metros.",
            "10 metros.",
            "14 metros.",
        ],
        "Na trigonometria do triângulo retângulo, o seno do ângulo é a razão entre o cateto oposto (altura h) e a hipotenusa (comprimento do cabo): sen(30°) = h / 20. Substituindo sen(30°) = 1/2: 1/2 = h / 20 ⇒ h = 20 / 2 = 10 metros. Outras medidas ignoram a definição da razão trigonométrica seno."
    ),
    (
        "a15/s04", "B",
        "Um terreno triangular possui base medindo 24 metros e altura relativa a essa base medindo 15 metros. Assinale a opção que indica a área total desse terreno em metros quadrados.",
        [
            "360 m²",
            "180 m²",
            "200 m²",
            "160 m²",
            "150 m²",
        ],
        "A área de um triângulo é obtida pela metade do produto entre a base e a respectiva altura: Área = (base × altura) / 2. Substituindo: Área = (24 × 15) / 2 = 360 / 2 = 180 m². O valor 360 m² decorre da omissão da divisão por 2, correspondendo à área de um paralelogramo de mesmas dimensões."
    ),

    # --- a15/s05 (5 qs) ---
    (
        "a15/s05", "E",
        "Em um triângulo ABC, o segmento AM é uma mediana que mede 18 cm e G é o baricentro desse triângulo. Assinale a opção que indica a medida do segmento AG compreendido entre o vértice A e o baricentro G.",
        [
            "9 cm",
            "6 cm",
            "10 cm",
            "14 cm",
            "12 cm",
        ],
        "O baricentro G divide cada mediana na proporção de 2 para 1 a partir do vértice correspondente. Logo, a distância do vértice ao baricentro corresponde a 2/3 do comprimento total da mediana: AG = (2/3) × AM = (2/3) × 18 = 12 cm (restando 6 cm para o segmento GM até o ponto médio). Dividir a mediana ao meio (9 cm) ignora a propriedade do baricentro."
    ),
    (
        "a15/s05", "D",
        "A respeito dos pontos notáveis de um triângulo na geometria plana, assinale a opção que indica o ponto notável que corresponde ao ponto de encontro das bissetrizes internas e ao centro da circunferência inscrita no triângulo.",
        [
            "Baricentro",
            "Circuncentro",
            "Ortocentro",
            "Incentro",
            "Ex-incentro",
        ],
        "O incentro é o ponto notável formado pela interseção das três bissetrizes internas dos ângulos de um triângulo. Como as bissetrizes contêm pontos equidistantes dos lados adjacentes, o incentro equidista dos três lados do triângulo e atua como centro da circunferência inscrita (circunferência tangente interna aos lados)."
    ),
    (
        "a15/s05", "B",
        "No estudo dos triângulos, o circuncentro é um dos pontos notáveis fundamentais. A respeito do circuncentro, assinale a opção correta.",
        [
            "É o ponto de encontro das alturas do triângulo e situa-se sempre no interior da figura.",
            "É o ponto de encontro das mediatrizes dos lados do triângulo e é equidistante de todos os vértices.",
            "É o ponto de encontro das medianas e coincide com o centro de gravidade da figura.",
            "É o centro da circunferência inscrita e equidista de todos os lados do triângulo.",
            "É o ponto de interseção das retas bissetrizes dos ângulos externos.",
        ],
        "O circuncentro é o ponto de concorrência das mediatrizes dos lados do triângulo. Sendo a mediatriz o lugar geométrico dos pontos equidistantes das extremidades de um segmento, o circuncentro equidista dos três vértices do triângulo e constitui o centro da circunferência circunscrita. O encontro das alturas é o ortocentro e o das medianas é o baricentro."
    ),
    (
        "a15/s05", "D",
        "Em relação ao ortocentro de um triângulo retângulo na geometria plana, assinale a opção correta.",
        [
            "O ortocentro localiza-se no ponto médio da hipotenusa.",
            "O ortocentro localiza-se na região externa ao triângulo retângulo.",
            "O ortocentro localiza-se no centro da circunferência inscrita.",
            "O ortocentro localiza-se exatamente sobre o vértice correspondente ao ângulo reto.",
            "O triângulo retângulo não possui ortocentro definido.",
        ],
        "Em um triângulo retângulo, as alturas relativas aos dois catetos coincidem com os próprios catetos. Portanto, as três alturas da figura concorrem exatamente no vértice do ângulo de noventa graus. O ponto médio da hipotenusa é o circuncentro do triângulo retângulo, e não o ortocentro."
    ),
    (
        "a15/s05", "C",
        "A respeito dos pontos notáveis (baricentro, incentro, circuncentro e ortocentro) em um triângulo equilátero, assinale a opção correta.",
        [
            "Os quatro pontos notáveis são colineares, porém ocupam quatro posições distintas.",
            "O baricentro e o ortocentro coincidem, mas o incentro situa-se fora da figura.",
            "Os quatro pontos notáveis coincidem exatamente no mesmo ponto geométrico.",
            "O circuncentro localiza-se no exterior do triângulo equilátero.",
            "Nenhum dos pontos notáveis coincide no triângulo equilátero.",
        ],
        "Devido à simetria total do triângulo equilátero, as alturas, medianas, mediatrizes e bissetrizes relativas a cada lado coincidem integralmente. Consequentemente, o baricentro, o incentro, o circuncentro e o ortocentro convergem todos para um único e mesmo ponto geométrico no interior da figura."
    ),

    # --- a15/s06 (4 qs) ---
    (
        "a15/s06", "A",
        "Um perito precisa determinar a soma das medidas dos ângulos internos de um terreno que possui a forma de um hexágono convexo (6 lados). Assinale a opção que indica o valor dessa soma.",
        [
            "720°",
            "540°",
            "900°",
            "1.080°",
            "360°",
        ],
        "A soma dos ângulos internos de um polígono convexo de n lados é dada por S_i = (n − 2) × 180°. Para um hexágono, temos n = 6: S_i = (6 − 2) × 180° = 4 × 180° = 720°. O valor 540° corresponde à soma angular do pentágono (n = 5) e 360° é a soma dos ângulos internos de quadriláteros ou a soma dos ângulos externos de qualquer polígono."
    ),
    (
        "a15/s06", "C",
        "Assinale a opção que indica o número total de diagonais de um octógono convexo (polígono de 8 lados).",
        [
            "16",
            "24",
            "20",
            "28",
            "14",
        ],
        "O número de diagonais de um polígono convexo de n vértices é dado pela fórmula d = [n(n − 3)] / 2. Para o octógono (n = 8): d = [8 × (8 − 3)] / 2 = (8 × 5) / 2 = 40 / 2 = 20 diagonais. O valor 40 desconsidera a divisão por dois (duplicando a contagem de cada diagonal ligando dois vértices)."
    ),
    (
        "a15/s06", "A",
        "Um terreno em formato de trapézio possui base maior medindo 30 metros, base menor medindo 18 metros e altura medindo 12 metros. Assinale a opção que indica a área desse terreno em metros quadrados.",
        [
            "288 m²",
            "576 m²",
            "240 m²",
            "320 m²",
            "216 m²",
        ],
        "A área do trapézio é dada pela média aritmética das bases multiplicada pela altura: Área = [(B + b) × h] / 2. Substituindo os dados: Área = [(30 + 18) × 12] / 2 = (48 × 12) / 2 = 576 / 2 = 288 m². De forma equivalente, base média 24 × altura 12 = 288 m². Esquecer de dividir por 2 geraria 576 m²."
    ),
    (
        "a15/s06", "C",
        "Uma insígnia metálica em formato de losango possui diagonais que medem 16 centímetros e 10 centímetros. Assinale a opção que indica a área dessa insígnia em centímetros quadrados.",
        [
            "160 cm²",
            "100 cm²",
            "80 cm²",
            "90 cm²",
            "70 cm²",
        ],
        "A área do losango é calculada pela metade do produto das suas diagonais: Área = (D × d) / 2. Substituindo as diagonais: Área = (16 × 10) / 2 = 160 / 2 = 80 cm². O produto simples 160 cm² corresponde à área de um retângulo que circunscreve o losango, e não ao próprio polígono."
    ),

    # --- a15/s07 (5 qs) ---
    (
        "a15/s07", "E",
        "Um quadrado está inscrito em uma circunferência cujo raio mede 6 cm. Assinale a opção que indica a medida do lado desse quadrado em centímetros.",
        [
            "6 cm",
            "12 cm",
            "3√2 cm",
            "12√2 cm",
            "6√2 cm",
        ],
        "No quadrado inscrito na circunferência, a diagonal coincide com o diâmetro da circunferência: d = 2R = 2 × 6 = 12 cm. Como a diagonal de um quadrado de lado l é d = l·raiz(2), temos: l = 12 / raiz(2) = 12·raiz(2) / 2 = 6·raiz(2) cm. Usar diretamente o raio como lado (6 cm) seria correto apenas para o hexágono regular inscrito."
    ),
    (
        "a15/s07", "D",
        "Um hexágono regular está inscrito em uma circunferência de raio igual a 8 cm. Assinale a opção que indica o perímetro desse hexágono em centímetros.",
        [
            "24 cm",
            "36 cm",
            "40 cm",
            "48 cm",
            "64 cm",
        ],
        "O hexágono regular inscrito na circunferência decompõe-se em 6 triângulos equiláteros cujos lados coincidem com o raio da circunferência: l = R = 8 cm. Sendo o hexágono composto por 6 lados congruentes, o perímetro é 6 × l = 6 × 8 = 48 cm. Perímetros como 24 ou 40 decorrem de quantidades errôneas de lados."
    ),
    (
        "a15/s07", "E",
        "Um triângulo equilátero está inscrito em uma circunferência de raio R = 10 cm. Assinale a opção que indica a medida do apótema desse triângulo equilátero.",
        [
            "10 cm",
            "5√3 cm",
            "2,5 cm",
            "10√3 cm",
            "5 cm",
        ],
        "No triângulo equilátero inscrito na circunferência, o centro coincide com o baricentro, que divide a altura na proporção 2:1. O raio R corresponde à distância do centro ao vértice (2/3 da altura), enquanto o apótema a é a distância do centro ao ponto médio do lado (1/3 da altura). Logo, o apótema vale a metade do raio: a = R / 2 = 10 / 2 = 5 cm."
    ),
    (
        "a15/s07", "B",
        "Uma praça triangular com o formato de um triângulo equilátero está inscrita em um canteiro circular de raio medindo 4 metros. Assinale a opção que indica o comprimento de cada lado desse triângulo.",
        [
            "4 metros.",
            "4√3 metros.",
            "8 metros.",
            "2√3 metros.",
            "8√3 metros.",
        ],
        "A medida do lado l de um triângulo equilátero inscrito em uma circunferência de raio R é dada pela relação l = R·raiz(3). Substituindo o raio de 4 metros: l = 4·raiz(3) metros. O valor 4 metros corresponderia ao lado de um hexágono regular, e 8 metros ao diâmetro da circunferência."
    ),
    (
        "a15/s07", "D",
        "Um polígono regular possui perímetro de 60 cm e seu apótema mede 4 cm. Assinale a opção que indica a área desse polígono em centímetros quadrados.",
        [
            "240 cm²",
            "60 cm²",
            "180 cm²",
            "120 cm²",
            "150 cm²",
        ],
        "A área de qualquer polígono regular é calculada pelo produto do semiperímetro p pelo apótema a: Área = p · a. O perímetro é 60 cm, portanto o semiperímetro vale p = 60 / 2 = 30 cm. Multiplicando pelo apótema: Área = 30 × 4 = 120 cm². Multiplicar diretamente o perímetro total pelo apótema sem dividir por 2 geraria o dobro da área real (240 cm²)."
    ),
]

def main():
    print(f"Total de questoes planejadas: {len(questions)}")
    assert len(questions) == 93, f"Esperado 93, obteve {len(questions)}"

    # Verificar distribuicao de gabaritos
    gabs = [q[1] for q in questions]
    cnt = Counter(gabs)
    print("Distribuicao dos gabaritos:", dict(cnt))

    # Verificar regras:
    # 1. Sem letras citadas no comentario
    forbidden_letter_patterns = [
        re.compile(r"\b(letra|alternativa|opção|opcao)\s+[A-E]\b", re.I),
        re.compile(r"\b[A-E]\s+(está|esta|é|e|erra|traz|apresenta)\b"),
    ]
    
    out_lines = []
    errors = []

    for idx, (seg, gab, stem, opts, comment) in enumerate(questions, 1):
        # Header
        out_lines.append(f"@@ {seg} | {gab}")
        out_lines.append(stem)
        
        # Stem word count
        words_stem = len(stem.split())
        if not (6 <= words_stem <= 140):
            errors.append(f"Q{idx} ({seg}): stem com {words_stem} palavras (esperado 6-140)")
        if not re.search(r"assinale|julgue|indique", stem, re.I):
            errors.append(f"Q{idx} ({seg}): stem sem comando")

        # Options
        labels = ["A", "B", "C", "D", "E"]
        if len(opts) != 5:
            errors.append(f"Q{idx} ({seg}): precisa de 5 opcoes")
        for l, opt in zip(labels, opts):
            out_lines.append(f"{l}) {opt}")

        # Check lengths
        opt_lens = [len(o) for o in opts]
        right_len = opt_lens[labels.index(gab)]
        mean_dist = (sum(opt_lens) - right_len) / 4.0
        if right_len > 80 and right_len > 1.8 * mean_dist:
            errors.append(f"Q{idx} ({seg}): gabarito muito mais longo que distratores ({right_len} vs mean {mean_dist:.1f})")

        # Comment
        if len(comment.split()) < 5:
            errors.append(f"Q{idx} ({seg}): comentario muito curto")

        for pat in forbidden_letter_patterns:
            m = pat.search(comment)
            if m:
                errors.append(f"Q{idx} ({seg}): mencao de letra no comentario: '{m.group(0)}'")

        out_lines.append(f"// Comentário: {comment}")
        out_lines.append("") # linha em branco entre blocos

    if errors:
        print(f"ERROS ENCONTRADOS ({len(errors)}):")
        for e in errors:
            print(" -", e)
        sys.exit(1)

    out_text = "\n".join(out_lines).strip() + "\n"
    out_path = Path("scratch/novas_questoes/matematica.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(out_text, encoding="utf-8")
    print(f"Sucesso! Arquivo gravado em {out_path} com {len(questions)} questoes.")

if __name__ == "__main__":
    main()
