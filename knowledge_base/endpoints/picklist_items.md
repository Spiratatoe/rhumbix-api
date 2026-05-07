# Picklist Items

- **Function:** `get_picklist_items` (in `src/picklist_items/api.py`)
- **HTTP path:** `/picklist_items/` (full URL = `${RHUMBIX_BASE_URL}/picklist_items/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.picklist_items.api import get_picklist_items
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| is_active | bool | Filter by active status. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| picklist | str | Filter by picklist. |

## Example call

```python
rows = get_picklist_items(picklist="some_picklist_id")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
