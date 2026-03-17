import sys
import urllib.request
import urllib.parse
import json
import base64

def main():
    try:
        repo_name = sys.argv[1]
        file_path = sys.argv[2]

        # GitHub API endpoint for getting file content
        api_url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"

        # Set up the request headers (including the Accept header)
        headers = {'Accept': 'application/vnd.github.v3.raw'}
        req = urllib.request.Request(api_url, headers=headers)

        with urllib.request.urlopen(req) as response:
            if response.getcode() == 200:
                content = response.read().decode('utf-8')
                print(content)
            else:
                print(f"Error: Unable to retrieve file. HTTP status code: {response.getcode()}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()