# Revisão de estatistica/m12 — rodada 1 — 2026-11-01

Decisão: DEVOLVIDO
Notas: didática 4 · densidade visual 4 · foco na prova 4 · português 4 · fixação 4
Validador (depois das correções do revisor): 7 erro(s), 4 aviso(s); conferidor de citações: 0 inexistentes
Lido: checagem automática de remissões, de notação e da Fixação; amostra de exercícios resolvidos

## Correções obrigatórias
1. Remissão ao material-base, proibida no conteúdo (briefing, seção 0, regra 4, e seção 18). O validador passou a acusar como ERRO:
   - frases como "Na página 9 do manual de referência", "Ponto de Atenção da Página 22", "Exemplo da página 58", "(Fonte, pág. 36)", "na página 32 da fonte teórica", "da apostila", "a aula 02";
   - em `fontes`, "Apostila Base MentorIA …" e "Apostila teórica Aula NN — MentorIA": não existe apostila MentorIA anterior, e isso é o material-base com outro nome.
   Rode `pipeline/validate_material.py` na pasta e corrija cada ocorrência: afirme a regra sem dizer de onde veio; troque títulos de quadro como "Ponto de Atenção da Página 22 (Constantes)" por um título do assunto ("Constantes em fórmulas"); em `fontes`, deixe só fontes primárias e obras publicadas que você de fato usou (documentação oficial, gramáticas, livros), no formato "Título — onde — consultado em AAAA-MM-DD".
2. Onde o texto dizia "exemplo da página N", o exemplo era o do material-base: substitua por exemplos seus (outros nomes, números e situações), como manda a seção 8 do briefing.
3. Depois de corrigir, rode `validate_material.py` (0 erros) e `check_citations.py`, responda em "## Resposta do autor — rodada 2" e volte o status para PRONTO_PARA_REVISAO.

## Observações
- O conteúdo não foi lido em detalhe nesta rodada: a devolução é pela remissão ao material-base. Na rodada 2 o revisor lê o volume.

# Neutralidade de concurso — 2026-11-02
Decisão: APROVADO (com correções do revisor)
Correções: 4 frases reescritas (direcionamento), 3 nomes de banca generalizados; fontes: removida a entrada "Apostila Base MentorIA - Estatística para Oficiais CBMPE e PMPE" (inexistente) nos 7 capítulos; mantidas Morettin & Bussab e Wooldridge
