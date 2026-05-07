# Timekeeping Statuses

- **Function:** `get_timekeeping_statuses` (in `src/timekeeping_statuses/api.py`)
- **HTTP path:** `/timekeeping_statuses/` (full URL = `${RHUMBIX_BASE_URL}/timekeeping_statuses/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.timekeeping_statuses.api import get_timekeeping_statuses
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| is_active | bool | Filter by active status. |

## Example call

```python
rows = get_timekeeping_statuses(is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
