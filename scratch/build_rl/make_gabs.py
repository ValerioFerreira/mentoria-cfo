import random
import json
from collections import Counter

letters = ['A'] * 27 + ['B'] * 27 + ['C'] * 26 + ['D'] * 26 + ['E'] * 26
random.seed(20261020)
random.shuffle(letters)

# Evitar 3 repeticoes consecutivas
for _ in range(10):
    for i in range(2, len(letters)):
        if letters[i] == letters[i-1] == letters[i-2]:
            for j in range(len(letters)):
                if letters[j] != letters[i] and (j < 2 or letters[j-1] != letters[i]) and (j >= len(letters)-1 or letters[j+1] != letters[i]):
                    letters[i], letters[j] = letters[j], letters[i]
                    break

# Verificar padroes ciclicos (ex: ABCDE ou EDCBA)
for i in range(len(letters) - 4):
    sub = "".join(letters[i:i+5])
    if sub in ("ABCDE", "BCDEA", "CDEAB", "DEABC", "EABCD", "EDCBA", "DCBAE", "CBAED", "BAEDC", "AEDCB"):
        letters[i+2], letters[(i+10)%len(letters)] = letters[(i+10)%len(letters)], letters[i+2]

print("Contagem:", Counter(letters))
print("Total:", len(letters))

# Salvar lista de gabaritos para uso nos blocos
with open("scratch/build_rl/gabaritos_132.json", "w", encoding="utf-8") as f:
    json.dump(letters, f, indent=2)

print("Salvo em scratch/build_rl/gabaritos_132.json")
