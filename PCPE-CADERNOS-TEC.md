# Cadernos do TecConcursos a montar — PCPE Agente de Polícia (Cebraspe)

> Gerado por `pipeline/pcpe_tools/gen_cadernos_tec.py` a partir do edital do PCPE (`content/edital`) e dos trechos do plano (`importance/segments.json`). Planilha equivalente: `PCPE-CADERNOS-TEC.csv`.

## Filtros comuns a todos os cadernos

- **Banca:** CEBRASPE (aparece como *CESPE / CEBRASPE*, *Cebraspe* ou *Cespe/UnB*; marque todas as grafias que o TEC oferecer). O caderno das atividades e os simulados do PCPE usam **só** essa banca.
- **Questões:** exclua *anuladas* e *desatualizadas*. Prefira **múltipla escolha com 5 alternativas**: o edital do PCPE (item 8.2) define a prova objetiva assim, com 60 questões (20 de Noções de Direito e 40 de Conhecimentos Específicos). Certo/Errado também serve para treino por assunto, e o sistema importa os dois tipos.
- **Ano:** de 2015 em diante para as disciplinas de legislação (Direito Constitucional, Administrativo, Penal, Processual Penal, Legislação Penal Especial, Legislação do PCPE); de 2012 em diante nas demais. Se faltar volume, amplie o intervalo.
- **Órgão/Cargo:** não restrinja (Polícia Civil, Polícia Federal, PRF, tribunais e MP servem); só na *Legislação do PCPE* filtre **Órgão = PC-PE**.
- **Ordenação:** por **Assunto** (ajuda a importar e classificar). **Nome do caderno:** exatamente o da tabela (o importador usa o título do caderno para organizar o relatório).
- **Exportar:** *Imprimir caderno* → PDF → salvar em `docs/questoes/`. Depois: `pipeline/.venv/Scripts/python pipeline/questoes/importar.py` (hoje o importador classifica só as matérias do CBMPE/PMPE; veja o aviso abaixo).
- **Tamanho:** cada caderno tem até ~220 questões (o tamanho dos cadernos já importados). Se o TEC não achar a meta, o **piso** é o mínimo que mantém ~5 questões por trecho de Teoria (o caderno das atividades usa 25 questões a cada até 4 Teorias).

## Resumo

| Disciplina | Questões na prova | Trechos no plano | Cadernos | Meta de questões |
| --- | ---: | ---: | ---: | ---: |
| Legislação Estadual (Pernambuco) / Legislação Específica | 4 | 12 | 1 | 108 |
| Direito Constitucional (CF/1988 e Doutrina) | 4 | 70 | 4 | 596 |
| Direito Administrativo (Doutrina e Leis Federais) | 4 | 109 | 5 | 920 |
| Direito Penal (Doutrina e Código Penal) | 3 | 69 | 4 | 556 |
| Legislação Penal e Processual Penal Especial | 2 | 29 | 2 | 248 |
| Direito Processual Penal (Doutrina e CPP) | 3 | 38 | 2 | 324 |
| Língua Portuguesa (Português) | 10 | 54 | 3 | 516 |
| Informática | 10 | 67 | 3 | 576 |
| Raciocínio Lógico | 3 | 72 | 4 | 632 |
| Matemática | 3 | 44 | 2 | 372 |
| Estatística | 4 | 32 | 2 | 280 |
| Contabilidade Geral | 10 | 44 | 2 | 380 |
| **Total** | 60 | 640 | 34 | 5508 |

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

### PCPE DCONST 1 — Direito Constitucional (CF/1988 e Doutrina)  (meta 208 · piso 131)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1.1 | Princípios fundamentais da CF/88 (arts. 1º a 4º) ⚠ complemento/lacuna | 1 | 12 |
| 1.2 | Poder constituinte (originário, derivado e decorrente) | 2 | 16 |
| 2 | Aplicabilidade e eficácia das normas constitucionais | 1 | 12 |
| 3 | Direitos e garantias fundamentais (individuais, coletivos, sociais, nacionalidade, políticos); remédios constitucionais | 21 | 168 |

### PCPE DCONST 2 — Direito Constitucional (CF/1988 e Doutrina)  (meta 144 · piso 90)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 4 | Organização do Estado: federação, União, estados, DF, municípios, territórios; competências; intervenção | 10 | 80 |
| 5 | Administração pública (art. 37) e servidores públicos | 6 | 48 |
| 6 | Poder Executivo | 2 | 16 |

### PCPE DCONST 3 — Direito Constitucional (CF/1988 e Doutrina)  (meta 208 · piso 131)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 7 | Poder Legislativo; processo legislativo; CPI | 11 | 88 |
| 8 | Poder Judiciário | 10 | 80 |
| 9.1 | Ministério Público | 2 | 16 |
| 9.2 | Advocacia pública | 1 | 12 |
| 9.3 | Defensoria Pública | 0 | 12 |

