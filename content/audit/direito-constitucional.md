# Auditoria — Direito Constitucional

Escopo: aulas a00–a18 do Estratégia (todas as páginas varridas com `--heads`; páginas suspeitas lidas) e complementos c01 (ECA), c02 (Estatuto da Juventude) e c03 (Lei Maria da Penha). Edital: Anexo II, itens 1 a 16.

## Números

| | Antes | Depois |
|---|---|---|
| Páginas de teoria (Estratégia) | 957 | 930 |
| Trechos de teoria (Estratégia) | 82 | 87 |
| Complementos (c01–c03) | 3 trechos / 20 págs. | iguais (são remontados pelo `build_complements.py`) |
| Trechos > 17 págs. | 0 | 0 (máx. 15) |
| Cortes no meio de tópico | 8 (a02, a03, a13) | 0 |

## Correções feitas (`content/overrides/direito-constitucional.json`)

| Aula | Correção | Motivo |
|---|---|---|
| a13 | Págs. 114–140 → COMMENTED; removido o título falso "Precatórios (Art. 100) - Pós ECs 113 e" na pág. 114 | O índice pôs um tópico de teoria sobre a continuação das questões comentadas (há gabaritos e "LETRA X. INCORRETA"). Eram 27 págs. de falsa teoria em 2 trechos. |
| a13 | STF movido da pág. 43 para a 40; Tribunais dos Estados da 80 para a 78; título "Precatórios (art. 100)" na pág. 82 | Os inícios reais estão nessas páginas. |
| a13 | Cortes em 13, 24, 31, 40, 53, 63, 74, 82, 91 | Um trecho por bloco: disposições gerais · garantias e estatuto da magistratura · quinto, órgão especial e reserva de plenário · CNJ · STF · STJ · Justiça Federal e do Trabalho · Justiça Eleitoral, Militar da União e Tribunais dos Estados, incluindo a **Justiça Militar estadual** · precatórios (2 trechos). Antes, o CNJ ficava no mesmo trecho que o STF e a Justiça Militar estadual ficava junto com precatórios. |
| a02 | 12 subtítulos por inciso (art. 5º, I a XXXI) e cortes em 13, 24, 34, 42 | As 52 págs. tinham um título só, e os cortes caíam no meio de incisos. Agora os trechos são: igualdade/legalidade/tortura · liberdades de expressão e de crença · intimidade e domicílio · sigilo das comunicações e liberdade profissional · locomoção, reunião, associação e propriedade. |
| a03 | 8 subtítulos (art. 5º, XXXII a LXXIX) e cortes em 14, 24, 34, 44 | Mesmo problema: os cortes caíam nas págs. 13, 35 e 45, no meio dos incisos XXXVI, LIV e LXIII. Os trechos de remédios constitucionais (HC/HD · MS · MI/AP/ACP) foram mantidos. |
| a08 | Territórios movido da pág. 37 para a 36; subtítulo art. 22 na pág. 59; cortes em 36, 51, 59, 67, 78, 87 | O trecho antigo de 17 págs. misturava territórios, bens e o início de repartição de competências, e a **intervenção** ficava colada às competências municipais. Agora: territórios/alterações/vedações/bens · repartição e art. 21 · art. 22 · arts. 23–25 · art. 30 · intervenção (6 págs., assunto autônomo e ligado à representação interventiva). |
| a09 | "Militares dos Estados (art. 42)" movido da pág. 69 para a 66 | O tópico começa na pág. 66. Para um concurso de bombeiro, o aluno precisa achar essa página. |
| a10 | Cortes em 14, 21, 32, 41, 47, 58 | Separa CPI (7 págs.) das atribuições do Congresso, junta as atribuições do Congresso, da Câmara e do Senado (antes divididas) e divide o estatuto dos congressistas em imunidades/foro e incompatibilidades/perda do mandato. |
| a15 | Cortes em 14, 19 | Estados de defesa e de sítio · Forças Armadas (art. 142, 5 págs.) · Segurança Pública (art. 144, inclui os corpos de bombeiros militares). Antes, o primeiro trecho tinha 16 págs. e misturava dois temas. |
| a17 | Cortes em 25, 35, 41, 52, 65, 77 | O controle difuso agora começa trecho próprio, súmula vinculante e recurso extraordinário ficam juntos (6 págs.) e o concentrado não divide trecho com o difuso. |
| a00 | Nota no catálogo | Avisa que recepção, repristinação, desconstitucionalização e o histórico constitucional não são ensinados. |
| a18 | `edital: partial` + nota | A aula cobre só os arts. 100 a 105-B da CE-PE. |

