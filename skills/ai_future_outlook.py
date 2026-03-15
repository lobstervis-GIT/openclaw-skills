import sys
import urllib.request
import urllib.parse
import json

def web_search(query, max_results=5):
    url = "https://duckduckgo.com/?q=" + urllib.parse.quote_plus(query) + "&kl=wt-wt&kp=-1&t=hk&df=y"
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            #print(html)
            # Extract relevant information (this will need refinement)
            results = []
            import re
            for match in re.finditer(r'<a href="([^"]*)" class="[^"]*">(.*?)</a>', html, re.IGNORECASE):
                link = match.group(1)
                title = match.group(2)
                if link.startswith("/"):
                  continue
                results.append({"title": title, "link": link})
            return results
    except Exception as e:
        print(f"Error during web search: {e}")
        return []


if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI 未來發展趨勢"
    search_results = web_search(query)
    print("Web Search Results:")
    for result in search_results:
        print(f"- {result['title']}: {result['link']}")