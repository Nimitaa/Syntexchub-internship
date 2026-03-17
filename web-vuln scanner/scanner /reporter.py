import json

def save_report(vulns):
    with open("reports/report.json", "w") as f:
        json.dump(vulns, f, indent=4)
