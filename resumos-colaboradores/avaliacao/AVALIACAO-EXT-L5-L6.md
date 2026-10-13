# Avaliação de qualidade dos resumos: EXT-L5 (Matemática + Física) e EXT-L6 (Química + Língua Espanhola)

Data: 2026-10-12. Padrão de referência: `resumos-colaboradores/INSTRUCOES.md`. Método: cada resumo foi lido por inteiro e conferido contra o texto-fonte do trecho (`summary_source.py`); fórmulas e exemplos foram refeitos; foi feita checagem automática de sobreposição de n-gramas com a fonte (4, 5, 6 e 8 palavras) e contagem de palavras, seções, tabelas, negritos e destaques. Escala: 1 a 5 (5 = excelente).

Observação sobre a amostra: o sorteio de EXT-L6 não trouxe nenhum resumo de Língua Espanhola; os cinco são de Química. Portanto, **nada foi avaliado de Espanhol**: o veredito de EXT-L6 vale para o trabalho em Química e não diz nada sobre os resumos de Espanhol do mesmo lote (recomenda-se sortear 2 a 3 de Espanhol).

---

## (a) Resultado por agente

| Agente | Cobertura | Correção | Originalidade | Clareza/didática | Tamanho/formato | Média geral |
| --- | --- | --- | --- | --- | --- | --- |
| EXT-L5 (S0590, S0593, S0611, S0647, S0660) | 3,8 | 4,8 | 3,4 | 3,0 | 3,2 | 3,6 |
| EXT-L6 (S0588, S0631, S0651, S0654, S0723) | 3,0 | 4,6 | 3,8 | 3,4 | 3,2 | 3,6 |

### Veredito EXT-L5: APROVADO COM RESSALVAS
- Pontos fortes verificados: todas as contas, fórmulas e resultados numéricos conferem (refiz cada exemplo resolvido; nenhum erro de cálculo). O agente achou e registrou um erro tipográfico real da fonte (S0647: "52,12 × 10³" no lugar de 54,12) e reinterpretou corretamente o enunciado inconsistente de S0660.
- Ressalvas: (1) os resumos são curtos para o alvo do índice (entre 27% e 39% do alvo; ver tabela de tamanhos), (2) os exemplos resolvidos são os mesmos do material, com os mesmos números e na mesma ordem (S0590, S0647, S0660), (3) nenhum dos cinco usa tabela, negrito ou bloco de destaque no analítico (a seção 5 pede tabelas para comparações e negrito para regras-chave), (4) três dos cinco sintéticos não seguem o formato "**Ponto**: explicação" (S0611, S0647, S0660), (5) S0647 provavelmente deixou de fora a tabela de prefixos do trecho sem registrar em NOTAS.
- Nenhuma refação integral necessária; precisa de **correções pontuais** (S0647, S0660, S0611, S0593).

### Veredito EXT-L6 (Química): APROVADO COM RESSALVAS, com refação obrigatória de S0651 e varredura do restante do lote
- Pontos fortes verificados: nenhum erro conceitual nem de balanceamento nos cinco (conferi todas as equações, cargas e somas de coeficientes: 35, 36, 19). Originalidade textual boa (nenhuma sequência de 8 palavras igual; no máximo 7 janelas de 6 palavras, todas em frases genéricas ou fórmulas). S0588 é o melhor resumo da amostra.
- Ressalvas graves: **cobertura**. O padrão é omitir o que está dentro do intervalo de páginas mas fora da lista de assuntos do índice (S0651: nove métodos de separação ausentes, incluindo separação magnética, que cai em prova) e omitir tópicos que estão na lista (S0723: "divisão entre metais e ametais"). Também suprime quase todos os exemplos resolvidos de balanceamento que são o conteúdo central de S0631 e S0654 (só o resultado final aparece).
- Como o padrão de omissão se repete em 3 dos 5 (S0651, S0723, S0654) e pode afetar o restante do lote de Química, a recomendação é: refazer S0651; complementar S0631, S0654 e S0723; e **conferir por amostra ampliada** (3 a 5 resumos adicionais de Química) se o agente deixa tópicos de fora quando o trecho tem mais assuntos do que a lista do índice. Se a segunda amostra repetir a omissão, a recomendação passa a ser REPROVAR LOTE para Química.
- Língua Espanhola: **não avaliada** (ver observação acima).

