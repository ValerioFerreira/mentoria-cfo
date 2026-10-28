import argparse
import json
import re
import sys
import time
from pathlib import Path

from browser import open_context
from crawler import discover_lessons, discover_subjects, wait_for_course
from selectors import CourseSelectors
from utils import clean_text


def extract_subject_cards_info(page) -> dict[str, dict]:
    """Extract extra info (like professor name) from the package page cards if available."""
    return page.evaluate(
        """() => {
            const info = {};
            const links = document.querySelectorAll('a[href*="/app/dashboard/cursos/"][href$="/aulas"]');
            for (const a of links) {
                const href = a.href;
                // Climb up to card container
                let card = a;
                for (let i = 0; i < 6; i++) {
                    if (card.parentElement) card = card.parentElement;
                }
                const text = (card.innerText || '').replace(/\\s+/g, ' ').trim();
                if (!info[href] || text.length > info[href].cardText.length) {
                    info[href] = { cardText: text };
                }
            }
            return info;
        }"""
    )


def extract_lessons_with_details(page, subject_url: str, delay: float) -> tuple[str, list[dict]]:
    """Discover lessons on a subject page and check PDF indicators / lesson details."""
    page.goto(subject_url, wait_until="domcontentloaded")
    wait_for_course(page)

    found: dict[str, dict] = {}
    stable_rounds = 0

    def scan_page():
        entries = page.evaluate(
            """() => {
                const results = [];
                const links = document.querySelectorAll('a[href*="/app/dashboard/cursos/"][href*="/aulas/"]');
                for (const a of links) {
                    const href = a.href;
                    const title = (a.innerText || a.getAttribute('aria-label') || '').replace(/\\s+/g, ' ').trim();
                    if (!title || !href) continue;
                    // Check parent container for PDF download links or text indicators
                    let container = a;
                    for (let i = 0; i < 5; i++) {
                        if (container.parentElement && !container.parentElement.matches('body, main, #root, #app')) {
                            container = container.parentElement;
                        }
                    }
                    const containerText = (container.innerText || '').replace(/\\s+/g, ' ').trim();
                    const pdfLinks = container.querySelectorAll('a[href*="/api/aluno/pdf/download/"]');
                    results.push({
                        href,
                        title,
                        containerText: containerText.slice(0, 500),
                        pdfCountInCard: pdfLinks.length
                    });
                }
                return results;
            }"""
        )
        for e in entries:
            url = e["href"]
            title = clean_text(e["title"])
            if title and url:
                # Avoid overwriting a longer lesson title with a shorter link text (e.g. "Assistir")
                if url not in found or len(title) > len(found[url]["title"]):
                    found[url] = {
                        "title": title,
                        "url": url,
                        "containerText": e["containerText"],
                        "pdfCountInCard": e["pdfCountInCard"],
                    }

    for _ in range(60):
        before = len(found)
        scan_page()
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(max(500, int(delay * 1000)))
        scan_page()
        if len(found) == before:
            stable_rounds += 1
        else:
            stable_rounds = 0
        if stable_rounds >= 2:
            break

    header_text = page.evaluate(
        """() => {
            const h = document.querySelector('header, h1, [class*="Header"], [class*="Course"]');
            return h ? h.innerText.replace(/\\s+/g, ' ').trim() : document.title;
        }"""
    )

    def order_key(item):
        title = item[1]["title"]
        match = re.search(r"Aula\s*(\d+)", title, re.I)
        return (int(match.group(1)) if match else 10**9, title.casefold())

    ordered = [item[1] for item in sorted(found.items(), key=order_key)]
    return header_text, ordered


