import sys
import urllib.request
import urllib.parse
import json

def github_list_issues(repo):
    url = f"https://api.github.com/repos/{repo}/issues"
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            return data
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    repo = sys.argv[1]
    issues = github_list_issues(repo)
    print(json.dumps(issues))