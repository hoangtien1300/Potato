import urllib.request
import csv
import io
import sys

# Ensure utf-8 output to avoid charmap errors
sys.stdout.reconfigure(encoding='utf-8')

spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

# Fetch Employee
url_emp = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=790611745"
response = urllib.request.urlopen(url_emp)
content = response.read().decode('utf-8')
reader = csv.DictReader(io.StringIO(content))
employees = [row for row in reader if row.get('Position', '').strip().lower() == 'teacher']

print("--- Employees (Teachers) ---")
for e in employees[:5]:
    print(f"Name: {e.get('Full Name')}, Eng Name: {e.get('Eng Name')}, Level: {e.get('Teaching Level')}, Band: {e.get('Teaching Band')}")

# Fetch Class_Dashboard
url_class = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=1019913137"
response = urllib.request.urlopen(url_class)
content = response.read().decode('utf-8')
lines = content.split('\n')
# Need to find the header row which has 'ID Dashboard'
header_idx = 0
for i, line in enumerate(lines):
    if 'ID Dashboard' in line:
        header_idx = i
        break
reader = csv.DictReader(io.StringIO('\n'.join(lines[header_idx:])))
classes = [row for row in reader]

print("\n--- Teachers in Class_Dashboard ---")
teachers_in_classes = set([c.get('Teacher', '') for c in classes if c.get('Teacher')])
print(list(teachers_in_classes)[:10])