### PCPE DCONST 4 — Direito Constitucional (CF/1988 e Doutrina)  (meta 36 · piso 23)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 10 | Defesa do Estado e das instituições democráticas; Segurança Pública (art. 144) | 3 | 24 |
| 11 | Constituição do Estado de Pernambuco – Segurança Pública ⚠ complemento/lacuna | 0 | 12 |

### PCPE DADM 1 — Direito Administrativo (Doutrina e Leis Federais)  (meta 200 · piso 125)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Estado, governo e administração pública | 8 | 64 |
| 2 | Conceito, objeto e fontes do Direito Administrativo | 4 | 32 |
| 3 | Atos administrativos | 13 | 104 |

### PCPE DADM 2 — Direito Administrativo (Doutrina e Leis Federais)  (meta 220 · piso 139)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 4.1 | Poderes: hierárquico, disciplinar, regulamentar e de polícia | 4 | 32 |
| 4.2 | Uso e abuso do poder | 1 | 12 |
| 5.1 | Regime jurídico-administrativo | 0 | 12 |
| 5.2 | Princípios expressos e implícitos da administração | 0 | 12 |
| 6 | Responsabilidade civil do Estado | 4 | 32 |
| 7 | Serviços públicos; concessão, permissão, autorização | 4 | 32 |
| 8.1 | Centralização, descentralização, concentração e desconcentração | 2 | 16 |
| 8.2 | Administração direta e indireta | 7 | 56 |
| 9.1 | Controle administrativo | 2 | 16 |

### PCPE DADM 3 — Direito Administrativo (Doutrina e Leis Federais)  (meta 120 · piso 76)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 9.2 | Controle judicial | 1 | 12 |
| 9.3 | Controle legislativo | 1 | 12 |
| 9.4 | Improbidade administrativa (Lei 8.429/1992) | 9 | 72 |
| 10 | Processo administrativo (Lei 9.784/1999 e Lei estadual 11.781/2000) ⚠ complemento/lacuna | 3 | 24 |

### PCPE DADM 4 — Direito Administrativo (Doutrina e Leis Federais)  (meta 280 · piso 175)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 11 | Licitações e contratos (Lei 14.133/2021 e, para provas antigas, 8.666/1993) | 35 | 280 |

### PCPE DADM 5 — Direito Administrativo (Doutrina e Leis Federais)  (meta 100 · piso 63)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 12.1 | Agentes públicos: legislação pertinente | 3 | 24 |
| 12.2 | Agentes públicos: disposições constitucionais ⚠ complemento/lacuna | 0 | 12 |
| 13 | Cargo, emprego e função pública; provimento e vacância | 8 | 64 |

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
| 5 | Medidas cautelares diversas da prisão | 0 | 12 |

### PCPE DPP 2 — Direito Processual Penal (Doutrina e CPP)  (meta 108 · piso 68)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6 | Prisão temporária (Lei 7.960/1989) | 1 | 12 |
| 7 | Juizados Especiais Criminais (Lei 9.099/1995) | 5 | 40 |
| 8 | Investigação criminal conduzida por delegado (Lei 12.830/2013) | 2 | 16 |
| 9 | Princípios constitucionais do processo penal | 5 | 40 |

### PCPE PORT 1 — Língua Portuguesa (Português)  (meta 192 · piso 120)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Compreensão e interpretação de textos | 3 | 24 |
| 2 | Tipologia e gêneros textuais | 3 | 24 |
| 3 | Ortografia oficial; acentuação | 5 | 40 |
| 4.1 | Coesão textual: referenciação, conectores, sequenciação | 7 | 56 |
| 4.2 | Tempos e modos verbais | 6 | 48 |

### PCPE PORT 2 — Língua Portuguesa (Português)  (meta 216 · piso 137)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 5.1 | Classes de palavras | 6 | 48 |
| 5.2 | Coordenação (orações e termos) | 3 | 24 |
| 5.3 | Subordinação (orações e termos) | 1 | 12 |
| 5.4 | Pontuação | 4 | 32 |
| 5.5 | Concordância verbal e nominal | 4 | 32 |
| 5.6 | Regência verbal e nominal | 2 | 16 |
| 5.7 | Crase | 1 | 12 |
| 5.8 | Colocação pronominal | 1 | 12 |
| 6.1 | Significação das palavras | 2 | 16 |
| 6.2 | Substituição de palavras ou trechos | 0 | 12 |

### PCPE PORT 3 — Língua Portuguesa (Português)  (meta 108 · piso 70)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6.3 | Reorganização de orações e períodos | 0 | 12 |
| 6.4 | Reescrita e níveis de formalidade | 6 | 48 |
| 7.1 | Redação oficial: aspectos gerais | 0 | 12 |
| 7.2 | Redação oficial: finalidade dos expedientes | 0 | 12 |
| 7.3 | Redação oficial: adequação da linguagem | 0 | 12 |
| 7.4 | Redação oficial: formato do texto | 0 | 12 |

