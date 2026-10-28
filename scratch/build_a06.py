# -*- coding: utf-8 -*-
"""Master build script for a06."""
import json
import os
import sys

# Add scratch to sys.path
sys.path.insert(0, os.path.dirname(__file__))

from a06_part1 import get_part1_data
from a06_part2 import get_part2_data

ITEMS_FILE = "content/items/direito-penal/a06.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a06.json"

with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

items_p1, summs_p1 = get_part1_data(get_fp)
items_p2, summs_p2 = get_part2_data(get_fp)

all_items = items_p1 + items_p2
all_summs = summs_p1 + summs_p2

print(f"Total items segments: {len(all_items)}")
print(f"Total summaries segments: {len(all_summs)}")

items_data = {
    "aula": "direito-penal/a06",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": all_items
}

summaries_data = {
    "aula": "direito-penal/a06",
    "batch": "pcpe-summary-direito-penal",
    "status": "DRAFT",
    "segments": all_summs
}

os.makedirs(os.path.dirname(ITEMS_FILE), exist_ok=True)
os.makedirs(os.path.dirname(SUMMARIES_FILE), exist_ok=True)

with open(ITEMS_FILE, "w", encoding="utf-8") as f:
    json.dump(items_data, f, ensure_ascii=False, indent=2)
print(f"Written: {ITEMS_FILE}")

with open(SUMMARIES_FILE, "w", encoding="utf-8") as f:
    json.dump(summaries_data, f, ensure_ascii=False, indent=2)
print(f"Written: {SUMMARIES_FILE}")
