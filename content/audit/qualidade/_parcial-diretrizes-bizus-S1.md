# Auditoria por amostragem — diretrizes, resumos do bizu e itens C/E (parcial S1)

- Código: **S1**
- Disciplinas: direito-constitucional, informatica, legislacoes-pe, direito-penal-militar, lingua-inglesa
- Semente: 71001 (amostra de 100 trechos; composição: informática 45, dir. constitucional 31, dir. penal militar 12, língua inglesa 10, legislações-PE 2)
- Data: 2026-10-10
- Verdade: somente o PDF (leitura independente de índice/estrutura/segmentos/overrides).

## Métricas acumuladas

Trechos auditados: **13** de 100.

| Dimensão | OK | PEQUENO | ERRO | taxa de erro (PEQ+ERRO) | taxa ERRO |
|---|---|---|---|---|---|
| Diretriz | 9 | 4 | 0 | 31% | 0% |
| Resumo | 7 | 6 | 0 | 46% | 0% |
| Ponteiros | 12 | 1 | 0 | 8% | 0% |
| C/E | 12 | 1 | 0 | 8% | 0% |

Itens C/E examinados: **117**; com gabarito errado: **0**; ambíguos/fora do trecho (problema, gabarito correto): **2**.

Por disciplina (PEQ = pequeno; ERR = erro):

| Disciplina | trechos | Dir PEQ/ERR | Res PEQ/ERR | Pont PEQ/ERR | C/E PEQ/ERR | itens C/E (gab. errado) |
|---|---|---|---|---|---|---|
| direito-constitucional | 1 | 0/0 | 0/0 | 0/0 | 0/0 | 10 (0) |
| direito-penal-militar | 2 | 1/0 | 0/0 | 0/0 | 0/0 | 18 (0) |
| informatica | 6 | 1/0 | 4/0 | 0/0 | 0/0 | 49 (0) |
| legislacoes-pe | 1 | 0/0 | 1/0 | 1/0 | 0/0 | 10 (0) |
| lingua-inglesa | 3 | 2/0 | 1/0 | 0/0 | 1/0 | 30 (0) |

Achados: 12 no total; corrigidos: 8; propostos (diretriz): 4; falso positivo: 0.

## Tabela por rodada

### Rodada 1 (n=1..10)

| n | segmentId | diretriz | resumo | ponteiros | C/E |
|---|---|---|---|---|---|
| 1 | informatica/a06/s06 | OK | PEQUENO | OK | OK (10 itens, 0 gab. errado) |
| 2 | informatica/a12/s06 | PEQUENO | PEQUENO | OK | OK (9 itens, 0 gab. errado) |
| 3 | informatica/a06/s10 | OK | PEQUENO | OK | OK (7 itens, 0 gab. errado) |
| 4 | lingua-inglesa/a04/s03 | PEQUENO | OK | OK | OK (10 itens, 0 gab. errado) |
| 5 | direito-penal-militar/a08/s06 | OK | OK | OK | OK (8 itens, 0 gab. errado) |
| 6 | informatica/a00/s04 | OK | OK | OK | OK (9 itens, 0 gab. errado) |
| 7 | direito-penal-militar/a04/s02 | PEQUENO | OK | OK | OK (10 itens, 0 gab. errado) |
| 8 | legislacoes-pe/a01/s02 | OK | PEQUENO | PEQUENO | OK (10 itens, 0 gab. errado) |
| 9 | lingua-inglesa/a02/s03 | OK | OK | OK | PEQUENO (10 itens, 0 gab. errado) |
| 10 | informatica/a07/s05 | OK | PEQUENO | OK | OK (7 itens, 0 gab. errado) |

### Rodada 2 (n=11..13)

| n | segmentId | diretriz | resumo | ponteiros | C/E |
|---|---|---|---|---|---|
| 11 | direito-constitucional/a11/s02 | OK | OK | OK | OK (10 itens, 0 gab. errado) |
| 12 | lingua-inglesa/a04/s02 | PEQUENO | PEQUENO | OK | OK (10 itens, 0 gab. errado) |
| 13 | informatica/a08/s05 | OK | OK | OK | OK (7 itens, 0 gab. errado) |

## Registro de achados

