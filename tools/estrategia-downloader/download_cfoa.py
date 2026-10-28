import json
import logging
import re
import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent.parent
DOCS_DIR = ROOT / "docs"
PROFILE_DIR = ROOT / "browser-profile"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(ROOT / "tools" / "estrategia-downloader" / "download_cfoa.log", encoding="utf-8"),
    ],
)
logger = logging.getLogger("cfoa_downloader")

COURSES = [
    {
        "id": "246322",
        "url": "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/246322/aulas",
        "folder": DOCS_DIR / "49 - CBM-PE (CFOA) Noções de Administração",
        "name": "Noções de Administração",
    },
    {
        "id": "231933",
        "url": "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/231933/aulas",
        "folder": DOCS_DIR / "50 - CBM-PE (CFOA) Direitos Humanos",
        "name": "Direitos Humanos",
    },
    {
        "id": "361830",
        "url": "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/361830/aulas",
        "folder": DOCS_DIR / "26 - PM-PE (Oficial) Direito Processual Penal Militar",
        "name": "Direito Processual Penal Militar",
    },
]


def clean_filename(text: str) -> str:
    text = re.sub(r'[\\/*?:"<>|]', "_", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text[:100]


def extract_aula_num(title: str, fallback_idx: int) -> int:
    m = re.search(r"Aula\s*(\d+|[úu]nica)", title, re.IGNORECASE)
    if not m:
        return fallback_idx
    val = m.group(1).lower()
    if val in ("única", "unica"):
        return 0
    return int(val)


def extract_aula_title(title: str) -> str:
    # Remove 'Aula XX' prefix from title if present
    cleaned = re.sub(r"^\s*Aula\s*(\d+|[úu]nica)\s*[-:]*\s*", "", title, flags=re.IGNORECASE).strip()
    return cleaned if cleaned else title


def download_course(context, page, course_info: dict):
    folder = course_info["folder"]
    folder.mkdir(parents=True, exist_ok=True)
    logger.info("=" * 70)
    logger.info("Iniciando processamento do curso %s (%s)", course_info["id"], course_info["name"])
    logger.info("Pasta destino: %s", folder)

    page.goto(course_info["url"], wait_until="domcontentloaded", timeout=45000)
    for _ in range(25):
        page.wait_for_timeout(1000)
        text = page.locator("body").inner_text()
        if "Carregando curso..." not in text and len(text) > 400:
            break

    lessons = page.evaluate("""() => {
        const links = document.querySelectorAll('a[href*="/app/dashboard/cursos/"][href*="/aulas/"]');
        return Array.from(links).map(a => ({
            href: a.href,
            text: (a.innerText || a.getAttribute('aria-label') || '').replace(/\\s+/g, ' ').trim()
        }));
    }""")

    # Deduplicate lesson links by href
    unique_lessons = []
    seen_hrefs = set()
    for l in lessons:
        if l["href"] not in seen_hrefs and l["text"]:
            seen_hrefs.add(l["href"])
            unique_lessons.append(l)

    logger.info("Encontradas %d aulas únicas no curso %s", len(unique_lessons), course_info["id"])

    # Order lessons by Aula number
    def sort_key(l):
        return extract_aula_num(l["text"], 999)

    unique_lessons.sort(key=sort_key)

    downloaded = 0
    skipped = 0

    for idx, lesson in enumerate(unique_lessons):
        aula_num = extract_aula_num(lesson["text"], idx)
        title_part = clean_filename(extract_aula_title(lesson["text"]))
        # Standard format: '001 - Aula 00 Titulo.pdf' (ordem 1-indexed, aula 0-indexed)
        target_name = f"{idx + 1:03d} - Aula {aula_num:02d} {title_part}.pdf"
        target_path = folder / target_name

        # Check if already downloaded with same prefix or exact name
        existing_matches = list(folder.glob(f"{idx + 1:03d} - Aula {aula_num:02d}*.pdf"))
        if existing_matches and existing_matches[0].stat().st_size > 100_000:
            with open(existing_matches[0], "rb") as ef:
                header = ef.read(10)
                if header.startswith(b"%PDF-"):
                    logger.info("  [%d/%d] Já existe: %s (%d bytes)", idx + 1, len(unique_lessons), existing_matches[0].name, existing_matches[0].stat().st_size)
                    skipped += 1
                    continue

        logger.info("  [%d/%d] Baixando: %s ...", idx + 1, len(unique_lessons), target_name)
        
        # Navigate to lesson page
        page.goto(lesson["href"], wait_until="domcontentloaded", timeout=45000)
        for _ in range(15):
            page.wait_for_timeout(500)
            text = page.locator("body").inner_text()
            if "Carregando" not in text and len(text) > 200:
                break

        # Find original PDF link
        pdf_url = page.evaluate("""() => {
            const anchors = Array.from(document.querySelectorAll('a'));
            for (const a of anchors) {
                const text = (a.innerText || '').toLowerCase();
                if (text.includes('livro eletr') && text.includes('original')) {
                    return a.href;
                }
            }
            // fallback: check any link with /api/aluno/pdf/download/
            for (const a of anchors) {
                if (a.href.includes('/api/aluno/pdf/download/')) {
                    return a.href;
                }
            }
            return null;
        }""")

        if not pdf_url:
            logger.error("    ERRO: Link do PDF original não encontrado para %s", lesson["href"])
            continue

        # Download PDF with authenticated context
        try:
            resp = context.request.get(pdf_url, timeout=60000)
            if not resp.ok:
                logger.error("    ERRO: HTTP %s ao baixar %s", resp.status, pdf_url)
                continue
            body = resp.body()
            if not body.startswith(b"%PDF-"):
                logger.error("    ERRO: Arquivo recebido não é um PDF válido (header: %s)", body[:20])
                continue

            part_path = target_path.with_suffix(".pdf.part")
            part_path.write_bytes(body)
            part_path.replace(target_path)
            logger.info("    SUCESSO: Salvo %s (%d bytes)", target_name, len(body))
            downloaded += 1
            time.sleep(1.2)
        except Exception as e:
            logger.exception("    EXCEÇÃO ao baixar %s: %s", target_name, e)

    logger.info("Resumo curso %s: %d baixados, %d já existentes (total: %d)", course_info["id"], downloaded, skipped, len(unique_lessons))


def main():
    logger.info("Iniciando sessão do Playwright no perfil %s", PROFILE_DIR)
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=str(PROFILE_DIR),
            headless=True,
            accept_downloads=True,
            args=["--disable-blink-features=AutomationControlled"],
        )
        page = context.new_page()

        for course in COURSES:
            try:
                download_course(context, page, course)
            except Exception as e:
                logger.exception("Falha ao processar curso %s: %s", course["id"], e)

        context.close()
    logger.info("Processamento concluído!")


if __name__ == "__main__":
    main()
