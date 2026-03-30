import sys
import subprocess
import json

repo_name = sys.argv[1]

command = ['gh', 'repo', 'list-files', repo_name, '--json', 'path']
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

if stderr:
    print(f"Error: {stderr.decode()}")
else:
    try:
        data = json.loads(stdout.decode())
        files = [item['path'] for item in data]
        print(json.dumps(files))
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Raw output: {stdout.decode()}")
    except Exception as e:
        print(f"Error: {e}")