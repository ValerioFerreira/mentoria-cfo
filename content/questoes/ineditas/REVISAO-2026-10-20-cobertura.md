# Relatório de Revisão das Questões Inéditas de Múltipla Escolha — Cobertura PCPE Agente

**Data:** 20 de outubro de 2026  
**Revisor:** Especialista em Estatística (MentorIA / CFO-BM)  
**Arquivo:** `content/questoes/ineditas/mc/estatistica.txt`

---

## 1. Estatística — Resumo da Produção e Validação

- **Trechos cobertos:** 13 trechos (todos os 13 trechos faltantes de Estatística).
- **Questões escritas:** 78 questões inéditas de múltipla escolha (A a E, padrão Cebraspe).
- **Meta por trecho:** 6 questões por trecho (todos com 6/6 atingidos).
- **Resultado do validador (`ineditas_mc_nativas.py --check`):**
  - Estatística: 78 questões · A 16 · B 16 · C 16 · D 15 · E 15
  - Erros: 0 (distribuição perfeitamente equilibrada, nenhuma letra ultrapassa 21%, longe do teto de 30%).
- **Resultado da cobertura (`cobertura_ineditas.py --minimo 6`):**
  - Estatística eliminada integralmente da lista de pendências (13/13 trechos com >= 6 questões).

---

## 2. Detalhamento por Trecho

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `estatistica/a00/s03` | Apresentação de Dados | Amplitude de classe, amplitude total, ponto médio, fac, frequências relativas, densidade, fad | 6 | A, B, C, D, E, A |
| `estatistica/a00/s04` | Apresentação de Dados | Histograma vs colunas, densidade de frequência, polígono de frequências, polimento de curva, ogiva, assimetria | 6 | B, C, D, E, A, B |
| `estatistica/a01/s01` | Médias | Posição vs separatrizes, propriedades do somatório (constante, homogeneidade, linearidade), soma dos quadrados vs quadrado da soma, soma dos produtos vs produto das somas, somatório com limites parciais | 6 | C, D, E, A, B, C |
| `estatistica/a01/s02` | Médias | Média simples e valor faltante, junção de grupos de tamanhos distintos, transformação linear, soma algébrica de desvios nula, minimização da soma de quadrados dos desvios, limites da média | 6 | D, E, A, B, C, D |
| `estatistica/a01/s05` | Médias | Média harmônica, velocidade média com distâncias iguais, trabalho conjunto de agentes, desigualdade das médias ($x̄ \ge G \ge H$), relação $G^2 = x̄ \cdot H$, restrições de domínio | 6 | E, A, B, C, D, E |
| `estatistica/a02/s04` | Medidas Separatrizes | Conceito de decis e D5 = Mediana, cálculo em dados brutos, dados sem classes com fac, interpolação em classes, intervalo interdecílico, interpretação percentual | 6 | A, B, C, D, E, A |
| `estatistica/a02/s05` | Medidas Separatrizes | Correspondência de percentis (P50 = Md = D5 = Q2), cálculo em rol, cálculo com fac, interpolação linear em classes, frequências relativas percentuais, amplitude interquartílica | 6 | B, C, D, E, A, B |
| `estatistica/a02/s06` | Medidas Separatrizes | Resumo dos 5 números do box plot, distância interquartílica (DIQ) e desvio quartílico, limites de Tukey ($1,5 \times DIQ$), detecção de outliers, coincidência de medidas (supressão de bigodes), comparação de box plots | 6 | C, D, E, A, B, C |
| `estatistica/a03/s01` | Moda | Moda como única medida central para variáveis qualitativas nominais, classificação (amodal, unimodal, bimodal), moda em dados sem classes, moda bruta em classes, moda em frequências relativas, comparação média x mediana x moda | 6 | D, E, A, B, C, D |
| `estatistica/a03/s03` | Moda | Fórmula de King, cálculo numérico da Moda de King, classes com amplitudes desiguais e densidade de frequência, moda com vizinhas de mesma densidade, transformações lineares na moda, King vs Czuber | 6 | E, A, B, C, D, E |
| `estatistica/a04/s02` | Medidas de Dispersão | Soma algébrica dos desvios nula na média, soma dos quadrados mínima na média, soma dos módulos mínima na mediana (ímpar), intervalo de mínimo dos módulos em n par, cálculo de desvios e quadrados, síntese das propriedades | 6 | A, B, C, D, E, A |
| `estatistica/a04/s03` | Medidas de Dispersão | Razão do módulo no desvio médio, cálculo em dados não agrupados, maior desvio absoluto vs desvio médio, Dm em dados discretos ponderados, convenção do ponto médio em classes, invariância por translação e homogeneidade de escala | 6 | B, C, D, E, A, B |
| `estatistica/a05/s05` | Análise Combinatória | Partição ordenada (multinomial), partição não-ordenada (divisão por $m!$), Primeiro Lema de Kaplansky (fila linear), aplicação do 1º Lema a escalas de plantão, Segundo Lema de Kaplansky (disposição circular), comparação e propriedades dos lemas | 6 | C, D, E, A, B, C |

