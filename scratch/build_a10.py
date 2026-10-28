# -*- coding: utf-8 -*-
"""Master build script for a10."""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from a10_data import get_a10_data

ITEMS_FILE = "content/items/direito-penal/a10.json"
SUMMARIES_FILE = "content/summaries/direito-penal/a10.json"

with open("content/segments/direito-penal.json", "r", encoding="utf-8") as f:
    all_segs = {s["id"]: s for s in json.load(f)["segments"]}

def get_fp(sid):
    s = all_segs[sid]
    return {"startPage": s["startPage"], "endPage": s["endPage"], "startTopic": s["startTopic"]}

all_items, all_summs = get_a10_data(get_fp)

print(f"Total items segments: {len(all_items)}")
print(f"Total summaries segments: {len(all_summs)}")

items_data = {
    "aula": "direito-penal/a10",
    "batch": "pcpe-bizu-direito-penal",
    "status": "DRAFT",
    "stage": "bizu",
    "segments": all_items
}

summaries_data = {
    "aula": "direito-penal/a10",
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
