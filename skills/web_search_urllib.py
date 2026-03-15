import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    """使用 DuckDuckGo 搜尋網路資訊。"""
    base_url = "https://api.duckduckgo.com/"
    params = {
        "q": query,
        "format": "json",
        "pretty": 1,
        "no_redirect": 1  # 防止重新導向
    }
    url = base_url + "?" + urllib.parse.urlencode(params)
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            results = []
            for result in data.get("RelatedTopics", [])[:max_results]:
                results.append(f'{result.get("Text", "")}: {result.get("FirstURL", "")}')
            return results
    except Exception as e:
        return f"搜尋失敗: {e}"

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    results = web_search(query)
    for r in results:
        print(r)