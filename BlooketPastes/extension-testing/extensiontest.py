import json
import requests
import sys

BASE_URL = ""
EXTENSIONS_FILE = "formats_simple.json"
OUTPUT_FILE = "results.json"

with open(EXTENSIONS_FILE, "r") as f:
    extensions = json.load(f)

results = {}

for ext in extensions:
    url = f"{BASE_URL}.{ext}"

    try:
        r = requests.get(url, timeout=10)
        status = str(r.status_code)

    except requests.RequestException:
        status = "request_error"

    if status not in results:
        results[status] = []

    results[status].append(ext)

    print(f"{url} -> {status}")

with open(OUTPUT_FILE, "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved results to", OUTPUT_FILE)