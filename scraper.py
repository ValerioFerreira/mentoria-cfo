import argparse
import logging
import sys
from pathlib import Path

from browser import open_context
from crawler import discover_lessons, discover_subjects
from downloader import save_original_pdf
from progress import ProgressStore
from utils import safe_name, valid_pdf


def make_logger(log_dir: Path) -> logging.Logger:
    log_dir.mkdir(parents=True, exist_ok=True)
    logger = logging.getLogger("course_pdf_downloader")
    logger.setLevel(logging.INFO)
    logger.handlers.clear()
    handler = logging.FileHandler(log_dir / "errors.log", encoding="utf-8")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(message)s"))
    logger.addHandler(handler)
    return logger


def parse_args():
    parser = argparse.ArgumentParser(description="Baixa PDFs originais das aulas visíveis na sua sessão autenticada.")
    parser.add_argument("--course", default="", help="URL da página do pacote/curso")
    parser.add_argument("--output", default="downloads", help="Diretório de saída (padrão: ./downloads)")
    parser.add_argument("--headless", action="store_true", help="Executa sem janela após autenticação já salva")
    parser.add_argument("--resume", action="store_true", help="Retoma com base no progress.json")
    parser.add_argument("--max-retries", type=int, default=3)
    parser.add_argument("--delay", type=float, default=1.0, help="Pausa entre páginas/downloads, em segundos")
    parser.add_argument("--timeout", type=int, default=30_000, help="Timeout de navegação em milissegundos")
    parser.add_argument("--profile", default="browser-profile", help="Perfil persistente local do Chromium")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    course_url = args.course.strip() or input("URL do curso/pacote: ").strip()
    if not course_url.startswith("https://www.estrategiaconcursos.com.br/"):
        print("Informe uma URL HTTPS do site estrategiaconcursos.com.br.")
        return 2
    if args.max_retries < 0 or args.delay < 0:
        print("--max-retries e --delay não podem ser negativos.")
        return 2

    root = Path.cwd()
    output = Path(args.output).resolve()
    progress = ProgressStore(root / "progress.json", course_url)
    logger = make_logger(root / "logs")
    manager, context = open_context(root / args.profile, args.headless, args.timeout)
    found_total = 0
    try:
        page = context.pages[0] if context.pages else context.new_page()
        page.goto(course_url, wait_until="domcontentloaded")
        subjects = discover_subjects(page, course_url)
        if not subjects:
            print("A página do pacote ainda não mostra os cursos. Faça login na janela do Chromium.")
            input("Depois de entrar e abrir novamente a página do pacote, pressione Enter aqui para continuar...")
            page.goto(course_url, wait_until="domcontentloaded")
            subjects = discover_subjects(page, course_url)
        if not subjects:
            print("Nenhum curso foi detectado. Verifique a sessão e a URL.")
            return 1

        print(f"[CURSO] {page.title()}")
        print(f"Matérias encontradas: {len(subjects)}")
        totals = {"downloaded": 0, "exists": 0, "failed": 0, "lessons": 0}
        for subject_index, subject in enumerate(subjects, 1):
            lessons = discover_lessons(page, subject.url, args.delay)
            found_total += len(lessons)
            subject_key = subject.url
            progress.record_subject(subject_key, subject.title, subject.url,
                                    [{"title": lesson.title, "url": lesson.url} for lesson in lessons])
            progress.save()
            folder = output / f"{subject_index:02d} - {safe_name(subject.title, max_length=72)}"
            print(f"\n[{subject_index}/{len(subjects)}] {subject.title} ({len(lessons)} aulas)")
            for lesson_index, lesson in enumerate(lessons, 1):
                totals["lessons"] += 1
                filename = f"{lesson_index:03d} - {safe_name(lesson.title, max_length=88)}.pdf"
                target = folder / filename
                if target.exists() and valid_pdf(target):
                    progress.set_lesson(subject_key, lesson.url, title=lesson.title, status="downloaded", file=str(target.relative_to(output)))
                    print(f"    [{lesson_index}/{len(lessons)}] {lesson.title} ........ JÁ EXISTE")
                    totals["exists"] += 1
                    continue
                progress.set_lesson(subject_key, lesson.url, title=lesson.title, status="downloading", file=str(target.relative_to(output)))
                try:
                    save_original_pdf(context, page, lesson.url, target, args.max_retries, args.delay, logger)
                    progress.set_lesson(subject_key, lesson.url, title=lesson.title, status="downloaded", file=str(target.relative_to(output)))
                    print(f"    [{lesson_index}/{len(lessons)}] {lesson.title} ........ OK")
                    totals["downloaded"] += 1
                except Exception as exc:
                    progress.set_lesson(subject_key, lesson.url, title=lesson.title, status="failed", error=str(exc))
                    print(f"    [{lesson_index}/{len(lessons)}] {lesson.title} ........ ERRO")
                    totals["failed"] += 1
            page.wait_for_timeout(int(args.delay * 1000))

        print("\n========================================\nDOWNLOAD CONCLUÍDO\n========================================")
        print(f"Matérias: {len(subjects)}\nAulas encontradas: {totals['lessons']}\nPDFs baixados: {totals['downloaded']}\nJá existentes: {totals['exists']}\nFalhas: {totals['failed']}\n\nDiretório:\n{output}")
        return 0 if totals["failed"] == 0 else 1
    except KeyboardInterrupt:
        print("\nInterrompido. O progresso salvo pode ser retomado com --resume.")
        return 130
    finally:
        try:
            context.close()
        except KeyboardInterrupt:
            pass
        finally:
            manager.stop()


if __name__ == "__main__":
    sys.exit(main())

