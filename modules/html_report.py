import datetime
import json
import os


def generate_html_report(findings, output_path="reports/report.html"):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>BugBot Scan Report</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 20px;
        }}
        h1 {{
            color: #333;
        }}
        .meta {{
            margin-bottom: 20px;
            color: #555;
        }}
        .finding {{
            background: #fff;
            padding: 15px;
            margin-bottom: 15px;
            border-left: 5px solid #e74c3c;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }}
        .severity {{
            font-weight: bold;
            color: #c0392b;
        }}
        .safe {{
            border-left-color: #2ecc71;
        }}
        code {{
            background: #eee;
            padding: 2px 4px;
        }}
    </style>
</head>
<body>

<h1>BugBot Scan Report</h1>
<div class="meta">
    <p><strong>Date:</strong> {date}</p>
    <p><strong>Total Findings:</strong> {len(findings)}</p>
</div>
"""

    if not findings:
        html += """
<div class="finding safe">
    <p>No vulnerabilities were found.</p>
</div>
"""
    else:
        for f in findings:
            html += f"""
<div class="finding">
    <p><strong>Type:</strong> {f.get("type", "N/A")}</p>
    <p><strong>Severity:</strong> <span class="severity">{f.get("severity", "N/A")}</span></p>
    <p><strong>URL:</strong> {f.get("url", "N/A")}</p>
    <p><strong>Payload:</strong> <code>{f.get("payload", "N/A")}</code></p>
    <p><strong>Description:</strong> {f.get("description", "N/A")}</p>
    <p><strong>Recommendation:</strong> {f.get("recommendation", "N/A")}</p>
</div>
"""

    html += """
</body>
</html>
"""

    os.makedirs("reports", exist_ok=True)

    with open(output_path, "w") as f:
        f.write(html)