### Tamanho do analítico (palavras por contagem simples) × alvo do índice

| ID | Páginas | Analítico | Alvo | % do alvo | Piso | Sintético (palavras / pontos) | Seções `###` | Itens de "Para fixar" |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S0590 | 7 | 379 | 1.050 | 36% | 250 | 124 / 8 | 3 | 7 |
| S0593 | 12 | 490 | 1.800 | 27% | 360 | 154 / 10 | 4 | **10** |
| S0611 | 9 | 522 | 1.350 | 39% | 270 | 160 / 8 | 3 | 8 |
| S0647 | 9 | 424 | 1.350 | 31% | 270 | 135 / 8 | 4 | 8 |
| S0660 | 11 | 524 | 1.650 | 32% | 330 | **101** / 6 | 4 | 7 |
| S0588 | 12 | 653 | 1.800 | 36% | 360 | 114 / 7 | 5 | 8 |
| S0631 | 10 | 464 | 1.500 | 31% | 300 | 140 / 8 | 3 | 8 |
| S0651 | 17 | 446 | 2.000 | **22%** | 400 | 156 / 8 | 4 | 8 |
| S0654 | 15 | 425 | 2.000 | 21% | 400 | 147 / 8 | 4 | 8 |
| S0723 | 10 | 437 | 1.500 | 29% | 300 | 132 / 8 | 3 | 7 |

Notas sobre a tabela: o verificador oficial aceita todos (ele conta fórmulas como várias "palavras"); por contagem simples por espaços, o sintético de S0660 tem 101 palavras (abaixo de 110) e o "Para fixar" de S0593 tem 10 itens (a seção 5 pede 5 a 8). Em S0651 e S0654 o analítico mal passa do piso, e é exatamente neles que falta conteúdo. A instrução diz que "o tamanho é o que o conteúdo pedir", mas a comparação com a cobertura mostra que o agente está parando perto do piso e não do que o trecho exige.

---

## (b) Avaliação por resumo

### S0590 (Matemática, Regra de Três Simples e Composta; págs. 3-9)
Notas: Cobertura 4 · Correção 5 · Originalidade 3 · Clareza 3 · Tamanho/formato 4. **Ação: CORREÇÃO PONTUAL.**
- Cobertura/correção: os dois assuntos do índice estão lá e todos os números conferem: 4/6 = 54/x dá x = 81; estoque de 6.000 pessoa-dias dá 24 dias para 250 pessoas; na composta, x/6 = (42/28)·(8/6) dá x = 12. A conferência "50% a mais de pessoas, 25% a menos de tempo, fator 1,5 × 8/6 = 2" está correta e é uma boa adição. O mnemônico "cruzado na direta, direto na inversa" foi preservado em outras palavras.
- Faltas: não há exemplo de composta com mais de uma relação inversa nem a pegadinha clássica (confundir o sentido ao comparar com a incógnita). A tabela de organização das grandezas, que é o centro do método, é só descrita, nunca montada (poderia ser uma tabela markdown).
- Originalidade: o texto está parafraseado, mas **os três exemplos são exatamente os do material, com os mesmos números** (4 médicos/54 pacientes, 200 pessoas/30 dias, 6 servidores/28 pessoas/8 horas). A instrução manda "trocar exemplos". O verificador de 10 palavras não pega isso (somente janelas curtas de 4 a 6 palavras coincidem: "médicos atendem 54 pacientes por dia", "servidores atendem 28 pessoas em 8 horas").
- Clareza: correta, mas o último parágrafo da seção composta ("constante de proporcionalidade ... expressar a relação") é vago e não ensina nada acionável.
- Sintético: 8 pontos coerentes, mas 2 são só repetição dos exemplos e 3 ("Comparação", "Inversão", "Conferência") são genéricos.

