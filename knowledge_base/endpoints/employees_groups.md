# Employees Groups

- **Function:** `get_employees_groups` (in `src/employees_groups/api.py`)
- **HTTP path:** `/employees_groups/` (full URL = `${RHUMBIX_BASE_URL}/employees_groups/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.employees_groups.api import get_employees_groups
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| employees | List[str] | One or more employee IDs. |
| groups | List[str] | One or more group IDs. |

## Example call

```python
rows = get_employees_groups(employees=["GREATCO-EMP-26"])
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