### PCPE INFO 1 — Informática  (meta 196 · piso 123)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1.1 | Windows: janelas, menus, barra de tarefas, área de trabalho | 5 | 40 |
| 1.2 | Windows: pastas e arquivos | 4 | 32 |
| 1.3 | Windows: configurações básicas | 6 | 48 |
| 1.4 | Windows Explorer | 0 | 12 |
| 2.1 | Word | 8 | 64 |

### PCPE INFO 2 — Informática  (meta 220 · piso 138)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 2.2 | Excel | 10 | 80 |
| 2.3 | PowerPoint | 5 | 40 |
| 3.1 | Internet, intranet, redes sociais, nuvem, deep web e dark web | 11 | 88 |
| 3.2 | Correio eletrônico | 0 | 12 |

### PCPE INFO 3 — Informática  (meta 160 · piso 101)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 3.3 | Navegadores e sítios de busca | 0 | 12 |
| 3.4 | Segurança: malwares, antivírus, criptografia | 17 | 136 |
| 3.5 | Backup e armazenamento na nuvem | 1 | 12 |

### PCPE RLOG 1 — Raciocínio Lógico  (meta 64 · piso 40)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 7 | Princípios de contagem (análise combinatória) | 8 | 64 |

### PCPE RLOG 2 — Raciocínio Lógico  (meta 168 · piso 105)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 9 | Estruturas lógicas | 21 | 168 |

### PCPE RLOG 3 — Raciocínio Lógico  (meta 200 · piso 126)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 10 | Lógica de argumentação | 22 | 176 |
| 11.1 | Proposições simples e compostas | 0 | 12 |
| 11.2 | Tabelas-verdade | 0 | 12 |

### PCPE RLOG 4 — Raciocínio Lógico  (meta 200 · piso 127)

_Se a matéria não tiver o assunto, use também 'Matemática'._

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 11.3 | Equivalências lógicas | 11 | 88 |
| 11.4 | Leis de De Morgan; negações | 0 | 12 |
| 11.5 | Diagramas lógicos | 2 | 16 |
| 12 | Lógica de primeira ordem (quantificadores) | 0 | 12 |
| 13 | Contagem e probabilidade | 6 | 48 |
| 14 | Operações com conjuntos (diagramas de Venn) ⚠ complemento/lacuna | 1 | 12 |
| 15 | Problemas matriciais: matrizes e determinantes ⚠ complemento/lacuna | 1 | 12 |

### PCPE MAT 1 — Matemática  (meta 188 · piso 119)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Conjuntos numéricos e operações | 4 | 32 |
| 2 | Sistema legal de medidas | 2 | 16 |
| 3 | Razões e proporções | 5 | 40 |
| 3.1 | Divisão proporcional ⚠ complemento/lacuna | 1 | 12 |
| 3.2 | Regras de três simples e compostas | 1 | 12 |
| 3.3 | Porcentagem | 3 | 24 |
| 4 | Equações e inequações de 1º e 2º graus | 5 | 40 |
| 5 | Sistemas lineares ⚠ complemento/lacuna | 0 | 12 |

### PCPE MAT 2 — Matemática  (meta 184 · piso 115)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 6 | Funções e gráficos (afim e quadrática) | 12 | 96 |
| 8 | Progressões aritméticas e geométricas | 3 | 24 |
| 15 | Problemas aritméticos e geométricos (geometria plana) | 8 | 64 |

### PCPE EST 1 — Estatística  (meta 216 · piso 135)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 1 | Estatística descritiva: gráficos, medidas de posição e dispersão, assimetria e curtose ⚠ complemento/lacuna | 27 | 216 |

### PCPE EST 2 — Estatística  (meta 64 · piso 41)

| Cód. | Assunto a marcar no TEC (aproximado) | Trechos | Meta |
| --- | --- | ---: | ---: |
| 2.1 | Probabilidade: definições e axiomas | 3 | 24 |
| 2.2 | Probabilidade condicional e independência | 2 | 16 |
| 3.1 | Amostragem: simples, estratificada, sistemática, conglomerados ⚠ complemento/lacuna | 0 | 12 |
| 3.2 | Tamanho amostral ⚠ complemento/lacuna | 0 | 12 |

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
| 8 | Balancete de verificação | 0 | 12 |

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
3. **Matemática × Raciocínio Lógico:** o edital do PCPE reúne os dois no bloco "Raciocínio Lógico"; análise combinatória e probabilidade ficam nos cadernos de RL (itens 7 e 13). Cada trecho do plano é contado uma só vez por disciplina (itens vizinhos que dividem os mesmos trechos aparecem com meta mínima).
4. **Importação:** `content/questoes/mapa-assuntos.json` ainda não tem as matérias do TEC de Direito Penal, Processo Penal, Contabilidade e Legislação PCPE, e o classificador só reconhece os cadernos do CBMPE/PMPE. Isso faz parte do **importador de questões por concurso** (sessão separada, ainda pendente): baixar os PDFs agora e importar depois é seguro.
