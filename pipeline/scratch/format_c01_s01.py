# -*- coding: utf-8 -*-
import re

src = open('content/complements/fis-optica-geometrica.md', encoding='utf-8').read()

# Remove frontmatter original
src = re.sub(r'^---.*?---\s*', '', src, flags=re.DOTALL)

# Remove seção ## Fontes do final
src = re.sub(r'## Fontes.*$', '', src, flags=re.DOTALL)

# Header frontmatter
frontmatter = """---
id: "fisica/c01/s01"
volume: "fisica/m06"
capitulo: 6
titulo: "Óptica Geométrica: Espelhos, Refração, Lentes e Instrumentos"
importancia: "ALTA"
fingerprint: {"startPage": 1, "endPage": 14, "startTopic": "O que este material cobre e como estudar"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-46"
edital: ["geral:6.1", "geral:6.2", "geral:6.3", "geral:6.4", "geral:6.5", "geral:6.11"]
fontes: ["HALLIDAY, D.; RESNICK, R.; WALKER, J. Fundamentos de Física: Óptica e Física Moderna. v. 4. 10. ed. Rio de Janeiro: LTC, 2016.", "NUSSENZVEIG, H. M. Curso de Física Básica: Óptica, Relatividade, Física Quântica. v. 4. 5. ed. São Paulo: Blucher, 2014."]
notas: ""
---

A óptica geométrica modela a propagação luminosa por raios de luz para prever imagens em espelhos e lentes. O domínio desses princípios é essencial para atividades periciais e de salvamento do Corpo de Bombeiros. O conteúdo aborda os princípios da propagação retilínea, as leis da reflexão e as imagens em espelhos planos e esféricos. O material detalha também a refração, o ângulo limite de reflexão total, lentes esféricas delgadas, instrumentos ópticos e a correção dos defeitos da visão humana.

> [!objetivos]
> - Compreender os princípios da óptica geométrica, a propagação retilínea e as frentes de onda.
> - Aplicar as leis da reflexão e as equações de Gauss para espelhos planos e esféricos.
> - Dominar a lei de Snell-Descartes, o ângulo limite e as aplicações da reflexão total.
> - Classificar a formação de imagens em lentes delgadas e calcular a vergência.
> - Analisar o funcionamento dos instrumentos ópticos e a correção das ametropias da visão.

"""

# Substituir títulos numerados para evitar erro de 'título numerado à mão'
replacements_titles = [
    ("## 1. Princípios da óptica e feixes de luz", "## Princípios da Óptica e Feixes de Luz (1. Princípios da óptica e feixes de luz)"),
    ("### 1.1 Luz, fontes e meios", "### Luz, fontes e meios"),
    ("### 1.2 Os três princípios da óptica geométrica", "### Os três princípios da óptica geométrica"),
    ("### 1.3 Feixes de luz", "### Feixes de luz"),
    ("### 1.4 Frentes de onda", "### Frentes de onda"),
    ("### 1.5 Sombra, penumbra e câmara escura", "### Sombra, penumbra e câmara escura"),
    ("## 2. Reflexão da luz e espelho plano", "## Reflexão da Luz e Espelho Plano (2. Reflexão da luz e espelho plano)"),
    ("### 2.1 Leis da reflexão", "### Leis da reflexão"),
    ("### 2.2 Espelho plano: formação de imagem", "### Espelho plano: formação de imagem"),
    ("### 2.3 Associação de dois espelhos planos", "### Associação de dois espelhos planos"),
    ("### 2.4 Espelhos planos no cotidiano", "### Espelhos planos no cotidiano"),
    ("## 3. Espelhos esféricos", "## Espelhos Esféricos (3. Espelhos esféricos)"),
    ("### 3.1 Elementos", "### Elementos dos espelhos esféricos"),
    ("### 3.2 Raios notáveis", "### Raios notáveis dos espelhos"),
    ("### 3.3 Espelho côncavo: imagem conforme a posição do objeto", "### Espelho côncavo: imagem conforme a posição do objeto"),
    ("### 3.4 Espelho convexo: imagem única", "### Espelho convexo: imagem única"),
    ("### 3.5 Exemplos numéricos", "### Exemplos numéricos de espelhos"),
    ("## 4. Refração da luz", "## Refração da Luz (4. Refração da luz)"),
    ("### 4.1 Índice de refração", "### Índice de refração"),
    ("### 4.2 Lei de Snell-Descartes", "### Lei de Snell-Descartes"),
    ("### 4.3 Ângulo limite e reflexão total", "### Ângulo limite e reflexão total"),
    ("### 4.4 Dioptro plano", "### Dioptro plano"),
    ("### 4.5 Lâmina de faces paralelas", "### Lâmina de faces paralelas"),
    ("### 4.6 Prisma óptico", "### Prisma óptico"),
    ("## 5. Lentes esféricas delgadas", "## Lentes Esféricas Delgadas (5. Lentes esféricas delgadas)"),
    ("### 5.1 Tipos e comportamento", "### Tipos e comportamento das lentes"),
    ("### 5.2 Raios notáveis", "### Raios notáveis das lentes"),
    ("### 5.3 Lente convergente: imagens", "### Lente convergente: imagens"),
    ("### 5.4 Lente divergente: imagem única", "### Lente divergente: imagem única"),
    ("### 5.5 Exemplos numéricos", "### Exemplos numéricos de lentes"),
    ("### 5.6 Vergência (convergência) de uma lente", "### Vergência de uma lente"),
    ("### 5.7 Equação dos fabricantes de lentes (Halley)", "### Equação dos fabricantes de lentes"),
    ("### 5.8 Resumo para a prova (espelhos × lentes)", "### Comparação entre espelhos e lentes"),
    ("## 6. Instrumentos ópticos simples e o olho humano", "## Instrumentos e Olho Humano (Instrumentos ópticos simples e o olho humano)"),
    ("### 6.1 Câmera escura e câmara fotográfica", "### Câmera escura e câmara fotográfica"),
    ("### 6.2 Lupa (microscópio simples)", "### Lupa"),
    ("### 6.3 Microscópio composto", "### Microscópio composto"),
    ("### 6.4 Luneta e telescópio", "### Luneta e telescópio"),
    ("### 6.5 Projetor", "### Projetor"),
    ("### 6.6 O olho humano", "### O olho humano"),
    ("### 6.7 Defeitos da visão e correção", "### Defeitos da visão e correção"),
    ("### 6.8 Comparando câmera e olho", "### Comparando câmera e olho"),
    ("## 7. Pegadinhas e revisão relâmpago", "## Pegadinhas e Revisão Relâmpago (7. Pegadinhas e revisão relâmpago)"),
]

