# Mensagens de início para os agentes autores (copiar e colar)

Cada agente roda numa sessão própria do Claude Code, com a pasta `C:\Users\Administrador\Documents\Projetos\CFO-BM` aberta. Mande **um volume por sessão**. Primeiro o piloto (dois agentes em paralelo); a onda 1 só segue depois da revisão do piloto.

---

## Piloto em uma única mensagem (um coordenador abre os dois autores em paralelo)

```
Você coordena o PILOTO do material próprio MentorIA. Você não escreve conteúdo: abre dois autores em paralelo, confere a entrega e me devolve os dados para calibragem.

1. Abra DOIS subagentes ao mesmo tempo (ferramenta Agent, em paralelo, na mesma mensagem), cada um com o texto de "Piloto · agente 1" e "Piloto · agente 2" de pipeline/briefs/material-inicio.md:
   - AGENTE-MAT-01 → legislacoes-pe/m01
   - AGENTE-MAT-02 → direito-penal-militar/m01
   Não leia o briefing inteiro você mesmo; os autores leem.
2. Quando os dois terminarem, rode (só leitura):
   PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py content/material/legislacoes-pe/m01 --json
   PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py content/material/direito-penal-militar/m01 --json
   Se algum autor entregou com ERRO no validador, devolva a ele (SendMessage) a lista de erros para corrigir, uma vez, e rode de novo.
3. Responda com o RELATÓRIO DE CALIBRAGEM abaixo e PARE. Não comece outros volumes, não faça commit, não edite arquivos fora das duas pastas.

RELATÓRIO DE CALIBRAGEM (para o revisor)
A. Por capítulo (tabela): arquivo · importância · palavras/meta · visuais/meta · quadros/meta · cobertura (nota) · palavras coincidentes com a fonte (copied) · nº de avisos.
B. Validador: erros finais (devem ser 0) e a lista completa de AVISOS restantes, com a justificativa do autor para cada um.
C. Fixação de cada volume: nº de questões, quantas AOCP, quantas inéditas (do banco e novas), questões descartadas e por quê (gabarito duvidoso, figura, lei mudada).
D. Metas: em quais capítulos a meta de palavras, de visuais ou de quadros pareceu alta ou baixa demais para o conteúdo, e por quê (palavras do próprio autor).
E. Fontes oficiais usadas (lista) e qualquer norma que faltou no cache (pipeline/leis.py) ou que exigiu web.
F. Problemas do material-base encontrados (desatualização, erro) e dúvidas de conteúdo deixadas em "notas".
G. Ferramentas: qualquer erro, lentidão ou instrução confusa em material_ficha.py, validate_material.py, leis.py, material-questoes.ts ou no briefing.
H. Custo: uso aproximado de tokens e tempo de cada autor (o que a ferramenta Agent informar ao terminar).
```

---

## Piloto · agente 1

```
Você é o AGENTE-MAT-01, autor do material próprio MentorIA.

1. Leia por inteiro pipeline/briefs/material.md. Da seção 16, leia só "Direito Administrativo, Constitucional, Penal… Legislações PE".
2. Produza o volume legislacoes-pe/m01 (Estatuto dos Militares de Pernambuco) completo: volume.md, os 3 capítulos e fixacao.json, seguindo o passo a passo da seção 12 e as regras de economia da seção 12.1.
3. Valide com pipeline/validate_material.py até zerar os erros, faça a autorrevisão (seção 13) e mude o status de todos os arquivos para "PRONTO_PARA_REVISAO".
4. Responda com o relatório da seção 15 e PARE. Não comece outro volume.

Trabalhe só em content/material/legislacoes-pe/m01/. Não faça commit, não grave no banco e não edite nenhum outro arquivo.
```

## Piloto · agente 2

```
Você é o AGENTE-MAT-02, autor do material próprio MentorIA.

1. Leia por inteiro pipeline/briefs/material.md. Da seção 16, leia só "Direito Administrativo, Constitucional, Penal… Legislações PE".
2. Produza o volume direito-penal-militar/m01 (Aplicação da lei penal militar) completo: volume.md, os 4 capítulos e fixacao.json, seguindo o passo a passo da seção 12 e as regras de economia da seção 12.1. Atenção à seção 10.2: confira na lei o gabarito de toda inédita MentorIA de Direito Penal Militar antes de usá-la.
3. Valide com pipeline/validate_material.py até zerar os erros, faça a autorrevisão (seção 13) e mude o status de todos os arquivos para "PRONTO_PARA_REVISAO".
4. Responda com o relatório da seção 15 e PARE. Não comece outro volume.

Trabalhe só em content/material/direito-penal-militar/m01/. Não faça commit, não grave no banco e não edite nenhum outro arquivo.
```

---

## Depois do piloto aprovado (modelo para a onda 1)

