import json
from pathlib import Path
from typing import Any


class ProgressStore:
    def __init__(self, path: Path, course_url: str):
        self.path = path
        self.data: dict[str, Any] = {"course": course_url, "subjects": {}}
        if path.exists():
            try:
                loaded = json.loads(path.read_text(encoding="utf-8"))
                if loaded.get("course") == course_url and isinstance(loaded.get("subjects"), dict):
                    self.data = loaded
            except (OSError, json.JSONDecodeError):
                pass

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temp = self.path.with_suffix(self.path.suffix + ".tmp")
        temp.write_text(json.dumps(self.data, ensure_ascii=False, indent=2), encoding="utf-8")
        temp.replace(self.path)

    def record_subject(self, key: str, title: str, url: str, lessons: list[dict]) -> None:
        subject = self.data["subjects"].setdefault(key, {"title": title, "url": url, "lessons": {}})
        subject.update({"title": title, "url": url})
        for lesson in lessons:
            subject["lessons"].setdefault(lesson["url"], {
                "title": lesson["title"], "status": "pending", "file": None
            })

    def set_lesson(self, subject_key: str, lesson_url: str, **values) -> None:
        self.data["subjects"][subject_key]["lessons"].setdefault(lesson_url, {}).update(values)
        self.save()

