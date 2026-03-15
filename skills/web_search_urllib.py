import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    base_url = "https://duckduckgo.com/?q="
    text = urllib.parse.quote_plus(query)
    url = base_url + text + "&kl=wt-wt"
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')

        start = html.find('results="')
        if start == -1:
            return []
        start += len('results="')
        end = html.find('" ',start)
        results = html[start:end]
        results = json.loads(results)

        return results[:max_results]

    except Exception as e:
        print(f"Error during web search: {e}")
        return []

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    search_results = web_search(query)
    print(json.dumps(search_results, indent=2, ensure_ascii=False))