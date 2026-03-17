import sys
import urllib.request
import urllib.parse
import json

def main():
    try:
        repo_name = sys.argv[1]
        file_path = sys.argv[2]

        # GitHub API endpoint for getting file content
        api_url = f"https://api.github.com/repos/{repo_name}/contents/{file_path}"

        # Make the request
        req = urllib.request.Request(api_url)
        response = urllib.request.urlopen(req)
        data = json.loads(response.read().decode())

        # Check if content is base64 encoded
        if 'encoding' in data and data['encoding'] == 'base64':
            import base64
            content = base64.b64decode(data['content']).decode()
        else:
            content = data['content']

        print(content)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()