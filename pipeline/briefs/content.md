# Briefing — Produção de bizus e questões (MentorIA / CFO-BM)

Você produz o banco autoral de UMA lista de aulas (dada no seu pedido). Outros agentes produzem outras aulas em paralelo: **só escreva os arquivos das suas aulas**.

## Contexto
- Repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM`. Leia `CLAUDE.md` (convenções; Questões AOCP = 5 alternativas A–E, 1 correta; Certo/Errado só nos bizus; conteúdo **original/parafraseado**).
- Concurso: 2º Tenente do Corpo de Bombeiros Militar de Pernambuco (CBMPE), banca **Instituto AOCP**, prova objetiva 28/02/2027. Edital do cargo: `pipeline/.cache/edital_2ten.txt`.
- Trechos (unidades de ~1 h de teoria): `content/segments/<disciplina>.json` — cada trecho tem `id` (`<disc>/aNN/sNN`), `startPage`–`endPage` (páginas do PDF), tópicos. Mapa edital → material da disciplina: `content/edital/<disciplina>.json`; relatório de auditoria: `content/audit/<disciplina>.md`.
- Texto das páginas: `pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --pages 10-22` (defina `PYTHONIOENCODING=utf-8`). Visão da aula: `inspect_aula.py <disc>/aNN`. Para complementos autorais (`cNN`), a fonte é `content/complements/<id>.md` (o `.md` tem a correspondência; páginas não se aplicam — veja `content/structure/<disc>.json` → tópicos com página do PDF gerado).
- Estilo AOCP medido no material: `content/style/aocp-profile.json` (enunciado mediano ~33 palavras; alternativas curtas; comandos "Assinale a alternativa correta/que/incorreta", "De acordo com…", "Em relação a…"; ~8% lei seca, ~14% cálculo, poucas assertivas romanas; gabarito equilibrado).
- Exemplo aprovado de formato: `content/items/direito-administrativo/a00.json` (trechos s01–s02).

## O que produzir — para CADA trecho de cada aula sua (inclusive o último, mesmo curto)
**Leia o trecho inteiro antes de escrever** (todas as páginas `startPage`–`endPage`). Antes de cada questão, defina qual conhecimento exato ela avalia. Tudo deve estar sustentado pelo que o trecho ensina — não traga matéria de fora do trecho, nem informação que o material não sustenta; se o material tiver um erro evidente ou estiver desatualizado, não crie questão sobre o ponto e registre na resposta final.

1. **Bizu** (`bizu`):
   - `summary`: 6–14 tópicos de revisão (markdown curto, **negrito** nos termos-chave): conceitos-chave, regras, exceções, comparações, pegadinhas, mnemônicos, literalidade relevante. Cubra TODOS os subtópicos relevantes do trecho.
   - `teoria`: 3–5 itens Certo/Errado para logo após a Teoria; `revisao`: 3–5 itens C/E **diferentes** para a Revisão espaçada. Cada item testa UM ponto, é inequívoco, explora detalhe/exceção/confusão comum, e tem `explanation` dizendo por que está certo/errado. Misture certos e errados em cada conjunto (ambos obrigatórios). Não crie C/E de enchimento.
2. **Questões** (`questions`), no padrão AOCP, por tamanho do trecho: < 6 págs. → 6–8; 6–9 págs. → 9–11; 10–13 págs. → 12–14; 14–17 págs. → 13–16 (densidade alta pode justificar o topo; pouca matéria, o piso). Mínimo absoluto: 8 (5 para trecho < 6 págs.). **Qualidade e cobertura acima de quantidade**: cada questão avalia um ponto diferente; nada de repetir a mesma ideia com troca de palavras.
   - Distribua entre: conceitos fundamentais, classificações, diferenças conceituais, exceções, aplicações/casos concretos, relações entre conceitos, pegadinhas plausíveis, literalidade normativa (quando a matéria é norma), pontos de alta incidência e de erro comum. Em exatas (Matemática, Física, Química, Estatística): ≥ 50% de cálculo/aplicação, com números verificados (faça a conta; se quiser, confira com Python). Em Informática: situações de uso, atalhos e menus **como o material apresenta** (Office 2019 / LibreOffice 7 / Windows 11). Em línguas estrangeiras: use `support` com um texto-base curto **original** (escrito por você, 60–160 palavras) quando a questão for de leitura/uso em contexto; vocabulário e gramática em contexto; enunciado em português, como a AOCP faz.
   - Dificuldade: ~25% nível 1, ~50% nível 2, ~25% nível 3 (nível de 2º Tenente: exige domínio, não decoreba trivial; evite questões obscuras).
   - 5 alternativas plausíveis, mesmo campo semântico, tamanhos parecidos (a correta NÃO deve ser sistematicamente a mais longa nem a mais "completa"); **exatamente uma** defensável. Evite "todas/nenhuma das anteriores". Use "incorreta"/"exceto" com moderação (≤ 20%) e destaque em MAIÚSCULAS a palavra de negação no enunciado (ex.: "assinale a alternativa INCORRETA").
   - Gabarito equilibrado por arquivo (cada letra entre ~14% e 26%), sem padrões (não repita a mesma letra mais de 3 vezes seguidas).
   - `explanation` (≥ 2 frases): por que a correta está certa e por que as erradas mais tentadoras estão erradas; pode citar o artigo/regra.
   - `pageRef`: página do PDF onde o ponto é ensinado (dentro do trecho). `topic`: subtópico (curto, em pt-BR, como no índice do trecho). `pattern`: um de `correta, incorreta, assertivas, lacuna, caso, lei-seca, conceito, calculo, texto, relacao, excecao`. `difficulty`: 1, 2 ou 3. `literal: true` SÓ quando a alternativa/enunciado reproduz texto de norma (lei, CF, súmula) — isso dispensa a checagem de originalidade, então use com parcimônia e só com o texto legal exato.
3. **Originalidade (o validador rejeita)**: nenhuma sequência de 10 palavras iguais ao PDF (em enunciados, alternativas, explicações, bizus). Parafraseie. Exemplos e casos devem ser seus (troque nomes, números, situações). Não reproduza as questões do PDF (nem as de concursos que o material traz).
4. Contexto bombeiro/militar é bem-vindo nos casos (ex.: "Um 2º Tenente do CBMPE…"), quando natural.

## Formato do arquivo: `content/items/<disciplina>/<aNN|cNN>.json` (um por aula, com TODOS os trechos da aula)
```json
{"aula": "<disc>/a05", "batch": "w1-<disc>", "status": "DRAFT",
 "segments": [
  {"id": "<disc>/a05/s01",
   "bizu": {"summary": ["**Termo** = ...", "..."],
            "teoria":  [{"statement": "...", "isTrue": false, "explanation": "..."}],
            "revisao": [{"statement": "...", "isTrue": true,  "explanation": "..."}]},
   "questions": [
     {"topic": "Atributos do ato", "pattern": "conceito", "difficulty": 2, "pageRef": 23,
      "statement": "…Assinale a alternativa correta.", "support": null,
      "options": ["…", "…", "…", "…", "…"], "answer": "C", "explanation": "…"}
   ]}
 ]}
