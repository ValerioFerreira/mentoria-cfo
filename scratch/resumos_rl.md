# TRECHO: raciocinio-logico/a00/s02
##### raciocinio-logico/a00/s02
Este trecho aprofunda o critério do valor lógico único: o que é valor lógico, por que não importa saber se a frase é verdadeira, e os casos que ficam de fora (sentenças abertas, paradoxos e opiniões), com os quantificadores e seus símbolos.

### Frases que não são proposições: questões iniciais

- "Pelé é o maior jogador de futebol de todos os tempos!" é **exclamativa** e não é proposição. Chamar uma frase de "proposição exclamativa" é inventar um conceito: uma proposição **não pode** ser exclamativa. "Saia daqui!" é imperativa e exclamativa. "É justo que toda a população seja penalizada pelos erros de seus dirigentes?" é **interrogativa**, e portanto nem sequer é proposição (muito menos composta).

### Valor lógico

- **Valor lógico** é o resultado do juízo sobre uma proposição. Na lógica formal, pode ser **verdadeiro ou falso, mas não ambos**.
- Para reconhecer uma proposição **não é preciso saber se é verdadeira ou falsa no mundo real**: "Recife é a capital de Pernambuco" (V), "Taubaté é a capital do Ceará" (F) e uma afirmação sobre a quantidade de estrelas da Via Láctea (ninguém sabe) são proposições, pois são orações declarativas que admitem um único valor lógico. Só quando a questão exige o valor (em conteúdos que envolvem matemática: "5 + 2 = 8" é F; "5 > 2" é V) é preciso confrontar com os fatos.

### Sentenças abertas

- **Sentença aberta** é aquela cujo valor lógico depende de uma **variável** (ou de algo indeterminado). "x + 9 = 10" não é proposição: com x = 1 é V, com x = 3 é F. Resolver a equação ("x vale 1") é **forçar** a verdade e não vale para decidir se é proposição. Inequações como 61x² − 61x > 0 também são abertas.
- Atenção: equações que se **simplificam para um número** viram proposições. "3x + 4 − x − 3 − 2x = 0" reduz-se a "1 = 0" (proposição falsa); "0 · x = 5" reduz-se a "0 = 5" (falsa); "7 + 3 = 11" e "43 − 1 = 42" são proposições. Já "13 · x = 7" é aberta.
- **Pronomes sem referência** também geram sentença aberta: "Ele correu 100 metros em 9,58 s em 2009" (se "ele" for Usain Bolt, V; se for outra pessoa, F), "Ela foi a melhor aluna da turma em 2022"; "x + y é um número par" (duas variáveis); frase sobre a queda do índice de criminalidade "da cidade" em certo ano (qual cidade?). Já "Mario foi o diretor do Colégio Liceu em 2020" é proposição. Na questão do INSS, "quem mandou mensagem, lembrou-se e quer ser lembrado" é uma sentença aberta formada ao se deixar indeterminadas as pessoas da proposição P.
- As bancas nem sempre são rigorosas com pronomes: "Você estudou diariamente para essa prova" foi tratada como proposição simples na questão GOINFRA. Nesses casos, escolha a alternativa que é claramente declarativa e fechada.

### Quantificadores e símbolos

- Quantificadores fecham a sentença: trocando "ele" por "alguém", "Alguém correu 100 metros em 9,58 s em 2009" é proposição (V: Usain Bolt). "Existem tubarões em Pernambuco" é proposição com o quantificador "existe". **"Ninguém ensina ninguém"** é proposição (com a variante de "nenhum"), e **não** sentença aberta.
- Símbolos: **∀** (todo, para todo, para qualquer, qualquer que seja), **∃** (existe, algum, pelo menos um), **∄** (nenhum, não existe) e **∃!** (existe um único). "∃ x ∈ ℕ | x + 9 = 10" é **verdadeira** (x = 1); "∀ x ∈ ℕ | x + 9 = 10" é **falsa**.

### Paradoxos

- "Esta frase é uma mentira": se for V, é F; se for F, é V, o que leva ao absurdo de ser V e F ao mesmo tempo; logo **não é proposição**. Na questão do TRF1, o autor diz que sua maior prova de honestidade é declarar que continuará sendo desonesto: a frase é paradoxal, não é proposição, e portanto não se pode concluir que o enunciador é honesto.

### Opiniões

- Frases de **alta carga de subjetividade** ("Maria é formosíssima", comparações de beleza entre pessoas, "João é incrível") **não são proposições**. Mas há "jogo de cintura": "Ainda é cedo" foi tratada como proposição. Cuidado também com o motivo: "A Terra é um geoide?" não é proposição por ser **interrogativa**, e não por ser opinativa.

### Para fixar
- Não é preciso saber se a frase é verdadeira para saber que é proposição.
- Variável ou pronome sem referência → sentença aberta; equação que se reduz a número é proposição.
- ∀ e ∃ fecham a sentença; "ninguém" é quantificador.
- Paradoxos e opiniões não são proposições; "proposição exclamativa" não existe.
- Equação que se reduz a número (como 0 · x = 5) é proposição; equação que depende de x é aberta.


---

# TRECHO: raciocinio-logico/a00/s06
##### raciocinio-logico/a00/s06
Este trecho traduz frases para a linguagem simbólica, explica condição suficiente e necessária, nomeia as partes da condicional, apresenta a bicondicional (se e somente se) e resolve questões de valoração de proposições compostas.

### Tradução para a linguagem simbólica

- Na frase em que Ana, quando vai de ônibus **ou** de carro, leva guarda-chuva **e** dinheiro, a estrutura é uma condicional "Quando..., ...", cujo antecedente é uma disjunção e o consequente, uma conjunção: **(P ∨ Q) → (R ∧ S)**. Para traduzir, identifique primeiro o conectivo principal e depois os internos.

### Condição suficiente e condição necessária

- Em **p → q**, **p** é **condição suficiente** para q e **q** é **condição necessária** para p. Macete: a palavra "**se**" do "se... então" aponta a **condição suficiente**.
- "Se alguém estuda muitas horas, é aprovado": estudar muito é condição **suficiente** para ser aprovado, e ser aprovado é condição **necessária** para estudar muito. Afirmar que estudar é condição necessária para a aprovação **troca** os papéis (erro).
- Na tirinha "penso, logo existo" (p → e): pensar é condição **suficiente** para existir, e existir é condição **necessária** para pensar.
- **Condição necessária e suficiente** refere-se à **bicondicional**.
- **Nomes das partes**: a primeira parcela (p) é o **antecedente** (ou precedente) e a segunda (q) é o **consequente** (subsequente). Não confunda "condição suficiente" com "subsequente". Questões: a condicional é falsa **somente em V → F**, isto é, antecedente verdadeiro e consequente falso. Dizer que a condicional falsa exige antecedente falso, ou que é falsa quando os dois são falsos, é **errado**.

### Bicondicional (p ↔ q)

- "**Se e somente se**" (ou "se e só se", "assim como"), símbolo ↔. É **verdadeira quando as duas parcelas têm o mesmo valor** (V↔V ou F↔F) e **falsa quando os valores diferem**. Exemplo: "Hoje é 01/09 se e somente se hoje é o primeiro dia de setembro": as duas V (V) ou as duas F (V); só uma delas V é absurdo (F).
- "5 + 5 = 5 se, e somente se, 10 + 10 = 10" é **verdadeira**, pois as duas equações são falsas e têm o mesmo valor. Se p é falsa, p ↔ q **não** é sempre verdadeira: com q verdadeira, F ↔ V é falsa.
- **Formas de escrever**: "p assim como q", "p se e só se q", "**se p, então q e se q, então p**" e "**p somente se q e q somente se p**" (duas condicionais, uma de ida e outra de volta, ligadas por "e"). Logo, **p ↔ q ≡ (p → q) ∧ (q → p)**. Em frases do tipo "X é semelhante a Y **assim como** Z é semelhante a W", o conectivo é a bicondicional. Na questão em que se afirma uma condicional e, em seguida, a sua recíproca sobre os atos terem causa e não haver atos livres, a conclusão é que uma coisa vale **se e somente se** a outra vale.
- Na bicondicional, p é **condição necessária e suficiente** para q, e q para p.

### Resumo dos cinco conectivos (decorar)

- **Conjunção**: V só se as duas forem V. **Disjunção inclusiva**: F só se as duas forem F. **Disjunção exclusiva**: F se as duas tiverem o mesmo valor. **Condicional**: F só em V → F. **Bicondicional**: V se as duas tiverem o mesmo valor. Treine reescrevendo as cinco tabelas-verdade de memória.

### Questões de valoração

- Com A falsa, B verdadeira e C falsa: **(A ∧ B) → C** é F → F, portanto **V**; **(A ∨ B) ↔ ~C** é V ↔ V, portanto **V**; **(~A ∨ B) → C** é V → F, portanto **F** (resposta V, V, F).
- Se "Se a camisa é preta e a calça é branca, então o cinto é marrom ou o sapato é marrom" é **falsa**, o antecedente é V (camisa preta **e** calça branca) e o consequente é F (cinto **não** marrom **e** sapato **não** marrom). A única condicional verdadeira entre as opções é a que liga "cinto marrom" a "sapato marrom" (F → F).
- Se as afirmações "sou casado ou não sou policial" e "não tenho filho e não sou casado" são verdadeiras, a segunda dá filho F e casado F; para a primeira ser V com casado F, "não sou policial" tem de ser V. Conclusão: sem casamento, sem filho e sem ser policial.
- "Ana é engenheira **somente se** Bianca é arquiteta" é P → Q, logo Ana ser engenheira é **condição suficiente** para Bianca ser arquiteta. "Implica" também exprime a condicional, mas "não implica" não; dizer que Ana ser engenheira é condição necessária para Bianca ser arquiteta inverte o sentido (Q → P); e "se e somente se" é outro conectivo.

### Para fixar
- Em p → q, p é condição suficiente (o "se") e q é condição necessária.
- Condicional falsa apenas em V → F; bicondicional verdadeira quando as parcelas têm o mesmo valor.
- p ↔ q equivale a (p → q) ∧ (q → p); "assim como", "se e só se" e "condição necessária e suficiente" são bicondicional.
- "Somente se" é condicional, não bicondicional.
- Para resolver, comece pelo conectivo principal e valore as partes com os valores dados.


---

# TRECHO: raciocinio-logico/a00/s11
##### raciocinio-logico/a00/s11
Este trecho retoma, em outra ordem, as questões comentadas de proposições compostas e fecha a lista de proposições simples. Serve de revisão: aqui o foco é o método para valorar e para deduzir informações a partir de proposições compostas.

### Fecho das proposições simples (negação e equivalência)

- Os últimos itens da lista de negação do Cebraspe insistem em três armadilhas: (1) **"isso é bom" e "isso não é mau" não são equivalentes**, pois a negação de "bom" não é "mau" (algo pode não ser bom nem mau); (2) em "**Não quero ser ninguém** além de mim", a negação dupla do português é ênfase, e a negação lógica é "quero ser alguém além de mim"; (3) ao negar uma frase com oração subordinada, **nega-se a principal e preserva-se a subordinada**. Os gabaritos dessa lista seguem esses critérios.

### Método para resolver questões de compostas

1. **Liste as proposições simples** e escreva cada uma de forma afirmativa (letras p, q, r...), anotando as negações à parte.
2. **Atribua valores** às simples a partir dos dados do enunciado (lembre que, se a frase dada é "a moto não é branca" e é verdadeira, a simples "a moto é branca" é **falsa**).
3. **Resolva dos parênteses internos para os externos**: negações, depois conjunções e disjunções, por último condicionais e bicondicionais.
4. Ao **deduzir valores** de uma composta dada como falsa ou verdadeira, use os casos únicos: **disjunção falsa** → as duas F; **conjunção verdadeira** → as duas V; **condicional falsa** → antecedente V e consequente F; **bicondicional** → valores iguais (verdadeira) ou diferentes (falsa); **exclusiva falsa** → valores iguais.

### Aplicando o método (revisão comentada)

- Reconhecer o conectivo pelo símbolo: ∧ é conjunção, ∨ disjunção inclusiva, → condicional e ↔ bicondicional. Interpretar uma fórmula como (¬p) ∨ q exige manter o "não" **só** em p.
- **(p ∨ q) ∧ ¬p**: as duas parcelas V → p é F e, então, q é V.
- **"X ou Y" falsa**, com Y uma condicional "se r, então l": X é F, Y é F, logo r é V e l é F.
- **Fatos dados**: se são verdadeiros "o carro é preto", "a moto não é branca" e "a bicicleta é vermelha", só é verdadeira a condicional cujo antecedente fica falso (F → F), como "se a bicicleta não é vermelha e o carro é preto, então a moto é branca".
- **Conectivo da frase**: "seguirá defendendo o caso **se, e somente se**, o cliente seguir as orientações" é **bicondicional**; "se... e... então..." é condicional com antecedente conjunção.
- **Afirmativas de teoria**: negação inverte o valor; conjunção só é V com duas V; **disjunção é V com ao menos uma V** (e não "uma falsa"); a exclusiva é F com valores iguais.
- **Proposições aritméticas**: primeiro calcule (4³ = 64, 6 × 9 = 54, √121 = 11) e depois aplique o conectivo; uma bicondicional de duas igualdades falsas é verdadeira.
- **Fórmula aninhada**: (~(p ∧ q) ∨ ~p) → (~p ∨ ~q) é V tanto com p, q ambos V quanto com ambos F.
- **Modus tollens**: se "alarme dispara → protocolo é ativado" é verdadeira e o protocolo **não** foi ativado, o alarme **não** disparou.

### Para fixar
- Tenha um roteiro fixo: listar simples, valorar, resolver de dentro para fora.
- Casos únicos: disjunção F (ambas F), conjunção V (ambas V), condicional F (V e F).
- Bom e mau não são negações um do outro; "não... ninguém" é ênfase.
- Consequente falso e condicional verdadeira → antecedente falso.
- Frases aritméticas: calcule primeiro cada igualdade e só depois aplique o conectivo.


---

# TRECHO: raciocinio-logico/a01/s03
##### raciocinio-logico/a01/s03
Este trecho conclui a construção da tabela-verdade (passo 4, com um exemplo completo e questões) e apresenta tautologia, contradição e contingência, com os métodos para identificá-las e a noção de implicação.

### Passo 4: calcular as colunas

- Para ~(p → ~q) ∨ (~r → q), calculam-se, nesta ordem: **~q** e **~r** (invertem q e r); **(p → ~q)**, falsa só quando p é V e ~q é F; **~(p → ~q)**; **(~r → q)**, falsa só quando ~r é V e q é F; e a **disjunção final**, falsa só quando as duas parcelas são falsas. A tabela mostra que a fórmula só é falsa em **dois casos**: p V com q e r F, e p, q e r todos F.
- Na prática, faz-se uma única tabela e calculam-se as colunas em sequência, sempre usando as colunas já calculadas como referência.

### Questões resolvidas

- **Questão do IBGE**: uma frase do tipo "se o instituto produz dados, então orienta as políticas públicas **e** justifica o uso dos recursos" tem a forma p → (a ∧ j), com três simples (8 linhas). A conjunção a ∧ j é V só quando a e j são V; a condicional é falsa quando p é V e (a ∧ j) é F, o que ocorre em **3 linhas**.
- **Tabela incompleta** de ((p ∧ q) → ~r) ↔ q: a bicondicional é V quando as duas colunas têm o **mesmo valor** e F quando diferem; assim se completam os pontos de interrogação (resposta V, F, V, F).
- **(Q ∨ R) ∧ P**: a disjunção é F apenas com Q e R falsas; a conjunção é V só com as duas parcelas V. Com a ordem padrão dos valores, a última coluna é **V V V F F F F F**, e a sequência V V V F V V F F seria **errada**.

### Tautologia, contradição e contingência