---

## 3. Revisão Cruzada e Qualidade Matemática

- Todas as contas foram resolvidas e conferidas à mão antes da redação e comentadas passo a passo.
- Dados numéricos simples, exatos e plausíveis no contexto de segurança pública / administração policial.
- Comandos no padrão Cebraspe ("assinale a opção correta"), sem figuras (dados expressos em prosa clara).
- Enunciados com extensão entre 25 e 60 palavras (respeitando rigorosamente a faixa de 6 a 140 palavras).
- Alternativas homogêneas em tamanho e plausibilidade técnica.
- Nenhuma menção a professor, curso ou material protegido.
- Mapeamento explícito de `| item=2.1` no cabeçalho do trecho `a05/s05` em estrita conformidade com as diretrizes.

---

## 4. Dúvidas para o Dono do Projeto (Estatística)

1. **Uso de item=2.1 no trecho `a05/s05`**: O trecho de análise combinatória (partições e Lemas de Kaplansky) foi devidamente mapeado para o item de Análise Combinatória (`item=2.1`) do edital PCPE.
2. **Nenhuma inconsistência matemática ou teórica identificada**: Todas as propriedades de somatório, média, mediana, moda, separatrizes, box plot, desvios e análise combinatória foram redigidas com base na teoria clássica consolidada e na jurisprudência das bancas (especialmente Cebraspe).

---

## 5. Língua Portuguesa — Resumo da Produção e Validação

- **Trechos cobertos:** 10 trechos (todos os 10 trechos faltantes de Língua Portuguesa).
- **Questões escritas:** 60 questões inéditas de múltipla escolha (5 alternativas A a E, uma correta, padrão Cebraspe).
- **Meta por trecho:** 6 questões por trecho (todos com 6/6 atingidos).
- **Arquivo gerado:** `content/questoes/ineditas/mc/lingua-portuguesa.txt`.
- **Resultado do validador (`ineditas_mc_nativas.py --check`):**
  - Língua Portuguesa: 60 questões · A 12 · B 12 · C 12 · D 12 · E 12
  - Erros: 0 (distribuição perfeitamente equilibrada de 20% para cada alternativa A, B, C, D, E).
- **Resultado da cobertura (`cobertura_ineditas.py --minimo 6`):**
  - Língua Portuguesa eliminada integralmente da lista de pendências (10/10 trechos com >= 6 questões).

---

## 6. Língua Portuguesa — Detalhamento por Trecho

