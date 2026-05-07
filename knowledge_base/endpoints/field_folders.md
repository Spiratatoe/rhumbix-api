# Field Folders

- **Function:** `get_field_folders` (in `src/field_folders/api.py`)
- **HTTP path:** `/field_folders/` (full URL = `${RHUMBIX_BASE_URL}/field_folders/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.field_folders.api import get_field_folders
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| project | List[int] | One or more project IDs. |
| created_on_from | str | Datetime; items created after this. |
| created_on_to | str | Datetime; items created before this. |
| last_updated_from | str | Datetime; items updated after this. |
| last_updated_to | str | Datetime; items updated before this. |

## Example call

```python
rows = get_field_folders(project=[12345])
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
