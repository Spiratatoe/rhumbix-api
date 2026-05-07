# Project Equipment

- **Function:** `get_project_equipment` (in `src/project_equipment/api.py`)
- **HTTP path:** `/project_equipment/` (full URL = `${RHUMBIX_BASE_URL}/project_equipment/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.project_equipment.api import get_project_equipment
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| equipment | List[str] | One or more equipment IDs. |
| job_numbers | List[str] | One or more job numbers. |

## Example call

```python
rows = get_project_equipment(job_numbers=["190375"])
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