| Trecho | Aula | Tópicos Cobertos | Item Edital | Qtd | Gabaritos |
|---|---|---|---|:---:|---|
| `lingua-portuguesa/a00/s01` | Nivelamento | Acentuação de proparoxítonas, paroxítonas e oxítonas; hífen no Acordo Ortográfico; porquês; haver x a; onde x aonde; encontros vocálicos | `item=3` | 6 | A, B, C, D, E, A |
| `lingua-portuguesa/a00/s02` | Nivelamento | Colocação pronominal (próclise obrigatória CNA da PRII e proibições); demonstrativos (espaço/tempo/discurso); advérbios e circunstâncias; preposições e valores semânticos; morfossintaxe (artigo substantivador); pronomes de tratamento e concordância de 3ª pessoa | `item=5.1` | 6 | B, C, D, E, A, B |
| `lingua-portuguesa/a00/s03` | Nivelamento | Conjunções coordenativas (adversativas, conclusivas, explicativas); conjunções subordinativas adverbiais (concessivas, causais, proporcionais); modos verbais (indicativo, subjuntivo, imperativo); pretéritos do indicativo (perfeito, imperfeito, mais-que-perfeito simples e composto); formas nominais do verbo; valores do futuro do pretérito | `item=5.1` | 6 | C, D, E, A, B, C |
| `lingua-portuguesa/a00/s04` | Nivelamento | Regência de assistir, aspirar e visar; pontuação da ordem direta SuVeCA e adjunto adverbial deslocado; complemento nominal x adjunto adnominal; haver impessoal e concordância; regência de implicar e obedecer; tipos de sujeito e núcleo não preposicionado | `item=5.4` | 6 | D, E, A, B, C, D |
| `lingua-portuguesa/a00/s05` | Nivelamento | Casos obrigatórios de crase (locuções de base feminina); casos proibidos de crase (antes de verbos e pronomes pessoais); crase facultativa (possessivo feminino singular, nomes próprios, até a); parônimos clássicos (absolver/absorver, retificar/ratificar, eminente/iminente); denotação x conotação e ambiguidade; tipologia textual (injuntivo, descritivo, expositivo, argumentativo) | Padrão | 6 | E, A, B, C, D, E |
| `lingua-portuguesa/a04/s04` | Classes de palavras: verbos | Verbos em -ear e -iar (grupo MARIO: mediar, ansiar, remediar, incendiar, odiar); verbos ver e vir e derivados no futuro do subjuntivo; derivados de ter e pôr (bases TIVE- e PUSE-); querer x requerer; verbos defectivos (reaver, precaver, abolir); alternância vocálica no radical de verbos em -ir (paradigma ferir: aderir, divergir) | Padrão | 6 | A, B, C, D, E, A |
| `lingua-portuguesa/a04/s05` | Classes de palavras: verbos | Correlação clássica de hipótese irreal (pretérito imperfeito do subjuntivo + futuro do pretérito); correlação de eventualidade futura (futuro do subjuntivo + futuro do presente); presente do subjuntivo com presente/futuro do indicativo; sucessão de pretéritos (imperfeito durativo interrompido por perfeito pontual); oração causal com "como" + imperfeito do subjuntivo; erro de correlação por mistura de tempos incompatíveis | Padrão | 6 | B, C, D, E, A, B |
| `lingua-portuguesa/a04/s06` | Classes de palavras: verbos | Conversão da ativa para passiva analítica (objeto direto vira sujeito paciente); voz passiva sintética (concordância de VTD com sujeito paciente posposto); partícula apassivadora x índice de indeterminação do sujeito (IIS com VTI, VI e VL); impossibilidade de apassivação com VTI, VI e VL; comportamento do particípio (variável na passiva analítica e invariável no tempo composto da ativa); voz reflexiva recíproca x passiva | Padrão | 6 | C, D, E, A, B, C |
| `lingua-portuguesa/a07/s04` | Concordância nominal e verbal | Concordância do verbo ser com sujeito pronome neutro e predicativo plural; concordância do adjetivo referente a mais de um substantivo (anteposto x posposto); expressões "é proibido", "é necessário" e "é bom" (com e sem determinante); flexão e invariabilidade de meio, bastante, caro e só; concordância de anexo, quite, mesmo, alerta e menos; adjetivos compostos (regra geral e invariabilidade com substantivo indicando cor) | Padrão | 6 | D, E, A, B, C, D |
| `lingua-portuguesa/a09/s02` | Mecanismos de coesão textual | Coesão referencial com demonstrativos ("isso" anafórico sintetizador de informação prévia); equivalência semântica entre conectivos adversativos (porém, contudo, todavia); coerência interna (compatibilidade lógica e ausência de contradição por conectivos inadequados); efeito semântico da pontuação em orações adjetivas explicativas x restritivas; conversão de orações reduzidas em desenvolvidas; reescritura de períodos com deslocamento de orações adverbiais | Padrão | 6 | E, A, B, C, D, E |

---

## 7. Língua Portuguesa — Revisão Cruzada e Qualidade Gramatical

- Todas as questões foram redigidas com estrita observância da gramática normativa culta (Celso Cunha & Lindley Cintra, Evanildo Bechara, Rocha Lima) e do Manual de Redação da Presidência da República (3ª edição, 2018).
- Todos os enunciados contêm comandos claros no padrão Cebraspe ("assinale a opção correta" ou "assinale a opção INCORRETA"), sem figuras e com tamanho estritamente dentro da faixa regulamentar (16 a 40 palavras).
- As alternativas A a E possuem extensão equilibrada e homogênea, sem distratores absurdos e sem pistas de extensão no gabarito.
- A distribuição de gabaritos foi rigorosamente calibrada ciclicamente (exatamente 12 questões para cada uma das letras A, B, C, D, E).
- Comentários didáticos e completos, justificando tecnicamente o gabarito e refutando os distratores.
- Nenhuma menção a "aula", "curso", "professor" ou materiais protegidos.
- Os parâmetros `| item=` foram aplicados com exatidão conforme as especificações do edital PCPE:
  - `a00/s01 | item=3`
  - `a00/s02 | item=5.1`
  - `a00/s03 | item=5.1`
  - `a00/s04 | item=5.4`

---

## 8. Dúvidas para o Dono do Projeto (Língua Portuguesa)

1. **Assuntos múltiplos no nivelamento (`a00`)**: O nivelamento aborda blocos amplos da língua. As questões foram calibradas para os itens específicos do edital indicados no briefing (`item=3` para ortografia, `item=5.1` para morfologia/classes de palavras e `item=5.4` para sintaxe/concordância/regência), garantindo perfeita integração ao banco e ao plano de estudos.
2. **Nenhuma controvérsia gramatical remanescente**: Todas as regras adotadas correspondem à doutrina pacífica da norma culta exigida pelo Cebraspe e pelo edital do concurso.


---

## 9. Informática — Resumo da Produção e Validação

