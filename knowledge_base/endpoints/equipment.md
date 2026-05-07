# Equipment

- **Function:** `get_equipment` (in `src/equipment/api.py`)
- **HTTP path:** `/equipment/` (full URL = `${RHUMBIX_BASE_URL}/equipment/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.equipment.api import get_equipment
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| name | str | Filter by equipment name. |
| is_active | bool | Filter by active status. |
| equipment_category | List[int] | One or more equipment category IDs. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_equipment(is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
