import requests
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse
import html

PAYLOADS = [
    "<script>alert(1)</script>",
    "\"'><svg/onload=alert(1)>",
    "<img src=x onerror=alert(1)>"
]

def build_test_urls(url, payload):
    parsed = urlparse(url)
    qs = parse_qs(parsed.query)

    test_urls = []

    if qs:
        for param in qs:
            new_qs = qs.copy()
            new_qs[param] = payload
            new_query = urlencode(new_qs, doseq=True)
            test_urls.append(
                urlunparse(parsed._replace(query=new_query))
            )
    else:
        test_urls.append(url + "?q=" + payload)

    return test_urls


def scan_xss(urls):
    findings = []

    for url in urls:
        for payload in PAYLOADS:
            test_urls = build_test_urls(url, payload)

            for test_url in test_urls:
                try:
                    r = requests.get(test_url, timeout=5)

                    body = r.text
                    decoded = html.unescape(body)

                    if payload in body or payload in decoded:
                        findings.append({
                            "type": "XSS",
                            "url": test_url,
                            "payload": payload
                        })

                except Exception:
                    continue

    return findings