- **Trechos cobertos:** 17 trechos (todos os 17 trechos faltantes de Informática).
- **Questões escritas:** 104 questões inéditas de múltipla escolha (5 alternativas A a E, uma correta, padrão Cebraspe).
- **Meta por trecho:** 6 questões por trecho para 16 trechos e 8 questões para `informatica/a10/s04` (peso 0.239 >= 0.20), totalizando exatamente 104 questões (todas as metas cumpridas integralmente).
- **Arquivo gerado:** `content/questoes/ineditas/mc/informatica.txt`.
- **Resultado do validador (`ineditas_mc_nativas.py --check`):**
  - Informática: 104 questões · A 21 · B 21 · C 21 · D 21 · E 20
  - Erros: 0 (distribuição equilibrada com no máximo 20,19% por letra, longe do teto de 30%/32%).
- **Resultado da cobertura (`cobertura_ineditas.py --minimo 6`):**
  - Informática eliminada integralmente da lista de pendências (17/17 trechos com >= 6 questões).

---

## 10. Informática — Detalhamento por Trecho

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `informatica/a00/s01` | Conceito de Internet e Redes | Comutação por pacotes vs circuitos (ARPANET); redes LAN (cabeada e sem fio); Internet vs World Wide Web (HTTP/HTTPS); redes WAN de grande abrangência geográfica; redes PAN (WPAN e Bluetooth); modelo de arquitetura cliente/servidor | 6 | A, B, C, D, E, A |
| `informatica/a01/s02` | Intranet e Extranet | Conceito de Extranet como extensão controlada da intranet; distinção entre Intranet remota, Extranet e Portal Web Público; arquitetura de VPN Site-to-Site entre filiais; VPN Client-to-Site para trabalho remoto; tunelamento vs criptografia em VPNs; aplicações corporativas B2B e supply chain | 6 | B, C, D, E, A, B |
| `informatica/a02/s01` | Segurança da Informação: Fundamentos | Controles físicos vs lógicos (critério pelo ativo/obstáculo); taxonomia de ativos, vulnerabilidades, ameaças e incidentes; controles administrativos/organizacionais (PSI e termos); controles preventivos, detectivos e corretivos; conceito e cálculo probabilístico de risco computacional; escopo institucional da ISO/IEC 27001 e PNSI (Decreto 9.637) | 6 | C, D, E, A, B, C |
| `informatica/a02/s02` | Princípios de Segurança da Informação | Princípio da Integridade e independência em relação à confidencialidade; princípio da Disponibilidade e redundâncias; relação entre Autenticidade e Irretratabilidade (Não Repúdio); rastreabilidade e requisitos de logs de auditoria (append-only e NTP); classificação de ataques por princípio violado (interrupção, interceptação, modificação, fabricação); Hexagrama Parkeriano (posse/controle e utilidade) | 6 | D, E, A, B, C, D |
| `informatica/a02/s03` | Criptologia e Criptografia | Esteganografia vs Criptografia; criptografia simétrica e principais algoritmos (AES, DES); gerenciamento e escalabilidade de chaves simétricas ($n(n-1)/2$); criptografia assimétrica e chaves pública/privada (confidencialidade vs assinatura); criptografia híbrida e chave de sessão (TLS/HTTPS); Princípio de Kerckhoffs em segurança computacional | 6 | E, A, B, C, D, E |
| `informatica/a02/s06` | Certificados Digitais e ICP-Brasil | Estrutura e padrão ITU-T X.509 de certificados digitais; papel e competências da AC-Raiz (operada pelo ITI); atribuições da Autoridade de Registro (AR); distinção entre certificados do tipo A1 (software, 1 ano) e A3 (hardware, token/smart card, até 5 anos); mecanismos de revogação por Lista de Certificados Revogados (LCR) e protocolo OCSP; categorias de certificados na ICP-Brasil (séries A, S e T) | 6 | A, B, C, D, E, A |
| `informatica/a03/s01` | Malwares: Conceitos e Classificação | Terminologia técnica: distinção entre Hacker e Cracker; módulos estruturais de um vírus (infecção, ativação/bomba lógica e carga útil); dependência de arquivo hospedeiro e execução no vírus; fases de execução do ciclo de vida de um vírus; suscetibilidade de sistemas operacionais a vírus (Linux e macOS não são imunes); conceito e impacto de ameaças internas do tipo Insider | 6 | B, C, D, E, A, B |
| `informatica/a03/s02` | Tipos Específicos de Vírus | Vírus de macro em documentos do pacote Office; vírus de boot em setor de inicialização (MBR); vírus multipartite e infecção cruzada de executáveis e boot; diferenças operacionais entre vírus polimórficos e metamórficos; vírus stealth (furtivo) e interceptação de chamadas de sistema; vírus time bomb (bomba-relógio) e condições temporais de disparo | 6 | C, D, E, A, B, C |
| `informatica/a03/s05` | Ataques e Golpes Virtuais | Ataques de negação de serviço (DoS/DDoS) e foco em indisponibilidade; ataque de força bruta (brute force) e defesas com bloqueio e MFA; e-mail spoofing e falsificação de cabeçalhos no SMTP; IP spoofing e mascaramento de endereçamento de origem; engenharia social e manipulação psicológica (phishing); conceito e finalidade defensiva de Honeypots | 6 | D, E, A, B, C, D |
| `informatica/a04/s02` | Mecanismos de Proteção Antimalware | Análise heurística estática e dinâmica de 2ª geração e risco de falsos positivos; interceptação de chamadas e monitoramento comportamental de 3ª geração; tecnologias de 4ª geração e antivírus NGAV com aprendizado de máquina em nuvem; filtros antispam (triagem bayesiana sem funções de criptografia); softwares antispyware e isolamento em quarentena; teste de código isolado em ambientes Sandbox | 6 | E, A, B, C, D, E |
| `informatica/a04/s03` | Firewalls Perimetrais e Pessoais | Conceito e formas de implementação de Firewalls (software, hardware e híbrido); modo operacional restritivo (lista branca / default deny); atuação do Firewall Pessoal contra backdoors; filtro de pacotes estático (stateless) nas camadas 3 e 4; zona desmilitarizada (DMZ) e isolamento de servidores públicos; limites de atuação do firewall perante arquivos com malwares | 6 | A, B, C, D, E, A |
| `informatica/a10/s01` | PowerPoint: Histórico e Microsoft 365 | Origem histórica do PowerPoint (Forethought, 1987) e aquisição pela Microsoft; inovação na proporção padrão widescreen 16:9 no PowerPoint 2013; caixa de assistência "Diga-me o que você deseja fazer" no PowerPoint 2016; novidades do PowerPoint 2019 (transição Transformar e navegação por Zoom); modelo de software como serviço (SaaS) no Microsoft 365 com atualizações mensais; coautoria em tempo real no PowerPoint online | 6 | B, C, D, E, A, B |
| `informatica/a10/s02` | PowerPoint: Interface e Componentes | Barra de Ferramentas de Acesso Rápido e suas regras de customização; restrições de personalização da Guia Arquivo (Modo Backstage); navegação, seções e organização no Painel de Slides; atalho de teclado Ctrl + F1 para alternar a Faixa de Opções; Painel de Anotações no Modo do Apresentador em múltiplos monitores; elementos informativos da Barra de Status | 6 | C, D, E, A, B, C |
| `informatica/a10/s04` | PowerPoint: Guias Inserir, Design, Transições e Animações | Organogramas e diagramas corporativos via SmartArt (guia Inserir); localização do comando Caixa de Texto na guia Inserir (grupo Texto); personalização do tamanho de slide na guia Design; distinção fundamental entre Transição (entre slides) e Animação (em objetos); botão "Aplicar a Todos" na guia Transições; categorias de animação (Entrada, Ênfase, Saída e Caminhos); Pincel de Animação (Alt + Shift + C); gerenciamento sequencial no Painel de Animação | 8 | D, E, A, B, C, D, E, A |
| `informatica/a12/s07` | Windows 11: Sistema e Configurações | Atalho Tecla Windows + I para o aplicativo Configurações; convivência harmônica entre Configurações e o Painel de Controle clássico; configuração de múltiplos monitores (duplicar/estender) em Sistema > Tela; recurso Luz Noturna para atenuação de luz azul; gerenciamento individual por aplicativo com o Mixer de Volume; modo Não Incomodar e sessões de Foco | 6 | B, C, D, E, A, B |
| `informatica/a12/s09` | Windows 11: Personalização e Aplicativos | Apresentação de slides na Tela de Fundo (intervalos de 1 minuto a 1 dia); modos de cores (Claro, Escuro e Personalizado) e efeitos de transparência; definição de Aplicativos Padrão por extensão de arquivo ou protocolo; tela de bloqueio (Tecla Windows + L) e aplicativos de status; Conta Microsoft (sincronizada em nuvem) vs Conta Local (offline); catálogo e instalação de fontes TrueType e OpenType | 6 | C, D, E, A, B, C |
| `informatica/a12/s10` | Windows 11: Entrada, Acessibilidade e Ferramentas | Armazenamento local seguro e criptografado de dados biométricos no Windows Hello; Bloqueio Dinâmico com emparelhamento Bluetooth de smartphone; atalhos e ampliação visual dinâmica com o aplicativo Lupa (Tecla Windows + [+] e Tecla Windows + Esc); ajuste de layout e idioma de teclado (ABNT2) em Hora e Idioma; cópias de segurança de versões anteriores com o Histórico de Arquivos; sobreposição e captura de tela com a Xbox Game Bar (Tecla Windows + G) | 6 | D, E, A, B, C, D |