- **Tautologia**: a coluna final da tabela é **sempre V**. **Contradição**: **sempre F**. **Contingência**: **V e F**, dependendo dos valores das simples. Clássicas: **p ∨ ~p é tautologia** ("A Terra é plana ou a Terra não é plana") e **p ∧ ~p é contradição**. Na questão da ALMG, ~(p ∧ q) ↔ (~p ∨ ~q) é tautologia, (p ∧ ~q) ↔ (~p ∨ q) é contradição e (p ∨ q) → p (da tabela III) é contingência.
- Podem-se representar a tautologia pela proposição genérica **⊤** (ou t) e a contradição por **⊥** (ou c): p ∨ ~p ≡ t (V) e p ∧ ~p ≡ c (F). Duas proposições com sempre os mesmos valores são **equivalentes** (símbolo ≡ ou ⇔).
- Em provas, as letras c e t às vezes designam proposições simples quaisquer (por exemplo, "Tiago é engenheiro"), quando isso estiver claro.

### Como identificar: três métodos

1. **Tabela-verdade** (olhar a última coluna).
2. **Prova por absurdo**: suspeitando de **tautologia**, tente atribuir **F** à fórmula; se for possível, **não** é tautologia (pode ser contradição ou contingência); se chegar a um **absurdo**, ela **nunca é falsa**: é tautologia. Suspeitando de **contradição**, tente atribuir **V**; se for possível, não é contradição; se levar a absurdo, é contradição. Se for possível F e também V, é **contingência**.
3. **Equivalências lógicas** (álgebra de proposições), vista em aula própria.

### Implicação

- **p implica q** (p ⇒ q) quando a condicional **p → q é uma tautologia**.

### Para fixar
- Passo 4: calcule negações, depois compostas internas, depois a fórmula final, usando as regras de cada conectivo.
- Tautologia: sempre V; contradição: sempre F; contingência: V e F.
- p ∨ ~p é tautologia; p ∧ ~p é contradição.
- Prova por absurdo: tente F para tautologia e V para contradição.
- p ⇒ q quando p → q é tautologia.


---

# TRECHO: raciocinio-logico/a01/s04
##### raciocinio-logico/a01/s04
Este trecho aplica os dois métodos de classificação de fórmulas: a tabela-verdade completa (com a fórmula [(p ∧ q) ∧ r] → [p ↔ (q ∨ r)] e questões de concurso) e a prova por absurdo, que costuma ser mais rápida.

### Método da tabela-verdade

- Roteiro dos quatro passos: (1) contar as linhas, 2ⁿ; (2) montar as colunas por "engenharia reversa"; (3) alternar V e F nas simples; (4) calcular as demais colunas. Depois, olha-se a **última coluna**: só V = **tautologia**; só F = **contradição**; V e F = **contingência**.
- Na fórmula [(p ∧ q) ∧ r] → [p ↔ (q ∨ r)] há três simples (8 linhas). As colunas são p ∧ q, (p ∧ q) ∧ r, q ∨ r, p ↔ (q ∨ r) e a condicional final. A conjunção tripla só é V quando p, q e r são V; nesse caso a bicondicional também é V (p e q ∨ r são V). Logo o antecedente V **nunca** convive com consequente F, e a condicional é **tautologia**.
- Cada conectivo segue a sua regra: ∧ só é V com as duas parcelas V; ∨ só é F com as duas F; ↔ é V quando os dois lados têm o mesmo valor; → só é F no caso V → F.

### Questões pelo método da tabela

- **CRO-RS (apontar uma contradição)**: com duas simples, são 4 linhas. (p ∧ q) → (p ∨ q), p ∨ ~p, p → (q → p) e (p ∧ q) → p são **tautologias** (a condicional só seria F com antecedente V e consequente F, o que não ocorre). A alternativa **(p ∨ ~q) ↔ (~p ∧ q)** é a contradição: o lado esquerdo é a **negação** do direito (p ∨ ~q é falso exatamente quando ~p ∧ q é verdadeiro), então os dois lados **nunca** têm o mesmo valor e a bicondicional é sempre F.
- **ISS Fortaleza (item sobre a frase "se a pessoa trabalha no que gosta e está de férias, então é feliz ou está de férias")**: com t, f e z, a forma é (t ∧ f) → (z ∨ f), com 8 linhas. Se o antecedente é V, f é V, e então z ∨ f é V. A condicional não tem linha F: **tautologia** (item certo).

### Método da prova por absurdo

- **Suspeita de tautologia**: tentar tornar a fórmula **falsa**. Se for possível, não é tautologia (é contradição ou contingência). Se levar a um **absurdo**, ela nunca é falsa: **tautologia**.
- **Suspeita de contradição**: tentar torná-la **verdadeira**. Se for possível, não é contradição. Se levar a absurdo, é **contradição**.
- Se for possível obter F e também V, a fórmula é **contingência**.
- **Absurdo** aqui é a situação contraditória que surge ao exigir F de uma tautologia (ou V de uma contradição): por exemplo, uma simples teria de ser V e F ao mesmo tempo.
- Aplicação a [(p ∧ q) ∧ r] → [p ↔ (q ∨ r)]: com p, q e r todos F, o antecedente é F e a condicional é V, logo **não é contradição**. Para torná-la F exige-se antecedente V (p, q, r verdadeiras) e consequente F; mas a bicondicional só é F com p V e q ∨ r F (impossível, pois q e r são V) ou com p F e q ∨ r V (impossível, pois p é V). **Absurdo**: é tautologia.
- Para questões de tautologia, contradição e contingência a prova por absurdo costuma ser **melhor** que a tabela, que dá mais trabalho.

### Questões pelo método do absurdo

- **Prefeitura de Penedo**: nas fórmulas formadas só por simples distintas (como P ∧ Q ∧ R, P ∨ Q ∧ R ∨ S, P ∨ Q ∨ R → S) basta mostrar uma atribuição que as torna V e outra que as torna F: são **contingências**. A que tem P e ~P na mesma disjunção, P ∨ Q ∨ R ∨ ~S ∨ ~P, é **tautologia**: para ser F, todos os termos teriam de ser F, inclusive P e ~P ao mesmo tempo, o que é absurdo.
- **Petrobras**: [(p → r) ∧ (q → r)] → [r → (p ∨ q)]. Para ser F, o consequente r → (p ∨ q) deve ser F: r V, p F, q F. Com esses valores, p → r e q → r são V, e o antecedente é V. Como foi possível obter F, **não é tautologia** (item errado).
- **ISS Fortaleza (de novo)**: pelo método do absurdo a conclusão é a mesma da tabela: tautologia.

### Para fixar
- Última coluna da tabela: só V (tautologia), só F (contradição) ou misto (contingência).
- Prova por absurdo: suspeitou de tautologia, tente F; suspeitou de contradição, tente V.
- Chegar a um absurdo significa que o valor testado é impossível para a fórmula.
- Se F e V forem ambos possíveis, é contingência.
- Fórmulas com P e ~P num mesmo "ou" são tautologias; com P e ~P num mesmo "e" são contradições.
- Duas fórmulas ligadas por ↔ em que uma é a negação da outra formam uma contradição.


---

# TRECHO: raciocinio-logico/a01/s08
##### raciocinio-logico/a01/s08
Este trecho termina as questões de classificação de fórmulas (tautologia, contradição, contingência) e reapresenta, para treino, a lista das questões de conversão para a linguagem proposicional, com o gabarito.

### Reconhecer as formas básicas

- **p ∨ ~p é tautologia**, mesmo quando a frase é longa e parece enganosa: "Aurora tatuou uma estrela ou ela não tatuou uma estrela" (item que a chamava de contradição está **errado**); "Laura será aprovada ou não será aprovada"; "o médico irá prescrever o medicamento ou não irá prescrever".
- **Ou exclusivo com uma simples e a sua negação**: g ⊻ ~g é V sempre, pois os dois lados têm valores **opostos**, e o ou exclusivo é V quando os valores diferem. "Ou Gael gosta de pequi, ou Gael não gosta de pequi" é tautologia, não contradição.
- **p ∧ ~p é contradição**. A contradição pode vir disfarçada em sinonímia: "não é caro, mas custa muito caro" é ~p ∧ p, porque "custa muito caro" tem o mesmo sentido de "é caro" (o "mas" funciona como "e").
- Uma **proposição simples** isolada ("Todo gato é verde", "Maria é alta") é contingência, assim como "nem estudou e nem passou" (~p ∧ ~q, que é V só quando as duas são F) e "Maria é alta e João é baixo" (p ∧ q).
- **P → ~P** é contingência: com P V dá F, com P F dá V. **(A ∨ B) → A** é contingência: com A F e B V dá F; com A e B V dá V.

### Tautologias por absurdo (questões de múltipla escolha)

- **FEPESE/Brusque**: tentar tornar falsa cada alternativa. "Se Maria não estuda, Pedro trabalha" falha com os dois F; "m → (m ∧ p)" falha com m V e p F; "(m ∨ p) → p" falha com m V e p F; "(m ∧ p) → (m ∧ ~p)" falha com m e p V. Só **m → (m ∨ p)** não admite F (m V garante m ∨ p V): tautologia.
- **SEBRAE-GO**: ((P ∨ Q) ∧ (P → Q)) → Q é tautologia. Para ser F, Q deveria ser F e o antecedente V; mas P ∨ Q com Q F exige P V, e então P → Q seria F, o que contradiz o antecedente V. As demais (como (P → Q) ∧ P ∧ ~Q e (P ∧ ~Q) ∨ (~P ∧ Q)) podem ser falsas.
- **Selecon/Cuiabá**: a única tautologia é P ∨ ¬P.

### Lista de questões para treino (conversão)

- O final do material reapresenta, sem novas explicações, as questões de conversão já resolvidas (FEPESE, UFG, VUNESP, INPI, AOCP, PM-SC, TRT-8, IBFC, Petrobras e ADAPAR), seguidas do gabarito para autoteste: nesta ordem, D, D, B, C, Certo, E, A, A, A, B, Certo, C. Vale refazê-las sem olhar a resolução.

### Para fixar
- p ∨ ~p é sempre tautologia, qualquer que seja a frase; p ∧ ~p é sempre contradição.
- g ⊻ ~g também é tautologia: os valores são sempre opostos.
- Sinônimos contam como a mesma simples ("é caro" e "custa muito caro").
- Para testar tautologia, tente tornar a alternativa falsa; o que não admite F é a resposta.
- Proposição simples isolada é contingência.
- Refaça a lista de questões sem consultar a resolução.


---

# TRECHO: raciocinio-logico/a02/s02
##### raciocinio-logico/a02/s02
Este trecho ensina as outras duas equivalências fundamentais da condicional e do "ou" (p → q ≡ ~p ∨ q e p ∨ q ≡ ~p → q), resolve questões com elas e introduz a ideia de negação lógica como uma equivalência.

### Condicional em disjunção inclusiva

- **p → q ≡ ~p ∨ q.** Procedimento: (1) **negar o primeiro termo**; (2) **trocar** o "se... então" por "ou"; (3) **manter o segundo termo**. Exemplo: "Se o motor esquenta, o ventilador liga" equivale a "O motor não esquenta **ou** o ventilador liga".
- **Prova pela tabela**: ~p ∨ q só é F quando ~p e q são F, isto é, p V e q F, que é o único caso em que p → q é F. Colunas iguais, logo equivalentes.
- A condicional tem **apenas duas equivalências possíveis**: a **contrapositiva** (~q → ~p) e a **disjunção** (~p ∨ q). Ou seja: a equivalente de uma condicional é sempre outra condicional (a contrapositiva) ou um "ou" inclusivo. Se as opções misturam "ou" e "e", use a disjunção; se todas forem condicionais, use a contrapositiva.

### Aplicações

- **PROCON-DF**: "Se Alice é estudante de medicina, então é inteligente" ≡ "Alice não é estudante de medicina ou é inteligente" (item **certo**).
- **PM-RN**: partindo de f → c (faltar ao serviço leva ao cancelamento da instrução), obtém-se ~f ∨ c, com o primeiro termo negado e o segundo igual (letra A).
- **Pref. S. Parnaíba**: "Se Marcos cozinha, então ele não lava a louça" (c → ~l). A contrapositiva é l → ~c, que não está nas alternativas; a disjunção ~c ∨ ~l (não cozinha ou não lava) está (letra A). Moral: se um método não gera nenhuma alternativa, tente o outro.
- **CM-POA**: p → ~q ≡ ~p ∨ ~q (letra E).

### Disjunção inclusiva em condicional

- **p ∨ q ≡ ~p → q.** Procedimento: (1) nega-se o **primeiro** termo; (2) troca-se "ou" por "se... então"; (3) mantém-se o segundo. Exemplo: "O técnico viaja ou o laboratório fecha" ≡ "Se o técnico não viaja, o laboratório fecha".
- **Demonstração sem tabela**: aplicando p → q ≡ ~p ∨ q com a primeira parcela sendo ~p, obtém-se ~p → q ≡ ~(~p) ∨ q ≡ p ∨ q. Invertendo a ordem da igualdade, p ∨ q ≡ ~p → q.
- Como "ou" é comutativo, p ∨ q também é ≡ ~q → p (nega-se o outro termo).

### Aplicações

- **EPC**: a frase a ∨ s (contar com os amigos ou ficar sozinho) equivale a ~a → s, ou seja, "se não posso contar com os amigos, ficarei sozinho" (letra A).
- **Pref. Campinas**: c ∨ ~o ("Os cantadores saíram hoje ou eu não ouço bem") ≡ ~c → ~o: "Se os cantadores não saíram hoje, então eu não ouço bem" (letra E). Atenção: ao negar o primeiro termo, o segundo não muda, mesmo que já seja negativo.

### Negações lógicas

- Uma **negação lógica** é uma equivalência vinda da negação de uma proposição: dizer que a negação de p ∧ q é ~p ∨ ~q equivale a dizer que ~(p ∧ q) ≡ ~p ∨ ~q.
- A negação de uma proposição tem valores **sempre opostos** aos da original. Por isso, ~p ∨ ~q tem, em toda linha da tabela, o valor contrário ao de p ∧ q.

### Para fixar
- p → q ≡ ~p ∨ q: nega o primeiro, troca por "ou", mantém o segundo.
- p ∨ q ≡ ~p → q: nega o primeiro, troca por "se... então", mantém o segundo.
- Condicional só é equivalente a outra condicional (contrapositiva) ou a uma disjunção.
- Ao negar o primeiro termo, o segundo não é alterado.
- Negação lógica = proposição de valores sempre opostos.


---

# TRECHO: raciocinio-logico/a02/s05
##### raciocinio-logico/a02/s05
Este trecho fecha as negações lógicas com as quatro formas de negar a bicondicional e abre a álgebra de proposições: o quadro das propriedades, a ideia de simplificar expressões e as propriedades comutativa e associativa.

### Negações da bicondicional

Há quatro formas comuns:

1. **~(p ↔ q) ≡ p ⊻ q** (a negação é a disjunção exclusiva).
2. **~(p ↔ q) ≡ ~p ↔ q**.
3. **~(p ↔ q) ≡ p ↔ ~q** (nega-se só um termo).
4. **~(p ↔ q) ≡ (p ∧ ~q) ∨ (q ∧ ~p)** (só com "e", "ou" e "não").

- **Demonstração da 1ª**: parte-se de ~(p ⊻ q) ≡ p ↔ q e nega-se dos dois lados; a dupla negação dá p ⊻ q ≡ ~(p ↔ q). Uma proposição composta se comporta como uma simples nesse raciocínio.
- **Demonstração da 4ª**: p ↔ q ≡ (p → q) ∧ (q → p). Negando: ~(p ↔ q) ≡ ~(p → q) ∨ ~(q → p) (De Morgan) ≡ (p ∧ ~q) ∨ (q ∧ ~p) (negação da condicional).
- Exemplo: negar "Durmo se e somente se estou cansado" pode dar "Ou durmo, ou estou cansado" (exclusiva) ou "Durmo se e somente se não estou cansado".
- **CAU-TO**: a negação de "A Fênix é imortal se, e somente se, renasce das cinzas" é "Ou a Fênix é imortal ou renasce das cinzas": item **certo**.
- **Pref. Vila Lângaro**: negar "João passa se e somente se João estuda" dá "Ou João passa ou João estuda" (letra D). A alternativa que nega os dois termos (~p ↔ ~e) é **equivalência** da bicondicional, não negação.

