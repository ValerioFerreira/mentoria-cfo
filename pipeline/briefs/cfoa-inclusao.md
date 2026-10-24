# Briefing: inclusão do concurso "2º Tenente CFOA CBMPE" na plataforma MentorIA

> Você é o agente responsável por **incluir um concurso novo, de ponta a ponta**, no repositório
> `C:\Users\Administrador\Documents\Projetos\CFO-BM`. Este documento é a sua especificação. Ele foi escrito para **não deixar
> decisões ao seu critério**: quando uma regra daqui resolver a questão, siga a regra; quando nada aqui resolver, **pare e pergunte
> ao dono** (não invente). A única parte que fica de fora é a **importação das questões reais do TecConcursos**, que o dono vai
> baixar depois (seção 13 diz como deixar tudo pronto para ela).

---

## 0. Antes de tudo (obrigatório)

1. Leia, inteiros: `CLAUDE.md`, `COLABORADORES.md`, `HISTORICO.md` (sobretudo "Inclusão do PCPE", seções 0 a 12: é o precedente
   que você vai repetir), `web/AGENTS.md`, `pipeline/briefs/bizu.md`, `pipeline/briefs/summary.md`, `pipeline/briefs/complement.md`,
   `pipeline/briefs/ineditas-cbmpe.md`, `pipeline/briefs/ineditas-cbmpe2.md` e `pipeline/questoes/EXTRACAO.md`.
2. Ambiente: Windows. Python sempre por `pipeline/.venv/Scripts/python` com `PYTHONIOENCODING=utf-8`. Arquivos grandes: ferramenta
   **Write** (heredoc longo no Bash quebra). Banco de desenvolvimento: `npx prisma dev -n cfo-bm -d` (em `web/`); leia a memória do
   projeto sobre o PGlite (cai com muitas conexões; `migrate` pode mirar o schema errado: confira `search_path`).
3. Git:
   - Trabalhe na branch **`cfoa`** (já existe e está à frente da `main` com o commit `6c13e84`). **Não reescreva histórico**
     (nada de `reset`, `rebase`, `--amend`, `push --force`). Corrija com commits novos.
   - A árvore de trabalho tem **alterações não commitadas de outra frente** (usuário de teste): `web/src/app/(app)/layout.tsx`,
     `web/src/app/(public)/pagamentos/contratacao/[id]/page.tsx`, `web/src/app/(public)/pagamentos/page.tsx`,
     `web/src/lib/plan/initial-status.ts`, `web/src/lib/plan/persist.ts` e os arquivos novos `web/scripts/create-test-user.ts`,
     `web/src/lib/test-user*.ts`. **Não as reverta, não as commite e não as inclua nos seus commits.** Se você precisar alterar
     `initial-status.ts` (seção 8.9), grave só o seu trecho no índice com um patch não interativo
     (`git diff web/src/lib/plan/initial-status.ts > x.patch`, edite o patch para conter só o seu hunk, `git apply --cached x.patch`).
     Outros arquivos não rastreados da raiz (`PCPE-*`, `extract_batch.py`, `scratch/`, zips em `resumos-colaboradores/entregas/`) não
     são seus: não os toque.
   - Faça **um commit por fase** (seções 3 a 12), mensagem em português no estilo do repositório (`feat(cfoa): ...`,
     `fix(cfoa): ...`), terminando com a linha de coautoria que o seu ambiente indicar.
   - **Proibido sem autorização escrita do dono nesta conversa:** `git push`, merge na `main`, qualquer comando com `--remoto`,
     `migrate deploy` na produção, escrita no Neon/Vercel, `migrate reset`. A seção 14 diz como pedir.
4. **Material protegido.** `docs/` tem marca d'água com nome/CPF do aluno: nunca versione, publique nem copie texto verbatim de
   `docs/` ou `pipeline/.cache/pages` para `content/`. Bizus, resumos, complementos e inéditas são **autorais/parafraseados** e
   passam pelos validadores de originalidade.
5. **Neutralidade.** Interface, títulos, bizus, resumos, questões e PDFs não citam o provedor do material, professores, "equipe",
   "Somente PDF" nem "Aula NN"/páginas. Só a Diretriz da atividade (`lib/directive.ts`) diz "aula X, págs. Y a Z".

---

## 1. O concurso

| Campo | Valor (fixo, não altere) |
|---|---|
| Nome exibido | **2º Tenente CFOA CBMPE** |
| Chave (`enum Contest`) | `CBMPE_CFOA` |
| Slug (URL) | `cbmpe-cfoa` (`/lista-de-espera/cbmpe-cfoa`) |
| `org` / `role` / `category` em `CONTESTS` | `"CBMPE"` / `"2º Tenente CFOA"` / `"Oficial"` |
| `CONTEST_SUBTITLES` | `"2º TENENTE CFOA - CBMPE"` |
| Imagem do card | `/images/CBMPE.webp`, `imagePosition: "center 70%"` |
| Categoria de preço (`ContestSetting.category`) | `OFICIAL` (R$ 120; lançamento R$ 90; cupom de parceiro R$ 72), sem `priceCents`/`siteDiscountPoints` próprios |
| Data da prova (`ContestSetting.examDate`) | **vazia (NULL)**: o concurso ainda não foi lançado |
| Banca | **não definida** (tratamento genérico, seção 8.6) |
| Base | Edital da Seleção Interna CFOA BM/2023 (Portaria Administrativa nº 1/2022 – CBMPE – DEIP), Anexo X |
| Pacote do material (`CONTEST_PACKAGES`) | **não acrescente** entrada (não há pacote único); ver 8.1 |
| Combo | nenhum |
| `available` | `false` durante o trabalho; `true` só no fim (seção 12) |

**Contexto do edital (para os textos e o simulado, não para a interface de venda):** seleção interna para o Curso de Formação de
Oficiais da Administração; 70 vagas (35 por antiguidade, sem prova; 35 por merecimento, com prova). O **Exame Intelectual** tem
**100 questões objetivas de múltipla escolha, 5 alternativas (A–E), 1 ponto cada, 5 horas (300 min)**. Reprovado quem fizer
**menos de 50 pontos** no total **ou zerar qualquer disciplina**. Não há mínimo por bloco.