### S0593 (Física, Trabalho, energia e potencial eletrostático; págs. 15-26)
Notas: Cobertura 4 · Correção 5 · Originalidade 4 · Clareza 3 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL (complementar).**
- Cobertura: todos os oito assuntos do índice aparecem (potencial, energia potencial, comportamento das cargas, trabalho, equipotenciais, condutores, capacitância, energia consumida). Correção: V = kQ/r, Ep = qV, τ = q(Vi − Vf), |U| = E·d, C = Q/V, C = R/k, cargas finais proporcionais aos raios, E = P·Δt em kWh, tudo certo. A explicação de que a carga negativa vai a maior potencial mas reduz Ep está correta e é o ponto que mais derruba aluno.
- Faltas: nenhum exemplo numérico de carga/potencial/capacitância (só o do kWh: 1,5 kW × 4 h = 6 kWh); o texto-fonte tem a divisão de cargas entre esferas de raios diferentes e o gráfico de E e V da esfera (campo máximo na superfície, nulo no interior, V cai fora), e o resumo só diz "fora, comporta-se como carga puntiforme" sem as relações. Não menciona que o Ep se mede em joule nem a unidade W·h do contexto.
- NOTAS "nenhuma" é imprecisa: a fórmula da capacitância da esfera foi **perdida na extração do PDF** (a fonte mostra a equação em branco depois de "Para um condutor esférico, podemos dizer que:"), e o agente a preencheu com C = R/k a partir do próprio conhecimento. O valor está correto, mas a instrução manda registrar em NOTAS o que não pôde confirmar na fonte.
- Formato: "Para fixar" com 10 itens (limite 8) e sintético com 10 pontos (limite 12, ok). Quase todo o texto é fórmula encadeada, sem tabela (poderia haver uma tabela "tipo de grandeza × fórmula × unidade").
- Originalidade: parafraseado, seguindo a mesma ordem dos tópicos da fonte, sem janelas copiadas de 6+ palavras.

### S0611 (Física, Estática dos fluidos e Teorema de Stevin; págs. 3-11)
Notas: Cobertura 4 · Correção 4 · Originalidade 4 · Clareza 3 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL.**
- Contas: p_atm = 13,6×10³ × 9,8 × 0,76 ≈ 1,01×10⁵ Pa (confere); coluna de água 1,01×10⁵ / (10³ × 9,8) ≈ 10,3 m (confere); 30 psi ≈ 2,1×10⁵ Pa (confere com 6,9×10³ Pa por psi).
- **Divergência com a fonte, não sinalizada**: o texto-fonte usa 1 psi ≈ 7,0×10³ N/m² e define "atm" como a atmosfera técnica (1 kgf/cm² = 10⁵ N/m²). O resumo põe 6,9×10³ (valor fisicamente mais exato) e chama 1,01×10⁵ Pa de "atmosfera padrão", misturando as duas. A NOTA diz "foram preservados os valores aproximados do material", o que não é verdade para o psi. Para a prova (AOCP) o aluno pode ver 1 atm = 10⁵ Pa em enunciado; vale o resumo dizer que atm técnica e padrão diferem pouco.
- Violação da regra de originalidade/anonimato: o analítico diz "o material também usa a equivalência aproximada 1 kgf/cm² ≈ 10⁵ Pa" (a seção 8 proíbe citar "o material"). Também a NOTA cita "o material", o que é aceitável só lá.
- Cobertura: Stevin, pressão, densidades e Torricelli estão; falta exemplo resolvido de pressão a uma profundidade (por exemplo, a 10 m de água a pressão absoluta é cerca de 2 atm) e a tabela de massas específicas do material. A parte conceitual (massa específica a pressão) não tem um `###` próprio, só a abertura (3 seções `###` no total contando "Para fixar").
- Formato: o sintético não usa o formato "**Ponto**: explicação" (são frases soltas com "- "); o primeiro ponto mistura três assuntos.

### S0647 (Matemática, Unidades de medida; págs. 6-14)
Notas: Cobertura 3 · Correção 5 · Originalidade 3 · Clareza 3 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL.**
- Correção: todas as conversões conferem (54,12 dam = 54.120 cm; 345,1 hg = 34.510 g; 52,7 hL = 527.000 cL; 10⁹·6×10⁻⁶·11 = 66.000; 15×10⁹ / 3×10⁻⁵ = 5×10¹⁴). A NOTA sobre o erro "52,12 × 10³" da fonte é real e correta. A frase final sobre área e volume (fator 100 e 1.000 por passo) está certa e é útil (não está no trecho, mas evita erro).
- Cobertura: o índice lista "Prefixos das unidades de medida", e o fim da fonte (pág. 14) termina com "Os prefixos utilizados são os seguintes:" seguido de tabela que a extração não trouxe. O resumo lista só quilo, hecto, deca, deci, centi e mili e não registra em NOTAS que a tabela estava cortada; é muito provável que a tabela original traga mega, giga, micro, nano etc. (**revisão humana**). Também faltam: as conversões "para a esquerda" com exemplo (dm para km, cg para kg, mL para daL; só o texto da regra), a expressão do TRF 3 resolvida por notação científica, e 10⁰ = 1.
- Originalidade: **todos os sete exemplos numéricos são os do material** (542.000... = 5,42·10¹⁷, 0,000000076, 11·10⁹ × 6·10⁻⁶, 15·10⁹ / 3·10⁻⁵, 54,12 dam, 345,1 hg, 52,7 hL). Redação própria, mas zero exemplos novos. O agente confirma, na verdade, que repetiu as contas do material.
- Formato: o sintético não tem negrito nem a estrutura "Ponto: explicação"; o analítico usa "o grama é a unidade usada no trecho" (referência ao material). Falta tabela dos prefixos (o assunto é exatamente uma tabela).

