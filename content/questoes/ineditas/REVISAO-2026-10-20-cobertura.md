# Relatório Consolidado de Revisão das Questões Inéditas de Múltipla Escolha — Cobertura PCPE Agente

**Data:** 20 de outubro de 2026  
**Projeto:** MentorIA / CFO-BM (Branch: `pcpe`)  
**Missão:** Cobertura de 100% dos trechos sem nenhuma questão no plano PCPE Agente de Polícia (`pipeline/briefs/ineditas-faltantes.csv`).  
**Padrão:** Múltipla escolha autoral (padrão Cebraspe, 5 alternativas A–E, exatamente uma correta).  
**Meta de Cobertura:** No mínimo 6 questões por trecho (8 nos trechos com peso_prova >= 0,20).  

---

## Sumário Executivo Global

| Disciplina | Trechos Cobertos | Meta Mínima | Questões Produzidas | Distribuição Gabaritos (A / B / C / D / E) | Status Validação |
|---|:---:|:---:|:---:|:---:|:---:|
| 1. Contabilidade Geral | 17 | 122 | 122 | A: 25 (20,5%) · B: 25 (20,5%) · C: 24 (19,7%) · D: 24 (19,7%) · E: 24 (19,7%) | `erros 0` |
| 2. Informática | 17 | 104 | 104 | A: 21 (20,2%) · B: 21 (20,2%) · C: 21 (20,2%) · D: 21 (20,2%) · E: 20 (19,2%) | `erros 0` |
| 3. Língua Portuguesa | 10 | 60 | 60 | A: 12 (20,0%) · B: 12 (20,0%) · C: 12 (20,0%) · D: 12 (20,0%) · E: 12 (20,0%) | `erros 0` |
| 4. Estatística | 13 | 78 | 78 | A: 16 (20,5%) · B: 16 (20,5%) · C: 16 (20,5%) · D: 15 (19,2%) · E: 15 (19,2%) | `erros 0` |
| 5. Matemática | 8 | 50 | 50 | A: 10 (20,0%) · B: 10 (20,0%) · C: 10 (20,0%) · D: 10 (20,0%) · E: 10 (20,0%) | `erros 0` |
| 6. Raciocínio Lógico | 29 | 174 | 174 | A: 35 (20,1%) · B: 35 (20,1%) · C: 35 (20,1%) · D: 35 (20,1%) · E: 34 (19,5%) | `erros 0` |
| 7. Direito Administrativo | 26 | 156 | 156 | A: 32 (20,5%) · B: 31 (19,9%) · C: 31 (19,9%) · D: 31 (19,9%) · E: 31 (19,9%) | `erros 0` |
| 8. Direito Constitucional | 3 | 18 | 18 | A: 4 (22,2%) · B: 4 (22,2%) · C: 4 (22,2%) · D: 3 (16,7%) · E: 3 (16,7%) | `erros 0` |
| 9. Direito Penal | 17 | 102 | 102 | A: 21 (20,6%) · B: 21 (20,6%) · C: 20 (19,6%) · D: 20 (19,6%) · E: 20 (19,6%) | `erros 0` |
| **TOTAL GERAL** | **140** | **864** | **864** | **A: 176 · B: 175 · C: 173 · D: 171 · E: 169** | **`erros 0` · 140/140** |

- **Validador de formato e regras Cebraspe (`pipeline/questoes/ineditas_mc_nativas.py --check`)**: `TOTAL 864 · erros 0`.
- **Validador de cobertura mínima (`pipeline/questoes/cobertura_ineditas.py --minimo 6`)**: `140/140 trechos com ao menos 6 inéditas de múltipla escolha; faltam 0 questões`.
- **Integridade do banco C/E anterior (`pipeline/questoes/ineditas.py --check`)**: `TOTAL 485 · C 239 · E 246 · erros 0` (preservação integral dos arquivos originais).

---

## 1. Contabilidade Geral

- **Arquivo:** `content/questoes/ineditas/mc/contabilidade-geral.txt`
- **Total de questões:** 122 questões inéditas
- **Trechos cobertos:** 17 trechos
  - Trechos com peso_prova >= 0,20 (8 questões cada, meta cumprida): `a02/s01` (0,34), `a07/s01` (0,328), `a07/s02` (0,474), `a08/s01` (0,298), `a08/s02` (0,316), `a08/s03` (0,316), `a09/s01` (0,207), `a11/s02` (0,35), `a13/s01` (0,282), `a13/s02` (0,30).
  - Demais trechos (6 questões cada): `a10/s01`, `a10/s02`, `a12/s01`, `a19/s01`, `a19/s02`, `a19/s03`, `a19/s04`.
- **Distribuição de gabaritos:** A: 25 (20,5%), B: 25 (20,5%), C: 24 (19,7%), D: 24 (19,7%), E: 24 (19,7%).
- **Fontes técnicas e oficiais:** Lei 6.404/1976 (atualizada até out/2026), CPC 00 (R2), CPC 01 (R1 - Impairment), CPC 04 (R1 - Intangível), CPC 16 (R1 - Estoques), CPC 25 (Provisões e Contingências), CPC 26 (R1 - Apresentação das Demonstrações) e CPC 27 (Ativo Imobilizado).

