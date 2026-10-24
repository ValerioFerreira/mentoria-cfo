# Briefing: revisão por amostra do conteúdo do 2º Tenente CFOA CBMPE (inéditas, resumos e bizus)

Você é um **revisor independente**: não escreveu nada do que vai conferir. O conteúdo foi produzido por outro agente em
24/10/2026 e já está no repositório e no banco **local**. Sua tarefa é **auditar por amostra, corrigir o que estiver
errado e medir a taxa de erro**, para o dono decidir se o restante pode ir à produção como está. Um erro de gabarito,
de norma desatualizada ou de resumo impreciso prejudica o aluno, e ele não percebe. Trabalhe com o rigor que você exigiria
de um professor titular de concurso público: **não confie no texto que está revisando; confirme na fonte oficial.**

## 1. Contexto

- Projeto **MentorIA / CFO-BM** (`C:\Users\Administrador\Documents\Projetos\CFO-BM`). Leia antes `CLAUDE.md` (convenções) e a
  seção 13 de `HISTORICO.md` e `pipeline/briefs/cfoa-inclusao.md` (como o CFOA foi incluído).
- Concurso: **2º Tenente CFOA CBMPE** (seleção interna de oficiais do Quadro de Administração do CBMPE; 100 questões; edital
  base 2023; sem data e sem banca definida; banca genérica AOCP, múltipla escolha com 5 alternativas A–E). O edital está em
  `content/edital/cfoa/` e o mapa edital → material em `content/edital/<disciplina>.json`.
- Disciplinas (9): Língua Portuguesa, Raciocínio Lógico, Direito Constitucional, Direito Administrativo, Legislações PE,
  Direito Penal Militar, **Administração**, **Direitos Humanos**, **Direito Processual Penal Militar** (as três últimas são
  novas no sistema e são as de **maior risco**: nada foi conferido por humano nelas).
- O que foi produzido e deve ser auditado:
  1. **1.333 questões inéditas de múltipla escolha** (provisórias até entrarem as reais do TecConcursos).
  2. **Resumos analíticos e sintéticos** (`content/summaries/<disciplina>/<aula>.json`) das aulas novas do CFOA.
  3. **Bizus** (`content/items/<disciplina>/<aula>.json`) das mesmas aulas.
  4. **7 complementos** autorais (`content/complements/*.md`: `adm-cfoa-lacunas`, `dppm-cfoa-lacunas`, `dh-*`/
     `dh-cedaw`/`dh-convencao-pcd`, `leg-lei-12527-lai`, `leg-pe-lei-13314-assedio`, `leg-pe-lei-6783-lacunas`,
     `dpm-crimes-licitacoes`).
- O autor trabalhou a partir dos PDFs do curso (`docs/`, protegidos) e dos resumos. **Os resumos podem conter erros**; por isso
  a conferência é sempre **contra a fonte oficial**, nunca contra o resumo.

## 2. Regras que não podem ser quebradas

- **Não grave em banco algum** (nem local, nem Neon). Não use `--remoto`. Não rode `prisma migrate`, seed ou importadores.
  Você só edita arquivos de texto e roda validadores.
