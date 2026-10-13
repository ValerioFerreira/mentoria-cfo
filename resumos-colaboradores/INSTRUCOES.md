# Instruções para escrever os resumos de estudo (MentorIA)

Este documento é **autossuficiente**: com ele, o índice (`INDICE-RESUMOS.xlsx` ou `.csv`) e a pasta de PDFs, você executa a tarefa completa, de qualquer matéria, **sem acesso ao sistema ou ao código**. Leia tudo antes de começar e siga **exatamente** o formato de entrega (seções 11 e 12): é por ele que seus resumos serão importados e auditados.

---

## 1. A tarefa em uma frase
Para cada **atividade de Teoria** indicada no seu intervalo do índice (ex.: "do ID S0101 ao S0120"), ler o trecho do PDF e escrever **dois textos novos, com as suas palavras**:

| Texto | O que é | Tamanho |
| --- | --- | --- |
| **Resumo analítico** | Substitui a leitura do material quando o aluno estiver sem tempo (ou preferir ler um resumo). Deve ser **suficiente por si só** para o aluno responder questões de prova sobre o assunto. | ≈ 20 min de leitura no máximo (≈ 100 palavras/min de estudo). **O tamanho é o que o conteúdo pedir**: o limite superior está na coluna "Alvo máx. (palavras)" do índice; o piso é o maior entre 250 palavras e 20% do alvo do índice. Nunca encha para chegar ao alvo. |
| **Resumo sintético** | Fica na seção "Bizu", que acompanha toda atividade de Teoria: os pontos-chave **com uma explicação breve e com conteúdo** (regra, exceção, número, fórmula). | 6 a 12 pontos; 110 a 320 palavras no total. |

Cada atividade = **um arquivo** de saída. Não junte atividades num mesmo arquivo.

## 2. O que você recebe e o que não tem
- **Pasta de PDFs** do material (um PDF por aula) e, para os "Complementos", um PDF curto do MentorIA.
- **INDICE-RESUMOS.xlsx / .csv**: uma linha por atividade (ver seção 3).
- **Este documento** e o script opcional `verificar_resumos.py` (autoverificação, seção 13).
- Você **não** tem acesso ao sistema, ao banco nem ao código. Trabalhe só com os arquivos recebidos. Se algo estiver ilegível ou faltando, registre em NOTAS (seção 9) e siga em frente.

## 3. O índice
Colunas do `INDICE-RESUMOS`:

| Coluna | Uso |
| --- | --- |
| **ID** | `S0001`, `S0002`… Identifica a atividade e dá nome ao seu arquivo de saída. Os IDs seguem a ordem de prioridade do produto. |
| **Matéria / Aula / Trecho** | Onde a atividade fica no material. "Trecho" (`disciplina/aNN/sNN`) é o código interno: copie-o no cabeçalho do arquivo. |
| **Atividade (assuntos do trecho)** | Os assuntos que o trecho cobre. Use como roteiro: todos precisam aparecer no resumo. |
| **Arquivo PDF do material** | Qual PDF abrir. |
| **Pág. inicial / Pág. final** | Leia **somente** esse intervalo (numeração do PDF, não a impressa). |
| **Alvo máx. (palavras)** | Teto de tamanho do resumo analítico (≈ 20 min). |
| **Lote / Sublote** | `Lote` (1 a 6, F2-A, F2-B) é a sua fatia do trabalho; `Sublote` (ex.: `L3-02`) é cada grupo de ~20 atividades, na ordem de prioridade. Vazio nas linhas já feitas. |
| **Status** | "A fazer" ou "Feito (já entregue)". Pule os já feitos. |

Você receberá uma instrução do tipo **"execute o Sublote L3-02"** (filtre a coluna **Sublote** do índice: são ~20 atividades) ou **"execute o Lote 3"** (todas as linhas da coluna **Lote**, um sublote por vez, na ordem). Também vale **"do ID Sxxxx ao Syyyy"**. Em todos os casos: faça as linhas com status "A fazer", **na ordem dos IDs** (é a ordem de prioridade; não pule para as mais fáceis) e **entregue por sublote**, sem esperar o lote inteiro (seção 12).

