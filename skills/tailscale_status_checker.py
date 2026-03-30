import sys
import json
import urllib.request
from urllib.parse import urlencode

def main():
    # 模擬 tailscale 狀態查詢 (因無實際 API key 故僅模擬格式)
    try:
        fake_data = {
            "Self": {"ID": "self-node", "HostName": "lobster-machine", "Online": True},
            "Peer": [
                {"ID": "peer-1", "HostName": "bakery-server", "Online": True},
                {"ID": "peer-2", "HostName": "playground-server", "Online": False}
            ]
        }
        print(json.dumps(fake_data, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()