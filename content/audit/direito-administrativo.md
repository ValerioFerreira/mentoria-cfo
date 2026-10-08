# Auditoria estrutural: Direito Administrativo (a00–a09)

Data: 2026-10-08. Material: Estratégia, prof. Herbert Almeida, 10 aulas, 1.602 págs. Correções em `content/overrides/direito-administrativo.json`; mapa do edital em `content/edital/direito-administrativo.json`.

## Números

| | Antes | Depois |
|---|---:|---:|
| Páginas de teoria | 749 | 754 (+5: a00 págs. 5–6, a04 pág. 3, a06 págs. 3–4) |
| Trechos de Teoria | 64 | 69 |
| Cortes no meio de tópico (flag do pipeline) | 17 | 0 |
| Trechos > 17 págs. | 0 | 0 (máx. 16) |

Ressalva sobre o "0": os títulos dos tópicos deste curso são **imagens**. Eles não aparecem no texto extraído, e o cache de subtítulos vem vazio em a00/a01. Localizei cada início de tópico pelo conteúdo e o registrei em `headings`. Como o corte é sempre por página, vários tópicos começam no meio da página anterior ao corte (detalhes abaixo). O flag zerado quer dizer que todo trecho começa numa página onde um tópico real começa ou recomeça. Não quer dizer que o corte cai na primeira linha do tópico.

## Método
- Conferi o índice `.xlsx` contra o **sumário do próprio PDF** (pág. 2 de cada aula). Os "não localizados" do índice são quase todos títulos em imagem, com a página certa. As exceções divergem do sumário e foram corrigidas (ver "Auditoria inversa").
- Varri todas as páginas de cada aula com `--heads`. Localizei os subtópicos por busca de conteúdo e li as páginas de fronteira.
- Busquei na disciplina inteira os termos da Lei 8.112/1990 (readaptação, reversão, recondução, redistribuição, remoção, substituição, vacância, ajuda de custo, licenças, advertência, PAD etc.).

## Correções por aula (com motivo)

**a00 Princípios.** As págs. 5–6 (início do regime jurídico administrativo) estavam como FRONT: o índice dizia pág. 7 e o sumário diz 5. Passaram a teoria. Adicionei 11 subtítulos (um por princípio) e forcei cortes nas págs. 17, 28, 36 e 46.
- Trechos: s01 5–16 (regime jurídico, noções e legalidade) · s02 17–27 (impessoalidade, moralidade, publicidade, eficiência) · s03 28–35 (supremacia, indisponibilidade, razoabilidade/proporcionalidade) · s04 36–45 (tutela/autotutela, motivação, continuidade, contraditório) · s05 46–57 (especialidade, segurança jurídica, presunção de legitimidade, demais princípios, jurisprudência).
- Antes: s03 28–37, s04 38–46 e s05 47–57, com a autotutela partida ao meio.
- **Impacto no piloto (`content/items/direito-administrativo/a00.json`, não editado):** s01 passou de 7–16 para **5–16**. Ganhou as duas páginas iniciais do regime jurídico; os `pageRef` do piloto (7–16) continuam dentro do trecho. s02 continua 17–27. s03–s05 mudaram de limites, mas não têm itens.

**a01 Noções / Estado, governo e administração.** Não havia nenhum subtítulo. Adicionei 9 e cortei nas págs. 14, 26, 34, 50 e 58. São 7 trechos (antes 5):
- 3–13: conceito, objeto, função administrativa
- 14–25: critérios/escolas, influências, tendências
- 26–33: fontes primárias e jurisprudência
- 34–40: doutrina, costumes, sistemas administrativos
- 41–49: Estado, poderes/funções, federação
- 50–57: governo
- 58–67: sentidos de administração pública

Motivos: o antigo s01 cortava no meio dos critérios, e o antigo s04 juntava Estado com metade de Governo. A nova divisão segue os três núcleos do item 1 do edital (Estado, governo, administração).

