import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    search_url = "https://duckduckgo.com/?q=" + urllib.parse.quote_plus(query)
    results = []
    try:
        with urllib.request.urlopen(search_url) as response:
            html = response.read().decode('utf-8')
            # DuckDuckGo Instant Answer API might be a better option for structured results
            # For now, just return the raw HTML
            results.append(html)
    except Exception as e:
        results.append(f"Error: {e}")
    return results

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    results = web_search(query)
    print(json.dumps(results))