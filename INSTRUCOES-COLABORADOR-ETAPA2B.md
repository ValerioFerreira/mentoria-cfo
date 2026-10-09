# MentorIA / CFO-BM — Instruções · ETAPA 2B (questões AOCP) · dois colaboradores

Os **bizus de todos os trechos estão prontos**. Dir. Constitucional, Dir. Administrativo e Língua Espanhola já estão sendo concluídos na branch `questoes-juridicas`. Falta a **Etapa 2 (questões AOCP de múltipla escolha)** de **183 trechos** (2.141 páginas), divididos em duas partes de tamanho parecido:

| Parte | Quem | Disciplinas | Trechos | Páginas | Pastas de PDF (em `docs/`) | Branch |
|---|---|---|---:|---:|---|---|
| **A** | Colaborador A | **Biologia** (68) + **Língua Inglesa** (23) | 91 | 1.106 | `07 - …Biologia/` (aulas 00–17) e `01 - …Língua Inglesa/` (aulas 00–06) | `questoes-parte-a` |
| **B** | Colaborador B | **Língua Portuguesa** (54) + **Dir. Penal Militar** (34) + **Legislações PE** (4) | 92 | 1.035 | `03 - …Língua Portuguesa/` (aulas 00–12), `13 - …Direito Penal Militar/` (aulas 00–11), `08 - …Legislações…/` (aulas 01 e 02) | `questoes-parte-b` |

Cada um escreve **somente** nas pastas da sua parte (assim o merge final não tem conflito):
- Parte A: `content/items/biologia/` e `content/items/lingua-inglesa/`
- Parte B: `content/items/lingua-portuguesa/`, `content/items/direito-penal-militar/` e `content/items/legislacoes-pe/`

Arquivo de progresso de cada um (novo, só seu): `PROGRESSO-COLABORADOR-ETAPA2-A.txt` ou `PROGRESSO-COLABORADOR-ETAPA2-B.txt`.

Exceções, **não fazer**: os trechos dos complementos (`cNN`) já têm questões; **Língua Portuguesa a13** (Redação Oficial) não é selecionável no plano (não entra na cobertura) e fica de fora.

## 1. O que é o trabalho
Cada `content/items/<disciplina>/aNN.json` já tem, em cada trecho, o `bizu` (resumo, C/E e `pointers`). Você **acrescenta `"questions": [...]` em cada trecho**, sem alterar o `bizu` nem o resto. Os `pointers` do bizu dizem onde está cada ponto-chave (com a página): use-os para se orientar, mas **leia as páginas do trecho** antes de escrever.

Briefing completo (quantidade por tamanho do trecho, estilo AOCP, dificuldade, gabarito, originalidade, explicação, segunda passada): **`pipeline/briefs/content.md`**, seções "Questões" e "Validação". Resumo:
- 5 alternativas (A–E), 1 correta; no mínimo 8 questões por trecho (5 se o trecho tem menos de 6 págs.); alvo: < 6 págs. → 6–8 · 6–9 págs. → 9–11 · 10–13 págs. → 12–14 · 14–17 págs. → 13–16.
- ~25% dificuldade 1, ~50% dificuldade 2, ~25% dificuldade 3; gabarito equilibrado **por arquivo** (cada letra entre ~14% e 26%, no máximo 3 iguais seguidas); a alternativa correta **não** pode ser sempre a mais longa; "incorreta/exceto" ≤ 20%.
- Nenhuma sequência de **10 palavras iguais** ao PDF (o validador rejeita): parafraseie. `literal: true` só para citação exata de norma (lei, CF, súmula, Código Penal Militar), com parcimônia.
- Cada questão: `topic`, `pattern`, `difficulty`, `pageRef` (página do PDF **dentro** do trecho) e `explanation` (≥ 2 frases: por que a certa está certa e por que as erradas mais tentadoras estão erradas).
- **Biologia:** ≥ 50% das questões devem usar situação/figura descrita em texto (experimento, esquema, cruzamento, heredograma) quando o tema permitir.
- **Língua Inglesa:** enunciado em português ou inglês conforme o padrão AOCP; questão de leitura usa `support` com um texto-base curto **original** em inglês (60–160 palavras).
- **Língua Portuguesa:** questões de interpretação/gramática com `support` (texto-base **original**, curto) quando fizer sentido; não copie frases dos exemplos do material.
- **Dir. Penal Militar e Legislações PE:** lei seca: troque verbos e ordem, quebre as listas legais; cuidado com alterações recentes de lei (não crie questão sobre ponto duvidoso).

## 2. O que NÃO usar nas questões (dúvidas do material)
`PROGRESSO-AUDITORIA.txt` lista as dúvidas do material já levantadas (lei citada com número errado, dado desatualizado, contradição entre páginas…). Não faça questão sobre esses pontos; se encontrar outro problema, anote no seu arquivo de progresso.

