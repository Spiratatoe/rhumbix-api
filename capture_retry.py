"""Retry endpoints that failed in capture_samples.py with corrected paths."""
import json
import logging
import os

import requests

from src.config import API_KEY, BASE_URL

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

SAMPLES_DIR = os.path.join("output", "samples")

# (slug_name, path, params)
RETRIES = [
    # clock_entries actually lives at /clock_in_clock_out_entries/
    ("clock_entries", "/clock_in_clock_out_entries/", {"page_size": 10, "start_date": "2025-04-12", "end_date": "2025-05-12"}),
]


def main():
    for name, path, params in RETRIES:
        url = f"{BASE_URL}{path}"
        headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
        try:
            r = requests.get(url, headers=headers, params=params, timeout=60)
            if r.status_code >= 400:
                logging.warning("HTTP %s %s -> %s", r.status_code, path, r.text[:200])
                continue
            body = r.json()
            rows = body if isinstance(body, list) else body.get("results", body)
            out = os.path.join(SAMPLES_DIR, f"{name}.json")
            with open(out, "w", encoding="utf-8") as f:
                json.dump(rows, f, indent=2)
            logging.info("%s -> %d rows", name, len(rows))
        except Exception as e:
            logging.error("FAIL %s: %s", path, e)


if __name__ == "__main__":
    main()
