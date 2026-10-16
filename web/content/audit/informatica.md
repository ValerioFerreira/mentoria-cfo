# Auditoria estrutural — Informática

Material: Estratégia (Diego Carvalho, Renato da Costa), aulas a00–a14, 2.217 págs. no total. Edital: Anexo II, itens 1–7 de Informática do 2º Tenente (5 questões na prova).

## Números

| | Antes | Depois |
|---|---:|---:|
| Páginas de teoria (T) | 1.129 | 1.085 |
| Trechos de Teoria | 107 | 109 |
| Págs. por trecho (mín–méd–máx) | 7–10,6–17 | 6–10,0–17 |
| Trechos cortados no meio de um tópico | 4 | 0 |
| Trechos > 17 págs. | 0 | 0 |

Auditei as 15 aulas. Varri todas as páginas com `--heads` e li as páginas de fronteira, os sumários, os glossários e os trechos suspeitos. Também conferi os níveis de "INCIDÊNCIA EM PROVA" que o próprio material marca em cada tópico.

## Correções feitas (`content/overrides/informatica.json`)

1. **Sumários classificados como teoria (13 aulas, 41 págs.)**. A detecção automática parou na pág. 2 (`tocMax = 2`), mas o sumário ("Tópicos da Aula"/"Sumário") e a "Apresentação" ficam nas págs. 3–9. Eles viraram teoria e inflavam o 1º trecho de cada aula (a06 tinha 7 págs. de sumário dentro do s01). Marquei como FRONT: a00 5–6, a02 3–5, a03 3–4, a04 3–4 e 59 (sumário da parte de Firewall), a05 3, a06 3–9, a07 3–6, a08 3–5, a09 3–5, a10 3–4, a11 3–5, a12 3–7, a13 3–5.
2. **a00 57–59 (Glossário)** passou a SUMMARY. É uma tabela de consulta, com incidência baixíssima segundo o material, e repete conceitos (traz também bitcoin, NFT e metaverso).
3. **Subtítulos**:
   - a03: adicionei "Tipos de vírus" (p.12). O tópico Vírus tem 12 págs. e era cortado no meio.
   - a02: adicionei "Criptografia Assimétrica" (p.28) e removi o falso subtítulo da URL do AES Crypt (p.27).
   - a06: adicionei "Referência Absoluta" (p.83).
   - a14: adicionei Famílias de Processadores (75), Memória RAM (85), Memória Cache (90), HD (107), Memórias ópticas (110) e SSD (114). Removi falsos subtítulos vindos de legendas e tabelas (21, 79, 94, 107, 120).
   - a00: removi 10 falsos subtítulos (URL do CERN, legendas de alcance de rede, do fluxo de e-mail, de DNS e de domínios).
4. **Cortes em inícios de seção reais** (motivo: o trecho misturava o fim de um assunto com o começo de outro):
   - a00: Web (15), Protocolos (26), Camada de Aplicação (38).
   - a02: Princípios (12), Criptologia (20).
   - a03: Tipos de vírus (12), Worm (21), Ataques e Golpes (50), Phishing (61).
   - a06: Interface (20), Fórmulas e Funções (70), Pesquisa e Referência (115), Conceitos Avançados/Gráficos (137).
   - a07: Estatísticas (41), Lógicas (50).
   - a08: Guia Arquivo (31).
   - a10: Interface (16), Opções da Faixa (25), Inserir (40).
   - a12: Área de Trabalho (14), Janelas (40), Painel de Controle (62), Configurações (74), Arquivos e Pastas (116), Ferramentas (138), Softwares Utilitários (155), Administração e Segurança (170).
   - a13: Modelos de Serviço (19), Armazenamento (33).
   - a14: CPU (69), Memória (83), Cache (90), Memória Secundária (101), Ópticas (110).
5. **Notas de aula** (aparecem no catálogo):
   - a07: o Calc não traz gráficos nem filtros nesta aula.
   - a12: o Prompt de Comando é tratado de forma rasa e a aula cita o DELTREE, que não existe no Windows 11.

Nenhuma aula saiu do plano: todas são `edital: yes`.

### a12 (Windows 11) e a06 (Excel)

**a12** ficou com 179 págs. de teoria e 20 trechos de 6 a 12 págs. Cada trecho agora pertence a uma única seção do sumário do material (Área de Trabalho, Janelas, Painel de Controle, Configurações, Arquivos, Ferramentas, Utilitários, Administração, Recursos avançados). Antes, o Painel de Controle começava no meio de "Snap Layouts" e terminava junto com Configurações.

