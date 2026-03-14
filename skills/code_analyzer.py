import sys
import os
import urllib.request
import json

def analyze_repo(repo_name):
    try:
        # 檢查 GitHub 倉庫是否存在
        url = f"https://api.github.com/repos/{repo_name}"
        response = urllib.request.urlopen(url)
        if response.getcode() != 200:
            print(f"倉庫 {repo_name} 不存在。")
            return

        # 在這裡可以進一步分析程式碼，例如：
        # 1. 找出依賴關係：分析 import 語句，找出模組之間的依賴關係。
        # 2. 檢查模組大小：找出過大的模組，這些模組可能需要拆分。
        # 3. 檢查循環依賴：找出循環依賴的模組，這些依賴關係會導致程式碼難以維護。
        # 4. 找出不穩定的依賴：找出依賴於過多其他模組的模組，這些模組可能需要重構。

        print(f"開始分析倉庫 {repo_name}...")
        print("（目前只檢查倉庫是否存在，尚未實作程式碼分析）")

    except urllib.error.URLError as e:
        print(f"發生網路錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else ""
    if repo_name:
        analyze_repo(repo_name)
    else:
        print("請提供 GitHub 倉庫名稱。")