Os PDFs do edital estão em `C:\Users\Administrador\Downloads\`:
`EDITAL CFOA 2023 - CBMPE_Portaria_Administrativa.pdf` e `CONTEÚDO PROGRAMÁTICO EDITAL CFOA 2023.pdf` (o nome tem "Ú"; use glob
`*CFOA 2023*.pdf`). Copie-os para `docs/edital-cfoa-2023.pdf` e `docs/edital-cfoa-2023-conteudo.pdf` (`docs/` é ignorado pelo git)
e grave o texto extraído em `pipeline/.cache/edital_cfoa.txt` (pymupdf). Ele é a fonte dos itens; a lista da seção 2 já é a
transcrição normalizada que você deve usar.

### 1.1 Distribuição da prova (Anexo da Portaria, item 4.1.2.1)

| Bloco | Disciplina (id no catálogo) | Questões |
|---|---|---|
| I – Direito (50) | Direito Penal Militar (`direito-penal-militar`) | 10 |
| | Direito Constitucional (`direito-constitucional`) | 10 |
| | Direito Administrativo (`direito-administrativo`) | 15 |
| | Direitos Humanos (`direitos-humanos`) | 5 |
| | Direito Processual Penal Militar (`direito-processual-penal-militar`) | 10 |
| II – Conhecimentos Gerais (50) | Noções de Administração (`administracao`) | 10 |
| | Raciocínio Lógico (`raciocinio-logico`) | 5 |
| | Legislação Extravagante (`legislacoes-pe`) | 15 |
| | Língua Portuguesa (`lingua-portuguesa`) | 20 |

São **9 disciplinas**. Não há Informática nem língua estrangeira. `CONTEST_SUBJECTS.CBMPE_CFOA` = exatamente estes 9 ids, nesta
ordem.

---

## 2. Itens do edital (códigos e títulos FIXOS)

Use exatamente estes códigos (`id`) e títulos (`item`) nos mapas da seção 5. Não junte, não divida, não renomeie.

### Direito Penal Militar (`content/edital/cfoa/direito-penal-militar.json`)
- `1.1` Aplicação da lei penal militar: princípio da legalidade
- `1.2` Crimes militares em tempo de paz (art. 9º do CPM)
- `1.3` Equiparação a militar da ativa; militar da reserva ou reformado; pessoa considerada militar
- `1.4` Equiparação a comandante; conceito de superior
- `2.1` Do crime: coação irresistível; coação física ou material
- `2.2` Do crime: obediência hierárquica
- `2.3` Exclusão de crime
- `3` Crimes contra a autoridade ou disciplina militar
- `4` Crimes contra o serviço militar e o dever militar
- `5` Crimes contra a administração militar
- `6` Crimes militares por extensão (art. 9º, II, do CPM, com a redação da Lei 13.491/2017)
- `6.1` Crimes em licitações e contratos (Lei 8.666/1993, hoje arts. 337-E a 337-P do Código Penal, pela Lei 14.133/2021)
- `6.2` Lei 13.869/2019: crimes de abuso de autoridade
- `6.3` Lei 7.716/1989: crimes resultantes de preconceito de raça ou de cor

### Direito Constitucional (`content/edital/cfoa/direito-constitucional.json`)
- `1.1` Direitos e deveres individuais e coletivos
- `1.2` Direitos políticos
- `2.1` Administração pública: disposições gerais
- `2.2` Militares dos Estados, do Distrito Federal e dos Territórios
- `3` Poder Judiciário: Tribunais e Juízes dos Estados
- `4.1` Defesa do Estado: Forças Armadas
- `4.2` Defesa do Estado: segurança pública

### Direito Administrativo (`content/edital/cfoa/direito-administrativo.json`)
- `1.1` Conceituação, princípios informativos, fontes e interpretação
- `1.2` Poderes e deveres do administrador público; uso e abuso de poder
- `1.3` Administração direta e indireta
- `1.4` Direitos e deveres do administrador e do servidor
- `1.5` Requisição administrativa
- `2.1` Administração Pública: estrutura
- `2.2` Responsabilidade civil do Estado
- `2.3` Delegação de competência
- `2.4` Tribunal de Contas da União e dos Estados
- `3.1` Poderes administrativos: vinculado, discricionário, hierárquico e disciplinar
- `3.2` Servidores públicos: remuneração e proteção social
- `3.3` Regime disciplinar
- `3.4` Processo administrativo estadual
- `4.1` Atividade administrativa: princípios básicos
- `4.2` Poder de polícia
- `4.3` Serviços públicos
- `5.1` Polícia administrativa: definição, limites, ramos e setores
- `5.2` Execução, inexecução e revogação do contrato administrativo
- `5.3` Bens públicos: classificação e atributos
- `6.1` Atos administrativos: conceito, requisitos e atributos
- `6.2` Atos administrativos: classificação e espécies
- `6.3` Atos administrativos: anulação e revogação
- `6.4` Contratos administrativos: conceito, peculiaridades, formalização e regime jurídico
- `7` Princípios da administração pública militar (legalidade, impessoalidade, moralidade, publicidade, eficiência, supremacia do interesse público, presunção de legitimidade e veracidade, autotutela, continuidade, motivação, razoabilidade e proporcionalidade, segurança jurídica, boa-fé, hierarquia)
- `8` Decreto Estadual 3.639/1975: Conselho de Disciplina
- `9` Lei 5.836/1972: Conselho de Justificação
- `10.1` Licitações (Lei 14.133/2021): modalidades licitatórias
- `10.2` Lei 14.133/2021: sistema de registro de preços
- `10.3` Lei 14.133/2021: segregação de funções
- `10.4` Lei 14.133/2021: procedimento de manifestação de interesse
- `10.5` Lei 14.133/2021: sistema de rating
- `10.6` Lei 14.133/2021: contratação compartilhada
- `10.7` Lei 14.133/2021: reajuste de preços

### Direitos Humanos (`content/edital/direitos-humanos.json`, mapa padrão da disciplina)
- `1.1` Fundamentos históricos dos Direitos Humanos
- `1.2` Conceito de Direitos Humanos, cidadania e democracia
- `1.3` Declaração Universal dos Direitos Humanos
- `2` Convenção sobre a Eliminação de Todas as Formas de Discriminação contra a Mulher
- `3` Convenção Internacional sobre os Direitos das Pessoas com Deficiência
- `4` A legislação e os Direitos Humanos no Brasil

### Direito Processual Penal Militar (`content/edital/direito-processual-penal-militar.json`, mapa padrão)
- `1.1` Lei de processo penal militar e sua aplicação
- `1.2` Prerrogativas do posto ou da função
- `1.3` Medidas preventivas e assecuratórias
- `1.4` Comparecimento espontâneo do indiciado ou acusado
- `1.5` Qualificação e interrogatório do acusado
- `1.6` Acareação
- `1.7` Documentos e indícios
- `2.1` Polícia judiciária militar
- `2.2` Inquérito policial militar
- `2.3` Auto de prisão em flagrante delito
- `2.4` Instrução provisória de deserção
- `2.5` Providências que recaem sobre coisas ou pessoas
- `2.6` Incidente de insanidade mental
- `2.7` Menagem (o edital grafa "mensagem"; o instituto do CPPM é a menagem, arts. 263 a 269)
- `2.8` Confissão
- `2.9` Perícias e exames
- `3.1` Prisão provisória
- `3.2` Prisão em flagrante
- `3.3` Prisão preventiva

### Noções de Administração (`content/edital/administracao.json`, mapa padrão)
- `1.1` Teorias clássicas da Administração
- `1.2` O ambiente externo e a organização
- `1.3` Organização formal: a organização burocrática
- `1.4` Abordagem mecanicista de administração
- `1.5` Estruturas organizacionais (tradicionais e inovadoras)
- `1.6` Abordagens recentes em administração
- `1.7` Autoridade e responsabilidade
- `1.8` Conceito de linha e assessoria
- `1.9` Direção: conceito e princípios de administração aplicados à direção
- `1.10` Processo decisório
- `1.11` Controle: elementos e princípios gerais aplicados ao controle
- `1.12` Mudança organizacional
- `1.13` Cultura organizacional

### Raciocínio Lógico (`content/edital/cfoa/raciocinio-logico.json`)
- `1` Compreensão de estruturas lógicas
- `2.1` Lógica de argumentação: analogias
- `2.2` Lógica de argumentação: inferências, deduções e conclusões
- `3` Diagramas lógicos
- `4.1` Princípios da contagem
- `4.2` Probabilidade

### Legislação Extravagante (`content/edital/cfoa/legislacoes-pe.json`)
- `1` Lei 11.817/2000: Código Disciplinar dos Militares do Estado de Pernambuco
- `2` Lei 6.783/1974: Estatuto dos Militares do Estado de Pernambuco
- `3` Decreto 22.114/2000: Regulamento de Ética dos Militares do Estado de Pernambuco
- `4` Lei Complementar 470/2021: promoção dos militares do Estado de Pernambuco
- `5` Lei 11.781/2000: processo administrativo no âmbito da Administração Pública de Pernambuco
- `6` Lei 8.429/1992: improbidade administrativa
- `7` Lei 12.527/2011: acesso à informação
- `8` Lei Estadual 13.314/2007: assédio moral na Administração Pública de Pernambuco
- `9` Portaria SDS 395/2015: instruções para a sindicância dos militares estaduais de Pernambuco
- `10` Provimento Correicional 21/2021: investigação preliminar (servidores civis e militares sob a Lei 11.929/2001)

### Língua Portuguesa (`content/edital/cfoa/lingua-portuguesa.json`)
- `1` Compreensão e interpretação de textos
- `2` Tipologia textual
- `3` Ortografia oficial
- `4` Acentuação gráfica
- `5` Emprego das classes de palavras
- `6` Emprego do sinal indicativo de crase
- `7` Sintaxe da oração e do período
- `8` Pontuação
- `9` Concordância nominal e verbal
- `10` Regência nominal e verbal
- `11` Significação das palavras
- `12` Redação de correspondências oficiais

---

## 3. Fase A — Revisar e corrigir o commit `6c13e84`

O commit `6c13e84` ("feat(cfoa): adiciona disciplinas e aulas do CFOA...") foi feito fora das convenções e tem erros conhecidos.
Trate o conteúdo dele como **provisório**:

1. **`content/contests.json` foi editado à mão** e está errado (60 questões, Informática 10, sem Raciocínio Lógico). Ele só pode ser
   gerado por `npx tsx web/scripts/export-contests.ts` (seção 8.4). Não edite à mão.
2. **Estrutura e trechos das 3 disciplinas novas vieram de um script avulso** (`tools/estrategia-downloader/build_cfoa_structure.py`),
   não do `pipeline/segment.py` + `content/overrides/`. Há tópicos ilegíveis (ex.: `"6. Discricionariedadedasinvestigações🡪OIPM..."`),
   rótulos de "Apresentação"/"Recurso" como tópicos e títulos de arquivo crus. **Refaça pelo pipeline oficial** (seção 4) e então
   **apague** `tools/estrategia-downloader/build_cfoa_structure.py` e `web/scripts/verify_cfoa_db.ts` (`git rm`).
3. **Os mapas do edital** `content/edital/{administracao,direitos-humanos,direito-processual-penal-militar}.json` só repetem os títulos
   das aulas, todos "covered". **Substitua** pelos mapas da seção 5, com os itens da seção 2.
4. Mantenha o que estiver certo: `subjects.json` (ids, nomes, `folderPrefix` 49/50/26), a limpeza de caracteres bidi e o rodapé
   `CBM-[A-Z]{2}` em `pipeline/extract.py`, e o filtro `contest in Contest` em `seedImportance` (`seed-structure.ts`).
5. Os ids de trecho das 3 disciplinas novas **podem mudar** nesta fase (nada de bizu, resumo ou questão depende deles ainda; confira
   com `rg -l "administracao/a|direitos-humanos/a|direito-processual-penal-militar/a" content/items content/summaries content/questoes`
   que não há nada; se houver, apague esses arquivos, porque foram feitos sobre a segmentação errada).

Commit: `fix(cfoa): refaz a estrutura das disciplinas novas pelo pipeline e remove o script avulso`.

---

## 4. Fase B — Estrutura e segmentação

### 4.1 Disciplinas novas (pastas inteiras)
- `docs/49 - CBM-PE (CFOA) Noções de Administração` → `administracao` (11 PDFs, aulas `a00`–`a10`)
- `docs/50 - CBM-PE (CFOA) Direitos Humanos` → `direitos-humanos` (6 PDFs, `a00`–`a05`)
- `docs/26 - PM-PE (Oficial) Direito Processual Penal Militar` → `direito-processual-penal-militar` (14 PDFs, `a00`–`a13`)

Rode, nesta ordem: `extract.py --only 49` (e 50, 26; `--force` se o cache tiver sido gerado pelo script avulso), `headings.py`,
`index_validate.py`, `segment.py --subject <disc>`, `build_catalog.py`, `build_complements.py`. As três não estão no índice `.xlsx`:
o `segment.py` usa os subtítulos de `headings.py` (`auto_headings`) e os `content/overrides/<disc>.json`.

Para **cada aula** das três disciplinas, abra o mapa com `inspect_aula.py <disc>/aNN --heads` e `--pages` e grave em
`content/overrides/<disc>.json` (formato de `content/overrides/direito-constitucional.json`):
- `title`: título neutro em pt-BR, sem "Apresentação do curso", nome de professor, "Parte I" só se houver Parte II;
- `pages`: tipos de página corretos (T teoria, C questões comentadas, L lista, K gabarito, S resumo, F capa/sumário, B branco,
  **EXTRA** para fora do edital do CFOA, duplicado ou opcional);
- `headings` e `dropHeadings`: tópicos com nomes reais do conteúdo (corrija os colados/ilegíveis; descarte "Apresentação",
  "Recurso", "Considerações finais", nomes de professor);
- `cuts`: só se o corte automático cair no meio de um tópico;
- `edital`: `"yes"`, `"partial"` ou `"no"` pela regra da 4.3;
- `note`: uma linha quando algo for incomum.

Regras de trecho (CLAUDE.md): Teoria 10–17 págs. (teto 17), cortes em início de tópico; aula com menos de 8 págs. de teoria pode ser
1 trecho só. Nenhum trecho pode passar de 17 págs. (`segment.py` sai com código 1 se passar).

### 4.2 Aulas novas em disciplinas existentes (material do Estratégia que já está em `docs/`)
Acrescente em `PDF_TARGET_OVERRIDES` (`pipeline/config.py`), com comentário no padrão dos existentes:
```python
# docs/39 -> Leis penais do edital do CFOA como crimes militares por extensão (Direito Penal Militar, só CBMPE_CFOA)
"39_004": ("direito-penal-militar", 20),  # Lei 13.869/2019 - Abuso de Autoridade
"39_007": ("direito-penal-militar", 21),  # Lei 7.716/1989 - Preconceito de Raça ou de Cor
```
e marque **todas as outras** chaves de `docs/39` como `None` (`"39_001": None`, ..., `"39_010": None`, exceto 004 e 007), para que
nada mais da pasta entre. Em `content/overrides/direito-penal-militar.json`, `direito-penal-militar/a20` e `a21` recebem
`"onlyContests": ["CBMPE_CFOA"]`, `title` neutro ("Lei 13.869/2019: crimes de abuso de autoridade" e "Lei 7.716/1989: crimes de
preconceito de raça ou de cor") e a mesma auditoria de páginas da 4.1. Não use `docs/30` (já é `legislacao-penal-especial` do PCPE).

### 4.3 Elegibilidade das aulas para o CFOA (regra única, sem exceções)
Para **cada aula selecionável** das 9 disciplinas (inclusive complementos `cNN` existentes):
- A aula **vale para o CFOA** se o mapa da seção 5 a cita em `where` de algum item (inclusive como `elsewhere`, 5.3).
- Se a aula **não é citada**:
  - disciplina nova (as 3 da 4.1): `"edital": "no"` no override (ela só existe para o CFOA);
  - disciplina compartilhada: acrescente `"CBMPE_CFOA"` a `excludeContests` da aula no `content/overrides/<disc>.json`
    (aula com `onlyContests` de outro concurso já não vale: não mexa nela).
- Aula com `onlyContests: ["PCPE_AGENTE"]` que o mapa do CFOA cite (ex.: `lingua-portuguesa/a13` Redação Oficial,
  `direito-administrativo/a20`–`a24` de licitações e Lei 11.781): mude para `["PCPE_AGENTE", "CBMPE_CFOA"]`.
- Dentro de uma aula que vale, páginas de teoria que só tratam de assunto fora do edital do CFOA **não** viram `EXTRA` se a aula
  também serve a outro concurso (mudaria o plano dele); só nas 3 disciplinas novas use `EXTRA` para isso.

### 4.4 Testes de estrutura
Atualize `pipeline/tests/test_content.py` (contagem de aulas base) com o número real e o comentário somando as parcelas.
`pipeline/.venv/Scripts/python -m pytest pipeline/tests -q`: nenhuma falha **nova** (anote as 5 falhas antigas conhecidas do
`HISTORICO.md` 10.4 e compare).

Commit: `feat(cfoa): estrutura e trechos das disciplinas novas e aulas do CFOA`.

---

## 5. Fase C — Mapa edital → material

### 5.1 Arquivos
- Disciplinas novas: o mapa padrão `content/edital/<disc>.json` (`{"subject": ..., "items": [...]}`) **é** o mapa do CFOA.
- Disciplinas compartilhadas (`direito-penal-militar`, `direito-constitucional`, `direito-administrativo`, `raciocinio-logico`,
  `legislacoes-pe`, `lingua-portuguesa`): mapa próprio em `content/edital/cfoa/<disc>.json`
  (`{"subject": ..., "contest": "CBMPE_CFOA", "items": [...]}`), **sem tocar** nos mapas padrão nem nos de `content/edital/pcpe/`.
- Gere todos por um script versionado `pipeline/cfoa_tools/build_edital_cfoa.py`, cópia adaptada de
  `pipeline/pcpe_tools/build_edital_pcpe.py` (troque `CONTEST`, a pasta de saída, a validade da aula e a lista de itens; para as 3
  disciplinas novas, escreva em `content/edital/<disc>.json`). Os `where` só podem apontar para **trechos reais** de
  `content/segments` (o script calcula páginas impressas e ids; nunca escreva página ou id à mão: foi o erro do mapa do PCPE
  corrigido na Rodada 6).
- Rode `pipeline/edital_map.py` depois e confira o resumo de cobertura.

### 5.2 Como localizar cada item
Para cada item da seção 2, procure no material com `inspect_aula.py <disc>/aNN --grep "<termo>"` e `--heads` (em todas as aulas da
disciplina, inclusive as que hoje não valem para outros concursos). Registre em `where` **todas** as aulas/trechos que ensinam o
item (teoria; não use só questões comentadas). Status:
- `covered`: o material ensina o item;
- `partial`: ensina parte; escreva em `notes` o que falta (e trate a parte que falta pela 6.1);
- `complement`: resolvido por complemento MentorIA (6.1);
- `elsewhere`: ensinado em outra disciplina (5.3);
- `gap`: sem material e sem complemento possível (só quando a 6.2 mandar).

### 5.3 Itens tratados em outra disciplina (fixo)
O seed só liga um item a aulas da própria disciplina. Estes itens ficam `elsewhere` com `where` apontando para a disciplina real, e a
aula citada passa a valer para o CFOA (4.3):
- Leg. Extravagante `5` (Lei 11.781/2000) → `direito-administrativo` (aula da Lei 11.781, hoje `a23` do PCPE);
- Leg. Extravagante `6` (Lei 8.429/1992) → `direito-administrativo` (aula de improbidade);
- Dir. Administrativo `2.4` (Tribunais de Contas) → `direito-constitucional`, **só se** `direito-administrativo` não ensinar
  (verifique primeiro; se ensinar, é `covered` lá).
Nenhum outro item pode ficar `elsewhere`.

Commit: `feat(cfoa): mapa do edital do CFOA para as 9 disciplinas`.

---

## 6. Fase D — Lacunas e materiais complementares

### 6.1 Regra
Todo item `partial` (na parte que falta) ou sem material vira **complemento MentorIA** (`content/complements/<id>.md`, briefing
`pipeline/briefs/complement.md`), com `onlyContests: "CBMPE_CFOA"` no front matter (como `da-lei-9784.md`), e uma lacuna em
`content/gaps.json` (`id` com prefixo `cfoa-`, `subject`, `item`, `evidence`, `severity`, `remedy`, `resolved: true`,
`resolution`). Antes de escrever, confirme por `inspect_aula.py --grep` em **todas** as aulas da disciplina que o assunto não está no
material (se estiver, mapeie; não escreva).

### 6.2 Complementos previstos (ids, disciplina e ordem fixos; `order` = próximo número livre da disciplina, na ordem abaixo)
| id | disciplina | conteúdo | itens |
|---|---|---|---|
| `dpm-crimes-licitacoes` | direito-penal-militar | crimes em licitações e contratos (arts. 337-E a 337-P do CP), com a revogação dos arts. 89–99 da Lei 8.666 pela Lei 14.133 e o enquadramento como crime militar por extensão | 6.1 |
| `dh-cedaw` | direitos-humanos | Convenção sobre a Eliminação de Todas as Formas de Discriminação contra a Mulher (Decreto 4.377/2002) e Protocolo Facultativo | 2 |
| `dh-convencao-pcd` | direitos-humanos | Convenção sobre os Direitos das Pessoas com Deficiência (Decreto 6.949/2009, status de emenda constitucional) | 3 |
| `da-conselhos-disciplina-justificacao` | direito-administrativo | Decreto Estadual 3.639/1975 (Conselho de Disciplina) e Lei 5.836/1972 (Conselho de Justificação) | 8, 9 |
| `leg-pe-dec-22114-etica` | legislacoes-pe | Decreto 22.114/2000 | 3 |
| `leg-pe-lc-470-promocao` | legislacoes-pe | Lei Complementar 470/2021 | 4 |
| `leg-lei-12527-lai` | legislacoes-pe | Lei 12.527/2011 | 7 |
| `leg-pe-lei-13314-assedio` | legislacoes-pe | Lei Estadual 13.314/2007 e alterações | 8 |
| `leg-pe-port-395-sindicancia` | legislacoes-pe | Portaria SDS 395/2015 | 9 |
| `leg-pe-prov-21-investigacao` | legislacoes-pe | Provimento Correicional 21/2021 (e Lei 11.929/2001 no que ele aplica) | 10 |

Complementos **condicionais** (só se a 6.1 confirmar que falta), com estes ids: `da-cfoa-lacunas` (o que faltar entre 1.4, 1.5, 2.3,
3.2, 5.3, 10.3, 10.5, 10.6 de Dir. Administrativo, uma seção `##` por item), `adm-cfoa-lacunas` (Noções de Administração),
`dppm-cfoa-lacunas` (DPPM, inclusive 2.7 menagem e 2.4 deserção se o material não tiver), `dh-legislacao-brasil` (DH 4),
`rl-analogias` (RL 2.1), `dc-cfoa-lacunas`, `lp-cfoa-lacunas`.

