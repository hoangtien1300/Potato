import urllib.request
import csv
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

# Fetch Employee
url_emp = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=790611745"
response = urllib.request.urlopen(url_emp)
content = response.read().decode('utf-8')
lines = content.split('\n')
start_idx = 0
for i, line in enumerate(lines):
    if 'ID Emp' in line:
        start_idx = i
        break

reader = csv.DictReader(io.StringIO('\n'.join(lines[start_idx:])))
rows = list(reader)

print("Unique Roles:")
print(set([r.get('Role', '').strip() for r in rows if r.get('Role')]))

print("\nUnique Search Divisions:")
print(set([r.get('Search Division', '').strip() for r in rows if r.get('Search Division')]))

print("\nEmployees with Academic Level:")
acad_level_staff = [r for r in rows if r.get('Academic Level')]
print(f"Found {len(acad_level_staff)} staff with Academic Level.")
for a in acad_level_staff[:3]:
    print(f"Name: {a['Full Name']}, Level: {a['Academic Level']}, Band: {a['Academic Band']}")
