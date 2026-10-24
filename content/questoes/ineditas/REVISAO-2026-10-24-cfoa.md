# Revisão — Inéditas CBMPE CFOA (2º Tenente CFOA CBMPE) — 2026-10-24

Questões provisórias de múltipla escolha (padrão AOCP, 5 alternativas A–E) escritas para suprir as atividades do plano de estudos do concurso **2º Tenente CFOA CBMPE** enquanto as questões do TecConcursos não são importadas.

Gravadas em `content/questoes/ineditas/mc/<disciplina>.txt` e semeadas no banco de dados local com `batch = "mentoria-inedita-2026-10-24-cfoa"`.
- `pipeline/questoes/ineditas_mc_nativas.py --check`: **6.509 questões · 0 erros**.
- `pipeline/questoes/lacunas_cfoa.py --check`: **0 trechos < 7, 0 aulas < 25, faltam 0 questões**.

---

## 1. Quantidade de Inéditas Produzidas por Disciplina (1.333 questões no total)

| Disciplina | Total Escritas | Trechos Cobertos | Total no Arquivo `.txt` | Distribuição de Gabaritos (A / B / C / D / E) |
| :--- | :---: | :---: | :---: | :---: |
| **Administração** (`administracao`) | 233 | 26 trechos em 8 aulas | 233 | A: 47 · B: 47 · C: 47 · D: 46 · E: 46 |
| **Direito Processual Penal Militar** (`direito-processual-penal-militar`) | 228 | 15 trechos em 9 aulas | 228 | A: 46 · B: 45 · C: 46 · D: 46 · E: 45 |
| **Direito Administrativo** (`direito-administrativo`) | 192 | 73 trechos em 17 aulas | 603 | A: 120 · B: 120 · C: 121 · D: 121 · E: 121 |
| **Legislações PE** (`legislacoes-pe`) | 184 | 11 trechos em 9 aulas | 314 | A: 63 · B: 63 · C: 63 · D: 62 · E: 63 |
| **Direitos Humanos** (`direitos-humanos`) | 175 | 13 trechos em 7 aulas | 175 | A: 35 · B: 35 · C: 35 · D: 35 · E: 35 |
| **Direito Penal Militar** (`direito-penal-militar`) | 158 | 20 trechos em 7 aulas | 482 | A: 96 · B: 96 · C: 97 · D: 97 · E: 96 |
| **Língua Portuguesa** (`lingua-portuguesa`) | 91 | 30 trechos em 13 aulas | 341 | A: 68 · B: 68 · C: 68 · D: 69 · E: 68 |
| **Raciocínio Lógico** (`raciocinio-logico`) | 47 | 22 trechos em 8 aulas | 386 | A: 77 · B: 77 · C: 77 · D: 77 · E: 78 |
| **Direito Constitucional** (`direito-constitucional`) | 25 | 1 trecho (`a18/s01`) | 248 | A: 50 · B: 49 · C: 50 · D: 50 · E: 49 |
| **TOTAL** | **1.333** | **207 trechos em 85 aulas** | **6.509** | **Perfeitamente balanceado (~20% por letra)** |

---

## 2. Fontes e Normas Oficiais Conferidas

1. **Administração Geral e Pública**:
   - Doutrinas consagradas (Idalberto Chiavenato, Antonio Cesar Amaru Maximiano, Stephen Robbins, Henry Mintzberg, Edgar Schein, Kurt Lewin, Robert Katz).
   - Tipologias de liderança, teorias motivacionais, funções administrativas (PODC), processo decisório e estruturas organizacionais contemporâneas.

2. **Direito Processual Penal Militar**:
   - Decreto-Lei nº 1.002/1969 (Código de Processo Penal Militar - CPPM) atualizado.
   - Competência da Justiça Militar Estadual (art. 125, § 4º, da CF/88) vs. Justiça Militar da União.
   - Jurisprudência pacificada do STM e do STF (HC 127.900/AM sobre o interrogatório ao final da instrução criminal militar).
   - Inquérito Policial Militar (IPM), medidas assecuratórias, busca e apreensão, prisão preventiva militar, menagem e crime de deserção.