## 4. Passo a passo de cada atividade
1. **Localize** o PDF e o intervalo de páginas pela linha do índice.
2. **Leia o trecho INTEIRO**, do início ao fim, antes de escrever uma linha. Conheça só o que o trecho ensina (não traga assunto de outras aulas).
3. **Liste mentalmente o que a banca cobra**: conceitos-chave, classificações, regras e exceções, prazos e números, fórmulas e condições de validade, literalidade de artigos curtos e essenciais, comparações, "pegadinhas", mnemônicos.
4. **Escreva o resumo analítico** (seção 5), **depois o sintético** (seção 7), sem copiar frases do material (seção 8).
5. **Releia como aluno** (entendi? dá para resolver uma questão com isto?) **e como banca** (algo cobrável ficou de fora? algum erro?). Corrija.
6. **Salve o arquivo IMEDIATAMENTE**, no formato da seção 11, com o seu identificador (seção 10): um arquivo por atividade, gravado assim que ela estiver pronta e conferida. **Nunca acumule vários resumos para salvar no fim**; se a sessão cair, o que já foi salvo não se perde, e na retomada você pula os IDs que já têm arquivo.
7. Passe para a próxima. Ao fim de cada sublote, monte a entrega daquele sublote (seção 12).

## 5. Como escrever o resumo analítico
### Estrutura (markdown)
- **Abertura**: 1–2 frases dizendo o que o trecho cobre.
- **Seções** `### Título`, na **ordem didática do trecho** (mínimo 3 seções quando o trecho tiver 5+ páginas). Subseções com `####`.
- **Listas** (`- `) para enumerações; **negrito** (`**termo**`) para termos e regras-chave; *itálico* só para latim/estrangeirismo.
- **Tabelas markdown** para comparações e classificações (com a linha separadora `| --- | --- |`; todas as linhas com o mesmo número de colunas; **uma tabela por assunto**, linhas de tabela nunca soltas no meio de listas).
- **Blocos de destaque** quando ajudarem (cada um em uma linha começando por `> `): `> 💡 **Exemplo:** …`, `> ⚖️ **Base normativa:** …`, `> ⚠️ **Pegadinha:** …`.
- **Fechamento**: `### Para fixar` com 5 a 8 pontos de revisão rápida.

### Conteúdo
- **Explique, não liste**: diga o porquê, dê um exemplo curto, destaque a exceção. Um resumo que só enumera tópicos é recusado.
- Seja **completo no que é cobrável** e **enxuto no resto** (história do instituto, curiosidades e repetições podem ser cortadas).
- **Fórmulas, unidades e símbolos** em texto simples (`v = v0 + a·t`, `Q = m·c·ΔT`, `x² − 5x + 6 = 0`). **Sem LaTeX.** Resolva um exemplo curto quando o trecho ensina um método de cálculo.
- **Números, prazos, percentuais, quóruns e artigos** devem estar **exatamente corretos**. Cite o artigo (`art. 5º, XI`) quando o assunto for lei.
- Lei seca: **parafraseie**; copie literalmente apenas dispositivo curto e essencial (e, mesmo assim, prefira a paráfrase).

### Guia por tipo de matéria
- **Jurídicas** (Constitucional, Administrativo, Penal Militar, Legislações PE): conceito → fundamento (artigo) → requisitos/classificações → exceções → jurisprudência/súmulas citadas no trecho → pegadinhas. Destaque verbos e palavras que mudam o sentido ("exclusivamente", "salvo", "ressalvado").
- **Língua Portuguesa**: regra → exemplo próprio → exceção. Em ortografia/acentuação/concordância/regência/crase, monte quadros "regra × exemplo × exceção". Os exemplos devem ser **seus**, não os do material.
- **Língua Inglesa / Espanhola**: explique em português, com exemplos **no idioma** (traduzidos). Tabelas de estruturas, falsos cognatos e conectores são bem-vindas.
- **Exatas** (Matemática, Estatística, Física, Química, Raciocínio Lógico): definição → fórmula → condições de uso → exemplo resolvido curto → erros comuns. Em Química, destaque reações, nomenclatura e propriedades que se repetem em prova.
- **Biologia**: processo → etapas na ordem → estruturas/funções → comparações em tabela.
- **Informática**: conceito → função → atalhos e caminhos de menu (listas curtas) → diferenças entre ferramentas/versões em tabela → pegadinhas de nomenclatura.
- **Atualidades / História de Pernambuco**: fatos com data, personagens, causas e consequências; cronologia em lista; datas e nomes exatos.
- **Complementos** (linhas "Complemento NN"): são materiais curtos do MentorIA; resuma o complemento **inteiro** e preserve a precisão dos artigos.

