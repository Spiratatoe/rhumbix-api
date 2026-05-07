# Shift Extra Schemas

- **Function:** `get_shift_extra_schemas` (in `src/shift_extra_schemas/api.py`)
- **HTTP path:** `/shift_extra_schemas/` (full URL = `${RHUMBIX_BASE_URL}/shift_extra_schemas/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.shift_extra_schemas.api import get_shift_extra_schemas
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |

## Example call

```python
rows = get_shift_extra_schemas()
```

## Output shape

Top-level keys (from `output/shift_extra_schemas_all_params.json`):
- `id`
- `name`
- `schema` (nested JSON-Schema-like object with `type`, `title`, `properties`, optionally `required`, `description`)

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
