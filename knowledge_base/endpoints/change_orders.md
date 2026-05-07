# Change Orders

- **Function:** `get_change_orders` (in `src/change_orders/api.py`)
- **HTTP path:** `/change_orders/` (full URL = `${RHUMBIX_BASE_URL}/change_orders/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.change_orders.api import get_change_orders
```

## Parameters

All optional. `None` values are stripped. Booleans (e.g. `is_active=False`) are sent.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | str | Filter by job number. |
| is_active | bool | Filter by active status. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ` format. |

## Example call

```python
rows = get_change_orders(job_number="190375", is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