## 6. Tabelas e figuras do material
O texto extraído dos PDFs costuma perder ou embaralhar tabelas e figuras. Regras:
- **Figuras** (desenhos, esquemas, gráficos, charges, fotos): em geral são só **ilustração do que o texto já explicou** — **descarte**. Só aproveite uma figura se o texto disser que ela é a **fonte** da informação **e** não descrever o conteúdo logo depois dela; nesse caso, reconstrua a informação **em texto** (não escreva "veja a figura").
- **Tabelas**: costumam repetir o que o texto diz. Como são dados escritos, **avalie**: se trazem informação relevante que **não** está no texto (classificações, prazos, quadros comparativos, listas de atalhos, fórmulas), **extraia-a** para o resumo (tabela markdown ou lista); se só repetem, **ignore**.
- Se uma página estiver **vazia, ilegível ou truncada**, resuma o que for legível, **não invente** o que faltou e registre a página em NOTAS.

## 7. Como escrever o resumo sintético
- 6 a 12 pontos, cada um em uma linha: `- **Ponto-chave**: explicação com o conteúdo (regra + exceção/número/exemplo).`
- Cubra o trecho de ponta a ponta, na ordem do trecho. Pode haver 1–2 cabeçalhos `### …` (não contam como ponto).
- **Proibido**: pontos sem explicação ("Princípios"), frases genéricas ("priorize a fixação dos conceitos fundamentais"), tabelas-modelo vazias, "Aspecto 1".
- Deve ser **diferente** do analítico: condensado e direto, não parágrafos copiados dele.

