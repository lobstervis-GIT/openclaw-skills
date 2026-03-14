import sys
import os
import urllib.request
import urllib.parse
import zipfile
import io

def download_and_extract(repo_name, dest_dir):
    """Downloads a GitHub repository as ZIP and extracts it."""
    zip_url = f"https://github.com/{{repo_name}}/archive/refs/heads/main.zip"
    try:
        with urllib.request.urlopen(zip_url) as resp:
            if resp.getcode() != 200:
                raise ValueError(f"Failed to download {{zip_url}}: HTTP {{resp.getcode()}}")
            data = resp.read()
            zip_file = zipfile.ZipFile(io.BytesIO(data))
            zip_file.extractall(dest_dir)
            # GitHub creates a root folder like "repo-main", rename it to dest_dir
            root_folder = os.path.join(dest_dir, os.listdir(dest_dir)[0])
            for item in os.listdir(root_folder):
                s = os.path.join(root_folder, item)
                d = os.path.join(dest_dir, item)
                os.rename(s, d)
            os.rmdir(root_folder)

    except Exception as e:
        print(f"Error downloading or extracting: {e}")
        return False
    return True

def main():
    if len(sys.argv) < 2:
        print("Usage: python get_github_code.py <repo_name>")
        return

    repo_name = sys.argv[1]
    dest_dir = "repo"  # Fixed destination directory

    os.makedirs(dest_dir, exist_ok=True)

    if download_and_extract(repo_name, dest_dir):
        print(f"Successfully downloaded and extracted {repo_name} to {dest_dir}")
    else:
        print(f"Failed to download and extract {repo_name}")

if __name__ == "__main__":
    main()