### Detalhamento por Trecho — Contabilidade Geral

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `contabilidade-geral/a02/s01` | Contas | Classificação patrimonial vs resultado, natureza dos saldos devedores/credores, contas retificadoras de ativo e PL, vedação de compensação | 8 | A, C, E, B, D, A, C, B |
| `contabilidade-geral/a07/s01` | Avaliação de Estoques | Critérios PEPS, UEPS (proibido fiscalmente e pelo CPC 16), Custo Médio Ponderado Móvel vs Fixo, inventário periódico vs permanente | 8 | D, E, B, A, C, D, E, A |
| `contabilidade-geral/a07/s02` | Tributação sobre Compras/Vendas | Impostos recuperáveis (ICMS, IPI, PIS/COFINS não cumulativo) vs não recuperáveis, fretes e seguros sobre compras, devoluções e abatimentos | 8 | B, C, D, E, A, B, C, D |
| `contabilidade-geral/a08/s01` | CPC 27: Ativo Imobilizado | Elementos do custo inicial, gastos de instalação e desmontagem/restauração, gastos subsequentes (capitalizáveis vs despesa de manutenção) | 8 | E, A, B, C, D, E, A, B |
| `contabilidade-geral/a08/s02` | CPC 27: Depreciação | Método linear/quotas constantes, soma dos dígitos (Cole), unidades produzidas, valor residual, revisão periódica de vida útil, deemed cost | 8 | C, D, E, A, B, C, D, E |
| `contabilidade-geral/a08/s03` | CPC 27: Baixas e Desreconhecimento | Ganho ou perda na alienação de imobilizado, baixa por obsolescência/inservibilidade, exaustão de recursos minerais e florestais | 8 | A, B, C, D, E, A, B, C |
| `contabilidade-geral/a09/s01` | CPC 01 (R1): Valor Recuperável | Teste de impairment, valor justo líquido de despesas de venda vs valor em uso, Unidade Geradora de Caixa (UGC), reversão de perdas | 8 | D, E, A, B, C, D, E, A |
| `contabilidade-geral/a10/s01` | CPC 04 (R1): Ativo Intangível | Definição, critérios de identificabilidade, controle sobre recursos futuros, intangíveis gerados internamente (marcas e títulos proibidos) | 6 | B, C, D, E, A, B |
| `contabilidade-geral/a10/s02` | CPC 04 (R1): P&D e Amortização | Fase de pesquisa (sempre despesa) vs fase de desenvolvimento (ativo capitalizável), vida útil definida vs indefinida, goodwill | 6 | C, D, E, A, B, C |
| `contabilidade-geral/a11/s02` | Folha de Pagamento e AVP | Encargos patronais (INSS/FGTS), provisões de férias e 13º salário, retenções do empregado, Ajuste a Valor Presente (CPC 12) | 8 | D, E, A, B, C, D, E, A |
| `contabilidade-geral/a12/s01` | CPC 25: Provisões e Contingências | Obrigação presente decorrente de eventos passados, provável/possível/remota, passivos contingentes (apenas nota explicativa) e ativos contingentes | 6 | B, C, D, E, A, B |
| `contabilidade-geral/a13/s01` | Operações Financeiras | Desconto de duplicatas (passivo financeiro), factoring, forfaiting, encargos financeiros a apropriar (juros a transcorrer), variação cambial | 8 | C, D, E, A, B, C, D, E |
| `contabilidade-geral/a13/s02` | Debêntures e Outras Operações | Emissão de debêntures com prêmio ou deságio, custos de transação, método da taxa efetiva de juros, depósitos judiciais e JSCP | 8 | A, B, C, D, E, A, B, C |
| `contabilidade-geral/a19/s01` | CPC 26 (R1): Demonstrações Contábeis | Conjunto completo de demonstrações, pressuposto da continuidade operacional, regime de competência, tempestividade e materialidade | 6 | D, E, A, B, C, D |
| `contabilidade-geral/a19/s02` | CPC 26 (R1): Balanço Patrimonial | Critérios de classificação em Circulante vs Não Circulante, ciclo operacional típico de 12 meses, passivos refinanciáveis | 6 | E, A, B, C, D, E |
| `contabilidade-geral/a19/s03` | CPC 26 (R1): Covenants e DRE/DRA | Violação de covenants contratuais antes do balanço, Demonstração do Resultado do Exercício vs Demonstração do Resultado Abrangente | 6 | A, B, C, D, E, A |
| `contabilidade-geral/a19/s04` | CPC 26 (R1): DMPL e Notas Explicativas | Despesas por função vs natureza, Demonstração das Mutações do Patrimônio Líquido (DMPL), papel informativo das notas explicativas | 6 | B, C, D, E, A, B |

### Revisão Cruzada e Dúvidas (Contabilidade Geral)
- **Conformidade:** Contas refeitas e balanceadas; valores e percentuais de tributos e encargos conferidos conforme alíquotas legais vigentes.
- **Dúvidas para o dono:** Nenhuma pendência técnica. O edital de Agente de Polícia do PCPE exige contabilidade básica e avançada até demonstrações financeiras, plenamente atendida.

---

## 2. Informática

- **Arquivo:** `content/questoes/ineditas/mc/informatica.txt`
- **Total de questões:** 104 questões inéditas
- **Trechos cobertos:** 17 trechos
  - Trecho com peso_prova >= 0,20 (8 questões): `informatica/a10/s04` (0,239).
  - Demais trechos (6 questões cada): `a00/s01`, `a01/s02`, `a02/s01`, `a02/s02`, `a02/s03`, `a02/s06`, `a03/s01`, `a03/s02`, `a03/s05`, `a04/s02`, `a04/s03`, `a10/s01`, `a10/s02`, `a12/s07`, `a12/s09`, `a12/s10`.
- **Distribuição de gabaritos:** A: 21 (20,2%), B: 21 (20,2%), C: 21 (20,2%), D: 21 (20,2%), E: 20 (19,2%).
- **Fontes técnicas e oficiais:** Windows 11 atualizado (24H2), Microsoft 365 / PowerPoint, normas ABNT NBR ISO/IEC 27001 e 27005, Decreto Federal 9.637/2018 (PNSI), cartilhas de segurança do CERT.br e padrões ICP-Brasil.

