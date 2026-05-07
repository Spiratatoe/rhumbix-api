# Clock In / Clock Out Entries

- **Function:** `get_clock_in_clock_out_entries` (in `src/clock_entries/api.py`)
- **HTTP path:** `/clock_in_clock_out_entries/` (full URL = `${RHUMBIX_BASE_URL}/clock_in_clock_out_entries/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.clock_entries.api import get_clock_in_clock_out_entries
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| worker | List[str] | One or more worker `company_supplied_id`s. |
| start_time | str | Datetime; entries with `entered_time` after this. |
| end_time | str | Datetime; entries with `entered_time` before this. |
| only_edited | bool | If true, return only edited entries. |
| entry_id | List[str] | Filter by a list of entry IDs. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_clock_in_clock_out_entries(
    worker=["GREATCO-EMP-26"],
    start_time="2025-12-15T00:00:00.000000Z",
)
```

## Output shape

Top-level keys (per docstring example, partial):
- `calculated_values`
- `client_created_on`
- `created_by`
- `created_on`
- `current_shift_date`
- `deleted_on`
- `entered_time`
- `entry_id`
- `entry_type`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
