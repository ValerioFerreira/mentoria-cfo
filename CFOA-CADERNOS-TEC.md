# CFOA — Cadernos do TecConcursos por Prioridade

Guia de extração, filtros e importação dos cadernos de questões do TecConcursos para o concurso de **2º Tenente CFOA CBMPE** (`CBMPE_CFOA`).

> [!NOTE]
> O sistema já conta com 1.333 questões inéditas MentorIA de múltipla escolha (padrão AOCP, 5 alternativas), garantindo que nenhum caderno do plano de estudos fique com menos de 25 questões. Quando o usuário fizer o download dos cadernos no TecConcursos, siga este documento para importar e, gradativamente, substituir as inéditas provisórias.

---

## 1. Regras Gerais de Filtro no TecConcursos

- **Banca:** Qualquer banca (a banca de referência é o **Instituto AOCP**; baixe AOCP primeiro, depois complete com bancas organizadoras consagradas como FGV, Cebraspe, FCC, Vunesp, IBFC, etc.).
- **Tipo de Questão:** **Múltipla Escolha** (4 ou 5 alternativas). Questões Certo/Errado **não** entram na prova do CFOA nem nos cadernos do plano.
- **Filtros de Qualidade:**
  - Desmarcar questões anuladas e desatualizadas.
  - Ano: $\ge 2018$ preferencialmente (leis e normas recentes); $\ge 2015$ para temas doutrinários consolidados.
- **Meta de Quantidade:**
  - Mínimo de 25 questões por aula ativa do plano.
  - Meta de 7 a 15 questões por trecho/atividade individual.

---

## 2. Ordem de Prioridade para Download dos Cadernos

A prioridade é guiada por: (1) matérias e normas exclusivas/novas no catálogo; (2) peso de questões na prova (Bloco I com 50 questões, Bloco II com 50 questões).

### Prioridade 1: Disciplinas Novas e Legislação Extravagante (Críticas)

| # | Disciplina | Assunto / Itens do Edital CFOA | Filtro Sugerido no TEC | Meta Mínima | Caderno Sugerido |
|---|---|---|---|:---:|---|
| 1 | **Direito Processual Penal Militar** | Inquérito Policial Militar (IPM), Polícia Judiciária Militar, Ação Penal Militar, Competência da JMU e JME, Processo Ordinário Militar, Nulidades e Recursos (`f01` a `f11`) | Matéria: *Direito Processual Penal Militar* → Assuntos correspondentes ao CPPM | 225 | `CFOA DPPM 1` e `2` |
| 2 | **Direitos Humanos** | Teoria Geral, DH na CF/88, Tratados Internacionais, Sistema Interamericano (Pacto de San José, Declaração Americana), Regras de Mandela, Grupos Vulneráveis (`f01` a `f07`) | Matéria: *Direitos Humanos* → Conceito, Classificação, Tratados, Sistema Interamericano | 175 | `CFOA DH 1` e `2` |
| 3 | **Noções de Administração** | Funções Administrativas (PODC), Estrutura Organizacional, Gestão por Processos, Gestão da Qualidade, Gestão de Pessoas, Gestão de Materiais, Gestão Estratégica / BSC (`f01` a `f10`) | Matéria: *Administração Geral* e *Administração Pública* | 250 | `CFOA ADM 1` e `2` |
| 4 | **Legislações PE (Normas Extravagantes)** | Estatuto dos Policiais Militares (Lei 6.783/1974), Código de Ética (Dec. 22.114/2000), Promoções (LC 470/2021), Assédio Moral/Sexual (Lei 13.314/2007), LAI (Lei 12.527/2011), LC 317/2015 | Matéria: *Legislação Estadual - PE* e *Legislação Específica CBM-PE / PM-PE* | 200 | `CFOA LEGPE 1` |
| 5 | **Direito Penal Militar (Extravagante)** | Abuso de Autoridade (Lei 13.869/2019), Crimes Ambientais (Lei 9.605/1998), Crimes em Licitações (CP arts. 337-E a 337-P) (`f06`, `f07`) | Matérias: *Legislação Penal Especial* / *Direito Penal* | 120 | `CFOA PENAL-EXTRA` |

### Prioridade 2: Disciplinas Jurídicas Tradicionais (Alto Peso na Prova)

