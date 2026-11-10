# Atualização mensal do material próprio MentorIA

Briefing do agente atualizador, rodado uma vez por mês pelo dono. Objetivo: manter os PDFs de acordo com a lei vigente, a jurisprudência e os temas pendentes, mexendo **só** no que mudou.

## 1. O que existe

- `content/material/atualizacao/indice.json` e `INDICE.md`: por volume e capítulo,
  - as normas citadas (lei + artigo + impressão digital do texto vigente);
  - a jurisprudência;
  - os pontos sensíveis (pendências, julgamentos em curso, redação nova);
  - a volatilidade da disciplina (ALTA: jurídicas e legislações; MÉDIA: Informática, Administração, Atualidades, Contabilidade; BAIXA: conhecimento fixado).

  Gerado por `pipeline/material_update_index.py`.
- `content/material/atualizacao/datas.json`: a data "Material atualizado em" de cada volume (última página do PDF). Ela é derivada da seção datada mais recente do `REVISAO.md` do volume.
- `pipeline/material_watch.py`: baixa de novo as leis e grava `content/material/atualizacao/relatorio-AAAA-MM.md` com:
  1. os artigos citados cujo texto vigente mudou, e os capítulos afetados;
  2. a jurisprudência dos volumes de volatilidade ALTA;
  3. os pontos sensíveis.

## 2. Roteiro do mês

1. `pipeline/.venv/Scripts/python pipeline/material_watch.py` (com internet). Leia o relatório.
2. **Seção 1 (lei mudou)**, para cada artigo:
   - leia o texto vigente: `pipeline/.venv/Scripts/python pipeline/leis.py art <norma> <art>`;
   - abra os capítulos listados e corrija o quadro `[!lei]` (transcrição literal) e o texto que explica o artigo (prazos, penas, requisitos), além do Mapa do capítulo e dos comentários da Fixação que citam o artigo (`grep` no `fixacao.json` do volume).
3. **Seção 2 (jurisprudência)**, para cada súmula, tema ou ação citada:
   - confira no site oficial do tribunal (STF, STJ, STM) se continua válida: cancelamento, revisão de tese, julgamento de mérito de ADI/ADPF, modulação;
   - procure também súmulas e teses novas sobre os assuntos do volume, publicadas no mês;
   - corrija o que mudou.
4. **Seção 3 (pontos sensíveis)**: dê prioridade a "pendente", "em julgamento" e "liminar". Exemplo: a ADI 7881 (LC 219/2025, Direito Constitucional m04). Se o caso foi julgado, reescreva o trecho com o resultado e a fonte.
5. **Normas fora do cache**: se o capítulo cita uma norma que `leis.py lista` não tem, acrescente-a ao dicionário `LEIS` de `pipeline/leis.py` (endereço oficial) para que entre no vigia do mês seguinte.
6. **Em cada volume alterado**, acrescente ao fim do `REVISAO.md`:

   ```
   # Atualização mensal — AAAA-MM-DD
   Decisão: APROVADO (atualização)
   Alterações: <arquivo>: <o que mudou, com a fonte oficial e a data da consulta>
   ```

   A data dessa seção vira a nova "Material atualizado em" do volume.
7. **Feche:**
   - `validate_material.py <volume>`: 0 erros;
   - `check_citations.py <volume>`;
   - `material_update_index.py` (o índice passa a ter as impressões digitais novas);
   - `build_material.py --only <volumes alterados>` e `--conferir`.
8. Entregue ao dono:
   - a tabela volume · o que mudou · fonte;
   - os casos em dúvida;
   - os PDFs regerados.

   A publicação (envio ao armazenamento e ao app) é decisão do dono.

## 3. Regras

- Mexa só no que mudou. Não reescreva capítulos inteiros e não mude o estilo nem a estrutura.
- Fontes: só oficiais (Planalto, ALEPE, STF, STJ, STM, Diário Oficial). Notícia não substitui a decisão publicada; use-a só para achar a decisão.
- Material genérico: nada de concurso, órgão ou banca específicos (`pipeline/briefs/neutralidade.md`).
- Nunca abra `.env*`, nunca grave em banco, sem commit (salvo pedido do dono).