### Álgebra de proposições: panorama

- Quadro das propriedades: **comutativa** (∧, ∨, ⊻ e ↔ comutam; a condicional **não**), **associativa** ((p ∧ q) ∧ r ≡ p ∧ (q ∧ r); (p ∨ q) ∨ r ≡ p ∨ (q ∨ r)), **distributiva** (p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r); p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)), **identidade** (p ∧ t ≡ p; p ∧ c ≡ c; p ∨ t ≡ t; p ∨ c ≡ p), **absorção** (p ∨ (p ∧ q) ≡ p; p ∧ (p ∨ q) ≡ p) e **idempotência** (p ∧ p ≡ p; p ∨ p ≡ p). Aqui t é tautologia e c é contradição.
- **Estratégia**: desenvolver a fórmula até chegar a uma tautologia t, uma contradição c ou uma contingência simples (uma simples, uma conjunção etc.).
- **Bicondicional em tautologia/contradição**: X ↔ Y é **tautologia** se X e Y são equivalentes e **contradição** se uma é a negação da outra.
- A álgebra serve para resolver mais rápido ou quando a banca "esconde" a equivalência nas alternativas. O essencial é dominar **comutativa, associativa e distributiva**; os casos complexos podem sempre ser resolvidos por tabela-verdade.

### Propriedade comutativa

- **p ∧ q ≡ q ∧ p; p ∨ q ≡ q ∨ p; p ⊻ q ≡ q ⊻ p; p ↔ q ≡ q ↔ p.** A condicional **não** comuta: p → q e q → p não são equivalentes (a equivalente é a contrapositiva).
- **Aplicação**: negar "Se corro, chego a tempo" dá p ∧ ~q, "Corro e não chego a tempo"; se as alternativas trouxerem "Não chego a tempo e corro" (~q ∧ p), pode marcar, pois a conjunção comuta.
- **EPC**: negar "(Animais são bípedes ou quadrúpedes) e árvores têm folhas verdes", isto é, (b ∨ q) ∧ a. Pela negação da conjunção: ~(b ∨ q) ∨ ~a; por De Morgan: (~b ∧ ~q) ∨ ~a. Pela comutativa: **~a ∨ (~b ∧ ~q)**: "Árvores não têm folhas verdes ou animais não são bípedes e não são quadrúpedes" (letra E).

### Propriedade associativa

- Como na aritmética (3 × 5) × 7 = 3 × (5 × 7), valem **(p ∧ q) ∧ r ≡ p ∧ (q ∧ r)** e **(p ∨ q) ∨ r ≡ p ∨ (q ∨ r)**. Não se misturam "e" e "ou" na associativa. Numa sequência só de "e" ou só de "ou", os parênteses podem ser retirados.
- **Exemplo**: p ∨ (q ∨ ~p) é tautologia: comuta-se (q ∨ ~p) para (~p ∨ q), associa-se para (p ∨ ~p) ∨ q ≡ t ∨ q, e uma disjunção com um termo sempre V é sempre V. Item **certo** (inédita).
- **TRT-1 (2008)**: a negação de uma condicional ~[[A ∧ ~B] → C] mantém o antecedente e nega o consequente: [A ∧ ~B] ∧ ~C, que pela associativa é **A ∧ ~B ∧ ~C** (opção a).

### Para fixar
- Negações da bicondicional: p ⊻ q; ~p ↔ q; p ↔ ~q; (p ∧ ~q) ∨ (q ∧ ~p).
- ~p ↔ ~q é equivalência de p ↔ q, não negação.
- Comutam: ∧, ∨, ⊻, ↔; a condicional não comuta.
- Associativa: só entre "e" com "e" ou "ou" com "ou".
- X ↔ Y é tautologia se X ≡ Y, e contradição se uma for a negação da outra.
- Álgebra: simplificar até chegar a t, c ou uma contingência simples.


---

# TRECHO: raciocinio-logico/a02/s06
##### raciocinio-logico/a02/s06
Este trecho continua a álgebra de proposições: propriedade distributiva (a mais cobrada depois da comutativa e da associativa), propriedades da identidade, absorção e idempotência (bônus) e o uso da álgebra para classificar fórmulas em tautologia, contradição ou contingência.

### Fim da questão do TRT-1

- A negação ~[[A ∧ ~B] → C] mantém o antecedente e nega o consequente: [A ∧ ~B] ∧ ~C. Pela associativa, tiram-se os colchetes: **A ∧ ~B ∧ ~C** (opção a).

### Propriedade distributiva

- Na aritmética, 3 × (5 + 7) = 3 × 5 + 3 × 7; fazendo ao contrário, "colocamos o 3 em evidência". Na lógica há duas distributivas:
  - **do "e" sobre o "ou"**: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r);
  - **do "ou" sobre o "e"**: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r).
- É preciso reconhecer também **de trás para frente** (colocar "p ∧" ou "p ∨" em evidência): (p ∧ q) ∨ (p ∧ r) ≡ p ∧ (q ∨ r) e (p ∨ q) ∧ (p ∨ r) ≡ p ∨ (q ∧ r).
- Não existe "distributiva da conjunção sobre a condicional": o item da ISS Fortaleza que afirmava isso está **errado**.
- Se a fórmula tem condicional, transforme antes em "ou" (p → q ≡ ~p ∨ q); se tem a negação da condicional, vire "e" (~(p → q) ≡ p ∧ ~q).

### Aplicações da distributiva

- **SEFAZ-SC**: (a ∧ b) ∨ (a ∧ ¬b) ≡ a ∧ (b ∨ ¬b) ≡ a ∧ t ≡ **a** (letra E), pois b ∨ ~b é tautologia e "a ∧ t" depende só de a.
- **Pref. Alumínio**: "Sueli é professora e, pratica ginástica ou pratica corrida" (a vírgula cria parênteses) é s ∧ (g ∨ k) ≡ (s ∧ g) ∨ (s ∧ k): "é professora e pratica ginástica, ou é professora e pratica corrida" (letra C).
- **MPE-RO**: (P → Q) ∧ (R ∨ Q) ≡ (~P ∨ Q) ∧ (R ∨ Q). Com a comutativa, (Q ∨ ~P) ∧ (Q ∨ R); colocando "Q ∨" em evidência: **Q ∨ (~P ∧ R)** (letra A). Sem álgebra, seria preciso comparar seis tabelas-verdade.
- **TCE-RO**: P ∨ [¬(Q → R)] ≡ P ∨ (Q ∧ ~R) ≡ (P ∨ Q) ∧ (P ∨ ~R): item **certo**.

### Identidade, absorção e idempotência (bônus)

Raramente caem; use como apoio. Sendo t uma tautologia e c uma contradição:

- **Identidade da conjunção**: p ∧ t ≡ p (o valor depende só de p) e p ∧ c ≡ c.
- **Identidade da disjunção**: p ∨ t ≡ t e p ∨ c ≡ p.
- **Absorção**: p ∨ (p ∧ q) ≡ p; p ∧ (p ∨ q) ≡ p. Na SEFAZ-MS, a negação de p ∧ (p ∨ q) é simplesmente **~p** (letra A).
- **Idempotência**: p ∧ p ≡ p; p ∨ p ≡ p.
- **ANPAD**: p ∧ (q ∨ ~p) ≡ (p ∧ q) ∨ (p ∧ ~p) ≡ (p ∧ q) ∨ c ≡ **p ∧ q** (letra B).
- **DPEN**: ¬[(P → Q) ∨ Q] ≡ ~(P → Q) ∧ ~Q ≡ (P ∧ ~Q) ∧ ~Q ≡ P ∧ (~Q ∧ ~Q) ≡ P ∧ ~Q (De Morgan, negação da condicional, associativa e idempotência): item **certo**.

### Álgebra para tautologia, contradição e contingência

- Costuma ser o método mais rápido, mas exige domínio das equivalências. Desenvolve-se a fórmula até obter **t**, **c** ou uma contingência simples.
- **STJ**: ¬P → (P → Q) ≡ P ∨ (P → Q) ≡ P ∨ (~P ∨ Q) ≡ (P ∨ ~P) ∨ Q ≡ t ∨ Q ≡ t. Tautologia (item certo).
- **CBM-AL**: Q ∨ (Q → P) ≡ Q ∨ (~Q ∨ P) ≡ (Q ∨ ~Q) ∨ P ≡ t ∨ P ≡ t. Tautologia (item certo).

### Para fixar
- Distributiva: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r) e p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r), e a leitura inversa ("colocar em evidência").
- Antes de usar a álgebra, troque condicionais por "ou" (e negações de condicional por "e").
- Identidade: p ∧ t ≡ p, p ∧ c ≡ c, p ∨ t ≡ t, p ∨ c ≡ p.
- Absorção e idempotência simplificam repetições de p.
- Tautologia por álgebra: chegue a t ∨ qualquer coisa.


---

# TRECHO: raciocinio-logico/a02/s08
##### raciocinio-logico/a02/s08
Este trecho segue com questões comentadas de várias bancas sobre equivalências e negações, agora com fórmulas mais longas: negar condicionais cujo consequente é um "ou", achar a contrapositiva de antecedentes compostos, usar De Morgan em sequência e contar elementos em conjuntos.

### Equivalente de ~p → q

- Contrapositiva: ~q → p (não aparece nas opções). Condicional em "ou": ~(~p) ∨ q = **p ∨ q**. Desenvolvendo ~((~p) ∧ (~q)) por De Morgan, obtém-se p ∨ q também. Logo ~p → q ≡ p ∨ q ≡ ~(~p ∧ ~q) (letra D).

### Negação de condicional com "ou" e "e" dentro

- **Gameleira/Verbena**: "Se hoje não chover, então vou à praia ou vou correr". Nega-se mantendo o antecedente, trocando por "e" e negando o consequente: ~c ∧ ~(p ∨ o). Por De Morgan: **~c ∧ ~p ∧ ~o**: não chove, não vou à praia e não corro (letra A).
- **VUNESP (Rio Preto Prev)**: a frase é (l ∧ s) ∨ ~v ("A e B bem, ou não devem seguir viagem"). Negando o "ou": ~(l ∧ s) ∧ ~(~v) = (~l ∨ ~s) ∧ v. Lê-se: um dos dois não está bem **e** devem seguir viagem (letra B).
- **Sinop (Joelma procuradora/competente)**: negação de p → c é p ∧ ~c (letra A). **Mariano**: "Vou dormir até meio-dia ou não me chamo Mariano" é d ∨ ~m; a negação é ~d ∧ m: "não vou dormir até meio-dia e me chamo Mariano" (letra C).
- **ISS-BH**: a declaração "o computador estava sem internet ou a porta emperrou" é falsa (o suspeito mentiu): vale a negação c ∧ ~p, isto é, o computador **tinha internet e a porta não emperrou** (letra C). Cuidado ao escolher a simples: "sem internet" é a negação de "com internet".

### Equivalentes de condicionais com antecedente composto

- **P → (Q ∨ R)** ≡ **(~Q ∧ ~R) → ~P** (contrapositiva + De Morgan; letra A).
- **VUNESP**: (v ∧ ~g) → s ("se como verduras e não como gordura, minha saúde agradece"). A contrapositiva é ~s → ~(v ∧ ~g) ≡ **~s → (~v ∨ g)** (letra E). Pelo "ou": (~v ∨ g) ∨ s, que não aparecia.
- **FGV/ALEGO**: (b ∧ ~a) → v não tem a contrapositiva nas opções (~v → (~b ∨ a)); mas pela transformação em "ou": ~(b ∧ ~a) ∨ v = **~b ∨ a ∨ v** (letra C).
- **AOCP/PMPE** ("Se Carlos mentiu, será criticado pela família"): a equivalente é a contrapositiva "Se Carlos não foi criticado, então não mentiu" (letra D). As demais são inversa ou recíproca ou afirmam o consequente/antecedente isoladamente.
- **Verbena/IFS** (números naturais): a contrapositiva de "se n² é par, então n é par" é "se n não é par, então n² não é par"; como "não par" é "ímpar", fica **"se n é ímpar, então n² é ímpar"** (letra A).
- **CRESS-PR**: "Se Lucca é ortopedista, Victória não é pediatra" ≡ "Lucca não é ortopedista ou Victória não é pediatra" (l → ~v ≡ ~l ∨ ~v): item **certo**.
- **NOVACAP**: "Se Gabriela cantou, Jacqueline não cantou" **não** é equivalente a "Ou Gabriela cantou ou Jacqueline cantou". As equivalentes da condicional são a contrapositiva (j → ~g) e ~g ∨ ~j; a exclusiva é outra coisa. Item **errado**.

### Contagem com De Morgan

- **Consulplan/CGM**: num grupo de 13 atletas, "no máximo 6 não têm experiência internacional e não competem profissionalmente" (~e ∧ ~p). Então pelo menos 13 − 6 = 7 atletas satisfazem a negação ~(~e ∧ ~p) ≡ e ∨ p: **pelo menos 7 têm experiência internacional ou competem profissionalmente** (letra C).

### Equivalente de ~p ∧ ~q

- Por De Morgan, ~p ∧ ~q ≡ **~(p ∨ q)** (letra E da ISS-BH).

### Para fixar
- Negar condicional com "ou" no consequente: mantém o antecedente, "e", e as duas negações.
- Contrapositiva de antecedente composto: nega-se tudo e aplica-se De Morgan ao que foi negado.
- Condicional em "ou": nega-se o antecedente inteiro (De Morgan) e mantém-se o consequente.
- Se o suspeito mentiu, vale a negação da declaração.
- Equivalente de condicional nunca é disjunção exclusiva.
- "No máximo k que satisfazem X" equivale a "pelo menos n − k que não satisfazem X".


---

# TRECHO: raciocinio-logico/a02/s09
##### raciocinio-logico/a02/s09
Este trecho reúne questões comentadas de várias bancas sobre as "outras equivalências e negações": negação da bicondicional e da disjunção exclusiva, negação da conjunção na forma condicional, conjunção de condicionais e o cuidado com antônimos ao negar proposições simples.

### Negação da bicondicional

- Regra principal: **~(p ↔ q) ≡ p ⊻ q**. Mantêm-se os dois termos e troca-se "se e somente se" por "ou... ou".
- Questões: IBADE/PCES (férias em Noronha × trabalho em janeiro: letra E, "Ou Olivia passou férias... ou Suzana trabalhou..."); QUADRIX/CORE-CE (casa de palha × casa de madeira: letra C); QUADRIX/CRP-6 (aranha × morcego): item **certo**; VUNESP/TCM-SP (ser feliz × você ser feliz: letra E).
- **Armadilha recorrente**: negar os **dois** termos da bicondicional (~p ↔ ~q) não a nega, apenas dá uma **equivalente** (~p ↔ ~q ≡ p ↔ q). Alternativas assim estão erradas.

### Negação da disjunção exclusiva

- **Principal**: ~(p ⊻ q) ≡ p ↔ q. **Outras**: ~p ⊻ q e p ⊻ ~q (nega-se só um termo).
- **INPI** ("Ou o jornalista é muito mal-informado ou age de má-fé"): sua negação pode ser "O jornalista é mal-informado se, e somente se, age de má-fé" (item **certo**). Já "Ou o jornalista é muito bem-informado ou age de boa-fé" está **errado** por dois motivos: (1) "bem-informado" e "boa-fé" são antônimos, não negações exatas das simples; (2) mesmo que fossem, ~m ⊻ ~a é equivalente (negam-se os dois termos), não negação.
- **VUNESP/CMSJC**: a negação de a ⊻ ~c ("Ou arranjo emprego ou não me caso") sem bicondicional nas opções é obtida negando um só termo: **~a ⊻ ~c** (letra D).

### Negação da conjunção na forma condicional

- **AOCP/DEPEN-PR**: "João nunca foi privado de liberdade e o relatório é inconclusivo" é j ∧ r. Cuidado com a negação de simples: a negação de "nunca" não é "sempre", e sim "**ao menos uma vez** foi privado". Por De Morgan, a negação é ~j ∨ ~r (não está nas opções). Na forma condicional: ~(j ∧ r) ≡ r → ~j, isto é, "Se o relatório é inconclusivo, então ao menos uma vez João foi privado de liberdade" (letra E).