---

## 11. Informática — Revisão Cruzada e Conformidade Técnica

- Todas as 104 questões foram redigidas observando com rigor os padrões de cobrança do Cebraspe para as carreiras policiais (PCPE Agente e similares).
- Atualização tecnológica: referências estritas ao Windows 11 (aplicativo Configurações, Windows Hello local, Bloqueio Dinâmico, Lupa, layouts de teclado) e à suíte Microsoft 365 / PowerPoint (proporção 16:9, Guia Arquivo não personalizável, transição Transformar, Zoom, guias Inserir, Design, Transições e Animações, Pincel de Animação Alt+Shift+C).
- Segurança da informação alinhada com as normas ISO/IEC 27001, ISO/IEC 27005, o Decreto federal nº 9.637/2018 (PNSI), as cartilhas do CERT.br e a legislação da ICP-Brasil (MP nº 2.200-2/2001).
- Todos os enunciados possuem comandos expressos ("assinale a opção correta", "assinale a opção que indica..." etc.) e extensão entre 25 e 60 palavras, dentro do intervalo permitido (6 a 140 palavras).
- As alternativas A a E possuem extensão equilibrada e homogênea, sem distratores absurdos e sem opções desproporcionalmente longas que denunciem o gabarito.
- A distribuição de gabaritos é rigorosamente equilibrada: A=21, B=21, C=21, D=21, E=20 (nenhuma ultrapassando 20,19%).
- Comentários detalhados justificam a alternativa correta e apontam especificamente o erro de cada distrator.
- Nenhuma menção a "aula", "curso", "professor" ou materiais protegidos.