| # | Disciplina | Assunto / Itens do Edital CFOA | Filtro Sugerido no TEC | Meta Mínima | Caderno Sugerido |
|---|---|---|---|:---:|---|
| 6 | **Direito Administrativo** | Lei 14.133/2021 (Licitações e Contratos), Improbidade (Lei 8.429/1992 com alterações da Lei 14.230/2021), Processo Administrativo PE (Lei 11.781/2000), Atos, Poderes e Regime Disciplinar | Matéria: *Direito Administrativo* | 350 | `CFOA DIRADM 1`, `2`, `3` |
| 7 | **Direito Penal Militar** | Aplicação da lei penal militar, Crime militar (art. 9º do CPM), Autoria e participação, Penas militares, Crimes militares em espécie (contra autoridade, contra o serviço, contra o patrimônio) | Matéria: *Direito Penal Militar* (CPM) | 250 | `CFOA DPM 1` e `2` |
| 8 | **Direito Constitucional** | Princípios Fundamentais, Direitos e Garantias Fundamentais, Organização do Estado, Forças Armadas e Segurança Pública (art. 144), Constituição Estadual de PE | Matéria: *Direito Constitucional* | 250 | `CFOA DCONST 1` e `2` |

### Prioridade 3: Conhecimentos Gerais (Bloco II)

| # | Disciplina | Assunto / Itens do Edital CFOA | Filtro Sugerido no TEC | Meta Mínima | Caderno Sugerido |
|---|---|---|---|:---:|---|
| 9 | **Língua Portuguesa** | Compreensão e interpretação, Tipologia e gêneros, Ortografia, Acentuação, Sintaxe, Concordância, Regência, Crase, Pontuação e Manual de Redação da Presidência da República (3ª ed.) | Matéria: *Língua Portuguesa* e *Redação Oficial* | 300 | `CFOA PORT 1` e `2` |
| 10 | **Raciocínio Lógico** | Estruturas lógicas, Lógica de argumentação, Diagramas lógicos, Lógica proposicional, Tabela-verdade, Equivalências e negações, Análise combinatória e probabilidade | Matéria: *Raciocínio Lógico* | 200 | `CFOA RLOG 1` |

---

## 3. Passo a Passo de Extração e Importação

### 3.1 Download dos Cadernos
1. Acesse o TecConcursos, monte os cadernos conforme a tabela acima e imprima/salve em PDF ("Imprimir Caderno").
2. Salve os arquivos baixados na pasta `docs/questoes/` do projeto (ex.: `docs/questoes/CFOA-ADMESTRATEGICA.pdf`).

### 3.2 Curadoria no Mapa de Assuntos (`content/questoes/mapa-assuntos.json`)
Antes de importar ou logo após a primeira extração, mapeie as matérias/assuntos do TEC para as disciplinas e aulas do MentorIA:
- Matérias novas no TEC:
  - *Administração Geral* / *Administração Pública* $\to$ `administracao` (aulas `a00` a `a08`, `c01`).
  - *Direitos Humanos* $\to$ `direitos-humanos` (aulas `a00` a `a05`, `c01`, `c02`).
  - *Direito Processual Penal Militar* $\to$ `direito-processual-penal-militar` (aulas `a00` a `a12`, `c01`).
- Assuntos que não caem no CFOA: marcar com `"skip": true`.

### 3.3 Importação no Banco de Dados Local
Execute o importador com o modo de extração e classificação:
```powershell
# Extrair e importar para o banco local
.\pipeline\.venv\Scripts\python.exe pipeline/questoes/importar.py --reclassificar
```
Verifique o resultado e a contagem no banco:
```powershell
npx tsx scripts/questoes-contagem.ts
```

### 3.4 Auditoria das Questões Importadas
Execute a ferramenta de auditoria para identificar eventuais falhas de extração geométrica:
```powershell
.\pipeline\.venv\Scripts\python.exe pipeline/questoes/auditoria.py
```
Se houver questões com texto truncado ou erro de gabarito, marque-as como rascunho:
```powershell
npx tsx scripts/questoes-marcar-rascunho.ts
```

### 3.5 Importação na Produção (Neon)
Quando validado no ambiente local:
1. **Gere backup íntegro com menos de 24 horas:**
   ```powershell
   npx tsx scripts/questoes-backup.ts --remoto
   ```
2. **Execute a importação na produção com confirmação:**
   ```powershell
   .\pipeline\.venv\Scripts\python.exe pipeline/questoes/importar.py --remoto --confirmo-producao
   ```

### 3.6 Aposentadoria de Inéditas Provisórias
Com as questões reais do TEC devidamente importadas no banco, simule a aposentadoria das inéditas provisórias:
```powershell
# Simulação segura
npx tsx scripts/questoes-ineditas.ts --aposentar --minimo 8 --simular
```
> [!CAUTION]
> **Ressalva do CBMPE:** Lembre-se de que o concurso CBMPE Oficial também utiliza questões inéditas como reforço. Nunca aposente inéditas em massa sem antes rodar `npx tsx scripts/cadernos-auditoria.ts --remoto` para garantir que nenhum caderno do CBMPE Oficial ou do CFOA fique abaixo de 25 questões!
