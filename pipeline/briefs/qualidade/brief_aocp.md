# Análise de questões no padrão AOCP — rodadas de auditoria com correção

Projeto: C:\Users\Administrador\Documents\Projetos\CFO-BM (leia CLAUDE.md, seção de convenções de `content/items`; e `pipeline/briefs/content.md` — é o briefing que guiou a produção das questões; e `content/style/aocp-profile.json` — estilo AOCP medido). Concurso: 2º Tenente do CBMPE, banca Instituto AOCP, prova 28/02/2027. Outros agentes editam outros arquivos/itens em paralelo.

## Sua fatia
O pedido indica: seu código (Q1/Q2), suas disciplinas, a semente e o documento. Você analisa **rodadas de 25 questões sorteadas** (gere a amostra com o script abaixo; cada rodada usa uma semente diferente = semente base + nº da rodada):

```
python <SCRATCH>\draw_questions.py <SCRATCH>\q_<codigo>_r<R>.json 25 <SEMENTE_BASE+R> <disc1,disc2,...>
```
Faça o MAIOR número de rodadas que conseguir (meta: ≥ 12 rodadas = 300 questões), priorizando a cobertura de todas as disciplinas da sua fatia (se uma disciplina ficar sub-representada, force uma rodada com ela). Cada item traz `file`, `segmentId`, `qIndex` e os campos da questão (`topic`, `pattern`, `difficulty`, `pageRef`, `statement`, `support`, `options`, `answer`, `explanation`, `literal`).

## O que verificar em CADA questão
1. **Gabarito**: a alternativa marcada em `answer` é realmente correta? Confirme no PDF da aula (`segmentId` → aula; `pageRef` = página do leitor de PDF) ou, em cálculo, refaça a conta (Python). Exatamente UMA alternativa defensável (nenhuma das outras também correta; nenhuma ambiguidade; sem depender de conhecimento ausente do trecho).
2. **Padrão AOCP**: 5 alternativas A–E; comando e estilo típicos (“Assinale a alternativa correta/incorreta”, “De acordo com…”, “Em relação a…”); enunciado claro e completo; contexto necessário presente (texto-base em `support` para leitura/idiomas; dados numéricos suficientes em cálculo); nível de 2º Tenente (nem trivial nem obscuro); negação (“INCORRETA”, “EXCETO”, “NÃO”) destacada em MAIÚSCULAS; sem “todas/nenhuma das anteriores”; assertivas romanas bem formadas.
3. **Qualidade dos distratores e vieses**: alternativas plausíveis, mesmo campo semântico, tamanhos parecidos (correta não é sistematicamente a mais longa/completa); sem alternativas duplicadas ou dicas gramaticais que entregam a resposta.
4. **Explicação**: consistente com o gabarito (sem contradição), explica por que a correta está certa e por que as tentadoras estão erradas.
5. **Fidelidade ao material**: o ponto avaliado é sustentado pelas páginas do trecho (`pageRef` dentro de startPage–endPage; a página indicada realmente trata do ponto); nada contrário ao PDF; `literal: true` só para citação exata de norma.
6. **Originalidade/higiene**: sem cópia do PDF (10 palavras seguidas), sem erro de português, sem pontuação/numeração quebrada, `pattern`/`difficulty`/`topic` coerentes.
Classifique cada achado: CRÍTICO (gabarito errado, sem resposta correta ou 2+ corretas, afirma algo falso), MAIOR (enunciado ambíguo/incompleto, explicação contraditória, pageRef errado, ponto fora do trecho), MENOR (estilo AOCP, distrator fraco, viés de tamanho, português).

## CORREÇÃO (obrigatória: documente de pronto e corrija)
Corrija cada erro direto em `content/items/<disciplina>/<aNN>.json`, na questão com aquele `segmentId` + `qIndex` (cuidado: confirme pelo `statement` antes de editar). Use a ferramenta **Edit** com strings exatas (nunca reescreva o arquivo inteiro com script — outros agentes editam os mesmos arquivos em paralelo; releia o trecho do arquivo imediatamente antes de editar). Ao corrigir: preserve 5 alternativas; se mudar o gabarito/alternativas, ajuste a explicação; mantenha o gabarito do arquivo equilibrado (cada letra ~14–26%); parafraseie (nunca 10 palavras seguidas do PDF). Se uma questão é irrecuperável, reescreva-a avaliando outro ponto do mesmo trecho (mesma quantidade de questões). NÃO altere bizus (`bizu`) nem trechos fora das questões sorteadas. Depois de cada rodada com edições, rode `PYTHONIOENCODING=utf-8 pipeline\.venv\Scripts\python pipeline\validate_content.py` e confirme que seus arquivos seguem sem erro. Não use git. Não rode seed nem scripts de segmentação.

## Como ler o PDF
`PYTHONIOENCODING=utf-8 python <SCRATCH>\pgread.py <disc>/aNN <pág> [<pág final>]` (página do leitor de PDF). Para figuras/fórmulas, abra o PDF original em `docs/` (subpastas: lingua-inglesa=01, direito-administrativo=02, lingua-portuguesa=03, direito-constitucional=04, lingua-espanhola=05, informatica=06, biologia=07, legislacoes-pe=08, quimica=09, matematica=10, estatistica=11, fisica=12, direito-penal-militar=13; arquivo “NNN - Aula NN ….pdf”) com `pipeline\.venv\Scripts\python -I` + `import pymupdf`. Scripts auxiliares só no scratchpad. `PYTHONIOENCODING=utf-8`. PDFs são protegidos (marca d’água): não copie trechos longos nem dados pessoais para o documento (máx. ~10 palavras).

## DOCUMENTAÇÃO — crie e atualize a CADA erro encontrado
Arquivo: `content\audit\qualidade\_parcial-questoes-aocp-<codigo>.md` (o orquestrador consolida os dois). Estrutura:
1. Cabeçalho (código, disciplinas, sementes, data).
2. **Métricas acumuladas** (atualize a cada rodada): rodadas e questões auditadas; questões OK × com achado; achados por severidade (CRÍTICO/MAIOR/MENOR); taxa de gabarito errado; taxa de erro por disciplina e por `pattern`; distribuição do gabarito (A–E) na amostra; % da correta mais longa; % de negações sem destaque; % de explicações problemáticas.
3. **Tabela por rodada**: rodada | questões | OK | críticos | maiores | menores.
4. **Registro de achados**: um bloco por achado — id (Q-01…), segmentId + qIndex + arquivo, severidade, categoria (gabarito / ambiguidade / padrão AOCP / distrator / explicação / fidelidade ao PDF / português), o que está errado (evidência do PDF com página; no máx. ~10 palavras citadas), correção aplicada (antes → depois, resumido) e status.
5. **Padrões recorrentes** e recomendações (ao final, para todo o banco).

## Retorno final (≤ 400 palavras, pt-BR)
Rodadas feitas, totais e taxas, os padrões de erro mais frequentes, o caminho do documento. Se o limite de uso da API cortar você, o documento já terá o que foi feito — por isso o atualize a cada rodada.