### Bicondicional como "ida e volta"

- **IDECAN/Pref. SCS**: p ↔ q ≡ (p → q) ∧ (q → p), letra B. **IDECAN/IFPA**: a bicondicional "todos os empresários terão sucesso se e somente se investirem tempo em estudo e pesquisa" equivale a duas condicionais ligadas por "e" (letra C). Atenção: as opções com "ou" entre as condicionais ou com a bicondicional repetida estão erradas.

### Conjunção de condicionais

- **PETROBRAS**: (p ∨ q) → r **não** é equivalente a (p → r) ∨ (q → r); o correto é (p → r) **∧** (q → r). Item **errado** (também se verifica por tabela).
- **VUNESP/TJ-SP**: (e → p) ∧ (e → ~t) tem antecedente comum e; logo ≡ e → (p ∧ ~t): "Se Alice estuda, então faz uma boa prova e não fica triste" (letra C).

### Para fixar
- ~(p ↔ q) ≡ p ⊻ q; ~(p ⊻ q) ≡ p ↔ q.
- Negar os dois termos de ↔ ou de ⊻ resulta em equivalência, não em negação.
- A negação de "nunca" é "ao menos uma vez"; antônimos (sempre, boa-fé) não são negações.
- ~(p ∧ q) ≡ p → ~q ≡ q → ~p quando as opções são condicionais.
- (p → r) ∧ (q → r) ≡ (p ∨ q) → r; (p → q) ∧ (p → r) ≡ p → (q ∧ r).


---

# TRECHO: raciocinio-logico/a04/s01
##### raciocinio-logico/a04/s01
Este trecho apresenta as questões clássicas com conectivos lógicos: o enunciado traz várias afirmações consideradas verdadeiras (ou declaradas falsas) e pede a consequência que delas decorre. Ensina o método em quatro etapas e o aplica em questões de várias bancas.

### Pré-requisito: os cinco conectivos "no sangue"

- **Conjunção (∧)**: V só quando as duas parcelas são V. **Disjunção inclusiva (∨)**: F só quando as duas são F. **Disjunção exclusiva (⊻)**: F quando as duas têm o mesmo valor. **Condicional (→)**: F só no caso V → F. **Bicondicional (↔)**: V só quando as duas têm o mesmo valor.

### O que são as questões clássicas

- O enunciado dá um conjunto de **afirmações** (que se consideram **verdadeiras**, a menos que se diga que alguma é falsa) e as alternativas trazem consequências possíveis; deve-se achar a que é **necessariamente verdadeira**. Em prova de certo/errado há uma só consequência para julgar.

### Método em quatro etapas

1. Identificar as afirmações em **"formato fácil"**.
2. **Desconsiderar o contexto**: passar as afirmações para a linguagem proposicional (letras e conectivos).
3. Obter o valor das **proposições simples**, sempre que possível, começando pelo formato fácil e propagando para as demais afirmações.
4. Analisar as alternativas e marcar a que resulta **verdadeira**.

**Formatos fáceis** (já dão o valor de uma ou mais simples "de graça"):
- **Proposição simples** (dada como V ou F): o valor da simples é conhecido.
- **Conjunção verdadeira**: as duas parcelas são V.
- **Disjunção inclusiva falsa**: as duas parcelas são F.
- **Condicional falsa**: antecedente V e consequente F.

### Questões resolvidas

- **MPSP (Marcos)**: afirmações: I. p ∨ n; II. f ∧ ~n; III. ~b ∨ ~p; IV. s → b (todas V). Começa-se pela II (conjunção V): f V e n F. Em I, n F obriga p V. Em III, ~p é F, logo ~b é V (b F). Em IV, b F obriga s F. Valores: Marcos tem filhos, não pratica natação, é professor, não é brasileiro e não conhece São Paulo. A alternativa b (é professor, não conhece São Paulo, não é brasileiro) é a única conjunção verdadeira (letra B).
- **Pref. Campo Bom (cadeia de condicionais)**: seis afirmações, uma cadeia a → u, u → m, m → j, j → s, s → c, mais ~c V (c F). Voltando pela cadeia: c F obriga s F; s F obriga j F; j F obriga m F; m F obriga u F; u F obriga a F. Logo, "Marcos não assiste televisão" (~m) é verdadeira (letra B). Moral: numa cadeia de condicionais com o último consequente falso, **todas as anteriores são falsas**.
- **SEFAZ-ES (Valter)**: "come carne ou frango", "come legumes ou não come carne", "come macarrão ou não come frango" e "não comeu macarrão". m F; na terceira, ~f V (f F); na primeira, c V; na segunda, ~c é F, então l V. Resposta: comeu legumes e carne (letra D). Cuidado: "nem" = "e não" (alternativas com "nem" ficam falsas porque ~c e ~l são F).
- **TJ-SP**: seis afirmações, algumas declaradas falsas: I. a → b (V); II. b ∨ c (V); III. e ∧ c (F); IV. g ⊻ e (V); V. b (F); VI. h → a (V). b F; em I, a F; em II, c V; em III (conjunção falsa) com c V, e F; em IV (exclusiva V) com e F, g V; em VI, a F obriga h F. A consequência verdadeira é "Hugo não é rico" (letra B).

### Para fixar
- Considere verdadeiras as afirmações do enunciado, salvo indicação de falsidade.
- Comece pelo formato fácil: simples, conjunção V, disjunção inclusiva F, condicional F.
- Condicional verdadeira com consequente F: antecedente F; disjunção verdadeira com uma parcela F: a outra é V.
- Numa cadeia de condicionais, consequente final falso torna todos os antecedentes falsos.
- "Nem" equivale a "e não".


---

# TRECHO: raciocinio-logico/a04/s02
##### raciocinio-logico/a04/s02
Este trecho conclui as questões clássicas de conectivos (casos em que nem todas as simples ficam determinadas e enunciados ambíguos com condicional) e abre a lógica de argumentação: definição de argumento, validade × veracidade, silogismo e um panorama dos métodos de verificação (tabela-verdade, conclusão falsa, transitividade, regras de inferência).

### Fim das questões clássicas

- **Resolução do TJ-SP (continuação)**: b F; I: a F; VI: h F; II: c V; III: e F; IV: g V. A alternativa com resultado verdadeiro é "Hugo não é rico" (~h).
- **TJ-SP (artes)** — seis pessoas com profissões, afirmações I–V (III e V falsas): em V (disjunção falsa) c V e e F; em III (condicional falsa) l V; em I, a F; em II, d V; em IV, p V. A única alternativa verdadeira é a **condicional com antecedente falso**: "se Paulo não é pintor, então André é arquiteto" (F → F é V) (letra E).
- **SEFAZ-AM**: p ∨ b é V e s → p é F: logo s V, p F, e então b V. Resposta: Paulo não é carioca, Bernardo é paulista e Sérgio é amazonense (letra C).
- **Quando nem todas as simples são determinadas** (TRT-4): "Quem viaja ao interior não vai à feira"; "Em férias e sem dia útil, viaja ao interior"; "Hoje foi à feira". f V; na primeira, v F; na segunda, (s ∧ ~u) deve ser F (consequente v F), mas não se sabe qual das duas parcelas é F. Mesmo assim, a alternativa "Luciano não viajou ao interior" (~v) é V (letra E). Moral: verifique as alternativas mesmo sem conhecer todas as simples.
- **SEFAZ-AL (Marcos, associação)**: P: (a ∧ p) → b; Q: ~a ∧ p (conjunção V, logo a F e p V). Com antecedente falso, a condicional é V qualquer que seja b: **nada se pode afirmar sobre b**; por isso o item "não se pode afirmar que ele não tenha direito" é certo.
- **ISS Manaus (domingos)**: o enunciado traz, além de três disjunções, a frase "não joguei futebol" como afirmação verdadeira (~f V) — não como antecedente de uma condicional. f F; "corro ou jogo futebol" dá c V; "tomo açaí ou não corro" dá a V; "como pizza ou não tomo açaí" dá p V. Resposta: corri e tomei açaí (letra E).

### Lógica de argumentação: conceitos

- **Argumento**: relação entre um conjunto de **premissas** (hipóteses, proposições consideradas verdadeiras) e uma **conclusão** que elas sustentam. **Argumentos dedutivos** não produzem conhecimento novo (a conclusão já está contida nas premissas).
- **Silogismo**: argumento dedutivo com **duas premissas e uma conclusão**. **Categóricos**: usam proposições categóricas; **hipotéticos**: usam os conectivos, sem categóricas.
- **Validade** é característica do **argumento**; **veracidade** é característica das **proposições**. O argumento é **válido** se a conclusão é necessariamente verdadeira quando as premissas são consideradas verdadeiras; **inválido** (sofisma ou falácia formal) se não for necessariamente.
- **Combinações possíveis**: um argumento válido pode ter (premissas V, conclusão V), (premissas F, conclusão V) ou (premissas F, conclusão F); **não** pode ter premissas V e conclusão F. Um inválido pode ter as quatro combinações. Não há relação direta entre validade e veracidade da conclusão.
- **Forma simbólica**: (P1 ∧ P2 ∧ ... ∧ Pn) → C, uma condicional cujo antecedente é a conjunção das premissas e cujo consequente é a conclusão.

### Silogismo categórico (panorama)

- **Termo maior**: predicado da conclusão. **Termo menor**: sujeito da conclusão. **Termo médio**: aparece nas premissas e não na conclusão. **Premissa maior** contém os termos maior e médio; **menor** contém o menor e o médio.
- **Modo**: três letras (A, E, I, O) na ordem premissa maior, menor, conclusão. **Figuras** (posição do termo médio): 1ª (sujeito na maior, predicado na menor); 2ª (predicado nas duas); 3ª (sujeito nas duas); 4ª (predicado na maior, sujeito na menor).
- **Regras de validade**: apenas três termos; médio universal ao menos uma vez; médio fora da conclusão; nenhum termo mais extenso na conclusão do que nas premissas; a conclusão acompanha a premissa mais fraca; duas premissas afirmativas dão conclusão afirmativa; duas particulares ou duas negativas não permitem conclusão.

### Métodos para verificar a validade

1. **Diagramas lógicos** (argumentos categóricos): considerar as premissas verdadeiras e ver se a conclusão decorre.
2. **Tabela-verdade**: se a condicional (premissas → conclusão) é tautologia, o argumento é válido. Em múltipla escolha, marcam-se as linhas em que todas as premissas são V e escolhe-se a conclusão V em todas.
3. **Conclusão falsa**: exige conclusão simples, "ou" ou condicional (vista adiante).
4. **Transitividade da condicional**: concatenar condicionais (usando contrapositiva e "ou" em condicional quando preciso). Se obtiver a conclusão, é válido. Para conclusão simples, buscar ~p → p (p é V) ou p → ~p (p é F).
5. **Regras de inferência**: modus ponens (p → q; p; logo q), modus tollens (p → q; ~q; logo ~p), silogismo hipotético (p → q; q → r; logo p → r), dilema construtivo (p → q; r → s; p ou r; logo q ou s) e dilema destrutivo (p → q; r → s; ~q ou ~s; logo ~p ou ~r). Todos são **válidos**.

### Para fixar
- Premissas verdadeiras e conclusão falsa: argumento inválido, sempre.
- Validade (argumento) ≠ veracidade (proposição).
- Forma do argumento: (P1 ∧ ... ∧ Pn) → C; válido se for tautologia.
- Modus ponens afirma o antecedente; modus tollens nega o consequente.
- Mesmo sem determinar todas as simples, teste as alternativas.


---

# TRECHO: raciocinio-logico/a04/s04
##### raciocinio-logico/a04/s04
Este trecho detalha o silogismo categórico (termos, premissas maior e menor, modos, figuras, oito regras de validade) e apresenta os dois primeiros métodos de verificação de validade: diagramas lógicos e o método que considera as premissas verdadeiras.

### Silogismo categórico

- É o argumento com **exatamente duas premissas**, ambas **proposições categóricas**, e uma conclusão. Costuma cair pouco em prova, mas completa o conteúdo.
- **Termos**: **maior** (predicado da conclusão), **menor** (sujeito da conclusão) e **médio** (aparece nas premissas e não na conclusão). Exemplo: "Todo felino é ágil; algum caracol não é ágil; logo, nenhum caracol é felino": maior = felino, menor = caracol, médio = ágil.
- **Premissa maior**: a que contém os termos maior e médio. **Premissa menor**: a que contém menor e médio. Por convenção a maior vem primeiro, mas a banca pode **inverter a ordem**; por isso se identificam pelos termos, não pela posição.

### Modo e figura

- **Modo**: três letras (A, E, I, O) na ordem [premissa maior][premissa menor][conclusão]. No exemplo: A (universal afirmativa), O (particular negativa), E (universal negativa): **AOE**.
- **Figura** (papel do termo médio): **1ª**: sujeito na maior e predicado na menor; **2ª**: predicado nas duas; **3ª**: sujeito nas duas; **4ª**: predicado na maior e sujeito na menor. No exemplo, "ágil" é predicado nas duas: **2ª figura**.
- **PC-SP**: um silogismo com premissa universal afirmativa sobre sapos e verde, premissa particular negativa sobre cães e verde, e conclusão universal negativa entre cães e sapos tem modo AOE e é de 2ª figura: **AOE-2** (letra D). O termo médio é "verde", o maior é "sapo" e o menor é "cão".

### Oito regras de validade

1. **Termos**: o silogismo usa apenas três (maior, médio, menor).
2. **Médio universal**: o termo médio precisa ser tomado em toda a sua extensão pelo menos numa premissa.
3. **Médio fora da conclusão**: ele só aparece nas premissas.
4. **Extensão**: o termo da conclusão não pode abranger mais do que abrangia na premissa.
5. **Premissa mais fraca**: premissa negativa produz conclusão negativa; premissa particular produz conclusão particular; havendo as duas, a conclusão é negativa e particular.
6. **Afirmativas**: duas premissas afirmativas exigem conclusão afirmativa.
7. **Particulares**: duas premissas particulares não permitem conclusão.
8. **Negativas**: duas premissas negativas não permitem conclusão.

- **Petrobras**: são regras válidas "só três termos", "duas particulares não geram conclusão" e "premissa particular ⇒ conclusão particular" (letra C). A frase "termo médio negativo ⇒ conclusão negativa" é inválida: não se fala em termo médio negativo, mas em premissas negativas.

### Métodos de verificação da validade (o ponto mais importante da aula)

**1. Diagramas lógicos** (argumentos categóricos): desenha-se cada premissa; se a conclusão não é obrigatória em todos os diagramas possíveis, o argumento é **inválido**.
- **BANESTES**: I) "toda criança gosta de pizza; quem gosta de refrigerante gosta de pizza; logo, toda criança gosta de refrigerante" é **inválido** (há diagramas com criança que não gosta de refrigerante). II) mesmas premissas, conclusão "quem gosta de refrigerante é criança": **inválido** (há quem goste de refrigerante e não seja criança). III) "toda criança gosta de pizza; quem gosta de refrigerante não gosta de pizza; logo, nenhuma criança gosta de refrigerante": **válido** (conjuntos disjuntos, único diagrama). Só o III é válido (letra B).

**2. Considerar as premissas verdadeiras**: é a própria definição de validade; só é prática quando há premissa em "formato fácil": **proposição simples verdadeira** ou **conjunção verdadeira**. Segue as mesmas quatro etapas das questões clássicas: identificar a premissa fácil, passar para a linguagem proposicional, achar os valores das simples e testar a conclusão.
- **CM Taubaté**: premissas: (I) fe → fa; (II) ~ce → ~ca; (III) ce ∧ ~fa. De III: ce V e fa F. Em I, fa F obriga fe F. Em II, o antecedente ~ce é F; logo nada se sabe sobre ca. Conclusão necessariamente verdadeira: **"Cicrano não foi aprovado ou Fulano não estudou"** (~ca ∨ ~fe), pois ~fe é V (letra D). As demais dependem de ca, que não se conhece, ou são falsas.

