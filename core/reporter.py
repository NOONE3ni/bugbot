import json
from datetime import datetime

def save_report(results):
    report = {
        "date": str(datetime.now()),
        "findings": results
    }

    with open("reports/results.json", "w") as f:
        json.dump(report, f, indent=4)
