import requests
from dotenv import load_dotenv
import os
load_dotenv("config/.env")
def run(query: str):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {"X-Subscription-Token": os.getenv("BRAVE_API_KEY")}
    params = {"q": query, "count": 5}
    resp = requests.get(url, headers=headers, params=params)
    results = resp.json().get("web", {}).get("results", [])
    return "\n".join([f"{r['title']}: {r['description']}" for r in results])
