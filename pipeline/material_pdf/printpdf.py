"""Chromium (Playwright): carrega o HTML do volume, espera o Mermaid e o Paged.js e imprime o PDF."""
from __future__ import annotations

from pathlib import Path

from .load import ContentError


class EngineError(Exception):
    """Falha do motor (navegador, paginação): conserta-se o motor, não o conteúdo."""


def print_pdf(html_path: Path, pdf_path: Path, timeout_s: int = 180) -> dict:
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--allow-file-access-from-files"])
        try:
            page = browser.new_page(viewport={"width": 1200, "height": 1600})
            logs: list[str] = []
            page.on("console", lambda m: logs.append(f"{m.type}: {m.text}") if m.type in ("error",) else None)
            page.on("pageerror", lambda e: logs.append(f"pageerror: {e}"))
            page.goto(html_path.as_uri(), wait_until="load")
            try:
                page.wait_for_function("window.__done === true", timeout=timeout_s * 1000, polling=500)
            except Exception as e:  # noqa: BLE001
                raise EngineError(f"paginação não terminou em {timeout_s}s; console: {logs[-5:]}") from e
            errors = page.evaluate("window.__errors")
            pages = page.evaluate("window.__pages")
            warns = page.evaluate("window.__warns")
            mermaid_errs = [e for e in errors if e.startswith("mermaid")]
            if mermaid_errs:
                raise ContentError("; ".join(mermaid_errs))
            if errors:
                raise EngineError("; ".join(errors))
            if not pages:
                raise EngineError(f"Paged.js não informou as páginas; console: {logs[-5:]}")
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            page.pdf(path=str(pdf_path), prefer_css_page_size=True, print_background=True, margin={"top": "0", "right": "0",
                                                                                                     "bottom": "0", "left": "0"})
            pages["warns"] = warns
            return pages
        finally:
            browser.close()
