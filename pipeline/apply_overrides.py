import json
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
OVERRIDES = ROOT / "content" / "overrides"

# 1. informatica.json
info_path = OVERRIDES / "informatica.json"
info_data = json.loads(info_path.read_text(encoding="utf-8"))
a12 = info_data["aulas"].setdefault("informatica/a12", {})
a12["dropHeadings"] = [
    {"page": 62, "title": "AINEL DE ONTROLE"},
    {"page": 74, "title": "ONFIGURAÇÕES"}
]
a12["headings"] = [
    {"page": 62, "title": "Painel de Controle", "level": 1},
    {"page": 74, "title": "Configurações", "level": 1}
]
info_path.write_text(json.dumps(info_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# 2. lingua-inglesa.json
ing_path = OVERRIDES / "lingua-inglesa.json"
ing_data = json.loads(ing_path.read_text(encoding="utf-8"))
a04_ing = ing_data["aulas"].setdefault("lingua-inglesa/a04", {})
a04_ing["dropHeadings"] = [
    {"page": 24, "title": "Futuro Simples e com GOING TO"}
]
a04_ing["headings"] = [
    {"page": 24, "title": "Futuro Simples e com o GOING TO", "level": 1}
]
ing_path.write_text(json.dumps(ing_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# 3. direito-penal-militar.json
dpm_path = OVERRIDES / "direito-penal-militar.json"
dpm_data = json.loads(dpm_path.read_text(encoding="utf-8"))
a04_dpm = dpm_data["aulas"].setdefault("direito-penal-militar/a04", {})
a04_dpm["headings"] = [
    {"page": 9, "title": "Aplicação da Pena", "level": 1},
    {"page": 19, "title": "Concurso de agravantes e atenuantes", "level": 1}
]
dpm_path.write_text(json.dumps(dpm_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

# 4. lingua-portuguesa.json
pt_path = OVERRIDES / "lingua-portuguesa.json"
pt_data = json.loads(pt_path.read_text(encoding="utf-8"))
a04_pt = pt_data["aulas"].setdefault("lingua-portuguesa/a04", {})
a04_pt["headings"] = [
    {"page": 69, "title": "Noções iniciais", "level": 1}
]
a13_pt = pt_data["aulas"].setdefault("lingua-portuguesa/a13", {})
a13_pt["headings"] = [
    {"page": 82, "title": "Uso de formas abreviadas", "level": 1}
]
pt_path.write_text(json.dumps(pt_data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")

print("Overrides aplicados com sucesso!")
