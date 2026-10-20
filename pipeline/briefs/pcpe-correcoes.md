# Briefing: correções para liberar o PCPE Agente de Polícia (planos, rótulos, resumos e questões)

Contexto: o cadastro do PCPE foi aberto, mas **todo plano do PCPE nasce "em análise"** (`web/src/lib/plan/initial-status.ts`; o aluno vê
"em até 24 horas"). O dono libera cada plano em Admin › Cadastros (ou `web/scripts/verify-plans.ts --apply`) **só depois** que estas
correções estiverem prontas. Você tem, portanto, algumas horas, mas não pode quebrar nada que já funciona. Projeto, convenções e
comandos: `CLAUDE.md` (raiz) e `README.md`. Idioma pt-BR. **Não faça push, não grave na produção, não toque em `.env*`** (o dono faz).
`docs/` é protegida (não copie texto). Commits só com `git add` explícito, terminando com
`Co-Authored-By: <seu modelo> <noreply@anthropic.com>`.

## Como o problema foi medido (reprodutível)

```bash
cd web && npx tsx scripts/pcpe-plan-test.ts                      # gera 10 planos de teste do PCPE -> pipeline/.cache/pcpe-planos.json
cd .. && pipeline/.venv/Scripts/python pipeline/pcpe_tools/audit_planos.py   # relatório: rótulos, resumos, ordem, revisões, cadernos
pipeline/.venv/Scripts/python pipeline/questoes/lacunas_pcpe.py --check      # trechos ainda abaixo do mínimo de questões
```

Resultado de 2026-10-20: ordem T→R→F→Q correta e revisões coerentes nos 10 planos; **mas** (T1) 51 cadernos que não abrem, (T2) 43
rótulos de diretriz suspeitos, (T3) resumos em rascunho com 76 casos para ler, (T4) motor deixa disciplinas de fora em um cenário.
Meta: `audit_planos.py` sem cadernos que não abrem, `lacunas_pcpe.py --check` com saída 0, e as demais tarefas fechadas.

## T1. Questões inéditas de múltipla escolha para todo trecho ficar com o mínimo (a maior tarefa)

- O caderno da atividade junta as questões dos trechos do grupo (até 4 Teorias) e **só abre com 5 ou mais**; o pedido é 25 (15 no Turbo).
  Hoje **311 trechos** estão abaixo do mínimo (6 por trecho; 8 nos de `peso_prova` ≥ 0,20): faltam **1.149 questões**. A lista, com
  disciplina, trecho, aula, páginas, tópicos, quantas existem e quantas faltam, está em `pipeline/briefs/ineditas-fracos.csv`
  (regenerada por `lacunas_pcpe.py`, que desconta o que você já escreveu).
- Formato, fontes, regras de escrita e de originalidade: **`pipeline/briefs/ineditas-cobertura.md`** (leia inteiro; vale igual aqui).
  Escreva em `content/questoes/ineditas/mc/<disciplina>.txt` (acrescente ao fim; **não altere as existentes**, a menos que ache erro,
  e nesse caso registre). Cada questão: 5 alternativas, uma correta, distratores plausíveis, comentário que explica o gabarito.
- Lições da revisão de 2026-10-20 (o validador agora acusa as duas primeiras):
  1. **Não deixe o gabarito em sequência A,B,C,D,E**: sorteie a posição (fique perto de 20% por letra em cada disciplina).
  2. **No comentário, não cite letras de alternativas erradas** (foi a maior fonte de erro depois do embaralhamento). Explique pelo
     conteúdo: "A afirmação de que ... está errada porque ...". Se citar a letra, ela nunca pode ser a do gabarito.
  3. **Confira a lei na fonte oficial e o texto-fonte do trecho** (`seg_summary.py`, `seg_bizu.py`, `summary_source.py`); legislação
     de out/2026 (Lei 15.397/2026 no furto, Lei 15.517/2026 combustíveis, LC 225/2026 etc. estão no material do curso). **Não cite
     número de súmula, tema, ADI, HC ou informativo que você não consiga confirmar**; prefira "conforme a jurisprudência do STJ".
  4. **Refaça cada conta à mão** (Estatística, Matemática, Raciocínio Lógico, Contabilidade); um erro de soma já passou uma vez.
  5. Em questões do tipo "assinale a INCORRETA", o comentário não pode dizer que "as demais estão incorretas".
- Validação: `ineditas_mc_nativas.py --check` (erros 0), `lacunas_pcpe.py --check` (saída 0), e releia cada questão nova como revisor
  independente. Registre em `content/questoes/ineditas/REVISAO-AAAA-MM-DD-lacunas.md`: por disciplina, quantas escreveu e as dúvidas
  para o dono.
- Prioridade das disciplinas (peso na prova): Contabilidade, Informática, Língua Portuguesa, Estatística, Legislação do PCPE, Direito
  Processual Penal, Direito Constitucional, Matemática, Raciocínio Lógico, Legislação Penal Especial, Direito Administrativo, Direito Penal.

## T2. Rótulos da diretriz que não batem com o PDF

