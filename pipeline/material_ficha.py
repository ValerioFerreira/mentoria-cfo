"""Ficha de produção de um volume do material próprio MentorIA (o ponto de partida do agente que escreve o volume).

Mostra, para cada capítulo (trecho): metas (palavras, elementos visuais, quadros), importância, concursos, tópicos da fonte,
itens do edital que o capítulo PRECISA cobrir, pontos de atenção da fonte (página + rótulo) e a impressão digital a copiar no
front matter. Mostra também as questões disponíveis para a Fixação e os volumes-par (mesmo assunto em outra disciplina).

Uso:  python pipeline/material_ficha.py <disciplina>/mNN            (ficha do volume)
      python pipeline/material_ficha.py --proximos [--onda N] [-n 5] (próximos volumes pendentes da fila)
      python pipeline/material_ficha.py --lote 4 [--onda N] [--frente B] [--simular]  (próximo lote da frente e RESERVA dos
                                       volumes novos: devolvidos primeiro, fila na ordem das ondas, uma disciplina por volume)
      python pipeline/material_ficha.py --fonte <disciplina>/aNN/sNN [--paginas 7-8]  (texto-fonte PROTEGIDO: só para ler)
"""
from __future__ import annotations

import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import CONTENT_DIR  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = CONTENT_DIR.parent
MATERIAL_DIR = CONTENT_DIR / "material"
QUESTIONS_DIR = ROOT / "pipeline" / ".cache" / "material" / "questoes"
SUMMARIES_DIR = CONTENT_DIR / "summaries"


def load_json(p):
    return json.loads(p.read_text(encoding="utf-8"))


def ficha(volume_id: str) -> int:
    subject, m = volume_id.split("/")
    vols = load_json(MATERIAL_DIR / "volumes" / f"{subject}.json")
    vol = next((v for v in vols["volumes"] if v["id"] == volume_id), None)
    if not vol:
        raise SystemExit(f"volume inexistente: {volume_id}")
    metrics = {r["id"]: r for r in load_json(MATERIAL_DIR / "metrics" / f"{subject}.json")["trechos"]}
    print(f"# FICHA DO VOLUME {volume_id} · {vol['title']}")
    print(f"onda {vol['wave']} · concursos: {', '.join(vol['contests'])} · {vol['chapters']} capítulos")
    print(f"pasta de entrega: content/material/{subject}/{m}/  (volume.md, um .md por capítulo, fixacao.json)")
    pares = [p for p in vols.get("pares", []) if volume_id in p["volumes"]]
    for p in pares:
        print(f"PAR: {p['assunto']} também em {[v for v in p['volumes'] if v != volume_id][0]} (veja a seção 9 do briefing)")
    tot = 0
    for i, t in enumerate(vol["trechos"], start=1):
        r = metrics[t]
        tg, src = r["targets"], r["source"]
        tot += tg["words"]
        aula, seg = t.split("/")[1:]
        print(f"\n## Capítulo {i} · {t} → arquivo {aula}-{seg}.md")
        print(f"importância {r['importance']['tier']} (nota {r['importance']['score']}) · concursos {', '.join(r['contests'])}"
              f"{' · COMPLEMENTO AUTORAL (texto nosso, pode reaproveitar)' if r['authored'] else ''}")
        print(f"meta: {tg['words']} palavras (aceito {tg['wordsMin']}–{tg['wordsMax']}) · ≥ {tg['visuals']} elementos visuais · ≥ {tg['callouts']} quadros")
        print(f"fonte: {src['theoryPages']} págs. de teoria, {src['words']} palavras, {src['figures']} figuras, {src['tables']} tabelas, "
              f"{src['boxes']} quadros")
        print(f"fingerprint: {json.dumps(r['fingerprint'], ensure_ascii=False)}")
        print("tópicos da fonte (cubra todos, na ordem que for mais didática):")
        for tp in r["topics"]:
            print(f"  - {tp}")
        if r["edital"]:
            print("itens do edital (copie os refs em 'edital' e cubra cada um):")
            for e in r["edital"]:
                print(f"  - {e['ref']}: {e['title']}")
        else:
            print("itens do edital: nenhum ligado diretamente (o capítulo cobre a base do assunto do volume)")
        if r["attention"]:
            print("pontos de atenção da fonte (leia a página e garanta o ponto no seu texto, com suas palavras):")
            for a in r["attention"][:25]:
                print(f"  - pág. {a['page']}: {a['label'] or 'quadro de destaque'} · {a['topic'] or ''}")
        summ = SUMMARIES_DIR / subject / f"{aula}.json"
        has = summ.exists() and any(s["id"] == t for s in load_json(summ).get("segments", []))
        print(f"resumo analítico próprio: {'sim, ' + str(summ.relative_to(ROOT)) if has else 'não há'}")
    print(f"\nTOTAL do volume: {tot} palavras de capítulos")
    q = QUESTIONS_DIR / f"{subject}__{m}.json"
    if q.exists():
        d = load_json(q)
        aocp = sum(1 for x in d["questoes"] if "AOCP" in str(x["banca"]).upper())
        print(f"questões para a Fixação: {d['total']} no banco ({aocp} AOCP) · por capítulo: {d['porCapitulo']}")
        print(f"arquivo: {q.relative_to(ROOT)}")
    else:
        print(f"questões: rode  cd web && npx tsx scripts/material-questoes.ts --volume {volume_id}")
    return 0


