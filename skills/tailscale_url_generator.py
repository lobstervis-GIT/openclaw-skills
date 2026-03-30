import sys
import urllib.parse

def main():
    args = sys.argv[1:]
    if not args:
        print("請提供主機名稱")
        return

    hostname = args[0]
    # 假設預設域名是 tailscale.net，實際應用中可以從環境變數或參數讀取
    domain = "tailnet.example.com"
    if len(args) > 1:
        domain = args[1]

    # 產生 URL
    url = f"https://{hostname}.{domain}"
    print(url)

if __name__ == "__main__":
    main()