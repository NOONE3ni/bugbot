import json
import os

def save_report(report):
    os.makedirs("reports", exist_ok=True)

    path = "reports/results.json"
    with open(path, "w") as f:
        json.dump(report, f, indent=4)
