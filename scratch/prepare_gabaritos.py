import random
from collections import Counter

# Target: 123 questions -> 25 A, 25 B, 25 C, 24 D, 24 E
letters = ['A']*25 + ['B']*25 + ['C']*25 + ['D']*24 + ['E']*24

# Seed for deterministic reproducible shuffle
rng = random.Random(42)

for _ in range(1000):
    rng.shuffle(letters)
    # Check max consecutive repetition <= 2
    max_rep = 1
    cur_rep = 1
    for i in range(1, len(letters)):
        if letters[i] == letters[i-1]:
            cur_rep += 1
            if cur_rep > max_rep:
                max_rep = cur_rep
        else:
            cur_rep = 1
    # Check that it's not cyclic (no A-B-C-D-E runs)
    has_cyclic = False
    for i in range(len(letters) - 4):
        if letters[i:i+5] == ['A', 'B', 'C', 'D', 'E'] or letters[i:i+5] == ['E', 'D', 'C', 'B', 'A']:
            has_cyclic = True
            break
    if max_rep <= 2 and not has_cyclic:
        break

print("Distribution:", Counter(letters))
print("Max consecutive:", max_rep)
print("Has cyclic:", has_cyclic)
print("First 20:", letters[:20])

with open("scratch/gabaritos_123.json", "w") as f:
    import json
    json.dump(letters, f)
print("Saved to scratch/gabaritos_123.json")
