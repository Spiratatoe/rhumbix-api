# Cohorts

- **Function:** `get_cohorts` (in `src/cohorts/api.py`)
- **HTTP path:** `/cohorts/` (full URL = `${RHUMBIX_BASE_URL}/cohorts/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.cohorts.api import get_cohorts
```

## Parameters

All optional. `None` values are stripped. Accepts `**kwargs` for custom field filters.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| **kwargs** | str / List[str] | Keys must start with `custom_field_` (e.g. `custom_field_zone_id="12345"` or `["12345","54321"]`). Other kwargs are silently ignored. |

## Example call

```python
rows = get_cohorts(custom_field_zone_id="12345")
```

## Output shape

Top-level keys (per docstring example):
- `id`
- `name`
- `description`
- `is_hidden`
- `employees`
- `employee_permissions`
- `projects`
- `groups`
- `custom_fields`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
