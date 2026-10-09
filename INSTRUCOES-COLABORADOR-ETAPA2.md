# MentorIA / CFO-BM — Instruções para o colaborador · ETAPA 2 (questões AOCP)

Você terminou as suas 5 disciplinas (bizus + questões). Os **bizus dos 761 trechos** estão prontos (a nossa frente fechou a Etapa 1). Falta só a **Etapa 2 (questões AOCP de múltipla escolha)** dos 373 trechos da nossa frente. Dividimos meio a meio:

| Quem | Disciplinas | Trechos | Páginas |
|---|---|---:|---:|
| **Valério + Claude** | Biologia (68), Língua Portuguesa (54), Dir. Penal Militar (34), Língua Inglesa (23), Legislações PE (4) | 183 | 2.141 |
| **Colaborador (você)** | **Direito Constitucional (87), Direito Administrativo (67), Língua Espanhola (36)** | **190** | 2.127 |

Escreva **somente** em `content/items/direito-constitucional/`, `content/items/direito-administrativo/` e `content/items/lingua-espanhola/`. Assim os dois lados não editam os mesmos arquivos e o merge final não tem conflito.

## 1. O que é o seu trabalho
Cada arquivo `content/items/<disciplina>/aNN.json` já tem, em cada trecho, o `bizu` (resumo, C/E e `pointers`). Você **acrescenta `"questions": [...]` em cada trecho**, sem alterar o `bizu` nem o resto do arquivo. Os `pointers` do bizu dizem onde está cada ponto-chave (com a página): use-os para não reler tudo, mas **leia as páginas do trecho** antes de escrever as questões.

O briefing completo (quantas questões por tamanho de trecho, estilo AOCP, dificuldade, gabarito, originalidade, explicação, segunda passada) está em **`pipeline/briefs/content.md`**, seções "Questões" e "Validação". Resumo:
- 5 alternativas (A–E), 1 correta; pelo menos 8 questões por trecho (5 se o trecho tem menos de 6 págs.); alvo: < 6 págs. → 6–8 · 6–9 págs. → 9–11 · 10–13 págs. → 12–14 · 14–17 págs. → 13–16.
- ~25% de dificuldade 1, ~50% de 2, ~25% de 3; gabarito equilibrado por arquivo (cada letra entre ~14% e 26%, no máximo 3 iguais seguidas); alternativa correta **não** pode ser sempre a mais longa.
- Nenhuma sequência de **10 palavras iguais** ao PDF (o validador rejeita): parafraseie. Em Direito isso exige atenção: o material reproduz o texto da lei, então troque verbos e ordem e quebre as listas legais. `literal: true` só para citação exata de norma (lei, CF, súmula), com parcimônia.
- Cada questão com `topic`, `pattern`, `difficulty`, `pageRef` (página do PDF **dentro** do trecho) e `explanation` (≥ 2 frases, dizendo por que a certa está certa e por que as erradas mais tentadoras estão erradas).
- **Língua Espanhola:** enunciado em português, como a AOCP faz; quando a questão for de leitura ou de uso em contexto, use `support` com um texto-base curto **original** em espanhol (60–160 palavras).

## 2. O que NÃO usar nas questões (dúvidas do material)
Nas seções 11–14 de `PROGRESSO-AUDITORIA.txt` estão as **dúvidas do material já levantadas** em Dir. Constitucional, Dir. Administrativo e Espanhol (lei citada com número errado, dado desatualizado, contradição entre páginas…). Não faça questão sobre esses pontos; se encontrar outro problema, anote em `PROGRESSO-COLABORADOR-ETAPA2.txt` (arquivo seu, novo).

## 3. Preparar a máquina
1. `git fetch origin` e crie a sua branch **a partir de `bizus-juridicas-linguas`**: `git switch -c questoes-juridicas origin/bizus-juridicas-linguas`. (Esta branch tem os bizus das suas três disciplinas e este arquivo.)
2. Coloque em `docs/` (mesma estrutura de pastas, **fora do Git**, nunca commitar) apenas estes PDFs:
   - `04 - CBM-PE (Oficial) Direito Constitucional/`: todos os 19 (`001 - Aula 00 …` até `019 - Aula 18 …`)
   - `02 - CBM-PE (Oficial) Direito Administrativo/`: todos os 10 (`001 - Aula 00 …` até `010 - Aula 09 …`)
   - `05 - CBM-PE (Oficial) Língua Espanhola/`: os 14 primeiros (`001 - Aula 00 …` até `014 - Aula 13 …`); as provas comentadas (`015` a `017`) não são necessárias
   - `docs/indice_topicos_curso.xlsx`, se você ainda não tiver.
