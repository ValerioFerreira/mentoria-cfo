# Briefing — Auditoria estrutural por disciplina (MentorIA / CFO-BM)

Você é responsável por UMA disciplina. Outras disciplinas estão sendo auditadas em paralelo por outros agentes: **nunca edite arquivos de outra disciplina nem arquivos globais**.

## Contexto
- Repositório: `C:\Users\Administrador\Documents\Projetos\CFO-BM`. Leia `CLAUDE.md` primeiro (convenções, regras de segmentação, proteção dos PDFs).
- Site que monta o plano de estudos para 2º Tenente CBMPE (banca Instituto AOCP, prova 28/02/2027) e aponta onde estudar no material do Estratégia (aula, página, tópico).
- Edital (Anexo II, conteúdo do 2º Tenente): `pipeline/.cache/edital_2ten.txt` — leia o trecho da sua disciplina inteiro.
- Texto dos PDFs por página (cache): `pipeline/.cache/pages/*.json`. **Nunca copie texto dos PDFs para `content/`** (títulos de tópicos podem ser citados; o resto, só paráfrase). `docs/` nunca é versionado.
- Estrutura gerada: `content/structure/<disciplina>.json` (por aula: `pageMap`, `topics`, `theoryRuns`, `commentedRuns`, `flags`) e `content/segments/<disciplina>.json` (trechos de teoria de ~1 h, id `<disciplina>/aNN/sNN`).
- Catálogo: `content/catalog.json` (somente leitura para você). Lacunas: `content/gaps.json` (somente leitura). Complementos autorais: `content/complements/*.md` (aulas `cNN`, fonte `authored`).
- Python: `pipeline/.venv/Scripts/python`. Defina `PYTHONIOENCODING=utf-8`.

## Ferramentas
```
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN              # mapa de páginas, tópicos, trechos
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --heads      # 1ª linha útil de cada página (varredura)
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --pages 10-14 [--chars 2500]
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc>/aNN --grep "regex sem acento"
pipeline/.venv/Scripts/python pipeline/inspect_aula.py <disc> --grep "regex"   # busca na disciplina toda
pipeline/.venv/Scripts/python pipeline/edital_audit.py --subject <disc>        # contagem por regex (heurística grosseira)
pipeline/.venv/Scripts/python pipeline/segment.py --subject <disc>             # regenera SÓ structure/ e segments/ da sua disciplina
```
Mapa de páginas: T teoria · C questões comentadas · L lista sem comentário · K gabarito · S resumo/mapa mental · F abertura/sumário · B fechamento · X extra (use `"EXTRA"` para fora do escopo do edital, página duplicada no PDF ou leitura opcional).
Só páginas T viram trechos de Teoria. C/L alimentam a atividade Fixação (o aluno resolve as questões do PDF). Resumo (S) não vira atividade.

## Como corrigir a estrutura: `content/overrides/<disciplina>.json` (o SEU arquivo)
Formato (todas as chaves opcionais, por aula):
```json
{"aulas": {
  "<disc>/a05": {
    "pages": {"40-62": "COMMENTED", "63": "THEORY"},          // tipo de página: THEORY|COMMENTED|LIST|SUMMARY|KEY|FRONT|BACK
    "headings": [{"page": 23, "title": "Atributos do ato", "level": 1}],  // subtítulo real ausente do índice
    "dropHeadings": [{"page": 30, "title": "Título falso"}],              // falso subtítulo (legenda, exemplo, frase)
    "cuts": [23, 41],                                           // páginas que DEVEM iniciar um trecho (início de tópico)
    "edital": "yes|partial|no", "kind": "theory|practice", "note": "explicação curta (aparece no catálogo)"
  }
}}
```
Depois de editar, rode `segment.py --subject <disc>` e confira com `inspect_aula.py`. O algoritmo particiona cada sequência contínua de teoria em trechos de 6–17 págs. (alvo ≈ 12 de "carga"), preferindo cortes em inícios de tópico; `cuts` força cortes. Use `cuts` com parcimônia e só em inícios de tópico reais; um trecho deve ficar com 6–17 págs. (teto 17 absoluto, o ideal é 10–17; trechos menores só quando o assunto é autônomo e curto).
Não edite `content/overrides.json` (geral), nem código do pipeline/web, nem `catalog.json`, `gaps.json`, outras disciplinas. **Não rode** `build_catalog.py`, `build_complements.py`, seed ou migrações. Se precisar de mudança de código ou de arquivo global, descreva-a no relatório (seção "Pedidos ao orquestrador").

