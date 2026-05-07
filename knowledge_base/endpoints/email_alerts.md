# Email Alerts

- **Function:** `get_email_alerts` (in `src/email_alerts/api.py`)
- **HTTP path:** `/email_alerts/` (full URL = `${RHUMBIX_BASE_URL}/email_alerts/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.email_alerts.api import get_email_alerts
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| company_supplied_id | str | Filter by company supplied ID. |

## Example call

```python
rows = get_email_alerts(job_number="190375")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
