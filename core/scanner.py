from modules.xss import test_xss
from modules.sqli import test_sqli

def scan_urls(urls):
    findings = []

    for url in urls:
        print("[*] Testing:", url)

        xss = test_xss(url)
        if xss:
            findings.append(xss)

        sqli = test_sqli(url)
        if sqli:
            findings.append(sqli)

    return findings