---

## 12. Dúvidas para o Dono do Projeto (Informática)

1. **Mapeamento de trechos e itens do edital**: Todos os 17 trechos de Informática possuem correspondência automática direta e unívoca no mapa do edital do PCPE (`p1.2`, `p1.3`, `p2.3`, `p3.1` e `p3.4`), dispensando o uso de qualificadores `| item=` adicionais.
2. **Nenhuma controvérsia técnica remanescente**: Todas as opções e conceitos adotados representam o estado da arte e a doutrina unânime da área de tecnologia da informação em concursos públicos contemporâneos.


---

## 13. Raciocínio Lógico — Resumo da Produção e Validação

- **Trechos cobertos:** 29 trechos (todos os 29 trechos faltantes de Raciocínio Lógico).
- **Questões escritas:** 174 questões inéditas de múltipla escolha (5 alternativas A a E, uma única correta, padrão Cebraspe).
- **Meta por trecho:** 6 questões por trecho (todos com 6/6 atingidos).
- **Arquivo gerado:** `content/questoes/ineditas/mc/raciocinio-logico.txt`.
- **Resultado do validador (`ineditas_mc_nativas.py --check`):**
  - Raciocínio Lógico: 174 questões · A 35 · B 35 · C 35 · D 35 · E 34
  - Erros: 0 (distribuição perfeitamente equilibrada de ~20% por alternativa, sem nenhuma letra excedendo o limite de 30%/32%).
- **Resultado da cobertura (`cobertura_ineditas.py --minimo 6`):**
  - Raciocínio Lógico integralmente coberto (29/29 trechos com >= 6 questões; 140/140 trechos no projeto global).

---

## 14. Raciocínio Lógico — Detalhamento por Trecho