- **Nunca copie texto de `docs/`** (material protegido com marca d'água do aluno) para qualquer arquivo versionado. Pode lê-lo
  para entender e conferir, mas escreva com as suas palavras. Citar norma oficial literal e curta é permitido (lei é domínio
  público).
- Não imprima nem altere arquivos `.env*`. Idioma: pt-BR.
- Não mencione o curso/material-base ("conforme a aula", "o curso", nomes de professor) em nada que o aluno vê.
- Não corrija estrutura (`content/structure`, `segments`, `overrides`): se achar problema de segmentação, **anote**, não mexa.
- **Não faça commit nem push.** Deixe as alterações na árvore de trabalho; o dono (ou a sessão principal) decide. Há mudanças
  de outros agentes na árvore: **não use `git add -A`, `git checkout`, `git stash` nem `git reset`**.
- Não invente fonte. Se não conseguir confirmar uma afirmação em fonte oficial, **não a mantenha como fato**: reescreva sem
  o detalhe duvidoso ou registre como "não confirmado".

## 3. Fontes aceitas

Somente fontes oficiais: textos legais no Planalto (`planalto.gov.br/ccivil_03`), Constituição Federal, Constituição do Estado
de Pernambuco e leis/decretos estaduais no portal da ALEPE e da legislação estadual (`legislacao.pe.gov.br`), súmulas e teses
nos sites do STF, STJ e STM, tratados no Planalto e no portal de direitos humanos do governo/ONU/OEA, Manual de Redação da
Presidência. Para Administração, use os autores consagrados citados no próprio material (Chiavenato, Maximiano, Robbins,
Mintzberg, Taylor, Fayol, Weber, Lewin, Schein, Katz, etc.) e a Lei 8.112/90, a Lei 14.133/21 e as normas de gestão pública
quando o item for normativo. Blogs, sites de cursinho e resumos de terceiros **não** servem de prova. Use a ferramenta de busca
na web e leitura de páginas para conferir; registre a URL de cada conferência relevante.

## 4. Onde está cada coisa

| O quê | Onde |
|---|---|
| Inéditas de múltipla escolha (fonte editável) | `content/questoes/ineditas/mc/<disciplina>.txt` |
| Só as questões **do CFOA** (nos arquivos compartilhados há também as do CBMPE) | `git show f0b5310 -- content/questoes/ineditas/mc/<disciplina>.txt` (as linhas `+` são as do CFOA; em `administracao`, `direitos-humanos` e `direito-processual-penal-militar` o arquivo inteiro é do CFOA) |
| Quais trechos são do CFOA e quantas questões cada um tem | `pipeline/briefs/ineditas-cfoa-base.json` e `pipeline/.venv/Scripts/python pipeline/questoes/lacunas_cfoa.py` |
| Validador das inéditas | `pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check` |
| Resumos | `content/summaries/<disciplina>/<aula>.json` (campos `analytic` e `synthetic`, por trecho) |
| Bizus | `content/items/<disciplina>/<aula>.json` (`bizu.summary`, `teoria`, `revisao`, ponteiros) |
| Validadores | `pipeline/.venv/Scripts/python pipeline/validate_content.py` e `pipeline/validate_summaries.py` |
| Texto-fonte do trecho (protegido; só para ler) | `pipeline/.venv/Scripts/python pipeline/summary_source.py <disciplina>/aNN/sNN` |
| Mapa de páginas/tópicos de uma aula | `pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disciplina>/aNN` |
| Complementos | `content/complements/*.md` (depois de editar, **não** regenere PDF; avise no relatório) |
| Regras de redação de resumos e bizus | `pipeline/briefs/summary.md`, `pipeline/briefs/bizu.md`, `pipeline/briefs/complement.md` |
| Um briefing parecido (modelo de rigor e de relatório) | `pipeline/briefs/revisao-ineditas.md` |

Formato de cada inédita (o cabeçalho `@@ aula/trecho | LETRA` é o **gabarito**):

```
@@ a01/s02 | C
Enunciado ("..., assinale a opção correta." ou "...INCORRETA.")
A) ...
B) ...
C) ...
D) ...
E) ...
// Comentário: por que a alternativa do gabarito está certa e, resumidamente, por que as outras estão erradas.
```

## 5. Amostragem (obrigatória, sorteada, não "as primeiras")

Use um sorteio reproduzível (por exemplo, `random.seed(20261024)` em um script seu fora do repositório) para evitar viés.

| Material | Amostra mínima | Estratificação |
|---|---|---|
| Inéditas | **15% de cada disciplina, no mínimo 20 por disciplina** (todas as 9), das questões do CFOA | pelo menos 1 questão de cada trecho com mais de 6 questões; nas 3 disciplinas novas, **25%** |
| Resumos | **25% dos trechos** de cada uma das 3 disciplinas novas e 3 trechos das demais | priorize trechos longos e de norma |
| Bizus | **20% dos arquivos de bizu** das 3 disciplinas novas e 1 arquivo por disciplina nas demais | confira as afirmações Certo/Errado (`isTrue`) uma a uma |
| Complementos | **os 7**, leitura integral dos pontos normativos (números, prazos, artigos, penas) | — |

**Regra de escalonamento:** se numa disciplina a amostra tiver **mais de 8% de questões com erro de fato** (gabarito errado,
norma errada/desatualizada, alternativa defensável como correta, comentário contraditório), **dobre a amostra daquela
disciplina**; se persistir acima de 8%, **revise a disciplina inteira** e diga isso no relatório. Erros de forma (estilo,
tamanho de alternativas) não contam para o gatilho, mas devem ser corrigidos.

## 6. O que verificar

### 6.1 Inéditas (uma a uma)

1. **Gabarito.** Resolva a questão sozinho **antes** de olhar a letra do cabeçalho. Só depois compare. Se discordar, descubra
   quem está certo na fonte oficial.
2. **Uma única alternativa correta.** Teste cada uma das outras quatro: existe leitura razoável em que também esteja certa?
   Cuidado com "sempre", "nunca", "somente", "exclusivamente" (só são erradas se a norma não for realmente absoluta), com
   alternativas incompletas que são verdadeiras e com enunciados "INCORRETA/EXCETO" (gabarito é a falsa).
3. **Fato.** Números, prazos, penas, quóruns, percentuais, órgãos competentes, nomes de autores, datas e numeração de
   leis/artigos/súmulas. É o que a banca troca para fazer uma alternativa errada, e o autor pode ter trocado sem querer.
4. **Vigência (outubro de 2026).** Exemplos de normas com alteração recente: Lei 14.133/2021 (valores atualizados por decreto),
   Lei 13.491/2017 e Lei 14.688/2023 no CPM/CPPM, Lei 13.869/2019 (abuso de autoridade), Lei 14.532/2023 (injúria racial),
   EC 103/2019 e EC 132/2023, Lei 13.964/2019 (CPP), Lei 14.230/2021 (improbidade). **Atenção ao específico do CFOA:**
   - **Direito Processual Penal Militar:** Decreto-Lei 1.002/1969 (CPPM), competência da Justiça Militar estadual (art. 125, §§ 3º
     e 4º, CF; EC 45/2004; Lei 13.491/2017), interrogatório ao final da instrução (HC 127.900/AM, STF; confira se vale para o
     CPPM e em que condições), IPM (prazos, encarregado, incomunicabilidade), prisão em flagrante e preventiva militar, menagem,
     deserção e insubmissão (processo especial), recursos, habeas corpus.
   - **Direitos Humanos:** DUDH, PNDH-3 (Decreto 7.037/2009, alterado pelo 7.177/2010), CEDAW (Decreto 4.377/2002), Convenção
     sobre os Direitos das Pessoas com Deficiência (Decreto 6.949/2009; art. 5º, § 3º, CF), Pacto de São José (Decreto 678/1992)
     e Sistema Interamericano, Regras de Mandela e uso da força (Princípios Básicos da ONU de 1990, Código de Conduta de 1979),
     Lei 9.455/1997 (tortura), Lei 13.869/2019. Confirme **ano, órgão e natureza** (tratado, resolução, soft law) de cada texto.
   - **Administração:** correção conceitual (escolas, autores e teorias atribuídos ao autor certo; conceitos de eficiência,
     eficácia, efetividade; funções PODC/PO3C; tipos de estrutura; liderança e motivação com o autor correto de cada teoria;
     gestão pública e qualidade no serviço público: Programa GESPÚBLICA e Decreto 5.378/2005 quando citados).
   - **Legislações PE:** Lei Estadual 6.783/1974, Lei 11.817/2000, Lei 13.314/2007, LC 470/2023 (confira a numeração), Decreto
     50.014/2020, Lei 15.187/2013, Lei 14.751/2023, LAI (Lei 12.527/2011).
5. **Qualidade de prova.** 5 alternativas A–E; enunciado completo e autossuficiente; sem pistas gramaticais; alternativa
   correta **não** muito mais longa que as demais (o validador avisa quando passa de 35% das questões); gabaritos equilibrados;
   sem alternativas "todas as anteriores"/"nenhuma das anteriores" (a banca AOCP evita); sem referência ao material-base.
6. **Comentário.** Cita o fundamento (dispositivo, autor, tese), explica por que a correta está certa e, resumidamente, por que
   as outras estão erradas, e **não contradiz** o gabarito nem o enunciado.
7. **Aderência.** A questão pertence ao trecho indicado em `@@ aula/trecho` e ao assunto do edital? Se não, aponte o trecho
   correto (`inspect_aula.py`), mas **só troque o cabeçalho se o trecho de destino existir** em `content/segments/`.
8. **Duplicatas.** Mesmo enunciado/alternativas repetidos (inclusive quase iguais) dentro do trecho ou da disciplina.

### 6.2 Resumos

Para cada trecho amostrado, leia o resumo **ao lado do texto-fonte** (`summary_source.py`) e confira:
- **Exatidão:** nenhuma afirmação falsa, imprecisa ou desatualizada; números/prazos/artigos corretos. Resumo que "arredonda"
  uma regra e a torna errada é erro grave.
- **Cobertura:** todo conceito cobrável do trecho está presente? Use `pipeline/.venv/Scripts/python pipeline/summary_coverage.py`
  (triagem; não detecta conceito errado) e leia a lista de termos que faltam.
- **Originalidade:** sem trechos copiados do material; o validador (`validate_summaries.py`) deve continuar passando.
- **Estrutura:** seções, `### Para fixar` com 5 a 8 itens em lista, tamanho (alvo ≈ 20 min de leitura, ~100 palavras/min).
- **Impressão digital** (`startPage`, `endPage`, `startTopic`) intacta: **não altere** esses campos.
- Pistas de "alucinação": nomes de autores, datas, números de artigo e de decreto que não aparecem no texto-fonte.

### 6.3 Bizus

- `bizu.summary`: 6 a 12 pontos com conteúdo, **negrito** como única marcação; sem itálico, crase ou lista.
- `teoria`/`revisao` (itens Certo/Errado): o `isTrue` está correto? A explicação confirma? A assertiva é de fato falsa quando
  `isTrue=false` e **falsa por um motivo verificável** (não por redação ambígua)? Há equilíbrio entre certos e errados?
- Nenhuma cópia literal do material (≥ 10 palavras iguais); sem questões objetivas dentro de `content/items`.

### 6.4 Complementos

Leia integralmente e confira cada número, prazo, artigo, pena e denominação de órgão contra o texto oficial. O complemento
**substitui** a lacuna do material, então um erro aqui é pior que em outros lugares. Confirme também que a lacuna que ele
declara cobrir (ver `content/gaps.json` / `pipeline/briefs/cfoa-inclusao.md`) foi de fato coberta.

## 7. Como corrigir

- **Inéditas:** edite o `.txt` mantendo o cabeçalho `@@ aula/trecho | LETRA`. Se mudar o gabarito, troque a letra **e**
  reescreva o comentário. Para remover, apague o bloco inteiro; depois confira se o trecho continua com **≥ 7 questões** e a
  aula com **≥ 25** (`lacunas_cfoa.py --check`); se não, escreva outra no mesmo padrão (ou diga no relatório que faltou).
  Mantenha os gabaritos equilibrados (~20% por letra na disciplina): se mudar muitos, reponha trocando a ordem das alternativas
  em outras. Corrija o enunciado quando a falha for ambiguidade, em vez de apagar a questão, se o conteúdo for bom.
- **Resumos/bizus:** edite o JSON preservando a estrutura e os campos de impressão digital. Depois de editar o resumo
  de um trecho, o **bizu sintético** (`bizu.summary`) que o espelha pode precisar do mesmo ajuste: confira os dois. Os espelhos
  em `web/content/` são gerados por `apply_synthetic.py`; **não edite `web/content/` à mão** e anote no relatório quais arquivos
  foram alterados para o dono rodar o espelhamento.
- **Complementos:** edite o `.md`; **não** gere PDF; liste os arquivos alterados no relatório.
- Mudou algo? Rode de novo os validadores relevantes até zerar os erros:
  `ineditas_mc_nativas.py --check`, `lacunas_cfoa.py --check`, `validate_content.py`, `validate_summaries.py`.

## 8. Ordem de trabalho sugerida

1. Rode os quatro validadores e anote a linha de base.
2. Faça o sorteio das amostras (§5) e salve a lista sorteada em um arquivo seu (fora do repositório, p. ex. na pasta temporária).
3. Revise primeiro **Direito Processual Penal Militar → Direitos Humanos → Administração** (disciplinas novas), depois Direito
   Penal Militar, Legislações PE, Direito Administrativo, Direito Constitucional, Língua Portuguesa (confira norma culta e
   Manual de Redação na fonte), Raciocínio Lógico (**refaça as contas à mão**, uma a uma).
4. Aplique a regra de escalonamento (§5) sempre que uma disciplina passar de 8%.
5. Complementos e resumos/bizus.
6. Rode os validadores e o `lacunas_cfoa.py --check` no final.

## 9. Relatório (obrigatório)

Grave em `content/questoes/ineditas/REVISAO-2026-10-24-cfoa-amostral.md` e responda no chat com o resumo.

1. **Tabela por disciplina (inéditas):** `total CFOA | amostra | OK | corrigidas | reescritas | removidas | taxa de erro de fato`.
   Diga se o escalonamento foi acionado e o resultado.
2. **Tabela de cada correção:** `arquivo | nº da questão (ordem no arquivo) ou trecho | tipo (gabarito, fato, vigência, ambiguidade,
   duplicata, aderência, forma) | o que estava errado | correção | fonte oficial (URL)`.
3. **Resumos e bizus:** quantos trechos/arquivos conferidos, erros por tipo e as correções.
4. **Complementos:** veredito por arquivo.
5. **As 10 falhas mais graves** (as que um aluno aprenderia errado).
6. **Parecer de risco por disciplina:** `LIBERAR` (taxa < 3%), `LIBERAR COM RESSALVA` (3–8%) ou `REVISAR TUDO ANTES` (> 8% após
   ampliar a amostra). Seja conservador: na dúvida, o parecer mais restritivo.
7. **Dúvidas que dependem do dono** (norma ambígua, jurisprudência não confirmada, divergência entre fontes) e **problemas de
   estrutura/segmentação** que você notou e não corrigiu.
8. **Arquivos alterados** (lista completa) e os comandos que o dono precisa rodar depois (por exemplo `apply_synthetic.py`,
   regerar PDFs dos complementos, regravar o lote de inéditas no banco **local**).

Seja honesto sobre o que não conseguiu confirmar: um "não confirmado" registrado vale mais que uma correção chutada.