Inícios de tópico no meio da página: os critérios começam no fim da pág. 13, o Governo na metade da 49 e a Doutrina no fim da 33.

**a02 Organização (parte 1).** Adicionei os títulos "Órgãos públicos" (pág. 14) e "Classificação dos órgãos" (pág. 20), e cortei nas págs. 34 e 49. Trechos: 3–13 · 14–24 · 25–33 (administração direta e indireta) · 34–48 (autarquias) · 49–63 (autarquias especiais e agências).

Antes, o s03 (25–37) misturava administração direta/indireta com o começo de autarquias. Os trechos 34–48 e 49–63 ficaram com 15 págs. e carga de ~16. As páginas são leves, mas o tempo vai bater no teto de 75 min. Achei melhor do que partir autarquias em blocos de 4–7 págs.

**a03 Organização (parte 2).** Adicionei 5 subtítulos de regime jurídico (patrimônio, falência, regime de pessoal, administradores, licitações) e cortei nas págs. 16 e 25. Trechos: 3–15 (EP/SEM: conceito, criação, atividades, controle, responsabilidade) · 16–24 (regime jurídico: natureza, bens, falência, imunidades, prescrição) · 25–37 (pessoal, administradores, licitações, diferenças EP × SEM) · 38–50 (fundações e jurisprudência). Antes havia corte no meio do regime de pessoal (pág. 26).

**a04 Poderes.** A pág. 3 (introdução aos poderes) estava como FRONT: o índice dizia 4, o sumário diz 3. Passou a teoria. A divisão restante já seguia os tópicos e foi mantida. O s05 47–62 tem 16 págs. (delegação de polícia → uso e abuso → jurisprudência): separar "uso e abuso" daria um trecho de 5 págs. com carga 4.

**a05 Ato administrativo (153 págs.).** O índice punha "Elementos" na pág. 32; começa na 31 (o sumário confirma). Adicionei 15 subtítulos (competência, finalidade/forma, motivo, objeto, critérios de classificação, ordinatórios, enunciativos, negociais, punitivos, decadência, revogação, limites da convalidação) e 11 cortes. São 13 trechos (antes 12):

| Trecho | Págs. | Conteúdo |
|---|---|---|
| s01 | 3–17 | Conceito e fatos |
| s02 | 18–30 | Atributos |
| s03 | 31–46 | Competência, finalidade, forma |
| s04 | 47–59 | Motivo, objeto |
| s05 | 60–68 | Vícios |
| s06 | 69–77 | Mérito (vinculação/discricionariedade) e primeiros critérios de classificação |
| s07 | 78–91 | Formação da vontade, validade, perfeição e eficácia |
| s08 | 92–101 | Normativos, ordinatórios, enunciativos |
| s09 | 102–115 | Negociais, punitivos |
| s10 | 116–125 | Modos de extinção e anulação |
| s11 | 126–138 | Decadência e revogação |
| s12 | 139–145 | Teoria das nulidades e convalidação |
| s13 | 146–155 | Limites, ratificação/reforma/conversão, confirmação, jurisprudência |

Motivos:
- Antes, Atributos levava a 1ª página de Elementos.
- Elementos era partido por número de páginas (46/47), e não por elemento.
- O antigo s06 juntava mérito com metade da classificação.
- O antigo s11 (128–142) misturava fim da decadência, revogação e início da convalidação.

O s12 (7 págs.) é curto, mas é um assunto autônomo (nulidades e convalidação). Inícios no meio da página: os negociais começam no fim da 101 e a decadência no fim da 125.

**a06 Serviços públicos.** As págs. 3–4 (noções introdutórias, art. 175 da CF) estavam como FRONT: o índice dizia 5, o sumário diz 3. Passaram a teoria. A divisão da concessão já caía em fronteiras razoáveis (13 delegação · 23 licitação/contrato · 33 encargos do poder concedente/intervenção/extinção); só adicionei os títulos.

