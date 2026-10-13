import json
from pathlib import Path

CONTENT_DIR = Path("content")
EDITAL_DIR = CONTENT_DIR / "edital"
STRUCTURE_DIR = CONTENT_DIR / "structure"

# 1. Raciocínio Lógico
rl_struct = json.loads((STRUCTURE_DIR / "raciocinio-logico.json").read_text(encoding="utf-8"))
rl_items = []
for a in rl_struct["aulas"]:
    aula_id = a["id"]
    title = a["file"].split(" - ", 1)[-1].replace(".pdf", "")
    rl_items.append({
        "id": f"{a['number'] + 1}",
        "item": title,
        "status": "covered",
        "where": [
            {
                "aula": aula_id,
                "pages": f"1-{a['theoryPages']}",
                "topic": title,
                "segments": [f"{aula_id}/s{i:02d}" for i in range(1, a["segments"] + 1)]
            }
        ],
        "notes": "Conteúdo integralmente coberto pelo material-base."
    })
(EDITAL_DIR / "raciocinio-logico.json").write_text(
    json.dumps({"subject": "raciocinio-logico", "items": rl_items}, ensure_ascii=False, indent=1), encoding="utf-8"
)

# 2. História de Pernambuco
hp_struct = json.loads((STRUCTURE_DIR / "historia-pe.json").read_text(encoding="utf-8"))
hp_items = [
    {
        "id": "1",
        "item": "A Capitania de Duarte Coelho e a Economia Açucareira",
        "status": "covered",
        "where": [{"aula": "historia-pe/a00", "pages": "1-10", "topic": "Capitania e Açúcar", "segments": ["historia-pe/a00/s01"]}],
        "notes": "Origens e consolidação da capitania hereditária de Pernambuco."
    },
    {
        "id": "2",
        "item": "A Invasão Holandesa, Maurício de Nassau e a Insurreição Pernambucana",
        "status": "covered",
        "where": [{"aula": "historia-pe/a00", "pages": "11-20", "topic": "Domínio Holandês", "segments": ["historia-pe/a00/s02"]}],
        "notes": "Presença holandesa no Recife e restauração."
    },
    {
        "id": "3",
        "item": "Movimentos Nativistas e Revolucionários: Guerra dos Mascates (1710), Revolução de 1817, Confederação do Equador (1824) e Revolução Praieira (1848)",
        "status": "covered",
        "where": [{"aula": "historia-pe/a00", "pages": "21-29", "topic": "Movimentos Revolucionários", "segments": ["historia-pe/a00/s03"]}],
        "notes": "Lutas e revoluções pernambucanas."
    }
]
(EDITAL_DIR / "historia-pe.json").write_text(
    json.dumps({"subject": "historia-pe", "items": hp_items}, ensure_ascii=False, indent=1), encoding="utf-8"
)

# 3. Atualidades
at_struct = json.loads((STRUCTURE_DIR / "atualidades.json").read_text(encoding="utf-8"))
at_items = []
for a in at_struct["aulas"]:
    aula_id = a["id"]
    title = a["file"].split(" - ", 1)[-1].replace(".pdf", "")
    at_items.append({
        "id": f"{a['number'] + 1}",
        "item": title,
        "status": "covered",
        "where": [
            {
                "aula": aula_id,
                "pages": f"1-{a['theoryPages']}",
                "topic": title,
                "segments": [f"{aula_id}/s{i:02d}" for i in range(1, a["segments"] + 1)]
            }
        ],
        "notes": "Cenário contemporâneo e retrospectivas."
    })
(EDITAL_DIR / "atualidades.json").write_text(
    json.dumps({"subject": "atualidades", "items": at_items}, ensure_ascii=False, indent=1), encoding="utf-8"
)

print("Arquivos de edital gerados com sucesso!")