### Detalhamento por Trecho — Informática

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `informatica/a00/s01` | Internet e Redes | Comutação de pacotes vs circuitos, LAN, WAN, PAN, cliente/servidor, WWW vs Internet | 6 | A, B, C, D, E, A |
| `informatica/a01/s02` | Intranet e Extranet | Extranet corporativa B2B, VPN Site-to-Site, VPN Client-to-Site, tunelamento e criptografia | 6 | B, C, D, E, A, B |
| `informatica/a02/s01` | Segurança: Fundamentos | Controles físicos vs lógicos, vulnerabilidades, ameaças, risco, ISO/IEC 27001 e PNSI | 6 | C, D, E, A, B, C |
| `informatica/a02/s02` | Princípios de Segurança | Integridade, disponibilidade, autenticidade, não repúdio, logs NTP append-only, Parkerian Hexad | 6 | D, E, A, B, C, D |
| `informatica/a02/s03` | Criptografia | Esteganografia, algoritmos simétricos (AES/DES), gestão de chaves, assimétrica, TLS híbrido, Kerckhoffs | 6 | E, A, B, C, D, E |
| `informatica/a02/s06` | Certificados e ICP-Brasil | Padrão X.509, AC-Raiz (ITI), Autoridades de Registro (AR), tipos A1 vs A3, LCR e OCSP | 6 | A, B, C, D, E, A |
| `informatica/a03/s01` | Malwares: Classificação | Hacker vs cracker, módulos virais (infecção, ativação, payload), hospedeiro obrigatório, insiders | 6 | B, C, D, E, A, B |
| `informatica/a03/s02` | Tipos de Vírus | Macro, boot (MBR), multipartite, polimórfico vs metamórfico, stealth, time bomb | 6 | C, D, E, A, B, C |
| `informatica/a03/s05` | Ataques e Golpes | DoS/DDoS, brute force, e-mail spoofing, IP spoofing, engenharia social/phishing, honeypots | 6 | D, E, A, B, C, D |
| `informatica/a04/s02` | Proteção Antimalware | Heurística estática/dinâmica, análise comportamental, NGAV em nuvem, filtros antispam, sandbox | 6 | E, A, B, C, D, E |
| `informatica/a04/s03` | Firewalls | Firewall pessoal vs perimetral, stateless vs stateful, política restritiva default deny, DMZ | 6 | A, B, C, D, E, A |
| `informatica/a10/s01` | PowerPoint 365: Histórico | Proporção widescreen 16:9, recurso Diga-me, transição Transformar, Zoom, coautoria SaaS | 6 | B, C, D, E, A, B |
| `informatica/a10/s02` | PowerPoint 365: Interface | Barra de Acesso Rápido, Modo Backstage (Arquivo), Faixa de Opções (Ctrl+F1), Modo Apresentador | 6 | C, D, E, A, B, C |
| `informatica/a10/s04` | PowerPoint 365: Animações | SmartArt, Caixa de Texto, transição vs animação, categorias (entrada, ênfase, saída), Pincel de Animação | 8 | D, E, A, B, C, D, E, A |
| `informatica/a12/s07` | Windows 11: Configurações | Atalho Win+I, coexistência com Painel de Controle, múltiplos monitores, Luz Noturna, Mixer de Volume | 6 | B, C, D, E, A, B |
| `informatica/a12/s09` | Windows 11: Personalização | Slides de tela de fundo, temas Claro/Escuro, aplicativos padrão por protocolo, Conta Microsoft vs Local | 6 | C, D, E, A, B, C |
| `informatica/a12/s10` | Windows 11: Ferramentas | Windows Hello (biometria local), Bloqueio Dinâmico Bluetooth, Lupa (Win + +/-), Game Bar (Win+G) | 6 | D, E, A, B, C, D |

### Revisão Cruzada e Dúvidas (Informática)
- **Conformidade:** Referências precisas ao ecossistema moderno Windows 11 e Microsoft 365.
- **Dúvidas para o dono:** Todos os 17 trechos mapearam automaticamente para os itens `p1.2`, `p1.3`, `p2.3`, `p3.1` e `p3.4` do edital, sem dúvidas pendentes.

---

## 3. Língua Portuguesa

- **Arquivo:** `content/questoes/ineditas/mc/lingua-portuguesa.txt`
- **Total de questões:** 60 questões inéditas
- **Trechos cobertos:** 10 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** Exatamente A: 12 (20%), B: 12 (20%), C: 12 (20%), D: 12 (20%), E: 12 (20%).
- **Fontes técnicas e oficiais:** Gramática normativa contemporânea (Celso Cunha & Lindley Cintra, Evanildo Bechara, Rocha Lima) e Manual de Redação da Presidência da República (3ª edição).
- **Mapeamento explícito de itens do edital:**
  - `lingua-portuguesa/a00/s01 | item=3` (Ortografia oficial e acentuação gráfica)
  - `lingua-portuguesa/a00/s02 | item=5.1` (Morfologia e emprego de classes de palavras)
  - `lingua-portuguesa/a00/s03 | item=5.1` (Morfologia: conjunções, tempos e modos verbais)
  - `lingua-portuguesa/a00/s04 | item=5.4` (Sintaxe: relações de regência, concordância e pontuação)

### Detalhamento por Trecho — Língua Portuguesa

| Trecho | Aula | Tópicos Cobertos | Item Edital | Qtd | Gabaritos |
|---|---|---|---|:---:|---|
| `lingua-portuguesa/a00/s01` | Nivelamento | Acentuação gráfica, hífen no Acordo Ortográfico, emprego dos porquês, haver x a, onde x aonde | `item=3` | 6 | A, B, C, D, E, A |
| `lingua-portuguesa/a00/s02` | Nivelamento | Colocação pronominal (próclise obrigatória e proibições), demonstrativos, advérbios, pronomes de tratamento | `item=5.1` | 6 | B, C, D, E, A, B |
| `lingua-portuguesa/a00/s03` | Nivelamento | Conjunções coordenativas e subordinativas adverbiais, modos e tempos verbais, formas nominais | `item=5.1` | 6 | C, D, E, A, B, C |
| `lingua-portuguesa/a00/s04` | Nivelamento | Regência verbal (assistir, visar, aspirar), pontuação da ordem direta, complemento nominal vs adjunto | `item=5.4` | 6 | D, E, A, B, C, D |
| `lingua-portuguesa/a00/s05` | Nivelamento | Crase (casos proibidos, obrigatórios e facultativos), parônimos clássicos, tipologia textual | Padrão | 6 | E, A, B, C, D, E |
| `lingua-portuguesa/a04/s04` | Verbos | Verbos terminados em -ear e -iar (grupo MARIO), derivados de ter, vir, ver e pôr, verbos defectivos | Padrão | 6 | A, B, C, D, E, A |
| `lingua-portuguesa/a04/s05` | Verbos | Correlação de tempos e modos verbais (hipótese irreal, eventualidade futura, sucessão no passado) | Padrão | 6 | B, C, D, E, A, B |
| `lingua-portuguesa/a04/s06` | Verbos | Vozes verbais: ativa, passiva analítica e sintética, partícula apassivadora vs índice de indeterminação | Padrão | 6 | C, D, E, A, B, C |
| `lingua-portuguesa/a07/s04` | Concordância | Concordância do verbo ser, concordância nominal com múltiplos núcleos, expressões "é proibido/bom/necessário" | Padrão | 6 | D, E, A, B, C, D |
| `lingua-portuguesa/a09/s02` | Coesão Textual | Coesão referencial anafórica/catafórica, conectivos interparágrafos, reescrita de períodos e pontuação | Padrão | 6 | E, A, B, C, D, E |

