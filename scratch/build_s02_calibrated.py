# Script to generate calibrated a09-s02.md
import subprocess
import json

content = """---
id: "direito-penal-militar/a09/s02"
volume: "direito-penal-militar/m05"
capitulo: 2
titulo: "Lesão Corporal, Rixa e Periclitação da Vida"
fingerprint: {"startPage": 11, "endPage": 19, "startTopic": "\\u202dLESÃO CORPORAL E RIXA\\u202c"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-30"
edital: ["geral:9.4"]
fontes: ["Código Penal Militar (Decreto-Lei nº 1.001/1969, arts. 209 a 213) — https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001.htm — consultado em 2026-10-31", "Lei nº 14.688/2023 — https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14688.htm — consultado em 2026-10-31"]
notas: "Estudo das lesões corporais dolosas (leve, grave, gravíssima, culposa pelo resultado e seguida de morte nos arts. 209 e 209, §§ 1º a 3º-A), lesão culposa (art. 210), rixa (art. 211) e crimes de periclitação da vida e saúde (abandono de pessoa no art. 212 e maus-tratos no art. 213 do CPM)."
---

A proteção da pessoa no Código Penal Militar vai além da preservação da vida. O legislador penal especial resguarda com rigor a integridade corporal e a saúde física e mental dos indivíduos, sancionando condutas agressivas e comportamentos omissivos que submetem terceiros a perigo concreto. No contexto das corporações armadas, em que vigoram hierarquia, disciplina estrita e o porte funcional de armamento, tais limites delimitam com clareza o treinamento legítimo e o abuso punível.

> [!objetivos]
> - Diferenciar as modalidades leve, grave, gravíssima e seguida de morte da lesão corporal dolosa no CPM.
> - Compreender a regra da lesão qualificada pelo resultado culposo e o tratamento da lesão levíssima.
> - Dominar a lesão culposa, suas majorantes e a concessão do perdão judicial após a Lei nº 14.688/2023.
> - Analisar a estrutura típica da rixa militar e os reflexos penais da morte ou lesão grave de participante.
> - Identificar os crimes de periclitação da vida e da saúde: abandono de pessoa e maus-tratos funcionais.

## Fecho do genocídio e introdução à integridade corporal

Antes de ingressar no exame das lesões corporais, cabe rememorar as modalidades executórias complementares do genocídio previstas no art. 208, parágrafo único, do Código Penal Militar. O tipo penal sanciona atos direcionados a inviabilizar a sobrevivência física ou identitária do grupo:

- **Dispersão forçada (inciso III):** deslocamento involuntário que rompe os laços de convivência da comunidade tutelada.
- **Medidas impeditivas de nascimentos (inciso IV):** métodos compulsórios de esterilização ou separação de casais com o propósito de extermínio biológico futuro.
- **Transferência forçada de crianças (inciso V):** remoção de infantes para grupo distinto, erradicando a cultura original.

Superada a tutela coletiva dos grupos humanos, o Capítulo III do Código dedica-se à integridade física individual.

```mermaid Crimes contra a integridade física e a saúde no CPM
flowchart TD
    A["Crimes contra a Integridade Física e Saúde"] --> B["Lesão Corporal Dolosa (art. 209)"]
    A --> C["Lesão Corporal Culposa (art. 210)"]
    A --> D["Participação em Rixa (art. 211)"]
    A --> E["Periclitação da Vida e Saúde (arts. 212 e 213)"]
    B --> B1["Leve (caput) | Levíssima (§ 6º)"]
    B --> B2["Grave (§ 1º) | Gravíssima (§ 2º)"]
    B --> B3["Resultado Culposo (§ 3º) | Seguida de Morte (§ 3º-A)"]
    C --> C1["Caput | Majorantes (§§ 1º e 2º) | Perdão Judicial (§ 3º)"]
    D --> D1["Caput (tumulto) | Parágrafo único (resultado grave/morte)"]
    E --> E1["Abandono de Pessoa (art. 212)"]
    E --> E2["Maus-Tratos na Instrução ou Serviço (art. 213)"]
```

## Lesão corporal dolosa leve (art. 209, caput)

O crime consiste em causar ofensa anatômica ou perturbação à integridade física ou à saúde de outra pessoa.

> [!lei] Art. 209, caput, do Código Penal Militar
> Ofender a integridade corporal ou a saúde de outrem:
> Pena - detenção, de três meses a um ano.

O objeto jurídico é a integridade física e o equilíbrio psíquico-fisiológico do ser humano. A conduta admite ação física (golpes, socos ou projéteis) e omissão imprópria (descumprimento do dever de proteção previsto no art. 29 do CPM). Pelo princípio da alteridade, ninguém responde por ofender o próprio corpo no art. 209; a autolesão para fugir de obrigações de serviço é crime militar autônomo (art. 184).

A lesão leve é subsidiária: abrange equimoses, hematomas superficiais e escoriações que não atinjam os resultados agravadores dos parágrafos seguintes. O diagnóstico depende de exame pericial de corpo de delito.

### A desclassificação para infração disciplinar (§ 6º)

> [!lei] Art. 209, § 6º, do Código Penal Militar
> No caso de lesões levíssimas, o juiz pode considerar a infração como disciplinar.

Essa conversão constitui faculdade judicial privativa. O perito apenas relata a insignificância dos vestígios corporais constatados. Cabe ao juiz togado ou ao Conselho de Justiça avaliar se o fato merece tutela criminal ou se a resposta regulamentar interna satisfaz a necessidade de justiça.

| Parâmetro | Lesão Leve (Art. 209, Caput) | Lesão Levíssima (Art. 209, § 6º) |
|---|---|---|
| **Efeito Físico** | Escoriações e feridas superficiais | Vestígios ínfimos sem maior dano funcional |
| **Resposta Estatal** | Sanção penal: detenção de 3 meses a 1 ano | Faculdade judicial de converter em transgressão disciplinar |
| **Avaliação** | Laudo pericial descreve a ofensa anatômica | Juízo de valor do magistrado sobre o contexto do fato |

> [!bizu]
> Na lesão corporal grave (art. 209, § 1º), a lei prescreve "reclusão, até cinco anos", sem fixar o piso mínimo. Aplica-se a regra geral do art. 58 do CPM, que define o mínimo de um ano para as penas de reclusão. Portanto, a baliza da lesão grave é de um a cinco anos.

## Lesões corporais graves e gravíssimas (art. 209, §§ 1º e 2º)

A Lei nº 14.688/2023 aperfeiçoou as figuras qualificadas da lesão dolosa militar, alinhando as hipóteses típicas ao sistema penal comum.

### Lesão corporal grave (art. 209, § 1º)

> [!lei] Art. 209, § 1º, do Código Penal Militar (redação da Lei nº 14.688/2023)
> Se se produz, dolosamente, aceleração de parto, perigo de vida, debilidade permanente de membro, sentido ou função, ou incapacidade para as ocupações habituais, por mais de 30 (trinta) dias:
> Pena - reclusão, até cinco anos.

As quatro hipóteses de lesão grave exigem demonstração pericial fundamentada:
1. **Aceleração de parto:** nascimento antecipado de feto viável em virtude do trauma físico sofrido pela mulher grávida.
2. **Perigo de vida:** probabilidade técnica, concreta e iminente de óbito decorrente das lesões sofridas, atestada conclusivamente por médico legista.
3. **Debilidade permanente:** diminuição parcial, duradoura e sensível da higidez de membro, sentido ou função corporal (órgãos pares conservam parte de sua função).
4. **Incapacidade para ocupações habituais por mais de 30 dias:** impedimento temporário para o exercício das atividades cotidianas, comprovado por perícia complementar no trigésimo primeiro dia.

### Lesão corporal gravíssima (art. 209, § 2º)

> [!lei] Art. 209, § 2º, do Código Penal Militar (redação da Lei nº 14.688/2023)
> Se se produz, dolosamente, enfermidade incurável, perda ou inutilização de membro, sentido ou função, incapacidade permanente para o trabalho, deformidade duradoura ou aborto:
> Pena - reclusão, de dois a oito anos.

As consequências gravíssimas representam danos anatômicos permanentes ou de altíssima severidade:
1. **Enfermidade incurável:** estado mórbido para o qual a ciência contemporânea não dispõe de cura definitiva no momento da agressão.
2. **Perda ou inutilização:** destruição completa, amputação ou ablação funcional de membro, sentido ou órgão (exemplo: destruição de ambos os olhos ou perda total da função renal).
3. **Incapacidade permanente para o trabalho:** inviabilidade laboral definitiva e ampla para ocupações produtivas em geral.
4. **Deformidade duradoura:** prejuízo estético marcante, visível e irreparável pelos meios médicos espontâneos, apto a provocar desconforto social.
5. **Aborto provocado por agressão:** destruição intrauterina do produto da concepção provocada pela agressão contra a gestante, sem dolo específico de provocar o aborto.

| Hipótese | Enquadramento Legal | Sanção Privativa de Liberdade |
|---|---|---|
| **Aceleração de parto** | Art. 209, § 1º (Grave) | Reclusão, 1 a 5 anos (mínimo pelo art. 58) |
| **Incapacidade habitual > 30 dias** | Art. 209, § 1º (Grave) | Reclusão, 1 a 5 anos |
| **Debilidade de membro, sentido ou função** | Art. 209, § 1º (Grave) | Reclusão, 1 a 5 anos |
| **Perigo concreto de vida** | Art. 209, § 1º (Grave) | Reclusão, 1 a 5 anos |
| **Perda ou ablação funcional completa** | Art. 209, § 2º (Gravíssima) | Reclusão, 2 a 8 anos |
| **Deformidade visível e duradoura** | Art. 209, § 2º (Gravíssima) | Reclusão, 2 a 8 anos |
| **Enfermidade sem cura conhecida** | Art. 209, § 2º (Gravíssima) | Reclusão, 2 a 8 anos |
| **Incapacidade definitiva para o trabalho** | Art. 209, § 2º (Gravíssima) | Reclusão, 2 a 8 anos |
| **Aborto consequente da agressão** | Art. 209, § 2º (Gravíssima) | Reclusão, 2 a 8 anos |

## Figuras preterdolosas na lesão corporal (art. 209, §§ 3º e 3º-A)

O Código Penal Militar possui fórmula singular para punir a lesão corporal qualificada pelo evento quando o agressor atua com dolo no ato antecedente e culpa estrita no resultado mais severo.

### Lesão qualificada pelo resultado culposo (art. 209, § 3º)

> [!lei] Art. 209, § 3º, do Código Penal Militar (redação da Lei nº 14.688/2023)
> Se os resultados previstos nos §§ 1º e 2º deste artigo forem causados culposamente:
> Pena – detenção, de 1 (um) a 4 (quatro) anos.

Essa norma disciplina situação clássica de crime preterdoloso: o autor deseja apenas lesionar levemente a vítima, mas, por inobservância do cuidado objetivo, produz debilidade permanente, enfermidade incurável ou incapacidade duradoura. O CPM comina detenção de um a quatro anos, resposta penal substancialmente inferior à das formas dolosas dos §§ 1º e 2º.

> [!pegadinha]
> Fique atento: no CPM, se as consequências do § 1º ou do § 2º decorrerem de culpa, o agente não é punido com reclusão. Ele incide na figura típica autônoma do art. 209, § 3º, cuja pena é de detenção de um a quatro anos. Não confunda essa lesão preterdolosa com a lesão puramente culposa do art. 210, na qual a própria conduta inicial é desprovida de dolo.

### Lesão corporal seguida de morte (art. 209, § 3º-A)

> [!lei] Art. 209, § 3º-A, do Código Penal Militar (incluído pela Lei nº 14.688/2023)
> Se da lesão resultar morte e as circunstâncias evidenciarem que o agente não quis o resultado nem assumiu o risco de produzi-lo:
> Pena – reclusão, de 4 (quatro) a 12 (doze) anos.

Essa figura jurídica configura o homicídio preterdoloso. Exige dolo antecedente direcionado exclusivamente a ofender a integridade física da vítima, aliado à culpa no resultado letal. Caso a instrução criminal evidencie que o agressor aceitou o risco de produzir a morte, o fato transmuda-se em homicídio doloso (art. 205), absorvendo a agressão corporal física.

| Combinação Subjetiva | Dispositivo Típico | Sanção Cominada |
|---|---|---|
| **Dolo na agressão e dolo no resultado grave** | Art. 209, § 1º | Reclusão, 1 a 5 anos |
| **Dolo na agressão e dolo no resultado gravíssimo** | Art. 209, § 2º | Reclusão, 2 a 8 anos |
| **Dolo na agressão e culpa no resultado agravador** | Art. 209, § 3º | Detenção, 1 a 4 anos |
| **Dolo na agressão e culpa estrita na morte** | Art. 209, § 3º-A | Reclusão, 4 a 12 anos |
| **Dolo na morte decorrente da agressão física** | Art. 205 (Homicídio) | Reclusão, 6 a 20 anos (ou 12 a 30) |

## Minoração de pena e lesões recíprocas (art. 209, §§ 4º e 5º)

O estatuto repressivo militar contempla hipóteses de abrandamento da reprimenda estatal motivadas por razões humanitárias ou probatórias.

### Lesão corporal privilegiada (art. 209, § 4º)

> [!lei] Art. 209, § 4º, do Código Penal Militar
> Se o agente comete o crime impelido por motivo de relevante valor moral ou social ou sob o domínio de violenta emoção, logo em seguida a injusta provocação da vítima, o juiz pode reduzir a pena, de um sexto a um terço.

A mitigação exige:
- Relevante valor moral ou relevante valor social motivador da agressão;
- Ou domínio de forte abalo emocional, reação imediata ao ato injusto e nexo causal direto com a conduta provocadora da vítima.

### Lesões leves recíprocas (art. 209, § 5º)

> [!lei] Art. 209, § 5º, do Código Penal Militar
> No caso de lesões leves, se estas são recíprocas, não se sabendo qual dos contendores atacou primeiro, ou quando ocorre qualquer das hipóteses do parágrafo anterior, o juiz pode diminuir a pena de um a dois terços.

A causa de diminuição de um a dois terços restringe-se às seguintes condições:
1. Deve cuidar-se estritamente de **lesões leves** mútuas. Se qualquer envolvido suportar ferimento de natureza grave, afasta-se o benefício;
2. Dúvida insuperável quanto a qual dos contendores desfechou o primeiro golpe agressivo. Se houver prova inequívoca sobre quem deu início ao entrevero, o agressor inicial responde pelo delito integral e a reação moderada do agredido caracteriza legítima defesa.

## Lesão corporal culposa militar (art. 210)

A lesão corporal culposa prescinde da intenção delitiva de machucar, decorrendo da quebra inescusável do dever geral de prudência.

> [!lei] Art. 210 do Código Penal Militar (com redação da Lei nº 14.688/2023)
> Se a lesão é culposa:
> Pena - detenção, de dois meses a um ano.
> § 1º A pena é aumentada de 1/3 (um terço) se o crime resulta da inobservância de regra técnica de profissão, arte ou ofício, ou se o agente deixa de prestar imediato socorro à vítima, não procura diminuir as consequências do seu ato ou foge para evitar prisão em flagrante.
> § 2º Se, em consequência de uma só ação ou omissão culposa, ocorrem lesões em várias pessoas, a pena é aumentada de um sexto até metade.
> § 3º O juiz poderá deixar de aplicar a pena se as consequências da infração atingirem o próprio agente de forma tão grave que a sanção penal se torne desnecessária.

Diferente do que se verifica no crime doloso, o Código Penal Militar não gradua a lesão culposa pela severidade anatômica do dano: o ferimento de ordem leve ou de ordem gravíssima gera a incidência inicial do preceito do caput.

### Causas de aumento (§§ 1º e 2º) e perdão judicial (§ 3º)

A majoração de um terço do § 1º é aplicável quando o militar atua com inobservância flagrante de regras operacionais de sua especialidade bélica, omite socorro urgente à vítima quando possível fazê-lo com segurança, deixa de mitigar os danos ou empreende fuga para burlar a prisão em flagrante. O § 2º pune o concurso formal culposo decorrente de ato único gerador de múltiplos lesionados com aumento de um sexto até a metade.

O § 3º incorporou formalmente o perdão judicial à legislação castrense, extinguindo a punibilidade nos casos em que as sequelas morais ou físicas do acidente atingem o próprio militar de maneira irreparável (como o disparo culposo acidental que atinge membro de sua família).

| Dispositivo Legal | Matéria Regulada no Art. 210 | Consequência Penal |
|---|---|---|
| **Art. 210, caput** | Lesão corporal decorrente de culpa estrita | Detenção, 2 meses a 1 ano |
| **Art. 210, § 1º** | Falta de socorro, inobservância técnica ou fuga | Aumento compulsório de 1/3 |
| **Art. 210, § 2º** | Concurso formal culposo de lesionados | Aumento de 1/6 até a metade |
| **Art. 210, § 3º** | Sequela moral ou física extrema suportada pelo autor | Perdão judicial (extingue a punibilidade) |

## Participação em rixa (art. 211)

A rixa caracteriza-se pelo confronto desordenado e violento entre vários indivíduos com posições antagônicas simultâneas.

> [!lei] Art. 211 do Código Penal Militar
> Participar de rixa, salvo para separar os contendores:
> Pena - detenção, até dois meses.
> Parágrafo único. Se ocorre morte ou lesão grave, aplica-se, pelo fato de participação na rixa, a pena de detenção, de seis meses a dois anos.

Elementos dogmáticos da rixa:
- **Pluralidade mínima de três contendores:** confronto violento desorganizado que requer concurso necessário de três pessoas no mínimo. Entreveros entre apenas dois agentes configuram lesões recíprocas ou vias de fato.
- **Agressões mútuas e desordenadas:** todos investem contra todos, inexistindo delimitação estável de frentes em litígio.
- **Intervenção apaziguadora lícita:** quem adentra no tumulto estritamente para apartar a luta física não pratica conduta punível.
- **Resultado qualificador solidário:** a ocorrência de óbito ou lesão de índole grave qualifica o crime para todos os envolvidos na rixa, haja vista o perigo geral alimentado pelo confronto coletivo descontrolado. Contudo, o participante individualizado que desferiu o golpe letal responderá pelo homicídio ou pela lesão grave em concurso com a rixa.

> [!esquema]
> - Rixa militar básica: confronto entre 3 ou mais contendores sem delimitação -> Pena de detenção de até 2 meses (mínimo de trinta dias pelo art. 58 do CPM).
> - Intervenção apartadora: ingressar unicamente para conter o conflito -> Fato atípico perante o art. 211.
> - Rixa qualificada solidária: advento de lesão grave ou óbito -> Detenção de seis meses a dois anos para todos os litigantes.
> - Autor do resultado lesivo apurado: responde pelo crime autônomo grave (homicídio ou lesão) cumulado com a participação em rixa.

## Abandono de pessoa no Código Penal Militar (art. 212)

O Capítulo IV do Título IV contempla os crimes de periclitação da vida e da saúde individual, iniciando pelo desamparo de vulneráveis sob tutela da autoridade militar.

> [!lei] Art. 212 do Código Penal Militar (com redação da Lei nº 14.688/2023)
> Abandonar o militar pessoa que está sob seu cuidado, guarda, vigilância ou autoridade e, por qualquer motivo, incapaz de defender-se dos riscos resultantes do abandono:
> Pena - detenção, de seis meses a três anos.
> § 1º Se do abandono resulta lesão grave:
> Pena - reclusão, até cinco anos.
> § 2º Se resulta morte:
> Pena - reclusão, de quatro a doze anos.
> § 3º As penas cominadas neste artigo são aumentadas de 1/3 (um terço):
> I – se o abandono ocorre em lugar ermo;
> II – se o agente é ascendente ou descendente, cônjuge, irmão, tutor ou curador da vítima;
> III – se a vítima é maior de 60 (sessenta) anos, menor de 14 (quatorze) anos ou pessoa com deficiência.

Cuida-se de crime próprio que exige condição funcional do autor ("o militar") detentor de dever jurídico de custódia, proteção ou vigilância sobre o ofendido. Trata-se de infração de perigo concreto. As formas dos §§ 1º e 2º são preterdolosas, exigindo dolo no abandono e culpa na lesão grave ou na morte gerada pelo isolamento desamparado. O § 3º impõe majorante de um terço pelo desamparo em áreas despovoadas ou em virtude de especial fragilidade etária ou biológica do tutelado.

## Maus-tratos em função ou ambiente militar (art. 213)

O crime de maus-tratos destina-se a reprimir abusos intoleráveis praticados a pretexto de instruir, custodiar, tratar ou educar subordinados ou administrados.

> [!lei] Art. 213 do Código Penal Militar (com redação da Lei nº 14.688/2023)
> Expor a perigo a vida ou saúde, em lugar sujeito à administração militar ou no exercício de função militar, de pessoa sob sua autoridade, guarda ou vigilância, para o fim de educação, instrução, tratamento ou custódia, quer privando-a de alimentação ou cuidados indispensáveis, quer sujeitando-a a trabalhos excessivos ou inadequados, quer abusando de meios de correção ou disciplina:
> Pena - detenção, de dois meses a um ano.
> § 1º Se do fato resulta lesão grave:
> Pena - reclusão, até quatro anos.
> § 2º Se resulta morte:
> Pena - reclusão, de dois a dez anos.
> § 3º A pena é aumentada de 1/3 (um terço) se o crime é praticado contra pessoa menor de 14 (quatorze) anos, maior de 60 (sessenta) anos ou com deficiência.

O núcleo incriminador é expor a perigo a vida ou a higidez da pessoa submetida à sua autoridade funcional. A norma estabelece três modos executórios taxativos:
1. Privação voluntária de alimentação substancial ou cuidados de saúde elementares;
2. Imposição de rotinas físicas de trabalho incompatíveis com os parâmetros normais de resistência orgânica;
3. Excesso arbitrário na imposição de castigos, correções de disciplina ou tarefas punitivas.

> [!exemplo]
> Em exercício de campanha militar, o instrutor militar responsável pela equipe submete pelotão de alunos a marchar sob sol inclemente por dez horas seguidas sem fornecer água potável ou permitir descanso mínimo, buscando "fortalecer o caráter" da tropa. Se um dos alunos sofre choque térmico seguido de colapso circulatório fatal sem que houvesse intenção assassina direta, o instrutor incide no crime de maus-tratos qualificado pela morte (art. 213, § 2º), punido com reclusão de dois a dez anos, e não em homicídio doloso.

> [!atencao]
> A prática de castigos corporais severos ou o esgotamento biológico desmedido durante instruções militares não se confundem com exercício regular de disciplina militar. Sob a ordem constitucional vigente, tais excessos ostentam tipicidade penal inequívoca pelo art. 213 do CPM, não se admitindo a desculpa de costume de caserna para convalidar práticas degradantes.

| Requisito Tipológico | Abandono de Pessoa (Art. 212) | Maus-Tratos (Art. 213) |
|---|---|---|
| **Conduta Subjacente** | Desamparo e isolamento da pessoa indefesa | Abuso corretivo, excesso de esforço ou privação |
| **Contexto Funcional** | Vínculo de custódia, cuidado, autoridade ou vigilância | Local militar ou desempenho estrito de função armada |
| **Finalidade Subjetiva** | Não exige fim específico de ensino ou disciplina | Finalidade de instrução, educação, custódia ou tratamento |
| **Pena do Preceito Básico** | Detenção, 6 meses a 3 anos | Detenção, 2 meses a 1 ano |
| **Qualificadora por Morte** | Reclusão, 4 a 12 anos (§ 2º) | Reclusão, 2 a 10 anos (§ 2º) |
| **Aumento de Pena (+1/3)** | Local ermo, parentesco, idade (<14 ou >60) ou deficiência | Vítima menor de 14 anos, maior de 60 ou com deficiência |

## Mapa do capítulo

A tabela a seguir sistematiza as figuras penais examinadas e as sanções cominadas pelo Código Penal Militar:

| Delito Militar | Fundamento Legal | Sanção Privativa de Liberdade | Elemento Dogmático Marcante |
|---|---|---|---|
| **Lesão Corporal Leve** | Art. 209, caput | Detenção, 3 meses a 1 ano | Ofensa residual à higidez corporal ou psíquica |
| **Lesão Levíssima** | Art. 209, § 6º | Faculdade de sanção disciplinar | Conversão judicial conforme gravidade ínfima do ato |
| **Lesão Corporal Grave** | Art. 209, § 1º | Reclusão, até 5 anos (mínimo de 1 ano) | Perigo de vida, debilidade ou incapacidade > 30 dias |
| **Lesão Gravíssima** | Art. 209, § 2º | Reclusão, 2 a 8 anos | Incurabilidade, perda funcional, deformidade ou aborto |
| **Preterdolosa Agravada** | Art. 209, § 3º | Detenção, 1 a 4 anos | Dolo no ato lesivo e culpa no resultado qualificador |
| **Preterdolosa Letal** | Art. 209, § 3º-A | Reclusão, 4 a 12 anos | Homicídio preterdoloso tipificado pela Lei 14.688/2023 |
| **Lesão Recíproca Leve** | Art. 209, § 5º | Redução de 1/3 a 2/3 | Dúvida insuperável sobre início da contenda física |
| **Lesão Culposa** | Art. 210, caput | Detenção, 2 meses a 1 ano | Ausência de graduação típica segundo a severidade |
| **Perdão Judicial Culposo** | Art. 210, § 3º | Extinção da punibilidade | Gravidade moral extrema das sequelas sobre o autor |
| **Participação em Rixa** | Art. 211, caput | Detenção, até 2 meses | Contenda física de no mínimo três participantes |
| **Rixa Qualificada** | Art. 211, parágrafo único | Detenção, 6 meses a 2 anos | Advento solidário de lesão corporal grave ou morte |
| **Abandono de Pessoa** | Art. 212, caput | Detenção, 6 meses a 3 anos | Desamparo voluntário de vulnerável sob dever funcional |
| **Maus-Tratos Militares** | Art. 213, caput | Detenção, 2 meses a 1 ano | Abuso em contexto de ensino, custódia ou treinamento |

### Para fixar

- A lesão leve comina detenção de três meses a um ano; a lesão levíssima pode ser desclassificada para infração disciplinar pelo magistrado militar.
- A lesão grave (art. 209, § 1º) tem pena de reclusão de um a cinco anos (mínimo balizado pelo art. 58 do CPM); a lesão gravíssima (art. 209, § 2º) comina reclusão de dois a oito anos.
- A produção culposa de resultado grave ou gravíssimo por agente que agiu com dolo de lesão corporal acarreta pena autônoma de detenção de um a quatro anos (art. 209, § 3º).
- A lesão corporal seguida de morte (art. 209, § 3º-A) comina reclusão de quatro a doze anos e exige ausência de intenção ou assunção do risco de matar.
- Na lesão culposa (art. 210), não há graduação legal da lesão corporal; o tipo comporta aumento de um terço por inobservância técnica ou fuga e faculta perdão judicial no § 3º.
- A rixa exige ao menos três pessoas em confronto generalizado mútuo; a ocorrência de morte ou lesão grave exaspera a sanção para todos os rixosos pelo resultado comum.
- O abandono de pessoa (art. 212) reprime o desamparo de vulnerável sob custódia, e os maus-tratos (art. 213) sancionam o abuso dos meios disciplinares ou sobrecarga física na instrução.
"""

with open("content/material/direito-penal-militar/m05/a09-s02.md", "w", encoding="utf-8") as f:
    f.write(content)

print("Saved a09-s02.md successfully")
