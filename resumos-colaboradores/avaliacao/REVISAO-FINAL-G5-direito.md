# Revisão final G5: Direito Administrativo e Direito Constitucional

Escopo: `content/summaries/direito-administrativo/*.json`, `content/summaries/direito-constitucional/*.json` e as 7 entregas rejeitadas de Direito Administrativo (`resumos-colaboradores/entregas/`). Nada foi gravado em banco, importado de verdade nem versionado.

## Resultado

| Item | Antes | Depois |
| --- | --- | --- |
| Arquivos com ERRO no validador (35 arquivos G5) | 3 (Para fixar fora de 5 a 8) | **0** |
| 7 entregas rejeitadas (S0372, S0373, S0374, S0375, S0388, S0473, S0491) | rejeitadas | **0 rejeitadas e 0 com cobertura baixa** em `import_agent_summaries.py --dry-run` |
| Cobertura Direito Administrativo | OK 28, REVISAR 6, REFAÇÃO 21, ATENÇÃO 7 | OK 46, ATENÇÃO 9, REVISAR 7, **REFAÇÃO 0** |
| Cobertura Direito Constitucional | OK 65, ATENÇÃO 13, REVISAR 9 | inalterada (ver abaixo) |

O veredito da cobertura é relativo à distribuição da disciplina, por isso os 7 "REVISAR" de Direito Administrativo que restam têm nota 0,52 a 0,56 e razão de tamanho 0,44 a 0,81. As palavras que "faltam" são nomes e números de questões ilustrativas do material (Carla, Joana, Matheus, "ilha", "João"), e não conteúdo cobrável.

## Parte A: erros de "Para fixar" nos arquivos já importados

- `direito-constitucional/a04` s02 (10 itens, consolidados em 8), `direito-constitucional/a06` s02 (9 itens, consolidados em 8), `direito-administrativo/c01` s02 (4 itens, ampliados para 8). Conteúdo checado contra a Constituição e o texto do complemento; na a04/s02 incluí a estabilidade do dirigente sindical, que faltava.

## Parte C: as 7 entregas rejeitadas (corrigidas nos `.md` de `entregas/`, sem gravar no content)

| ID | Trecho | Problema | O que foi feito |
| --- | --- | --- | --- |
| S0372 | da/a06/s01 | Para fixar com 4 itens | ampliado para 7 itens |
| S0373 | da/a06/s02 | Para fixar com 4 itens | 7 itens; acrescidos lei autorizativa (Lei 9.074/1995, art. 2º), prazo, autorização vinculada em telecomunicações, permissão x concessão |
| S0374 | da/a06/s03 | Para fixar com 4 itens; **erro**: lista dos critérios do art. 15 da Lei 8.987 incluía "menor contraprestação" (critério da Lei de PPPs) | critérios corrigidos conforme a fonte (inclusive a combinação e a preferência por empresa brasileira); 7 itens |
| S0375 | da/a06/s04 | Para fixar com 4 itens | 8 itens |
| S0388 | da/a08/s04 | Para fixar com 4 itens; **vários erros**: art. 143 do CPC como responsabilidade objetiva do Estado, "Tema 841" inexistente para morte de detento, omissões (Temas 1.055, 512, 591.874, prescrição, tortura) | analítico reescrito do zero, 8 itens |
| S0473 | da/a09/s11 | cópia longa da fonte; **desatualizado**: exigia cargo "técnico ou científico" para acumular com professor | reescrito do zero seguindo a fonte (EC 138/2025, Tema 1.081, proventos, mandato, subsídio) |
| S0491 | da/a09/s15 | cópia longa da fonte | reescrito do zero (estabilidade, perda do cargo, art. 169, ADCT 19, vitaliciedade, reintegração, recondução, aproveitamento) |

## Parte B: trechos reescritos ou enriquecidos (JSON em `content/summaries/`)

