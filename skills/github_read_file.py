import sys
import requests

def github_read_file(repo, path):
    url = f"https://raw.githubusercontent.com/{repo}/main/{path}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # 檢查是否有錯誤發生
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error reading file: {e}"

if __name__ == "__main__":
    repo_path = sys.argv[1] if len(sys.argv) > 1 else ""
    if "/" not in repo_path:
        print("Invalid repo/path format.  Should be repo_owner/repo_name/path/to/file")
    else:
      repo, path = repo_path.split("/", 1)
      content = github_read_file(repo, path)
      print(content)