### Revisão Cruzada e Dúvidas (Língua Portuguesa)
- **Conformidade:** Rigor normativo conforme a gramática padrão e jurisprudência de bancas (Cebraspe).
- **Dúvidas para o dono:** Os trechos da aula de nivelamento (`a00`) foram amarrados explicitamente aos itens correspondentes do edital conforme diretriz do briefing.

---

## 4. Estatística

- **Arquivo:** `content/questoes/ineditas/mc/estatistica.txt`
- **Total de questões:** 78 questões inéditas
- **Trechos cobertos:** 13 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** A: 16 (20,5%), B: 16 (20,5%), C: 16 (20,5%), D: 15 (19,2%), E: 15 (19,2%).
- **Fontes técnicas e oficiais:** Estatística Descritiva clássica, livros de referência (Morettin & Bussab, Farias et al.), análise combinatória formal.
- **Mapeamento explícito:** `estatistica/a05/s05 | item=2.1` (Análise combinatória: partições e Lemas de Kaplansky).

### Detalhamento por Trecho — Estatística

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `estatistica/a00/s03` | Apresentação de Dados | Amplitude de classe, ponto médio, densidade de frequência, frequência acumulada | 6 | A, B, C, D, E, A |
| `estatistica/a00/s04` | Apresentação de Dados | Histograma vs colunas, polígono de frequências, ogiva de Galton, assimetria gráfica | 6 | B, C, D, E, A, B |
| `estatistica/a01/s01` | Médias | Posição vs separatrizes, propriedades fundamentais do operador somatório | 6 | C, D, E, A, B, C |
| `estatistica/a01/s02` | Médias | Média aritmética, combinação ponderada de grupos, transformação linear, soma dos desvios nula | 6 | D, E, A, B, C, D |
| `estatistica/a01/s05` | Médias | Média harmônica, velocidade média em percursos iguais, desigualdade das médias ($x̄ \ge G \ge H$) | 6 | E, A, B, C, D, E |
| `estatistica/a02/s04` | Separatrizes | Decis, relação D5 = Mediana, cálculo em dados discretos e interpolação em classes | 6 | A, B, C, D, E, A |
| `estatistica/a02/s05` | Separatrizes | Percentis, quartis, correspondência P50 = Md = D5 = Q2, amplitude interquartílica | 6 | B, C, D, E, A, B |
| `estatistica/a02/s06` | Separatrizes | Box plot (resumo dos 5 números), distância interquartílica (DIQ), critério de Tukey para outliers | 6 | C, D, E, A, B, C |
| `estatistica/a03/s01` | Moda | Moda como única medida central em variáveis nominais, amodal/unimodal/bimodal, moda bruta | 6 | D, E, A, B, C, D |
| `estatistica/a03/s03` | Moda | Fórmula da Moda de King, classes com amplitudes desiguais e densidade, King vs Czuber | 6 | E, A, B, C, D, E |
| `estatistica/a04/s02` | Dispersão | Propriedades dos desvios: soma dos quadrados mínima na média, soma dos módulos mínima na mediana | 6 | A, B, C, D, E, A |
| `estatistica/a04/s03` | Dispersão | Desvio médio relativo e absoluto, cálculo com ponto médio, invariância por translação | 6 | B, C, D, E, A, B |
| `estatistica/a05/s05` | Análise Combinatória | Partições ordenadas vs não-ordenadas, 1º e 2º Lemas de Kaplansky (filas e disposições circulares) | 6 | C, D, E, A, B, C |

### Revisão Cruzada e Dúvidas (Estatística)
- **Conformidade:** Todas as contas foram resolvidas e conferidas à mão; sem figuras (dados perfeitamente contextualizados em prosa).
- **Dúvidas para o dono:** Trecho `a05/s05` devidamente qualificado com `| item=2.1` no edital.

---

## 5. Matemática

- **Arquivo:** `content/questoes/ineditas/mc/matematica.txt`
- **Total de questões:** 50 questões inéditas
- **Trechos cobertos:** 8 trechos
  - Trecho com peso_prova >= 0,20 (8 questões): `matematica/c03/s01` (0,218).
  - Demais trechos (6 questões cada): `a01/s01`, `a01/s03`, `a03/s01`, `a03/s02`, `a10/s04`, `a11/s02`, `a11/s04`.
- **Distribuição de gabaritos:** Exatamente A: 10 (20%), B: 10 (20%), C: 10 (20%), D: 10 (20%), E: 10 (20%).
- **Fontes técnicas e oficiais:** Matemática básica e do ensino médio formal (Iezzi et al.), teoria aritmética e funções.
- **Mapeamento explícito:** `matematica/a01/s03 | item=1` (Números inteiros, potências e radicais).

