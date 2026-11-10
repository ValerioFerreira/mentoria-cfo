"""Leis oficiais em cache local, para consultar artigo por artigo sem abrir a página inteira (economia de tokens).

A página da Constituição no Planalto tem 1,8 MB (≈ 500 mil tokens): nunca leia a página inteira. Baixe uma vez para o cache e
consulte só o artigo ou o termo de que precisa.

Uso:
  python pipeline/leis.py lista                          # leis registradas, se estão no cache e de onde vêm
  python pipeline/leis.py baixar cf cpm pe11817          # baixa (ou atualiza) do Planalto / ALEPE
  python pipeline/leis.py baixar --todas
  python pipeline/leis.py art cpm 9 10                   # imprime os artigos 9 e 10 do CPM (texto riscado vira [REVOGADO …])
  python pipeline/leis.py buscar l12016 "prazo|decad"    # artigos que contêm o termo (expressão regular, sem acento obrigatório)
Cache: pipeline/.cache/leis-oficiais/leis/<nome>.htm e <nome>.clean.txt (fora do git).
Texto compilado do Planalto: dispositivos revogados aparecem como [REVOGADO: …]; "(Redação dada pela Lei …)" indica alteração.
"""
from __future__ import annotations

import argparse
import html
import os
import re
import sys
import unicodedata
import urllib.request
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
LEIS_DIR = ROOT / "pipeline" / ".cache" / "leis-oficiais" / "leis"
P = "https://www.planalto.gov.br/ccivil_03/"
A = "https://legis.alepe.pe.gov.br/texto.aspx?"

