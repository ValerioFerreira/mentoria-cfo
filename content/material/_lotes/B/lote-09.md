# Lote 09 — Frente B (produção contínua)

Início: 2026-10-31 · Término: 2026-10-31

| Tipo | Volume | Título | Capítulos | Autor | Situação |
|---|---|---|---|---|---|
| NOVO | direito-administrativo/m22 | Improbidade administrativa I | 5 | AGENTE-MATB-30 | concluído 31/10 |

Seleção: `material_ficha.py --lote 4 --onda 1 --frente B` (uma única execução; só um volume da onda 1 estava livre; a onda 1 está praticamente esgotada para a frente B). O volume foi reservado com `.frente` = B.
Sessão sem subagentes: o coordenador escreve o volume. Ficou em PRONTO_PARA_REVISAO.

## Validação (1 volumes)

### direito-administrativo/m22 — 0 erro(s), 18 aviso(s)

| Capítulo | Importância | Palavras/meta | Visuais/meta | Quadros/meta | Cobertura | Copiadas | Palavras por frase | Jargão |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| a24/s01 | BASE (20) | 4161/4866 | 12/4 | 10/9 | 0.75 | 34 | 16.9 | 0 |
| a24/s02 | BASE (20) | 2988/3462 | 9/6 | 7/6 | 0.78 | 0 | 18.9 | 0 |
| a24/s03 | BASE (12) | 2703/3180 | 7/4 | 7/6 | 0.68 | 20 | 14.2 | 0 |
| a24/s04 | BASE (20) | 2988/3494 | 8/5 | 7/6 | 0.73 | 20 | 16.5 | 0 |
| a24/s05 | BASE (9) | 2264/2348 | 5/4 | 5/4 | 0.77 | 21 | 19.3 | 0 |

Fixação: 16 questões · AOCP 0 · inéditas do banco 16 · inéditas novas 0
- AVISO a24-s01.md: seção 'Espécies de ato e leis especiais' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s01.md: seção 'Improbidade, ilegalidade e imoralidade' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “a perda da função pública e a suspensão dos direitos políticos” (11 palavras)
- AVISO a24-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “atos que atentam contra os princípios da administração pública art 11” (11 palavras)
- AVISO a24-s01.md: coincidência com a fonte (definição/norma? reescreva se puder): “dolo é a vontade livre e consciente de alcançar o resultado ilícito” (12 palavras)
- AVISO a24-s02.md: seção 'Sujeito ativo: duas categorias' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s02.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s03.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s03.md: coincidência com a fonte (definição/norma? reescreva se puder): “xii usar em proveito próprio bens rendas verbas ou valores” (10 palavras)
- AVISO a24-s03.md: coincidência com a fonte (definição/norma? reescreva se puder): “de bem ou serviço por preço superior ao de mercado” (10 palavras)
- AVISO a24-s04.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s04.md: coincidência com a fonte (definição/norma? reescreva se puder): “xxii conceder aplicar ou manter benefício financeiro ou tributário contrário” (10 palavras)
- AVISO a24-s04.md: coincidência com a fonte (definição/norma? reescreva se puder): “da autoridade nomeante ou de servidor da mesma pessoa jurídica” (10 palavras)
- AVISO a24-s05.md: seção 'Atos de menor ofensa' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s05.md: seção 'Como a banca cobra este assunto' com menos de 120 palavras: junte com outra ou desenvolva
- AVISO a24-s05.md: coincidência com a fonte (definição/norma? reescreva se puder): “a da efetiva ocorrência de dano ao patrimônio público salvo quanto” (11 palavras)
- AVISO a24-s05.md: coincidência com a fonte (definição/norma? reescreva se puder): “constar do cadastro nacional de empresas inidôneas e suspensas ceis” (10 palavras)
- AVISO mentoria_mc_direito-administrativo_008_c8f095: classificada no banco em direito-administrativo/a24/s01, você pôs em direito-administrativo/a24/s02

### Notas dos autores

### direito-administrativo/m22 (AGENTE-MATB-30)
- 0 erros; 18 avisos (seções curtas e coincidências de 10 a 15 palavras com dispositivos legais). Os arts. 1º a 3º, 7º a 12, 20 da Lei 8.429/1992 foram conferidos com `pipeline/leis.py art l8429 N`; `check_citations.py` não apontou citação inexistente.
- Pontos para o revisor conferir: (1) as decisões do STF nas ADIs 7156 e 7236 (interpretação conforme do art. 1º, § 8º; perda da função em todos os vínculos; proibição de contratar com todos os entes; inconstitucionalidade do art. 12, § 10; exigência de benefícios diretos para sócios no art. 3º, § 1º; constitucionalidade dos §§ 3º e 4º do art. 11) vêm do texto de apoio, que as data de 2026; o texto compilado em cache ainda mostra só as remissões "Vide ADI"; confirmar existência, data e alcance; (2) a tese do Tema 1199 (ARE 843.989), a Pet 3240, o ARE 1.484.966 e o REsp 2.107.601 foram resumidos de memória e do texto de apoio, sem consulta aos acórdãos; (3) a Súmula Vinculante 13 foi descrita em síntese; (4) a alíquota mínima de 2% do ISS e as exceções da LC 116/2003 vêm do texto de apoio; (5) o art. 11 foi descrito com os incisos III a VIII, XI e XII em vigor, e I, II, IX e X revogados, conforme o cache da lei; o art. 10, XIII, aparece no cache sem marca de revogação.
- Exemplos do texto de apoio (prefeito Jorge e ação rescisória, prescrição intercorrente de janeiro de 2017, mesário, vereador médico ou professor, entre outros) foram trocados por cenários próprios após comparação com a fonte.
- Fixação: 16 questões inéditas MentorIA do banco (0 AOCP). Descartadas as de Certo/Errado, as da Lei Anticorrupção, uma que cita a dosimetria do antigo parágrafo único do art. 12 (revogado) e duas sobre o alcance da perda da função pela redação original do art. 12, § 1º.
- A onda 1 está praticamente esgotada para a frente B; o próximo `material_ficha.py --lote 4 --onda 1 --frente B` deve voltar vazio. Seguir para `--onda 2` depende da instrução do usuário.

### Ferramentas e custo
- Sessão sem subagentes; capítulos escritos um a um, com validação a cada capítulo.
- Scripts auxiliares (fora do repositório): fix_da22.py gera o fixacao.json; p_m22c*.py aplicaram ajustes de texto.
- Nenhum arquivo .frente foi apagado ou editado; nenhum volume reservado por A ou C foi tocado; nada foi commitado nem gravado no banco.
- Este foi o sétimo lote de frente B da sessão (lotes 03 a 09), por autorização expressa do usuário ("Sim, lote 09").
