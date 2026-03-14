import sys
import os
import urllib.request
import urllib.parse
import zipfile
import io

def download_and_extract_zip(repo_name, output_dir):
    zip_url = f"https://github.com/{repo_name}/archive/refs/heads/main.zip"
    try:
        with urllib.request.urlopen(zip_url) as response:
            if response.getcode() != 200:
                raise Exception(f"Failed to download zip file: HTTP {response.getcode()}")
            zip_content = response.read()
            
            with zipfile.ZipFile(io.BytesIO(zip_content), 'r') as zip_ref:
                # 避免壓縮檔內的絕對路徑攻擊
                for member in zip_ref.infolist():
                    filepath = os.path.normpath(member.filename)
                    if filepath.startswith("..") or os.path.isabs(filepath):
                        raise Exception("Invalid file path in zip archive")

                zip_ref.extractall(output_dir)
            
            # GitHub 預設會在 zip 裡放一層目錄，需要調整
            extracted_folder = os.path.join(output_dir, os.path.splitext(os.path.basename(zip_url))[0])
            repo_folder = os.path.join(output_dir, repo_name.split("/")[1] + "-main")
            if os.path.exists(extracted_folder) and os.path.isdir(extracted_folder):
                # 將內容移動到 repo_folder
                for item in os.listdir(extracted_folder):
                    s = os.path.join(extracted_folder, item)
                    d = os.path.join(repo_folder, item)
                    if os.path.isdir(s):
                        import shutil
                        shutil.move(s, d)
                    else:
                        os.rename(s, d)
                # 刪除空目錄
                os.rmdir(extracted_folder)


            print(f"程式碼已下載並解壓縮到 {repo_folder}")
            return repo_folder
    except Exception as e:
        print(f"下載或解壓縮失敗: {e}")
        return None

if __name__ == "__main__":
    repo_name = sys.argv[1] if len(sys.argv) > 1 else None
    if not repo_name:
        print("請提供 GitHub 倉庫名稱 (例如: lobstervis-GIT/bakery-seat-system)")
        sys.exit(1)
    
    output_dir = "repo"
    os.makedirs(output_dir, exist_ok=True)
    
    repo_path = download_and_extract_zip(repo_name, output_dir)
    if repo_path:
        print(f"倉庫路徑: {repo_path}")
    else:
        sys.exit(1)