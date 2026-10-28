# Briefing 2: inéditas para o PRIMEIRO caderno de cada aula do CBMPE Oficial chegar a 25 questões

Repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM` (branch `pcpe`). Português do Brasil. Windows: use a ferramenta Write para
arquivos grandes e `PYTHONIOENCODING=utf-8` nos comandos Python (`pipeline/.venv/Scripts/python`). **Não faça commit, não use git, não grave
em banco algum, não use `--remoto`.**

**Leia primeiro, inteiro, `pipeline/briefs/ineditas-cbmpe.md`** (formato do rascunho com a correta sempre em A, ferramenta
`pipeline/pcpe_tools/ineditas_append.py`, `ineditas_mc_nativas.py --check`, padrão AOCP, fonte do conteúdo, originalidade, revisão cruzada).
Tudo vale aqui. Só mudam a meta e a lista, descritas abaixo.

## O que mudou

Na rodada anterior cada trecho passou a ter pelo menos 7 questões. Falta um detalhe: o primeiro caderno de uma disciplina no plano de um
aluno cobre até os **4 primeiros trechos de uma aula** e não tem trecho anterior para completar. Para ter 25 questões, **a soma dos até 4
primeiros trechos de cada aula precisa chegar a 25**.

`pipeline/briefs/ineditas-cbmpe2-faltantes.csv` lista os trechos (os primeiros de 88 aulas) onde faltam questões, com `questoes_hoje` e
`escrever` (a quantidade exata a escrever naquele trecho; é a parte do que falta da aula que cabe a ele). São **975 questões** no total.
Acompanhe com:

```bash
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_cbmpe_aula.py                 # resumo por disciplina
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/lacunas_cbmpe_aula.py --lista fisica  # aulas ainda abaixo de 25
```

## Cuidados específicos

- Esses trechos **já têm** inéditas (as da rodada anterior estão em `content/questoes/ineditas/mc/<disciplina>.txt`). **Leia o que já existe
  do trecho antes de escrever** e cubra **outros tópicos** (veja `topicos` no CSV e o resumo do trecho): nada de repetir enunciado ou
  variar só os números. Se os tópicos do trecho já estiverem todos cobertos, aprofunde: casos concretos, exceções, comparações,
  cálculos de outro tipo, itens "INCORRETA".
- Escreva exatamente o que o CSV pede em `escrever` (pode passar de 1 a 2; não fique abaixo). Se a aula tem trechos com muito pouco
  conteúdo cobrável, é aceitável concentrar mais no trecho mais rico **desde que a soma da aula chegue a 25** e você avise na resposta.
- Grave **cada aula** assim que escrevê-la (ferramenta de anexar + `--check`), nunca tudo no fim: um corte de uso não pode perder trabalho.
- O aviso "trecho sem assunto do edital" é só aviso; não use `item=`.
- Relatório: `content/questoes/ineditas/REVISAO-2026-10-22-cbmpe2-<seu-nome>.md` (quantas por aula e dúvidas que dependem do dono).
- Resposta final curta: totais por disciplina, aulas que ainda não chegaram a 25 (e por quê), dúvidas.
