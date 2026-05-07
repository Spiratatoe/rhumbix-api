# Work Shift Details

- **Function:** `get_work_shift_details` (in `src/work_shift_details/api.py`)
- **HTTP path:** `/work_shift_details/` (full URL = `${RHUMBIX_BASE_URL}/work_shift_details/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.work_shift_details.api import get_work_shift_details
```

## Parameters

All optional. `None` values are stripped before sending.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| start_date | str | YYYY-MM-DD. |
| end_date | str | YYYY-MM-DD. |
| creator | str | Filter by creator. |
| work_shift_keys | List[int] | Filter by work shift keys. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |

## Example call

```python
rows = get_work_shift_details(start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
