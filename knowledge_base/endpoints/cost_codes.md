# Cost Codes

- **Function:** `get_cost_codes` (in `src/cost_codes/api.py`)
- **HTTP path:** `/cost_codes/` (full URL = `${RHUMBIX_BASE_URL}/cost_codes/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.cost_codes.api import get_cost_codes
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`. Accepts `**kwargs` for custom field filters.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| job_number | List[str] | One or more job numbers. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| is_active | bool | Filter by active status. |
| code | str | Filter by cost code. |
| description | str | Filter by description. |
| has_budgets | bool | If true, only cost codes that have budgets. |
| include_deleted | bool | If true, retrieve deleted records. |
| **kwargs** | str / List[str] | Keys starting with `custom_field_` are forwarded as filters. |

## Example call

```python
rows = get_cost_codes(job_number=["190375"], is_active=True)
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
