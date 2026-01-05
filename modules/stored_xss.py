import requests
import time

PAYLOAD = "<script>alert(99)</script>"

def scan_stored_xss(url):
    findings = []

    try:
        requests.get(url + f"?comment={PAYLOAD}", timeout=10)
        time.sleep(2)
        r = requests.get(url, timeout=10)

        if PAYLOAD in r.text:
            findings.append({
                "type": "Stored XSS",
                "severity": "Critical",
                "payload": PAYLOAD,
                "url": url
            })
    except:
        pass

    return findings