```
JSON válido em UTF-8 (escreva com a ferramenta Write; aspas internas escapadas). Se o arquivo da aula já existir (ex.: piloto de Dir. Administrativo a00), **preserve as questões boas dos trechos que ainda existem** (revise-as) e complete o resto; remova trechos órfãos (ids que não existem mais em `content/segments`).

## Validação obrigatória (antes de terminar cada aula)
```
pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json [outros arquivos seus]
```
Corrija TODOS os erros (originalidade, gabarito, distribuição, pageRef, mínimos, duplicatas). Leia os avisos e corrija os pertinentes (ex.: alternativa correta muito mais longa).

## Segunda passada (auditoria do seu próprio banco) — obrigatória
Releia cada questão como se fosse o aluno e como se fosse a banca recorrendo: mais de uma alternativa defensável? gabarito compatível? alternativa absurda (troque por distrator plausível)? exige matéria não estudada no trecho? erro conceitual, jurídico, de cálculo, gramatical? ambiguidade em C/E? questão trivial ou obscura demais? duas questões testando a mesma coisa? Corrija e revalide.

## Resposta final (curta, ≤ 15 linhas)
Por aula: trechos, questões, itens C/E; problemas encontrados no material (erros, desatualização, páginas sem teoria real); dúvidas que exigem revisão humana. Não cole o conteúdo produzido.