def proximos(onda: int | None, n: int) -> int:
    queue = load_json(MATERIAL_DIR / "_queue.json")["queue"]
    shown = 0
    for r in queue:
        if onda and r["wave"] != onda:
            continue
        subject, m = r["volume"].split("/")
        if (MATERIAL_DIR / subject / m).exists():
            continue
        print(f"{r['rank']:4d}  onda {r['wave']}  {r['volume']:40s} {r['chapters']} cap.  {r['targetWords']:6d} palavras  {r['title']}")
        shown += 1
        if shown >= n:
            break
    if not shown:
        print("nenhum volume pendente")
    return 0


def volume_status(subject: str, m: str) -> str:
    """PENDENTE (sem pasta), DEVOLVIDO (algum arquivo devolvido), EM_PRODUCAO (algum rascunho), senão o status comum
    (PRONTO_PARA_REVISAO, EM_REVISAO, APROVADO)."""
    import re  # noqa: PLC0415

    d = MATERIAL_DIR / subject / m
    if not d.exists():
        return "PENDENTE"
    states = set()
    for f in d.iterdir():
        if f.suffix == ".md" and f.name != "REVISAO.md":
            mm = re.search(r'^status:\s*"([A-Z_]+)"', f.read_text(encoding="utf-8"), re.M)
            states.add(mm.group(1) if mm else "RASCUNHO")
        elif f.name == "fixacao.json":
            states.add(load_json(f).get("status", "RASCUNHO"))
    for s in ("DEVOLVIDO", "RASCUNHO", "PRONTO_PARA_REVISAO", "EM_REVISAO"):
        if s in states:
            return "EM_PRODUCAO" if s == "RASCUNHO" else s
    return "APROVADO" if states else "EM_PRODUCAO"


RESERVA = ".frente"  # arquivo na pasta do volume com a frente que o reservou (pasta antiga sem ele = frente A)


def dono(subject: str, m: str) -> str | None:
    """Frente dona do volume: a do arquivo .frente; pasta antiga com arquivos e sem .frente = A; sem pasta, ou pasta vazia
    sendo criada agora por outro coordenador = None."""
    d = MATERIAL_DIR / subject / m
    if not d.exists():
        return None
    f = d / RESERVA
    if f.exists():
        return f.read_text(encoding="utf-8").split()[0]
    return "A" if any(d.iterdir()) else None


