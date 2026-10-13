# Revisão final G6 — Biologia

## Resultado
- Content: 16 arquivos `content/summaries/biologia/*.json`, 0 erros no validador (só avisos de tamanho/cobertura).
- Entregas rejeitadas (Tarefa C): 15 de 15 refeitas e válidas no `import_agent_summaries.py --dry-run` (0 rejeitados, 0 com cobertura baixa). Nada foi gravado no content.
- Como o veredito de cobertura é relativo (percentil), ao sair os 9 REFAÇÃO originais outros trechos desceram de faixa; ver pendências.

## Tarefa C — entregas refeitas (em `resumos-colaboradores/entregas/`)
As 14 entregas EXT-L3 estavam fracas (genéricas, sem números, parágrafo em "Para fixar", alguns erros: ex. S0300 trazia fases do atendimento erradas e omitia XABCDE, HIT, valores de pulso; S0340 omitia mutações/técnicas/doenças recessivas; S0543 omitia mico-leão e onça-parda). Todas reescritas a partir da fonte, com "Para fixar" de 8 itens e sintético de 11 a 12 pontos:

S0253 (c01/s01), S0257 (c02/s01), S0329 (c02/s02), S0300 (a16/s01), S0318 (a16/s02), S0333 (a17/s01), S0362 (a17/s02), S0340 (a02/s01), S0355 (a02/s02), S0356 (a02/s03), S0359 (a10/s03), S0369 (a05/s01), S0380 (a01/s01), S0381 (a01/s02), S0543 (a14/s04, CODEX-L3D; removida a cópia da denominação oficial da CITES).

## Tarefa B — trechos do content refeitos (REFAÇÃO antes → depois)
Analítico reescrito (de ~370-430 para ~750-1.050 palavras) e sintético de 11-12 pontos; vereditos saíram de REFAÇÃO (nota 0,34-0,39) e a nota subiu:
a03/s02 (S0547), a03/s03 (S0548), a03/s04 (S0558), a00/s03 (S0531), a00/s05 (S0532), a04/s02 (S0546), a13/s03 (S0555), a13/s04 (S0562), a13/s06 (S0536).
Arquivos alterados: `a00.json`, `a03.json`, `a04.json`, `a13.json` (a13.json mantido com CRLF).

## Pendências (não tratadas por orçamento)
Hoje REFAÇÃO/REVISAR por posição relativa, nota 0,41-0,47 e analítico ~400-550 palavras: a14/s03 (S0542), a00/s01 (S0553), a15/s01 (S0539), a13/s01 (S0554), a13/s07 (S0519), a14/s01 (S0512). ATENÇÃO: a14/s02, a15/s03, a03/s01, a04/s01, a00/s07, a00/s06, a09/s02, a06/s04. Parte da nota baixa vem de ruído (créditos de figuras, nomes de lugares/exemplos). Todos os demais trechos antigos do content têm 360-690 palavras contra alvo 1.000-2.000 (aviso "confira se não faltou conteúdo"); recomenda-se uma passada de ampliação.
Avisos de coincidência (10-14 palavras, listas de nomes/estados) em a13/s04 e a13/s06: aceitáveis.

## Dúvidas para revisão humana
1. a16/s01: material trata PA e dor como sinais vitais "na ordem das bancas"; fases do atendimento (local, vida, sinais vitais, avaliação detalhada) seguem o material, XABCDE do PHTLS. A relação compressão/ventilação (30:2) não consta do material (a17/s01) e costuma ser cobrada; o número de compressões na manobra de Heimlich ("cinco") varia por protocolo.
2. a16/s01 e a17/s01: sinais de choque e conduta de queimadura (a17/s02) seguem manual do Ministério/FIOCRUZ; o material diz que queimadura de 1º grau "usualmente há bolhas" (erro de digitação; resumo diz sem bolhas).
3. a02/s02: prevenção da eritroblastose descrita no material como anti-Rh para mãe "sensibilizada"; na prática a imunoglobulina anti-D é dada à mãe Rh negativa ainda não sensibilizada. Resumo registrou a divergência em notas.
4. a10/s03 e a00/s03: o material coloca o retorno do potencial em "-90 mV" na fase 4, e o repouso em -70 mV; o resumo mantém -70 mV como repouso e +30/+50 mV como pico (material varia entre os dois). Bomba 3Na/2K acrescentada por consenso técnico.
5. a01/s01: tabela de localização dos epitélios veio embaralhada; reconstruída pela ordem das colunas; o ânus aparece em duas colunas no material.
6. a13/s03: material afirma "8 bilhões de toneladas de plástico produzidos por ano" (valor implausível; ordem real é cerca de 400 milhões) e "8 milhões de toneladas no oceano"; o resumo não repete os 8 bilhões. Dados de reciclagem citados são do material.
7. a13/s04: material diz que temperatura e pressão são "inversamente proporcionais" para o oxigênio dissolvido; resumo diz apenas que água quente retém menos oxigênio.
8. c01/c02 (complementos): números com ano (IDH do Brasil 0,786, linhas do Banco Mundial, Vigitel) e artigos/metas legais (Lei 11.105, 9.433, 12.651, 9.985, 14.026) seguem o texto autoral conferido em 08/10/2026; conferir se a banca citar valor atualizado. Vacinas de dengue e chikungunya em incorporação gradual ao SUS.
9. Figuras não reconstruídas: pirâmides e curvas de sobrevivência (a14/s04), esquemas de HIT/fases (a16), heredogramas (a02), cortes histológicos (a01, a05).
10. Em a13/s04, S0543 e outros, os termos "material" e "Aula" foram evitados no corpo, mas ficam em NOTAS (campo não renderizado).
