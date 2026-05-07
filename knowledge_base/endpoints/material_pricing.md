# Material Pricing

- **Function:** `get_material_pricing` (in `src/material_pricing/api.py`)
- **HTTP path:** `/material_pricing/` (full URL = `${RHUMBIX_BASE_URL}/material_pricing/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.material_pricing.api import get_material_pricing
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| materials | List[str] | One or more material IDs. |

## Example call

```python
rows = get_material_pricing()
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
