import urllib.request, re
url = 'https://docs.google.com/spreadsheets/d/1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE/htmlview'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read().decode('utf-8')

# Search for "Employee"
idx = html.find('Employee')
if idx != -1:
    print(html[max(0, idx-100):idx+100])
else:
    print("Employee not found")

import json
# maybe the data is in some JS object?
matches = re.findall(r'\{[^{}]*Employee[^{}]*\}', html)
for m in matches:
    print(m)
