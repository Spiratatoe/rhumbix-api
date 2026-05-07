# Employee Shifts and Breaks

- **Function:** `get_employee_shifts_and_breaks` (in `src/employee_shifts_and_breaks/api.py`)
- **HTTP path:** `/employee_shifts_and_breaks/` (full URL = `${RHUMBIX_BASE_URL}/employee_shifts_and_breaks/`)
- **Returns:** `List[Dict]` — paginated, all pages collected.

## Import

```python
from src.employee_shifts_and_breaks.api import get_employee_shifts_and_breaks
```

## Parameters

All optional. `None` values are stripped. Booleans are sent when not `None`.

| Name | Type | Notes |
|---|---|---|
| page_size | int | Results per page. |
| employee | str | Filter by employee. |
| end_date | str | YYYY-MM-DD. |
| is_approved | bool | Filter by approval status. |
| last_updated | str | Datetime, `YYYY-MM-DDThh:mm:ss.ffffffZ`. |
| start_date | str | YYYY-MM-DD. |
| status | str | Filter by status. |
| work_shift_keys | List[int] | Filter by work shift keys. |
| include_deleted | bool | If true, retrieve deleted records. |

## Example call

```python
rows = get_employee_shifts_and_breaks(start_date="2024-02-01", end_date="2024-02-29")
```

## Output shape

No captured sample. Run once and inspect; common Rhumbix fields include `id`, `created_on`, `last_updated`.

## Failure modes

- Network / non-2xx -> `get_all_paginated_results` logs and returns `[]`.
- Empty list is ambiguous (no records vs. error) — check logs.
- 401/403 -> bad `RHUMBIX_API_KEY`. 400 -> unknown filter or malformed date.
