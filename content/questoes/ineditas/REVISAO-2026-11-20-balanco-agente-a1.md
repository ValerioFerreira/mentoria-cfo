# Balanço de Produção — Lote A (Parte 1): Direito Processual Penal Militar (`a00/s01` a `a08/s01`)

**Agente:** `agente-a1` / `agente-a1-cont`
**Disciplina:** `direito-processual-penal-militar`
**Arquivo-alvo:** `content/questoes/ineditas/mc/direito-processual-penal-militar.txt` (gravado exclusivamente via `pipeline/pcpe_tools/ineditas_append.py`)
**Base legal consultada:** Código de Processo Penal Militar (Decreto-Lei nº 1.002/1969, via `pipeline/leis.py`), Constituição Federal de 1988, Lei nº 8.457/1992 (alterada pela Lei nº 13.774/2018), Lei nº 13.869/2019 e resumos de `pipeline/pcpe_tools/seg_summary.py`.

## Resumo Quantitativo — Parte 1 (`a00/s01` a `a08/s01`)

| Trecho | Tema Principal | Adicionadas (`agente-a1`) | Adicionadas (`agente-a1-cont`) | Total Adicionado | Total Final no Arquivo | Comando `INCORRETA` (adicionadas) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `a00/s01` | Processo Penal Militar em Geral e Aplicação da Lei (arts. 1º a 6º) | 16 | — | 16 | 41 | 4 (25,0%) |
| `a01/s01` | Polícia Judiciária Militar (arts. 7º e 8º) | 16 | — | 16 | 41 | 4 (25,0%) |
| `a02/s01` | Inquérito Policial Militar — Parte I (arts. 9º a 17) | 28 | — | 28 | 41 | 6 (21,4%) |
| `a02/s02` | Inquérito Policial Militar — Parte II (arts. 18 a 28) | 29 | — | 29 | 41 | 7 (24,1%) |
| `a06/s01` | Competência da Justiça Militar: Foro, Lugar da Infração e Domicílio (arts. 82 a 98) | 27 | 1 | 28 | 41 | 6 (21,4%) |
| `a06/s02` | Sede de Serviço, Prerrogativa, Conexão, Continência, Desaforamento e Conflitos (arts. 94 a 112) | — | 29 | 29 | 41 | 6 (20,7%) |
| `a07/s01` | Incidentes de Insanidade Mental e de Falsidade Documental (arts. 156 a 169) | — | 16 | 16 | 41 | 3 (18,8%) |
| `a08/s01` | Medidas Preventivas e Assecuratórias: Busca, Apreensão e Restituição (arts. 170 a 198) | — | 30 | 30 | 37 | 8 (26,7%) |
| **Total Parte 1** | **`a00/s01` a `a08/s01`** | **116** | **76** | **192** | **324** | **44 (22,9%)** |

## Cobertura da Retomada (`agente-a1-cont`, 76 questões)

- **`a06/s01` (+1 questão):** caso concreto com comando `INCORRETA` sobre coautoria entre civil e bombeiro militar da ativa contra patrimônio de quartel estadual (limitação do art. 125, § 4º, CF, monopólio da JMU sobre civis e separação obrigatória do art. 102, "a", CPPM).
- **`a06/s02` (+29 questões):** art. 94 (prevenção pré-denúncia), art. 95 (infração permanente/continuada e múltiplas residências), art. 96 (alcance subjetivo da sede de serviço), art. 97, parágrafo único (corporações diferentes e prevalência do oficial da ativa), art. 98 (distribuição e prevenção), arts. 99 e 100 (espécies de conexão e continência), art. 101 (prevalência da especializada e maior graduação), art. 102 e parágrafo único (separação obrigatória e concurso militar/comum), arts. 103 e 104 (prorrogação e *perpetuatio jurisdictionis*), arts. 105 e 106 (separação de julgamentos vs. processos e recurso de ofício em traslado sem efeito suspensivo), art. 107 (avocação e sentença definitiva), art. 108 e Lei 8.457/1992 / Lei 13.774/2018 (prerrogativa, Juiz Federal da JM para civis, Conselho Especial mesmo após exclusão do oficial), arts. 109 e 110 (legitimados, procedimento e renovação do desaforamento) e arts. 111 e 112 (exceção e modalidades de conflito, inclusive inciso II).
- **`a07/s01` (+16 questões):** art. 157 (internação preso/solto, prazo prorrogável de 45 dias e entrega dos autos aos peritos no processo e no IPM), art. 158 (sustação parcial de provas), art. 159 e parágrafo único (quesitos obrigatórios e embriaguez por caso fortuito/força maior), art. 160 (não vinculação automática do juiz ao laudo), art. 161, § 2º (reinquirição após restabelecimento), art. 162, §§ 1º e 2º (corréus e encerramento do IPM sem laudo), arts. 163 a 169 (juízo de necessidade, arguição oral por termo, tríduo probatório, documento de outro juízo, sustação facultativa, poderes especiais, irrecorribilidade e ausência de coisa julgada penal).
- **`a08/s01` (+30 questões):** busca domiciliar e pessoal (arts. 170 a 184: finalidades, conceito de casa e exclusões, horário e Lei 13.869/2019, reserva de jurisdição na CF/88 vs. arts. 176-177, requisitos do mandado, ausência do morador e casa desabitada, rompimento com menor dano/serralheiro e reposição, execução por oficial de justiça ou oficial no IPM respeitada a hierarquia, requisição à polícia civil), apreensão (arts. 185 a 189: armas de uso exclusivo, correspondência aberta ou fechada, proteção do documento com defensor salvo corpo de delito, seguimento em outra jurisdição e apresentação posterior por urgência, auto circunstanciado com duas testemunhas e especificações do anexo) e restituição de coisas apreendidas (arts. 190 a 198: bens irrestituíveis e produto do crime, requisitos do art. 191, direito duvidoso e alta indagação no juízo cível, terceiro de boa-fé e prazos de 5 e 3 dias, depositário idôneo, oitiva obrigatória do MP e recurso com efeito suspensivo, bens deterioráveis, destinação em 90 dias após sentença condenatória ou absolutória e juiz de ausentes).

## Validação Técnica

- Comando executado: `pipeline/.venv/Scripts/python pipeline/questoes/ineditas_mc_nativas.py --check content/questoes/ineditas/mc/direito-processual-penal-militar.txt`
- Resultado: **`TOTAL 578 · erros 0`**
- Distribuição final de gabaritos no arquivo completo: `A 115 · B 116 · C 116 · D 116 · E 115` (equilíbrio perfeito).
- Todos os rascunhos preservados em `C:\Users\Administrador\.gemini\antigravity\brain\c28c4a66-3966-4c2e-b895-c0c451b94f33\scratch\agentes\agente-a1\`.