```
Você é o AGENTE-MAT-<NN>, autor do material próprio MentorIA.

1. Leia por inteiro pipeline/briefs/material.md. Da seção 16, leia só a parte da sua disciplina.
2. Pegue o primeiro volume pendente da onda 1 de <disciplina>:
   PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --proximos --onda 1 -n 20
   (escolha o primeiro da lista que seja de <disciplina>; crie a pasta e o volume.md na hora para reservá-lo).
3. Produza o volume completo seguindo as seções 12 e 12.1, valide até zerar os erros, faça a autorrevisão e mude o status para "PRONTO_PARA_REVISAO".
4. Responda com o relatório da seção 15 e PARE.

Trabalhe só na pasta do seu volume. Não faça commit, não grave no banco e não edite nenhum outro arquivo.
```

Dê a cada agente simultâneo uma disciplina diferente, para não haver disputa pelo mesmo volume. O orquestrador revisa cada volume entregue com `pipeline/briefs/material-revisao.md`.

---

## Correção depois da revisão (rodada 2 do piloto)

```
Você coordena a RODADA 2 do piloto do material próprio MentorIA. Você não escreve conteúdo.

1. Abra DOIS subagentes ao mesmo tempo (ferramenta Agent, em paralelo, na mesma mensagem):
   - AGENTE-MAT-01 → corrigir content/material/legislacoes-pe/m01
   - AGENTE-MAT-02 → corrigir content/material/direito-penal-militar/m01
   Mensagem para cada um:
   "Você é o AGENTE-MAT-0X. Seu volume <volume> foi DEVOLVIDO. Leia o REVISAO.md da pasta do volume e, do briefing pipeline/briefs/material.md, as seções 5.2 (Voz e estilo), 6.1 e 18, que foram atualizadas. Corrija TODOS os itens de 'Correções obrigatórias' com edições pontuais (Edit, sem reescrever arquivos inteiros, salvo onde o REVISAO pedir reescrita), conferindo cada número de artigo com pipeline/leis.py. Atenda também às 'Melhorias pedidas'. Revalide com pipeline/validate_material.py até zerar os erros e resolver os avisos de estilo. Ao fim do REVISAO.md acrescente '## Resposta do autor — rodada 1' com uma linha por item (número do item: o que foi feito). Mude o status de todos os arquivos para PRONTO_PARA_REVISAO e PARE. Trabalhe só nessa pasta; sem commit."
2. Quando os dois terminarem, rode (só leitura) o validador com --json nas duas pastas.
3. Responda e PARE:
   A. Por volume: itens corrigidos / itens do REVISAO (e qualquer item que o autor não conseguiu resolver, com o motivo).
   B. Saída do validador: erros (devem ser 0) e avisos restantes.
   C. Por capítulo: palavras, quadros, média de palavras por frase (sentenceWords) e jargão (jargon) do --json.
   D. Custo de cada autor (tokens e tempo informados pela ferramenta Agent).
```

---

## Onda 1 em lotes (depois do piloto aprovado em 29/10/2026)

Cada lote tem 4 volumes de disciplinas diferentes, produzidos em paralelo. O coordenador para no fim do lote e o revisor revisa antes do lote seguinte. Copie a mensagem abaixo e troque `<N>` pelo número do lote.

```
Você coordena o LOTE <N> da onda 1 do material próprio MentorIA. Você não escreve conteúdo.

1. Liste os pendentes (só leitura):
   PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --proximos --onda 1 -n 40
   Escolha os 4 PRIMEIROS da lista que sejam de 4 disciplinas DIFERENTES.
2. Abra 4 subagentes ao mesmo tempo (ferramenta Agent, em paralelo, na mesma mensagem), um por volume, com o identificador AGENTE-MAT-<NN> (continue a numeração a partir do 03) e esta mensagem:
   "Você é o AGENTE-MAT-<NN>, autor do material próprio MentorIA. Leia por inteiro pipeline/briefs/material.md (da seção 16, só a parte da sua disciplina). Produza o volume <volume> completo (volume.md, todos os capítulos e fixacao.json), seguindo as seções 12 e 12.1. Confira TODO número de artigo com pipeline/leis.py antes de escrevê-lo (seção 6.1). Valide com pipeline/validate_material.py até zerar erros e avisos (aviso que restar, justifique em 'notas'), faça a autorrevisão da seção 13, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e responda com o relatório da seção 15. Trabalhe só em content/material/<disciplina>/<mNN>/; sem commit, sem gravar no banco."
3. Quando os 4 terminarem, rode o validador com --json em cada pasta (só leitura). Se algum ficou com ERRO, devolva ao autor (SendMessage) uma vez e rode de novo.
4. Responda e PARE:
   A. Por capítulo: arquivo · importância · palavras/meta · visuais/meta · quadros/meta · cobertura · copied · sentenceWords · jargon · nº de avisos.
   B. Avisos restantes com a justificativa do autor.
   C. Fixação por volume: total, AOCP, inéditas (do banco/novas), descartes relevantes.
   D. Problemas do material-base e dúvidas deixadas em "notas".
   E. Problemas de ferramenta ou de instrução.
   F. Custo e tempo de cada autor.
```

