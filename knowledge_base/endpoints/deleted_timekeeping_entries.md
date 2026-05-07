# Deleted Timekeeping Entries

- **Function:** `get_deleted_timekeeping_entries` (in `src/deleted_timekeeping_entries/api.py`)
- **HTTP path:** `/deleted_timekeeping_entries/` (full URL = `${RHUMBIX_BASE_URL}/deleted_timekeeping_entries/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.deleted_timekeeping_entries.api import get_deleted_timekeeping_entries
```

## Parameters

All optional. `None` values are stripped. Note: this function does NOT expose a `page_size` parameter.

| Name | Type | Notes |
|---|---|---|
| history_start_date | str | Retrieve history from this date onwards. |
| history_end_date | str | Retrieve history up to this date. |

## Example call

```python
rows = get_deleted_timekeeping_entries(history_start_date="2024-01-01", history_end_date="2024-01-31")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
