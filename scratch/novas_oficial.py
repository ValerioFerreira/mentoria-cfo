import re, sys
NEW = {
"estatistica": """
@@ a13/s02 | A
Em um modelo de regressão linear múltipla, a soma de quadrados total (SQT) é 200 e a soma de quadrados dos resíduos (SQE) é 50. Assinale a opção que apresenta o coeficiente de determinação R².
A) 0,75
B) 0,25
C) 0,80
D) 0,60
E) 4,00
// Comentário: R² = 1 − SQE/SQT = 1 − 50/200 = 0,75, ou seja, SQR/SQT = 150/200. O valor 0,25 é a fração da variação não explicada pelo modelo, e 4,00 é a razão SQT/SQE, que não pode ser um R².

@@ a13/s02 | C
Em uma regressão linear múltipla com 3 variáveis explicativas e intercepto, ajustada a 24 observações, o teste F da significância global do modelo tem, respectivamente, quais graus de liberdade (numerador e denominador)? Assinale a opção correta.
A) 3 e 24
B) 4 e 20
C) 3 e 20
D) 3 e 21
E) 2 e 20
// Comentário: O numerador tem k graus de liberdade (k = 3 variáveis explicativas) e o denominador, n − k − 1 = 24 − 3 − 1 = 20. As demais combinações usam n ou n − k, ou contam o intercepto como variável explicativa.

@@ a13/s03 | B
Quando se omite de um modelo de regressão uma variável explicativa relevante, que se relaciona com as variáveis incluídas, assinale a opção correta sobre os estimadores de mínimos quadrados dos coeficientes das variáveis incluídas.
A) Permanecem não viesados e de menor variância, pois o modelo ficou mais simples.
B) Tornam-se viesados, porque parte do efeito da variável omitida é atribuída às variáveis incluídas.
C) Permanecem não viesados, mas passam a ter variância maior.
D) Tornam-se viesados apenas o intercepto, ficando os demais coeficientes corretos.
E) Deixam de ser calculáveis, pois o sistema de equações normais se torna indeterminado.
// Comentário: Na subespecificação, E(b1) = β1 + θ1·β3: o coeficiente incluído capta parte do efeito da variável omitida (β3), e o estimador fica viesado. A perda de eficiência, sem viés, é a consequência de incluir variável desnecessária.

@@ a13/s03 | E
Se o modelo estimado inclui uma variável explicativa desnecessária, isto é, sem efeito sobre Y no modelo verdadeiro, assinale a opção que descreve a consequência para os estimadores dos demais coeficientes.
A) Tornam-se viesados, em direção ao efeito da variável incluída.
B) Passam a ter variância menor e continuam não viesados.
C) Tornam-se inconsistentes, mesmo com amostras muito grandes.
D) Deixam de ter qualquer relação com os parâmetros verdadeiros do modelo.
E) Continuam não viesados, mas perdem eficiência, com variância maior que a do modelo correto.
// Comentário: A superespecificação não gera viés, mas aumenta a variância dos estimadores. Viés e inconsistência são consequências da omissão de variável relevante correlacionada com as incluídas.
""",
"biologia": """
@@ a01/s03 | C
Sobre o sarcômero, unidade morfofuncional do tecido muscular estriado, assinale a opção correta.
A) É a faixa do tecido conjuntivo que envolve cada fibra muscular, ricamente vascularizada.
B) É o conjunto de fibras envolvidas pelo perimísio, formando um fascículo muscular.
C) É o segmento da miofibrila delimitado por duas linhas Z sucessivas, formado por filamentos finos de actina e espessos de miosina.
D) É a rede de retículo liso que armazena íons cálcio no interior da fibra.
E) É a membrana plasmática da fibra muscular, que contém os núcleos periféricos.
// Comentário: O sarcômero vai de uma linha Z à seguinte e contém actina e miosina, que deslizam na contração. O endomísio envolve cada fibra, o perimísio agrupa fascículos, o retículo sarcoplasmático armazena cálcio e o sarcolema é a membrana da fibra.

@@ a01/s03 | A
Quanto às características do tecido muscular estriado cardíaco, assinale a opção correta.
A) Suas células são curtas, frequentemente ramificadas, com um núcleo central e unidas por discos intercalares que contêm junções comunicantes.
B) Suas células são longas, multinucleadas e com núcleos periféricos, sem comunicação entre os sarcoplasmas vizinhos.
C) Suas células são fusiformes, sem estriações e com um único núcleo, unidas apenas por desmossomos.
D) Sua contração é voluntária e depende de comando do sistema nervoso somático.
E) Suas células são multinucleadas e se regeneram por mitose após lesões do miocárdio.
// Comentário: O miocárdio tem células curtas, ramificadas, com um núcleo central e discos intercalares (desmossomos e junções comunicantes), que dão continuidade iônica. A descrição de células longas multinucleadas refere-se ao músculo esquelético, e a de células fusiformes sem estrias, ao músculo liso.

@@ a01/s03 | D
No músculo esquelético, assinale a opção que apresenta corretamente as camadas de tecido conjuntivo que o envolvem, de dentro para fora.
A) epimísio, perimísio e endomísio.
B) perimísio, endomísio e epimísio.
C) endomísio, epimísio e perimísio.
D) endomísio, que envolve cada fibra, perimísio, que agrupa fascículos, e epimísio, que reveste o músculo inteiro.
E) perimísio, que envolve cada fibra, endomísio, que agrupa fascículos, e epimísio, que reveste o ventre.
// Comentário: O endomísio envolve cada fibra individualmente, o perimísio agrupa as fibras em fascículos e o epimísio circunda todo o ventre muscular, prolongando-se em tendões e aponeuroses.

@@ a01/s02 | E
Sobre o tecido cartilaginoso, assinale a opção correta.
A) É ricamente vascularizado, e seus condrócitos recebem nutrientes diretamente dos capilares da matriz.
B) É inervado por abundantes terminações livres, o que explica sua grande sensibilidade à dor.
C) Tem matriz mineralizada por sais de cálcio, o que lhe confere dureza semelhante à do osso.
D) É formado por células em contato direto, com pouca matriz extracelular.
E) É avascular, e os nutrientes chegam aos condrócitos por difusão a partir do tecido conjuntivo vizinho, o pericôndrio.
// Comentário: A cartilagem é avascular e desprovida de vasos e nervos: a nutrição ocorre por difusão a partir do pericôndrio. A matriz mineralizada é do osso, e o epitélio é que tem células justapostas com pouca matriz.
""",
"fisica": """
@@ a03/s01 | B
Um objeto é abandonado, a partir do repouso, de uma altura de 45 m em local onde g = 10 m/s². Desprezando a resistência do ar, assinale a opção que apresenta a velocidade com que ele atinge o solo.
A) 15 m/s
B) 30 m/s
C) 45 m/s
D) 90 m/s
E) 60 m/s
// Comentário: Na queda livre, 45 = 5·t², logo t = 3 s, e v = g·t = 30 m/s. Também v² = 2·g·h = 900. O valor 90 m/s seria o quadrado da velocidade.

@@ a03/s01 | D
Uma pedra é lançada verticalmente para cima com velocidade inicial de 20 m/s, em local onde g = 10 m/s², desprezada a resistência do ar. Assinale a opção que apresenta a altura máxima atingida em relação ao ponto de lançamento.
A) 10 m
B) 40 m
C) 30 m
D) 20 m
E) 25 m
// Comentário: No ponto mais alto a velocidade é nula, então v² = v0² − 2·g·h, ou seja, 0 = 400 − 20·h e h = 20 m. O tempo de subida é 2 s e h = 20·2 − 5·4 = 20 m. O valor 40 m resulta de dividir v0² por g, esquecendo o fator 2.

@@ a03/s01 | A
Uma bola é lançada verticalmente para cima com velocidade de 30 m/s, em local onde g = 10 m/s². Desprezando o ar, assinale a opção que apresenta o tempo total para retornar ao ponto de lançamento.
A) 6 s
B) 3 s
C) 9 s
D) 4,5 s
E) 12 s
// Comentário: O tempo de subida é v0/g = 3 s e o de descida até o mesmo nível é igual, 3 s, totalizando 6 s. O valor 3 s é só o tempo de subida.
""",
"direito-constitucional": """
@@ c05/s01 | C
No que se refere à relação entre a nova Constituição e as situações constituídas sob a ordem anterior, segundo a jurisprudência do Supremo Tribunal Federal, assinale a opção correta.
A) O direito adquirido sob a Constituição anterior prevalece sobre a nova Constituição, por ser garantia absoluta.
B) A nova Constituição só revoga a anterior nos pontos em que declara expressamente a revogação.
C) Não há direito adquirido em face do poder constituinte originário, salvo se o próprio texto constitucional o ressalvar.
D) A nova Constituição só produz efeitos para o futuro, vedada sua incidência sobre fatos já consumados em qualquer hipótese.
E) O poder constituinte originário está sujeito às cláusulas pétreas da Constituição anterior.
// Comentário: O poder constituinte originário é inicial e ilimitado juridicamente, e por isso o direito adquirido não pode ser oposto à nova Constituição, a não ser que ela mesma o preserve. A nova Constituição revoga globalmente a anterior, e as cláusulas pétreas limitam apenas o poder reformador.

@@ c05/s01 | E
Quanto ao controle de constitucionalidade de leis editadas antes da vigência da Constituição de 1988, que se mostrem materialmente incompatíveis com ela, assinale a opção correta.
A) Cabe ação direta de inconstitucionalidade perante o Supremo Tribunal Federal, por violação à nova Constituição.
B) Cabe ação declaratória de constitucionalidade, para confirmar a revogação da lei anterior.
C) Não cabe qualquer controle concentrado, só o difuso, por ser matéria de recepção.
D) A lei anterior é declarada inconstitucional com efeitos retroativos desde a sua edição.
E) A lei é considerada não recepcionada ou revogada, e sua análise pode ser feita em arguição de descumprimento de preceito fundamental.
// Comentário: A lei anterior incompatível com a nova Constituição não é inconstitucional: é revogada (não recepcionada). O STF admite a ADPF para esse exame, e a ADI não cabe contra direito pré-constitucional.

@@ c05/s01 | A
Acerca dos efeitos da promulgação de uma nova Constituição sobre a Constituição anterior, assinale a opção correta.
A) A nova Constituição revoga integralmente a anterior, ainda que não haja norma expressa nesse sentido, pois há substituição da ordem constitucional.
B) A Constituição anterior permanece em vigor em tudo que não for expressamente revogado pela nova.
C) As normas da Constituição anterior compatíveis com a nova mantêm sua natureza constitucional.
D) A revogação da Constituição anterior depende de lei que regulamente a transição.
E) A Constituição anterior continua vigendo em relação às matérias que a nova deixou de disciplinar.
// Comentário: A nova Constituição revoga por inteiro a anterior, por ser expressão de nova ordem constitucional, sem depender de revogação expressa. As normas anteriores compatíveis podem ser recepcionadas como infraconstitucionais, mas perdem a natureza constitucional.
""",
}
for f, q in NEW.items():
    p = f"content/questoes/ineditas/mc/{f}.txt"
    s = open(p, encoding="utf-8", newline="").read()
    crlf = "\r\n" in s
    s = s.replace("\r\n", "\n")
    if not s.endswith("\n"): s += "\n"
    # enunciado sem comando ganha o prefixo do padrão das demais questões
    blocks = q.strip("\n").split("\n@@ ")
    fixed = []
    for b in blocks:
        L = b.split("\n")
        i = 1
        if "assinale a opção" not in L[i].lower():
            L[i] = "Considerando o que dispõe a norma, assinale a opção correta: " + L[i]
        fixed.append("\n".join(L))
    s += "\n@@ " + "\n@@ ".join(fixed).lstrip("@ ") if False else "\n" + "\n".join(("@@ " if not x.startswith("@@") else "") + x + "\n" for x in fixed)
    open(p, "w", encoding="utf-8", newline="\r\n" if crlf else "\n").write(s)
