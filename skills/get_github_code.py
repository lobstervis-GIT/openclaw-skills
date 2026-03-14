import sys
import os
import subprocess

repo_name = sys.argv[1] if len(sys.argv) > 1 else ""

if not repo_name:
    print("請提供 GitHub 倉庫名稱 (例如: lobstervis-GIT/bakery-seat-system)")
    sys.exit(1)

repo_url = f"https://github.com/{repo_name}"
repo_dir = f"/tmp/{repo_name.replace('/', '_')}"

if os.path.exists(repo_dir):
    print(f"倉庫 {repo_name} 已經存在於 {repo_dir}，將先刪除。")
    subprocess.run(['rm', '-rf', repo_dir])

try:
    result = subprocess.run(['git', 'clone', repo_url, repo_dir], capture_output=True, text=True, timeout=60)
    if result.returncode == 0:
        print(f"成功抓取 {repo_name} 到 {repo_dir}")
        print(f"程式碼位置: {repo_dir}")
        print(repo_dir)
    else:
        print(f"抓取 {repo_name} 失敗: {result.stderr}")
        if "Repository not found" in result.stderr:
            print("倉庫不存在。")
        else:
            print("Git 命令執行錯誤。")
        sys.exit(1)
except Exception as e:
    print(f"發生錯誤: {e}")
    sys.exit(1)