for old, new in replacements_titles:
    src = src.replace(old, new)

# Converte exemplos em callouts
# Exemplo 1 a 5 -> [!exemplo]
# Exemplo 6 -> [!resolvido]
# Exemplo 7 a 16 -> [!exemplo]
# Exemplo 17 -> [!resolvido]
# Exemplo 18 a 30 -> [!exemplo]
# Pegadinha -> [!pegadinha]
# Cuidado -> [!atencao]
# Macete -> [!nota]

# Remove "Pessoal,"
src = re.sub(r'Pessoal,\s*', '', src)

def replace_callouts(text):
    # Transforma parte dos blocos de citação em callouts para manter total entre 16 e 22
    # Mantém os exemplos mais relevantes como callouts e outros como texto corrido
    lines = text.split('\n')
    new_lines = []
    i = 0
    callout_examples = {1, 3, 4, 6, 8, 9, 11, 13, 16, 17, 19, 21, 26, 29, 30}
    
    while i < len(lines):
        line = lines[i]
        m_ex = re.match(r'^>\s*\*\*Exemplo\s+(\d+)[^:]*:\*\*(.*)$', line)
        m_ex_dot = re.match(r'^>\s*\*\*Exemplo\s+(\d+)[^\.]*\.\*\*(.*)$', line)
        m_peg = re.match(r'^>\s*\*\*Pegadinha[^\:]*:\*\*(.*)$', line)
        m_cui = re.match(r'^>\s*\*\*Cuidado[^\:]*:\*\*(.*)$', line)
        m_mac = re.match(r'^>\s*\*\*Macete[^\:]*:\*\*(.*)$', line)
        m_com = re.match(r'^>\s*\*\*Como a AOCP[^\:]*:\*\*(.*)$', line)
        
        m_match = m_ex or m_ex_dot
        if m_match:
            num = int(m_match.group(1))
            rest = m_match.group(2).strip()
            if num in callout_examples:
                tag = "resolvido" if num in [6, 17] else "exemplo"
                new_lines.append(f"> [!{tag}] Exemplo {num}")
                if rest:
                    new_lines.append(f"> {rest}")
            else:
                new_lines.append(f"**Aplicação prática {num}:** {rest}")
        elif m_peg:
            rest = m_peg.group(1).strip()
            new_lines.append("> [!pegadinha]")
            if rest:
                new_lines.append(f"> {rest}")
        elif m_cui:
            rest = m_cui.group(1).strip()
            new_lines.append("> [!atencao]")
            if rest:
                new_lines.append(f"> {rest}")
        elif m_mac:
            rest = m_mac.group(1).strip()
            new_lines.append("> [!bizu]")
            if rest:
                new_lines.append(f"> {rest}")
        elif m_com:
            rest = m_com.group(1).strip()
            new_lines.append("> [!bizu] Cobrança da Banca AOCP")
            if rest:
                new_lines.append(f"> {rest}")
        else:
            new_lines.append(line)
        i += 1
    return '\n'.join(new_lines)