**a07 Controle.** "Jurisprudência" estava na pág. 45, mas a 45 ainda é controle judicial (habeas data, improbidade). O título foi movido para a 46, como no sumário. O controle judicial agora fica inteiro em s04 (33–45).

**a08 Responsabilidade civil.** Eram 3 trechos, 2 deles cortados no meio. Agora são 4, com cortes nas págs. 10, 21 e 32:
- 3–9: evolução e teorias
- 10–20: art. 37, § 6º, e excludentes
- 21–31: omissão, ação regressiva/denunciação, prescrição
- 32–41: atos legislativos e jurisdicionais, notários, jurisprudência

Na pág. 10, o art. 37, § 6º, começa na linha 18. O topo da página ainda trata de prestadoras privadas, o que não prejudica o corte.

**a09 Agentes públicos (172 págs.).**
- O antigo s05/s06 (49–58/59–69) cortava "direito à nomeação" no meio. Agora: s05 49–60 (hipóteses, situações excepcionais, quadro-resumo) e s06 61–69 (nomeação tardia, reserva de vagas, isenção de taxa).
- O antigo s08/s09 juntava nepotismo com greve e partia greve/temporários. Agora: s08 81–87 (nepotismo, criação de cargo em comissão) · s09 88–96 (sindicalização e greve) · s10 97–105 (contratação temporária).
- O título "Responsabilidades do servidor" (pág. 164) foi adicionado; antes o trecho começava em "Civil".
- Os demais cortes antigos (70, 106, 118, 130, 141, 153, 164) foram mantidos como `cuts`. O corte forçado em 61 fazia o algoritmo remanejar tudo para baixo.

Resultado: 16 trechos (antes 15). Também adicionei uma `note` sobre a ausência da Lei 8.112/1990.

## Cobertura do edital (resumo; detalhe no JSON)

| Item | Situação | Onde |
|---|---|---|
| 1 Estado, governo, administração pública | covered | a01 41–67; a00 |
| 2 Direito Administrativo: conceito, fontes, princípios | covered | a01 3–36; a00 5–57 |
| 3 Centralização/desconcentração; administração direta e indireta | covered | a02, a03 |
| 3 Organização administrativa da União | **partial** | a02 25–33 (DL 200/1967); não trata a estrutura atual dos ministérios (Lei 14.600/2023) |
| 4 Espécies/classificação; cargo, emprego e função; RJU (noção, ADI 2.135); responsabilidade civil/penal/administrativa | covered | a09 3–23, 75–87, 146–147, 164–168 |
| 4 Poderes, deveres e prerrogativas | partial | a04 3–9; a09 153–163 |
| 4 RJU: provimento | **partial** | a09 24–74 e 162–163 (só visão constitucional) |
| 4 RJU: vacância, remoção, redistribuição, substituição | **gap** | sem material |
| 4 RJU: direitos e vantagens | **partial** | a09 115–145 (só remuneração constitucional) |
| 4 RJU: regime disciplinar | **partial** | a04 20–24 (poder disciplinar); a09 164–168 |
| 5 Poderes administrativos (todos) | covered | a04 3–62 (uso e abuso só 2 págs., reforçado por vícios em a05) |
| 6 Ato administrativo (todos os subitens) | covered | a05 3–155 (perfeição/validade/eficácia em 84–91; exteriorização na forma, 44–46) |
| 7 Serviços públicos e delegação | covered | a06 3–42 |
| 8 Controle administrativo/legislativo/judicial; responsabilidade civil do Estado | covered | a07 3–45; a08 3–41 |

## Lacuna principal: regime jurídico único (Lei 8.112/1990)
A Aula 09 trata agentes públicos pela **Constituição** (arts. 37–41). Ela não cobre o estatuto: formas de provimento (nomeação, posse, exercício, promoção, readaptação, reversão), vacância, remoção, redistribuição, substituição, vencimento e vantagens (indenizações, gratificações, adicionais, férias, licenças, afastamentos, concessões), deveres e proibições, penalidades, prescrição disciplinar, sindicância e PAD.

