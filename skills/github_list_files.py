import sys
import urllib.request
import json

def main():
    repo_name = sys.argv[1] if len(sys.argv) > 1 else "bakery-seat-system"
    owner = "lobstervis-GIT"
    url = f"https://api.github.com/repos/{owner}/{repo_name}/contents"
    
    try:
        req = urllib.request.Request(url)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read())
        
        print(f"{repo_name} 的檔案列表:")
        for item in data:
            print(f"- {item['name']} ({item['type']})")
    except Exception as e:
        print(f"錯誤: {e}")

if __name__ == "__main__":
    main()