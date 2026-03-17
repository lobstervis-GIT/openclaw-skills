import sys
import json
import urllib.request

def read_file_from_github(repo, path):
    url = f"https://raw.githubusercontent.com/{repo}/main/{path}"
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode()
            return data
    except Exception as e:
        print(f"Error reading file from GitHub: {e}")
        return None

def execute_operation(config):
    # 這裡根據 config 內容執行操作，目前只是一個範例
    print(f"執行 config 裡定義的操作，config 內容: {config}")

if __name__ == "__main__":
    repo_name = sys.argv[1]
    config_file_path = "config.json"
    config_content = read_file_from_github(repo_name, config_file_path)

    if config_content:
        try:
            config = json.loads(config_content)
            execute_operation(config)
        except json.JSONDecodeError as e:
            print(f"Error decoding config.json: {e}")
    else:
        print("無法讀取 config.json 檔案")