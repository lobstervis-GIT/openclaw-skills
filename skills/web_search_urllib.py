import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    search_url = "https://duckduckgo.com/?q=" + urllib.parse.quote_plus(query) + "&kl=wt-wt"
    try:
        with urllib.request.urlopen(search_url) as response:
            html = response.read().decode('utf-8')
            # This is a very basic scraping, you might want to use a proper HTML parser
            results = []
            for i in range(min(max_results, html.count("result__a"))):
                start = html.find("result__a")
                end = html.find("</a>", start)
                link = html[start + 10:end]
                results.append(link)
                html = html[end+4:]
        return results
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "test"
    results = web_search(query)
    print(json.dumps(results))