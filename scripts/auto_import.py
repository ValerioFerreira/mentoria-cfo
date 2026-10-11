"""Script mestre para execução da rotina automática de importação de questões.

Pode ser disparado via cron diário, agendador do Windows (Task Scheduler),
ou sob demanda sempre que novos PDFs forem adicionados em docs/questoes.
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

def main():
    print("==================================================")
    print("INICIANDO ROTINA DE IMPORTAÇÃO AUTOMÁTICA")
    print("==================================================")

    # 1. Executar detector e extrator Python
    print("\nPasso 1: Detectando novos PDFs e extraindo questões...")
    res = subprocess.run([sys.executable, "-m", "pipeline.auto_import"] + sys.argv[1:], cwd=str(ROOT))
    if res.returncode != 0:
        print("Erro na extração de PDFs.")
        sys.exit(res.returncode)

    # 2. Sincronizar com banco de dados via Prisma se houver pendências
    pending_file = ROOT / "pipeline" / ".cache" / "pending_auto_import.json"
    if pending_file.exists():
        print("\nPasso 2: Sincronizando com o banco de dados...")
        sync_script = str(ROOT / "scripts" / "sync_pending_questions.ts")
        npm_cmd = "npx.cmd" if sys.platform == "win32" else "npx"
        res_sync = subprocess.run([npm_cmd, "--prefix", "web", "tsx", sync_script], cwd=str(ROOT / "web"))
        if res_sync.returncode != 0:
            print("Erro na sincronização com o banco.")
            sys.exit(res_sync.returncode)
    else:
        print("\nNenhuma pendência para o banco de dados.")

    print("\n==================================================")
    print("ROTINA DE IMPORTAÇÃO FINALIZADA COM SUCESSO!")
    print("==================================================")

if __name__ == "__main__":
    main()