### 6.3 Exatidão das normas
- Só escreva dispositivos que você **leu no texto oficial** (planalto.gov.br, legis.alepe.pe.gov.br, diário oficial de PE, site da
  SDS-PE/Corregedoria). Registre URL e data da consulta em `## Fontes`.
- **Se o texto oficial de uma norma não for encontrado** (provável para a Portaria SDS 395/2015 e o Provimento 21/2021): não escreva
  de memória. Deixe o item `gap`, a lacuna com `resolved: false` e `remedy: "dono fornecer o texto oficial"`, e liste no relatório
  final. Os itens 10.5 (rating) e 10.6 (contratação compartilhada) de Dir. Administrativo seguem a mesma regra: se não achar
  dispositivo na Lei 14.133/2021 ou em regulamento federal oficial, `gap` com nota, sem inventar.
- Complementos não citam o material-base ("o curso principal", "Aula NN": pendência conhecida, não repita).
- Gere cada PDF com `build_complements.py --only <id> --no-merge`; ao fim de todos, uma vez `build_complements.py` (com merge),
  depois de `segment.py`/`build_catalog.py`.

Commit: `feat(cfoa): complementos das lacunas do edital do CFOA`.

---

## 7. Fase E — Importância e pesos

1. `npx tsx web/scripts/export-contests.ts` (depois da seção 8.1–8.3) para regenerar `content/contests.json`. Confira que
   `CBMPE_CFOA` tem `totalQuestions: 100`, os 9 `subjects` e o `exam` da 1.1. Não acrescente `note`.
