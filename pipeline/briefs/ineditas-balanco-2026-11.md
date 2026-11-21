# Briefing 3 (20/11/2026): inéditas para completar a base de questões do site

Repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM`. Idioma de tudo: português do Brasil. Windows: use a ferramenta Write para
arquivos grandes (heredoc longo no Bash quebra) e defina `PYTHONIOENCODING=utf-8` nos comandos Python (`pipeline/.venv/Scripts/python`).
**Não faça commit, não use git, não grave em banco algum, não use `--remoto`, não rode seed nem importadores.** O orquestrador revisa,
faz o backup e grava no banco.

**Leia primeiro, inteiro, `pipeline/briefs/ineditas-cbmpe.md`** (formato do rascunho, ferramenta de anexar, padrão AOCP, fonte do conteúdo,
originalidade). Tudo o que está lá vale aqui. Este documento só acrescenta: a lista do que falta (por matéria e por assunto), o que mudou
nas regras do comentário e as instruções de cada matéria.

## 1. Por que e quanto

O balanço de produção de 20/11/2026 comparou, para cada matéria de cada concurso, as questões que o aluno recebe com a **meta**:

- **Meta de uso:** 25 questões × número de cadernos do ciclo mínimo (um caderno a cada 4 trechos de Teoria), para o aluno não repetir questão ao longo do plano;
- **Meta de proporção:** 60 questões por questão da prova, limitadas a 40 por trecho (não há conteúdo para mais);
- vale a maior das duas. Hoje 8 matérias estão abaixo dela em algum concurso.

**Faltam 1193 questões**, todas de múltipla escolha (A a E), todas inéditas MentorIA:

| Matéria | Arquivo de destino | Trechos com quota | **A escrever** |
|---|---|---:|---:|
| Direito Processual Penal Militar (`direito-processual-penal-militar`) | `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` | 15 | **372** |
| Atualidades (`atualidades`) | `content/questoes/ineditas/mc/atualidades.txt` | 51 | **350** |
| Legislações Pertinentes aos Militares de PE (`legislacoes-pe`) | `content/questoes/ineditas/mc/legislacoes-pe.txt` | 10 | **157** |
| História de Pernambuco (`historia-pe`) | `content/questoes/ineditas/mc/historia-pe.txt` | 3 | **87** |
| Língua Inglesa (`lingua-inglesa`) | `content/questoes/ineditas/mc/lingua-inglesa.txt` | 19 | **82** |
| Direitos Humanos (`direitos-humanos`) | `content/questoes/ineditas/mc/direitos-humanos.txt` | 9 | **81** |
| Legislação Estadual do PCPE (`legislacao-pcpe`) | `content/questoes/ineditas/mc/legislacao-pcpe.txt` | 9 | **49** |
| Língua Espanhola (`lingua-espanhola`) | `content/questoes/ineditas/mc/lingua-espanhola.txt` | 15 | **15** |
| **Total** | | | **1193** |

Ordem de prioridade (o que mais pesa na prova × o que está mais distante da meta):

1. **Direito Processual Penal Militar**: 372 questões.
2. **Atualidades**: 350 questões.
3. **Legislações Pertinentes aos Militares de PE**: 157 questões.
4. **História de Pernambuco**: 87 questões.
5. **Língua Inglesa**: 82 questões.
6. **Direitos Humanos**: 81 questões.
7. **Legislação Estadual do PCPE**: 49 questões.
8. **Língua Espanhola**: 15 questões.

A quantidade por trecho está em **`pipeline/briefs/ineditas-balanco-faltantes.csv`** (e nas tabelas da seção 6). Ela foi calculada para que
**primeiro** os trechos mais vazios recebam questões e para que os trechos compartilhados entre concursos recebam mais, sem ultrapassar 45 questões por trecho.
**Escreva exatamente a quantidade pedida em cada trecho** (pode passar 1 ou 2; não fique abaixo). Se um trecho realmente não comportar a quantidade
(acabou o conteúdo cobrável), pare, **avise no relatório** e diga em que outro trecho da mesma aula concentrou o resto; nunca repita assunto para fechar a conta.

Acompanhamento (mostra o que já foi escrito desde 20/11/2026):

```bash
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_balanco.py                       # resumo por matéria
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_balanco.py --lista atualidades   # trechos ainda abaixo da quota
```

## 2. Divisão sugerida em lotes de trabalho

Trabalhe em lotes independentes (no máximo **6 agentes ao mesmo tempo**; um agente por lote). Dois agentes nunca escrevem o mesmo trecho.

| Lote | Matéria(s) | Questões |
|---|---|---:|
| A | Direito Processual Penal Militar | 372 |
| B | Atualidades | 350 |
| C | Legislações PE + Legislação do PCPE | 206 |
| D | História de PE + Direitos Humanos | 168 |
| E | Inglês + Espanhol | 97 |

Os lotes A e B são grandes: podem ser divididos ao meio, na ordem das tabelas da seção 6 (primeira e segunda metade dos trechos), desde que cada metade tenha um agente próprio.

## 3. O que cada questão precisa ter

Formato idêntico ao das inéditas existentes (`content/questoes/ineditas/mc/<matéria>.txt`). A pessoa que estuda vê o enunciado, as 5 alternativas, marca, e depois lê o comentário.

1. **Enunciado**: completo e claro, com 25 a 90 palavras (textos de língua e situações-problema podem passar, até 140); termina com um comando
   ("assinale a opção correta", "assinale a opção INCORRETA", "indique..."). Sem referência a "conforme a aula", "o curso", "o professor", a página ou ao material-base.
2. **Cinco alternativas A) a E)**, plausíveis, **homogêneas e de tamanho parecido**; **uma só correta e indiscutível**. Os distratores trocam um elemento
   (número, prazo, órgão, autoridade, exceção, conceito vizinho); nada de absurdos nem de "todas/nenhuma das anteriores". A correta **nunca é a mais longa**.
3. **Gabarito**: no rascunho, a correta é **sempre a A**. A ferramenta de anexar sorteia a posição final e equilibra as letras (cada uma perto de 20%, nenhuma acima de ~30% por matéria, sem sequência A-B-C-D-E). Não tente embaralhar à mão.
4. **Comentário**: o texto depois de `// Comentário:`. Ele é o que o aluno lê depois de responder, então tem de **ensinar**:
   - **40 a 110 palavras** (o `--check` só barra abaixo de 5, mas este é o padrão exigido neste lote);
   - 1ª frase: o que a alternativa correta afirma e **por que** está certa (a regra, o conceito, a conta, o dispositivo);
   - em seguida, o erro específico dos distratores principais (o prazo certo, o órgão certo, o conceito trocado), sem enumerar as cinco alternativas;
   - **não cite letras** das alternativas erradas ("A e C erram") nem escreva "a alternativa correta é a A": o `--check` reprova e a ordem muda no sorteio;
   - cite o dispositivo ("art. 37, II, da CF") **só depois de conferi-lo** no texto da norma; se não conseguir conferir, explique a regra sem o número;
   - em cálculo, mostre a conta passo a passo (texto simples, sem LaTeX);
   - cada comentário é escrito para aquela questão: nada de frase de modelo repetida.
   - **Não há nota por alternativa** neste formato (isso é só das questões do TecConcursos): o comentário geral é suficiente e já faz a questão contar como "comentada" no sorteio do caderno.
