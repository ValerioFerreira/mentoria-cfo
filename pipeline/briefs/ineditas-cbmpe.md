# Briefing: inéditas MentorIA de múltipla escolha para completar os cadernos do CBMPE Oficial

Repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM` (branch `pcpe`). Idioma de tudo: português do Brasil. Windows: use a ferramenta
Write para arquivos grandes (heredoc longo no Bash quebra) e defina `PYTHONIOENCODING=utf-8` nos comandos Python
(`pipeline/.venv/Scripts/python`). **Não faça commit, não mexa em git, não grave em banco algum e não use `--remoto`.** O orquestrador consolida.

## 1. Contexto

O caderno de Questões de cada atividade do plano do **CBMPE Oficial (2º Tenente, banca Instituto AOCP)** deve ter **25 questões**. Hoje
muitos cadernos ficam curtos porque há poucas questões AOCP por trecho. O dono decidiu: (a) o caderno passa a completar com questões
de múltipla escolha de outras bancas e com **inéditas MentorIA**; (b) onde ainda faltar, você escreve inéditas.

**Meta: no mínimo 7 questões servíveis por trecho** (4 trechos × 7 ≥ 25). `pipeline/briefs/ineditas-cbmpe-faltantes.csv` lista os
**401 trechos** abaixo disso, com `questoes_hoje` e `faltam`. São **1.767 questões** no total. O CSV já desconta as AOCP, as de outras
bancas em múltipla escolha e as inéditas já gravadas. Escreva **exatamente o que falta por trecho** (pode passar 1 ou 2, nunca ficar
abaixo). Acompanhe o avanço com:

```bash
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_cbmpe.py                 # resumo por disciplina
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_cbmpe.py --lista quimica # trechos ainda abaixo de 7 na disciplina
```

## 2. Formato e ferramenta (rascunho com a correta sempre em A)

Escreva seu rascunho num arquivo **seu**, fora do repositório, em
`C:\Users\ADMINI~1\AppData\Local\Temp\claude\C--Users-Administrador-Documents-Projetos-CFO-BM\dc4cfef5-0de0-4070-81b3-9237d477ecd9\scratchpad\agentes\<seu-nome>\` (crie a pasta), em blocos:

```
@@ <aula>/<trecho> | A
Enunciado ... assinale a opção correta.   (ou "... assinale a opção INCORRETA." / "julgue ... indique ...")
A) alternativa CORRETA (sempre a A no rascunho)
B) alternativa
C) alternativa
D) alternativa
E) alternativa
// Comentário: por que a A está certa e, em resumo, por que as outras não (1 a 4 frases; não cite letras das erradas).
```

(`<aula>/<trecho>` sem o nome da disciplina: por exemplo `a02/s03`.) Anexe com a ferramenta, que **embaralha a posição da correta**
(balanceando as letras), valida o formato e **grava com trava** em `content/questoes/ineditas/mc/<disciplina>.txt` (outros agentes
escrevem em outras disciplinas ou no mesmo arquivo ao mesmo tempo; a trava cuida disso). Nunca edite os `.txt` à mão.

```bash
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <disciplina> --dry   # confere
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/pcpe_tools/ineditas_append.py <rascunho.txt> <disciplina>         # grava
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check                            # precisa terminar com "erros 0"
```

Faça lotes pequenos (uma aula por vez), grave logo e rode `--check`. Se `--check` acusar erro numa questão **sua**, corrija o rascunho
e regrave só o necessário (não duplique): a ferramenta recusa lote com problema. Regras que o `--check` exige: 5 alternativas A–E
distintas, enunciado com comando (assinale/julgue/indique), comentário, sem questão repetida, **alternativa do gabarito não bem mais
longa que as outras**, nenhuma letra acima de ~30% dos gabaritos da disciplina, comentário que não cita a letra correta entre as erradas.

## 3. Como escrever (padrão Instituto AOCP, 5 alternativas)

- **Fonte do conteúdo.** Para cada trecho: resumo `pipeline/.venv/Scripts/python pipeline/pcpe_tools/seg_summary.py <disc>/<aula>/<trecho>`,
  bizu `.../seg_bizu.py <trecho>` e texto-fonte `.../pipeline/summary_source.py <trecho>` (**protegido: só para entender, nunca copiar**;
  pode ter bytes NUL, redirecione para arquivo seu e leia com `tr -d '\000'`). O resumo pode ter erro: **confirme leis, números, fórmulas e
  nomenclaturas em fonte oficial** (Planalto, STF/STJ, IUPAC, documentação oficial etc.; use as ferramentas Firecrawl de busca/scrape
  se disponíveis). Vale a norma vigente em outubro de 2026. Não cite súmula/tema/ADI que não consiga confirmar.
- **Estilo AOCP.** Enunciado claro e completo; 5 alternativas plausíveis, homogêneas e de tamanho parecido; **uma** só correta e
  indiscutível; distratores que trocam um elemento (número, prazo, órgão, exceção, conceito vizinho), nunca absurdos; sem "todas/nenhuma
  das anteriores". Varie o comando (correta, INCORRETA), o tipo (conceito, caso concreto, comparação, exceção, cálculo) e a dificuldade.
  Seis a oito questões num trecho devem cobrir **tópicos diferentes** (veja `topicos` no CSV), não variações da mesma frase.
- **Disciplinas de cálculo** (Matemática, Estatística, Física, Química): refaça **cada conta à mão**, por dois caminhos, antes de fixar o
  gabarito, e mostre a conta no comentário. Dados fictícios e valores simples. Fórmulas em texto simples (`v = v0 + a·t`), sem LaTeX e
  sem figuras: descreva tudo em texto (tabelas viram frases). Cuidado: o texto-fonte perdeu expoentes na extração (2^n aparece "2n").
- **Línguas** (Inglês, Espanhol): textos curtos autorais na língua, perguntas na própria língua ou em português conforme o padrão da
  banca; confira gramática e vocabulário. Nada de copiar textos de provas.
- **Originalidade e neutralidade.** Não reproduza questões do TecConcursos nem de provas, nem texto do material protegido (`docs/`).
  Nada de "conforme a aula", "o curso", "o professor" nem nome do material-base.
- **Contexto militar.** Os exemplos podem usar o cotidiano do Corpo de Bombeiros Militar de Pernambuco, mas o direito e a ciência devem
  estar corretos e não podem depender de fato inventado sobre a corporação.

## 4. Conferência e entrega

1. `lacunas_cbmpe.py --lista <sua disciplina>` sem nenhum trecho; `ineditas_mc_nativas.py --check` com `erros 0`.
2. Revisão cruzada: releia **cada** questão nova como um revisor independente (gabarito, vigência, números, comentário coerente) e
   **corrija** o que errar (regrave só o que mudar; se precisar trocar uma questão já gravada, avise o orquestrador na resposta com o
   trecho, pois os `.txt` não se editam à mão).
3. Escreva `content/questoes/ineditas/REVISAO-2026-10-21-cbmpe-<seu-nome>.md`: quantas escreveu por disciplina/aula, dúvidas que dependem do
   dono (norma ambígua, valor desatualizado, divergência do material).
4. Resposta final curta: totais por disciplina, trechos que ainda não chegaram a 7 (e por quê), dúvidas para o dono. Não cole as questões.
