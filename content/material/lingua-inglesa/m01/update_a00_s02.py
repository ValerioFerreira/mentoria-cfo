# -*- coding: utf-8 -*-
with open("content/material/lingua-inglesa/m01/a00-s02.md", "r", encoding="utf-8") as f:
    text = f.read()

text = text.replace("```mermaid", "```mermaid Fluxo de Leitura e Interpretação Multimodal")

target = "Em segundo lugar, analise uma tirinha que constrói uma paródia inteligente de uma obra clássica de Shakespeare. Um personagem com óculos observa um gato com olhar triste e declama: *\"To be or not to be...\"*. A paródia e o humor residem na inadequação solene do texto shakesperiano aplicado a uma situação prosaica e cômica do cotidiano doméstico."

repl = "Em segundo lugar, analise uma tirinha humorística que constrói uma paródia de peças clássicas do dramaturgo William Shakespeare. O personagem usa óculos escuros (sunglasses) e anéis (rings), enquanto um palestrante profere paráfrases solenes sobre a existência humana. A estilização visual das figuras e a expressão triste do animal tornam evidente o tom cômico, tornando impossível considerar errado o sentido satírico pretendido pelo cartunista."

text = text.replace(target, repl)

with open("content/material/lingua-inglesa/m01/a00-s02.md", "w", encoding="utf-8") as f:
    f.write(text)

print("Atualizado com sucesso!")
