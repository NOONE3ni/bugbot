#!/usr/bin/env python3

import argparse
from core.crawler import crawl
from modules.xss import scan_xss
from modules.sqli import scan_sqli
from modules.report import save_report
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        description="BugBot - Educational Web Vulnerability Scanner"
    )

    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scan a target URL")
    scan_parser.add_argument("-u", "--url", required=True, help="Target URL")

    args = parser.parse_args()

    if args.command == "scan":
        target = args.url
        print("[*] Crawling target...")

        urls = crawl(target)
        findings = []

        print(f"[*] Testing {len(urls)} URLs...\n")

        # XSS
        xss_results = scan_xss(urls)
        for f in xss_results:
            print(f"[+] XSS found at: {f['url']}")
            findings.append(f)

        # SQLi
        sqli_results = scan_sqli(urls)
        for f in sqli_results:
            print(f"[+] SQLi found at: {f['url']}")
            findings.append(f)

        report = {
            "tool": "BugBot",
            "date": str(datetime.now()),
            "target": target,
            "findings": findings
        }

        save_report(report)

        print("\n[✓] Scan complete. Reports saved in reports/")

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
