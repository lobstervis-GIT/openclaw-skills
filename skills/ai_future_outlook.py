import sys
import urllib.request
import urllib.parse
import json

def search(query, max_results=3):
    url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json"
    try:
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        results = []
        for result in data.get("RelatedTopics", []):
            if isinstance(result, dict) and "FirstURL" in result and "Text" in result:
                results.append({"title": result["Text"], "url": result["FirstURL"]})
                if len(results) >= max_results:
                    break
        return results
    except Exception as e:
        return [{"error": str(e)}]

if __name__ == "__main__":
    query = sys.argv[1] if len(sys.argv) > 1 else "AI future trends"
    results = search(query)
    for r in results:
        print(f"- {r.get('title', '')}: {r.get('url', '')}")