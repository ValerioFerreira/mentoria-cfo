# Auditoria e Correção de Rótulos da Diretriz (PCPE Agente)

## Contexto
A diretriz orienta o aluno indicando: *“comece na pág. X, no tópico ‘T’”*.
Na medição inicial de 2026-10-20 via `pipeline/pcpe_tools/audit_planos.py`, **43 trechos** apresentavam tópicos cujo texto não constava nas duas primeiras páginas do trecho no PDF (além do caso notório de `informatica/a04/s03`, com rótulo truncado *“IREWALL”*).

## Metodologia de Correção e Invariante
- Todas as correções foram feitas **exclusivamente via `content/overrides/<disciplina>.json`** (`headings` e `dropHeadings`).
- **Invariante rigorosamente preservada:** Nenhum ID de trecho, nem `startPage` e `endPage` foram alterados. O script `scratch/check_segments_invariant.py` comparou todos os 1.147 trechos antes e depois da regeneração (`segment.py`, `build_catalog.py`, `build_complements.py --no-pdf`, `edital_map.py`) e atestou 100% de integridade estrutural.

---

## Relação de Trechos Corrigidos por Disciplina

### contabilidade-geral

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `contabilidade-geral/a00` | 3 | Conceito, Objeto, Finalidade e Funções da Contabilidade | **Apresentação do Curso e Metodologia de Contabilidade** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a03` | 31 | Retificação de Lançamentos: Estorno e Transferência | **Tipos de Fatos Contábeis e Atos Administrativos** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a06` | 30 | Classificação do Ativo Circulante e Não Circulante | **Perdas estimadas com créditos de liquidação duvidosa (PECLD)** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a08` | 19 | Depreciação: Métodos de Cálculo, Taxas e Baixa de Bens | **Critério de avaliação do ativo imobilizado e custo atribuído** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a10` | 12 | Fases de Pesquisa e Desenvolvimento e Amortização de Intangíveis | **Investimentos: mais-valia e goodwill** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a13` | 19 | Variação Cambial, Debêntures e Depósitos Judiciais | **Debêntures: conceito, características básicas e aspectos contábeis** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a17` | 12 | Princípios da Oportunidade, Registro pelo Valor Original e Prudência | **Critérios de avaliação de ativos e passivos: valor realizável** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a19` | 18 | Políticas Contábeis, Continuidade e Distinção Circulante/Não Circulante | **Demonstrações contábeis: considerações gerais, estrutura e conteúdo** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a19` | 33 | Estrutura do Balanço e Demonstração do Resultado Abrangente (DRA) | **Passivo circulante e não circulante no balanço patrimonial** | Ajuste para coincidir com o texto real do PDF |
| `contabilidade-geral/a19` | 46 | Notas Explicativas e Divulgações Obrigatórias | **Demonstração do resultado do período e formas de apresentação das despesas** | Ajuste para coincidir com o texto real do PDF |

### direito-administrativo

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `direito-administrativo/a20` | 103 | Regras Gerais de Julgamento e Jurisprudência | **Julgamento por melhor técnica ou técnica e preço: quesitos técnicos** | Ajuste para coincidir com o texto real do PDF |
| `direito-administrativo/a21` | 100 | Homologação, Adjudicação e Encerramento | **Propostas inexequíveis e critérios de desempate e preferência** | Ajuste para coincidir com o texto real do PDF |
| `direito-administrativo/a21` | 145 | Disposições Setoriais e Jurisprudência Relevante | **Termo de referência e projeto básico na licitação** | Ajuste para coincidir com o texto real do PDF |
| `direito-administrativo/a22` | 16 | Formalização e Principais Contratos Administrativos | **Serviços contínuos e contratos de fornecimento** | Ajuste para coincidir com o texto real do PDF |
| `direito-administrativo/a22` | 160 | Procedimento Sancionatório e Irregularidades | **Procedimento de apuração e aplicação de sanções** | Ajuste para coincidir com o texto real do PDF |
| `direito-administrativo/a22` | 175 | Impugnações, Controle das Contratações e Portal Nacional | **Do recurso e pedido de reconsideração** | Ajuste para coincidir com o texto real do PDF |

### direito-constitucional

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `direito-constitucional/a03` | 24 | Penas, presos e extradição (art. 5º, XLV a LII) | **Crimes inafiançáveis e individualização da pena (art. 5º, XLIII a XLVI)** | Ajuste para coincidir com o texto real do PDF |

