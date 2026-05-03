import re
import sys
import os

def check_syntax():
    index_path = r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\index.html'
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract script tag content
    scripts = re.findall(r'<script type="text/babel">(.*?)</script>', content, re.DOTALL)
    if not scripts:
        print("No babel script found")
        return

    full_js = scripts[0]
    
    # Write to a temp file
    temp_path = r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\scratch\temp_check.js'
    with open(temp_path, 'w', encoding='utf-8') as f:
        f.write(full_js)
    
    print(f"JS extracted to {temp_path}")

if __name__ == "__main__":
    check_syntax()
