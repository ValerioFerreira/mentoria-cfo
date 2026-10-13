import re
import time
from urllib.parse import urljoin

from models import Lesson, Subject
from selectors import CourseSelectors
from utils import clean_text


def wait_for_course(page) -> None:
    page.wait_for_load_state("domcontentloaded")
    # The site renders course data after its initial app shell.
    for _ in range(30):
        if page.locator(CourseSelectors.SUBJECT_LINKS).count():
            return
        if page.locator(CourseSelectors.LESSON_LINKS).count():
            return
        page.wait_for_timeout(500)


def discover_subjects(page, course_url: str) -> list[Subject]:
    page.goto(course_url, wait_until="domcontentloaded")
    wait_for_course(page)
    entries = page.locator(CourseSelectors.SUBJECT_LINKS).evaluate_all(
        "els => els.map(a => ({title: (a.innerText || a.getAttribute('aria-label') || '').trim(), href: a.href}))"
    )
    subjects = []
    seen = set()
    for entry in entries:
        url = entry["href"]
        title = clean_text(entry["title"])
        if url not in seen and title:
            seen.add(url)
            subjects.append(Subject(title=title, url=url))
    return subjects


def _lesson_entries(page) -> list[dict]:
    return page.locator(CourseSelectors.LESSON_LINKS).evaluate_all(
        "els => els.map(a => ({title: (a.innerText || a.getAttribute('aria-label') || '').trim(), href: a.href}))"
    )


def discover_lessons(page, subject_url: str, delay: float) -> list[Lesson]:
    page.goto(subject_url, wait_until="domcontentloaded")
    wait_for_course(page)
    found: dict[str, str] = {}
    stable_rounds = 0
    # Scroll through dynamically appended lists. Wait for the count to settle at bottom.
    for _ in range(60):
        before = len(found)
        for entry in _lesson_entries(page):
            title, url = clean_text(entry["title"]), entry["href"]
            if title and url:
                found[url] = title
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(max(500, int(delay * 1000)))
        for entry in _lesson_entries(page):
            title, url = clean_text(entry["title"]), entry["href"]
            if title and url:
                found[url] = title
        if len(found) == before:
            stable_rounds += 1
        else:
            stable_rounds = 0
        if stable_rounds >= 2:
            break

    # Follow only explicit rel=next pagination links; unrelated carousel buttons are ignored.
    next_link = page.locator(CourseSelectors.NEXT_PAGE_LINK)
    visited_pages = {page.url}
    while next_link.count() and next_link.first.is_visible():
        next_url = urljoin(page.url, next_link.first.get_attribute("href") or "")
        if not next_url or next_url in visited_pages:
            break
        visited_pages.add(next_url)
        page.goto(next_url, wait_until="domcontentloaded")
        wait_for_course(page)
        for entry in _lesson_entries(page):
            title, url = clean_text(entry["title"]), entry["href"]
            if title and url:
                found[url] = title
        next_link = page.locator(CourseSelectors.NEXT_PAGE_LINK)

    def order_key(item):
        title = item[1]
        match = re.search(r"Aula\s*(\d+)", title, re.I)
        return (int(match.group(1)) if match else 10**9, title.casefold())

    return [Lesson(title, url) for url, title in sorted(found.items(), key=order_key)]