### S0660 (Matemática, Taxas equivalentes; págs. 24-34)
Notas: Cobertura 4 · Correção 5 · Originalidade 3 · Clareza 3 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL (sintético e exemplos).**
- Correção: tudo certo, inclusive 1,05¹² = 1,7959 (79,59%), (1,04)³ = 1,124864 (12,49%), 1,05^(1/3) = 1,0164, raiz de 1,050625 = 1,025, e 36%/12 = 3%, (1,03)² = 1,0609. O resumo acertou onde a fonte erra: o gabarito da questão "Inédita 2022" (12% nominal, capitalização bimestral, taxa semestral efetiva) está como "Alternativa C" na fonte, mas o valor calculado (12,49%) é a alternativa D; o resumo calcula certo e adota "ao semestre" (a fonte escreve "ao ano" na resolução). A NOTA fala da inconsistência de rótulo, mas **não registra o gabarito errado da fonte**.
- Cobertura: falta o último exemplo da fonte (15% a.a. com capitalização quadrimestral dar taxa efetiva anual de 15,76%, que é o caso típico "nominal para efetiva anual") e a definição explícita de taxa efetiva. O sintético tem só 6 pontos (o mínimo) e ~101 palavras; não traz a fórmula geral nem o caso 5% a.m. dando 79,59% a.a. (contraexemplo dos 60%), portanto não cobre o trecho de ponta a ponta.
- Originalidade: os oito exemplos aparecem com os mesmos números e na mesma ordem da fonte (5% → 10,25%; 16% → 34,56%; 33,10% → 10%; 14,49% → 7%; 6% → 1% → 3,03%; 10% → 5% → 1,64%; 12% → 4% → 12,49%; 5% → 79,59%; 5,0625% → 2,5%; 36% → 3% → 6,09%), apenas encurtados.
- Clareza: a seção "Aplicações e exemplos de cálculo" é uma sequência de resultados em parágrafo corrido, sem passo a passo nem tabela de "o que o enunciado dá × o que fazer". A frase entre aspas "Quem define o período efetivo..." imita citação da fonte; remover as aspas.
- Formato: sintético sem negritos e sem o formato "Ponto: explicação".

### S0588 (Química, Equilíbrio químico, Le Châtelier e Kps; págs. 3-14)
Notas: Cobertura 4 · Correção 5 · Originalidade 4 · Clareza 4 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL (retirar referência ao "segmento seguinte").**
- Correção: sem erros. Q = 0,8²/0,16 = 4 = K confere; Q < K / Q > K, Kw, pH + pOH = 14, Kps = x², K' = 1/Kps estão certos. O agente também corrige, sem avisar, o erro da fonte que define o pOH como "logaritmo negativo da concentração de H⁺" (pág. 13).
- Cobertura: tópicos do índice e as demais constantes (Kw, Ka, Kb) presentes. Faltam o número do Kps do BaSO₄ (1,0×10⁻¹⁰) e a solubilidade resultante (1,0×10⁻⁵ mol/L), que mostram o "Kps = x²" funcionando, e a K' = 1,0×10¹⁰ do exemplo. Falta o aviso de que, em fase gasosa, a água entra na expressão de K (pegadinha cobrada em questão do trecho). O sintético tem pontos sem a conclusão ("Excesso em água pura dá concentrações iguais" sem dizer que Kps = x²; "Inverter a reação inverte K" sem dizer 1/K).
- Quebra de regra: "O segmento seguinte desenvolve cálculos de tais constantes" (analítico) e NOTAS "aparecem em outro trecho": a seção 14 proíbe remeter a outros trechos; deve ser removido do analítico.
- Formato: sintético sem negritos/estrutura "Ponto: explicação"; 7 pontos, 114 palavras (no limite). Nenhuma tabela, embora Le Châtelier (concentração, temperatura, pressão × sentido) seja o caso de ouro para uma.
- Originalidade: bem parafraseado (no máximo 2 janelas de 5 palavras); mantém os mesmos sistemas-exemplo (N₂O₄, NH₃, BaSO₄).

