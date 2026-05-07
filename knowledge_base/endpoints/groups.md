# Groups

- **Function:** `get_groups` (in `src/groups/api.py`)
- **HTTP path:** `/groups/` (full URL = `${RHUMBIX_BASE_URL}/groups/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.groups.api import get_groups
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| name | str | Filter by group name. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_groups(name="Field Operations")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
