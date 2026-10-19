# Cadernos do TecConcursos a montar — PCPE Agente de Polícia (Cebraspe)

> Gerado por `pipeline/pcpe_tools/gen_cadernos_tec.py` a partir do edital do PCPE (`content/edital`) e dos trechos do plano (`importance/segments.json`). Planilha equivalente: `PCPE-CADERNOS-TEC.csv`.

## Filtros comuns a todos os cadernos

- **Banca:** CEBRASPE (aparece como *CESPE / CEBRASPE*, *Cebraspe* ou *Cespe/UnB*; marque todas as grafias que o TEC oferecer). O caderno das atividades e os simulados do PCPE usam **só** essa banca.
- **Questões:** exclua *anuladas* e *desatualizadas*. Mantenha **Certo/Errado e múltipla escolha** (a prova do PCPE tem 60 itens e o sistema importa os dois tipos).
- **Ano:** de 2015 em diante para as disciplinas de legislação (Direito Constitucional, Administrativo, Penal, Processual Penal, Legislação Penal Especial, Legislação do PCPE); de 2012 em diante nas demais. Se faltar volume, amplie o intervalo.
- **Órgão/Cargo:** não restrinja (Polícia Civil, Polícia Federal, PRF, tribunais e MP servem); só na *Legislação do PCPE* filtre **Órgão = PC-PE**.
- **Ordenação:** por **Assunto** (ajuda a importar e classificar). **Nome do caderno:** exatamente o da tabela (o importador usa o título do caderno para organizar o relatório).
- **Exportar:** *Imprimir caderno* → PDF → salvar em `docs/questoes/`. Depois: `pipeline/.venv/Scripts/python pipeline/questoes/importar.py` (hoje o importador classifica só as matérias do CBMPE/PMPE; veja o aviso abaixo).
- **Tamanho:** cada caderno tem até ~220 questões (o tamanho dos cadernos já importados). Se o TEC não achar a meta, o **piso** é o mínimo que mantém ~5 questões por trecho de Teoria (o caderno das atividades usa 25 questões a cada até 4 Teorias).

## Resumo

| Disciplina | Questões na prova | Trechos no plano | Cadernos | Meta de questões |
| --- | ---: | ---: | ---: | ---: |
| Legislação Estadual (Pernambuco) / Legislação Específica | 4 | 12 | 1 | 108 |
| Direito Constitucional (CF/1988 e Doutrina) | 4 | 79 | 4 | 636 |
| Direito Administrativo (Doutrina e Leis Federais) | 4 | 120 | 6 | 936 |
| Direito Penal (Doutrina e Código Penal) | 3 | 69 | 4 | 556 |
| Legislação Penal e Processual Penal Especial | 2 | 29 | 2 | 248 |
| Direito Processual Penal (Doutrina e CPP) | 3 | 39 | 2 | 324 |
| Língua Portuguesa (Português) | 10 | 59 | 3 | 472 |
| Informática | 10 | 53 | 3 | 424 |
| Raciocínio Lógico | 3 | 89 | 4 | 724 |
| Matemática | 3 | 16 | 1 | 152 |
| Estatística | 4 | 36 | 2 | 292 |
| Contabilidade Geral | 10 | 45 | 2 | 380 |
| **Total** | 60 | 646 | 34 | 5252 |

## Cadernos

### PCPE LEGPCPE — Legislação Estadual (Pernambuco) / Legislação Específica  (meta 108 · piso 69)

_Filtre Órgão = PC-PE; se a matéria não existir, pesquise pelo nome da lei._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Constituição Estadual (PE) – Segurança Pública, arts. 101 a 105-B ⚠ complemento/lacuna | 1 | 12 |
| 2 | Estatuto do Policial Civil de PE (Lei 6.425/1972) | 4 | 32 |
| 3 | Estatuto dos Servidores Públicos do Estado de PE (Lei 6.123/1968) | 5 | 40 |
| 4 | Lei Complementar Estadual 137/2008 | 1 | 12 |
| 5 | Lei Complementar Estadual 317/2015 | 1 | 12 |

### PCPE DCONST 1 — Direito Constitucional (CF/1988 e Doutrina)  (meta 88 · piso 55)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Princípios fundamentais; Poder constituinte; Teoria da Constituição | 6 | 48 |
| 2 | Aplicabilidade e eficácia das normas constitucionais | 5 | 40 |

