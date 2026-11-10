# Protocolo do revisor: material próprio MentorIA

Quem revisa é o orquestrador, não o autor. O autor segue `pipeline/briefs/material.md`; este protocolo aplica a rubrica da seção 14 daquele briefing, sempre do mesmo jeito.

## 1. Quando revisar

Revise um volume quando todos os arquivos dele estiverem com `status: "PRONTO_PARA_REVISAO"`. Para ver o andamento:

```
PYTHONIOENCODING=utf-8 pipeline/.venv/Scripts/python pipeline/validate_material.py --status --wave 1
```

Ao começar, mude o status de todos os arquivos do volume para `"EM_REVISAO"`.

## 2. Checagem automática (sempre)

1. Rode o validador com estatísticas:

   ```
   pipeline/.venv/Scripts/python pipeline/validate_material.py content/material/<disc>/<mNN> --json
   ```

   - Qualquer ERRO devolve o volume na hora.
   - Os AVISOS entram na leitura: cada um precisa estar resolvido ou justificado em `notas`.
2. Na saída do `--json`, compare por capítulo:
   - `words` com `target`;
   - `visuals` e `callouts` com as metas;
   - `coverage`: abaixo de 0,70, leia a seção inteira contra a fonte;
   - `copied`: 20 palavras ou mais coincidentes, procure as frases.
3. Se a exportação de questões tiver mudado, regenere-a:

   ```
   cd web && npx tsx scripts/material-questoes.ts --volume <id>
   ```

## 3. Leitura humana (por importância, da ficha)

| Importância | O que ler |
|---|---|
| ALTA | O capítulo inteiro, linha a linha |
| MEDIA | Metade das seções `##`, sorteadas, mais o Mapa do capítulo |
| BASE | Uma seção em cada três, sorteada, mais o Mapa do capítulo |

Em cada seção lida, faça três coisas:

1. **Correção.** Confira na fonte oficial pelo menos três afirmações verificáveis: artigo, prazo, número, súmula, fórmula ou cálculo.
   - Legislação: use o texto compilado do Planalto ou da ALEPE, ou `pipeline/.cache/leis-oficiais/art.py`.
   - Súmulas: use os sites dos tribunais.
   - Exatas: refaça as contas dos `[!resolvido]`.
2. **Cobertura.** Abra a mesma parte do texto-fonte (`pipeline/material_ficha.py --fonte <trecho>`) e confirme que tópicos, itens do edital e pontos de atenção estão lá, com profundidade suficiente para resolver questões.
3. **Originalidade.**
   - Escolha duas frases do capítulo e procure-as entre aspas na web (`firecrawl_search`), para pegar cópia de terceiros.
   - Compare os exemplos e as tabelas com os da fonte: personagem, número ou estrutura reaproveitados são bloqueantes.

Para as figuras: confira se o `svg`, o `mermaid` e o `grafico` mostram algo correto e legível. Quando houver dúvida, abra o SVG no navegador do app.

Na Fixação:
- Sorteie 5 questões e confira gabarito e comentário (regra certa, todas as alternativas explicadas).
- Toda inédita escrita pelo autor tem de ser lida inteira.

## 4. Decisão

Os bloqueantes são os da seção 14 do briefing: erro de conteúdo, lacuna, cópia, menção proibida e formato. Qualquer um deles leva a **DEVOLVIDO**.

Sem bloqueantes, dê a nota de 1 a 5 em didática, densidade visual, foco na prova, português e Fixação:
- média ≥ 4 e nenhuma nota menor que 3: **APROVADO**;
- caso contrário: **DEVOLVIDO**.

Registre a decisão em `content/material/<disc>/<mNN>/REVISAO.md`:

```
# Revisão de <disc>/<mNN> — rodada N — AAAA-MM-DD

Decisão: APROVADO | DEVOLVIDO
Notas: didática X · densidade visual X · foco na prova X · português X · fixação X
Validador: 0 erros, N avisos (lista dos avisos aceitos)
Lido: a00-s01 (integral), a00-s02 (seções 1 e 3) ...

## Correções obrigatórias
1. a00-s02.md, seção "Retroatividade": diz X; o art. 2º, § 1º do CPM diz Y. Corrigir e ajustar o Para fixar.
2. ...

## Melhorias pedidas (não bloqueiam)
- ...
```

Depois:
- Atualize o `status` de todos os arquivos do volume para `"APROVADO"` ou `"DEVOLVIDO"`.
- Em cada rodada nova, acrescente a seção da rodada no mesmo arquivo, sem apagar o histórico.
- Volume APROVADO fica pronto para o motor de PDF (Etapa 2 do plano). Nada vai para alunos antes disso.

## 5. Calibragem

Nos primeiros volumes (o piloto: `legislacoes-pe/m01` e `direito-penal-militar/m01`), anote quanto as metas automáticas acertaram:
- palavras;
- elementos visuais;
- quadros;
- limiares de cobertura (0,55 e 0,70).

Se precisarem de ajuste:
1. Mude as constantes em `pipeline/material_metrics.py` ou `pipeline/validate_material.py`.
2. Rode `material_metrics.py` de novo.
3. Registre a mudança no `HISTORICO.md`.

## 6. Revisão de lotes contínuos (a partir de 29/10/2026)

A produção roda em lotes encadeados (prompt em `pipeline/briefs/material-inicio.md`), e o revisor revisa por fora, sem segurar a fila. O que for DEVOLVIDO volta sozinho no lote seguinte.

**Ferramentas que reduzem a leitura:**
- `pipeline/check_citations.py <pasta> --lista`: acusa artigo inexistente e lista o início de cada artigo citado. Comparar a lista com o texto troca a leitura da lei inteira por uma conferência rápida.
- `content/material/_lotes/lote-NN.md`: métricas e avisos de cada capítulo.

**Leitura econômica (calibrada no lote 1):**
1. Validador e conferência de citações em todos os volumes.
2. Um capítulo inteiro por volume: o de maior importância.
3. Nos demais capítulos, todas as afirmações com norma, súmula, número ou cálculo (use `grep` em "art.", "Súmula", "STF", números).
4. Uma ou duas questões da Fixação.

O que achar de errado no capítulo lido inteiro vale como alerta para o volume todo: peça ao autor que confira o mesmo tipo de afirmação nos outros capítulos.
