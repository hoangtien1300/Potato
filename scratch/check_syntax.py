import sys
import re

with open(r'd:\02 POTATO English\Antigravity\Dashboard\Dashboard\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract script content
scripts = re.findall(r'<script type="text/babel">(.*?)</script>', text, re.DOTALL)
if scripts:
    content = scripts[0]
    # Simple brace balance check
    open_braces = content.count('{')
    close_braces = content.count('}')
    print(f"Open braces: {open_braces}, Close braces: {close_braces}")
    if open_braces != close_braces:
        print("ERROR: Unbalanced braces!")
    
    # Check for unmatched parentheses
    open_parens = content.count('(')
    close_parens = content.count(')')
    print(f"Open parens: {open_parens}, Close parens: {close_parens}")
else:
    print("No script block found")
