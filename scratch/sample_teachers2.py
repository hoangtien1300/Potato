import urllib.request
import csv
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

url_emp = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=790611745"
response = urllib.request.urlopen(url_emp)
content = response.read().decode('utf-8')
reader = csv.DictReader(io.StringIO(content))
rows = list(reader)

positions = set([r.get('Position', '').strip() for r in rows if r.get('Position')])
print("Positions in Employee sheet:")
print(positions)

teachers = [r for r in rows if 'teacher' in r.get('Position', '').lower()]
print(f"\nFound {len(teachers)} employees with 'teacher' in Position.")
for e in teachers[:5]:
    print(f"Name: {e.get('Full Name')}, Eng Name: {e.get('Eng Name')}, Position: {e.get('Position')}, Level: {e.get('Teaching Level')}, Band: {e.get('Teaching Band')}")
