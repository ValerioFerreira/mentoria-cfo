import logging
import re
import sys
import time
from pathlib import Path

from browser import open_context
from crawler import discover_lessons
from downloader import save_original_pdf
from utils import safe_name, valid_pdf


def make_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("atualidades_downloader")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = logging.FileHandler(log_dir / "errors_atualidades.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def is_target_lesson(title: str) -> bool:
    # Procura o número da aula no título (ex: "Aula 00", "Aula 01", "Aula 13")
    match = re.search(r"Aula\s*(\d+)", title, re.I)
    if not match:
        print(f"  [AVISO] Não foi possível identificar o número da aula em: '{title}'")
        return False
    num = int(match.group(1))
    
    # Da 00 até a 07
    if 0 <= num <= 7:
        return True
    
    # Ímpares da 09 até a 19 (09, 11, 13, 15, 17, 19)
    if 9 <= num <= 19 and num % 2 != 0:
        return True
    
    return False


def main():
    course_url = "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/384116/aulas"
    output_dir = Path("docs/16 - CBMP-PE (Praça) Atualidades").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    profile_dir = Path("browser-profile").resolve()
    logger = make_logger(Path("logs"))

    print("==========================================================")
    print("INICIANDO DOWNLOAD DE ATUALIDADES (CBMPE - PRAÇA)")
    print(f"URL: {course_url}")
    print(f"Destino: {output_dir}")
    print("Aulas alvo: 00 a 07, e ímpares de 09 a 19 (09, 11, 13, 15, 17, 19)")
    print("==========================================================")

    manager, context = open_context(profile_dir, headless=False, timeout_ms=45_000)
    try:
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(course_url, wait_until="domcontentloaded")

        # Verifica se precisa de login / aguarda renderização das aulas
        print("\nVerificando acesso às aulas...")
        lessons = discover_lessons(page, course_url, delay=1.0)
        
        if not lessons:
            print("\n[ATENÇÃO] As aulas não foram detectadas imediatamente.")
            print("Se a tela de login estiver aberta, faça login no navegador.")
            print("Aguardando login ou carregamento da página por até 60 segundos...")
            for _ in range(30):
                time.sleep(2)
                lessons = discover_lessons(page, course_url, delay=1.0)
                if lessons:
                    break

        if not lessons:
            print("Nenhuma aula encontrada na página. Verifique a sessão e URL.")
            return 1

        print(f"\nTotal de aulas encontradas na página: {len(lessons)}")
        
        # Filtra as aulas solicitadas
        target_lessons = []
        for l in lessons:
            if is_target_lesson(l.title):
                target_lessons.append(l)

        print(f"Total de aulas selecionadas para download: {len(target_lessons)}")
        for l in target_lessons:
            print(f"  -> {l.title}")

        print("\n--- Iniciando downloads ---")
        downloaded = 0
        already_exists = 0
        failed = 0

        for idx, lesson in enumerate(target_lessons, 1):
            # Formato do nome do arquivo (ex: 001 - Aula 00 ...pdf)
            match = re.search(r"Aula\s*(\d+)", lesson.title, re.I)
            aula_num = int(match.group(1)) if match else idx
            filename = f"{aula_num + 1:03d} - {safe_name(lesson.title, max_length=88)}.pdf"
            target = output_dir / filename

            if target.exists() and valid_pdf(target):
                print(f"[{idx}/{len(target_lessons)}] {lesson.title} ........ JÁ EXISTE")
                already_exists += 1
                continue

            print(f"[{idx}/{len(target_lessons)}] Baixando {lesson.title} ...")
            try:
                save_original_pdf(context, page, lesson.url, target, retries=3, delay=1.0, logger=logger)
                print(f"[{idx}/{len(target_lessons)}] {lesson.title} ........ OK")
                downloaded += 1
            except Exception as exc:
                print(f"[{idx}/{len(target_lessons)}] {lesson.title} ........ ERRO: {exc}")
                failed += 1

        print("\n==========================================================")
        print("RESULTADO DO DOWNLOAD:")
        print(f"Baixados com sucesso: {downloaded}")
        print(f"Já existentes:        {already_exists}")
        print(f"Falhas:               {failed}")
        print(f"Arquivos em:          {output_dir}")
        print("==========================================================")
        return 0 if failed == 0 else 1

    finally:
        try:
            context.close()
        except Exception:
            pass
        try:
            manager.stop()
        except Exception:
            pass


if __name__ == "__main__":
    sys.exit(main())
