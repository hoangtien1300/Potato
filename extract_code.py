import json, re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard_theme_2.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace escaped characters
text = text.replace(r'\n', '\n').replace(r'\"', '"')

# Search for <!DOCTYPE html> ... </html>
matches = re.finditer(r'(<!DOCTYPE html.*?>.*?</html>)', text, re.IGNORECASE | re.DOTALL)

best_match = None
max_len = 0
for match in matches:
    print(f"Found match of length {len(match.group(1))}")
    if len(match.group(1)) > max_len:
        max_len = len(match.group(1))
        best_match = match.group(1)

# Also check for code blocks like ```html ... ```
code_blocks = re.finditer(r'```html(.*?)```', text, re.IGNORECASE | re.DOTALL)
for match in code_blocks:
    print(f"Found code block of length {len(match.group(1))}")
    if len(match.group(1)) > max_len:
        max_len = len(match.group(1))
        best_match = match.group(1)

if best_match:
    with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\extracted_theme.html', 'w', encoding='utf-8') as out:
        out.write(best_match.strip())
    print(f'Extracted {max_len} bytes to extracted_theme.html')
else:
    print('No code block found.')