---

## Lotes em sequência contínua (a partir do lote 2, 29/10/2026)

O coordenador encadeia lotes sem esperar a revisão. Cada lote tem 4 volumes de disciplinas diferentes, sempre nesta ordem de prioridade:
1. **CORREÇÃO**: volumes que o revisor devolveu;
2. **RETOMAR**: volumes que ficaram pela metade;
3. **NOVO**: volumes da fila.

O revisor lê os relatórios em `content/material/_lotes/` quando puder e marca cada volume APROVADO ou DEVOLVIDO. O que ele devolver entra sozinho no lote seguinte. Para começar, ou para continuar depois de uma parada, cole a mensagem abaixo numa sessão nova. Ela descobre sozinha em que lote está.

```
Você coordena a produção CONTÍNUA do material próprio MentorIA (onda 1). Você não escreve conteúdo. Trabalhe em ciclos de lote, um atrás do outro, SEM pedir confirmação entre eles.

CICLO DE UM LOTE
1. Número do lote: 1 + o maior N entre os arquivos content/material/_lotes/lote-NN.md (se a pasta não existir, comece em 2).
2. Seleção (só leitura): PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --lote 4 --onda 1
   - Se a saída começar com "FIM", vá para PARADA.
   - Crie content/material/_lotes/lote-NN.md com: data e hora de início, e uma linha por volume (tipo, volume, título, autor).
3. Abra os subagentes ao mesmo tempo (um por volume, em paralelo, na mesma mensagem). Identificadores AGENTE-MAT-<NN>: continue a numeração a partir do maior já usado (veja o campo "autor" dos volumes existentes; o lote 1 usou até 06).
   - NOVO → "Você é o AGENTE-MAT-<NN>, autor do material próprio MentorIA. Leia por inteiro pipeline/briefs/material.md (da seção 16, só a parte da sua disciplina). Produza o volume <volume> completo (volume.md, todos os capítulos e fixacao.json), seguindo as seções 12 e 12.1. Confira TODO número de artigo com pipeline/leis.py e rode pipeline/check_citations.py na pasta (zero inexistentes). Valide com pipeline/validate_material.py até zerar erros e avisos (aviso que restar, justifique em 'notas'), faça a autorrevisão da seção 13, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e responda com o relatório da seção 15. Trabalhe só em content/material/<disciplina>/<mNN>/; sem commit, sem gravar no banco."
   - CORRECAO → "Você é o AGENTE-MAT-<NN>. O volume <volume> foi DEVOLVIDO pelo revisor. Leia o REVISAO.md da pasta (a rodada mais recente) e, do briefing pipeline/briefs/material.md, as seções 5.2, 6.1, 12.1 e 18. Corrija TODOS os itens de 'Correções obrigatórias' com edições pontuais (Edit), conferindo artigos com pipeline/leis.py e pipeline/check_citations.py. Ao fim do REVISAO.md acrescente '## Resposta do autor — rodada <R>' com uma linha por item. Revalide até zerar erros, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e responda com a lista de itens corrigidos. Trabalhe só nessa pasta; sem commit."
   - RETOMAR → igual a NOVO, mas: "A pasta já tem arquivos de um autor anterior que não terminou. Aproveite o que estiver correto, complete o que falta e siga o mesmo fluxo."
4. Quando TODOS os autores do lote terminarem:
   a. Para cada pasta: rode pipeline/check_citations.py <pasta> e pipeline/validate_material.py <pasta>. Se houver artigo inexistente ou ERRO, devolva ao mesmo autor (SendMessage) UMA vez e rode de novo.
   b. Autor que falhar por erro da ferramenta: reabra-o uma vez. Se falhar de novo, registre no relatório e deixe a pasta como está (no próximo lote ela volta como RETOMAR).
   c. Grave a validação no relatório: PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py --relatorio content/material/_lotes/lote-NN.md <as pastas do lote>
   d. Acrescente ao fim do lote-NN.md (texto curto, sem copiar o conteúdo dos volumes): "Notas dos autores" (problemas do material-base, dúvidas em 'notas'), "Ferramentas" (falhas, reaberturas, devoluções do passo a), "Custo" (tempo e tokens de cada autor) e a hora de término.
5. Comece IMEDIATAMENTE o próximo ciclo (volte ao passo 1). Não espere o revisor.

PARADA (escreva uma linha final e pare só nestes casos):
- A seleção respondeu "FIM": escreva "ONDA 1 CONCLUÍDA: aguardando revisão".
- Você completou 5 lotes nesta sessão (o contexto fica grande): escreva "PAUSA: continuar no lote <próximo número> numa sessão nova".
- Dois lotes seguidos com um mesmo volume que falhou duas vezes: escreva "BLOQUEIO: <volume>, <motivo>".

Regras: nunca faça commit, nunca grave no banco, nunca edite arquivos fora de content/material/<disciplina>/<mNN>/ e de content/material/_lotes/. Nunca altere um REVISAO.md além de deixar o autor acrescentar a resposta. Nunca mude um status APROVADO ou DEVOLVIDO: isso é do revisor.
```