5. **Dificuldade e tipo** (em cada trecho): cerca de 30% fáceis (definição, conceito), 50% médias (aplicação, exceção, comparação), 20% difíceis (situação-problema com mais de um passo). Pelo menos **20% com comando "INCORRETA"**, e variedade de tipo: conceito, caso concreto, prazo/competência, comparação, interpretação.
6. **Originalidade**: nada copiado do TecConcursos, de provas, do material protegido (`docs/`) ou de textos de sites. Não reproduza 10 ou mais palavras seguidas de nenhuma fonte. Contexto militar (bombeiros, policiais) é bem-vindo, mas **sem fato inventado sobre a corporação**.
7. **Vigência**: valem as normas, os fatos e os números de **novembro de 2026**. Confirme leis, números e nomes em fonte oficial (Planalto, ALEPE, STF/STJ, IBGE, Banco Central, ONU, Fundaj...). O resumo do curso pode ter erro: **a norma manda**. Não cite súmula, tema ou ADI que não consiga confirmar.
8. **Sem repetição**: antes de escrever um trecho, leia o que o arquivo de destino já tem dele (`grep -n "^@@ aNN/sNN" content/questoes/ineditas/mc/<matéria>.txt`) e cubra **outros tópicos**. Nada de mudar só os números ou trocar sinônimos.
9. **Cálculo** (não há matéria de cálculo neste lote, exceto contagem de prazos no Processual Penal Militar): refaça a conta por dois caminhos antes de fixar o gabarito.

## 4. Fluxo de trabalho (o mesmo do briefing das inéditas do CBMPE)

