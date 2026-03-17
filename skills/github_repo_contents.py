import sys
import urllib.request
import urllib.parse
import json

def get_repo_contents(repo_name):
    """
    從 GitHub API 取得專案的檔案列表。
    """
    url = f"https://api.github.com/repos/{repo_name}/contents"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.load(response)
            return data
    except Exception as e:
        return f"錯誤: {e}"

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else ""
    if not repo_name:
        print("請提供 GitHub 專案名稱 (例如: lobstervis-GIT/bakery-seat-system)")
    else:
        contents = get_repo_contents(repo_name)
        print(contents)