### A-01 — informatica/a06/s06 — Resumo — PEQUENO
- **Site diz:** Resumo cobre ABS, ALEATÓRIO, ARRED, FATORIAL, RAIZ, ÍMPAR, MOD e MULT; ignora a função PAR(), que está dentro do intervalo (começa no fim da pág. 97 e é explicada na pág. 98 antes de PI).
- **PDF mostra:** Pág. 97 (fim) e pág. 98 (início): =PAR(núm) arredonda ao inteiro par mais distante do zero (PAR(3)=4; PAR(-1)=-2), antes do tópico Função PI().
- **Correção/proposta:** content/items/informatica/a06.json, summary[9]: acrescentado "PAR(núm) faz o mesmo para o par (PAR(3) = 4; PAR(-1) = -2)".
- **Status:** corrigido

### A-02 — informatica/a12/s06 — Diretriz — PEQUENO
- **Site diz:** Diretriz cita o tópico inicial como “AINEL DE ONTROLE” e o final como “ONFIGURAÇÕES” (a 1ª letra de cada palavra sumiu).
- **PDF mostra:** Pág. 62: título em versaletes “PAINEL DE CONTROLE” (a inicial é maiúscula grande, o resto em caixa alta menor); pág. 74: “CONFIGURAÇÕES”. A extração de texto perde a inicial de cada palavra em versaletes.
- **Correção/proposta:** Proposta de override em content/overrides/informatica.json, aula a12: dropHeadings [{"page":62,"title":"AINEL DE ONTROLE"},{"page":74,"title":"ONFIGURAÇÕES"}] e headings [{"page":62,"title":"Painel de Controle","level":1},{"page":74,"title":"Configurações","level":1}]. Melhor ainda: corrigir em pipeline/headings.py (juntar a inicial grande dos versaletes à palavra seguinte); o mesmo erro aparece em vários trechos da amostra (ver padrões).
- **Status:** proposto

### A-03 — informatica/a12/s06 — Resumo — PEQUENO
- **Site diz:** Resumo diz que o Painel de Controle “exibe-se por categorias ou por ícones (grandes/pequenos)”.
- **PDF mostra:** Págs. 62-73: nenhuma menção à exibição por ícones grandes/pequenos (a pág. 62 só diz como abrir: pesquisa ou Win + R com control). É conhecimento externo ao trecho.
- **Correção/proposta:** content/items/informatica/a12.json, summary[0]: trocado por “Abre-se pela barra de pesquisa ou pelo atalho Win + R com o comando control”.
- **Status:** corrigido

### A-04 — informatica/a06/s10 — Resumo — PEQUENO
- **Site diz:** Resumo [5] diz que a tabela dinâmica “exige dados organizados em colunas com cabeçalho” e [6] que ela “deve ser atualizada” ou que se use o intervalo “como Tabela para ampliar automaticamente”.
- **PDF mostra:** Págs. 147-148: os dados devem estar em tabela sem linhas/colunas vazias e com tipos separados por coluna; assim as linhas novas entram ao atualizar; senão, ajuste manual do intervalo de origem. “Cabeçalho” e “usar como Tabela” não aparecem no intervalo.
- **Correção/proposta:** content/items/informatica/a06.json, summary[5] e summary[6] reescritos conforme as págs. 147-148 (preparo dos dados; soma por padrão, outras funções de resumo).
- **Status:** corrigido

### A-05 — lingua-inglesa/a04/s03 — Diretriz — PEQUENO
- **Site diz:** Diretriz cita o tópico inicial como “Futuro Simples e com GOING TO”.
- **PDF mostra:** Pág. 24: o título é “FUTURO SIMPLES E COM O GOING TO” (tem o artigo “O”). Idem no segmento vizinho a04/s02 (mesma citação, ver n=12).
- **Correção/proposta:** Proposta: override headings/dropHeadings em content/overrides/lingua-inglesa.json (aula a04): dropHeadings [{"page":24,"title":"Futuro Simples e com GOING TO"}] + headings [{"page":24,"title":"Futuro Simples e com o GOING TO","level":1}]. Grafia apenas; localização correta.
- **Status:** proposto

### A-06 — direito-penal-militar/a04/s02 — Diretriz — PEQUENO
- **Site diz:** Diretriz cita o tópico inicial “Aplicação das Penas” e o tópico seguinte “Concurso de agravantes e atenuantes, pena indeterminada e concurso de crimes”.
- **PDF mostra:** Pág. 9: o título é “APLICAÇÃO DA PENA” (singular). Pág. 19: existe “CONCURSO DE AGRAVANTES E ATENUANTES” (art. 75) e, só mais abaixo, “CRIMINOSO HABITUAL OU POR TENDÊNCIA”; o título composto citado não existe. A localização (meio da pág. 19, após o art. 74) está correta.
- **Correção/proposta:** Proposta (content/overrides/direito-penal-militar.json, aula a04): headings [{"page":9,"title":"Aplicação da Pena","level":1},{"page":19,"title":"Concurso de agravantes e atenuantes","level":1}] (e dropHeadings para os títulos antigos), ou renomear o tópico composto para o título real.
- **Status:** proposto

