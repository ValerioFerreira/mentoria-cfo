# Revisão — inéditas CBMPE (briefing 2), química (agente quimica2)

Data: 2026-10-22. Disciplina: química. Total escrito: **118 questões** em 15 aulas (meta do CSV cumprida). `lacunas_cbmpe_aula.py --lista quimica` não lista mais nenhuma aula abaixo de 25.

## Questões por aula (trechos)

| Aula | Escritas | Distribuição |
|---|---|---|
| a01 | 4 | s01: 2, s02: 1, s03: 1 |
| a03 | 4 | s01: 2, s02: 1, s03: 1 |
| a05 | 4 | s01: 2, s02: 1, s03: 1 |
| a07 | 4 | s01: 2, s02: 1, s03: 1 |
| a08 | 11 | s01: 6, s02: 5 |
| a09 | 6 | s01: 6 |
| a11 | 11 | s01: 6, s02: 5 |
| a12 | 11 | s01: 6, s02: 5 |
| a13 | 11 | s01: 6, s02: 5 |
| a15 | 4 | s01: 2, s02: 1, s03: 1 |
| a16 | 4 | s01: 2, s02: 1, s03: 1 |
| a20 | 11 | s01: 6, s02: 5 |
| a21 | 4 | s01: 2, s02: 1, s03: 1 |
| a23 | 11 | s01: 6, s02: 5 |
| c01 | 18 | s01: 18 (o complemento tem um único trecho) |

## Método

- Cada conta foi refeita por dois caminhos (proporção/estequiometria e conferência por outra via, como balanço de massa, de cargas ou de elétrons) e a conferência está no comentário.
- Textos sem figuras; fórmulas em texto simples; valores fictícios ou simples (sal "X", "A2X", "HA").
- Os tópicos de cada trecho foram cruzados com as questões já gravadas para evitar repetição de enunciado.
- Nomenclatura e fatos conferidos de memória em fonte padrão (IUPAC, tabelas usuais de pKa), sem consulta a página externa nesta rodada.

## Pendência que depende do orquestrador (questão com defeito do `--check`)

`ineditas_mc_nativas.py --check` acusa `ERRO quimica #473 (quimica/a12/s02): enunciado com 4 palavras`. É questão **minha**, gravada com o enunciado "Assinale a opção correta." (curto demais). Os `.txt` não se editam à mão; por isso não alterei o arquivo. Sugestão de substituição do enunciado (alternativas e comentário ficam como estão):

> Sobre entalpias de formação e de combustão, assinale a opção correta.

A alternativa correta é "A entalpia de combustão do carbono grafite coincide com a entalpia de formação padrão do CO2(g)." (as demais: formação do diamante nula, combustão do grafite = formação do CO, formação do CO2 nula, formação do O3 nula). Todo o resto do `--check` de química está sem erro.

## Pontos para o dono / observações

- **c01 (complemento):** o trecho tem só `s01`, então as 18 questões ficaram nele (aviso do briefing). As questões usam o conteúdo do complemento (siderurgia, FDS, água, fogo, polímeros, proteção radiológica, gases). Dois valores do complemento merecem conferência humana periódica: a Portaria GM/MS nº 888/2021 (cloro residual livre mínimo de 0,2 mg/L) e a classificação inflamável/combustível com limite de 60 °C, que varia entre normas (NR-20 usa 60 °C como limite superior dos inflamáveis, outras fontes usam 37,8 °C); a questão sobre o tema declara no enunciado o critério de 60 °C (o do complemento), com líquidos de 38 °C e 85 °C; pelo critério de 37,8 °C o de 38 °C já seria "combustível", então o enunciado não pode perder essa frase.
- **a23:** não foram usados percentuais de etanol na gasolina (E27/E30), porque a regra mudou recentemente e pode mudar de novo.
- **a20 (nucleofilicidade, OH- x H2O):** questão conceitual simples; se o dono preferir mais dificuldade, vale trocar por uma comparação de solvente prótico/aprótico.
- Distribuição final de gabaritos de química depois da gravação: A 108, B 107, C 108, D 107, E 107.