Os resumos abaixo estavam fracos (3% a 30% do alvo, em geral 20% a 35%) ou continham conteúdo de outro trecho. Todos foram relidos contra o texto-fonte e refeitos (analítico e sintético; `Para fixar` com 7 a 8 itens). Vereditos de cobertura passaram de REFAÇÃO/REVISAR para OK ou ATENÇÃO.

| ID | Trecho | Observação |
| --- | --- | --- |
| S0499 | da/a01/s01 | trazia Estado e governo, assunto de outro trecho; refeito (direito público x privado, conceito, origem, objeto, função administrativa) |
| S0485 | da/a01/s02 | critérios de definição, influências estrangeiras, tendências |
| S0549 | da/a01/s03 | fontes, lei em sentido amplo, jurisprudência vinculante |
| S0561 | da/a01/s04 | costume, sistemas de controle |
| S0541 | da/a01/s05 | Estado, poderes e funções, federação |
| S0550 | da/a01/s06 | governo, presidencialismo, república |
| S0520 | da/a01/s07 | Administração em sentido amplo e estrito, atividades-fim e meio |
| S0422 | da/a03/s02 | estatais: regime, imunidade, prescrição |
| S0407 | da/a02/s03 | Direta e Indireta |
| S0391 | da/a00/s03 | supremacia, indisponibilidade, razoabilidade e proporcionalidade |
| S0414, S0415 | da/a07/s01 e s02 | controle da Administração |
| S0508, S0471, S0451, S0472 | da/a09/s02, s03, s04, s05 | cargo, emprego e função; acesso e concurso; concurso (especiais); direito à nomeação |
| S0488, S0528, S0489, S0559 | da/a09/s01, s06, s07, s08 | agentes públicos; nomeação tardia e cotas; controle judicial de concurso e comissionados; nepotismo e cargos em comissão |
| S0529, S0530, S0474, S0490, S0475, S0492 | da/a09/s09, s10, s12, s13, s14, s16 | sindicato e greve; temporários; remuneração e teto; efeito cascata e direitos sociais; licenças, RJU e previdência; responsabilidades e jurisprudência |
| S0444, S0445, S0425, S0426, S0495, S0427 | da/a05/s05, s06, s08, s10, s12, s13 | vícios do ato, mérito, espécies, extinção, convalidação |
| S0455, S0417 | da/a08/s01, da/a06/s05 | responsabilidade civil do Estado; jurisprudência de serviços públicos |
| S0208 | dc/a13/s09 (Direito Constitucional) | **atualizado** com a EC 136/2025 (data-limite de 1º de fevereiro, juros simples de 2% a.a., IPCA e Selic, limites do art. 100, § 23, e § 27) e acordos do § 20 |

### Direito Constitucional: 9 trechos REVISAR

Foram conferidos por amostragem contra a fonte (a04/s03, a02/s03, a02/s04, a03/s02, a03/s03, a08/s03, a08/s08, a10/s02). Não encontrei erro nem omissão relevante; as notas baixas decorrem de ruído (nomes de casos e números de questões). Mantidos sem alteração, exceto o a13/s09, que foi atualizado. **Pendência**: leitura integral desses 8 trechos por revisor humano, pois a verificação foi por amostragem de números, artigos, súmulas e temas.

## Lista de dúvidas para revisão humana

**Atualizações recentes que dependem do texto vigente (confirmar na Constituição e na lei):**
1. **EC 138/2025** (art. 37, XVI, b): o material diz que o professor pode acumular com cargo "de qualquer natureza" (antes: técnico ou científico). Resumo S0473 segue o material.
2. **EC 136/2025** (art. 100 e art. 3º da EC 113/2021): data-limite de 1º/2, juros de 2% a.a., limites do § 23 de 1% a 5% da RCL, § 27 (sequestro). Resumo dc/a13/s09 segue o material; emenda muito recente.
3. **Lei 15.142/2025** (reserva de 30% de vagas para pretos, pardos, indígenas e quilombolas na administração federal) e **Lei 14.768/2023** (surdez unilateral como deficiência) em S0528. Conferir percentual e alcance.
4. **Temas e julgados de 2025**: Tema 1.164 (extinção de cargos por limite de gastos), 1.424 (altura mínima na PM, 1,60 m e 1,55 m), 1.388, ADPF 1.095, ADI 7.640, Tema 1.427 (S0472 e S0492). Confirmar numeração e teses.
5. **Fim do regime jurídico único**: decisão de 2024 na ADI 2.135 (S0508, S0475), citada sem número de processo no material.

