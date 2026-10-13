import logging
import time
from pathlib import Path

from selectors import CourseSelectors
from utils import valid_pdf


def find_original_pdf(page) -> str | None:
    links = page.locator(CourseSelectors.ORIGINAL_PDF_LINK)
    for i in range(links.count()):
        link = links.nth(i)
        text = (link.inner_text() or "").casefold()
        if "original" in text:
            return link.get_attribute("href")
    return None


def save_original_pdf(context, page, lesson_url: str, target: Path, retries: int, delay: float, logger: logging.Logger) -> str:
    for attempt in range(retries + 1):
        try:
            page.goto(lesson_url, wait_until="domcontentloaded")
            pdf_url = None
            for _ in range(30):
                pdf_url = find_original_pdf(page)
                if pdf_url:
                    break
                page.wait_for_timeout(500)
            if not pdf_url:
                raise RuntimeError("Link de PDF original não encontrado na página da aula")

            # Use the exact, signed URL rendered by the authenticated page and the
            # same browser context/cookie jar. No endpoint or signature is guessed.
            response = context.request.get(pdf_url, timeout=60_000)
            if not response.ok:
                raise RuntimeError(f"Download respondeu HTTP {response.status}")
            content_type = response.headers.get("content-type", "").casefold()
            body = response.body()
            if not body.startswith(b"%PDF-"):
                raise RuntimeError(f"Resposta não é um PDF (Content-Type: {content_type or 'ausente'})")
            if content_type and "pdf" not in content_type and "octet-stream" not in content_type:
                raise RuntimeError(f"Content-Type inesperado: {content_type}")
            target.parent.mkdir(parents=True, exist_ok=True)
            partial = target.with_suffix(target.suffix + ".part")
            partial.write_bytes(body)
            if not valid_pdf(partial):
                partial.unlink(missing_ok=True)
                raise RuntimeError("Assinatura do PDF inválida após gravar o arquivo")
            partial.replace(target)
            time.sleep(delay)
            return "downloaded"
        except Exception as exc:
            logger.exception("Falha em %s (tentativa %s/%s): %s", lesson_url, attempt + 1, retries + 1, exc)
            if attempt >= retries:
                raise
            time.sleep(min(delay * (2 ** attempt), 30))
    raise RuntimeError("Falha inesperada de download")

