# Relatório de Auditoria Estrutural — Legislação Penal Especial (PCPE)

**Data**: 16/10/2026  
**Auditor**: Agente MentorIA  
**Aulas auditadas**: `legislacao-penal-especial/a11` a `a21` (pastas `docs/30` e `docs/46`) + complemento `c01` (`leg-penal-eca.md`)  
**Total de páginas auditadas**: 1.171 págs. (material-base) + 4 págs. (complemento autoral)  
**Total de trechos de teoria gerados**: 29 trechos (28 base + 1 complemento, média de 11,4 págs/seg, 0 violações de teto, 0 cortes no meio de tópico)  

---

## 1. Visão Geral e Estrutura das Aulas

A disciplina atende integralmente aos itens de legislação extravagante criminal previstos no edital da Polícia Civil de Pernambuco (Portaria Conjunta SAD/SDS nº 306/2026, banca Cebraspe, itens 8 a 19 de Noções de Direito Penal):
1. **Aula `a11`**: Lei nº 8.072/1990 (Crimes Hediondos).
2. **Aula `a12`**: Lei nº 7.716/1989 (Preconceito de Raça ou de Cor).
3. **Aula `a13`**: Lei nº 13.869/2019 (Abuso de Autoridade).
4. **Aula `a14`**: Lei nº 9.455/1997 (Crimes de Tortura).
5. **Complemento `c01`**: Lei nº 8.069/1990 (Estatuto da Criança e do Adolescente — Aspectos Penais, Procedimentos e Corrupção de Menores).
6. **Aula `a15`**: Lei nº 12.850/2013 (Organizações Criminosas).
7. **Aula `a16`**: Lei nº 9.503/1997 (Crimes de Trânsito — CTB).
8. **Aula `a17`**: Lei nº 11.340/2006 (Lei Maria da Penha).
9. **Aula `a18`**: Lei nº 11.343/2006 (Lei de Drogas).
10. **Aula `a19`**: Lei nº 14.344/2022 (Violência Doméstica contra Criança e Adolescente — Lei Henry Borel).
11. **Aula `a20`**: Lei nº 9.605/1998 (Crimes Ambientais).
12. **Aula `a21`**: Lei nº 10.826/2003 (Estatuto do Desarmamento).

---

## 2. Diagnóstico e Correções Estruturais (`content/overrides/legislacao-penal-especial.json`)

### Mapeamento das Aulas e Preservação de IDs
- As aulas foram indexadas a partir de `a11` para harmonização com o curso específico da PC-PE (pacote 361849 / curso 361847), mantendo rigorosamente isolados os identificadores e evitando qualquer sobreposição com outras matrizes.
- As transições para blocos de questões comentadas e listas de questões foram mapeadas com precisão a partir dos sumários estruturados e do texto dos PDFs.

### Particionamento Pedagógico das Aulas Extensas
- Aulas com extensos diplomas legislativos foram particionadas para garantir sessões de estudo equilibradas:
  - `a11` (Hediondos): cortes nas páginas 9 (*Rol de Crimes Hediondos*) e 24 (*Crimes no ECA e Regras Processuais*), gerando 3 trechos (6p, 15p e 11p).
  - `a13` (Abuso de Autoridade): corte na página 12 (*Crimes em Espécie*), gerando 2 trechos (9p e 16p).
  - `a15` (Organizações Criminosas): corte na página 7 (*Meios de Prova e Colaboração Premiada*), gerando 2 trechos (4p e 13p).
  - `a16` (Crimes de Trânsito): corte na página 11 (*Crimes de Trânsito em Espécie*), gerando 2 trechos (8p e 14p).
  - `a17` (Maria da Penha): cortes nas páginas 15 (*Atendimento Policial*) e 28 (*Medidas Protetivas de Urgência*), gerando 3 trechos (12p, 13p e 16p).
  - `a18` (Lei de Drogas): cortes nas páginas 22 (*Porte para Consumo*), 35 (*Tráfico e Equiparados*) e 53 (*Procedimento Penal*), gerando 4 trechos (19p, 13p, 18p e 17p).
  - `a20` (Crimes Ambientais): cortes nas páginas 18 (*Fauna*), 28 (*Flora*) e 38 (*Poluição e Administração Ambiental*), gerando 4 trechos (15p, 10p, 10p e 9p).
  - `a21` (Estatuto do Desarmamento): cortes nas páginas 15 (*Competências*) e 25 (*Crimes em Espécie*), gerando 3 trechos (12p, 10p e 15p).

---

## 3. Cobertura do Edital

| Item do Edital | Descrição | Onde é estudado | Status |
|---|---|---|---|
| **8** | Crimes hediondos (Lei nº 8.072/1990) | `legislacao-penal-especial/a11` | Coberto (100%) |
| **9** | Preconceito de raça ou cor (Lei nº 7.716/1989) | `legislacao-penal-especial/a12` | Coberto (100%) |
| **10** | Abuso de autoridade (Lei nº 13.869/2019) | `legislacao-penal-especial/a13` | Coberto (100%) |
| **11** | Crimes de tortura (Lei nº 9.455/1997) | `legislacao-penal-especial/a14` | Coberto (100%) |
| **12** | Estatuto da Criança e do Adolescente (Lei nº 8.069/1990) | `legislacao-penal-especial/c01` | Coberto por Complemento |
| **13** | Organizações criminosas (Lei nº 12.850/2013) | `legislacao-penal-especial/a15` | Coberto (100%) |
| **14** | Crimes de trânsito (Lei nº 9.503/1997) | `legislacao-penal-especial/a16` | Coberto (100%) |
| **15** | Violência contra a mulher (Lei nº 11.340/2006) | `legislacao-penal-especial/a17` | Coberto (100%) |
| **16** | Lei de drogas (Lei nº 11.343/2006) | `legislacao-penal-especial/a18` | Coberto (100%) |
| **17** | Violência contra menor (Lei nº 14.344/2022) | `legislacao-penal-especial/a19` | Coberto (100%) |
| **18** | Crimes ambientais (Lei nº 9.605/1998) | `legislacao-penal-especial/a20` | Coberto (100%) |
| **19** | Estatuto do Desarmamento (Lei nº 10.826/2003) | `legislacao-penal-especial/a21` | Coberto (100%) |

**Resultado**: 100% dos itens de legislação penal extravagante do edital PCPE plenamente cobertos.