Para o revisor: os relatórios ficam em `content/material/_lotes/`. Para revisar o que já foi entregue, use `validate_material.py --status --wave 1` (volumes em PRONTO_PARA_REVISAO) e siga `pipeline/briefs/material-revisao.md`.

---

## Frentes paralelas B e C (a partir de 29/10/2026)

Três coordenadores rodam ao mesmo tempo, cada um numa sessão própria, sem disputar volumes. Todos seguem a **mesma fila, na ordem das ondas: CFOA primeiro** (decisão do dono, 29/10/2026), depois CFO BM, PCPE e CFHP BM. A regra está em `content/material/_lotes/frentes.json` e é aplicada pelo seletor `material_ficha.py --lote 4 --frente X`:
- A seleção **reserva** cada volume NOVO na hora (cria a pasta com um arquivo `.frente`, de forma atômica), então duas frentes nunca pegam o mesmo volume. Por isso a seleção roda **uma única vez por lote**; `--simular` só mostra, sem reservar.
- RETOMAR e CORRECAO só pegam volumes da própria frente (pasta antiga sem `.frente` é da frente A).
- No mesmo lote, nunca duas vezes a mesma disciplina; entre frentes, a mesma disciplina pode correr em volumes diferentes.
- Um volume-par (seção 9 do briefing) espera até que a base seja entregue.
- A frente A (o coordenador contínuo acima, prompt sem mudança, `--onda 1`) para ao fim do CFOA; B e C seguem pela fila nas ondas seguintes. Atualidades fica reservada (é escrita perto da prova).

Relatórios: `_lotes/lote-NN.md` (A), `_lotes/B/lote-NN.md` e `_lotes/C/lote-NN.md`. Autores: `AGENTE-MAT-NN`, `AGENTE-MATB-NN` e `AGENTE-MATC-NN`.

O prompt abaixo serve às duas frentes: troque `<F>` por B ou C.

