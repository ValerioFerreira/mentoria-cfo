# Comentários das questões do banco (cadernos, treino e simulados)

As questões do site vêm dos cadernos do TecConcursos e entram sem comentário. Seu trabalho é escrever, para cada questão dos lotes que receber, um **comentário geral** e uma **nota por alternativa**. O aluno lê o comentário logo depois de responder, no caderno do plano de estudos, sem o PDF do material ao lado. O comentário tem de **ensinar**: explicar corretamente o conceito que a questão cobra, de modo que o aluno que errou entenda por que errou e o que acertou saiba por que acertou.

## Onde está cada coisa

- **O lote:** `pipeline/.cache/questoes-comentar/<disciplina>__<lote>.json`. Lá estão:
  - `trecho`, `aula` e `topicoInicial`: o assunto do lote (um trecho por lote);
  - `capitulo`: o capítulo do material MentorIA sobre o trecho (`content/material/...md`), quando existe; `resumo`: o arquivo do resumo analítico (`content/summaries/<disc>/aNN.json`, campo `analytic` do trecho);
  - `questoes[]`: `id`, `tipo` (`MULTIPLA_ESCOLHA` ou `CERTO_ERRADO`), `ano`, `assunto`, `textoBase`, `enunciado`, `alternativas[{letra, texto}]`, `gabarito` (o oficial), `contentHash` e `figuras` (caminhos de PNG);
  - `arquivoDeSaida`: onde gravar o resultado.
- **Figuras:** se a questão tem `figuras`, abra cada PNG com a ferramenta Read antes de comentar. Fórmulas e tabelas costumam estar nelas.
- **Lei:** `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <artigo>` (ex.: `art cf 37`, `art cpm 9`, `art l8112 116`); `pipeline/.venv/Scripts/python pipeline/leis.py lista` mostra as normas no cache e `buscar <norma> "<termo>"` procura um termo. **Todo artigo citado no comentário tem de ser conferido ali.** Lei que não está no cache: não cite o número do artigo; explique a regra.
- **Fonte do conteúdo:** o `capitulo` (ou, sem ele, o `resumo`) mostra os termos e a explicação que o aluno já viu; use-os quando servirem e complete com o seu conhecimento. **Nunca** abra `docs/`, PDFs, `*.ref.json`, `pipeline/summary_source.py` ou o texto do material-base: o comentário é texto original.

## Formato do arquivo de saída (`arquivoDeSaida`)

```json
{
 "lote": "<disciplina>/<nome do lote>",
 "trecho": "<disciplina>/aNN/sNN",
 "autor": "<seu nome de agente>",
 "data": "AAAA-MM-DD",
 "comentarios": [
  {
   "id": "tec_123456",
   "contentHash": "<copie do pacote>",
   "gabarito": "C",
   "comentario": "…",
   "alternativas": {"A": "Errada: …", "B": "Errada: …", "C": "Correta: …", "D": "Errada: …", "E": "Errada: …"}
  }
 ],
 "descartes": [{"id": "tec_654321", "motivo": "QUALIDADE: …"}]
}
```

- Copie `id`, `contentHash` e `gabarito` do pacote. Nunca os altere.
- Grave com um script Python que monta o objeto e chama `json.dumps(obj, ensure_ascii=False, indent=1)`, ou com a ferramenta Write. Nada de heredoc com regex no Bash (o `\b` vira caractere de controle).

## Como escrever

### Comentário geral (`comentario`): 50 a 250 palavras

1. Comece pelo que a questão pede, com as palavras dela (o conceito, a regra, o cálculo, o trecho do texto).
2. Explique a regra ou o conceito **corretamente e por completo**: definição, condição, exceção, prazo, competência, fórmula. É aqui que o aluno aprende. Prefira o porquê ao "decore".
3. Aplique a regra à questão e mostre por que o gabarito responde ao comando.
4. Em lei, cite o dispositivo (ex.: "CF, art. 37, II") só depois de conferi-lo em `leis.py`.
5. Em cálculo (Matemática, Raciocínio Lógico, Estatística, Física, Química, Contabilidade): refaça a conta e mostre o caminho, passo a passo, com fórmulas em Unicode (x², √, ≤, ×, π, Σ, x̄), sem LaTeX e sem `^`/`_`.
6. Em interpretação de texto: aponte o trecho do texto-base (parágrafo, frase, palavra) que decide a resposta.
7. Em Certo/Errado: a primeira frase diz se o item está **certo** ou **errado**, e o resto explica por quê.

Cada comentário é escrito para aquela questão. Nada de frase de modelo repetida ("Trata-se de questão que exige…", "Vamos analisar as alternativas…"), nem de introdução vazia.

### Nota por alternativa (`alternativas`): 6 a 70 palavras cada

- Uma nota para **cada** letra da questão (4 ou 5).
- Começa por **"Correta:"** (só a letra do gabarito) ou **"Errada:"** (todas as outras), seguida do porquê, com conteúdo: o erro específico daquela alternativa (o prazo certo, o conceito que ela trocou, o resultado correto da conta).
- Questão do tipo "assinale a **incorreta**" / "**exceto**": a letra do gabarito é a "Correta:" (ela responde ao comando) e a nota explica por que a afirmação é falsa; as outras são "Errada:" e a nota diz que a afirmação é verdadeira e por quê.
- Certo/Errado: `"alternativas": {}`.

### Estilo

- Português do Brasil, claro e direto; frases curtas; o aluno estuda sozinho e cansado.
- Sem jargão ("castrense", "outrossim", "hodiernamente"…).
- Sem "professor", sem nome de site, curso ou provedor de material, sem nome de banca (diga "a banca"), sem concurso, órgão ou cargo para o qual o aluno estuda (`pipeline/briefs/neutralidade.md`).
- Sem remissão ao material: nada de "como vimos no capítulo", "neste volume", "no resumo", "na página N". O comentário se explica sozinho.
- Texto puro: sem markdown, sem listas, sem negrito no `comentario` e nas notas.

## Quando NÃO comentar (vai para `descartes`)

Não escreva o comentário e registre em `descartes` `{"id": "...", "motivo": "QUALIDADE: <uma frase, com o artigo/regra>"}` quando:

- o gabarito oficial lhe parecer **errado** (explique o porquê e qual seria a resposta);
- a questão estiver **desatualizada**: a lei mudou depois da prova e hoje a resposta seria outra (diga a norma e a mudança);
- a resposta depender de figura, tabela ou texto que não está no pacote;
- o enunciado estiver truncado ou ilegível a ponto de não dar para resolver.

Na dúvida sobre o gabarito, confira a lei e refaça o raciocínio duas vezes antes de descartar. Nenhuma questão é rebaixada no banco sem decisão do dono: o descarte só a manda para a lista dele.

## Ao terminar cada lote

```
pipeline/.venv/Scripts/python pipeline/questoes/validate_comentarios.py <arquivoDeSaida>
```

Corrija todos os ERROS. Leia os AVISOS (frase repetida, coincidência com o material-base, artigo revogado) e corrija o que for problema de fato.

## Regras

- Grave só os arquivos de saída dos seus lotes. Outros agentes trabalham nos demais.
- Nunca abra `.env*`; nunca grave em banco; sem commit.
- Responda com:
  - a tabela lote · comentadas · descartadas (com o motivo de cada descarte);
  - a confirmação do validador (0 erros em cada arquivo);
  - no máximo 5 casos em que ficou em dúvida.

  Seja conciso.
