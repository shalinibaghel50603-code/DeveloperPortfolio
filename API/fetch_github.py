import json
import urllib.request

# Fetch public GitHub user profile via REST API (Q3 - C03)
USERNAME = "shalinibaghel50603-code"
URL = f"https://github.com{USERNAME}"

def fetch_profile():
    req = urllib.request.Request(URL, headers={"User-Agent": "Python-Portfolio-Script"})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode("utf-8"))

    summary = {
        "login": data.get("login"),
        "profile_url": data.get("html_url"),
        "public_repos": data.get("public_repos"),
        "followers": data.get("followers"),
        "created_at": data.get("created_at")
    }

    with open("response.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4)

    print("API Response Saved to response.json:")
    print(json.dumps(summary, indent=4))

if __name__ == "__main__":
    fetch_profile()
