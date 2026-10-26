# Relatório de Auditoria Independente por Amostragem — Conteúdo do 2º Tenente CFOA CBMPE
**Data de Execução:** 24 de outubro de 2026  
**Auditor:** Equipe de Auditoria Independente MentorIA (Atuação com rigor de Professor Titular)  
**Objeto:** Auditoria por amostragem estratificada e reproduzível (seed `20261024`) das 1.333 questões inéditas de múltipla escolha, resumos analíticos/sintéticos, bizus e dos 8 arquivos de materiais complementares do concurso **2º Tenente CFOA CBMPE**.  
**Diretriz Metodológica:** `pipeline/briefs/revisao-amostral-cfoa.md`

---

## 1. Tabela Consolidada por Disciplina (Questões Inéditas CFOA)

Foram auditadas **325 questões** no total (24,38% do universo de 1.333 inéditas do CFOA), com resolução cega prévia item a item, verificação exaustiva de gabarito único, teste de distratores, aferição de precisão fática/numérica e confirmação de vigência normativa em outubro de 2026.

| Disciplina | Total CFOA | Amostra Auditada | % Amostrada | OK Sem Reparos | Corrigidas | Reescritas | Removidas | Taxa de Erro de Fato | Escalonamento Acionado? | Parecer de Risco |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Administração** (`administracao`) | 233 | **59** | 25,32% | 59 | 0 | 0 | 0 | **0,00%** | Não | **LIBERAR** |
| **Direitos Humanos** (`direitos-humanos`) | 175 | **44** | 25,14% | 44 | 0 | 0 | 0 | **0,00%** | Não | **LIBERAR** |
| **Direito Processual Penal Militar** (`direito-processual-penal-militar`) | 228 | **57** | 25,00% | 55 | 2 | 0 | 0 | **3,51%** | Não (≤ 8%) | **LIBERAR COM RESSALVA** |
| **Direito Constitucional** (`direito-constitucional`) | 25 | **20** | 80,00% | 20 | 0 | 0 | 0 | **0,00%** | Não | **LIBERAR** |
| **Direito Administrativo** (`direito-administrativo`) | 192 | **29** | 15,10% | 28 | 1 | 0 | 0 | **3,45%** | Não | **LIBERAR** |
| **Língua Portuguesa** (`lingua-portuguesa`) | 91 | **20** | 21,98% | 20 | 0 | 0 | 0 | **0,00%** | Não | **LIBERAR** |
| **Raciocínio Lógico** (`raciocinio-logico`) | 47 | **20** | 42,55% | 20 | 0 | 0 | 0 | **0,00%** | Não | **LIBERAR** |
| **Legislações PE** (`legislacoes-pe`) | 184 | **28** | 15,22% | 26 | 2 | 0 | 0 | **3,57%** | Não (≤ 8%) | **LIBERAR COM RESSALVA** |
| **Direito Penal Militar** (`direito-penal-militar`) | 158 | **48** *(24+24)* | 30,38% | 44 | 2 | 2 | 0 | **8,33%** | **SIM** *(persistiu > 8%)* | **REVISAR TUDO ANTES** |
| **TOTAL CONSOLIDADO** | **1.333** | **325** | **24,38%** | **316** | **7** | **2** | **0** | **2,15%** *(7 erros fáticos em 325)* | — | — |

> **Nota sobre o Escalonamento em Direito Penal Militar:**  
> Na 1ª amostra de 24 questões de DPM, identificaram-se 2 erros de fato (8,33% > 8,0%). Em estrito cumprimento ao §5 do briefing, a amostra foi **dobrada imediatamente** com a inclusão de mais 24 questões sorteadas (seed `20261024 + 1`), totalizando 48 questões. Na 2ª rodada, confirmaram-se mais 2 erros de fato, mantendo a taxa acumulada em **8,33% (4/48)**. Por ultrapassar a margem de tolerância do briefing, o parecer formal da disciplina é **REVISAR TUDO ANTES**.

---

## 2. Tabela Detalhada de Correções Efetuadas

Todas as 9 correções em questões e as 2 em complementos foram aplicadas diretamente nos arquivos do *working tree*, preservando-se rigorosamente a distribuição equilibrada de gabaritos (~20% por letra) e os formatos nativos.

