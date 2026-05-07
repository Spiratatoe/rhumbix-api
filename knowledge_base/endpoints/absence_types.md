# Absence Types

- **Function:** `get_absence_types` (in `src/absence_types/api.py`)
- **HTTP path:** `/absence_types/` (full URL = `${RHUMBIX_BASE_URL}/absence_types/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.absence_types.api import get_absence_types
```

## Parameters

All optional. `None` values are stripped. Note: this function only sets `page_size` if truthy (so `0` would also be skipped).

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |

## Example call

```python
rows = get_absence_types(page_size=100)
```

## Output shape

Top-level keys (from `output/absence_types.json`):
- `name`
- `code`
- `is_active`
- `created_by`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
