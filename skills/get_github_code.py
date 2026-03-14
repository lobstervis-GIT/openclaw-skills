import sys
import os
import urllib.request
import urllib.parse
import json

def get_github_code(repo_name):
    """
    從 GitHub 倉庫抓取程式碼。
    """
    try:
        # 1. 取得仓库信息
        api_url = f"https://api.github.com/repos/{repo_name}"
        with urllib.request.urlopen(api_url) as response:
            repo_info = json.load(response)
        
        # 2. 取得預設分支
        default_branch = repo_info["default_branch"]
        
        # 3. 取得根目錄下的所有檔案
        api_url = f"https://api.github.com/repos/{repo_name}/git/trees/{default_branch}?recursive=1"
        with urllib.request.urlopen(api_url) as response:
            tree_info = json.load(response)
        
        # 4. 抓取程式碼
        code_files = {}
        for item in tree_info["tree"]:
            if item["type"] == "blob":
                file_path = item["path"]
                raw_url = f"https://raw.githubusercontent.com/{repo_name}/{default_branch}/{file_path}"
                try:
                    with urllib.request.urlopen(raw_url) as raw_response:
                        code = raw_response.read().decode("utf-8")
                        code_files[file_path] = code
                except Exception as e:
                    print(f"抓取檔案 {file_path} 失敗: {e}")

        return code_files

    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else ""
    if repo_name:
        result = get_github_code(repo_name)
        if result:
            print(json.dumps(result))
        else:
            print("抓取程式碼失敗")
    else:
        print("請提供 GitHub 倉庫名稱")