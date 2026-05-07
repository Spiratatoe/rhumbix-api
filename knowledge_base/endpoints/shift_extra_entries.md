# Shift Extra Entries

- **Function:** `get_shift_extra_entries` (in `src/shift_extra_entries/api.py`)
- **HTTP path:** `/shift_extra_entries/` (full URL = `${RHUMBIX_BASE_URL}/shift_extra_entries/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.shift_extra_entries.api import get_shift_extra_entries
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
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| is_active | bool | Filter by active status. |
| work_shift_keys | List[int] | Filter by work shift keys. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_shift_extra_entries(start_date="2019-07-01", end_date="2019-07-31")
```

## Output shape

Top-level keys (from `output/shift_extra_entries_list.json`):
- `work_shift_key`
- `created_on`
- `shift_start_time`
- `shift_end_time`
- `shift_date`
- `employee`
- `entry_name`
- `entry_store`
- `is_approved`
- `status`
- `timezone`
- `id`
- `job_number`
- `deleted_on`
- `last_updated`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
