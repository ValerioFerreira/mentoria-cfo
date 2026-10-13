# Auditoria por amostragem S3: diretrizes, resumos de bizu, ponteiros e itens C/E

- Código: S3
- Disciplinas: estatistica, matematica, lingua-portuguesa, lingua-espanhola
- Semente: 73003 (100 trechos de teoria, processados em rodadas de 10)
- Data: 2026-10-10
- Método: cada trecho conferido só contra o texto do PDF (intervalo início..fim mais a parte da pág. fim+1 antes do título seguinte).

## Métricas acumuladas

Trechos auditados: **20** de 100. Itens C/E avaliados: **180**; com gabarito errado: **0**; itens não sustentados pelo trecho ou contraditórios com o material: **1**.

| Dimensão | OK | PEQUENO | ERRO | Taxa de ERRO | Taxa PEQUENO+ERRO |
|---|---|---|---|---|---|
| Diretriz | 18 | 2 | 0 | 0% | 10% |
| Resumo | 14 | 5 | 1 | 5% | 30% |
| Ponteiros | 19 | 1 | 0 | 0% | 5% |
| C/E | 19 | 0 | 1 | 5% | 5% |

Por disciplina (OK/PEQUENO/ERRO em cada dimensão):

| Disciplina | Trechos | Diretriz | Resumo | Ponteiros | C/E |
|---|---|---|---|---|---|
| estatistica | 4 | 4/0/0 | 3/1/0 | 4/0/0 | 4/0/0 |
| lingua-espanhola | 3 | 3/0/0 | 2/1/0 | 3/0/0 | 3/0/0 |
| lingua-portuguesa | 6 | 4/2/0 | 4/1/1 | 5/1/0 | 5/0/1 |
| matematica | 7 | 7/0/0 | 5/2/0 | 7/0/0 | 7/0/0 |

## Tabela por rodada

| n | segmentId | diretriz | resumo | ponteiros | C/E | achados |
|---|---|---|---|---|---|---|
| 1 | lingua-portuguesa/a04/s05 | PEQUENO | PEQUENO | PEQUENO | OK | A-01,A-02 |
| 2 | lingua-espanhola/a06/s02 | OK | PEQUENO | OK | OK | A-03 |
| 3 | lingua-portuguesa/a06/s01 | OK | OK | OK | OK |  |
| 4 | matematica/a11/s04 | OK | OK | OK | OK |  |
| 5 | estatistica/a01/s05 | OK | OK | OK | OK |  |
| 6 | lingua-portuguesa/a00/s03 | OK | OK | OK | OK |  |
| 7 | estatistica/a12/s03 | OK | PEQUENO | OK | OK | A-04 |
| 8 | lingua-portuguesa/a13/s05 | PEQUENO | ERRO | OK | ERRO | A-05,A-06,A-07 |
| 9 | matematica/a12/s02 | OK | OK | OK | OK |  |
| 10 | matematica/a17/s12 | OK | PEQUENO | OK | OK | A-08 |
| 11 | estatistica/a03/s03 | OK | OK | OK | OK |  |
| 12 | lingua-portuguesa/a03/s01 | OK | OK | OK | OK |  |
| 13 | matematica/a16/s04 | OK | OK | OK | OK |  |
| 14 | lingua-portuguesa/a04/s01 | OK | OK | OK | OK |  |
| 15 | lingua-espanhola/a08/s02 | OK | OK | OK | OK |  |
| 16 | matematica/a00/s02 | OK | OK | OK | OK |  |
| 17 | estatistica/a01/s04 | OK | OK | OK | OK |  |
| 18 | matematica/a07/s04 | OK | PEQUENO | OK | OK | A-09 |
| 19 | matematica/a16/s01 | OK | OK | OK | OK |  |
| 20 | lingua-espanhola/a09/s06 | OK | OK | OK | OK |  |

## Registro de achados

**A-01** · lingua-portuguesa/a04/s05 · Diretriz · PEQUENO · proposto
- Site: início no tópico "Noções iniciais - Correlação e vozes verbais", pág. 69.
- PDF: a pág. 69 traz o título "NOÇÕES INICIAIS" (apresentação da aula, só introduz correlação e voz passiva); o conteúdo de correlação propriamente dito começa na pág. 70 ("CORRELAÇÃO DOS TEMPOS VERBAIS"). O nome do tópico é composto (não literal do PDF); a faixa de páginas está correta.
- Proposta: em `content/overrides/lingua-portuguesa.json`, aula 04, `headings` da pág. 69: renomear para "Noções iniciais" (ou manter; sem efeito no intervalo). Impacto baixo.

