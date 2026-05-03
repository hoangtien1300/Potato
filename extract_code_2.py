from bs4 import BeautifulSoup
import re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard_theme_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

codes = soup.find_all('code')
found = False
for i, code in enumerate(codes):
    if len(code.text) > 500:
        with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\code_{i}.txt', 'w', encoding='utf-8') as out:
            out.write(code.text)
        print(f'Wrote code_{i}.txt (length {len(code.text)})')
        found = True

if not found:
    # If that fails, look for strings containing "\u003c!DOCTYPE html" inside the raw text.
    import ast
    # Let's see if we can find any string like "\u003c!DOCTYPE html\u003e" 
    # Or just use regex to match the escaped html
    raw_matches = re.finditer(r'(\\u003c!DOCTYPE html.*?\\u003c/html\\u003e)', text, re.IGNORECASE)
    for i, m in enumerate(raw_matches):
        content = m.group(1).encode().decode('unicode_escape')
        if len(content) > 500:
             with open(fr'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\raw_html_{i}.txt', 'w', encoding='utf-8') as out:
                 out.write(content)
             print(f'Wrote raw_html_{i}.txt (length {len(content)})')