1. Escolha um **trecho** da sua matéria. Para cada um: `pipeline/.venv/Scripts/python pipeline/pcpe_tools/seg_summary.py <disciplina>/<aula>/<trecho>` (resumo analítico; só existe em matéria com resumo, veja a seção 6) e, se quiser, `pipeline/pcpe_tools/seg_bizu.py <trecho>`.
2. Escreva o rascunho num arquivo **seu**, fora do repositório, na pasta de rascunhos da sua sessão (`...\scratchpad\agentes\<seu-nome>\`), em blocos:

```
@@ <aula>/<trecho> | A
Enunciado completo ... assinale a opção correta.
A) alternativa CORRETA (sempre a A no rascunho)
B) alternativa
C) alternativa
D) alternativa
E) alternativa
// Comentário: por que a A está certa e o erro específico dos principais distratores (40 a 110 palavras; não cite letras das erradas).
```

   `<aula>/<trecho>` sem o nome da matéria (por exemplo `a08/s02` ou `c06/s01`).
3. Confira e grave (a ferramenta embaralha a posição da correta, valida e grava com trava em `content/questoes/ineditas/mc/<matéria>.txt`; **nunca edite os `.txt` à mão**):

```bash
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <matéria> --dry   # confere
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <matéria>         # grava
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check                         # precisa terminar com "erros 0"
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_balanco.py --lista <matéria>                   # o que ainda falta
```

4. Grave **uma aula por vez**, assim que escrevê-la (nunca tudo no fim): um corte de uso não pode perder trabalho. O aviso "trecho sem assunto do edital" do `--check` é só aviso; não use `item=`.
5. O `--check` barra: menos de 5 alternativas ou alternativas repetidas, enunciado sem comando, enunciado com menos de 6 ou mais de 140 palavras, comentário com menos de 5 palavras, questão repetida, **alternativa do gabarito bem mais longa que as outras**, letra acima de ~32% dos gabaritos, sequência cíclica de gabaritos e comentário que cita a letra correta entre as erradas. Se acusar erro numa questão sua, corrija o rascunho e regrave só o necessário (a ferramenta recusa lote com problema; não duplique).

## 5. Revisão cruzada e entrega

1. `lacunas_balanco.py --lista <matéria>` sem trecho pendente; `ineditas_mc_nativas.py --check` com `erros 0`.
2. **Releia cada questão nova como um revisor independente**: o gabarito é indiscutível? A norma e os números estão vigentes? O comentário bate com a alternativa? Só uma alternativa é correta? Corrija o que errar. Se precisar trocar uma questão **já gravada**, avise o orquestrador na resposta (trecho e número no arquivo), pois os `.txt` não se editam à mão.
3. Escreva `content/questoes/ineditas/REVISAO-2026-11-20-balanco-<seu-nome>.md` com: quantas escreveu por matéria e por aula; as fontes oficiais consultadas por trecho (principalmente Atualidades e História de PE); dúvidas que dependem do dono (norma ambígua, valor desatualizado, divergência do material); trechos que ficaram abaixo da quota e por quê.
4. Resposta final curta: totais por matéria, trechos que não chegaram à quota (e por quê), dúvidas para o dono. Não cole as questões.

**Depois da entrega (orquestrador, não os agentes):** `ineditas_mc_nativas.py --batch mentoria-inedita-mcn-2026-11-20 --json lote.json <arquivos>`, backup remoto (`web/scripts/questoes-backup.ts --remoto`), gravação (`web/scripts/questoes-ineditas.ts lote.json --remoto`, antes sem `--remoto`) e nova rodada do balanço de cadernos (`web/scripts/cadernos-auditoria.ts --remoto`). As questões entram como `APPROVED` e provisórias: a revisão humana por amostra vem depois.

## 6. Instruções por matéria e quotas por trecho

### 6.1. Direito Processual Penal Militar: 372 questões

Arquivo de destino: `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` · matéria `direito-processual-penal-militar`

**Concurso beneficiado:** CFOA (prova com 10 questões de DPPM; 9 cadernos do ciclo mínimo, mas só 228 questões, todas inéditas; nenhuma de banca real no banco).

**Norma:** Código de Processo Penal Militar (Decreto-Lei 1.002/1969), com a redação vigente em novembro de 2026. O CPM e o CPPM tiveram alterações recentes (por exemplo, a Lei 13.491/2017 e a Lei 14.688/2023): confirme no Planalto a redação do artigo antes de cobrá-lo. Confira cada artigo com `pipeline/.venv/Scripts/python pipeline/leis.py art cppm <número>`; se a norma não abrir, confirme no Planalto e **não cite o número do artigo** no comentário.

**Onde está o conteúdo:** resumo analítico de cada trecho (`pipeline/pcpe_tools/seg_summary.py <trecho>`) e material MentorIA em `content/material/direito-processual-penal-militar/`. O resumo pode ter erro: o texto da lei manda.

**Cuidados:**
- Não confunda o CPPM com o CPP comum (Lei 3.689/1941): prazos, nomenclatura e órgãos são diferentes (por exemplo, IPM × inquérito policial, encarregado × delegado, auditor × juiz). Nenhuma alternativa pode ficar correta por analogia ao CPP.
- Trechos mais fracos (7 a 13 questões hoje): `a08/s01` a `s04` (busca, apreensão, arresto, sequestro, prisão em flagrante, preventiva, menagem), `a02/s01` e `s02` (IPM), `a06/s01` e `s02` (competência) e `a10/s01` e `s02` (provas). Concentre variedade ali: prazos, autoridades, hipóteses de cabimento, exceções.
- Varie o tipo: conceito, situação-problema (um oficial instaura IPM...), prazos e contagem, competência (quem processa e julga), "INCORRETA".
- Contexto militar é bem-vindo (militar estadual do CBMPE), mas o direito tem de estar certo e nenhum fato pode depender de regra interna inventada.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a00/s01` | Lei de Processo Penal Militar e sua Aplicação (arts. 1º a 6º | Lei de Processo Penal Militar: Sistemas, Princípios e Aplicação (arts. 1º a 6º) ; Princípios do Processo Penal Militar ; Fontes do processo penal militar ; Aplicação d... | CFOA | 25 | **16** | 41 |
| `a01/s01` | Polícia Judiciária Militar (arts. 7º e 8º do CPPM) | Polícia Judiciária Militar: Exercício, Delegação e Competência (arts. 7º e 8º) | CFOA | 25 | **16** | 41 |
| `a02/s01` | Inquérito Policial Militar (arts. 9º a 28 do CPPM) | Inquérito Policial Militar: Finalidade, Características, Instauração e Providências (arts. 9º a 15) | CFOA | 13 | **28** | 41 |
| `a02/s02` | Inquérito Policial Militar (arts. 9º a 28 do CPPM) | Inquérito Policial Militar: Sigilo, Detenção, Prazos, Relatório e Arquivamento (arts. 16 a 28) | CFOA | 12 | **29** | 41 |
| `a06/s01` | Competência da Justiça Militar e Prerrogativa do Posto ou da | Competência da Justiça Militar, Foro Militar e Prerrogativa do Posto ou da Função ; Da Competência em Geral ; Da Competência pelo Lugar da Infração ; Da Competência pe... | CFOA | 13 | **28** | 41 |
| `a06/s02` | Competência da Justiça Militar e Prerrogativa do Posto ou da | Da Competência pela Sede ou Lugar do Serviço ; Da Competência pela Prerrogativa de Posto ou da Função | CFOA | 12 | **29** | 41 |
| `a07/s01` | Incidente de Insanidade Mental e Incidente de Falsidade de D | Incidente de Insanidade Mental e Incidente de Falsidade Documental (arts. 156 a 169) | CFOA | 25 | **16** | 41 |
| `a08/s01` | Medidas Preventivas e Assecuratórias: Providências sobre Coi | Providências que Recaem sobre Coisas: Busca, Apreensão e Restituição (arts. 170 a 198) ; Da apreensão | CFOA | 7 | **30** | 37 |
| `a08/s02` | Medidas Preventivas e Assecuratórias: Providências sobre Coi | Medidas Assecuratórias: Arresto, Sequestro e Hipoteca Legal (arts. 199 a 219) ; Da restituição ; Sequestro ; Hipoteca Legal ; Arresto | CFOA | 7 | **30** | 37 |
| `a08/s03` | Medidas Preventivas e Assecuratórias: Providências sobre Coi | Providências que Recaem sobre Pessoas: Prisão Provisória e Prisão em Flagrante (arts. 220 a 253) | CFOA | 7 | **30** | 37 |
| `a08/s04` | Medidas Preventivas e Assecuratórias: Providências sobre Coi | Prisão Preventiva e Menagem (arts. 254 a 269) ; Menagem ; Liberdade provisória ; Aplicação provisória de medidas de segurança | CFOA | 7 | **30** | 37 |
| `a10/s01` | Atos Probatórios: Interrogatório, Confissão, Perícias, Teste | Atos Probatórios: Qualificação e Interrogatório, Confissão e Perícias e Exames (arts. 302 a 346) ; Confissão ; Perícias e Exames | CFOA | 13 | **28** | 41 |
| `a10/s02` | Atos Probatórios: Interrogatório, Confissão, Perícias, Teste | Testemunhas, Acareação, Reconhecimento, Documentos e Indícios (arts. 347 a 383) ; Acareação ; Documentos ; Indícios | CFOA | 12 | **30** | 42 |
| `a12/s01` | Instrução Provisória de Deserção e Processos Especiais | Instrução Provisória de Deserção de Oficial e de Praça (arts. 451 a 462) | CFOA | 25 | **16** | 41 |
| `c01/s01` | Prerrogativas de Posto ou Função, Comparecimento Espontâneo, | 1. Prerrogativas do Posto ou da Função no Processo Penal Militar (Item 1.2 do Edital) ; 2. Comparecimento Espontâneo do Indiciado ou Acusado (Item 1.4 do Edital) ; 3. ... | CFOA | 25 | **16** | 41 |
| | | | | | **372** | |

### 6.2. Atualidades: 350 questões

Arquivo de destino: `content/questoes/ineditas/mc/atualidades.txt` · matéria `atualidades`

**Concurso beneficiado:** CBMPE Soldado (5 questões na prova; 22 cadernos no ciclo mínimo e só 200 questões no pool).

**Atenção máxima: Atualidades envelhece.** A prova é em 28/02/2027 e as questões ficam no banco por meses. Por isso **só vale conteúdo estável**:
- **Pode:** conceitos (globalização, neoliberalismo, multilateralismo), organizações e suas funções (ONU, OMC, OTAN, BRICS, UE, Mercosul, OEA), tratados e acordos **já assinados** com o ano, eventos históricos consolidados, causas, contexto e consequências, geografia política, conceitos ambientais e energéticos (Acordo de Paris, matriz energética, biomas), temas de Pernambuco que não mudam (Suape, transposição do São Francisco, Fernando de Noronha, regiões de desenvolvimento), conceitos de segurança pública, tecnologia e sociedade (LGPD, marco civil, inteligência artificial como conceito).
- **Não pode:** quem ocupa cargo hoje (presidentes, ministros, secretários), resultados de eleições e competições recentes, índices e números anuais (PIB, inflação, desmatamento, população, ranking), conflitos em andamento descritos no estado atual, preços, fatos posteriores a outubro de 2026 e qualquer "recentemente".
- **Vários tópicos dos trechos são datados por natureza** (por exemplo, medidas de um governo, intervenções, conflitos e crises em curso, eleições). **Não escreva questão sobre o fato em andamento.** Use os outros tópicos do mesmo trecho ou o **conceito estável** por trás do tema (o que é migração forçada, o que faz a OTAN, o que é matriz energética, causas históricas do conflito até um marco já encerrado). Se o trecho só tiver tópico datado, escreva menos e registre no relatório.
- As questões "datadas" foram **retiradas na auditoria de 14/10/2026**: não as ressuscite (`content/questoes/overrides-questoes.json`).
- Confirme todo fato em fonte oficial ou primária (IBGE, Banco Central, ONU/OMC/OMS, sites oficiais de tratados, governo federal e de PE) e registre no relatório as fontes de cada trecho.

**Onde está o conteúdo:** esta disciplina **não tem resumo analítico nem capítulo do material MentorIA**, e os bizus existentes são genéricos (não os use como fonte). Parta do `assunto` e dos `tópicos` da tabela; para entender o escopo, `pipeline/summary_source.py <trecho>` mostra o texto-fonte protegido (só para entender; **nunca copie**; pode ter bytes NUL: grave em arquivo seu e leia com `tr -d '\000'`). Antes de escrever, anote no seu relatório os subtópicos estáveis escolhidos para cada trecho.

**Já existem 24 questões** (trechos `a00/s01` a `s04` e `a01/s01` e `s02`: neoliberalismo, globalização, crise de 2008, OMC, Brexit, UE, Mercosul, Nova Rota da Seda, Primavera Árabe, sunitas e xiitas, curdos, Israel, Qatar, Turquia etc.). Leia `mc/atualidades.txt` e **cubra outros assuntos**.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a00/s04` | Panorama Internacional – I | Medidas do Governo de Donald Trump ; Imigração ; Política Externa ; Economia ; Meio Ambiente ; Saúde | Soldado | 4 | **4** | 8 |
| `a01/s01` | Panorama Internacional - II | Primavera Árabe ; Síria ; Iraque ; Curdistão ; Iêmen | Soldado | 5 | **3** | 8 |
| `a02/s01` | Panorama Internacional - III | Deslocados à Força no Mundo ; Migrantes Climáticos ; Panorama Atual das Migrações ; Nacionalismo ; Xenofobia ; O Bem que o Migrante Faz | Soldado | 3 | **5** | 8 |
| `a02/s02` | Panorama Internacional - III | ) Organização das Nações Unidas (ONU) ; ) Organização dos Estados Americanos (OEA) ; ) Comunidade dos Estados Latino-Americanos e Caribenhos (CELAC) ; ) UNASUL e PROSU... | Soldado | 4 | **4** | 8 |
| `a02/s03` | Panorama Internacional - III | A Questão da OTAN ; A Crimeia e os Territórios Separatistas Pró-Rússia ; Início e Evolução da Guerra ; Crise Migratória ; Argentina | Soldado | 5 | **3** | 8 |
| `a02/s04` | Panorama Internacional - III | Venezuela ; Intervenção dos Estados Unidos e captura de Nicolás Maduro ; ) Como é o Vírus ; ) Vacinas Contra o Vírus ; ) Cenário Global Pós-pandemia de Covid-19 | Soldado | 6 | **2** | 8 |
| `a03/s03` | Panorama Nacional - I | ) Desindustrialização ; ) Descentralização Industrial ; ) Transporte Rodoviário ; ) Transporte Aquaviário ; ) Transporte Ferroviário ; ) Transporte Aéreo | Soldado | 2 | **6** | 8 |
| `a03/s04` | Panorama Nacional - I | ) Transporte Intermodal ; ) Concessões ; Energia Limpa e Energia Suja ; Energia Renovável e Energia Não Renovável ; Energia Tradicional e Energia Alternativa ; Matriz ... | Soldado | 6 | **2** | 8 |
| `a04/s01` | Panorama Nacional – II | ) Federação ; ) República ; ) Estrutura dos Poderes ; Redução das Taxas de Crescimento da População | Soldado | 3 | **5** | 8 |
| `a05/s02` | Panorama Nacional – III | Perfil das Vítimas ; Os Custos da Violência ; Causas da violência ; Propostas de Soluções para a Redução da Violência e da Criminalidade ; Violência Policial e Morte d... | Soldado | 6 | **2** | 8 |
| `a05/s03` | Panorama Nacional – III | Soluções para a Crise do Sistema Prisional ; Diretrizes da Educação ; Plano Nacional da Educação (PNE) ; Avaliação da Educação Brasileira ; Desafios da Educação Brasil... | Soldado | 7 | **1** | 8 |
| `a07/s01` | Retrospectiva de Atualidades Março de 2026 | Fatos Internacionais ; Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a07/s02` | Retrospectiva de Atualidades Março de 2026 | Guerra Estados Unidos e Israel X Irã ; Ciência e Tecnologia | Soldado | 0 | **8** | 8 |
| `a07/s03` | Retrospectiva de Atualidades Março de 2026 | Sociedade, Cultura e Personalidades ; Fatos Nacionais ; Economia Brasileira | Soldado | 0 | **8** | 8 |
| `a07/s04` | Retrospectiva de Atualidades Março de 2026 | Política Brasileira ; Sociedade | Soldado | 0 | **8** | 8 |
| `a07/s05` | Retrospectiva de Atualidades Março de 2026 | Segurança Pública | Soldado | 0 | **7** | 7 |
| `a09/s01` | Retrospectiva de Atualidades Abril de 2026 | Fatos Internacionais ; Guerras e Conflitos | Soldado | 0 | **8** | 8 |
| `a09/s02` | Retrospectiva de Atualidades Abril de 2026 | Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a09/s03` | Retrospectiva de Atualidades Abril de 2026 | Ciência e Tecnologia | Soldado | 0 | **8** | 8 |
| `a09/s04` | Retrospectiva de Atualidades Abril de 2026 | Sociedade, Cultura e Personalidades ; Fatos Nacionais ; Economia Brasileira | Soldado | 0 | **8** | 8 |
| `a09/s05` | Retrospectiva de Atualidades Abril de 2026 | Política Brasileira | Soldado | 1 | **7** | 8 |
| `a09/s06` | Retrospectiva de Atualidades Abril de 2026 | Segurança Pública | Soldado | 0 | **8** | 8 |
| `a11/s01` | Retrospectiva de Atualidades Maio de 2026 | A Copa e sua organização ; Copa do Mundo 2026: veja perguntas e respostas ; A Copa do Mundo mais cara da história para os torcedores ; Exigência da FIFA reduz capacida... | Soldado | 0 | **8** | 8 |
| `a11/s02` | Retrospectiva de Atualidades Maio de 2026 | Copa do Mundo 2026: entenda as novas regras anunciadas pela FIFA ; curiosidades sobre a Trionda, a bola tecnológica da Copa do Mundo de 2026 ; Maior e mais caro: 10 cu... | Soldado | 0 | **7** | 7 |
| `a11/s03` | Retrospectiva de Atualidades Maio de 2026 | Das flores em Lyon aos consulados americanos, a rivalidade entre Estados Unidos e Irã ganha um novo campo ; Seleções e suas histórias ; Brasil iguala período de maior ... | Soldado | 0 | **8** | 8 |
| `a11/s04` | Retrospectiva de Atualidades Maio de 2026 | Fatos Internacionais ; Guerras e Conflitos ; Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a11/s05` | Retrospectiva de Atualidades Maio de 2026 | Ciência e Meio Ambiente ; Fatos Nacionais ; Economia Brasileira | Soldado | 1 | **7** | 8 |
| `a11/s06` | Retrospectiva de Atualidades Maio de 2026 | Política Brasileira ; Sociedade Brasileira | Soldado | 0 | **8** | 8 |
| `a11/s07` | Retrospectiva de Atualidades Maio de 2026 | Segurança Pública | Soldado | 0 | **8** | 8 |
| `a13/s01` | Retrospectiva de Atualidades Junho de 2026 | Fatos Internacionais ; Guerras e Conflitos | Soldado | 0 | **8** | 8 |
| `a13/s02` | Retrospectiva de Atualidades Junho de 2026 | Economia Internacional ; América Latina | Soldado | 0 | **8** | 8 |
| `a13/s03` | Retrospectiva de Atualidades Junho de 2026 | Sociedade ; Copa do Mundo 2026 | Soldado | 0 | **8** | 8 |
| `a13/s04` | Retrospectiva de Atualidades Junho de 2026 | Fatos Nacionais ; Economia Brasileira | Soldado | 0 | **8** | 8 |
| `a13/s05` | Retrospectiva de Atualidades Junho de 2026 | Política Brasileira | Soldado | 1 | **7** | 8 |
| `a13/s06` | Retrospectiva de Atualidades Junho de 2026 | Meio Ambiente e Ciência e Tecnologia | Soldado | 0 | **8** | 8 |
| `a15/s01` | Retrospectiva de Atualidades Julho de 2026 | Fatos Internacionais ; Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a15/s02` | Retrospectiva de Atualidades Julho de 2026 | Sociedade | Soldado | 0 | **8** | 8 |
| `a15/s03` | Retrospectiva de Atualidades Julho de 2026 | Meio Ambiente ; Tecnologia ; Fatos Nacionais ; Economia Brasileira | Soldado | 0 | **8** | 8 |
| `a15/s04` | Retrospectiva de Atualidades Julho de 2026 | Política Brasileira e Sociedade | Soldado | 0 | **8** | 8 |
| `a15/s05` | Retrospectiva de Atualidades Julho de 2026 | Segurança Pública ; Cultura e Personalidades | Soldado | 0 | **8** | 8 |
| `a17/s01` | Retrospectiva de Atualidades Agosto de 2026 | Fatos Internacionais ; Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a17/s02` | Retrospectiva de Atualidades Agosto de 2026 | Guerras e Conflitos | Soldado | 0 | **8** | 8 |
| `a17/s03` | Retrospectiva de Atualidades Agosto de 2026 | Estados Unidos ; Tecnologia | Soldado | 0 | **8** | 8 |
| `a17/s04` | Retrospectiva de Atualidades Agosto de 2026 | Fatos Nacionais ; Economia Brasileira | Soldado | 0 | **8** | 8 |
| `a17/s05` | Retrospectiva de Atualidades Agosto de 2026 | Política Brasileira ; Sociedade | Soldado | 0 | **8** | 8 |
| `a17/s06` | Retrospectiva de Atualidades Agosto de 2026 | Fatos Internacionais | Soldado | 0 | **7** | 7 |
| `a19/s01` | Retrospectiva de Atualidades Setembro de 2026 | Fatos Internacionais ; Guerras e Conflitos | Soldado | 0 | **8** | 8 |
| `a19/s02` | Retrospectiva de Atualidades Setembro de 2026 | Pelo Mundo | Soldado | 0 | **8** | 8 |
| `a19/s03` | Retrospectiva de Atualidades Setembro de 2026 | Ciência e Tecnologia ; Fatos Nacionais ; Economia Brasileira | Soldado | 1 | **7** | 8 |
| `a19/s04` | Retrospectiva de Atualidades Setembro de 2026 | Política Brasileira ; Sociedade | Soldado | 0 | **8** | 8 |
| `a19/s05` | Retrospectiva de Atualidades Setembro de 2026 | Educação, Cultura e Personalidades | Soldado | 0 | **8** | 8 |
| | | | | | **350** | |

### 6.3. Legislações Pertinentes aos Militares de PE: 157 questões

Arquivo de destino: `content/questoes/ineditas/mc/legislacoes-pe.txt` · matéria `legislacoes-pe`

**Concursos beneficiados:** Oficial (10 questões na prova), CFOA (15) e Soldado (5), que compartilham os mesmos trechos. Por isso a conta é de **157 questões** (e não 101 + 60 + 41): os trechos compartilhados valem para os três e os trechos `c06` a `c11` valem só para o CFOA. O Oficial e o Soldado só têm 2 questões reais da AOCP: o resto do pool é inédita.

**Normas (use sempre a redação vigente em novembro de 2026):** Lei 11.817/2000 (Código Disciplinar dos Militares de PE), Lei 6.783/1974 (Estatuto dos Militares de PE), Decreto 50.014/2020, Lei Estadual 15.187/2013, Lei Federal 14.751/2023 (Lei Orgânica Nacional das PMs e CBMs), Código de Ética dos Militares de PE, Lei de Promoção (trecho `c07`), Lei de Acesso à Informação (Lei 12.527/2011), assédio moral e sexual na administração estadual (Lei 13.314/2007), Sindicância Administrativo-Disciplinar Militar (portaria) e Investigação Preliminar (Provimento Correicional 21). Confira cada artigo com `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <artigo>` (normas no cache: `pe11817`, `pe6783`, `pe13314`, `pe15187`, `ped50014`, `ped22114`, `pelc470`, `l14751`, `l12527`); o que não estiver ali, confirme no site da ALEPE ou no Diário Oficial e, se não conseguir, **não cite o número do artigo** e explique a regra. Nada de súmula, tema ou decisão que você não possa confirmar.

**Cuidados:**
- É a matéria de maior peso do Oficial e do CFOA e a mais sujeita a erro de número (prazos, percentuais, quóruns, penas). Refaça cada número no texto da norma.
- Transgressões e penas têm gradação (classificação das transgressões, escala das penas): cuidado com distratores que trocam um degrau e confira cada degrau no texto da lei.
- Trechos mais fracos: `a01/s02` (transgressões), `a02/s01` e `s02` (Estatuto) e `c06` a `c11` (CFOA).
- Leia o que já existe em `mc/legislacoes-pe.txt` (368 questões) antes de escrever, trecho a trecho: cubra artigos e regras ainda não cobrados.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a01/s01` | Lei 11.817/2000: Código Disciplinar dos Militares de Pernamb | Código Disciplinar dos Militares do Estado de Pernambuco ; Do Regime Disciplinar ; Da Esfera De Ação E Da Competência Para Aplicação | Oficial+CFOA+Soldado | 20 | **21** | 41 |
| `a01/s02` | Lei 11.817/2000: Código Disciplinar dos Militares de Pernamb | Da Conceituação E Da Especificação Das Transgressões ; Consumação, Tentativa, Desistência Voluntária e Transgressão Impossível ; Do Julgamento Das Transgressões ; Da C... | Oficial+CFOA+Soldado | 15 | **27** | 42 |
| `a02/s01` | Lei 6.783/1974: Estatuto dos Militares de Pernambuco | Da Hierarquia e da Disciplina ; Do Cargo e da Função Policiais-Militares ; Das Obrigações Policiais-Militares | Oficial+CFOA+Soldado | 16 | **26** | 42 |
| `a02/s02` | Lei 6.783/1974: Estatuto dos Militares de Pernambuco | Dos Direitos ; Das Licenças ; Das Prerrogativas ; Das Situações Especiais ; Do Desligamento ou Exclusão do Serviço Ativo ; Do Tempo de Serviço | Oficial+CFOA+Soldado | 15 | **27** | 42 |
| `c06/s01` | Código de Ética dos Militares do Estado de Pernambuco (Decre | 1. Disposições Preliminares e Princípios Fundamentais (Arts. 1º a 5º) ; 2. Os Doze Valores Militares Estaduais (Art. 6º, Incisos I a XII) ; 3. Os Deveres Éticos e as R... | CFOA | 25 | **10** | 35 |
| `c07/s01` | Lei de Promoção dos Militares do Estado de Pernambuco (Lei C | 1. Disposições Preliminares e Critérios de Promoção (Arts. 1º a 15) ; 2. As Seis Promoções Extraordinárias em Detalhe (Arts. 8º a 15) ; 3. Requisitos Essenciais, Inter... | CFOA | 25 | **10** | 35 |
| `c08/s01` | Lei de Acesso à Informação — LAI (Lei Federal nº 12.527, de  | 1. Abrangência, Diretrizes e Conceitos Fundamentais (Arts. 1º a 5º) ; 2. Transparência Ativa vs. Transparência Passiva e Procedimento de Acesso (Arts. 6º a 20) ; 3. Re... | CFOA | 25 | **10** | 35 |
| `c09/s01` | Assédio Moral e Sexual na Administração Pública Estadual de  | 1. Visão Geral, Evolução Legislativa e Abrangência (Art. 1º e Parágrafo Único) ; 2. Conceitos de Assédio Moral (Art. 2º) e de Assédio Sexual (Art. 2º-C) ; 3. Condutas ... | CFOA | 25 | **10** | 35 |
| `c10/s01` | Sindicância Administrativo-Disciplinar Militar (Portaria nº  | 1. Finalidade, cabimento e quem instaura (Arts. 1º a 4º) ; 2. Instauração e roteiro do encarregado (Arts. 5º e 6º) ; 3. Prazos e revelia (Arts. 7º a 13) ; 4. Defesa (A... | CFOA | 27 | **8** | 35 |
| `c11/s01` | Investigação Preliminar (Provimento Correicional nº 21/2021  | 1. Objetivo e conceitos (Arts. 1º a 3º) ; 2. Registro e admissibilidade (Arts. 4º a 8º) ; 3. Instauração e prazo (Arts. 9º e 10) ; 4. Instrução no SEI (Art. 11) ; 5. R... | CFOA | 27 | **8** | 35 |
| | | | | | **157** | |

### 6.4. História de Pernambuco: 87 questões

Arquivo de destino: `content/questoes/ineditas/mc/historia-pe.txt` · matéria `historia-pe`

**Concurso beneficiado:** CBMPE Soldado (10 questões na prova de 60, ou 17%, com apenas 3 trechos; hoje só 33 questões, quase todas escritas no dia 16/11/2026).

**Já cobertos (não repita):** `a00/s01` coivara, tapuias, Caetés, Tabajaras, Potiguares, Parã-Nambuco, pau-brasil, aldeamentos, capitanias, Olinda e Recife; `a00/s02` açúcar e engenhos, União Ibérica, resistência, Nassau, Insurreição Pernambucana, Paz de Haia, Palmares, resistência quilombola, Mascates; `a00/s03` 1817, Confederação do Equador, Cabanada, Praieira, cangaço, Intentona, agamenonismo, Ligas e Arraes, frevo e maracatu. Leia `mc/historia-pe.txt` e **aprofunde com outros recortes**: personagens (Duarte Coelho, Jerônimo de Albuquerque, Maurício de Nassau, João Fernandes Vieira, André Vidal de Negreiros, Henrique Dias, Felipe Camarão, Frei Caneca, Joaquim Nabuco, Gilberto Freyre, Josué de Castro...), cronologia e ordem de fatos, causas e consequências, comparações entre revoltas (1817 × 1824 × Praieira), economia (açúcar, algodão, pecuária, sertão), sociedade (escravidão, abolição, urbanização do Recife), cultura (frevo, maracatu, manguebeat, patrimônio), Era Vargas e redemocratização em PE, símbolos e geografia histórica.

**Fontes:** esta disciplina **não tem resumo analítico**. Confirme datas, nomes e fatos em fonte acadêmica ou oficial (Fundaj, ALEPE, IPHAN, Arquivo Público Estadual, IBGE). Nada de data "arredondada"; cuidado com as confusões clássicas (Insurreição Pernambucana × Revolução de 1817 × Confederação do Equador × Praieira; Batalhas dos Guararapes; Mascates × Emboabas). Se um fato é controverso entre historiadores, **não o cobre**.

**Cuidado com a meta:** 29 questões novas por trecho exigem muitos recortes diferentes. Se acabar o conteúdo de um trecho, pare e avise no relatório: é melhor ficar abaixo do alvo do que repetir assunto.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a00/s01` | Aula única | Pernambuco: colonização, ocupação e sociedade ; Os contatos iniciais do europeu com os indígenas ; Os Caetés ; Os Tabajaras ; Os Potiguares ; O significado de Pernambu... | Soldado | 10 | **30** | 40 |
| `a00/s02` | Aula única | A importância do açúcar para a economia local ; A União Ibérica e o domínio holandês ; Escravidão e resistência em Pernambuco ; Movimentos de resistência e emancipacio... | Soldado | 11 | **29** | 40 |
| `a00/s03` | Aula única | Revolução de 1817 ; Confederação do Equador (1824) ; Guerra dos Cabanos (1832-1835) ; A Revolução Praieira (1848-1850) ; Pernambuco e a República ; Cangaço | Soldado | 12 | **28** | 40 |
| | | | | | **87** | |

### 6.5. Língua Inglesa: 82 questões

Arquivo de destino: `content/questoes/ineditas/mc/lingua-inglesa.txt` · matéria `lingua-inglesa`

**Concurso beneficiado:** CBMPE Oficial (5 questões na prova; só 68 questões reais da AOCP e 150 inéditas, 24 trechos com 7 a 13 questões cada).

**Formato:** textos curtos e **autorais** em inglês (3 a 8 linhas) com perguntas de interpretação, mais itens de gramática com frase própria. Na AOCP o comando costuma vir em português; você pode usar o enunciado em português e as alternativas em inglês ou o contrário, mas **mantenha o padrão dentro de cada questão**. As alternativas de interpretação são afirmações completas; as de gramática, a forma ou a palavra pedida.

**Cuidados:**
- Confira gramática, ortografia e vocabulário (use dicionário e gramática de referência: Cambridge, Oxford, Merriam-Webster). Uma só alternativa pode ser correta, inclusive em inglês britânico × americano (evite as variações).
- Nada de copiar textos de provas ou de sites. Evite temas datados e nomes reais.
- Cubra, por trecho, os tópicos do assunto (veja a tabela) e **varie**: cognatos verdadeiros e falsos, inferência, referência do pronome, tempos verbais, voz passiva, discurso indireto, comparativos, preposições, question tags, phrasal verbs, conectivos.
- Leia `mc/lingua-inglesa.txt` antes e não repita o ponto gramatical nem o texto-base.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a01/s01` | Substantivos, Artigos, Pronomes, Preposições e Resolução de  | Formação de Frases ; Substantivos ; 2.2. Substantivos Contáveis e Incontáveis ; 2.3. Plural dos Substantivos ; 2.4. Gêneros dos Substantivos (Nouns Gender) | Oficial | 7 | **5** | 12 |
| `a01/s02` | Substantivos, Artigos, Pronomes, Preposições e Resolução de  | 2.5. Substantivo que indica Posse (The Genitive Case) ; Artigos ; 3.2. O Artigo Indefinido A (um, uma) ; 3.3. O Artigo Indefinido AN (um, uma) ; 3.4. Plural dos Artigo... | Oficial | 7 | **5** | 12 |
| `a01/s03` | Substantivos, Artigos, Pronomes, Preposições e Resolução de  | Pronomes ; 4.2. PRONOMES REFLEXIVOS ; 4.3. PRONOMES POSSESSIVOS ; 4.4. PRONOMES DEMONSTRATIVOS ; 4.5. PRONOMES INTERROGATIVOS | Oficial | 7 | **5** | 12 |
| `a01/s04` | Substantivos, Artigos, Pronomes, Preposições e Resolução de  | 4.6. PRONOMES RELATIVOS ; 4.7. PRONOMES INDEFINIDOS | Oficial | 7 | **5** | 12 |
| `a01/s05` | Substantivos, Artigos, Pronomes, Preposições e Resolução de  | Preposições ; 5.2. PREPOSIÇÕES ABOVE e OVER ; 5.3. PREPOSIÇÕES DE LUGAR ; 5.4. PREPOSIÇÕES DE MOVIMENTO ; 5.5. PREPOSIÇÕES DESPITE E SPITE OF | Oficial | 7 | **5** | 12 |
| `a02/s01` | Adjetivos, Advérbios, Afixos e Resolução de Provas | Conjunções ; 1.2. Conjunções Subordinadas ; 1.3. Conjunções Correlativas | Oficial | 7 | **4** | 11 |
| `a02/s02` | Adjetivos, Advérbios, Afixos e Resolução de Provas | Adjetivos ; 1.2. Formação dos Adjetivos: ; 1.3. Graus dos Adjetivos: Comparativos e Superlativos | Oficial | 9 | **3** | 12 |
| `a02/s03` | Adjetivos, Advérbios, Afixos e Resolução de Provas | Advérbios ; 2.1. Advérbios de Tempo ; 2.2. Advérbios de Lugar ; 2.4. Advérbios de Frequência ; 2.5. Advérbios Interrogativos ; 2.6. Locução Adverbial | Oficial | 7 | **5** | 12 |
| `a02/s04` | Adjetivos, Advérbios, Afixos e Resolução de Provas | Prefixos ; Sufixos ; 4.2. O Sufixo LESS ; Funções Comunicativas do Discurso ; Registro Discursivo ; Pluralidade Cultural | Oficial | 7 | **5** | 12 |
| `a04/s01` | Tempos Verbais (Parte 1) e Resolução de Provas | Presente Simples ; 1.2. Presente Simples na Interrogativa ; 1.3. Presente Simples na Negativa ; Exercícios | Oficial | 9 | **3** | 12 |
| `a04/s02` | Tempos Verbais (Parte 1) e Resolução de Provas | Passado Simples ; 2.2. Verbos Irregulares ; 2.3. O Passado Simples na Interrogativa ; 2.4. O Passado Simples na Negativa ; Exercícios | Oficial | 8 | **4** | 12 |
| `a04/s03` | Tempos Verbais (Parte 1) e Resolução de Provas | Futuro Simples e com o GOING TO ; 3. 6. Para falar sobre acontecimentos sobre os quais não se tem certeza ; 3.8. Futuro na Negativa com WILL ; 3.10. Com o GOING TO ; 3... | Oficial | 8 | **4** | 12 |
| `a05/s01` | Tempos Verbais (Parte 2) e Resolução Provas | Presente, Passado e Futuro Contínuo ; 1.2. Passado Contínuo ; 1.3. Futuro Contínuo | Oficial | 7 | **4** | 11 |
| `a05/s02` | Tempos Verbais (Parte 2) e Resolução Provas | Present Perfect ; 2.1. Forma Negativa ; 2.2. Forma Interrogativa ; 2.3. Exercício ; Past e Future Perfect, Futuro Perfeito Contínuo ; 3.2. Futuro Perfeito | Oficial | 7 | **5** | 12 |
| `a05/s03` | Tempos Verbais (Parte 2) e Resolução Provas | Voz Ativa e Voz Passiva ; 4.1. Voz Passiva com o Presente Simples (Present simple) ; 4.3. Voz Passiva com o Futuro Simples (Future) ; 4.6. Voz Passiva com o Presente P... | Oficial | 7 | **5** | 12 |
| `a05/s04` | Tempos Verbais (Parte 2) e Resolução Provas | Imperativo ; 5.2. Imperativo Negativo ; Subjuntivo | Oficial | 7 | **4** | 11 |
| `a06/s01` | Expressões (Idioms) e Resolução de Provas | Expressões Idiomáticas ; Discurso Direto e Indireto ; EXERCÍCIOS | Oficial | 9 | **3** | 12 |
| `a06/s02` | Expressões (Idioms) e Resolução de Provas | Numerais ; 5.2. Os Números Ordinais ; Quantificadores e Determinantes ; 4.2. Os Quantificadores/Determinantes Both (ambos), Neither (nenhum de dois) e Either (um de do... | Oficial | 8 | **4** | 12 |
| `a06/s03` | Expressões (Idioms) e Resolução de Provas | Question Tags e Respostas Curtas ; Wh-questions ; Infinitivo e Gerúndio ; Estrutura da Oração: Período Composto ; 10.4. Oração Condicional tipo 2 ; 10.7. Orações Relat... | Oficial | 8 | **4** | 12 |
| | | | | | **82** | |

### 6.6. Direitos Humanos: 81 questões

Arquivo de destino: `content/questoes/ineditas/mc/direitos-humanos.txt` · matéria `direitos-humanos`

**Concurso beneficiado:** CFOA (5 questões na prova; 7 cadernos do ciclo mínimo; só 45 questões da AOCP e 175 inéditas).

**Fontes:** Constituição Federal (art. 4º, II; art. 5º, §§ 2º, 3º e 4º; EC 45/2004), Declaração Universal dos Direitos Humanos (ONU, 1948), PNDH-3 (Decreto 7.037/2009), CEDAW (Decreto 4.377/2002), Convenção sobre os Direitos das Pessoas com Deficiência (Decreto 6.949/2009, com status de emenda constitucional), Comissão Nacional da Verdade (Lei 12.528/2011). Confira com `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <artigo>` (`cf`, `d7037`, `d4377`, `d6949`); resumos e material em `content/summaries/direitos-humanos/` e `content/material/direitos-humanos/`.

**Cuidados:**
- Gerações (dimensões) dos direitos, natureza jurídica da DUDH (declaração, não tratado), incorporação de tratados (quórum do art. 5º, § 3º, supralegalidade, Tribunal Penal Internacional) são os pontos que mais caem: varie entre conceito, comparação e situação concreta.
- Trechos mais fracos: `a05/s03` (9), `a05/s01` e `s02` (12), `a04/s02` (12), `a00/s02` (12), `a02/s03`, `a04/s01` e `a02/s01` (15 a 17).
- Não cite número de artigo da DUDH sem conferir. Não use opinião: só o texto normativo e a doutrina majoritária.

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a00/s01` | Teoria Geral dos Direitos Humanos: Conceito, Classificação,  | Teoria Geral dos Direitos Humanos: Conceito, Terminologia e Classificação ; 2 – Classificação dos Direitos Humanos ; 2.2 - Classificação do Caso Lüth ; 2.3 - Estrutura... | CFOA | 19 | **3** | 22 |
| `a00/s02` | Teoria Geral dos Direitos Humanos: Conceito, Classificação,  | Fundamentos, Estrutura Normativa e Pós-Positivismo nos Direitos Humanos ; 3.2 - Fundamentos ; 4 – Estrutura Normativa ; 5 – Pós-positivismo e os Direitos Humanos | CFOA | 12 | **10** | 22 |
| `a02/s01` | Declaração Universal dos Direitos Humanos (ONU, 1948) | Declaração Universal dos Direitos Humanos: Introdução, Natureza Jurídica e Preâmbulo ; 2 - Direitos albergados ; 3 - Natureza jurídica ; 4 - Estrutura ; 5.1 - Preâmbulo | CFOA | 17 | **5** | 22 |
| `a02/s03` | Declaração Universal dos Direitos Humanos (ONU, 1948) | Direitos Econômicos, Sociais e Culturais e Disposições Finais da DUDH (arts. 22 a 30) ; 5.14 - Direitos trabalhistas ; 5.15 - Direitos Sociais ; 5.16 - Disposições Finais | CFOA | 15 | **7** | 22 |
| `a04/s01` | Política e Programas Nacionais de Direitos Humanos (PNDH) | Política e Programas Nacionais de Direitos Humanos (PNDH I, II e III) ; 2.1 - Eixo Orientador | CFOA | 15 | **7** | 22 |
| `a04/s02` | Política e Programas Nacionais de Direitos Humanos (PNDH) | Diretrizes, Objetivos Estratégicos do PNDH-3 e Comissão Nacional da Verdade ; 2.3 - Objetivos Estratégicos ; 2.4 - Ações Programáticas | CFOA | 12 | **10** | 22 |
| `a05/s01` | A Legislação e os Direitos Humanos na Constituição e no Bras | Histórico dos Direitos Humanos nas Constituições e na Legislação Brasileira ; 1 - Direitos Humanos e as Constituições Anteriores ; 2 - Direitos Humanos e a Legislação ... | CFOA | 9 | **14** | 23 |
| `a05/s02` | A Legislação e os Direitos Humanos na Constituição e no Bras | Direitos Humanos na Constituição de 1988: Princípios, Tratados e IDC ; 1.4 - Prevalência dos Direitos Humanos como princípio regente das relações internacionais ; 2 - ... | CFOA | 12 | **11** | 23 |
| `a05/s03` | A Legislação e os Direitos Humanos na Constituição e no Bras | Teoria Geral dos Direitos Fundamentais: Conceito, Garantias e Características ; 2 - Direitos Fundamentais versus Garantias Fundamentais ; 3 - Fundamentos ; 4 - Classif... | CFOA | 8 | **14** | 22 |
| | | | | | **81** | |

### 6.7. Legislação Estadual do PCPE: 49 questões

Arquivo de destino: `content/questoes/ineditas/mc/legislacao-pcpe.txt` · matéria `legislacao-pcpe`

**Concurso beneficiado:** PCPE Agente de Polícia (4 questões na prova; 191 hoje, quase todas inéditas).

**Normas:** Lei Complementar Estadual 137/2008 (`a01`), LC 317/2015 (`a02`), Lei 6.425/1972, Estatuto do Policial Civil (`a03`, `a04`), Lei 6.123/1968, Estatuto do Servidor do Estado (`a05` a `a07`) e Constituição do Estado de Pernambuco, segurança pública (`c01`). Normas no cache de `leis.py`: `pelc137`, `pelc317`, `pe6425`, `pe6123`. Confirme o resto no site da ALEPE e, sem confirmação, **não cite o número do artigo**.

**Formato:** a prova do PCPE é Cebraspe, mas o banco usa múltipla escolha A–E nas inéditas (como em `mc/legislacao-pcpe.txt`): enunciado com a situação ou a regra e **alternativas que são afirmações completas** (estilo "julgue... assinale"), uma só correta. Leia o que existe em `mc/legislacao-pcpe.txt` (102 questões) e **cubra artigos novos**.

**Cuidados:** prazos, penalidades e competências do regime disciplinar do policial civil (Lei 6.425/1972) não se confundem com os do servidor comum (Lei 6.123/1968): use distratores que trocam um pelo outro. Trechos mais fracos: `a05/s02`, `a06/s01`, `a07/s01` e `a07/s02` (8 a 9 hoje).

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a03/s01` | Lei nº 6.425/1972 - Estatuto do Policial Civil de P | Sumário e Apresentação: Lei nº 6.425/1972 | PCPE | 15 | **2** | 17 |
| `a03/s02` | Lei nº 6.425/1972 - Estatuto do Policial Civil de P | Regime jurídico e Da Nomeação | PCPE | 16 | **2** | 18 |
| `a04/s01` | Lei nº 6.425/1972 - Estatuto do Policial Civil de P | Regime Disciplinar e Transgressões ; Das Transgressões Disciplinares ; Das Penas Disciplinares | PCPE | 15 | **3** | 18 |
| `a04/s02` | Lei nº 6.425/1972 - Estatuto do Policial Civil de P | Das Penas Disciplinares e Processo ; Do Inquérito E Da Sindicância Disciplinar ; Da Medalha Do Mérito Pessoal ; Do Conselho Superior De Polícia ; Das Disposições Finais | PCPE | 15 | **3** | 18 |
| `a05/s01` | Lei nº 6.123/1968 - Estatuto do Servidor do Estado de Pernam | Apresentação do Curso: Lei Estadual nº 6.123/1968 ; Das disposições preliminares ; Do provimento ; Da posse ; Do exercício | PCPE | 14 | **3** | 17 |
| `a05/s02` | Lei nº 6.123/1968 - Estatuto do Servidor do Estado de Pernam | Da remoção, estágio probatório e promoção ; Da reintegração ; Da reversão ; Da vacância | PCPE | 9 | **8** | 17 |
| `a06/s01` | Lei nº 6.123/1968 - Estatuto do Servidor do Estado de Pernam | Direitos, Vencimentos e Vantagens ; Das licenças ; Do vencimento ; Das concessões ; Do direito de petição | PCPE | 8 | **10** | 18 |
| `a07/s01` | Lei nº 6.123/1968 - Estatuto do Servidor do Estado de Pernam | Apresentação e Estatuto dos Servidores: Regime disciplinar ; Da acumulação ; Dos deveres ; Das proibições ; Da responsabilidade ; Das penalidades | PCPE | 8 | **9** | 17 |
| `a07/s02` | Lei nº 6.123/1968 - Estatuto do Servidor do Estado de Pernam | Penalidades Disciplinares e Processo ; Do processo administrativo e sua revisão | PCPE | 8 | **9** | 17 |
| | | | | | **49** | |

### 6.8. Língua Espanhola: 15 questões

Arquivo de destino: `content/questoes/ineditas/mc/lingua-espanhola.txt` · matéria `lingua-espanhola`

**Concurso beneficiado:** CBMPE Oficial (opção do candidato; já cumpre 96% da meta, 15 questões a escrever).

Escreva a questão em espanhol (texto, frase ou item gramatical autorais) com comando em português, no padrão AOCP. Confira gramática e vocabulário na RAE/DPD e nos dicionários (Real Academia, Cervantes). Os trechos com 7 questões são os que recebem a nova: substantivos, verbos, silabeo e sinonímia, marcadores temporais, interpretação. Leia `mc/lingua-espanhola.txt` e **não repita** o tópico nem o texto-base. Prefira pontos ainda pouco cobertos (heterosemánticos, heterogenéricos, perífrasis verbales).

| Trecho (`aula/trecho`) | Assunto | Tópicos | Concursos | Tem hoje | **Escrever** | Alvo |
|---|---|---|---|---:|---:|---:|
| `a06/s01` | Substantivos | Palavras iniciais ; Substantivos ; Gênero dos substantivos | Oficial | 7 | **1** | 8 |
| `a06/s02` | Substantivos | Substantivos invariáveis ; Substantivos epicenos ; Substantivos bigêneros ; Substantivos que parecem femininos ; Substantivos "heterogenéricos" ; Número dos substantivos | Oficial | 7 | **1** | 8 |
| `a06/s03` | Substantivos | Substantivos mais comuns ; Comercio y servicios (comércio e serviços) ; Medios de transporte (meios de transporte) ; Família ; Cores ; Profesiones en español (profissõ... | Oficial | 7 | **1** | 8 |
| `a06/s04` | Substantivos | Frutas en español (frutas em espanhol) ; Las verduras y legumbres (verduras e legumes) ; Utensilios de cocina y mesa (utensílios de cozinha e mesa) ; Turismo y viajes ... | Oficial | 7 | **1** | 8 |
| `a09/s01` | Verbos | Palavras iniciais ; Verbos ; Verbo: conjugação (verbos regulares e irregulares) ; Verbos regulares ; Verbos irregulares ; Infinitivo | Oficial | 7 | **1** | 8 |
| `a09/s02` | Verbos | Verbo: formas pessoais ; Números do verbo ; Pessoas do verbo ; Modo Imperativo ; Tempos do verbo ; Tempos imperfeitos | Oficial | 7 | **1** | 8 |
| `a09/s04` | Verbos | Presente de subjuntivo ; Imperativo | Oficial | 7 | **1** | 8 |
| `a09/s05` | Verbos | Desinências ; Desinências verbais ; Desinências verbais na língua espanhola e tradução livre | Oficial | 7 | **1** | 8 |
| `a09/s06` | Verbos | Verbo Composto ; Verbos compostos, como traduzir? ; Verbo: perífrasis verbales ; Verbo: forma passiva ; Formação da voz passiva ; Verbos e tradução livre | Oficial | 7 | **1** | 8 |
| `a11/s01` | Interpretação de textos | Palavras iniciais ; Interpretação de Textos ; Frase ; Frase exclamativa ; Oração ; Período | Oficial | 7 | **1** | 8 |
| `a11/s02` | Interpretação de textos | Descrição ; Dissertação ; Injunção instrucional ; Narração ; Textos no estilo direto e no estilo indireto ; Interpretação de textos ‘versus’ prova de espanhol | Oficial | 7 | **1** | 8 |
| `a13/s01` | Silabeo, sinonimia, antonimia e heterosemánticos | Palavras iniciais ; Silabeo ; Silabeo: uma consoante entre duas vogais ; Silabeo: duas consoantes entre duas vogais ; Silabeo: três consoantes entre duas vogais ; Sila... | Oficial | 7 | **1** | 8 |
| `a13/s03` | Silabeo, sinonimia, antonimia e heterosemánticos | Divergências Léxicas ; Heterotônicos ; Heterosemânticos ; Heterogenéricos | Oficial | 7 | **1** | 8 |
| `a13/s04` | Silabeo, sinonimia, antonimia e heterosemánticos | Falsos Cognatos | Oficial | 7 | **1** | 8 |
| `a13/s05` | Silabeo, sinonimia, antonimia e heterosemánticos | Marcadores Temporais ; Marcadores temporais e tempos verbais ; “Desde” versus “hace” versus “desde hace” | Oficial | 7 | **1** | 8 |
| | | | | | **15** | |

## 7. Checklist final (por lote)

- [ ] Quantidade por trecho igual à da tabela (ou justificada no relatório).
- [ ] `ineditas_mc_nativas.py --check` com `erros 0` e `lacunas_balanco.py` sem trecho pendente.
- [ ] Cada comentário com 40 a 110 palavras, sem citar letras, com artigos conferidos.
- [ ] Gabarito indiscutível e **uma só** alternativa correta em cada questão; alternativas de tamanho parecido.
- [ ] Nenhuma questão datada (Atualidades), nenhum fato inventado, nenhuma frase copiada.
- [ ] Nenhum `git`, banco, `--remoto` ou edição manual dos `.txt`.
- [ ] `REVISAO-2026-11-20-balanco-<seu-nome>.md` escrito.