2. `pipeline/importance.py`. Confira: toda disciplina do CFOA tem trechos `appears: true` (o teste
   `test_all_exam_subjects_have_appearing_segments` deve cobrir o CFOA) e nenhum trecho de aula fora do mapa aparece para o CFOA.
3. **Zero divergência nos concursos existentes** (bloqueante):
   - `pipeline/compare_importance_main.py`: 0 discrepâncias nos trechos dos concursos que já existiam;
   - `npx tsx web/scripts/compare-plans-main.ts`: 0 divergências nos 96 cenários;
   - `npx tsx web/scripts/plan-snapshot.ts` antes (na `main`, numa worktree temporária) e depois: idênticos para os 5 concursos
     individuais. Não acrescente o CFOA à lista desse script (ele é a rede de segurança dos existentes).
   - Se houver divergência por causa da fatia das aulas `onlyContests` em `pipeline/build_catalog.py`/`build_complements.py` (as aulas
     exclusivas de todos os concursos são somadas numa fatia só, então as do CFOA em `direito-administrativo` e `lingua-portuguesa`
     mudariam a fatia do PCPE), corrija o cálculo para que a fatia exclusiva seja **por concurso** e repita as três verificações.
     Não aceite divergência "pequena".
4. Espelhe em `web/content` (`apply_synthetic.py` faz o espelho de summaries/importance/contests; para catalog/structure/segments/
   edital/complements, siga o que o PCPE fez: `pipeline/pcpe_tools/mirror_web.py` como modelo, incluindo `content/edital/cfoa/`).

---

## 8. Fase F — Código da aplicação (web/)

Leia `web/node_modules/next/dist/docs/` antes de mexer em rotas. `cacheComponents` desligado. Sem `Date.now()` no render.

### 8.1 `web/src/lib/contests.ts`
- `CONTESTS`: entrada da seção 1, logo depois de `cbmpe-oficial` (o card fica na linha da corporação CBMPE), `available: false`.
- `CONTEST_SUBTITLES.CBMPE_CFOA = "2º TENENTE CFOA - CBMPE"`.
- `BASE_CONTEST_SUBJECTS.CBMPE_CFOA` = os 9 ids da seção 1.1, na ordem da tabela.
- `CONTEST_PACKAGES`: sem entrada. Confirme que `packageFor("CBMPE_CFOA", ...)` devolvendo `undefined` não quebra a Diretriz nem
  nenhuma tela; se quebrar, faça o código tratar `undefined` (não invente pacote).

### 8.2 Prisma (`web/prisma/schema.prisma` + migrações)
- `enum Contest`: `CBMPE_CFOA // CBMPE · 2º Tenente CFOA (Oficiais da Administração)`.
- Duas migrações, como no combo (valor de enum não pode ser usado na mesma transação):
  `20261024120000_cfoa_enum` (`ALTER TYPE "Contest" ADD VALUE IF NOT EXISTS 'CBMPE_CFOA';`) e
  `20261024120100_cfoa_settings` (`INSERT INTO "ContestSetting" ("contest","category","examDate","updatedAt") VALUES ('CBMPE_CFOA','OFICIAL',NULL,NOW()) ON CONFLICT ("contest") DO UPDATE SET "category" = COALESCE("ContestSetting"."category", EXCLUDED."category");`
  com comentário explicando que a data fica vazia até sair o edital).