### direito-penal

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `direito-penal/a00` | 30 | Fontes, Tribunal do Júri e Menoridade | **Súmulas pertinentes do STJ sobre Direito Penal** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a01` | 33 | Aplicação Pessoal, Sentença Estrangeira e Conflito Aparente | **Aplicação da Lei penal em relação às pessoas: Sujeito ativo e passivo** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a02` | 19 | Tipicidade e Classificação dos Crimes | **Tipicidade penal: tipicidade formal, material e conglobante** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a04` | 22 | Feminicídio, Vicaricídio e Majorantes | **Homicídio qualificado-privilegiado e majorantes** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a04` | 37 | Induzimento ao Suicídio, Infanticídio e Aborto | **Art. 121-B, vicaricídio e induzimento ao suicídio** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a05` | 139 | Receptação e Escusas Absolutórias | **Da receptação: aspectos gerais e tipo penal** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a06` | 35 | Crimes Sexuais contra Vulneráveis e Divulgação Ilícita | **Favorecimento da prostituição de vulnerável (art. 218-B)** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a07` | 21 | Corrupção Passiva, Prevaricação e Violação de Sigilo Funcional | **Facilitação de contrabando ou descaminho e prevaricação** | Ajuste para coincidir com o texto real do PDF |
| `direito-penal/a09` | 18 | Falso Testemunho, Perícia e Coação no Curso do Processo | **Comunicação falsa de crime e autoacusação** | Ajuste para coincidir com o texto real do PDF |

### direito-processual-penal

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `direito-processual-penal/a00` | 8 | Princípios Processuais Penais Fundamentais | **Princípio do devido processo legal, contraditório e ampla defesa** | Ajuste para coincidir com o texto real do PDF |
| `direito-processual-penal/a01` | 46 | Investigação Criminal (Lei nº 12.830/2013) e Jurisprudência | **Disposições legais do CPP sobre o Inquérito Policial** | Ajuste para coincidir com o texto real do PDF |
| `direito-processual-penal/a03` | 45 | Declarações do Ofendido | **Da confissão: conceito, requisitos e aspectos gerais** | Ajuste para coincidir com o texto real do PDF |
| `direito-processual-penal/a06` | 2 | JECRIM: Princípios, Competência e Atos Processuais | **Juizados Especiais Criminais: Considerações gerais e rito sumaríssimo** | Ajuste para coincidir com o texto real do PDF |

### estatistica

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `estatistica/a01` | 3 | (sem título específico) | **Introdução às Médias e Medidas de Posição** | Inclusão de título alinhado ao PDF |

### informatica

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `informatica/a04` | 60 | (sem título específico) | **Firewall** | Inclusão de título alinhado ao PDF |

### legislacao-pcpe

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `legislacao-pcpe/a03` | 2 | Disposições Preliminares e Provimento | **Sumário e Apresentação: Lei nº 6.425/1972** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-pcpe/a03` | 10 | Da Nomeação, Posse e Exercício | **Regime jurídico e Da Nomeação** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-pcpe/a05` | 3 | Disposições Gerais, Provimento e Posse | **Apresentação do Curso: Lei Estadual nº 6.123/1968** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-pcpe/a05` | 12 | Remoção, Redistribuição e Vacância | **Da remoção, estágio probatório e promoção** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-pcpe/a07` | 3 | Deveres, Proibições e Responsabilidades | **Apresentação e Estatuto dos Servidores: Regime disciplinar** | Ajuste para coincidir com o texto real do PDF |

### legislacao-penal-especial

| Aula / Trecho | Pág. | Rótulo Anterior | Rótulo Novo | Justificativa |
|---|---|---|---|---|
| `legislacao-penal-especial/a11` | 24 | Crimes Hediondos no ECA, Pacote Anticrime e Regras Processuais | **Crimes hediondos no Estatuto da Criança e do Adolescente (ECA)** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-penal-especial/a13` | 3 | Lei nº 13.869/2019 — Disposições Gerais, Sujeitos e Efeitos da Condenação | **Lei nº 13.869/2019: Crimes de abuso de autoridade** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-penal-especial/a18` | 35 | Tráfico Ilícito de Drogas e Tipos Equiparados (arts. 33 a 37) | **Do tráfico privilegiado de drogas** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-penal-especial/a20` | 38 | Crimes de Poluição, Ordenamento Urbano e Administração Ambiental | **Crimes contra a flora em florestas de preservação permanente** | Ajuste para coincidir com o texto real do PDF |
| `legislacao-penal-especial/a21` | 15 | Regras Gerais e Competências | **Porte de arma de fogo: agentes e guardas prisionais** | Ajuste para coincidir com o texto real do PDF |

---

## Trechos Mantidos e Justificativa

Os 3 casos residuais apontados por `audit_planos.py` pertencem a `raciocinio-logico`:

| Trecho | Rótulo Atual | Pág. Inicial | Motivo da Manutenção |
|---|---|---|---|
| `raciocinio-logico/a00/s01` | Proposição lógica | 1 | Mantido porque a inclusão de heading na pág. 1 em `segment.py` recalcula a partição automática dos trechos da aula, violando a invariante de `{id, startPage, endPage}` (que sustentam resumos e bizus). O conteúdo trata de introdução e conceitos fundamentais de proposições. |
| `raciocinio-logico/a01/s01` | Introdução | 1 | Mantido pelo mesmo motivo de integridade estrutural e preservação dos IDs de segmentos. O tópico cobre a introdução teórica do PDF. |
| `raciocinio-logico/a03/s01` | Introdução | 1 | Mantido pelo mesmo motivo de integridade estrutural e preservação dos IDs de segmentos. |

---
**Total de intervenções:** 42 rótulos corrigidos/adicionados via overrides.