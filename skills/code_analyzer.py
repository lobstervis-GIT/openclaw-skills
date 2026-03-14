import sys
import os
import re
import urllib.request
import urllib.parse
import json

def analyze_code_coupling(repo_name):
    try:
        # 檢查 repo_name 格式
        if not re.match(r"^[^/]+/[^/]+$", repo_name):
            print(f"倉庫名稱格式不正確: {repo_name}，應為 owner/repo_name")
            return

        # GitHub API 獲取倉庫資訊
        api_url = f"https://api.github.com/repos/{repo_name}"
        try:
            response = urllib.request.urlopen(api_url)
            if response.getcode() != 200:
                print(f"無法找到倉庫: {repo_name}")
                return
            repo_info = json.loads(response.read().decode())
        except urllib.error.URLError as e:
            print(f"無法連接 GitHub API: {e}")
            return

        # 這裡可以加入更詳細的程式碼分析邏輯
        # 由於環境限制，無法使用 ast 等模組進行深入分析
        # 目前僅簡單示範，可以根據檔案名或內容進行初步判斷
        print(f"開始分析倉庫：{repo_name}")
        print(f"倉庫描述：{repo_info.get('description', '無描述')}")
        print("初步分析：")
        print("- 檢查是否存在過於緊密的依賴關係 (例如：大量的 import 語句)")
        print("- 檢查是否存在循環依賴")
        print("- 檢查模組或類別是否具有單一職責")

        # 示例：列出倉庫中的檔案（前 10 個）
        contents_url = f"https://api.github.com/repos/{repo_name}/contents"
        try:
            response = urllib.request.urlopen(contents_url)
            if response.getcode() == 200:
                contents = json.loads(response.read().decode())
                print("\n檔案列表 (前 10 個):")
                for i, item in enumerate(contents[:10]):
                    print(f"{i+1}. {item['name']}")
            else:
                print("無法獲取檔案列表")
        except urllib.error.URLError as e:
            print(f"無法獲取檔案列表: {e}")

    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else ""
    if repo_name:
        analyze_code_coupling(repo_name)
    else:
        print("請提供 GitHub 倉庫名稱 (owner/repo_name)")