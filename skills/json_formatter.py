import sys, json

json_string = sys.argv[1]

try:
    data = json.loads(json_string)
    formatted_json = json.dumps(data, indent=4, ensure_ascii=False)
    print(formatted_json)
except json.JSONDecodeError as e:
    print(f"JSON 格式錯誤: {e}")
except Exception as e:
    print(f"發生錯誤: {e}")