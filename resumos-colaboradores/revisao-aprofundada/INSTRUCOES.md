# Revisão aprofundada dos resumos analíticos — protocolo

Objetivo: conferir cada resumo (`analytic` e `synthetic`) **contra o texto-fonte** do trecho e corrigir o que estiver errado ou faltando. A triagem automática de cobertura só mede termos; esta revisão procura **conceito errado, número/prazo/artigo trocado, omissão de ponto cobrável e texto confuso**.

Leia antes: `CLAUDE.md` (seção "Resumos analíticos") e `pipeline/briefs/summary.md` (regras de escrita e originalidade). Use `PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python`.

## Por trecho (um de cada vez)
1. Texto-fonte (PROTEGIDO, nunca copiar verbatim): `pipeline/summary_source.py <trecho>`; lista dos termos que a triagem aponta como faltando: `pipeline/summary_coverage.py --subject <disciplina> --top 100`.
2. Leia o resumo em `content/summaries/<disciplina>/<aNN>.json` (campo `analytic` e `synthetic` do trecho). Verifique, nesta ordem:
   - **Correção**: números, prazos, quóruns, artigos de lei, nomes, fórmulas, classificações, exceções. Onde o material-fonte estiver errado ou ambíguo, siga o texto legal/consenso e registre em `notes`.
   - **Completude**: todo conceito, regra, exceção, tabela ou exemplo cobrável do trecho está no resumo? Acrescente o que faltar (parafraseado, com exemplo próprio quando útil).
   - **Clareza e coerência**: sem contradição interna, sem frase truncada, `### Para fixar` com 5 a 8 itens, `synthetic` com 6 a 12 pontos que **não** repetem o analítico.
   - **Regras do projeto**: pt-BR; nunca citar "aula", "PDF", "professor", "curso" ou páginas; originalidade (nenhuma sequência de 10 palavras iguais ao material).
3. **Não afirme o que não puder confirmar** (leis, emendas, julgados, datas recentes): omita e registre em `notes` para revisão humana.
4. Corrija direto no JSON (ferramenta de edição de arquivos; não heredoc). Mantenha `fingerprint`, `agent` e os demais trechos intactos. Valide: `pipeline/validate_summaries.py content/summaries/<disciplina>/<aNN>.json` (0 erros; avisos de tamanho são aceitáveis) e rode a cobertura de novo — ela não deve cair.

## Registro (obrigatório)
Grave `resumos-colaboradores/revisao-aprofundada/RELATORIO-<LOTE>.md` com uma linha por trecho do lote: `ID | trecho | resultado (corrigido / sem alteração / dúvida humana) | o que foi alterado ou duvidado`. Trechos que dependem de figura/tabela ilegível no texto extraído entram como "dúvida humana".

## Limites
- Edite só os arquivos do seu lote (listados em `LOTE-<X>.md`); não toque em `content/items`, em `web/content` nem nos arquivos do outro lote.
- Depois de terminar, o orquestrador roda `apply_synthetic.py` e o seed. Quem revisa pode commitar **apenas** os arquivos do seu lote e o relatório.
