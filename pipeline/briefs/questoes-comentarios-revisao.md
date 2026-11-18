# Revisão dos comentários aproveitados da Fixação

Os comentários da Fixação do material (`content/material/**/fixacao.json`) foram convertidos para comentários das questões do banco em `content/questoes/comentarios/<disciplina>/fixacao-mNN.json`. Na conversão (16/11/2026) apareceram comentários **escritos para outra questão** (ex.: questão sobre o grupo "Estilos" do Excel com comentário sobre "Mesclar e Centralizar"; questão de inglês sobre acoplamento de testes de software com comentário sobre acoplamentos mecânicos). Por isso nenhum desses arquivos é publicado antes da sua revisão (`"revisao": "pendente"`).

O padrão de qualidade e de formato é o de `pipeline/briefs/questoes-comentarios.md`: **leia-o primeiro, por inteiro**. Esta revisão aplica aquele padrão a comentários que já existem.

## O que fazer em cada arquivo da sua lista

1. Monte a lista das questões do arquivo com o texto completo:
   `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/questao_texto.py <arquivo fixacao-mNN.json>`
   (imprime, para cada id: enunciado, texto-base, alternativas, gabarito, figuras e o comentário atual com as notas).
2. Para **cada** questão, confira:
   - **Aderência:** o comentário e as notas tratam desta questão (mesmo assunto, mesmas alternativas)? A nota de cada letra fala do conteúdo daquela letra?
   - **Correção:** o conceito, a regra, o artigo de lei (confira em `pipeline/leis.py`) e a conta estão certos? O comentário mostra por que o gabarito responde ao comando?
   - **Forma:** 50–250 palavras; notas "Correta:"/"Errada:" (só o gabarito é "Correta:"); sem remissão ao material; sem jargão; texto puro.
3. Decida:
   - **OK:** mantenha.
   - **Ajuste:** corrija o trecho errado ou fraco (erro pontual, nota vaga, artigo trocado).
   - **Reescrita:** comentário de outra questão, errado no conceito ou que não explica: reescreva o comentário e as notas do zero, seguindo o briefing de autoria.
   - **Descarte:** gabarito que lhe parece errado, questão desatualizada ou dependente de figura ausente: tire de `comentarios` e ponha em `descartes` com `{"id": "...", "motivo": "QUALIDADE: ..."}`.
4. Registre cada problema encontrado em `revisaoNotas` (lista no nível do arquivo): `{"id": "...", "problema": "TROCADO" | "ERRO" | "AJUSTE" | "DESCARTE", "detalhe": "<uma frase>"}`. Questão OK não entra. Essa lista volta para o dono, porque o mesmo comentário está no PDF do material.
5. No fim do arquivo, troque `"revisao": "pendente"` por `"revisao": "<seu nome de agente> 2026-11-16"`.
6. Rode o validador até 0 erros:
   `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/validate_comentarios.py <arquivo>`

Não altere `id`, `contentHash` nem `gabarito`. Grave com um script Python (`json.dumps(obj, ensure_ascii=False, indent=1)`) ou com Edit; nada de heredoc com regex no Bash.

## Regras

- Mexa só nos arquivos da sua lista. Não mexa no `content/material/**/fixacao.json` (o material é corrigido à parte).
- Nunca abra `.env*`, `docs/`, PDFs ou `*.ref.json`; nunca grave em banco; sem commit.
- Responda com a tabela arquivo · questões · OK · ajustadas · reescritas (trocadas) · descartadas, a confirmação do validador e no máximo 5 casos de dúvida. Seja conciso.
