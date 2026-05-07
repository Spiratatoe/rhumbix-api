# Locked Time Periods

- **Function:** `get_locked_time_periods` (in `src/locked_time_periods/api.py`)
- **HTTP path:** `/locked_time_periods/` (full URL = `${RHUMBIX_BASE_URL}/locked_time_periods/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.locked_time_periods.api import get_locked_time_periods
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |

## Example call

```python
rows = get_locked_time_periods()
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
