import requests
import json

app_id = "35e5f9f7-248a-4eb4-a87e-672f26329edc"
access_key = "V2-ETGLA-CModK-89vqJ-sDZuU-PRMcH-y4WbA-429bw-9A60N"
tables = ['Lich_Truc', 'Danh_Sach_Lop', 'Hoc_Vien', 'Diem_Danh', 'Cong_No']

all_data = {}

for table_name in tables:
    url = f"https://api.appsheet.com/api/v2/apps/{app_id}/tables/{table_name}/Action"
    headers = {
        "ApplicationAccessKey": access_key,
        "Content-Type": "application/json"
    }
    payload = {
        "Action": "Find",
        "Properties": {
            "Locale": "vi-VN",
            "Timezone": "Asia/Bangkok"
        },
        "Rows": []
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        print(f"--- Table: {table_name} ---")
        print(f"Status: {response.status_code}")
        print(f"Raw: '{response.text}'")
        if response.status_code == 200:
            try:
                data = response.json()
                all_data[table_name] = data[:3] if isinstance(data, list) else data
            except:
                all_data[table_name] = "Non-JSON response"
        else:
            all_data[table_name] = f"Error: {response.status_code}"
    except Exception as e:
        all_data[table_name] = f"Exception: {str(e)}"

print(json.dumps(all_data, indent=2, ensure_ascii=False))
