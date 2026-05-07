# Project Materials

- **Function:** `get_project_materials` (in `src/project_materials/api.py`)
- **HTTP path:** `/project_materials/` (full URL = `${RHUMBIX_BASE_URL}/project_materials/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.project_materials.api import get_project_materials
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| materials | List[str] | One or more material IDs. |
| job_numbers | List[str] | One or more job numbers. |

## Example call

```python
rows = get_project_materials(job_numbers=["190375"])
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
