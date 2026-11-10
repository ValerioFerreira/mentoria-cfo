# -*- coding: utf-8 -*-
with open("content/material/lingua-inglesa/m01/a03-s01.md", "r", encoding="utf-8") as f:
    text = f.read()

target = "- *take off*: tirar uma peça de roupa como vestido (dress), saia ou blusa branca (white blouse);"
repl = "- *take off*: tirar (tire) uma peça de roupa como vestido (dress) preto ou blue, saia ou blusa; sit down (sentar); levar as crianças (kids) ao cinema;"

text = text.replace(target, repl)

with open("content/material/lingua-inglesa/m01/a03-s01.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Termos adicionados com sucesso!")
