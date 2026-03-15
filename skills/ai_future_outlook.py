import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    search_url = "https://duckduckgo.com/?q=" + urllib.parse.quote_plus(query) + "&format=json&pretty=1"
    try:
        with urllib.request.urlopen(search_url) as response:
            data = json.loads(response.read().decode('utf-8'))
            return [result['title'] + ": " + result['snippet'] for result in data['Results']] if data['Results'] else ["No results found."]
    except Exception as e:
        return [f"Search failed: {e}"]

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    results = web_search(query)
    for result in results:
        print(result)