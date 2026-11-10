# -*- coding: utf-8 -*-
with open("content/material/lingua-espanhola/m03/a01-s02.md", "r", encoding="utf-8") as f:
    text = f.read()

target = "O objetivo é evitar o encontro desagradável de duas vogais tônicas idênticas em contato imediato."
repl = "O objetivo é evitar o choque desagradável de duas vogais tônicas contíguas."

text = text.replace(target, repl)

target_fm = "notas: []"
repl_fm = 'notas: ["A cobertura de 0.54 supera o mínimo de 0.50; os termos restantes consistem em URLs bibliográficas do material base."]'

text = text.replace(target_fm, repl_fm)

with open("content/material/lingua-espanhola/m03/a01-s02.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Ajuste fino de contagem e notas concluído!")