### S0631 (Química, Balanceamento redox e meio básico; págs. 166-175)
Notas: Cobertura 3 · Correção 4 · Originalidade 4 · Clareza 3 · Tamanho/formato 4. **Ação: CORREÇÃO PONTUAL (complementar com semirreações).**
- Correção: 3Br₂ + 6OH⁻ → BrO₃⁻ + 5Br⁻ + 3H₂O (átomos e carga conferem), 2KMnO₄ + 16HCl → 2KCl + 2MnCl₂ + 8H₂O + 5Cl₂ (soma 35, correta; a fonte escreve a soma com um "3" digitado no lugar de 5 e o resumo acerta). A NOTA sobre o "Mn e S" copiados no passo 1 do bromo é real e boa.
- Problema de correção/clareza: a descrição de meio básico ("também se pode equilibrar O com água e H mediante H₂O/OH⁻, de modo que o meio final não conserve H⁺ livre") é vaga; a conversão correta (somar OH⁻ aos dois lados até eliminar H⁺) só aparece no parágrafo seguinte, de forma genérica.
- Cobertura: o núcleo do trecho são os 7 passos com **semirreações escritas**; o resumo não escreve nenhuma semirreação (nem MnO₄⁻ + 8H⁺ + 5e⁻ → Mn²⁺ + 4H₂O, que é a mais cobrada) nem demonstra o meio básico do bromo passo a passo. Também omite os resultados dos outros três exercícios do trecho: MnO₄⁻ + H₂SO₃ (2MnO₄⁻ + 5H₂SO₃ + H⁺ → 2Mn²⁺ + 5HSO₄⁻ + 3H₂O), Cr₂O₇²⁻ + I⁻ (Cr₂O₇²⁻ + 14H⁺ + 6I⁻ → 2Cr³⁺ + 7H₂O + 3I₂, com a expressão de Q correspondente) e CuS + NO₃⁻ (3CuS + 2NO₃⁻ + 8H⁺ → 3Cu²⁺ + 3S + 2NO + 4H₂O). O "Para fixar" e o sintético são só procedimento.
- Sintético: o ponto "Estados físicos" é desvio do tema (vem de uma questão de Q); nenhum ponto traz número concreto (5 e⁻ do Mn, soma 35).
- Originalidade: sem sobreposição (0 janelas de 4 palavras).

### S0651 (Química, Métodos de separação; págs. 18-34)
Notas: Cobertura 2 · Correção 4 · Originalidade 4 · Clareza 3 · Tamanho/formato 3. **Ação: REFAÇÃO.**
- O resumo cobre só os dez assuntos listados no índice. As 17 páginas do trecho incluem, além deles, **fusão fracionada, solidificação fracionada, levigação, ventilação, peneiramento (tamisação), flotação, floculação, separação magnética e dissolução fracionada**, todos com definição e exemplo, e há questões comentadas do trecho que cobram separação magnética (ferro × alumínio) e a ordem de operações em mistura areia/sal/óleo/água. Nada disso aparece. Também faltam: coeficiente de distribuição K = [S]fase 2 / [S]fase 1 (extração líquido-líquido), densidades relativas de solventes (éter, tolueno e hexano menos densos que a água; clorofórmio, diclorometano e CCl₄ mais densos; "cloro tende a ser mais denso"), as quatro etapas da extração com funil, a filtração simples (papel pregueado), os componentes da filtração a vácuo (funil de Büchner, kitassato, bomba de vácuo, papel umedecido), e os critérios do solvente de cristalização (P.E. do solvente menor que P.F. do composto, baixa toxicidade e inflamabilidade).
- O que está lá está correto: Soxhlet (ciclo, economia de solvente, saturação), cristalização × precipitação, ordem filtração, funil, método de recuperação do sal.
- O agente diz em NOTAS que "nenhuma dificuldade impediu resumir as operações principais", o que contraria a ausência dos nove métodos; o trecho começa no meio da explicação de arraste de vapor (pág. 18), e o resumo o tratou como assunto completo.
- Tamanho: 446 palavras para 17 páginas é 22% do alvo e só 11% acima do piso; é o caso em que a brevidade causa perda de cobertura.