### PCPE DCONST 2 — Direito Constitucional (CF/1988 e Doutrina)  (meta 152 · piso 95)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 3 | Direitos e garantias fundamentais (individuais, coletivos, sociais, nacionalidade, políticos); remédios constitucionais | 19 | 152 |

### PCPE DCONST 3 — Direito Constitucional (CF/1988 e Doutrina)  (meta 184 · piso 115)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 4 | Organização do Estado: federação, União, estados, DF, municípios, territórios; intervenção | 10 | 80 |
| 5 | Administração pública (art. 37) e servidores públicos | 13 | 104 |

### PCPE DCONST 4 — Direito Constitucional (CF/1988 e Doutrina)  (meta 212 · piso 133)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6 | Poder Executivo | 10 | 80 |
| 7 | Poder Legislativo; processo legislativo; CPI | 8 | 64 |
| 8 | Poder Judiciário | 3 | 24 |
| 9 | Funções essenciais à justiça: MP, advocacia pública, defensoria | 2 | 16 |
| 10 | Defesa do Estado e das instituições democráticas; Segurança Pública (art. 144) | 2 | 16 |
| 11 | Constituição do Estado de Pernambuco – Segurança Pública | 1 | 12 |

### PCPE DADM 1 — Direito Administrativo (Doutrina e Leis Federais)  (meta 208 · piso 130)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Estado, governo e administração; princípios | 2 | 16 |
| 2 | Conceito, objeto e fontes do Direito Administrativo | 2 | 16 |
| 3 | Atos administrativos | 5 | 40 |
| 4 | Poderes administrativos; uso e abuso de poder | 7 | 56 |
| 5 | Regime jurídico-administrativo; princípios | 5 | 40 |
| 6 | Responsabilidade civil do Estado | 5 | 40 |

### PCPE DADM 2 — Direito Administrativo (Doutrina e Leis Federais)  (meta 56 · piso 35)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 7 | Serviços públicos; concessão, permissão, autorização | 4 | 32 |
| 8 | Organização administrativa; administração direta e indireta | 3 | 24 |

### PCPE DADM 3 — Direito Administrativo (Doutrina e Leis Federais)  (meta 240 · piso 150)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 9 | Controle da administração; improbidade (Lei 8.429/1992); Lei de Abuso/Acesso quando constar | 30 | 240 |

### PCPE DADM 4 — Direito Administrativo (Doutrina e Leis Federais)  (meta 24 · piso 15)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 10 | Processo administrativo (Lei 9.784/1999 e Lei estadual 11.781/2000) | 3 | 24 |

### PCPE DADM 5 — Direito Administrativo (Doutrina e Leis Federais)  (meta 320 · piso 200)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 11 | Licitações e contratos (Lei 14.133/2021 e, para provas antigas, 8.666/1993) | 43 | 320 |

### PCPE DADM 6 — Direito Administrativo (Doutrina e Leis Federais)  (meta 88 · piso 55)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 12 | Agentes públicos; Estatuto federal (Lei 8.112/1990) como base | 6 | 48 |
| 13 | Cargo, emprego e função; provimento, vacância; responsabilidades | 5 | 40 |

### PCPE DPEN 1 — Direito Penal (Doutrina e Código Penal)  (meta 128 · piso 80)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Princípios do Direito Penal | 2 | 16 |
| 2 | Teoria do crime: fato típico, ilicitude, culpabilidade, erro | 10 | 80 |
| 3 | Aplicação da lei penal no tempo e no espaço; conflito aparente | 4 | 32 |

### PCPE DPEN 2 — Direito Penal (Doutrina e Código Penal)  (meta 112 · piso 70)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 4 | Crimes contra a pessoa (homicídio, lesões, periclitação, honra, liberdade individual) | 14 | 112 |

### PCPE DPEN 3 — Direito Penal (Doutrina e Código Penal)  (meta 176 · piso 110)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 5 | Crimes contra o patrimônio | 14 | 112 |
| 6 | Crimes contra a dignidade sexual | 8 | 64 |