```
Você coordena a FRENTE <F> da produção CONTÍNUA do material próprio MentorIA. Outros dois coordenadores trabalham ao mesmo tempo na mesma fila (CFOA primeiro); o seletor reserva cada volume que lhe entrega (content/material/_lotes/frentes.json), então não há disputa. Você não escreve conteúdo. Trabalhe em ciclos de lote, um atrás do outro, SEM pedir confirmação entre eles.

CICLO DE UM LOTE
1. Número do lote: 1 + o maior NN entre os arquivos content/material/_lotes/<F>/lote-NN.md (se não houver nenhum, comece em 01). Ignore os relatórios de outras pastas.
2. Seleção (só leitura): PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --lote 4 --frente <F>
   - Rode esse comando UMA única vez por lote (ele reserva os volumes) e use exatamente a lista que ele devolver; nunca escolha volumes por outra listagem nem crie pastas de volume por conta própria.
   - Se a saída começar com "FIM", vá para PARADA.
   - Crie content/material/_lotes/<F>/lote-NN.md com: data e hora de início, e uma linha por volume (tipo, volume, título, autor).
3. Abra os subagentes ao mesmo tempo (um por volume, em paralelo, na mesma mensagem). Identificadores AGENTE-MAT<F>-<NN>, começando em 01 e continuando a partir do maior já usado nos seus relatórios.
   - NOVO → "Você é o AGENTE-MAT<F>-<NN>, autor do material próprio MentorIA. Leia por inteiro pipeline/briefs/material.md (da seção 16, só a parte da sua disciplina). Produza o volume <volume> completo (volume.md, todos os capítulos e fixacao.json), seguindo as seções 12 e 12.1. As questões do banco para a Fixação já estão exportadas em pipeline/.cache/material/questoes/ (a ficha mostra o arquivo). Confira na fonte oficial todo número de artigo, fórmula, constante e dado numérico (seção 6.1; legislação com pipeline/leis.py e pipeline/check_citations.py na pasta, zero inexistentes) e refaça as contas de todo exemplo resolvido. Valide com pipeline/validate_material.py até zerar erros e avisos (aviso que restar, justifique em 'notas'), faça a autorrevisão da seção 13, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e responda com o relatório da seção 15. Trabalhe só em content/material/<disciplina>/<mNN>/; sem commit, sem gravar no banco."
   - CORRECAO → "Você é o AGENTE-MAT<F>-<NN>. O volume <volume> foi DEVOLVIDO pelo revisor. Leia o REVISAO.md da pasta (a rodada mais recente) e, do briefing pipeline/briefs/material.md, as seções 5.2, 6.1, 12.1 e 18. Corrija TODOS os itens de 'Correções obrigatórias' com edições pontuais (Edit), conferindo cada dado na fonte oficial. Ao fim do REVISAO.md acrescente '## Resposta do autor — rodada <R>' com uma linha por item. Revalide até zerar erros, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e responda com a lista de itens corrigidos. Trabalhe só nessa pasta; sem commit."
   - RETOMAR → igual a NOVO, mas: "A pasta já tem arquivos de um autor anterior que não terminou. Aproveite o que estiver correto, complete o que falta e siga o mesmo fluxo."
4. Quando TODOS os autores do lote terminarem:
   a. Para cada pasta: rode pipeline/check_citations.py <pasta> e pipeline/validate_material.py <pasta>. Se houver artigo inexistente ou ERRO, devolva ao mesmo autor (SendMessage) UMA vez e rode de novo.
   b. Autor que falhar por erro da ferramenta: reabra-o uma vez. Se falhar de novo, registre no relatório e deixe a pasta como está (no próximo lote ela volta como RETOMAR).
   c. Grave a validação no relatório: PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py --relatorio content/material/_lotes/<F>/lote-NN.md <as pastas do lote>
   d. Acrescente ao fim do lote-NN.md (texto curto, sem copiar o conteúdo dos volumes): "Notas dos autores" (problemas do material-base, dúvidas em 'notas'), "Ferramentas" (falhas, reaberturas, devoluções do passo a), "Custo" (tempo e tokens de cada autor) e a hora de término.
5. Comece IMEDIATAMENTE o próximo ciclo (volte ao passo 1). Não espere o revisor.

PARADA (escreva uma linha final e pare só nestes casos):
- A seleção respondeu "FIM" sem "aguardando base": escreva "FRENTE <F> CONCLUÍDA: aguardando revisão".
- A seleção respondeu "FIM" com "aguardando base": escreva "FRENTE <F> EM ESPERA: <a lista que a seleção mostrou>".
- Você completou 5 lotes nesta sessão (o contexto fica grande): escreva "PAUSA: frente <F>, continuar no lote <próximo número> numa sessão nova".
- Dois lotes seguidos com um mesmo volume que falhou duas vezes: escreva "BLOQUEIO: <volume>, <motivo>".

Regras: nunca faça commit, nunca grave no banco, nunca edite arquivos fora das pastas dos volumes do seu lote e de content/material/_lotes/<F>/. Nunca rode scripts que regravam arquivos compartilhados (material_metrics.py, material_volumes.py, segment.py, build_*.py, importar.py, o seed). Nunca altere um REVISAO.md além de deixar o autor acrescentar a resposta. Nunca mude um status APROVADO ou DEVOLVIDO: isso é do revisor.
```

## Troca de coordenador de uma frente (30/10/2026)

Quando o coordenador de uma frente não puder mais ser usado, outro agente assume **a mesma letra**: as reservas `.frente`, a numeração dos lotes e a dos autores continuam. Ele usa o prompt da seção anterior, com o acréscimo "ASSUNÇÃO DA FRENTE" do prompt entregue ao dono (sessão sem subagentes = o próprio coordenador escreve os volumes, um de cada vez; relatório atualizado ao fim de cada volume para que a próxima sessão retome sem perda).

## Dois coordenadores (30/10/2026, noite)

Situação às 23h48 de 30/10: só dois agentes em produção. Diagnóstico do revisor:
- **Nenhuma colisão de volume.** Cada pasta tem um único dono (`.frente`), e nenhum volume foi mexido por outra frente; as únicas edições cruzadas são correções do revisor.
- **Desvio de rota da frente B.** Como o prompt das frentes B e C roda sem `--onda 1` e o seletor não repete disciplina no lote, ele completou os lotes com volumes da onda 2: DC m01, já entregue no lote 05, e as reservas de DC m05 e Biologia m01, no lote 06. Isso acontece enquanto o CFOA ainda tem Direito Administrativo m16 a m23 e Raciocínio Lógico m02 a m06 pendentes. Daqui em diante, as duas frentes rodam com `--onda 1` até o "FIM".
- **Autor repetido.** DH m04 e DPPM m04 estão com o mesmo autor, AGENTE-MATB-22.
- **Lote B 06 sem relatório.** Às 21:00 foram reservados 6 volumes, mas DH m04 é o único completo. DPPM m04 está em rascunho (3 capítulos, sem `volume.md` e sem `fixacao.json`). Nada mudou desde 21:07.
- **Volumes presos.** Oito volumes das frentes A e C, paradas desde 29/10, só podem ser retomados por um coordenador dessas letras. O seletor só entrega RETOMAR e CORRECAO à frente dona do volume:
  - A: LP m07, DA m08, DC m07, DPM m04;
  - C: DA m06 e DPM m06 (devolvidos), DA m11 e DPM m07 (sem Fixação).