# nome -> (endereço oficial, descrição)
LEIS: dict[str, tuple[str, str]] = {
    "cf": (P + "constituicao/constituicao.htm", "Constituição Federal de 1988"),
    "cpm": (P + "decreto-lei/del1001.htm", "Código Penal Militar (DL 1.001/1969)"),
    "cppm": (P + "decreto-lei/del1002.htm", "Código de Processo Penal Militar (DL 1.002/1969)"),
    "cp": (P + "decreto-lei/del2848compilado.htm", "Código Penal (DL 2.848/1940)"),
    "cpp": (P + "decreto-lei/del3689compilado.htm", "Código de Processo Penal (DL 3.689/1941)"),
    "l8457": (P + "leis/l8457.htm", "Lei 8.457/1992 (organização da Justiça Militar da União)"),
    "l8112": (P + "leis/l8112cons.htm", "Lei 8.112/1990 (servidores públicos civis da União)"),
    "l9784": (P + "leis/l9784.htm", "Lei 9.784/1999 (processo administrativo federal)"),
    "l14133": (P + "_ato2019-2022/2021/lei/l14133.htm", "Lei 14.133/2021 (licitações e contratos)"),
    "l8429": (P + "leis/l8429.htm", "Lei 8.429/1992 (improbidade administrativa)"),
    "abuso": (P + "_ato2019-2022/2019/lei/l13869.htm", "Lei 13.869/2019 (abuso de autoridade)"),
    "racismo": (P + "leis/l7716.htm", "Lei 7.716/1989 (crimes de preconceito de raça ou de cor)"),
    "l12016": (P + "_ato2007-2010/2009/lei/l12016.htm", "Lei 12.016/2009 (mandado de segurança)"),
    "l13300": (P + "_ato2015-2018/2016/lei/l13300.htm", "Lei 13.300/2016 (mandado de injunção)"),
    "l9507": (P + "leis/l9507.htm", "Lei 9.507/1997 (habeas data)"),
    "l4717": (P + "leis/l4717.htm", "Lei 4.717/1965 (ação popular)"),
    "l8069": (P + "leis/l8069.htm", "Lei 8.069/1990 (ECA)"),
    "l12852": (P + "_ato2011-2014/2013/lei/l12852.htm", "Lei 12.852/2013 (Estatuto da Juventude)"),
    "l11340": (P + "_ato2004-2006/2006/lei/l11340.htm", "Lei 11.340/2006 (Maria da Penha)"),
    "l14344": (P + "_ato2019-2022/2022/lei/l14344.htm", "Lei 14.344/2022 (violência contra criança e adolescente)"),
    "l12527": (P + "_ato2011-2014/2011/lei/l12527.htm", "Lei 12.527/2011 (acesso à informação)"),
    "l13303": (P + "_ato2015-2018/2016/lei/l13303.htm", "Lei 13.303/2016 (empresas estatais)"),
    "l9637": (P + "leis/l9637.htm", "Lei 9.637/1998 (organizações sociais)"),
    "l9790": (P + "leis/l9790.htm", "Lei 9.790/1999 (OSCIP)"),
    "l11107": (P + "_ato2004-2006/2005/lei/l11107.htm", "Lei 11.107/2005 (consórcios públicos)"),
    "l8987": (P + "leis/l8987cons.htm", "Lei 8.987/1995 (concessões e permissões)"),
    "l14751": (P + "_ato2023-2026/2023/lei/l14751.htm", "Lei 14.751/2023 (Lei Orgânica Nacional das PMs e CBMs)"),
    "d4377": (P + "decreto/2002/d4377.htm", "Decreto 4.377/2002 (CEDAW)"),
    "d6949": (P + "_ato2007-2010/2009/decreto/d6949.htm", "Decreto 6.949/2009 (Convenção sobre os Direitos das Pessoas com Deficiência)"),
    "d7037": (P + "_ato2007-2010/2009/decreto/d7037.htm", "Decreto 7.037/2009 (PNDH-3)"),
    "d6583": (P + "_ato2007-2010/2008/decreto/d6583.htm", "Decreto 6.583/2008 (Acordo Ortográfico)"),
    "l11343": (P + "_ato2004-2006/2006/lei/l11343.htm", "Lei 11.343/2006 (drogas)"),
    "l10826": (P + "leis/2003/l10.826.htm", "Lei 10.826/2003 (Estatuto do Desarmamento)"),
    "l9605": (P + "leis/l9605.htm", "Lei 9.605/1998 (crimes ambientais)"),
    "l8072": (P + "leis/l8072.htm", "Lei 8.072/1990 (crimes hediondos)"),
    "l9455": (P + "leis/l9455.htm", "Lei 9.455/1997 (tortura)"),
    "l12850": (P + "_ato2011-2014/2013/lei/l12850.htm", "Lei 12.850/2013 (organizações criminosas)"),
    "l9503": (P + "leis/l9503compilado.htm", "Lei 9.503/1997 (Código de Trânsito)"),
    "l9099": (P + "leis/l9099.htm", "Lei 9.099/1995 (Juizados Especiais)"),
    "l7960": (P + "leis/l7960.htm", "Lei 7.960/1989 (prisão temporária)"),
    "l12830": (P + "_ato2011-2014/2013/lei/l12830.htm", "Lei 12.830/2013 (investigação criminal pelo delegado)"),
    "l6404": (P + "leis/l6404consol.htm", "Lei 6.404/1976 (sociedades por ações)"),
    "pe6783": (A + "tiponorma=1&numero=6783&complemento=0&ano=1974&tipo=&url=", "Lei PE 6.783/1974 (Estatuto dos Militares de PE)"),
    "pe11817": (A + "tiponorma=1&numero=11817&complemento=0&ano=2000&tipo=&url=", "Lei PE 11.817/2000 (Código Disciplinar dos Militares de PE)"),
    "pe13314": (A + "tiponorma=1&numero=13314&complemento=0&ano=2007&tipo=&url=", "Lei PE 13.314/2007 (assédio moral e sexual)"),
    "pe15187": (A + "tiponorma=1&numero=15187&complemento=0&ano=2013&tipo=&url=", "Lei PE 15.187/2013"),
    "pelc470": (A + "tiponorma=2&numero=470&complemento=0&ano=2021&tipo=&url=", "LC PE 470/2021 (promoção)"),
    "ped22114": (A + "tiponorma=6&numero=22114&complemento=0&ano=2000&tipo=&url=", "Decreto PE 22.114/2000 (Código de Ética)"),
    "ped50014": (A + "tiponorma=6&numero=50014&complemento=0&ano=2020&tipo=&url=", "Decreto PE 50.014/2020"),
    "pe6425": (A + "tiponorma=1&numero=6425&complemento=0&ano=1972&tipo=&url=", "Lei PE 6.425/1972 (Estatuto do Policial Civil de PE)"),
    "pe6123": (A + "tiponorma=1&numero=6123&complemento=0&ano=1968&tipo=&url=", "Lei PE 6.123/1968 (Estatuto do Servidor de PE)"),
    "pelc137": (A + "tiponorma=2&numero=137&complemento=0&ano=2008&tipo=&url=", "LC PE 137/2008"),
    "pelc317": (A + "tiponorma=2&numero=317&complemento=0&ano=2015&tipo=&url=", "LC PE 317/2015"),
}


def _decode(b: bytes) -> str:
    if b[:2] in (b"\xff\xfe", b"\xfe\xff"):  # algumas páginas do Planalto vêm em UTF-16 (ex.: Lei 11.340/2006)
        return b.decode("utf-16", errors="replace")
    head = b[:4000].lower()
    if b"windows-1252" in head or b"iso-8859-1" in head:
        return b.decode("cp1252", errors="replace")
    try:
        return b.decode("utf-8")
    except UnicodeDecodeError:
        return b.decode("cp1252", errors="replace")