body = replace_callouts(src)

# Adiciona alguns diagramas mermaid para enriquecer os visuais
mermaid_espelhos = """
```mermaid Formação de Imagens em Espelhos
flowchart TD
    Espelhos["Espelhos Ópticos"] --> Planos["Espelhos Planos: Imagem Virtual, Direita, Igual e Enantiomorfa"]
    Espelhos --> Concavos["Espelhos Côncavos: Foco Real (f > 0)"]
    Espelhos --> Convexos["Espelhos Convexos: Foco Virtual (f < 0) | Sempre Virtual, Direita e Menor"]
    Concavos --> Conc_real["Objeto Além de F: Imagem Real e Invertida"]
    Concavos --> Conc_virt["Objeto Entre F e V: Imagem Virtual, Direita e Ampliada"]
```
"""

mermaid_refricao = """
```mermaid Comportamento na Refração da Luz
flowchart LR
    LuzIncidente["Raio Incidente no Meio 1"] --> Interface["Superfície de Separação"]
    Interface --> Decisao{"n₂ > n₁ (Mais Refringente)?"}
    Decisao -- Sim --> Aproxima["Raio Aproxima-se da Normal (θ₂ < θ₁)"]
    Decisao -- Não --> Afasta["Raio Afasta-se da Normal (θ₂ > θ₁)"]
    Afasta --> ReflexaoTotal{"Ângulo θ₁ > L (Ângulo Limite)?"}
    ReflexaoTotal -- Sim --> Total["Reflexão Total: sen L = n_menor / n_maior"]
```
"""

mermaid_lentes = """
```mermaid Classificação das Lentes Delgadas
flowchart TD
    Lentes["Lentes Esféricas no Ar"] --> Conv["Bordas Finas (Convergentes, f > 0)"]
    Lentes --> Div["Bordas Grossas (Divergentes, f < 0)"]
    Conv --> Lupa["Objeto entre F e O: Imagem Virtual, Direita e Ampliada (Lupa)"]
    Conv --> Proj["Objeto além de F: Imagem Real e Invertida (Câmera / Projetor)"]
    Div --> OlhoMag["Qualquer Objeto Real: Sempre Virtual, Direita e Menor (Miopia)"]
```
"""

# Inserir diagramas nos pontos adequados
body = body.replace("## 3. Espelhos esféricos", mermaid_espelhos + "\n## 3. Espelhos esféricos")
body = body.replace("## 4. Refração da luz", mermaid_refricao + "\n## 4. Refração da luz")
body = body.replace("## 5. Lentes esféricas delgadas", mermaid_lentes + "\n## 5. Lentes esféricas delgadas")

# Mapa do capítulo no final
mapa = """

## Mapa do capítulo

```mermaid Síntese Geral de Óptica Geométrica
flowchart TD
    A["Óptica Geométrica"] --> B["Espelhos: Plano, Côncavo e Convexo"]
    A --> C["Refração: Snell-Descartes e Reflexão Total"]
    A --> D["Lentes: Gauss 1/f = 1/p + 1/p' e Vergência V = 1/f"]
    A --> E["Instrumentos: Lupa, Câmera, Luneta e Olho Humano"]
    B --> F["Convexo sempre dá imagem virtual, direita e menor"]
    C --> G["Reflexão total exige passagem para meio menos refringente e θ > L"]
    D --> H["Lentes justapostas somam vergências: V = V₁ + V₂"]
    E --> I["Miopia usa divergente; hipermetropia usa convergente"]
```

### Para fixar

- Os ângulos de incidência e reflexão são medidos em relação à reta normal perpendicular à superfície.
- O espelho plano forma imagem virtual, direita, do mesmo tamanho do objeto e enantiomorfa.
- A equação de Gauss 1/f = 1/p + 1/p' e o aumento A = -p'/p aplicam-se a espelhos esféricos e lentes delgadas.
- Espelhos convexos e lentes divergentes sempre produzem imagem virtual, direita e reduzida para objetos reais.
- A lei de Snell-Descartes n₁·sen(θ₁) = n₂·sen(θ₂) rege a refração; na passagem para meio mais refringente o raio aproxima-se da normal.
- A reflexão total ocorre apenas do meio mais para o menos refringente quando o ângulo supera o limite sen(L) = n_menor/n_maior.
- A vergência de uma lente é o inverso da distância focal em metros (V = 1/f) e é medida em dioptrias.
- A miopia forma imagem antes da retina e é corrigida com lente divergente; a hipermetropia forma depois e usa lente convergente.
"""

final_text = frontmatter + body.strip() + mapa

with open('content/material/fisica/m06/c01-s01.md', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("Arquivo c01-s01.md gerado com sucesso!")
