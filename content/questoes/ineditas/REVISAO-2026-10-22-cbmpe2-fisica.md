# Revisão 2026-10-22 — inéditas de múltipla escolha, segunda rodada (CBMPE Oficial) — Física (fisica2)

Gravadas em `content/questoes/ineditas/mc/fisica.txt` pela ferramenta `ineditas_append.py` (correta embaralhada e balanceada; letras finais A 73, B 72, C 72, D 73, E 73). `ineditas_mc_nativas.py --check` termina com erros 0 e `lacunas_cbmpe_aula.py --lista fisica` não lista nenhuma aula abaixo de 25. Total escrito: **212 questões em 18 aulas**, exatamente o pedido no CSV.

## Quantidade por aula e trecho

| Aula | Trecho (qtde) | Total |
| --- | --- | --- |
| a00 | s01 (6), s02 (5) | 11 |
| a01 | s01 (6), s02 (5) | 11 |
| a02 | s01 (6), s02 (5) | 11 |
| a03 | s02 (1), s03 (1) | 2 |
| a04 | s01 (6), s02 (5) | 11 |
| a05 | s01 (1) | 1 |
| a06 | s01 (6), s02 (5) | 11 |
| a07 | s01 (2), s02 (5) | 7 |
| a08 | s01 (6), s02 (5) | 11 |
| a09 | s01 (18) | 18 |
| a10 | s01 (6), s02 (2) | 8 |
| a12 | s01 (18) | 18 |
| a14 | s01 (6), s02 (5) | 11 |
| a15 | s01 (18) | 18 |
| a16 | s01 (6), s02 (5) | 11 |
| a17 | s01 (18) | 18 |
| c01 | s01 (18) | 18 |
| c02 | s01 (16) | 16 |

## Método de conferência

- Cada conta foi feita por dois caminhos (fórmula direta e conferência por outra relação, grandeza auxiliar ou razão), e o segundo caminho aparece, quando cabe, no comentário. Unidades convertidas ao SI; sem figuras (gráficos descritos em texto); π = 3 só onde o enunciado manda adotá-lo.
- Os tópicos foram escolhidos fora dos já cobertos pelas inéditas anteriores do trecho (lidos antes de escrever): por exemplo, na a09 e na a12 entraram Kepler (1ª, 2ª e 3ª), velocidade orbital, energia potencial e velocidade de escape; Fourier em cinco variações, convecção, brisa, calor específico e irradiação.
- Distratores baseados em erros típicos (esquecer o quadrado, não converter unidade, inverter razão, somar em vez de compor vetores).

## Dúvidas e observações para o dono

1. **Escopo na a12 (condução/convecção/irradiação):** uma questão usa a lei de Stefan-Boltzmann (potência irradiada proporcional a T⁴), que não aparece no resumo do trecho, embora seja conteúdo usual de irradiação. Se preferir manter estritamente ao resumo, trocar essa questão.
2. **Escopo na a09:** além de Kepler e gravitação (no resumo), há questões de velocidade orbital e relação v_escape = √2·v_orbital rasante; constam do tópico "Corpos em órbita"/"Velocidade de escape" do trecho.
3. **c02 (tópicos sem cobertura no curso):** as questões de marés, estações, El Niño, albedo e Hubble seguem o resumo do complemento; o valor H = 70 km/s/Mpc é aproximado (a literatura vai de ~67 a ~73) e o enunciado o fornece, então não há risco de ambiguidade no gabarito.
4. **c01:** as contas de óptica usam a convenção de sinais de Gauss (f > 0 para côncavo/convergente, p' < 0 para imagem virtual), a mesma do resumo.
5. **a17:** as contas deixam o resultado em múltiplos de π, com μ0 = 4π·10⁻⁷ T·m/A dado no enunciado, para evitar aproximações.
6. Nenhuma questão antiga precisou ser trocada; nada foi editado à mão nos `.txt`.
