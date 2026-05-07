# Employees Projects

- **Function:** `get_employees_projects` (in `src/employees_projects/api.py`)
- **HTTP path:** `/employees_projects/` (full URL = `${RHUMBIX_BASE_URL}/employees_projects/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.employees_projects.api import get_employees_projects
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| employees | List[str] | One or more employee IDs. |
| job_numbers | List[str] | One or more job numbers. |

## Example call

```python
rows = get_employees_projects(employees=["1003"])
```

## Output shape

Top-level keys (from `output/employees_projects_list.json`):
- `company_supplied_id`
- `job_numbers`

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