## O que auditar (faça de verdade, aula por aula; não confie na estrutura atual)
1. **Edital → material.** Quebre o conteúdo da sua disciplina no edital em itens/subitens tão granulares quanto o edital lista. Para cada um: localize no material (aula, páginas), confirme lendo o texto que o conteúdo é realmente ensinado (não só citado), verifique se a página está classificada como T e cai num trecho coerente. Status: `covered` | `partial` (só parte do item, ou tratamento muito raso) | `complement` (coberto por complemento autoral `cNN`) | `gap` (ausente) | `elsewhere` (coberto em outra disciplina — diga onde, ex.: contagem/probabilidade em Estatística).
2. **Material → estrutura (auditoria inversa, obrigatória).** Para cada aula, varra TODAS as páginas com `--heads` (e leia páginas suspeitas com `--pages`). Procure: teoria classificada como C/L/S/F/B (conteúdo perdido); questões/gabarito/resumo classificados como T (inflam a teoria); subtítulos importantes ignorados; falsos subtítulos; tópicos indexados na aula errada; páginas iniciais/finais erradas. Classifique cada descoberta: `já corretamente indexada` | `indexada no lugar errado` | `subindexada` | `superfragmentada` | `conteúdo complementar` | `possível fora do escopo` | `necessita revisão humana`.
3. **Divisão pedagógica de cada aula.** Pergunte: "se eu projetasse hoje a melhor divisão desta aula para este concurso, manteria estes trechos?" Considere coerência temática, subtítulos, densidade, carga cognitiva, autonomia, possibilidade de gerar questões específicas, relação com o edital, risco de misturar assuntos. Corte em inícios de tópico naturais (use `cuts`/`headings`). Não faça mudanças cosméticas: cada override precisa de motivo concreto.
4. **Aulas inteiras.** Aula fora do edital → `"edital": "no"` (sai do plano); parcialmente → `"partial"` com nota. Aula que é só prova/questões comentadas → todas as páginas C e `"kind": "practice"`.
5. **Lacunas e complementos** (`content/gaps.json`, `content/complements/*.md` da sua disciplina, se houver). Confirme no PDF cada lacuna. Se o material cobre, é falsa lacuna (diga). Se não cobre e não há complemento, registre. Se há complemento, avalie se ele é suficiente para o peso do item na prova e se tem erros. Não crie conteúdo duplicado. Você PODE editar os `.md` de complemento da SUA disciplina para corrigir erros ou completar (conteúdo original/parafraseado a partir do texto legal oficial; nada copiado do Estratégia); diga no relatório o que mudou. Não crie complementos novos sem necessidade clara — se achar necessário, descreva no relatório (o orquestrador decide).

## Entregáveis (todos em pt-BR)
1. `content/overrides/<disciplina>.json` — as correções (pode ficar `{"aulas": {}}` se nada precisar mudar).
2. `content/edital/<disciplina>.json` — mapa edital → material, depois das suas correções:
```json
{"subject": "<disc>", "items": [
  {"id": "3.2", "item": "Texto curto do item/subitem do edital", "status": "covered|partial|complement|gap|elsewhere",
   "where": [{"aula": "<disc>/a05", "pages": "23-31", "topic": "título do tópico no PDF"}],
   "notes": "opcional: ressalva, profundidade, conflito"}
 ],
 "inverse": [{"aula": "<disc>/a03", "pages": "40-44", "topic": "...", "class": "possível fora do escopo", "notes": "..."}]}
```
   (`where` usa páginas do PDF, não ids de trecho; o orquestrador calcula os trechos.)
3. `content/audit/<disciplina>.md` — relatório objetivo: aulas e páginas auditadas; correções feitas (assunto adicionado/movido/dividido/agrupado, páginas e trechos corrigidos) com o motivo; tabela de cobertura do edital; achados da auditoria inversa classificados; lacunas/complementos; **pendências** (o que não pôde ser resolvido, exige validação humana, ambiguidade no material, conflito edital × PDF). Não esconda incertezas. Sem texto copiado dos PDFs.
4. Na resposta final (curta, ≤ 25 linhas): números (aulas, páginas de teoria antes/depois, trechos antes/depois), correções principais, pendências principais, pedidos ao orquestrador.

Antes de terminar, rode `segment.py --subject <disc>` uma última vez e confirme que não há trecho > 17 págs. e que os arquivos JSON são válidos.