Partes de incidência baixíssima e escopo discutível foram mantidas como trechos identificáveis, sem tirar páginas: Jogos, Regedit, Sandbox, formatação, partição, sistemas de arquivos, BitLocker e AppData. Elas cabem em "recursos do sistema".

**a06** tem 172 págs. e 16 trechos. Fórmulas e funções (70–136) vêm separadas por família. Funções financeiras e macros/VBA/ODBC formam os trechos s15–s16 (aprofundamento). As páginas do Excel têm pouco texto (muitas imagens), por isso os trechos chegam a 13–17 págs. com carga normal.

### Muitos trechos pequenos (média de 10 págs.)

A causa é a carga e não a estrutura. Informática usa `DENSITY_FACTOR = 1,25` (o mesmo de Matemática e Física), e a página "cheia" chega a 1,6 de carga. Com o alvo de 12, isso dá cerca de 8 págs. por trecho em aulas de texto corrido (a00, a02, a03, a12).

O texto do Diego Carvalho é prosa didática, com tabelas, capturas de tela e muitas questões resolvidas no meio da teoria (blocos "Comentários: … (Letra X)"). Ele é lido bem mais rápido que Matemática. Os trechos atuais são coerentes, mas o tempo planejado parece superestimado: cerca de 109 h de Teoria para 5 questões. Ver os pedidos ao orquestrador.

## Cobertura do edital

| Item | Status | Onde |
|---|---|---|
| 1.1 Internet | covered | a00 7–25; a01 6–9 |
| 1.2 Intranet/extranet | covered | a01 5–21 |
| 2.1 Protocolos e serviços | covered | a00 26–56 |
| 2.2 Navegadores | **partial** | a00 15–17 (conceito); a12 168–169 (Edge, 1,5 pág.) |
| 2.3 Serviços de internet (e-mail, busca…) | **partial** | a00 38–43, 55–56; a13 41–52 |
| 2.4 Computação em nuvem | covered | a13 6–40; a12 166–167 |
| 3.1 Princípios e controles | covered | a02 6–19 |
| 3.2 Ameaças e vulnerabilidades | covered | a02 10–11; a03 50–81 |
| 3.3 Malwares | covered | a03 5–49 |
| 3.4 Phishing | covered | a03 61–72 |
| 3.5 Criptografia, assinatura, certificado | covered | a02 20–34, 44–51, 56–67 |
| 3.6 Autenticação | covered | a02 35–43, 52–55 |
| 3.7 Boas práticas (antimalware, firewall) | covered | a04 5–20, 60–77; a03 62–66 |
| 4.1–4.3 Backup: procedimentos, tipos, restauração | covered | a05 4–20; a12 86–87, 108, 173–175 |
| 4.4 Dispositivos de armazenamento | covered | a14 101–120 |
| 5.1 Arquivos e pastas (criar, renomear, copiar, mover, excluir) | covered | a12 116–137 |
| 5.2–5.4 Processador, memórias, E/S e periféricos | covered | a14 14–100 |
| 5.5 Instalação/configuração de periféricos | **partial** | a12 67–68, 91; a14 63–64 |
| 6.1–6.4 Windows 11 (interface, arquivos, configurações, Painel de Controle) | covered | a12 8–186 |
| 6.5 Comandos do Prompt de Comando | **partial** | a12 122 (1 pág.) |
| 7.1 Word 2019 | covered | a08 6–108 |
| 7.2 Excel 2019 | covered | a06 10–181 |
| 7.3 PowerPoint 2019 | covered | a10 5–66 |
| 7.4 Writer 7 | covered | a09 6–73 |
| 7.5 Calc 7 | **partial** | a07 7–64 (sem gráficos, filtros, formatação condicional) |
| 7.6 Impress 7 | covered (enxuto) | a11 6–26 |
| Exportação de arquivos (PDF etc.) | covered | a08 31–41; a06 40–47; a10 26–32; a09 20–27; a07 12; a11 19 |

**Fora do edital?** Não há aula de Linux, Outlook ou Office 365. Esses nomes só aparecem em menções e comparações. Há seções "Novidades" de outras versões e do Microsoft 365 em a06 (13–19), a08 (9–20) e a10 (8–15), de incidência baixa. O edital fixa a versão 2019, mas mantive essas seções por serem curtas.

## Achados da auditoria inversa

O detalhe está em `content/edital/informatica.json` → `inverse`.

