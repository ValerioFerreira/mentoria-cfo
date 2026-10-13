"""Perfil de aprovação dos últimos concursos PMPE/CBMPE (praça e oficial), a partir das listas oficiais de resultado.

Baixa os PDFs públicos de classificação (Instituto AOCP 2024; UPE/IAUPE 2016-2018), lê a nota de cada candidato e calcula,
para os **aprovados dentro das vagas**, a média e o mínimo de acertos (total e, quando a lista traz, por disciplina).
Só **agregados** vão para o repositório (`web/src/lib/approval/profiles.json`): nenhum nome ou inscrição é guardado (LGPD).

Uso: python pipeline/approval_profiles.py [--offline]   (--offline: usa só os PDFs já baixados em pipeline/.cache/aprovados/)

Fontes (todas públicas):
- AOCP, PMPE (concurso 588) e CBMPE (concurso 589): "Anexo I/II do Edital de Resultado e Classificação" de 04/09/2024
  (Anexo I = PcD, Anexo II = ampla concorrência; juntos cobrem todos os classificados; usa-se a posição na ampla concorrência).
- UPE: CFO PM/BM 2018 (aprovados na 1ª etapa × resultado da prova objetiva), Praça PMPE 2016 (aprovados na 1ª etapa),
  Praça CBMPE 2017 (resultado das provas objetiva e dissertativa, com a ordem de classificação).
- Omitidos por falta de lista classificada com nota dentro das vagas: Praça PMPE 2018 (só "aprovados na prova de conhecimentos").
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import statistics
import sys
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / "pipeline" / ".cache" / "aprovados"
OUT = ROOT / "web" / "src" / "lib" / "approval" / "profiles.json"

AOCP = "https://arquivos-site.institutoaocp.org.br/publicacoes/"
UPE = "https://www.upenet.com.br/concluido/"

SOURCES = {
    "cbmpe24_a1": AOCP + "4ed3d9a4-a9c7-49b9-bf66-0a1afc6a8c51.pdf",
    "cbmpe24_a2": AOCP + "8c539784-12f8-4ff0-b47a-c615632ee530.pdf",
    "pmpe24_a1": AOCP + "bd36d326-37e7-447d-a3ae-9de00ff6bb1d.pdf",
    "pmpe24_a2": AOCP + "6470031d-6b95-464c-80a4-1a3cd44902a0.pdf",
    "cfo18_obj": UPE + "2018/18_cfo/Resultado/240918_CFO-2018%20-%20Result%20da%20Prova%20Objetiva%20de%20Conhecimentos%20e%20Discursivas-24-09-18.pdf",
    "cfo18_aprov": UPE + "2018/18_cfo/Resultado/141218_CFO%202018%20-%20APROVADOS%20ETAPA%201-.pdf",
    "pmpe16_aprov": UPE + "2016/16_pm_16/resultado/PM2016_-_Candidatos_aprovados_na_1a_ETAPA_-_13-12-2016.pdf",
    "cbmpe17_res": UPE + "2017/17_Bombeiro_PM_17/Publicacao/240717_Bomb2017%20-%20Resultado%20das%20Provas%20Objetivas%20e%20Dissertativas-Apos%20Recursos%20Administrativo-24-07-2017.pdf",
}

# Colunas de disciplina das listas AOCP, na ordem em que aparecem; depois delas vêm nota objetiva, [redação], nota final.
# Chave = slug da disciplina no sistema ("lingua-estrangeira" agrupa inglês/espanhol); None = sem equivalente na prova do CBMPE 2027.
CBM_OFICIAL = [("lingua-portuguesa", 5), ("lingua-estrangeira", 5), ("informatica", 5), ("estatistica", 5), ("matematica", 5), ("fisica", 5),
               ("quimica", 5), ("biologia", 5), ("direito-constitucional", 8), ("direito-administrativo", 7), ("legislacoes-pe", 10), ("direito-penal-militar", 5)]
# PMPE oficial: LP, LE, Rac. Lógico, Estatística, Informática, D. Const., D. Adm., D. Penal, D.P. Penal, Dir. Garantias Fund., D. Penal Militar, D.P.P. Militar
PM_OFICIAL = [("lingua-portuguesa", 10), ("lingua-estrangeira", 5), (None, 5), ("estatistica", 5), ("informatica", 5), ("direito-constitucional", 5),
              ("direito-administrativo", 5), (None, 5), (None, 5), (None, 10), ("direito-penal-militar", 5), (None, 5)]
CBM_PRACA = [("lingua-portuguesa", 10), ("informatica", 5), ("matematica", 10), (None, 5), ("fisica", 5), ("biologia", 5), ("direito-constitucional", 10),
             (None, 5), (None, 5)]
# Prefixo da inscrição AOCP + nº de notas na linha -> (disciplinas, total de questões, posição da nota objetiva)
# (a nota final é sempre a última; a lista de PcD não traz a coluna de redação, por isso há dois tamanhos para o oficial PMPE)
AOCP_LAYOUTS = {
    ("3640", 15): (CBM_OFICIAL, 70, 12),
    ("3320", 12): (CBM_PRACA, 60, 9),
    ("4020", 15): (PM_OFICIAL, 70, 12),
    ("4020", 14): (PM_OFICIAL, 70, 12),
    ("3970", 9): ([], 60, 6),  # praça PMPE: só total (o cabeçalho do PDF não traz as colunas de disciplina)
    ("3970", 8): ([], 60, 6),
}

# Perfis: vagas = quantos classificados formam o grupo "aprovados" (1ª etapa: edital); relevance pesa o perfil no agregado.
PROFILES = [
    dict(id="cbmpe-oficial-2024", label="CBMPE · 2º Tenente 2024", corp="CBMPE", cargo="oficial", year=2024, banca="Instituto AOCP",
         vagas=60, first_call=30, relevance=1.0, kind="aocp", prefix="3640", sources=["cbmpe24_a1", "cbmpe24_a2"]),
    dict(id="pmpe-oficial-2024", label="PMPE · Oficial 2024", corp="PMPE", cargo="oficial", year=2024, banca="Instituto AOCP",
         vagas=300, first_call=150, relevance=0.85, kind="aocp", prefix="4020", sources=["pmpe24_a1", "pmpe24_a2"]),
    dict(id="cbmpe-praca-2024", label="CBMPE · Soldado 2024", corp="CBMPE", cargo="praca", year=2024, banca="Instituto AOCP",
         vagas=600, first_call=300, relevance=0.5, kind="aocp", prefix="3320", sources=["cbmpe24_a1", "cbmpe24_a2"]),
    dict(id="pmpe-praca-2024", label="PMPE · Soldado 2024", corp="PMPE", cargo="praca", year=2024, banca="Instituto AOCP",
         vagas=2400, first_call=2400, relevance=0.5, kind="aocp", prefix="3970", sources=["pmpe24_a1", "pmpe24_a2"]),
    dict(id="cfo-pmpe-2018", label="PMPE · CFO 2018", corp="PMPE", cargo="oficial", year=2018, banca="IAUPE/UPE",
         vagas=60, first_call=60, relevance=0.85, kind="cfo2018", cfo="PM", total_questions=70, sources=["cfo18_obj", "cfo18_aprov"]),
    dict(id="cfo-cbmpe-2018", label="CBMPE · CFO 2018", corp="CBMPE", cargo="oficial", year=2018, banca="IAUPE/UPE",
         vagas=20, first_call=20, relevance=1.0, kind="cfo2018", cfo="BM", total_questions=70, sources=["cfo18_obj", "cfo18_aprov"]),
    dict(id="cbmpe-praca-2017", label="CBMPE · Soldado 2017", corp="CBMPE", cargo="praca", year=2017, banca="IAUPE/UPE",
         vagas=300, first_call=300, relevance=0.5, kind="cbmpe2017", total_questions=80, sources=["cbmpe17_res"]),
    dict(id="pmpe-praca-2016", label="PMPE · Soldado 2016", corp="PMPE", cargo="praca", year=2016, banca="IAUPE/UPE",
         vagas=1500, first_call=1500, relevance=0.5, kind="pmpe2016", total_questions=60, points_per_question=2, sources=["pmpe16_aprov"]),
]


# ---------------------------------------------------------------- download / leitura
def pdf_lines(path: Path) -> list[str]:
    import pymupdf

    out: list[str] = []
    with pymupdf.open(path) as doc:
        for page in doc:
            out += [ln.strip() for ln in page.get_text().split("\n")]
    return out


def fetch(key: str, offline: bool) -> list[str]:
    path = CACHE / f"{key}.pdf"
    if not path.exists():
        if offline:
            raise SystemExit(f"falta {path} (rode sem --offline)")
        CACHE.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(SOURCES[key], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            path.write_bytes(r.read())
    return pdf_lines(path)


# ---------------------------------------------------------------- parsers (puros; testados)
NUM_DOT = re.compile(r"\d+\.\d\d")
NUM_COMMA = re.compile(r"\d+,\d\d")


def parse_aocp(lines: list[str]) -> list[dict]:
    """Lista AOCP: inscrição (10 dígitos), notas (N.NN), data de nascimento e posição na ampla concorrência."""
    recs: list[dict] = []
    i = 0
    while i < len(lines):
        if re.fullmatch(r"\d{10}", lines[i]):
            j = i + 1
            nums: list[float] = []
            while j < len(lines) and NUM_DOT.fullmatch(lines[j]):
                nums.append(float(lines[j]))
                j += 1
            rank = None
            if j + 1 < len(lines) and re.fullmatch(r"\d{2}/\d{2}/\d{4}", lines[j]) and lines[j + 1].isdigit():
                rank = int(lines[j + 1])
            recs.append({"id": lines[i], "nums": nums, "rank": rank})
            i = j
        else:
            i += 1
    return recs


def parse_upe_pairs(lines: list[str], width: int) -> list[dict]:
    """Lista UPE: inscrição de 6 dígitos seguida de `width` notas (N,NN)."""
    recs: list[dict] = []
    for i, ln in enumerate(lines):
        if re.fullmatch(r"\d{6}", ln) and i + width < len(lines) and all(NUM_COMMA.fullmatch(lines[i + 1 + k]) for k in range(width)):
            recs.append({"id": ln, "nums": [float(lines[i + 1 + k].replace(",", ".")) for k in range(width)]})
    return recs


def parse_upe_ranked(lines: list[str]) -> list[dict]:
    """Resultado UPE 2017: inscrição, objetiva, redação, total e ordem (`750º`)."""
    recs: list[dict] = []
    for i, ln in enumerate(lines):
        if re.fullmatch(r"\d{6}", ln) and i + 4 < len(lines) and all(NUM_COMMA.fullmatch(lines[i + 1 + k]) for k in range(3)):
            m = re.match(r"(\d+)\S$", lines[i + 4])
            if m:
                recs.append({"id": ln, "obj": float(lines[i + 1].replace(",", ".")), "rank": int(m.group(1))})
    return recs


def parse_cfo_list(lines: list[str]) -> dict[str, list[str]]:
    """Lista "aprovados na 1ª etapa" do CFO 2018 em ordem de classificação, por cargo (PM/BM)."""
    out: dict[str, list[str]] = {"PM": [], "BM": []}
    cargo = None
    for i, ln in enumerate(lines):
        if "OFICIAL DA POL" in ln and "PMPE" in ln:
            cargo = "PM"
        elif "OFICIAL DO CORPO" in ln:
            cargo = "BM"
        elif cargo and re.fullmatch(r"\d{6}", ln) and i + 1 < len(lines) and re.match(r"\d+\S?$", lines[i + 1]) and len(lines[i + 1]) <= 5:
            out[cargo].append(ln)
    return out


def parse_cfo_obj(lines: list[str]) -> dict[tuple[str, str], float]:
    """Resultado da prova objetiva do CFO 2018: (cargo, inscrição) -> acertos."""
    out: dict[tuple[str, str], float] = {}
    cargo = None
    for i, ln in enumerate(lines):
        if "OFICIAL DA POL" in ln:
            cargo = "PM"
        elif "OFICIAL DO CORPO" in ln:
            cargo = "BM"
        elif cargo and re.fullmatch(r"\d{6}", ln) and i + 3 < len(lines) and all(NUM_COMMA.fullmatch(lines[i + 1 + k]) for k in range(3)):
            out[(cargo, ln)] = float(lines[i + 1].replace(",", "."))
    return out


# ---------------------------------------------------------------- estatística
def r2(v: float) -> float:
    return round(v, 2)


def summarize(totals: list[float], total_questions: int) -> dict:
    return {
        "n": len(totals),
        "mean": r2(statistics.mean(totals)),
        "min": r2(min(totals)),
        "max": r2(max(totals)),
        "meanPct": round(statistics.mean(totals) / total_questions, 3),
        "minPct": round(min(totals) / total_questions, 3),
    }


def build_aocp(profile: dict, offline: bool) -> dict:
    by_id: dict[str, dict] = {}
    for src in profile["sources"]:
        for rec in parse_aocp(fetch(src, offline)):
            if rec["id"].startswith(profile["prefix"]) and rec["rank"] is not None and (profile["prefix"], len(rec["nums"])) in AOCP_LAYOUTS:
                by_id.setdefault(rec["id"], rec)  # PcD aparece também na ampla concorrência
    recs = sorted(by_id.values(), key=lambda r: r["rank"])
    if not recs:
        raise SystemExit(f"{profile['id']}: nenhum registro")
    disc, total_q, obj_idx = AOCP_LAYOUTS[(profile["prefix"], len(recs[0]["nums"]))]
    approved = recs[: profile["vagas"]]
    first = recs[: profile["first_call"]]
    out = {
        "classified": len(recs),
        "approved": summarize([r["nums"][obj_idx] for r in approved], total_q),
        "firstCall": summarize([r["nums"][obj_idx] for r in first], total_q),
        "minClassified": r2(min(r["nums"][obj_idx] for r in recs)),
        "totalQuestions": total_q,
        "finalScoreMin": r2(min(r["nums"][-1] for r in approved)),
    }
    subjects: dict[str, dict] = {}
    for k, (slug, mx) in enumerate(disc):
        if slug is None:
            continue
        vals = [r["nums"][k] for r in approved]
        subjects[slug] = {"max": mx, "mean": r2(statistics.mean(vals)), "min": r2(min(vals))}
    if subjects:
        out["subjects"] = subjects
    return out


def build_cfo2018(profile: dict, offline: bool) -> dict:
    ordered = parse_cfo_list(fetch("cfo18_aprov", offline))[profile["cfo"]]
    obj = parse_cfo_obj(fetch("cfo18_obj", offline))
    scores = [obj[(profile["cfo"], i)] for i in ordered if (profile["cfo"], i) in obj]
    habil = [v for (c, _), v in obj.items() if c == profile["cfo"]]
    tq = profile["total_questions"]
    return {
        "classified": len(scores),
        "approved": summarize(scores[: profile["vagas"]], tq),
        "firstCall": summarize(scores[: profile["first_call"]], tq),
        "minClassified": r2(min(scores)),
        "minHabilitated": r2(min(habil)),
        "totalQuestions": tq,
    }


def build_cbmpe2017(profile: dict, offline: bool) -> dict:
    recs = sorted(parse_upe_ranked(fetch("cbmpe17_res", offline)), key=lambda r: r["rank"])
    tq = profile["total_questions"]
    scores = [r["obj"] for r in recs]
    return {
        "classified": len(recs),
        "approved": summarize(scores[: profile["vagas"]], tq),
        "firstCall": summarize(scores[: profile["first_call"]], tq),
        "minClassified": r2(min(scores)),
        "totalQuestions": tq,
    }


def build_pmpe2016(profile: dict, offline: bool) -> dict:
    ppq = profile["points_per_question"]
    pts = sorted((float(m.group(0).replace(",", ".")) for ln in fetch("pmpe16_aprov", offline) if (m := re.fullmatch(r"\d{2,3},\d\d", ln))), reverse=True)
    hits = [p / ppq for p in pts]  # pontos -> acertos
    tq = profile["total_questions"]
    return {
        "classified": len(hits),
        "approved": summarize(hits[: profile["vagas"]], tq),
        "firstCall": summarize(hits[: profile["first_call"]], tq),
        "minClassified": r2(min(hits)),
        "totalQuestions": tq,
        "note": "lista de aprovados na 1ª etapa (aptos nas demais fases) ordenada por nota",
    }


BUILDERS = {"aocp": build_aocp, "cfo2018": build_cfo2018, "cbmpe2017": build_cbmpe2017, "pmpe2016": build_pmpe2016}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--offline", action="store_true")
    args = ap.parse_args()
    profiles = []
    for p in PROFILES:
        stats = BUILDERS[p["kind"]](p, args.offline)
        meta = {k: p[k] for k in ("id", "label", "corp", "cargo", "year", "banca", "vagas", "relevance")}
        meta["firstCallVagas"] = p["first_call"]
        profiles.append({**meta, **stats})
        a = stats["approved"]
        print(f"{p['id']:22} aprovados={a['n']:5} média={a['mean']:6.2f}/{stats['totalQuestions']} ({a['meanPct']:.0%}) mín={a['min']:5.1f}")
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({"generatedAt": datetime.date.today().isoformat(), "profiles": profiles}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("->", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
