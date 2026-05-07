# Start Stop Types

- **Function:** `get_start_stop_types` (in `src/start_stop_types/api.py`)
- **HTTP path:** `/start_stop_types/` (full URL = `${RHUMBIX_BASE_URL}/start_stop_types/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.start_stop_types.api import get_start_stop_types
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |

## Example call

```python
rows = get_start_stop_types()
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
