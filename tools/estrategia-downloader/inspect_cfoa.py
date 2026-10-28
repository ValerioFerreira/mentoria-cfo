import sys
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

profile = Path("browser-profile").resolve()
urls = [
    "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/361830/aulas",
    "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/246322/aulas",
    "https://www.estrategiaconcursos.com.br/app/dashboard/cursos/231933/aulas",
]

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir=str(profile),
        headless=True,
        args=["--disable-blink-features=AutomationControlled"],
    )
    page = context.new_page()
    for url in urls:
        print("=" * 60)
        print("Testing:", url)
        page.goto(url, wait_until="domcontentloaded", timeout=45000)
        for i in range(25):
            page.wait_for_timeout(1000)
            text = page.locator("body").inner_text()
            if "Carregando curso..." not in text and len(text) > 400:
                break
        print("Title:", page.title())
        h1 = page.locator("h1").all_inner_texts()
        print("H1:", h1)
        
        # Extract course name from text
        body_lines = [line.strip() for line in page.locator("body").inner_text().split("\n") if line.strip()]
        for idx, line in enumerate(body_lines[:25]):
            if "Pró-Edital" in line or "Pós-Edital" in line or "Pré-Edital" in line or "Curso" in line:
                print("Context line:", line, "-> Next:", body_lines[idx+1:idx+3])

        lessons = page.evaluate("""() => {
            const links = document.querySelectorAll('a[href*="/app/dashboard/cursos/"][href*="/aulas/"]');
            return Array.from(links).map(a => ({
                href: a.href,
                text: (a.innerText || '').replace(/\\s+/g, ' ').trim()
            }));
        }""")
        print(f"Found {len(lessons)} lesson links:")
        for l in lessons:
            print("  ", l["text"], "->", l["href"])
    context.close()
