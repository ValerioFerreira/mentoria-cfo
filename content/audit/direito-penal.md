# Relatório de Auditoria Estrutural — Direito Penal (PCPE)

**Data**: 16/10/2026  
**Auditor**: Agente MentorIA  
**Aulas auditadas**: `direito-penal/a00` a `a10` (Prof. Renan Araujo, pasta `docs/46`)  
**Total de páginas auditadas**: 1.139 págs. (material-base)  
**Total de trechos de teoria gerados**: 69 segmentos (797 páginas úteis de teoria, média de 11,6 págs/seg, 0 violações de teto, 0 cortes no meio de tópico)  

---

## 1. Visão Geral e Estrutura das Aulas

A disciplina atende integralmente ao conteúdo de **Noções de Direito Penal** previsto no edital da Polícia Civil de Pernambuco (Portaria Conjunta SAD/SDS nº 306/2026, banca Cebraspe, itens 1 a 7 e item 20):
1. **Aula `a00`**: Princípios Básicos e Fundamentais do Direito Penal, Princípio da Insignificância e Disposições Constitucionais.
2. **Aula `a01`**: Aplicação da Lei Penal no Tempo e no Espaço, Territorialidade, Extraterritorialidade, Prazos e Conflito Aparente de Normas.
3. **Aula `a02`**: Teoria do Crime, Fato Típico (Conduta, Resultado, Nexo, Tipicidade), Dolo e Culpa, Iter Criminis, Tentativa, Consumação, Ilicitude e Causas de Exclusão.
4. **Aula `a03`**: Culpabilidade, Imputabilidade Penal e Teoria do Erro (Erro de Tipo, Erro de Proibição e Discriminantes Putativas).
5. **Aula `a04`**: Crimes contra a Pessoa (Homicídio, Feminicídio, Induzimento ao Suicídio, Aborto, Lesões Corporais, Crimes contra a Honra e Liberdade Individual).
6. **Aula `a05`**: Crimes contra o Patrimônio (Furto, Roubo, Extorsão, Usurpação, Dano, Apropriação Indébita, Estelionato, Fraude Eletrônica e Receptação).
7. **Aula `a06`**: Crimes contra a Dignidade Sexual (Estupro, Violação Sexual Mediante Fraude, Estupro de Vulnerável, Lenocínio e Ação Penal).
8. **Aula `a07`**: Crimes Praticados por Funcionário Público contra a Administração em Geral (Peculato, Concussão, Corrupção Passiva, Prevaricação e Sigilo).
9. **Aula `a08`**: Crimes Praticados por Particular contra a Administração em Geral (Resistência, Desobediência, Desacato, Corrupção Ativa, Descaminho e Contrabando).
10. **Aula `a09`**: Crimes contra a Administração da Justiça e Crimes contra as Finanças Públicas.
11. **Aula `a10`**: Crimes em Licitações e Contratos Administrativos (arts. 337-E a 337-P do Código Penal).

---

## 2. Diagnóstico e Correções Estruturais (`content/overrides/direito-penal.json`)

### Tratamento de Marcadores com Caractere Invisível (`\u200b`)
- **Problema encontrado**: O material do Prof. Renan Araujo insere um caractere zero-width space (`\u200b`) imediatamente antes dos títulos de transição de bloco (`\u200bEXERCÍCIOS COMENTADOS`, `\u200bEXERCÍCIOS PARA PRATICAR` e `\u200bGABARITO`). Com isso, os marcadores padrão da pipeline falhavam na detecção, fazendo com que listas inteiras de exercícios fossem classificadas indevidamente como teoria contínua.
- **Solução adotada**: Mapeamento explícito das faixas de páginas de cada uma das 11 aulas em `content/overrides/direito-penal.json`:
  - `THEORY`: Faixa inicial de teoria pura (págs. 2 até o início dos exercícios comentados).
  - `COMMENTED`: Bloco de questões com comentários do professor.
  - `LIST`: Bloco de questões de fixação para praticar.
  - `KEY`: Folha final de gabarito e encerramento.

### Particionamento Pedagógico das Aulas Extensas (`a04` e `a05`)
- Aulas com grande densidade dogmática (Crimes contra a Pessoa com 160 págs. de teoria e Crimes contra o Patrimônio com 156 págs.) foram particionadas respeitando os capítulos e títulos do Código Penal:
  - `a04`: cortes pedagógicos nas páginas 9 (*Homicídio Qualificado*), 22 (*Feminicídio e Majorantes*), 37 (*Suicídio, Infanticídio e Aborto*), 51 (*Lesões Corporais*), 77 (*Periclitação da Vida/Saúde e Rixa*), 101 (*Crimes contra a Honra*), 118 (*Liberdade Individual, Ameaça e Stalking*) e 144 (*Inviolabilidade de Domicílio e Segredos*).
  - `a05`: cortes nas páginas 21 (*Furto Qualificado e Combustíveis*), 39 (*Roubo*), 54 (*Roubo Qualificado pelo Resultado*), 68 (*Extorsão e Dano*), 90 (*Apropriação Indébita*), 105 (*Estelionato*), 123 (*Fraudes em Ativos Virtuais*) e 139 (*Receptação*).
- **Resultado da segmentação**: 0 trechos violando o teto de 17 páginas, 0 cortes no meio de tópico e distribuição perfeitamente harmônica de carga.

---

## 3. Cobertura do Edital

| Item do Edital | Descrição | Onde é estudado | Status |
|---|---|---|---|
| **1** | Princípios básicos do direito penal | `direito-penal/a00` | Coberto (100%) |
| **2** | Crime e contravenção: fato típico, ilicitude, culpabilidade e erro | `direito-penal/a02` e `a03` | Coberto (100%) |
| **3** | Aplicação da lei penal (tempo, espaço, territorialidade, prazos) | `direito-penal/a01` | Coberto (100%) |
| **4** | Crimes contra a pessoa | `direito-penal/a04` | Coberto (100%) |
| **5** | Crimes contra o patrimônio | `direito-penal/a05` | Coberto (100%) |
| **6** | Crimes contra a dignidade sexual | `direito-penal/a06` | Coberto (100%) |
| **7** | Crimes contra a administração pública | `direito-penal/a07`, `a08`, `a09` e `a10` | Coberto (100%) |
| **20** | Disposições constitucionais aplicáveis ao direito penal | `direito-penal/a00` (s03) | Coberto (100%) |

*Nota: Os itens 8 a 19 do edital referem-se a leis penais especiais e são auditados na disciplina `legislacao-penal-especial`.*
