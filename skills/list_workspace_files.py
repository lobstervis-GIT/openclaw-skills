import os
import sys

def list_files(path):
    try:
        files = os.listdir(path)
        for file in files:
            print(file)
    except OSError:
        print(f"無法存取路徑: {path}")

list_files("." if len(sys.argv) <= 1 else sys.argv[1])