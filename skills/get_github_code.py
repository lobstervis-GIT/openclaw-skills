import sys
import os
import urllib.request
import urllib.parse
import zipfile
import io

def download_and_extract(repo_name, output_dir):
    zip_url = f"https://github.com/{repo_name}/archive/refs/heads/main.zip"
    try:
        with urllib.request.urlopen(zip_url) as response:
            if response.getcode() == 200:
                zip_content = response.read()
                with zipfile.ZipFile(io.BytesIO(zip_content), 'r') as zip_ref:
                    zip_ref.extractall(output_dir)
                extracted_folder = os.path.join(output_dir, f"{os.path.basename(repo_name)}-main")
                # Rename the extracted folder to remove '-main' suffix
                target_folder = os.path.join(output_dir, os.path.basename(repo_name))
                os.rename(extracted_folder, target_folder)
                print(f"程式碼已下載並解壓縮到 {target_folder}")
                return target_folder
            else:
                print(f"無法下載倉庫。HTTP 狀態碼: {response.getcode()}")
                return None
    except Exception as e:
        print(f"發生錯誤: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        repo_name = sys.argv[1]
        output_dir = "/tmp/github_code"
        os.makedirs(output_dir, exist_ok=True)
        downloaded_path = download_and_extract(repo_name, output_dir)
        if downloaded_path:
            print(downloaded_path)
        else:
            print("下載失敗")
    else:
        print("請提供 GitHub 倉庫名稱 (例如: lobstervis-GIT/bakery-seat-system)")