import requests

def check_headers(url):
    try:
        r = requests.get(url, timeout=5)
        headers = r.headers
        return any(h in headers.get("Server", "") for h in ["Invision", "IPS"]) or                "X-IPS-LoggedIn" in headers or                "Powered by Invision Community" in r.text
    except:
        return False