- Gere com `prisma migrate diff` + aplique com `npx prisma migrate deploy` **no banco local**; `npx prisma generate`. Prisma pinado em
  `7.10.0`.

### 8.3 `web/src/lib/simulado-rules.ts`
Acrescente `"CBMPE_CFOA"` a `SupportedSimuladoContest` e:
```ts
CBMPE_CFOA: {
  contest: "CBMPE_CFOA",
  title: "CBMPE — 2º Tenente CFOA (Oficiais da Administração)",
  role: "Oficial CFOA",
  durationMinutes: 300, // 5h00min
  durationSeconds: 300 * 60,
  totalQuestions: 100,
  minPercentPerBlock: 0,
  minPercentTotal: 50, // mínimo de 50 pontos no total
  noZeroInAnyArea: true, // zerar qualquer disciplina reprova
  blocks: {
    I: { name: "Bloco I (Direito)", totalQuestions: 50, minQuestions: 0 },
    II: { name: "Bloco II (Conhecimentos Gerais)", totalQuestions: 50, minQuestions: 0 },
  },
  subjects: [ /* os 9 da seção 1.1, block "I"/"II", count da tabela, names da tabela */ ],
},
```
Confira que `noZeroInAnyArea` é avaliado **por disciplina** no corretor do simulado (leia o código); se for por bloco, corrija para o
CFOA sem mudar o comportamento dos outros concursos. O módulo de simulados segue desligado (`SIMULADOS_ENABLED = false`); acrescente
o CFOA a `checkSimuladoReadiness` em `app/(app)/simulados/page.tsx` como o PCPE.

### 8.4 Blocos próprios da prova
Hoje `onboarding/page.tsx` (blockNames e block por disciplina) e `lib/data/questoes.ts` (linha do `exam`) só usam os blocos do
`EXAM_CONFIGS` quando o concurso é `PCPE_AGENTE`. Crie em `simulado-rules.ts` a função
`usesOwnExamBlocks(contest): boolean` (true para `PCPE_AGENTE` e `CBMPE_CFOA`) e use-a nesses dois lugares e em qualquer outro que o
`rg "=== \"PCPE_AGENTE\""` mostrar com a mesma intenção. Os outros usos de `"PCPE_AGENTE"` (banca, inéditas, revisão de plano) são
tratados nas seções 8.6–8.9; não generalize nada além disso.

### 8.5 Edital próprio no seed (`web/prisma/seed-structure.ts`)
- `OWN_EDITAL_DIRS` ganha `{ dir: "cfoa", contest: "CBMPE_CFOA", prefix: "f" }`; acrescente `prefix: "p"` ao do PCPE e use
  `o.prefix` em `pushItems` (ids `<disciplina>/f<código>`).
- A aposentadoria de assuntos próprios usa `/\/p[^/]*$/`: troque por uma regex montada dos prefixos de `OWN_EDITAL_DIRS`.
- Disciplina com os dois mapas próprios (ex.: `direito-administrativo` tem `pcpe/` e `cfoa/`): os itens padrão (`/e`) ganham
  `excludeContests` com **os dois** concursos (o código já faz isso com `own.map(...)`; confirme).
- `pipeline/questoes/ineditas.py` (`OWN_EDITAL`) e qualquer script do pipeline que monte id de assunto: aceitar a pasta `cfoa` com o
  prefixo `f`.

### 8.6 Banca genérica (`web/src/lib/quiz/banca.ts`) — decisão do dono: "qualquer banca, AOCP primeiro"
- `contestBancas("CBMPE_CFOA")` = `AOCP_BANCAS` (o caderno pega AOCP primeiro).
- `REFORCO_CONTESTS` = `["CBMPE_OFICIAL", "CBMPE_CFOA"]`: depois da AOCP vem o reforço (múltipla escolha de qualquer outra banca e
  inéditas MentorIA), que é exatamente a ordem pedida.
- `hideInedita("CBMPE_CFOA")` = `{}` (o aluno do CFOA vê as inéditas no treino livre). Os demais concursos ficam como estão.
- Questões **certo/errado** não entram no caderno nem no simulado do CFOA (a prova é de 5 alternativas). Confira que o reforço já
  filtra `kind: "MULTIPLA_ESCOLHA"` e que o caderno AOCP não traz C/E; se trouxer, filtre só para o CFOA.
- Testes em `banca.test.ts` para as três funções com `CBMPE_CFOA`.

### 8.7 Comercial e administração (sem mudar regras de preço)
- Inclua `CBMPE_CFOA` em: `commerce/admin-actions.ts` (`CONTESTS`), `admin/financeiro/filters.ts`, `commerce/legacy.ts`
  (mapa de categoria → `"OFICIAL"`), `admin/cadastros/cadastros-view.tsx` (rótulo `"CBMPE 2º Tenente CFOA"`),
  `perfil/perfil-view.tsx` (`{ key: "CBMPE_CFOA", label: "2º TENENTE CFOA - CBMPE" }`), `web/scripts/waitlist.ts`
  (`"CBMPE 2º Tenente CFOA"`) e todo `Record<Contest, ...>` que o `npm run typecheck` acusar (cada um com o valor análogo ao do
  CBMPE Oficial, salvo regra desta seção).
- **Data da prova vazia** (decisão do dono): não crie data padrão no banco. Pela regra atual, a contratação é registrada mas o
  acesso "até a prova" não é liberado e o pagamento vai para os pontos de atenção. **Verifique** no código e com um teste de
  integração (Mercado Pago falso, como `waitlist-online.integration.test.ts`) que: (a) a inscrição e o pagamento do CFOA funcionam
  sem `examDate`; (b) o pagamento aparece nos pontos de atenção; (c) o administrador consegue aprovar o cadastro em Cadastros. Se (c)
  for impossível sem data (a única opção é "Até a data da prova"), **não mude as regras de acesso**: registre como pendência do
  dono no relatório final.
- `pricing.ts` não muda (a categoria `OFICIAL` já existe).

