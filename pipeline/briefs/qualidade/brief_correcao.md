# Correção de bizus: ponteiros e resumos x páginas do trecho

Projeto: C:\Users\Administrador\Documents\Projetos\CFO-BM (leia CLAUDE.md rapidamente; foque nas regras de `content/items`).
Contexto: o validador `pipeline/check_ranges.py` (heurístico) listou, para cada trecho de teoria, alertas de dois tipos nos bizus em `content/items/<disciplina>/<aula>.json`. Sua lista de trabalho está no arquivo indicado no prompt. Cada trecho tem páginas `startPage–endPage` (a página é a do leitor de PDF, a mesma usada em `pageRef`).

Tipos de alerta:
- `ponteiro fora / deslocado / revisar`: o `pageRef` de um ponteiro (`bizu.pointers[].topic/pageRef`) pode não ser a página onde o tópico é explicado.
- `resumo com N termo(s) só fora do intervalo`: um termo em **negrito** ou número do `bizu.summary` só aparece em páginas fora do trecho (fim declarado + a parte da página seguinte que vem antes do título do próximo tópico, que a diretriz manda ler, conta como dentro).
Muitos alertas são FALSOS POSITIVOS (palavra genérica, paráfrase, termo presente em figura). Decida com o PDF, não pelo alerta.

Como ler o PDF: `PYTHONIOENCODING=utf-8 python C:\Users\ADMINI~1\AppData\Local\Temp\claude\C--Users-Administrador-Documents-Projetos-CFO-BM\b630aa62-3d12-4bad-9e2b-ce020951b53c\scratchpad\pgread.py <aula> <pág> [<pág final>]` (ex.: `... quimica/a17 29 31`). Para texto em imagem, abra o PDF original com pymupdf (`pipeline\.venv\Scripts\python -I`, pasta `docs/`, arquivo da aula). NÃO use `docs/indice_topicos_curso.xlsx`.

O que fazer em cada alerta (só se o PDF confirmar o problema):
1. PONTEIRO: ajuste `pageRef` para a página onde a explicação do tópico COMEÇA (a do título; se o título está no pé de uma página e o conteúdo vem na seguinte, use a do título só quando houver conteúdo relevante nela; senão a seguinte). Sempre dentro de startPage–endPage do trecho. Se o ponteiro estiver correto, deixe como está.
2. RESUMO: se uma afirmação do `summary` (ou um item Certo/Errado do mesmo trecho que dependa dela) NÃO está nas páginas do trecho — nem na parte da página seguinte anterior ao título do próximo tópico —, reescreva a frase para o que o trecho realmente sustenta, ou troque por outro ponto do trecho. Mantenha o estilo (negrito `**x**`, parágrafos curtos, conteúdo parafraseado — nunca copie 10 palavras seguidas do PDF), preserve o gabarito dos itens (se mudar um item, o gabarito e a explicação devem continuar corretos) e NÃO altere a quantidade de itens Certo/Errado nem o número de parágrafos do resumo, a menos que seja inevitável. Afirmações corretas mas ausentes do PDF (conhecimento externo) também devem sair ou ser substituídas por algo do trecho.
3. Não toque em questões (`questions`), em outros trechos, nem em arquivos fora das suas disciplinas.

Edição: edite o JSON preservando a formatação (indentação e ordem das chaves), com a ferramenta Edit (strings exatas), não reescrevendo o arquivo inteiro. Depois de editar uma disciplina, rode `PYTHONIOENCODING=utf-8 pipeline\.venv\Scripts\python pipeline\validate_content.py` e confirme que seus arquivos continuam [ok] (sem erro). Você pode rodar `PYTHONIOENCODING=utf-8 pipeline\.venv\Scripts\python pipeline\check_ranges.py --subject <disciplina> --out <arquivo no scratchpad>` para ver quantos alertas restam (cada agente use um nome de saída próprio).

RELATÓRIO FINAL (português, ≤ 350 palavras): quantos ponteiros corrigidos, quantos resumos/itens reescritos, quantos alertas eram falsos positivos, e a lista de qualquer coisa que exija decisão humana (ex.: erro do próprio material). Não commite nada.
