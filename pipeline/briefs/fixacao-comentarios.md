# Comentários das questões novas da Fixação (material próprio MentorIA)

A Fixação de cada volume foi ampliada para a quantidade média de questões comentadas do material-base (`content/material/metrics/_fixacao.json`). As questões novas já estão no `fixacao.json` do volume, com `"comentario": ""` e `"alternativas": {}`. A lista está em `pipeline/.cache/material/a-comentar.json` (volume → ids). Seu trabalho: escrever os comentários dessas questões.

## Onde está cada coisa

- **A questão:** `pipeline/.cache/material/questoes/<disciplina>__mNN.json`, em `questoes[]` pelo `id`. Lá estão `enunciado`, `textoBase`, `alternativas[{letra, texto}]`, `gabarito` (o oficial), `tipo`, `banca`, `ano` e `capitulo`.
  - **Nunca abra `*.ref.json`.**
- **O capítulo:** `content/material/<disciplina>/mNN/<aula>-<seg>.md`. O comentário deve usar a mesma explicação e os mesmos termos do capítulo.
- **Lei:** `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <art>` (por exemplo, `cf 37`, `l9784 54`, `l14133 75`). Todo artigo citado no comentário tem de ser conferido ali.
- **Regras gerais do material:** `pipeline/briefs/material.md` §10.3 a §10.5 (formato e estilo da Fixação) e `pipeline/briefs/neutralidade.md` (nada de concurso, órgão ou banca).

## Como escrever

- `comentario`, de 50 a 250 palavras: a regra que resolve a questão e por que o gabarito oficial está certo, partindo do enunciado da própria questão. Cada comentário é único; nada de frase de modelo repetida.
- `alternativas`: uma explicação por letra (de 6 a 70 palavras), começando por "Correta:" ou "Errada:", e dizendo o porquê. Comente todas as letras da questão.
  - Questão Certo/Errado: `alternativas` fica `{}`, e o comentário diz se a afirmação está certa ou errada e por quê.
- Não mude `id`, `capitulo` nem `gabarito`.
- Português claro, frases curtas, sem jargão ("castrense", "outrossim"…).
- Sem "professor", sem "Estratégia", sem nome de banca, concurso ou órgão no comentário, sem "gabarito oficial diz".
- **Gabarito que lhe pareça errado ou questão desatualizada** (a lei mudou depois da prova, a resposta depende de uma figura que não existe):
  - não escreva o comentário;
  - tire a questão de `questoes[]`;
  - acrescente em `descartes` (crie a lista, se não existir) `{"id": "...", "motivo": "QUALIDADE: <explique em uma frase, com o artigo>"}`;
  - o orquestrador repõe outra questão depois.
- Para questões de cálculo (Raciocínio Lógico): refaça a conta e mostre o caminho no comentário (fórmula em Unicode, sem LaTeX).

## Ao terminar cada volume

- `pipeline/.venv/Scripts/python pipeline/validate_material.py content/material/<disciplina>/mNN`
  - Não pode sobrar erro de comentário, alternativa, neutralidade ou repetição nas questões que você escreveu.
  - O erro de quantidade de questões pode aparecer se você descartou alguma: o orquestrador repõe.
- Acrescente ao fim do `REVISAO.md` do volume:

  ```
  # Fixação ampliada — 2026-11-02
  Decisão: APROVADO (Fixação ampliada pela média do material-base)
  Comentários novos: N · Descartadas por qualidade: M (ids)
  ```

## Regras

- Mexa só nos `fixacao.json` e nos `REVISAO.md` dos volumes do seu lote. Outros agentes trabalham nos demais volumes.
- Use a ferramenta Edit, ou um script Python que leia e regrave o JSON com `ensure_ascii=False` e `indent=1`. Nada de heredoc com regex.
- Nunca abra `.env*`; nunca grave em banco; sem commit.
- Responda com:
  - a tabela volume · comentados · descartados (com o motivo);
  - a confirmação do validador;
  - no máximo 5 casos em dúvida.

  Seja conciso.