Divisão: o **agente 1 continua a frente B**; o **agente 2 assume as sobras de A e C** e depois produz como frente C.

### Agente 1 · frente B

```
CONTINUIDADE DA FRENTE B (30/10/2026, noite)

Você coordena a FRENTE B do material próprio MentorIA, SEM subagentes: você mesmo escreve os volumes, um de cada vez. Siga pipeline/briefs/material.md (releia a seção 18: entraram três padrões de erro em 30/10 — EC 138/2025 na acumulação de cargos, Súmula 172 do STJ superada pela Lei 13.491/2017 e licença-paternidade com lei de 31/03/2026) e o fluxo do prompt "Frentes paralelas B e C" de pipeline/briefs/material-inicio.md (seleção, validação, relatório, paradas e regras valem como lá, trocando "abra os subagentes" por "escreva você mesmo"). Só há mais um agente trabalhando: ele cuida das frentes A e C. Nunca toque em pasta cujo .frente não seja B, nem em pasta antiga sem .frente (= frente A).

ESTADO EM 30/10, 23h48
- Lotes B 01 a 04: revisados e aprovados. Lote 05 (DA m15, DPPM m03, DH m03, RL m01, DC m01): entregue, aguardando o revisor. Não mexa.
- Às 21:00 a seleção reservou 6 volumes para B e não existe content/material/_lotes/B/lote-06.md:
  - direitos-humanos/m04: completo, PRONTO_PARA_REVISAO, autor AGENTE-MATB-22;
  - direito-processual-penal-militar/m04: a10-s01, a10-s02 e a12-s01 em RASCUNHO, sem volume.md e sem fixacao.json, autor também AGENTE-MATB-22;
  - direito-administrativo/m16 e raciocinio-logico/m02: só a reserva (.frente);
  - direito-constitucional/m05 e biologia/m01: só a reserva, e são da ONDA 2 (furaram a prioridade do CFOA).

PASSO 0 (uma vez, antes de tudo)
1. Se estiver no meio de um arquivo, termine-o e grave-o.
2. Libere as reservas da onda 2: apague content/material/direito-constitucional/m05/ e content/material/biologia/m01/ SOMENTE se `ls -a` mostrar apenas .frente em cada uma. Se houver outro arquivo, não apague e registre no relatório.
3. Crie content/material/_lotes/B/lote-06.md: início 2026-10-30 21:00; uma linha por volume (NOVO direitos-humanos/m04 · AGENTE-MATB-22; NOVO direito-processual-penal-militar/m04 · AGENTE-MATB-23; NOVO direito-administrativo/m16 · AGENTE-MATB-24; NOVO raciocinio-logico/m02 · AGENTE-MATB-25) e a nota "direito-constitucional/m05 e biologia/m01 liberados: onda 2". Troque o campo autor dos capítulos de DPPM m04 para AGENTE-MATB-23.
4. Termine o lote nesta ordem: DPPM m04 (releia e autorrevise os 3 capítulos, escreva o que faltar, volume.md e fixacao.json) → DA m16 → RL m02. DH m04 já está pronto: só valide. Ao fim de CADA volume, marque no lote-06.md "concluído <hora>" na linha dele.
5. Feche o lote como no prompt-base: check_citations e validate_material em cada pasta, `validate_material.py --relatorio content/material/_lotes/B/lote-06.md <as 4 pastas>`, notas dos autores, ferramentas, custo e término.

DAQUI EM DIANTE
- Seleção SEMPRE com onda: PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --lote 4 --onda 1 --frente B (uma única vez por lote). Como no CFOA só restam Direito Administrativo e Raciocínio Lógico, os lotes terão 1 ou 2 volumes; está certo assim.
- Quando a seleção com --onda 1 responder "FIM" sem "aguardando base", passe a --onda 2 (CFO BM), com a mesma regra.
- Autores: continue em AGENTE-MATB-26, um por volume, nunca repetido.
- Relatório atualizado ao fim de cada volume, para que outra sessão retome sem perda.
```

### Agente 2 · frentes A e C

