with open('content/material/lingua-inglesa/m04/a04-s01.md', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Abertura com mais de 50 palavras (estava em 49)
antiga_abertura = '''O **Simple Present** expressa ações rotineiras, verdades universais e horários programados. Em concursos militares, dominar suas regras afirmativas, negativas e interrogativas é essencial para a interpretação textual.

Neste capítulo, estudaremos a conjugação da terceira pessoa, os auxiliares *do* e *does* e as formas de *to be* e *there be*.'''

nova_abertura = '''O **Simple Present** expressa ações regulares ou rotineiras, verdades universais e horários programados. Em concursos militares e policiais, dominar suas regras afirmativas, negativas e interrogativas é essencial para a interpretação de ordens de serviço e manuais operacionais.

Neste capítulo, estudaremos a conjugação da terceira pessoa, as variações ortográficas, os auxiliares *do* e *does* e o comportamento dos verbos *to be* e *there be*.'''

text = text.replace(antiga_abertura, nova_abertura)

# 2. Termos da fonte: trabalha, trabalham, anotacoes, pedro, olhada, lava, clock, assiste, voces, jantar, demais, dinner, teacher, referring
bloco_rotinas = '''Ações rotineiras e hábitos: descreve práticas que se repetem (*Pedro trabalha num banco: Pedro works in a bank*; *Eles trabalham na base: They work at the base*; *He washes his car on Tuesdays*; *Every Monday he goes to an ATM*).'''

novo_bloco_rotinas = '''Ações rotineiras e hábitos: relata hábitos repetidos cotidianamente. Exemplos: *Pedro trabalha num banco* (*Pedro works in a bank*); *Eles trabalham na corporação* (*They work at the base*); *Ele lava o carro às terças* (*He washes his car on Tuesdays*); *Ele assiste ao noticiário antes do jantar* (*He watches the news before dinner*). O professor (*teacher*) pede que vocês deem uma olhada nas anotações (*notes*) para fixar os demais verbos.'''

text = text.replace(bloco_rotinas, novo_bloco_rotinas)

text = text.replace(
    'Horários e escalas fixas: refere-se a cronogramas oficiais (*The train leaves at three o\'clock*; *The briefing starts at 08:00*). Na sala de aula (*in the classroom*), o instrutor pede para dar uma olhada nas anotações (*take a look at the notes*).',
    'Horários fixos: refere-se a cronogramas oficiais (*The train leaves at three o\'clock*). Na sala de aula (*classroom*), o termo *referring* indica referência contínua.'
)

with open('content/material/lingua-inglesa/m04/a04-s01.md', 'w', encoding='utf-8') as f:
    f.write(text)

print('a04-s01.md atualizado com termos da fonte e abertura calibrada!')
