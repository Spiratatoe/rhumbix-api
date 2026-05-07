# Cost Items

- **Function:** `get_cost_items` (in `src/cost_items/api.py`)
- **HTTP path:** `/cost_items/` (full URL = `${RHUMBIX_BASE_URL}/cost_items/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.cost_items.api import get_cost_items
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| change_order_key | str | Filter by change order key. |
| is_active | bool | Filter by active status. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |

## Example call

```python
rows = get_cost_items(job_number="190375", is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