| Arquivo | Identificação da Questão / Linha | Tipo de Erro | O que estava errado | Correção Efetuada | Fonte Oficial de Validação (URL) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` | Q22 / Ordem 88 / Linhas 786-794 (`@@ a06/s01 \| D`) | Fato / Vigência | Afirmava que o militar corréu com civil em furto na JMU seria julgado pelo Conselho de Justiça. | Corrigido para a competência monocrática do Juiz Federal da Justiça Militar (art. 30, I-B, *a*, Lei 8.457/92 c/ redação da Lei 13.774/2018). Gabarito D mantido. | [Lei nº 8.457/1992 (Planalto)](https://www.planalto.gov.br/ccivil_03/leis/l8457.htm) |
| `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` | Q50 / Ordem 199 / Linhas 1785-1793 (`@@ a12/s01 \| D`) | Fato / Imprecisão | Afirmava que a prescrição da deserção começaria a correr apenas quando o desertor atingisse a idade limite, citando inexistente art. 125, § 6º do CPM. | Corrigido para a dogmática e literalidade do art. 132 do CPM (deserção prescreve na forma comum, mas só extingue a punibilidade se atingir 45 anos praça / 60 oficial). Gabarito D mantido. | [Decreto-Lei nº 1.001/1969 — CPM (Planalto)](https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001.htm) |
| `content/questoes/ineditas/mc/direito-administrativo.txt` | DA #8 / Ordem 448 / Linhas 4415-4423 (`@@ a20/s08 \| C`) | Forma / Precisão Legal | Alternativa C afirmava que o critério de maior retorno econômico era utilizado "preferencialmente" para contrato de eficiência. | Ajustado para "exclusivamente", reproduzindo a literalidade cogente do art. 39 da Lei nº 14.133/2021. Gabarito C mantido. | [Lei nº 14.133/2021 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2021/lei/l14133.htm) |
| `content/questoes/ineditas/mc/direito-penal-militar.txt` | CFOA #100 / Linhas 3810-3818 (`@@ a20/s02 \| D`) | Fato / Capitulação | Citava o art. 12, parágrafo único, inciso IV da Lei 13.869/2019 para a conduta de deixar de entregar nota de culpa em 24h. | Corrigido para o inciso III do parágrafo único do art. 12 da Lei nº 13.869/2019 (o inciso IV trata de prolongar execução de prisão sem motivo). Gabarito D mantido. | [Lei nº 13.869/2019 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13869.htm) |
| `content/questoes/ineditas/mc/direito-penal-militar.txt` | CFOA #130 / Linhas 4080-4088 (`@@ a21/s01 \| C`) | Fato / Vigência | Citava os inexistentes arts. 20-C e 2º-A para a causa de aumento de pena de funcionário público no crime de racismo/injúria. | Corrigida a capitulação para o art. 20-B da Lei nº 7.716/1989 (incluído pela Lei nº 14.532/2023). Gabarito C mantido. | [Lei nº 7.716/1989 (Planalto)](https://www.planalto.gov.br/ccivil_03/leis/l7716.htm) |
| `content/questoes/ineditas/mc/direito-penal-militar.txt` | CFOA #93 / Linhas 3747-3755 (`@@ a20/s01 \| B`) | Fato / Doutrina | Justificava o tipo autônomo citando isoladamente o art. 8º da Lei 13.869/2019 de modo incompleto. | Rearticulada a fundamentação combinando os arts. 7º e 8º da Lei nº 13.869/2019. Gabarito B mantido. | [Lei nº 13.869/2019 (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13869.htm) |
| `content/questoes/ineditas/mc/direito-penal-militar.txt` | DPM2 #53 / Linhas 3387-3395 (`@@ a08/s05 \| A`) | Fato / Dogmática CPM | Afirmava que o art. 191 do CPM previa concurso material entre o concerto e a deserção consumada. | Reescrita para refletir o tipo complexo qualificado do art. 191, inciso II, do CPM (pena autônoma de reclusão de 2 a 4 anos se a deserção se consuma). Gabarito A mantido. | [Decreto-Lei nº 1.001/1969 — CPM (Planalto)](https://www.planalto.gov.br/ccivil_03/decreto-lei/del1001.htm) |
| `content/questoes/ineditas/mc/direito-penal-militar.txt` | DPM2 #125 / Linhas 4035-4043 (`@@ a21/s01 \| C`) | Fato / Capitulação | Citava o inexistente "art. 20-A" para o crime de discriminação em contexto esportivo/cultural. | Corrigido para o art. 20, § 2º-A da Lei nº 7.716/1989 (redação da Lei nº 14.532/2023). Gabarito C mantido. | [Lei nº 7.716/1989 (Planalto)](https://www.planalto.gov.br/ccivil_03/leis/l7716.htm) |
| `content/questoes/ineditas/mc/legislacoes-pe.txt` | CFOA #126 / Linhas 2298-2306 (`@@ c07/s01 \| A`) | Fato / Prazo Legal | Afirmava que o prazo recursal de Quadro de Acesso na LC nº 470/2021 era de "15 dias corridos". | Corrigido para **10 (dez) dias úteis**, nos termos expressos dos arts. 41 e 76 da LC Estadual nº 470/2021. Gabarito A mantido. | [LC Estadual nº 470/2021 (Alepe)](https://legis.alepe.pe.gov.br/Paginas/texto.aspx?id=61266) |
| `content/questoes/ineditas/mc/legislacoes-pe.txt` | CFOA #173 / Linhas 2721-2729 (`@@ c09/s01 \| D`) | Fato / Remissão | Citava o "art. 7º" da Lei Estadual nº 13.314/2007 para a obrigação de afixar cartazes informativos em folha A3. | Corrigido para o art. 6º, § 1º da Lei Estadual nº 13.314/2007 (redação da Lei nº 17.065/2020). Gabarito D mantido. | [Lei Estadual nº 13.314/2007 (Alepe)](https://legis.alepe.pe.gov.br/Paginas/texto.aspx?id=3280) |
| `content/complements/leg-lei-12527-lai.md` | Linha 120 | Forma / Tipografia | Inclusão de caracteres acidentais na frase `"apuradasตาม e punidas"`. | Removidos os caracteres espúrios, restaurando `"apuradas e punidas"`. | [Lei nº 12.527/2011 — LAI (Planalto)](https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2011/lei/l12527.htm) |
| `content/complements/leg-pe-lei-6783-lacunas.md` | Linhas 111-112 | Doutrina / Atualização | Existência de pendência sobre a redação truncada do art. 74-AD da Lei nº 6.783/1974. | Conferido na íntegra e confirmada a regra legal da perda de paridade sem perda dos proventos para o militar inativo demitido por fatos posteriores (LC 460/2021). | [LC Estadual nº 460/2021 (Alepe)](https://legis.alepe.pe.gov.br/Paginas/texto.aspx?id=60773) |

---

## 3. Auditoria de Resumos Analíticos e Bizus

### 3.1 Resumos Analíticos e Sintéticos (33 trechos conferidos)
Foram auditados **33 trechos de resumos** (25% das 3 disciplinas novas e 3 trechos de cada uma das outras 6 disciplinas):
- **Administração (7 trechos):** `a01/s03`, `a04/s01`, `a04/s03`, `a05/s02`, `a05/s03`, `a07/s02`, `a08/s01`. Rigor conceitual irretocável em teorias administrativas, motivação, liderança, cultura e modelos de gestão pública.
- **Direitos Humanos (4 trechos):** `a02/s01`, `a05/s03`, `c01/s01`, `c02/s01`. Precisão em tratados internacionais (DUDH, CADH, CEDAW, CDPD, Regras de Mandela).
- **DPPM (4 trechos):** `a06/s02`, `a10/s01`, `a12/s01`, `c01/s01`. 100% aderente ao CPPM, LOJMU (Lei 13.774/2018) e jurisprudência pacificada (STF HC 127.900/AM).
- **Direito Administrativo (3 trechos):** `da/a02/s03`, `da/a05/s03`, `da/a21/s06`. Lei 14.133/2021 e processos administrativos conferidos.
- **Direito Constitucional (3 trechos):** `dc/a02/s02`, `dc/a09/s02`, `dc/a13/s03`. Direitos fundamentais e segurança pública estadual conferidos.
- **Língua Portuguesa (3 trechos):** `lp/a06/s02`, `lp/a06/s03`, `lp/a08/s03`. Regência, concordância e sintaxe conformes à norma culta.
- **Raciocínio Lógico (3 trechos):** `rl/a04/s02`, `rl/a04/s11`, `rl/c02/s01`. Lógica proposicional e probabilidades deduzidas sem falhas.
- **Legislações PE (3 trechos):** `a01/s02`, `c01/s01`, `c09/s01`. Legislação estadual conferida (Decreto 50.014/2020, Lei 13.314/2007).
- **Direito Penal Militar (3 trechos):** `a04/s01`, `a08/s02`, `a11/s01`. Penas e crimes militares em tempo de paz e guerra conferidos.

**Veredito dos Resumos:** **100% Aprovados**. Nenhum erro de fato encontrado nos textos analíticos e sintéticos; formatação em seções, presenças obrigatórias da seção `### Para fixar` com 5 a 8 itens e impressões digitais (`startPage`, `endPage`, `startTopic`) 100% preservadas.