| Trecho | Aula | Tópicos Cobertos | Qtd | Gabaritos |
|---|---|---|:---:|---|
| `raciocinio-logico/a00/s02` | Estruturas Lógicas I | Conceito de proposição; orações não proposicionais; sentenças abertas e equações; quantificadores lógicos; princípios fundamentais; paradoxos lógicos | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a00/s06` | Estruturas Lógicas I | Tabela-verdade da bicondicional; condição suficiente e necessária na bicondicional; simbolização formal; valoração com proposições aritméticas; equivalência com conjunção de condicionais; dedução prática em normas | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a00/s11` | Estruturas Lógicas I | Número de linhas da tabela-verdade ($2^n$); disjunção falsa e deduções necessárias; valoração com fatos dados; negação na linguagem natural vs lógica; condicional falsa; Modus Tollens básico | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a01/s03` | Estruturas Lógicas II | Tabela-verdade de condicional com conjunção; conceito de contingência; identificação de tautologia; cálculo passo a passo de composta; definição e reconhecimento de contradição; implicação lógica tautológica | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a01/s04` | Estruturas Lógicas II | Método da prova por absurdo; tautologia do Modus Ponens; custo operacional da tabela-verdade em $n \ge 4$; teste rápido de contingência; análise indireta de contradição; análise tautológica de fórmula complexa | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a01/s08` | Estruturas Lógicas II | Terceiro excluído ($p \lor \sim p$ tautologia); não contradição ($p \land \sim p$ contradição); disjunção exclusiva tautológica ($p \underline{\lor} \sim p$); contingência em proposições simples atômicas; contradição disfarçada em adversativas; bicondicional contraditória ($p \leftrightarrow \sim p$) | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a02/s02` | Equivalências Lógicas e Negações | Condicional em disjunção inclusiva ($\sim p \lor q$); contrapositiva ($\sim q \rightarrow \sim p$); disjunção em condicional ($\sim p \rightarrow q$); as duas únicas equivalentes da condicional; negação da condicional ($p \land \sim q$); negação de condicional no contexto policial | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a02/s05` | Equivalências Lógicas e Negações | Negação da bicondicional em disjunção exclusiva ($p \underline{\lor} q$); negação com bicondicional e um termo negado; negação com e/ou/não; comutatividade e a exceção da condicional; associatividade de conjunção e disjunção; armadilha da negação dupla ($\sim p \leftrightarrow \sim q$) | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a02/s06` | Equivalências Lógicas e Negações | Distributiva do e sobre o ou; distributiva do ou sobre o e; colocar em evidência (fatoração lógica); lei da absorção; idempotência; leis da identidade com verdadeiro e falso | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a02/s08` | Equivalências Lógicas e Negações | Negação de condicional com disjunção no consequente ($p \land \sim q \land \sim r$); negação com conjunção no consequente; contrapositiva com antecedente disjuntivo; equivalente de $\sim p \rightarrow q$ em disjunção; De Morgan em expressão mista; contrapositiva com termos negativos | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a02/s09` | Equivalências Lógicas e Negações | Negação da disjunção exclusiva em bicondicional; negação de conjunção transformada em condicional; negação de quantificador universal (Todo); negação de quantificador existencial (Algum); negação de universal negativo (Nenhum); contraposição em conjunção de condicionais | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a04/s01` | Lógica de Argumentação | Método em quatro etapas em questões clássicas de conectivos; Modus Ponens direto; disjunção exclusiva e fixação de valor único; condicional com consequente falso; conjunção verdadeira e propagação; cadeia de condicionais com consequente final falso | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a04/s02` | Lógica de Argumentação | Definição estrutural de argumento dedutivo; validade vs verdade; critério de invalidade dedutiva; argumento válido com premissas falsas; conceito de argumento sólido (sound argument); análise com variável indeterminada | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a04/s04` | Lógica de Argumentação | Estrutura canônica do silogismo categórico; função lógica do termo médio; regra das duas premissas negativas; regra da conclusão seguir a premissa mais fraca; teste por diagramas de Euler-Venn; falácia do termo médio não distribuído | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a04/s07` | Lógica de Argumentação | Estrutura clássica do Dilema Construtivo; estrutura clássica do Dilema Destrutivo; regra do Silogismo Disjuntivo; transitividade no Silogismo Hipotético; aplicação prática de Dilema Construtivo em operação; encadeamento de Silogismo Disjuntivo e Modus Ponens | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a04/s08` | Lógica de Argumentação | Resolução de trás para frente em cadeia de condicionais; inconsistência lógica interna em sistema de premissas; condicional com disjunção no antecedente e Modus Tollens; bicondicional combinada com disjunção; dedução em sistema com três agentes; encadeamento reverso em escala funcional | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a04/s09` | Lógica de Argumentação | Apuração com cinco suspeitos e implicação lógica; dedução a partir de condicional declarada falsa; teste dedutivo com quatro agentes e bicondicional; depoimentos contraditórios e terceiro excluído; disjunção exclusiva combinada com condicional; problema dos três policiais que mentem ou dizem a verdade | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a04/s10` | Lógica de Argumentação | Falácia formal da afirmação do consequente; falácia formal da negação do antecedente; Modus Ponens válido; Modus Tollens válido; validação silogística por diagramas de inclusão de conjuntos; dedução vs indução (validade vs força) | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a04/s11` | Lógica de Argumentação | Modus Tollens combinado com De Morgan; inferência a partir de conjunção falsa; encadeamento de Modus Tollens e Silogismo Disjuntivo; cadeia em linguagem natural dedutiva; Dilema Destrutivo em contexto operacional; princípio da explosão (ex contradictione sequitur quodlibet) | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a04/s12` | Lógica de Argumentação | Roteiro de verificação de validade dedutiva; identificação de argumentos dedutivamente válidos em grupo; dedução em cadeia com negação fática; definição técnica de conjunto consistente de premissas; escala de plantão e deduções necessárias; intercambialidade dos métodos de teste de validade | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a05/s01` | Raciocínio Crítico I | Estrutura básica dos argumentos (premissas e conclusão); indicadores linguísticos de premissa; identificação de conclusão em texto forense; argumento vs explicação; premissas como razões probatórias; identificação de premissa em parágrafo discursivo | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a05/s02` | Raciocínio Crítico I | Inferências analíticas (dedutivas) vs sintéticas (indutivas/abdutivas); argumento indutivo por regularidade observada; raciocínio abdutivo (inferência para a melhor explicação); argumento por analogia e critérios de força; indução por generalização estatística; fatores determinantes da força indutiva | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a05/s04` | Raciocínio Crítico I | Falácia Ad Hominem (ataque à pessoa); apelo à autoridade indevida (Ad Verecundiam); apelo à ignorância (Ad Ignorantiam); falácia do Falso Dilema; falácia da Pergunta Complexa; falácia formal da afirmação do consequente vs falácias informais | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a05/s05` | Raciocínio Crítico I | Falácia do Espantalho (homem de palha); petição de princípio (raciocínio circular); conclusão irrelevante (Ignoratio Elenchi); falácia do Falso Escocês (nenhum escocês verdadeiro); apelo à piedade (Ad Misericordiam); falácia do Acidente (Dicto Simpliciter) | 6 | D, E, A, B, C, D |
| `raciocinio-logico/a05/s06` | Raciocínio Crítico I | Falácia da causa falsa (Post hoc ergo propter hoc); falácia da causa complexa; falácia da causa insignificante; falácias de Composição e de Divisão; falácia do equívoco (ambiguidade lexical); falácia da anfibologia (ambiguidade sintática) | 6 | E, A, B, C, D, E |
| `raciocinio-logico/a05/s07` | Raciocínio Crítico I | Entimemas e premissas ocultas; identificação de pressuposto implícito em caso penal; enfraquecimento de argumento causal por rota alternativa; fortalecimento de argumento por validação de premissa oculta; pressupostos em declarações de autoridades; enfraquecimento por hipótese alternativa | 6 | A, B, C, D, E, A |
| `raciocinio-logico/a05/s08` | Raciocínio Crítico I | Apelo ao povo (Argumentum ad Populum); falácia da Ladeira Escorregadia (Slippery Slope); apelo às consequências (Ad Consequentiam); falácia Tu Quoque (você também); apelo ao medo e às consequências institucionais; Ad Hominem Circunstancial em contestação pericial | 6 | B, C, D, E, A, B |
| `raciocinio-logico/a05/s09` | Raciocínio Crítico I | Conclusões intermediárias (subconclusões); premissas dependentes (copulativas); premissas independentes (convergentes); análise de convergência probatória em inquérito; identificação de conclusão principal em cadeia; método de identificação da tese central | 6 | C, D, E, A, B, C |
| `raciocinio-logico/a05/s10` | Raciocínio Crítico I | Método do contraexemplo na refutação dedutiva; inconsistência lógica interna em relatos; avaliação crítica de amostragem indutiva; refutação de falsa analogia por dessemelhanças essenciais; falha de relevância lógica temática (non sequitur); critérios clássicos ARS de avaliação crítica | 6 | D, E, A, B, C, D |

---

## 15. Raciocínio Lógico — Revisão Cruzada e Conformidade Lógica

- **Conformidade teórica e matemática:** Todas as deduções, tabelas-verdade, aplicações de De Morgan, contrapositivas, propriedades algébricas e regras de inferência foram rigorosamente calculadas e conferidas à mão antes de fixar cada gabarito.
- **Padrão Cebraspe em múltipla escolha:**
  - Enunciados claros, objetivos e contextualizados com situações operacionais, periciais e institucionais da Polícia Civil, além de problemas lógicos formais canônicos.
  - Todos os 174 enunciados contêm comandos explícitos ("assinale a opção correta", "assinale a opção que indica...", etc.) e extensão entre 20 e 65 palavras (dentro da faixa exigida de 6 a 140 palavras).
  - Alternativas A a E homogêneas em conteúdo e extensão, sem distratores absurdos e sem pistas de comprimento no gabarito (todas com `len(certa) <= 1.8 * média(distratores)`).
  - Distribuição ciclicamente perfeita: exatamente A 35, B 35, C 35, D 35, E 34 (nenhuma letra ultrapassa 20.12%, longe do limite de 30%/32%).
- **Comentários didáticos:** Cada questão traz justificativa dedutiva e matemática completa do porquê o gabarito é verdadeiro e por que cada um dos quatro distratores é incorreto ou falacioso.
- **Neutralidade absoluta:** Sem nenhuma menção a "aula", "curso", "professor" ou nomes de materiais-base protegidos.
- **Sem figuras:** Todas as tabelas, diagramas e dados foram perfeitamente descritos em prosa textual inteligível.

---

## 16. Dúvidas para o Dono do Projeto (Raciocínio Lógico)

1. **Correspondência de itens do edital:** Todos os 29 trechos mapeiam diretamente e sem ambiguidades para os códigos do edital do PCPE (`raciocinio-logico/p9`, `p10`, `p11.1`, `p11.2`, `p11.3` e `p11.4`), dispensando o uso de qualificadores `item=` manuais.
2. **Nenhuma controvérsia remanescente:** Todos os 29 trechos atingiram a meta integral de 6 questões inéditas de múltipla escolha validadas com zero erros (`erros 0`) pelo validador oficial.