def clean_html(t: str) -> str:
    t = re.sub(r"(?is)<(script|style|head)\b.*?</\1>", "", t)
    t = re.sub(r"(?is)<(strike|s|del)\b[^>]*>(.*?)</\1>", lambda m: " [REVOGADO: " + re.sub(r"<[^>]+>", "", m.group(2)) + "] ", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</tr>|</h\d>", "\n", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\xa0\r]+", " ", t)
    t = re.sub(r"\n(?! ?(Art\.? ?\d|§|[IVXL]+ ?[-–]|[a-z]\)|Pena|Parágrafo|\[REVOGADO|CAPÍTULO|TÍTULO|SEÇÃO|Seção|Capítulo))", " ", t)
    return re.sub(r" +", " ", t)


def load(name: str) -> str:
    cache = LEIS_DIR / f"{name}.clean.txt"
    if cache.exists():
        return cache.read_text(encoding="utf-8")
    raw = LEIS_DIR / f"{name}.htm"
    if not raw.exists():
        raise SystemExit(f"'{name}' não está no cache: rode  python pipeline/leis.py baixar {name}")
    t = clean_html(_decode(raw.read_bytes()))
    cache.write_text(t, encoding="utf-8")
    return t


def baixar(names: list[str]) -> int:
    LEIS_DIR.mkdir(parents=True, exist_ok=True)
    bad = 0
    for n in names:
        if n not in LEIS:
            print(f"{n}: não registrada (veja 'lista'; peça ao orquestrador para incluir)")
            bad += 1
            continue
        url, desc = LEIS[n]
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
            b = urllib.request.urlopen(req, timeout=90).read()  # noqa: S310 (endereços oficiais fixos)
        except Exception as e:  # noqa: BLE001
            print(f"{n}: falha ao baixar ({e})")
            bad += 1
            continue
        text = clean_html(_decode(b))
        num = re.search(r"(\d[\d.]*)/(\d{4})", desc)
        ok = len(re.findall(r"Art\.? ?\d", text)) >= 3
        if num and "alepe" in url:
            ok = ok and num.group(1).replace(".", "") in text.replace(".", "")[:20000]
        if not ok:
            print(f"{n}: o conteúdo baixado não parece ser a norma ({desc}); nada gravado")
            bad += 1
            continue
        (LEIS_DIR / f"{n}.htm").write_bytes(b)
        (LEIS_DIR / f"{n}.clean.txt").write_text(text, encoding="utf-8")
        print(f"{n}: ok ({len(text) // 1000} mil caracteres) · {desc}")
    return 1 if bad else 0


def lista() -> int:
    for n, (url, desc) in LEIS.items():
        f = LEIS_DIR / f"{n}.clean.txt"
        g = LEIS_DIR / f"{n}.htm"
        st = "no cache" if f.exists() or (g.exists() and g.stat().st_size > 5000) else "FALTA"
        print(f"{n:10s} {st:9s} {desc}")
    return 0


def art(name: str, nums: list[str]) -> int:
    t = load(name)
    for n in nums:
        pat = re.compile(r"Art\.? ?" + re.escape(n) + r"(º|o|°)?(?![\d])[-–.\s]")
        hits = [m.start() for m in pat.finditer(t)]
        if not hits:
            print(f"== art. {n}: não achado")
            continue
        for h in hits:
            end = re.search(r"\n ?Art\.? ?\d", t[h + 5:])
            print(f"== {name} art. {n}\n{t[h: h + 5 + (end.start() if end else 3000)].strip()}\n")
    return 0


def _fold(s: str) -> str:
    return unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode().lower()


def buscar(name: str, termo: str, maximo: int) -> int:
    t = load(name)
    starts = [m.start() for m in re.finditer(r"\n ?Art\.? ?\d", t)] + [len(t)]
    rx = re.compile(_fold(termo))
    shown = 0
    for a, b in zip(starts, starts[1:]):
        chunk = t[a:b].strip()
        if rx.search(_fold(chunk)):
            print(chunk[:900] + (" […]" if len(chunk) > 900 else "") + "\n")
            shown += 1
            if shown >= maximo:
                print(f"(parei em {maximo} artigos; refine o termo ou use --max)")
                break
    if not shown:
        print("nenhum artigo com esse termo")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("lista")
    b = sub.add_parser("baixar")
    b.add_argument("nomes", nargs="*")
    b.add_argument("--todas", action="store_true")
    a = sub.add_parser("art")
    a.add_argument("nome")
    a.add_argument("nums", nargs="+")
    s = sub.add_parser("buscar")
    s.add_argument("nome")
    s.add_argument("termo")
    s.add_argument("--max", type=int, default=8)
    args = ap.parse_args()
    if args.cmd == "lista":
        return lista()
    if args.cmd == "baixar":
        return baixar(list(LEIS) if args.todas else args.nomes)
    if args.cmd == "art":
        return art(args.nome, args.nums)
    return buscar(args.nome, args.termo, args.max)


if __name__ == "__main__":
    os.environ.setdefault("PYTHONIOENCODING", "utf-8")
    raise SystemExit(main())
