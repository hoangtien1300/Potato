import json, re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard_theme_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace escaped characters and search for HTML content
text = text.replace('\\n', '\n').replace('\\"', '"')
matches = re.finditer(r'(<!DOCTYPE html.*?>.*?</html>|&lt;!DOCTYPE html.*?&lt;/html&gt;)', text, re.IGNORECASE | re.DOTALL)

for i, match in enumerate(matches):
    content = match.group(1)
    if len(content) > 1000:
        with open(rf'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\extracted_html_{i}.txt', 'w', encoding='utf-8') as out:
            import html
            out.write(html.unescape(content))
        print(f'Wrote extracted_html_{i}.txt (length {len(content)})')