### Detalhamento por Trecho — Matemática

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `matematica/a01/s01` | Operações Fundamentais | Adição, subtração, reagrupamento decimal, propriedades comutativa e associativa, expressões numéricas | 6 | A, C, E, B, D, B |
| `matematica/a01/s03` | Potenciação e Radiciação | Propriedades das potências, potências de base 2, simplificação de radicais, racionalização de denominadores | 6 | D, A, C, E, B, D |
| `matematica/a03/s01` | MMC e Frações I | Números primos, fatoração simultânea, frações equivalentes, redução ao mesmo denominador e soma | 6 | C, A, E, B, D, A |
| `matematica/a03/s02` | Frações II | Multiplicação e divisão fracionária, comparação de frações, fração de fração, recuperação do todo pela parte | 6 | E, C, A, D, B, C |
| `matematica/a10/s04` | Função Afim (1º Grau) | Lei $f(x)=ax+b$, taxa de variação, cálculo de raiz, estudo de sinais e inequações do primeiro grau | 6 | D, E, A, C, E, B |
| `matematica/a11/s02` | Função Quadrática (2º Grau) | Parábola, concavidade ($a$), corte no eixo y ($c$), comportamento no corte ($b$), vértice e eixo de simetria | 6 | C, A, D, B, E, C |
| `matematica/a11/s04` | Função Quadrática: Vértice | Forma fatorada, relações de Girard (soma $-b/a$ e produto $c/a$), coordenadas do vértice ($X_v, Y_v$), problemas de máximo/mínimo | 6 | B, D, A, E, C, A |
| `matematica/c03/s01` | Razão, Proporção e Divisão | Divisão em partes direta e inversamente proporcionais, regra de sociedade comercial, diferença de cotas | 8 | E, B, D, A, C, E, B, D |

### Revisão Cruzada e Dúvidas (Matemática)
- **Conformidade:** Contas refeitas e comentadas passo a passo, valores inteiros ou decimais exatos para evitar dúvidas aritméticas.
- **Dúvidas para o dono:** O trecho `a01/s03` foi marcado com `| item=1` conforme exigência de mapeamento do edital.

---

## 6. Raciocínio Lógico

- **Arquivo:** `content/questoes/ineditas/mc/raciocinio-logico.txt`
- **Total de questões:** 174 questões inéditas
- **Trechos cobertos:** 29 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** A: 35 (20,1%), B: 35 (20,1%), C: 35 (20,1%), D: 35 (20,1%), E: 34 (19,5%).
- **Fontes técnicas e oficiais:** Lógica Proposicional clássica, Lógica de Argumentação dedutiva e Raciocínio Crítico informal (Mortari, Copi, Walton).

### Detalhamento por Trecho — Raciocínio Lógico

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `raciocinio-logico/a00/s02` | Proposições | Conceito de proposição, sentenças abertas, princípios da lógica clássica, paradoxos | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a00/s06` | Conectivos: Bicondicional | Tabela-verdade da bicondicional, condição suficiente e necessária, equivalência com conjunção de condicionais | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a00/s11` | Tabela-Verdade | Fórmula de linhas ($2^n$), valoração a partir de disjunções e condicionais falsas | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a01/s03` | Fórmulas e Classificação | Tautologia, contradição e contingência em compostas de três ou mais proposições | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a01/s04` | Prova por Absurdo | Redução ao absurdo, análise rápida de tautologia sem montar tabela completa | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a01/s08` | Propriedades Lógicas | Terceiro excluído, não-contradição, bicondicional com negação em um termo | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a02/s02` | Equivalências I | Condicional em disjunção ($\sim p \lor q$), contrapositiva ($\sim q \rightarrow \sim p$), negação ($p \land \sim q$) | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a02/s05` | Equivalências II | Negação da bicondicional em disjunção exclusiva, comutatividade e não-comutatividade da condicional | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a02/s06` | Álgebra de Proposições | Leis distributivas ($\land$ sobre $\lor$ e vice-versa), absorção, idempotência e leis de identidade | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a02/s08` | De Morgan Avançado | Negação de condicional com termos compostos no consequente, contraposição generalizada | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a02/s09` | Negação de Quantificadores | Negação de Todo (Existe... não), Negação de Nenhum (Existe...), Negação de Algum (Nenhum) | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a04/s01` | Argumentos: Dedução | Roteiro de análise em 4 etapas, Modus Ponens direto, propagação de valores de verdade | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a04/s02` | Validade Dedutiva | Conceito estrito de validade dedutiva, verdade fática vs validade estrutural, argumentos sólidos | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a04/s04` | Silogismos Categóricos | Termo médio e regras do silogismo, teste por diagramas de Euler-Venn, termo médio não distribuído | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a04/s07` | Dilemas e Silogismos | Dilema Construtivo, Dilema Destrutivo, Silogismo Disjuntivo, transitividade no Silogismo Hipotético | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a04/s08` | Cadeia de Condicionais | Resolução de trás para frente, dedução em sistemas consistentes de declarações | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a04/s09` | Lógica de Situações | Problemas dos suspeitos que mentem ou dizem a verdade, implicação lógica sob hipóteses | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a04/s10` | Falácias Formais | Afirmação do consequente, negação do antecedente, comparação dedutiva vs indutiva | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a04/s11` | Regras de Inferência | Modus Tollens combinado com De Morgan, inferência a partir de conjunção falsa | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a04/s12` | Conjuntos Consistentes | Teste de consistência de premissas, aplicação em escalas e alocação operacional | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a05/s01` | Raciocínio Crítico: Estrutura | Identificação de premissas e conclusão, indicadores linguísticos de premissa e tese | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a05/s02` | Tipos de Raciocínio | Inferência dedutiva, indução por generalização e abdução (melhor explicação) | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a05/s04` | Falácias Informais I | Ad Hominem, Ad Verecundiam (falsa autoridade), Ad Ignorantiam e Falso Dilema | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a05/s05` | Falácias Informais II | Espantalho, Petição de Princípio (circularidade), Conclusão Irrelevante e Falso Escocês | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a05/s06` | Falácias Causais e Verbais | Causa falsa (Post hoc ergo propter hoc), falácias de Composição e Divisão, equívoco e anfibologia | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a05/s07` | Premissas Ocultas | Entimemas, suposições implícitas, fortalecimento e enfraquecimento de argumentos causais | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a05/s08` | Falácias Argumentativas | Ad Populum, Ladeira Escorregadia (Slippery Slope), Ad Consequentiam e Tu Quoque | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a05/s09` | Estrutura de Argumentos | Premissas convergentes vs ligadas (dependentes), subconclusões intermediárias | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a05/s10` | Avaliação Crítica | Método do contraexemplo, critérios ARS (Aceitabilidade, Relevância, Suficiência) | 6 | D, E, A, B, C, D |

