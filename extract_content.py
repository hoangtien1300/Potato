import json
import re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Teacher.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for the bard-initial-data or WIZ_global_data
# In this specific file, it seems the content is in a script tag or JSON blob.
# Let's just find everything that looks like a Vietnamese string.

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\extracted_raw.txt', 'w', encoding='utf-8') as out:
    matches = re.findall(r'"([^"]*[\u00C0-\u1EF9][^"]*)"', content)
    for m in matches:
        if len(m) > 10:
            out.write(m + '\n')
