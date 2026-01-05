import requests
import time
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

TIME_PAYLOADS = [
    "' AND SLEEP(3)-- ",
    "\" AND SLEEP(3)-- ",
    "'; WAITFOR DELAY '0:0:3'--",
    "\"; WAITFOR DELAY '0:0:3'--"
]

THRESHOLD = 2.5  # seconds


def scan_blind_sqli(urls):
    findings = []

    for url in urls:
        parsed = urlparse(url)
        params = parse_qs(parsed.query)

        if not params:
            continue

        for param in params:
            for payload in TIME_PAYLOADS:
                test_params = params.copy()
                test_params[param] = payload
                new_query = urlencode(test_params, doseq=True)
                test_url = urlunparse(parsed._replace(query=new_query))

                try:
                    start = time.time()
                    requests.get(test_url, timeout=10)
                    elapsed = time.time() - start

                    if elapsed > THRESHOLD:
                        findings.append({
                            "type": "Blind SQL Injection (Time-Based)",
                            "severity": "Critical",
                            "parameter": param,
                            "payload": payload,
                            "url": test_url,
                            "description": "Response delay indicates possible time-based SQL injection.",
                            "recommendation": "Use parameterized queries and avoid dynamic SQL."
                        })
                        return findings  # stop after confirmation
                except:
                    pass

    return findings