### S0654 (Química, Balanceamento com íons pelo método misto; págs. 25-39)
Notas: Cobertura 3 · Correção 5 · Originalidade 4 · Clareza 3 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL (complementar).**
- Correção: Bi₂O₃ + 2NaClO + 2NaOH → 2NaBiO₃ + 2NaCl + H₂O (confere), 3Br₂ + 6OH⁻ → BrO₃⁻ + 5Br⁻ + 3H₂O, Cr₂O₇²⁻ + 14H⁺ + 6Fe²⁺ → 2Cr³⁺ + 7H₂O + 6Fe³⁺ (carga 24 = 24, soma 36).
- Cobertura: o centro do trecho é o balanço de carga em íons, mas o primeiro exemplo (Pb + Al³⁺, para mostrar por que contar átomos não basta e que a equação de carga é obrigatória) e o ClO⁻ + CrO₂⁻ + OH⁻ → Cl⁻ + CrO₄²⁻ + H₂O (3, 2, 2, 3, 2, 1) estão ausentes. Também faltam a exceção "o elemento de maior subíndice (H) pode não ser a melhor escolha quando dois compostos recebem o mesmo coeficiente" (exemplo FeSO₄/KMnO₄/H₂SO₄, o exercício que a própria fonte classifica como o difícil) e o exemplo MnO₂ + NaI + H₂SO₄. O Br₂ é citado só com a equação final; a passagem pela fração 1/3 e 5/3, que é o ponto didático, não aparece.
- NOTAS genérica: "pequenos erros de rótulo em comentários/exemplos do trecho" não diz qual (a instrução pede ponto, local e motivo). Erros reais da fonte que merecem registro: página 28 rotula "Na:" no balanço de enxofre; página 38 escreve "7 Cr³⁺" onde deveria ser 2 Cr³⁺ na legenda; as listas de verificação trocam "lado direito/esquerdo".
- Originalidade: bem parafraseado, mas os três exemplos escolhidos são os da fonte; a frase "elementos que aparecem uma única vez" repete a expressão do material (janela de 6).
- Notação de carga inconsistente no analítico ("Fe²+" ao lado de "Cr³+").

### S0723 (Química, Balanceamento: regras gerais e MACHO; págs. 3-12)
Notas: Cobertura 3 · Correção 5 · Originalidade 3 · Clareza 4 · Tamanho/formato 3. **Ação: CORREÇÃO PONTUAL (complementar).**
- Correção: Fe₂(SO₄)₃ = 2 Fe, 3 S, 12 O; Fe₄[Fe(CN)₆]₃ = 7 Fe, 18 C, 18 N; Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂; 2C₂H₆ + 7O₂ → 4CO₂ + 6H₂O (soma 19). Tudo certo.
- Cobertura: o índice lista **"Divisão entre metais e ametais"** e o resumo não a explica (é pré-requisito do M e do A de MACHO: onde ficam metais e ametais na tabela periódica). Falta também a regra de que, no MACHO, "A" exclui C, H e O (que têm letra própria), os exemplos em que um coeficiente já definido precisa ser refeito (NH₄Cl + Ba(OH)₂: o coeficiente do cloreto de amônio vira 2 e o do amoníaco também), o caso Cl em dois produtos (MnO₂ + HCl) e o cuidado de reduzir ao menor inteiro (12Fe + 9O₂ → 6Fe₂O₃ vira 4Fe + 3O₂ → 2Fe₂O₃). O resumo trata só do cuidado de "fração para inteiro".
- Originalidade: Fe₂(SO₄)₃, Fe₄[Fe(CN)₆]₃, Na₂CO₃ + HCl e etano são exatamente os exemplos do material; a sobreposição de n-gramas é a mais alta da amostra (7 janelas de 6 palavras, todas em frases de definição de contagem de átomos), embora nenhuma de 8.
- Clareza: boa; o único resumo da amostra com exemplo resolvido passo a passo. NOTAS "nenhuma" omite que a última página do trecho termina antes da resolução do exemplo 12Fe + 9O₂.
- Sintético: item "Estruturas" ocupa um dos 8 pontos para tema secundário, enquanto "metais e ametais" não aparece.

