import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    base_url = "https://duckduckgo.com/?q="
    quote_query = urllib.parse.quote_plus(query)
    search_url = base_url + quote_query + "&kl=wt-wt"

    try:
        req = urllib.request.Request(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')

        # Extract results (this is a simplified example, you might need a more robust HTML parsing)
        results = []
        start = html.find('Results') # 簡單地尋找 "Results" 這個詞
        if start != -1:
            results = html[start:start+500] # 簡單地擷取一段文字

        return results
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI的未來"
    results = web_search(query)
    print(results)