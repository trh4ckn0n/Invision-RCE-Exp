import requests

def zoomeye_search(api_key, dork):
    headers = {"API-KEY": api_key}
    url = f"https://api.zoomeye.org/host/search?query={dork}"
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return [hit["ip"] for hit in r.json().get("matches", [])]
    else:
        return []
