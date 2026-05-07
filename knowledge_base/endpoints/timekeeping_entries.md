# Timekeeping Entries

- **Function:** `get_timekeeping_entries` (in `src/timekeeping_entries/api.py`)
- **HTTP path:** `/timekeeping_entries/` (full URL = `${RHUMBIX_BASE_URL}/timekeeping_entries/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.timekeeping_entries.api import get_timekeeping_entries
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD. |
| is_approved | bool | Filter by approval status. |
| status | str | Filter by status. |
| employee | str | Filter by employee. |
| foreman | str | Filter by foreman. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_timekeeping_entries(start_date="2026-02-01", end_date="2026-02-28")
```

## Output shape

Top-level keys (from `output/timekeeping_entries_date_params.json`):
- `work_shift_key`
- `shift_date`
- `cost_code`
- `cost_code_uuid`
- `job_number`
- `employee`
- `foreman`
- `status`
- `is_approved`
- `over_time_minutes`
- `double_time_minutes`
- `standard_time_minutes`
- `timezone`
- `id`
- `deleted_on`
- `comment`
- `last_updated`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
