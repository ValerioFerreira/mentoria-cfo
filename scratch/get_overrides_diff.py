import json
import subprocess

diff = subprocess.check_output(["git", "diff", "content/overrides/"], encoding="utf-8", errors="replace")

with open("scratch/diff_overrides.txt", "w", encoding="utf-8") as f:
    f.write(diff)

print(f"Diff written, length: {len(diff)}")