### 8.8 Assistente do plano sem data da prova
`onboarding/wizard.tsx` usa `EXAM_DEFAULT = "2027-02-28"` quando o concurso não tem `examDate`. Para o CFOA (e só para concurso sem
`examDate`), a data sugerida passa a ser **hoje em Recife + 365 dias** (`todayISO()` no servidor, passada como `defaultExamDate`;
nunca `new Date().toISOString()`), editável, com um `InfoTip` ao lado do campo: "A data da prova ainda não foi divulgada. Informe a
data prevista; você pode alterá-la depois refazendo o plano." Os outros concursos não mudam (todos têm `examDate`). Respeite o limite
de 2 anos de `onboarding/actions.ts`.

### 8.9 Plano em análise
Acrescente `"CBMPE_CFOA"` a `CONTESTS_HELD_FOR_REVIEW` (`lib/plan/initial-status.ts`): todo plano do CFOA nasce `PENDING_ANALYSIS`
e passa pela rotina `verify-plans.ts` do dono. Atenção à regra de git da seção 0 (esse arquivo tem alterações de outra frente).

### 8.10 Verificação de planos e combos
- `planner/verify.ts` e `scripts/verify-plans.ts` devem aceitar o CFOA (pedido, disciplinas, edital do concurso pelos itens `/f`).
  Rode `verify-plans.ts` **local** e confira LIBERAR para os planos de teste da seção 11.
- `combos.ts`: o CFOA **não** é membro de combo. Confira que `comboMembers("CBMPE_CFOA")` devolve `["CBMPE_CFOA"]`.

### 8.11 Desempenho › Você × aprovados
Não há listas de aprovados do CFOA. `profilesForContest("CBMPE_CFOA")` devolve `[]` e a tela mostra o mesmo estado vazio do PCPE.
Não reaproveite os perfis do CFO.

### 8.12 Testes unitários
Acrescente o CFOA em `contests.test.ts`, `user-contest.test.ts`, `planner/planner.test.ts` (um plano CFOA de 20 h/semana gera, cobre
as 9 disciplinas e passa em `verifyPlan`), `quiz/topic-map.test.ts` (questão de `direito-administrativo` com assunto `/e` vai para o
assunto `/f` do CFOA) e `plan/initial-status.test.ts`. `npm run typecheck`, `npm run lint` (sem erro novo além da baseline) e
`npm test` passando.

Commit: `feat(cfoa): concurso CBMPE_CFOA no app (enum, migrações, prova, banca, seed e testes)`.

---

## 9. Fase G — Bizus e resumos analíticos

Escopo: **todo trecho que vale para o CFOA e ainda não tem** bizu (`content/items/<disc>/<aula>.json`) ou resumo analítico
(`content/summaries/<disc>/<aula>.json`). Isso inclui as 3 disciplinas novas, `direito-penal-militar/a20`–`a21` e todos os
complementos novos. Liste com `validate_content.py --coverage` e `validate_summaries.py --coverage`, filtrando os trechos com
`appears: true` para `CBMPE_CFOA` em `content/importance/segments.json`.

- Bizus: `pipeline/briefs/bizu.md` à risca (resumo sintético em `summary` só com **negrito**; 8 itens C/E autorais por trecho;
  ponteiros de página reais; `literal: true` só para citação de norma).
- Resumos: `pipeline/briefs/summary.md` à risca, lendo o texto-fonte com `summary_source.py <trecho>` (nunca escrever a partir do
  título do tópico: foi o defeito encontrado na Rodada 6 do PCPE). Seções, `### Para fixar` com 5 a 8 itens, alvo de tamanho da
  fila (`summary_queue.py --pending --subject <disc>`), impressão digital do trecho.
- Os resumos novos entram com o status que `summary.md` define para produção por agente (não promova a aprovado).
- Validação sem erro: `validate_content.py`, `validate_summaries.py` (originalidade: nenhuma sequência ≥ 16 palavras igual à
  fonte); `summary_coverage.py --md` e **releia contra a fonte** todo trecho REFAÇÃO/REVISAR.
- Depois: `apply_synthetic.py` (grava o sintético nos bizus e espelha em `web/content`) e `npx tsx prisma/seed-structure.ts` local.
- Pode dividir o trabalho em subagentes por disciplina, um arquivo de saída por agente (nunca dois no mesmo arquivo), com os mesmos
  briefings; você consolida e valida.
- Dúvidas e possíveis erros do material-base: registre em `notes` da aula e na seção do `HISTORICO.md` (13.x), sem alterar gabarito.

Commit: `feat(cfoa): bizus e resumos analíticos dos trechos do CFOA`.

---

## 10. Fase H — Questões inéditas MentorIA provisórias (decisão do dono: sim)

Objetivo: o caderno de cada atividade do CFOA não fica curto enquanto as questões reais do TEC não chegam.

1. Crie `web/scripts/cfoa-cadernos-base.ts` (só leitura, banco **local**) que grava `pipeline/briefs/ineditas-cfoa-base.json`: por
   trecho com `appears: true` para o CFOA, quantas questões **servíveis** existem (aprovadas, múltipla escolha, AOCP + reforço de
   outras bancas + inéditas ativas, exatamente como `lib/quiz/pool.ts` montaria para o CFOA).
2. Crie `pipeline/questoes/lacunas_cfoa.py` a partir de `lacunas_cbmpe_aula.py` (mesmos modos: resumo, `--lista <disc>`, `--check`),
   com duas metas: **≥ 7 questões servíveis por trecho** e **≥ 25 na soma dos até 4 primeiros trechos de cada aula**.
3. Escreva as inéditas que faltam, **só múltipla escolha de 5 alternativas**, seguindo `pipeline/briefs/ineditas-cbmpe.md` e
   `ineditas-cbmpe2.md` (formato de rascunho com a correta em A, ferramenta que embaralha e grava com trava em
   `content/questoes/ineditas/mc/<disciplina>.txt`, comentário obrigatório, alternativas de tamanho equilibrado, sem citar o
   material-base). Estilo: padrão AOCP (é a referência do sistema para o CBMPE). Fonte do conteúdo: o resumo analítico e o texto
   legal oficial do trecho. Validação: `ineditas_mc_nativas.py --check` sem erro.
4. Grave **só no banco local**: `npx tsx web/scripts/questoes-ineditas.ts` com `batch = mentoria-inedita-<AAAA-MM-DD>-cfoa`,
   `banca = "Inédita MentorIA"`, ids `mentoria_*`. Nada com `--remoto` (a produção é a seção 14).
5. `lacunas_cfoa.py --check` sai 0. Registre um relatório de revisão humana em
   `content/questoes/ineditas/REVISAO-<data>-cfoa.md` (dúvidas de números, prazos e leis recentes).
6. **Nunca** rode `--limpar-estrategia`, nem `--aposentar` sem `--simular` (há regra do CBMPE: ver `HISTORICO.md` 11.2).

