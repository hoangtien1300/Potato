import urllib.request
import csv
import io

gids = {
    'Danh_Sach_Lop': '2009932031',
    'Class_Dashboard': '1019913137',
    'Employee': '790611745'
}
spreadsheet_id = '1dTcxPgSS2olUtgjjk2ZUvUo8e53Vi6J5Kk4bynKL0OE'

for name, gid in gids.items():
    url = f"https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv&gid={gid}"
    try:
        response = urllib.request.urlopen(url)
        content = response.read().decode('utf-8')
        reader = csv.reader(io.StringIO(content))
        lines = list(reader)
        print(f"--- {name} ---")
        for i, row in enumerate(lines[:5]):
            print(f"Row {i}: {row}")
    except Exception as e:
        print(f"Error fetching {name}: {e}")