Divisões mantidas sem mudança: a00, a01, a04, a05, a06, a07, a09, a11, a12, a14, a16 e a18. Os trechos já seguem os tópicos e têm 8 a 15 págs.

## Cobertura do edital (resumo; detalhe em `content/edital/direito-constitucional.json`)

| Item | Status | Onde |
|---|---|---|
| 1 Conceito, classificação, elementos | coberto | a00 5–36 |
| 1 Histórico | **parcial** | só menções (a00 29–30; a17 6–7) |
| 2 Estrutura | coberto | a00 16–20 |
| 3 Poder constituinte originário/derivado, titularidade | coberto | a00 50–60; a11 45–55 |
| 3 Difuso, supranacional, mutação | coberto (raso) | a00 60–61; a11 55 |
| 3 Recepção | **parcial** | a17 12–13 (só como consequência da inexistência de inconstitucionalidade superveniente) |
| 3 Repristinação | **parcial** | a17 61 (só o efeito repristinatório da ADI) |
| 3 Desconstitucionalização | **lacuna** | — |
| 4 Eficácia e aplicabilidade | coberto | a00 37–49 |
| 5 Controle (conceito, sistemas, momentos, difuso, concentrado, ADI, ADO, ADC, ADPF) | coberto | a17 3–90 |
| 5 Representação interventiva | coberto | a17 70–71 + a08 87–92 |
| 6 Direitos e garantias, sociais, nacionalidade, políticos, partidos, remédios | coberto | a01–a07 |
| 7 Organização do Estado, competências | coberto | a08; a12 3–7 |
| 7 Administração pública e servidores (arts. 37–41) | coberto | a09 3–65 |
| 7 Militares dos Estados (art. 42) | coberto | a09 66–69; a15 14–18; a18 5–7 |
| 8 Legislativo, Executivo, Judiciário | coberto | a10–a13 |
| 9 Funções essenciais | coberto | a14 |
| 10 Defesa do Estado | coberto | a15 |
| 11 Ordem social | coberto | a16 |
| 12 Constituição de Pernambuco | **parcial** | a18 5–13 (arts. 100–105-B) |
| 13 Súmulas e jurisprudência | coberto (transversal) | distribuído; súmula vinculante em a17 35–37 |
| 14 ECA | complemento | c01 (+ a16 62–65) |
| 15 Estatuto da Juventude | complemento | c02 |
| 16 Maria da Penha | complemento | c03 |

## Auditoria inversa (achados)

- **Indexada no lugar errado:** a13 114–140 (questões tratadas como teoria); a13 STF (pág. 40), Tribunais dos Estados (pág. 78); a08 Territórios (pág. 36); a09 Militares dos Estados (pág. 66). Todos corrigidos.
- **Subindexada:** a02 e a03 (art. 5º sem subtítulos); a13 precatórios sem título; a08 art. 22. Todos corrigidos.
- **Já corretamente indexada:** questões resolvidas intercaladas na teoria (estilo do material, em todas as aulas); a18: fechamento na pág. 14 e gabarito nas págs. 40–41.
- **Necessita revisão humana:** a09 49–59, previdência do servidor civil (art. 40). Está no edital ("servidores públicos"), mas tem pouca utilidade para o militar estadual. a13 82–100, precatórios (19 págs., 2 trechos). Está no edital (Judiciário), mas é de baixa incidência. As duas partes foram mantidas; avaliar se merecem só a camada Completo.
- **Conteúdo complementar:** a16 62–65 (art. 227) dá a base constitucional de c01 e c02.
- Nenhuma página de teoria classificada como C/L/S/F/B foi encontrada.