**Divergências material x texto legal ou erros prováveis do material:**
6. S0474: o material cita o art. 52, VIII, e o art. 32, VI (vereadores); o subsídio de vereadores consta no **art. 29, VI**. Resumo indica a divergência nas notas.
7. S0475: o material cita o art. 41, § 1º, como base das aposentadorias; o correto é o **art. 40, § 1º**. Também cita o art. 37, VIII, no lugar do XIII, ao tratar de vinculação.
8. S0490: o material fundamenta a SV 42 também no art. 37, XII; a vedação à vinculação está no inciso XIII.
9. S0495: o material cita ora o art. 54, ora o art. 55 da Lei 9.784/1999; a convalidação está no **art. 55**.
10. S0388: Tema 365 (condições de presídio) e RE 841.526 (morte de detento) usam a numeração do material; conferir os números dos temas de repercussão geral (365, 362, 366, 512, 777, 940, 1.055). O art. 143 do CPC faz o juiz responder regressivamente; o material fala em responsabilidade objetiva do Estado com regresso (mantive essa leitura).
11. S0427: o material atribui a Súmula 674 sem indicar o tribunal (identifiquei como STJ por associação); conferir.
12. S0391: o RE sobre transação aparece como 253.885 e 252.885 no material.
13. S0373 e S0455: o material inclui a autorização entre as formas de delegação submetidas ao art. 37, § 6º; a doutrina costuma limitar a concessão e à permissão.
14. S0422: abrangência da imunidade recíproca para estatais (ACO 3410, Tema 508, RE 407.099, RE 363.412) é jurisprudência em evolução.
15. Dúvida geral: a numeração de temas e súmulas foi mantida como no material; qualquer divergência com o STF deve ser corrigida na fonte.

**Divergências doutrinárias registradas nos resumos (válido cobrar o enfoque do autor citado):** controle da Direta sobre a Indireta (externo, interno exterior ou interno; S0414), atos normativos como fonte primária ou secundária (S0549), convalidação (ratificação, reforma, conversão; S0427), competência para os consórcios públicos (S0407), critérios de classificação de agentes (S0488), intervenção direta no domínio econômico como função administrativa (S0520).

**Figuras não reconstruídas:** o material de Direito Administrativo contém quadros e esquemas (tabelas com V/D dos elementos do ato, esquema do critério da Administração Pública, quadros de convalidação e de subsídio). Todos foram reconstruídos em texto ou tabela markdown a partir do texto e dos quadros extraídos. Não identifiquei figura essencial perdida nos trechos revisados; as notas dos agentes em `REVISAO-HUMANA-NOTAS.md` não foram reabertas trecho a trecho, exceto os trechos refeitos.

## Pendências

- Direito Constitucional: leitura integral dos 8 trechos REVISAR por revisor humano (ver acima).
- Os resumos refeitos não passaram por segunda leitura independente; recomenda-se amostragem de 5 trechos pelo dono do conteúdo, priorizando S0473, S0388, S0474, S0475 e dc/a13/s09, onde há referências recentes.
- O orquestrador deve rodar a importação real das 7 entregas de `entregas/resumos_EXT-L2_L1-06/` e `entregas/resumos_CODEX-L1_L1-DA-01/`; os `.md` já passam no `--dry-run` sem rejeitados e sem cobertura baixa.
- A reescrita dos JSON usou `json.dump(indent=2)`; o formato dos arquivos alterados pode diferir do original apenas na identação, sem mudança de esquema.
- Apenas os campos `notes` dos JSON receberam registros `[sNN revisão G5]` com as ressalvas acima.
