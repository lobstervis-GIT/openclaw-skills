import sys
import requests

def github_read_file(repo, path):
    url = f"https://raw.githubusercontent.com/{repo}/main/{path}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 檢查是否有錯誤
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    repo_path = sys.argv[1].split(',')
    repo = repo_path[0]
    path = repo_path[1]
    result = github_read_file(repo, path)
    print(result)