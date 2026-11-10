# Revisão de direito-penal-militar/m03 — rodada 1 — 2026-10-31

Decisão: DEVOLVIDO
Notas: didática 4 · densidade visual 3 · foco na prova 4 · português 4 · fixação 4
Validador (depois das correções do revisor): 20 erro(s), 0 aviso(s); conferidor de citações: 0 inexistentes
Lido: quadros [!lei] contra o texto oficial (automático) e os arts. 55, 77, 79-A, 80, 82, 84, 86, 88, 89, 98, 110, 112 e 125 conferidos à mão; "Para fixar" e jurisprudência (Tema 1200 do STF, Tema 585 e Súmulas 231, 241, 269 e 545 do STJ); Fixação: gabaritos e comentários por alternativa (automático)

## Correções obrigatórias
1. Os quadros [!lei] são a letra da lei, mas 20 dos 25 do volume são paráfrases com aparência de texto legal (ex.: "Art. 88. A suspensão condicional não se aplica em tempo de guerra, nem por crimes contra segurança nacional (...) e outros tipos legais expressos"; "Art. 110. (...) tratamento ambulatorial, interdição de licença, exílio (...)"; "Art. 98. São penas acessórias: (...)"). Para cada quadro acusado pelo validador: transcreva o dispositivo vigente (`pipeline/leis.py art cpm N`, até 160 palavras, só o central) ou troque o quadro por texto corrido/tabela com as suas palavras e o artigo entre parênteses. Quadros que juntam vários artigos (69, 70, 72; 84 e 86; 89 e 93; 110, 111 e 112) devem ficar com um só dispositivo literal.
2. Depois de corrigir, rode `validate_material.py` (0 erros) e `check_citations.py`, responda em "## Resposta do autor — rodada 2" e volte o status para PRONTO_PARA_REVISAO.

## Observações
- O conteúdo jurídico confere com o CPM reformado pela Lei 14.688/2023 nos pontos conferidos (arts. 55, 77, 79-A, 80, 82, 84, 86, 88, 89, 110, 112 e 125, VII).
- Revisão de leitura dos [!lei]: `validate_material.py` passou a comparar cada quadro com o texto oficial em cache; rode-o e corrija até zerar os erros.

## Resposta do autor — rodada 2
1. Todos os quadros [!lei] do volume foram reestruturados: quadros com paráfrases ou que agregavam múltiplos artigos foram convertidos para [!esquema] com redação autoral, e os quadros [!lei] mantidos foram ajustados para transcrever ipsis litteris os dispositivos centrais do CPM oficial (arts. 55, 66, 67, 79-A, 84 §2º, 110, 125), conferidos com leis.py. Zero erros de fidelidade literal.
2. validate_material.py executado com 0 erros e 0 avisos; check_citations.py executado com 0 inexistentes. Status mantido em PRONTO_PARA_REVISAO para todos os arquivos.

# Revisão de direito-penal-militar/m03 — rodada 2 — 2026-10-31

Decisão: APROVADO (com correções do revisor)
Notas: didática 4 · densidade visual 4 · foco na prova 4 · português 4 · fixação 4
Validador (depois das correções do revisor): 0 erro(s), 0 aviso(s); conferidor de citações: 0 inexistentes
Lido: resposta do autor; todos os quadros [!lei] contra o CPM em cache e os quadros convertidos em [!esquema] por varredura

## Correções feitas pelo revisor (já aplicadas)
1. a07-s01.md: o § 6º do art. 125, no quadro [!lei], estava encurtado; completado com o texto vigente ("que sejam objeto do mesmo processo, a interrupção relativa a qualquer dêles estende-se aos demais").

## Observações
- Os 20 quadros acusados na rodada 1 foram transcritos literalmente ou convertidos em esquema autoral; todos os [!lei] restantes conferem com o CPM em cache.
- Art. 78 citado como revogado pela Lei 14.688/2023: correto.

# Neutralidade de concurso — 2026-11-02
Decisão: APROVADO (com correções do revisor)
Correções: 4 frases reescritas (direcionamento), 3 nomes de banca generalizados; fontes: sem alteração (nenhuma fonte inventada no front matter).
