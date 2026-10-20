# Briefing: inéditas MentorIA para os trechos do PCPE Agente que ficaram sem nenhuma questão

Você vai escrever questões **inéditas de MÚLTIPLA ESCOLHA** (autorais; a prova do PCPE, item 8.2 do edital, é de múltipla escolha com 5 alternativas, A a E, uma só correta) para que **nenhum trecho do plano do PCPE Agente de Polícia fique sem questão**,
enquanto o dono não importa as reais do TecConcursos. É trabalho de conteúdo: não mexa em código do site nem na produção.

## 1. O que falta

`pipeline/briefs/ineditas-faltantes.csv` lista **140 trechos** (disciplina; trecho; aula; páginas; tópicos; peso na prova) que não têm
nenhuma questão, nem real nem inédita. Meta: **no mínimo 6 questões de múltipla escolha por trecho (≈ 840 no total)**; 8 nos trechos
de `peso_prova` ≥ 0,20 (Contabilidade Geral, Matemática c03, Informática a10/a04 etc.). Distribuição:
Raciocínio Lógico 29 · Direito Administrativo 26 · Contabilidade Geral 17 · Direito Penal 17 · Informática 17 · Estatística 13 ·
Língua Portuguesa 10 · Matemática 8 · Direito Constitucional 3.

Confira o avanço a qualquer momento (offline):

```bash
pipeline/.venv/Scripts/python pipeline/questoes/cobertura_ineditas.py --minimo 6   # (conta as de content/questoes/ineditas/mc/) lista os trechos ainda abaixo do mínimo
```

## 2. Onde escrever e em que formato

Crie/complete **`content/questoes/ineditas/mc/<disciplina>.txt`** (pasta nova, uma por disciplina). **Não mexa** nos `.txt` certo/errado
da pasta acima (são outro lote). Formato de cada questão (blocos separados por linhas `@@`; a letra do cabeçalho é o **gabarito**):

```
@@ <aula>/<trecho> | <A|B|C|D|E> [| item=<código do assunto>]
Acerca de ..., assinale a opção correta.      (ou "... assinale a opção INCORRETA.")
A) alternativa
B) alternativa
C) alternativa
D) alternativa
E) alternativa
// Comentário: por que a do gabarito está certa e, em resumo, por que as outras não (1 a 4 frases).
```

Regras que `ineditas_mc_nativas.py --check` exige: trecho existente e com assunto do edital (use `item=` só se o trecho servir a mais de um
assunto), exatamente 5 alternativas A) a E) em ordem e todas diferentes, comando no enunciado ("assinale/julgue/indique"), comentário,
sem questões repetidas, **alternativa do gabarito não pode ser bem mais longa que as outras** e **nenhuma letra pode passar de ~30% dos
gabaritos de uma disciplina** (distribua A–E por todo o arquivo; não deixe um padrão previsível). Rode a cada disciplina:

```bash
pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check    # precisa terminar com erros 0
```

## 3. Como escrever bem (padrão Cebraspe)

- **Fonte do conteúdo.** Para cada trecho, leia o texto-fonte e o resumo:
  `pipeline/.venv/Scripts/python pipeline/pcpe_tools/seg_summary.py <trecho>` (resumo analítico),
  `pipeline/.venv/Scripts/python pipeline/pcpe_tools/seg_bizu.py <trecho>` (bizu) e
  `pipeline/.venv/Scripts/python pipeline/summary_source.py <trecho>` (texto-fonte protegido: **só para entender, nunca copiar**).
  O resumo pode ter erro: confirme leis e números na **fonte oficial** (Planalto, STF/STJ, CPC/CFC, Manual de Redação, documentação
  oficial do software em Informática). Vale a legislação vigente em outubro de 2026.
- **Padrão Cebraspe em múltipla escolha.** Enunciado claro e completo (com os dados do caso); 5 alternativas plausíveis, homogêneas e de
  tamanho parecido; **um** só gabarito indiscutível; distratores que trocam um elemento (número, prazo, órgão, exceção, conceito
  vizinho), nunca absurdos; evite "todas as anteriores", "nenhuma das anteriores" e "sempre/nunca/somente" sem apoio na norma. Varie
  o comando (correta, INCORRETA), o tipo (conceito, caso concreto, comparação, exceção, cálculo) e a dificuldade.
- **Disciplinas de cálculo** (Raciocínio Lógico, Matemática, Estatística, Contabilidade): refaça **cada conta à mão** antes de fixar o
  gabarito e mostre a conta no comentário. Dados fictícios e valores simples. Sem figuras: descreva tudo em texto (tabelas viram frases).
- **Informática**: baseie-se em recursos que existem nas versões atuais (Windows 11, Microsoft 365/Excel/Word/PowerPoint, navegadores);
  atalhos e menus só se tiver certeza.
- **Originalidade.** Não reproduza questões do TecConcursos, de provas anteriores nem texto do material protegido (`docs/`); o texto
  legal oficial pode ser citado de forma curta.
- **Neutralidade.** Nada de "conforme a aula", "o curso", "o professor" nem nomes do material-base.
- **Cobertura do trecho.** As 6–8 questões devem cobrir tópicos **diferentes** dos `topicos` do CSV, não variações da mesma frase.

## 4. Conferência e entrega

1. `ineditas_mc_nativas.py --check` → `erros 0`; `cobertura_ineditas.py --minimo 6` → `140/140`; `ineditas.py --check` continua com `erros 0`
   (você não o altera).
3. Revisão cruzada: releia **cada** questão nova como se fosse um revisor independente (gabarito, vigência, números, comentário
   coerente). Registre em `content/questoes/ineditas/REVISAO-AAAA-MM-DD-cobertura.md`: por disciplina, quantas escreveu, e as dúvidas
   que dependem do dono (norma ambígua, valor desatualizado).
4. Commit só dos seus arquivos, com `git add` explícito (`content/questoes/ineditas/mc/*.txt`, o arquivo de revisão); termine a mensagem
   com `Co-Authored-By: <seu modelo> <noreply@anthropic.com>`. **Não faça push, não grave no banco de produção** e não rode
   `--remoto`. Pode gravar no banco **local** para testar:
   ```bash
   pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --json web/lote-mcn.json
   cd web && npx tsx scripts/questoes-ineditas.ts lote-mcn.json
   ```
5. Responda com: totais por disciplina, trechos que ainda não chegaram ao mínimo (e por quê), dúvidas para o dono e o hash do commit.

## 5. Regras do projeto

Idioma pt-BR. Não imprima nem altere `.env*`. `docs/` é protegida (não copie texto). Trabalhe por disciplina, em ordem de peso na
prova: Contabilidade Geral, Informática, Língua Portuguesa, Estatística, Matemática, Raciocínio Lógico, Direito Administrativo,
Direito Constitucional, Direito Penal.
