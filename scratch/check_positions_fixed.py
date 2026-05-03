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
# Skip empty rows or rows that don't have 'ID Emp'
start_idx = 0
for i, line in enumerate(lines):
    if 'ID Emp' in line:
        start_idx = i
        break

reader = csv.DictReader(io.StringIO('\n'.join(lines[start_idx:])))
rows = list(reader)

print("Unique Positions:")
positions = set([r.get('Position', '').strip() for r in rows if r.get('Position')])
print(positions)

academic_staff = [r for r in rows if 'academic' in r.get('Position', '').lower()]
print(f"\nFound {len(academic_staff)} Academic staff.")
for a in academic_staff[:3]:
    print(f"ID: {a['ID Emp']}, Name: {a['Full Name']}, Position: {a['Position']}")
