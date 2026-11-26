import os

ENTRY = "My smart fridge livestreams my leftovers, judges my 3am cheese raids, and still can't keep ice from tasting like frozen Wi-Fi."

assert ENTRY.strip() == ENTRY and ENTRY, "entry must be non-blank with no padding"
assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "wb") as f:
    f.write(ENTRY.encode("utf-8"))
