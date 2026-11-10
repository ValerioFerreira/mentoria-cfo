# Neutralidade de concurso no material próprio (varredura de 02/11/2026)

Regra do dono: o material MentorIA é **genérico**. Ele serve a qualquer concurso do site (CBMPE, PMPE, PCPE, CFOA e os que vierem) e a qualquer banca. **Nenhum texto pode direcionar a preparação para um concurso, órgão, cargo, carreira ou banca.**

## O que reescrever

- **Direcionamento a concurso, cargo ou carreira.** Exemplos:
  - "voltado para o concurso de Oficiais do CBMPE";
  - "se você está se preparando para o Corpo de Bombeiros";
  - "para quem presta concurso de bombeiro";
  - "nas provas do CFOA";
  - "em provas para oficiais e praças";
  - "concursos militares e policiais de Pernambuco";
  - "o candidato ao CFO".

  Reescreva para qualquer leitor: "nas provas", "em concursos", "as bancas costumam…", "quem estuda este tema…".
- **Nome de banca** (AOCP, Instituto AOCP, Cebraspe, Cespe, FGV, FCC, Vunesp, IBFC, IAUPE, UPENET…): vira "a banca" / "as bancas". Ajuste a frase para continuar natural ("Em provas da banca AOCP, …" → "Nas provas, …").
- **Introduções de volume** (`volume.md`) e seções "Como a banca cobra este assunto": leia-as inteiras. É ali que o direcionamento aparece com mais frequência, inclusive sem sigla ("forças de segurança de Pernambuco", "provas militares").
- **Comentários da Fixação** (`fixacao.json`: `comentario` e `alternativas`): mesma regra. Não mexa em `id`, `gabarito`, `capitulo` nem nos enunciados das questões do banco.

## O que manter

- **Exemplo ambientado numa instituição:** "o Comandante do CBMPE determinou…", "uma guarnição de bombeiros atende…". É exemplo, não direcionamento.
- **Conteúdo legal de Pernambuco:** Estatuto dos militares, LC 470/2021, Portaria SDS e normas que citam CBMPE, PMPE ou PCPE porque **são o assunto**.
- **Termos jurídicos:** "concurso de agentes", "concurso de crimes", "concurso público" como instituto.
- **Quadros `[!lei]`:** são a letra da lei; o validador não os verifica.
- **O cabeçalho de origem de cada questão** ("AOCP 2024 · CBMPE") é montado pelo motor a partir do banco: não está nos arquivos.

## Como trabalhar

1. Liste as ocorrências do seu grupo:
   `pipeline/.venv/Scripts/python pipeline/contest_mentions.py --lista <pasta1> <pasta2>`
   - `direcionamento` e `banca` sempre se corrigem.
   - `instituicao` é só aviso: confira cada uma e corrija só se for direcionamento.
2. Edite com a ferramenta Edit, mudando o mínimo. Não mude o sentido, os artigos, os números nem a estrutura. Frases curtas, sem jargão.
3. **Fontes inventadas no front matter** (ex.: "Material didático institucional CBMPE"):
   - troque por uma fonte primária real que sustente o capítulo (lei, órgão oficial, obra publicada), conferida por você;
   - se não houver, remova a entrada;
   - registre.
4. Em cada volume tocado, acrescente ao fim do `REVISAO.md`:

   ```
   # Neutralidade de concurso — 2026-11-02
   Decisão: APROVADO (com correções do revisor)
   Correções: N frases reescritas (direcionamento), M nomes de banca generalizados; fontes: ...
   ```

   O status dos arquivos continua o mesmo.
5. **Complementos** (`content/complements/*.md`): mesma regra. Depois de editar cada um, regenere só o PDF dele:
   `pipeline/.venv/Scripts/python pipeline/build_complements.py --only <id> --no-merge`
   (o `<id>` é o nome do arquivo sem `.md`). Não há `REVISAO.md`: liste as mudanças na resposta.
6. Confira com o validador:
   `pipeline/.venv/Scripts/python pipeline/validate_material.py content/material/<disc>/<mNN>`
   - zero erros "direciona a um concurso" e "nome de banca";
   - nenhum erro novo de outro tipo (erros antigos de volumes ainda em produção podem existir: não são seus);
   - rode também `contest_mentions.py --lista <pastas> --sem-instituicao`, que deve ficar vazio.

## Regras

- Não toque em outras pastas, em `metrics/`, `volumes/`, nos briefings nem no validador.
- Nunca abra `.env*`. Sem commit.
- Windows: `PYTHONIOENCODING=utf-8`; nada de heredoc com regex no Bash.

## Resposta

Tabela pasta/volume · frases reescritas · bancas generalizadas · instituições mantidas como exemplo. Também:
- as fontes trocadas ou removidas;
- casos em dúvida (no máximo 10, com arquivo e linha);
- a confirmação de que o validador e o `contest_mentions` ficaram limpos no seu grupo.

Seja conciso.