## 8. Originalidade (regra inegociável)
O material é protegido (tem marca d'água do aluno). Seus textos precisam ser **autorais**:
- **Nenhuma sequência de 10 palavras iguais** às do material, em lugar nenhum (analítico, sintético, exemplos). Parafraseie, reorganize, troque exemplos.
- **Nunca** copie a marca d'água (nome/CPF) nem nomes de arquivos do aluno.
- **Não cite** "a aula", "o PDF", "o material", "o professor", "o curso", "nesta página", páginas, nomes de plataforma ou de coleção. O resumo precisa servir a quem nunca viu o material.
- Expressões proibidas (o conferidor rejeita): `Aspecto 1`, `Priorize a fixação`, `lorem ipsum`, `TODO`, `[inserir`, `conforme o material`, `de acordo com a aula`, `segundo o professor`, `no PDF`, `Estratégia Concursos`, `nesta aula`, `visto na aula`.

## 9. Fidelidade, dúvidas e problemas do material
- **Não invente.** Se o material estiver errado, ambíguo ou incompleto, siga o texto legal/consenso técnico e **registre em NOTAS** (qual ponto, onde, por quê). O que depender de figura não extraída também vai em NOTAS.
- Informações que você **não conseguiu confirmar** (artigo, número, data) ficam **fora** do resumo e vão para NOTAS, para revisão humana.
- Estilo: português do Brasil, direto, objetivo; 2ª pessoa só quando ajudar. Acentuação correta; arquivo em **UTF-8**; sem o caractere `�`.

## 10. Identificação do agente (obrigatória)
Escolha **um identificador próprio e estável** (sem espaços nem acentos; letras, números, `-` e `_`), por exemplo `GPT-ANA-07` ou `CLAUDE-LOTE3`. Use o **mesmo** em tudo:
- no **nome de cada arquivo**: `S0123__GPT-ANA-07.md` (ID, dois sublinhados, agente);
- no **cabeçalho** de cada arquivo (`agente:`);
- no **nome da pasta de entrega** e no relatório.
É isso que permite auditar a qualidade por agente depois.

## 11. Formato exato de cada arquivo
Um arquivo `.md` (UTF-8) por atividade, nomeado `ID__AGENTE.md`:

```markdown
---
id: S0123
agente: GPT-ANA-07
materia: Direito Constitucional
aula: Aula 05 — Nacionalidade
trecho: direito-constitucional/a05/s01
paginas_lidas: 100-114
---
# ANALÍTICO

Nacionalidade é o vínculo jurídico-político que liga a pessoa a um Estado e a integra ao povo. O trecho cobre as formas de aquisição, os cargos privativos e a perda da nacionalidade.

### Conceitos básicos

Povo não é sinônimo de população: **população** é quem vive no território; **povo** são os nacionais...

| Modo | Fonte | Resultado |
| --- | --- | --- |
| Originária | nascimento | brasileiro nato |
| Derivada | ato de vontade (naturalização) | brasileiro naturalizado |

> ⚠️ **Pegadinha:** a ...

### Para fixar
- ...

# SINTÉTICO

- **Nacionalidade × cidadania**: nacionalidade separa nacionais de estrangeiros; cidadania é o gozo dos direitos políticos...
- **Natos (art. 12, I)**: ...

# NOTAS

nenhuma
```

Regras do formato:
- O cabeçalho `---` … `---` traz **exatamente** as chaves `id`, `agente`, `materia`, `aula`, `trecho`, `paginas_lidas` (copie `materia`, `aula` e `trecho` do índice).
- As três seções se chamam **`# ANALÍTICO`**, **`# SINTÉTICO`** e **`# NOTAS`**, nessa ordem, cada uma na sua linha, com `#` de **nível 1** (dentro do analítico use só `###` e `####`).
- Em NOTAS escreva `nenhuma` ou a lista de problemas/dúvidas. Não deixe vazio.
- Não use HTML, imagens, links, notas de rodapé nem blocos de código.

## 12. Como devolver o trabalho
A entrega é **por sublote** (a cada ~20 atividades), não só no fim do lote.
1. Crie uma pasta chamada **`resumos_AGENTE_SUBLOTE`** (ex.: `resumos_GPT-ANA-07_L3-02`; se o intervalo veio por IDs, `resumos_GPT-ANA-07_S0101-S0120`).
2. Coloque nela **todos** os arquivos `ID__AGENTE.md` daquele sublote (e **só** eles + o relatório).
3. Inclua `RELATORIO_AGENTE.md` com: sublote/intervalo recebido; lista dos IDs entregues; IDs **não** feitos (e o motivo); problemas do material por ID (resumo do que está em NOTAS); contagem de palavras do analítico de cada ID (mín./média/máx.).
4. Rode a autoverificação (seção 13) e corrija os erros.
5. Compacte a pasta (`.zip`) e entregue; siga para o próximo sublote.
Não renomeie arquivos depois de entregues, não junte resumos e não altere o índice. Se o intervalo ficar incompleto (limite de sessão, material ilegível), entregue o que está pronto e liste o restante no relatório.

## 13. Autoverificação
Checklist por arquivo — todos devem ser "sim":
- [ ] Nome `ID__AGENTE.md`, cabeçalho com as 6 chaves, seções `# ANALÍTICO`, `# SINTÉTICO`, `# NOTAS`.
- [ ] Analítico: ≥ o piso (o maior entre 250 palavras e 20% do alvo) e ≤ o alvo máx. do índice; ≥ 3 seções `###` (trechos de 5+ págs.); termina em `### Para fixar`.
- [ ] Todos os assuntos da coluna "Atividade" do índice aparecem.
- [ ] Sintético: 6–12 pontos, 110–320 palavras, cada ponto com explicação.
- [ ] Nenhuma frase copiada do material (nenhuma sequência de 10 palavras iguais); sem expressões proibidas; sem `�`; negritos e tabelas íntegros.
- [ ] Números, artigos, fórmulas e datas conferidos de novo no PDF.
- [ ] Dúvidas e problemas do material em NOTAS.

Script opcional (Python 3, sem dependências), que confere formato, tamanhos e expressões proibidas:
```
python verificar_resumos.py resumos_AGENTE_S0101-S0120 --indice INDICE-RESUMOS.csv
```
Ele **não** compara com o PDF (não consegue verificar originalidade nem exatidão): isso continua sendo responsabilidade sua.

## 14. Casos especiais
- **Trecho curto** (poucas páginas): o resumo é proporcionalmente curto (piso: o maior entre 250 palavras e 20% do alvo); não encha.
- **Trecho com muitas questões comentadas**: resuma a **teoria** que sustenta as questões; não resuma as questões nem copie enunciados.
- **Trecho que começa ou termina no meio de um tópico**: resuma só o que está no intervalo de páginas.
- **Conteúdo repetido entre trechos vizinhos**: resuma como se o aluno fosse ler um trecho de cada vez, sem remeter aos outros ("como visto antes" é proibido).
- **Cálculos longos**: ensine o método com um exemplo curto; não reproduza a resolução passo a passo de todos os exemplos.

## 15. Como seu trabalho será auditado
De cada agente serão sorteados **5 resumos** para análise, com nota por critério:
1. **Cobertura**: todos os assuntos do trecho e tudo que é cobrável estão presentes?
2. **Correção**: números, artigos, fórmulas e conceitos exatos?
3. **Originalidade**: sem trechos copiados; exemplos próprios?
4. **Clareza e didática**: explica, não só lista; ordem lógica; tabelas úteis?
5. **Tamanho e formato**: dentro do teto, sem enchimento; arquivo no padrão (seções 11–12).
Resumos fora do padrão serão devolvidos para refação; vale mais **acertar** do que **escrever muito**.