### Para fixar
- Termos: maior (predicado da conclusão), menor (sujeito da conclusão), médio (nas premissas, não na conclusão).
- Modo = A/E/I/O das premissas e da conclusão; figura = papel do termo médio.
- Duas premissas particulares ou duas negativas não geram conclusão.
- A conclusão acompanha a premissa mais fraca (negativa e/ou particular).
- Diagramas servem para categóricos; premissa verdadeira em formato fácil serve para hipotéticos.


---

# TRECHO: raciocinio-logico/a04/s07
##### raciocinio-logico/a04/s07
Este trecho fecha as regras de inferência (dilema construtivo e dilema destrutivo) e começa as questões comentadas de múltiplas bancas sobre questões clássicas de conectivos, resolvidas pelas quatro etapas da aula.

### Fim da questão do CM Indaiatuba (dilema construtivo)

- Premissas: (j ∧ a) → ~c; i → j'; (j ∧ a) ∨ i. As duas condicionais e a disjunção dos antecedentes caracterizam o **dilema construtivo**; a conclusão válida é a disjunção dos consequentes: **~c ∨ j'**, "Cristina não é funcionária pública ou João é solteiro" (letra D, com a ordem das parcelas trocada).

### Dilema destrutivo

- Forma: p → q; r → s; **~q ou ~s**; logo **~p ou ~r**. Três premissas: duas condicionais e a disjunção das **negações dos consequentes**; a conclusão é a disjunção das **negações dos antecedentes**.
- **PC-SP**: "se A compareceu, o boletim de A foi lavrado"; "se B compareceu, o de B foi lavrado"; "o boletim de A não foi lavrado ou o de B não foi lavrado". Conclusão válida: **A não compareceu ou B não compareceu** (letra B). Concluir sobre um só dos dois (a ou e) ou a conjunção (c) vai além do que se garante.
- **CREA-MG**: premissas (r ∧ s) → t, s → (t ∧ u) e ~t ∨ ~(t ∧ u): a conclusão é a disjunção das negações dos antecedentes, **~(r ∧ s) ∨ ~s** (letra C).

### Questões clássicas de múltiplas bancas

- **VUNESP/Rio Preto Prev (Fátima, Hugo, Júlia, Gerson)**: afirmações: n ∨ j; ~j ∨ e; a ∨ ~n; ~e (todas V). Começa-se por ~e V: e F. Em ~j ∨ e, ~j é V, logo j F. Em n ∨ j, n é V. Em a ∨ ~n, a é V. A única conjunção verdadeira é **n ∧ a**: "Fátima quer ir à Noruega e Júlia escolheu a Argentina" (letra C).
- **FEPESE/Campos Novos (monitoramento)**: regras s → a (CPU alta gera alerta) e a → d (alerta inicia diagnóstico); fato: d V. Como o consequente d é V, **nada se sabe** sobre a (e, em consequência, sobre s). Resposta: não se pode afirmar com certeza que o servidor ultrapassou o limite (letra E). Moral: afirmar o consequente não prova o antecedente.
- **IBADE/PCES (preparo para o concurso)**: f → (~s ∧ ~c); ~c → b; b → t; e "todos **não** foram aprovados". Cuidado: "todos não foram aprovados" não é a negação de t (t = todos foram aprovados); a negação é "alguém não foi aprovado", e como a frase afirma o fato, **~t é V** (t F). Em b → t, b F; em ~c → b, ~c F (c V); em f → (~s ∧ ~c), o consequente é F, logo f F. A alternativa verdadeira: "Fernando e Bruno não se prepararam" (letra A). O valor de s é indeterminado.
- **Fundatec/Candiota (cadeia de cinco condicionais)**: com o último consequente falso ("Bela não gosta de matemática"), todos os antecedentes anteriores são falsos; logo "Amanda não vai ao cinema" (letra D). As alternativas com "e" adicionam proposições novas e ficam falsas porque a primeira parcela é F.
- **Legalle/Caxias do Sul**: a → b; c → ~d; b → c; d V. De c → ~d com d V: c F; de b → c: b F; de a → b: a F. Resposta: "Ana não é professora" (letra D).
- **QUADRIX/CRMV-TO**: "ou capa laranja ou capa verde" (⊻) é V; "se verde, então vermelha" é F. A condicional falsa dá g V e l F; a exclusiva V com g V dá b F. Alternativa verdadeira: "A capa do diário não é laranja, a da agenda é verde e a do livro não é vermelha" (letra E).
- **IBFC/SES-SE (Zorro, Tica, Diva, Dori)**: I. ~z (V); IV. z ⊻ d (V): d V; III. ~t ∧ dori (V): t F, dori V; II: t → ~d é V porque t F. Conclusão: "Diva é calopsita e Dori é tartaruga" (letra C).

### Para fixar
- Dilema construtivo: duas condicionais + disjunção dos antecedentes ⊢ disjunção dos consequentes.
- Dilema destrutivo: duas condicionais + disjunção das negações dos consequentes ⊢ disjunção das negações dos antecedentes.
- Consequente verdadeiro não informa o antecedente de uma condicional verdadeira.
- "Todos não..." não é a negação de "todos..."; considere o fato dado como verdadeiro.
- Comece sempre pela simples dada, pela conjunção verdadeira ou pela condicional falsa.


---

# TRECHO: raciocinio-logico/a04/s08
##### raciocinio-logico/a04/s08
Este trecho segue com questões comentadas de múltiplas bancas sobre questões clássicas de conectivos (cadeias de condicionais, premissas mistas, itens de certo/errado em bloco) e mostra como o método das quatro etapas se aplica a cada formato.

### Cadeias de condicionais e premissas simples

- **IBFC/SES-SE (conclusão)**: com ~t ∧ r (V), ~z (V) e z ⊻ d (V), obtêm-se t F, r V, z F, d V. A condicional t → ~d fica V porque t é F. A conjunção verdadeira é "Diva é calopsita e Dori é tartaruga" (d ∧ r) (letra C).
- **Fundatec/Sarandi (cinco condicionais)**: a → m → t → ~c → s → f, com f F. De trás para frente: s F; ~c F (c V); t F; m F; a F. Logo, "Carol dança ballet" (c) é V (letra A). Alternativas com proposições novas (Cris canta bem; Ana toca violino) não podem ser verdadeiras.
- **IDECAN/EMPARN (Ângela e Ângelo)**: ~p e e dados como V. De a → p com p F: a F. De e → j com e V: j V. A conclusão verdadeira é "Ângela não estudou para o concurso" (~a) (letra D). Cuidado com a alternativa "estudou **sozinha**": o advérbio cria uma proposição nova e não permitida.
- **IDECAN/Pref. João Pessoa (jardim)**: afirmações ~j → ~p; j → b; c; ~b. De ~b: b F; de j → b: j F; de ~j → ~p com ~j V: ~p V. Logo, jardim não bem cuidado, passarinho não voa e crianças brincam: **~j ∧ ~p ∧ c** (letra E). "Independentemente de a borboleta pousar" indica que c vale em qualquer cenário.
- **SELECON/CIDES (batata, pastel, empada)**: ~e → f; e → ~m; m V (a Márcia comeu empada). De e → ~m com ~m F: e F; então ~e V e f V. A conclusão é "Edelson não comeu batata e Francisco comeu pastel" (letra B).
### Premissas mistas e itens em bloco

- **IBFC/TJPE (irmão, irmã, primo, prima)**: I. a ∧ c (V) dá a e c V. II. c → ~p dá p F. III. ~c ∨ m dá m V. IV. a ⊻ p é V com a V e p F. Alternativa verdadeira: "meu primo não é casado e minha prima é médica" (letra A).
- **QUADRIX/CRESS-PR (itens certo/errado em bloco)**: premissas: Ayra desonesta → Bárbara honesta; Bárbara honesta → Carolina desonesta; Carolina honesta ↔ Déborah desonesta; Déborah desonesta. d V; pela bicondicional, c V; em b → ~c, b F; em a → b, a F. Os três itens ("Ayra é desonesta", "Bárbara é honesta", "Carolina é desonesta") são **errados**. Observe que o texto usa "honesta/desonesta" como simples contrárias; defina a simples em termos afirmativos e use a negação.
- **IBFC/PM-ES**: ~c ∨ b; b → a; ~a. Daí a F, b F, c F; a conclusão verdadeira é "Bruno não joga dama" (~b) (letra E). A alternativa "Se Carlos não joga xadrez, então Arthur joga gamão" é uma condicional **falsa** (V → F).
- **Consulplan/ISS-BH (Demétrio e a matemática)**: "Ou matemática é fácil, ou Demétrio não gosta de matemática" (m ⊻ ~d), "se português não é difícil (é fácil), matemática é difícil" (p → ~m) e d V. De m ⊻ ~d com ~d F: m V. De p → ~m com ~m F: p F. Verdadeira: "português é difícil e matemática é fácil" (~p ∧ m) (letra B). Aqui "difícil" foi tratado como a negação de "fácil", como o enunciado impõe.

### Para fixar
- Comece sempre pelo formato fácil e leve os valores adiante pelas condicionais, de trás para frente quando o consequente é falso.
- Defina as simples de modo afirmativo e trate "difícil/fácil", "honesta/desonesta" como negações apenas se o enunciado deixar claro.
- Um advérbio ou complemento novo ("sozinha", "com Ângela") cria proposição nova: a alternativa não pode ser aceita.
- Em itens de certo/errado em bloco, calcule os valores uma vez e julgue cada item.
- Condicional com antecedente falso é verdadeira; não é preciso conhecer o consequente.


---

# TRECHO: raciocinio-logico/a04/s09
##### raciocinio-logico/a04/s09
Este trecho conclui as questões clássicas de conectivos e abre as questões comentadas de lógica de argumentação (argumentos dedutivos): analisar se a conclusão decorre das premissas, com tabela-verdade e com diagramas lógicos.

### Questões clássicas (continuação)

- **AOCP/DEPEN-PR (cinco suspeitos)**: d → e; ~d → c; (b ∨ c) → ~a; ~e. De ~e: e F. De d → e: d F. De ~d → c com ~d V: c V. Em (b ∨ c) → ~a, o antecedente é V (c V), logo ~a V (a F). O valor de b não se determina. Não foram capturados, além de Enzo, **Adelmo e Dênis** (letra C).
- **Consulplan/Prodabel (afirmação I falsa)**: I. b → a é F, logo b V e a F; II. "ou d ou c" (exclusiva) V; III. c ∧ b V, logo c V e b V; com c V, d F. A conclusão verdadeira é a condicional "se Daniela é engenheira, então Adriana é analista" (d → a, caso F → F; letra D). A opção que usa "ou exclusivo" entre b e c é falsa (os dois são V).
- **Consulplan/Prodabel (cinco proposições com valores dados)**: IV (m → d) é F: m V e d F. I (t ∨ d) V com d F: t V. III (~c ∨ ~t) V com ~t F: ~c V (c F). V (~c ⊻ ~j) V com ~c V: ~j F (j V). II (f ∧ j) é F com j V: f F. A conclusão: "Jonatas fez intercâmbio **ou** Diana é advogada" (j ∨ d) é V (letra A).
- **AOCP/PMPE (Beth, Carla, Esther)**: ~b → c; b → ~e; e V. De b → ~e com ~e F: b F; de ~b → c: c V. A conclusão verdadeira é "Carla é cantora" (letra E).
- **AOCP/PMPE (André, César, Paula, Roberto)**: a → (c ∨ r); c → p; p → r; ~r. De trás: r F; p F; c F; a F. A condicional "se André é de Alagoas, então César não é do Ceará" (a → ~c) tem antecedente F e é V (letra C).

### Lógica de argumentação: argumentos dedutivos (múltiplas bancas)

- **FEPESE/Campos Novos (backup)**: premissas f → b ("sempre que há falha, o backup é acionado") e b V. Afirmar o consequente **não** permite concluir o antecedente. A conclusão válida é "não é possível afirmar que houve falha" (letra E).
- **QUADRIX/CFO (brinquedos de Gael)**: c → e; e → o; ~e ⊻ ~o; c ∨ o. Por tabela, só uma linha torna as quatro premissas V: **c F, e F, o V**. Caminho curto: em ~e ⊻ ~o, e e o diferem; se e fosse V, e → o exigiria o V (e iguais), contradição; logo e F e o V; de c → e com e F: c F. Itens: "O caminhão é vermelho" (**errado**), "A escavadeira é laranja" (**errado**), "O ônibus é azul" (**certo**).
- **Consulplan/CM Araraquara (quatro argumentos)**: por diagramas, só vale o que decorre em todos os diagramas possíveis.
  - **I** (todo aprovado é sancionado; todo sancionado está no orçamento; alguns do orçamento são da saúde; X aprovado): **inválido**, pois X pode estar fora da parte "saúde".
  - **II** (quem falta três vezes é advertido; Carlos foi advertido; logo, faltou): **inválido** (afirmação do consequente; pode haver outro motivo de advertência).
  - **III** (nenhum temporário tem licença remunerada; João está de licença; logo, João não é temporário): **válido** (conjuntos disjuntos).
  - **IV** (se a Câmara rejeita, o projeto é arquivado; Y foi arquivado; logo, Y foi rejeitado): **inválido** (afirmação do consequente).
  - Total de válidos: **um** (letra A).

### Para fixar
- Condicional verdadeira com consequente verdadeiro: o antecedente fica indeterminado; não se pode "voltar" da consequência para a causa.
- Premissa de "nenhum" gera conjuntos disjuntos: bom para conclusões negativas.
- Premissa "alguns" não garante a pertença de um elemento específico.
- Em exclusiva verdadeira, os termos têm valores diferentes.
- Quando um dos termos de uma exclusiva é conhecido, o outro se obtém por oposição.


---

# TRECHO: raciocinio-logico/a04/s10
##### raciocinio-logico/a04/s10
Este trecho segue com questões de lógica de argumentação: validade por diagramas, transitividade, modus ponens e modus tollens, falácias (afirmação do consequente, negação do antecedente), silogismos categóricos e a relação entre validade e premissas falsas.

### Fim da questão de Araraquara e validade por diagramas

- O argumento IV (se a Câmara rejeita, arquiva; Y foi arquivado; logo, foi rejeitado) é **inválido**: Y pode ter sido arquivado por outro motivo. Só o III é válido: há **um** argumento válido.
- **Consulplan/Patrocínio do Muriaé**: no primeiro argumento, os patrocinenses estão contidos nos mineiros e João está fora dos mineiros; logo, está fora dos patrocinenses: **válido** (quem está fora do conjunto maior está fora do menor). No segundo, vitoriosos e quem dorme até tarde são conjuntos disjuntos, e Jéssica não dorme até tarde; isso não a coloca entre os vitoriosos (pode estar fora dos dois): **inválido**. Só o primeiro é válido (letra C).

### Transitividade e contrapositiva

- **QUADRIX/CRESS-PR**: l → ~v e n → v. Contrapositiva da primeira: v → ~l. Encadeando n → v → ~l, obtém-se n → ~l, que é a condicional proposta no item: item **certo**.
- **Fundatec/UFCSPA**: m → ~a; ~r → a (contrapositiva ~a → r); r → ~m. Encadeando m → ~a → r → ~m: **m → ~m**, logo m é F: Marcela **não** é professora (letra B).
- **FGV/DNIT**: "todo carro novo não tem defeitos" (n → ~d) e ~d → s: encadeando, n → s; a contrapositiva é **~s → ~n**: "se não é seguro para viajar, não é novo" (letra E).
- **VUNESP/PC-SP**: premissas ~a; b → ~g; (~g ∨ ~d) → a; ~d → (~e ∧ z). Com ~a (a F), na terceira o antecedente é F: ~g F e ~d F, ou seja, g V e d V. Em b → ~g, com ~g F: b F. Concluindo: "Beta não é cúmplice" (letra C); e e z ficam indeterminados porque ~d é F.

### Falácias e regras de inferência

