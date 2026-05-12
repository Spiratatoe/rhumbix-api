"""
Capture one page of real data per Rhumbix endpoint into output/samples/.
Single-page fetch (no full pagination) so this is cheap and won't drown us
in records. We keep >=2 records per endpoint so the anonymizer has enough
variety to learn from (admin/test record is usually #1).
"""
import json
import logging
import os
from datetime import datetime, timedelta

import requests

from src.config import API_KEY, BASE_URL

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

SAMPLES_DIR = os.path.join("output", "samples")
PAGE_SIZE = 10
TIMEOUT = 60

NOW = datetime.utcnow()
ISO_30D = (NOW - timedelta(days=30)).isoformat() + "Z"
ISO_90D = (NOW - timedelta(days=90)).isoformat() + "Z"
ISO_NOW = NOW.isoformat() + "Z"
DATE_30D = (NOW - timedelta(days=30)).strftime("%Y-%m-%d")
DATE_TODAY = NOW.strftime("%Y-%m-%d")

# (path, extra params). Endpoints that need date windows get sensible defaults.
ENDPOINTS = [
    ("/absences/", {}),
    ("/absences/history/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/absence_types/", {}),
    ("/budgets/", {}),
    ("/change_orders/", {}),
    ("/clock_entries/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/clock_in_clock_out_timelines/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/cohorts/", {}),
    ("/companies/", {}),
    ("/company_classifications/", {}),
    ("/company_groups/", {}),
    ("/company_trades/", {}),
    ("/cost_codes/", {}),
    ("/cost_code_controls/", {}),
    ("/cost_items/", {}),
    ("/deleted_timekeeping_entries/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/email_alerts/", {}),
    ("/employees/", {}),
    ("/employees_groups/", {}),
    ("/employees_pricing/", {}),
    ("/employees_projects/", {}),
    ("/employee_shifts_and_breaks/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/employee_shifts_and_breaks/history/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/employee_shift_details/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/equipment/", {}),
    ("/equipment_pricing/", {}),
    ("/field_folders/", {}),
    ("/field_folder_notes/", {}),
    ("/groups/", {}),
    ("/locked_time_periods/", {}),
    ("/materials/", {}),
    ("/material_pricing/", {}),
    ("/notes/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/picklists/", {}),
    ("/picklist_items/", {}),
    ("/projects/", {}),
    ("/project_equipment/", {}),
    ("/project_materials/", {}),
    ("/quantity_entries/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/shift_extra_entries/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/shift_extra_entries/history/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/shift_extra_schemas/", {}),
    ("/start_stop_types/", {}),
    ("/timekeeping_entries/", {"start_date": DATE_30D, "end_date": DATE_TODAY}),
    ("/timekeeping_entries/history/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/timekeeping_statuses/", {}),
    ("/timeoff_requests/", {}),
    ("/users/", {}),
    ("/workflow_entries/", {}),
    ("/workflow_entries/history/", {"history_start_date": ISO_90D, "history_end_date": ISO_NOW}),
    ("/work_shift_details/", {}),
]


def slug(path: str) -> str:
    """`/employee_shifts_and_breaks/history/` -> `employee_shifts_and_breaks_history`."""
    return path.strip("/").replace("/", "_")


def fetch_one_page(path: str, extra: dict):
    url = f"{BASE_URL}{path}"
    headers = {"x-api-key": API_KEY, "Content-Type": "application/json"}
    params = {"page_size": PAGE_SIZE, **extra}
    try:
        r = requests.get(url, headers=headers, params=params, timeout=TIMEOUT)
        if r.status_code >= 400:
            logging.warning("HTTP %s %s -> %s", r.status_code, path, r.text[:200])
            return None
        body = r.json()
        # Rhumbix usually returns {"results": [...], "next": "..."} but some endpoints
        # return a bare list. Normalize.
        if isinstance(body, list):
            return body
        return body.get("results", body)
    except Exception as e:
        logging.error("FAIL %s: %s", path, e)
        return None


def main():
    if not API_KEY or not BASE_URL:
        raise SystemExit("Missing RHUMBIX_API_KEY / RHUMBIX_BASE_URL")
    os.makedirs(SAMPLES_DIR, exist_ok=True)

    summary = {}
    for path, extra in ENDPOINTS:
        name = slug(path)
        logging.info("Capturing %s", path)
        rows = fetch_one_page(path, extra)
        if rows is None:
            summary[name] = "error"
            continue
        out = os.path.join(SAMPLES_DIR, f"{name}.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(rows, f, indent=2)
        summary[name] = f"{len(rows)} rows"

    with open(os.path.join(SAMPLES_DIR, "_capture_summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
    logging.info("Done. Summary: %s", summary)


if __name__ == "__main__":
    main()