Commit: `feat(cfoa): inéditas provisórias de múltipla escolha para os trechos do CFOA`.

---

## 11. Fase I — Teste ponta a ponta (local, navegador do app)

Com o banco local semeado (`seed-structure.ts`) e `npm run dev`:
1. `/concursos` (com `available` temporariamente `true` só no local, sem commitar): o card "2º Tenente CFOA" aparece na linha do
   CBMPE, abre `/lista-de-espera/cbmpe-cfoa`, mostra R$ 120 / R$ 90 e a inscrição funciona (Mercado Pago falso ou Pix estático).
2. Crie um usuário de teste do CFOA pelo mecanismo existente (`scripts/invite.ts` ou o de usuário de teste local, se já estiver na
   branch; não commite o segundo). No assistente: 9 disciplinas, blocos "Bloco I (Direito)" e "Bloco II (Conhecimentos Gerais)",
   pesos da 1.1, sem língua estrangeira, anamnese com os assuntos `/f` e os das 3 disciplinas novas, data sugerida = hoje + 365 dias
   com o InfoTip.
3. Gere planos com 10, 20 e 40 h/semana, níveis iniciante e avançado, com e sem Turbo (12 planos). Para cada um: `verify-plans.ts`
   local = LIBERAR; `plan-demo.ts` sem atividade de aula excluída do CFOA; nenhum trecho de Informática, Inglês, Espanhol etc.
4. Abra uma atividade de Teoria de cada disciplina nova e de `direito-penal-militar/a20`: Diretriz com aula e páginas, resumo
   analítico, Bizu com o sintético; o PDF de um complemento novo abre na página certa.
5. Caderno de Questões de 3 atividades (uma de disciplina nova): 25 questões, sem C/E. Banco de Questões: assuntos do CFOA nos
   filtros, blocos do CFOA.
6. Desempenho: estados vazios corretos, "Você × aprovados" sem dados.
7. `npx tsx web/scripts/cadernos-auditoria.ts` (local) para o CFOA: 0 cadernos abaixo de 25.
Registre o resultado de cada passo (com print quando for visual) no relatório final.

---

## 12. Fase J — Documentação e liberação

1. `available: true` no `CONTESTS` do CFOA (decisão do dono: "ao fim do trabalho") e `export-contests.ts` de novo.
2. `CLAUDE.md`: na linha **Concursos**, de "cinco" para "seis" e uma frase sobre o CFOA (seleção interna, 100 questões, base no
   edital 2023, sem data e sem banca, `content/edital/cfoa/` → itens `<disciplina>/f<código>`, aulas `onlyContests: CBMPE_CFOA`).
   Ajuste a linha de banca/reforço (`REFORCO_CONTESTS` com o CFOA). Mantenha o estilo do arquivo.
3. `HISTORICO.md`: nova seção **13. Inclusão do CFOA (data)** com: decisões do dono (seção 1 e 8.6–8.8), o que foi corrigido do
   commit `6c13e84`, aulas e trechos por disciplina, complementos, lacunas não resolvidas, inéditas (quantas por disciplina),
   verificações com números, dúvidas do material e pendências do dono.
4. `README.md`: só se ele lista concursos.
5. Bateria final, toda verde (ou com as falhas antigas listadas e comparadas): `pytest`, `validate_content.py`,
   `validate_summaries.py`, `compare_importance_main.py`, `compare-plans-main.ts`, `plan-snapshot.ts` (antes × depois),
   `npm run typecheck`, `npm run lint`, `npm test`, `npm run build`.

Commit: `feat(cfoa): libera o 2º Tenente CFOA CBMPE e documenta a inclusão`.

---

## 13. Deixar pronto para as questões do TecConcursos (o dono baixa depois)

Não importe nada. Produza `CFOA-CADERNOS-TEC.md` na raiz (modelo: `PCPE-PRIORIDADE-TEC.md`), com:
- por disciplina e item do edital (códigos da seção 2), o que filtrar no TEC (matéria e assunto como o TEC costuma nomear, banca
  "qualquer" com AOCP primeiro, só múltipla escolha) e a meta de questões por item (proporcional às questões da prova; mínimo 25
  por aula ativa);
- prioridade: primeiro as 3 disciplinas novas e as normas da Legislação Extravagante, depois o resto;
- o passo a passo de importação já existente (`importar.py`, curadoria em `content/questoes/mapa-assuntos.json` para as matérias
  novas do TEC → `administracao`, `direitos-humanos`, `direito-processual-penal-militar` e às aulas `onlyContests: CBMPE_CFOA`,
  backup antes da produção, `--confirmo-producao`) e, depois da importação, `questoes-ineditas.ts --aposentar --simular` para ver
  quais inéditas do CFOA podem sair, lembrando a ressalva do CBMPE.
Não acrescente entradas ao `mapa-assuntos.json` agora (os nomes de matéria só se conhecem com os cadernos na mão).

---

## 14. Publicação na produção (só com autorização do dono)

Quando as fases A–J estiverem commitadas e a bateria verde, **pare** e mande ao dono, numa mensagem só:
- resumo do que foi feito, com os números (aulas, trechos, complementos, lacunas abertas, inéditas, testes);
- a lista de pendências dele (textos de norma não encontrados, aprovação sem data da prova, revisão humana das inéditas e dos
  resumos, dúvidas do material);
- os passos exatos de publicação, na ordem, e a pergunta "Posso publicar?":
  1. `git push origin cfoa` e merge na `main` (o build da Vercel roda `seed-structure.ts` na produção);
  2. migrações na produção (`migrate deploy` com a URL de `web/.env.remote`);
  3. backup íntegro de questões (`questoes-backup.ts --remoto`, < 24 h) e gravação das inéditas do CFOA
     (`questoes-ineditas.ts --remoto`, sem `--retirar-ausentes` a menos que o dono peça);
  4. `cadernos-auditoria.ts` na produção (só leitura) para conferir 0 cadernos curtos no CFOA e nenhuma mudança no CBMPE/PCPE.

Só execute depois de um "sim" explícito do dono nesta conversa, e exatamente esses passos. Se algum falhar, pare e relate (não tente
contornar).

---

## 15. Quando parar e perguntar (lista fechada)

Pergunte ao dono, sem decidir sozinho, se:
- um item do edital admitir duas leituras que mudem o material a usar (ex.: um assunto que caberia em duas disciplinas);
- o material-base de uma aula contradisser o texto legal oficial em ponto que caia na prova (registre e pergunte qual seguir);
- alguma verificação de zero divergência (7.3) não puder ser zerada;
- qualquer passo exigir mudar regra comercial, de acesso, de preço ou de planejamento além do que está escrito aqui;
- você precisar de qualquer credencial, conta ou download (nunca adivinhe senha nem acesse conta do dono).

Fora desses casos, siga este documento até o fim sem pedir confirmação a cada fase.