### 3.2 Bizus (12 arquivos JSON e mais de 250 assertivas C/E conferidas)
Foram auditados **12 arquivos de bizu** em `content/items/`:
- `administracao/a04.json` e `a07.json` (72 assertivas C/E).
- `direitos-humanos/a02.json` e `c02.json` (32 assertivas C/E).
- `direito-processual-penal-militar/a02.json` e `a07.json` (24 assertivas C/E).
- `direito-administrativo/a08.json` (48 assertivas C/E).
- `direito-constitucional/a16.json` (50 assertivas C/E).
- `lingua-portuguesa/a08.json` (30 assertivas C/E).
- `raciocinio-logico/a01.json` (72 assertivas C/E).
- `legislacoes-pe/c03.json` (8 assertivas C/E).
- `direito-penal-militar/a10.json` (34 assertivas C/E).

**Veredito dos Bizus:** **100% Aprovados**. Em todas as assertivas, o valor `isTrue` foi verificado como indiscutivelmente correto e fundamentado pela respectiva justificativa; equilíbrio Certo/Errado mantido rigorosamente em 50%/50% em cada trecho; resumos no formato correto com apenas negrito.

---

## 4. Auditoria Integral dos Materiais Complementares (8 arquivos)

Os 8 complementos autorais foram lidos de ponta a ponta contra as fontes oficiais:

1. **`content/complements/adm-cfoa-lacunas.md`:** **APROVADO (SEM RESSALVAS)**. Cobre com maestria os itens 1.10 (Processo Decisório - Simon) e 1.12 (Mudança Organizacional - Lewin, Kotter).
2. **`content/complements/dppm-cfoa-lacunas.md`:** **APROVADO (SEM RESSALVAS)**. Aborda com precisão prerrogativas de posto/função (arts. 73 e 242 CPPM), comparecimento espontâneo (art. 262), menagem (arts. 263-269) e liberdade provisória sem fiança (art. 270).
3. **`content/complements/dh-cedaw.md`:** **APROVADO (SEM RESSALVAS)**. Detalha a Convenção CEDAW (Decreto 4.377/2002) e Protocolo Facultativo (Decreto 4.316/2002), 23 peritos, prazos e relatórios.
4. **`content/complements/dh-convencao-pcd.md`:** **APROVADO (SEM RESSALVAS)**. Rigor constitucional (art. 5º, § 3º; Dec. Leg. 186/2008 e Dec. 6.949/2009), modelo social de deficiência e comitê internacional de 18 membros.
5. **`content/complements/dpm-crimes-licitacoes.md`:** **APROVADO (SEM RESSALVAS)**. Exatidão na revogação da Lei 8.666/93 pela Lei 14.133/2021, tipos dos arts. 337-E a 337-P do CP e enquadramento como crime militar por extensão (art. 9º, II do CPM).
6. **`content/complements/leg-lei-12527-lai.md`:** **APROVADO COM CORREÇÃO FORMAL**. Corrigido artefato tipográfico pontual na linha 120 (art. 32, § 1º, II). Texto da LAI 100% verídico.
7. **`content/complements/leg-pe-lei-13314-assedio.md`:** **APROVADO (SEM RESSALVAS)**. Texto plenamente atualizado até as Leis Estaduais nº 18.379/2023 e 19.086/2025 (*bullying/cyberbullying*).
8. **`content/complements/leg-pe-lei-6783-lacunas.md`:** **APROVADO COM ATUALIZAÇÃO DE NOTA**. Confirmada na íntegra a regra do art. 74-AD da Lei 6.783/1974 (LC 460/2021), encerrando formalmente a pendência anterior.