```
ASSUNÇÃO DAS FRENTES A E C (30/10/2026, noite)

Você passa a coordenar as frentes A e C do material próprio MentorIA, cujos coordenadores pararam em 29/10. SEM subagentes: você mesmo escreve, um volume de cada vez. Siga pipeline/briefs/material.md (releia a seção 18: entraram três padrões de erro em 30/10) e o fluxo dos prompts "Lotes em sequência contínua" (frente A) e "Frentes paralelas B e C" (frente C) de pipeline/briefs/material-inicio.md (validação, relatório, paradas e regras valem como lá, trocando "abra os subagentes" por "escreva você mesmo"). Só há mais um agente trabalhando, na frente B. Nunca toque em pasta cujo .frente seja B. Se até agora você vinha trabalhando como frente B, pare: deixe os arquivos como estão (o agente da frente B os retoma) e não escreva em content/material/_lotes/B/.

ETAPA 1 — sobras da frente A (relatório: content/material/_lotes/lote-06.md, que já existe)
1. Seleção, uma vez: PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --lote 4 --onda 1 --frente A. Deve devolver RETOMAR para:
   - lingua-portuguesa/m07: 4 de 4 capítulos; falta fixacao.json;
   - direito-administrativo/m08: 5 de 6; falta o último capítulo e fixacao.json;
   - direito-constitucional/m07: 4 de 6; faltam 2 capítulos e fixacao.json. ATENÇÃO: a09-s03 e a09-s04 já têm correções do revisor (CF, art. 37, XVI, b, na redação da EC 138/2025: "um cargo de professor com outro de qualquer natureza"; militar estadual pelo art. 42, § 3º, com o art. 37, XVI, inteiro). Não volte à redação antiga em nenhum capítulo;
   - direito-penal-militar/m04: 6 de 6; falta fixacao.json.
   Se a lista for outra, use a que a seleção devolver e registre a diferença.
2. Os autores anteriores pararam por cota, sem autorrevisão: releia os capítulos existentes, passe neles a autorrevisão da seção 13, complete o que falta e feche cada volume (PRONTO_PARA_REVISAO). Autores: AGENTE-MAT-26 (LP m07), 27 (DA m08), 28 (DC m07), 29 (DPM m04); troque o campo autor de todos os arquivos do volume.
3. No lote-06.md, acrescente "## Retomada (<data e hora>)" com os 4 novos autores e, ao fim de cada volume, a linha "concluído <hora>". Feche com `validate_material.py --relatorio content/material/_lotes/lote-06.md <as 4 pastas>`, notas, ferramentas, custo e término.
4. A frente A termina aqui: não rode mais --frente A (ela pegaria volumes NOVOS).

ETAPA 2 — sobras da frente C (relatório novo: content/material/_lotes/C/lote-04.md)
1. Seleção A, uma vez: material_ficha.py --lote 2 --onda 1 --frente C. Deve devolver CORRECAO direito-administrativo/m06 e direito-penal-militar/m06. O lote é de 2 de propósito, para não reservar volume novo.
   Nos dois, a devolução é da Fixação: comentários de modelo repetidos. Reescreva cada comentário a partir do enunciado da própria questão (a regra aplicada, o motivo do gabarito, o erro de cada alternativa), até o validador não acusar comentário igual nem frase repetida. Não altere os capítulos: em DPM m06, as três correções do revisor já estão aplicadas. Responda no REVISAO.md ("## Resposta do autor — rodada 2") e mude o status para PRONTO_PARA_REVISAO.
2. Só depois disso, Seleção B, uma vez: material_ficha.py --lote 2 --onda 1 --frente C. Deve devolver RETOMAR direito-administrativo/m11 (6 de 6 capítulos; falta fixacao.json) e direito-penal-militar/m07 (3 de 3; falta fixacao.json). Releia e autorrevise os capítulos e faça a Fixação.
3. Autores: AGENTE-MATC-13 (DA m06), 14 (DPM m06), 15 (DA m11), 16 (DPM m07). Em C/lote-03.md, acrescente: "LP m09 e DC m12 aprovados; DA m11 e DPM m07 concluídos no lote 04". Feche o C/lote-04.md com `--relatorio` das 4 pastas, notas, ferramentas, custo e término.

ETAPA 3 — produção nova como frente C
Daí em diante, siga o ciclo da frente C: material_ficha.py --lote 4 --onda 1 --frente C (uma vez por lote), relatórios C/lote-05.md em diante, autores a partir de AGENTE-MATC-17. No CFOA só restam Direito Administrativo e Raciocínio Lógico, então os lotes terão 1 ou 2 volumes. Quando a seleção com --onda 1 responder "FIM" sem "aguardando base", passe a --onda 2 (CFO BM). Atualize o relatório ao fim de cada volume.
```

## Reativação da frente A (01/11/2026)

A frente A parou em 31/10, às 00h37, ao fim do CFOA (o prompt antigo rodava só com `--onda 1`). O CFOA está 71/71 aprovado; a frente A volta na onda 2 com um agente novo, sem subagentes. As frentes B e C seguem; o seletor reserva cada volume (`.frente`), então não há disputa.

