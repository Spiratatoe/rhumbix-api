# Users

- **Function:** `get_users` (in `src/users/api.py`)
- **HTTP path:** `/users/` (full URL = `${RHUMBIX_BASE_URL}/users/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.users.api import get_users
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| email | str | Filter by user email address. |

## Example call

```python
rows = get_users(email="solutions@aedo.com")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
