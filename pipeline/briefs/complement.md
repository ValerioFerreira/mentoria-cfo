# Briefing — Criação de materiais complementares (MentorIA / CFO-BM)

Você cria UM ou MAIS materiais complementares autorais para preencher lacunas do edital do 2º Tenente CBMPE (banca Instituto AOCP). Outros agentes trabalham em paralelo: só crie/edite os arquivos que lhe foram atribuídos.

## Contexto
- Repositório `C:\Users\Administrador\Documents\Projetos\CFO-BM`. Leia `CLAUDE.md` (seção "Materiais complementares") e um complemento existente como modelo de tom e estrutura: `content/complements/leg-pe-lei-14751.md` (norma) e `content/complements/ing-estruturas-complementares.md` (conteúdo conceitual).
- Edital do cargo: `pipeline/.cache/edital_2ten.txt` (leia o trecho da sua disciplina). Lacuna a resolver: `content/gaps.json` (campos `id`, `item`, `evidence`) e relatório `content/audit/<disciplina>.md`.
- O material é lido por um aluno que estuda para a prova: linguagem direta ("Pessoal, ..."), em pt-BR, com o que mais cai na AOCP, quadros comparativos, macetes, pegadinhas, exemplos resolvidos (exatas) e remissão a artigos (normas).
- **Originalidade**: conteúdo próprio, parafraseado a partir de fonte oficial/pública (texto legal, normas técnicas, conhecimento didático padrão). **Nunca copie texto do Estratégia** (`docs/` e `pipeline/.cache/pages` servem só para você saber o que JÁ está coberto e evitar duplicar). Não reproduza longos trechos de livros; cite artigos/fórmulas, não parágrafos de terceiros.
- **Exatidão acima de tudo**: normas — só dispositivos que você viu no texto oficial (use WebFetch/WebSearch: planalto.gov.br, legis.alepe.pe.gov.br, câmara/senado; se um site recusar a conexão, tente outro) e nunca invente artigo, prazo ou número; o que não conseguir verificar, omita e liste em "Pendências". Exatas — confira cada conta (use Python se ajudar). Registre a data da consulta.

## Formato: `content/complements/<id>.md`
```
---
id: <prefixo>-<assunto>
subject: <disciplina>
title: Título completo
short: Título curto
subtitle: Uma linha dizendo o que cobre (cite o item do edital)
weight: 0.10          # fatia do peso da disciplina entre os complementos+aulas; use 0.05–0.25 conforme a importância do item na prova
order: N              # número do complemento NA DISCIPLINA (aula cNN); veja a ordem atribuída ao seu pedido
resolves: <id-da-lacuna>[,<outra>]   # ids de content/gaps.json
---

## Primeira seção ...
(Markdown: ## seções, ### subseções, tabelas, listas, > citações-macete)

## Fontes
(lista das fontes consultadas, com data — vira o rodapé "Fontes e método" do PDF)
```
- Cada seção `##` é um possível ponto de corte de trecho de ~1 h (o build agrupa seções em trechos de até 17 págs. A4; ~8–9 págs. de material denso por hora). Comece cada assunto autônomo com `##`. Um complemento deve ter entre 3 e ~20 páginas A4 (≈ 1.200–7.000 palavras): profundidade proporcional ao peso do item no edital e na AOCP, sem encher linguiça.
- Fórmulas em texto simples/Unicode (o PDF é gerado de HTML simples: sem LaTeX). Tabelas Markdown funcionam.
- Termine com seção `## Fontes`.

## Verificação (rode para o SEU arquivo; não rode build_catalog/seed)
```
cd pipeline && .venv/Scripts/python build_complements.py --only <id> --no-merge
```
(defina `PYTHONIOENCODING=utf-8`; confira que gerou o PDF em `web/public/complementos/<id>.pdf`, o número de páginas e de segmentos impressos). **Sempre com `--no-merge`**: o orquestrador faz a mesclagem no catálogo no fim; sem a flag, execuções paralelas se atropelam. Se der erro de front matter, corrija.

## Entrega
Resposta final curta (≤ 12 linhas): arquivos criados, páginas/segmentos de cada, lacunas que resolve (ids), o que não conseguiu verificar (pendências) e se algo no edital continua descoberto.
