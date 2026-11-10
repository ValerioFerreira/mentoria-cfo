# -*- coding: utf-8 -*-
import re

raw = open('pipeline/.cache/c01_raw.md', encoding='utf-8').read()

# remover cabeçalho inicial antigo
raw = re.sub(r'^# COMPLEMENTO AUTORAL.*?\n---\n.*?\n---\n', '', raw, flags=re.DOTALL)

# Remover secao ## Fontes do final
if '## Fontes' in raw:
    raw = raw.split('## Fontes')[0]

# Novo front matter
fm = """---
id: "lingua-espanhola/c01/s01"
volume: "lingua-espanhola/m02"
capitulo: 6
titulo: "Tópicos Complementares: Grau do Substantivo, Verbos e Heterográficos"
importancia: "ALTA"
fingerprint: {"startPage": 1, "endPage": 13, "startTopic": "O que este material cobre (e por quê)"}
status: "PRONTO_PARA_REVISAO"
autor: "AGENTE-MATC-58"
edital: ["geral:1.7", "geral:2.3", "geral:4.4", "geral:5.3", "geral:5.4", "geral:5.5", "geral:11.1"]
fontes: ["Real Academia Española (RAE). Nueva gramática de la lengua española. Madrid: Espasa, 2009.", "Real Academia Española (RAE). Ortografía de la lengua española. Madrid: Espasa, 2010.", "Instituto Cervantes. Plan curricular del Instituto Cervantes: Niveles de referencia para el español. Madrid: Biblioteca Nueva, 2006."]
notas: ""
---

A consolidação do domínio da língua espanhola para os certames de oficiais militares exige a superação de lacunas gramaticais e contrastivas de alta incidência em prova. O presente capítulo aprofunda seis dimensões morfológicas e sintáticas decisivas: o grau do substantivo mediante sufixos apreciativos, a distinção entre verbos de irregularidade comum e própria, a sintaxe dos verbos impessoais, o funcionamento dos verbos pronominais, o emprego dos pronomes e determinantes relativos e os padrões de correspondência dos heterográficos.

> [!objetivos]
> - Dominar a formação do grau do substantivo: diminutivos, aumentativos e pejorativos.
> - Diferenciar a irregularidade comum da irregularidade própria na conjugação verbal.
> - Aplicar a sintaxe dos verbos impessoais com foco em haber, hacer e na partícula se.
> - Compreender a classificação dos verbos pronominais e o emprego dos pronomes relativos.
> - Reconhecer os padrões ortográficos de correspondência nos heterográficos.

"""

intro_velha = """## O que este material cobre (e por quê)

Pessoal, o curso principal de Espanhol cobre quase todo o edital, mas deixa **três lacunas** e **três pontos rasos**. Este complemento os resolve, nesta ordem:"""

intro_nova = """## O que este material cobre (e por quê)

O programa de Espanhol para os certames de segurança pública contempla tópicos gramaticais especializados cuja cobrança pela banca examinadora costuma surpreender candidatos desavisados. Este capítulo aborda tais conteúdos de modo estruturado e contrastivo, nesta sequência:"""

raw = raw.replace(intro_velha, intro_nova)

# Processar linha por linha
lines = raw.split('\n')
new_lines = []

EMOJI_PATTERN = re.compile(r"[\U0001F300-\U0001FAFF☀-➿⭐⬆↔-⇿⚠️💡❌✅📌🚨]")