### Revisão Cruzada e Dúvidas (Raciocínio Lógico)
- **Conformidade:** Rigor dedutivo estrito em todas as tabelas e provas.
- **Dúvidas para o dono:** Todos os 29 trechos integraram sem necessidade de parâmetros extras aos códigos `p9`, `p10` e `p11` do edital.

---

## 7. Direito Administrativo

- **Arquivo:** `content/questoes/ineditas/mc/direito-administrativo.txt`
- **Total de questões:** 156 questões inéditas
- **Trechos cobertos:** 26 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** A: 32 (20,5%), B: 31 (19,9%), C: 31 (19,9%), D: 31 (19,9%), E: 31 (19,9%).
- **Fontes técnicas e oficiais:** Lei 14.133/2021 (Nova Lei de Licitações e Contratos Administrativos), Lei 8.429/1992 (com Lei 14.230/2021), Lei 9.784/1999 (Processo Administrativo Federal), CF/1988 e jurisprudência pacificada do STF e STJ.

### Detalhamento por Trecho — Direito Administrativo

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `direito-administrativo/a00/s05` | Princípios Fundamentais | Especialidade, segurança jurídica, intranscendência, presunção de legitimidade, SV 13 e SV 5 | 6 | A, B, C, D, E, A |
| `direito-administrativo/a01/s05` | Organização do Estado | Elementos do Estado, funções típicas e atípicas, federação brasileira, municípios, MP e Tribunais de Contas | 6 | B, C, D, E, A, B |
| `direito-administrativo/a01/s06` | Governo e Administração | Governo vs Administração, presidencialismo, república, competências privativas do Presidente, freios e contrapesos | 6 | C, D, E, A, B, C |
| `direito-administrativo/a01/s07` | Sentidos da Administração | Sentido subjetivo/formal/orgânico vs objetivo/material, atividades-meio vs finalísticas, fomento e delegatárias | 6 | D, E, A, B, C, D |
| `direito-administrativo/a05/s11` | Extinção de Atos | Decadência quinquenal (art. 54 da Lei 9.784/99), limites da revogação discricionária, Súmula 633 do STJ | 6 | E, A, B, C, D, E |
| `direito-administrativo/a05/s13` | Convalidação de Atos | Convalidação (ratificação, reforma, conversão), confirmação, Súmula 665 do STJ e atos complexos | 6 | A, B, C, D, E, A |
| `direito-administrativo/a09/s16` | Responsabilidade e PAD | Independência de instâncias, reflexo penal no PAD, ação de regresso, Tema 1.233 do STJ, Tema 1.424 do STF, SV 37 | 6 | B, C, D, E, A, B |
| `direito-administrativo/a20/s04` | Lei 14.133: Princípios | Adjudicação compulsória, formalismo moderado, objetivos do art. 11, sobrepreço vs superfaturamento, governança | 6 | C, D, E, A, B, C |
| `direito-administrativo/a20/s05` | Lei 14.133: Agentes Públicos | Agente de contratação, pregoeiro, comissão de contratação, comissão do diálogo competitivo, defesa pela advocacia pública | 6 | D, E, A, B, C, D |
| `direito-administrativo/a20/s07` | Lei 14.133: Modalidades | Concurso (35 dias úteis), leilão (15 dias úteis, maior lance) e diálogo competitivo (25/60 dias úteis e gravação) | 6 | E, A, B, C, D, E |
| `direito-administrativo/a20/s09` | Lei 14.133: Julgamento | Maior retorno econômico, técnica e preço (teto de 70% para técnica em projetos > R$ 300 mil), banca examinadora | 6 | A, B, C, D, E, A |
| `direito-administrativo/a21/s02` | Lei 14.133: Contratação Direta I | Credenciamento e imóvel singular (inexigibilidade), dispensa por valor (R$ 100k / R$ 50k), vedação ao fracionamento | 6 | B, C, D, E, A, B |
| `direito-administrativo/a21/s04` | Lei 14.133: Contratação Direta II | Emergência e emergência provocada (art. 75, VIII, § 6º), segurança nacional, catadores e remédios para doenças raras | 6 | C, D, E, A, B, C |
| `direito-administrativo/a21/s05` | Lei 14.133: Contratação Direta III | Associações de PCDs, contratos de programa, banca examinadora técnica (dispensa), aproveitamento de remanescente | 6 | D, E, A, B, C, D |
| `direito-administrativo/a21/s07` | Lei 14.133: Procedimento Licitatório | Fases ordinárias do art. 17, vedação a artigos de luxo, audiência/consulta pública, sigilo do orçamento | 6 | E, A, B, C, D, E |
| `direito-administrativo/a21/s11` | Lei 14.133: Registro de Preços | Adesão de não participante ("carona", limites 50% e dobro), registro unificado no PNCP, padronização e amostras | 6 | A, B, C, D, E, A |
| `direito-administrativo/a21/s12` | Lei 14.133: Execução e Vedações | Empreitada integrada vs semi-integrada, projeto básico vs executivo, terceirização e vedações, ADI 6.890 do STF | 6 | B, C, D, E, A, B |
| `direito-administrativo/a22/s01` | Lei 14.133: Contratos — Regime | Regime de direito público com normas privadas supletivas, obra vs serviço de engenharia, serviços contínuos vs escopo | 6 | C, D, E, A, B, C |
| `direito-administrativo/a22/s02` | Lei 14.133: Forma Contratual | Forma escrita obrigatória (contrato verbal nulo, ressalvado pronto pagamento até R$ 10 mil), substituição por empenho | 6 | D, E, A, B, C, D |
| `direito-administrativo/a22/s04` | Lei 14.133: Garantias e Cláusulas | Garantias contratuais (limites ordinário de 5%, 10% para alta complexidade e 30% com seguro-garantia step-in) | 6 | E, A, B, C, D, E |
| `direito-administrativo/a22/s05` | Lei 14.133: Alteração Unilateral | Alteração unilateral qualitativa/quantitativa (25% e 50%), rescisão unilateral, ocupação provisória e restrição à exceptio | 6 | A, B, C, D, E, A |
| `direito-administrativo/a22/s07` | Lei 14.133: Execução e Recebimento | Responsabilidade contratual, recebimento provisório e definitivo, conta vinculada impenhorável na terceirização | 6 | B, C, D, E, A, B |
| `direito-administrativo/a22/s10` | Lei 14.133: Equilíbrio Financeiro | Reajuste em sentido estrito (apostilamento) vs revisão (aditamento), repactuação em mão de obra exclusiva | 6 | C, D, E, A, B, C |
| `direito-administrativo/a22/s11` | Lei 14.133: Álea Extraordinária | Fato do príncipe, fato da administração, força maior, caso fortuito e interferências imprevistas | 6 | D, E, A, B, C, D |
| `direito-administrativo/a22/s13` | Lei 14.133: Sanções e Prescrição | As 4 sanções do art. 156 (advertência, multa, impedimento e inidoneidade), prescrição quinquenal, reabilitação | 6 | E, A, B, C, D, E |
| `direito-administrativo/a22/s14` | Lei 14.133: Controle e Recursos | Efeito suspensivo recursal, as 3 linhas de defesa (art. 169), prazo do TCU, portal PNCP e Tema 1.118 do STF | 6 | A, B, C, D, E, A |