- **Legalle/Caxias do Sul**: (I) "se chove, a rua molha; a rua está molhada; logo, choveu" é **inválido** (afirmação do consequente; método da conclusão falsa: c F, m V mantém as premissas V). (II) "se A ganha, B perde; B perdeu; logo, A ganhou": **inválido**, mesma forma. (III) "se estudo, passo; não passei; logo, não estudei": **modus tollens, válido**. Só 1 é válido (letra B).
- **ACCESS/Mal. Floriano**: "se o sistema é implantado, os professores precisam de formação; o sistema será implantado; logo, precisam" é **modus ponens** (letra D).
- **ACCESS/Apiaí**: "se o alarme dispara, houve invasão; o alarme disparou; logo, houve invasão" é **modus ponens**, forma válida, e não falácia nem indução (letra B).
- **AOCP/PMPE (hipóteses)**: se uma série de hipóteses apontava para um evento que **não ocorreu**, a conclusão é falsa. Um argumento válido não pode ter premissas todas verdadeiras e conclusão falsa; logo, **pelo menos uma hipótese é falsa** (letra B).
- **CEBRASPE/ANA (astronauta)**: a conclusão "morrerei aqui" contém uma proposição que não aparece nas premissas; não decorre necessariamente delas: argumento **inválido** (item errado).
- **VUNESP/TCM-SP**: (f ∧ a) → m e ~m. Modus tollens: ~(f ∧ a) ≡ **~f ∨ ~a** (a fiscalização não foi correta **ou** as auditorias não foram consistentes; letra E).

### Silogismo categórico por diagramas

- **IBFC/PCP-PR**: "Algum perito é observador" e "Nenhum policial é observador". Desenha-se primeiro o universal (policiais e observadores disjuntos); o perito observador está fora dos policiais. A conclusão válida: **"Algum perito não é policial"** (letra B). "Todo perito é policial", "algum perito é policial", "todo perito é observador" e "todo perito não é observador" não decorrem necessariamente.

### Para fixar
- Afirmar o consequente e negar o antecedente são falácias; modus ponens e modus tollens são válidos.
- Argumento válido com conclusão falsa exige pelo menos uma premissa falsa.
- Encadear condicionais pode levar a p → ~p, que prova p falso.
- Premissa particular afirmativa com universal negativa: conclusão particular negativa.
- Conclusão com proposição estranha às premissas não é válida.


---

# TRECHO: raciocinio-logico/a04/s11
##### raciocinio-logico/a04/s11
Este trecho conclui as questões comentadas de argumentos dedutivos (com dois métodos para a mesma questão e o dilema construtivo) e reapresenta, para treino, a lista das questões clássicas de conectivos resolvidas anteriormente.

### Fim da questão do TCM-SP (modus tollens com De Morgan)

- Premissas: (f ∧ a) → m e ~m. Modus tollens: ~(f ∧ a), que por De Morgan é ~f ∨ ~a (letra E).

### VUNESP/PC-SP: afirmações sem formato fácil

- Dados: "Fulano é culpado e Beltrano é inocente" é **falsa**; "se Fulano é culpado, Beltrano é inocente" é **verdadeira**. Chamando a simples de "inocente" (f para Fulano, b para Beltrano), ~f é "culpado".
- **Por tabela-verdade**: I. ~f ∧ b (F); II. ~f → b (V). As linhas com I falsa e II verdadeira têm f V; logo é falso que Fulano seja culpado (letra E).
- **Por transitividade**: a afirmação I falsa vira verdadeira por negação: ~(~f ∧ b) ≡ f ∨ ~b. Pela regra "ou em condicional", f ∨ ~b ≡ ~f → ~b. Com II (~f → b, cuja contrapositiva é ~b → f), encadeia-se ~f → ~b → f, ou seja, **~f → f**, o que prova que f é V (se f fosse F ocorreria V → F). Mesmo resultado.

### VUNESP/Docas-PB: dilema construtivo

- Premissas: c → m (mais novo que Helena ⇒ Maria estudante); a → j (Amanda trabalha com Ricardo ⇒ José tem 30 anos); c ∨ a. A conclusão do dilema construtivo é **m ∨ j** ("Maria é estudante ou José tem 30 anos"), que aparece com a ordem trocada (letra E).

### QUADRIX/CRN-4: bicondicional e cadeia

- Fatos: "Beatriz come salada ⇔ a salada está temperada" (b ↔ t); João sempre come; t → a (Ana); b → m (Maurício); ~t → j' (Josefina). A bicondicional se quebra em duas condicionais: b → t e t → b.
- **Item 1**: "Se Maurício não comeu salada, ela não estava temperada": contrapositiva de b → m é ~m → ~b; contrapositiva de t → b é ~b → ~t; encadeando ~m → ~b → ~t: item **certo**.
- **Item 2**: "Se Ana não comeu salada, Beatriz também não comeu": contrapositiva de t → a é ~a → ~t; contrapositiva de b → t é ~t → ~b; encadeando ~a → ~t → ~b: item **certo**.
- Observação: as expressões "no almoço" e "todos os dias" são desconsideradas para identificar a mesma simples.

### Lista de questões para treino

- As páginas finais repetem, sem resolução, as questões clássicas já comentadas (Fátima e a Noruega, monitoramento de CPU, preparo para o concurso, cadeia de cinco condicionais, Legalle, capas da Quadrix, IBFC com animais, EMPARN, jardim, batata/pastel/empada, irmão/irmã/primo, itens do CRESS, xadrez/dama/gamão, Demétrio, DEPEN, Prodabel, Beth e Esther, André e Roberto). A recomendação é refazer todas e só depois conferir.

### Para fixar
- Afirmação falsa pode ser reescrita pela sua negação verdadeira (De Morgan).
- Quando surgir ~f → f, f é verdadeira; quando surgir p → ~p, p é falsa.
- Bicondicional vira duas condicionais; depois encadeie com contrapositivas.
- Dilema construtivo: duas condicionais e a disjunção dos antecedentes dão a disjunção dos consequentes.
- Nas listas finais, refaça as questões antes de ver as resoluções.


---

# TRECHO: raciocinio-logico/a04/s12
##### raciocinio-logico/a04/s12
Este trecho final traz os gabaritos das listas de questões da aula e a lista de treino de lógica de argumentação (argumentos dedutivos). Como não há matéria nova, este resumo reúne um roteiro de revisão da aula inteira e os resultados esperados de cada bloco.

### Gabarito do bloco "questões clássicas de conectivos" (22 questões)

- Na ordem da lista: C, E, A, D, D, E, C, A, D, E, B, A, Errado, Errado, Errado, E, B, C, D, A, E, C.
- Padrões: cadeias de condicionais com consequente final falso (quatro questões); simples dada como V no enunciado (várias); condicional falsa; disjunção exclusiva verdadeira; conjunção verdadeira que fixa duas simples; indeterminação de uma simples sem prejudicar a resposta.

### Gabarito do bloco "argumentos dedutivos" (21 questões)

- Na ordem da lista: E, Errado, Errado, Certo, A, C, Certo, B, D, B, B, Errado, B, E, B, C, E, E, E, Certo, Certo.
- Padrões: afirmação do consequente (inválido); modus ponens e modus tollens (válidos); silogismo hipotético e encadeamento de condicionais com contrapositiva; dilema construtivo; diagramas para "todo", "nenhum" e "alguns"; argumento válido com pelo menos uma premissa falsa quando a conclusão é falsa.

### Roteiro de revisão da aula

1. **Questões clássicas**: quatro etapas (formato fácil, símbolos, valores das simples, alternativa verdadeira).
2. **Conceitos**: argumento, premissas, conclusão, silogismo, categórico × hipotético, validade × veracidade, condicional associada.
3. **Silogismo categórico**: termos, modos, figuras, oito regras (duas particulares ou duas negativas não concluem; conclusão segue a premissa mais fraca).
4. **Métodos**: diagramas (categóricos); premissas verdadeiras (formatos fáceis); tabela-verdade (linhas com todas as premissas V); conclusão falsa (conclusão simples, "ou" ou condicional); transitividade; regras de inferência.
5. **Regras de inferência**: modus ponens, modus tollens, silogismo hipotético, dilema construtivo, dilema destrutivo.
6. **Falácias**: afirmação do consequente e negação do antecedente.

### Para fixar
- Faça de novo as listas de questões antes de olhar os gabaritos.
- Use os gabaritos para identificar o tipo de erro (leitura, regra, cálculo).
- Revise as regras de inferência e as falácias, que mais caem.
- Em argumentos com "alguns", desconfie: raramente decorre conclusão sobre um elemento específico.
- Argumento inválido pode ter conclusão verdadeira; válido pode ter conclusão falsa.


---

# TRECHO: raciocinio-logico/a05/s01
##### raciocinio-logico/a05/s01
Este trecho apresenta a estrutura básica dos argumentos (premissas e conclusão), os indicadores de premissa e de conclusão e a classificação em argumentos dedutivos, indutivos e abdutivos.

### Estrutura básica

- **Argumento**: relação entre um conjunto de **premissas** que sustentam a defesa de uma **conclusão**, ligadas por um vínculo lógico.
- **Premissa**: declaração, afirmação ou fato a partir do qual a conclusão é construída; indica as **razões** pelas quais a conclusão deve ser aceita (responde "por que devo aceitar isso? quais as evidências?"). Em argumentos dedutivos, as premissas são proposições **consideradas verdadeiras**.
- **Conclusão**: afirmação ou julgamento resultante das razões apresentadas; é o que se **quer demonstrar**.
- **Conclusão**: costuma ser marcada por "portanto", "logo" e "por isso", e também por "assim", "então", "consequentemente", "deste modo", "por conseguinte" ou "pode-se inferir que".
- **Premissa**: costuma vir depois de "porque", "pois", "visto que", "dado que" ou "uma vez que", e de "tanto que", "devido a", "admitindo que" e "assumindo que". As listas são apenas auxiliares.
- As listas **não esgotam** as possibilidades; o que decide é o conceito (a conclusão é o julgamento, a premissa é o fato que o sustenta).
- **A conclusão pode aparecer em qualquer posição** (início, meio ou fim). Exemplo: "Esta rua é a mais segura do bairro, porque tem câmeras em todos os postes e policiamento diário" tem a conclusão no início; já em "A loja abre cedo, logo vende mais, e ainda fecha tarde", a conclusão está no meio.
- Uma frase com **uma só proposição** simples, sem razões, **não é argumento** (ANVISA/2016: a enumeração de consequências ambientais não configura argumento válido, item errado).

### Reconhecimento da estrutura em questões

- **PC-AM**: pede o trecho em que **a premissa vem antes e leva à conclusão**. Na alternativa certa, um ruído ouvido na cozinha é o fato e, em seguida, vem o julgamento sobre o que a cozinheira deve ter deixado no chão (letra A). Nas outras alternativas a conclusão (com "deve", "possivelmente", "talvez") vem antes da razão introduzida por "porque", "já que" ou "pois" (ou por ponto e vírgula).
- Palavras de **probabilidade** (talvez, possivelmente, deve) sinalizam o julgamento, ou seja, a conclusão.
- **Pref. Sete Lagoas**: "É lógico que o time A é o melhor ..., uma vez que tem o melhor ataque, a defesa menos vazada e mais pontos" tem como conclusão que o time A é o melhor do campeonato (letra A); o "uma vez que" introduz as premissas.
- **BNB**: num texto que afirma que a saúde enriquece "pois" quem é saudável trabalha muito e quem trabalha muito enriquece, a conclusão é a primeira frase (item certo): o "pois" indica que o que vem depois são premissas.

### Classificação dos argumentos

- **Dedutivos**: objeto da lógica formal/proposicional; **não produzem conhecimento novo** (a conclusão já estava nas premissas); usam uma **regra geral** para casos particulares; **só eles** podem ser **válidos ou inválidos**.
- **Indutivos**: a conclusão traz conhecimento novo, que **transcende** as premissas, por **generalização** de casos observados ou extensão para um novo caso. Não são válidos/inválidos: são "mais fortes" ou "mais fracos" (conclusão "mais" ou "menos provável"). A **analogia** é um tipo de indução em que se destacam características comuns.
- **Abdutivos**: a conclusão é a **melhor explicação** para os fatos das premissas, uma **hipótese explicativa**. Também não são válidos/inválidos; podem ser mais fortes ou mais fracos conforme surjam novas informações.
- **Peirce**: na **dedução**, dados a regra e a hipótese (premissa), chega-se à conclusão; na **indução**, dados a hipótese (premissa) e a conclusão, chega-se à regra; na **abdução**, dados a regra e a conclusão, chega-se à hipótese (premissa).

### Para fixar
- Premissa é a razão; conclusão é o que se quer demonstrar.
- "Logo", "portanto" e "assim" introduzem conclusão; "pois", "porque" e "visto que" introduzem premissa.
- A conclusão pode estar em qualquer posição do texto.
- Só o argumento dedutivo é válido ou inválido; indutivo e abdutivo são fortes ou fracos.
- Indução generaliza; abdução propõe a melhor explicação; dedução não traz conhecimento novo.


---

# TRECHO: raciocinio-logico/a05/s02
##### raciocinio-logico/a05/s02
Este trecho aprofunda a classificação dos argumentos: inferência analítica (dedutiva) e sintética (indutiva e abdutiva), o raciocínio indutivo com questões de concurso, a noção de argumento mais forte ou mais fraco e as analogias.

### Dedução

- Inferência pode ser **analítica** (dedutiva) ou **sintética** (indutiva ou abdutiva). Os dedutivos **não produzem conhecimento novo**: a informação da conclusão já estava nas premissas. Em regra, são objeto da lógica formal/proposicional, mas o conceito vale para qualquer raciocínio que parte de uma **regra geral** para analisar **casos particulares**.
- **Só eles** são válidos ou inválidos: válido se a conclusão é necessariamente verdadeira quando as premissas são consideradas verdadeiras; inválido se não é necessariamente verdadeira. Os outros dois tipos são avaliados de modo subjetivo.

### Indução

- O argumento indutivo traz **conhecimento novo**, que **não está nas premissas, nem implicitamente**: a conclusão **transcende** as premissas, estendendo fatos observados a um novo caso ou a todos os casos (**generalização**).
- **TJDFT**: entre as alternativas, a indutiva é a que parte de um caso particular do passado ("ontem nevou bastante") para um caso novo ("as estradas devem estar intransitáveis"); as demais partem de uma regra geral para um caso particular, ou seja, são dedutivas (letra E).
- **SEDUC-AM**: raciocínios que generalizam a partir de metais específicos que conduzem eletricidade ("todos os metais conduzem") e de corvos observados ("provavelmente todos os corvos são negros") são **indutivos**; o que conclui "todo homem é vertebrado" de "todo homem é mamífero" e "todo mamífero é vertebrado" é **dedutivo** (diagramas: homens dentro de mamíferos, dentro de vertebrados). Resposta: só 1 e 3 (letra C).

### Argumentos mais fortes ou mais fracos

- Indução não é válida/inválida: é **mais forte** (conclusão mais provável) ou **mais fraca**. Exemplo: observar cinco cães que comem brócolis permite "a maioria dos cães come brócolis"; mais observações **fortalecem** o argumento, enquanto casos contrários o **enfraquecem**. Trocar a conclusão por algo menos ambicioso ("mais de 20% dos cães comem") também a fortalece. "Mais forte" ou "mais fraco" **nada diz sobre a validade**.
- Exemplo estatístico: se 80% dos professores de um instituto têm mestrado e Fulano é professor ali, "Fulano tem mestrado" é provável mas não garantido; com 50% em vez de 80%, o argumento fica **mais fraco**.
- **SEFAZ-SP (2002)**: a conclusão mais forte é a que abrange a **maior fração do intervalo** da premissa. Frações: 10/30 = 1/3, 20/30 = 2/3, 5/45 = 1/9, 15/40 = 3/8 e 10/40 = 1/4; a maior é 2/3, em "os livros custam de 10 a 40; este custa de 10 a 30" (letra B).
- **Ciências experimentais** usam indução: observam casos particulares (dois pares de corpos com a mesma lei de atração) e formulam uma conclusão geral.
- **MPE-SP (2011)**: o argumento "a = b e b = c; logo a = c" é dedutivo válido; o argumento "5/6 dos funcionários têm nível superior; José é funcionário; logo, tem nível superior" **não é válido** na lógica dedutiva: é indutivo (letra D).

