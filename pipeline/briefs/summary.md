# Briefing — Resumos de cada atividade de Teoria (analítico + sintético)

Cada trecho (`<disciplina>/aNN/sNN`) é uma atividade de Teoria de ~1 h. Para cada um você escreve **dois textos novos**, do zero, a partir do que o trecho ensina:

1. **`analytic` — resumo analítico** (markdown): substitui a leitura do material quando o aluno estiver sem tempo (Modo Turbo) ou preferir ler o resumo. Deve ser lido em **no máximo 20 minutos** (~100 palavras/min de estudo) e ser **suficiente por si só** para responder as questões do tema. O **tamanho é o que o conteúdo pedir**: `targetWords` em `content/summaries/_queue.json` é só o teto de referência (≈ 20 min); o validador bloqueia acima de +25% do alvo e abaixo de um mínimo de ~250 palavras. Não encha para chegar ao alvo.
2. **`synthetic` — resumo sintético** (lista de linhas): é o resumo da seção **Bizu** que acompanha toda atividade de Teoria. 6 a 12 pontos-chave, cada um com **o conteúdo e uma explicação breve** (110 a 320 palavras no total). Não é índice de tópicos nem frase genérica: o aluno precisa sair sabendo a regra, a exceção, o número, a fórmula.

## Como trabalhar (um trecho por vez, na ordem em que a reserva os listou)
```
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/summary_source.py <trecho>               # texto-fonte (PROTEGIDO)
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/summary_source.py <trecho> --fingerprint # copie para "fingerprint"
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/summary_queue.py --claim <seu-nome> --count 8   # reserva as próximas AULAS pendentes (JSON com os trechos); trabalhe só nelas
```
Leia o trecho INTEIRO antes de escrever. Conhecimento só do que o trecho ensina (nada de assunto de outra aula). Prioridade para o que a banca (AOCP, mas também FGV/outras nas provas militares de PE) cobra: conceitos-chave, classificações, regras e exceções, prazos e números, literalidade de artigos curtos e essenciais, comparações, pegadinhas.

## Como escrever o analítico
- **Estrutura**: abra com 1–2 frases do que o trecho cobre; depois seções `### Título` na ordem didática do trecho (mínimo 3). Use `####` para subseções, listas (`- `) para enumerações, **negrito** para termos/regras-chave, tabelas markdown para comparações e classificações (sempre com a linha `| --- | --- |`), e blocos `> 💡 Exemplo:`, `> ⚖️ Base normativa:`, `> ⚠️ Pegadinha:` quando ajudarem. Feche com `### Para fixar` (5–8 pontos de revisão rápida).
- **Conteúdo**: explique (não liste). Mostre o porquê, dê um exemplo curto, destaque exceções. Fórmulas, unidades e condições de validade em texto simples (`v = v0 + a·t`, `Q = m·c·ΔT`), sem LaTeX; cálculo só quando o trecho ensina o método (resolva um exemplo curto).
- **Voz**: português do Brasil, direta, em 2ª pessoa só quando útil. **Nunca** cite "a aula", "o PDF", "o professor", "o curso", páginas, nomes de plataforma ou de material ("conforme visto…"). O resumo precisa servir a qualquer aluno que não viu o material.
- **Tabelas e figuras do material** (o texto extraído as perde ou as embaralha): **figuras** são, em geral, só ilustração do que o texto já explica: descarte-as. Só aproveite uma figura se o texto disser que ela é a **fonte** da informação e não descrever o conteúdo logo depois dela (nesse caso, reconstrua a informação em texto). **Tabelas** costumam repetir o que o texto diz, mas, por serem dados escritos, avalie: se trazem informação relevante que não está no texto (classificações, prazos, quadros comparativos, fórmulas), extraia-a e apresente em tabela markdown ou lista; se apenas repetem, ignore. Se uma página vier vazia ou ilegível, registre em `notes`.
- **Fidelidade**: não invente. Se o material estiver errado, ambíguo ou incompleto, siga o texto legal/consenso e **registre o problema na entrega** (campo `notes` do arquivo) para revisão humana.

## Como escrever o sintético
- Cada linha: `**Ponto-chave**: explicação com o conteúdo (regra + exceção/número/exemplo)`. Cubra o trecho de ponta a ponta; ordem do trecho. Pode haver 1–2 cabeçalhos `### …` (não contam como ponto).
- Proibido: "Aspecto 1", "Priorize a fixação…", "conceitos fundamentais", linhas sem explicação, tabelas-modelo vazias.
- Deve ser **diferente** do analítico (condensado, não cópia de parágrafos).

## Originalidade (o validador rejeita)
O material do Estratégia é protegido (marca d'água). Nenhuma sequência de **10 palavras iguais** ao texto-fonte, em lugar nenhum. Parafraseie, reorganize, troque os exemplos. Citação literal só de dispositivo legal curto e essencial (e mesmo assim prefira a paráfrase). Os complementos autorais (`cNN`) são do próprio MentorIA e dispensam a checagem, mas devem ser resumidos, não copiados.

## Formato do arquivo — `content/summaries/<disciplina>/<aNN>.json` (um por aula, todos os trechos pedidos dessa aula)
```json
{"aula": "<disc>/a05", "batch": "<lote>", "status": "DRAFT", "notes": "problemas do material, dúvidas para revisão humana",
 "segments": [
  {"id": "<disc>/a05/s01",
   "fingerprint": {"startPage": 3, "endPage": 17, "startTopic": "..."},
   "analytic": "Texto de abertura.\n\n### Primeira seção\n...",
   "synthetic": ["**Ponto**: explicação", "**Outro ponto**: explicação"]}
 ]}
```
- Se o arquivo da aula já existir, **acrescente** os trechos novos sem apagar os existentes (leia antes de escrever). Escreva com a ferramenta **Write** (aspas internas escapadas, `\n` nas quebras); heredoc longo no Bash quebra com aspas.
- UTF-8, acentos corretos, sem `�`.

## Validação (a cada aula, antes de passar para a próxima)
```
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_summaries.py content/summaries/<disc>/<aNN>.json
```
Corrija todos os erros (tamanho, seções, originalidade, impressão digital, markdown) e revalide. Depois faça uma **segunda passada** como aluno e como a banca: está correto? falta algum ponto cobrável? algum trecho do texto-fonte ficou colado demais?

## Entrega
Por aula: trechos feitos, palavras do analítico (vs alvo) e problemas do material. Não cole o conteúdo produzido na resposta. **Não** edite `content/items/`, o catálogo nem arquivos de outras disciplinas; não faça commit (o orquestrador consolida).