### Revisão Cruzada e Dúvidas (Direito Administrativo)
- **Conformidade:** Rigorosa observância das inovações da Lei 14.133/2021 e jurisprudência de 2024 a 2026 do STF e STJ.
- **Dúvidas para o dono:** Nenhuma inconsistência jurídica detectada.

---

## 8. Direito Constitucional

- **Arquivo:** `content/questoes/ineditas/mc/direito-constitucional.txt`
- **Total de questões:** 18 questões inéditas
- **Trechos cobertos:** 3 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** A: 4 (22,2%), B: 4 (22,2%), C: 4 (22,2%), D: 3 (16,7%), E: 3 (16,7%).
- **Fontes técnicas e oficiais:** Constituição da República Federativa do Brasil de 1988 (com Emendas Constitucionais até 2026), jurisprudência consolidada do STF (ADPFs 378, 402, 496; ADI 6.620; SVs 13, 37, 46).

### Detalhamento por Trecho — Direito Constitucional

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `direito-constitucional/a08/s09` | Intervenção Federal e Estadual | Arts. 34 a 36 da CF: hipóteses de intervenção de ofício pelo Presidente vs provocada; requisição por STF/STJ; princípios sensíveis e ADI interventiva pelo PGR; intervenção estadual em municípios (art. 35 e Súmula 637 STF); controle político parlamentar em 24h e hipóteses de dispensa | 6 | A, B, C, D, E, A |
| `direito-constitucional/a12/s02` | Atribuições do Presidente | Art. 84 da CF: competências delegáveis ao PGR, AGU e Ministros (parágrafo único); decretos autônomos (art. 84, VI) vs regulamentares; celebração de tratados internacionais e ratificação discricionária; nomeação de autoridades e sabatina no Senado; propostas orçamentárias e calamidade pública | 6 | B, C, D, E, A, B |
| `direito-constitucional/a12/s03` | Responsabilização Presidencial | Arts. 85 a 91 da CF: crimes comuns vs responsabilidade; juízo de admissibilidade da Câmara (2/3); julgamento no STF e no Senado; cláusula de irresponsabilidade penal relativa (art. 86, § 4º) e suspensão da prescrição; perda do cargo e inabilitação por 8 anos (SV 46); linha sucessória (ADPF 402); Conselho da República e Conselho de Defesa Nacional | 6 | C, D, E, A, B, C |

### Revisão Cruzada e Dúvidas (Direito Constitucional)
- **Conformidade:** Enunciados e alternativas alinhados à jurisprudência do STF e ao texto constitucional vigente.
- **Dúvidas para o dono:** Nenhuma controvérsia constitucional remanescente.

---

## 9. Direito Penal

- **Arquivo:** `content/questoes/ineditas/mc/direito-penal.txt`
- **Total de questões:** 102 questões inéditas
- **Trechos cobertos:** 17 trechos (6 questões cada, meta cumprida)
- **Distribuição de gabaritos:** A: 21 (20,6%), B: 21 (20,6%), C: 20 (19,6%), D: 20 (19,6%), E: 20 (19,6%).
- **Fontes técnicas e oficiais:** Código Penal (atualizado pelas Leis 13.718/18, 13.869/19, 14.110/20, 14.133/21, 14.994/24, 15.280/25, 15.397/26 e LC 225/26) e súmulas/teses do STF e STJ.