### A-07 — legislacoes-pe/a01/s02 — Resumo — PEQUENO
- **Site diz:** Resumo [9] lista as causas de justificação, atenuantes e agravantes como se fossem completas: atenuantes = 3 itens; agravantes = 3 itens.
- **PDF mostra:** Pág. 17 (quadro): 4 causas de justificação (ação meritória; legítima defesa etc.; caso fortuito/força maior; falta de esclarecimentos/ordem/meios), 4 atenuantes (inclui influência de fatores diversos) e 9 agravantes (inclui prática simultânea/conexão, abuso de autoridade, execução do serviço, presença de subordinados/tropa/público civil, tentada ou consumada em desrespeito à continuidade do serviço).
- **Correção/proposta:** content/items/legislacoes-pe/a01.json, summary[9] reescrito com os 4/4/9 incisos (parafraseados).
- **Status:** corrigido

### A-08 — legislacoes-pe/a01/s02 — Ponteiros — PEQUENO
- **Site diz:** Ponteiro “Julgamento, justificação, atenuantes e agravantes” aponta a pág. 18.
- **PDF mostra:** Os quadros de justificação/atenuantes/agravantes e o amplo direito de defesa estão na pág. 17 (o tópico começa no fim da pág. 16); a pág. 18 só tem observações e uma questão.
- **Correção/proposta:** content/items/legislacoes-pe/a01.json, pointers: pageRef 18 -> 17.
- **Status:** corrigido

### A-09 — lingua-inglesa/a02/s03 — C/E — PEQUENO
- **Site diz:** Dois itens de revisão: (a) “pretty é advérbio de intensidade” (Na frase The tool seems pretty knowledgeable) e (b) “yet equivale a so far” (I haven't finished my homework yet).
- **PDF mostra:** O intervalo é págs. 24-32. A questão do “pretty” só tem enunciado na pág. 32 e o comentário (gabarito: intensidade) está na pág. 33; o “yet = so far” aparece apenas num comentário de questão bem além do intervalo (págs. >33). Gabaritos corretos, mas itens não sustentados pelo trecho.
- **Correção/proposta:** content/items/lingua-inglesa/a02.json, revisao: item “pretty” trocado por item sobre o quadro de classificação (enough/rather/equally/thoroughly = intensidade, pág. 31); item “yet” trocado por item sobre locução adverbial (as quickly as possible, pág. 30). Ambos V, mesma ordem.
- **Status:** corrigido

### A-10 — informatica/a07/s05 — Resumo — PEQUENO
- **Site diz:** Resumo [0] escreve a função como “NíO (inverte)”.
- **PDF mostra:** Pág. 50: a função é NÃO(). A sequência “ÃO” em caixa alta virou “íO” (corrupção de caracteres) — 114 ocorrências em content/items (ver padrões).
- **Correção/proposta:** content/items/informatica/a07.json, summary[0]: NíO -> NÃO. Correção global proposta (ver padrões).
- **Status:** corrigido

### A-11 — lingua-inglesa/a04/s02 — Diretriz — PEQUENO
- **Site diz:** Diretriz cita o tópico final “Futuro Simples e com GOING TO” (a mesma citação de A-05).
- **PDF mostra:** Pág. 24: “FUTURO SIMPLES E COM O GOING TO” (falta o “O”).
- **Correção/proposta:** Mesma proposta de A-05 (corrige as duas diretrizes de uma vez, pois o título é o mesmo).
- **Status:** proposto

### A-12 — lingua-inglesa/a04/s02 — Resumo — PEQUENO
- **Site diz:** Resumo [4] diz que em read “a grafia é igual, a pronúncia muda”.
- **PDF mostra:** Págs. 12-23: a lista só mostra read -> read (mesma grafia); nada sobre pronúncia (conhecimento externo).
- **Correção/proposta:** content/items/lingua-inglesa/a04.json, summary[4]: trocado por “a lista traz a mesma grafia no passado”.
- **Status:** corrigido

## Padrões recorrentes e recomendações