def reservar(subject: str, m: str, frente: str) -> bool:
    """Reserva atômica: cria a pasta do volume (falha se outro coordenador já a criou) e grava a frente."""
    import datetime  # noqa: PLC0415

    d = MATERIAL_DIR / subject / m
    d.parent.mkdir(parents=True, exist_ok=True)  # pasta da disciplina; a do volume continua atômica
    try:
        d.mkdir(parents=False)
    except FileExistsError:
        return False
    (d / RESERVA).write_text(f"{frente} {datetime.datetime.now().isoformat(timespec='seconds')}\n", encoding="utf-8")
    return True


def lote(tamanho: int, onda: int | None, frente: str = "A", simular: bool = False) -> int:
    """Próximo lote da frente. Ordem: volumes DEVOLVIDOS (correção) e volumes pela metade (retomar) que são DESTA frente,
    depois os pendentes da fila, na ordem da fila (onda 1 = CFOA primeiro, para todas as frentes). Nunca duas vezes a mesma
    disciplina no lote. Cada volume NOVO é reservado na hora (pasta + .frente, criação atômica), de modo que vários
    coordenadores em paralelo nunca pegam o mesmo volume; rode a seleção UMA vez por lote (--simular só mostra). Volume-par
    cuja base (o par que vem antes na fila) ainda não foi entregue espera. Disciplinas 'reservadas' de frentes.json não
    entram. Imprime uma linha por volume: <TIPO> <volume> <título>, com TIPO = CORRECAO, RETOMAR ou NOVO."""
    queue = load_json(MATERIAL_DIR / "_queue.json")["queue"]
    fpath = MATERIAL_DIR / "_lotes" / "frentes.json"
    cfg = load_json(fpath) if fpath.exists() else {"frentes": {"A": {}}}
    if frente not in cfg["frentes"]:
        raise SystemExit(f"frente inexistente: {frente} (veja {fpath.relative_to(ROOT)})")
    reservadas = set(cfg.get("reservadas", []))
    rank = {r["volume"]: r["rank"] for r in queue}
    entregue = {"PRONTO_PARA_REVISAO", "EM_REVISAO", "APROVADO"}

    def base_pendente(r: dict) -> str | None:
        for p in r.get("pares") or []:
            for v in p["volumes"]:
                if v != r["volume"] and rank.get(v, 10**9) < r["rank"] and volume_status(*v.split("/")) not in entregue:
                    return v
        return None

    picked: list[tuple[str, dict]] = []
    used: set[str] = set()
    esperando: list[str] = []
    # RETOMAR = pasta desta frente com rascunho e nenhum autor trabalhando nela (autor que falhou ou sessão interrompida):
    # a seleção só é feita com todos os autores do lote anterior da frente encerrados.
    for tipo, want in (("CORRECAO", "DEVOLVIDO"), ("RETOMAR", "EM_PRODUCAO"), ("NOVO", "PENDENTE")):
        for r in queue:
            if len(picked) >= tamanho:
                break
            subject, m = r["volume"].split("/")
            if subject in reservadas or subject in used:
                continue
            if onda and r["wave"] != onda and tipo == "NOVO":
                continue
            if volume_status(subject, m) != want:
                continue
            if tipo != "NOVO" and dono(subject, m) != frente:
                continue
            if tipo == "NOVO":
                if b := base_pendente(r):
                    esperando.append(f"{r['volume']} (espera a base {b})")
                    continue
                if not simular and not reservar(subject, m, frente):
                    continue
            picked.append((tipo, r))
            used.add(subject)
    if not picked:
        print(f"FIM: nenhum volume devolvido nem pendente para a frente {frente}" + (f", onda {onda}" if onda else "")
              + (f"; aguardando base: {', '.join(esperando)}" if esperando else ""))
        return 0
    for tipo, r in picked:
        print(f"{tipo:9s} {r['volume']:40s} {r['chapters']} cap.  {r['title']}")
    counts: dict[str, int] = {}
    for r in queue:
        if r["volume"].split("/")[0] not in reservadas and (not onda or r["wave"] == onda):
            st = volume_status(*r["volume"].split("/"))
            counts[st] = counts.get(st, 0) + 1
    print("situação geral" + (f" da onda {onda}" if onda else "") + ": " + " · ".join(f"{k} {v}" for k, v in sorted(counts.items()))
          + (" (simulação: nada reservado)" if simular else ""))
    return 0