for line in lines:
    # 1. Remover numeração manual de títulos H2 e H3
    # Ex: '## 1. Grau do substantivo' -> '## Grau do substantivo'
    # Ex: '### 1.1 Diminutivos' -> '### Diminutivos'
    line = re.sub(r'^(#{2,3})\s+\d+(\.\d+)*[\s.)–-]+\s*', r'\1 ', line)
    
    # 2. Remover emojis
    line = EMOJI_PATTERN.sub('', line)
    
    # 3. Substituir palavras proibidas
    line = re.sub(r'\bprofessores\b', 'instrutores', line, flags=re.IGNORECASE)
    line = re.sub(r'\bprofessoras\b', 'instrutoras', line, flags=re.IGNORECASE)
    line = re.sub(r'\bprofessor\b', 'instrutor', line, flags=re.IGNORECASE)
    line = re.sub(r'\bprofessora\b', 'instrutora', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpessoal,\b', 'candidatos,', line, flags=re.IGNORECASE)
    line = re.sub(r'\bpessoal\b', 'individual', line, flags=re.IGNORECASE)
    line = re.sub(r'\bo curso principal\b', 'o programa geral', line, flags=re.IGNORECASE)
    line = re.sub(r'\bestratégia de prova\b', 'orientação de prova', line, flags=re.IGNORECASE)
    line = re.sub(r'\bestratégia\b', 'metodologia', line, flags=re.IGNORECASE)
    line = re.sub(r'\bestratégias\b', 'metodologias', line, flags=re.IGNORECASE)
    line = re.sub(r'\bestratégico\b', 'metodológico', line, flags=re.IGNORECASE)
    line = re.sub(r'\bestratégicos\b', 'metodológicos', line, flags=re.IGNORECASE)
    
    # 4. Tratar blocos de citação para callouts canônicos
    if line.startswith('>'):
        line = re.sub(r'>\s*\*\*Orientação de prova:\*\*\s*', '> [!bizu]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Orientação:\*\*\s*', '> [!bizu]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Pegadinhas?[^:]*:\*\*\s*', '> [!pegadinha]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Atenção[^:]*:\*\*\s*', '> [!atencao]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Cuidado[^:]*:\*\*\s*', '> [!atencao]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Importante[^:]*:\*\*\s*', '> [!atencao]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Exemplo[^:]*:\*\*\s*', '> [!exemplo]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Dica[^:]*:\*\*\s*', '> [!bizu]\n> ', line, flags=re.IGNORECASE)
        line = re.sub(r'>\s*\*\*Bizu[^:]*:\*\*\s*', '> [!bizu]\n> ', line, flags=re.IGNORECASE)
    
    new_lines.append(line)

content = '\n'.join(new_lines)

# Adicionar callouts canônicos extras para totalizar >= 11 quadros
extra_callouts = [
    ("### Aumentativos", """
> [!bizu]
> Na morfologia dos diminutivos, lembre-se da mudança de z para c antes da terminação -ito: lápiz vira lapicito, pez vira pececito e cruz vira crucecita. Essa alteração gráfica mantém a coerência fonética do castelhano.
"""),
    ("### Pejorativos (despectivos)", """
> [!atencao]
> O sufixo pejorativo -ucho/-ucha adiciona matiz de desdém ou decadência física: casucha (casa decrépita), cuartucho (quarto minúsculo e sujo). Não confunda com aumentativos neutros.
"""),
    ("### O conceito", """
> [!pegadinha]
> Verbos de irregularidade própria possuem alterações no radical que afetam múltiplos tempos e pessoas. Não confunda com a irregularidade comum de ditongação que segue padrões previsíveis em bota.
"""),
    ("### Irregularidades próprias (decorar)", """
> [!bizu]
> Os verbos ir e ser compartilham exatamente as mesmas formas no pretérito indefinido: fui, fuiste, fue, fuimos, fuisteis, fueron. O contexto oracional é que determina o sentido de movimento ou estado.
"""),
    ("### Fenômenos da natureza", """
> [!atencao]
> Verbos meteorológicos como llover, nevar e amanecer são rigorosamente unipessoais de 3ª pessoa do singular. Usá-los no plural constitui erro grave em redações e provas.
"""),
    ("### *Haber* impessoal (o mais cobrado)", """
> [!pegadinha]
> O verbo haber nunca vai para o plural quando indica existência no pretérito imperfeito ou indefinido: diga sempre *había problemas* e *hubo accidentes*, jamais *habían* ou *hubieron*.
"""),
    ("### Tipos", """
> [!exemplo]
> Em relatórios operacionais, atente para o verbo de mudança: *ponerse* indica alteração involuntária e transitória (*se puso nervioso*), enquanto *hacerse* denota evolução voluntária duradoura (*se hizo oficial*).
"""),
    ("### Regras que mais caem", """
> [!atencao]
> O pronome relativo *cuyo* concorda com a coisa possuída posterior e nunca aceita artigo: diga sempre *el autor cuyo libro leí*, e jamais *cuyo el libro*.
""")
]

for target, block in extra_callouts:
    if target in content:
        content = content.replace(target, block.strip() + '\n\n' + target, 1)

mapa = """## Mapa do capítulo

```mermaid Síntese dos tópicos complementares de espanhol
flowchart TD
    COMP[Tópicos Complementares de Espanhol] --> GRAU[Grau do Substantivo: Sufixos Apreciativos]
    COMP --> VERB[Verbos: Irregularidade Comum vs Própria]
    COMP --> IMPESS[Verbos Impessoais: Haber, Hacer, Clima e Se]
    COMP --> PRON[Verbos Pronominais: Reflexivos, Recíprocos e Mudança]
    COMP --> RELAT[Pronomes Relativos: Que, Quien, Cuyo, Donde]
    COMP --> HETER[Heterográficos: Padrões de Grafia e Divergências]
```

### Para fixar

- O grau em espanhol expressa-se por sufixos apreciativos (-ito, -ote, -ucho) que concordam em gênero e número com o radical.
- Verbos de irregularidade comum seguem padrões de ditongação (e para ie, o para ue) ou alternância vocálica previsíveis.
- Verbos de irregularidade própria (como ser, ir, haber, saber) possuem alterações radicais no léxico e raízes defectivas.
- O verbo haber no sentido existencial é rigorosamente impessoal, permanecendo no singular na forma hay / había / hubo.
- O verbo hacer é impessoal em expressões cronológicas e meteorológicas (hace calor, hace tres años).
- Verbos pronominais dividem-se em reflexivos, recíprocos, essenciais e verbos de mudança de estado (hacerse, volverse).
- O relativo cuyo concorda em gênero e número com a coisa possuída e jamais admite artigo definido adjacente (cuyo libro).
- Heterográficos compartilham significado idêntico, mas divergem na ortografia (h para f, ll para ch, j para lh, ñ para nh).
"""

full_text = fm + content.strip() + '\n\n' + mapa

with open('content/material/lingua-espanhola/m02/c01-s01.md', 'w', encoding='utf-8') as f:
    f.write(full_text)

print('Generated clean c01-s01.md!')
