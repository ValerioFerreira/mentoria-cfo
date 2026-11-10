# Revisão de legislacoes-pe/m01 — rodada 1 — 2026-10-29

**Decisão: DEVOLVIDO**

**Notas:** didática 3 · densidade visual 4 · foco na prova 4 · português 4 · Fixação 3

**Validador:** 0 erros. Avisos após a recalibragem:
- a02-s01: linguagem rebuscada;
- a02-s02: frases longas.

**Lido:** os três capítulos de forma integral (todos de importância ALTA), conferidos contra a Lei 6.783/1974 compilada (`pipeline/leis.py pe6783`). Da Fixação, duas questões sorteadas.

Pontos fortes: cobertura completa dos tópicos e do edital, boas tabelas (círculos, licenças, afastamentos, exclusão), linha do tempo ausente → extraviado, pegadinhas bem escolhidas.

## Correções obrigatórias

### a02-s02.md (bloqueantes)

1. **Elegibilidade.** O capítulo ensina o art. 51 (menos de 5 anos: excluído; 5 anos ou mais: agregado) como regra vigente. A CF, art. 14, § 8º, aplicável aos militares estaduais pelo art. 42, § 1º, fixa 10 anos: com menos de 10, afasta-se da atividade; com mais de 10, é agregado e, se eleito, passa à inatividade na diplomação. Pelo art. 14, § 2º, só os conscritos são inalistáveis.
   - Reescreva com as duas regras e diga que a CF prevalece.
   - Diga que a banca pode cobrar a literalidade do art. 51.
   - Ajuste o Mapa e o Para fixar.
2. **Números de artigo errados.** Corrija cada um, conferindo com `leis.py art pe6783 <n>`:

   | Assunto | Está no capítulo | Correto |
   | --- | --- | --- |
   | Ausente | art. 85 | art. 81 |
   | Desaparecido | art. 86 | art. 83 |
   | Extraviado | art. 87 | art. 84 |
   | Desligamento 6 meses após a agregação por extravio | — | art. 117, § 1º |
   | Prisão só em flagrante (Mapa) | art. 71 | art. 69 |
   | Excedente (Mapa) | art. 83 | art. 80 |
   | Licenciamento (Mapa) | art. 110 | art. 109 |

   Além disso:
   - causas de desligamento: art. 85;
   - dispensa do júri e da Justiça Eleitoral: art. 70;
   - "Ag" e promoção só por antiguidade: art. 76, caput e § 1º.

   Revise **todos** os outros números do capítulo do mesmo modo.
3. **Excedente.** As hipóteses "reversão sem vaga" e "anulação de ato" não estão na lei. O art. 80 traz:
   - promovido por bravura sem vaga;
   - o mais moderno que ultrapassa o efetivo pela promoção de outro em ressarcimento de preterição;
   - quem retorna ao quadro completo depois de cessado o motivo da reforma por incapacidade definitiva;
   - quem ultrapassa o efetivo por desativação parcial do quadro.

   O inciso II ("promovido indevidamente") foi revogado. Reescreva a partir do art. 80.
4. **Desaparecido.** O art. 83 fala em paradeiro ignorado por mais de 8 dias "no desempenho de qualquer serviço, em viagem, em operações policiais-militares ou em caso de calamidade pública", só quando não houver indício de deserção. Ajuste o texto e o esquema.
5. **Prazo de recurso.** A lei diz que o direito de recorrer "prescreverá" (art. 50, § 1º), e não que o prazo é decadencial. Ajuste.

### a02-s01.md

6. A antiguidade entre alunos de um mesmo órgão de formação segue "o regulamento do respectivo órgão" (art. 15, § 2º, c), e não "a classificação final". Corrija.
7. **Art. 28.** A lei veda ao militar da ativa "ser sócio ou participar" de sociedade, salvo como acionista (S.A.) ou quotista (Ltda.). Não é só "sócio administrador". Corrija a lista e a tabela.
8. Falta o **art. 28, § 1º**: o militar da reserva remunerada convocado não pode tratar de interesses de empresas privadas nas organizações militares e repartições públicas. Inclua.
9. O dever de informar a origem e a natureza dos bens está no **art. 29**. Cite-o.
10. **Estilo.** Abertura e definições com jargão ("vigas mestras", "limites axiológicos e negociais", "consubstancia-se", "precípua", "plexo"). Reescreva em linguagem direta (seção 5.2 do briefing).

### c05-s01.md

11. A abertura começa com "O que este material cobre integra…", texto colado do título do complemento. Reescreva.
12. **Art. 30, II**: "culto aos símbolos nacionais" (a lei não diz "e estaduais"). Corrija a lista.
13. A alíquota de 10,5% está no **art. 74-E, § 3º** (o Mapa diz 74-D). Confira também os artigos citados para a ordem da pensão (74-N) e para o recurso de 90 dias.
14. **Quota compulsória.**
    - Não localizei no Estatuto a publicação "até 15 de janeiro". Confirme em qual norma está e cite-a, ou retire.
    - O art. 60 diz que a quota assegura um número fixo de vagas à promoção (renovação dos quadros). Ajuste a redação.

### fixacao.json

15. O comentário de **tec_2454604** cita "art. 87". O correto é o art. 84 (extraviado após 30 dias) e o art. 117, § 1º (desligamento 6 meses após a agregação). Revise os números de artigo de **todos** os comentários.

## Melhorias pedidas (não bloqueiam)

