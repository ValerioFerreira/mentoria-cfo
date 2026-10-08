# Briefing — ETAPA 1: Bizu de cada trecho (resumo + Certo/Errado)

A produção do banco é feita em DUAS etapas. **Esta é a etapa 1 (só bizu).** As questões AOCP (etapa 2, `pipeline/briefs/content.md`) vêm depois, nos mesmos arquivos, quando todos os bizus estiverem prontos.

Leia antes: `CLAUDE.md`, `INSTRUCOES-COLABORADOR.md` (divisão de disciplinas e fluxo de trabalho) e o exemplo aprovado `content/items/direito-administrativo/a00.json` (trechos s01–s02; já tem as questões da etapa 2).

## O que é um trecho e onde ele aparece
Trecho = unidade de ~1 h de teoria (6–17 págs. do PDF), id `<disciplina>/aNN/sNN`, definido em `content/segments/<disciplina>.json` (`startPage`–`endPage`, `topicsCovered`). No site, a atividade de **Teoria** mostra o Bizu (resumo + itens C/E "da Teoria") logo após o estudo; a **Revisão** espaçada mostra os itens C/E "da Revisão" (conjunto diferente) e o mesmo resumo. É conteúdo de FIXAÇÃO RÁPIDA: precisa ser correto, enxuto e cobrir o trecho inteiro.

## O que produzir por trecho
**Leia o trecho inteiro** (todas as págs. `startPage`–`endPage`; `pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --pages 10-22`, defina `PYTHONIOENCODING=utf-8`; a visão geral da aula e os trechos saem de `inspect_aula.py <disc>/aNN`). Conhecimento só do que o trecho ensina. Se o material tiver erro evidente ou estiver desatualizado, não use o ponto e registre no relatório.

1. `summary` — **6 a 14 tópicos** de revisão, cada um uma frase/ parágrafo curto. Cubra TODOS os subtópicos relevantes: conceitos-chave, regras, exceções, classificações, comparações, pegadinhas, mnemônicos, literalidade normativa (artigos/prazos). Só use **negrito** (`**termo**`) para destaque: o site NÃO renderiza itálico, crase, listas nem tabelas dentro do resumo.
2. `teoria` — **3 a 5** itens Certo/Errado para fazer logo após a Teoria. `revisao` — **3 a 5** itens C/E **diferentes** (outros pontos ou outros ângulos) para a Revisão. Cada item: `statement` (UMA afirmação, objetiva, inequívoca, sustentada pelo trecho; explore detalhe, exceção, troca de termos plausível), `isTrue` (booleano) e `explanation` (por que está certo/errado, citando a regra). Cada conjunto precisa ter itens certos E errados; não repita afirmação em nenhum lugar do arquivo; sem C/E de enchimento.
3. `pointers` — **≥ 4 pontos-chave** `{ "topic": "...", "pageRef": N }` (N = página do PDF onde o ponto é ensinado, dentro do trecho). Servem para a etapa 2 não reler o trecho inteiro; cubra o trecho de ponta a ponta (ideal 6–10).
4. **Originalidade (o validador rejeita)**: nenhuma sequência de 10 palavras igual ao PDF. Parafraseie; troque exemplos. Citação literal de lei só em C/E/resumo quando for dispositivo legal curto e essencial — e prefira sempre a paráfrase.
5. **Complementos autorais** (aulas `cNN`) já têm bizu e questões: não mexa. Aulas `practice`/fora do edital não têm trecho.
6. Dê prioridade ao que a AOCP cobra (ver `content/style/aocp-profile.json`); em exatas, os C/E podem ser afirmações sobre fórmulas, unidades, condições de validade, sinais e propriedades (nunca cálculo com contas longas).

## Formato do arquivo — `content/items/<disciplina>/<aNN>.json` (um por aula, TODOS os trechos da aula)
```json
{"aula": "<disc>/a05", "batch": "w2-bizu-<disc>", "status": "DRAFT", "stage": "bizu",
 "segments": [
  {"id": "<disc>/a05/s01",
   "bizu": {
     "summary": ["**Termo** = ...", "..."],
     "teoria":  [{"statement": "...", "isTrue": false, "explanation": "..."}],
     "revisao": [{"statement": "...", "isTrue": true,  "explanation": "..."}],
     "pointers": [{"topic": "Atributos do ato", "pageRef": 23}]
   }}
 ]}
```
`"stage": "bizu"` marca que ainda não há questões (o validador não cobra o mínimo de questões e proíbe questões onde ele estiver). Pode ficar no arquivo (todos os trechos só com bizu) ou em um trecho (`{"id": ..., "stage": "bizu", "bizu": {...}}`), útil quando o arquivo já tem trechos completos: é o caso de `direito-administrativo/a00.json` (s01–s02 com questões — preserve — e s03–s05 novos com `"stage": "bizu"` por trecho). Na etapa 2 o campo `stage` é removido e as `questions` entram nos mesmos trechos.

## Validação (a cada aula)
```
pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json
pipeline/.venv/Scripts/python pipeline/validate_content.py --coverage --stage bizu --subject <disc>
```
Corrija todos os erros (JSON válido, UTF-8, 6–14 tópicos, 3–5 C/E por conjunto com certos e errados, pointers, originalidade, duplicatas entre arquivos da disciplina). Escreva os arquivos com a ferramenta Write (aspas internas escapadas); heredoc longo no Bash quebra com aspas.

## Segunda passada (obrigatória por aula)
Releia cada C/E como o aluno e como a banca recorrendo: ambíguo? duas leituras possíveis? gabarito certo? depende de matéria que o trecho não ensina? erro conceitual, jurídico, de fórmula? afirmação "absoluta" (sempre/nunca/somente) injusta? Reescreva e revalide.

## Entrega
Por aula: trechos, itens C/E, problemas encontrados no material, dúvidas para revisão humana. Commit pequeno e frequente (ver `INSTRUCOES-COLABORADOR.md`). Não cole o conteúdo produzido na resposta.