3. **Direitos Humanos**:
   - Declaração Universal dos Direitos Humanos (DUDH/1948) e estrutura do Pórtico de René Cassin.
   - Programa Nacional de Direitos Humanos (PNDH-1, PNDH-2 e PNDH-3 - Decreto nº 7.037/2009 com alterações do Decreto nº 7.177/2010).
   - Convenção sobre a Eliminação de Todas as Formas de Discriminação contra a Mulher (CEDAW - Decreto nº 4.377/2002) e Protocolo Facultativo.
   - Convenção Internacional sobre os Direitos das Pessoas com Deficiência (CDPD - Decreto nº 6.949/2009) incorporada com equivalência de Emenda Constitucional (art. 5º, § 3º, da CF/88).

4. **Direito Administrativo e Licitações**:
   - Lei nº 14.133/2021 (Nova Lei de Licitações e Contratos Administrativos).
   - Regime de desapropriação (Decreto-Lei nº 3.365/1941 e Lei nº 4.132/1962).
   - Conselho de Disciplina (Decreto Estadual nº 3.639/1975) e Conselho de Justificação (Lei Federal nº 5.836/1972).
   - Processo Administrativo Estadual de Pernambuco (Lei Estadual nº 11.781/2000).

5. **Direito Penal Militar e Legislação Extravagante**:
   - Decreto-Lei nº 1.001/1969 (CPM) com alterações das Leis nº 13.491/2017 e 14.688/2023.
   - Lei nº 13.869/2019 (Abuso de Autoridade).
   - Lei nº 7.716/1989 (Crimes de Preconceito de Raça ou de Cor) e equiparação da injúria racial pelo STF e pela Lei nº 14.532/2023.
   - Crimes contra as finanças públicas e licitações (arts. 337-E a 337-P do CP).

6. **Legislações Estaduais de Pernambuco**:
   - Lei Estadual nº 6.783/1974 (Estatuto dos Militares do Estado de Pernambuco).
   - Lei Estadual nº 11.817/2000 (Código Disciplinar dos Militares do Estado).
   - Decreto Estadual nº 22.114/2000 (Código de Ética dos Militares do Estado).
   - Lei Complementar Estadual nº 470/2021 (Critérios de Promoção dos Militares do Estado).
   - Lei Estadual nº 13.314/2007 (Prevenção e punição ao assédio moral e sexual no âmbito estadual).
   - Lei Federal nº 12.527/2011 (Lei de Acesso à Informação - LAI).

---

## 3. Dúvidas e Observações para o Dono (Pontos de Atenção)

1. **Provisórias até a chegada do TecConcursos**:
   - Conforme diretriz do projeto, todas as 1.333 questões são inéditas de múltipla escolha autorais da MentorIA.
   - Quando as questões reais do TecConcursos forem importadas pelo dono na fase posterior, poderá ser executada a rotina `questoes-ineditas.ts --aposentar --simular` para verificar quais trechos já atingiram o piso com questões de bancas reais, atentando-se à ressalva do CBMPE (não aposentar se for reabrir cadernos curtos).

2. **Conselho de Disciplina e de Justificação**:
   - O Decreto Estadual nº 3.639/1975 regula o Conselho de Disciplina para Aspirantes e praças estáveis no âmbito da PMPE e CBMPE. O Conselho de Justificação segue a Lei Federal nº 5.836/1972 para Oficiais, cabendo a decisão final de perda de posto/patente e perda de graduação ao Tribunal de Justiça de Pernambuco (TJPE), conforme o art. 125, § 4º, da CF/88 (já que PE não possui Tribunal Militar de 2ª instância estadual). As questões refletem essa jurisprudência uniforme.

3. **Alterações Penais e Militares Recentes**:
   - A Lei nº 14.688/2023 reformou partes substantivas da Parte Geral do CPM (penas, prescrição, exclusão de ilicitude); as questões foram calibradas de acordo com a redação em vigor em outubro de 2026.
   - A Lei nº 14.133/2021 revogou os tipos penais da antiga Lei 8.666/93 e inseriu os arts. 337-E a 337-P no Código Penal; as questões de crimes licitatórios em `direito-penal-militar/c02` baseiam-se exclusivamente nos arts. 337-E a 337-P do CP.
