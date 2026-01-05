import requests

PAYLOADS = [
    "' OR '1'='1",
    "' OR 1=1--"
]

def scan_sqli(urls):
    results = []

    for url in urls:
        for payload in PAYLOADS:
            try:
                r = requests.get(url, params={"id": payload}, timeout=5)
                if "sql" in r.text.lower() or "syntax" in r.text.lower():
                    results.append({
                        "type": "SQL Injection",
                        "url": url,
                        "payload": payload
                    })
            except Exception:
                pass

    return results
