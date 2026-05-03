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
reader = csv.DictReader(io.StringIO(content))
employees = list(reader)
academic_staff = [e['ID Emp'] for e in employees if 'academic' in e.get('Position', '').lower()]

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

teachers_in_classes = set([c.get('Teacher', '') for c in classes if c.get('Teacher')])

overlap = set(academic_staff).intersection(teachers_in_classes)
print(f"Academic Staff IDs: {academic_staff[:5]}")
print(f"Overlap between Academic Staff and Class 'Teacher' column: {overlap}")