## Complementos

- **c01 ECA (9 págs.): correto no núcleo, com 3 correções feitas no `.md`.**
  1. Viagens (art. 83): a regra agora vale para **menor de 16 anos** e exige autorização judicial (redação da Lei 13.812/2019). Entraram também as dispensas e as regras de viagem ao exterior (art. 84). O texto antigo falava só em "criança" e era impreciso.
  2. O macete do art. 101 dizia que a colocação em família substituta (IX) é "provisória e excepcional". Pelo art. 101, § 1º, isso vale só para os acolhimentos (VII e VIII). O acolhimento emergencial agora cita o art. 93 (comunicação ao juiz em 24 h).
  3. Conselho Tutelar: incluídas as atribuições dadas pela Lei 14.344/2022 (violência doméstica contra criança e adolescente).

  Os demais números foram conferidos e estão corretos: idades, acolhimento (3 e 18 meses), adoção, medidas socioeducativas, internação (45 dias, 6 meses, 3 anos, 21 anos) e Conselho Tutelar (5 membros, 4 anos, recondução por novos processos). Para o peso do item, é suficiente.
- **c02 Juventude (4 págs.): correto e suficiente** para uma lei de 48 artigos. Sem alteração.
- **c03 Maria da Penha (7 págs.): correto e atualizado.** Já traz o art. 12-D (Lei 15.383/2026), o art. 16-A (Lei 15.438/2026, decadência em 12 meses) e a pena do art. 24-A (2 a 5 anos). Os dois artigos novos foram conferidos em publicações da Câmara/Senado, porque o portal do Planalto recusou a conexão. Sem alteração.
- Depois da edição do c01, rodar `build_complements.py` para regenerar o PDF.

## Pendências

1. **Desconstitucionalização (lacuna), recepção e repristinação (parciais):** o material não tem a teoria do direito constitucional intertemporal. São temas clássicos de prova e o edital os nomeia expressamente. **Sugestão de complemento curto (3–4 págs.):** recepção e não recepção, recepção material, repristinação (LINDB, art. 2º, § 3º, e vedação da repristinação tácita), desconstitucionalização (não adotada no Brasil), além de mutação × reforma, com remissões à a00 e à a17. Decisão do orquestrador.
2. **Histórico constitucional (parcial):** falta um panorama de 1824 a 1988. Pode entrar no mesmo complemento (1–2 págs.).
3. **Constituição de Pernambuco (parcial):** a a18 tem 9 págs. e cobre só militares e segurança pública (arts. 100–105-B), que é o núcleo mais provável para bombeiro. O edital, porém, pede a CE-PE sem recorte. **Sugestão de complemento** com o restante: princípios e organização do Estado e dos Municípios, Assembleia e processo legislativo estadual (inclusive emenda à CE), Governador, TJPE/Justiça Militar estadual, administração pública e servidores estaduais e ordem social estadual. Deve ser escrito a partir do texto oficial da ALEPE; os números de artigo não foram verificados aqui.
4. Precatórios (a13) e previdência do servidor civil (a09): validar a prioridade (ver acima).
5. ECA: não verifiquei no Planalto se há alterações de 2025–2026 no texto do próprio ECA, porque a conexão com o portal falhou. Conferir antes de aprovar.

## Pedidos ao orquestrador

- Rodar `build_catalog.py` e depois `build_complements.py`. O `segment.py --subject direito-constitucional` regrava `segments/` sem os trechos c01–c03, que o `build_complements.py` repõe. Em seguida, rodar o seed.
- Decidir sobre os complementos sugeridos: (a) direito intertemporal + histórico; (b) CE-PE além dos arts. 100–105-B.