### Analogias

- **Analogia** é indução em que se destacam **características comuns** entre dois casos para concluir algo sobre o segundo. Sua força depende de:
  - **relevância** das características comparadas para a conclusão (ser acionista de empresa lucrativa é mais relevante para ser bilionário do que acordar cedo);
  - **força da conclusão** em relação às premissas ("não é pobre" é mais provável que "é bilionário");
  - **número de comparações** (mais casos semelhantes tornam a analogia mais forte);
  - **quantidade de características** comparadas (acrescentar uma característica comum, como a loja de compra, a fortalece).

### Para fixar
- Dedução: sem conhecimento novo, regra geral → caso particular, válida ou inválida.
- Indução: generalização que transcende as premissas; mais forte ou mais fraca, nunca válida.
- Conclusão menos ambiciosa e mais observações fortalecem a indução; casos contrários a enfraquecem.
- Em questões de "argumento mais forte" com intervalos, compare a fração do intervalo coberta.
- Analogia: depende da relevância e do número de características e de casos comparados.


---

# TRECHO: raciocinio-logico/a05/s04
##### raciocinio-logico/a05/s04
Este trecho conclui as falácias formais (negação do antecedente) e inicia as falácias informais: ad hominem (três tipos), apelo à autoridade, apelo à ignorância, falso dilema e pergunta complexa, todas com questões de concurso.

### Falácia da negação do antecedente

- O **modus tollens** (p → q; ~q; logo ~p) é válido. A **negação do antecedente** (p → q; **~p**; logo **~q**) é **inválida**. Outra forma: de "p → q" concluir "~p → ~q" (a inversa). Exemplo: "Se o motor esquenta, o ventilador liga; o motor não esquentou; logo, o ventilador não ligou" (o ventilador pode ligar por outro motivo).

### Falácias informais: ideia geral

- Têm **erro no conteúdo** (ou na relação entre premissas e conclusão), mas aparentam correção; **não se identificam** por regras de inferência ou tabela-verdade. As bancas cobram mais o **reconhecimento** da falácia do que a nomenclatura.

### Argumento contra a pessoa (ad hominem)

- Forma geral: A afirma X; B ataca A; logo X é falso. Rejeita-se o argumento **pela desqualificação de quem o apresenta**, afastando a discussão do conteúdo.
- **Ofensivo ou abusivo**: ataque direto à pessoa (moral, profissional, religioso, de classe etc.). Exemplo: A propõe um plano de trânsito com razões X e Y; B responde "o seu plano não presta, você é um incompetente". O oponente não discute X e Y.
- **Circunstancial**: expõe circunstâncias individuais de A para pôr em dúvida sua **imparcialidade** (B diz que A só fala isso porque é dono de uma empresa que ganha com a medida).
- **"Você também" (tu quoque)**: aponta a incoerência entre o que A diz e o que A faz (B diz "quem fala, usava o mesmo método no mês passado").
- **CGU/2022** (crônica de Rubem Braga sobre o padre Feijó): ataque direto à pessoa, com expressões como "mediocridade", "limitado": **ad hominem ofensivo**. A alternativa correta diz que o argumento "não procura desacreditar uma ideia em função de um aspecto negativo da pessoa, mas se prende diretamente às marcas negativas da própria pessoa" (letra C). A que descreve a contradição entre dizer e fazer é o "você também".

### Apelo à autoridade

- Forma: A é suposta autoridade no assunto; A afirma X; logo X é verdadeiro. Muito usado na venda de produtos e ideias (uma celebridade do entretenimento "recomenda" um xampu).
- É **lícito** apelar a uma autoridade se, cumulativamente: (1) ela tem de fato **expertise** no assunto; (2) há **concordância** entre outros especialistas; (3) há **outros elementos** que sustentam o argumento; (4) a autoridade é **identificada**.
- Falácia quando a pessoa não é autoridade no tema (alguém com doutorado em matemática opinando sobre a Idade Média) ou quando a autoridade é **anônima** ("especialistas dizem", "cientistas acreditam", "li num livro").
- Citar Newton para leigos que discutem a gravitação reforça o argumento; entre físicos teóricos debatendo avanços recentes, já não bastaria.

### Apelo à ignorância

- Considerar algo **verdadeiro porque não se provou que é falso**, ou **falso porque não se provou que é verdadeiro**: "não há provas de X, logo X é falso" / "não há provas de que X é falso, logo X é verdadeiro". Exemplo: "ninguém provou que o produto faz mal, portanto é seguro".

### Falso dilema (falsa dicotomia)

- Apresentam-se só **duas opções** (ou poucas) quando há outras: "só X ou só Y; Y é falso; logo X". Exemplos: "ou você apoia o projeto ou é contra o progresso"; "ame-o ou deixe-o" (é possível não amar sem partir). **DPE-RO**: o autor do texto usa "no banco da escola ou no banco dos réus", um falso "ou um ou outro" (letra D).
- **Pref. Cruzeiro do Sul**: "João nunca fez terapia, logo não pode falar de terapia" e "se o terapeuta vota nesse partido, é mau terapeuta" são **ad hominem**; "a terapia sempre funciona, pois ninguém mostrou que não funciona" é **apelo à ignorância** (letra B).

### Pergunta complexa

- Une dois temas numa só pergunta, de modo que qualquer resposta "sim" ou "não" **aceita ambos**. Exemplo: "O senhor já parou de falsificar documentos?" Responder "sim" admite que falsificava e agora não; "não" admite que falsificava e continua. Defesa: **quebrar** a pergunta ("Eu nunca falsifiquei e nunca falsificarei").
- **INPI/2024**: "Você continua furtando celulares e carteiras no transporte público?": tanto "sim" quanto "não" prejudicam o interrogado (item certo).
- **TCU/2015**: "Você deixou de roubar dinheiro de seus pais?" pressupõe que **no passado** roubava; nada se pressupõe sobre o presente. O item que dizia que pressupõe que "não rouba mais" é **errado**.

### Para fixar
- Negação do antecedente: p → q; ~p; logo ~q (inválida); o modus tollens é o correto.
- Ad hominem: ofensivo (ataque direto), circunstancial (imparcialidade) e "você também" (incoerência).
- Apelo à autoridade é legítimo só com expertise, concordância, outros elementos e autoridade identificada.
- Apelo à ignorância: "não provaram que é falso, logo é verdade".
- Falso dilema reduz as opções; pergunta complexa embute uma acusação.


---

# TRECHO: raciocinio-logico/a05/s05
##### raciocinio-logico/a05/s05
Este trecho segue com as falácias informais: espantalho, petição de princípio, conclusão irrelevante, falso escocês, apelos emocionais (povo, piedade, força, consequências), acidente e sua inversão, divisão e composição, falácias indutivas (generalização apressada, falsa analogia, jogador, derrapagem) e o início das falácias causais.

### Fim da pergunta complexa

- Para desfazer "Você deixou de roubar dinheiro dos seus pais?", separa-se em "você roubava?" e "e agora, você rouba?". A pergunta original pressupõe apenas o passado (item da TCU, errado).

### Espantalho (homem de palha)

- A afirma X; B combate uma versão **distorcida** Y. Exemplo: A defende que todos tenham direito a ampla defesa; B responde "você quer criminosos soltos?" e discorre sobre violência. A distorção troca o tema.

### Petição de princípio (raciocínio circular)

- A premissa só é verdadeira se a **conclusão já for aceita**. Exemplo: "Este manual é infalível porque o seu autor nunca erra, e sabemos que o autor nunca erra porque escreveu o manual infalível."
- **INPI/2024**: um professor conclui que o livro é fraco porque "já pelo capítulo inicial se vê que traz informações superficiais"; conclusão e premissa dizem o mesmo. É **petição de princípio**, e não apelo à autoridade (item errado).

### Conclusão irrelevante (*ignoratio elenchi*)

- As premissas **não têm relação relevante** com a conclusão. Exemplo: um vereador diz que quer uma cidade com emprego e renda para todos e conclui que se deve aprovar a redução do imposto sobre serviços. O desejo é consensual e não prova que o projeto produzirá esse resultado; falta demonstrar a relação.

### Falso escocês

- B mostra um **contraexemplo** à afirmação X de A; A **restringe a definição** de X para excluir o caso ("não é um verdadeiro..."). Exemplo: "Todo carioca torce por tal clube" – "meu tio é carioca e não torce" – "então ele não é carioca de verdade, saiu do estado".

### Apelos às emoções

- **Apelo ao povo**: "todos acreditam/fazem X, logo X é verdadeiro/bom" (o uso generalizado não prova qualidade).
- **Apelo à piedade**: alegações para causar pena ("estudei dez horas por dia e minha mãe me castiga se eu tirar nota baixa, então mereço a nota").
- **Apelo à força**: alegações para causar **medo** (inclusive ameaça velada, como lembrar ao professor que a mãe do aluno é a reitora).
- **Apelo às consequências**: algo é verdadeiro se tem consequências boas, ou falso se tem consequências ruins ("não acredito em crise, senão não dormiria tranquilo"; "você não pode ser favorável porque perde adicionais").

### Acidente e inversão do acidente

- **Acidente**: aplicar a regra geral onde as circunstâncias pedem **exceção**. Exemplo: o limite de velocidade é 110 km/h, "logo, mesmo diante de uma emergência médica, você não pode passar disso"; ou "devolver o que foi emprestado" mesmo que seja uma arma a alguém perigoso.
- **Inversão do acidente**: tomar a **exceção como regra**. Exemplo: "se um paciente terminal pode usar certa droga, todos devem poder". **ANPAD**: "já que você pode ir à boate, todos aqui de casa podem" (letra D).

### Divisão e composição

- **Divisão**: "o todo X tem a característica C, logo as partes têm C" (a água sanitária desinfeta, logo o sódio isolado desinfeta; "homens ganham em média 30% mais, logo João da Etiópia ganha mais que Maria americana").
- **Composição**: "as partes têm C, logo o todo tem C" (um átomo não tem cor, logo um carro não tem cor; "uma fábrica gasta mais energia que uma casa, logo todas as fábricas gastam mais que todas as casas").

### Falácias indutivas

- **Generalização apressada**: conclusão de uma amostra não representativa (um motorista grosseiro de uma cidade e a conclusão de que todos os moradores são mal-educados).
- **Falsa analogia**: comparação entre coisas tão diferentes que a indução é fraca demais (alunos "como diamantes", logo devem ser pressionados). **São Joaquim**: falsa analogia é a analogia entre dois casos inadequada ou inválida (letra D).
- **Falácia do jogador**: crer que um evento "tem de ocorrer" porque não ocorreu há tempo (dez caras seguidas e a certeza de que a próxima será coroa; ações subindo dez dias e "agora vai cair"). Cada lance é **independente**.
- **Derrapagem (bola de neve)**: encadeia condicionais em que ao menos um elo é fraco (beber leva ao vício, que leva a perder o emprego, que leva à miséria da família).

### Falácias causais

- Para afirmar **causa e efeito** são necessárias três coisas: **correlação**, **precedência temporal** da causa e **eliminação de outras causas**.
- **Falsa causa**: atribuir causa a algo sem base (um torcedor famoso no estádio "causou" a goleada). **FUNPRESP-JUD**: "sempre que venho aqui, chove; logo minha vinda traz chuva" é falsa causa (item certo).
- **Causa comum (efeito conjunto)**: X e Y correlacionados, ignora-se um fator Z que gera ambos (o consumo de sorvete e os casos de uma doença sazonal sobem juntos por causa do verão).
- **Post hoc ergo propter hoc**: "X ocorreu antes de Y, logo X causa Y" (o galo canta antes do nascer do sol, mas não o provoca).
- **Inversão de causa e efeito**: troca-se o que causa pelo que é efeito (o mofo no pão é que o deteriora, não o contrário).
- **Causa complexa**: apresenta-se apenas **uma** das várias causas (um acidente atribuído somente à falta de treinamento).

### Para fixar
- Espantalho distorce a tese; petição de princípio é circular; conclusão irrelevante não se relaciona.
- Falso escocês muda a definição para escapar do contraexemplo.
- Apelos: povo (todos aceitam), piedade (pena), força (medo), consequências (resultados).
- Acidente aplica regra onde cabe exceção; inversão do acidente generaliza a exceção.
- Divisão vai do todo às partes; composição vai das partes ao todo.
- Causalidade exige correlação, precedência e eliminação de outras causas.


---

# TRECHO: raciocinio-logico/a05/s06
##### raciocinio-logico/a05/s06
Este trecho fecha o catálogo de falácias (causa complexa e insignificante, falácias de ambiguidade) e inicia as questões comentadas de múltiplas bancas sobre estrutura básica e classificação dos argumentos (dedução, indução, abdução).

### Causa complexa e causa insignificante

- **Causa complexa**: um fenômeno multifatorial é explicado por apenas parte das causas. **INPI/2024**: um entrevistado explica o seu sucesso listando algumas virtudes pessoais; há outros fatores, logo é causa complexa, que é uma espécie de **falsa causa** (item certo).
- **Causa insignificante**: a causa citada é legítima, mas **pequena** diante das demais. Exemplo: "ao fazer churrasco com carvão você contribui para o aquecimento global" (contribui, mas é desprezível frente a outras fontes).

### Falácias de ambiguidade

- **Equívoco**: uma palavra usada com **dois sentidos** no mesmo raciocínio. Exemplo: "Quem sofre de transtorno mental não deve portar arma; Pedro é louco por futebol; logo, não deve portar arma" ("louco" muda de significado).
- **Anfibologia**: a **construção** da frase admite duas leituras ("João atirou no irmão da vítima com uma pistola": quem tinha a pistola?).
- **Ênfase**: a conclusão depende de **enfatizar** certas palavras da premissa. "Não devemos falar mal dos amigos" não permite concluir "podemos falar mal de quem não é nosso amigo", a menos que se enfatize "nossos amigos". Mesmo uma afirmação verdadeira pode enganar pela ênfase (manchete em letras grandes "PROTESTOS VIOLENTOS" seguida, em letras minúsculas, de "são esperados pelas autoridades").
- Para a prova, importa mais **identificar** o erro do que decorar a classificação.

### Questões: estrutura básica e classificação

- **FGV/TCE-PE**: dedução = regra geral → caso particular; indução = casos observados → generalização. O raciocínio "nenhum gato visto até hoje era roxo, logo não existe gato roxo" é **indutivo**; o da regra dos números primos é dedutivo; o da empresa que aumenta lucro e "logo reduziu custos" é dedutivo **inválido** (afirmação do consequente). Só o terceiro é indutivo (letra E).
- **SEBRAE-GO**: "pela manhã estava calor e sem nuvens; à tarde, ameno e parcialmente nublado; logo, quando está nublado não pode fazer calor" generaliza a partir de duas observações: **indução** (letra D).
- **Consulplan/DPE-PR**: o indutivo é o que generaliza a partir de casos (três servidores com oportunidades de formação no exterior ⟶ "ser servidor da DPE significa ter oportunidades de aprimoramento"; letra D). Os demais partem de regra geral para caso particular.
- **CEBRASPE/TRF-6**: "João e Maria têm cabelo preto; logo, os filhos terão" é **indução** (item errado se chamar de abdução). "Não achei o livro na estante; logo, alguém mexeu e o pegou" é **abdução** (melhor explicação), não indução (item errado).
- **FEPESE/Brusque**: "todos os cães que conheci são bravos; logo, todos os cães devem ser bravos" é **indução** (letra E).
- **SELECON/Rio Brilhante**: o exemplo dedutivo é o que parte de uma regra geral ("viagens aéreas produzem tragédias") para um caso particular ilustrativo (letra D).
- **COPESE/UFT (características da dedução)**: consequente que é inferência **necessária** do antecedente (certo); consequente que **não excede** o conteúdo do antecedente (certo); não traz conhecimento novo, apenas organiza o já adquirido (certo); organização por enumeração e "sempre do particular ao geral" são características da indução (errado). Corretas: I, III e V (letra D).
- **CEBRASPE/CGE-RJ**: de uma opinião genérica ("se acredita, não precisa de explicação; se não acredita, não adianta explicar") não se infere que a ideologia "prescinde de explicação": nem dedução, nem indução, nem abdução sustentam isso (item errado).
- **IBFC/Pref. Cuiabá**: usar a regra e a premissa para chegar à conclusão é **dedução** (letra D); usar a conclusão e a regra para propor a premissa que a explica é **abdução** (letra C).
- **IDCAP/CREA-BA**: "Carlos é atleta; todo atleta gosta de açaí; logo, Carlos gosta" é **dedução** (letra A).
- **FGV/Câmara dos Deputados**: passar de fatos particulares a um princípio geral, pela repetição de regularidades, é **indução** (letra D).
- **IMPARH/Fortaleza (modus tollens em cadeia)**: d → b, b → r, r → s, s → a, com ~r. De b → r e ~r: ~b; de d → b: ~d. Logo, João **não comeu muitos doces** (letra A); nada se sabe sobre sono nem atraso.

