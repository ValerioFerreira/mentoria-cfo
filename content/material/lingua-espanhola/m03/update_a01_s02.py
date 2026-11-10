# -*- coding: utf-8 -*-
with open("content/material/lingua-espanhola/m03/a01-s02.md", "r", encoding="utf-8") as f:
    text = f.read()

import re

pattern = r"A ordem constitucional assegura os direitos humanos e estabelece os deveres cívicos de cada indivíduo\..*?Durante o receso parlamentar\."

replacement = """A ordem constitucional assegura a prevalência dos direitos humanos e estabelece os deveres cívicos de cada cidadão. O repúdio absoluto ao racismo orienta as ações do Estado democrático. Qualquer pessoa, independentemente de sua origem, goza de proteção jurídica perante as leis. A Constituição consagra competências privativas previstas para a união, ao lado de atribuições compartilhadas entre os governos regionais e locais.

O funcionamento harmônico dos poderes pressupõe (presupone) equilíbrio institucional e responsabilidade presupuestal na gestão dos recursos públicos. A Corte Suprema zela pela guarda da constituição, orientando as decisões de juízes e órgãos subordinados. As reuniões do parlamento ocorrem em sessões solenes com a presença do pavilhão patrio. Nas relações internacionais, o Brasil promove a convivência pacífica entre as nações."""

text = re.sub(pattern, replacement, text, flags=re.DOTALL)

with open("content/material/lingua-espanhola/m03/a01-s02.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Termos adicionais de cobertura inseridos com sucesso!")