### PCPE DPEN 4 — Direito Penal (Doutrina e Código Penal)  (meta 140 · piso 88)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 7 | Crimes contra a administração pública (peculato, corrupção, contrabando, desacato, falso testemunho…) | 16 | 128 |
| 20 | Direito penal na Constituição (art. 5º) | 1 | 12 |

### PCPE LPE 1 — Legislação Penal e Processual Penal Especial  (meta 192 · piso 122)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 8 | Crimes hediondos (Lei 8.072/1990) | 3 | 24 |
| 9 | Racismo (Lei 7.716/1989) | 1 | 12 |
| 10 | Abuso de autoridade (Lei 13.869/2019) | 2 | 16 |
| 11 | Tortura (Lei 9.455/1997) | 1 | 12 |
| 12 | ECA – crimes e infrações administrativas (Lei 8.069/1990) ⚠ complemento/lacuna | 1 | 12 |
| 13 | Organização criminosa (Lei 12.850/2013) | 2 | 16 |
| 14 | Crimes de trânsito (Lei 9.503/1997 – CTB) | 2 | 16 |
| 15 | Violência doméstica (Lei Maria da Penha 11.340/2006) | 3 | 24 |
| 16 | Lei de Drogas (Lei 11.343/2006) | 6 | 48 |
| 17 | Violência contra criança e adolescente (Lei 14.344/2022 – Henry Borel) | 1 | 12 |

### PCPE LPE 2 — Legislação Penal e Processual Penal Especial  (meta 56 · piso 35)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 18 | Crimes ambientais (Lei 9.605/1998) | 4 | 32 |
| 19 | Estatuto do Desarmamento (Lei 10.826/2003) | 3 | 24 |

### PCPE DPP 1 — Direito Processual Penal (Doutrina e CPP)  (meta 216 · piso 136)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Lei processual penal no tempo, no espaço e quanto às pessoas | 1 | 12 |
| 2 | Inquérito policial | 3 | 24 |
| 3 | Provas; cadeia de custódia; interrogatório; testemunhas | 11 | 88 |
| 4 | Prisão em flagrante, preventiva, liberdade provisória e fiança | 10 | 80 |
| 5 | Medidas cautelares diversas da prisão | 1 | 12 |

### PCPE DPP 2 — Direito Processual Penal (Doutrina e CPP)  (meta 108 · piso 68)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6 | Prisão temporária (Lei 7.960/1989) | 1 | 12 |
| 7 | Juizados Especiais Criminais (Lei 9.099/1995) | 5 | 40 |
| 8 | Investigação criminal conduzida por delegado (Lei 12.830/2013) | 2 | 16 |
| 9 | Princípios constitucionais do processo penal | 5 | 40 |

### PCPE PORT 1 — Língua Portuguesa (Português)  (meta 152 · piso 95)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Compreensão e interpretação de textos | 2 | 16 |
| 2 | Tipologia e gêneros textuais | 3 | 24 |
| 3 | Ortografia oficial; acentuação | 5 | 40 |
| 4 | Coesão textual; coesão e coerência; pronomes e conectivos | 9 | 72 |

### PCPE PORT 2 — Língua Portuguesa (Português)  (meta 224 · piso 140)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 5 | Morfossintaxe: classes de palavras, termos da oração, período composto, pontuação, concordância, regência, crase | 28 | 224 |

### PCPE PORT 3 — Língua Portuguesa (Português)  (meta 96 · piso 60)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6 | Reescrita de frases e parágrafos | 6 | 48 |
| 7 | Correspondência oficial (Manual de Redação da Presidência) | 6 | 48 |

### PCPE INFO 1 — Informática  (meta 120 · piso 75)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Windows (explorador, configurações, atalhos) | 15 | 120 |

### PCPE INFO 2 — Informática  (meta 200 · piso 125)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 2 | Microsoft 365: Word, Excel, PowerPoint | 25 | 200 |

### PCPE INFO 3 — Informática  (meta 104 · piso 65)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 3 | Redes, Internet/intranet, segurança, nuvem, redes sociais | 13 | 104 |

### PCPE RLOG 1 — Raciocínio Lógico  (meta 184 · piso 115)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Conjuntos numéricos | 2 | 16 |
| 2 | Sistema legal de medidas | 2 | 16 |
| 3 | Razão, proporção, regra de três, porcentagem | 9 | 72 |
| 4 | Equações e inequações | 10 | 80 |

