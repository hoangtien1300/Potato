import urllib.request
import csv
import io
import sys

sys.stdout.reconfigure(encoding='utf-8')

spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

# Check HR (Shift Scheduler data)
url_hr = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid=2074366601"
try:
    response = urllib.request.urlopen(url_hr)
    content = response.read().decode('utf-8')
    reader = csv.reader(io.StringIO(content))
    rows = list(reader)
    print("--- HR Tab Headers ---")
    print(rows[1] if len(rows) > 1 else rows[0])
    print("\n--- Sample Row ---")
    print(rows[2] if len(rows) > 2 else "No data")
except Exception as e:
    print(f"Error: {e}")
