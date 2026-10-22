# Revisão — inéditas CBMPE (briefing 2), biologia (agente biologia2)

Gravadas em `content/questoes/ineditas/mc/biologia.txt` (múltipla escolha, 5 alternativas, gabarito embaralhado pela ferramenta). Total: **60 questões**, exatamente o pedido no CSV. `ineditas_mc_nativas.py --check` não acusa nenhum erro de biologia (o único erro do geral é de química, #473, enunciado curto, de outro agente). `lacunas_cbmpe_aula.py` não lista mais nenhuma aula de biologia abaixo de 25.

| Aula | Trecho | Escritas |
| --- | --- | --- |
| a01 Histologia | s01 | 2 (coloração HE; junções celulares) |
| | s02 | 1 (tipos de cartilagem) |
| | s03 | 1 (tipos de tecido muscular) |
| a05 Tegumentar | s01 | 2 (melanócitos e melanina; impressões digitais) |
| | s02 | 1 (circulação e termorregulação da pele) |
| | s03 | 1 (coagulação na cicatrização) |
| a11 Endócrino e imunitário | s02 | 2 (febre; leucócitos) |
| a12 Embriologia | s01 | 6 (ordem da fecundação; ovulação e corpo lúteo; SRY e células de Sertoli; clivagem; mórula e blastocisto; implantação e disco bilaminar) |
| | s02 | 5 (somitos; blastóporo e deuterostômios; hCG; origem dos folhetos, INCORRETA; sequência cronológica) |
| a16 Primeiros socorros 1 | s01 | 6 (urgência × emergência; fases do atendimento; HIT; choque; isquemia/hipoxemia/hipóxia; incidente com múltiplas vítimas) |
| | s02 | 5 (talas; tipos de ferimento; entorses; concussão × contusão cerebral; conduta INCORRETA no TCE) |
| a17 Primeiros socorros 2 | s01 | 5 (corte; torniquete; hemorragia interna; PCR/DEA; obstrução parcial × total) |
| | s02 | 5 (queimadura grave; 1º grau; fogo na roupa; 3º grau; 2º grau) |
| c01 Qualidade de vida | s01 | **20** (pedido: 18) |

## Pontos que dependem do dono

1. **c01/s01 com 20 em vez de 18.** O trecho é muito amplo (pobreza, indicadores, doenças, drogas, saúde mental, sustentabilidade) e os temas do edital pedem a cobertura; a soma da aula passa de 25 em 2. Se quiser exatamente 18, basta aposentar duas (diabetes e prevenção primária/secundária/terciária são as mais dispensáveis).
2. **Queimaduras (a17/s02): divergência com a orientação atual.** O resumo do material manda lavar a queimadura de 1º grau com água em temperatura ambiente por **no máximo um minuto**, oferecer água com sal e elevar as pernas 30 cm. Protocolos atuais (inclusive pré-hospitalares) recomendam resfriar com água corrente por vários minutos (cerca de 10 a 20). Por isso **não** escrevi nenhuma questão sobre tempo de resfriamento, sal ou elevação de pernas; mantive só pontos consensuais (sem gelo, sem pomadas, sem furar bolhas, fogo na roupa, graus). Vale revisar o resumo e as questões já existentes do trecho sobre esse ponto.
3. **Classificação leve/moderada/grave das queimaduras:** usei somente o critério que é comum a qualquer tabela (lesão do trato respiratório é sempre grave; 1º grau pequeno e 2º grau muito pequeno são leves). As porcentagens exatas variam entre fontes e não foram cobradas.
4. **Trauma torácico aberto (a16/s02):** o material manda vedar totalmente a abertura; protocolos recentes (PHTLS/ATLS) falam em curativo de três lados ou válvula de alívio. Não escrevi questão nova sobre isso; a questão já existente da ferida aspirante vale ser conferida pelo dono.
5. **Imobilização com talas:** não usei a regra dos "20 minutos" do material (sem fonte oficial confirmada); a questão trata de tala rígida e acolchoada, articulação acima e abaixo e amarração fora do foco.
6. **Hanseníase:** não cobrei tempo de tratamento (6/12 meses) porque o esquema único de 6 meses (PQT-U) vem sendo adotado no Brasil; cobrei agente, órgãos acometidos, cura e gratuidade.
7. **Dados numéricos de IDH e linha de pobreza** (Brasil 0,786; US$ 3,00/dia) ficaram de fora, por mudarem a cada relatório.

## Verificações externas
- Tuberculose: "tosse por três semanas ou mais" (Ministério da Saúde, gov.br).
- RCP do adulto: 100 a 120 compressões/min, 5 a 6 cm, DEA assim que disponível (AHA).
- Demais itens (histologia, embriologia, imunologia, epidemiologia básica) conferidos com o resumo do trecho e com o conhecimento de livro-texto; nenhuma divergência relevante.