def fonte(seg_id: str, only: str | None = None) -> int:
    """Texto-fonte enxuto: só as páginas de teoria (pageMap = T), sem marcas invisíveis, sem linhas que se repetem em quase
    todas as páginas (cabeçalho/rodapé) e com espaços colapsados. Complemento autoral: o .md (é nosso)."""
    import re  # noqa: PLC0415
    from collections import Counter  # noqa: PLC0415

    from summary_source import authored_md, segment  # noqa: PLC0415
    from textutil import aula_key_map, load_pages  # noqa: PLC0415

    seg = segment(seg_id)
    md = authored_md(seg["aula"])
    if md is not None:
        print(f"# COMPLEMENTO AUTORAL {seg_id} (texto do MentorIA; pode reaproveitar, adaptando ao formato)\n")
        print(md)
        return 0
    subject = seg_id.split("/")[0]
    struct = {a["id"]: a for a in load_json(CONTENT_DIR / "structure" / f"{subject}.json")["aulas"]}
    pm = struct.get(seg["aula"], {}).get("pageMap", "")
    key = aula_key_map().get(seg["aula"])
    if not key:
        raise SystemExit(f"sem cache de texto para {seg['aula']}")
    bidi = re.compile(r"[​-‏‪-‮⁦-⁩﻿]+")
    pages = {p["n"]: bidi.sub(" ", p["text"]) for p in load_pages(key)["pages"]}
    freq = Counter(ln.strip() for t in pages.values() for ln in set(t.splitlines()) if ln.strip())
    noisy = {ln for ln, c in freq.items() if c > 0.5 * len(pages) and len(ln) < 120}
    nums = [n for n in range(seg["startPage"], seg["endPage"] + 1) if n - 1 < len(pm) and pm[n - 1] == "T"] or list(
        range(seg["startPage"], seg["endPage"] + 1))
    if only:
        a, _, b = only.partition("-")
        nums = [n for n in nums if int(a) <= n <= int(b or a)]
        if not nums:
            raise SystemExit(f"nenhuma página de teoria em {only} neste trecho")
    print(f"# TEXTO-FONTE PROTEGIDO de {seg_id} · páginas de teoria {nums[0]}–{nums[-1]}. Só para ler: NUNCA copie.\n")
    for n in nums:
        lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in pages.get(n, "").splitlines()]
        body = "\n".join(ln for ln in lines if ln and ln not in noisy)
        print(f"=== pág. {n} ===\n{body}\n")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("volume", nargs="?")
    ap.add_argument("--proximos", action="store_true")
    ap.add_argument("--lote", type=int, metavar="N", help="seleciona o próximo lote de N volumes (devolvidos primeiro)")
    ap.add_argument("--onda", type=int)
    ap.add_argument("--frente", default="A", help="com --lote: frente de produção (content/material/_lotes/frentes.json)")
    ap.add_argument("--simular", action="store_true", help="com --lote: mostra a seleção sem reservar os volumes")
    ap.add_argument("-n", type=int, default=5)
    ap.add_argument("--fonte")
    ap.add_argument("--paginas", help="com --fonte: só estas páginas (ex.: 7 ou 7-8)")
    args = ap.parse_args()
    if args.fonte:
        return fonte(args.fonte, args.paginas)
    if args.lote:
        return lote(args.lote, args.onda, args.frente, args.simular)
    if args.proximos:
        return proximos(args.onda, args.n)
    if not args.volume:
        ap.print_help()
        return 2
    return ficha(args.volume)


if __name__ == "__main__":
    raise SystemExit(main())