3. Gere o cache de texto só dessas pastas: `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/extract.py --only 02`, depois `--only 04` e `--only 05`.
4. Confira: `pipeline/.venv/Scripts/python pipeline/inspect_aula.py direito-administrativo/a01` (mostra páginas, tópicos e trechos) e `pytest pipeline/tests -q` (inclui o teste de originalidade, que só roda com o cache).

## 4. O que NÃO fazer
- Não rodar `segment.py`, `build_catalog.py`, `build_complements.py`, `edital_map.py` nem o seed (os ids dos trechos são posicionais).
- Não editar `content/structure`, `segments`, `catalog.json`, `gaps.json`, `overrides`, `edital`, `audit`, `complements`, `pipeline/*.py`, `web/`, `CLAUDE.md`, `PROGRESSO-AUDITORIA.txt`, nem arquivos de outras disciplinas. Problema nesses arquivos: anote e avise Valério.
- Não copiar texto do PDF; não versionar `docs/` nem `pipeline/.cache/`.

## 5. Fluxo por aula
1. `inspect_aula.py <disc>/aNN` lista os trechos (`startPage`–`endPage`); `--pages 10-22` mostra o texto; `--grep "regex"` busca.
2. Leia o trecho e o `bizu` dele; escreva as questões; acrescente-as ao `aNN.json` (mesma estrutura de `content/items/direito-administrativo/a00.json`, que já tem questões em s01–s02: preserve e revise essas).
3. Valide: `pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json` — corrija TODOS os erros e leia os avisos. Depois faça a segunda passada de qualidade do briefing.
4. Commit pequeno e frequente (1–3 aulas): `git add content/items/<disc> && git commit -m "Questoes <disciplina> aNN-aMM (DRAFT)"`; `git push -u origin questoes-juridicas`.
5. Acompanhe o que falta: `validate_content.py --coverage --subject <disc>`.

Dica: pode usar até 2–3 agentes do Claude Code em paralelo (uma aula por arquivo por agente) e peça "Leia `pipeline/briefs/content.md` e produza as questões das aulas aNN–aMM de `<disciplina>`".

## 6. O que cabe a você, por aula (trechos pendentes · páginas)
- **Direito Constitucional** (87 · 930): a00 5·58 · a01 1·15 · a02 5·52 · a03 8·86 · a04 3·36 · a05 1·14 · a06 2·22 · a07 1·12 · a08 9·90 · a09 6·67 · a10 7·62 · a11 5·54 · a12 3·35 · a13 10·98 · a14 3·35 · a15 3·28 · a16 6·69 · a17 8·88 · a18 1·9
- **Direito Administrativo** (67 · 731): a00 3·30 (s03–s05; s01–s02 já têm questões) · a01 7·65 · a02 5·61 · a03 4·48 · a04 5·60 · a05 13·153 · a06 5·48 · a07 5·55 · a08 4·39 · a09 16·172
- **Língua Espanhola** (36 · 466): a00 1·15 · a01 2·26 · a02 2·31 · a03 1·8 · a04 2·28 · a05 2·25 · a06 4·50 · a07 2·26 · a08 2·31 · a09 6·80 · a10 3·36 · a11 3·29 · a12 1·17 · a13 5·64

Ordem sugerida: Dir. Administrativo → Língua Espanhola → Dir. Constitucional (a maior).
Os trechos dos complementos (`cNN`) dessas três disciplinas já têm questões; não mexa neles.

## 7. Como será o merge
Quando os dois lados terminarem: PR de cada branch para a `main`/`lancamento` (pastas disjuntas, sem conflito), `pytest` e `validate_content.py --coverage` (meta: 761 trechos com bizu e questões) e, por fim, o seed e a revisão humana (`/admin/revisao`).
