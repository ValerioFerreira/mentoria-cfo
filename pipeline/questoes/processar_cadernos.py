"""Rotina completa dos cadernos novos do TecConcursos: extrai, grava na produção, arquiva e marca o PDF como extraído.

    pipeline/.venv/Scripts/python pipeline/questoes/processar_cadernos.py            # processa o que estiver na pasta e termina
    pipeline/.venv/Scripts/python pipeline/questoes/processar_cadernos.py --vigiar   # fica vigiando a pasta (a cada 60 s) e processa cada caderno novo
    pipeline/.venv/Scripts/python pipeline/questoes/processar_cadernos.py --simular  # só confere e diz o que faria (nada é gravado, arquivado nem renomeado)

O que faz, em ordem (para na primeira falha e não renomeia nada):
 1. Lista os PDFs de docs/questoes que ainda não começam com "EXTRAÍDO - " (e que terminaram de ser copiados).
 2. Se há caderno novo: backup remoto verificado (reaproveita o de menos de 20 h), `importar.py` (banco local e produção),
    comentários versionados na produção.
 3. Confere, no banco de produção, que TODA questão esperada de cada caderno existe (as anuladas, as fora do edital e as
    em quarentena não são esperadas).
 4. Arquiva em docs/questoes/acervo/: `extraidas-AAAA-MM-DD.tar.xz` (todos os cadernos extraídos + manifesto, compactado) e
    `imagens.zip` (figuras, só acrescenta). Relê o arquivo e confere o hash de cada item antes de seguir.
 5. Renomeia cada PDF liberado para "EXTRAÍDO - <nome original>.pdf" (o dono apaga depois). PDF com questão em quarentena ou
    anomalia de leitura NÃO é renomeado (só ele permite corrigir a questão); use --renomear-com-pendencia para forçar.
 6. Escreve o relatório docs/questoes/relatorios/processamento-AAAA-MM-DD-HHMM.md.

Restaurar o acervo (ex.: PC novo): descompacte o .tar.xz em docs/questoes/.extraidas (o .importadas.json vai para docs/questoes)
e as figuras de imagens.zip em docs/questoes/.extraidas/img. Detalhes em docs/questoes/acervo/LEIA-ME.md.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import socket
import subprocess
import sys
import tarfile
import time
import zipfile
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from importar import EXTRACTOR_VERSION, PREFIXO_EXTRAIDO, sha256_file  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[2]
WEB = ROOT / "web"
FOLDER = ROOT / "docs" / "questoes"
EXTRAIDAS = FOLDER / ".extraidas"
MANIFESTO = FOLDER / ".importadas.json"
ACERVO = FOLDER / "acervo"
BACKUP_VALIDADE_H = 20  # o importador aceita 24 h; aqui sobra folga para o tempo da rotina
SHELL = sys.platform == "win32"
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8"}
LINHAS: list[str] = []
ULTIMO_RETIDOS: tuple = ()  # no modo --vigiar: não reconfere a cada ciclo quando só restam PDFs retidos e nada mudou


def log(msg: str) -> None:
    print(msg, flush=True)
    LINHAS.append(msg)


def run(cmd: list[str], cwd: Path = ROOT, timeout: int | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace", shell=SHELL and cmd[0] == "npx", env=ENV, timeout=timeout)


def ultima_json(texto: str) -> dict:
    for ln in reversed(texto.strip().splitlines()):
        if ln.startswith("{"):
            try:
                return json.loads(ln)
            except json.JSONDecodeError:
                continue
    return {}


# ---------------------------------------------------------------- PDFs
def pdfs_estaveis() -> list[Path]:
    """PDFs ainda sem o prefixo, já copiados por inteiro (tamanho estável e sem alteração nos últimos 20 s)."""
    cand = [p for p in sorted(FOLDER.glob("*.pdf")) if not p.name.startswith(PREFIXO_EXTRAIDO)]
    if not cand:
        return []
    antes = {p: p.stat().st_size for p in cand}
    time.sleep(2)
    out = []
    for p in cand:
        try:
            st = p.stat()
        except FileNotFoundError:
            continue
        if st.st_size == antes[p] and time.time() - st.st_mtime > 20:
            out.append(p)
        else:
            log(f"aguardando terminar de copiar: {p.name}")
    return out


def carregar_manifesto() -> dict:
    if MANIFESTO.exists():
        return json.loads(MANIFESTO.read_text(encoding="utf-8"))
    return {"cadernos": {}}


def estado_desatualizado() -> bool:
    """O estado por caderno (_estado.json) some ou é mais antigo que o importador: regera (só leitura, sem gravar em banco)."""
    est = EXTRAIDAS / "_estado.json"
    return not est.exists() or est.stat().st_mtime < (Path(__file__).resolve().parent / "importar.py").stat().st_mtime


def precisa_extrair(sha: str, man: dict) -> bool:
    e = man["cadernos"].get(sha)
    return not (e and e.get("extrator") == EXTRACTOR_VERSION and (EXTRAIDAS / f"{sha}.json").exists())


# ---------------------------------------------------------------- bancos
def porta_local() -> int:
    env = WEB / ".env"
    if env.exists():
        import re
        m = re.search(r"DATABASE_URL\s*=\s*\"?postgres(?:ql)?://[^@]*@[^:/]+:(\d+)/", env.read_text(encoding="utf-8"))
        if m:
            return int(m.group(1))
    return 51218


def local_no_ar() -> bool:
    try:
        with socket.create_connection(("127.0.0.1", porta_local()), timeout=2):
            return True
    except OSError:
        return False


def garantir_banco_local() -> bool:
    if local_no_ar():
        return True
    log("banco local fora do ar: tentando ligar (`prisma dev`, até 4 min) …")
    try:
        run(["npx", "prisma", "dev", "-n", "cfo-bm", "-d"], cwd=WEB, timeout=240)
    except subprocess.TimeoutExpired:
        pass
    for _ in range(24):
        if local_no_ar():
            time.sleep(5)
            return True
        time.sleep(10)
    return False


def backup_verificado() -> Path:
    """Devolve um backup remoto íntegro com menos de BACKUP_VALIDADE_H; cria um se for preciso."""

    def valido(d: Path) -> bool:
        man = d / "manifest.json"
        if not man.exists() or (time.time() - man.stat().st_mtime) / 3600 > BACKUP_VALIDADE_H:
            return False
        return run(["npx", "tsx", "scripts/questoes-backup.ts", "--verificar", str(d)], cwd=WEB).returncode == 0

    bks = sorted((ROOT / "backups").glob("questoes-remoto-*"))
    if bks and valido(bks[-1]):
        log(f"backup remoto reaproveitado: {bks[-1].name}")
        return bks[-1]
    log("criando backup remoto verificável (alguns minutos) …")
    p = run(["npx", "tsx", "scripts/questoes-backup.ts", "--remoto"], cwd=WEB)
    if p.returncode != 0 or "BACKUP ÍNTEGRO" not in p.stdout:
        raise SystemExit(f"backup remoto falhou; nada foi gravado.\n{p.stdout[-800:]}\n{p.stderr[-800:]}")
    novo = sorted((ROOT / "backups").glob("questoes-remoto-*"))[-1]
    log(f"backup remoto criado e íntegro: {novo.name}")
    return novo


def importar(so_remoto: bool, extrair_so: bool = False) -> dict[str, dict]:
    cmd = [sys.executable, str(ROOT / "pipeline/questoes/importar.py")]
    if extrair_so:
        cmd.append("--so-extrair")
    else:
        cmd += ["--so-remoto" if so_remoto else "--remoto", "--confirmo-producao"]
    log("importar.py " + " ".join(cmd[2:]) + " …")
    p = run(cmd)
    saida = p.stdout
    resultados: dict[str, dict] = {}
    for ln in saida.splitlines():
        for alvo in ("local", "remoto"):
            if ln.startswith(f"{alvo}: {{") and "created" in ln:
                try:
                    resultados[alvo] = json.loads(ln[len(alvo) + 2:])
                except json.JSONDecodeError:
                    pass
    if p.returncode != 0:
        raise SystemExit(f"importar.py falhou (código {p.returncode}); nada foi renomeado.\n{saida[-1500:]}\n{p.stderr[-1500:]}")
    for alvo, r in resultados.items():
        log(f"  {alvo}: criadas {r.get('created')}, atualizadas {r.get('updated')}, iguais {r.get('unchanged')}, aposentadas {r.get('retired')}")
        if r.get("skippedMissingSegment"):
            raise SystemExit(f"{alvo}: questões ligadas a trecho inexistente ({len(r['skippedMissingSegment'])}); interrompido para revisão.")
    return resultados


def aplicar_comentarios_remoto() -> None:
    p = run(["npx", "tsx", "scripts/questoes-comentarios.ts", "--remoto", "--aplicar"], cwd=WEB)
    r = ultima_json(p.stdout)
    if r:
        log(f"  comentários na produção: gravados {r.get('gravados')}, desatualizados {r.get('desatualizado')}, não gravados {r.get('naoGravados')}")
    else:
        log("  comentários na produção: sem resposta legível (confira com questoes-comentarios.ts --remoto)")


# ---------------------------------------------------------------- verificação
def verificar(pdfs: list[Path], man: dict, com_pendencia: bool) -> tuple[list[tuple[Path, str]], list[tuple[Path, str]]]:
    """Devolve (liberados, retidos com motivo)."""
    est_path = EXTRAIDAS / "_estado.json"
    estado = json.loads(est_path.read_text(encoding="utf-8"))["cadernos"] if est_path.exists() else {}
    por_sha: dict[str, list[Path]] = {}
    retidos: list[tuple[Path, str]] = []
    for p in pdfs:
        sha = sha256_file(p)
        if sha not in man["cadernos"] or sha not in estado:
            retidos.append((p, "caderno ainda não extraído/classificado"))
        else:
            por_sha.setdefault(sha, []).append(p)
    ids = sorted({i for sha in por_sha for i in estado[sha]["esperadasNoBanco"]})
    ausentes: set[str] = set()
    if ids:
        tmp = EXTRAIDAS / "_ids-verificar.json"
        tmp.write_text(json.dumps(ids), encoding="utf-8")
        p = run(["npx", "tsx", "scripts/questoes-existem.ts", str(tmp), "--remoto"], cwd=WEB)
        r = ultima_json(p.stdout)
        tmp.unlink(missing_ok=True)
        if "ausentes" not in r:
            raise SystemExit(f"não consegui conferir o banco de produção; nada foi renomeado.\n{p.stdout[-600:]}\n{p.stderr[-600:]}")
        ausentes = set(r["ausentes"])
        log(f"conferência na produção: {r['presentes']} de {r['consultadas']} questões esperadas presentes")
    liberados: list[tuple[Path, str]] = []
    for sha, ps in por_sha.items():
        e = estado[sha]
        falta = [i for i in e["esperadasNoBanco"] if i in ausentes]
        motivo = None
        if e["questoes"] == 0:
            motivo = "nenhuma questão lida no PDF"
        elif falta:
            motivo = f"{len(falta)} questão(ões) esperada(s) ausente(s) na produção"
        elif not com_pendencia and e["quarentena"]:
            motivo = f"{e['quarentena']} questão(ões) em quarentena (só o PDF permite corrigir)"
        elif not com_pendencia and e["anomalias"]:
            motivo = "anomalia de leitura: " + "; ".join(e["anomalias"])[:120]
        for p in ps:
            if motivo:
                retidos.append((p, motivo))
            else:
                liberados.append((p, f"{e['questoes']} questões; {e['anuladas']} anuladas; {e['foraDoEdital']} fora do edital"))
    return liberados, retidos


# ---------------------------------------------------------------- arquivo compacto
def sha_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def arquivar() -> tuple[Path, Path]:
    ACERVO.mkdir(exist_ok=True)
    hoje = datetime.now().strftime("%Y-%m-%d")
    tar_final = ACERVO / f"extraidas-{hoje}.tar.xz"
    tar_tmp = ACERVO / f"extraidas-{hoje}.tar.xz.tmp"
    fontes = sorted(p for p in EXTRAIDAS.glob("*.json") if not p.name.startswith("_"))
    log(f"arquivando {len(fontes)} cadernos extraídos …")
    with tarfile.open(tar_tmp, "w:xz", preset=6) as tf:
        for p in fontes:
            tf.add(p, arcname=f".extraidas/{p.name}")
        tf.add(MANIFESTO, arcname=".importadas.json")
    # confere: cada item do arquivo tem o mesmo hash do original
    n_ok = 0
    with tarfile.open(tar_tmp, "r:xz") as tf:
        for m in tf:
            if not m.isfile():
                continue
            orig = FOLDER / m.name
            dados = tf.extractfile(m).read()  # type: ignore[union-attr]
            if sha_bytes(dados) != sha256_file(orig):
                tar_tmp.unlink(missing_ok=True)
                raise SystemExit(f"arquivo compacto divergente em {m.name}; nada foi renomeado.")
            n_ok += 1
    if n_ok != len(fontes) + 1:
        tar_tmp.unlink(missing_ok=True)
        raise SystemExit(f"arquivo compacto com {n_ok} itens, esperado {len(fontes) + 1}; nada foi renomeado.")
    tar_tmp.replace(tar_final)
    # figuras: só acrescenta (PNG já é comprimido, então vai sem compressão extra)
    zip_path = ACERVO / "imagens.zip"
    pngs = {p.name: p for p in (EXTRAIDAS / "img").glob("*.png")}
    with zipfile.ZipFile(zip_path, "a", zipfile.ZIP_STORED) as zf:
        ja = set(zf.namelist())
        novas = [n for n in pngs if n not in ja]
        for n in novas:
            zf.write(pngs[n], arcname=n)
    with zipfile.ZipFile(zip_path) as zf:
        ruim = zf.testzip()
        nomes = set(zf.namelist())
    if ruim:
        raise SystemExit(f"imagens.zip corrompido em {ruim}; nada foi renomeado.")
    usadas: set[str] = set()
    for p in fontes:
        for q in json.loads(p.read_text(encoding="utf-8"))["questoes"]:
            usadas.update(q.get("images", {}).keys())
    sem = [s for s in usadas if f"{s}.png" not in nomes]
    if sem:
        raise SystemExit(f"{len(sem)} figura(s) usadas pelas questões não estão no imagens.zip; nada foi renomeado.")
    # mantém só as 2 versões mais recentes do arquivo de texto
    antigos = sorted(ACERVO.glob("extraidas-*.tar.xz"))[:-2]
    for a in antigos:
        a.unlink()
        log(f"  versão antiga do arquivo removida: {a.name}")
    (ACERVO / "LEIA-ME.md").write_text(
        "# Arquivo compacto das questões extraídas\n\n"
        "Gerado por `pipeline/questoes/processar_cadernos.py`. Substitui os PDFs originais do TecConcursos.\n\n"
        "- `extraidas-AAAA-MM-DD.tar.xz`: texto, alternativas, gabarito e metadados de TODAS as questões extraídas de cada caderno "
        "(inclusive as anuladas, as fora do edital e as em quarentena), mais o `.importadas.json`.\n"
        "- `imagens.zip`: figuras e fórmulas (`<sha256>.png`), referenciadas no texto como `/q-img/<sha256>`.\n\n"
        "## Restaurar (PC novo ou pasta perdida)\n\n"
        "```powershell\n"
        "cd docs/questoes\n"
        "tar -xf acervo/extraidas-AAAA-MM-DD.tar.xz          # recria .extraidas/*.json e .importadas.json\n"
        "mkdir .extraidas/img -Force\n"
        "tar -xf acervo/imagens.zip -C .extraidas/img        # figuras\n"
        "```\n\n"
        "Depois, `pipeline/.venv/Scripts/python pipeline/questoes/importar.py --reclassificar` reenvia o acervo ao banco "
        "(o remoto exige backup e `--confirmo-producao`). Os PDFs só são necessários para reextrair com um extrator novo "
        "ou corrigir questões em quarentena.\n\n"
        "Guarde uma cópia desta pasta fora do computador (nuvem ou HD externo): `docs/` não está no git.\n",
        encoding="utf-8",
    )
    log(f"  {tar_final.name}: {tar_final.stat().st_size / 1e6:.1f} MB · imagens.zip: {zip_path.stat().st_size / 1e6:.1f} MB (+{len(novas)} figuras)")
    return tar_final, zip_path


# ---------------------------------------------------------------- rotina
def processar(args: argparse.Namespace) -> int:
    LINHAS.clear()
    pdfs = pdfs_estaveis()
    if not pdfs:
        if not args.vigiar:
            log("nenhum PDF novo (todos já começam com 'EXTRAÍDO - ').")
        return 0
    global ULTIMO_RETIDOS
    assinatura = tuple((p.name, p.stat().st_size) for p in pdfs)
    if args.vigiar and assinatura == ULTIMO_RETIDOS:
        return 0
    log(f"== {datetime.now():%d/%m/%Y %H:%M} · processar_cadernos ==")
    man = carregar_manifesto()
    novos = [p for p in pdfs if precisa_extrair(sha256_file(p), man)]
    log(f"{len(pdfs)} PDF(s) sem o prefixo; {len(novos)} ainda não extraído(s).")
    if args.simular:
        log("modo --simular: nada será gravado, arquivado nem renomeado.")
    else:
        if novos:
            backup_verificado()
            so_remoto = not garantir_banco_local()
            if so_remoto:
                log("AVISO: banco local indisponível; gravando só na produção (o local fica pendente até a próxima rodada).")
            importar(so_remoto)
            aplicar_comentarios_remoto()
        elif estado_desatualizado():
            importar(False, extrair_so=True)
        man = carregar_manifesto()
    liberados, retidos = verificar(pdfs, man, args.renomear_com_pendencia)
    if not args.simular and not novos and any("ausente" in m for _, m in retidos):
        log("há questões esperadas ainda não gravadas na produção: importando o que falta …")
        backup_verificado()
        importar(not garantir_banco_local())
        aplicar_comentarios_remoto()
        man = carregar_manifesto()
        liberados, retidos = verificar(pdfs, man, args.renomear_com_pendencia)
    log(f"liberados para renomear: {len(liberados)} · retidos: {len(retidos)}")
    for p, motivo in retidos:
        log(f"  RETIDO {p.name}: {motivo}")
    if args.simular:
        return 0
    if not liberados and not novos:
        ULTIMO_RETIDOS = assinatura
    if liberados:
        arquivar()
        renomeados = 0
        for p, info in liberados:
            novo = p.with_name(PREFIXO_EXTRAIDO + p.name)
            k = 2
            while novo.exists():
                novo = p.with_name(f"{PREFIXO_EXTRAIDO}{p.stem} ({k}).pdf")
                k += 1
            try:
                p.rename(novo)
                renomeados += 1
            except OSError as e:
                log(f"  não consegui renomear {p.name} (aberto em outro programa?): {e}")
        log(f"{renomeados} PDF(s) renomeado(s) para 'EXTRAÍDO - …'. Pode apagá-los quando quiser.")
    rel_dir = FOLDER / "relatorios"
    rel_dir.mkdir(exist_ok=True)
    rel = rel_dir / f"processamento-{datetime.now():%Y-%m-%d-%H%M}.md"
    rel.write_text("# Processamento de cadernos\n\n" + "\n".join(f"- {ln}" for ln in LINHAS) + "\n", encoding="utf-8")
    log(f"relatório: {rel}")
    return 0


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--vigiar", nargs="?", const=60, type=int, metavar="SEGUNDOS", help="fica vigiando a pasta (padrão 60 s)")
    ap.add_argument("--simular", action="store_true", help="só confere; nada é gravado, arquivado nem renomeado")
    ap.add_argument("--renomear-com-pendencia", action="store_true", help="renomeia também PDFs com questão em quarentena/anomalia")
    args = ap.parse_args()
    lock = FOLDER / ".processando.lock"
    if lock.exists() and time.time() - lock.stat().st_mtime < 3 * 3600:
        raise SystemExit(f"outra execução parece em andamento ({lock}); se não houver, apague esse arquivo.")
    lock.write_text(str(os.getpid()))
    try:
        if args.vigiar:
            log(f"vigiando {FOLDER} a cada {args.vigiar} s (Ctrl+C para sair)")
            while True:
                try:
                    processar(args)
                except SystemExit as e:
                    log(f"ERRO: {e}")
                lock.touch()
                time.sleep(args.vigiar)
        else:
            processar(args)
    finally:
        lock.unlink(missing_ok=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass
