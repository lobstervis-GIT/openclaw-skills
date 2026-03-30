import sys
import socket
import urllib.parse

def simulate_local_deployment():
    # 模擬本地部署的邏輯
    # 這裡我們假設服務運行在本地的8080端口
    local_ip = socket.gethostbyname(socket.gethostname())
    port = 8080
    service_name = "bakery-seat-system"
    
    # 生成Tailscale URL
    tailscale_url = f"https://{urllib.parse.quote(service_name)}.local:{port}"
    
    return {
        "local_ip": local_ip,
        "port": port,
        "service_name": service_name,
        "tailscale_url": tailscale_url
    }

if __name__ == "__main__":
    try:
        result = simulate_local_deployment()
        print(f"模擬本地部署完成:")
        print(f"  服務名稱: {result['service_name']}")
        print(f"  本地IP: {result['local_ip']}")
        print(f"  端口: {result['port']}")
        print(f"  Tailscale URL: {result['tailscale_url']}")
    except Exception as e:
        print(f"模擬本地部署時發生錯誤: {e}")