---

## (c) Padrões recorrentes

### EXT-L5
1. **Resumos corretos e enxutos demais**: 27% a 39% do alvo do índice, quase sempre na faixa baixa permitida. Para Exatas, o que se perde é o exemplo resolvido novo e a tabela de organização, não a fórmula.
2. **Reaproveita os exemplos do material com os mesmos números e na mesma ordem** (S0590, S0647, S0660). O texto é parafraseado, mas o aluno que já tem o material não recebe exemplo novo, e a regra de "trocar exemplos" não é cumprida. O verificador de 10 palavras não detecta isso.
3. **Nenhuma tabela, negrito ou bloco de destaque** em nenhum dos cinco analíticos, embora a seção 5 peça tabelas para comparações (direta × inversa, prefixos, fórmulas e unidades) e negrito para regras-chave.
4. **Sintético sem o formato "Ponto: explicação"** em 3 de 5, e dois sintéticos com pontos que são só exemplo ou lema genérico.
5. **Não registra falhas da fonte que contornou**: formula em branco (S0593), tabela cortada (S0647), gabarito errado (S0660), conversão alterada (S0611). Registra, porém, um erro tipográfico real (S0647), o que mostra que lê com atenção; o problema é inconsistência.
6. Menção ao material ("o material", "no trecho") em S0611 e S0647.

### EXT-L6 (Química)
1. **Omite o que está no intervalo de páginas mas fora da lista do índice** (S0651, nove métodos) e **omite assuntos da lista** (S0723, metais e ametais). É o defeito mais grave porque o aluno acredita que o resumo substitui a leitura.
2. **Entrega o resultado final de balanceamento sem a construção** (S0631 sem semirreações; S0654 sem os exemplos iônicos). Em Química de concurso, o passo a passo é a coisa cobrada.
3. **Excelente correção química** (nenhum erro nas 15+ equações conferidas), boa paráfrase (nenhuma janela de 8 palavras) e uma boa capacidade de corrigir silenciosamente erros da fonte (pOH em S0588, soma dos coeficientes em S0631).
4. **NOTAS genéricas ou "nenhuma"** quando a fonte tem falhas (S0654, S0723, S0588) e afirmação enganosa em S0651 ("nenhuma dificuldade").
5. **Sem tabela, sem negrito e sem blocos de destaque** em nenhum dos cinco; Le Châtelier, métodos de separação e MACHO pediam tabela.
6. Referência a outro trecho (S0588: "O segmento seguinte...").
7. Nenhum exemplo novo: todos são os da fonte (N₂O₄, BaSO₄, Br₂, Bi₂O₃, Na₂CO₃ + HCl, etano).

---

## (d) REVISÃO HUMANA