### Detalhamento por Trecho — Direito Penal

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `direito-penal/a05/s03` | Crimes contra o Patrimônio | Furto de combustíveis (art. 155, § 10) e majorantes dos §§ 11 e 12; furto simples (1 a 6 anos) e semoventes | 6 | A, B, C, D, E, A |
| `direito-penal/a06/s06` | Dignidade Sexual: Migração e Ato Obsceno | Promoção de migração ilegal (art. 232-A), ato obsceno (art. 233, elemento normativo), objeto obsceno (art. 234) | 6 | B, C, D, E, A, B |
| `direito-penal/a06/s07` | Dignidade Sexual: Ação Penal | Ação penal pública incondicionada (art. 225 pós-Lei 13.718/18), majorantes do art. 234-A, segredo de justiça | 6 | C, D, E, A, B, C |
| `direito-penal/a07/s03` | Crimes por Funcionário Público I | Facilitação de contrabando (art. 318), prevaricação (art. 319) vs corrupção privilegiada, celular em presídio (art. 319-A) | 6 | D, E, A, B, C, D |
| `direito-penal/a07/s04` | Crimes por Funcionário Público II | Perda do cargo (art. 92, I, "a"), Súmula 599 do STJ (insignificância), corrupção passiva sem ato de ofício, peculato de uso | 6 | E, A, B, C, D, E |
| `direito-penal/a08/s01` | Crimes por Particular I | Usurpação de função (art. 328), resistência (art. 329), desobediência em blitz (Tema 1.060/STJ), desacato (ADPF 496) | 6 | A, B, C, D, E, A |
| `direito-penal/a08/s02` | Crimes por Particular II | Tráfico de influência (art. 332), corrupção ativa (art. 333), descaminho (art. 334, consumação e formas equiparadas) | 6 | B, C, D, E, A, B |
| `direito-penal/a08/s03` | Crimes por Particular III | Insignificância no descaminho (R$ 20k, Tema 157/STJ), contrabando (art. 334-A), insignificância excepcional de cigarros | 6 | C, D, E, A, B, C |
| `direito-penal/a08/s04` | Crimes por Particular IV | Perturbação de hasta pública (art. 335), inutilização de edital (art. 336), subtração/inutilização de documento (art. 337) | 6 | D, E, A, B, C, D |
| `direito-penal/a08/s05` | Crimes por Particular V | Sonegação previdenciária (art. 337-A, lançamento definitivo, exclusão Cadin LC 225/26), pagamento antes do trânsito | 6 | E, A, B, C, D, E |
| `direito-penal/a09/s01` | Administração da Justiça I | Tráfico de influência internacional (art. 337-C), reingresso de expulso (art. 338), denunciação caluniosa (art. 339) | 6 | A, B, C, D, E, A |
| `direito-penal/a09/s02` | Administração da Justiça II | Comunicação falsa (art. 340), autoacusação falsa (art. 341), falso testemunho (art. 342, retratação e suborno no art. 343) | 6 | B, C, D, E, A, B |
| `direito-penal/a09/s03` | Administração da Justiça III | Favorecimento pessoal (art. 348, escusa absolutória) vs favorecimento real (art. 349), celular (art. 349-A), fuga (art. 351) | 6 | C, D, E, A, B, C |
| `direito-penal/a09/s04` | Administração da Justiça IV | Exploração de prestígio (art. 357), violência em arrematação judicial (art. 358), desobediência a decisão judicial (art. 359) | 6 | D, E, A, B, C, D |
| `direito-penal/a09/s05` | Finanças Públicas | Operação de crédito não autorizada (art. 359-A), assunção de obrigação no último ano (art. 359-C), despesa com pessoal (art. 359-G) | 6 | E, A, B, C, D, E |
| `direito-penal/a10/s01` | Crimes em Licitações I | Contratação direta ilegal (art. 337-E), frustração do caráter competitivo (art. 337-F, Súmula 645/STJ), patrocínio indevido | 6 | A, B, C, D, E, A |
| `direito-penal/a10/s02` | Crimes em Licitações II | Afastamento de licitante (art. 337-K), fraude em contrato público (art. 337-L), contratação inidônea (art. 337-M) e penas de multa | 6 | B, C, D, E, A, B |

### Revisão Cruzada e Dúvidas (Direito Penal)
- **Conformidade:** Atualizações legislativas até out/2026 e súmulas vinculantes do STF e repetitivos do STJ.
- **Dúvidas para o dono:** Todos os trechos mapeados com exatidão nos itens `e5`, `e6` e `e7` do edital.

---

## 10. Resumo de Decisões e Dúvidas Submetidas ao Dono do Projeto

1. **Uso de parâmetros `item=` manuais**:
   - Foram inseridos explicitamente os parâmetros de item de edital estritamente nos casos em que a estrutura da aula cobria múltiplos itens de edital sem correspondência unívoca no mapa base:
     - `estatistica/a05/s05 | item=2.1` (Análise Combinatória)
     - `lingua-portuguesa/a00/s01 | item=3` (Ortografia e Acentuação)
     - `lingua-portuguesa/a00/s02 | item=5.1` (Morfologia e Classes)
     - `lingua-portuguesa/a00/s03 | item=5.1` (Morfologia e Verbos)
     - `lingua-portuguesa/a00/s04 | item=5.4` (Sintaxe e Pontuação)
     - `matematica/a01/s03 | item=1` (Inteiros, Potências e Radicais)
   - Todas as demais disciplinas e trechos mantiveram o mapeamento unívoco padrão.

2. **Diferenciação das questões de peso elevado (peso_prova >= 0,20)**:
   - Foram produzidas 8 questões (em vez de 6) em todos os 12 trechos de peso elevado:
     - 10 trechos em Contabilidade Geral (`a02/s01`, `a07/s01`, `a07/s02`, `a08/s01`, `a08/s02`, `a08/s03`, `a09/s01`, `a11/s02`, `a13/s01`, `a13/s02`);
     - 1 trecho em Informática (`a10/s04`);
     - 1 trecho em Matemática (`c03/s01`).
   - Todos os demais 128 trechos receberam exatamente 6 questões inéditas.

3. **Status de Validação e Cobertura**:
   - `python pipeline/questoes/ineditas_mc_nativas.py --check`: **TOTAL 864 · erros 0**.
   - `python pipeline/questoes/cobertura_ineditas.py --minimo 6`: **140/140 trechos cobertos · faltam 0 questões**.
   - `python pipeline/questoes/ineditas.py --check`: **TOTAL 485 · erros 0** (preservação intacta do acervo anterior de certo/errado).
