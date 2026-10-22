# Revisão — inéditas MentorIA CBMPE, Língua Inglesa (agente `ingles`, 2026-10-21)

Arquivo: `content/questoes/ineditas/mc/lingua-inglesa.txt` (104 questões, 5 alternativas, gabaritos balanceados: A 20, B 21, C 21, D 21, E 21).

## Questões por aula e trecho

| Aula | Trecho | Escritas | Assunto |
|---|---|---|---|
| a00 | s01 | 6 | falsos cognatos, skimming, inferência pelo contexto, ideia central |
| a00 | s02 | 3 | aviso (texto não verbal), fatores pragmáticos, gráfico descrito |
| a01 | s01 | 4 | plural irregular, incontáveis, plural em -f/-fe, gênero |
| a01 | s02 | 5 | genitivo (2), a/an (2), plural dos artigos |
| a01 | s03 | 1 | pronomes reflexivos |
| a01 | s04 | 3 | whose, indefinidos, relativas explicativas |
| a01 | s05 | 7 | at/on, over, above, between, through, in spite of, despite + gerúndio |
| a02 | s01 | 7 | conjunções coordenadas, subordinadas e correlativas |
| a02 | s03 | 4 | advérbios interrogativos, frequência, tempo/lugar, conjunct |
| a02 | s04 | 6 | prefixo mis-, sufixos, -less, função comunicativa, registro, variedades |
| a03 | s01 | 4 | phrasal verbs, to be, to do |
| a04 | s01 | 5 | presente simples (afirmativa, interrogativa, negativa, usos) |
| a04 | s02 | 1 | passado simples |
| a04 | s03 | 6 | will e going to |
| a05 | s01 | 7 | tempos contínuos, verbos de estado, grafia -ing |
| a05 | s02 | 1 | present perfect (since) |
| a05 | s03 | 6 | voz passiva (4 tempos), causativa, identificação |
| a05 | s04 | 4 | imperativo, let's, subjuntivo |
| a06 | s01 | 6 | idioms (3), discurso indireto (3) |
| a06 | s02 | 7 | numerais, quantificadores, marcadores de discurso |
| a06 | s03 | 6 | question tag, wh-, infinitivo/gerúndio, condicional 2, relativa |
| c01 | s01 | 5 | adverbial de tempo, condicional 3, omissão do relativo, padrão verbal, tag de let's |
| **Total** | | **104** | |

Todos os trechos chegaram a 7 ou mais (`lacunas_cbmpe.py --lista lingua-inglesa` sem pendências).

## Pontos para o dono

1. **a05/s04 sem assunto do edital.** O trecho (imperativo e subjuntivo) não aparece em nenhum item de `content/edital/lingua-inglesa.json`, embora conste como relevante no CBMPE Oficial em `content/importance/segments.json`. Por isso `ineditas_mc_nativas.py --check` acusa 4 erros ("trecho sem assunto do edital") nas questões `lingua-inglesa #77–#80`. Solução sugerida: ligar o trecho a um item do edital (por exemplo, incluí-lo no `where` do item 3.9, Modais, ou criar item próprio) ou marcar as 4 questões com `item=<código>`; os `.txt` não foram editados à mão. Fora esses 4, a disciplina está sem erros.
2. **Variação de uso.** A questão do subjuntivo (a05/s04) cobra a forma base depois de suggest; em inglês britânico informal admite-se também "should be" ou o indicativo, mas as alternativas não oferecem essas formas.
3. **Questões de cognatos e idioms** foram escritas de acordo com dicionários comuns; nenhum texto de prova foi usado.
