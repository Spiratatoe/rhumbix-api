# Cost Code Controls

- **Function:** `get_cost_code_controls` (in `src/cost_code_controls/api.py`)
- **HTTP path:** `/cost_code_controls/` (full URL = `${RHUMBIX_BASE_URL}/cost_code_controls/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.cost_code_controls.api import get_cost_code_controls
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| is_active | bool | Filter by active status. |
| labor_type | str | Filter by labor type. |
| cost_code_type | str | Filter by cost code type. |

## Example call

```python
rows = get_cost_code_controls(is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
