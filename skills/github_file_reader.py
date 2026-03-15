import sys
import os
import urllib.request
import urllib.parse
import json

def read_github_file(repo, path):
    try:
        # Construct the API URL for the file content
        url = f"https://api.github.com/repos/{repo}/contents/{path}"
        
        # Add authentication if needed (replace with your token or credentials)
        # For public repos, this might not be necessary
        # auth = "token YOUR_GITHUB_TOKEN"
        # headers = {"Authorization": auth}
        # req = urllib.request.Request(url, headers=headers)

        req = urllib.request.Request(url)
        
        # Fetch the file content
        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode('utf-8'))
                content = data['content']
                encoding = data['encoding']

                if encoding == 'base64':
                    import base64
                    content = base64.b64decode(content).decode('utf-8')
                
                print(content)
            else:
                print(f"Failed to fetch file: {response.getcode()}")
    
    except urllib.error.URLError as e:
        print(f"URLError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python github_file_reader.py <repo> <path>")
        sys.exit(1)

    repo = sys.argv[1]
    path = sys.argv[2]
    read_github_file(repo, path)