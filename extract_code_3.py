import re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard_theme_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's see if we can find any string like "\u003c!DOCTYPE html" 
# Or just use regex to match the escaped html
raw_matches = re.finditer(r'(\\u003c!DOCTYPE html.*?\\u003c/html\\u003e)', text, re.IGNORECASE)
found = False
for i, m in enumerate(raw_matches):
    content = m.group(1).encode().decode('unicode_escape')
    if len(content) > 500:
         with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\raw_html_{i}.txt', 'w', encoding='utf-8') as out:
             out.write(content)
         print(f'Wrote raw_html_{i}.txt (length {len(content)})')
         found = True

# Let's also check for html embedded in markdown blocks in json string inside WIZ_global_data
# E.g. \"```html\\n<!DOCTYPE html>\\n<html...```\"
import json
start_idx = text.find('window.WIZ_global_data = {')
if start_idx != -1:
    end_idx = text.find('};', start_idx)
    if end_idx != -1:
        wiz_data = text[start_idx+25:end_idx+1]
        try:
            data = json.loads(wiz_data)
            # just stringify the json and search for it
            data_str = json.dumps(data)
            matches_md = re.finditer(r'```html(.*?)```', data_str, re.IGNORECASE | re.DOTALL)
            for i, md in enumerate(matches_md):
                c = md.group(1)
                # unescape standard escaped characters line \n
                c = c.replace('\\n', '\n').replace('\\"', '"').replace('\\\\', '\\')
                with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\md_html_{i}.txt', 'w', encoding='utf-8') as out:
                     out.write(c.strip())
                print(f'Wrote md_html_{i}.txt (length {len(c)})')
        except Exception as e:
            print("Json parsing failed", e)
