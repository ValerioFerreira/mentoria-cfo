from dataclasses import dataclass, field


@dataclass
class Lesson:
    title: str
    url: str


@dataclass
class Subject:
    title: str
    url: str
    lessons: list[Lesson] = field(default_factory=list)