- **Indexada no lugar errado**: sumários e apresentações como teoria em 13 aulas (corrigido).
- **Subindexada**: Vírus (a03), criptografia assimétrica (a02), memórias e CPU (a14), referências (a06) — corrigido.
- **Superfragmentada**: falsos subtítulos de legenda em a00 e a14 (corrigido).
- **Conteúdo complementar**: Glossário (a00 57–59, agora S), OSI (a00 27–29), Azure e ferramentas colaborativas (a13 39–52), funções financeiras e VBA (a06 163–177).
- **Possível fora do escopo** (mantido, baixa prioridade):
  - Novidades de outras versões do Office.
  - Conversão de base (a14 7–13).
  - Barramentos legados (a14 54–68).
  - Jogos, Regedit, Sandbox, partição, sistemas de arquivos, BitLocker e AppData (a12).
- **Necessita revisão humana**:
  - a12 122: lista DELTREE como comando do Prompt, mas ele não existe no Windows 11.
  - a12 161–162: o WordPad foi removido do Windows 11 a partir do 24H2.
- **Questões dentro da teoria**: todas as aulas intercalam questões com comentário no texto teórico. Mantive essas páginas como T: o comentário faz parte da explicação, e separá-las quebraria os tópicos.

## Lacunas e complementos

`gaps.json` não registra lacunas de Informática e não existe complemento `cNN` da disciplina. A auditoria encontrou **lacunas reais parciais** (não criei complementos):

1. **Navegadores (item 2)**: falta o uso prático. Navegação privativa, histórico, downloads, favoritos, cookies e cache, extensões, bloqueio de pop-ups, sincronização e atalhos comuns do Chrome/Edge/Firefox. Também faltam ferramentas de busca (operadores). É tema frequente na AOCP.
2. **Prompt de Comando (item 6)**: só uma tabela de 11 comandos de arquivo, sem parâmetros. Faltam ipconfig, ping, tracert, nslookup, tasklist/taskkill, chkdsk, sfc, shutdown, cls, type, attrib, help e curingas (* ?). O DELTREE está errado (no Windows 11 é RD /S).
3. **Instalação e configuração de periféricos (item 5)**: faltam drivers, plug and play, Gerenciador de Dispositivos, impressora padrão e fila de impressão. O material só menciona esses pontos.
4. **Calc (item 7)**: gráficos, classificar/filtrar (AutoFiltro), formatação condicional e tabela dinâmica no Calc. Prioridade menor, porque os conceitos estão no Excel (a06 137–151).

## Pendências

- Decidir se o fator de densidade de Informática deve cair (ver pedidos). Isso muda o número de trechos (~109 → ~85–90).
- Validar se as partes de incidência baixíssima do Windows e do Hardware devem virar "Aprofundamento". Hoje não há como marcar uma faixa de páginas dentro da aula como opcional pelo override.
- Revisão humana: DELTREE (a12 p.122) e WordPad (a12 161–162).
- a02 s08 começa com o rótulo "Brasil)". O subtítulo do índice "Infraestrutura de Chave Pública (ICP-Brasil)" vem quebrado em duas linhas; é só cosmético.

## Pedidos ao orquestrador

1. **Detecção de sumário (pipeline)**: `tocMax` fica em 2 para todo o material de Informática. O regex `FRONTMATTER` não reconhece "T ÓPICOS DA / A ULA" (letra separada pela capitular), "Sumário" na p.3 nem "Nessa aula, nós veremos…". Corrigi via override, mas outras disciplinas do mesmo professor/formato podem ter o mesmo erro.
2. **`DENSITY_FACTOR["informatica"]`**: sugiro baixar de 1,25 para 1,0. O texto é descritivo, não matemático; hoje resulta em ~8 págs./h nas aulas de prosa. Com 1,0, os trechos ficariam com ~10–13 págs. e cerca de 20% menos horas de Teoria. Se aceito, os cortes deste override continuam válidos (todos ficam em inícios de seção).
3. **Complementos sugeridos** (decisão do orquestrador): (a) "Navegadores e ferramentas de busca"; (b) "Prompt de Comando e periféricos no Windows 11" (comandos com parâmetros, drivers/plug and play/Gerenciador de Dispositivos/impressoras). Opcional: (c) "Calc: gráficos, filtros e formatação condicional".
4. Se for desejável, criar no override um mecanismo para marcar faixas de páginas como "aprofundamento" dentro de uma aula (ex.: a06 163–177, a12 178–185, a14 54–68).