```
REATIVAÇÃO DA FRENTE A (01/11/2026)

Você coordena a FRENTE A do material próprio MentorIA, SEM subagentes: você mesmo escreve os volumes, um de cada vez. Outras duas frentes (B e C) trabalham ao mesmo tempo na mesma fila; o seletor reserva cada volume que lhe entrega, então não há disputa. Nunca toque em pasta cujo .frente seja B ou C.

ANTES DE COMEÇAR (uma vez)
1. Leia por inteiro pipeline/briefs/material.md. Da seção 16, leia só a parte da disciplina de cada volume, quando chegar nele. Releia com atenção a seção 18 (erros que já devolveram volumes) e a tabela de quadros da seção 5.
2. Leia content/material/_lotes/REVISOES.md a partir de "Frente B lote 10" (31/10): é o que o revisor corrigiu nos lotes recentes.

CICLO DE UM LOTE
1. Número do lote: 1 + o maior NN entre os arquivos content/material/_lotes/lote-NN.md (hoje o maior é 06; comece em 07). Ignore as pastas B/ e C/.
2. Seleção, UMA única vez por lote (ela reserva os volumes): PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/material_ficha.py --lote 4 --onda 2 --frente A
   - Use exatamente a lista devolvida; nunca escolha volumes por outra listagem nem crie pastas de volume por conta própria.
   - Se a saída começar com "FIM": com --onda 2 esgotada sem "aguardando base", passe a --onda 3 (PCPE), com a mesma regra; se for "aguardando base", vá para PARADA.
   - Crie content/material/_lotes/lote-NN.md com a data e hora de início e uma linha por volume (tipo, volume, título, autor, situação).
3. Para cada volume, na ordem: CORRECAO, RETOMAR, NOVO. Autores AGENTE-MAT-30, 31, 32… (um por volume, nunca repetido; o último usado foi AGENTE-MAT-29).
   - NOVO: produza o volume completo (volume.md, todos os capítulos e fixacao.json) pelas seções 12 e 12.1 do briefing, com a ficha de material_ficha.py <volume>. As questões da Fixação já estão em pipeline/.cache/material/questoes/.
   - CORRECAO: leia o REVISAO.md da pasta (rodada mais recente), corrija todos os itens com edições pontuais, acrescente "## Resposta do autor — rodada <R>" com uma linha por item.
   - RETOMAR: aproveite o que estiver correto, complete o que falta e siga o fluxo de NOVO.
   - Ao fim de cada volume: valide (pipeline/validate_material.py <pasta>, zero erros; aviso que restar, justifique em 'notas'), faça a autorrevisão da seção 13, mude o status de todos os arquivos para PRONTO_PARA_REVISAO e marque "concluído <hora>" na linha do volume no lote-NN.md.
4. Fechamento do lote (obrigatório, é por ele que o revisor é avisado):
   a. pipeline/check_citations.py <pasta> e pipeline/validate_material.py <pasta> em cada volume.
   b. PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py --relatorio content/material/_lotes/lote-NN.md <as pastas do lote>  (isso grava a seção "## Validação (…)").
   c. Acrescente "Notas dos autores" (por volume: o que conferir, dados de memória, questões descartadas e por quê), "Ferramentas" e "Custo", e a hora de término.
5. Comece o próximo lote sem pedir confirmação.

PADRÃO DE QUALIDADE (o revisor devolve o volume que falhar nisto)
- Quadro [!lei] é a letra da lei: transcreva o dispositivo vigente (pipeline/leis.py art <lei> N). O validador dá ERRO para paráfrase dentro do quadro. Explicação vai no texto corrido.
- Legislação e jurisprudência: confira cada artigo, cada número de Tema, RE, ADI e súmula na fonte antes de escrever. No cache das leis, a redação revogada vem antes da vigente e "(Vide ADI …)" marca dispositivo julgado pelo STF: procure o julgamento. Na dúvida sobre um número, cite só o tribunal e o ano.
- Exatas: refaça toda conta de exemplo e de comentário de questão. Use símbolos (μ, σ, λ, ×, %, ·), nunca "mi", "sigma", "vezes" ou "por cento" por extenso.
- Fixação: gabarito igual ao do banco; comentário que parte do enunciado da questão e explica cada alternativa; questão com gabarito duvidoso sai e vai para as notas.
- Português: acentos sempre; sem "\n" literal no texto; "Para fixar" em lista com "- ".
- Nada de "Estratégia", "professor", "aula X", "página Y", "texto de apoio" ou "texto-base".

PARADA (uma linha final e pare)
- Seleção com "FIM" e "aguardando base": "FRENTE A EM ESPERA: <a lista>".
- 4 lotes completos nesta sessão: "PAUSA: frente A, continuar no lote <próximo> numa sessão nova".
- Um volume que falhou duas vezes: "BLOQUEIO: <volume>, <motivo>".

REGRAS
- Nunca faça commit, nunca grave no banco.
- Edite só as pastas dos volumes do seu lote e content/material/_lotes/lote-NN.md.
- Nunca edite ferramentas (nada em pipeline/, inclusive validate_material.py e check_citations.py) nem crie arquivos lá; scripts auxiliares ficam fora do repositório (pasta temporária).
- Nunca rode scripts que regravam arquivos compartilhados (material_metrics.py, material_volumes.py, segment.py, build_*.py, importar.py, o seed).
- Nunca mude um status APROVADO ou DEVOLVIDO nem edite REVISAO.md além da resposta do autor.
```
