# Comentários das questões: divisão em três partes (18/11/2026)

Três agentes comentam as questões dos cadernos dos planos ativos **em paralelo**, cada um com uma parte da fila, sem lote em comum:

| Parte | Quem | Disciplinas (principais) |
|---|---|---|
| **A** | ORQUESTRADOR (a sessão que desenvolve as features de riscar e reprogramar; usa subagentes em esforço médio) | administração, contabilidade, direito administrativo, direito penal militar, legislações de PE, língua inglesa, química |
| **B** | AGENTE-B | atualidades, direito processual penal, direitos humanos, física, informática, legislação penal especial, língua portuguesa, matemática |
| **C** | AGENTE-C | biologia, direito constitucional, direito penal, estatística, história de PE, legislação PCPE, língua espanhola, raciocínio lógico |

Cada parte é uma lista de pacotes (um por linha) em `pipeline/.cache/questoes-comentar/_partes/parte-<A|B|C>.txt`. **Só o ORQUESTRADOR** gera e redistribui essas listas, regenera a fila, grava no banco e atualiza documentação. Um lote está **entregue** quando o arquivo de saída existe (`arquivoDeSaida` do pacote).

## Modelo

Use um modelo em **esforço médio**. A qualidade é conferida pelo validador e por amostras, então siga o briefing à risca.

## O que cada agente de comentário faz

1. Leia, por inteiro, `pipeline/briefs/questoes-comentarios.md` (onde está cada coisa, formato de saída, como escrever, quando descartar, como validar).
2. Trabalhe a sua lista, lote a lote, na ordem do arquivo (a ordem é a prioridade: cadernos mais próximos primeiro). Para cada pacote: leia o pacote, abra as figuras (PNG) com a ferramenta Read quando houver, consulte o capítulo/resumo indicado e confira **todo** artigo citado com `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <n>`; escreva o arquivo em `arquivoDeSaida` (em partes, nos lotes grandes) e rode o validador até 0 erros:
   `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/validate_comentarios.py <arquivoDeSaida>`
3. **Descarte em vez de comentar** (`descartes`, com o motivo) quando: o gabarito parece errado; a questão está desatualizada pela lei atual (EC 131/2023, EC 141/2026, Lei 14.688/2023 no CPM, Lei 14.133/2021, Lei 14.230/2021 etc.); duas alternativas atendem ao comando; falta figura, dado ou o destaque do enunciado se perdeu; a conta não confere com o gabarito. Decisão de rebaixar a questão no banco é do dono.
4. Erros que apareceram nas revisões e que você deve evitar: comentário ou notas de **outra** questão (leia o enunciado e as alternativas antes de escrever); nota "Correta:" fora da letra do gabarito (em "assinale a incorreta" a letra do gabarito é a "Correta:"); artigo de lei citado de memória (confira no `leis.py`; norma fora do cache: explique a regra sem número); decisão do STF/STJ citada sem certeza (explique a regra, sem número de tema); markdown no texto; palavras "professor", "estratégia", nome de banca ou de concurso; cópia de texto de lei (mais de 15 palavras seguidas: parafraseie).
5. Registre o andamento em `pipeline/.cache/coord/STATUS-COMENT-<B|C>.md` (a cada 5 lotes ou ao parar): lotes entregues, descartes (id e motivo), dúvidas, bloqueios. O orquestrador também confere o andamento pelos arquivos de saída (`dividir_partes.py --status`).
6. Quando o limite de uso o interromper, retome do primeiro lote da sua lista sem arquivo de saída. Um arquivo de saída incompleto (você estava gravando em partes) deve ser refeito por inteiro: o validador acusa questão faltando só se ela estiver no arquivo, então ao retomar abra o pacote e confira se todas as questões têm comentário ou descarte.

## Regras de convivência (mesma pasta, mesmo banco local)

- Grave **somente** os arquivos de saída dos lotes da sua parte, o seu STATUS e scripts temporários em `pipeline/.cache/<seu nome>/`. **Nenhum outro arquivo.** Sem commit, push, stash, reset.
- **Não grave no banco** (nem local nem remoto), não rode `prisma`, não regenere a fila nem os pacotes, não reinicie o banco, não abra `.env*`. A gravação no banco local é do orquestrador (`web/scripts/questoes-comentarios.ts --aplicar`), depois do validador.
- Não abra `docs/`, PDFs, `*.ref.json` nem texto do material-base: a fonte do conteúdo é o capítulo do material próprio indicado no pacote (ou o resumo) e a lei no cache.
- Sobrou lote de outra parte na sua lista? Não faça: avise em STATUS.

## Prompt para os agentes B e C (copie; troque `<B|C>`)

```
Você é o AGENTE-<B|C> de comentários de questões no projeto MentorIA (pasta C:\Users\Administrador\Documents\Projetos\CFO-BM). Mais dois agentes (o orquestrador e o outro) comentam OUTRAS partes da mesma fila ao mesmo tempo, sem lote em comum. Use um modelo em esforço médio.

1. Leia por inteiro: CLAUDE.md (só a seção "Comentários das questões") e pipeline/briefs/comentarios-3-agentes.md (regras de convivência e o que fazer). Em seguida, o briefing pipeline/briefs/questoes-comentarios.md.
2. Sua lista de pacotes (um por linha) é pipeline/.cache/questoes-comentar/_partes/parte-<B|C>.txt. Faça os lotes na ordem, até acabar a lista ou o limite de uso. Um lote está entregue quando o arquivo de saída existe e passa no validador.
3. Para cada pacote: leia o pacote, abra as figuras com Read, confira todo artigo de lei em pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <n>, escreva o arquivo em arquivoDeSaida (em partes nos lotes grandes) e rode: PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/questoes/validate_comentarios.py <arquivoDeSaida> até 0 erros.
4. Descarte (em "descartes", com o motivo) em vez de comentar: gabarito que parece errado, questão desatualizada pela lei atual, duas alternativas que atendem ao comando, figura/dado/destaque ausente, conta que não confere.
5. Grave somente os arquivos de saída dos seus lotes, seu STATUS (pipeline/.cache/coord/STATUS-COMENT-<B|C>.md, atualizado a cada 5 lotes ou ao parar) e temporários em pipeline/.cache/<seu nome>/. Não grave em banco, não regenere a fila, não faça commit, não abra .env* nem docs/.
6. Ao parar, deixe no STATUS: lotes entregues, descartes (id e motivo), até 5 dúvidas e o próximo lote.
```