### Para fixar
- Equívoco: palavra com dois sentidos; anfibologia: frase ambígua; ênfase: sentido alterado por destaque.
- Causa complexa omite causas; causa insignificante cita causa pequena demais.
- Dedução: regra → caso; indução: casos → regra; abdução: explicação hipotética.
- "Não encontrei X, logo alguém levou" é abdução.
- Modus tollens em cadeia nega os antecedentes anteriores.


---

# TRECHO: raciocinio-logico/a05/s07
##### raciocinio-logico/a05/s07
Este trecho continua as questões comentadas sobre estrutura básica e classificação dos argumentos: reconhecer premissa e conclusão, classificar o raciocínio em dedução, indução ou abdução e distinguir indução forte e fraca.

### Fim da questão de João e o remédio

- Com ~r (não tomou remédio), o modus tollens em b → r dá ~b; o modus tollens em d → b dá ~d: João **não comeu muitos doces**. Nada se conclui sobre sono (s) nem sobre atraso (a). Letra A.

### Tipos de raciocínio (Peirce) em questões do IBFC

- **Regra + premissa ⇒ conclusão**: dedução (IBFC/MGS, letra A).
- **Premissa + conclusão ⇒ regra**: indução (IBFC/DPE-MT, letra A).
- **Regra + conclusão ⇒ premissa que explica**: abdução (letra C). Dadas a premissa, a conclusão e a regra, "abdução corresponde a determinar a premissa".

### Premissa levando à conclusão

- **FGV/PC-AM** (mesma questão da PC-AM): a alternativa certa é a em que o **fato vem antes** e o julgamento depois (um barulho ouvido na cozinha e a hipótese sobre o pote de ração); o raciocínio é abdutivo. Nas outras o julgamento (com "deve", "possivelmente", "talvez") vem primeiro.
- **FGV/TJDFT**: a alternativa indutiva é a que parte de um caso passado ("ontem nevou bastante") para um novo caso ("as estradas devem estar intransitáveis"); as demais são regras gerais aplicadas a um caso particular.

### Itens do FUNPRESP-Jud (AOCP)

- Um raciocínio com a regra "trabalhar de manhã leva a folgar à tarde" e o fato de ter trabalhado hoje de manhã, concluindo que se folgará à tarde, é **dedução** (modus ponens): item certo.
- Se o mesmo raciocínio parte do fato de ter folgado à tarde para supor que se trabalhou de manhã, é a **melhor explicação** (abdução), e não indução: item errado.
- "Todo argumento por analogia é sempre indutivo, nunca dedutivo; infere a conclusão como provavelmente verdadeira": item **certo**.

### Outras classificações

- **FGV/TCE-AM**: "Sinto vergonha, logo existo" tem **uma premissa e a conclusão** (introduzida por "logo"). Para ser um silogismo dedutivo válido faltaria a premissa maior ("quem sente vergonha existe"). A afirmação **inadequada** é a que diz que falta a conclusão (letra A); é verdade que há intertextualidade com "penso, logo existo", opinião pessoal, texto argumentativo e ausência de duas premissas.
- **IBFC/Cruzeiro do Sul (rosas e violetas)**: com "só há rosas e violetas", "rosas são vermelhas" e "violetas são azuis", concluir que uma flor vermelha é rosa é **dedução** (letra D).
- **IBFC/Candeias**: indução parte de particularidades para conclusão geral (V); dedução usa regra geral para casos particulares (V); indução e dedução são tipos diferentes de raciocínio (V). Sequência V, V, V (letra C).
- **IBFC/Santo Agostinho (urna com 20 bolas)**: a probabilidade de 50% de tirar azul (10 azuis e 10 vermelhas) é **dedução** (certeza matemática); concluir que o sorteio é "provavelmente viciado" após dez azuis seguidas é **indução** (probabilística); saber a última bola após retirar 19 é **dedução**. Letra A.
- **IBFC/IDAM**: o exemplo de indução é o que generaliza a partir de casos ("os cães do bairro têm rabo; cães são quadrúpedes; então quadrúpedes têm rabo"); os demais são dedutivos (letra A).
- **IBFC/Cruzeiro do Sul (lei da inércia)**: de atritos cada vez menores resultando em deslocamentos cada vez maiores, generaliza-se que sem atrito o corpo não pararia: **indução** (letra B).
- **Consulplan/CM-BH (gato preto)**: três pessoas veem um gato preto e sofrem azar; generaliza-se que gato preto traz azar: **indução** (letra A), e fraca.
- **Consulplan/CM-BH (fumaça e bombeiros)**: concluir que há incêndio no terminal é uma **abdução** (melhor explicação). Como as opções não trazem abdução, e parte da literatura divide os argumentos só em dedutivos e indutivos, classifica-se como **indutivo forte** (letra B), pois as evidências tornam o incêndio muito provável.

### Para fixar
- Fato primeiro, julgamento depois: premissa levando à conclusão.
- Regra + premissa = dedução; premissa + conclusão = indução; regra + conclusão = abdução.
- Analogia é sempre indução; a conclusão é provável, não necessária.
- Probabilidade de um sorteio com quantidades conhecidas é dedução; "provavelmente viciado" é indução.
- Quando só há dois tipos de argumento (dedutivos e indutivos), a abdução entra como indutivo.


---

# TRECHO: raciocinio-logico/a05/s08
##### raciocinio-logico/a05/s08
Este trecho reúne questões comentadas de várias bancas sobre argumentos falaciosos e apelativos: identificar o tipo de falácia a partir de um diálogo ou de uma frase.

### Falácias apelativas e de ideia popular (CEBRASPE/TRF-6)

- **Apelo à piedade**: pedir que o relatório seja aprovado porque "a comissão trabalhou com muito afinco" não dá razões; busca pena (item certo).
- **Apelo ao povo**: B diz que C é incompetente porque "muitas pessoas dizem isso" (item certo: aceitação geral não prova).
- **Apelo à ignorância**: "não há estudos que mostrem que o remédio faz mal, logo faz bem" (item certo). A frase "o que não mata, engorda" reforça o tom apelativo.
- **Apelo às consequências**: João defende priorizar o setor jurídico porque, sem recursos, decisões perdem eficiência. Prova que "não priorizar" é errado só pelas consequências negativas (item certo).
- **Falso dilema**: "lute contra a corrupção! Ou, por acaso, o senhor não é digno do cargo?" Só duas opções extremas, com intuito de forçar a adesão (item certo). "A automação em todos os processos é o futuro e, portanto, a única solução viável" ignora a alternativa gradual: falsa dicotomia (item certo). **IAUPE**: falsa dicotomia = apresentar duas opções quando há várias (letra A).

### Falácias formais (negação do antecedente e afirmação do consequente)

- "Todos os funcionários do setor virão de branco; João não é do setor; logo, não virá de branco" tem a forma p → q; ~p; logo ~q: **negação do antecedente, inválido**. Também é errado chamar um argumento dedutivo de "válido, porém fraco": fraco/forte só se aplica a indutivos (item errado).
- "Quando chove, a rua alaga; a rua está alagada; logo, choveu" é **afirmação do consequente, inválido** (item errado se disser que é válido).
- **IDCAP/Serra**: "Se o aluno estuda, tem bom desempenho; Marina não estudou; logo, não teve" é **negação do antecedente** (letra C).
- **AOCP/FUNPRESP-Jud**: "Se Antenor é analista de seguridade, é servidor; é servidor; logo, é analista" é afirmação do consequente (item certo).

### Falsa analogia e causalidade

- **IGEDUC/Camaragibe**: concluir que quem tem água tem automaticamente oxigênio, só porque ambos são essenciais à vida, é **falsa analogia** (item errado se afirmar validade).
- **IMPARH/ACFor**: ver que a temperatura média sobe enquanto o número de piratas cai e concluir que os piratas resfriavam as águas é **falsa causa** (confunde correlação com causalidade; letra B). **IMPARH/PGM**: um planeta esquentou depois de adotar nova tecnologia agrícola; a conclusão "a tecnologia causa o aquecimento" **pode estar errada** porque ignora outras variáveis (letra C): não se pode afirmar nem que é impossível nem que está provado.
- **FUNATEC/S. J. Basílios**: a falácia de **falsa analogia** é a analogia entre dois casos que é inválida ou inadequada (letra D); um exemplo de falácia apelativa é o apelo à emoção no lugar de evidências (letra C).

### Autoridade e ad hominem

- **IBADE/PMPB** (anulada): uma grande figura da música afirma um fato técnico sobre instrumento (violão com cinco cordas) e isso é tomado como prova porque "é grande violonista": **apelo à autoridade**, pois a autoridade não basta para um fato verificável (e o fato é falso).
- **IBFC/SGDA**: o item que faz crítica geral a um conjunto de pessoas por déficit educacional não é ad hominem; "o filósofo deu entrevista à revista X, então sua opinião não é confiável" e "quem nunca fumou não pode opinar sobre tabagismo" são **ad hominem circunstanciais** (letra D).

### Para fixar
- Apelo ao povo: "muitos acham"; apelo à piedade: "trabalhamos muito"; consequências: "se não, perde-se a eficiência".
- Falso dilema: opções restritas; falsa analogia: comparação inadequada; falsa causa: correlação sem causa.
- Afirmação do consequente e negação do antecedente são inválidas; modus ponens e tollens são válidos.
- "Válido, mas fraco" é contradição de termos: fraco/forte é só para indução.
- Ad hominem circunstancial: desqualifica pela situação pessoal.


---

# TRECHO: raciocinio-logico/a05/s09
##### raciocinio-logico/a05/s09
Este trecho conclui as questões da aula com o último item do FUNPRESP-Jud (negação do antecedente) e reapresenta, sem resolução, a lista das questões de estrutura básica e classificação dos argumentos, com o gabarito do bloco.

### Fim das questões do FUNPRESP-Jud

- "Se Antenor é analista de seguridade, então é servidor; logo, se Antenor não é analista de seguridade, então não é servidor": é a segunda forma da **negação do antecedente** (de p → q, concluir ~p → ~q): item **certo**. A forma de primeira ordem, com premissa ~p e conclusão ~q, também é a falácia.

### Gabarito do bloco "estrutura básica e classificação" (30 questões)

- Na ordem da lista: E, D, D, Errado, Errado, E, D, D, Errado, D, C, A, D, A, A, A, C, A, E, Certo, Errado, Certo, A, D, C, A, A, B, A, B.
- O bloco cobra, em essência: (a) indução × dedução × abdução em exemplos do dia a dia; (b) premissa levando à conclusão; (c) os esquemas de Peirce; (d) analogia como indução; (e) indução forte × fraca; (f) cadeia de condicionais com modus tollens.

### Como estudar este bloco

1. Classifique cada exemplo antes de ver a resposta: o raciocínio vai do geral ao particular (dedução), de casos à regra (indução) ou procura a melhor explicação (abdução)?
2. Procure a palavra-chave: "logo", "portanto" indica conclusão; "porque", "já que" indica premissa; "deve", "possivelmente", "talvez" indicam julgamento.
3. Quando a questão mistura lógica formal e probabilidade (urna, sorteio), separe o que é cálculo exato (dedução) do que é inferência estatística (indução).
4. Em itens do CEBRASPE, diferencie "válido" (só dedutivo) de "forte" (indutivo).

### Itens que mais se repetem na lista

- Reconhecimento do tipo de raciocínio em exemplos curtos (casos de cachorros bravos, rosas e violetas, atrito, gato preto).
- Identificação de premissa e conclusão a partir da ordem do texto e das palavras de probabilidade.
- Cadeias de condicionais resolvidas por modus tollens, como a do João que não tomou remédio.
- Julgamentos do CEBRASPE sobre raciocínio analítico, sempre pedindo distinguir dedução, indução e abdução.

### Lista de questões (reapresentação)

- A lista traz de novo as questões da FGV (TCE-PE), SEBRAE-GO, Consulplan (DPE-PR), CEBRASPE (TRF-6, CGE-RJ), FEPESE, SELECON, UFT, IBFC (vários), IDCAP, FGV (Câmara dos Deputados, TJDFT, PC-AM, TCE-AM), IMPARH, FUNPRESP-Jud, entre outras, e as de falácias de que trata o trecho seguinte.

### Para fixar
- A negação do antecedente tem duas formas: premissa ~p com conclusão ~q, ou conclusão ~p → ~q a partir de p → q.
- Faça a lista sem olhar a resolução e confira com o gabarito.
- Classifique pelo esquema: geral → particular, particular → geral ou melhor explicação.
- Separe "válido/inválido" (dedutivo) de "forte/fraco" (indutivo).
- Palavras de probabilidade sinalizam conclusão.


---

# TRECHO: raciocinio-logico/a05/s10
##### raciocinio-logico/a05/s10
Este trecho final reapresenta a lista de questões sobre argumentos falaciosos e apelativos e traz o respectivo gabarito. Não há matéria nova; serve de conferência da aula inteira.

### Gabarito do bloco "falácias" (19 questões)

- Na ordem da lista: Certo, Certo, Certo, Certo, Certo, Errado, Certo, Errado, A, Errado, B, C, C, C, D, C, D, Certo, Certo.
- Distribuição do que se cobra: apelos emocionais (piedade, povo, ignorância, consequências), falso dilema, falácias formais (negação do antecedente e afirmação do consequente), falsa analogia, falsa causa, apelo à autoridade, ad hominem circunstancial.

### Roteiro de revisão da aula

1. **Estrutura**: argumento = premissas + conclusão; indicadores de premissa (pois, porque) e de conclusão (logo, portanto); a conclusão pode estar em qualquer posição.
2. **Classificação**: dedução (válida/inválida, sem conhecimento novo); indução (forte/fraca, generaliza); abdução (melhor explicação); analogia como indução.
3. **Peirce**: dedução (regra + caso ⇒ resultado), indução (caso + resultado ⇒ regra), abdução (regra + resultado ⇒ caso).
4. **Falácias formais**: afirmação do consequente e negação do antecedente (inválidas).
5. **Falácias informais**: ad hominem (3 tipos), autoridade, ignorância, falso dilema, pergunta complexa, espantalho, petição de princípio, conclusão irrelevante, falso escocês; apelos (povo, piedade, força, consequências); acidente e inversão; divisão e composição; generalização apressada, falsa analogia, jogador, derrapagem; causais (falsa causa, causa comum, post hoc, inversão, causa complexa, insignificante); ambiguidade (equívoco, anfibologia, ênfase).

### Dicas para a prova

- Questões de falácia costumam trazer um **diálogo curto**: identifique o que o interlocutor faz (ataca a pessoa, apela à maioria, pede piedade, restringe as opções, confunde correlação com causa).
- Nas falácias formais, **monte a forma** (p → q etc.) e compare com modus ponens/tollens.
- Se aparecer "argumento válido, mas fraco" ou "dedução forte", desconfie: os adjetivos pertencem a classes diferentes de argumento.

### Para fixar
- O gabarito do bloco de falácias tem 19 itens, quase todos de reconhecimento de nome ou forma.
- Faça de novo a lista antes de ver o gabarito.
- Compare a forma do argumento com modus ponens e modus tollens.
- Monte uma tabela pessoal de falácias com um exemplo seu para cada uma.
- Revise as armadilhas: válido ≠ verdadeiro; fraco ≠ inválido.


---
