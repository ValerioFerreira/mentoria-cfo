import sys, json
sys.stdout.reconfigure(encoding="utf-8")

with open("pipeline/.cache/material/questoes/quimica__m01.json", encoding="utf-8") as f:
    data = json.load(f)

for q in data["questoes"]:
    if q["id"] == "tec_2189288":
        print("Enunciado:\n", q["enunciado"])
        print("\nAlternativas:")
        for a in q["alternativas"]:
            print(f"  {a['letra']}: {a['texto']}")
        print("\nTemFigura:", q.get("temFigura"))
        print("Gabarito:", q.get("gabarito"))