### Pontos duvidosos encontrados por mim (abrir o PDF para confirmar)
| ID | Ponto | Motivo |
| --- | --- | --- |
| S0647 | Tabela de prefixos no fim da pág. 14 (índice "Prefixos das unidades de medida") | A extração termina em "Os prefixos utilizados são os seguintes:" sem a tabela. O resumo só tem os seis prefixos já mostrados nas escalas. Conferir se o PDF traz mega, giga, tera, micro, nano, pico etc. e, se trouxer, incluir. |
| S0593 | Fórmula da capacitância da esfera (pág. 24) e gráficos de E e V da esfera condutora (pág. 23) | A fórmula estava em branco no texto extraído; o resumo usa C = R/k (correto fisicamente). Conferir no PDF se há mais relações (por exemplo C = 4πε₀R) e se há valores numéricos para incluir. |
| S0611 | 1 psi ≈ 7,0×10³ (fonte) × 6,9×10³ (resumo); 1 atm = 10⁵ Pa (técnica, na fonte) × 1,01×10⁵ Pa (padrão, no resumo) | O resumo mudou o valor e misturou os dois conceitos de atmosfera sem avisar. Decidir qual referência o produto adota e alinhar as NOTAS. |
| S0660 | Questão "Inédita 2022" (12% nominal, capitalização bimestral): gabarito da fonte "C" × cálculo 12,49% (alternativa D) | Erro do material; o resumo calculou certo. Confirmar no PDF e registrar em NOTAS. Também o enunciado diz "semestral" e a resolução diz "anual". |
| S0651 | Se a ausência de levigação, ventilação, peneiramento, flotação, floculação, separação magnética, dissolução fracionada, fusão e solidificação fracionadas é intencional | Todas estão nas págs. 19 e 31-34. Não são assuntos "do índice" mas são do intervalo de páginas. Decidir se entram (recomendado) ou se o intervalo do índice deve ser reduzido. |
| S0723 | "Divisão entre metais e ametais" (págs. 7-8) | Assunto listado no índice, não coberto. A fonte usa uma figura da tabela periódica colorida (não extraível); o resumo precisa descrevê-la em texto (metais à esquerda e no centro, ametais à direita, semimetais na fronteira, gases nobres). |
| S0723 | Última página (pág. 12) termina em "12 Fe + 9 O₂ → 6 Fe₂O₃" sem a resolução | Truncamento possível; o raciocínio é "reduzir ao menor inteiro" (4 : 3 : 2). Registrar em NOTAS. |
| S0654 | Erros do material não registrados em NOTAS | Pág. 28 rótulo "Na:" no balanço de S; pág. 38 "7 Cr³⁺"; trocas "lado direito/esquerdo" nas verificações. |
| S0588 | Pegadinhas da fonte omitidas | Em fase gasosa a água entra na expressão de K; o exemplo numérico de Kps do BaSO₄ (1,0×10⁻¹⁰). |
| Lote L6 | Língua Espanhola | A amostra não incluiu nenhum resumo de Espanhol. Sortear pelo menos 3 para verificar conjugações, tradução e vocabulário colado de tabelas. |

### Itens relevantes das NOTAS dos 10 resumos
| ID | NOTA do agente | Observação |
| --- | --- | --- |
| S0590 | nenhuma | Plausível; sem falhas relevantes na fonte. |
| S0593 | nenhuma | Impreciso: a fórmula da capacitância da esfera veio em branco. |
| S0611 | Conversões de atm e psi "preservadas" | Divergente: psi mudou de 7,0 para 6,9×10³. Revisar. |
| S0647 | Erro "52,12 × 10³" na fonte | Correto e verificado. Falta registrar a tabela de prefixos cortada. |
| S0660 | Erros de OCR; rótulo temporal inconsistente em um exercício; "12% nominal" reinterpretado | Correto, mas incompleto: falta o gabarito errado (C × D). Texto confuso ("a resolução a reinterpreta como anual"): revisar redação. |
| S0588 | Figuras convertidas em texto; segmento termina em Ka/Kb | O trecho "aparecem em outro trecho" quebra a regra de não remeter a outros trechos. Falta o erro do pOH na fonte. |
| S0631 | Erro tipográfico "Mn e S" no desproporcionamento do Br₂ | Correto e verificado. Outros erros da fonte não registrados (soma "2+16+2+2+8+3+5", "KCr₂O₇", "NO (aq)", conversões do H em meio básico escritas com "12 H₂O"). |
| S0651 | Imagens de Soxhlet e vidrarias omitidas; nenhuma dificuldade | O resumo deixou de fora nove métodos; a afirmação de "nenhuma dificuldade" não procede. |
| S0654 | "Pequenos erros de rótulo" e notação embaralhada | Genérico; especificar. |
| S0723 | nenhuma | Omite o truncamento da última página e o assunto metais/ametais não coberto. |

### Itens extras para o responsável
- Nenhum resumo da amostra contém `�`, expressões proibidas literais do conferidor, nem trecho de 10 palavras copiado; mas as referências a "o material" (S0611), "no trecho" (S0647) e "o segmento seguinte" (S0588) estão contra a seção 8 e a seção 14.
- O verificador automático (`verificar_resumos.py`) aprova os 10 e não detecta: exemplos copiados, itens de "Para fixar" acima de 8, sintético fora do formato "Ponto: explicação", tópicos do índice não cobertos, nem omissões do intervalo de páginas. Sugestão: acrescentar ao verificador (a) aviso quando o analítico tiver menos de 30% do alvo em trecho com mais de 8 páginas, (b) aviso de lista "Para fixar" fora de 5 a 8 itens, (c) aviso quando o sintético não usa negrito no início do ponto, (d) aviso de analítico sem nenhuma tabela, negrito ou destaque.
