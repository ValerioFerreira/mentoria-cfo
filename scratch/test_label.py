import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path("c:/Users/Administrador/Documents/Projetos/CFO-BM")
sys.path.insert(0, str(ROOT / "pipeline"))
from textutil import aula_key_map, load_pages

STOPW = set("de da do das dos para com por que uma nos nas ao aos ou lei art arts".split())

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s.replace("​", ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "", s)

keymap = aula_key_map()
_cache = {}

def pages(aula):
    if aula not in _cache:
        k = keymap.get(aula)
        _cache[aula] = {p["n"]: norm(p["text"]) for p in load_pages(k)["pages"]} if k else None
    return _cache[aula]

def frac(topic, aula, rng):
    pg = pages(aula)
    words = [norm(w) for w in re.findall(r"[A-Za-zÀ-ú]{4,}", topic) if norm(w) not in STOPW]
    if not words:
        return 1.0, words, []
    blob = "".join(pg.get(i, "") for i in rng)
    matched = [w for w in words if w in blob]
    return (sum(w in blob for w in words) / len(words)), words, matched

if __name__ == "__main__":
    if len(sys.argv) > 3:
        aula = sys.argv[1]
        sp = int(sys.argv[2])
        topic = sys.argv[3]
        score, words, matched = frac(topic, aula, [sp, sp + 1])
        print(f"Aula: {aula}, Pág: {sp}-{sp+1}")
        print(f"Topic: {topic}")
        print(f"Score: {score:.2f} ({len(matched)}/{len(words)})")
        print(f"Words: {words}")
        print(f"Matched: {matched}")