def main() -> int:
    parser = argparse.ArgumentParser(description="Lista cursos e aulas de um pacote do Estratégia Concursos sem baixar PDFs.")
    parser.add_argument("--course", default="https://www.estrategiaconcursos.com.br/app/dashboard/pacote/361849")
    parser.add_argument("--profile", default="browser-profile")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--delay", type=float, default=1.0)
    parser.add_argument("--timeout", type=int, default=45_000)
    parser.add_argument("--out-json", default="docs/pacote-361849/inventario_raw.json")
    parser.add_argument("--check-lesson-pdf", action="store_true", help="Visita cada aula para confirmar link de PDF caso não apareça na listagem")
    args = parser.parse_args()

    root = Path.cwd()
    profile_path = (root / args.profile).resolve()
    out_json = (root / args.out_json).resolve()
    out_json.parent.mkdir(parents=True, exist_ok=True)

    manager, context = open_context(profile_path, args.headless, args.timeout)
    try:
        page = context.pages[0] if context.pages else context.new_page()
        api_courses: dict[str, dict] = {}

        def on_response(resp):
            if "api.estrategiaconcursos.com.br/api/aluno/curso/" in resp.url and resp.status == 200:
                try:
                    data = resp.json()
                    cid = resp.url.rstrip("/").split("/")[-1]
                    api_courses[cid] = data.get("data", data)
                except Exception:
                    pass

        page.on("response", on_response)

        print(f"Acessando pacote: {args.course}", flush=True)
        page.goto(args.course, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)

        subjects = []
        if "estrategiaconcursos.com.br/app/" in page.url.lower():
            subjects = discover_subjects(page, args.course)

        if not subjects:
            print("\n" + "=" * 60, flush=True)
            print(">>> NAVEGADOR ABERTO PARA AUTENTICAÇÃO NO ESTRATÉGIA <<<", flush=True)
            print("Por favor, faça seu login na janela do navegador que se abriu.", flush=True)
            print("A listagem detectará seu login automaticamente e iniciará o inventário.", flush=True)
            print("=" * 60 + "\n", flush=True)
            for _ in range(300):
                page.wait_for_timeout(2000)
                cur_url = page.url.lower()
                if "estrategiaconcursos.com.br/app/" in cur_url and "login" not in cur_url:
                    subjects = discover_subjects(page, args.course)
                    if subjects:
                        print(f"✓ Autenticação detectada com sucesso! {len(subjects)} curso(s) encontrado(s).", flush=True)
                        break

        if not subjects:
            print("Nenhum curso encontrado após aguardar login.", flush=True)
            return 1

        cards_info = extract_subject_cards_info(page)
        package_title = page.title()
        print(f"Pacote: {package_title} | Cursos encontrados: {len(subjects)}", flush=True)

        result = {
            "package_url": args.course,
            "package_title": package_title,
            "subjects": [],
        }

        for idx, subj in enumerate(subjects, 1):
            m_cid = re.search(r"/cursos/(\d+)/", subj.url)
            cid = m_cid.group(1) if m_cid else ""
            print(f"[{idx}/{len(subjects)}] Listando aulas de: {subj.title} (id={cid}) ...", flush=True)
            header_text, lessons = extract_lessons_with_details(page, subj.url, args.delay)
            card_text = cards_info.get(subj.url, {}).get("cardText", "")
            api_info = api_courses.get(cid, {})
            professores = [p.get("nome", "") for p in api_info.get("professores", []) if isinstance(p, dict)]
            api_aulas_by_id = {str(a.get("id")): a for a in api_info.get("aulas", []) if isinstance(a, dict)}

            for lesson in lessons:
                m_aid = re.search(r"/aulas/(\d+)", lesson["url"])
                aid = m_aid.group(1) if m_aid else ""
                a_meta = api_aulas_by_id.get(aid, {})
                lesson["aula_id"] = aid
                lesson["nome_api"] = a_meta.get("nome")
                lesson["conteudo_api"] = a_meta.get("conteudo")
                lesson["is_disponivel"] = a_meta.get("is_disponivel")
                lesson["has_pdf"] = bool(a_meta.get("pdf"))
                lesson["has_pdf_grifado"] = bool(a_meta.get("pdf_grifado"))
                lesson["has_pdf_simplificado"] = bool(a_meta.get("pdf_simplificado"))
                lesson["videos_count"] = len(a_meta.get("videos") or [])

            print(f"    -> {len(lessons)} aulas encontradas | Profs: {', '.join(professores)}", flush=True)

            result["subjects"].append({
                "index": idx,
                "course_id": cid,
                "title": subj.title,
                "url": subj.url,
                "professores": professores,
                "lessons": lessons,
            })
            out_json.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
            page.wait_for_timeout(int(args.delay * 1000))

        print(f"\nInventário completo salvo em: {out_json}", flush=True)
        return 0
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
