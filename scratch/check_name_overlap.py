import urllib.request
import csv
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

# Fetch Class_Dashboard
url_class = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=1019913137"
response = urllib.request.urlopen(url_class)
content = response.read().decode('utf-8')
lines = content.split('\n')
header_idx = 0
for i, line in enumerate(lines):
    if 'ID Dashboard' in line:
        header_idx = i
        break
reader = csv.DictReader(io.StringIO('\n'.join(lines[header_idx:])))
classes = list(reader)

teachers = set([c.get('Teacher', '').strip() for c in classes if c.get('Teacher')])
print("Sample Teachers in Class_Dashboard:")
print(list(teachers)[:10])

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
employees = list(reader)

acad_staff = [r for r in rows if r.get('Academic Level')] # Wait, 'rows' was defined in previous cell.
# Better fetch again.
acad_staff_names = [r.get('Full Name', '').strip() for r in employees if r.get('Academic Level')]
print(f"\nAcademic Staff Names: {acad_staff_names}")

overlap = set(acad_staff_names).intersection(teachers)
print(f"\nOverlap: {overlap}")
