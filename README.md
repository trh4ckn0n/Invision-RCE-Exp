# Invision RCE Exploit Toolkit

## Features

- Interactive shell with Rich UI
- Dorking via Zoomeye API
- Header-based vulnerability scanner
- Full payload control
- Report generation (future)

## Usage

```bash
pip install -r requirements.txt
python3 -m invision_rce.exploit https://target.com
```

## Dork example

```
zoomeye_search("API_KEY", "X-IPS-LoggedIn")
```
