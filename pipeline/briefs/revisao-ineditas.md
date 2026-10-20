# Briefing: revisão jurídica e didática das questões inéditas MentorIA (PCPE Agente)

Você é um revisor independente (não escreveu estas questões). Sua tarefa é **conferir, uma a uma, as 485 questões
inéditas certo/errado e as 50 de múltipla escolha derivadas delas**, corrigir o que estiver errado e registrar o que fez.
Trabalhe com rigor: uma questão com gabarito errado ou lei desatualizada prejudica o aluno, e ele não percebe.

## 1. Contexto

- Projeto **MentorIA / CFO-BM** (repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM`). Concurso: **Agente de
  Polícia da PCPE** (Cebraspe; prova objetiva em 07/03/2027). O edital (item 22.2.3) lista 12 disciplinas; a legislação
  cobrada é **a vigente na data de publicação do edital (outubro de 2026)** e jurisprudência dos tribunais superiores
  publicada até 30 dias antes da prova (itens 21.32 e 21.33).
- **Formato da prova (edital, item 8.2): múltipla escolha com cinco alternativas (A a E), uma única correta.** As
  inéditas certo/errado servem para treino por assunto; as de múltipla escolha servem ao simulado.
- As questões foram escritas porque o assunto do edital **não tinha nenhuma questão real** no banco. São provisórias: quando
  as questões reais do TecConcursos forem importadas, as inéditas do assunto são aposentadas
  (`web/scripts/questoes-ineditas.ts --aposentar`).
- Foram escritas a partir dos **resumos do curso** (`content/summaries/<disciplina>/<aula>.json`, campos `analytic` e
  `synthetic`), que podem conter erros ou estar desatualizados. Por isso a conferência precisa ser feita **contra a fonte
  oficial**, não contra o resumo.

## 2. Onde está o que revisar

| O quê | Onde |
|---|---|
| Questões certo/errado (fonte editável) | `content/questoes/ineditas/<disciplina>.txt` (12 arquivos) |
| Questões de múltipla escolha | geradas por `python pipeline/questoes/ineditas_mc.py` a partir dos `.txt`; **não edite o resultado, corrija o `.txt` e gere de novo** |
| Regras de formato e validação | `pipeline/questoes/ineditas.py` (`--check`) |
| Mapa dos assuntos do edital e dos trechos | `content/edital/pcpe/<disciplina>.json` (7 disciplinas) e `content/edital/<disciplina>.json` (as outras 5) |
| Resumo do trecho (só para contexto) | `python pipeline/pcpe_tools/seg_bizu.py <trecho>` e `seg_summary.py <trecho>` |

Formato de cada questão no `.txt`:

```
@@ <aula>/<trecho> | <C|E> [| item=<código do assunto>]
Frase de abertura ("Com relação a ..., julgue o item a seguir.")

Assertiva única.
// Comentário (justificativa do gabarito, 1 a 3 frases).
```

## 3. O que verificar em cada questão

1. **Gabarito.** A assertiva é mesmo certa (`C`) ou errada (`E`)? Releia o dispositivo legal, a súmula ou a tese citados.
   Atenção a **números, prazos, penas, quóruns, percentuais e órgãos competentes**: são o que o Cebraspe troca para fazer
   um item errado.
2. **Vigência.** A norma citada está em vigor em outubro de 2026 com esse texto? Verifique alterações recentes
   (por exemplo: Lei 14.230/2021 e a Lei de Improbidade; Lei 14.133/2021 e os valores atualizados por decreto; Lei 13.964/2019
   no CPP; Lei 14.994/2024 e o feminicídio; Lei 14.532/2023 e a injúria racial; Lei 14.344/2022; Lei 14.071/2020 no CTB; Lei
   15.358/2026 no processo penal; alterações do Código Penal em 2025 e 2026; Manual de Redação da Presidência da República, 3ª
   edição). Quando houver dúvida entre texto antigo e novo, vale o novo, e a questão deve dizer o que a norma diz hoje.
3. **Jurisprudência.** Súmulas, temas e teses citados existem, têm esse número e dizem isso? (Ex.: Súmulas Vinculantes 5, 11,
   14, 21, 35; Súmulas 243, 337, 444, 500, 536, 587, 600 do STJ; Súmulas 145, 524, 603, 704 do STF; Temas 977 do STF e 1.249 do
   STJ.) Se não for possível confirmar, **reescreva sem citar o número** ou marque como "não confirmado".
4. **Uma só assertiva e sem ambiguidade.** A questão deve se sustentar sozinha, sem depender de outra. Se tiver duas
   afirmações, as duas precisam ser verdadeiras para o gabarito `C`; se uma for falsa, `E`. Evite "sempre", "nunca",
   "somente", a menos que a norma realmente seja absoluta.
5. **Padrão Cebraspe.** Frase de abertura iniciando por "Com relação a", "No que se refere a", "Acerca de", "Em relação a"
   e terminando em "julgue o item a seguir/seguinte/subsequente"; assertiva de uma ou duas orações, linguagem jurídica
   precisa, entre 14 e 140 palavras (mediana próxima de 46). Casos hipotéticos devem trazer todos os dados necessários.
6. **Comentário.** Explica o porquê do gabarito e cita o dispositivo. Não pode contradizer o gabarito nem a assertiva.
7. **Aderência ao assunto.** A questão está no trecho e no assunto certos? Se o conteúdo não pertence ao trecho indicado em
   `@@ <aula>/<trecho>`, troque para o trecho correto (veja `python pipeline/pcpe_tools/dump_segs.py <disciplina>`).
8. **Equilíbrio.** O conjunto deve ficar perto de 50% certas e 50% erradas (hoje: 239 C e 246 E). Se corrigir um gabarito,
   reequilibre mudando outra questão do mesmo assunto, se necessário.
9. **Originalidade.** Não copie texto de questões do TecConcursos nem de provas; o texto legal oficial pode ser citado de
   forma literal e curta, quando for o caso (a lei é domínio público).
10. **Nada de menção ao material-base.** Não escreva "conforme a aula", "o curso" nem nome de professor ou de curso.

## 4. Fontes aceitas

Use **somente fontes oficiais**: texto da lei no portal do Planalto (`planalto.gov.br/ccivil_03`), Constituição Federal,
Constituição do Estado de Pernambuco e leis estaduais no portal da ALEPE / SEFAZ-PE / legislação estadual oficial, súmulas e
teses nos sites do STF e do STJ, Manual de Redação da Presidência da República (gov.br), CPC/CFC para Contabilidade. Registre a
fonte de cada correção. **Não use** blogs, sites de cursinho nem resumos de terceiros como prova.

## 5. Como trabalhar (ordem sugerida)

1. Rode `pipeline/.venv/Scripts/python pipeline/questoes/ineditas.py --check`: deve terminar com `erros 0`.
2. Revise por disciplina, nesta ordem de risco jurídico: Legislação Penal Especial, Direito Processual Penal, Direito
   Administrativo (Lei 14.133 e Lei 8.429), Legislação do PCPE (LC 137/2008 e LC 317/2015), Direito Constitucional, Direito Penal,
   Contabilidade Geral, Língua Portuguesa (Manual de Redação e regência/crase), Raciocínio Lógico, Matemática e Estatística (refaça as
   contas à mão).
3. **Pontos que o autor marcou como menos seguros** (confira primeiro):
   - Estatuto do Desarmamento: entrega espontânea de armas e extinção da punibilidade (arts. 31 e 32).
   - Lei Maria da Penha, art. 24-A: pena e quem concede fiança.
   - Lei 11.343/2006: Tema 506 do STF e limites de 40 g / 6 plantas; majorantes do art. 40 e Súmula 587 do STJ.
   - CTB: exame toxicológico (categorias C, D e E), prazos de habilitação (art. 145) e penas do art. 302, 306 e 308.
   - Lei 14.133/2021: valores de dispensa (originais da lei; há decreto de atualização), prazos de recurso e de divulgação,
     sanções (art. 156) e duração dos contratos (art. 106).
   - Lei 12.850/2013: prazo da infiltração (art. 10) e ação controlada.
   - LC estadual 137/2008: números de matrizes, classes e faixas, prazos de recurso, limite de cessão (5%).
   - Manual de Redação (3ª edição): margens, fonte, fechos e formatação; os expedientes "requerimento", "atestado" e
     "circular" não estão todos no Manual, então a questão deve ser reescrita com base em fonte oficial ou removida.
   - Contabilidade: itens do CPC 00 (R2), CPC 26 e Lei 6.404/1976 (art. 176, 178, 193, 202).
4. Para cada questão alterada, edite o `.txt` e **mantenha o cabeçalho** `@@ trecho | gabarito`. Se o gabarito mudar, troque a
   letra e reescreva o comentário. Para remover uma questão, apague o bloco inteiro (e confira que o assunto ainda tem ao
   menos 8 questões; se não tiver, escreva outras).
5. Registre cada decisão em `content/questoes/ineditas/REVISAO-AAAA-MM-DD.md` com uma tabela:
   `disciplina | nº da questão (ordem no arquivo) | veredito (OK / CORRIGIDA / REMOVIDA / REESCRITA) | o que mudou e por quê | fonte oficial (URL)`.
   Questões sem alteração entram só na contagem (por exemplo, "Direito Processual Penal: 113 revisadas, 9 corrigidas").
6. Ao terminar: `ineditas.py --check` sem erros; rode `ineditas_mc.py --resumo` e confira que o simulado continua com ao menos 3
   questões de múltipla escolha em Direito Processual Penal e 2 em Legislação Penal Especial.

## 6. Como gravar (somente local, a menos que o dono peça)

```bash
# a partir da raiz
pipeline/.venv/Scripts/python pipeline/questoes/ineditas.py --json web/lote.json
pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc.py --json web/lote-mc.json
# em web/
npx tsx scripts/questoes-ineditas.ts lote.json --retirar-ausentes   # grava no banco LOCAL e aposenta as de texto antigo
npx tsx scripts/questoes-ineditas.ts lote-mc.json --retirar-ausentes
```

O id de cada questão depende do número e de um hash do texto: ao **editar** o texto de uma questão, o id muda e a antiga fica
no banco; use `--retirar-ausentes` ao gravar o lote para aposentar (status `RETIRED`) as antigas do mesmo batch (o dono decide
a produção). **Nunca grave na produção (`--remoto`) sem pedido explícito do dono**, que exige backup recente
(`npx tsx scripts/questoes-backup.ts --remoto`).

## 7. Regras do projeto que valem aqui

- Idioma pt-BR. Não imprima nem altere arquivos `.env*`. A pasta `docs/` é protegida (não copie texto dela).
- Commits só dos seus arquivos, com `git add` explícito; termine a mensagem com a linha
  `Co-Authored-By: <seu modelo> <noreply@anthropic.com>`. Não publique em remoto nem faça push sem o dono pedir.
- Se encontrar erro nos resumos do curso (`content/summaries`), **não corrija lá**; anote na tabela de revisão para o dono decidir.

## 8. Entrega

Responda com: (a) totais por disciplina (revisadas, corrigidas, removidas, reescritas); (b) as 10 correções mais graves; (c)
as dúvidas que dependem do dono (norma ambígua, jurisprudência não confirmada); (d) o caminho do arquivo de revisão e os
commits feitos.
