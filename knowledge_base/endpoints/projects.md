# Projects

- **Function:** `get_projects` (in `src/projects/api.py`)
- **HTTP path:** `/projects/` (full URL = `${RHUMBIX_BASE_URL}/projects/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.projects.api import get_projects
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`. Accepts `**kwargs` for custom field filters.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| job_number | List[str] | One or more job numbers. |
| name | str | Filter by project name. |
| is_active | bool | Filter by active status. |
| include_deleted | bool | If true, retrieve deleted records. |
| **kwargs** | str / List[str] | Keys starting with `custom_field_` are forwarded as filters. |

## Example call

```python
rows = get_projects(is_active=True, job_number=["190375"])
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