A busca na disciplina toda confirma:
- "ajuda de custo" e "cassação de aposentadoria": 0 páginas;
- "redistribuição": só 2 questões de a04;
- "readaptação": 2 menções em a09.

O `edital_audit.py` marcou o item como "COBERTO" porque a regex casa com "agentes públicos", "regime disciplinar" e "responsabilidade". **Não há entrada para isso em `content/gaps.json`.**

Ambiguidade: o edital diz "regime jurídico único" sem citar a lei. A AOCP costuma usar a Lei 8.112/1990. O estatuto dos servidores civis de PE (Lei 6.123/1968) não se aplica ao oficial bombeiro, e o Estatuto dos Militares de PE (Lei 6.783/1974) já está em legislacoes-pe. Recomendo complemento autoral baseado na Lei 8.112/1990, com validação humana da escolha.

## Auditoria inversa (achados)
- **Subindexada (corrigido):** a00 págs. 5–6, a04 pág. 3 e a06 págs. 3–4 tinham teoria classificada como abertura, por erro de página no índice `.xlsx`.
- **Indexada no lugar errado (corrigido):** a05 Elementos (32 → 31); a07 Jurisprudência (45 → 46).
- **Subindexada (corrigido com headings):** a00, a01, a05 e a09 tinham títulos em imagem ausentes do cache de subtítulos.
- **Já corretamente indexada:** questões resolvidas e quadros-resumo intercalados à teoria (padrão do autor em todas as aulas), mantidos como teoria; seções C/L começam exatamente nos marcadores do sumário em todas as aulas; nada de teoria nas seções C/L.
- **Conteúdo complementar:** a01 21–26 (influência estrangeira, tendências); a09 24–74 (concurso público, 50 págs. de jurisprudência); a09 88–113 (greve, temporários, acumulação).
- **Possível fora do escopo:** a09 148–152 (previdência dos servidores), de peso baixo; mantido.

## Pendências
1. **Lei 8.112/1990** (provimento, vacância, remoção, redistribuição, substituição, direitos e vantagens, regime disciplinar e PAD): falta material. É o item de maior risco na disciplina; ver pedidos.
2. Organização administrativa da União: tratamento parcial (DL 200/1967). Não recomendo complemento: peso baixo.
3. Os cortes por página fazem alguns tópicos começarem no fim da página anterior ao trecho (a01 págs. 13, 33 e 49; a05 págs. 101 e 125; a00 pág. 46, segurança jurídica). Só se resolve com recorte por linha, o que exigiria mudar o pipeline.
4. Os trechos a02/s04, a02/s05 e a04/s05 (15–16 págs., carga ~16) vão ficar no teto de 75 min. Escolha consciente para não fragmentar os assuntos, mas vale revisão humana.
5. O piloto a00/s01 agora cobre 5–16 (antes 7–16). Os itens continuam válidos, mas o bizu não menciona as págs. 5–6 (regimes de direito público e privado, já resumidos no item "regime jurídico da Administração").

## Pedidos ao orquestrador
- Criar a entrada em `content/gaps.json` para "Lei 8.112/1990: provimento, vacância, remoção, redistribuição, substituição, direitos e vantagens, regime disciplinar" (severidade alta; evidência acima). Decidir se haverá complemento autoral (sugestão: um módulo, ~25–35 págs., a partir do texto da lei, numerado 101+).
- Ajustar a regex do item "Agentes públicos / regime disciplinar" em `edital_audit.py`, que hoje dá falso "COBERTO" (por exemplo, exigir termos do estatuto: redistribuição, vacância, readaptação).
- (Opcional) Consertar no `.xlsx`/`xlsx_index.py` as páginas divergentes do sumário: a00 Regime Jurídico (5), a04 Deveres (3), a05 Elementos (31), a06 Conceitos (3), a07 Jurisprudência (46). Os overrides já corrigem.
- Rodar `build_catalog.py` / `build_complements.py` / seed (não rodei, como manda o briefing).