## 3. Preparar a máquina
1. `git fetch origin` e crie a sua branch **a partir de `questoes-juridicas`** (tem todos os bizus e este arquivo):
   - Parte A: `git switch -c questoes-parte-a origin/questoes-juridicas`
   - Parte B: `git switch -c questoes-parte-b origin/questoes-juridicas`
2. Coloque em `docs/` (na **raiz do projeto**, fora do Git, nunca commitar) apenas os PDFs da sua parte, na mesma estrutura de pastas (`docs/<pasta>/<NNN - Aula XX ….pdf>`), além de `docs/indice_topicos_curso.xlsx`.
3. Gere o cache de texto só dessas pastas: `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/extract.py --only 07` (e `--only 01`, no caso da parte A; `--only 03`, `--only 13`, `--only 08`, no caso da parte B).
4. Confira: `pipeline/.venv/Scripts/python pipeline/inspect_aula.py biologia/a00` (mostra páginas, tópicos e trechos) e `pytest pipeline/tests -q`.

## 4. O que NÃO fazer
- Não rodar `segment.py`, `build_catalog.py`, `build_complements.py`, `edital_map.py` nem o seed (os ids dos trechos são posicionais).
- Não editar `content/structure`, `segments`, `catalog.json`, `gaps.json`, `overrides`, `edital`, `audit`, `complements`, `pipeline/*.py`, `web/`, `CLAUDE.md`, `PROGRESSO-AUDITORIA.txt`, nem arquivos de outras disciplinas. Problema nesses arquivos: anote e avise Valério.
- Não copiar texto do PDF; não versionar `docs/` nem `pipeline/.cache/`.

## 5. Fluxo por aula
1. `inspect_aula.py <disc>/aNN` lista os trechos (`startPage`–`endPage`); `--pages 10-22` mostra o texto; `--grep "regex"` busca.
2. Leia o trecho e o `bizu`; escreva as questões; acrescente ao `aNN.json` (estrutura de `content/items/direito-administrativo/a00.json`, que já tem questões).
3. Valide: `pipeline/.venv/Scripts/python pipeline/validate_content.py content/items/<disc>/aNN.json` — corrija TODOS os erros, leia os avisos, depois faça a segunda passada de qualidade do briefing.
4. Commit pequeno e frequente (1–3 aulas): `git add content/items/<disc> PROGRESSO-COLABORADOR-ETAPA2-<A|B>.txt && git commit -m "Questoes <disciplina> aNN-aMM (DRAFT)"`, depois `git push -u origin questoes-parte-<a|b>`.
5. Acompanhe: `validate_content.py --coverage --stage full --subject <disc>`.

Dica: pode usar 2–3 agentes do Claude Code em paralelo (uma aula/arquivo por agente; peça gravação a cada aula): "Leia `pipeline/briefs/content.md` e produza as questões das aulas aNN–aMM de `<disciplina>`, só dos trechos sem questões".

## 6. O que cabe a cada um, por aula (trechos pendentes · páginas)

### Parte A
- **Biologia** (68 · 828): a00 7·91 · a01 3·42 · a02 4·50 · a03 4·50 · a04 2·24 · a05 3·34 · a06 5·67 · a07 4·49 · a08 6·63 · a09 3·42 · a10 3·32 · a11 2·17 · a12 2·28 · a13 8·96 · a14 4·51 · a15 4·47 · a16 2·28 · a17 2·17
- **Língua Inglesa** (23 · 278): a00 2·25 · a01 5·68 · a02 4·41 · a03 2·25 · a04 3·30 · a05 4·41 · a06 3·48

### Parte B
- **Língua Portuguesa** (54 · 708): a00 5·65 · a01 5·62 · a02 7·90 · a03 3·39 · a04 6·89 · a05 6·82 · a06 4·51 · a07 4·53 · a08 3·38 · a09 2·21 · a10 2·27 · a11 5·67 · a12 2·24
- **Dir. Penal Militar** (34 · 287): a00 4·34 · a01 2·26 · a02 1·7 · a03 1·5 · a04 5·41 · a05 1·5 · a06 1·2 · a07 1·11 · a08 6·52 · a09 6·53 · a10 4·32 · a11 2·19
- **Legislações PE** (4 · 40): a01 2·18 · a02 2·22

Ordem sugerida — A: Língua Inglesa → Biologia. B: Legislações PE → Dir. Penal Militar → Língua Portuguesa.

## 7. Como será o merge
Quando todas as frentes terminarem: `questoes-juridicas`, `questoes-parte-a`, `questoes-parte-b` e `bizus-exatas` vão para a `main`/`lancamento` (pastas disjuntas, sem conflito), `pytest` e `validate_content.py --coverage --stage full` (meta: todos os trechos com bizu e questões), depois o seed e a revisão humana (`/admin/revisao`).