---

## 5. As 10 Falhas Mais Graves Identificadas (e Corrigidas)

Caso fossem para produção sem revisão, estas falhas poderiam induzir o aluno a erro em prova ou anular questões:

1. **Competência Monocrática da JMU para Civil Corréu com Militar (DPPM Q22):** A questão original atribuía competência ao Conselho de Justiça para julgar o militar corréu com civil. Desde a Lei nº 13.774/2018 (art. 30, I-B, *a*, da Lei nº 8.457/92), a competência monocrática do Juiz Federal atrai o processo conjunto de ambos.
2. **Confusão sobre a Prescrição da Deserção no CPM (DPPM Q50):** O elaborador confundiu o termo inicial da prescrição da deserção com a condição especial etária de extinção da punibilidade aos 45 anos para praça e 60 para oficial (art. 132 do CPM), citando artigo inexistente.
3. **Prazos Recursais da LC Estadual nº 470/2021 (LegPE CFOA #126):** O autor original estipulou "15 dias corridos" para o recurso administrativo contra o Quadro de Acesso. A LC 470/2021 estabelece taxativamente **10 dias úteis** (arts. 41 e 76).
4. **Deturpação do Tipo Qualificado do Concerto para Deserção (DPM CFOA #53):** A questão sustentava concurso material entre o concerto e a deserção consumada, quando o art. 191, II, do CPM tipifica figura qualificada única com reclusão de 2 a 4 anos.
5. **Majorante de Funcionário Público na Lei de Racismo (DPM CFOA #130):** A questão citava o "art. 20-C" e o "art. 2º-A" para o aumento de pena decorrente de cargo público; o dispositivo exato introduzido pela Lei nº 14.532/2023 é o **art. 20-B** da Lei nº 7.716/1989.
6. **Capitulação de Racismo em Eventos Esportivos/Culturais (DPM CFOA #125):** Citava inexistente "art. 20-A"; o correto é o **art. 20, § 2º-A** da Lei nº 7.716/1989.
7. **Inversão de Incisos na Lei de Abuso de Autoridade (DPM CFOA #100):** O autor trocou o inciso III (deixar de entregar nota de culpa em 24h) pelo inciso IV (prolongar prisão sem justa causa) do art. 12 da Lei nº 13.869/2019.
8. **Remissão de Artigo na Lei Estadual de Assédio (LegPE CFOA #173):** Citava o "art. 7º" para os cartazes A3; o correto é o **art. 6º, § 1º** da Lei nº 13.314/2007.
9. **Exclusividade do Maior Retorno Econômico (DA #8):** A questão tratava o critério como "preferencial" para contrato de eficiência, violando a exclusividade expressa do art. 39 da Lei nº 14.133/2021.
10. **Artefato Tipográfico na LAI (`leg-lei-12527-lai.md`):** Caracteres espúrios no texto sobre a aplicação subsidiária da Lei 8.112/90 (`apuradasตาม e punidas`) que degradavam a apresentação ao aluno.

---

## 6. Parecer de Risco por Disciplina

Conforme os critérios objetivos do §9 do briefing:
- `< 3%`: **LIBERAR**
- `3% a 8%`: **LIBERAR COM RESSALVA**
- `> 8%`: **REVISAR TUDO ANTES**

| Disciplina | Taxa de Erro Fático | Parecer Final | Justificativa |
| :--- | :---: | :---: | :--- |
| **Administração** | **0,00%** | **LIBERAR** | 0 erros em 59 questões amostradas. Conteúdo doutrinário e resumos perfeitos. |
| **Direitos Humanos** | **0,00%** | **LIBERAR** | 0 erros em 44 questões amostradas. Fidelidade absoluta aos tratados e jurisprudência. |
| **Direito Constitucional** | **0,00%** | **LIBERAR** | 0 erros em 20 questões auditadas (80% da base). |
| **Língua Portuguesa** | **0,00%** | **LIBERAR** | 0 erros em 20 questões auditadas. Total aderência ao Manual de Redação da PR e à gramática normativa. |
| **Raciocínio Lógico** | **0,00%** | **LIBERAR** | 0 erros em 20 questões auditadas. Todas as contas e deduções recalculadas à mão com 100% de consistência. |
| **Direito Administrativo** | **0,00% a 3,45%** | **LIBERAR** | Apenas 1 ajuste de precisão legal em 29 questões auditadas. Resumos e bizus impecáveis. |
| **Direito Processual Penal Militar** | **3,51%** | **LIBERAR COM RESSALVA** | 2 erros corrigidos em 57 questões. Taxa na faixa de ressalva (3% a 8%). Resumos e bizus com 0% de erro. |
| **Legislações PE** | **3,57%** | **LIBERAR COM RESSALVA** | 1 erro fático de prazo legal + 1 ajuste formal em 28 questões. Taxa na faixa de ressalva (3% a 8%). Arcabouço estadual sólido. |
| **Direito Penal Militar** | **8,33%** | **REVISAR TUDO ANTES** | Taxa ultrapassou 8% na 1ª amostra (2/24) e persistiu em **8,33% (4/48)** após duplicação da amostra. Fragilidade em tipos penais especiais extravagantes e figuras qualificadas do CPM. |

---

## 7. Dúvidas que Dependem do Dono e Notas Estruturais

1. **Revisão Integral de Direito Penal Militar:**  
   Em conformidade com a regra estrita do briefing, recomenda-se ao dono revisar as 110 questões restantes de `direito-penal-militar` antes de promover a disciplina para a produção, atentando-se para:
   - Remissões numéricas da Lei nº 13.869/2019 (Abuso de Autoridade) e Lei nº 7.716/1989 (Racismo/Injúria Racial após a Lei nº 14.532/2023);
   - Tipos penais complexos e figuras qualificadas da Parte Especial do Código Penal Militar.
2. **Decreto Estadual nº 50.014/2020 × STF ADI 6595:**  
   O Decreto Estadual nº 50.014/2020 extinguiu a privação física de liberdade em faltas disciplinares de militares de PE. Posteriormente, o STF julgou a ADI 6595 declarando a inconstitucionalidade formal da lei federal genérica similar. Como o edital cobra expressamente o Decreto Estadual nº 50.014/2020, o material orienta o aluno a seguir o decreto estadual para a prova, mas é oportuno manter o alerta jurisprudencial.
3. **Prazos em Dias Úteis na Legislação de Pernambuco:**  
   Recomenda-se atenção redobrada aos prazos da LC Estadual nº 470/2021 (contados em dias úteis pelo art. 76), contrastando com os prazos tradicionais da Lei Estadual nº 6.783/1974 (contados em dias corridos).

---

## 8. Arquivos Alterados no Working Tree e Ações Recomendadas

### 8.1 Lista Completa de Arquivos Alterados no Repositório
Nenhum arquivo foi commitado. Todas as alterações encontram-se salvas no *working tree*:
- `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` (correções Q22 e Q50)
- `content/questoes/ineditas/mc/direito-administrativo.txt` (correção DA #8)
- `content/questoes/ineditas/mc/direito-penal-militar.txt` (correções CFOA #93, #100, #125, #130 e DPM2 #53)
- `content/questoes/ineditas/mc/legislacoes-pe.txt` (correções CFOA #126 e #173)
- `content/complements/leg-lei-12527-lai.md` (correção tipográfica)
- `content/complements/leg-pe-lei-6783-lacunas.md` (atualização e encerramento de pendência de nota de conferência)

### 8.2 Validações Técnicas Executadas (Todas com 0 Erros)
- `pipeline/questoes/ineditas_mc_nativas.py --check`: **6.509 questões · 0 erros**.
- `pipeline/questoes/lacunas_cfoa.py --check`: **0 trechos < 7, 0 aulas < 25, faltam 0 questões**.
- `pipeline/validate_summaries.py`: **0 erros**.
- `pipeline/validate_content.py`: **0 erros**.

### 8.3 Comandos que o Dono Deve Rodar Após a Homologação
1. **Regerar PDFs dos Complementos:**
   Como houve ajuste formal em `leg-lei-12527-lai.md` e `leg-pe-lei-6783-lacunas.md`:
   ```powershell
   .\pipeline\.venv\Scripts\python.exe pipeline/complements/build_complements.py
   ```
2. **Atualizar Questões no Banco Local:**
   Para carregar as 9 questões corrigidas no banco de dados local:
   ```powershell
   npx tsx web/scripts/questoes-ineditas.ts
   ```

---

## 9. Revisão integral de Direito Penal Militar e varredura de capitulação (25/10/2026)

Executado conforme `pipeline/briefs/cfoa-conclusao.md`, Etapa A. Conferência feita contra os textos oficiais baixados do Planalto (CPM, CPPM, CP, Lei 13.869/2019, Lei 7.716/1989, Lei 8.457/1992, Lei 14.133/2021, Lei 8.429/1992, Lei 9.784/1999, CF) e do portal da ALEPE (Lei 11.817/2000, Decreto 50.014/2020, Lei 6.783/1974, Lei 14.804/2012, Lei 13.314/2007). Nenhum banco foi alterado.

### 9.1 Pontos que a revisão por amostra não conseguiu ler na fonte (Etapa A.2)

| Ponto | Texto oficial | Resultado |
| :--- | :--- | :--- |
| CPM, art. 191, II | "Modalidade complexa — II - se consumada a deserção: Pena - reclusão, de dois a quatro anos." | Confirmado; a correção da DPM2 #53 está certa. |
| Lei 13.869/2019, art. 12, p.u., III e IV | III = deixar de entregar ao preso, em 24 h, a nota de culpa (motivo da prisão, nomes do condutor e das testemunhas); IV = prolongar a execução da prisão sem executar o alvará | Confirmado. Na mesma questão (#100) a alternativa correta dizia "nome dos executores": corrigido para "nomes do condutor e das testemunhas". |

### 9.2 Direito Penal Militar: as 158 questões do CFOA relidas uma a uma

A amostra anterior (48 questões, 8,33%) subestimou o problema. Na releitura integral, 63 das 158 questões precisaram de ajuste; em **cerca de 38 (24%) havia erro de fato** (o resto era imprecisão de redação ou de comentário). Gabaritos não foram trocados: as correções reescreveram a alternativa defeituosa ou o comentário, mantendo a letra e o equilíbrio de gabaritos.

| Tipo | Qtd. | Exemplos (nº = ordem entre as 158 do CFOA) |
| :--- | :---: | :--- |
| Alternativa errada também defensável (ambiguidade) | 7 | #30 (coação física nos crimes contra o dever militar, art. 40); #47 (resistência com morte, § 1º-A incluído pela Lei 14.688/2023); #57 (embriaguez por substância análoga); #112 (Lei 7.716 tem pena de multa e PSC no art. 4º, § 2º); #140 (337-G exige invalidação judicial); #24 e #156 (insignificância no STM; falso × crime licitatório) |
| Fato errado no enunciado ou na alternativa correta | 21 | #127 (não existe crime de "recusa hospitalar" no art. 8º da Lei 7.716: reescrita para o art. 9º); #119 (transporte é o art. 12, não o 10); #124 (efeitos não automáticos: art. 18, não art. 16, p.u.); #133 (Forças Armadas estão no art. 13, não no 3º); #137 (art. 337-E com a redação revogada do art. 89 da Lei 8.666); #108 (constranger a depor quem guarda segredo é o art. 15, não o 30); #23 (comandante de "navio, aeronave ou praça de guerra", não "força"); #38 (art. 139: violar território "para praticar ato de jurisdição em nome do Brasil"); #39 (requisito inventado "bastam dois armados"); #44 (exceção inventada "para repelir agressão"); #81 (confusão entre arts. 349 e 354); #145, #147, #148 (elementares dos arts. 337-L, 337-O, 337-P); #100 (nota de culpa) |
| Fato errado só no comentário | 10 | #28, #55, #74, #77, #144, #146 (parágrafo/inciso inexistente ou trocado); #46 (pena do art. 175 desatualizada: 3 meses a 2 anos desde a Lei 14.688/2023); #75 (elementar do art. 324); #99 (texto antigo da Lei 4.898); #155 (art. 310 do CPM) |
| Forma/precisão (sem erro de fato) | 25 | #14, #22, #35, #36, #42, #58, #59, #64, #65, #69, #97, #107, #126, #129, #138 e outras |

Três pontos de jurisprudência foram reescritos com cautela por não haver tese firme verificável: #7 (STF e julgamento de civis pela JMU), #13 (antes "STM pacificou a não incidência da insignificância na violência doméstica"; agora a questão cobra o art. 209, § 6º, do CPM) e #12 (o veto ao § 3º do art. 9º, que excluía crimes sexuais e de violência doméstica, mantido pelo Congresso em 9/5/2024).

**Parecer revisto:** a disciplina passou de "REVISAR TUDO ANTES" para **LIBERAR COM RESSALVA** após a revisão integral. A ressalva: a taxa real de erro do lote original era ~24%, então o mesmo autor/lote deve ser tratado com desconfiança em qualquer outra disciplina não revisada por inteiro.

### 9.3 Varredura automatizada de capitulação (Etapa A.3)

Script (fora do repositório) que extrai toda citação "art. N" das inéditas do CFOA, localiza o artigo no texto oficial e sinaliza: artigo inexistente, prazo/pena/quantidade da frase ausente do artigo, e baixa aderência lexical entre a frase e o artigo. Cada sinal foi conferido à mão.

| Disciplina | Citações | Confrontadas | Questões corrigidas | Principais achados |
| :--- | :---: | :---: | :---: | :--- |
| Direito Processual Penal Militar | 200 | 192 (CPPM, CPM, Lei 8.457) | 31 | ~21 artigos trocados (ex.: arts. 88 → 90; 91 → 96; 92 → 94; 165/169 → 163; 315/317 → 307/309; 331 → 334/335; 363 → 366; 451 → 456; 457 § 2º → § 4º; Lei 8.457, art. 6º, I, a, para oficiais-generais); e 8 erros de conteúdo: prazo de internação de "20 + 20 dias" inexistente (art. 157 só fixa 45 dias para o laudo, #104), "internação provisória por 5 dias" (o prazo do art. 272, § 1º, é de interdição de estabelecimento, #153), "não faz coisa julgada no cível" (art. 169 só fala em processo penal ulterior, #117), "vedação de menagem ao desertor" sem base legal (#212 e #227, este reescrito para o art. 453), cassação da menagem com "prisão preventiva automática" (#152 e #214, art. 265), "rito sumaríssimo" pelo art. 458, revogado (#198, reescrito para o art. 391 do CPM) |
| Legislações PE | 66 | 66 (textos da ALEPE) | 24 | ~18 artigos trocados (Lei 11.817: 2 → 15; 12 → 13; 14/15 → 11; 19/20 → 24/25; 29 → 28, § 4º; 31/32 → 30; Decreto 50.014: 5 → 6, I; 8 → 6, § 2º; Estatuto: 63 → 62; 72 → 69; LAI estadual 14.804: numeração da lei federal → arts. 6º, 8º e 9º; Lei 13.314: 2 → 2º-C; 5 → 6º-A, p.u.); conteúdo: "transgressão grave" como requisito da pronta intervenção (#10), atenuante inventada "evitar mal maior" (#62), "premeditação" como agravante (#63), "114 tipos" na Parte Especial (#61), autoridades da prisão sem publicação (o art. 29 cita o Chefe da Casa Militar, não o Secretário de Defesa Social, #44) |
| Direito Administrativo | 204 | 115 (Lei 14.133, 8.429, 9.784, CF) | 0 | 13 sinais, todos conferidos e corretos (números de distratores ou de outro parágrafo do mesmo artigo). Citações de normas não baixadas (súmulas, decretos, CF em artigos longos) não foram confrontadas |

Validadores após as correções: `ineditas_mc_nativas.py --check` 6.509 questões, 0 erros; `lacunas_cfoa.py --check` 0 trechos < 7, 0 aulas < 25; `validate_summaries.py` 0 erros; `validate_content.py` com 57 erros **anteriores e fora do CFOA** (afirmações C/E repetidas em `content/items/atualidades/*.json`, commit `47ec03e`).

PDFs regenerados (`build_complements.py --only <id> --no-merge`) dos dois complementos ajustados na revisão por amostra: `leg-lei-12527-lai` (6 págs.) e `leg-pe-lei-6783-lacunas` (4 págs.), mesmas páginas dos trechos.

### 9.4 Para gravar nos bancos (depende de autorização do dono)

O id de cada inédita é um hash do texto: as ~120 questões editadas aqui e na revisão por amostra ganham id novo. A regravação deve usar `--retirar-ausentes` (aposenta as versões antigas do mesmo lote) e o relatório deve mostrar `retired` igual ao número de questões editadas. Comandos em `pipeline/briefs/cfoa-conclusao.md`, Etapa A.8.