A diretriz diz "comece na pág. X, no tópico “T”". Em 43 trechos, T não aparece nas duas primeiras páginas do trecho (lista em
`pipeline/.cache/pcpe-rotulos-suspeitos.json`, gerada por `audit_planos.py`). Casos conhecidos: Contabilidade Geral (títulos do
índice ≠ cabeçalhos do PDF), Direito Administrativo licitações (a20/s09, a21/s12, a22/s14, a24/s02 ...), Direito Penal (a04/s04 abre em
"Art. 121-B", não em "Induzimento ao suicídio"), Legislação do PCPE (a03/s01 começa no sumário, a05/s01 na "Apresentação"),
Legislação Penal Especial, DPP, e **`informatica/a04/s03`: o tópico saiu como “IREWALL” (a letra F inicial se perdeu)**.

- Para cada um dos 43: abra o PDF (`pipeline/inspect_aula.py <disc>/aNN --pages X-Y`), decida o rótulo correto (o cabeçalho real da
  página ou, se não houver, o primeiro assunto tratado) e corrija **somente o texto do rótulo** por `content/overrides/<disciplina>.json`
  (`headings`), conforme o `CLAUDE.md` (nunca edite `structure/` ou `segments/` à mão).
- **Invariante inegociável:** ids dos trechos, `startPage` e `endPage` não podem mudar (ids são posicionais e prendem resumos, bizus e
  questões). Antes e depois de regenerar (`segment.py --subject <disc>`, `build_catalog.py`, `build_complements.py`, `edital_map.py`),
  compare `{id, startPage, endPage}` de todos os trechos e **reverta tudo** se algum mudar. Não rode `build_complements.py` sem `--only`
  se isso reescrever arquivos alheios (já houve esse efeito colateral; veja o histórico no `HISTORICO.md`).
- Depois: `audit_planos.py` deve cair para perto de 0 em [1]; o que sobrar, justifique em `content/audit/pcpe-rotulos.md`
  (trecho, rótulo antigo, rótulo novo ou "mantido porque ...").

## T3. Resumos analíticos em rascunho

Os 662 resumos usados nos planos de teste estão em `DRAFT`. A triagem automática (`pipeline/summary_coverage.py --csv ...`) marca
76 como REVISAR/REFAÇÃO para os trechos do PCPE (11 disciplinas; mais Raciocínio Lógico, que tem muitos exemplos com nomes), e 24 têm
menos de 60% dos tópicos do trecho citados.

- Gere a lista (`summary_coverage.py --csv pipeline/.cache/cov.csv`, filtre os trechos do PCPE em `content/importance/segments.json`),
  leia cada resumo **contra o texto-fonte** (`summary_source.py <trecho>`) e reescreva o que omite assunto relevante ou erra conceito.
  Siga `pipeline/briefs/summary.md` (tamanho, seções, `### Para fixar` com 5 a 8 itens, originalidade).
- Rode `validate_summaries.py` (sem erro), `apply_synthetic.py` e espelhe em `web/content` como no `CLAUDE.md`. **Não** mude a impressão
  digital nem o status para aprovado (isso é decisão do dono depois da amostragem); registre os trechos tratados em
  `content/audit/pcpe-resumos.md`.

## T4. Motor: disciplinas ficam de fora no plano mais curto sem Turbo

Cenário reproduzível: PCPE, todas as 12 disciplinas, 10 h/semana, nível iniciante, **sem Turbo** → o plano deixa **Direito Penal e
Direito Processual Penal sem nenhuma aula** (o verificador `planner/verify.ts` acusa `DISCIPLINA_SEM_CONTEUDO` e bloqueia). A regra do
projeto é que nenhuma disciplina fique de fora (`CLAUDE.md`, seção do ciclo mínimo). Investigue `web/src/lib/planner/select.ts`,
decida a correção mais simples e segura (garantir ao menos o ciclo mínimo da aula de maior valor de cada disciplina antes de completar
as demais, ou forçar a oferta do Turbo quando não couber), e cubra com teste em `planner/` (reproduza o cenário). **Não altere as
durações das atividades nem a divisão por dias** (regras do `CLAUDE.md`). Rode `npm test`, `npx tsx scripts/plan-audit.ts` e
`scripts/compare-plans-main.ts` para garantir que CBMPE e PMPE não mudam (0 divergências).

## Ordem de trabalho e entrega

T1 é a mais longa: faça T2, T4 e T3 primeiro se o dono precisar liberar antes; ou paralelize por disciplina em T1. Ao fim:

1. `audit_planos.py`: 0 cadernos que não abrem; rótulos sem pendência; `lacunas_pcpe.py --check` saída 0; `ineditas.py --check` e
   `ineditas_mc_nativas.py --check` sem erros; testes do web passando.
2. Um commit por tarefa (T1 pode ser por disciplina), sem push e sem escrita em produção.
3. Resposta com: totais por tarefa, o que **não** foi possível (e por quê), dúvidas para o dono, os hashes dos commits e o comando
   exato para gravar as novas inéditas (`ineditas_mc_nativas.py --json web/lote-mcn.json` e
   `npx tsx scripts/questoes-ineditas.ts lote-mcn.json --retirar-ausentes --remoto`, que o dono executa com backup).
