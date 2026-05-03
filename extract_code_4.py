import re
import json

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard_theme_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.finditer(r'```([a-z]*)\\n(.*?)\\n```', text, re.IGNORECASE | re.DOTALL)
found = 0
for m in matches:
    lang = m.group(1)
    code = m.group(2)
    # unescape
    code = code.replace(r'\n', '\n').replace(r'\"', '\"').replace(r'\\', '\\')
    if len(code) > 200:
        with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\extracted_code_block_{found}.txt', 'w', encoding='utf-8') as out:
            out.write(code)
        found += 1

print(f'Done pass 1, found {found} code blocks.')

if found == 0:
    matches2 = re.finditer(r'\\u003c([a-z]+)[^>]*\\u003e(.*?)\\u003c/\\1\\u003e', text, re.IGNORECASE | re.DOTALL)
    for m in matches2:
        if m.group(1).lower() in ['html', 'style', 'script', 'div']:
            content = m.group(0).encode().decode('unicode_escape')
            if len(content) > 500:
                with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\extracted_tag_{found}.txt', 'w', encoding='utf-8') as out:
                    out.write(content)
                found += 1
    print(f'Done pass 2, found {found} tags.')
