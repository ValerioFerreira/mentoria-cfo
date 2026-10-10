"""Selectors based on the observed Estratégia page semantics and URL shape."""


class CourseSelectors:
    # Package entries and lesson entries are links in the rendered course UI.
    SUBJECT_LINKS = 'a[href*="/app/dashboard/cursos/"][href$="/aulas"]'
    # Some Estratégia courses use /aulas/{id}, while others add /videos/{id}.
    LESSON_LINKS = 'a[href*="/app/dashboard/cursos/"][href*="/aulas/"]'
    ORIGINAL_PDF_LINK = 'a[href*="/api/aluno/pdf/download/"]'
    NEXT_PAGE_LINK = 'a[rel="next"]'

