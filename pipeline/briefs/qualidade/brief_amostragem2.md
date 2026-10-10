# Auditoria por amostragem (10 rodadas × 10 atividades): diretriz, resumo do bizu e itens C/E x PDF — COM correção

Projeto: C:\Users\Administrador\Documents\Projetos\CFO-BM (leia CLAUDE.md para contexto, em especial a seção `content/items`). Outros agentes trabalham em paralelo em outras disciplinas/tarefas.

## Sua fatia
O pedido indica: seu código (S1/S2/S3), suas disciplinas, a semente e o arquivo do documento. Gere sua amostra de 100 trechos de teoria (já com a diretriz exatamente como o site mostra ao aluno):

```
cd web && npx tsx scripts/_sample-audit.ts <SCRATCH>/amostra_<codigo>.json 100 <SEMENTE> <disc1,disc2,...>
```
Processe em **10 rodadas de 10 trechos** (itens n=1..10, 11..20, ...). Cada item traz `segmentId`, `subject`, `aulaNumber`, `diretriz`, `paginas`, `bizu.summary`, `bizu.pointers` e `bizu.certoErrado` (itens Certo/Errado de teoria + revisão, com `isTrue`).

## REGRA DE INDEPENDÊNCIA
Não consulte `docs/indice_topicos_curso.xlsx`, `content/structure`, `content/segments`, `content/overrides`, `content/edital`, `content/catalog.json` nem `pipeline/.cache` para decidir se algo está certo. A verdade é só o PDF. (Exceção: o leitor `pgread.py` abaixo lê o cache de texto das páginas do PDF — é só uma forma de ler o PDF, é permitido.)

## Como ler o PDF
- Texto rápido: `PYTHONIOENCODING=utf-8 python <SCRATCH>\pgread.py <disc>/aNN <pág> [<pág final>]` (ex.: `... quimica/a17 29 31`; a página é a do leitor de PDF = "pág." da diretriz).
- Texto em imagem/figura/fórmula: abra o PDF original na pasta `docs/` (subpastas: lingua-inglesa=01, direito-administrativo=02, lingua-portuguesa=03, direito-constitucional=04, lingua-espanhola=05, informatica=06, biologia=07, legislacoes-pe=08, quimica=09, matematica=10, estatistica=11, fisica=12, direito-penal-militar=13; arquivo "NNN - Aula NN ....pdf" com NN = `aulaNumber`) com `pipeline\.venv\Scripts\python -I` + `import pymupdf` (`doc[p-1].get_text()` e `page.get_pixmap()` para imagem).
- Scripts auxiliares só no scratchpad, nunca no projeto. Defina `PYTHONIOENCODING=utf-8`.

## O que verificar em CADA trecho
A. DIRETRIZ — (1) o tópico citado como início aparece de fato na página inicial (ou, em "Continue… dentro do tópico", a página inicial está dentro dele e o título aparece antes)? (2) "parando antes do tópico Z": Z aparece na página final ou logo após (fim+1), de modo que estudar do início ao fim da página final cobre o conteúdo antes de Z? (3) os nomes dos tópicos batem com os títulos reais do PDF (grafia, não inventados)? (4) a numeração "impressa" confere com o rodapé? (5) o intervalo é coerente (não corta uma explicação no meio nem inclui tópico alheio)?
B. RESUMO — cada afirmação factual do `summary` está no texto do intervalo (início..fim, mais a parte da pág. fim+1 antes do título seguinte, que a diretriz manda ler)? Afirmações só de fora do intervalo, inexistentes no PDF ou contraditórias = erro. Tópico relevante do intervalo ignorado pelo resumo = pequeno. Fórmulas, datas, números, artigos de lei e nomes devem bater.
C. PONTEIROS e CERTO/ERRADO — o `pageRef` de cada ponteiro leva à página onde o tópico realmente é explicado? O gabarito `isTrue` de cada item C/E está correto segundo o PDF e o item é sustentado pelo intervalo do trecho? Item ambíguo ou que avalia algo fora do trecho conta como problema.
Veredito por dimensão: OK / PEQUENO (imprecisão que não induz a erro) / ERRO (induz a estudar o lugar errado ou afirma algo falso).

## CORREÇÃO (obrigatória: documente de pronto e corrija)
- **Resumo, ponteiros (`pointers[].pageRef`/`topic`) e itens C/E (`teoria`/`revisao`)**: corrija direto em `content/items/<disciplina>/<aNN>.json` (o segmento tem o mesmo `segmentId`). Use a ferramenta **Edit** com strings exatas (nunca reescreva o arquivo inteiro com script — outros agentes editam os mesmos arquivos em paralelo; sempre releia o trecho do arquivo imediatamente antes de editar). Regras: parafraseie (nunca 10 palavras seguidas do PDF); mantenha **negrito** `**x**` e parágrafos curtos; não mude a quantidade de itens C/E nem o nº de parágrafos, salvo inevitável; se mudar um item, gabarito e explicação devem continuar corretos; `pageRef` sempre dentro de startPage–endPage do trecho; afirmação correta mas ausente do trecho (conhecimento externo) deve sair ou ser trocada por algo do trecho. NÃO altere `questions` (outros agentes cuidam delas), nem trechos fora da sua amostra.
- **Diretriz**: ela é calculada a partir de `content/segments` + `content/overrides`, que NÃO podem ser editados à mão e cuja regeração mudaria ids em todo o grupo. Portanto, para erro de diretriz: documente com evidência (página exata, título real) e a **correção proposta já pronta** (campo do override e valor). NÃO rode `segment.py`, `build_catalog.py`, `build_complements.py` nem `prisma db seed`; o orquestrador aplica todas as propostas de uma vez.
- Depois de cada rodada com edições, rode `PYTHONIOENCODING=utf-8 pipeline\.venv\Scripts\python pipeline\validate_content.py` e confirme que seus arquivos seguem sem erro. Não use git (nada de commit, stash, checkout, restore).

## DOCUMENTAÇÃO — crie e atualize SEMPRE, a cada erro encontrado (não só no fim)
Arquivo: `content\audit\qualidade\_parcial-diretrizes-bizus-<codigo>.md` (o orquestrador consolida os três). Estrutura:
1. Cabeçalho: código, disciplinas, semente, data.
2. **Métricas acumuladas** (atualize após cada rodada): trechos auditados; OK/PEQUENO/ERRO em Diretriz, Resumo, Ponteiros, C/E (contagem de itens e de itens com gabarito errado); taxa de erro por dimensão; por disciplina.
3. **Tabela por rodada**: n | segmentId | diretriz | resumo | ponteiros | C/E.
4. **Registro de achados**: um bloco por achado — id (A-01…), segmentId, dimensão, severidade, o que o site diz, o que o PDF mostra (págs. exatas; no máximo ~10 palavras citadas), correção aplicada (arquivo + o que mudou) OU proposta de override (para diretriz) e status (corrigido / proposto / falso positivo).
5. **Padrões recorrentes** e recomendações (ao final).
PROTEÇÃO: os PDFs são protegidos; não copie trechos longos nem dados pessoais (marca d'água) para o documento.

## Retorno final (≤ 400 palavras, pt-BR)
Totais por dimensão, quantos achados corrigidos × propostos, os padrões de erro mais frequentes e o caminho do documento. Se o limite de uso da API cortar você, o documento já terá o que foi feito até ali — por isso o atualize a cada rodada.