**A-02** · lingua-portuguesa/a04/s05 · Resumo e ponteiros · PEQUENO · corrigido
- Site: o resumo citava "caso/embora" na correlação do presente do subjuntivo e exemplos ("quando eles acabarem, eu estarei descansando"; "se eu fosse rico, já teria viajado") que não estão no PDF; o ponteiro da pág. 75 prometia também a "incoerência hipótese x futuro", tratada na pág. 76.
- PDF: págs. 70-71 e 76 trazem "Caso eu possa, farei", "Quando terminarem, estarei dormindo", "Se eu tivesse esse carro, já teria morrido"; "embora" não aparece nessa regra.
- Correção: `content/items/lingua-portuguesa/a04.json` (summary[2] e [3]; ponteiro da pág. 75 renomeado para "Futuro com relação lógica (condição implícita)").

**A-03** · lingua-espanhola/a06/s02 · Resumo · PEQUENO · corrigido
- Site: "em televisión → televisiones, o acento gráfico da forma singular some no plural", no parágrafo de plural invariável.
- PDF: a pág. 27 lista televisión/televisiones só como plural em -es; não comenta o acento (afirmação externa ao trecho e sem relação com o plural invariável).
- Correção: `content/items/lingua-espanhola/a06.json` (summary de plural invariável): frase trocada por "a diferença entre singular e plural fica por conta do artigo".

**A-04** · estatistica/a12/s03 · Resumo · PEQUENO · corrigido
- Site: "para inferência, costuma-se supor erros normais" nos pressupostos.
- PDF: as págs. 32-33 listam só três pressupostos (média 0, variância constante, independência); a normalidade só aparece na pág. 46 (EMV, fora do trecho). Faltavam também os termos heterocedasticidade e autocorrelação (pág. 32).
- Correção: `content/items/estatistica/a12.json` (summary[1]): removida a frase sobre normalidade e acrescentados heterocedasticidade/autocorrelação.

**A-05** · lingua-portuguesa/a13/s05 · Diretriz · PEQUENO · proposto
- Site: "parando antes do tópico 'Formas de Abreviação'", dizendo que ele pode começar no meio da pág. 82.
- PDF: a pág. 82 começa com o título "USO DE FORMAS ABREVIADAS" no topo (não no meio); o nome do site difere do título real.
- Proposta: `content/overrides/lingua-portuguesa.json`, aula 13: usar o título literal "Uso de formas abreviadas" no `headings` (pág. 82). Efeito prático nulo (o intervalo 65-81 está certo).

**A-06** · lingua-portuguesa/a13/s05 · Resumo · ERRO · corrigido
- Site: "Atestado ... (diferente da declaração, em que o fato consta)".
- PDF: a pág. 65 define atestado sem essa oposição; a pág. 66 (comentário da questão UFPB) diz que o atestado é "também tratado ... como declaração". A distinção não está no intervalo e contradiz o material.
- Correção: `content/items/lingua-portuguesa/a13.json` (summary[0]): trecho entre parênteses removido. Também corrigido o texto corrompido "CERTIDíO" para "CERTIDÃO" (summary[2]).

**A-07** · lingua-portuguesa/a13/s05 · C/E (teoria, item 1) · ERRO (item não sustentado) · corrigido
- Site: "O atestado declara fato ... que não consta ..., ao passo que a declaração trata de fato que neles consta." (V); a explicação dizia ser "a distinção apresentada no material".
- PDF: o material (págs. 65-66) não faz essa distinção; trata atestado e declaração como o mesmo documento. O item avalia algo fora do trecho e o atribui falsamente ao material.
- Correção: `content/items/lingua-portuguesa/a13.json` (teoria[0]): enunciado trocado para "O atestado declara fato existente que não consta ... e é firmado por servidor em razão do cargo ou função" (V), explicação reescrita; gabarito mantido (V).

**A-08** · matematica/a17/s12 · Resumo · PEQUENO · corrigido
- Site: "arccos(−1/2) = 2π/3" (exemplo inexistente no PDF).
- PDF: a pág. 149 dá arcsen(−√3/2) = −π/3 e arccos(−√3/2) = 5π/6.
- Correção: `content/items/matematica/a17.json` (summary[6]): exemplos substituídos pelos do PDF.

**A-09** · matematica/a07/s04 · Resumo · PEQUENO · corrigido
- Site: "Para uma fração de período, o regime simples rende mais, e por isso a convenção linear costuma resultar em montante maior" (generalização que o PDF não faz).
- PDF: pág. 35-36 só mostram o exemplo (exponencial 153,56; linear 157,73), sem a regra geral.
- Correção: `content/items/matematica/a07.json` (summary[4]): reescrito como constatação do exemplo, com a decomposição 146,41 + 5% de juros simples.


## Padrões recorrentes e recomendações
(a preencher ao final)