### PCPE RLOG 2 — Raciocínio Lógico  (meta 208 · piso 130)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 5 | Sistemas lineares | 5 | 40 |
| 6 | Funções e gráficos | 11 | 88 |
| 7 | Análise combinatória | 8 | 64 |
| 8 | Progressões | 2 | 16 |

### PCPE RLOG 3 — Raciocínio Lógico  (meta 176 · piso 110)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 9 | Estruturas lógicas | 3 | 24 |
| 10 | Lógica de argumentação | 4 | 32 |
| 11 | Lógica proposicional | 9 | 72 |
| 12 | Lógica de primeira ordem (quantificadores) | 6 | 48 |

### PCPE RLOG 4 — Raciocínio Lógico  (meta 156 · piso 98)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 13 | Contagem e probabilidade | 6 | 48 |
| 14 | Operações com conjuntos (diagramas de Venn) ⚠ complemento/lacuna | 0 | 12 |
| 15 | Problemas aritméticos, geométricos e matriciais; matrizes e determinantes ⚠ complemento/lacuna | 12 | 96 |

### PCPE MAT — Matemática  (meta 152 · piso 96)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Conjuntos numéricos e operações | 2 | 16 |
| 2 | Funções: afim, quadrática, exponencial, logarítmica | 6 | 48 |
| 3 | Progressões | 3 | 24 |
| 4 | Análise combinatória | 0 | 12 |
| 5 | Probabilidade | 0 | 12 |
| 6 | Sistemas lineares e equações | 5 | 40 |

### PCPE EST 1 — Estatística  (meta 152 · piso 95)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Estatística descritiva e análise exploratória (gráficos, medidas de posição e dispersão) | 19 | 152 |

### PCPE EST 2 — Estatística  (meta 140 · piso 88)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 2 | Probabilidade (axiomas, condicional, independência) | 16 | 128 |
| 3 | Amostragem e tamanho amostral ⚠ complemento/lacuna | 1 | 12 |

### PCPE CONT 1 — Contabilidade Geral  (meta 176 · piso 112)

_Cebraspe cobra pouco: veja a observação sobre outras bancas._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Conceitos e finalidades da contabilidade | 2 | 16 |
| 2 | Patrimônio e equação fundamental | 1 | 12 |
| 3 | Atos e fatos administrativos | 1 | 12 |
| 4 | Contas, débito e crédito | 2 | 16 |
| 5 | Plano de contas | 1 | 12 |
| 6 | Escrituração e lançamentos | 4 | 32 |
| 7 | Operações diversas (juros, descontos, tributos, aluguéis…) | 8 | 64 |
| 8 | Balancete de verificação | 1 | 12 |

### PCPE CONT 2 — Contabilidade Geral  (meta 204 · piso 128)

_Cebraspe cobra pouco: veja a observação sobre outras bancas._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 9 | Balanço patrimonial | 9 | 72 |
| 10 | DRE | 1 | 12 |
| 11 | CPC / princípios contábeis | 15 | 120 |

## Avisos

1. **Contabilidade Geral:** o Cebraspe cobra pouca Contabilidade em provas de polícia; é provável que o TEC devolva menos que a meta. O plano e os simulados do PCPE só usam Cebraspe, então vale decidir antes se Contabilidade pode usar outras bancas (FCC, FGV, Vunesp…) no caderno das atividades. Monte também um caderno **sem filtro de banca** (nome `PCPE CONT extra`) para o treino livre.
2. **Itens com ⚠:** têm material complementar ou lacuna no conteúdo; a classificação dessas questões depende de os complementos estarem no catálogo.
3. **Matemática × Raciocínio Lógico:** o edital do PCPE repete assuntos (análise combinatória, probabilidade) nas duas disciplinas. Os cadernos de RL cobrem esses assuntos; no de Matemática, itens 4 e 5 não geram trechos próprios (marcados com 0 trechos): pode pular.
4. **Importação:** `content/questoes/mapa-assuntos.json` ainda não tem as matérias do TEC de Direito Penal, Processo Penal, Contabilidade e Legislação PCPE, e o classificador só reconhece os cadernos do CBMPE/PMPE. Isso faz parte do **importador de questões por concurso** (sessão separada, ainda pendente): baixar os PDFs agora e importar depois é seguro.
