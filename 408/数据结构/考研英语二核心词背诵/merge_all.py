# -*- coding: utf-8 -*-
import json, os

base_dir = r"f:\obsidiannote\obsidian-\408\数据结构\考研英语二核心词背诵"
gen_dir = os.path.join(base_dir, "data_generators")

files = [
    "data_2022_2026.json",
    "data_2021_2020.json",
    "data_2019_2018.json",
    "data_2017_2016.json",
    "data_2015_2014.json",
    "data_2013_2012.json",
    "data_2011_2010.json"
]

all_items = []
current_id = 1

for fn in files:
    fp = os.path.join(gen_dir, fn)
    with open(fp, "r", encoding="utf-8") as f:
        data = json.load(f)
        for item in data:
            word = item.get("word", "").strip()
            trans = item.get("trans", "").strip()
            pos = item.get("pos", "").strip()
            
            # Clean up word
            word = word.rstrip(".,;:，；")
            
            # If word is empty, skip
            if not word or not trans:
                continue
                
            entry = {
                "id": current_id,
                "year": int(item["year"]),
                "section": item["section"].strip(),
                "category": item.get("category", "核心词汇").strip(),
                "word": word,
                "pos": pos,
                "trans": trans
            }
            all_items.append(entry)
            current_id += 1

print(f"Total valid items: {len(all_items)}")

# Check years distribution
years_count = {}
sections_count = {}
for it in all_items:
    y = it["year"]
    s = it["section"]
    years_count[y] = years_count.get(y, 0) + 1
    sections_count[s] = sections_count.get(s, 0) + 1

print("Years distribution:", sorted(years_count.items(), reverse=True))
print("Sections count:", sections_count)

# Save as words_data.json
json_path = os.path.join(base_dir, "words_data.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(all_items, f, ensure_ascii=False, indent=2)

# Save as words_data.js
js_path = os.path.join(base_dir, "words_data.js")
with open(js_path, "w", encoding="utf-8") as f:
    f.write("// 考研英语二 (2010-2026) 真题核心词汇数据库\n")
    f.write("// 总词汇量: " + str(len(all_items)) + "\n")
    f.write("window.KNOW_WORDS_DATA = ")
    json.dump(all_items, f, ensure_ascii=False)
    f.write(";\n")

print("Files saved successfully!")
