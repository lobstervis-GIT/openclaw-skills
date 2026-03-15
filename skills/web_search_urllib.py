import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    base_url = "https://duckduckgo.com/?q={}&kl=wt-wt&t=h_&ia=web"
    quoted_query = urllib.parse.quote_plus(query)
    url = base_url.format(quoted_query)

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8")

        # DuckDuckGo doesn't provide a clean API, so we'll have to use some basic string parsing.
        results = []
        for i in range(max_results):
            start = html.find('result__a href="', i*500) # Adjust offset as needed
            if start == -1:
                break
            start += len('result__a href="')
            end = html.find('"', start)
            link = html[start:end]
            results.append(link)

        return results
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    results = web_search(query)
    print(json.dumps(results))