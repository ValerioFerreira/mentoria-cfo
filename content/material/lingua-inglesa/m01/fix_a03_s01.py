# -*- coding: utf-8 -*-
with open("content/material/lingua-inglesa/m01/a03-s01.md", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Substituir expressao proibida 'preencher'
text = text.replace("preencher formulários", "completar formulários")
text = text.replace("preencher documento", "completar documento")
text = text.replace("preencher", "completar")

# 2. Inserir termos da fonte
target = """- *fill in / fill out*: completar formulários e relatórios mantidos na pasta do destacamento;
- *put away*: guardar ou arrumar equipamentos após a exibição pública de viaturas."""

repl = """- *fill in / fill out*: completar formulários e relatórios mantidos na pasta do destacamento;
- *wake up*: acordar cedo e levantar da cama sem demora;
- *break up / broke up*: encerrar um relacionamento que acabou ou desiludiu os parceiros;
- *take off*: tirar uma peça de roupa como vestido (dress), saia ou blusa branca (white blouse);
- *give back*: devolver um objeto ou deixar de volta na mesa do oficial;
- *blow up*: explodir um artefato tático ou destruir uma ponte;
- *put away*: guardar ou arrumar equipamentos após a exibição pública de viaturas."""

text = text.replace(target, repl)

with open("content/material/lingua-inglesa/m01/a03-s01.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Ajustes em a03-s01 concluidos!")