- Diminua o vocabulário rebuscado nos três capítulos e encurte as frases do a02-s02 (média de 28 palavras).
- A licença especial e a de interesse particular mudaram de competência (LC 300/2015 e LC 314/2015: Secretário de Defesa Social). Vale uma linha, porque a banca cobra a redação atual.

## Resposta do autor — rodada 1

1: Reescrita a elegibilidade apresentando a regra constitucional (CF, art. 14, § 8º: 10 anos, que prevalece) e a literalidade do art. 51 (5 anos), alertando sobre o critério cobrado pela banca; ajustados alistabilidade (CF, art. 14, § 2º), Mapa e Para fixar.
2: Corrigidos todos os artigos errados: ausente (art. 81), desaparecido (art. 83), extraviado (art. 84), desligamento por extravio (art. 117, § 1º), prisão em flagrante (art. 69), dispensa do júri e Justiça Eleitoral (art. 70), agregação e antiguidade (art. 76, caput e § 1º), excedente (art. 80), licenciamento (art. 109), causas de desligamento (art. 85), períodos não computáveis (art. 122, § 3º) e contagem de tempo (arts. 120 a 126).
3: Reescrito o instituto do excedente com base estrita no art. 80 (4 hipóteses vigentes), excluídas as menções a "reversão sem vaga" e "anulação de ato" e destacada a revogação do inciso II pela Lei nº 12.441/2003.
4: Ajustada a caracterização do desaparecido (art. 83: mais de 8 dias em serviço, viagem, operações ou calamidade pública, sem indício de deserção) e atualizado o esquema Mermaid correspondente.
5: Retificada a natureza do prazo recursal administrativo para prazo de prescrição ("prescreverá", art. 50, § 1º), expungindo o termo "decadencial".
6: Corrigido o critério de antiguidade entre alunos de mesmo órgão de formação para o regulamento do respectivo órgão (art. 15, § 2º, c).
7: Ajustada a vedação do art. 28 no texto e na tabela, esclarecendo a proibição de ser sócio ou participar de sociedade, salvo como acionista de S.A. ou quotista de Ltda.
8: Incluída a vedação do art. 28, § 1º, que proíbe o militar da reserva convocada de tratar de interesses privados em organizações militares e repartições públicas.
9: Inserida a citação expressa do art. 29 para o dever de prestar informações sobre origem e natureza dos bens.
10: Reescrevemos abertura, definições e tabelas eliminando o vocabulário rebuscado ("vigas mestras", "limites axiológicos", "consubstancia-se", "precípua", "plexo").
11: Reescrevemos a abertura de c05-s01.md em linguagem direta, sem colar o título do complemento.
12: Corrigido o art. 30, II, para "culto aos símbolos nacionais", suprimindo "e estaduais".
13: Corrigida a alíquota de 10,5% para o art. 74-E, § 3º no texto e no Mapa; conferidos e citados os artigos da pensão (art. 74-N) e do recurso administrativo de 90 dias (art. 74-Z, §§ 12 a 15).
14: Indicado o art. 60, § 2º (acrescido pela LC nº 92/2007) para a fixação de vagas da quota compulsória até 15 de janeiro, ajustando a redação sobre a finalidade de assegurar renovação e vagas à promoção.
15: Corrigidos os comentários da Fixação, retificando tec_2454604 (art. 84 e art. 117, § 1º), tec_2775595 (art. 80) e tec_533712 (art. 50, § 1º).
- Melhorias: Atualizadas as competências da licença especial (art. 65, § 6º, LC nº 300/2015: Cmt-Geral, SDS ou Casa Militar) e da licença particular (art. 66, § 2º, LC nº 314/2015: Secretário de Defesa Social); frases de a02-s02.md encurtadas e vocabulário rebuscado eliminado nos três capítulos.


---

# Revisão de legislacoes-pe/m01 — rodada 2 — 2026-10-29

**Decisão: APROVADO**

**Notas:** didática 4 · densidade visual 4 · foco na prova 5 · português 4 · Fixação 4

**Validador:** 0 erros, 0 avisos.

**Lido:** os 15 itens da rodada 1, conferidos um a um contra a Lei 6.783/1974 compilada:
- elegibilidade (CF, art. 14, § 8º × art. 51);
- números dos arts. 69, 70, 71, 75, 76, 78, 80, 81, 83, 84, 85, 89, 109 e 117, § 1º;
- excedente (art. 80);
- art. 60, § 2º (15 de janeiro, confirmado);
- arts. 74-E, § 3º, 74-N e 74-Z, §§ 12 a 15.

**Ajuste do revisor:** em a02-s02, a agregação por licença de saúde estava citada como "art. 75, § 1º, b". O correto é a alínea c, III (saúde própria) e a alínea c, V (pessoa da família).

# Neutralidade de concurso — 2026-11-02
Decisão: APROVADO (com correções do revisor)
Correções: 1 frases reescritas (direcionamento), 3 nomes de banca generalizados; fontes: nenhuma fonte inventada; sem alteração; conteúdo legal de PE mantido

# Fixação ampliada — 2026-11-03
Decisão: APROVADO (Fixação ampliada pela média do material-base)
Comentários novos: 10 · Descartadas por qualidade: 1

# Fixação ampliada (reposição) — 2026-11-03
Decisão: APROVADO (Fixação ampliada pela média do material-base)
Comentários novos: 1 · Descartadas por qualidade: 0
